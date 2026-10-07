"""Check package structure. A structural pass makes no host behavior claim."""
import argparse
import hashlib
import json
from pathlib import Path
import re
from urllib.parse import unquote, urlsplit


REMNANTS = re.compile(r'\bTask\b|\bAskQuestion\b|\.cursor(?:[-/\w.]*)|\b(?:claude-\S+|gpt-\S+)\b|\b(?:create_routine|update_routine|delete_routine|routines? API|cloud_only|cloudOnly|destinationHostId)\b')


def schema_errors(value, schema, label):
    """Validate the subset used by the checked-in inventory and case contracts."""
    errors = []
    types = {'object': dict, 'array': list, 'string': str, 'boolean': bool, 'integer': int}
    if 'type' in schema and not isinstance(value, types[schema['type']]):
        return [f'{label}: expected {schema["type"]}']
    if 'enum' in schema and value not in schema['enum']:
        errors.append(f'{label}: invalid value {value!r}')
    if 'const' in schema and value != schema['const']:
        errors.append(f'{label}: expected {schema["const"]!r}')
    if isinstance(value, str):
        if len(value) < schema.get('minLength', 0) or ('pattern' in schema and not re.search(schema['pattern'], value)):
            errors.append(f'{label}: invalid string {value!r}')
    if isinstance(value, list):
        if len(value) < schema.get('minItems', 0):
            errors.append(f'{label}: too few items')
        for index, item in enumerate(value):
            errors += schema_errors(item, schema.get('items', {}), f'{label}[{index}]')
    if isinstance(value, dict):
        for key in schema.get('required', []):
            if key not in value:
                errors.append(f'{label}.{key}: required')
        properties = schema.get('properties', {})
        for key, item in value.items():
            if key in properties:
                errors += schema_errors(item, properties[key], f'{label}.{key}')
            elif schema.get('additionalProperties') is False:
                errors.append(f'{label}.{key}: unknown field')
    return errors


def contained(root, path):
    candidate = root / path
    if Path(path).is_absolute() or not candidate.resolve().is_relative_to(root):
        return None
    return candidate


def read_json(path, fallback):
    return json.loads(path.read_text()) if path.is_file() else fallback


def quoted_regions(lines):
    """Return complete fenced-code and consecutive blockquote regions."""
    regions = []
    fence, start = None, None
    quote_start = None
    for number, line in enumerate(lines, 1):
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if fence:
            closing = re.fullmatch(r' {0,3}' + re.escape(fence[0]) + '{' + str(len(fence)) + r',}[ \t]*', line)
            if closing:
                regions.append((start, number - 1))
                fence, start = None, None
            continue
        if marker and not (marker[1][0] == '`' and '`' in marker[2]):
            if quote_start is not None:
                regions.append((quote_start, number - 1))
                quote_start = None
            fence, start = marker[1], number + 1
        elif re.match(r'^\s{0,3}>', line):
            if quote_start is None:
                quote_start = number
        elif quote_start is not None:
            regions.append((quote_start, number - 1))
            quote_start = None
    if quote_start is not None:
        regions.append((quote_start, len(lines)))
    return regions


