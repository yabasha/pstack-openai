"""Render the reviewed catalog without claiming behavioral verification."""
import argparse
import json
import os
import re
from pathlib import Path

REQUIRED = ('name', 'kind', 'purpose', 'triggers', 'inputs', 'outputs',
            'ordinaryExample', 'dependencies', 'capabilityLimits', 'sourcePaths', 'caseIds')
ARRAY_FIELDS = ('triggers', 'inputs', 'outputs', 'dependencies', 'capabilityLimits', 'sourcePaths', 'caseIds')
NAME = re.compile(r'[a-z0-9]+(?:-[a-z0-9]+)*')
LEAF = re.compile(r'skills/([^/]+)/SKILL\.md')


def load_cases(root: Path) -> dict:
    """Read object and array case files; retain their owning file paths."""
    cases = {}
    for path in sorted((root / 'docs/parity/cases').rglob('*.json')):
        if path.name == 'schema.json':
            continue
        value = json.loads(path.read_text())
        for case in value if isinstance(value, list) else [value]:
            case_id = case.get('id')
            if not case_id or case_id in cases:
                raise ValueError(f'Invalid or duplicate case ID in {path}')
            cases[case_id] = (path.relative_to(root).as_posix(), case)
    return cases


def local_link(root: Path, destination: str, target: str, label: str | None = None) -> str:
    path = Path(target)
    resolved = (root / path).resolve()
    if path.is_absolute() or not resolved.is_relative_to(root.resolve()) or not resolved.exists():
        raise ValueError(f'Missing or unsafe local link: {target}')
    relative = os.path.relpath(root / path, (root / destination).parent)
    return f'[{label or target}]({relative})'


def bullets(values: list[str]) -> str:
    return '\n'.join(f'- {value}' for value in values)


def validate_entries(inventory: list[dict], entries: list[dict]) -> None:
    expected = {match.group(1) for row in inventory
                if (match := LEAF.fullmatch(row['upstreamPath']))}
    if len(expected) != 51 or sum(name.startswith('principle-') for name in expected) != 24:
        raise ValueError('Inventory must contain exactly 51 root skills and 24 principles')
    names = []
    for entry in entries:
        if set(entry) != set(REQUIRED):
            raise ValueError('Catalog entry fields must match the catalog schema')
        for field in ('name', 'purpose', 'ordinaryExample'):
            if not isinstance(entry[field], str) or not entry[field].strip():
                raise ValueError(f'Empty or invalid catalog {field}')
        if not NAME.fullmatch(entry['name']):
            raise ValueError('Invalid catalog name')
        principle = entry['name'].startswith('principle-')
        if (entry['kind'] not in ('principle', 'workflow', 'skill', 'mode') or
                principle != (entry['kind'] == 'principle')):
            raise ValueError(f'Invalid kind for {entry["name"]}')
        for field in ARRAY_FIELDS:
            values = entry[field]
            if (not isinstance(values, list) or (field != 'dependencies' and not values) or
                    any(not isinstance(value, str) or not value.strip() for value in values) or
                    len(values) != len(set(values))):
                raise ValueError(f'Invalid catalog {field} for {entry["name"]}')
        if f'skills/{entry["name"]}/SKILL.md' not in entry['sourcePaths']:
            raise ValueError('Catalog entry must cite its owning root skill')
        names.append(entry['name'])
    if len(names) != len(set(names)) or set(names) != expected:
        raise ValueError('Catalog names must exactly match the 51 inventoried root skills')


