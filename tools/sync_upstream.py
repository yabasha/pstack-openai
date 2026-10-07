"""Fetch public pinned source data and prepare review artifacts only."""
import argparse
import difflib
import hashlib
import io
import json
from pathlib import Path
import re
import subprocess
import tarfile
import urllib.request

from tools.compare_upstream import compare_sources, index_records, relative_path, safe_path, sha256

BASELINE = 'df581122cde17e6e27686b5a448bde23e4ad4318'
ARCHIVE_SHA256 = '7e76b77c76fca022e17483cdaba0f3efa583043d98ac604d59a20bc22bf5091f'
API = 'https://api.github.com/repos/cursor/plugins'
ARCHIVE = 'https://codeload.github.com/cursor/plugins/tar.gz/'
MAX_DOWNLOAD = 64 * 1024 * 1024
REVISION_SCHEMA = {'type': 'string', 'pattern': '^[0-9a-f]{40}$'}
HASH_SCHEMA = {'type': 'string', 'pattern': '^[0-9a-f]{64}$'}
PATH_SCHEMA = {'type': 'string', 'minLength': 1, 'pattern': r'^(?!/)(?!.*(?:^|/)\.{1,2}(?:/|$))(?!.*\\)[^\r\n]+$'}
REVIEW_KIND = 'pstack-upstream-review'
RESOLUTION_KIND = 'pstack-upstream-resolutions'


def object_schema(properties):
    return {'type': 'object', 'additionalProperties': False,
            'required': list(properties), 'properties': properties}


ENTRY_PROPERTIES = {'path': PATH_SCHEMA, 'destinationPath': PATH_SCHEMA,
    **{name: {'anyOf': [HASH_SCHEMA, {'type': 'null'}]} for name in ('oldSha256', 'newSha256', 'adaptedSha256')},
    'resolution': {'enum': ['required', 'unchanged']},
    'dependencies': {'type': 'array', 'items': {'type': 'string'}},
    'dependentCallers': {'type': 'array', 'items': PATH_SCHEMA}}
ENTRY_SCHEMA = object_schema(ENTRY_PROPERTIES)
FILE_SCHEMA = object_schema({
    **{name: {'type': 'array', 'items': ENTRY_SCHEMA} for name in ('added', 'removed', 'changed', 'unchanged', 'conflicts', 'noticeChanges')},
    'possibleRenames': {'type': 'array', 'items': object_schema({'oldPath': PATH_SCHEMA, 'newPath': PATH_SCHEMA, 'sha256': HASH_SCHEMA})},
    'schemaVersion': {'const': 1}, 'acceptanceReady': {'const': False},
    'skills': object_schema({name: {'type': 'array', 'items': PATH_SCHEMA} for name in ('added', 'removed', 'changed', 'unchanged')})})
REVIEW_SCHEMA = {'$schema': 'https://json-schema.org/draft/2020-12/schema',
    **object_schema({'schemaVersion': {'const': 1}, 'kind': {'const': REVIEW_KIND},
        'command': {'enum': ['check', 'prepare']}, 'baseline': {'const': BASELINE},
        'candidate': REVISION_SCHEMA, 'packageCommit': REVISION_SCHEMA, 'files': FILE_SCHEMA,
        'sourceIdentity': object_schema({'repository': {'const': 'https://github.com/cursor/plugins'},
            'subtree': {'const': 'pstack/'}, 'baselineArchiveSha256': HASH_SCHEMA,
            'candidateArchiveSha256': HASH_SCHEMA, 'candidateTree': REVISION_SCHEMA,
            'lineage': {'enum': ['ahead', 'identical']}, 'manifestSha256': HASH_SCHEMA}),
        'artifactHashes': {'type': 'object', 'additionalProperties': HASH_SCHEMA}})}
