"""Dependency audit integrity. These are structural tests, never host evidence."""
import copy
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "docs/parity/dependencies.json"
CRITICAL = {
    "create-skill": ["skills/automate-me/SKILL.md", "skills/reflect/SKILL.md", "skills/poteto-mode/playbooks/authoring-a-skill.md"],
    "deslop": ["skills/poteto-mode/SKILL.md", "skills/poteto-mode/playbooks/autopilot-full.md"],
    "control-cli": ["skills/poteto-mode/SKILL.md", "skills/poteto-mode/playbooks/shipping.md"],
    "control-ui": ["skills/poteto-mode/SKILL.md", "skills/poteto-mode/playbooks/shipping.md"],
    "orch": ["skills/poteto-mode/playbooks/orchestrate.md"],
    "watch-pr": ["skills/poteto-mode/playbooks/shipping.md", "skills/poteto-mode/playbooks/babysit.md"],
    "check-plan": ["skills/poteto-mode/playbooks/multi-phase-plan.md"],
    "worktree-audit": ["skills/poteto-mode/playbooks/worktree-cleanup.md"],
}


def errors(data):
    failures = []
    inventory = json.loads((ROOT / "docs/parity/inventory.json").read_text())
    rows = data.get("sourceAudit", [])
    by_source = {r["sourcePath"]: r for r in rows}
    if len(rows) != len(by_source) or set(by_source) != {r["upstreamPath"] for r in inventory}:
        failures.append("source coverage")
    dependencies = data.get("dependencies", [])
    by_id = {d["id"]: d for d in dependencies}
    if len(dependencies) != len(by_id):
        failures.append("duplicate dependency")
    for source in inventory:
        audit = by_source.get(source["upstreamPath"], {})
        if audit.get("sourceSha256") != source["upstreamSha256"]:
            failures.append("source hash: " + source["upstreamPath"])
        if audit.get("packageDependencies") != source["dependencies"]:
            failures.append("package dependency coverage: " + source["upstreamPath"])
        for path in audit.get("packageDependencies", []):
            if not (ROOT / path).exists():
                failures.append("missing package binding: " + path)
        destination = ROOT / source["destinationPath"]
        if audit.get("destinationSha256") != hashlib.sha256(destination.read_bytes()).hexdigest():
            failures.append("stale destination: " + source["destinationPath"])
        reference_ids = [ref["dependencyId"] for ref in audit.get("references", [])]
        declared_ids = audit.get("dependencyIds", [])
        if set(reference_ids) != set(declared_ids):
            failures.append("reference index mismatch: " + source["upstreamPath"])
        if len(reference_ids) != len(set(reference_ids)):
            failures.append("duplicate reference: " + source["upstreamPath"])
        for dep in reference_ids:
            if dep not in by_id:
                failures.append("unknown reference: " + dep)
            elif source["upstreamPath"] not in by_id[dep].get("callers", []):
                failures.append("unaccounted reference caller: " + source["upstreamPath"] + ":" + dep)
        for dep in declared_ids:
            if dep not in by_id or source["upstreamPath"] not in by_id[dep].get("callers", []):
                failures.append("unaccounted dependency: " + dep)
        if destination.suffix == ".md":
            text = destination.read_text()
            for dep in ("create-skill", "deslop", "control-cli", "control-ui"):
                if re.search(r"(?<![\w-])" + dep + r"(?![\w-])", text) and dep not in audit.get("dependencyIds", []):
                    failures.append("hidden companion: " + source["upstreamPath"] + ":" + dep)
    for dep, callers in CRITICAL.items():
        if dep not in by_id or not set(callers) <= set(by_id[dep].get("callers", [])):
            failures.append("missing critical caller: " + dep)
    for d in dependencies:
        for field in ("callers", "requiredProof", "blockedReason", "setupEffects", "evidence"):
            if not d.get(field):
                failures.append("missing " + field + ": " + d["id"])
        if d.get("executionStatus") != "blocked":
            failures.append("unobserved execution: " + d["id"])
        if d.get("binding") is not None:
            for p in d["binding"].get("paths", []):
                if not (ROOT / p).exists():
                    failures.append("missing binding: " + p)
        for caller in d.get("callers", []):
            if caller not in by_source or d["id"] not in by_source[caller]["dependencyIds"]:
                failures.append("orphan caller: " + caller)
    return failures


