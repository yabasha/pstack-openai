import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

from tools.validate_evidence import validate_evidence


class EvidenceTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(dir=Path(__file__).resolve().parents[1])
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        (self.root / 'result.txt').write_text('observed')
        registry = json.loads((Path(__file__).resolve().parents[1] / 'docs/parity/case-registry.json').read_text())
        directory = self.root / 'docs/parity'
        directory.mkdir(parents=True)
        (directory / 'case-registry.json').write_text(json.dumps(registry))
        self.record = dict(caseId='absent-workers', sourcePaths=['pstack/commands/poteto.md'],
            packageVersion='0.15.15', packageCommit='a'*40, host='codex', hostMode='test',
            date='2026-10-07', documentedCapabilities=[], exposedTools=['observed.spawn'],
            successfulOperations=[dict(operation='spawn', tool='observed.spawn', evidence='result.txt')],
            permissions=dict(execution='granted', writes='granted', externalActions='denied'),
            input='fixture', observedOutput='fixture observation', artifacts=['result.txt'],
            status='pass', limits=[], execution='workers', models=dict(requested='unknown', actual='unknown'),
            priorActionIdentities=[])
        self.record['sourcePaths'] = next(entry['sourcePaths'] for entry in registry['entries']
                                          if entry['caseId'] == 'absent-workers')
        self.record['successfulOperations'] += [dict(operation=x,tool='observed.spawn',evidence='result.txt') for x in ('inspect-result','read')]

    def check(self):
        return validate_evidence(self.record, 'a'*40, self.root)

    def test_stale_commit_rejected(self):
        self.record['packageCommit'] = 'b'*40
        self.assertTrue(self.check())

    def test_missing_artifact_rejected(self):
        self.record['artifacts'] = ['missing.txt']
        self.assertTrue(self.check())

    def test_reduced_is_not_full(self):
        self.record['execution'] = 'sequential'
        self.record['limits'] = ['external actions denied']
        self.assertTrue(self.check())
        self.record['status'] = 'reduced-pass'
        self.assertEqual([], self.check())

    def test_claimed_worker_without_operation(self):
        self.record['successfulOperations'] = []
        self.assertTrue(self.check())

    def test_blocked_denial_preserved(self):
        self.record.update(status='blocked', execution='unavailable', artifacts=[], successfulOperations=[])
        self.record['permissions']['execution'] = 'denied'
        self.assertEqual([], self.check())

    def test_pass_requires_permissions_and_artifacts(self):
        self.record['successfulOperations'].append(dict(operation='isolated-write',tool='observed.spawn',evidence='result.txt'))
        self.record['permissions']['writes'] = 'unknown'
        self.assertTrue(self.check())
        self.record['permissions']['writes'] = 'granted'
        self.record['artifacts'] = []
        self.assertTrue(self.check())

    def test_unexposed_tool_and_escaping_artifact_rejected(self):
        self.record['successfulOperations'][0]['tool'] = 'imaginary.spawn'
        self.record['artifacts'] = ['../outside']
        self.assertTrue(self.check())

    def test_valid_worker_fixture(self):
        self.assertEqual([], self.check())

    def test_malformed_record_rejected(self):
        self.record['exposedTools'] = None
        self.assertTrue(self.check())

    def test_registry_rejects_wrong_scope_and_structural_host_claim(self):
        directory = self.root / 'docs/parity'
        directory.mkdir(parents=True, exist_ok=True)
        entry = dict(caseId='absent-workers', sourcePaths=['other'], requiredHosts=['codex'], structuralOnly=False,
                     requiredObservations={'pass':['spawn','inspect-result'],'reduced-pass':['read']})
        path = directory / 'case-registry.json'
        path.write_text(json.dumps(dict(entries=[entry])))
        self.assertTrue(self.check())
        entry.pop('requiredHosts')
        entry['structuralOnly'] = False
        path.write_text(json.dumps(dict(entries=[entry])))
        self.assertTrue(self.check())
        entry['sourcePaths'] = self.record['sourcePaths']
        entry['requiredHosts'] = ['codex']
        entry['structuralOnly'] = True
        path.write_text(json.dumps(dict(entries=[entry])))
        self.assertTrue(self.check())

    def test_missing_registry_unknown_case_and_nonfile_registry_rejected(self):
        self.record['caseId'] = 'unknown-case'
        self.assertTrue(self.check())
        self.record['caseId'] = 'absent-workers'
        path = self.root / 'docs/parity/case-registry.json'
        path.unlink()
        self.assertTrue(self.check())
        path.mkdir()
        self.assertTrue(self.check())

    def test_worker_result_inspection_required(self):
        self.record['successfulOperations'] = [x for x in self.record['successfulOperations'] if x['operation'] != 'inspect-result']
        self.assertTrue(self.check())

    def test_case_specific_full_observations_required(self):
        registry = json.loads((self.root / 'docs/parity/case-registry.json').read_text())
        for entry in registry['entries']:
            self.record['caseId'] = entry['caseId']
            self.record['sourcePaths'] = entry['sourcePaths']
            if entry['structuralOnly']:
                self.assertTrue(self.check(), entry['caseId'])
                continue
            self.record['permissions']['externalActions'] = 'granted'
            self.record['priorActionIdentities'] = ['action-1']
            self.record['execution'] = 'workers' if 'workers' in entry['executionModes']['pass'] else 'direct'
            operations = set(entry['requiredObservations']['pass'])
            if self.record['execution'] == 'workers':
                operations |= {'spawn','inspect-result'}
            native = operations & {'supplied-input','response','review-outcome'}
            self.record['nativeObservations'] = [dict(observation=x,evidence='result.txt',reviewedBy='synthetic-reviewer') for x in native]
            self.record['successfulOperations'] = [dict(operation=x,tool='observed.spawn',evidence='result.txt') for x in operations-native]
            if entry.get('requiredMethod'):
                from tests.evidence_fixtures import method_fixture
                method_fixture(self.root, self.record, entry['requiredMethod'])
            self.assertEqual([],self.check(),entry['caseId'])
            for omitted in entry['requiredObservations']['pass']:
                with self.subTest(case=entry['caseId'], omitted=omitted):
                    original = self.record['successfulOperations']
                    native_original = self.record.get('nativeObservations', [])
                    self.record['nativeObservations'] = [x for x in native_original if x['observation'] != omitted]
                    self.record['successfulOperations'] = [x for x in original if x['operation'] != omitted]
                    self.assertTrue(self.check())
                    self.record['nativeObservations'] = native_original
                    self.record['successfulOperations'] = original

    def test_sharpen_rewrite_pass_needs_no_execution_or_write_permission(self):
        registry = json.loads((self.root / 'docs/parity/case-registry.json').read_text())
        entry = next(e for e in registry['entries'] if e['caseId'] == 'task-sharpen')
        self.record.update(caseId=entry['caseId'], sourcePaths=entry['sourcePaths'],
                           execution='direct', successfulOperations=[],
                           permissions=dict(execution='denied', writes='denied', externalActions='denied'),
                           nativeObservations=[dict(observation=x, evidence='result.txt', reviewedBy='synthetic-reviewer')
                                               for x in ('supplied-input','response','review-outcome')])
        for host in ('chatgpt','codex'):
            with self.subTest(host=host):
                self.record['host'] = host
                self.assertEqual([], self.check())
        self.record['execution'] = 'workers'
        self.assertTrue(self.check())

    def test_read_only_reduced_with_denied_writes(self):
        self.record.update(caseId='denied-writes', status='reduced-pass',execution='sequential',limits=['writes denied; read-only findings'])
        self.record['permissions']['writes'] = 'denied'
        self.record['successfulOperations'] = [dict(operation='read',tool='observed.spawn',evidence='result.txt')]
        self.assertEqual([],self.check())

    def test_external_recovery_requires_observations_permission_and_identity(self):
        self.record['caseId'] = 'interrupted-external-write'
        self.record['successfulOperations'] += [dict(operation=x,tool='observed.spawn',evidence='result.txt') for x in ('inspect-prior-action','inspect-destination','safe-recovery')]
        self.assertTrue(self.check())
        self.record['permissions']['externalActions'] = 'granted'
        self.assertTrue(self.check())
        self.record['priorActionIdentities'] = ['action-1']
        self.assertEqual([], self.check())
        for omitted in ('inspect-prior-action','inspect-destination','safe-recovery'):
            with self.subTest(omitted=omitted):
                original = self.record['successfulOperations']
                self.record['successfulOperations'] = [x for x in original if x['operation'] != omitted]
                self.assertTrue(self.check())
                self.record['successfulOperations'] = original

    def test_external_write_requires_prior_identity(self):
        self.record['successfulOperations'].append(dict(operation='external-write',tool='observed.spawn',evidence='result.txt'))
        self.assertTrue(self.check())
        self.record['permissions']['externalActions'] = 'granted'
        self.record['priorActionIdentities'] = ['action-1']
        self.assertEqual([], self.check())

    def test_cli_invalid_and_valid(self):
        evidence = self.root / 'docs/parity/evidence'
        evidence.mkdir(parents=True)
        record_path = evidence / 'fixture.json'
        record_path.write_text(json.dumps(self.record))
        command = [sys.executable, '-B', str(Path(__file__).resolve().parents[1] / 'tools/validate_evidence.py'),
                   '--root', str(self.root), '--commit', 'a'*40]
        good = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(0, good.returncode, good.stdout)
        self.record['packageCommit'] = 'b'*40
        record_path.write_text(json.dumps(self.record))
        bad = subprocess.run(command, capture_output=True, text=True)
        self.assertEqual(1, bad.returncode)
        self.assertIn('packageCommit', bad.stdout)

