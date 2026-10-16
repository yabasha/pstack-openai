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


def quoted_regions(lines, *, fenced_only=False):
    """Return complete fences, consecutive blockquotes and quoted bullets.

    fenced_only excludes blockquotes and quoted single-line bullets.
    """
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
        elif not fenced_only and re.match(r'^ {0,3}- "[^"\n]*"\s*$', line):
            if quote_start is not None:
                regions.append((quote_start, number - 1))
                quote_start = None
            regions.append((number, number))
        elif not fenced_only and re.match(r'^\s{0,3}>', line):
            if quote_start is None:
                quote_start = number
        elif quote_start is not None:
            regions.append((quote_start, number - 1))
            quote_start = None
    if quote_start is not None:
        regions.append((quote_start, len(lines)))
    return regions


def unique_json_object(pairs):
    """Reject ambiguous duplicate fields in report data and its membership marker."""
    result = dict(pairs)
    if len(result) != len(pairs):
        raise ValueError('duplicate JSON object field')
    return result


def captured_report_paths(root):
    """Read explicit report membership without asserting tested Git identity."""
    path = root/'docs/parity/tested-package.json'
    if not path.exists() and not path.is_symlink():
        return None, []
    try:
        if contained(root, 'docs/parity/tested-package.json') is None or not path.is_file():
            raise ValueError('unsafe or non-file marker')
        marker = json.loads(path.read_text(), object_pairs_hook=unique_json_object)
        if (not isinstance(marker, dict) or set(marker) != {'schemaVersion','kind','testedCommit','reportPaths'}
                or type(marker['schemaVersion']) is not int or marker['schemaVersion'] != 1
                or marker['kind'] != 'pstack-tested-package'
                or not isinstance(marker['testedCommit'], str) or not re.fullmatch('[0-9a-f]{40}', marker['testedCommit'])
                or not isinstance(marker['reportPaths'], list)
                or any(not isinstance(p, str) or not p or '\\' in p or Path(p).is_absolute()
                       or any(part in ('', '.', '..') for part in p.split('/')) for p in marker['reportPaths'])
                or len(marker['reportPaths']) != len(set(marker['reportPaths']))):
            raise ValueError('invalid report marker shape')
        return set(marker['reportPaths']), []
    except (OSError, ValueError, TypeError, KeyError) as error:
        return set(), [f'docs/parity/tested-package.json: invalid report-data membership: {error}']


