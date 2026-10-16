# codex: unsupported-selected-model

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "unsupported-selected-model",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-12.json#3",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "The requested model is unavailable or rejects the selected effort.",
  "caseDefinition": {
    "id": "unsupported-selected-model",
    "sourcePaths": [
      "agents/poteto-agent.md",
      "agents/comment-sicko.md"
    ],
    "prompt": "The requested model is unavailable or rejects the selected effort.",
    "requirements": [
      "Record the rejected request and supported effort; disclose any inherited fallback before proceeding.",
      "Read portable role instructions; bind operations to observed session capabilities."
    ],
    "expectedFull": "Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.",
    "expectedReduced": "Authorized sequential role review preserves scope and reports reduced capability. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.",
    "expectedBlocked": "Required independent worker or selected model is unavailable and fallback is not authorized; stop dependent work and record blocked.",
    "forbiddenClaims": [
      "Requested model proves actual model.",
      "Different role names prove model diversity.",
      "Unknown actual models establish diversity.",
      "Cached documentation proves current session tools.",
      "Portable prompt files register custom agents.",
      "Sequential fallback is independent workers or full pass."
    ],
    "caseFile": "docs/parity/cases/model-roles.json"
  },
  "registry": {
    "caseId": "unsupported-selected-model",
    "caseFile": "docs/parity/cases/model-roles.json",
    "sourcePaths": [
      "agents/poteto-agent.md",
      "agents/comment-sicko.md"
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
  "attempts": [
    {
      "attemptId": "grades-native-12.json#3",
      "order": 0,
      "gradeFile": "grades-native-12.json",
      "rankWithinFile": 3,
      "host": "codex",
      "caseId": "unsupported-selected-model",
      "status": "pass",
      "grade": {
        "caseId": "unsupported-selected-model",
        "host": "codex",
        "status": "pass",
        "execution": "workers",
        "rawTrace": "codex/batch-12.events.jsonl",
        "actualReadEventIds": [
          "item_14",
          "item_36",
          "item_38",
          "item_41"
        ],
        "actualExecutionEventIds": [
          "item_41"
        ],
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "review-outcome"
        ],
        "missing": [],
        "review": "Retains actual host-validation rejection of unavailable model and unsupported effort, then disclosed inherited fallback to a fresh native readonly worker. Returned comment review and parent source inspection are concrete. Rejected selections are not represented as successful, and actual fallback model/effort remain unknown.",
        "responseArtifact": "fixtures/batch-12/unsupported-selected-model.result.md",
        "variantReview": [
          "Actual case-owned source/artifacts and native trace reviewed; conditional withholding is simulation unless a concrete host error is preserved.",
          "No schema-validator, bookkeeping label, compiler version, or verification script selfgrade is accepted as workflow success."
        ],
        "limits": [
          "Original source freeze and actual task input revision are distinct.",
          "Native coordinator capture and actual worker artifact/result evidence are scoped; complete offline native envelope or process teardown is not inferred."
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "evidence": [
          "fixtures/batch-12/unsupported-selected-model/observations.json",
          "fixtures/batch-12/unsupported-selected-model/fallback-receipt.json",
          "fixtures/batch-12/unsupported-selected-model/fallback-response.txt"
        ],
        "fullExpected": "Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Record the rejected request and supported effort; disclose any inherited fallback before proceeding."
      },
      "topLevelContext": {
        "attempt": "batch-12",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "All six cases independently reviewed against full/reduced contracts. Full program or app behavior is not inferred from structural checkers.",
          "Actual native operation captures can be inspected in case artifacts; top-level trace command/item locators are not fabricated worker event ids."
        ]
      },
      "response": {
        "text": "# unsupported-selected-model\n\nThe host rejected an unavailable model and an invalid effort. After disclosure, an inherited fallback produced an inspected read-only comment review. Its actual model and effort remain unknown.\n\nThe supplied prompt and acceptance contract are in `unsupported-selected-model/supplied-input.json`. Both named portable prompts were read through the exposed file execution tool from installed pstack-openai 0.1.0. Their bytes and hashes are in `source-readback.txt` and `source-inventory.json`. The portable prompts route to `references/agent-prompts/`, as explicitly named by the user; they do not register custom agents. The actual capability and model-role contracts were read before selecting operations. No other package version was used.\n\n## Native rejection trials\n\nThe real exposed operation was `collaboration.spawn_agent`. These intentionally invalid probes exercise rejection without inventing a service failure. They were rejected by host validation before creating a worker.\n\n| Request | Actual tool result |\n| --- | --- |\n| Model fixture-unavailable-model, effort fixture-unsupported-effort, fork none | `Unknown model fixture-unavailable-model for spawn_agent`. Available models reported were gpt-6.1-sol, gpt-6-astra, gpt-6-sol, gpt-6-luna and gpt-5.6-sol. |\n| Model gpt-6.1-sol, effort fixture-unsupported-effort, fork none | `Reasoning effort fixture-unsupported-effort is not supported for model gpt-6.1-sol`. Supported efforts reported were low, medium, high, xhigh, max and ultra. |\n\n`unsupported-selected-model/observations.json` retains the requests and verbatim tool messages. There is no worker identity or actual model for either rejected attempt. The supported effort values are observations of current host validation for gpt-6.1-sol, not a claim that the later inherited fallback used one of them. No retry with an unsupported explicit selection was performed.\n\n## Disclosed fallback and actual response\n\nBefore proceeding, the coordinator told the user it would retain both rejections and use an inherited fallback where authorized, while keeping absent actual telemetry unknown. The task permits the inherited alternative and does not require the deliberately invalid sentinel model. A real exact-model requirement would instead block dependent work.\n\nThe next successful `collaboration.spawn_agent` omitted model and effort and used full-history inheritance. It supplied the complete comment-sicko prompt, assignment `unsupported-selected-model-fallback-v1`, exact input SHA `933a5f5df924b2b089f410615f99af7851010643`, and the single copied scoped file `unsupported-selected-model/dashboard.mjs`. Read-only review was authorized; no application edits, comment writes, nested workers or external actions were permitted. The native receipt returned `{\"task_name\":\"/root/inherited_fallback_observation\"}`. This was a fresh worker, not a resumed rejected attempt.\n\nThe actual returned terminal response is in `unsupported-selected-model/fallback-response.txt`. The coordinator inspected it and the scoped source. The source contains two functions and no comments, so zero actual deletions, no touched files and no MUST KILL flags are supported. The worker independently checked the input commit and matching blob `92e482b756144714545be37621de0998854ca753`. The fallback receipt is preserved in `fallback-receipt.json`. The coordinator wrote and read back these result artifacts; the child made no file writes.\n\nRequested fallback model and effort are `inherit-parent`. Observed model and effort are `unknown`. This successful independent worker establishes a scoped comment review only. It does not prove the rejected selection worked, model diversity, background or remote execution, application correctness, behavior testing, or complete workflow parity. Different role prompts never establish different model families.\n\nThe source freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c` is supplied provenance. The installed tree has no Git metadata, so no package HEAD was verified. All source reads used the requested 0.1.0 root. The task input SHA is independently verified and distinct from plugin provenance and current output artifacts. No live service, installation, configuration change, commit, push, PR, message, publication or scheduling occurred.\n\nParent artifact readback and matching fixture Git blob checks are retained in `unsupported-selected-model/parent-inspection.json`.\n",
        "artifact": {
          "path": "fixtures/batch-12/unsupported-selected-model.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model.result.md",
          "sha256": "313c11627ffd7c37d4840b970c27f240b4b20f514a1a4f95aff3d4d037382f34",
          "bytes": 4442
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-12.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-12.events.jsonl",
            "sha256": "67954ee0571d6cdc9d2b8c299428822b19cd77b3146edb9a48ef7690ae013431",
            "bytes": 711397,
            "eventReferences": [
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9915ad0b5e250f091010676ae3cb5a68dd9248f26fc12086546b36ff73cffbca"
              },
              {
                "eventId": "item_14",
                "line": 27,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4a795edb33ae1d0568407fa6bfee2a6f3988c6220a90de4e7116cb02c0c15afe",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_36",
                "line": 67,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e3186f06c1abcf50f9e262185828a15544e7bef0319c6e68332867cac0b000f5"
              },
              {
                "eventId": "item_36",
                "line": 68,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "235aa4b3187137c005ce51ea485779dbe63e1efe082806322077ddfbec3514b2",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_38",
                "line": 71,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4c83dfa84abc2cbda382a254f2e6dbd466d0ddc02cf59294772c00c7f27575ad"
              },
              {
                "eventId": "item_38",
                "line": 72,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "011beda3aaf2215b173d01b79165f14e8e689a432478f4adb9e10b33e8ada974",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_41",
                "line": 76,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "cb5174c10a12d9354390b4d17be7167a20e72415844b2ad8b51bc6e36c565e94"
              },
              {
                "eventId": "item_41",
                "line": 77,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a56fa9796085f57f5117e8e370d9e14cf179db850675d667349a02da33fc994a",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_41",
                "line": 76,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "cb5174c10a12d9354390b4d17be7167a20e72415844b2ad8b51bc6e36c565e94"
              },
              {
                "eventId": "item_41",
                "line": 77,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a56fa9796085f57f5117e8e370d9e14cf179db850675d667349a02da33fc994a",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/batch-12/unsupported-selected-model/observations.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model/observations.json",
            "sha256": "0a46afa8a65d0c0f80afc12d9a3fcca536d6cfb4d9ec8a223ff222945b0d572e",
            "bytes": 1461
          },
          {
            "path": "fixtures/batch-12/unsupported-selected-model/fallback-receipt.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model/fallback-receipt.json",
            "sha256": "f723e0664172088ffaf91aa54dca7d015d02531d6f1c8e9ab30f10b1e18821fd",
            "bytes": 909
          },
          {
            "path": "fixtures/batch-12/unsupported-selected-model/fallback-response.txt",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model/fallback-response.txt",
            "sha256": "5cb5a0561c42c054a3dbc62ea9d53f40d74032be5cd4b25cf5c26f1720488716",
            "bytes": 1378
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_14",
            "item_36",
            "item_38",
            "item_41"
          ],
          "actualExecutionEventIds": [
            "item_41"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-12/unsupported-selected-model/fallback-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model/fallback-receipt.json",
      "sha256": "f723e0664172088ffaf91aa54dca7d015d02531d6f1c8e9ab30f10b1e18821fd",
      "bytes": 909,
      "owners": [
        "grades-native-12.json#3"
      ],
      "text": "{\n  \"receiptKind\": \"Coordinator capture of native operation/result, not model telemetry\",\n  \"assignmentId\": \"unsupported-selected-model-fallback-v1\",\n  \"operation\": \"collaboration.spawn_agent\",\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"explicitSelectionOmitted\": true,\n  \"actualModel\": \"unknown\",\n  \"actualEffort\": \"unknown\",\n  \"workerId\": \"/root/inherited_fallback_observation\",\n  \"returned\": {\"task_name\": \"/root/inherited_fallback_observation\"},\n  \"role\": \"comment-sicko\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"scope\": \"Read-only unsupported-selected-model/dashboard.mjs comment review, no edits\",\n  \"outputOwner\": \"coordinator capturing returned read-only artifact\",\n  \"resultArtifact\": \"unsupported-selected-model/fallback-response.txt\",\n  \"terminalObserved\": \"FINAL_ANSWER\",\n  \"resultInspected\": true,\n  \"modelDiversity\": \"unverified\"\n}\n"
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/fallback-response.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model/fallback-response.txt",
      "sha256": "5cb5a0561c42c054a3dbc62ea9d53f40d74032be5cd4b25cf5c26f1720488716",
      "bytes": 1378,
      "owners": [
        "grades-native-12.json#3"
      ],
      "text": "Worker: `/root/inherited_fallback_observation`  \nAssignment: `unsupported-selected-model-fallback-v1`\n\nRequested model/effort: `inherit-parent` / `inherit-parent`. Actual model/effort: **unknown**. The supplied rejection record reports supported `gpt-6.1-sol` efforts as `low`, `medium`, `high`, `xhigh`, `max`, `ultra`; inheritance does not identify the fallback’s actual selection.\n\nRead both portable role prompts plus `references/model-roles.md` and `references/host-capabilities.md` from package `0.1.0`. Observed reads and Git commands used `functions.exec` → `tools.exec_command`, exit status 0. No nested workers.\n\nVerified input commit `933a5f5df924b2b089f410615f99af7851010643`. Scoped `unsupported-selected-model/dashboard.mjs` has Git blob `92e482b756144714545be37621de0998854ca753`, matching `committed-inputs/dashboard.mjs` at that commit.\n\nReviewed only `unsupported-selected-model/dashboard.mjs`. It contains two exported functions and no comments.\n\n- Touched files: none.\n- Actual deletions: **0**.\n- Proposed deletions: none.\n- `MUST KILL` flags: none.\n- Skips: application correctness and behavior testing are outside this comment-review scope. Actual model and effort metadata were not exposed; model diversity remains unverified.\n\nThe two prior rejection observations were read from the coordinator’s record; this worker did not execute those probes.\n"
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/observations.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model/observations.json",
      "sha256": "0a46afa8a65d0c0f80afc12d9a3fcca536d6cfb4d9ec8a223ff222945b0d572e",
      "bytes": 1461,
      "owners": [
        "grades-native-12.json#3"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"operation\": \"collaboration.spawn_agent\",\n  \"attempts\": [\n    {\n      \"task_name\": \"unsupported_model_probe\",\n      \"fork_turns\": \"none\",\n      \"requestedModel\": \"fixture-unavailable-model\",\n      \"requestedEffort\": \"fixture-unsupported-effort\",\n      \"toolResult\": \"Unknown model `fixture-unavailable-model` for spawn_agent. Available models: gpt-6.1-sol, gpt-6-astra, gpt-6-sol, gpt-6-luna, gpt-5.6-sol\",\n      \"workerId\": null,\n      \"actualModel\": \"unknown\",\n      \"actualEffort\": \"unknown\"\n    },\n    {\n      \"task_name\": \"unsupported_effort_probe\",\n      \"fork_turns\": \"none\",\n      \"requestedModel\": \"gpt-6.1-sol\",\n      \"requestedEffort\": \"fixture-unsupported-effort\",\n      \"toolResult\": \"Reasoning effort `fixture-unsupported-effort` is not supported for model `gpt-6.1-sol`. Supported reasoning efforts: low, medium, high, xhigh, max, ultra\",\n      \"workerId\": null,\n      \"actualModel\": \"unknown\",\n      \"actualEffort\": \"unknown\",\n      \"supportedEfforts\": [\"low\", \"medium\", \"high\", \"xhigh\", \"max\", \"ultra\"]\n    }\n  ],\n  \"fallbackDisclosure\": \"The host rejected both the unavailable model and the unsupported effort probes, and returned the supported choices. I will retain those rejections and use an inherited fallback where authorized. Spawn receipts that omit actual model metadata will remain unknown.\",\n  \"receiptKind\": \"Coordinator capture of actual native tool results in this turn, not provider model telemetry\"\n}\n"
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/parent-inspection.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model/parent-inspection.json",
      "sha256": "822c87c16236da5dc6a8c9a49f88e24720dae0e254f314803eb291cee6d90220",
      "bytes": 2352,
      "owners": [
        "grades-native-12.json#3"
      ],
      "text": "{\n  \"commands\": [\n    {\n      \"argv\": [\n        \"git\",\n        \"rev-parse\",\n        \"HEAD\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"933a5f5df924b2b089f410615f99af7851010643\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"argv\": [\n        \"git\",\n        \"hash-object\",\n        \"unsupported-selected-model/dashboard.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"92e482b756144714545be37621de0998854ca753\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"argv\": [\n        \"git\",\n        \"rev-parse\",\n        \"933a5f5df924b2b089f410615f99af7851010643:committed-inputs/dashboard.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"92e482b756144714545be37621de0998854ca753\\n\",\n      \"stderr\": \"\"\n    }\n  ],\n  \"source\": \"export function visible(orders,status){return orders.filter(o=>o.status===status)}\\nexport function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n\",\n  \"workerResponse\": \"Worker: `/root/inherited_fallback_observation`  \\nAssignment: `unsupported-selected-model-fallback-v1`\\n\\nRequested model/effort: `inherit-parent` / `inherit-parent`. Actual model/effort: **unknown**. The supplied rejection record reports supported `gpt-6.1-sol` efforts as `low`, `medium`, `high`, `xhigh`, `max`, `ultra`; inheritance does not identify the fallback’s actual selection.\\n\\nRead both portable role prompts plus `references/model-roles.md` and `references/host-capabilities.md` from package `0.1.0`. Observed reads and Git commands used `functions.exec` → `tools.exec_command`, exit status 0. No nested workers.\\n\\nVerified input commit `933a5f5df924b2b089f410615f99af7851010643`. Scoped `unsupported-selected-model/dashboard.mjs` has Git blob `92e482b756144714545be37621de0998854ca753`, matching `committed-inputs/dashboard.mjs` at that commit.\\n\\nReviewed only `unsupported-selected-model/dashboard.mjs`. It contains two exported functions and no comments.\\n\\n- Touched files: none.\\n- Actual deletions: **0**.\\n- Proposed deletions: none.\\n- `MUST KILL` flags: none.\\n- Skips: application correctness and behavior testing are outside this comment-review scope. Actual model and effort metadata were not exposed; model diversity remains unverified.\\n\\nThe two prior rejection observations were read from the coordinator’s record; this worker did not execute those probes.\\n\"\n}"
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/source-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model/source-inventory.json",
      "sha256": "00729eb628d4c012e88ef392f7f1516c222612c7c0d4666b269b873d1463407a",
      "bytes": 588,
      "owners": [
        "grades-native-12.json#3"
      ],
      "text": "[\n  {\n    \"requested\": \"agents/poteto-agent.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\",\n    \"bytes\": 1221,\n    \"sha256\": \"9839239c6ebc72de8165f8a6fa4a6326fea7293e15a47d24f98396df2a61b3fb\"\n  },\n  {\n    \"requested\": \"agents/comment-sicko.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/comment-sicko.md\",\n    \"bytes\": 3625,\n    \"sha256\": \"5d119d21ad7184209fd6d375d3232acf468e2c8700d186934f8f24ca5c7e668e\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model/supplied-input.json",
      "sha256": "feab667669c83a494b7ce1864cc8ec2807239bcabd2910b715bf4e0e8fc27b9a",
      "bytes": 1432,
      "owners": [
        "grades-native-12.json#3"
      ],
      "text": "{\n  \"id\": \"unsupported-selected-model\",\n  \"sourcePaths\": [\n    \"agents/poteto-agent.md\",\n    \"agents/comment-sicko.md\"\n  ],\n  \"prompt\": \"The requested model is unavailable or rejects the selected effort.\",\n  \"requirements\": [\n    \"Record the rejected request and supported effort; disclose any inherited fallback before proceeding.\",\n    \"Read portable role instructions; bind operations to observed session capabilities.\"\n  ],\n  \"expectedFull\": \"Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.\",\n  \"expectedReduced\": \"Authorized sequential role review preserves scope and reports reduced capability. Record the rejected request and supported effort; disclose any inherited fallback before proceeding.\",\n  \"expectedBlocked\": \"Required independent worker or selected model is unavailable and fallback is not authorized; stop dependent work and record blocked.\",\n  \"forbiddenClaims\": [\n    \"Requested model proves actual model.\",\n    \"Different role names prove model diversity.\",\n    \"Unknown actual models establish diversity.\",\n    \"Cached documentation proves current session tools.\",\n    \"Portable prompt files register custom agents.\",\n    \"Sequential fallback is independent workers or full pass.\"\n  ],\n  \"caseFile\": \"docs/parity/cases/model-roles.json\"\n}"
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unsupported-selected-model.result.md",
      "sha256": "313c11627ffd7c37d4840b970c27f240b4b20f514a1a4f95aff3d4d037382f34",
      "bytes": 4442,
      "owners": [
        "grades-native-12.json#3"
      ],
      "text": "# unsupported-selected-model\n\nThe host rejected an unavailable model and an invalid effort. After disclosure, an inherited fallback produced an inspected read-only comment review. Its actual model and effort remain unknown.\n\nThe supplied prompt and acceptance contract are in `unsupported-selected-model/supplied-input.json`. Both named portable prompts were read through the exposed file execution tool from installed pstack-openai 0.1.0. Their bytes and hashes are in `source-readback.txt` and `source-inventory.json`. The portable prompts route to `references/agent-prompts/`, as explicitly named by the user; they do not register custom agents. The actual capability and model-role contracts were read before selecting operations. No other package version was used.\n\n## Native rejection trials\n\nThe real exposed operation was `collaboration.spawn_agent`. These intentionally invalid probes exercise rejection without inventing a service failure. They were rejected by host validation before creating a worker.\n\n| Request | Actual tool result |\n| --- | --- |\n| Model fixture-unavailable-model, effort fixture-unsupported-effort, fork none | `Unknown model fixture-unavailable-model for spawn_agent`. Available models reported were gpt-6.1-sol, gpt-6-astra, gpt-6-sol, gpt-6-luna and gpt-5.6-sol. |\n| Model gpt-6.1-sol, effort fixture-unsupported-effort, fork none | `Reasoning effort fixture-unsupported-effort is not supported for model gpt-6.1-sol`. Supported efforts reported were low, medium, high, xhigh, max and ultra. |\n\n`unsupported-selected-model/observations.json` retains the requests and verbatim tool messages. There is no worker identity or actual model for either rejected attempt. The supported effort values are observations of current host validation for gpt-6.1-sol, not a claim that the later inherited fallback used one of them. No retry with an unsupported explicit selection was performed.\n\n## Disclosed fallback and actual response\n\nBefore proceeding, the coordinator told the user it would retain both rejections and use an inherited fallback where authorized, while keeping absent actual telemetry unknown. The task permits the inherited alternative and does not require the deliberately invalid sentinel model. A real exact-model requirement would instead block dependent work.\n\nThe next successful `collaboration.spawn_agent` omitted model and effort and used full-history inheritance. It supplied the complete comment-sicko prompt, assignment `unsupported-selected-model-fallback-v1`, exact input SHA `933a5f5df924b2b089f410615f99af7851010643`, and the single copied scoped file `unsupported-selected-model/dashboard.mjs`. Read-only review was authorized; no application edits, comment writes, nested workers or external actions were permitted. The native receipt returned `{\"task_name\":\"/root/inherited_fallback_observation\"}`. This was a fresh worker, not a resumed rejected attempt.\n\nThe actual returned terminal response is in `unsupported-selected-model/fallback-response.txt`. The coordinator inspected it and the scoped source. The source contains two functions and no comments, so zero actual deletions, no touched files and no MUST KILL flags are supported. The worker independently checked the input commit and matching blob `92e482b756144714545be37621de0998854ca753`. The fallback receipt is preserved in `fallback-receipt.json`. The coordinator wrote and read back these result artifacts; the child made no file writes.\n\nRequested fallback model and effort are `inherit-parent`. Observed model and effort are `unknown`. This successful independent worker establishes a scoped comment review only. It does not prove the rejected selection worked, model diversity, background or remote execution, application correctness, behavior testing, or complete workflow parity. Different role prompts never establish different model families.\n\nThe source freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c` is supplied provenance. The installed tree has no Git metadata, so no package HEAD was verified. All source reads used the requested 0.1.0 root. The task input SHA is independently verified and distinct from plugin provenance and current output artifacts. No live service, installation, configuration change, commit, push, PR, message, publication or scheduling occurred.\n\nParent artifact readback and matching fixture Git blob checks are retained in `unsupported-selected-model/parent-inspection.json`.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-12/unsupported-selected-model/dashboard.mjs",
      "owner": "grades-native-12.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/orders.json",
      "owner": "grades-native-12.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/source-readback.txt",
      "owner": "grades-native-12.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/dashboard.mjs",
      "owner": "grades-native-12.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/orders.json",
      "owner": "grades-native-12.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/unsupported-selected-model/source-readback.txt",
      "owner": "grades-native-12.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    }
  ],
  "globalLimits": [
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
