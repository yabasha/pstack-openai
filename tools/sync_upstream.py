"""Prepare source reviews and stage explicitly approved updates in owned worktrees.

Apply ownership setup belongs to the task coordinator, outside this command.
In the linked worktree absolute Git directory, pstack-update-owner.json contains
exactly schemaVersion=1, owner=<task identifier>, worktree=<absolute real path>,
and packageCommit=<review package commit>. Never register the original checkout.
A marker asserts task ownership; it is not an authorization credential.

Copy version-1 pending resolutions into the version-2 example contract. Bind
reviewSha256 to report.json, select a higher candidateVersion, and provide exact
contentPath and reviewedSha256 for each decision. Content paths are relative to
the retained review bundle. Use null content/hash for deletion. Paired rename
entries must both use rename-reviewed. Review rationale and dependent callers.
Keep all original bundle artifacts unchanged; put manual bytes under resolved/.

Only after explicit user approval of those exact resolutions and owned worktree,
supply their digest with --approve-resolutions-sha256. Never infer approval from
a resolution file. Apply neither executes candidate code nor accepts a release.

For a later update, a separate reviewed acceptance process must record
docs/parity/upstream-manifests/accepted.json using ACCEPTANCE_SCHEMA: schemaVersion
1, kind pstack-accepted-baseline, commit, manifestPath, manifestSha256,
packageCommit, evidencePath and evidenceSha256. The referenced package commit
must contain the exact accepted manifest and be an ancestor of the checkout.
Evidence paths are relative to the checkout. This receipt records an explicit
review assertion, not authenticated human approval. Apply never creates or
advances it. Report version 2 binds this selection and its evidence digests;
the original canonical manifest is always retained and verified.
"""
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
ACCEPTANCE_SCHEMA = object_schema({'schemaVersion': {'const': 1},
    'kind': {'const': 'pstack-accepted-baseline'}, 'commit': REVISION_SCHEMA,
    'manifestPath': PATH_SCHEMA, 'manifestSha256': HASH_SCHEMA,
    'packageCommit': REVISION_SCHEMA, 'evidencePath': PATH_SCHEMA,
    'evidenceSha256': HASH_SCHEMA})
ACCEPTED_SELECTION_SCHEMA = object_schema({'commit': REVISION_SCHEMA,
    'manifestPath': PATH_SCHEMA, 'manifestSha256': HASH_SCHEMA,
    'canonicalManifestSha256': HASH_SCHEMA,
    'receiptSha256': {'anyOf': [HASH_SCHEMA, {'type': 'null'}]},
    'receipt': {'anyOf': [ACCEPTANCE_SCHEMA, {'type': 'null'}]}})


