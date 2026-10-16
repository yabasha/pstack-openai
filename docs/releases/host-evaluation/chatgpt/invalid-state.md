# chatgpt: invalid-state

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "invalid-state",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#15",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Review a typed task model { completed: boolean; completedAt?: Date }, interchangeable UserId and OrderId strings, an unchecked JSON payload, and a switch over task states. Make invalid typed states unrepresentable or identify the actual language limit. Explain where a non-empty list is needed for head and why sum can keep a plain list.",
  "caseDefinition": {
    "id": "invalid-state",
    "sourcePaths": [
      "skills/principle-type-system-discipline/SKILL.md"
    ],
    "prompt": "Review a typed task model { completed: boolean; completedAt?: Date }, interchangeable UserId and OrderId strings, an unchecked JSON payload, and a switch over task states. Make invalid typed states unrepresentable or identify the actual language limit. Explain where a non-empty list is needed for head and why sum can keep a plain list.",
    "requirements": [
      "Inspect the model and relevant language/compiler constraints.",
      "Use authorized file access and compiler execution when available; do not install tools incidentally."
    ],
    "expectedFull": "Replace contradictory optional fields with explicit open and done variants or one authoritative completion value. Construct constrained values, brand semantic IDs, parse external data at boundaries, avoid unsupported casts, require exhaustive handling, and derive types from owned schemas where available. Strengthen types where an operation is partial, keeping total sum on plain lists. Verify with the available compiler that an invalid state or missing variant fails, or identify the actual language limit and the remaining validation requirement.",
    "expectedReduced": "When source, writes, or compiler execution are unavailable, provide the proposed typed model and explain actual language limits. State which invalid states the construction excludes, which checks remain runtime checks, and which edits or compiler checks were not performed.",
    "expectedBlocked": "If the relevant language or source cannot be established sufficiently to assess the invariant, report the missing inputs or denied capability and leave the result unverified.",
    "forbiddenClaims": [
      "An unchecked cast proves validity.",
      "Every language can encode every invariant.",
      "A proposed type model or structural package check proves compiler rejection or host behavior.",
      "Unavailable writes or checks succeeded."
    ],
    "caseFile": "docs/parity/cases/skills/principle-type-system-discipline.json"
  },
  "registry": {
    "caseId": "invalid-state",
    "caseFile": "docs/parity/cases/skills/principle-type-system-discipline.json",
    "sourcePaths": [
      "skills/principle-type-system-discipline/SKILL.md"
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
      "attemptId": "grades-chatgpt-01-04.json#15",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 15,
      "host": "chatgpt",
      "caseId": "invalid-state",
      "status": "reduced-pass",
      "grade": {
        "caseId": "invalid-state",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Compiler proof of invalid-state/missing-variant rejection",
          "Concrete runtime date validation"
        ],
        "review": "Provides tagged states, opaque-ID/schema/exhaustiveness guidance, NonEmpty versus total-sum distinction and genuine Date/assertion language limits. It clearly discloses no compiler run. This is a typed proposal, not observed compiler acceptance/rejection.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-state/result.json",
        "variantReview": [
          {
            "name": "state/ID/JSON/exhaustiveness review",
            "reportedObservation": "attempted supplied model",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "head/sum distinction",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "compiler acceptance/rejection",
            "reportedObservation": "blocked Bun absent",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "runtime date validation",
            "reportedObservation": "blocked no executable adapter",
            "assessment": "blocked-or-partial"
          }
        ],
        "limits": [
          "Bun absent; no alternate JS/Python runtime used.",
          "No live accounts/actions.",
          "Hypothetical denial/unavailable variants are premises, not real host failures.",
          "Task full Git SHA and durable persistence unavailable/unverified.",
          "Retained responses and model-captured raw tool envelopes have early capture gaps/truncation; no blanket independent verification of all tool returns.",
          "Actual task Git revision unavailable; source-freeze binding is separate."
        ],
        "reviewedBy": "independent case_fixture_audit reviewer",
        "sourceCaseFile": "docs/parity/cases/skills/principle-type-system-discipline.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence",
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
        "text": "Use Task = {kind:'open'} | {kind:'done',at:Date}. Replace interchangeable strings with validated opaque UserId and OrderId construction at the boundary; parse JSON as unknown through the repository schema, not a cast. Exhaustively switch with a never binding so a new task variant requires handling. For head use NonEmpty<T> = [T,...T[]]; sum accepts T[] because the empty case totals zero. TypeScript still permits invalid Date instances and assertions that bypass types, so date validity needs runtime parsing. No compiler ran because Bun is absent; no package was installed.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-state/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-state/result.json",
          "sha256": "f8ab82951c8eadbb572fd6f3274345e6784a03b21ff3683ebcb0b609ff9585e1",
          "bytes": 1607
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/checkpoint-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/checkpoint-tool.json",
            "sha256": "5ff0b3d446f0116643156b668c2703fd1775ab987f584cabb0e91b5ecbacb837",
            "bytes": 770
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/dependencies-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/dependencies-tool.json",
            "sha256": "4037e877b78c1d685ddcbfd6fcb62f9ec8fba7ed110e4cffd57e68237d351fbe",
            "bytes": 13986
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/guide-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/guide-tool.json",
            "sha256": "dacb1cebf9fdb79ee78fe5a8c4f2b3b63dac797fede04e6a587d1cd978b31c4b",
            "bytes": 69880
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-design-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-design-tool.json",
            "sha256": "01cd1df403efd14e1f49f7c9675bc5ac6914961006bf7eb4415bb484c987c918",
            "bytes": 373
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-overnight-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-overnight-tool.json",
            "sha256": "d56fa813bd76acea14ab5527df7ddd1badbcaf33521a83c695073fd6cb78564f",
            "bytes": 379
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-recipes-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-recipes-tool.json",
            "sha256": "328a8f67da821e29e0427b7ba4425207912cb92eb4c32149434712961ed5d22f",
            "bytes": 375
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-router-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-router-tool.json",
            "sha256": "44fdbe3d9b14af08559a62d34f018fafb5aa26b80aa9105a7b9eba6665ca24d2",
            "bytes": 373
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-understanding-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-understanding-tool.json",
            "sha256": "c3c462efa3b1be1332191a3c98e6fe14a9af2a0afbbcb582ed35d4ffee10476f",
            "bytes": 387
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-verification-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-verification-tool.json",
            "sha256": "506cf0b3bd255ba43d29e4fe86c96b535a405098f327a0a8bcda3a5b154859f9",
            "bytes": 385
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/playbooks-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/playbooks-tool.json",
            "sha256": "02cb0544a5e2d13f2f8d2cb19e49b1baf7b5ffe7bda396f519eed886a10861b8",
            "bytes": 21342
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-state/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-state/result.json",
      "sha256": "f8ab82951c8eadbb572fd6f3274345e6784a03b21ff3683ebcb0b609ff9585e1",
      "bytes": 1607,
      "owners": [
        "grades-chatgpt-01-04.json#15"
      ],
      "text": "{\n  \"caseId\": \"invalid-state\",\n  \"batch\": \"batch-02\",\n  \"actualResponse\": \"Use Task = {kind:'open'} | {kind:'done',at:Date}. Replace interchangeable strings with validated opaque UserId and OrderId construction at the boundary; parse JSON as unknown through the repository schema, not a cast. Exhaustively switch with a never binding so a new task variant requires handling. For head use NonEmpty<T> = [T,...T[]]; sum accepts T[] because the empty case totals zero. TypeScript still permits invalid Date instances and assertions that bypass types, so date validity needs runtime parsing. No compiler ran because Bun is absent; no package was installed.\",\n  \"observedOperations\": [\n    \"case.json and named installed sources read with tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/guide-tool.json\",\n    \"../../evidence/playbooks-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"state/ID/JSON/exhaustiveness review\",\n      \"observation\": \"attempted supplied model\"\n    },\n    {\n      \"name\": \"head/sum distinction\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"compiler acceptance/rejection\",\n      \"observation\": \"blocked Bun absent\"\n    },\n    {\n      \"name\": \"runtime date validation\",\n      \"observation\": \"blocked no executable adapter\"\n    }\n  ],\n  \"limits\": [\n    \"Bun absent; no alternate JS/Python runtime used.\",\n    \"No live accounts/actions.\",\n    \"Hypothetical denial/unavailable variants are premises, not real host failures.\",\n    \"Task full Git SHA and durable persistence unavailable/unverified.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-state/case.json",
      "owner": "grades-chatgpt-01-04.json#15",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-state/input",
      "owner": "grades-chatgpt-01-04.json#15",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-state/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#15",
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
