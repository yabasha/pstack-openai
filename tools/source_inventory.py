"""Record pinned source files without executing source code."""

import argparse
import hashlib
import json
from pathlib import Path


def inspect_source(root: Path, commit: str) -> list[dict]:
    root = Path(root)
    if '..' in root.parts or root.is_symlink():
        raise ValueError('Source root must be a direct directory path')
    root = root.resolve(strict=True)
    if not root.is_dir():
        raise ValueError('Source root must be a directory')
    records = []
    for path in sorted(root.rglob('*')):
        if path.is_symlink() or not path.resolve().is_relative_to(root):
            raise ValueError(f'Unsafe source path: {path}')
        if path.is_dir():
            continue
        if not path.is_file():
            raise ValueError(f'Non-regular source path: {path}')
        relative = path.relative_to(root).as_posix()
        destination = relative
        disposition = 'runtime'
        rationale = 'Retain the canonical path; adaptation review remains pending.'
        if relative == '.cursor-plugin/plugin.json':
            destination = 'plugin.json'
            disposition = 'metadata-replaced'
            rationale = 'Replace host-specific package metadata with the portable manifest.'
        elif relative.startswith('agents/'):
            destination = 'references/agent-prompts/' + path.name
            disposition = 'relocated'
            rationale = 'Keep role instructions as portable prompt references.'
        elif relative in ('README.md', '.gitignore', 'LICENSE') or relative.startswith(('docs/', 'assets/')):
            disposition = 'reference-only'
            rationale = 'Preserve source provenance; this file does not establish runtime behavior.'
        records.append({
            'upstreamPath': relative,
            'upstreamCommit': commit,
            'upstreamSha256': hashlib.sha256(path.read_bytes()).hexdigest(),
            'destinationPath': destination,
            'disposition': disposition,
            'rationale': rationale,
            'dependencies': [],
            'licenseProvenance': {'license': 'MIT', 'copyright': 'Copyright (c) 2026 Lauren Tan', 'sourcePath': 'LICENSE'},
            'adaptationStatus': 'pending',
            'verification': {host: {'status': 'not-run', 'evidence': []} for host in ('chatgpt', 'codex')},
        })
    return records


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source', required=True, type=Path)
    parser.add_argument('--commit', required=True)
    parser.add_argument('--output', required=True, type=Path)
    args = parser.parse_args()
    records = inspect_source(args.source, args.commit)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(records, indent=2) + '\n')


if __name__ == '__main__':
    main()
