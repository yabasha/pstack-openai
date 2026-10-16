# codex: trace-path

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "trace-path",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Explain how a supplied request execution path works, from entry point through its downstream calls. Cite actual files and disclose whether explorers ran independently.",
  "caseDefinition": {
    "id": "trace-path",
    "sourcePaths": [
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md"
    ],
    "prompt": "Explain how a supplied request execution path works, from entry point through its downstream calls. Cite actual files and disclose whether explorers ran independently.",
    "requirements": [
      "Readable supplied codebase and execution path",
      "Observed worker operations for independent exploration and synthesis"
    ],
    "expectedFull": "Choose the simple or complex path. Complex work uses 2 to 4 distinct read-only explorers and one explainer; simple work uses one read-only explainer. Cite actual read files, functions, data flow and relevant line numbers; reconcile conflicting findings against code and retain open questions.",
    "expectedReduced": "When workers are absent, disclose reduced capability and sequential exploration. Apply the same explorer and explainer roles in sequence, cite actual files along the supplied path, and retain unknown links without claiming independent workers.",
    "expectedBlocked": "When required source cannot be read or permission is denied, identify the unavailable path and explain the resulting gap without inventing execution flow.",
    "forbiddenClaims": [
      "Independent explorers without observed spawn and result inspection",
      "Runtime behavior inferred only from names",
      "Actual model selection or host pass without evidence",
      "Complete flow when source links remain untraced"
    ],
    "caseFile": "docs/parity/cases/skills/how.json"
  },
  "registry": {
    "caseId": "trace-path",
    "caseFile": "docs/parity/cases/skills/how.json",
    "sourcePaths": [
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md"
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
        "inspect-result"
      ],
      "reduced-pass": [
        "read"
      ]
    },
    "executionModes": {
      "pass": [
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
