"""Compare source digests with adapted bytes without changing the package."""
import hashlib
from pathlib import Path, PurePosixPath
import re


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def relative_path(value):
    if not isinstance(value, str) or not value or '\\' in value or any(ord(c) < 32 for c in value):
        raise ValueError('Expected a relative POSIX path')
    path = PurePosixPath(value)
    if path.is_absolute() or any(p in ('', '.', '..') for p in value.split('/')):
        raise ValueError(f'Unsafe path: {value}')
    return path


def adapted_path(root, relative):
    parts = relative_path(relative).parts
    if any(part.lower() in ('.git', '.upstream', '.codex', '.claude', '.cursor', '.ssh', '.aws', 'credentials', 'secrets') or part.lower().startswith('.env') for part in parts):
        raise ValueError(f'Protected adapted path: {relative}')
    return safe_path(root, relative)


def safe_path(root, relative):
    relative_path(relative)
    root = Path(root).absolute()
    path = root / relative
    for parent in (path, *path.parents):
        if parent.is_symlink():
            raise ValueError(f'Symlink is not allowed: {parent}')
    if not path.resolve().is_relative_to(root.resolve()):
        raise ValueError('Path escapes root')
    return path


def index_records(records):
    result = {}
    destinations = set()
    commits = set()
    for record in records:
        path = record['upstreamPath']
        relative_path(path)
        destination = record.get('destinationPath', path)
        relative_path(destination)
        if path in result or destination in destinations:
            raise ValueError('Duplicate source or destination identity')
        if not re.fullmatch('[0-9a-f]{64}', record['upstreamSha256']):
            raise ValueError('Invalid source SHA-256')
        if not re.fullmatch('[0-9a-f]{40}', record['upstreamCommit']):
            raise ValueError('Invalid source commit')
        commits.add(record['upstreamCommit'])
        destinations.add(destination)
        result[path] = record
    if len(commits) > 1:
        raise ValueError('Mixed source revisions')
    return result


def compare_sources(old: list[dict], new: list[dict], adapted_root: Path) -> dict:
    before, after = index_records(old), index_records(new)
    result = {key: [] for key in ('added', 'removed', 'changed', 'unchanged',
                                  'possibleRenames', 'conflicts', 'noticeChanges')}
    result.update(schemaVersion=1, acceptanceReady=False)
    for path in sorted(before.keys() | after.keys()):
        original, candidate = before.get(path), after.get(path)
        owner = original or candidate
        destination = owner.get('destinationPath', path)
        target = adapted_path(adapted_root, destination)
        if target.exists() and not target.is_file():
            raise ValueError(f'Adapted target is not a regular file: {destination}')
        local_hash = sha256(target.read_bytes()) if target.exists() else None
        old_hash = original['upstreamSha256'] if original else None
        new_hash = candidate['upstreamSha256'] if candidate else None
        category = 'added' if original is None else 'removed' if candidate is None else 'unchanged' if old_hash == new_hash else 'changed'
        entry = {'path': path, 'destinationPath': destination,
                 'oldSha256': old_hash, 'newSha256': new_hash, 'adaptedSha256': local_hash,
                 'resolution': 'required' if category != 'unchanged' else 'unchanged',
                 'dependencies': owner.get('dependencies', []),
                 'dependentCallers': sorted(p for p, record in before.items()
                                            if path in record.get('dependencies', []) or destination in record.get('dependencies', []))}
        result[category].append(entry)
        if category == 'changed' and local_hash not in (old_hash, new_hash):
            result['conflicts'].append(entry)
        elif category == 'added' and local_hash is not None and local_hash != new_hash:
            result['conflicts'].append(entry)
        if category != 'unchanged' and any(token in Path(path).name.upper() for token in ('LICENSE', 'NOTICE', 'COPYING', 'COPYRIGHT')):
            result['noticeChanges'].append(entry)
    for removed in result['removed']:
        for added in result['added']:
            if removed['oldSha256'] == added['newSha256']:
                result['possibleRenames'].append({'oldPath': removed['path'], 'newPath': added['path'], 'sha256': added['newSha256']})
    result['skills'] = {key: [entry['path'] for entry in result[key] if entry['path'].endswith('/SKILL.md')] for key in ('added', 'removed', 'changed', 'unchanged')}
    return result