def captured_report_regions(root, relative, lines, inventory, declared_paths):
    """Classify only identity-bound closed workflow-report JSON as inert data.

    The fixed path/envelope contract survives an updater removing its old marker.
    This does not validate grades, host execution or immutable Git provenance.
    Prose outside the JSON remains ordinary checked package documentation.
    """
    match = re.fullmatch(r'docs/releases/host-evaluation/(chatgpt|codex)/([a-z0-9]+(?:-[a-z0-9]+)*)\.md', relative)
    if not match:
        return [], []
    error = lambda detail: ([], [f'{relative}: invalid captured workflow report: {detail}'])
    rows = {row['upstreamPath']: row for row in inventory}
    operative = {row['destinationPath'] for row in inventory}
    operative.update(rows.get(dep, {}).get('destinationPath', dep) for row in inventory for dep in row.get('dependencies', []))
    target = (root/relative).resolve()
    if target.relative_to(root).as_posix() != relative:
        return error('symlink aliases cannot classify operative content as report data')
    if any(target == (root/path).resolve() or target.is_relative_to((root/path).resolve()) for path in operative):
        return error('inventory destinations and dependencies are operative')
    if declared_paths is not None and relative not in declared_paths:
        return error('not explicitly listed in tested-package reportPaths')
    fences = [(first, last) for first, last in quoted_regions(lines, fenced_only=True)
              if re.fullmatch(r' {0,3}(?:`{3,}|~{3,})json[ \t]*', lines[first-2])]
    if len(fences) != 1:
        return error('exactly one closed JSON envelope required')
    first, last = fences[0]
    try:
        data = json.loads('\n'.join(lines[first-1:last]), object_pairs_hook=unique_json_object)
    except (ValueError, TypeError):
        return error('malformed JSON envelope')
    fields = {'schemaVersion','sourceFreeze','reportScope','host','caseId','acceptedStatus',
              'acceptedAttemptId','acceptanceRule','casePrompt','caseDefinition','registry',
              'attempts','artifactProjections','skippedManifest','globalLimits'}
    statuses = {'pass','reduced-pass','blocked','fail','not-run'}
    if (not isinstance(data, dict) or set(data) != fields
            or type(data['schemaVersion']) is not int or data['schemaVersion'] != 1
            or data['host'] != match[1] or data['caseId'] != match[2]
            or not isinstance(data['sourceFreeze'], str) or not re.fullmatch('[0-9a-f]{40}', data['sourceFreeze'])
            or any(not isinstance(data[k], str) or not data[k].strip()
                   for k in ('reportScope','acceptedStatus','acceptanceRule','casePrompt'))
            or data['acceptedStatus'] not in statuses | {'pending'}
            or (data['acceptedStatus'] != 'pending' and (not isinstance(data['acceptedAttemptId'], str) or not data['acceptedAttemptId'].strip()))
            or not isinstance(data['caseDefinition'], dict) or data['caseDefinition'].get('id') != data['caseId']
            or data['caseDefinition'].get('prompt') != data['casePrompt']
            or not isinstance(data['registry'], dict) or data['registry'].get('caseId') != data['caseId']
            or any(not isinstance(data[k], list) for k in ('attempts','artifactProjections','skippedManifest','globalLimits'))
            or not data['globalLimits']
            or any(not isinstance(limit, str) or not limit.strip() for limit in data['globalLimits'])):
        return error('envelope shape or identity differs from the report path')
    if data['acceptedStatus'] == 'pending':
        if data['acceptedAttemptId'] is not None or data['attempts']:
            return error('pending reports cannot claim a selected or graded attempt')
        return fences, []
    ids = set()
    for attempt in data['attempts']:
        if (not isinstance(attempt, dict) or not isinstance(attempt.get('attemptId'), str)
                or not attempt['attemptId'].strip() or attempt['attemptId'] in ids
                or attempt.get('host') != data['host'] or attempt.get('caseId') != data['caseId']
                or not isinstance(attempt.get('status'), str) or attempt['status'] not in statuses
                or not isinstance(attempt.get('grade'), dict)):
            return error('attempt identities must match the envelope')
        ids.add(attempt['attemptId'])
    selected = [a for a in data['attempts'] if a['attemptId'] == data['acceptedAttemptId']]
    if len(selected) != 1 or selected[0]['status'] != data['acceptedStatus']:
        return error('selected attempt identity or status differs')
    return fences, []


def mask_inline_code(text):
    """Mask matched backtick runs for link extraction, retaining line boundaries."""
    # Delimiters in separate blocks cannot form a code span. Treat block
    # marker lines independently; ordinary consecutive prose lines stay together.
    boundary = re.compile(r'^ {0,3}(?:#{1,6}(?:[ \t]|$)|>|[-+*][ \t]+|1[.)][ \t]+|`{3,}|~{3,}|(?:=[ \t]*)+$|-+[ \t]*$|(?:[-_*][ \t]*){3,}$)')
    html_tags = 'address article aside base basefont blockquote body caption center col colgroup dd details dialog dir div dl dt fieldset figcaption figure footer form frame frameset h1 h2 h3 h4 h5 h6 head header hr html iframe legend li link main menu menuitem nav noframes ol optgroup option p param search section summary table tbody td tfoot th thead title tr track ul'
    html_boundary = re.compile(r'^ {0,3}(?:<!--|<\?|<![A-Z]|<!\[CDATA\[|(?i:<(?:script|pre|style|textarea)(?:[ \t>]|$)|</?(?:' + '|'.join(html_tags.split()) + r')(?:[ \t]|/?>|$)))')
    output, paragraph = [], []
    for line in text.splitlines(keepends=True):
        if not line.strip() or boundary.match(line.rstrip('\r\n')) or html_boundary.match(line.rstrip('\r\n')):
            output.append(mask_inline_code_block(''.join(paragraph)))
            paragraph = []
            output.append(mask_inline_code_block(line))
        else:
            paragraph.append(line)
    output.append(mask_inline_code_block(''.join(paragraph)))
    return ''.join(output)


