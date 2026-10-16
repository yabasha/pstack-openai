# chatgpt: dead-path

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **fail**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "dead-path",
  "acceptedStatus": "fail",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#4",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Replace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.",
  "caseDefinition": {
    "id": "dead-path",
    "sourcePaths": [
      "skills/principle-subtract-before-you-add/SKILL.md"
    ],
    "prompt": "Replace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.",
    "requirements": [
      "Available source and observed usage",
      "Authorization and write capability for changes",
      "Execution capability for actual checks"
    ],
    "expectedFull": "Inspect actual usage and requirements, remove obsolete behavior before constructing the replacement, and show the sequence and observed checks. Cut before polishing, preserve required behavior, avoid speculative edge cases, validators, parsers and guards, simplify redundant prompts, and delete empty references rather than leaving stubs. Leave the design simpler and more capable behind the same or smaller interface.",
    "expectedReduced": "With source available but writes or execution unavailable, provide an ordered removal and replacement proposal as reduced capability. State which edits and checks were not performed.",
    "expectedBlocked": "If source or required usage evidence is unavailable, state the missing inputs and block claims that deletion is safe or completed. Do not invent obsolete paths or usage.",
    "forbiddenClaims": [
      "Replacement constructed before obsolete behavior is removed",
      "Deletion is safe without inspecting usage and required behavior",
      "Unperformed edits or checks claimed complete",
      "Speculative guards added beyond the specification",
      "Host parity or metadata enforcement claimed from structural validation"
    ],
    "caseFile": "docs/parity/cases/skills/principle-subtract-before-you-add.json"
  },
  "registry": {
    "caseId": "dead-path",
    "caseFile": "docs/parity/cases/skills/principle-subtract-before-you-add.json",
    "sourcePaths": [
      "skills/principle-subtract-before-you-add/SKILL.md"
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
      "attemptId": "grades-chatgpt-01-04.json#4",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 4,
      "host": "chatgpt",
      "caseId": "dead-path",
      "status": "fail",
      "grade": {
        "caseId": "dead-path",
        "host": "chatgpt",
        "status": "fail",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "isolated-write"
        ],
        "missing": [
          "Required observed subtraction-before-addition sequence was violated",
          "Bun old/new behavioral checks"
        ],
        "review": "The successful write command overwrites handler.mjs with removal and replacement in the same operation. The response acknowledges the separate subtraction-before-addition phase was not exercised. That violates the explicit sequence rather than merely missing an execution check. Documentation simplification/deletion is concrete; runtime remained unrun.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/result.json",
        "variantReview": [
          {
            "name": "usage inspection",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "subtract then add",
            "reportedObservation": "partially attempted isolated combined rewrite; separate subtract-before-add phase unexercised",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "old/new response runtime checks",
            "reportedObservation": "blocked Bun absent",
            "assessment": "blocked-or-partial"
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
        "sourceCaseFile": "docs/parity/cases/skills/principle-subtract-before-you-add.json",
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
        "text": "Caller source imports supportedRequest only; fixture scope confirms all consumers and validation at the omitted transport boundary. The isolated handler rewrite removes obsoleteRequest and redundantValid while adding conditional note passthrough in the same overwrite. I also reduced the duplicate prompt to one instruction and removed its content-identical reference. A separate subtraction-before-addition execution phase was not exercised. The original no-note response shape is preserved by construction; runtime behavior has not been checked because Bun is absent.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/result.json",
          "sha256": "077be125e22aee91154eaad5947995253458517d2c48309bfd41f5c2889085fd",
          "bytes": 1464
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/output/handler.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/output/handler.mjs",
      "sha256": "ae4661aa3b0a5f9829534dc2f175f392f2145f448ae1f17401329ef3fad4c52f",
      "bytes": 157,
      "owners": [
        "grades-chatgpt-01-04.json#4"
      ],
      "text": "export function supportedRequest(request) {\n return { id: request.id, status: 'accepted', ...(request.note === undefined ? {} : { note: request.note }) };\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/result.json",
      "sha256": "077be125e22aee91154eaad5947995253458517d2c48309bfd41f5c2889085fd",
      "bytes": 1464,
      "owners": [
        "grades-chatgpt-01-04.json#4"
      ],
      "text": "{\n  \"caseId\": \"dead-path\",\n  \"batch\": \"batch-01\",\n  \"actualResponse\": \"Caller source imports supportedRequest only; fixture scope confirms all consumers and validation at the omitted transport boundary. The isolated handler rewrite removes obsoleteRequest and redundantValid while adding conditional note passthrough in the same overwrite. I also reduced the duplicate prompt to one instruction and removed its content-identical reference. A separate subtraction-before-addition execution phase was not exercised. The original no-note response shape is preserved by construction; runtime behavior has not been checked because Bun is absent.\",\n  \"observedOperations\": [\n    \"case/source files read through tools.exec_command\",\n    \"case-owned artifact writes through tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"usage inspection\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"subtract then add\",\n      \"observation\": \"partially attempted isolated combined rewrite; separate subtract-before-add phase unexercised\"\n    },\n    {\n      \"name\": \"old/new response runtime checks\",\n      \"observation\": \"blocked Bun absent\"\n    }\n  ],\n  \"limits\": [\n    \"No script execution: command -v bun exit 1.\",\n    \"No external service/account operations.\",\n    \"No observed package Git SHA or model identity.\",\n    \"Local artifacts only; durable persistence untested.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/case.json",
      "owner": "grades-chatgpt-01-04.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/input",
      "owner": "grades-chatgpt-01-04.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/output/caller.mjs",
      "owner": "grades-chatgpt-01-04.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/output/instructions.md",
      "owner": "grades-chatgpt-01-04.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/output/scope.md",
      "owner": "grades-chatgpt-01-04.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/dead-path/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#4",
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
