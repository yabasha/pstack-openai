"""Owned-worktree apply fixtures. No operative checkout is updated."""
import json
from pathlib import Path
import subprocess
from unittest.mock import patch
import unittest
from tests import test_upstream_check as fixtures
from tests.test_upstream_check import digest
from tools import sync_upstream as sync


class UpstreamApplyTests(unittest.TestCase):
    snapshot = fixtures.PublicSourceContractTests.snapshot
    run_review = fixtures.PublicSourceContractTests.run_review
    # Reuse source fixtures without inheriting their test cases.
    def setUp(self):
        fixtures.PublicSourceContractTests.setUp(self)
        for name, data in {'plugin.json': b'{"version":"0.1.0"}', 'NOTICE.md': b'Original notice\n'}.items():
            (self.root / name).write_bytes(data)
        inventory_path = self.root / "docs/parity/inventory.json"
        inventory = json.loads(inventory_path.read_text())
        for row in inventory:
            row.update(disposition="runtime", rationale="Fixture source", dependencies=[], adaptationStatus="adapted-reviewed",
                licenseProvenance={"license":"MIT", "copyright":"Copyright (c) 2026 Lauren Tan", "sourcePath":"LICENSE"},
                verification={host: {"status":"pass", "evidence":["fixture"]} for host in ("chatgpt", "codex")})
        inventory_path.write_text(json.dumps(inventory))
        (self.root / "docs/parity/inventory.schema.json").write_bytes((self.package / "docs/parity/inventory.schema.json").read_bytes())
        self.git("add", ".")
        self.git('commit', '-qm', 'fixture metadata')
        self.original_root = self.root
        self.root = self.original_root / 'owned'
        self.git_at(self.original_root, 'worktree', 'add', '-q', '--detach', str(self.root))
        self.bundle = self.run_review('prepare')
        self.review = self.root / '.upstream/reviews' / self.candidate
        self.report_hash = digest((self.review / 'report.json').read_bytes())
        self.owner = 'task-26B-fixture'
        admin = Path(self.git('rev-parse', '--absolute-git-dir').strip())
        (admin / 'pstack-update-owner.json').write_text(json.dumps(dict(schemaVersion=1, owner=self.owner, worktree=str(self.root), packageCommit=self.bundle['packageCommit'])))
        self.resolutions = dict(schemaVersion=2, kind=sync.RESOLUTION_KIND, candidate=self.candidate,
            packageCommit=self.bundle['packageCommit'], reviewSha256=self.report_hash, candidateVersion='0.1.1', entries=[])
        for entry in self.bundle['files']['added'] + self.bundle['files']['removed'] + self.bundle['files']['changed']:
            content = 'sources/candidate/' + entry['path']
            self.resolutions['entries'].append(dict(**entry, disposition='add-reviewed' if entry['oldSha256'] is None else 'adapt-manually', rationale='Reviewed fixture change.', reviewedCallers=entry['dependentCallers'], contentPath=content, reviewedSha256=digest((self.review / content).read_bytes())))
        self.resolution_path = self.review / 'approved.json'
        self.save_resolutions()

    def git_at(self, root, *args):
        return subprocess.run(['git', '-C', str(root), '-c', 'user.name=Fixture', '-c', 'user.email=fixture@example.invalid', *args], check=True, capture_output=True, text=True).stdout

    def git(self, *args):
        return self.git_at(self.root, *args)

    def save_resolutions(self):
        self.resolution_path.write_text(json.dumps(self.resolutions))

    def apply(self, **kwargs):
        with patch.object(sync, 'ARCHIVE_SHA256', self.baseline_hash):
            return sync.apply_review(self.review, self.resolution_path, self.root, owner=self.owner,
                approval=digest(self.resolution_path.read_bytes()), **kwargs)

    def test_stale_working_hash_rejected(self):
        (self.root / self.leaf).write_bytes(b'stale')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.apply()
        self.assertEqual(before, self.snapshot())

    def test_added_reference_relocates_without_creating_runtime_root(self):
        entry = next(e for e in self.resolutions['entries'] if e['path'] == 'skills/new/SKILL.md')
        entry.update(disposition='reference-only', referenceDestinationPath='references/upstream-deferred/new/REFERENCE.md')
        self.save_resolutions()
        self.apply()
        self.assertFalse((self.root / 'skills/new/SKILL.md').exists())
        self.assertEqual((self.root / entry['referenceDestinationPath']).read_bytes(), self.proposed[entry['path']])
        inventory = json.loads((self.root / 'docs/parity/inventory.json').read_text())
        row = next(r for r in inventory if r['upstreamPath'] == entry['path'])
        self.assertEqual(row['destinationPath'], entry['referenceDestinationPath'])
        manifest = json.loads((self.root / f'docs/parity/upstream-manifests/{self.candidate}.json').read_text())
        self.assertEqual(next(r for r in manifest['files'] if r['upstreamPath'] == entry['path'])['destinationPath'], entry['referenceDestinationPath'])

    def test_reference_relocation_rejects_runtime_existing_and_unsafe_paths(self):
        entry = next(e for e in self.resolutions['entries'] if e['path'] == 'skills/new/SKILL.md')
        for destination in ('skills/other/SKILL.md', '../escape', 'references/upstream-deferred/new/SKILL.md'):
            entry.update(disposition='reference-only', referenceDestinationPath=destination)
            self.save_resolutions()
            before = self.snapshot()
            with self.subTest(destination=destination), self.assertRaises(ValueError): self.apply()
            self.assertEqual(before, self.snapshot())
        destination = 'references/upstream-deferred/new/REFERENCE.md'
        target = self.root / destination
        target.parent.mkdir(parents=True)
        target.write_text('Unrelated existing reference')
        entry['referenceDestinationPath'] = destination; self.save_resolutions()
        # Exercise collision handling after the independently tested clean-tree gate.
        with patch.object(sync, 'verify_owned_worktree'), self.assertRaisesRegex(ValueError, 'already exists'):
            self.apply()
        target.unlink(); target.parent.rmdir()
        target.parent.symlink_to(self.root)
        with patch.object(sync, 'verify_owned_worktree'), self.assertRaises(ValueError): self.apply()

    def test_managed_owner_root_preserves_marker_commit_and_realpath_checks(self):
        import shutil
        import tempfile
        managed = Path.home() / '.codex/worktrees'
        managed.mkdir(parents=True, exist_ok=True)
        container = Path(tempfile.mkdtemp(prefix='pstack-owner-fixture-', dir=managed))
        owned = container / 'owned'
        self.git_at(self.original_root, 'worktree', 'add', '-q', '--detach', str(owned))
        self.addCleanup(lambda: shutil.rmtree(container, ignore_errors=True))
        admin = Path(self.git_at(owned, 'rev-parse', '--absolute-git-dir').strip())
        marker = dict(schemaVersion=1, owner=self.owner, worktree=str(owned), packageCommit=self.bundle['packageCommit'])
        (admin / 'pstack-update-owner.json').write_text(json.dumps(marker))
        sync.verify_owned_worktree(owned, self.owner, self.bundle['packageCommit'])
        with self.assertRaises(ValueError): sync.verify_owned_worktree(owned, 'other', self.bundle['packageCommit'])
        alias = container / 'alias'; alias.symlink_to(owned)
        with self.assertRaises(ValueError): sync.verify_owned_worktree(alias, self.owner, self.bundle['packageCommit'])

    def test_unresolved_conflict_no_write(self):
        self.resolutions['entries'][0]['disposition'] = 'pending'
        self.save_resolutions()
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.apply()
        self.assertEqual(before, self.snapshot())

    def test_user_customization_untouched(self):
        protected = {p: (self.root / p).read_bytes() for p in ('.env', '.codex/settings.json', 'personal.md')}
        result = self.apply()
        self.assertFalse(result['acceptanceReady'])
        for p, data in protected.items():
            self.assertEqual(data, (self.root / p).read_bytes())
        self.assertEqual(self.proposed[self.leaf], (self.root / self.leaf).read_bytes())
        self.assertTrue((self.root / f'docs/parity/upstream-manifests/{sync.BASELINE}.json').exists())

    def test_failure_mid_apply_restores_owned_checkout(self):
        before = self.snapshot()
        def fail(stage):
            self.assertEqual(stage, 'before-inventory')
            self.assertEqual(self.proposed[self.leaf], (self.root / self.leaf).read_bytes())
            raise RuntimeError('injected failure')
        with self.assertRaises(RuntimeError):
            self.apply(failure_hook=fail)
        self.assertEqual(before, self.snapshot())
        self.assertEqual(self.report_hash, digest((self.review / 'report.json').read_bytes()))

    def test_approval_and_ownership_fail_closed(self):
        before = self.snapshot()
        for owner, approval, root in ((self.owner, '', self.root), ('other', digest(self.resolution_path.read_bytes()), self.root), (self.owner, digest(self.resolution_path.read_bytes()), self.original_root)):
            with self.subTest(owner=owner, root=root), self.assertRaises(ValueError):
                sync.apply_review(self.review, self.resolution_path, root, owner=owner, approval=approval)
        self.assertEqual(before, self.snapshot())

    def test_tampered_artifact_and_reviewed_content_rejected(self):
        target = self.review / self.resolutions['entries'][0]['contentPath']
        target.write_bytes(b'tampered')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.apply()
        self.assertEqual(before, self.snapshot())

    def test_unsafe_destination_and_missing_callers_rejected(self):
        entry = self.resolutions['entries'][0]
        for destination in ('.env', '.codex/settings.json', '../escape', 'personal.md'):
            entry['destinationPath'] = destination
            self.save_resolutions()
            before = self.snapshot()
            with self.subTest(destination=destination), self.assertRaises(ValueError):
                self.apply()
            self.assertEqual(before, self.snapshot())

    def test_no_final_newline_resolved_bytes_and_evidence_invalidation(self):
        entry = next(e for e in self.resolutions['entries'] if e['path'] == self.leaf)
        entry['contentPath'] = 'resolved/leaf.md'
        data = b'reviewed exact bytes without a final newline'
        (self.review / 'resolved').mkdir()
        (self.review / entry['contentPath']).write_bytes(data)
        entry['reviewedSha256'] = digest(data)
        self.save_resolutions()
        self.apply()
        self.assertEqual(data, (self.root / self.leaf).read_bytes())
        inventory = json.loads((self.root / 'docs/parity/inventory.json').read_text())
        for row in inventory:
            self.assertEqual(row['upstreamCommit'], self.candidate)
            for host in ('chatgpt', 'codex'):
                self.assertEqual(row['verification'][host], {'status':'not-run', 'evidence':[]})
        self.assertIn(b'MIT fixture notice', (self.root / 'NOTICE.md').read_bytes())

    def test_symlink_in_resolved_content_rejected(self):
        entry = self.resolutions['entries'][0]
        (self.review / 'resolved').symlink_to(self.root)
        entry['contentPath'] = 'resolved/personal.md'
        entry['reviewedSha256'] = digest((self.root / 'personal.md').read_bytes())
        self.save_resolutions()
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.apply()
        self.assertEqual(before, self.snapshot())

    def test_cli_requires_explicit_approval_without_writes(self):
        before = self.snapshot()
        command = ['python3', '-B', '-m', 'tools.sync_upstream', 'apply', '--review', str(self.review), '--resolutions', str(self.resolution_path), '--worktree', str(self.root), '--owner', self.owner]
        result = subprocess.run(command, cwd=self.package, capture_output=True, text=True)
        self.assertEqual(result.returncode, 2)
        self.assertIn('requires', result.stderr)
        self.assertEqual(before, self.snapshot())

    def test_explicit_rename_and_deletion_preserve_notices(self):
        import shutil
        import hashlib
        old_path, new_path, deleted = 'docs/file-2.md', 'docs/moved.md', 'docs/file-1.md'
        self.proposed[new_path] = self.proposed.pop(old_path)
        del self.proposed[deleted]
        del self.proposed['LICENSE']
        self.responses[sync.ARCHIVE + self.candidate] = fixtures.archive_bytes(self.proposed, self.candidate)
        self.responses[sync.API + '/git/trees/' + self.tree_sha + '?recursive=1'] = json.dumps({'sha':self.tree_sha, 'truncated':False, 'tree':[
            {'path':'pstack/' + path, 'type':'blob', 'mode':'100644', 'sha':hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()} for path, data in self.proposed.items()]}).encode()
        shutil.rmtree(self.review)
        self.bundle = self.run_review('prepare')
        self.resolutions['reviewSha256'] = digest((self.review / 'report.json').read_bytes())
        self.resolutions['entries'] = []
        for entry in self.bundle['files']['added'] + self.bundle['files']['removed'] + self.bundle['files']['changed']:
            action = 'rename-reviewed' if entry['path'] in (old_path, new_path) else 'delete-reviewed' if entry['newSha256'] is None else 'add-reviewed' if entry['oldSha256'] is None else 'adapt-manually'
            content = 'sources/candidate/' + entry['path'] if entry['newSha256'] else None
            self.resolutions['entries'].append(dict(**entry, disposition=action, rationale='Reviewed source move or deletion.', reviewedCallers=entry['dependentCallers'], contentPath=content, reviewedSha256=digest((self.review / content).read_bytes()) if content else None))
        self.save_resolutions()
        self.apply()
        self.assertFalse((self.root / old_path).exists())
        self.assertFalse((self.root / deleted).exists())
        self.assertEqual(self.original[old_path], (self.root / new_path).read_bytes())
        self.assertIn(self.original['LICENSE'], (self.root / 'NOTICE.md').read_bytes())

    def test_missing_caller_review_rejected(self):
        self.resolutions['entries'][0]['reviewedCallers'] = ['skills/undeclared/SKILL.md']
        self.save_resolutions()
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.apply()
        self.assertEqual(before, self.snapshot())
    def test_unaccepted_candidate_cannot_advance_baseline(self):
        self.apply()
        self.git('add', '.', ':!.upstream')
        self.git('commit', '-qm', 'stage unaccepted fixture')
        self.review.rename(self.review.parent / 'retained-A')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.run_review('prepare')
        self.assertEqual(before, self.snapshot())

    def test_sequential_updates_use_explicitly_accepted_manifest(self):
        import hashlib
        self.apply()
        self.git('add', '.', ':!.upstream')
        self.git('commit', '-qm', 'stage fixture A')
        accepted_commit = self.git('rev-parse', 'HEAD').strip()
        manifest_path = f'docs/parity/upstream-manifests/{self.candidate}.json'
        evidence_path = 'docs/parity/fixture-acceptance.json'
        (self.root / evidence_path).write_text('{"fixtureOnly":true,"review":"separately reviewed acceptance assertion"}')
        receipt = dict(schemaVersion=1, kind='pstack-accepted-baseline', commit=self.candidate,
            manifestPath=manifest_path, manifestSha256=digest((self.root / manifest_path).read_bytes()),
            packageCommit=accepted_commit, evidencePath=evidence_path,
            evidenceSha256=digest((self.root / evidence_path).read_bytes()))
        (self.root / 'docs/parity/upstream-manifests/accepted.json').write_text(json.dumps(receipt))
        self.git('add', '.', ':!.upstream')
        self.git('commit', '-qm', 'record fixture acceptance assertion')
        previous = self.candidate
        self.candidate = 'd' * 40
        self.proposed[self.leaf] += b'Second candidate.\n'
        self.responses[sync.ARCHIVE + self.candidate] = fixtures.archive_bytes(self.proposed, self.candidate)
        self.responses[sync.API + '/commits/' + self.candidate] = json.dumps({'sha':self.candidate,'commit':{'tree':{'sha':self.tree_sha}}}).encode()
        self.responses[sync.API + '/compare/' + previous + '...' + self.candidate] = json.dumps({'merge_base_commit':{'sha':previous},'base_commit':{'sha':previous},'status':'ahead'}).encode()
        self.responses[sync.API + '/git/trees/' + self.tree_sha + '?recursive=1'] = json.dumps({'sha':self.tree_sha, 'truncated':False, 'tree':[
            {'path':'pstack/' + path, 'type':'blob','mode':'100644','sha':hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()} for path, data in self.proposed.items()]}).encode()
        self.bundle = self.run_review('prepare')
        self.assertEqual(self.bundle['baseline'], previous)
        self.assertEqual(len(self.bundle['files']['unchanged']), 164)
        self.review = self.root / '.upstream/reviews' / self.candidate
        admin = Path(self.git('rev-parse', '--absolute-git-dir').strip())
        (admin / 'pstack-update-owner.json').write_text(json.dumps(dict(schemaVersion=1, owner=self.owner, worktree=str(self.root),packageCommit=self.bundle['packageCommit'])))
        self.resolutions.update(candidate=self.candidate, packageCommit=self.bundle['packageCommit'], reviewSha256=digest((self.review / 'report.json').read_bytes()), candidateVersion='0.1.2', entries=[])
        for entry in self.bundle['files']['changed']:
            content = 'drafts/' + entry['destinationPath']
            self.resolutions['entries'].append(dict(**entry, disposition='adapt-manually', rationale='Reviewed second fixture update.', reviewedCallers=entry['dependentCallers'], contentPath=content, reviewedSha256=digest((self.review / content).read_bytes())))
        self.resolution_path = self.review / 'approved.json'
        self.save_resolutions()
        evidence = self.root / evidence_path
        original_evidence = evidence.read_bytes()
        evidence.write_bytes(b'changed acceptance evidence')
        before = self.snapshot()
        with self.assertRaises(ValueError):
            self.apply()
        self.assertEqual(before, self.snapshot())
        evidence.write_bytes(original_evidence)
        self.apply()
        self.assertEqual(self.proposed[self.leaf], (self.root / self.leaf).read_bytes())
        self.assertTrue((self.root / manifest_path).exists())
        self.assertEqual(receipt, json.loads((self.root / 'docs/parity/upstream-manifests/accepted.json').read_text()))

    def preview(self, output):
        with patch.object(sync, 'ARCHIVE_SHA256', self.baseline_hash):
            return sync.preview_review(self.review, self.resolution_path, self.root,
                owner=self.owner, output=output)

    def preview_output(self):
        import tempfile
        temporary = tempfile.TemporaryDirectory(prefix='pstack-preview-fixture-', dir=Path.home() / 'Herd')
        self.addCleanup(temporary.cleanup)
        return Path(temporary.name) / 'new-preview'

    def test_preview_materializes_without_apply_receipt_or_source_writes(self):
        output = self.preview_output()
        before = self.snapshot()
        plan = self.preview(output)
        self.assertFalse(plan['applied'])
        self.assertEqual(plan['resolutionsSha256'], digest(self.resolution_path.read_bytes()))
        self.assertEqual(before, self.snapshot())
        package = output / 'package'
        self.assertEqual((package / self.leaf).read_bytes(), self.proposed[self.leaf])
        self.assertFalse((package / plan['omittedApplyReceipt']).exists())
        self.assertFalse((self.root / plan['omittedApplyReceipt']).exists())
        self.assertTrue((output / 'planned-transaction.json').is_file())
        self.assertIn('not execution evidence', (output / 'README.md').read_text())

    def test_preview_rejects_existing_symlink_and_repository_outputs(self):
        output = self.preview_output()
        output.mkdir()
        sentinel = output / 'preserve.txt'
        sentinel.write_text('keep')
        before = self.snapshot()
        for bad in (output, self.root / 'preview', self.root.parent, self.review / 'preview'):
            with self.subTest(output=str(bad)), self.assertRaises(ValueError):
                self.preview(bad)
        self.assertEqual(sentinel.read_text(), 'keep')
        linked = output.parent / 'linked'
        linked.symlink_to(output, target_is_directory=True)
        with self.assertRaises(ValueError):
            self.preview(linked / 'nested')
        self.assertEqual(before, self.snapshot())

    def test_preview_rejects_stale_review_digest_and_source_baseline(self):
        output = self.preview_output()
        before = self.snapshot()
        self.resolutions['reviewSha256'] = '0' * 64
        self.save_resolutions()
        with self.assertRaises(ValueError):
            self.preview(output)
        self.assertFalse(output.exists())
        self.resolutions['reviewSha256'] = self.report_hash
        self.save_resolutions()
        inventory = self.root / 'docs/parity/inventory.json'
        rows = json.loads(inventory.read_text())
        rows[0]['upstreamCommit'] = 'f' * 40
        inventory.write_text(json.dumps(rows))
        altered = self.snapshot()
        with self.assertRaises(ValueError):
            self.preview(output)
        self.assertFalse(output.exists())
        self.assertEqual(altered, self.snapshot())

    def test_apply_rejects_resolution_change_between_approval_and_plan(self):
        original_plan = sync.review_plan
        before = self.snapshot()
        def changed_plan(*args, **kwargs):
            changed = json.loads(self.resolution_path.read_text())
            changed['entries'][0]['rationale'] += ' changed after approval'
            self.resolution_path.write_text(json.dumps(changed))
            return original_plan(*args, **kwargs)
        with patch.object(sync, 'review_plan', changed_plan), self.assertRaisesRegex(ValueError, 'changed after approval'):
            self.apply()
        self.assertEqual(before, self.snapshot())

    def test_preview_does_not_adopt_or_remove_concurrent_output(self):
        output = self.preview_output()
        original_mkdir = Path.mkdir
        def competing_mkdir(path, *args, **kwargs):
            if path == output:
                original_mkdir(path)
                (path / 'sentinel.txt').write_text('belongs to another invocation')
            return original_mkdir(path, *args, **kwargs)
        before = self.snapshot()
        with patch.object(Path, 'mkdir', competing_mkdir), self.assertRaises(FileExistsError):
            self.preview(output)
        self.assertEqual((output / 'sentinel.txt').read_text(), 'belongs to another invocation')
        self.assertEqual(before, self.snapshot())