def mask_inline_code_block(text):
    """Mask equal-length delimiter pairs within one conservatively bounded block."""
    characters = list(text)
    runs = list(re.finditer(r'`+', text))
    next_match, following = {}, {}
    for index in range(len(runs) - 1, -1, -1):
        length = len(runs[index][0])
        if length in following:
            next_match[index] = following[length]
        following[length] = index
    index = 0
    while index < len(runs):
        opening = runs[index]
        position = opening.start() - 1
        while position >= 0 and text[position] == '\\':
            position -= 1
        escaped = (opening.start() - position - 1) % 2
        closing_index = next_match.get(index)
        if escaped or closing_index is None:
            index += 1
            continue
        closing = runs[closing_index]
        for position in range(opening.start(), closing.end()):
            if characters[position] not in '\r\n':
                characters[position] = ' '
        index = closing_index + 1
    return ''.join(characters)


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
    fragment_owners = set()
    for file in sorted((root/'docs/parity/adaptations').glob('*.json')):
        fragment = read_json(file, [])
        fragment_errors = schema_errors(fragment, schema, str(file.relative_to(root)))
        errors += fragment_errors
        if not fragment_errors:
            for row in fragment:
                source = row['upstreamPath']
                if source not in effective:
                    errors.append(f'{file.name}: unknown active fragment source {source}')
                elif source in fragment_owners:
                    errors.append(f'{file.name}: duplicate active fragment owner {source}')
                elif any(v != effective[source].get(k) for k,v in row.items() if k != 'verification'):
                    # During leaf development only a scoped pending row can be supplied.
                    if scope == source and effective[source]['adaptationStatus'] == 'pending' and all(row[k] == effective[source][k] for k in ('upstreamCommit','upstreamSha256')):
                        effective[source] = row
                    else:
                        errors.append(f'{file.name}: conflicting active fragment {source}')
                fragment_owners.add(source)
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
    def check(path, context, allow_deferred=True):
        candidate = contained(root, path)
        if candidate is not None and candidate.resolve().is_relative_to(root / '.upstream'):
            errors.append(f'{context}: {path}: inert review data cannot be an operative destination or dependency')
            return None
        if candidate is None:
            errors.append(f'{context}: {path}: path or symlink escapes package')
        elif not candidate.exists():
            row = destinations.get(path)
            if allow_deferred and scope is not None and row and row['adaptationStatus'] == 'pending':
                deferred.append(f'{context}: {path}: inventoried pending dependency')
            else:
                errors.append(f'{context}: {path}: missing path')
        return candidate
    for row in selected:
        check(row['destinationPath'], row['upstreamPath'], allow_deferred=False)
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
    declared_reports, report_errors = captured_report_paths(root)
    errors += report_errors
    markdown = sorted(root.rglob('*.md')) if scope is None else [root/row['destinationPath'] for row in selected if row['destinationPath'].endswith('.md')]
    for file in markdown:
        relative = file.relative_to(root).as_posix()
        if relative.startswith(('.git/', '.superpowers/', '.upstream/')):
            continue
        if contained(root, relative) is None:
            errors.append(f'{relative}: symlink escapes package')
            continue
        if not file.is_file():
            continue
        content = file.read_text()
        lines = content.splitlines()
        report_data, report_errors = captured_report_regions(root, relative, lines, rows, declared_reports)
        errors += report_errors
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
            # Fenced literals are not rendered links. Remnants still require exact review.
            fences = quoted_regions(lines, fenced_only=True)
            operative = '\n'.join('' if any(begin <= number <= end for begin, end in fences) or any(entry.get('kind') == 'source-only' and entry['startLine'] <= number <= entry['endLine'] for entry in approved) else line for number, line in enumerate(lines, 1))
            operative = mask_inline_code(operative)
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
            if any(first <= number <= last for first, last in report_data):
                continue
            for match in REMNANTS.finditer(line):
                token = match[0]
                if not any(entry.get('token') == token and isinstance(entry.get('startLine'), int) and isinstance(entry.get('endLine'), int) and entry['startLine'] <= number <= entry['endLine'] for entry in approved):
                    errors.append(f'{relative}:{number}: remnant {token!r} needs reviewed binding or source-only disposition')
    cases_root = contained(root, 'docs/parity/cases')
    if cases_root is None:
        errors.append('docs/parity/cases: path or symlink escapes package')
        return sorted(set(errors)), sorted(set(deferred))
    schema_path = contained(root, 'docs/parity/cases/schema.json')
    if schema_path is None:
        errors.append('docs/parity/cases/schema.json: path or symlink escapes package')
    case_schema = read_json(schema_path, None) if schema_path else None
    if case_schema is None:
        errors.append('docs/parity/cases/schema.json: missing contract')
    case_ids = set()
    for file in sorted(cases_root.rglob('*')):
        relative = file.relative_to(root).as_posix()
        if contained(root, relative) is None:
            errors.append(f'{relative}: case path or symlink escapes package')
            continue
        if not file.is_file() or file.suffix != '.json' or file == schema_path:
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
