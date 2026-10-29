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
    entry = None
    if registry_path.is_file():
        try:
            entries = json.loads(registry_path.read_text())['entries']
            entry = next((item for item in entries if item['caseId'] == record['caseId']), None)
            if entry is None or entry.get('structuralOnly') or record['host'] not in entry['requiredHosts']:
                errors.append('caseId: no applicable behavioral registry entry for host')
            elif set(record['sourcePaths']) != set(entry['sourcePaths']):
                errors.append('sourcePaths: must match registered case scope')
            if entry is not None:
                requirements = entry.get('requiredObservations')
                if not isinstance(requirements, dict) or any(not isinstance(requirements.get(status), list) or not requirements[status] or any(not isinstance(x, str) or not x.strip() for x in requirements[status]) for status in ('pass', 'reduced-pass')):
                    errors.append('case registry: pass and reduced-pass observations required')
                    entry = None
        except (OSError, ValueError, KeyError, TypeError):
            entry = None
            errors.append('case registry: malformed applicability artifact')
    else:
        errors.append('case registry: required file missing or not a file')
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
    if execution not in ('direct', 'workers', 'sequential', 'unavailable', 'not-run'):
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
        if op.get('operation') in ('supplied-input', 'response', 'review-outcome'):
            errors.append('successfulOperations: native text observations are not callable tools')
            continue
        if not isinstance(op, dict) or not isinstance(op.get('operation'), str) or not op['operation'].strip() or op.get('tool') not in record.get('exposedTools', []) or not artifact(op.get('evidence')):
            errors.append('successfulOperations: requires operation, exposed tool and existing evidence')
        else:
            valid_operations.append(op['operation'])
    if status in ('pass', 'reduced-pass'):
        if not record.get('artifacts'):
            errors.append('artifacts: passing observation requires artifacts')
        for observation in record.get('nativeObservations', []):
            if observation['evidence'] not in record['artifacts'] or not artifact(observation['evidence']):
                errors.append('nativeObservations: existing listed evidence required')
            else:
                valid_operations.append(observation['observation'])
        if entry is not None:
            if execution not in entry.get('executionModes', {}).get(status, []):
                errors.append('execution: mode does not satisfy this case method')
            for permission in entry.get('requiredPermissions', {}).get(status, []):
                if permissions.get(permission) != 'granted':
                    errors.append('permissions: required ' + permission)
            if status == 'pass' and entry.get('requiredMethod'):
                errors += validate_method(record, entry['requiredMethod'], root, artifact, entry.get('requiredSliceCount'))
        if set(valid_operations) & {'spawn', 'execution', 'compile-proof', 'stop'} and permissions.get('execution') != 'granted':
            errors.append('permissions: performed execution requires granted execution')
        if entry is not None:
            for operation in entry['requiredObservations'][status]:
                if operation not in valid_operations:
                    errors.append(f'{record["caseId"]}: missing required observation {operation}')
        if status == 'reduced-pass' and any(permissions.get(k) in ('denied', 'unavailable') for k in ('writes', 'externalActions')) and not record['limits']:
            errors.append('limits: reduced outcome must preserve denied or unavailable permissions')
        if execution in ('unavailable', 'not-run'):
            errors.append('execution: unavailable execution must be blocked or not-run')
        if execution == 'workers':
            for operation in ('spawn', 'inspect-result'):
                if operation not in valid_operations:
                    errors.append(f'execution: worker claim requires successful {operation} operation')
        if execution == 'sequential' and status != 'reduced-pass':
            errors.append('status: sequential execution is reduced-pass, never full pass')
    if set(valid_operations) & {'isolated-write', 'persistence'} and permissions.get('writes') != 'granted':
        errors.append('permissions: performed writes require granted writes')
    if set(valid_operations) & {'external-write', 'safe-recovery'} or (record['caseId'] == 'interrupted-external-write' and status == 'pass'):
        if permissions.get('externalActions') != 'granted' or not record.get('priorActionIdentities'):
            errors.append('external recovery: explicit permission and prior action identities required')
    return errors