def inspect_package(root: Path, inventory: list[dict], scope=None):
    root = Path(root).resolve()
    errors, deferred = [], []
    schema = read_json(root/'docs/parity/inventory.schema.json', None)
    if schema is None:
        return ['docs/parity/inventory.schema.json: missing contract'], []
    errors += schema_errors(inventory, schema, 'inventory')
    if errors:
        return errors, []
    # Fragments supply reviewed destinations without rewriting coordinator-owned inventory.
    effective = {row['upstreamPath']: row for row in inventory}
    for file in sorted((root/'docs/parity/adaptations').glob('*.json')):
        fragment = read_json(file, [])
        fragment_errors = schema_errors(fragment, schema, str(file.relative_to(root)))
        errors += fragment_errors
        if not fragment_errors:
            for row in fragment:
                if row['upstreamPath'] in effective:
                    effective[row['upstreamPath']] = row
    rows = list(effective.values())
    for row in rows:
        for path in [row['destinationPath'], *row['dependencies']]:
            if contained(root, path) is None:
                errors.append(f'{row["upstreamPath"]}: {path}: path or symlink escapes package')
    selected = [row for row in rows if scope is None or row['upstreamPath'] == scope]
    if scope is not None and not selected:
        errors.append(f'{scope}: scope is not inventoried')
    destinations = {row['destinationPath']: row for row in rows}
    seen = set()
    for row in inventory:
        path = row['upstreamPath']
        if path in seen:
            errors.append(f'{path}: duplicate inventory source')
        seen.add(path)
        if contained(root, path) is None:
            errors.append(f'{path}: source path escapes package')
    def check(path, context):
        candidate = contained(root, path)
        if candidate is None:
            errors.append(f'{context}: {path}: path or symlink escapes package')
        elif not candidate.exists():
            row = destinations.get(path)
            if scope is not None and row and row['adaptationStatus'] == 'pending':
                deferred.append(f'{context}: {path}: inventoried pending dependency')
            else:
                errors.append(f'{context}: {path}: missing path')
        return candidate
    for row in selected:
        check(row['destinationPath'], row['upstreamPath'])
        for dependency in row['dependencies']:
            # Explicit upstream dependencies map to their package destinations.
            check(effective.get(dependency, {}).get('destinationPath', dependency), row['upstreamPath'])
    names = {}
    for file in sorted((root/'skills').glob('*/SKILL.md')):
        relative = file.relative_to(root).as_posix()
        check(relative, 'root discovery')
        if contained(root, relative) is None:
            continue
        name = re.search(r'^name:\s*(.+)$', file.read_text(), re.M)
        if name:
            key = name[1].strip(' "\'')
            if key in names:
                errors.append(f'{relative}: duplicate root skill {key}, also {names[key]}')
            names[key] = relative
        if file.parent.name == 'benny' or (name and name[1].strip() == 'benny'):
            errors.append(f'{relative}: benny must stay outside registered root skills')
    manifest = read_json(root/'plugin.json', None)
    if not isinstance(manifest, dict):
        errors.append('plugin.json: missing or invalid manifest')
    else:
        if 'skills' in manifest or 'skills' in manifest.get('extensions', {}).get('com.openai', {}):
            errors.append('plugin.json: root skill discovery must be implicit')
        interface = manifest.get('extensions', {}).get('com.openai', {}).get('interface', {})
        for key in ('logo', 'icon'):
            if key in interface:
                check(interface[key], 'plugin.json')
    dispositions = read_json(root/'docs/parity/remnant-dispositions.json', [])
    if not isinstance(dispositions, list):
        errors.append('docs/parity/remnant-dispositions.json: expected array')
        dispositions = []
    for entry in dispositions:
        if isinstance(entry, dict) and entry.get('kind') == 'historical' and entry.get('path') not in ('docs/superpowers/specs/2026-10-07-pstack-openai-design.md', 'docs/superpowers/plans/2026-10-07-pstack-openai.md'):
            errors.append(f'docs/parity/remnant-dispositions.json: {entry.get("path")}: historical exemption is limited to approved spec and plan')
        if isinstance(entry, dict) and (not re.fullmatch(r'[a-f0-9]{64}', str(entry.get('sha256', ''))) or not entry.get('token') or type(entry.get('startLine')) is not int or type(entry.get('endLine')) is not int or not 1 <= entry['startLine'] <= entry['endLine']):
            errors.append(f'docs/parity/remnant-dispositions.json: invalid hash or token range {entry!r}')
        if not isinstance(entry, dict) or set(entry) != {'path', 'sha256', 'token', 'startLine', 'endLine', 'kind', 'rationale', 'reviewed'} or entry.get('reviewed') is not True or entry.get('kind') not in ('source-only', 'binding', 'historical') or not entry.get('rationale') or any(c in entry.get('path', '') for c in '*?[') or contained(root, entry.get('path', '')) is None:
            errors.append(f'docs/parity/remnant-dispositions.json: invalid narrow disposition {entry!r}')
    markdown = sorted(root.rglob('*.md')) if scope is None else [root/row['destinationPath'] for row in selected if row['destinationPath'].endswith('.md')]
    for file in markdown:
        relative = file.relative_to(root).as_posix()
        if relative.startswith(('.git/', '.superpowers/')):
            continue
        if contained(root, relative) is None:
            errors.append(f'{relative}: symlink escapes package')
            continue
        if not file.is_file():
            continue
        content = file.read_text()
        lines = content.splitlines()
        digest = hashlib.sha256(file.read_bytes()).hexdigest()
        approved = [entry for entry in dispositions if isinstance(entry, dict) and entry.get('path') == relative and entry.get('sha256') == digest and entry.get('reviewed') is True]
        valid = []
        regions = quoted_regions(lines)
        for entry in approved:
            first, last = entry.get('startLine'), entry.get('endLine')
            if type(first) is not int or type(last) is not int or not 1 <= first <= last <= len(lines):
                errors.append(f'{relative}: invalid disposition range {first}..{last}')
                continue
            if entry.get('kind') == 'source-only' and not any(begin <= first <= last <= end for begin, end in regions):
                errors.append(f'{relative}: source-only range {first}..{last} must stay inside one explicit quote or fenced example')
                continue
            if not any(entry.get('token') == match[0] for line in lines[first - 1:last] for match in REMNANTS.finditer(line)):
                errors.append(f'{relative}: disposition range {first}..{last} does not contain exact remnant token')
                continue
            valid.append(entry)
        approved = valid
        historical = any(entry.get('kind') == 'historical' for entry in approved)
        if not historical:
            # Exact source-only ranges are data. Unreviewed examples remain checked.
            operative = '\n'.join(line for number, line in enumerate(content.splitlines(), 1) if not any(entry.get('kind') == 'source-only' and isinstance(entry.get('startLine'), int) and isinstance(entry.get('endLine'), int) and entry['startLine'] <= number <= entry['endLine'] for entry in approved))
            links = re.findall(r'!?\[[^\]]*\]\(\s*(<[^>]*>|[^\s)]+)', operative)
            definitions = re.findall(r'^\s*\[([^\]]+)\]:\s*(<[^>]*>|\S+)', operative, re.M)
            links += [target for _, target in definitions]
            labels = {label.casefold() for label, _ in definitions}
            for label, reference in re.findall(r'!?\[([^\]]+)\]\[([^\]]*)\]', operative):
                reference = reference or label
                if reference.casefold() not in labels:
                    errors.append(f'{relative}: [{reference}]: undefined Markdown reference')
            for link in links:
                target = unquote(link.strip('<>'))
                parsed = urlsplit(target)
                if parsed.scheme or target.startswith('#') or not parsed.path:
                    continue
                if Path(parsed.path).is_absolute():
                    check(parsed.path, relative)
                    continue
                path = (file.parent/parsed.path).relative_to(root).as_posix()
                # Normalize .. before matching inventory, but never permit escape.
                resolved = (root/path).resolve()
                normalized = resolved.relative_to(root).as_posix() if resolved.is_relative_to(root) else path
                check(normalized, relative)
        for number, line in enumerate(content.splitlines(), 1):
            for match in REMNANTS.finditer(line):
                token = match[0]
                if not any(entry.get('token') == token and isinstance(entry.get('startLine'), int) and isinstance(entry.get('endLine'), int) and entry['startLine'] <= number <= entry['endLine'] for entry in approved):
                    errors.append(f'{relative}:{number}: remnant {token!r} needs reviewed binding or source-only disposition')
    case_schema = read_json(root/'docs/parity/cases/schema.json', None)
    if case_schema is None:
        errors.append('docs/parity/cases/schema.json: missing contract')
    case_ids = set()
    for file in sorted((root/'docs/parity/cases').glob('*.json')):
        if file.name == 'schema.json':
            continue
        cases = read_json(file, [])
        for case in cases if isinstance(cases, list) else [cases]:
            if scope is None or (isinstance(case, dict) and scope in case.get('sourcePaths', [])):
                errors += schema_errors(case, case_schema or {}, file.relative_to(root).as_posix())
                if isinstance(case, dict):
                    case_id = case.get('id')
                    if isinstance(case_id, str):
                        if case_id in case_ids:
                            errors.append(f'{file.relative_to(root)}: duplicate case id {case_id}')
                        case_ids.add(case_id)
                    for source in case.get('sourcePaths', []):
                        if source not in effective:
                            errors.append(f'{file.relative_to(root)}: {source}: case source is not inventoried')
    return sorted(set(errors)), sorted(set(deferred))


def validate_package(root: Path, inventory: list[dict]) -> list[str]:
    return inspect_package(root, inventory)[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--inventory', type=Path, required=True)
    parser.add_argument('--scope')
    args = parser.parse_args()
    try:
        inventory = json.loads(args.inventory.read_text())
        errors, deferred = inspect_package(args.root, inventory, args.scope)
    except (OSError, ValueError, TypeError) as error:
        parser.exit(2, f'Invalid input: {error}\n')
    for error in errors:
        print(f'ERROR: {error}')
    for dependency in deferred:
        print(f'DEFERRED: {dependency}')
    if not errors:
        print('Scoped structural checks passed; deferred dependencies and full package acceptance remain unverified.' if args.scope else 'Package structural checks passed; host behavior remains unverified.')
    return int(bool(errors))


if __name__ == '__main__':
    raise SystemExit(main())