RESOLUTION_SCHEMA = {'$schema': 'https://json-schema.org/draft/2020-12/schema',
    **object_schema({'schemaVersion': {'const': 1}, 'kind': {'const': RESOLUTION_KIND},
        'candidate': REVISION_SCHEMA, 'packageCommit': REVISION_SCHEMA,
        'entries': {'type': 'array', 'items': object_schema({**ENTRY_PROPERTIES,
            'disposition': {'enum': ['pending', 'retain-adaptation', 'adapt-manually', 'add-reviewed', 'delete-reviewed', 'rename-reviewed', 'reference-only']},
            'rationale': {'type': 'string'}, 'reviewedCallers': {'type': 'array', 'items': {'type': 'string'}}})}})}


def exact_revision(value):
    if not re.fullmatch('[0-9a-f]{40}', value):
        raise ValueError('Candidate must be an exact lowercase 40-character commit SHA')
    return value


def fetch_public(url):
    if not (url.startswith(API + '/') or url.startswith(ARCHIVE)):
        raise ValueError('Only the canonical public source endpoints are permitted')
    # No credential lookup, Git remote, dependency manager, or source execution.
    request = urllib.request.Request(url, headers={'Accept': 'application/vnd.github+json', 'User-Agent': 'pstack-upstream-review'})
    class NoRedirect(urllib.request.HTTPRedirectHandler):
        def redirect_request(self, req, fp, code, msg, headers, newurl):
            raise ValueError('Unexpected public source redirect')
    with urllib.request.build_opener(NoRedirect).open(request, timeout=30) as response:
        data = response.read(MAX_DOWNLOAD + 1)
    if len(data) > MAX_DOWNLOAD:
        raise ValueError('Public source response exceeds size limit')
    return data


def unpack_archive(data, commit):
    if len(data) > MAX_DOWNLOAD:
        raise ValueError('Archive exceeds size limit')
    prefix = f'plugins-{commit}'
    files, seen, total = {}, set(), 0
    with tarfile.open(fileobj=io.BytesIO(data), mode='r:gz') as archive:
        for member in archive:
            name = member.name.rstrip('/')
            relative_path(name)
            if name in seen or name.split('/')[0] != prefix:
                raise ValueError('Duplicate archive path or unexpected archive identity')
            seen.add(name)
            if not (member.isdir() or member.isfile()):
                raise ValueError('Archive links and special members are forbidden')
            total += member.size
            if total > MAX_DOWNLOAD:
                raise ValueError('Expanded source exceeds size limit')
            if member.isfile() and name.startswith(prefix + '/pstack/'):
                relative = name[len(prefix + '/pstack/'):]
                relative_path(relative)
                files[relative] = archive.extractfile(member).read()
    if not seen:
        raise ValueError('Archive has no repository entries')
    return files


def verify_tree(files, tree):
    if tree.get('truncated') is not False:
        raise ValueError('Incomplete candidate tree')
    expected = {}
    for entry in tree['tree']:
        path = entry['path']
        relative_path(path)
        if not path.startswith('pstack/') or entry['type'] == 'tree':
            continue
        if entry['type'] != 'blob' or entry['mode'] not in ('100644', '100755'):
            raise ValueError('Candidate subtree contains a link or special object')
        relative = path[len('pstack/'):]
        if relative in expected:
            raise ValueError('Duplicate candidate tree entry')
        expected[relative] = entry['sha']
    actual = {path: hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest() for path, data in files.items()}
    if actual != expected:
        raise ValueError('Candidate archive bytes do not match the commit tree')