def build_catalog(root: Path, inventory: list[dict], entries: list[dict]) -> dict[str, str]:
    """Return only the 51 leaf pages and two overview pages."""
    root = root.resolve()
    validate_entries(inventory, entries)
    sources = {row['upstreamPath']: row for row in inventory}
    cases = load_cases(root)
    pages = {}
    entries = sorted(entries, key=lambda entry: entry['name'])
    for entry in entries:
        name = entry['name']
        destination = f'docs/skills/{name}.md'
        link = lambda target, label=None: local_link(root, destination, target, label)
        lines = [f'# {name}', '',
                 'Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.', '',
                 f'Catalog record: {link(f"docs/catalog/skills/{name}.json")}.', '',
                 f'Skill: {link(f"skills/{name}/SKILL.md")}. Kind: {entry["kind"]}.', '',
                 '## Purpose', '', entry['purpose'], '', '## Triggers', '', bullets(entry['triggers']), '',
                 '## Required input', '', bullets(entry['inputs']), '', '## Output contract', '', bullets(entry['outputs']), '',
                 '## Ordinary example', '', entry['ordinaryExample'], '',
                 'The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.', '']
        for case_id in entry['caseIds']:
            if case_id not in cases:
                raise ValueError(f'Missing case {case_id} for {name}')
            case_path, case = cases[case_id]
            if f'skills/{name}/SKILL.md' not in case['sourcePaths']:
                raise ValueError(f'Case {case_id} does not cover {name}')
            for field in ('prompt', 'expectedFull', 'expectedReduced', 'expectedBlocked'):
                if not isinstance(case.get(field), str) or not case[field].strip():
                    raise ValueError(f'Invalid {field} in {case_id}')
            lines += [f'### Case {link(case_path, case_id)}', '', case['prompt'], '',
                      'Full capability expectation:', '', case['expectedFull'], '',
                      'Reduced capability expectation:', '', case['expectedReduced'], '',
                      'Blocked capability expectation:', '', case['expectedBlocked'], '',
                      'Required observations:', '', bullets(case['requirements']), '',
                      'Forbidden claims:', '', bullets(case['forbiddenClaims']), '']
        lines += ['## Dependencies', '', bullets([link(path) for path in entry['dependencies']]) or 'No dependencies declared in the reviewed record.', '',
                  '## Host limits', '', bullets(entry['capabilityLimits']), '',
                  '## Source proof and release evidence', '',
                  'The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.', '']
        for source_path in entry['sourcePaths']:
            if source_path not in sources:
                raise ValueError(f'Uninventoried source {source_path}')
            row = sources[source_path]
            lines += [f'### `{source_path}`', '',
                      f'Destination: {link(row["destinationPath"])}.', '',
                      f'Upstream commit: `{row["upstreamCommit"]}`. SHA-256: `{row["upstreamSha256"]}`.', '',
                      f'Disposition: `{row["disposition"]}`. Aggregate adaptation status: `{row["adaptationStatus"]}`.', '']
            for host in ('chatgpt', 'codex'):
                verification = row['verification'][host]
                evidence = verification['evidence']
                refs = ', '.join(link(path) for path in evidence) if evidence else 'none recorded'
                lines += [f'- {host}: `{verification["status"]}`. Tested release evidence: {refs}.']
            lines.append('')
        pages[destination] = '\n'.join(lines).rstrip() + '\n'
    for destination, title, selection in (
        ('docs/skills/README.md', 'Skill catalog', entries),
        ('docs/principles/README.md', 'Principle catalog', [entry for entry in entries if entry['kind'] == 'principle']),
    ):
        link = lambda target, label=None: local_link(root, destination, target, label)
        # Leaf links are generated in the same batch and may not exist yet.
        lines = [f'# {title}', '', 'Generated from 51 reviewed leaf records, including 24 principles. No additional root skill is registered.', '',
                 'Host support depends on capabilities, permissions and observed evidence. Inventory review may remain pending, and a not-run result remains untested.', '',
                 f'Source inventory: {link("docs/parity/inventory.json")}. Catalog schema: {link("docs/catalog/schema.json")}.', '',
                 '| Name | Purpose |', '| --- | --- |']
        for entry in selection:
            target = os.path.relpath(root / f'docs/skills/{entry["name"]}.md', (root / destination).parent)
            purpose = entry['purpose'].replace('|', '\\|').replace('\n', ' ')
            lines.append(f'| [{entry["name"]}]({target}) | {purpose} |')
        pages[destination] = '\n'.join(lines) + '\n'
    return pages


def sync_catalog(root: Path, pages: dict[str, str], *, check: bool) -> list[str]:
    """Compare or write owned outputs; never delete unrelated files."""
    root = root.resolve()
    targets = {}
    for destination in pages:
        allowed = destination in ('docs/skills/README.md', 'docs/principles/README.md') or (
            destination.startswith('docs/skills/') and destination.endswith('.md') and
            NAME.fullmatch(destination.removeprefix('docs/skills/').removesuffix('.md')))
        target = root / destination
        if not allowed or not target.resolve().is_relative_to(root):
            raise ValueError(f'Unowned output path: {destination}')
        if any(part.is_symlink() for part in (target, *target.parents) if part != root and part.is_relative_to(root)):
            raise ValueError(f'Symlink output path: {destination}')
        targets[destination] = target
    stale = []
    for destination, target in targets.items():
        if not target.is_file() or target.read_text() != pages[destination]:
            stale.append(destination)
            if not check:
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(pages[destination])
    return sorted(stale)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, default=Path('.'))
    parser.add_argument('--check', action='store_true')
    args = parser.parse_args()
    try:
        root = args.root.resolve()
        inventory = json.loads((root / 'docs/parity/inventory.json').read_text())
        entries = [json.loads(path.read_text()) for path in sorted((root / 'docs/catalog/skills').glob('*.json'))]
        stale = sync_catalog(root, build_catalog(root, inventory, entries), check=args.check)
    except (ValueError, OSError, KeyError, TypeError) as error:
        parser.error(str(error))
    if args.check and stale:
        print('Catalog drift:\n' + '\n'.join(stale))
        return 1
    print(f'Catalog {"check passed" if args.check else "generated"}: 51 skills, 24 principles.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
