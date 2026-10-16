"""Read-only pstack plan checks run through Bun; fixtures stay under Herd."""
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / 'skills/poteto-mode/scripts/check-plan.mjs'
RULE = 'Tests alone are not sufficient verification. Full verification requires unit evidence, live evidence, and performance evidence or justified non-applicability.'

def plan(capabilities='Independent workers available. Evidence `workers.log`. Capacity 1.\nLive control available. Evidence `control.log`.\nScheduling unavailable. Evidence `schedule.log`.\nRemote unavailable. Evidence `remote.log`.\nModel selection unavailable. Evidence `model.log`.', live=None, perf=None):
    live = live or 'Status full. Lanes 1.\n- [ ] Lane 1. Regression against trunk and head. Save `live.log`. Pass when output matches.'
    perf = perf or '\n'.join('- [ ] ' + x for x in ['Metric. latency', 'Probe. interleaved trunk and head', 'Baseline. trunk first', 'Rule. head under 10ms'])
    blocks = ['**Depends on.** None.', '**Files.**\n- [ ] Edit `app.py`.', '**Build.**\n- [ ] Change output. Save `diff.log`.', '**You see.**\n- [ ] Output matches. Save `output.log`.', '**Verify, unit.** ' + RULE + '\n- [ ] Run `tests`. Save `unit.log`. Pass when tests pass.', '**Verify, live.** ' + RULE + ' ' + live, '**Verify, perf.** ' + RULE + '\n' + perf, '**Review gate.** Independent review available.\n- [ ] Independent reviewer checks `diff.log`. Save `review.log`. Pass when no findings remain.', '**Merge.**\n- [ ] Verdict at exact head. Save `verdict.log`.']
    blocks = [b.replace('Independent review available.', 'Independent review available. Interaction not applicable. Reason CLI output only. Evidence `scope.log`.') for b in blocks]
    return '# Example plan\n\nA scoped change.\n\n## How to read this\nOne box is one unit of work and names the evidence. Check a box only when its evidence exists. Run `playbooks/autopilot-full.md`.\n' + RULE + '\n\n## Capabilities\n' + capabilities + '\n\n## Program checklist\n' + '\n'.join('### ' + h + '\n- [ ] Save `program.log`.' for h in ['Arm the program', 'Spawn owners', 'PR mechanics', 'Verdict and merge', 'Boot recipe']) + '\nRead recorded baseline. Post a status message only on change.\n## Change output (PR1)\n' + '\n\n'.join(blocks) + '\n## Close the program\n- [ ] Report evidence and limits.\n## Appendix A. Prototype evidence\nRecorded separately.\n'