class DirectAndMethodTests(unittest.TestCase):
    setUp = EvidenceTests.setUp
    check = EvidenceTests.check
    def select(self, case):
        registry = json.loads((self.root/'docs/parity/case-registry.json').read_text())
        entry = next(e for e in registry['entries'] if e['caseId'] == case)
        self.record.update(caseId=case, sourcePaths=entry['sourcePaths'])
        return entry

    def test_direct_completion_without_execution_or_workers(self):
        for case in ('plain-restate', 'dense-doc', 'prose-rewrite'):
            self.select(case)
            self.record.update(execution='direct', successfulOperations=[], exposedTools=[],
                nativeObservations=[dict(observation=o,evidence='result.txt',reviewedBy='synthetic-reviewer') for o in ('supplied-input','response','review-outcome')])
            self.record['permissions']['execution'] = 'unavailable'
            self.record['permissions']['writes'] = 'denied'
            self.assertEqual([], self.check(), case)

    def test_direct_discovery_requires_complete_operations(self):
        self.select('package-discovery')
        self.record.update(execution='direct', successfulOperations=[dict(operation=o,tool='observed.spawn',evidence='result.txt') for o in ('discover-package','enumerate-skills','inspect-installed-copy')])
        self.record['permissions']['execution'] = 'unavailable'
        self.assertEqual([], self.check())
        self.record['successfulOperations'].pop()
        self.assertTrue(self.check())

    def test_direct_cannot_bypass_required_workers(self):
        self.select('candidate-cross-review')
        self.record['execution'] = 'direct'
        self.assertTrue(self.check())

    def test_generic_workers_do_not_prove_methods(self):
        for case in ('candidate-cross-review','partition-and-race'):
            self.select(case)
            self.assertTrue(self.check(), case)

    def test_structured_arena_and_swarm_relationships(self):
        from tests.evidence_fixtures import method_fixture
        import copy
        for case, kind in [('candidate-cross-review','arena'),('partition-and-race','swarm')]:
            self.select(case)
            self.record['successfulOperations'] = [dict(operation=o,tool='observed.spawn',evidence='result.txt') for o in ('read','inspect-result')]
            receipt = method_fixture(self.root,self.record,kind)
            self.assertEqual([], self.check(), kind)
            bad = [lambda r: r['assignments'][0].update(inputRevision='b'*40),
                   lambda r: r['assignments'][0].update(resultRevision='d'*40),
                   lambda r: r['assignments'][0].update(resultMethod={'sampleCount':99}),
                   lambda r: r['assignments'][0].update(outputSha256='0'*64),
                   lambda r: r['assignments'][0].pop('resultMethod'),
                   lambda r: r['assignments'][0].update(outputOwner='someone-else'),
                   lambda r: r['assignments'][1].update(outputPath=r['assignments'][0]['outputPath'])]
            if kind == 'arena':
                bad += [lambda r: r.update(candidates=['assignment-0']),
                        lambda r: r['assignments'][2].update(workerId=r['assignments'][0]['workerId']),
                        lambda r: r['assignments'][2].update(startedOrder=5)]
            else:
                bad += [lambda r: r['partition']['results'].pop('left'),
                        lambda r: r.update(quarantined=[]),
                        lambda r: r['race'].update(winner='assignment-3'),
                        lambda r: r.update(failureExercises=[]),
                        lambda r: r['failureExercises'].pop(1),
                        lambda r: r['failureExercises'][1].update(attempt=2)]
            for mutate in bad:
                broken = copy.deepcopy(receipt); mutate(broken)
                (self.root/self.record['methodReceipt']).write_text(json.dumps(broken))
                self.assertTrue(self.check(), (kind,broken))
            (self.root/self.record['methodReceipt']).write_text(json.dumps(receipt))
            self.record['permissions']['writes'] = 'denied'
            self.assertTrue(self.check())
            self.record['permissions']['writes'] = 'granted'

    def test_cancelled_losing_racer_remains_valid_participant(self):
        from tests.evidence_fixtures import method_fixture
        import copy
        self.select('partition-and-race')
        receipt = method_fixture(self.root, self.record, 'swarm')
        receipt['assignments'][4]['role'] = 'race'
        receipt['race']['assignments'].append('assignment-4')
        (self.root / self.record['methodReceipt']).write_text(json.dumps(receipt))
        self.assertEqual([], self.check())
        for name, mutate in [
                ('cancelled winner', lambda r: r['race'].update(winner='assignment-4')),
                ('cancelled partition output', lambda r: r['partition']['results'].update(left='assignment-4')),
                ('missing quarantine', lambda r: r.update(quarantined=[])),
                ('incomplete rank-all', lambda r: r['race'].update(rule='rank-all'))]:
            with self.subTest(name=name):
                broken = copy.deepcopy(receipt)
                mutate(broken)
                (self.root / self.record['methodReceipt']).write_text(json.dumps(broken))
                self.assertTrue(self.check())

    def test_arena_requires_judge_rubric_delivery(self):
        from tests.evidence_fixtures import method_fixture
        import copy
        self.select('candidate-cross-review')
        receipt = method_fixture(self.root, self.record, 'arena')
        for name, mutate in [
                ('no delivery', lambda a: a.update(rubricProvided=False)),
                ('absent delivery', lambda a: a.pop('rubricProvided')),
                ('non-Boolean delivery', lambda a: a.update(rubricProvided='true'))]:
            with self.subTest(name=name):
                broken = copy.deepcopy(receipt)
                judge = next(a for a in broken['assignments'] if a['id'] == broken['judge'])
                mutate(judge)
                (self.root / self.record['methodReceipt']).write_text(json.dumps(broken))
                self.assertTrue(self.check())
        judge = next(a for a in receipt['assignments'] if a['id'] == receipt['judge'])
        self.assertIs(True, judge['rubricProvided'])
        candidates = [a for a in receipt['assignments'] if a['id'] in receipt['candidates']]
        self.assertTrue(all(a['rubricProvided'] is False for a in candidates))
        (self.root / self.record['methodReceipt']).write_text(json.dumps(receipt))
        self.assertEqual([], self.check())
        candidates[0]['rubricProvided'] = True
        (self.root / self.record['methodReceipt']).write_text(json.dumps(receipt))
        self.assertTrue(self.check())

    def test_partition_only_walkthrough_and_assignment_operation_binding(self):
        from tests.evidence_fixtures import method_fixture
        self.select('swarm-walkthrough')
        receipt=method_fixture(self.root,self.record,'swarm-partition')
        self.assertEqual(3,len(receipt['partition']['requiredSlices']))
        (self.root/self.record['methodReceipt']).write_text(json.dumps(receipt))
        self.assertEqual([],self.check())
        broken=json.loads(json.dumps(receipt));broken['partition']['requiredSlices'].pop();broken['partition']['results'].pop('third')
        (self.root/self.record['methodReceipt']).write_text(json.dumps(broken))
        self.assertTrue(self.check())
        (self.root/self.record['methodReceipt']).write_text(json.dumps(receipt))
        self.record['successfulOperations']=[o for o in self.record['successfulOperations'] if not (o.get('assignmentId')=='assignment-0' and o['operation']=='isolated-write')]
        self.assertTrue(self.check())

    def test_native_response_cannot_be_fabricated_as_a_tool_operation(self):
        self.select('plain-restate')
        self.record.update(execution='direct',successfulOperations=[dict(operation=o,tool='observed.spawn',evidence='result.txt') for o in ('supplied-input','response','review-outcome')])
        self.assertTrue(any('native text' in e for e in self.check()))
