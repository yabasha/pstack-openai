# codex: red-green

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "red-green",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Fix a bug with an obvious cheap local regression target using TDD. Show a real failing behavior test before fixing production code. Repeat with execution unavailable.",
  "caseDefinition": {
    "id": "red-green",
    "sourcePaths": [
      "skills/tdd/SKILL.md"
    ],
    "prompt": "Fix a bug with an obvious cheap local regression target using TDD. Show a real failing behavior test before fixing production code. Repeat with execution unavailable.",
    "requirements": [
      "An authorized code change and a clear cheap local test target.",
      "Available file access and execution with observed exit status and output for full evidence."
    ],
    "expectedFull": "Write a focused intended-behavior test first, observe its failure for the intended reason before changing production code, apply the smallest fix, and observe the same test passing. Report commands, failure output, passing output, and nearby validation. Correct passing or unrelated-failing tests before implementation edits.",
    "expectedReduced": "If a new test is impractical, explain why and use the closest useful executable regression check. Preserve observed failure and passing evidence when available; explicitly state any missing failing-before evidence.",
    "expectedBlocked": "If execution is unavailable or denied, mark the proposed failing-before and passing-after sequence unrun. Explain the missing capability and do not claim observed failure, success, or a demonstrated regression fix.",
    "forbiddenClaims": [
      "Claiming an unrun proposed sequence is red-green evidence.",
      "Calling a structural package check a failing behavior test.",
      "Changing assertions to match incorrect implementation or forcing expensive infrastructure.",
      "Assuming execution permission or automatic enforcement of invocation metadata."
    ],
    "caseFile": "docs/parity/cases/skills/tdd.json"
  },
  "registry": {
    "caseId": "red-green",
    "caseFile": "docs/parity/cases/skills/tdd.json",
    "sourcePaths": [
      "skills/tdd/SKILL.md"
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