def load_sources(root, candidate, fetch):
    manifest_path = safe_path(root, f'docs/parity/upstream-manifests/{BASELINE}.json')
    manifest = json.loads(manifest_path.read_text())
    if manifest.get('schemaVersion') != 1 or manifest.get('commit') != BASELINE or manifest.get('repository') != 'https://github.com/cursor/plugins' or manifest.get('subtree') != 'pstack/' or manifest.get('archiveSha256') != ARCHIVE_SHA256:
        raise ValueError('Invalid canonical manifest identity')
    old = manifest['files']
    indexed = index_records(old)
    if len(indexed) != 164 or any(row['upstreamCommit'] != BASELINE for row in old):
        raise ValueError('Canonical manifest must retain all 164 baseline files')
    baseline_archive = fetch(ARCHIVE + BASELINE)
    if sha256(baseline_archive) != ARCHIVE_SHA256:
        raise ValueError('Canonical archive digest mismatch')
    original = unpack_archive(baseline_archive, BASELINE)
    if {path: sha256(data) for path, data in original.items()} != {path: row['upstreamSha256'] for path, row in indexed.items()}:
        raise ValueError('Canonical manifest differs from approved source bytes')
    identity = json.loads(fetch(API + '/commits/' + candidate))
    if identity.get('sha') != candidate:
        raise ValueError('Candidate commit identity mismatch')
    tree_sha = exact_revision(identity['commit']['tree']['sha'])
    lineage = json.loads(fetch(API + '/compare/' + BASELINE + '...' + candidate))
    if lineage.get('merge_base_commit', {}).get('sha') != BASELINE or lineage.get('base_commit', {}).get('sha') != BASELINE or lineage.get('status') not in ('ahead', 'identical'):
        raise ValueError('Candidate is not a verified descendant of the baseline')
    tree = json.loads(fetch(API + '/git/trees/' + tree_sha + '?recursive=1'))
    if tree.get('sha') != tree_sha:
        raise ValueError('Candidate tree identity mismatch')
    candidate_archive = fetch(ARCHIVE + candidate)
    proposed = unpack_archive(candidate_archive, candidate)
    verify_tree(proposed, tree)
    new = [{'upstreamPath': path, 'destinationPath': indexed.get(path, {}).get('destinationPath', path),
            'upstreamCommit': candidate, 'upstreamSha256': sha256(data)} for path, data in sorted(proposed.items())]
    return old, new, original, proposed, {'repository': manifest['repository'], 'subtree': 'pstack/',
        'baselineArchiveSha256': ARCHIVE_SHA256, 'candidateArchiveSha256': sha256(candidate_archive),
        'candidateTree': tree_sha, 'lineage': lineage['status'], 'manifestSha256': sha256(manifest_path.read_bytes())}


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def build_review(root, candidate, command, fetch=fetch_public):
    root = Path(root).absolute()
    exact_revision(candidate)
    if command not in ('check', 'prepare'):
        raise ValueError('Only check and prepare are supported')
    # Check all output ancestors before reading any source or contacting the network.
    review = safe_path(root, '.upstream/reviews/' + candidate)
    if review.exists():
        raise ValueError('Review bundle already exists; retain it or move it aside intentionally')
    old, new, original, proposed, identity = load_sources(root, candidate, fetch)
    # Read the current destination/dependency map, but never use its hashes as source truth.
    inventory = json.loads(safe_path(root, 'docs/parity/inventory.json').read_text())
    current = index_records(inventory)
    if set(current) != {row['upstreamPath'] for row in old}:
        raise ValueError('Working inventory differs from the accepted baseline path set')
    for row in old:
        mapping = current[row['upstreamPath']]
        if mapping['upstreamCommit'] != BASELINE or mapping['upstreamSha256'] != row['upstreamSha256']:
            raise ValueError('Working inventory changed the accepted source pin or hashes')
        row['destinationPath'] = mapping['destinationPath']
        row['dependencies'] = mapping.get('dependencies', [])
    for row in new:
        if row['upstreamPath'] in current:
            row['destinationPath'] = current[row['upstreamPath']]['destinationPath']
    report = compare_sources(old, new, root)
    package_commit = subprocess.run(['git', '-C', str(root), 'rev-parse', 'HEAD'], check=True, capture_output=True, text=True).stdout.strip()
    exact_revision(package_commit)
    artifacts, patches = {}, []
    changed = report['added'] + report['removed'] + report['changed']
    for entry in changed:
        path, destination = entry['path'], entry['destinationPath']
        for label, data in (('original', original.get(path)), ('candidate', proposed.get(path))):
            if data is not None:
                artifacts[f'sources/{label}/{path}'] = data
        target = safe_path(root, destination)
        adapted = target.read_bytes() if target.exists() else None
        if adapted is not None:
            artifacts[f'sources/adapted/{path}'] = adapted
        if entry in report['conflicts']:
            artifacts[f'conflicts/{path}.json'] = json_bytes(entry)
        # Drafts only when the adapted bytes still equal the original source.
        if command == 'prepare' and entry['oldSha256'] is not None and entry['adaptedSha256'] == entry['oldSha256'] and path in proposed:
            artifacts[f'drafts/{destination}'] = proposed[path]
            try:
                patches.extend(difflib.unified_diff(adapted.decode('utf-8').splitlines(True), proposed[path].decode('utf-8').splitlines(True), fromfile='a/' + destination, tofile='b/' + destination))
            except UnicodeDecodeError:
                patches.append(f'Binary draft: {destination}\n')
    resolutions = {'schemaVersion': 1, 'kind': RESOLUTION_KIND, 'candidate': candidate, 'packageCommit': package_commit,
                   'entries': [{**entry, 'disposition': 'pending', 'rationale': '', 'reviewedCallers': []} for entry in changed]}
    artifacts['resolutions.json'] = json_bytes(resolutions)
    artifacts['review-schema.json'] = json_bytes(REVIEW_SCHEMA)
    artifacts['resolution-schema.json'] = json_bytes(RESOLUTION_SCHEMA)
    artifacts['draft.patch'] = ''.join(patches).encode()
    artifacts['notice-differences.json'] = json_bytes(report['noticeChanges'])
    artifacts['original-manifest.json'] = json_bytes(old)
    artifacts['candidate-manifest.json'] = json_bytes(new)
    artifacts['summary.md'] = ('# Upstream review\n\n'
        f'Candidate `{candidate}` compared with `{BASELINE}`. Working package `{package_commit}`.\n\n'
        f"Files added: {len(report['added'])}. Removed: {len(report['removed'])}. Changed: {len(report['changed'])}. Unchanged: {len(report['unchanged'])}.\n\n"
        'Every changed source needs an intentional disposition and caller review. Possible renames are guesses. '
        'Drafts require semantic review. This bundle does not accept a source pin or write package content. '
        'Both host verification statuses remain not-run.\n').encode()
    bundle = {'schemaVersion': 1, 'kind': REVIEW_KIND, 'command': command,
              'baseline': BASELINE, 'candidate': candidate, 'packageCommit': package_commit,
              'files': report, 'sourceIdentity': identity,
              'artifactHashes': {path: sha256(data) for path, data in sorted(artifacts.items())}}
    artifacts['report.json'] = json_bytes(bundle)
    # Validate the complete write set before creating anything; never follow output links.
    for path in artifacts:
        safe_path(review, path)
    review.mkdir(parents=True, exist_ok=False)
    for path, data in sorted(artifacts.items()):
        output = safe_path(review, path)
        output.parent.mkdir(parents=True, exist_ok=True)
        with output.open('xb') as stream:
            stream.write(data)
    return bundle


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('check', 'prepare'))
    parser.add_argument('--candidate', required=True)
    parser.add_argument('--root', type=Path, default=Path.cwd())
    args = parser.parse_args()
    try:
        bundle = build_review(args.root, args.candidate, args.command)
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError, tarfile.TarError) as error:
        parser.exit(2, f'Upstream review failed: {error}\n')
    print(f"Review saved under .upstream/reviews/{bundle['candidate']}/")


if __name__ == '__main__':
    main()