REVIEW_SCHEMA = {'$schema': 'https://json-schema.org/draft/2020-12/schema',
    **object_schema({'schemaVersion': {'const': 2}, 'kind': {'const': REVIEW_KIND},
        'command': {'enum': ['check', 'prepare']}, 'baseline': REVISION_SCHEMA,
        'acceptedBaseline': ACCEPTED_SELECTION_SCHEMA,
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


def accepted_baseline(root):
    """Read a separate acceptance assertion; staging never creates this receipt.

    A receipt is evidence of the caller's recorded review, not authentication or
    human authorization. Its package commit must be an ancestor of this checkout
    and contain the exact accepted manifest. Evidence bytes are hash-bound.
    """
    canonical_path = f'docs/parity/upstream-manifests/{BASELINE}.json'
    canonical_bytes = safe_path(root, canonical_path).read_bytes()
    canonical = json.loads(canonical_bytes)
    if canonical.get('schemaVersion') != 1 or canonical.get('commit') != BASELINE or canonical.get('archiveSha256') != ARCHIVE_SHA256 or canonical.get('repository') != 'https://github.com/cursor/plugins' or canonical.get('subtree') != 'pstack/':
        raise ValueError('Original canonical provenance changed')
    canonical_rows = index_records(canonical['files'])
    if len(canonical_rows) != 164 or any(r['upstreamCommit'] != BASELINE for r in canonical_rows.values()):
        raise ValueError('Original canonical manifest must retain all 164 files')
    selection = dict(commit=BASELINE, manifestPath=canonical_path,
        manifestSha256=sha256(canonical_bytes), canonicalManifestSha256=sha256(canonical_bytes),
        receiptSha256=None, receipt=None)
    manifest = canonical
    receipt_path = safe_path(root, 'docs/parity/upstream-manifests/accepted.json')
    if receipt_path.exists():
        receipt = read_json(receipt_path)
        validate_shape(receipt, ACCEPTANCE_SCHEMA)
        if receipt['manifestPath'] != f"docs/parity/upstream-manifests/{receipt['commit']}.json":
            raise ValueError('Accepted manifest path does not match its commit')
        manifest_bytes = safe_path(root, receipt['manifestPath']).read_bytes()
        if sha256(manifest_bytes) != receipt['manifestSha256']:
            raise ValueError('Accepted manifest digest mismatch')
        evidence = safe_path(root, receipt['evidencePath']).read_bytes()
        if not evidence or sha256(evidence) != receipt['evidenceSha256']:
            raise ValueError('Acceptance evidence digest mismatch')
        subprocess.run(['git', '-C', str(root), 'merge-base', '--is-ancestor', receipt['packageCommit'], 'HEAD'], check=True, capture_output=True)
        recorded = subprocess.run(['git', '-C', str(root), 'show', receipt['packageCommit'] + ':' + receipt['manifestPath']], check=True, capture_output=True).stdout
        if sha256(recorded) != receipt['manifestSha256']:
            raise ValueError('Accepted package commit does not contain the exact manifest')
        manifest = json.loads(manifest_bytes)
        package_inventory = subprocess.run(['git', '-C', str(root), 'show', receipt['packageCommit'] + ':docs/parity/inventory.json'], check=True, capture_output=True).stdout
        committed_rows = index_records(json.loads(package_inventory))
        manifest_rows = index_records(manifest['files'])
        if set(committed_rows) != set(manifest_rows) or any(any(committed_rows[p][field] != row[field] for field in ('upstreamCommit', 'upstreamSha256')) for p, row in manifest_rows.items()):
            raise ValueError('Accepted package inventory differs from its source manifest')
        selection.update(commit=receipt['commit'], manifestPath=receipt['manifestPath'],
            manifestSha256=receipt['manifestSha256'], receiptSha256=sha256(receipt_path.read_bytes()), receipt=receipt)
    if manifest.get('schemaVersion') != 1 or manifest.get('commit') != selection['commit'] or manifest.get('repository') != canonical['repository'] or manifest.get('subtree') != canonical['subtree'] or not re.fullmatch('[0-9a-f]{64}', manifest.get('archiveSha256', '')):
        raise ValueError('Accepted source identity mismatch')
    rows = index_records(manifest['files'])
    if not rows or any(r['upstreamCommit'] != selection['commit'] for r in rows.values()):
        raise ValueError('Accepted source revisions mismatch')
    return manifest, selection


def load_sources(root, candidate, fetch):
    manifest, selection = accepted_baseline(root)
    baseline = selection['commit']
    old = manifest['files']
    indexed = index_records(old)
    baseline_archive = fetch(ARCHIVE + baseline)
    if sha256(baseline_archive) != manifest['archiveSha256']:
        raise ValueError('Accepted archive digest mismatch')
    original = unpack_archive(baseline_archive, baseline)
    if {path: sha256(data) for path, data in original.items()} != {path: row['upstreamSha256'] for path, row in indexed.items()}:
        raise ValueError('Accepted manifest differs from approved source bytes')
    identity = json.loads(fetch(API + '/commits/' + candidate))
    if identity.get('sha') != candidate:
        raise ValueError('Candidate commit identity mismatch')
    tree_sha = exact_revision(identity['commit']['tree']['sha'])
    lineage = json.loads(fetch(API + '/compare/' + baseline + '...' + candidate))
    if lineage.get('merge_base_commit', {}).get('sha') != baseline or lineage.get('base_commit', {}).get('sha') != baseline or lineage.get('status') not in ('ahead', 'identical'):
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
        'baselineArchiveSha256': manifest['archiveSha256'], 'candidateArchiveSha256': sha256(candidate_archive),
        'candidateTree': tree_sha, 'lineage': lineage['status'], 'manifestSha256': selection['manifestSha256']}


def json_bytes(value):
    return (json.dumps(value, indent=2, sort_keys=True) + '\n').encode()


def draft_patch(old, new, destination):
    lines = difflib.unified_diff(old.decode('utf-8').splitlines(True), new.decode('utf-8').splitlines(True), fromfile='a/' + destination, tofile='b/' + destination)
    return ''.join(line if line.endswith('\n') else line + '\n\\ No newline at end of file\n' for line in lines)


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
    accepted, selection = accepted_baseline(root)
    baseline = selection['commit']
    # Read the current destination/dependency map, but never use its hashes as source truth.
    inventory = json.loads(safe_path(root, 'docs/parity/inventory.json').read_text())
    current = index_records(inventory)
    if set(current) != {row['upstreamPath'] for row in old}:
        raise ValueError('Working inventory differs from the accepted baseline path set')
    for row in old:
        mapping = current[row['upstreamPath']]
        if mapping['upstreamCommit'] != baseline or mapping['upstreamSha256'] != row['upstreamSha256']:
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
                patches.append(draft_patch(adapted, proposed[path], destination))
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
        f'Candidate `{candidate}` compared with `{baseline}`. Working package `{package_commit}`.\n\n'
        f"Files added: {len(report['added'])}. Removed: {len(report['removed'])}. Changed: {len(report['changed'])}. Unchanged: {len(report['unchanged'])}.\n\n"
        'Every changed source needs an intentional disposition and caller review. Possible renames are guesses. '
        'Drafts require semantic review. This bundle does not accept a source pin or write package content. '
        'Both host verification statuses remain not-run.\n').encode()
    bundle = {'schemaVersion': 2, 'kind': REVIEW_KIND, 'command': command,
              'baseline': baseline, 'acceptedBaseline': selection, 'candidate': candidate, 'packageCommit': package_commit,
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


# Apply uses a separate strict resolution version. Version 1 is a pending review
# artifact and cannot authorize mutations. Approval is supplied out of band.
APPLY_RESOLUTION_SCHEMA = {'$schema': 'https://json-schema.org/draft/2020-12/schema',
    **object_schema({'schemaVersion': {'const': 2}, 'kind': {'const': RESOLUTION_KIND},
        'candidate': REVISION_SCHEMA, 'packageCommit': REVISION_SCHEMA,
        'reviewSha256': HASH_SCHEMA, 'candidateVersion': {'type': 'string', 'pattern': r'^\d+\.\d+\.\d+$'},
        'entries': {'type': 'array', 'items': object_schema({**ENTRY_PROPERTIES,
            'disposition': {'enum': ['retain-adaptation', 'adapt-manually', 'add-reviewed', 'delete-reviewed', 'rename-reviewed', 'reference-only']},
            'rationale': {'type': 'string', 'minLength': 1},
            'reviewedCallers': {'type': 'array', 'items': PATH_SCHEMA},
            'contentPath': {'anyOf': [PATH_SCHEMA, {'type': 'null'}]},
            'reviewedSha256': {'anyOf': [HASH_SCHEMA, {'type': 'null'}]}})}})}


# Optional for inventory-only development fixtures, mandatory for full packages.
APPLY_RESOLUTION_SCHEMA['properties']['packageMetadata'] = object_schema({'contentPath': PATH_SCHEMA, 'reviewedSha256': HASH_SCHEMA})


def validate_shape(value, schema):
    """Validate the small exported contract vocabulary without dependencies."""
    if 'anyOf' in schema:
        for choice in schema['anyOf']:
            try:
                validate_shape(value, choice)
                return
            except ValueError:
                pass
        raise ValueError('Value does not match any allowed type')
    if 'const' in schema and (value != schema['const'] or type(value) is not type(schema['const'])):
        raise ValueError('Invalid schema identity or constant')
    if 'enum' in schema and value not in schema['enum']:
        raise ValueError('Unrecognized disposition or status')
    kind = schema.get('type')
    types = {'object': dict, 'array': list, 'string': str, 'null': type(None)}
    if kind and type(value) is not types[kind]:
        raise ValueError('Invalid contract value type')
    if kind == 'object':
        properties = schema.get('properties', {})
        if not set(schema.get('required', [])).issubset(value):
            raise ValueError('Missing required contract fields')
        for key, item in value.items():
            rule = properties.get(key, schema.get('additionalProperties', {}))
            if rule is False:
                raise ValueError('Unknown contract field: ' + key)
            validate_shape(item, rule)
    elif kind == 'array':
        for item in value:
            validate_shape(item, schema['items'])
    elif kind == 'string':
        if len(value) < schema.get('minLength', 0) or ('pattern' in schema and not re.fullmatch(schema['pattern'], value)):
            raise ValueError('Invalid contract string')


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError('Duplicate JSON key: ' + key)
            result[key] = value
        return result
    return json.loads(path.read_bytes(), object_pairs_hook=unique)


def git_read(root, *args):
    return subprocess.run(['git', '-C', str(root), *args], check=True, capture_output=True, text=True).stdout.strip()


def verify_owned_worktree(root, owner, package_commit):
    herd = Path.home() / 'Herd'
    if not root.is_absolute() or root != root.resolve() or not root.is_relative_to(herd.resolve()):
        raise ValueError('Apply requires a real owned worktree beneath ~/Herd')
    safe_path(root, 'plugin.json')
    if not (root / '.git').is_file() or (root / '.git').is_symlink():
        raise ValueError('Apply refuses original repositories; use a linked implementation worktree')
    admin = Path(git_read(root, 'rev-parse', '--absolute-git-dir'))
    common = Path(git_read(root, 'rev-parse', '--path-format=absolute', '--git-common-dir'))
    if admin == common or Path(git_read(root, 'rev-parse', '--show-toplevel')) != root:
        raise ValueError('Not an isolated linked worktree')
    marker = read_json(safe_path(admin, 'pstack-update-owner.json'))
    if not owner or marker != dict(schemaVersion=1, owner=owner, worktree=str(root), packageCommit=package_commit):
        raise ValueError('Worktree ownership does not match this task and package base')
    if git_read(root, 'rev-parse', 'HEAD') != package_commit:
        raise ValueError('Stale package commit')
    # Review files may be present. Everything else, including untracked files,
    # must be clean. Ignored files are never eligible for a new destination.
    status = git_read(root, 'status', '--porcelain', '--untracked-files=all', '--', '.', ':(exclude).upstream')
    if status:
        raise ValueError('Implementation worktree must be clean')


def apply_review(review, resolutions, worktree, *, owner, approval, failure_hook=None):
    """Stage a reviewed candidate with recovery. Never accept or release it.

    The caller must obtain explicit user approval for the exact resolution-file
    digest, then pass that digest as approval. A resolution document alone does
    not grant authorization. Ownership is established by the task coordinator
    in the linked worktree Git administration directory before invoking apply.
    """
    from tools.compare_upstream import adapted_path
    root, review, resolution_file = Path(worktree).absolute(), Path(review).absolute(), Path(resolutions).absolute()
    safe_path(review, 'report.json')
    safe_path(resolution_file.parent, resolution_file.name)
    resolution_bytes = resolution_file.read_bytes()
    if not approval or approval != sha256(resolution_bytes):
        raise ValueError('Explicit approval must match the exact reviewed resolution file SHA-256')
    decisions = read_json(resolution_file)
    validate_shape(decisions, APPLY_RESOLUTION_SCHEMA)
    report_bytes = (review / 'report.json').read_bytes()
    if sha256(report_bytes) != decisions['reviewSha256']:
        raise ValueError('Review report hash mismatch')
    report = read_json(review / 'report.json')
    validate_shape(report, REVIEW_SCHEMA)
    candidate, commit = report['candidate'], report['packageCommit']
    if decisions['candidate'] != candidate or decisions['packageCommit'] != commit:
        raise ValueError('Resolution identity differs from the review')
    verify_owned_worktree(root, owner, commit)
    artifacts = {}
    for path, expected in report['artifactHashes'].items():
        data = safe_path(review, path).read_bytes()
        if sha256(data) != expected:
            raise ValueError('Review artifact hash mismatch: ' + path)
        artifacts[path] = data
    for required in ('original-manifest.json', 'candidate-manifest.json', 'review-schema.json', 'resolution-schema.json', 'resolutions.json', 'notice-differences.json', 'draft.patch'):
        if required not in artifacts:
            raise ValueError('Missing review artifact: ' + required)
    if json.loads(artifacts['review-schema.json']) != REVIEW_SCHEMA or json.loads(artifacts['resolution-schema.json']) != RESOLUTION_SCHEMA:
        raise ValueError('Review schema differs from supported version')
    original = json.loads(artifacts['original-manifest.json'])
    proposed = json.loads(artifacts['candidate-manifest.json'])
    old, new = index_records(original), index_records(proposed)
    accepted, selection = accepted_baseline(root)
    baseline = selection['commit']
    identity = report['sourceIdentity']
    if selection != report['acceptedBaseline'] or report['baseline'] != baseline or identity['manifestSha256'] != selection['manifestSha256'] or identity['baselineArchiveSha256'] != accepted['archiveSha256'] or accepted['repository'] != identity['repository'] or accepted['subtree'] != identity['subtree']:
        raise ValueError('Accepted baseline or evidence changed since review')
    accepted_rows = index_records(accepted['files'])
    if set(old) != set(accepted_rows) or any(r['upstreamCommit'] != baseline or r['upstreamSha256'] != accepted_rows[p]['upstreamSha256'] for p, r in old.items()) or any(r['upstreamCommit'] != candidate for r in new.values()):
        raise ValueError('Source manifests disagree with accepted identity')
    inventory = read_json(safe_path(root, 'docs/parity/inventory.json'))
    current = index_records(inventory)
    if set(current) != set(old) or any(any(current[p].get(k) != r.get(k) for k in ('upstreamSha256', 'upstreamCommit', 'destinationPath')) or current[p].get('dependencies', []) != r.get('dependencies', []) for p, r in old.items()):
        raise ValueError('Original inventory mapping changed')
    # Recompute every original working hash and every report classification.
    if compare_sources(original, proposed, root) != report['files']:
        raise ValueError('Stale working hashes or altered comparison report')
    changed = report['files']['added'] + report['files']['removed'] + report['files']['changed']
    entries = decisions['entries']
    if len(entries) != len(changed) or {e['path'] for e in entries} != {e['path'] for e in changed}:
        raise ValueError('Every change needs exactly one intentional resolution')
    entries = {e['path']: e for e in entries}
    writes, affected = {}, set()
    metadata_paths = {'plugin.json', 'UPSTREAM.md', 'NOTICE.md', 'docs/parity/inventory.json', 'docs/parity/baseline-paths.txt'}
    for change in changed:
        path = change['path']
        decision = entries[path]
        if any(decision[k] != change[k] for k in ENTRY_PROPERTIES):
            raise ValueError('Resolution changed a reviewed identity, destination, or original hash')
        if not decision['rationale'].strip() or sorted(decision['reviewedCallers']) != change['dependentCallers']:
            raise ValueError('Resolution requires rationale and exact dependent caller review')
        destination = change['destinationPath']
        target = adapted_path(root, destination)
        action = decision['disposition']
        generated = destination in metadata_paths or destination.startswith('docs/parity/')
        if generated and action != 'retain-adaptation':
            raise ValueError('Generated metadata must retain its adaptation: ' + destination)
        old_hash, new_hash = change['oldSha256'], change['newSha256']
        if action == 'delete-reviewed' and new_hash is not None or action == 'add-reviewed' and old_hash is not None:
            raise ValueError('Disposition is incompatible with source change')
        if action == 'rename-reviewed' and not any(path in (r['oldPath'], r['newPath']) and all(entries.get(p, {}).get('disposition') == action for p in (r['oldPath'], r['newPath'])) for r in report['files']['possibleRenames']):
            raise ValueError('Rename needs an explicit paired exact-content source resolution')
        deleting = new_hash is None and action in ('delete-reviewed', 'rename-reviewed')
        if new_hash is None and not deleting and action != 'retain-adaptation':
            raise ValueError('Removed source needs deletion, paired rename, or explicit retention')
        for label, expected in (('original', old_hash), ('candidate', new_hash), ('adapted', change['adaptedSha256'])):
            if expected is not None and sha256(artifacts.get(f'sources/{label}/{path}', b'')) != expected:
                raise ValueError('Source artifact bytes differ from manifest: ' + path)
        if deleting:
            if decision['contentPath'] is not None or decision['reviewedSha256'] is not None:
                raise ValueError('Deletion must explicitly review absence')
            data = None
        else:
            content_path = decision['contentPath']
            if not content_path:
                raise ValueError('Reviewed content path is required')
            data = safe_path(review, content_path).read_bytes()
            if sha256(data) != decision['reviewedSha256']:
                raise ValueError('Reviewed content hash mismatch')
            if not (content_path.startswith(('drafts/', 'sources/candidate/', 'sources/adapted/', 'resolved/'))):
                raise ValueError('Only exact reviewed source, draft, or resolved bytes may be applied')
            if content_path in artifacts and sha256(data) != report['artifactHashes'][content_path]:
                raise ValueError('Draft/source artifact changed')
            if action == 'retain-adaptation' and sha256(data) != change['adaptedSha256']:
                raise ValueError('Retention must preserve existing adapted bytes')
            if old_hash is None and action not in ('add-reviewed', 'rename-reviewed', 'reference-only', 'retain-adaptation'):
                raise ValueError('New source needs an explicit addition disposition')
        if old_hash is None and target.exists():
            raise ValueError('New source cannot overwrite a destination-only file')
        if not generated:
            writes[destination] = data
        affected.update([path, *change['dependentCallers']])
    # Invalidate transitively dependent callers as well as changed source files.
    while True:
        extra = {p for p, r in current.items() if any(dep in affected or any(dep == current[a]['destinationPath'] for a in affected if a in current) for dep in r.get('dependencies', []))}
        if extra.issubset(affected):
            break
        affected.update(extra)
    result_inventory = []
    for path, source in new.items():
        row = dict(current.get(path, source))
        row.update(upstreamCommit=candidate, upstreamSha256=source['upstreamSha256'])
        if path in entries:
            decision = entries[path]
            row.update(destinationPath=decision['destinationPath'], rationale=decision['rationale'],
                disposition='reference-only' if decision['disposition'] == 'reference-only' else row.get('disposition', 'runtime'),
                adaptationStatus='reference-only-reviewed' if decision['disposition'] == 'reference-only' else 'adapted-reviewed')
            row.setdefault('dependencies', decision['dependencies'])
            row.setdefault('licenseProvenance', {'license': 'MIT', 'copyright': 'Copyright (c) 2026 Lauren Tan', 'sourcePath': 'LICENSE'})
        # Every pin/version change requires fresh host evidence, including callers.
        row['verification'] = {host: {'status': 'not-run', 'evidence': []} for host in ('chatgpt', 'codex')}
        result_inventory.append(row)
    validate_shape(result_inventory, read_json(safe_path(root, 'docs/parity/inventory.schema.json')))
    plugin = read_json(safe_path(root, 'plugin.json'))
    version = decisions['candidateVersion']
    if not re.fullmatch(r'\d+\.\d+\.\d+', plugin['version']) or tuple(map(int, version.split('.'))) <= tuple(map(int, plugin['version'].split('.'))):
        raise ValueError('Candidate version must increase')
    plugin['version'] = version
    manifest_path = f'docs/parity/upstream-manifests/{candidate}.json'
    if candidate == baseline or safe_path(root, manifest_path).exists():
        raise ValueError('Candidate manifest must be new; old manifests are retained')
    writes[manifest_path] = json_bytes(dict(schemaVersion=1, repository=identity['repository'], subtree=identity['subtree'], commit=candidate, archiveSha256=identity['candidateArchiveSha256'], files=proposed))
    writes['plugin.json'] = json_bytes(plugin)
    writes['docs/parity/baseline-paths.txt'] = ('\n'.join(sorted(new)) + '\n').encode()
    writes['UPSTREAM.md'] = safe_path(root, 'UPSTREAM.md').read_bytes() + (f'\n## Unaccepted candidate {candidate}\n\nCandidate version {version}. Archive SHA-256 {identity["candidateArchiveSha256"]}. Review SHA-256 {decisions["reviewSha256"]}.\nThe inventory stages this candidate. The accepted baseline above remains historical evidence. Structural checks, helper regression tests, and affected host cases must run before separate acceptance.\n').encode()
    notice = safe_path(root, 'NOTICE.md').read_bytes()
    for change in report['files']['noticeChanges']:
        for label in ('original', 'candidate'):
            data = artifacts.get(f'sources/{label}/{change["path"]}')
            if data is not None:
                notice += f'\n## Reviewed {label} notice: {change["path"]}\n\n'.encode() + data + b'\n'
    writes['NOTICE.md'] = notice
    state_path = f'docs/parity/upstream-manifests/{candidate}.apply.json'
    if safe_path(root, state_path).exists():
        raise ValueError('Existing apply evidence must be retained')
    state = dict(schemaVersion=1, candidate=candidate, packageCommit=commit, acceptanceReady=False, releasable=False,
        reviewSha256=decisions['reviewSha256'], resolutionsSha256=approval, invalidatedSources=sorted(affected),
        checks={'structural': 'not-run', 'helperRegression': 'not-run', 'affectedHostCases': {'chatgpt': 'not-run', 'codex': 'not-run'}}, resolutions=decisions)
    writes[state_path] = json_bytes(state)
    from tools.update_metadata import closure_writes
    result_inventory = closure_writes(root, review, decisions, result_inventory, writes)
    # Inventory is last so fault injection proves all metadata and pin recovery.
    writes.pop('docs/parity/inventory.json', None)
    writes['docs/parity/inventory.json'] = json_bytes(result_inventory)
    backup, modes, created_dirs = {}, {}, []
    for path in writes:
        target = adapted_path(root, path)
        if target.exists() and not target.is_file():
            raise ValueError('Write target is not a regular file')
        if target.exists() and target.stat().st_nlink != 1:
            raise ValueError('Multiply linked write targets are forbidden')
        backup[path] = target.read_bytes() if target.exists() else None
        modes[path] = target.stat().st_mode if target.exists() else None
    try:
        for path, data in writes.items():
            if path == 'docs/parity/inventory.json' and failure_hook:
                failure_hook('before-inventory')
            target = adapted_path(root, path)
            missing = []
            parent = target.parent
            while not parent.exists():
                missing.append(parent)
                parent = parent.parent
            for directory in reversed(missing):
                directory.mkdir()
                created_dirs.append(directory)
            if data is None:
                if target.exists():
                    target.unlink()
            else:
                target.write_bytes(data)
    except BaseException:
        for path, data in backup.items():
            target = adapted_path(root, path)
            if data is None:
                if target.exists():
                    target.unlink()
            else:
                target.write_bytes(data)
                target.chmod(modes[path])
        for directory in reversed(created_dirs):
            directory.rmdir()
        raise
    return state


# Ownership is exhaustive over both immutable trees. No directory prefix grants
# ownership; excluded paths need an explicit preservation reason in this review.
ROLLBACK_OWNERSHIP_SCHEMA = object_schema({'schemaVersion': {'const': 1},
    'kind': {'const': 'pstack-rollback-ownership'}, 'release': REVISION_SCHEMA,
    'packageCommit': REVISION_SCHEMA, 'runtimeState': {'const': 'no-runtime-state-migrations'},
    'ownedPaths': {'type': 'array', 'items': PATH_SCHEMA},
    'preservedPaths': {'type': 'object', 'additionalProperties': {'type': 'string', 'minLength': 1}}})


def committed_tree(root, commit):
    """Read immutable bytes and modes without checkout, filters, or execution."""
    exact_revision(commit)
    if git_read(root, 'rev-parse', commit + '^{commit}') != commit:
        raise ValueError('Rollback requires an exact package commit')
    entries = subprocess.run(['git', '-C', str(root), 'ls-tree', '-rz', commit],
        check=True, capture_output=True).stdout
    result = {}
    for entry in entries.split(b'\0'):
        if not entry:
            continue
        metadata, path = entry.split(b'\t', 1)
        mode, kind, oid = metadata.decode().split()
        path = path.decode('utf-8')
        relative_path(path)
        # Even preserved paths cannot hide submodules, links or special objects.
        if kind != 'blob' or mode not in ('100644', '100755'):
            raise ValueError('Rollback tree contains unsupported object: ' + path)
        data = subprocess.run(['git', '-C', str(root), 'cat-file', 'blob', oid],
            check=True, capture_output=True).stdout
        result[path] = (data, int(mode, 8) & 0o777)
    return result


def package_digest(files):
    return sha256(json_bytes({p: {'sha256': sha256(d), 'mode': m} for p, (d, m) in sorted(files.items())}))


POST_FREEZE_REPORTS = frozenset({"docs/testing/codex.md", "docs/testing/chatgpt.md",
    "docs/testing/release-checklist.md"})
TESTED_PACKAGE_PATH = 'docs/parity/tested-package.json'
TESTED_PACKAGE_SCHEMA = object_schema({'schemaVersion': {'const': 1},
    'kind': {'const': 'pstack-tested-package'}, 'testedCommit': REVISION_SCHEMA,
    'reportPaths': {'type': 'array', 'items': PATH_SCHEMA}})


def rollback_tested_commit(root, release, files, inventory):
    """Prove a frozen tested tree still supplies the release's operative bytes.

    A later immutable release may add named evidence/reports and change inventory
    verification. Everything else in both Git trees must remain byte/mode equal.
    The provenance record is itself committed in the release, never caller input.
    """
    if TESTED_PACKAGE_PATH not in files:
        raise ValueError('Passing rollback evidence requires immutable tested-package provenance')
    provenance = json.loads(files[TESTED_PACKAGE_PATH][0])
    validate_shape(provenance, TESTED_PACKAGE_SCHEMA)
    tested = provenance['testedCommit']
    subprocess.run(['git', '-C', str(root), 'merge-base', '--is-ancestor', tested, release], check=True, capture_output=True)
    frozen, released = committed_tree(root, tested), committed_tree(root, release)
    if released.get(TESTED_PACKAGE_PATH) != files[TESTED_PACKAGE_PATH]:
        raise ValueError('Tested provenance differs from immutable release')
    reports = provenance['reportPaths']
    if len(reports) != len(set(reports)) or not set(reports).issubset(set(frozen) | set(released)):
        raise ValueError('Report provenance has duplicate or missing paths')
    rows = index_records(inventory)
    operative = {r['destinationPath'] for r in rows.values()}
    operative.update(rows.get(dep, {}).get('destinationPath', dep) for r in rows.values() for dep in r.get('dependencies', []))
    for path in reports:
        relative_path(path)
        receipt_metadata = path == "docs/parity/upstream-manifests/accepted.json" and path in files
        if not (receipt_metadata or path in POST_FREEZE_REPORTS or path.startswith(('docs/parity/evidence/', 'docs/releases/'))) or Path(path).suffix not in ('.json', '.md', '.txt') or any(path == p or path.startswith(p.rstrip('/') + '/') for p in operative):
            raise ValueError('Report provenance cannot exempt operative content: ' + path)
    inventory_path = 'docs/parity/inventory.json'
    frozen_inventory = json.loads(frozen[inventory_path][0])
    def identity(records):
        return {p: {k:v for k,v in row.items() if k != 'verification'} for p,row in index_records(records).items()}
    # Source pin, source hashes, mappings, dependencies and dispositions all stay
    # fixed; only host observations may advance after the operative freeze.
    if identity(frozen_inventory) != identity(inventory):
        raise ValueError('Operative package differs in inventory identity')
    exemptions = set(reports) | {TESTED_PACKAGE_PATH, inventory_path}
    for path in (set(frozen) | set(released)) - exemptions:
        if frozen.get(path) != released.get(path):
            raise ValueError('Operative package differs from tested commit: ' + path)
    if frozen[inventory_path][1] != released[inventory_path][1]:
        raise ValueError('Operative package differs in inventory mode')
    version = json.loads(released['plugin.json'][0])['version']
    return tested, version


def validate_rollback_snapshot(root, release, files):
    """Validate the immutable package, inventory and provenance before replacement."""
    import tempfile
    from tools.validate_package import validate_package, schema_errors
    inventory = json.loads(files['docs/parity/inventory.json'][0])
    contract_root = Path(__file__).resolve().parents[1]
    for path in ('docs/parity/inventory.schema.json', 'docs/parity/cases/schema.json'):
        if json.loads(files[path][0]) != read_json(contract_root / path):
            raise ValueError('Unknown rollback schema version: ' + path)
    errors = schema_errors(inventory, read_json(contract_root / 'docs/parity/inventory.schema.json'), 'inventory')
    if errors:
        raise ValueError('Invalid release inventory: ' + '; '.join(errors))
    rows = index_records(inventory)
    if not rows:
        raise ValueError('Release inventory is empty')
    if "docs/parity/baseline-paths.txt" in files and files["docs/parity/baseline-paths.txt"][0].decode().splitlines() != sorted(rows):
        raise ValueError("Release baseline path list differs from inventory")
    source_commit = next(iter(rows.values()))['upstreamCommit']
    manifest_path = f'docs/parity/upstream-manifests/{source_commit}.json'
    manifest = json.loads(files[manifest_path][0])
    sources = index_records(manifest['files'])
    if manifest.get('schemaVersion') != 1 or manifest.get('commit') != source_commit or manifest.get('repository') != 'https://github.com/cursor/plugins' or manifest.get('subtree') != 'pstack/' or not re.fullmatch('[0-9a-f]{64}', manifest.get('archiveSha256', '')):
        raise ValueError('Release manifest has incompatible provenance')
    if set(rows) != set(sources) or any(any(rows[p][k] != sources[p][k] for k in ('upstreamCommit', 'upstreamSha256')) for p in rows):
        raise ValueError('Release package inventory and source manifest differ')
    receipt_path = 'docs/parity/upstream-manifests/accepted.json'
    if receipt_path in files:
        receipt = json.loads(files[receipt_path][0])
        validate_shape(receipt, ACCEPTANCE_SCHEMA)
        if not files[receipt["evidencePath"]][0]:
            raise ValueError("Release acceptance evidence must be nonempty")
        if receipt['commit'] != source_commit or receipt['manifestPath'] != manifest_path or receipt['manifestSha256'] != sha256(files[manifest_path][0]) or receipt['evidenceSha256'] != sha256(files[receipt['evidencePath']][0]):
            raise ValueError('Release acceptance receipt differs from package snapshot')
        subprocess.run(['git', '-C', str(root), 'merge-base', '--is-ancestor', receipt['packageCommit'], release], check=True, capture_output=True)
        accepted = committed_tree(root, receipt['packageCommit'])
        accepted_rows = index_records(json.loads(accepted["docs/parity/inventory.json"][0]))
        if set(accepted_rows) != set(sources) or any(any(accepted_rows[p][k] != sources[p][k] for k in ("upstreamCommit", "upstreamSha256")) for p in sources):
            raise ValueError("Release acceptance inventory lacks immutable provenance")
        if accepted[manifest_path][0] != files[manifest_path][0]:
            raise ValueError('Release acceptance manifest lacks immutable provenance')
    elif source_commit != BASELINE:
        raise ValueError('Rollback target is an unaccepted candidate')
    # These temporary files are inert validation data, never executed.
    with tempfile.TemporaryDirectory(prefix='pstack-rollback-validate-', dir=Path.home() / 'Herd') as directory:
        snapshot = Path(directory)
        for path, (data, mode) in files.items():
            target = safe_path(snapshot, path)
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
        # Validate original provenance even when a later receipt is present.
        canonical = json.loads(files[f"docs/parity/upstream-manifests/{BASELINE}.json"][0])
        canonical_rows = index_records(canonical["files"])
        if canonical.get("schemaVersion") != 1 or canonical.get("commit") != BASELINE or canonical.get("archiveSha256") != ARCHIVE_SHA256 or canonical.get("repository") != "https://github.com/cursor/plugins" or canonical.get("subtree") != "pstack/" or len(canonical_rows) != 164 or any(r["upstreamCommit"] != BASELINE for r in canonical_rows.values()):
            raise ValueError("Original rollback provenance changed")
        errors = validate_package(snapshot, inventory)
        if errors:
            raise ValueError('Release structural validation failed: ' + '; '.join(errors))
        from tools.validate_evidence import validate_evidence
        tested_identity = None
        for row in inventory:
            for host, verification in row["verification"].items():
                if verification["status"] not in ("pass", "reduced-pass"):
                    continue
                if not verification["evidence"]:
                    raise ValueError("Passing rollback inventory requires host evidence")
                if tested_identity is None:
                    tested_identity = rollback_tested_commit(root, release, files, inventory)
                tested_commit, tested_version = tested_identity
                for path in verification["evidence"]:
                    records = read_json(safe_path(snapshot, path))
                    records = records if isinstance(records, list) else [records]
                    matching = [r for r in records if isinstance(r, dict) and r.get("host") == host and row["upstreamPath"] in r.get("sourcePaths", []) and r.get("status") == verification["status"]]
                    if not matching or any(r.get("packageVersion") != tested_version or validate_evidence(r, tested_commit, snapshot) for r in matching):
                        raise ValueError("Invalid rollback host evidence: " + path)


def rollback_plan(worktree, ownership, *, owner):
    """Read-only preview. Its digest is the distinct human-approval boundary."""
    from tools.compare_upstream import adapted_path
    validate_shape(ownership, ROLLBACK_OWNERSHIP_SCHEMA)
    root = Path(worktree).absolute()
    current, release = ownership['packageCommit'], ownership['release']
    verify_owned_worktree(root, owner, current)
    subprocess.run(['git', '-C', str(root), 'merge-base', '--is-ancestor', release, current], check=True, capture_output=True)
    before, after = committed_tree(root, current), committed_tree(root, release)
    owned = ownership['ownedPaths']
    preserved = ownership['preservedPaths']
    if not owned or owned != sorted(set(owned)) or set(owned) & set(preserved) or set(owned) | set(preserved) != set(before) | set(after) or any(not reason.strip() for reason in preserved.values()):
        raise ValueError('Ownership must exhaustively classify both trees without duplicates or overlaps')
    # Inventory, dependency paths and update metadata cannot be labelled personal.
    required = {'plugin.json', 'UPSTREAM.md', 'NOTICE.md', 'docs/parity/inventory.json',
        'docs/parity/inventory.schema.json', 'docs/parity/cases/schema.json'}
    for tree in (before, after):
        inventory = json.loads(tree['docs/parity/inventory.json'][0])
        rows = index_records(inventory)
        required.update(r['destinationPath'] for r in rows.values())
        for row in rows.values():
            for dependency in row.get('dependencies', []):
                destination = rows.get(dependency, {}).get('destinationPath', dependency)
                matches = {p for p in tree if p == destination or p.startswith(destination.rstrip('/') + '/')}
                if not matches:
                    raise ValueError('Missing declared package dependency: ' + destination)
                required.update(matches)
        if TESTED_PACKAGE_PATH in tree:
            required.add(TESTED_PACKAGE_PATH)
        if "docs/parity/baseline-paths.txt" in tree:
            required.add("docs/parity/baseline-paths.txt")
        required.update(p for p in tree if p.startswith('docs/parity/upstream-manifests/'))
        if 'docs/parity/upstream-manifests/accepted.json' in tree:
            receipt = json.loads(tree['docs/parity/upstream-manifests/accepted.json'][0])
            required.add(receipt['evidencePath'])
    if not required.issubset(owned):
        raise ValueError('Ownership omits required package or inventory paths')
    changes = []
    for path in owned:
        target = adapted_path(root, path)
        if target.exists() and (not target.is_file() or target.stat().st_nlink != 1):
            raise ValueError('Rollback target must be an unshared regular file: ' + path)
        observed = (target.read_bytes(), target.stat().st_mode & 0o777) if target.exists() else None
        if observed != before.get(path):
            raise ValueError('Working bytes or modes differ from current commit: ' + path)
        changes.append({'path': path,
            'before': {'sha256': sha256(before[path][0]), 'mode': before[path][1]} if path in before else None,
            'after': {'sha256': sha256(after[path][0]), 'mode': after[path][1]} if path in after else None})
    old_package = {p: before[p] for p in owned if p in before}
    release_package = {p: after[p] for p in owned if p in after}
    validate_rollback_snapshot(root, release, release_package)
    return dict(schemaVersion=1, kind='pstack-rollback-plan', packageCommit=current, release=release,
        worktree=str(root), owner=owner, ownershipSha256=sha256(json_bytes(ownership)),
        runtimeState=ownership['runtimeState'], currentPackageSha256=package_digest(old_package),
        releasePackageSha256=package_digest(release_package), changes=changes,
        preservedPaths=preserved, acceptanceReady=False, releasable=False)


def rollback_release(release, worktree, *, ownership, owner, approval, failure_hook=None):
    """Restore an approved immutable package snapshot; never reset Git or runtime state."""
    from tools.compare_upstream import adapted_path
    if release != ownership.get('release'):
        raise ValueError('Requested release differs from reviewed ownership')
    root = Path(worktree).absolute()
    plan = rollback_plan(root, ownership, owner=owner)
    if not approval or approval != sha256(json_bytes(plan)):
        raise ValueError('Explicit approval must match the exact rollback plan SHA-256')
    snapshot = committed_tree(root, release)
    paths = ownership['ownedPaths']
    backup = {p: ((root / p).read_bytes(), (root / p).stat().st_mode & 0o777) if (root / p).exists() else None for p in paths}
    created_dirs = []
    try:
        # Inventory is last. Exceptions, including KeyboardInterrupt, restore all
        # bytes and modes. This is not crash-safe storage or an atomic tree swap.
        for path in [p for p in paths if p != 'docs/parity/inventory.json'] + ['docs/parity/inventory.json']:
            if path == 'docs/parity/inventory.json' and failure_hook:
                failure_hook('before-inventory')
            target = adapted_path(root, path)
            if path not in snapshot:
                if target.exists():
                    target.unlink()
                continue
            missing, parent = [], target.parent
            while not parent.exists():
                missing.append(parent)
                parent = parent.parent
            for directory in reversed(missing):
                directory.mkdir()
                created_dirs.append(directory)
            data, mode = snapshot[path]
            target.write_bytes(data)
            target.chmod(mode)
        actual = {p: ((root / p).read_bytes(), (root / p).stat().st_mode & 0o777) for p in paths if (root / p).exists()}
        actual_hash = package_digest(actual)
        if actual_hash != plan['releasePackageSha256']:
            raise ValueError('Restored package digest mismatch')
    except BaseException:
        for path, value in backup.items():
            target = adapted_path(root, path)
            if value is None:
                if target.exists():
                    target.unlink()
            else:
                target.write_bytes(value[0])
                target.chmod(value[1])
        for directory in reversed(created_dirs):
            directory.rmdir()
        raise
    return {**plan, 'actualPackageSha256': actual_hash, 'approvalSha256': approval}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("check", "prepare", "apply", "rollback"))
    parser.add_argument("--candidate")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    parser.add_argument("--review", type=Path)
    parser.add_argument("--resolutions", type=Path)
    parser.add_argument("--worktree", type=Path)
    parser.add_argument("--owner", help="Task owner from the linked worktree Git-admin ownership marker")
    parser.add_argument("--approve-resolutions-sha256", help="Supply only after explicit user approval of this exact resolution digest and worktree")
    parser.add_argument("--release", help="Exact previous package commit")
    parser.add_argument("--ownership", type=Path, help="Reviewed exhaustive rollback ownership JSON")
    parser.add_argument("--approve-plan-sha256", help="Explicit approval of preview plan digest; omit for read-only preview")
    args = parser.parse_args()
    try:
        if args.command == "rollback":
            if not all((args.release, args.worktree, args.owner, args.ownership)):
                raise ValueError("Rollback requires --release, --worktree, --owner and --ownership")
            ownership = read_json(safe_path(args.ownership.absolute().parent, args.ownership.name))
            if args.release != ownership.get("release"):
                raise ValueError("Release differs from ownership document")
            plan = rollback_plan(args.worktree, ownership, owner=args.owner)
            if args.approve_plan_sha256:
                plan = rollback_release(args.release, args.worktree, ownership=ownership, owner=args.owner, approval=args.approve_plan_sha256)
            print(json.dumps({"plan": plan, "planSha256": sha256(json_bytes(plan))}, indent=2))
        elif args.command == "apply":
            if not all((args.review, args.resolutions, args.worktree, args.owner, args.approve_resolutions_sha256)):
                raise ValueError("Apply requires --review, --resolutions, --worktree, --owner and --approve-resolutions-sha256")
            apply_review(args.review, args.resolutions, args.worktree, owner=args.owner, approval=args.approve_resolutions_sha256)
            print("Candidate staged. Acceptance and release remain blocked pending structural, helper and host checks.")
        else:
            if not args.candidate:
                raise ValueError("Check and prepare require --candidate")
            bundle = build_review(args.root, args.candidate, args.command)
            print(f"Review saved under .upstream/reviews/{bundle["candidate"]}/")
    except (ValueError, OSError, KeyError, TypeError, subprocess.CalledProcessError, tarfile.TarError) as error:
        parser.exit(2, f"Upstream update failed: {error}\n")


if __name__ == "__main__":
    main()
