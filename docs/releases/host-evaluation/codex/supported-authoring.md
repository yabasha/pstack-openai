# codex: supported-authoring

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "supported-authoring",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Author or modify a skill with this playbook. Inspect the available authoring workflow and its validator. Preserve the skill voice, validate structural contracts, and report unknown trigger performance without assuming create-skill is installed or PR writes are authorized.",
  "caseDefinition": {
    "id": "supported-authoring",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/authoring-a-skill.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md"
    ],
    "prompt": "Author or modify a skill with this playbook. Inspect the available authoring workflow and its validator. Preserve the skill voice, validate structural contracts, and report unknown trigger performance without assuming create-skill is installed or PR writes are authorized.",
    "requirements": [
      "Inspect exposed capabilities and the available authoring workflow instructions and actual validator before use; identify the missing create-skill dependency.",
      "Preserve voice ownership, decision-changing prose, confusing-rule explanations, scope-matched tone, structural-source pointers, path delegation and proposals for recurring uncaptured workflows.",
      "Check name and description frontmatter, referenced files and cross-skill links; run structural test cases with fixtures and skip subjective tests.",
      "Apply Opening a PR only when its dependency, capabilities and authorization permit; preserve the skill artifact when PR delivery is deferred.",
      "Reply with skill summary, key design decisions and validation notes; distinguish observed results from unknown trigger performance."
    ],
    "expectedFull": "An available supported authoring workflow runs after its instructions and validator are inspected. The authored skill passes the observed structural checks and structural test cases. Subjective tests are skipped. The reply identifies the actual workflow, states create-skill is absent unless discovered, leaves unknown trigger performance unverified and reports observed authorized PR delivery or its explicit deferral.",
    "expectedReduced": "With authorized writes but no supported authoring workflow, produce only a provisional skill draft and manual checklist. Preserve the missing create-skill block, unexecuted validation and unknown trigger performance. If authoring and validation succeed but PR delivery is unavailable, retain the validated local skill and report the deferred PR dependency.",
    "expectedBlocked": "Without an available authoring workflow and without authorization or capability for a provisional draft, report the missing create-skill dependency and unavailable operation. Unavailable validation or PR delivery remains explicitly blocked or deferred; no completion claim substitutes for it.",
    "forbiddenClaims": [
      "create-skill shipped or executed without discovery and observed evidence.",
      "A provisional draft or manual checklist proves supported authoring execution or validator success.",
      "Structural checks prove trigger performance, subjective quality or host behavioral parity.",
      "A PR was created, commits made or external writes performed without authorization and observed results.",
      "Path delegation to another skill proves independent worker execution."
    ],
    "caseFile": "docs/parity/cases/playbooks/authoring-a-skill.json"
  },
  "registry": {
    "caseId": "supported-authoring",
    "caseFile": "docs/parity/cases/playbooks/authoring-a-skill.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/authoring-a-skill.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md"
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
        "review-outcome",
        "execution",
        "isolated-write"
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
        "execution",
        "writes"
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
