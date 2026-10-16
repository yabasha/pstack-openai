# chatgpt: invalid-input

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "invalid-input",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#14",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.",
  "caseDefinition": {
    "id": "invalid-input",
    "sourcePaths": [
      "skills/principle-boundary-discipline/SKILL.md"
    ],
    "prompt": "Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.",
    "requirements": [
      "Validate external input at its boundary without duplicating internal guards.",
      "Parse raw input into domain types and propagate errors internally; keep business logic in pure functions and framework wiring thin.",
      "Expose domain concepts rather than transport, storage, framework or wire types; keep general-purpose mechanism inside and special-purpose policy at the edge.",
      "Report implementation and checks only when writes and execution are authorized and observed."
    ],
    "expectedFull": "The adapter validates and narrows raw quantity before calling typed domain logic, returns boundary errors for invalid input, and removes redundant internal guards. Pricing remains a pure function. Parsing, prompt construction and scoring remain pure transforms where applicable. Public interfaces expose domain concepts. Report observed implementation and checks only.",
    "expectedReduced": "If writes or execution are unavailable, provide a reduced proposal with boundary validation and typed pure internal logic. State which edits and checks were not performed.",
    "expectedBlocked": "If relevant source or the input contract is unavailable, identify the missing information and keep any proposal provisional. Do not claim that boundary validation or guard removal was verified.",
    "forbiddenClaims": [
      "Structural checks prove behavioral parity.",
      "Unavailable writes or execution succeeded.",
      "Internal validation is required after the boundary has validated typed data.",
      "Invocation metadata proves host enforcement."
    ],
    "caseFile": "docs/parity/cases/skills/principle-boundary-discipline.json"
  },
  "registry": {
    "caseId": "invalid-input",
    "caseFile": "docs/parity/cases/skills/principle-boundary-discipline.json",
    "sourcePaths": [
      "skills/principle-boundary-discipline/SKILL.md"
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
      "attemptId": "grades-chatgpt-01-04.json#14",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 14,
      "host": "chatgpt",
      "caseId": "invalid-input",
      "status": "blocked",
      "grade": {
        "caseId": "invalid-input",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Actual affected HTTP adapter/internal source and authoritative error contract",
          "Bun execution and actual guard migration"
        ],
        "review": "The response explicitly has no actual affected adapter or precise response contract in this cloud input. Its quantity design is provisional and cannot prove narrowing or redundant-guard removal. Additional-v3 inputs created later cannot retroactively satisfy this run.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-input/result.json",
        "variantReview": [
          {
            "name": "boundary validation design",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "internal guard removal",
            "reportedObservation": "blocked affected source absent",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "invalid quantity execution",
            "reportedObservation": "blocked Bun absent",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "wire/domain separation",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
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
        "sourceCaseFile": "docs/parity/cases/skills/principle-boundary-discipline.json",
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
        "text": "Parse raw order JSON at the HTTP adapter into a domain Order containing a validated positive integer Quantity. Reject missing quantity, null, strings, zero, negative, fractional and nonfinite values with a boundary error before pricing. Quantity policy is provisional because no actual adapter contract is supplied. Pass only that typed order to a pure price function and remove duplicate nil/quantity checks from trusted internal calls. The framework shell translates parse errors to the agreed HTTP response and propagates internal errors. Do not expose transport request objects as domain types. No affected adapter source or precise response contract was provided, and Bun checks are blocked; this is a concrete proposal, not an implemented fix.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-input/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-input/result.json",
          "sha256": "4c0796505d114220f5e2c2b2b491e7804eac5aff969eeb10c221b581eb55f779",
          "bytes": 1754
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-input/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-input/result.json",
      "sha256": "4c0796505d114220f5e2c2b2b491e7804eac5aff969eeb10c221b581eb55f779",
      "bytes": 1754,
      "owners": [
        "grades-chatgpt-01-04.json#14"
      ],
      "text": "{\n  \"caseId\": \"invalid-input\",\n  \"batch\": \"batch-02\",\n  \"actualResponse\": \"Parse raw order JSON at the HTTP adapter into a domain Order containing a validated positive integer Quantity. Reject missing quantity, null, strings, zero, negative, fractional and nonfinite values with a boundary error before pricing. Quantity policy is provisional because no actual adapter contract is supplied. Pass only that typed order to a pure price function and remove duplicate nil/quantity checks from trusted internal calls. The framework shell translates parse errors to the agreed HTTP response and propagates internal errors. Do not expose transport request objects as domain types. No affected adapter source or precise response contract was provided, and Bun checks are blocked; this is a concrete proposal, not an implemented fix.\",\n  \"observedOperations\": [\n    \"case.json and named installed sources read with tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/guide-tool.json\",\n    \"../../evidence/playbooks-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"boundary validation design\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"internal guard removal\",\n      \"observation\": \"blocked affected source absent\"\n    },\n    {\n      \"name\": \"invalid quantity execution\",\n      \"observation\": \"blocked Bun absent\"\n    },\n    {\n      \"name\": \"wire/domain separation\",\n      \"observation\": \"attempted\"\n    }\n  ],\n  \"limits\": [\n    \"Bun absent; no alternate JS/Python runtime used.\",\n    \"No live accounts/actions.\",\n    \"Hypothetical denial/unavailable variants are premises, not real host failures.\",\n    \"Task full Git SHA and durable persistence unavailable/unverified.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-input/case.json",
      "owner": "grades-chatgpt-01-04.json#14",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-input/input",
      "owner": "grades-chatgpt-01-04.json#14",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/invalid-input/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#14",
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
