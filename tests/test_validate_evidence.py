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
        self.record['sourcePaths'] = registry['entries'][0]['sourcePaths']
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
            self.record['permissions']['externalActions'] = 'granted'
            self.record['priorActionIdentities'] = ['action-1']
            operations = set(entry['requiredObservations']['pass']) | {'spawn','inspect-result'}
            self.record['successfulOperations'] = [dict(operation=x,tool='observed.spawn',evidence='result.txt') for x in operations]
            self.assertEqual([],self.check(),entry['caseId'])
            for omitted in entry['requiredObservations']['pass']:
                with self.subTest(case=entry['caseId'], omitted=omitted):
                    original = self.record['successfulOperations']
                    self.record['successfulOperations'] = [x for x in original if x['operation'] != omitted]
                    self.assertTrue(self.check())
                    self.record['successfulOperations'] = original

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
