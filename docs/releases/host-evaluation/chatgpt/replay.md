# chatgpt: replay

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "replay",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#26",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "An interrupted job may already have sent a payment request. Design recovery for a retry, including partial local state, stale locks and a destination whose prior outcome is unknown.",
  "caseDefinition": {
    "id": "replay",
    "sourcePaths": [
      "skills/principle-make-operations-idempotent/SKILL.md"
    ],
    "prompt": "An interrupted job may already have sent a payment request. Design recovery for a retry, including partial local state, stale locks and a destination whose prior outcome is unknown.",
    "requirements": [
      "Inspect the stable prior action identity and destination outcome before recovery.",
      "Preserve explicit authorization and observed capabilities for external writes.",
      "Exercise repeated runs and crashes at each possible point; reconcile partial state."
    ],
    "expectedFull": "The retry converges to the same end state through reconciliation and a destination-appropriate idempotency mechanism. It adopts live sessions, removes stale artifacts by content equivalence, detects stale PID locks and regenerates fresh scheduling input. Completed external actions are recognized without blind replay; unknown outcomes block replay.",
    "expectedReduced": "Without destination inspection or authorized execution, provide a reduced recovery design and state which checks and actions were not performed. Unknown prior outcomes still block external replay.",
    "expectedBlocked": "If action identity, destination outcome or external permission cannot be established, block replay and identify the missing requirement.",
    "forbiddenClaims": [
      "Blind external replay is safe because the local operation is idempotent.",
      "Unknown action outcomes count as completion.",
      "A proposed reconciliation design proves host execution or unattended recovery."
    ],
    "caseFile": "docs/parity/cases/skills/principle-make-operations-idempotent.json"
  },
  "registry": {
    "caseId": "replay",
    "caseFile": "docs/parity/cases/skills/principle-make-operations-idempotent.json",
    "sourcePaths": [
      "skills/principle-make-operations-idempotent/SKILL.md"
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
      "attemptId": "grades-chatgpt-01-04.json#26",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 26,
      "host": "chatgpt",
      "caseId": "replay",
      "status": "reduced-pass",
      "grade": {
        "caseId": "replay",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Matching payment identity/destination observation",
          "Observed repeat/crash reconciliation and destination idempotency"
        ],
        "review": "Provides a useful state/idempotency/lock reconciliation design and blocks unknown-outcome payment replay. No matching payment action/destination receipt or repeated-run/crash-window execution supports actual convergence.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/replay/result.json",
        "variantReview": [
          {
            "name": "recovery design",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "payment identity/destination inspection",
            "reportedObservation": "blocked not supplied/live actions forbidden",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "already complete/explicitly absent/unknown branches",
            "reportedObservation": "attempted textual decision boundaries",
            "assessment": "textual-or-proposed-only"
          },
          {
            "name": "repeated runs/all crash windows/stale lock probes",
            "reportedObservation": "blocked Bun absent",
            "assessment": "blocked-or-partial"
          }
        ],
        "limits": [
          "No Bun execution or alternate runtime.",
          "No live external actions/commits/settings changes.",
          "No observed task Git revision/model identity.",
          "Source fixtures inert; local persistence only.",
          "Retained responses and model-captured raw tool envelopes have early capture gaps/truncation; no blanket independent verification of all tool returns.",
          "Actual task Git revision unavailable; source-freeze binding is separate."
        ],
        "reviewedBy": "independent case_fixture_audit reviewer",
        "sourceCaseFile": "docs/parity/cases/skills/principle-make-operations-idempotent.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence",
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
        "text": "Keep the stable payment action ID as the destination idempotency key and an immutable local intent with destination and permission. Recovery first reads prior action identity and destination outcome. If already completed, reconcile the local result without resending; if explicitly absent, retry only within authorization and the destination's observed idempotency guarantee; if unknown, block replay. Preserve partial intents, distinguish prepared/dispatched/confirmed states, and reconcile stale locks using process/lease ownership evidence rather than timestamp deletion alone. The supplied forge action is a ticket record, not a payment receipt. No actual payment ID, destination outcome or safe recovery binding exists. Repeated runs and crashes before intent, after intent, after dispatch and before local confirmation remain unexercised because Bun is absent; no external request was made.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/replay/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/replay/result.json",
          "sha256": "9959f20140702168155d0b79e73d57a6f1d11a0cfb9680a8248efc791e4b47cb",
          "bytes": 1971
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/checkpoint-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/checkpoint-tool.json",
            "sha256": "1df96ab7545558223a3c050be004d8a053fb0822a09132fd04b811b37a5caa10",
            "bytes": 1439
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/conflict-inspect-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/conflict-inspect-tool.json",
            "sha256": "bd33bdc4673ed1bc05eb737bc930299894deb9e1ce1f63d6b5553b941d6acedd",
            "bytes": 717
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/final-checkpoint-and-bun-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/final-checkpoint-and-bun-tool.json",
            "sha256": "30713134ca12a1fe6735284d2487f95cc2db675826f38bc8150e474760a25a8f",
            "bytes": 1646
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-and-mode-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-and-mode-tool.json",
            "sha256": "956feba3fb45b2ce44ee67c8b6354c8c76e41531f748dc384abcb8972fb3c8ac",
            "bytes": 48048
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-branch-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-branch-tool.json",
            "sha256": "a11a29d31b0f740b48beaa5b0500b6327cbface9b66bdfb77a963941a376dc3c",
            "bytes": 419
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-log-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-log-tool.json",
            "sha256": "17f7de712f41c8307ee4122061afea11aa05641c81c10d8801974e7c8b47342e",
            "bytes": 414
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-rev-parse-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-rev-parse-tool.json",
            "sha256": "24e30f9bab0a6115cf8ed66e20e5ce6e51a59fcbad9025fd50eb677bb11d3357",
            "bytes": 413
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-status-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-status-tool.json",
            "sha256": "1a27a70ac423417b61150f03a2ae57b9da068697e632ed30588896c99a9d7336",
            "bytes": 413
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/owned-dirs-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/owned-dirs-tool.json",
            "sha256": "25eb472070400045f84cc8a5f3eb6c1b1f760df9a2396e15ee41a156234ab072",
            "bytes": 411
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/proposals-readback-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/proposals-readback-tool.json",
            "sha256": "f682f5f43dc511286c869dd13047e9edda92e42d11f612b803f0efbb13fc6ca2",
            "bytes": 14018
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/replay/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/replay/result.json",
      "sha256": "9959f20140702168155d0b79e73d57a6f1d11a0cfb9680a8248efc791e4b47cb",
      "bytes": 1971,
      "owners": [
        "grades-chatgpt-01-04.json#26"
      ],
      "text": "{\n  \"caseId\": \"replay\",\n  \"batch\": \"batch-04\",\n  \"actualResponse\": \"Keep the stable payment action ID as the destination idempotency key and an immutable local intent with destination and permission. Recovery first reads prior action identity and destination outcome. If already completed, reconcile the local result without resending; if explicitly absent, retry only within authorization and the destination's observed idempotency guarantee; if unknown, block replay. Preserve partial intents, distinguish prepared/dispatched/confirmed states, and reconcile stale locks using process/lease ownership evidence rather than timestamp deletion alone. The supplied forge action is a ticket record, not a payment receipt. No actual payment ID, destination outcome or safe recovery binding exists. Repeated runs and crashes before intent, after intent, after dispatch and before local confirmation remain unexercised because Bun is absent; no external request was made.\",\n  \"observedOperations\": [\n    \"case.json and named installed sources read via tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/proposals-readback-tool.json\",\n    \"../../evidence/git-and-mode-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"recovery design\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"payment identity/destination inspection\",\n      \"observation\": \"blocked not supplied/live actions forbidden\"\n    },\n    {\n      \"name\": \"already complete/explicitly absent/unknown branches\",\n      \"observation\": \"attempted textual decision boundaries\"\n    },\n    {\n      \"name\": \"repeated runs/all crash windows/stale lock probes\",\n      \"observation\": \"blocked Bun absent\"\n    }\n  ],\n  \"limits\": [\n    \"No Bun execution or alternate runtime.\",\n    \"No live external actions/commits/settings changes.\",\n    \"No observed task Git revision/model identity.\",\n    \"Source fixtures inert; local persistence only.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/replay/case.json",
      "owner": "grades-chatgpt-01-04.json#26",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/replay/input",
      "owner": "grades-chatgpt-01-04.json#26",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/replay/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#26",
      "reason": "copied source/input or administrative evaluator helper"
    }
  ],
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
