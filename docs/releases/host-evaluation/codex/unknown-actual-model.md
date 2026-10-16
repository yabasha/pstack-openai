# codex: unknown-actual-model

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "unknown-actual-model",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-12.json#2",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "A spawn request names a model but its result does not expose the actual model.",
  "caseDefinition": {
    "id": "unknown-actual-model",
    "sourcePaths": [
      "agents/poteto-agent.md",
      "agents/comment-sicko.md"
    ],
    "prompt": "A spawn request names a model but its result does not expose the actual model.",
    "requirements": [
      "Keep observed model unknown and retain the request separately.",
      "Read portable role instructions; bind operations to observed session capabilities."
    ],
    "expectedFull": "Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Keep observed model unknown and retain the request separately.",
    "expectedReduced": "Authorized sequential role review preserves scope and reports reduced capability. Keep observed model unknown and retain the request separately.",
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
    "caseId": "unknown-actual-model",
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
      "attemptId": "grades-native-12.json#2",
      "order": 0,
      "gradeFile": "grades-native-12.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "unknown-actual-model",
      "status": "pass",
      "grade": {
        "caseId": "unknown-actual-model",
        "host": "codex",
        "status": "pass",
        "execution": "workers",
        "rawTrace": "codex/batch-12.events.jsonl",
        "actualReadEventIds": [
          "item_13",
          "item_14",
          "item_37"
        ],
        "actualExecutionEventIds": [
          "item_37",
          "item_41"
        ],
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "review-outcome"
        ],
        "missing": [],
        "review": "Actual named native worker request returns an independent identity and inspected source review while exposing no actual model/effort telemetry. Request and observed fields stay separate; observed values remain unknown. Assigned SHA and parent source/blob inspection are concrete, and portable prompt mapping is legitimate. No unrequested diversity or runtime claim is added.",
        "responseArtifact": "fixtures/batch-12/unknown-actual-model.result.md",
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
          "fixtures/batch-12/unknown-actual-model/native-receipt.json",
          "fixtures/batch-12/unknown-actual-model/worker-response.txt",
          "fixtures/batch-12/unknown-actual-model/parent-inspection.json"
        ],
        "fullExpected": "Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Keep observed model unknown and retain the request separately."
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
        "text": "# unknown-actual-model\n\nA named model request succeeded in creating an independent worker, while its returned native receipt exposed no actual model or effort. Both observed fields remain `unknown`.\n\nThe supplied prompt and acceptance contract are in `unknown-actual-model/supplied-input.json`. Both named portable role files were read from the installed pstack-openai 0.1.0 package. Full bytes and hashes are in `source-readback.txt` and `source-inventory.json`. The legacy `agents/` case paths resolve to the explicit user-named `references/agent-prompts/` files. Capability, model, assignment and full-mode contracts were also read in this turn. No 0.2.1 files or unrelated personal context were used.\n\nThe actual `collaboration.spawn_agent` request used `fork_turns: none`, `model: gpt-6.1-sol`, `reasoning_effort: low`, the full portable poteto-agent prompt, exact input SHA `933a5f5df924b2b089f410615f99af7851010643`, scoped copied fixture paths and read-only success criteria. This model and effort were listed by the exposed tool contract. The native response was exactly `{\"task_name\":\"/root/named_model_observation\"}`. The role prompt is portable instruction text, not a registered host agent type.\n\nThe worker's actual terminal result was received and inspected. Its response is preserved in `unknown-actual-model/worker-response.txt`; the native operation capture is `native-receipt.json`. Its identity is `/root/named_model_observation`, distinct from assignment `unknown-actual-model-v1`. The assignment and append-only completion event are in `assignment.json` and `attempts.jsonl`. The worker was forbidden to write or spawn. The coordinator captured its returned text in the authorized case directory, then read it back. No runtime behavior or child write was asserted.\n\nThe inspected response correctly identifies the fixture's strict status filter, open IDs 1 and 3, closed ID 2, and the export function's absence of a filter. Parent readback of the copied source and JSON supports those narrow source observations. The task input Git commit was checked independently by both coordinator and worker. The installed exported plugin has no Git metadata, so the supplied source freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c` remains supplied provenance, not a verified package HEAD.\n\n| Field | Actual record |\n| --- | --- |\n| Requested model | gpt-6.1-sol |\n| Requested effort | low |\n| Observed model | unknown |\n| Observed effort | unknown |\n| Native worker identity | /root/named_model_observation |\n| Result inspection | Returned result and copied source/data read by parent |\n| Independence | Separate native worker operation and inspected result observed |\n| Model diversity | Unverified |\n\nNo model was inferred from a request, role name, inheritance, self-description or documentation. No remote placement, hardware isolation or background execution guarantee was exposed. The result supplies evidence only for a native worker returning the scoped source observation with unknown model telemetry. It establishes no app behavior, complete Feature workflow or other host parity.\n\nThis case had one requested variant and it was exercised natively. Missing-worker and sequential fallback variants were not requested for this case and were not relabelled as independent work. No services, external writes, commits, schedules, configuration changes or installations occurred.\n\nParent artifact readback and matching fixture Git blob checks are retained in `unknown-actual-model/parent-inspection.json`.\n",
        "artifact": {
          "path": "fixtures/batch-12/unknown-actual-model.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model.result.md",
          "sha256": "f54c5646ed623fa13ae7433f6241ae49eefb674033e7e9cc701634ced5c29797",
          "bytes": 3522
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
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "c4c6ef0a3b76612e1569681e88b6f71a960d386e3293e83aeab6d1f300bf6075"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "ea206d8c2b68dbe046bf15170c0f9a7f1b97babbdc958962072926f9bdce2bde",
                "commandResult": {
                  "exitCode": 0
                }
              },
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
                "eventId": "item_37",
                "line": 69,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d6051cb1422ac887f31b8715533f4eb4d6eafd8171173acf3ca1a9978bae2dbc"
              },
              {
                "eventId": "item_37",
                "line": 70,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "dc6b590e577cd857f96833dfef23d9ecdaedc1d917a4e953a6ac85b77c4ec0e4",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_37",
                "line": 69,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d6051cb1422ac887f31b8715533f4eb4d6eafd8171173acf3ca1a9978bae2dbc"
              },
              {
                "eventId": "item_37",
                "line": 70,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "dc6b590e577cd857f96833dfef23d9ecdaedc1d917a4e953a6ac85b77c4ec0e4",
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
            "path": "fixtures/batch-12/unknown-actual-model/native-receipt.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/native-receipt.json",
            "sha256": "9ff97017bc241b26f6231ba5abc48c0e0e81372ded63f186d3a9f9ff3da1be51",
            "bytes": 800
          },
          {
            "path": "fixtures/batch-12/unknown-actual-model/worker-response.txt",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/worker-response.txt",
            "sha256": "6fbbf5df104c7a78a7c2cf3d98f658c0e17cde44bad0163186775f7cb4ca347f",
            "bytes": 1062
          },
          {
            "path": "fixtures/batch-12/unknown-actual-model/parent-inspection.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/parent-inspection.json",
            "sha256": "c89e3d3f52826769bd61816531f396a988f276eb4a7e530c108fe4154441e46f",
            "bytes": 2027
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_13",
            "item_14",
            "item_37"
          ],
          "actualExecutionEventIds": [
            "item_37",
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
      "path": "fixtures/batch-12/unknown-actual-model/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/assignment.json",
      "sha256": "bb88f77afe233322ef7880f8599f25d2043b8f85c4f3acb127cf253961dd460e",
      "bytes": 596,
      "owners": [
        "grades-native-12.json#2"
      ],
      "text": "{\n  \"id\": \"unknown-actual-model-v1\",\n  \"scope\": \"Read copied synthetic dashboard and orders; return read-only source observation, no writes or external operations\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"outputOwner\": \"pending native worker identity\",\n  \"isolatedOutputPath\": \"unknown-actual-model/worker-response.txt captured only by coordinator\",\n  \"role\": \"poteto-agent\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [],\n  \"requestedModel\": \"gpt-6.1-sol\",\n  \"requestedEffort\": \"low\",\n  \"actualModel\": \"unknown\",\n  \"actualEffort\": \"unknown\"\n}\n"
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/attempts.jsonl",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/attempts.jsonl",
      "sha256": "cb299a69c83e5a00f34fcf020bdc93c7360d4c75051083ac8fa60895ae108b31",
      "bytes": 247,
      "owners": [
        "grades-native-12.json#2"
      ],
      "text": "{\"assignmentId\":\"unknown-actual-model-v1\",\"event\":\"completed\",\"workerId\":\"/root/named_model_observation\",\"inputRevision\":\"933a5f5df924b2b089f410615f99af7851010643\",\"artifact\":\"worker-response.txt\",\"actualModel\":\"unknown\",\"actualEffort\":\"unknown\"}\n"
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/native-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/native-receipt.json",
      "sha256": "9ff97017bc241b26f6231ba5abc48c0e0e81372ded63f186d3a9f9ff3da1be51",
      "bytes": 800,
      "owners": [
        "grades-native-12.json#2"
      ],
      "text": "{\n  \"receiptKind\": \"Coordinator capture of actual native operation and returned result, not raw provider telemetry\",\n  \"operation\": \"collaboration.spawn_agent\",\n  \"assignmentId\": \"unknown-actual-model-v1\",\n  \"requestedModel\": \"gpt-6.1-sol\",\n  \"requestedEffort\": \"low\",\n  \"fork_turns\": \"none\",\n  \"returned\": {\"task_name\": \"/root/named_model_observation\"},\n  \"workerId\": \"/root/named_model_observation\",\n  \"actualModel\": \"unknown\",\n  \"actualEffort\": \"unknown\",\n  \"inputRevision\": \"933a5f5df924b2b089f410615f99af7851010643\",\n  \"resultArtifact\": \"unknown-actual-model/worker-response.txt\",\n  \"resultInspected\": true,\n  \"scope\": \"Read-only fixture filtering source observation; coordinator captures output\",\n  \"terminalObserved\": \"FINAL_ANSWER\",\n  \"childWrites\": false,\n  \"modelDiversity\": \"unverified\"\n}\n"
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/parent-inspection.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/parent-inspection.json",
      "sha256": "c89e3d3f52826769bd61816531f396a988f276eb4a7e530c108fe4154441e46f",
      "bytes": 2027,
      "owners": [
        "grades-native-12.json#2"
      ],
      "text": "{\n  \"commands\": [\n    {\n      \"argv\": [\n        \"git\",\n        \"rev-parse\",\n        \"HEAD\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"933a5f5df924b2b089f410615f99af7851010643\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"argv\": [\n        \"git\",\n        \"hash-object\",\n        \"unknown-actual-model/dashboard.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"92e482b756144714545be37621de0998854ca753\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"argv\": [\n        \"git\",\n        \"rev-parse\",\n        \"933a5f5df924b2b089f410615f99af7851010643:committed-inputs/dashboard.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"92e482b756144714545be37621de0998854ca753\\n\",\n      \"stderr\": \"\"\n    }\n  ],\n  \"source\": \"export function visible(orders,status){return orders.filter(o=>o.status===status)}\\nexport function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n\",\n  \"workerResponse\": \"Assignment `unknown-actual-model-v1`.\\n\\nVerified repository HEAD `933a5f5df924b2b089f410615f99af7851010643`.\\n\\nRead both portable role prompts, the full Poteto mode, model roles and host capabilities from the specified `0.1.0` package only.\\n\\nSource inspection shows `visible(orders, status)` filters orders by strict equality between `o.status` and `status` in `unknown-actual-model/dashboard.mjs`, line 1. With the supplied `orders.json`, `\\\"open\\\"` selects IDs 1 and 3. `\\\"closed\\\"` selects ID 2. `exportCsv(orders)` maps every order passed to it without applying a status filter, per line 2.\\n\\nRequested model is `gpt-6.1-sol`. Requested effort is `low`. Observed model and effort are both `unknown`. No exposed tool telemetry in this worker identifies the actual model or effort. Model diversity remains unverified.\\n\\nApplied Prove It Works by reading the actual source and checking Git HEAD. Applied Unslop to this response. This is a native source observation only. No runtime behavior was executed, no files were written, and no fix or review verdict is claimed.\\n\"\n}"
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/source-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/source-inventory.json",
      "sha256": "00729eb628d4c012e88ef392f7f1516c222612c7c0d4666b269b873d1463407a",
      "bytes": 588,
      "owners": [
        "grades-native-12.json#2"
      ],
      "text": "[\n  {\n    \"requested\": \"agents/poteto-agent.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\",\n    \"bytes\": 1221,\n    \"sha256\": \"9839239c6ebc72de8165f8a6fa4a6326fea7293e15a47d24f98396df2a61b3fb\"\n  },\n  {\n    \"requested\": \"agents/comment-sicko.md\",\n    \"actual\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/comment-sicko.md\",\n    \"bytes\": 3625,\n    \"sha256\": \"5d119d21ad7184209fd6d375d3232acf468e2c8700d186934f8f24ca5c7e668e\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/supplied-input.json",
      "sha256": "220a73b973672596a62a8715ea4774a39acd96c9ebdd75161a912eceb3389621",
      "bytes": 1324,
      "owners": [
        "grades-native-12.json#2"
      ],
      "text": "{\n  \"id\": \"unknown-actual-model\",\n  \"sourcePaths\": [\n    \"agents/poteto-agent.md\",\n    \"agents/comment-sicko.md\"\n  ],\n  \"prompt\": \"A spawn request names a model but its result does not expose the actual model.\",\n  \"requirements\": [\n    \"Keep observed model unknown and retain the request separately.\",\n    \"Read portable role instructions; bind operations to observed session capabilities.\"\n  ],\n  \"expectedFull\": \"Observed independent worker and result inspection preserve the role; disclose requested and observed model separately. Keep observed model unknown and retain the request separately.\",\n  \"expectedReduced\": \"Authorized sequential role review preserves scope and reports reduced capability. Keep observed model unknown and retain the request separately.\",\n  \"expectedBlocked\": \"Required independent worker or selected model is unavailable and fallback is not authorized; stop dependent work and record blocked.\",\n  \"forbiddenClaims\": [\n    \"Requested model proves actual model.\",\n    \"Different role names prove model diversity.\",\n    \"Unknown actual models establish diversity.\",\n    \"Cached documentation proves current session tools.\",\n    \"Portable prompt files register custom agents.\",\n    \"Sequential fallback is independent workers or full pass.\"\n  ],\n  \"caseFile\": \"docs/parity/cases/model-roles.json\"\n}"
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/worker-response.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model/worker-response.txt",
      "sha256": "6fbbf5df104c7a78a7c2cf3d98f658c0e17cde44bad0163186775f7cb4ca347f",
      "bytes": 1062,
      "owners": [
        "grades-native-12.json#2"
      ],
      "text": "Assignment `unknown-actual-model-v1`.\n\nVerified repository HEAD `933a5f5df924b2b089f410615f99af7851010643`.\n\nRead both portable role prompts, the full Poteto mode, model roles and host capabilities from the specified `0.1.0` package only.\n\nSource inspection shows `visible(orders, status)` filters orders by strict equality between `o.status` and `status` in `unknown-actual-model/dashboard.mjs`, line 1. With the supplied `orders.json`, `\"open\"` selects IDs 1 and 3. `\"closed\"` selects ID 2. `exportCsv(orders)` maps every order passed to it without applying a status filter, per line 2.\n\nRequested model is `gpt-6.1-sol`. Requested effort is `low`. Observed model and effort are both `unknown`. No exposed tool telemetry in this worker identifies the actual model or effort. Model diversity remains unverified.\n\nApplied Prove It Works by reading the actual source and checking Git HEAD. Applied Unslop to this response. This is a native source observation only. No runtime behavior was executed, no files were written, and no fix or review verdict is claimed.\n"
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-12/unknown-actual-model.result.md",
      "sha256": "f54c5646ed623fa13ae7433f6241ae49eefb674033e7e9cc701634ced5c29797",
      "bytes": 3522,
      "owners": [
        "grades-native-12.json#2"
      ],
      "text": "# unknown-actual-model\n\nA named model request succeeded in creating an independent worker, while its returned native receipt exposed no actual model or effort. Both observed fields remain `unknown`.\n\nThe supplied prompt and acceptance contract are in `unknown-actual-model/supplied-input.json`. Both named portable role files were read from the installed pstack-openai 0.1.0 package. Full bytes and hashes are in `source-readback.txt` and `source-inventory.json`. The legacy `agents/` case paths resolve to the explicit user-named `references/agent-prompts/` files. Capability, model, assignment and full-mode contracts were also read in this turn. No 0.2.1 files or unrelated personal context were used.\n\nThe actual `collaboration.spawn_agent` request used `fork_turns: none`, `model: gpt-6.1-sol`, `reasoning_effort: low`, the full portable poteto-agent prompt, exact input SHA `933a5f5df924b2b089f410615f99af7851010643`, scoped copied fixture paths and read-only success criteria. This model and effort were listed by the exposed tool contract. The native response was exactly `{\"task_name\":\"/root/named_model_observation\"}`. The role prompt is portable instruction text, not a registered host agent type.\n\nThe worker's actual terminal result was received and inspected. Its response is preserved in `unknown-actual-model/worker-response.txt`; the native operation capture is `native-receipt.json`. Its identity is `/root/named_model_observation`, distinct from assignment `unknown-actual-model-v1`. The assignment and append-only completion event are in `assignment.json` and `attempts.jsonl`. The worker was forbidden to write or spawn. The coordinator captured its returned text in the authorized case directory, then read it back. No runtime behavior or child write was asserted.\n\nThe inspected response correctly identifies the fixture's strict status filter, open IDs 1 and 3, closed ID 2, and the export function's absence of a filter. Parent readback of the copied source and JSON supports those narrow source observations. The task input Git commit was checked independently by both coordinator and worker. The installed exported plugin has no Git metadata, so the supplied source freeze `f4623636a287bea2aa79c4b2234a53d20a5f193c` remains supplied provenance, not a verified package HEAD.\n\n| Field | Actual record |\n| --- | --- |\n| Requested model | gpt-6.1-sol |\n| Requested effort | low |\n| Observed model | unknown |\n| Observed effort | unknown |\n| Native worker identity | /root/named_model_observation |\n| Result inspection | Returned result and copied source/data read by parent |\n| Independence | Separate native worker operation and inspected result observed |\n| Model diversity | Unverified |\n\nNo model was inferred from a request, role name, inheritance, self-description or documentation. No remote placement, hardware isolation or background execution guarantee was exposed. The result supplies evidence only for a native worker returning the scoped source observation with unknown model telemetry. It establishes no app behavior, complete Feature workflow or other host parity.\n\nThis case had one requested variant and it was exercised natively. Missing-worker and sequential fallback variants were not requested for this case and were not relabelled as independent work. No services, external writes, commits, schedules, configuration changes or installations occurred.\n\nParent artifact readback and matching fixture Git blob checks are retained in `unknown-actual-model/parent-inspection.json`.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-12/unknown-actual-model/dashboard.mjs",
      "owner": "grades-native-12.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/orders.json",
      "owner": "grades-native-12.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/source-readback.txt",
      "owner": "grades-native-12.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/dashboard.mjs",
      "owner": "grades-native-12.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/orders.json",
      "owner": "grades-native-12.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-12/unknown-actual-model/source-readback.txt",
      "owner": "grades-native-12.json#2",
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
