# chatgpt: dense-doc

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "dense-doc",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#6",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Rewrite this how-to without changing behavior: In order to configure the proto import ratchet budget script parameters, use budget.json. It is important to note that budget.mjs counts files that import protos. If the count exceeds the budget, CI fails. Run budget.mjs --write only when lowering the budget.",
  "caseDefinition": {
    "id": "dense-doc",
    "sourcePaths": [
      "skills/technical-writing/SKILL.md"
    ],
    "prompt": "Rewrite this how-to without changing behavior: In order to configure the proto import ratchet budget script parameters, use budget.json. It is important to note that budget.mjs counts files that import protos. If the count exceeds the budget, CI fails. Run budget.mjs --write only when lowering the budget.",
    "requirements": [
      "Read the supplied document and preserve its how-to purpose.",
      "Preserve budget.mjs, budget.json, --write, CI, the count condition, and the lower-only restriction.",
      "Apply all four layers and the unslop skill; do not invent facts."
    ],
    "expectedFull": "Remove filler, retain every named symbol and condition, and keep a clear how-to purpose. Apply Diátaxis, reader-directed sentences, STE rules, Global English, and unslop. Provide the rewrite or authorized document edit; propose any new abstract-metaphor offender with a diff without editing unslop.",
    "expectedReduced": "If required source text is incomplete or unslop is unavailable, identify the missing input or dependency and label the review partial. Returning the requested supplied-text rewrite in conversation is full direct completion; a specifically requested saved edit still requires an observed authorized write.",
    "expectedBlocked": "If no document text can be read or supplied, state the missing input and do not invent a rewrite or claim review completion.",
    "forbiddenClaims": [
      "Changing real symbol names or lower-only --write behavior.",
      "Claiming unslop was applied without reading it.",
      "Claiming edits were saved without observed authorized writes.",
      "Claiming host enforcement of disable-model-invocation metadata or host parity from structural validation."
    ],
    "caseFile": "docs/parity/cases/skills/technical-writing.json"
  },
  "registry": {
    "caseId": "dense-doc",
    "caseFile": "docs/parity/cases/skills/technical-writing.json",
    "sourcePaths": [
      "skills/technical-writing/SKILL.md"
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
        "supplied-input",
        "response",
        "review-outcome"
      ],
      "reduced-pass": [
        "supplied-input",
        "response",
        "review-outcome"
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
      "attemptId": "grades-chatgpt-01-04.json#6",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 6,
      "host": "chatgpt",
      "caseId": "dense-doc",
      "status": "pass",
      "grade": {
        "caseId": "dense-doc",
        "host": "chatgpt",
        "status": "pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "supplied-input",
          "response",
          "review-outcome"
        ],
        "missing": [],
        "review": "Direct supplied-text rewrite preserves budget.json, budget.mjs, proto-import counting, conditional CI failure and --write only when lowering the budget. It removes filler and retains how-to purpose. No script execution or saved edit is required by this direct branch.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dense-doc/result.json",
        "variantReview": [
          {
            "name": "supplied rewrite",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "Diataxis/Google/STE/Global English review",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "unslop dependency",
            "reportedObservation": "attempted source read",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          }
        ],
        "limits": [
          "No script execution: command -v bun exit 1.",
          "No external service/account operations.",
          "No observed package Git SHA or model identity.",
          "Local artifacts only; durable persistence untested.",
          "Retained responses and model-captured raw tool envelopes have early capture gaps/truncation; no blanket independent verification of all tool returns.",
          "Actual task Git revision unavailable; source-freeze binding is separate."
        ],
        "reviewedBy": "independent case_fixture_audit reviewer",
        "sourceCaseFile": "docs/parity/cases/skills/technical-writing.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence",
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
        "text": "Use budget.json to configure the script. budget.mjs counts files that import protos. If the count exceeds the budget, CI fails. Run budget.mjs --write only when lowering the budget. This preserves the how-to purpose, uses direct instructions, keeps the condition with its consequence and keeps only next to the lower-only restriction. I applied the complete unslop source without editing it.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dense-doc/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dense-doc/result.json",
          "sha256": "649ce5852496c489cd9ffe48a7192f2f4a9202a9231b9f8e50c76849549e1027",
          "bytes": 1154
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/actual-diffs-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/actual-diffs-tool.json",
            "sha256": "9c56bf96534fec4fb5a250108c99470239ddde7df96ae7833e3dd8d1ae0b371e",
            "bytes": 6155
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/read3-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/read3-tool.json",
            "sha256": "660fa99f9c84d5ec913f03e7c1fc3bb5f2b5fd9121f35275ca5d029277ea37fa",
            "bytes": 40695
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/read4-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/read4-tool.json",
            "sha256": "b0333000e00eba1939a09afc0c196151f2cd24ac784c4fe0a1ad605675532d94",
            "bytes": 48493
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/write1-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/write1-tool.json",
            "sha256": "617547cd73494b82fb01aa9d3e43fc21405f0d67cd9bfccd01cb191d0579ff5f",
            "bytes": 2795
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dense-doc/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dense-doc/result.json",
      "sha256": "649ce5852496c489cd9ffe48a7192f2f4a9202a9231b9f8e50c76849549e1027",
      "bytes": 1154,
      "owners": [
        "grades-chatgpt-01-04.json#6"
      ],
      "text": "{\n  \"caseId\": \"dense-doc\",\n  \"batch\": \"batch-01\",\n  \"actualResponse\": \"Use budget.json to configure the script. budget.mjs counts files that import protos. If the count exceeds the budget, CI fails. Run budget.mjs --write only when lowering the budget. This preserves the how-to purpose, uses direct instructions, keeps the condition with its consequence and keeps only next to the lower-only restriction. I applied the complete unslop source without editing it.\",\n  \"observedOperations\": [\n    \"case/source files read through tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"supplied rewrite\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"Diataxis/Google/STE/Global English review\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"unslop dependency\",\n      \"observation\": \"attempted source read\"\n    }\n  ],\n  \"limits\": [\n    \"No script execution: command -v bun exit 1.\",\n    \"No external service/account operations.\",\n    \"No observed package Git SHA or model identity.\",\n    \"Local artifacts only; durable persistence untested.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dense-doc/case.json",
      "owner": "grades-chatgpt-01-04.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dense-doc/input",
      "owner": "grades-chatgpt-01-04.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dense-doc/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#6",
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