def validate_method(record, kind, root, artifact, required_slice_count=None):
    """Check observable method relationships, never the quality of a judgment."""
    errors = []
    require_race = kind == 'swarm'
    kind = 'swarm' if kind == 'swarm-partition' else kind
    def require(condition, detail):
        if not condition:
            errors.append('method receipt: ' + detail)
    def inspected(path):
        return path in record['artifacts'] and artifact(path)
    path = record.get('methodReceipt')
    if not inspected(path):
        return ['method receipt: existing listed receipt required']
    operations = record['successfulOperations']
    require(any(o['operation'] == 'inspect-method' and o['evidence'] == path for o in operations), 'receipt must be inspected')
    try:
        receipt = json.loads((root / path).read_text())
        common = {'schemaVersion', 'kind', 'inputRevision', 'assignments', 'reviewArtifact', 'reviewedBy', 'declaredOrder'}
        extra = {'candidates', 'judge', 'rubricArtifact', 'synthesis', 'modelFamilyEvidence'} if kind == 'arena' else {'partition', 'race', 'cancelled', 'quarantined', 'failureExercises'}
        require(set(receipt) == common | extra and receipt['schemaVersion'] == 1 and receipt['kind'] == kind, 'invalid method shape or identity')
        require(re.fullmatch('[0-9a-f]{40}', record.get('inputRevision', '')) is not None and receipt['inputRevision'] == record.get('inputRevision'), 'exact assigned input revision required')
        require(inspected(receipt['reviewArtifact']) and bool(receipt['reviewedBy'].strip()), 'qualitative outcome needs an explicit reviewed artifact')
        assignments = receipt['assignments']
        require(isinstance(assignments, list) and len(assignments) >= 2, 'independent assignments required')
        by_id, workers, outputs = {}, set(), []
        for a in assignments:
            keys = {'id','workerId','inputRevision','outputOwner','outputPath','role','status','startedOrder','completedOrder','requestedModel','actualModel','retryCount','method','taskArtifact','rubricProvided','resultRevision','resultMethod','outputSha256'}
            require(set(a) == keys, 'assignment fields differ from contract')
            require(a['id'] not in by_id and a['workerId'] not in workers, 'assignment and worker identities must be distinct')
            by_id[a['id']] = a; workers.add(a['workerId'])
            require(a['inputRevision'] == receipt['inputRevision'], 'assignment revision mismatch')
            require(a['outputOwner'] == a['workerId'], 'output owner differs from assigned worker')
            require(a['resultRevision'] == a['inputRevision'] and a['resultMethod'] == a['method'], 'result revision or method differs from assignment')
            output = (root / a['outputPath']).resolve()
            require(artifact(a['outputPath']) and __import__('hashlib').sha256(output.read_bytes()).hexdigest() == a['outputSha256'], 'output bytes differ from inspected result')
            require(inspected(a['outputPath']) and all(output != prior and not output.is_relative_to(prior.parent) and not prior.is_relative_to(output.parent) for prior in outputs), 'output ownership overlaps or artifact missing')
            outputs.append(output)
            require(all(type(a[k]) is int for k in ('startedOrder','completedOrder','retryCount')) and type(receipt['declaredOrder']) is int, 'orders and retry count must be integers')
            require(receipt['declaredOrder'] < a['startedOrder'] < a['completedOrder'] and a['retryCount'] in (0,1), 'invalid phase order or retry budget')
            require(a['status'] in ('completed','cancelled','blocked','failed'), 'invalid terminal state')
            require(all(isinstance(a[k], str) and a[k].strip() for k in ('id','workerId','role','requestedModel','actualModel')), 'assignment identity, role and observed-or-unknown models required')
            require(inspected(a['taskArtifact']), 'assignment task artifact must be inspected')
            method = a['method']
            require(set(method) == {'sampleCount','sampleDefinition','order'} and type(method['sampleCount']) is int and method['sampleCount'] > 0 and bool(method['sampleDefinition'].strip()) and bool(method['order'].strip()), 'exact measurement method required')
            needed = ['spawn', 'inspect-result'] + ([] if a['role'] == 'judge' else ['isolated-write'])
            if a['status'] == 'cancelled': needed += ['stop','inspect-terminal','quarantine-artifacts']
            for op in needed:
                require(any(o.get('assignmentId') == a['id'] and o['operation'] == op and o['evidence'] == a['outputPath'] for o in operations), a['id'] + ': missing bound ' + op)
        require(record['permissions']['execution'] == 'granted' and record['permissions']['writes'] == 'granted', 'worker execution and output writes require grants')
        if kind == 'arena':
            ids = receipt['candidates']
            require(len(ids) >= 2 and len(set(ids)) == len(ids), 'at least two distinct candidates required')
            candidates = [by_id[i] for i in ids]
            judge = by_id[receipt['judge']]
            require(judge['id'] not in ids and judge['role'] == 'judge' and judge['status'] == 'completed', 'fresh completed judge required')
            require(judge['rubricProvided'] is True, 'judge must receive the rubric')
            families = receipt['modelFamilyEvidence']
            require(set(families) == {'parentModel', 'parentFamily', 'judgeModel', 'judgeFamily', 'evidence'}, 'invalid model family evidence shape')
            require(inspected(families['evidence']), 'observed model family evidence must be inspected')
            unknown = {'unknown', 'unavailable', 'auto', 'inherit-parent', ''}
            require(all(isinstance(families[k], str) and families[k].strip().lower() not in unknown for k in ('parentModel', 'parentFamily', 'judgeModel', 'judgeFamily')), 'observed parent and judge model families required')
            require(judge['requestedModel'].strip().lower() not in {'auto', 'inherit-parent'}, 'inherited aliases never judge')
            require(families['judgeModel'] == judge['actualModel'], 'judge family evidence must bind its actual model')
            require(families['parentModel'].strip().lower() != families['judgeModel'].strip().lower() and families['parentFamily'].strip().lower() != families['judgeFamily'].strip().lower(), 'judge must differ from parent model family')
            require(all(a['role'] == 'candidate' and a['status'] == 'completed' and a['rubricProvided'] is False for a in candidates), 'completed candidates must not receive the rubric')
            require(len({a['taskArtifact'] for a in candidates}) == 1, 'candidates need the same task artifact')
            require(all(a['completedOrder'] < judge['startedOrder'] for a in candidates), 'judge started before candidates completed')
            require(inspected(receipt['rubricArtifact']), 'rubric evidence missing')
            synthesis = receipt['synthesis']
            require(set(synthesis) == {'order','inspectedCandidates','artifact','verificationArtifact'}, 'invalid synthesis shape')
            require(set(synthesis['inspectedCandidates']) == set(ids) and len(synthesis['inspectedCandidates']) == len(ids), 'parent must inspect every candidate')
            require(type(synthesis['order']) is int and synthesis['order'] > judge['completedOrder'] and inspected(synthesis['artifact']) and inspected(synthesis['verificationArtifact']), 'inspected synthesis and verification must follow judgment')
        else:
            partition, race = receipt['partition'], receipt['race']
            require(set(partition) == {'requiredSlices','results','gaps'}, 'partition shape invalid')
            slices = partition['requiredSlices']
            if required_slice_count is not None:
                require(len(slices) == required_slice_count, 'case requires exact declared slice count')
            require(bool(slices) and len(slices) == len(set(slices)) and set(partition['results']) == set(slices) and not partition['gaps'], 'full coverage needs every required slice without gaps')
            require(len(set(partition['results'].values())) == len(slices), 'each slice needs its assigned output')
            require(all(by_id[i]['role'] == 'partition' and by_id[i]['status'] == 'completed' for i in partition['results'].values()), 'required slices must complete')
            if race is None and not require_race:
                require(not receipt['cancelled'] and not receipt['quarantined'] and not receipt['failureExercises'], 'partition-only receipt cannot hide cancellation or failure exercises')
                return errors
            require(set(race) == {'rule','assignments','winner','ruleArtifact'}, 'race shape invalid')
            racers = [by_id[i] for i in race['assignments']]
            require(len(racers) >= 2 and len({a['id'] for a in racers}) == len(racers) and all(a['role'] == 'race' for a in racers), 'race needs distinct competing assignments')
            require(race['rule'] in ('first-pass','rank-all','best-of') and inspected(race['ruleArtifact']), 'declared race rule and inspected selection required')
            survivors = [a for a in racers if a['status'] == 'completed']
            require(bool(survivors) and race['winner'] in {a['id'] for a in survivors}, 'winner must be an inspected survivor')
            if race['rule'] == 'first-pass' and survivors:
                require(race['winner'] == min(survivors, key=lambda a: a['completedOrder'])['id'], 'first-pass winner violates completion order')
            if race['rule'] == 'rank-all': require(len(survivors) == len(racers), 'rank-all requires all race results')
            cancelled = {a['id'] for a in assignments if a['status'] == 'cancelled'}
            require(bool(cancelled) and set(receipt['cancelled']) == cancelled and set(receipt['quarantined']) == cancelled, 'cancellation exercise requires observed stop, terminal inspection and quarantine')
            exercises = receipt['failureExercises']
            rejected, dropouts, rejected_paths = {}, set(), set()
            require(isinstance(exercises,list), 'failure exercise records required')
            for event in exercises:
                require(set(event) == {'assignmentId','kind','attempt','order','reason','evidence'}, 'failure exercise shape invalid')
                a = by_id[event['assignmentId']]
                require(type(event['attempt']) is int and event['attempt'] in (0,1) and type(event['order']) is int and a['startedOrder'] < event['order'] <= a['completedOrder'], 'invalid failure attempt or order')
                require(inspected(event['evidence']) and isinstance(event['reason'],str) and bool(event['reason'].strip()), 'failure exercise needs inspected evidence and reason')
                operation='inspect-rejected-result' if event['kind']=='rejected' else 'inspect-terminal'
                require(any(o.get('assignmentId')==a['id'] and o['operation']==operation and o['evidence']==event['evidence'] for o in operations), 'failure exercise lacks bound inspection')
                if event['kind']=='rejected':
                    require(event['reason'] in ('missing-revision','missing-method'), 'rejection must identify missing required evidence')
                    rejected_path = (root / event['evidence']).resolve()
                    require(rejected_path not in rejected_paths, 'rejected attempts must use distinct resolved artifacts')
                    require(rejected_path not in outputs, 'rejected attempt cannot alias a final output')
                    rejected_paths.add(rejected_path)
                    rejected.setdefault(a['id'],[]).append(event)
                elif event['kind']=='dropout':
                    require(a['status'] in ('failed','blocked') and event['attempt']==a['retryCount'], 'dropout must have a non-success terminal result')
                    dropouts.add(a['id'])
                else: require(False,'unknown failure exercise kind')
            require(bool(rejected) and bool(dropouts), 'combined case requires rejected evidence, exhausted retry and dropout exercises')
            require(not set(rejected) & dropouts, 'dropout assignment must be separate from rejected assignments')
            for identity, events in rejected.items():
                require([e['attempt'] for e in events]==[0,1] and events[0]['order']<events[1]['order'] and by_id[identity]['retryCount']==1 and by_id[identity]['status'] in ('failed','blocked'), 'second invalid result exhausts the one retry and must remain a gap')
            used = set(partition['results'].values()) | {race['winner']}
            require(not set(partition['results'].values()) & (set(rejected)|dropouts), 'failed exercise cannot satisfy a required slice')
            require(not used & cancelled, 'cancelled output cannot be integrated')
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        errors.append('method receipt: malformed or incomplete structured evidence')
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
