# chatgpt: migration-units

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "migration-units",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#17",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Plan a multi-step schema migration and its commit delivery. Give each ordered unit a specific check, show when the next unit can begin, and handle an unavailable test runner or unauthorized Git operation.",
  "caseDefinition": {
    "id": "migration-units",
    "sourcePaths": [
      "skills/principle-sequence-verifiable-units/SKILL.md"
    ],
    "prompt": "Plan a multi-step schema migration and its commit delivery. Give each ordered unit a specific check, show when the next unit can begin, and handle an unavailable test runner or unauthorized Git operation.",
    "requirements": [
      "Each ordered unit ends in a specific check.",
      "Start from a known-good baseline and verify one change before the next.",
      "Order independently landable commits and PRs so a reviewer can replay the argument.",
      "Preserve authorization and observed execution limits."
    ],
    "expectedFull": "Inspect a clean trunk baseline and rebase when authorized. Every ordered migration unit identifies its known-good start, one change and concrete check; advance only on green. Delivery uses a failing test before its fix, or another justified order such as subtraction before reshape, baseline before treatment or scaffold before feature. Every commit lands on its own. Use the prove-it-works and build-the-lever principles to keep checks real and cheap.",
    "expectedReduced": "When execution or Git writes are unavailable or unauthorized, provide a reduced ordered migration and delivery plan with a concrete check per unit. State which checks and Git operations were not performed; do not treat an unrun check as green.",
    "expectedBlocked": "Block advancement past a failed or unavailable required check and identify the missing capability or permission. Preserve the current unit for diagnosis.",
    "forbiddenClaims": [
      "An unrun or failed check is green.",
      "A batch check replaces verification of each unit.",
      "A delivery plan proves independently landable commits or actual host execution.",
      "The principle authorizes rebase, commit or PR writes without permission."
    ],
    "caseFile": "docs/parity/cases/skills/principle-sequence-verifiable-units.json"
  },
  "registry": {
    "caseId": "migration-units",
    "caseFile": "docs/parity/cases/skills/principle-sequence-verifiable-units.json",
    "sourcePaths": [
      "skills/principle-sequence-verifiable-units/SKILL.md"
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
      "pass": [],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-chatgpt-01-04.json#17",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 17,
      "host": "chatgpt",
      "caseId": "migration-units",
      "status": "reduced-pass",
      "grade": {
        "caseId": "migration-units",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Concrete schema/source baseline",
          "Observed per-unit checks and authorized Git delivery"
        ],
        "review": "Provides ordered baseline/schema/backfill/caller/removal units with concrete checks and gated advancement, plus delivery order and explicit unrun Git/runtime limits. Missing concrete schema makes this provisional rather than a completed migration.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/migration-units/result.json",
        "variantReview": [
          {
            "name": "ordered plan",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "known-good baseline",
            "reportedObservation": "blocked no actual schema/check runner",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "per-unit checks",
            "reportedObservation": "blocked Bun absent",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "Git delivery",
            "reportedObservation": "blocked no authorization",
            "assessment": "blocked-or-partial"
          }
        ],
        "limits": [
          "Bun absent; no Node/Python substitution.",
          "No live external actions.",
          "No model identity/full Git task revision observed.",
          "Local artifacts retained; durable persistence unverified.",
          "Retained responses and model-captured raw tool envelopes have early capture gaps/truncation; no blanket independent verification of all tool returns.",
          "Actual task Git revision unavailable; source-freeze binding is separate."
        ],
        "reviewedBy": "independent case_fixture_audit reviewer",
        "sourceCaseFile": "docs/parity/cases/skills/principle-sequence-verifiable-units.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence",
        "observedVersusReported": "Direct response and saved artifacts reviewed; script/runtime behavior receives no credit without matching observed execution."
      },
      "topLevelContext": {
        "gradingNotes": [
          "Independent contract review of original batches 01..04, not the evaluated model self-grade.",
          "Root independently observed actual native dispatches, reads and commands during a 21m31s turn; retained exact tool returns are model-captured and are not all independently verified.",
          "Early missing raw envelopes and host-render truncation remain evidence limits; artifact checks/aggregation and source availability do not reconstruct unseen tool output.",
          "Bun was absent in the cloud runtime. No JavaScript/Python substitute or proxy execution receives workflow credit; shell/jq preparation, source reading and artifact administration prove only those operations.",
          "Installed operative source freeze was independently byte-verified by root before this review. This is separate from unavailable actual task Git revision and does not invent a Git checkout.",
          "Canonical agents/*.md may map to installed references/agent-prompts/*.md. Failed old path followed by observed mapped fallback is legitimate, not automatically missing source.",
          "Two invented timestamp placeholders in another batch remain original errors despite appended corrections; neither is accepted as original runtime evidence.",
          "Text-only supplied draft/recipe branches can pass without runtime. Missing required implementation or execution stays reduced/blocked; an observed contract violation is fail."
        ]
      },
      "response": {
        "text": "Treat this as a plan, with no Git action. Unit 0 records a known-good baseline using the current schema contract and migration smoke check. Unit 1 adds the new schema shape and a literal compatibility contract; verify old and new reads. Unit 2 backfills data with a count-and-content reconciliation and rerun/idempotency check. Unit 3 switches callers and verifies the real read/write path. Unit 4 removes old fields only after no old callers remain and verifies a fresh and upgraded database. Begin each unit only after its named check is observed. Order delivery as baseline, failing regression, fix and cleanup, each independently reviewable. Exact schema is missing so this is provisional. With Bun absent the runner gate blocks implementation advancement; unauthorized rebase/commit/PR operations remain unperformed.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/migration-units/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/migration-units/result.json",
          "sha256": "bf5f15f4bd9839064d24f41c1f06100191913a29250861e28aa0012a3d8162df",
          "bytes": 1736
        },
        "extraction": "Actual response field when present; otherwise complete retained JSON"
      },
      "evidence": {
        "cloudCaptureIdentity": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "sha256": "667b5681288f125d3857df0388ae65288954542d8545c2b44a420635baa66c49",
            "bytes": 430462
          }
        ],
        "cloudCaptureLimit": "Shared model-captured log identity; attribution/actual operation credit remains limited to independently reviewed case locators and UI corroboration, not every log record.",
        "rawTraces": [],
        "retainedEvidence": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/checkpoint-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/checkpoint-tool.json",
            "sha256": "670a2c14d83c250d48f126dc3441653bc5a6fc2197f4fedecfe8b90a5f9e5296",
            "bytes": 770
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/required-companions-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/required-companions-tool.json",
            "sha256": "c821110b84d2270e05324a05fc8fb8387270bd8df8fb657592c9635d78974a0c",
            "bytes": 58320
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/migration-units/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/migration-units/result.json",
      "sha256": "bf5f15f4bd9839064d24f41c1f06100191913a29250861e28aa0012a3d8162df",
      "bytes": 1736,
      "owners": [
        "grades-chatgpt-01-04.json#17"
      ],
      "text": "{\n  \"caseId\": \"migration-units\",\n  \"batch\": \"batch-03\",\n  \"actualResponse\": \"Treat this as a plan, with no Git action. Unit 0 records a known-good baseline using the current schema contract and migration smoke check. Unit 1 adds the new schema shape and a literal compatibility contract; verify old and new reads. Unit 2 backfills data with a count-and-content reconciliation and rerun/idempotency check. Unit 3 switches callers and verifies the real read/write path. Unit 4 removes old fields only after no old callers remain and verifies a fresh and upgraded database. Begin each unit only after its named check is observed. Order delivery as baseline, failing regression, fix and cleanup, each independently reviewable. Exact schema is missing so this is provisional. With Bun absent the runner gate blocks implementation advancement; unauthorized rebase/commit/PR operations remain unperformed.\",\n  \"observedOperations\": [\n    \"named case and installed sources read using tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/required-companions-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"ordered plan\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"known-good baseline\",\n      \"observation\": \"blocked no actual schema/check runner\"\n    },\n    {\n      \"name\": \"per-unit checks\",\n      \"observation\": \"blocked Bun absent\"\n    },\n    {\n      \"name\": \"Git delivery\",\n      \"observation\": \"blocked no authorization\"\n    }\n  ],\n  \"limits\": [\n    \"Bun absent; no Node/Python substitution.\",\n    \"No live external actions.\",\n    \"No model identity/full Git task revision observed.\",\n    \"Local artifacts retained; durable persistence unverified.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/migration-units/case.json",
      "owner": "grades-chatgpt-01-04.json#17",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/migration-units/input",
      "owner": "grades-chatgpt-01-04.json#17",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/migration-units/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#17",
      "reason": "copied source/input or administrative evaluator helper"
    }
  ],
  "globalLimits": [
    "Orchestrator receipt durations can include controller pauses; they are not inferred native case execution times or benchmark measurements.",
    "Only the supplied frozen f462 source is bound by this reviewed baseline; no later operative tree or current release acceptance is established.",
    "Cloud UI corroborates native dispatch/read/command activity in specified turns, not every exact argument, raw output, exit code or model-captured receipt. Early raw capture gaps and truncation remain explicit.",
    "The two invented cloud timestamps remain retained errors despite appended correction.",
    "Native event metadata proves retained trace identity and locators; per-case independent grade determines qualitative result. File counts, test selfgrades and proxy scripts never generate grades.",
    "Input Git revisions, observed actual models, persistence, external service, scheduler and live-surface proof remain exactly as limited in each attempt.",
    "Implementation/test/log projections are source/artifact bytes for review, not independent runtime confirmation. Copied source skill blobs, inputs/before/dependencies/Git and binary files are omitted; each text file is capped at 1 MiB with explicit skip entries.",
    "Existing historical report contents are not imported. Root may append them separately."
  ]
}
```
