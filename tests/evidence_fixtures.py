"""Synthetic method receipts. These exercise validation, never host support."""
import json
from pathlib import Path


def method_fixture(root, record, kind):
    partition_only = kind == 'swarm-partition'
    kind = 'swarm' if partition_only else kind
    assignments = []
    roles = ['candidate','candidate','judge'] if kind=='arena' else ['partition']*3 if partition_only else ['partition','partition','race','race','cancelled','invalid','dropout']
    for i, role in enumerate(roles):
        worker = f'synthetic-worker-{i}'
        output = f'outputs/{worker}/result.txt'
        target = root / output
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text('SYNTHETIC: reviewed output for validator fixture only')
        a = dict(id=f'assignment-{i}', workerId=worker, inputRevision='c'*40,
                 outputOwner=worker, outputPath=output, role=role, status='cancelled' if role == 'cancelled' else 'failed' if role in ('invalid','dropout') else 'completed',
                 startedOrder=10+i if role != 'judge' else 30, completedOrder=20+i if role != 'judge' else 40,
                 requestedModel='inherit-parent', actualModel='unknown', retryCount=1 if role=='invalid' else 0,
                 method=dict(sampleCount=2, sampleDefinition='two fixed synthetic inputs', order='input order'),
                 taskArtifact='result.txt', rubricProvided=role == 'judge')
        a.update(resultRevision=a['inputRevision'],resultMethod=dict(a['method']),outputSha256=__import__('hashlib').sha256(target.read_bytes()).hexdigest())
        assignments.append(a)
        record['artifacts'].append(output)
        ops = ['spawn', 'inspect-result'] + ([] if role == 'judge' else ['isolated-write'])
        if role == 'cancelled': ops += ['stop', 'inspect-terminal', 'quarantine-artifacts']
        if role=='dropout': ops += ['inspect-terminal']
        for op in ops:
            record['successfulOperations'].append(dict(operation=op, tool='observed.spawn', evidence=output, assignmentId=a['id']))
    receipt = dict(schemaVersion=1, kind=kind, inputRevision='c'*40, assignments=assignments,
                   reviewArtifact='result.txt', reviewedBy='synthetic-reviewer', declaredOrder=1)
    if kind == 'arena':
        receipt.update(candidates=['assignment-0', 'assignment-1'], judge='assignment-2', rubricArtifact='result.txt',
                       synthesis=dict(order=50, inspectedCandidates=['assignment-0', 'assignment-1'], artifact='result.txt', verificationArtifact='result.txt'))
    elif not partition_only:
        failures = []
        for attempt in (0, 1):
            output = f'captures/assignment-5/attempt-{attempt}.txt'
            target = root / output
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text('SYNTHETIC raw return: required method reporting omitted')
            record['artifacts'].append(output)
            record['successfulOperations'].append(dict(operation='inspect-rejected-result', tool='observed.spawn', evidence=output, assignmentId='assignment-5'))
            failures.append(dict(assignmentId='assignment-5',kind='rejected',attempt=attempt,order=17+attempt,reason='missing-method',evidence=output))
        receipt.update(partition=dict(requiredSlices=['left','right'], results={'left':'assignment-0','right':'assignment-1'}, gaps=[]),
                       race=dict(rule='first-pass', assignments=['assignment-2','assignment-3'], winner='assignment-2', ruleArtifact='result.txt'),
                       cancelled=['assignment-4'], quarantined=['assignment-4'],
                       failureExercises=failures+[dict(assignmentId='assignment-6',kind='dropout',attempt=0,order=19,reason='worker failed',evidence=assignments[6]['outputPath'])])
    if partition_only:
        receipt.update(partition=dict(requiredSlices=['first','second','third'],results={name:f'assignment-{i}' for i,name in enumerate(['first','second','third'])},gaps=[]),race=None,cancelled=[],quarantined=[],failureExercises=[])
    path = f'{kind}-receipt.txt'
    (root / path).write_text(json.dumps(receipt))
    record.update(inputRevision='c'*40, methodReceipt=path)
    record['artifacts'].append(path)
    record['successfulOperations'].append(dict(operation='inspect-method', tool='observed.spawn', evidence=path))
    return receipt
