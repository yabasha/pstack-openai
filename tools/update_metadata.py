"""Preflight reviewed full-package metadata into the existing apply transaction."""
import json
from pathlib import Path
import re
import shutil
import tempfile
from tools.compare_upstream import safe_path, sha256
from tools.baseline_policy import validate_policy


def closure_writes(root, review, decisions, inventory, writes):
    """Bind exact reviewed metadata; validate a projection without executing it."""
    from tools.sync_upstream import read_json, read_json_bytes, json_bytes, git_read
    from tools.validate_package import validate_package, schema_errors
    from tools.release_report import registry_checks
    from tools.build_catalog import build_catalog
    fragments = sorted((root/'docs/parity/adaptations').glob('*.json'))
    full = bool(fragments) or (root/'docs/parity/case-registry.json').exists() or (root/'docs/catalog/skills').exists()
    if not full:
        if decisions.get('packageMetadata'):
            raise ValueError('metadata closure requires a full package')
        return inventory
    reference = decisions.get('packageMetadata')
    if not reference:
        raise ValueError('Full-package metadata closure is required before mutation')
    content = safe_path(review,reference['contentPath']).read_bytes()
    if not reference['contentPath'].startswith('resolved/') or sha256(content) != reference['reviewedSha256']:
        raise ValueError('Reviewed metadata closure digest or path mismatch')
    bundle = read_json_bytes(content)
    if set(bundle) != {'schemaVersion','kind','inventory','fragmentOwners','files'} or bundle['schemaVersion'] != 1 or bundle['kind'] != 'pstack-package-metadata':
        raise ValueError('Invalid metadata closure contract')
    proposed = bundle['inventory']
    errors = schema_errors(proposed,read_json(root/'docs/parity/inventory.schema.json'),'metadata inventory')
    expected = {r['upstreamPath']:r for r in inventory}
    if errors or len(proposed) != len(expected) or {r['upstreamPath'] for r in proposed} != set(expected):
        raise ValueError('Metadata closure inventory membership mismatch')
    for row in proposed:
        source = expected[row['upstreamPath']]
        for key in ('upstreamCommit','upstreamSha256','destinationPath','verification'):
            if row[key] != source[key]: raise ValueError('Metadata closure changed source identity or synthesized evidence: '+key)
        if row['adaptationStatus'] == 'pending':
            raise ValueError('Metadata closure cannot retain pending dispositions')
        if len(row['dependencies']) != len(set(row['dependencies'])):
            raise ValueError('Metadata closure duplicates dependencies')
    by_source = {r['upstreamPath']:r for r in proposed}
    owners = bundle['fragmentOwners']
    if not isinstance(owners,dict) or set(owners) != set(by_source) or any(not re.fullmatch(r'docs/parity/adaptations/[a-zA-Z0-9_-]+\.json',p) for p in owners.values()):
        raise ValueError('Metadata closure needs one explicit active fragment owner for every source')
    previous = {}
    seen = set()
    current = read_json(root/'docs/parity/inventory.json')
    current_by_source = {r['upstreamPath']:r for r in current}
    for fragment in fragments:
        path = fragment.relative_to(root).as_posix()
        rows = read_json(safe_path(root,path))
        previous[path] = rows
        for row in rows:
            source = row['upstreamPath']
            if source in seen or source not in current_by_source or any(v != current_by_source[source].get(k) for k,v in row.items() if k != 'verification'):
                raise ValueError('Conflicting existing active fragment ownership')
            seen.add(source)
    if seen != set(current_by_source): raise ValueError('Incomplete existing active fragment ownership')
    history = f"docs/parity/upstream-manifests/{decisions['candidate']}.previous-fragments.json"
    if safe_path(root,history).exists(): raise ValueError('Prior fragment provenance already exists')
    writes[history] = json_bytes(dict(schemaVersion=1,packageCommit=decisions['packageCommit'],fragments=previous))
    for path in set(previous) | set(owners.values()):
        writes[path] = json_bytes([by_source[p] for p in sorted(by_source) if owners[p] == path]) if path in owners.values() else None
    supplied = set()
    for entry in bundle['files']:
        if set(entry) != {'path','contentPath','sha256'}: raise ValueError('Invalid closure file entry')
        path = entry['path']
        allowed = path in ('docs/parity/dependencies.json','docs/parity/case-registry.json','docs/parity/remnant-dispositions.json','docs/parity/support-map.md','docs/parity/baseline-policy.json') or re.fullmatch(r'docs/(?:catalog/skills/[a-z0-9-]+\.json|skills/[a-z0-9A-Z-]+\.md|principles/README\.md|parity/cases/(?:[a-z0-9-]+/)*[a-z0-9-]+\.json)',path)
        if not allowed or path.endswith('/schema.json') or path in supplied or path in writes:
            raise ValueError('Unowned or duplicate metadata closure path: '+path)
        supplied.add(path)
        if entry['contentPath'] is None:
            if entry['sha256'] is not None: raise ValueError('Metadata deletion must review absence')
            writes[path] = None
        else:
            data = safe_path(review,entry['contentPath']).read_bytes()
            if not entry['contentPath'].startswith('resolved/') or sha256(data) != entry['sha256']:
                raise ValueError('Metadata closure file digest mismatch: '+path)
            writes[path] = data
    if not {'docs/parity/dependencies.json','docs/parity/case-registry.json','docs/parity/baseline-policy.json'} <= supplied:
        raise ValueError('Metadata closure requires reviewed dependencies, cases and baseline policy')
    writes['docs/parity/inventory.json'] = json_bytes(proposed)
    # Existing observations stay at their historical identity and cannot transfer.
    # The registry and aggregate describe the candidate as untested.
    with tempfile.TemporaryDirectory(prefix='pstack-update-projection-',dir=root.parent) as directory:
        projected = Path(directory)
        for path in git_read(root,'ls-files').splitlines():
            source = safe_path(root,path)
            target = projected/path; target.parent.mkdir(parents=True,exist_ok=True)
            shutil.copy2(source,target)
        for path,data in writes.items():
            target = safe_path(projected,path)
            if data is None:
                if target.exists(): target.unlink()
            else:
                target.parent.mkdir(parents=True,exist_ok=True); target.write_bytes(data)
        errors = validate_package(projected,proposed)
        counts = validate_policy(projected,proposed)
        registry, issues = registry_checks(projected,proposed); errors += issues
        if any(e.get('hostStatus') != {'chatgpt':'not-run','codex':'not-run'} for e in registry.values() if not e['structuralOnly']):
            errors.append('candidate registry must invalidate old host status')
        entries = [read_json(p) for p in sorted((projected/'docs/catalog/skills').glob('*.json'))]
        pages = build_catalog(projected,proposed,entries)
        if any(not (projected/p).is_file() or (projected/p).read_text() != text for p,text in pages.items()):
            errors.append('reviewed generated catalog is stale')
        if {p.relative_to(projected).as_posix() for p in (projected/'docs/skills').glob('*.md')} != {p for p in pages if p.startswith('docs/skills/')}:
            errors.append('unowned or removed catalog page remains')
        audit = read_json(projected/'docs/parity/dependencies.json')
        audited = {r['sourcePath']:r for r in audit['sourceAudit']}
        deps = {d['id']:d for d in audit['dependencies']}
        if audit.get('counts') != dict(files=counts['sourceFiles'],rootSkills=counts['leafSkills'],supportIncludingPlaybooks=counts['supportFiles'],playbooks=counts['playbooks']):
            errors.append('dependency counts differ from reviewed baseline')
        if len(audited) != len(audit['sourceAudit']) or set(audited) != set(by_source) or audit['sourceCommit'] != decisions['candidate'] or len(deps) != len(audit['dependencies']):
            errors.append('dependency metadata source closure mismatch')
        for source,row in by_source.items():
            a = audited.get(source,{})
            if (a.get('sourceSha256') != row['upstreamSha256'] or a.get('destinationPath') != row['destinationPath'] or a.get('packageDependencies') != row['dependencies'] or a.get('destinationSha256') != sha256(safe_path(projected,row['destinationPath']).read_bytes())):
                errors.append('dependency metadata differs: '+source)
            if set(a.get('dependencyIds',[])) != {r['dependencyId'] for r in a.get('references',[])}:
                errors.append('dependency reference index differs: '+source)
            for dep in a.get('dependencyIds',[]):
                if dep not in deps or source not in deps[dep]['callers']: errors.append('missing dependency caller: '+source)
        for dep in deps.values():
            if any(p not in audited or dep['id'] not in audited[p]['dependencyIds'] for p in dep['callers']): errors.append('orphan dependency caller: '+dep['id'])
        if errors: raise ValueError('Metadata closure validation failed: '+'; '.join(errors))
    return proposed