class PlanCheckTests(unittest.TestCase):
    def call(self, text):
        scratch = ROOT / '.superpowers/sdd/2026-10-07-pstack-openai/task-17-fixtures'
        scratch.mkdir(exist_ok=True)
        with tempfile.TemporaryDirectory(dir=scratch) as folder:
            path = Path(folder) / 'plan.md'
            path.write_text(text)
            before = path.read_bytes()
            result = subprocess.run(['bun', '--no-install', str(HELPER), str(path)], capture_output=True, text=True)
            self.assertEqual(path.read_bytes(), before)
            return result

    def test_valid_pstack_plan(self):
        result = self.call(plan())
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_no_capability_evidence(self):
        result = self.call(plan(capabilities='Independent workers available. Capacity 1.'))
        self.assertEqual(result.returncode, 1)
        self.assertIn('capability evidence', result.stderr)

    def test_unsupported_ten_lane_claim(self):
        result = self.call(plan(live='Status full. Lanes 10.\n' + '\n'.join(f'- [ ] Lane {n}. Scenario. Save `lane{n}.log`. Pass when correct.' for n in range(1, 11))))
        self.assertEqual(result.returncode, 1)
        self.assertIn('capacity', result.stderr)

    def test_justified_perf_not_applicable(self):
        result = self.call(plan(perf='Not applicable. Reason documentation-only change has no runtime path. Evidence `scope.log`.'))
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_superpowers_not_rewritten(self):
        result = self.call('# Implementation plan\n## Task 1\n- [ ] Implement helper.\n')
        self.assertEqual(result.returncode, 1)
        self.assertIn('pstack', result.stderr)

    def test_usage_and_missing_file(self):
        for args in [[], [str(ROOT / 'missing-task-17.md')]]:
            result = subprocess.run(['bun', '--no-install', str(HELPER), *args], capture_output=True, text=True)
            self.assertEqual(result.returncode, 2)

    def test_checked_reduced_live_cannot_claim_full(self):
        result = self.call(plan(live='Status reduced. Lanes 1. Full success.\n- [x] Lane 1. Scenario. Save `live.log`. Pass when correct.'))
        self.assertEqual(result.returncode, 1)
        self.assertIn('full success', result.stderr)

    def test_independent_review_required_when_available(self):
        result = self.call(plan().replace('Independent review available.', 'None. No interaction change.'))
        self.assertEqual(result.returncode, 1)
        self.assertIn('independent review', result.stderr)

    def test_checked_live_requires_receipt(self):
        result = self.call(plan().replace('- [ ] Lane 1.', '- [x] Lane 1.'))
        self.assertEqual(result.returncode, 1)
        self.assertIn('checkbox is not proof', result.stderr)

    def test_blocked_and_reduced_are_explicit(self):
        caps = 'Independent workers unavailable. Evidence `workers.log`.\nLive control unavailable. Evidence `control.log`.\nScheduling unavailable. Evidence `schedule.log`.\nRemote unavailable. Evidence `remote.log`.\nModel selection unavailable. Evidence `model.log`.'
        for live in ['Status blocked. Lanes 0. Reason no control. Evidence `blocked.log`.', 'Status reduced. Lanes 1. Reason sequential local verification. Evidence `limits.log`.\n- [ ] Lane 1. Regression against trunk and head. Save `live.log`. Pass when correct.']:
            text = plan(capabilities=caps, live=live).replace('Independent review available.', 'Reduced review. Reason workers unavailable. Evidence `review-limit.log`.')
            result = self.call(text)
            self.assertEqual(result.returncode, 0, result.stderr)

    def test_lane_order_is_enforced(self):
        text = plan().replace('Capacity 1.', 'Capacity 2.').replace('Lanes 1.', 'Lanes 2.').replace('Lane 1.', 'Lane 2.')
        text = text.replace('**Verify, perf.**', '- [ ] Lane 1. Scenario. Save `lane.log`. Pass when correct.\n\n**Verify, perf.**')
        result = self.call(text)
        self.assertEqual(result.returncode, 1)
        self.assertIn('ordered', result.stderr)

    def test_none_review_still_requires_reduced_worker_record(self):
        text = plan().replace('Independent workers available. Evidence `workers.log`. Capacity 1.', 'Independent workers unavailable. Evidence `workers.log`.')
        text = text.replace('Status full. Lanes 1.\n- [ ] Lane 1. Regression against trunk and head. Save `live.log`. Pass when output matches.', 'Status blocked. Lanes 0. Reason no workers. Evidence `blocked.log`.')
        text = text.replace('Independent review available.', 'None.').replace('- [ ] Independent reviewer checks `diff.log`. Save `review.log`. Pass when no findings remain.', '')
        result = self.call(text)
        self.assertEqual(result.returncode, 1)
        self.assertIn('explicit reduced review', result.stderr)
        text = text.replace('**Review gate.** None.', '**Review gate.** None. Reduced review. Reason workers unavailable. Evidence `review-limit.log`.')
        result = self.call(text)
        self.assertEqual(result.returncode, 0, result.stderr)

    def test_interaction_applicability_is_required(self):
        text = plan().replace('Interaction not applicable. Reason CLI output only. Evidence `scope.log`.', '')
        result = self.call(text)
        self.assertEqual(result.returncode, 1)
        self.assertIn('interaction applicability', result.stderr)

    def test_applicable_interaction_requires_operator_media(self):
        text = plan().replace('Interaction not applicable. Reason CLI output only. Evidence `scope.log`.', 'Interaction applicable.')
        result = self.call(text)
        self.assertEqual(result.returncode, 1)
        for word in ['operator', 'screenshot', 'video']:
            self.assertIn(word, result.stderr)
        text = text.replace('**Merge.**', '- [ ] The operator reviews screenshot and video before merge. Save `media.log`.\n\n**Merge.**')
        result = self.call(text)
        self.assertEqual(result.returncode, 0, result.stderr)
