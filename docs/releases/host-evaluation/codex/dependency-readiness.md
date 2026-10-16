# codex: dependency-readiness

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "dependency-readiness",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Audit the current session before authoring a skill or verifying an app change. Use the dependency readiness records to name the selected authoring, review, control and repository-helper branches. Initially withhold control tools and installed helper metadata. Report what is blocked and what a local draft can establish. If the tester later supplies an authorized real driver and prepared helper copy, verify the exact caller contract and retain its action/result artifacts. Never install or enable a dependency to complete this case.",
  "caseDefinition": {
    "id": "dependency-readiness",
    "sourcePaths": [
      "skills/automate-me/SKILL.md",
      "skills/reflect/SKILL.md",
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/authoring-a-skill.md",
      "skills/poteto-mode/playbooks/shipping.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/scripts/bootstrap.ts",
      "automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md"
    ],
    "prompt": "Audit the current session before authoring a skill or verifying an app change. Use the dependency readiness records to name the selected authoring, review, control and repository-helper branches. Initially withhold control tools and installed helper metadata. Report what is blocked and what a local draft can establish. If the tester later supplies an authorized real driver and prepared helper copy, verify the exact caller contract and retain its action/result artifacts. Never install or enable a dependency to complete this case.",
    "requirements": [
      "Read the actual caller and available companion or helper contract, not only a skill name. Record exact exposed tool identifiers, denied or missing operations and observed outcomes.",
      "Missing control-cli or control-ui leaves real-surface verification blocked. A named alternative must satisfy the same revision, user-path and action/result proof before use.",
      "Missing create-skill leaves its required authoring loop unmet; provisional drafts and a manual structural checklist are reduced capability. Reflect application needs its required loop and approval.",
      "Missing deslop is an unmet review gate until an explicitly authorized replacement review completes. Unslop alone does not satisfy it.",
      "Selected orch and watch-pr helpers remain runtime bindings. Missing current package metadata blocks execution; do not install, bypass bootstrap or substitute historical snapshot results.",
      "Discover each repository, forge, integration and setup requirement. Keep authorizations separate for writes, credentials, enabling, networking and schedules.",
      "Retain current package commit, exact app/input revision and actual artifacts. Both hosts require their own observations; local tests establish only structural coverage."
    ],
    "expectedFull": "With separately supplied and authorized capabilities, reads resolve the exact authoring validator and real app driver, required authoring/review loops complete, selected helpers execute from the prepared copy, and inspected artifacts prove the requested actions and end states. Missing-capability trials still stop dependent work without setup side effects. Record precise tools and successful operations for each exercised branch.",
    "expectedReduced": "Authorized local drafting, source review or manual checklist work completes with inspected local artifacts. The response explicitly retains missing authoring loops, companion review, helper execution and real-control gates as unmet; no live verification or helper pass is claimed.",
    "expectedBlocked": "With controls, required authoring workflows, helper metadata or permissions absent, the dependent branch stops and names the missing proof and setup scope. No installation, plugin enablement, credential change, integration connection, schedule or external action occurs. Keep partial local drafts separate from completed verification.",
    "forbiddenClaims": [
      "A skill name, bundled prompt or documented command proves an exposed and successful capability.",
      "CI, a screenshot, fixtures or source inspection proves real user interaction.",
      "The historical isolated 37b68c8 snapshot passes prove current helper or host execution.",
      "Sequential roles are independent workers, or requested models are observed models.",
      "A setup approval also authorizes host loading, integrations, credentials or external actions."
    ],
    "caseFile": "docs/parity/cases/dependencies.json"
  },
  "registry": {
    "caseId": "dependency-readiness",
    "caseFile": "docs/parity/cases/dependencies.json",
    "sourcePaths": [
      "skills/automate-me/SKILL.md",
      "skills/reflect/SKILL.md",
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/authoring-a-skill.md",
      "skills/poteto-mode/playbooks/shipping.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "skills/poteto-mode/scripts/bootstrap.ts",
      "automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md"
    ],
    "requiredHosts": [
      "chatgpt",
      "codex"
    ],
    "structuralOnly": false,
    "hostStatus": {
      "chatgpt": "blocked",
      "codex": "blocked"
    },
    "requiredObservations": {
      "pass": [
        "read",
        "execution",
        "review-outcome"
      ],
      "reduced-pass": [
        "read"
      ]
    },
    "executionModes": {
      "pass": [
        "direct",
        "workers"
      ],
      "reduced-pass": [
        "direct",
        "sequential",
        "workers"
      ]
    },
    "requiredPermissions": {
      "pass": [
        "execution"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [],
  "artifactProjections": [],
  "skippedManifest": [],
  "globalLimits": [
    "Only the supplied frozen f462 source is bound by this reviewed baseline; no later operative tree or current release acceptance is established.",
    "Cloud UI corroborates native dispatch/read/command activity in specified turns, not every exact argument, raw output, exit code or model-captured receipt. Early raw capture gaps and truncation remain explicit.",
    "The two invented cloud timestamps remain retained errors despite appended correction.",
    "Native event metadata proves retained trace identity and locators; per-case independent grade determines qualitative result. File counts, test selfgrades and proxy scripts never generate grades.",
    "Task Git revisions, observed actual models, persistence, external service, scheduler and live-surface proof remain exactly as limited in each attempt.",
    "Implementation/test/log projections are source/artifact bytes for review, not independent runtime confirmation. Copied source skill blobs, inputs/before/dependencies/Git and binary files are omitted; each text file is capped at 1 MiB with explicit skip entries.",
    "Existing historical report contents are not imported. Root may append them separately."
  ]
}
```
