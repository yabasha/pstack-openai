# codex: scoped-history

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "scoped-history",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Recall my work on the cache subsystem in the active workspace over the last seven days. I supply a complete state capsule with paths, branch and change. Check current state independently. Repeat without the capsule, with three relevant chats, a shipped then reverted fix, unavailable error tracking, and one current PR status that contradicts history. Also distinguish a partial capsule, a single-session pickup, pure activity recall and an explicit all-history request.",
  "caseDefinition": {
    "id": "scoped-history",
    "sourcePaths": [
      "skills/recall/SKILL.md"
    ],
    "prompt": "Recall my work on the cache subsystem in the active workspace over the last seven days. I supply a complete state capsule with paths, branch and change. Check current state independently. Repeat without the capsule, with three relevant chats, a shipped then reverted fix, unavailable error tracking, and one current PR status that contradicts history. Also distinguish a partial capsule, a single-session pickup, pure activity recall and an explicit all-history request.",
    "requirements": [
      "Authorized scoped history and shared-record reads",
      "Independent workers for parallel mining when exposed and authorized",
      "Independent live file, git, PR and ticket state reads"
    ],
    "expectedFull": "State topic, workspace and exact time range before search; default recent to seven days and preserve explicit all. A complete supplied capsule skips mining, but named-target shared-record sweep and independent current-state checks still apply. A partial capsule cannot justify skipping needed history. For three chats, partition parallel investigators by real modification time, match topic and relevant regions, exclude current and noisy chats, return each chat schema with UUID citations and keep raw transcripts out of the parent. Sweep named targets through why source investigators concurrently, distinguish unavailable from searched-empty sources, and inspect full transcripts when actual agent actions matter. Report capsule of at most five bullets, every thread with one exact permitted status tag, at most five recurring problems including reverted fixes, and one concrete next move. Route one prior session to session-pickup, habits to automate-me and human-readable work summaries separately. Pure activity recall skips the shared-record sweep.",
    "expectedReduced": "When independent workers are unavailable, use authorized sequential scoped history and source passes and disclose reduced capability. A complete capsule still avoids mining. Missing history or live access remains explicit; historical claims do not establish current status. Cite retrieved UUIDs or observed host record identifiers and shared sources, preserve output caps, private visibility and exact status tags without inventing verification.",
    "expectedBlocked": "Denied or unavailable required history, shared source or live reads block the affected conclusion. Report gaps and what the supplied capsule supports, without claiming mined history, checked current state, independence or a completed thread. An unknown status cannot receive an invented done tag.",
    "forbiddenClaims": [
      "A complete capsule proves current state or permits skipping a named-target shared-record sweep",
      "A partial capsule is complete",
      "Sequential passes are independent parallel workers",
      "Unavailable sources are searched-empty results",
      "Transcript UUID ordering proves recency",
      "History proves a PR remains open or merged today",
      "All history silently means recent N",
      "Other-workspace history access without authorization",
      "Requested models prove observed models",
      "Missing evidence warrants verified uncommitted or merged status"
    ],
    "caseFile": "docs/parity/cases/skills/recall.json"
  },
  "registry": {
    "caseId": "scoped-history",
    "caseFile": "docs/parity/cases/skills/recall.json",
    "sourcePaths": [
      "skills/recall/SKILL.md"
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
