"""Validate observations without inferring host support from maintenance checks."""
import argparse
import json
import re
from datetime import date
from pathlib import Path
try:
    from .validate_package import schema_errors
except ImportError:
    from validate_package import schema_errors


def validate_evidence(record: dict, package_commit: str, root: Path) -> list[str]:
    errors = []
    if not isinstance(record, dict):
        return ['record must be an object']
    schema = json.loads((Path(__file__).resolve().parents[1] / 'docs/parity/evidence.schema.json').read_text())
    shape_errors = schema_errors(record, schema, 'record')
    if shape_errors:
        return shape_errors
    registry_path = root / 'docs/parity/case-registry.json'
    if registry_path.is_file():
        try:
            entries = json.loads(registry_path.read_text())['entries']
            entry = next((item for item in entries if item['caseId'] == record['caseId']), None)
            if entry is None or entry.get('structuralOnly') or record['host'] not in entry['requiredHosts']:
                errors.append('caseId: no applicable behavioral registry entry for host')
            elif set(record['sourcePaths']) != set(entry['sourcePaths']):
                errors.append('sourcePaths: must match registered case scope')
        except (OSError, ValueError, KeyError, TypeError):
            errors.append('case registry: malformed applicability artifact')
    required_strings = ('caseId', 'packageVersion', 'packageCommit', 'host', 'hostMode', 'date',
                        'input', 'observedOutput', 'status', 'execution')
    for key in required_strings:
        if not isinstance(record.get(key), str) or not record[key].strip():
            errors.append(f'{key}: expected nonempty string')
    for key in ('sourcePaths', 'documentedCapabilities', 'exposedTools', 'artifacts', 'limits',
                'priorActionIdentities'):
        value = record.get(key)
        if not isinstance(value, list) or any(not isinstance(x, str) or not x.strip() for x in value):
            errors.append(f'{key}: expected string array')
    if not record.get('sourcePaths'):
        errors.append('sourcePaths: at least one source required')
    if record.get('packageCommit') != package_commit or not re.fullmatch(r'[0-9a-f]{40}', str(record.get('packageCommit'))):
        errors.append('packageCommit: must match exact tested package revision')
    try:
        date.fromisoformat(record.get('date', ''))
    except (ValueError, TypeError):
        errors.append('date: expected ISO date')
    if record.get('host') not in ('chatgpt', 'codex'):
        errors.append('host: unknown host')
    status = record.get('status')
    if status not in ('not-run', 'pass', 'reduced-pass', 'blocked', 'fail'):
        errors.append('status: unknown status')
    execution = record.get('execution')
    if execution not in ('workers', 'sequential', 'unavailable', 'not-run'):
        errors.append('execution: unknown execution mode')
    permissions = record.get('permissions')
    if not isinstance(permissions, dict) or any(permissions.get(k) not in ('granted', 'denied', 'unavailable', 'unknown') for k in ('execution', 'writes', 'externalActions')):
        errors.append('permissions: execution, writes and externalActions decisions required')
        permissions = {}
    models = record.get('models')
    if not isinstance(models, dict) or any(not isinstance(models.get(k), str) or not models[k].strip() for k in ('requested', 'actual')):
        errors.append('models: requested and actual must be observed values or unknown')
    operations = record.get('successfulOperations')
    if not isinstance(operations, list):
        errors.append('successfulOperations: expected array')
        operations = []
    def artifact(path):
        if not isinstance(path, str) or not path:
            return False
        resolved = (root / path).resolve()
        return not Path(path).is_absolute() and resolved.is_relative_to(root.resolve()) and resolved.is_file()
    for path in record.get('artifacts', []) if isinstance(record.get('artifacts'), list) else []:
        if not artifact(path):
            errors.append(f'artifacts: missing or outside root: {path}')
    valid_operations = []
    for op in operations:
        if not isinstance(op, dict) or not isinstance(op.get('operation'), str) or not op['operation'].strip() or op.get('tool') not in record.get('exposedTools', []) or not artifact(op.get('evidence')):
            errors.append('successfulOperations: requires operation, exposed tool and existing evidence')
        else:
            valid_operations.append(op['operation'])
    if status in ('pass', 'reduced-pass'):
        if not record.get('artifacts'):
            errors.append('artifacts: passing observation requires artifacts')
        if permissions.get('execution') != 'granted' or permissions.get('writes') != 'granted':
            errors.append('permissions: passing execution requires granted execution and writes')
        if execution in ('unavailable', 'not-run'):
            errors.append('execution: unavailable execution must be blocked or not-run')
        if execution == 'workers' and 'spawn' not in valid_operations:
            errors.append('execution: worker claim requires successful spawn operation')
        if execution == 'sequential' and status != 'reduced-pass':
            errors.append('status: sequential execution is reduced-pass, never full pass')
    if 'external-write' in valid_operations:
        if permissions.get('externalActions') != 'granted' or not record.get('priorActionIdentities'):
            errors.append('external-write: explicit permission and prior action identities required')
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--commit', required=True)
    args = parser.parse_args()
    errors = []
    if not re.fullmatch(r'[0-9a-f]{40}', args.commit):
        errors.append('--commit: expected full lowercase Git SHA')
    for path in sorted((args.root / 'docs/parity/evidence').rglob('*.json')):
        try:
            records = json.loads(path.read_text())
            records = records if isinstance(records, list) else [records]
            for index, record in enumerate(records):
                errors.extend(f'{path}[{index}]: {error}' for error in validate_evidence(record, args.commit, args.root))
        except (OSError, ValueError) as exc:
            errors.append(f'{path}: {exc}')
    for error in errors:
        print(error)
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
