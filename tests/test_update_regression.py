"""Fixture-only package rollback and candidate acceptance regressions."""
import hashlib
import json
from pathlib import Path
import shutil
import unittest
from unittest.mock import patch
from tests import test_upstream_apply as apply_fixtures
from tests import test_upstream_check as fixtures
from tools import sync_upstream as sync
from tools.validate_package import validate_package
from tools.validate_evidence import validate_evidence


class UpdateRegressionTests(unittest.TestCase):
    snapshot = apply_fixtures.UpstreamApplyTests.snapshot
    run_review = apply_fixtures.UpstreamApplyTests.run_review
    git_at = apply_fixtures.UpstreamApplyTests.git_at
    git = apply_fixtures.UpstreamApplyTests.git
    save_resolutions = apply_fixtures.UpstreamApplyTests.save_resolutions
    apply = apply_fixtures.UpstreamApplyTests.apply

    def setUp(self):
        apply_fixtures.UpstreamApplyTests.setUp(self)
        shutil.rmtree(self.review)
        for path in ("docs/parity/cases/schema.json",):
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes((self.package / path).read_bytes())
        (self.root / "tools").mkdir()
        (self.root / "tools/portable.py").write_bytes(b"# reviewed portable helper v1\n")
        inventory = json.loads((self.root / "docs/parity/inventory.json").read_bytes())
        for row in inventory:
            row["verification"] = {h: {"status":"not-run", "evidence":[]} for h in ("chatgpt", "codex")}
        (self.root / "docs/parity/inventory.json").write_text(json.dumps(inventory))
        self.git("add", ".", ":!.upstream")
        self.git("commit", "-qm", "fixture rollback release")
        self.release = self.git("rev-parse", "HEAD").strip()
        self.original_package = self.snapshot()
        self.proposed["docs/moved.md"] = self.proposed.pop("docs/file-2.md")
        del self.proposed["docs/file-1.md"]
        self.refresh_review()

    def refresh_review(self):
        if self.review.exists():
            shutil.rmtree(self.review)
        self.responses[sync.ARCHIVE + self.candidate] = fixtures.archive_bytes(self.proposed, self.candidate)
        self.responses[sync.API + "/git/trees/" + self.tree_sha + "?recursive=1"] = json.dumps({"sha": self.tree_sha, "truncated":False, "tree":[
            {"path":"pstack/" + p, "type":"blob", "mode":"100644", "sha":hashlib.sha1(b"blob " + str(len(d)).encode() + b"\0" + d).hexdigest()} for p,d in self.proposed.items()]}).encode()
        self.bundle = self.run_review("check")
        self.assertFalse(self.bundle["files"]["acceptanceReady"])
        self.review.rename(self.review.parent / ("checked-" + str(len(list(self.review.parent.iterdir())))))
        self.bundle = self.run_review("prepare")
        self.resolutions.update(packageCommit=self.bundle["packageCommit"], reviewSha256=fixtures.digest((self.review / "report.json").read_bytes()), entries=[])
        for e in self.bundle["files"]["added"] + self.bundle["files"]["removed"] + self.bundle["files"]["changed"]:
            action = "rename-reviewed" if e["path"] in ("docs/file-2.md", "docs/moved.md") else "delete-reviewed" if e["newSha256"] is None else "add-reviewed" if e["oldSha256"] is None else "adapt-manually"
            content = "sources/candidate/" + e["path"] if e["newSha256"] else None
            if e["path"] == self.leaf:
                action, content = "retain-adaptation", "sources/adapted/" + self.leaf
            self.resolutions["entries"].append(dict(**e, disposition=action, rationale="Reviewed fixture disposition and callers.", reviewedCallers=e["dependentCallers"], contentPath=content, reviewedSha256=fixtures.digest((self.review / content).read_bytes()) if content else None))
        self.save_resolutions()
        self.set_owner()

    def set_owner(self):
        admin = Path(self.git("rev-parse", "--absolute-git-dir").strip())
        (admin / "pstack-update-owner.json").write_text(json.dumps(dict(schemaVersion=1, owner=self.owner, worktree=str(self.root), packageCommit=self.git("rev-parse", "HEAD").strip())))

    def stage_candidate(self):
        self.apply()
        (self.root / "tools/portable.py").write_bytes(b"# reviewed portable helper v2\n")
        for p in ("personal.md", ".env", ".codex/settings.json"):
            (self.root / p).write_bytes(b"newer destination-only bytes\n")
        self.git("add", ".", ":!.upstream")
        self.git("commit", "-qm", "fixture staged candidate")
        self.set_owner()

    def ownership(self, release=None):
        return dict(schemaVersion=1, kind="pstack-rollback-ownership", release=release or self.release,
            packageCommit=self.git("rev-parse", "HEAD").strip(), runtimeState="no-runtime-state-migrations",
            ownedPaths=sorted((set(self.original_package) | set(self.snapshot())) - {".git", "personal.md", ".env", ".codex/settings.json"}),
            preservedPaths={p:"Destination-only private customization, outside package ownership." for p in ("personal.md", ".env", ".codex/settings.json")})

    def rollback(self, document=None, **kwargs):
        document = document or self.ownership()
        with patch.object(sync, "ARCHIVE_SHA256", self.baseline_hash):
            plan = sync.rollback_plan(self.root, document, owner=self.owner)
            return sync.rollback_release(self.release, self.root, ownership=document, owner=self.owner, approval=fixtures.digest(sync.json_bytes(plan)), **kwargs)

    def test_update_breaks_reference(self):
        self.proposed["docs/file-0.md"] = b"[broken](missing.md)\n"
        self.refresh_review()
        self.assertFalse(self.apply()["acceptanceReady"])
        inventory = json.loads((self.root / "docs/parity/inventory.json").read_bytes())
        self.assertTrue(any(e.startswith("docs/file-0.md:") and "missing.md" in e for e in validate_package(self.root, inventory)))
        # Missing rollback was the RED boundary for the complete recovery sequence.
        self.assertTrue(callable(sync.rollback_release))

    def test_update_changes_capability_claim(self):
        self.proposed["docs/file-0.md"] = b"Use Task for independent workers.\n"
        self.refresh_review()
        self.assertFalse(self.apply()["acceptanceReady"])
        inventory = json.loads((self.root / "docs/parity/inventory.json").read_bytes())
        self.assertTrue(any(e.startswith("docs/file-0.md:") and "remnant" in e for e in validate_package(self.root, inventory)))
        self.assertTrue(validate_evidence({"status":"pass"}, self.release, self.root))
        self.assertTrue(callable(sync.rollback_release))

    def test_rollback_package_and_inventory_match(self):
        before = self.snapshot()
        def interrupt(stage):
            self.assertEqual("before-inventory", stage)
            raise KeyboardInterrupt("fixture interrupted update")
        with self.assertRaises(KeyboardInterrupt):
            self.apply(failure_hook=interrupt)
        self.assertEqual(before, self.snapshot())
        self.proposed["docs/file-0.md"] = b"[broken](missing.md)\n"
        self.refresh_review()
        self.stage_candidate()
        errors = validate_package(self.root, json.loads((self.root / "docs/parity/inventory.json").read_bytes()))
        self.assertTrue(any(e.startswith("docs/file-0.md:") and "missing.md" in e for e in errors))
        self.assertFalse(json.loads((self.root / f"docs/parity/upstream-manifests/{self.candidate}.apply.json").read_bytes())["acceptanceReady"])
        preserved = {p:(self.root / p).read_bytes() for p in ("personal.md", ".env", ".codex/settings.json")}
        current = self.snapshot()
        with self.assertRaises(KeyboardInterrupt):
            self.rollback(failure_hook=interrupt)
        self.assertEqual(current, self.snapshot())
        result = self.rollback()
        self.assertEqual(result["release"], self.release)
        self.assertEqual(result["actualPackageSha256"], result["releasePackageSha256"])
        for p in self.ownership()["ownedPaths"]:
            self.assertEqual(self.original_package.get(p), self.snapshot().get(p), p)
        for p, data in preserved.items():
            self.assertEqual(data, (self.root / p).read_bytes())
        self.assertEqual(b"portable adapted instructions\n", (self.root / self.leaf).read_bytes())
        self.assertEqual(b"# reviewed portable helper v1\n", (self.root / "tools/portable.py").read_bytes())

    def test_missing_previous_release_preserves_current(self):
        self.stage_candidate()
        before = self.snapshot()
        with self.assertRaises((ValueError, __import__("subprocess").CalledProcessError)):
            self.rollback(self.ownership("f" * 40))
        self.assertEqual(before, self.snapshot())

    def test_rollback_preflight_and_authorization_fail_closed(self):
        self.stage_candidate()
        before = self.snapshot()
        document = self.ownership()
        cases = []
        for state in ('unknown', 'incompatible', 'migration-required'):
            cases.append({**document, 'runtimeState': state})
        cases.append({**document, 'ownedPaths': document['ownedPaths'][:-1]})
        cases.append({**document, 'ownedPaths': document['ownedPaths'] + [document['ownedPaths'][0]]})
        cases.append({**document, 'preservedPaths': {**document['preservedPaths'], 'imaginary': 'not tracked'}})
        cases.append({**document, 'ownedPaths': sorted(document['ownedPaths'] + ['.env']),
                      'preservedPaths': {p:r for p,r in document['preservedPaths'].items() if p != '.env'}})
        for candidate in cases:
            with self.subTest(candidate=candidate), self.assertRaises(ValueError):
                sync.rollback_plan(self.root, candidate, owner=self.owner)
            self.assertEqual(before, self.snapshot())
        with patch.object(sync, 'ARCHIVE_SHA256', self.baseline_hash):
            for owner, approval in ((self.owner, ''), ('wrong-owner', 'f' * 64)):
                with self.assertRaises(ValueError):
                    sync.rollback_release(self.release, self.root, ownership=document, owner=owner, approval=approval)
                self.assertEqual(before, self.snapshot())
        # A clean index cannot conceal an owned file with changed executable mode.
        (self.root / 'tools/portable.py').chmod(0o755)
        changed = self.snapshot()
        with self.assertRaises(ValueError):
            sync.rollback_plan(self.root, document, owner=self.owner)
        self.assertEqual(changed, self.snapshot())

    def test_invalid_release_snapshot_never_replaces_current(self):
        # Commit a bad prior package, then restore the working leaf in a later
        # fixture commit. Preview must validate the bad target before any write.
        (self.root / self.leaf).write_bytes(b'[missing](missing.md)\n')
        self.git('add', self.leaf)
        self.git('commit', '-qm', 'fixture broken previous release')
        self.release = self.git('rev-parse', 'HEAD').strip()
        (self.root / self.leaf).write_bytes(b'portable adapted instructions\n')
        self.git('add', self.leaf)
        self.git('commit', '-qm', 'fixture repaired current package')
        self.set_owner()
        before = self.snapshot()
        with patch.object(sync, 'ARCHIVE_SHA256', self.baseline_hash):
            with self.assertRaisesRegex(ValueError, 'structural validation'):
                sync.rollback_plan(self.root, self.ownership(), owner=self.owner)
        self.assertEqual(before, self.snapshot())

    def test_host_claim_requires_actual_matching_evidence(self):
        self.stage_candidate()
        registry = {'entries':[{'caseId':'fixture-workers', 'sourcePaths':[self.leaf],
            'requiredHosts':['codex'], 'structuralOnly':False,
            'executionModes':{'pass':['workers'],'reduced-pass':['sequential']},
            'requiredPermissions':{'pass':['execution'],'reduced-pass':[]},
            'requiredObservations':{'pass':['spawn','inspect-result'], 'reduced-pass':['read']}}]}
        (self.root / 'docs/parity/case-registry.json').write_text(json.dumps(registry))
        record = dict(caseId='fixture-workers', sourcePaths=[self.leaf], packageVersion='0.1.1',
            packageCommit=self.git('rev-parse','HEAD').strip(), host='codex', hostMode='fixture',
            date='2026-10-07', documentedCapabilities=['fixture workers'], exposedTools=[],
            successfulOperations=[], permissions=dict(execution='granted',writes='granted',externalActions='denied'),
            input='fixture only', observedOutput='unverified claimed workers', artifacts=[], status='pass',
            limits=[], execution='workers', models=dict(requested='unknown',actual='unknown'), priorActionIdentities=[])
        errors = validate_evidence(record, record['packageCommit'], self.root)
        self.assertTrue(any('requires successful spawn' in e for e in errors))
        self.assertTrue(any('artifacts' in e for e in errors))
        self.assertTrue(any('missing required observation' in e for e in errors))
        self.assertTrue(all(r['verification']['codex']['status'] == 'not-run' for r in json.loads((self.root / 'docs/parity/inventory.json').read_bytes())))

    def test_cli_preview_is_read_only_and_requires_ownership(self):
        import subprocess
        before = self.snapshot()
        result = subprocess.run(['python3','-B','-m','tools.sync_upstream','rollback',
            '--release',self.release,'--worktree',str(self.root)], cwd=self.package, capture_output=True,text=True)
        self.assertEqual(2, result.returncode)
        self.assertIn('--ownership', result.stderr)
        self.assertEqual(before, self.snapshot())

    def test_rollback_later_accepted_snapshot_keeps_matching_receipt(self):
        self.stage_candidate()
        staged = self.git('rev-parse', 'HEAD').strip()
        manifest = f'docs/parity/upstream-manifests/{self.candidate}.json'
        evidence = 'docs/parity/fixture-acceptance.json'
        (self.root / evidence).write_bytes(b'{"fixtureOnly":true,"review":"separate synthetic assertion"}\n')
        receipt = dict(schemaVersion=1, kind='pstack-accepted-baseline', commit=self.candidate,
            manifestPath=manifest, manifestSha256=fixtures.digest((self.root / manifest).read_bytes()),
            packageCommit=staged, evidencePath=evidence, evidenceSha256=fixtures.digest((self.root / evidence).read_bytes()))
        (self.root / 'docs/parity/upstream-manifests/accepted.json').write_text(json.dumps(receipt))
        self.git('add', '.', ':!.upstream')
        self.git('commit', '-qm', 'fixture separate acceptance assertion')
        self.release = self.git('rev-parse', 'HEAD').strip()
        self.original_package = self.snapshot()
        (self.root / 'tools/portable.py').write_bytes(b'# fixture later broken helper\n')
        self.git('add', 'tools/portable.py')
        self.git('commit', '-qm', 'fixture later package')
        self.set_owner()
        result = self.rollback()
        self.assertEqual(result['actualPackageSha256'], result['releasePackageSha256'])
        self.assertEqual(receipt, json.loads((self.root / 'docs/parity/upstream-manifests/accepted.json').read_bytes()))
        self.assertEqual(b'# reviewed portable helper v2\n', (self.root / 'tools/portable.py').read_bytes())

    def test_snapshot_rejects_mismatched_inventory_and_invalid_host_evidence(self):
        files = sync.committed_tree(self.root, self.release)
        files = {p:v for p,v in files.items() if p in self.ownership()['ownedPaths']}
        before = self.snapshot()
        inventory = json.loads(files['docs/parity/inventory.json'][0])
        inventory[0]['upstreamSha256'] = '0' * 64
        changed = {**files, 'docs/parity/inventory.json': (sync.json_bytes(inventory), 0o644)}
        with patch.object(sync, 'ARCHIVE_SHA256', self.baseline_hash):
            with self.assertRaisesRegex(ValueError, 'inventory and source manifest differ'):
                sync.validate_rollback_snapshot(self.root, self.release, changed)
            inventory = json.loads(files['docs/parity/inventory.json'][0])
            inventory[0]['verification']['codex'] = {'status':'pass','evidence':[]}
            changed['docs/parity/inventory.json'] = (sync.json_bytes(inventory), 0o644)
            with self.assertRaisesRegex(ValueError, 'requires host evidence'):
                sync.validate_rollback_snapshot(self.root, self.release, changed)
        self.assertEqual(before, self.snapshot())

    def freeze_with_passing_evidence(self, change_operative=False, extra_report=None, declare_extra=False):
        registry = {'entries':[{'caseId':'fixture-workers', 'sourcePaths':[self.leaf],
            'requiredHosts':['codex'], 'structuralOnly':False,
            'executionModes':{'pass':['workers'],'reduced-pass':['sequential']},
            'requiredPermissions':{'pass':['execution'],'reduced-pass':[]},
            'requiredObservations':{'pass':['spawn','inspect-result'], 'reduced-pass':['read']}}]}
        (self.root / 'docs/parity/case-registry.json').write_text(json.dumps(registry))
        self.git('add', '.', ':!.upstream')
        self.git('commit', '-qm', 'fixture frozen operative package')
        frozen = self.git('rev-parse', 'HEAD').strip()
        artifact = 'docs/parity/evidence/fixture-result.txt'
        evidence = 'docs/parity/evidence/fixture-host.json'
        (self.root / artifact).parent.mkdir(parents=True)
        (self.root / artifact).write_bytes(b'Fixture only: synthetic observations, no real host run.\n')
        record = dict(caseId='fixture-workers', sourcePaths=[self.leaf], packageVersion='0.1.0',
            packageCommit=frozen, host='codex', hostMode='fixture', date='2026-10-07',
            documentedCapabilities=['synthetic workers'], exposedTools=['fixture.spawn'],
            successfulOperations=[dict(operation=op,tool='fixture.spawn',evidence=artifact) for op in ('spawn','inspect-result')],
            permissions=dict(execution='granted',writes='granted',externalActions='denied'),
            input='synthetic fixture', observedOutput='synthetic fixture only', artifacts=[artifact], status='pass',
            limits=['No actual host observation'], execution='workers', models=dict(requested='unknown',actual='unknown'), priorActionIdentities=[])
        (self.root / evidence).write_text(json.dumps(record))
        inventory = json.loads((self.root / 'docs/parity/inventory.json').read_bytes())
        next(r for r in inventory if r['upstreamPath'] == self.leaf)['verification']['codex'] = {'status':'pass','evidence':[evidence]}
        (self.root / 'docs/parity/inventory.json').write_text(json.dumps(inventory))
        planned_reports = ["docs/testing/codex.md", "docs/testing/chatgpt.md", "docs/testing/release-checklist.md"]
        for path in planned_reports + ([extra_report] if extra_report else []):
            target = self.root / path
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(b"Synthetic post-freeze report fixture.\n")
        provenance = dict(schemaVersion=1, kind='pstack-tested-package', testedCommit=frozen,
            reportPaths=[evidence,artifact,*planned_reports] + ([extra_report] if declare_extra else []))
        (self.root / 'docs/parity/tested-package.json').write_text(json.dumps(provenance))
        if change_operative:
            (self.root / 'tools/portable.py').write_bytes(b'# untested operative change\n')
        self.git('add', '.', ':!.upstream')
        self.git('commit', '-qm', 'fixture evidence release snapshot')
        self.release = self.git('rev-parse', 'HEAD').strip()
        self.original_package = self.snapshot()
        (self.root / 'tools/portable.py').write_bytes(b'# later current package\n')
        self.git('add', 'tools/portable.py')
        self.git('commit', '-qm', 'fixture current descendant')
        self.set_owner()
        return frozen

    def test_rollback_accepts_frozen_tested_commit_with_later_evidence(self):
        frozen = self.freeze_with_passing_evidence()
        self.assertNotEqual(frozen, self.release)
        for path in ("docs/testing/codex.md", "docs/testing/chatgpt.md", "docs/testing/release-checklist.md"):
            self.assertTrue((self.root / path).is_file())
        result = self.rollback()
        self.assertEqual(result['actualPackageSha256'], result['releasePackageSha256'])
        self.assertEqual(b'# reviewed portable helper v1\n', (self.root / 'tools/portable.py').read_bytes())

    def test_rollback_rejects_operative_changes_after_tested_commit(self):
        self.freeze_with_passing_evidence(change_operative=True)
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'Operative package differs'):
            self.rollback()
        self.assertEqual(before, self.snapshot())

    def test_empty_acceptance_evidence_blocks_rollback(self):
        self.stage_candidate()
        staged = self.git('rev-parse', 'HEAD').strip()
        manifest = f'docs/parity/upstream-manifests/{self.candidate}.json'
        evidence = 'docs/parity/empty-acceptance.json'
        (self.root / evidence).write_bytes(b'')
        receipt = dict(schemaVersion=1, kind='pstack-accepted-baseline', commit=self.candidate,
            manifestPath=manifest, manifestSha256=fixtures.digest((self.root / manifest).read_bytes()),
            packageCommit=staged,evidencePath=evidence,evidenceSha256=fixtures.digest(b''))
        (self.root / 'docs/parity/upstream-manifests/accepted.json').write_text(json.dumps(receipt))
        self.git('add', '.', ':!.upstream')
        self.git('commit', '-qm', 'fixture empty acceptance evidence')
        self.release = self.git('rev-parse', 'HEAD').strip()
        self.original_package = self.snapshot()
        self.set_owner()
        before = self.snapshot()
        with self.assertRaisesRegex(ValueError, 'acceptance evidence'):
            self.rollback()
        self.assertEqual(before, self.snapshot())

    def test_frozen_provenance_does_not_accept_wrong_evidence_identity(self):
        self.freeze_with_passing_evidence()
        files = sync.committed_tree(self.root, self.release)
        files = {p:v for p,v in files.items() if p in self.ownership()['ownedPaths']}
        path = 'docs/parity/evidence/fixture-host.json'
        original = json.loads(files[path][0])
        before = self.snapshot()
        with patch.object(sync, 'ARCHIVE_SHA256', self.baseline_hash):
            for field, value in (('packageVersion','9.9.9'),('packageCommit',self.release)):
                changed = {**files,path:(sync.json_bytes({**original,field:value}),0o644)}
                with self.subTest(field=field), self.assertRaisesRegex(ValueError, 'Invalid rollback host evidence'):
                    sync.validate_rollback_snapshot(self.root,self.release,changed)
        self.assertEqual(before,self.snapshot())

    def assert_unplanned_report_rejected(self, path, declared):
        self.freeze_with_passing_evidence(extra_report=path, declare_extra=declared)
        before = self.snapshot()
        message = "Report provenance cannot exempt operative content" if declared else "Operative package differs"
        with self.assertRaisesRegex(ValueError, message + ".*" + path):
            self.rollback()
        self.assertEqual(before, self.snapshot())

    def test_declared_testing_helper_is_not_a_report(self):
        self.assert_unplanned_report_rejected("docs/testing/helper-setup.md", True)

    def test_undeclared_testing_helper_is_not_a_report(self):
        self.assert_unplanned_report_rejected("docs/testing/helper-setup.md", False)

    def test_declared_setup_guide_is_not_a_report(self):
        self.assert_unplanned_report_rejected("docs/setup/helper.md", True)

    def test_undeclared_setup_guide_is_not_a_report(self):
        self.assert_unplanned_report_rejected("docs/setup/helper.md", False)
