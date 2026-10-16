# codex: real-app-contract

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "real-app-contract",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Create a verification skill for this repo. Inspect its real app controls and existing harness, seed a feature map, and prove one feature if authorized tools are available. Retain the Notes example contracts as examples only.",
  "caseDefinition": {
    "id": "real-app-contract",
    "sourcePaths": [
      "skills/create-verification-skill/SKILL.md",
      "skills/create-verification-skill/references/feature-map-example/README.md",
      "skills/create-verification-skill/references/feature-map-example/create-note.md",
      "skills/create-verification-skill/references/feature-map-example/search.md"
    ],
    "prompt": "Create a verification skill for this repo. Inspect its real app controls and existing harness, seed a feature map, and prove one feature if authorized tools are available. Retain the Notes example contracts as examples only.",
    "requirements": [
      "Repository reads and authorized project-local writes",
      "Observed execution and app-driving tools for end-to-end proof",
      "Preserve all three feature-map examples and their exact commands",
      "Discover the active host project-local skill location and verify registration",
      "Follow the active workflow owner and permission boundaries"
    ],
    "expectedFull": "Inspect real routes, controls, commands and startup before authoring. Generate registered YAML metadata and Launch, Doctor, Drive, Evidence, Cleanup and Helpers sections using actual controls; seed the top 3-5 identifiable features with the prescribed four headings and all user entry points. Launch, doctor, drive one mapped feature, capture action, resulting state and side effects, clean up each attempt, then confirm evidence survives. Report observed proof only and point to /maintain-verification-skill without scheduling.",
    "expectedReduced": "When repository controls can be inspected and writes are authorized but execution or app-driving is unavailable, author a draft grounded in those controls. Mark verification not-run, name missing capabilities and unproved entry points; do not present the draft as a verified deliverable. If project-local registration is unconfirmed, report a portable draft with registration unverified.",
    "expectedBlocked": "If repository access or required authoring permission is unavailable, report the exact blocker and do not invent app controls or write files. If startup is broken, fix within authorization or report the precise failure before generation. Denied execution blocks proof and cannot count as a pass.",
    "forbiddenClaims": [
      "Notes example commands are real controls in an unrelated app",
      "An unexecuted generated skill is a verified deliverable",
      "A final screenshot alone proves the user action or side effects",
      "Skipped entry points are verified through another path",
      "A documented tool or project-local path proves discovery or successful execution",
      "Cleanup may delete evidence or kill processes by name",
      "Suggested cadence authorizes recurring scheduling"
    ],
    "caseFile": "docs/parity/cases/skills/create-verification-skill.json"
  },
  "registry": {
    "caseId": "real-app-contract",
    "caseFile": "docs/parity/cases/skills/create-verification-skill.json",
    "sourcePaths": [
      "skills/create-verification-skill/SKILL.md",
      "skills/create-verification-skill/references/feature-map-example/README.md",
      "skills/create-verification-skill/references/feature-map-example/create-note.md",
      "skills/create-verification-skill/references/feature-map-example/search.md"
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
