# chatgpt: dead-path

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "dead-path",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-rerun-01.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
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
    },
    {
      "attemptId": "grades-chatgpt-rerun-01.json#0",
      "order": 101,
      "gradeFile": "grades-chatgpt-rerun-01.json",
      "rankWithinFile": 0,
      "host": "chatgpt",
      "caseId": "dead-path",
      "status": "reduced-pass",
      "grade": {
        "caseId": "dead-path",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "isolated-write",
          "review-outcome"
        ],
        "missing": [
          "Bun runtime absent: original/final behavioral tests, omitted/undefined/empty note and caller integration unexecuted"
        ],
        "review": "Retained removal snapshot/diff/hash/readback and absence-of-replacement checkpoint establish subtraction-only stage before separate replacement directory and note passthrough. Original combined-overwrite failure is preserved unchanged. Sequence flaw is corrected, but actual runtime behavior remains unverified because command-v-bun returned1; static diffs/hashes do not supply behavioral execution. Canonical agent prompts were legitimately read via mapped installed references paths.",
        "responseArtifact": "chatgpt/dead-path-rerun/dead-path-rerun-01/dead-path-rerun.results.json",
        "evidence": [
          "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/00-through-removal-tool-returns.json",
          "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal-checkpoint.json",
          "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal.diff",
          "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/02-replacement.diff",
          "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/through-replacement-tool-returns.json",
          "chatgpt/dead-path-rerun/dead-path-rerun.artifacts.zip"
        ],
        "rawEvidenceScope": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence",
        "variantReview": [
          "Actual saved removal-before-addition sequence completed in distinct owned stages.",
          "Bun missing: no syntax/behavior/test execution, no substitute runtime.",
          "Original cloud fail remains historical; new reduced result does not rewrite it."
        ],
        "limits": [
          "Tool-return archive is a model-captured record, not blanket independently verified native telemetry.",
          "Source freeze supplied separately from unavailable task Git revision.",
          "No workers, external actions, install or source edits occurred."
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "priorAttempt": {
          "artifact": "grades-chatgpt-01-04.json",
          "status": "fail",
          "retained": true
        }
      },
      "topLevelContext": {
        "attempt": "rerun-01",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Archive copied from Downloads and safely extracted; zipSHA2567c44ffab3f04ae8dbd11c95c389ea257202f48125d5605fa41970bf6d7563465.",
          "Exact cloud return objects are model-captured. No additional independent UI/command-output corroboration is invented."
        ]
      },
      "response": {
        "text": "Starting from original attachment fixture bytes, I removed obsoleteRequest and redundantValid, collapsed duplicate instructions, and removed duplicate-reference.md. I saved and read back that removal-only stage and recorded its diff and hashes while the replacement stage did not exist. Only afterward I copied that stage into a separate replacement directory and added optional request.note passthrough. I saved and read back the replacement, whose diff changes only supportedRequest. These are observed edits and static file checks; runtime behavior is unverified.",
        "artifact": {
          "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/dead-path-rerun.results.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/dead-path-rerun.results.json",
          "sha256": "6d7b3698514f3357b06b169f98d8a6c2fd24a1e97c0cf54d078e21f081f4557f",
          "bytes": 7511
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
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/00-through-removal-tool-returns.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/00-through-removal-tool-returns.json",
            "sha256": "0cfdf9315c92dc0748b60f48f120d29d21a38d1358705671552c6a0dd09251e8",
            "bytes": 29260
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal-checkpoint.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal-checkpoint.json",
            "sha256": "d90311fa11272a89d8419182d7d87818cc479edfc28c4c55783f008a9b6d244b",
            "bytes": 643
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal.diff",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal.diff",
            "sha256": "0a61082efe93d522c5e5f4d7c6c9b8e3d1f196801081d9723a89d8052de29de3",
            "bytes": 1212
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/02-replacement.diff",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/02-replacement.diff",
            "sha256": "bceb4bc9702931fa9fc4e910680e42f6e1cc289857cf395e80a2a69f7c3e700d",
            "bytes": 594
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/through-replacement-tool-returns.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/through-replacement-tool-returns.json",
            "sha256": "7fdb4e79b2651bf5f58457daa60d79d4538fbb5650135e70a9adcb5ab6ae19f6",
            "bytes": 65997
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun.artifacts.zip",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun.artifacts.zip",
            "sha256": "7c44ffab3f04ae8dbd11c95c389ea257202f48125d5605fa41970bf6d7563465",
            "bytes": 103011
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/00-through-removal-tool-returns.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/00-through-removal-tool-returns.json",
            "sha256": "0cfdf9315c92dc0748b60f48f120d29d21a38d1358705671552c6a0dd09251e8",
            "bytes": 29260
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal-checkpoint.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal-checkpoint.json",
            "sha256": "d90311fa11272a89d8419182d7d87818cc479edfc28c4c55783f008a9b6d244b",
            "bytes": 643
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/packaging-tool-returns.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/packaging-tool-returns.json",
            "sha256": "0ee1f9572832a3f2f1c890f43aa6ee089f8a3e0405731cbd7b6aedaaffd2ee7a",
            "bytes": 5206
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-actual-diffs-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-actual-diffs-tool.json",
            "sha256": "9c56bf96534fec4fb5a250108c99470239ddde7df96ae7833e3dd8d1ae0b371e",
            "bytes": 6155
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/result-readback.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/result-readback.json",
            "sha256": "6d7b3698514f3357b06b169f98d8a6c2fd24a1e97c0cf54d078e21f081f4557f",
            "bytes": 7511
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/through-replacement-tool-returns.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/through-replacement-tool-returns.json",
            "sha256": "7fdb4e79b2651bf5f58457daa60d79d4538fbb5650135e70a9adcb5ab6ae19f6",
            "bytes": 65997
          },
          {
            "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/tool-returns.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/tool-returns.json",
            "sha256": "26f2d83e478e8fe55cc264a51b5304f16a351a9c87a8a7bc2e97c9524e2087d7",
            "bytes": 143294
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
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/case-contract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/case-contract.json",
      "sha256": "cdb5c2585e18f8b99a0c2bff17d2105be9993c1be43b3db2929339ba2e581a3b",
      "bytes": 681,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "{\n  \"id\": \"dead-path\",\n  \"sourcePaths\": [\n    \"skills/principle-subtract-before-you-add/SKILL.md\"\n  ],\n  \"prompt\": \"Replace an obsolete request path whose callers have moved to the supported handler. Inspect usage, remove the obsolete behavior and redundant validator first, then add the specified replacement. Simplify duplicate prompt instructions and delete a reference with no novel content. Show the order and checks. If writes or execution are unavailable, give a read-only proposal with explicit limits.\",\n  \"requirements\": [\n    \"Available source and observed usage\",\n    \"Authorization and write capability for changes\",\n    \"Execution capability for actual checks\"\n  ]\n}\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/dead-path-rerun.results.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/dead-path-rerun.results.json",
      "sha256": "6d7b3698514f3357b06b169f98d8a6c2fd24a1e97c0cf54d078e21f081f4557f",
      "bytes": 7511,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"caseId\": \"dead-path\",\n  \"rerun\": \"dead-path-rerun-01\",\n  \"workflow\": \"installed principle-subtract-before-you-add\",\n  \"grading\": \"No self-assigned grade\",\n  \"actualResponse\": \"Starting from original attachment fixture bytes, I removed obsoleteRequest and redundantValid, collapsed duplicate instructions, and removed duplicate-reference.md. I saved and read back that removal-only stage and recorded its diff and hashes while the replacement stage did not exist. Only afterward I copied that stage into a separate replacement directory and added optional request.note passthrough. I saved and read back the replacement, whose diff changes only supportedRequest. These are observed edits and static file checks; runtime behavior is unverified.\",\n  \"originalFailure\": {\n    \"preservedAt\": \"prior-attempt/\",\n    \"description\": \"Original combined overwrite removed old behavior and added note passthrough together; it did not exercise a separate removal stage. It remains unchanged, not relabeled as this rerun.\",\n    \"additionalEvidence\": \"evidence/prior-actual-diffs-tool.json\"\n  },\n  \"inputProvenance\": {\n    \"attachment\": \"/workspace/scratch/305945b957dd/upload/remaining-batches.input.json\",\n    \"extraction\": \".fixtures[\\\"additional/dead-path/<name>\\\"]\",\n    \"files\": [\n      \"handler.mjs\",\n      \"caller.mjs\",\n      \"instructions.md\",\n      \"duplicate-reference.md\",\n      \"scope.md\"\n    ],\n    \"fullCaseContract\": \"case-contract.json\",\n    \"originalInputs\": \"original-inputs/\",\n    \"scopeContract\": \"original-inputs/scope.md\"\n  },\n  \"installedSource\": {\n    \"path\": \"/root/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-subtract-before-you-add/SKILL.md\",\n    \"copy\": \"sources/principle-subtract-before-you-add.SKILL.md\",\n    \"disableModelInvocation\": true,\n    \"sourceReadToolChunk\": \"5abe5f\",\n    \"capabilityGuide\": \"sources/host-capabilities.md\",\n    \"noInstalledSourceEdits\": true\n  },\n  \"canonicalPathMapping\": [\n    {\n      \"upstream\": \"agents/poteto-agent.md\",\n      \"installed\": \"references/agent-prompts/poteto-agent.md\",\n      \"actualMappedRead\": {\n        \"tool\": \"tools.exec_command\",\n        \"chunk\": \"882bae\",\n        \"exitCode\": 0,\n        \"contentRetained\": \"sources/poteto-agent.md\"\n      },\n      \"interpretation\": \"Packaged support is available at its canonical mapped path; a prior failed upstream pathname is not proof of missing packaged support.\"\n    },\n    {\n      \"upstream\": \"agents/comment-sicko.md\",\n      \"installed\": \"references/agent-prompts/comment-sicko.md\",\n      \"actualMappedRead\": {\n        \"tool\": \"tools.exec_command\",\n        \"chunk\": \"882bae\",\n        \"exitCode\": 0,\n        \"contentRetained\": \"sources/comment-sicko.md\"\n      },\n      \"interpretation\": \"Packaged support is available at its canonical mapped path; a prior failed upstream pathname is not proof of missing packaged support.\"\n    }\n  ],\n  \"sequence\": [\n    {\n      \"order\": 1,\n      \"action\": \"Read installed skill, full case and scope, original code and caller usage\",\n      \"toolChunks\": [\n        \"5abe5f\",\n        \"882bae\"\n      ]\n    },\n    {\n      \"order\": 2,\n      \"action\": \"Materialize fresh original fixture inputs and preserve prior attempt\",\n      \"toolChunk\": \"a4907b\"\n    },\n    {\n      \"order\": 3,\n      \"action\": \"Apply only subtraction in stages/01-removal\",\n      \"tool\": \"tools.apply_patch\",\n      \"rawResult\": {}\n    },\n    {\n      \"order\": 4,\n      \"action\": \"Save/read back removal-only files, diff and hashes before replacement exists\",\n      \"toolChunk\": \"10bd5e\",\n      \"checkpoint\": \"evidence/01-removal-checkpoint.json\",\n      \"readback\": \"evidence/01-removal-readback.txt\",\n      \"diff\": \"evidence/01-removal.diff\"\n    },\n    {\n      \"order\": 5,\n      \"action\": \"Read saved checkpoint and verify removal hashes, then copy removal stage into new replacement directory\",\n      \"toolChunk\": \"1c9638\"\n    },\n    {\n      \"order\": 6,\n      \"action\": \"Add scoped optional note passthrough only in stages/02-replacement/handler.mjs\",\n      \"tool\": \"tools.apply_patch\",\n      \"rawResult\": {}\n    },\n    {\n      \"order\": 7,\n      \"action\": \"Save/read back replacement, diff against removal and recheck removal/prior hashes\",\n      \"toolChunk\": \"516299\",\n      \"readback\": \"evidence/02-replacement-readback.txt\",\n      \"diff\": \"evidence/02-replacement.diff\"\n    }\n  ],\n  \"observedFileChecks\": {\n    \"removalDiffExit\": 1,\n    \"removalDiffMeaning\": \"Differences found, not error\",\n    \"removalObsoleteAndNoteSearchExit\": 1,\n    \"searchMeaning\": \"No obsoleteRequest, redundantValid or request.note match in removal handler\",\n    \"removalDuplicateReferenceAbsenceExit\": 0,\n    \"removalCallerComparisonExit\": 0,\n    \"replacementDirectoryAbsentAtRemovalReadbackExit\": 0,\n    \"replacementDiffExit\": 1,\n    \"replacementDiffMeaning\": \"Only handler.mjs changed relative to saved removal stage\",\n    \"removalHashReadback\": \"All four files matched before and after adding replacement\",\n    \"priorCaseHashReadbackExit\": 0,\n    \"priorDeliverablesHashReadback\": \"All four named prior deliverables matched\",\n    \"replacementCallerComparisonExit\": 0,\n    \"replacementInstructionsComparisonExit\": 0\n  },\n  \"replacementSemantics\": {\n    \"source\": \"stages/02-replacement/handler.mjs\",\n    \"implementation\": \"Creates {id,status:'accepted'}, adds note only when request.note !== undefined, returns response.\",\n    \"undefinedInterpretation\": \"An undefined note is omitted; no new parser or validator was added.\",\n    \"behaviorObserved\": false\n  },\n  \"unexecutedChecks\": [\n    {\n      \"check\": \"Execute original and final supportedRequest({id:'r1'}) and compare literal {id:'r1',status:'accepted'}\",\n      \"reason\": \"Bun absent; no substitute runtime authorized\"\n    },\n    {\n      \"check\": \"Execute supportedRequest({id:'r1',note:'hello'}) and compare literal note passthrough\",\n      \"reason\": \"Bun absent\"\n    },\n    {\n      \"check\": \"Execute omitted/undefined note and empty-string note cases\",\n      \"reason\": \"Bun absent; source inspection is not an observed output\"\n    },\n    {\n      \"check\": \"Run caller integration and tests covering removal of obsolete export/validator\",\n      \"reason\": \"Bun absent; no runtime check performed\"\n    },\n    {\n      \"check\": \"Syntax, lint, test runner, package evidence validator or compilation\",\n      \"reason\": \"Not executed; no alternate runtime, dependency installation or configuration authorized\"\n    }\n  ],\n  \"capabilities\": {\n    \"fileReads\": \"Observed\",\n    \"sandboxWrites\": \"Observed\",\n    \"diffsReadbackAndHashes\": \"Observed with native file tools\",\n    \"bun\": \"command -v bun returned exit 1 and no path in chunk 5abe5f\",\n    \"runtimeExecution\": \"Not performed\",\n    \"workers\": \"Not invoked; no independent worker requirement for this direct scoped rerun\",\n    \"durablePersistence\": \"Not tested; sandbox artifacts only\"\n  },\n  \"restrictions\": {\n    \"liveServices\": false,\n    \"installedPackageEdits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"commits\": false,\n    \"nodeOrPythonSubstitution\": false\n  },\n  \"rawToolEvidence\": {\n    \"capture\": \"Each primary tool return was stored immediately after the awaited call. Removal-stage raw snapshot was saved before creating replacement. Full retained returns follow in evidence/tool-returns.json.\",\n    \"removalSnapshot\": \"evidence/00-through-removal-tool-returns.json\",\n    \"packagingBoundary\": \"Final archive transport metadata remains in the conversation; no reconstructed receipts or fabricated runtime outcomes.\"\n  }\n}\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal-checkpoint.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal-checkpoint.json",
      "sha256": "d90311fa11272a89d8419182d7d87818cc479edfc28c4c55783f008a9b6d244b",
      "bytes": 643,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "{\n  \"stage\": \"01-removal\",\n  \"replacementStageCreated\": false,\n  \"evidence\": \"evidence/01-removal-readback.txt\",\n  \"diff\": \"evidence/01-removal.diff\",\n  \"hashes\": \"evidence/01-removal.sha256\",\n  \"observedChecks\": {\n    \"diffExit\": 1,\n    \"diffMeaning\": \"Differences found; not an execution failure\",\n    \"searchExit\": 1,\n    \"searchMeaning\": \"No obsolete symbols or request.note in removal handler\",\n    \"duplicateReferenceAbsentExit\": 0,\n    \"callerByteComparisonExit\": 0,\n    \"replacementStageAbsenceExit\": 0\n  },\n  \"runtimeChecks\": \"Not executed; Bun absent. This checkpoint records files/readback only.\",\n  \"readbackToolChunk\": \"10bd5e\"\n}\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal-readback.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal-readback.txt",
      "sha256": "b78cb0659ee90bbeebc7daef319380b21e91c7e5a0869783a509ee34fd73cc40",
      "bytes": 242,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "export function supportedRequest(request) { return { id: request.id, status: 'accepted' }; }\nUse the supported request handler.\nimport { supportedRequest } from './handler.mjs';\nexport function submit(id) { return supportedRequest({ id }); }\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal.diff",
      "sha256": "0a61082efe93d522c5e5f4d7c6c9b8e3d1f196801081d9723a89d8052de29de3",
      "bytes": 1212,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "Only in dead-path-rerun-01/original-inputs: duplicate-reference.md\ndiff -ru dead-path-rerun-01/original-inputs/handler.mjs dead-path-rerun-01/stages/01-removal/handler.mjs\n--- dead-path-rerun-01/original-inputs/handler.mjs\t2026-10-16 10:14:53.284429789 +0200\n+++ dead-path-rerun-01/stages/01-removal/handler.mjs\t2026-10-16 10:15:02.616629050 +0200\n@@ -1,6 +1 @@\n-function redundantValid(request) { return request && typeof request === 'object' && typeof request.id === 'string'; }\n-export function obsoleteRequest(request) {\n-  if (!redundantValid(request)) throw new Error('invalid');\n-  return { id: request.id, obsolete: true };\n-}\n export function supportedRequest(request) { return { id: request.id, status: 'accepted' }; }\ndiff -ru dead-path-rerun-01/original-inputs/instructions.md dead-path-rerun-01/stages/01-removal/instructions.md\n--- dead-path-rerun-01/original-inputs/instructions.md\t2026-10-16 10:14:53.292429960 +0200\n+++ dead-path-rerun-01/stages/01-removal/instructions.md\t2026-10-16 10:15:03.332644523 +0200\n@@ -1 +1 @@\n-Use the supported request handler. Use the supported request handler for requests. Read duplicate-reference.md for the same instruction.\n+Use the supported request handler.\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal.sha256",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/01-removal.sha256",
      "sha256": "977c2901fc8a261af822e9197157d2d1d7e7d5adbd2a52eb94158ac16a5c8f04",
      "bytes": 460,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931  dead-path-rerun-01/stages/01-removal/caller.mjs\n8e33a884b99b3be3c4d4c7f6c63e2c619b322d968b5f061bd155744b0b273db0  dead-path-rerun-01/stages/01-removal/handler.mjs\n0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974  dead-path-rerun-01/stages/01-removal/instructions.md\n1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510  dead-path-rerun-01/stages/01-removal/scope.md\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/02-replacement-readback.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/02-replacement-readback.txt",
      "sha256": "6fb2bbc1bbc36a515c56d7cb1cf3e9e0e15b32df89f9967dd1ad150164261c9c",
      "bytes": 337,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "export function supportedRequest(request) {\n  const response = { id: request.id, status: 'accepted' };\n  if (request.note !== undefined) response.note = request.note;\n  return response;\n}\nUse the supported request handler.\nimport { supportedRequest } from './handler.mjs';\nexport function submit(id) { return supportedRequest({ id }); }\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/02-replacement.diff",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/02-replacement.diff",
      "sha256": "bceb4bc9702931fa9fc4e910680e42f6e1cc289857cf395e80a2a69f7c3e700d",
      "bytes": 594,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "diff -ru dead-path-rerun-01/stages/01-removal/handler.mjs dead-path-rerun-01/stages/02-replacement/handler.mjs\n--- dead-path-rerun-01/stages/01-removal/handler.mjs\t2026-10-16 10:15:02.616629050 +0200\n+++ dead-path-rerun-01/stages/02-replacement/handler.mjs\t2026-10-16 10:15:46.361560965 +0200\n@@ -1 +1,5 @@\n-export function supportedRequest(request) { return { id: request.id, status: 'accepted' }; }\n+export function supportedRequest(request) {\n+  const response = { id: request.id, status: 'accepted' };\n+  if (request.note !== undefined) response.note = request.note;\n+  return response;\n+}\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/02-replacement.sha256",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/02-replacement.sha256",
      "sha256": "d25ea4b2ee539c5cb7dd8b8d50999e12f9cc95a4b27551f2f068bf98fbd466af",
      "bytes": 476,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931  dead-path-rerun-01/stages/02-replacement/caller.mjs\n53a8ea5210c43ef794af64baa29a225b70cc333b5661e1734823a25e832d2758  dead-path-rerun-01/stages/02-replacement/handler.mjs\n0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974  dead-path-rerun-01/stages/02-replacement/instructions.md\n1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510  dead-path-rerun-01/stages/02-replacement/scope.md\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/packaging-tool-returns.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/packaging-tool-returns.json",
      "sha256": "0ee1f9572832a3f2f1c890f43aa6ee089f8a3e0405731cbd7b6aedaaffd2ee7a",
      "bytes": 5206,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "{\n  \"receiptExport\": {\n    \"tool\": \"tools.apply_patch\",\n    \"argumentsSummary\": \"Added evidence/tool-returns.json from the immediately captured raw-return journal\",\n    \"result\": {}\n  },\n  \"artifactReadbackAndPackaging\": {\n    \"tool\": \"tools.exec_command\",\n    \"arguments\": {\n      \"cmd\": \"cat dead-path-rerun-01/dead-path-rerun.results.json > dead-path-rerun-01/evidence/result-readback.json\\ncmp dead-path-rerun-01/dead-path-rerun.results.json dead-path-rerun-01/evidence/result-readback.json\\nprintf 'result_json_readback_cmp_exit=%s\\\\n' \\\"$?\\\"\\njq '{caseId,sequence: [.sequence[]|{order,action}],unexecutedChecks,canonicalPathMapping}' dead-path-rerun-01/evidence/result-readback.json\\ncmp dead-path-rerun-01/sources/principle-subtract-before-you-add.SKILL.md /root/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-subtract-before-you-add/SKILL.md\\nprintf 'installed_skill_unchanged_cmp_exit=%s\\\\n' \\\"$?\\\"\\ncmp dead-path-rerun-01/sources/poteto-agent.md /root/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\\nprintf 'mapped_poteto_source_unchanged_cmp_exit=%s\\\\n' \\\"$?\\\"\\ncmp dead-path-rerun-01/sources/comment-sicko.md /root/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/comment-sicko.md\\nprintf 'mapped_comment_source_unchanged_cmp_exit=%s\\\\n' \\\"$?\\\"\\nzip -qr /workspace/scratch/305945b957dd/dead-path-rerun.artifacts.zip dead-path-rerun-01\\nunzip -tq /workspace/scratch/305945b957dd/dead-path-rerun.artifacts.zip\",\n      \"max_output_tokens\": 3000,\n      \"yield_time_ms\": 1000\n    },\n    \"result\": {\n      \"chunk_id\": \"02de52\",\n      \"wall_time_seconds\": 0.000046371,\n      \"exit_code\": 0,\n      \"original_token_count\": 760,\n      \"output\": \"result_json_readback_cmp_exit=0\\n{\\n  \\\"caseId\\\": \\\"dead-path\\\",\\n  \\\"sequence\\\": [\\n    {\\n      \\\"order\\\": 1,\\n      \\\"action\\\": \\\"Read installed skill, full case and scope, original code and caller usage\\\"\\n    },\\n    {\\n      \\\"order\\\": 2,\\n      \\\"action\\\": \\\"Materialize fresh original fixture inputs and preserve prior attempt\\\"\\n    },\\n    {\\n      \\\"order\\\": 3,\\n      \\\"action\\\": \\\"Apply only subtraction in stages/01-removal\\\"\\n    },\\n    {\\n      \\\"order\\\": 4,\\n      \\\"action\\\": \\\"Save/read back removal-only files, diff and hashes before replacement exists\\\"\\n    },\\n    {\\n      \\\"order\\\": 5,\\n      \\\"action\\\": \\\"Read saved checkpoint and verify removal hashes, then copy removal stage into new replacement directory\\\"\\n    },\\n    {\\n      \\\"order\\\": 6,\\n      \\\"action\\\": \\\"Add scoped optional note passthrough only in stages/02-replacement/handler.mjs\\\"\\n    },\\n    {\\n      \\\"order\\\": 7,\\n      \\\"action\\\": \\\"Save/read back replacement, diff against removal and recheck removal/prior hashes\\\"\\n    }\\n  ],\\n  \\\"unexecutedChecks\\\": [\\n    {\\n      \\\"check\\\": \\\"Execute original and final supportedRequest({id:'r1'}) and compare literal {id:'r1',status:'accepted'}\\\",\\n      \\\"reason\\\": \\\"Bun absent; no substitute runtime authorized\\\"\\n    },\\n    {\\n      \\\"check\\\": \\\"Execute supportedRequest({id:'r1',note:'hello'}) and compare literal note passthrough\\\",\\n      \\\"reason\\\": \\\"Bun absent\\\"\\n    },\\n    {\\n      \\\"check\\\": \\\"Execute omitted/undefined note and empty-string note cases\\\",\\n      \\\"reason\\\": \\\"Bun absent; source inspection is not an observed output\\\"\\n    },\\n    {\\n      \\\"check\\\": \\\"Run caller integration and tests covering removal of obsolete export/validator\\\",\\n      \\\"reason\\\": \\\"Bun absent; no runtime check performed\\\"\\n    },\\n    {\\n      \\\"check\\\": \\\"Syntax, lint, test runner, package evidence validator or compilation\\\",\\n      \\\"reason\\\": \\\"Not executed; no alternate runtime, dependency installation or configuration authorized\\\"\\n    }\\n  ],\\n  \\\"canonicalPathMapping\\\": [\\n    {\\n      \\\"upstream\\\": \\\"agents/poteto-agent.md\\\",\\n      \\\"installed\\\": \\\"references/agent-prompts/poteto-agent.md\\\",\\n      \\\"actualMappedRead\\\": {\\n        \\\"tool\\\": \\\"tools.exec_command\\\",\\n        \\\"chunk\\\": \\\"882bae\\\",\\n        \\\"exitCode\\\": 0,\\n        \\\"contentRetained\\\": \\\"sources/poteto-agent.md\\\"\\n      },\\n      \\\"interpretation\\\": \\\"Packaged support is available at its canonical mapped path; a prior failed upstream pathname is not proof of missing packaged support.\\\"\\n    },\\n    {\\n      \\\"upstream\\\": \\\"agents/comment-sicko.md\\\",\\n      \\\"installed\\\": \\\"references/agent-prompts/comment-sicko.md\\\",\\n      \\\"actualMappedRead\\\": {\\n        \\\"tool\\\": \\\"tools.exec_command\\\",\\n        \\\"chunk\\\": \\\"882bae\\\",\\n        \\\"exitCode\\\": 0,\\n        \\\"contentRetained\\\": \\\"sources/comment-sicko.md\\\"\\n      },\\n      \\\"interpretation\\\": \\\"Packaged support is available at its canonical mapped path; a prior failed upstream pathname is not proof of missing packaged support.\\\"\\n    }\\n  ]\\n}\\ninstalled_skill_unchanged_cmp_exit=0\\nmapped_poteto_source_unchanged_cmp_exit=0\\nmapped_comment_source_unchanged_cmp_exit=0\\nNo errors detected in compressed data of /workspace/scratch/305945b957dd/dead-path-rerun.artifacts.zip.\\n\"\n    }\n  },\n  \"boundary\": \"Final receipt-file write and archive refresh results are captured in the conversation; no runtime behavior checks were performed.\"\n}\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-actual-diffs-tool.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-actual-diffs-tool.json",
      "sha256": "9c56bf96534fec4fb5a250108c99470239ddde7df96ae7833e3dd8d1ae0b371e",
      "bytes": 6155,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "{\n  \"tool\": \"tools.exec_command\",\n  \"arguments\": {\n    \"cmd\": \"diff -ru remaining-evaluation/batches/batch-01/cases/caller-migration/input/additional/migration remaining-evaluation/batches/batch-01/cases/caller-migration/output; diff -ru remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path remaining-evaluation/batches/batch-01/cases/dead-path/output\",\n    \"max_output_tokens\": 6000\n  },\n  \"result\": {\n    \"chunk_id\": \"9e3770\",\n    \"wall_time_seconds\": 0.000030526,\n    \"exit_code\": 1,\n    \"original_token_count\": 1375,\n    \"output\": \"diff -ru remaining-evaluation/batches/batch-01/cases/caller-migration/input/additional/migration/api.mjs remaining-evaluation/batches/batch-01/cases/caller-migration/output/api.mjs\\n--- remaining-evaluation/batches/batch-01/cases/caller-migration/input/additional/migration/api.mjs\\t2026-10-16 09:47:52.291543838 +0200\\n+++ remaining-evaluation/batches/batch-01/cases/caller-migration/output/api.mjs\\t2026-10-16 09:50:13.405545273 +0200\\n@@ -1 +1,4 @@\\n-export function lookupUser(users, id) { return users.find(user => user.id === id) ?? null; }\\n+export function findUser({ users, id }) {\\n+  const user = users.find(user => user.id === id);\\n+  return user === undefined ? { kind: 'missing' } : { kind: 'found', user };\\n+}\\ndiff -ru remaining-evaluation/batches/batch-01/cases/caller-migration/input/additional/migration/contract.mjs remaining-evaluation/batches/batch-01/cases/caller-migration/output/contract.mjs\\n--- remaining-evaluation/batches/batch-01/cases/caller-migration/input/additional/migration/contract.mjs\\t2026-10-16 09:47:52.291561444 +0200\\n+++ remaining-evaluation/batches/batch-01/cases/caller-migration/output/contract.mjs\\t2026-10-16 09:50:13.409159843 +0200\\n@@ -1,6 +1,13 @@\\n-import { strict as assert } from 'node:assert';\\n-import { lookupUser } from './api.mjs';\\n-const users = [{ id: 'u1', name: 'Ada', email: 'ada@example.invalid' }];\\n-assert.equal(lookupUser(users, 'u1').name, 'Ada');\\n-assert.equal(lookupUser(users, 'absent'), null);\\n-console.log('original lookupUser contract checked');\\n+import { expect, test } from 'bun:test';\\n+import { findUser } from './api.mjs';\\n+import { profileLabel } from './profile.mjs';\\n+import { recipient } from './notification.mjs';\\n+test('found and missing behavior', () => {\\n+ const users = [{ id: 'u1', name: 'Ada', email: 'ada@example.invalid' }];\\n+ expect(findUser({ users, id: 'u1' })).toEqual({ kind: 'found', user: users[0] });\\n+ expect(findUser({ users, id: 'absent' })).toEqual({ kind: 'missing' });\\n+ expect(profileLabel(users, 'u1')).toBe('Ada');\\n+ expect(profileLabel(users, 'absent')).toBe('Unknown');\\n+ expect(recipient(users, 'u1')).toBe('ada@example.invalid');\\n+ expect(recipient(users, 'absent')).toBe(null);\\n+});\\ndiff -ru remaining-evaluation/batches/batch-01/cases/caller-migration/input/additional/migration/notification.mjs remaining-evaluation/batches/batch-01/cases/caller-migration/output/notification.mjs\\n--- remaining-evaluation/batches/batch-01/cases/caller-migration/input/additional/migration/notification.mjs\\t2026-10-16 09:47:52.291575706 +0200\\n+++ remaining-evaluation/batches/batch-01/cases/caller-migration/output/notification.mjs\\t2026-10-16 09:50:13.407980018 +0200\\n@@ -1,2 +1,5 @@\\n-import { lookupUser } from './api.mjs';\\n-export function recipient(users, id) { return lookupUser(users, id)?.email ?? null; }\\n+import { findUser } from './api.mjs';\\n+export function recipient(users, id) {\\n+  const result = findUser({ users, id });\\n+  return result.kind === 'found' ? result.user.email : null;\\n+}\\ndiff -ru remaining-evaluation/batches/batch-01/cases/caller-migration/input/additional/migration/profile.mjs remaining-evaluation/batches/batch-01/cases/caller-migration/output/profile.mjs\\n--- remaining-evaluation/batches/batch-01/cases/caller-migration/input/additional/migration/profile.mjs\\t2026-10-16 09:47:52.291590057 +0200\\n+++ remaining-evaluation/batches/batch-01/cases/caller-migration/output/profile.mjs\\t2026-10-16 09:50:13.406808044 +0200\\n@@ -1,2 +1,5 @@\\n-import { lookupUser } from './api.mjs';\\n-export function profileLabel(users, id) { const user = lookupUser(users, id); return user ? user.name : 'Unknown'; }\\n+import { findUser } from './api.mjs';\\n+export function profileLabel(users, id) {\\n+  const result = findUser({ users, id });\\n+  return result.kind === 'found' ? result.user.name : 'Unknown';\\n+}\\nOnly in remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path: duplicate-reference.md\\ndiff -ru remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/handler.mjs remaining-evaluation/batches/batch-01/cases/dead-path/output/handler.mjs\\n--- remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/handler.mjs\\t2026-10-16 09:47:52.312759356 +0200\\n+++ remaining-evaluation/batches/batch-01/cases/dead-path/output/handler.mjs\\t2026-10-16 09:50:13.410546551 +0200\\n@@ -1,6 +1,3 @@\\n-function redundantValid(request) { return request && typeof request === 'object' && typeof request.id === 'string'; }\\n-export function obsoleteRequest(request) {\\n-  if (!redundantValid(request)) throw new Error('invalid');\\n-  return { id: request.id, obsolete: true };\\n+export function supportedRequest(request) {\\n+ return { id: request.id, status: 'accepted', ...(request.note === undefined ? {} : { note: request.note }) };\\n }\\n-export function supportedRequest(request) { return { id: request.id, status: 'accepted' }; }\\ndiff -ru remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/instructions.md remaining-evaluation/batches/batch-01/cases/dead-path/output/instructions.md\\n--- remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/instructions.md\\t2026-10-16 09:47:52.312773558 +0200\\n+++ remaining-evaluation/batches/batch-01/cases/dead-path/output/instructions.md\\t2026-10-16 09:50:13.410841209 +0200\\n@@ -1 +1 @@\\n-Use the supported request handler. Use the supported request handler for requests. Read duplicate-reference.md for the same instruction.\\n+Use the supported request handler.\\n\"\n  }\n}\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-case-before.sha256",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-case-before.sha256",
      "sha256": "52c43468f8500baab3e5829dfe68622902048ff0324682247d1de29feb2b5d3a",
      "bytes": 7608,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "cdb5c2585e18f8b99a0c2bff17d2105be9993c1be43b3db2929339ba2e581a3b  remaining-evaluation/batches/batch-01/cases/dead-path/case.json\n6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a  remaining-evaluation/batches/batch-01/cases/dead-path/input/README.md\nd196849f4d82de3618f0e530cdddc68d486b3b2cd7ec807fa1a98412ddc4532c  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/README.md\nb6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/README.md\ne634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/cache.mjs\n9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/caller.mjs\n0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/invalidation.diff\n5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/manifest.json\nfa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/probe.mjs\nd33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/vendor/disposer-v1.mjs\nbba536a5394a6ddb455eddd0d9f04f67426bc5f9ef08325d543aab696a94a061  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/corpus/records.jsonl\n1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/caller.mjs\n0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/duplicate-reference.md\na86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/handler.mjs\nd29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/instructions.md\n1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/scope.md\n68475aad9893f5968ac61b2c68b9e1dda09450d5a631bce1fbb5394e562b5568  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/history/capsule.json\n6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/history/history.json\n477ba7aaaeab112324c1ee03db183869bc46ec8f4bdc4b8b76dceeb6ca563f3f  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/history/jay-mode.md\n7859c51afe5feade4176ed6f0c4c9a6aff7141e83df0a32f71c455d70a1b94c1  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/history/shared-records.json\na3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/adapter.mjs\n1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/calculator.mjs\n90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/controller.mjs\n324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/decision.md\nb877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/exporter.mjs\n6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/facade.mjs\n405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/formatter.mjs\nda37375054eb4140f6b2ba19dac4c5de3846183029177d58473b38d320cf8436  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/legal-header/source.diff\n7579a6b456d0cd513fd8f55d69096119304833f0dc5dfca7f66c727ec002df91  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/legal-header/source.mjs\n822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/api.mjs\n1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/contract.mjs\nddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/notification.mjs\n2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/profile.mjs\ne8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/scope.md\na732248ad7fdf1f003452602cd92f3571201ce6b2839569246f02155311a9a0b  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/scenario-map.json\n201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/types/README.md\n5e98773209677f72d526c420f60a406972988e8fc0067963f781fe5955188e42  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/types/boundary.ts\n862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58  remaining-evaluation/batches/batch-01/cases/dead-path/input/additional/types/context.ts\n34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9  remaining-evaluation/batches/batch-01/cases/dead-path/input/dashboard.mjs\n0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c  remaining-evaluation/batches/batch-01/cases/dead-path/input/forge.json\nf424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930  remaining-evaluation/batches/batch-01/cases/dead-path/input/history.json\n64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8  remaining-evaluation/batches/batch-01/cases/dead-path/input/invoice.mjs\n561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93  remaining-evaluation/batches/batch-01/cases/dead-path/input/orders.json\ne04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5  remaining-evaluation/batches/batch-01/cases/dead-path/input/runtime.mjs\n1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931  remaining-evaluation/batches/batch-01/cases/dead-path/output/caller.mjs\nae4661aa3b0a5f9829534dc2f175f392f2145f448ae1f17401329ef3fad4c52f  remaining-evaluation/batches/batch-01/cases/dead-path/output/handler.mjs\n0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974  remaining-evaluation/batches/batch-01/cases/dead-path/output/instructions.md\n1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510  remaining-evaluation/batches/batch-01/cases/dead-path/output/scope.md\n077be125e22aee91154eaad5947995253458517d2c48309bfd41f5c2889085fd  remaining-evaluation/batches/batch-01/cases/dead-path/result.json\nc3df22e09a911f26abdd405a59f56a0ddaff1142d1841237406bdadf91dc0de2  remaining-evaluation/batches/batch-01/cases/dead-path/source-reads.txt\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-case-integrity-readback.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-case-integrity-readback.txt",
      "sha256": "fe4ae54d43532d993c87ea089b2ece1c11824ffdb9ba03170b721ff1fd85598a",
      "bytes": 4508,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "remaining-evaluation/batches/batch-01/cases/dead-path/case.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/README.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/README.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/README.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/cache.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/caller.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/invalidation.diff: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/manifest.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/probe.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/cache/vendor/disposer-v1.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/corpus/records.jsonl: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/caller.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/duplicate-reference.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/handler.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/instructions.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/dead-path/scope.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/history/capsule.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/history/history.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/history/jay-mode.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/history/shared-records.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/adapter.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/calculator.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/controller.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/decision.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/exporter.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/facade.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/invoice/formatter.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/legal-header/source.diff: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/legal-header/source.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/api.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/contract.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/notification.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/profile.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/migration/scope.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/scenario-map.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/types/README.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/types/boundary.ts: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/additional/types/context.ts: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/dashboard.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/forge.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/history.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/invoice.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/orders.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/input/runtime.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/output/caller.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/output/handler.mjs: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/output/instructions.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/output/scope.md: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/result.json: OK\nremaining-evaluation/batches/batch-01/cases/dead-path/source-reads.txt: OK\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-deliverables-before.sha256",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/prior-deliverables-before.sha256",
      "sha256": "90bb5933480303316cac5151ab18e8650b0acaeef1e8be65b131c50755863ea9",
      "bytes": 413,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "fd3558789769100a1b8e2d2908074af536608124c8a4a47a8c814f150b3be707  remaining-batches.artifacts.zip\n1d18c06a098d15d73b95654aee6b5d3fe6cfa905b16336e2b0ebaee5b16030f9  remaining-evaluation/remaining-batches.results.json\n2ed7fd99d804480ba9234b0decbd29ace7df95b66ea1c20b07ad043328903527  batch-00.artifacts.zip\nd301d3ac626147fdcbdd2ad770f42e221c1093e3f7d4cccb734aa6abd4cee76b  batch-00-evaluation/batch-00.results.json\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/result-readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/result-readback.json",
      "sha256": "6d7b3698514f3357b06b169f98d8a6c2fd24a1e97c0cf54d078e21f081f4557f",
      "bytes": 7511,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"caseId\": \"dead-path\",\n  \"rerun\": \"dead-path-rerun-01\",\n  \"workflow\": \"installed principle-subtract-before-you-add\",\n  \"grading\": \"No self-assigned grade\",\n  \"actualResponse\": \"Starting from original attachment fixture bytes, I removed obsoleteRequest and redundantValid, collapsed duplicate instructions, and removed duplicate-reference.md. I saved and read back that removal-only stage and recorded its diff and hashes while the replacement stage did not exist. Only afterward I copied that stage into a separate replacement directory and added optional request.note passthrough. I saved and read back the replacement, whose diff changes only supportedRequest. These are observed edits and static file checks; runtime behavior is unverified.\",\n  \"originalFailure\": {\n    \"preservedAt\": \"prior-attempt/\",\n    \"description\": \"Original combined overwrite removed old behavior and added note passthrough together; it did not exercise a separate removal stage. It remains unchanged, not relabeled as this rerun.\",\n    \"additionalEvidence\": \"evidence/prior-actual-diffs-tool.json\"\n  },\n  \"inputProvenance\": {\n    \"attachment\": \"/workspace/scratch/305945b957dd/upload/remaining-batches.input.json\",\n    \"extraction\": \".fixtures[\\\"additional/dead-path/<name>\\\"]\",\n    \"files\": [\n      \"handler.mjs\",\n      \"caller.mjs\",\n      \"instructions.md\",\n      \"duplicate-reference.md\",\n      \"scope.md\"\n    ],\n    \"fullCaseContract\": \"case-contract.json\",\n    \"originalInputs\": \"original-inputs/\",\n    \"scopeContract\": \"original-inputs/scope.md\"\n  },\n  \"installedSource\": {\n    \"path\": \"/root/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-subtract-before-you-add/SKILL.md\",\n    \"copy\": \"sources/principle-subtract-before-you-add.SKILL.md\",\n    \"disableModelInvocation\": true,\n    \"sourceReadToolChunk\": \"5abe5f\",\n    \"capabilityGuide\": \"sources/host-capabilities.md\",\n    \"noInstalledSourceEdits\": true\n  },\n  \"canonicalPathMapping\": [\n    {\n      \"upstream\": \"agents/poteto-agent.md\",\n      \"installed\": \"references/agent-prompts/poteto-agent.md\",\n      \"actualMappedRead\": {\n        \"tool\": \"tools.exec_command\",\n        \"chunk\": \"882bae\",\n        \"exitCode\": 0,\n        \"contentRetained\": \"sources/poteto-agent.md\"\n      },\n      \"interpretation\": \"Packaged support is available at its canonical mapped path; a prior failed upstream pathname is not proof of missing packaged support.\"\n    },\n    {\n      \"upstream\": \"agents/comment-sicko.md\",\n      \"installed\": \"references/agent-prompts/comment-sicko.md\",\n      \"actualMappedRead\": {\n        \"tool\": \"tools.exec_command\",\n        \"chunk\": \"882bae\",\n        \"exitCode\": 0,\n        \"contentRetained\": \"sources/comment-sicko.md\"\n      },\n      \"interpretation\": \"Packaged support is available at its canonical mapped path; a prior failed upstream pathname is not proof of missing packaged support.\"\n    }\n  ],\n  \"sequence\": [\n    {\n      \"order\": 1,\n      \"action\": \"Read installed skill, full case and scope, original code and caller usage\",\n      \"toolChunks\": [\n        \"5abe5f\",\n        \"882bae\"\n      ]\n    },\n    {\n      \"order\": 2,\n      \"action\": \"Materialize fresh original fixture inputs and preserve prior attempt\",\n      \"toolChunk\": \"a4907b\"\n    },\n    {\n      \"order\": 3,\n      \"action\": \"Apply only subtraction in stages/01-removal\",\n      \"tool\": \"tools.apply_patch\",\n      \"rawResult\": {}\n    },\n    {\n      \"order\": 4,\n      \"action\": \"Save/read back removal-only files, diff and hashes before replacement exists\",\n      \"toolChunk\": \"10bd5e\",\n      \"checkpoint\": \"evidence/01-removal-checkpoint.json\",\n      \"readback\": \"evidence/01-removal-readback.txt\",\n      \"diff\": \"evidence/01-removal.diff\"\n    },\n    {\n      \"order\": 5,\n      \"action\": \"Read saved checkpoint and verify removal hashes, then copy removal stage into new replacement directory\",\n      \"toolChunk\": \"1c9638\"\n    },\n    {\n      \"order\": 6,\n      \"action\": \"Add scoped optional note passthrough only in stages/02-replacement/handler.mjs\",\n      \"tool\": \"tools.apply_patch\",\n      \"rawResult\": {}\n    },\n    {\n      \"order\": 7,\n      \"action\": \"Save/read back replacement, diff against removal and recheck removal/prior hashes\",\n      \"toolChunk\": \"516299\",\n      \"readback\": \"evidence/02-replacement-readback.txt\",\n      \"diff\": \"evidence/02-replacement.diff\"\n    }\n  ],\n  \"observedFileChecks\": {\n    \"removalDiffExit\": 1,\n    \"removalDiffMeaning\": \"Differences found, not error\",\n    \"removalObsoleteAndNoteSearchExit\": 1,\n    \"searchMeaning\": \"No obsoleteRequest, redundantValid or request.note match in removal handler\",\n    \"removalDuplicateReferenceAbsenceExit\": 0,\n    \"removalCallerComparisonExit\": 0,\n    \"replacementDirectoryAbsentAtRemovalReadbackExit\": 0,\n    \"replacementDiffExit\": 1,\n    \"replacementDiffMeaning\": \"Only handler.mjs changed relative to saved removal stage\",\n    \"removalHashReadback\": \"All four files matched before and after adding replacement\",\n    \"priorCaseHashReadbackExit\": 0,\n    \"priorDeliverablesHashReadback\": \"All four named prior deliverables matched\",\n    \"replacementCallerComparisonExit\": 0,\n    \"replacementInstructionsComparisonExit\": 0\n  },\n  \"replacementSemantics\": {\n    \"source\": \"stages/02-replacement/handler.mjs\",\n    \"implementation\": \"Creates {id,status:'accepted'}, adds note only when request.note !== undefined, returns response.\",\n    \"undefinedInterpretation\": \"An undefined note is omitted; no new parser or validator was added.\",\n    \"behaviorObserved\": false\n  },\n  \"unexecutedChecks\": [\n    {\n      \"check\": \"Execute original and final supportedRequest({id:'r1'}) and compare literal {id:'r1',status:'accepted'}\",\n      \"reason\": \"Bun absent; no substitute runtime authorized\"\n    },\n    {\n      \"check\": \"Execute supportedRequest({id:'r1',note:'hello'}) and compare literal note passthrough\",\n      \"reason\": \"Bun absent\"\n    },\n    {\n      \"check\": \"Execute omitted/undefined note and empty-string note cases\",\n      \"reason\": \"Bun absent; source inspection is not an observed output\"\n    },\n    {\n      \"check\": \"Run caller integration and tests covering removal of obsolete export/validator\",\n      \"reason\": \"Bun absent; no runtime check performed\"\n    },\n    {\n      \"check\": \"Syntax, lint, test runner, package evidence validator or compilation\",\n      \"reason\": \"Not executed; no alternate runtime, dependency installation or configuration authorized\"\n    }\n  ],\n  \"capabilities\": {\n    \"fileReads\": \"Observed\",\n    \"sandboxWrites\": \"Observed\",\n    \"diffsReadbackAndHashes\": \"Observed with native file tools\",\n    \"bun\": \"command -v bun returned exit 1 and no path in chunk 5abe5f\",\n    \"runtimeExecution\": \"Not performed\",\n    \"workers\": \"Not invoked; no independent worker requirement for this direct scoped rerun\",\n    \"durablePersistence\": \"Not tested; sandbox artifacts only\"\n  },\n  \"restrictions\": {\n    \"liveServices\": false,\n    \"installedPackageEdits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"commits\": false,\n    \"nodeOrPythonSubstitution\": false\n  },\n  \"rawToolEvidence\": {\n    \"capture\": \"Each primary tool return was stored immediately after the awaited call. Removal-stage raw snapshot was saved before creating replacement. Full retained returns follow in evidence/tool-returns.json.\",\n    \"removalSnapshot\": \"evidence/00-through-removal-tool-returns.json\",\n    \"packagingBoundary\": \"Final archive transport metadata remains in the conversation; no reconstructed receipts or fabricated runtime outcomes.\"\n  }\n}\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/stages/01-removal/handler.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/stages/01-removal/handler.mjs",
      "sha256": "8e33a884b99b3be3c4d4c7f6c63e2c619b322d968b5f061bd155744b0b273db0",
      "bytes": 93,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "export function supportedRequest(request) { return { id: request.id, status: 'accepted' }; }\n"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/stages/02-replacement/handler.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/stages/02-replacement/handler.mjs",
      "sha256": "53a8ea5210c43ef794af64baa29a225b70cc333b5661e1734823a25e832d2758",
      "bytes": 188,
      "owners": [
        "grades-chatgpt-rerun-01.json#0"
      ],
      "text": "export function supportedRequest(request) {\n  const response = { id: request.id, status: 'accepted' };\n  if (request.note !== undefined) response.note = request.note;\n  return response;\n}\n"
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
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/00-through-removal-tool-returns.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/00-through-removal-tool-returns.json",
      "sha256": "0cfdf9315c92dc0748b60f48f120d29d21a38d1358705671552c6a0dd09251e8",
      "bytes": 29260,
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "Source-read capture hash retained; pinned source text is reconstructible and not duplicated"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/through-replacement-tool-returns.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/through-replacement-tool-returns.json",
      "sha256": "7fdb4e79b2651bf5f58457daa60d79d4538fbb5650135e70a9adcb5ab6ae19f6",
      "bytes": 65997,
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "Source-read capture hash retained; pinned source text is reconstructible and not duplicated"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/tool-returns.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/dead-path-rerun/dead-path-rerun-01/evidence/tool-returns.json",
      "sha256": "26f2d83e478e8fe55cc264a51b5304f16a351a9c87a8a7bc2e97c9524e2087d7",
      "bytes": 143294,
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "Source-read capture hash retained; pinned source text is reconstructible and not duplicated"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/original-inputs",
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/prior-attempt",
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/sources",
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/stages/01-removal/caller.mjs",
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/stages/01-removal/instructions.md",
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/stages/01-removal/scope.md",
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/stages/02-replacement/caller.mjs",
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/stages/02-replacement/instructions.md",
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "chatgpt/dead-path-rerun/dead-path-rerun-01/stages/02-replacement/scope.md",
      "owner": "grades-chatgpt-rerun-01.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
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
