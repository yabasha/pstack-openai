# codex: partition-and-race

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "partition-and-race",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Run a swarm with coverage slices and a race. Declare the slices and race selection rule before dispatch. Verify exact revisions with a declared sampling method; inject one result missing required evidence, a repeated miss, and a dropout, then cancel one assignment.",
  "caseDefinition": {
    "id": "partition-and-race",
    "sourcePaths": [
      "skills/swarm/SKILL.md"
    ],
    "prompt": "Run a swarm with coverage slices and a race. Declare the slices and race selection rule before dispatch. Verify exact revisions with a declared sampling method; inject one result missing required evidence, a repeated miss, and a dropout, then cancel one assignment.",
    "requirements": [
      "Independent worker spawn, wait and result inspection when available and authorized",
      "Exact SHA and measurement method in assignment and result",
      "Distinct writable outputs and existing evidence artifacts",
      "Stop, terminal inspection and artifact quarantine for cancellation"
    ],
    "expectedFull": "Declare each partition slice and first pass, rank all or best-of race rule before dispatch. Record exact SHAs and method including sample count, sample definition and order. Reject invalid evidence, retry the same assignment at most once and leave a second miss as a gap. Continue with N-1 after a dropout and disclose it. Aggregate coverage only with results for every required slice. Inspect artifacts and quarantine cancelled partial output; report table, evidenced issues, gaps, dropouts and the declared race rule.",
    "expectedReduced": "Authorized sequential slices retain revisions, method, evidence checks and visible gaps, and explicitly report reduced capability without claiming independent workers, background execution, model diversity or race parity. Missing cancellation or persistence bindings remain visible.",
    "expectedBlocked": "Unavailable or denied worker execution blocks full swarm behavior. Missing exact required model, source revision, artifact access or permission blocks the affected assignment. An unobserved stop leaves termination unverified and partial artifacts excluded.",
    "forbiddenClaims": [
      "Sequential work proves independent workers or race parity",
      "Missing SHA, method, artifacts or coverage counts as PASS",
      "More than one retry for invalid SHA or method evidence",
      "Requested models prove actual models or diversity",
      "Cancellation notification proves termination without terminal inspection",
      "Unapproved external action or cloud setup is authorized by swarm"
    ],
    "caseFile": "docs/parity/cases/skills/swarm.json"
  },
  "registry": {
    "caseId": "partition-and-race",
    "caseFile": "docs/parity/cases/skills/swarm.json",
    "sourcePaths": [
      "skills/swarm/SKILL.md"
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
        "execution",
        "writes"
      ],
      "reduced-pass": []
    },
    "requiredMethod": "swarm"
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