class DependencyTests(unittest.TestCase):
    def load(self):
        return json.loads(MANIFEST.read_text())

    def test_no_hidden_dependencies(self):
        self.assertEqual(errors(self.load()), [])

    def test_missing_control_is_blocked(self):
        data = self.load()
        for name in ("control-cli", "control-ui"):
            dep = next(d for d in data["dependencies"] if d["id"] == name)
            self.assertIsNone(dep["binding"])
            self.assertEqual(dep["executionStatus"], "blocked")
            self.assertIn("real", dep["requiredProof"].lower())
            self.assertIn("name", dep["blockedReason"].lower())
        broken = copy.deepcopy(data)
        next(d for d in broken["dependencies"] if d["id"] == "control-ui")["executionStatus"] = "pass"
        self.assertIn("unobserved execution: control-ui", errors(broken))

    def test_deleting_companion_or_caller_is_detected(self):
        data = self.load()
        data["dependencies"] = [d for d in data["dependencies"] if d["id"] != "deslop"]
        self.assertIn("missing critical caller: deslop", errors(data))
        data = self.load()
        next(r for r in data["sourceAudit"] if r["sourcePath"] == "skills/poteto-mode/SKILL.md")["dependencyIds"].remove("control-cli")
        self.assertTrue(any("hidden companion:" in e for e in errors(data)))

    def test_unknown_reference_is_rejected(self):
        data = self.load()
        data["sourceAudit"][0]["references"].append({
            "dependencyId": "unknown-review-dependency",
            "sourceLines": [1],
            "destinationLines": [],
        })
        self.assertIn("unknown reference: unknown-review-dependency", errors(data))

    def test_removing_disposition_cannot_hide_retained_references(self):
        data = self.load()
        name = "profile-trace-sqlite"
        data["dependencies"] = [d for d in data["dependencies"] if d["id"] != name]
        for row in data["sourceAudit"]:
            row["dependencyIds"] = [dep for dep in row["dependencyIds"] if dep != name]
        self.assertIn("unknown reference: profile-trace-sqlite", errors(data))

    def test_missing_reference_for_declared_dependency_is_rejected(self):
        data = self.load()
        row = next(r for r in data["sourceAudit"] if "profile-trace-sqlite" in r["dependencyIds"])
        row["references"] = [r for r in row["references"] if r["dependencyId"] != "profile-trace-sqlite"]
        self.assertIn("reference index mismatch: " + row["sourcePath"], errors(data))

    def test_incomplete_proof_and_stale_audit_are_rejected(self):
        data = self.load()
        next(d for d in data["dependencies"] if d["id"] == "orch")["requiredProof"] = ""
        self.assertIn("missing requiredProof: orch", errors(data))
        data = self.load()
        row = next(r for r in data["sourceAudit"] if r["sourcePath"] == "skills/poteto-mode/SKILL.md")
        row["destinationSha256"] = "0" * 64
        self.assertIn("stale destination: skills/poteto-mode/SKILL.md", errors(data))

    def test_audit_counts(self):
        data = self.load()
        rows = data["sourceAudit"]
        from tools.baseline_policy import validate_policy
        inventory = json.loads((ROOT / "docs/parity/inventory.json").read_text())
        counts = validate_policy(ROOT, inventory)
        self.assertEqual({r["sourcePath"] for r in rows}, {r["upstreamPath"] for r in inventory})
        self.assertEqual(len(rows), counts["sourceFiles"])
        self.assertEqual(sum(r["kind"] == "root-skill" for r in rows), counts["leafSkills"])
        self.assertEqual(sum(r["kind"] == "playbook" for r in rows), counts["playbooks"])
        self.assertEqual(data["counts"], dict(files=counts["sourceFiles"], rootSkills=counts["leafSkills"],
                         supportIncludingPlaybooks=counts["supportFiles"], playbooks=counts["playbooks"]))

    def test_selected_helpers_remain_binding(self):
        data = self.load()
        for name in ("orch", "watch-pr", "check-plan", "worktree-audit", "decision-log"):
            dep = next(d for d in data["dependencies"] if d["id"] == name)
            self.assertEqual(dep["binding"]["kind"], "selected-runtime")
            self.assertTrue(dep["binding"]["paths"])
            self.assertEqual(dep["executionStatus"], "blocked")

    def test_case_is_behavioral_and_blocked(self):
        case = json.loads((ROOT / "docs/parity/cases/dependencies.json").read_text())
        registry = json.loads((ROOT / "docs/parity/case-registry.json").read_text())
        entry = next(e for e in registry["entries"] if e["caseId"] == case["id"])
        self.assertFalse(entry["structuralOnly"])
        self.assertEqual(entry["requiredHosts"], ["chatgpt", "codex"])
        inventory = json.loads((ROOT / "docs/parity/inventory.json").read_text())
        callers = [r for r in inventory if r["upstreamPath"] in case["sourcePaths"]]
        self.assertEqual({r["upstreamPath"] for r in callers}, set(case["sourcePaths"]))
        for host in entry["requiredHosts"]:
            statuses = {r["verification"][host]["status"] for r in callers}
            self.assertEqual(len(statuses), 1, f"Dependency caller statuses disagree for {host}")
            self.assertEqual(entry["hostStatus"][host], statuses.pop())
        self.assertEqual(entry["sourcePaths"], case["sourcePaths"])
        from tools.validate_package import schema_errors
        schema = json.loads((ROOT / "docs/parity/cases/schema.json").read_text())
        self.assertEqual(schema_errors(case, schema, "dependency case"), [])

    def test_blocked_case_receipts_cannot_be_promoted_to_pass(self):
        from tools.validate_evidence import validate_evidence
        for host in ("chatgpt", "codex"):
            with self.subTest(host=host):
                receipt = json.loads((ROOT / f"docs/parity/evidence/{host}/dependency-readiness.json").read_text())
                self.assertEqual(receipt["status"], "blocked")
                self.assertEqual(receipt["execution"], "unavailable")
                self.assertEqual(receipt["successfulOperations"], [])
                self.assertEqual(validate_evidence(receipt, receipt["packageCommit"], ROOT), [])
                for status in ("pass", "reduced-pass"):
                    promoted = copy.deepcopy(receipt)
                    promoted["status"] = status
                    failures = validate_evidence(promoted, receipt["packageCommit"], ROOT)
                    self.assertIn("execution: unavailable execution must be blocked or not-run", failures)
                    self.assertIn("dependency-readiness: missing required observation read", failures)
