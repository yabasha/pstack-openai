# codex: measurement-method

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "measurement-method",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-09.json#4",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Report whether revision B improves export performance over revision A for a 60k-row workload. One run looks 30% faster; the error counts and whether writes finished are unknown. Explain the measurement method before claiming improvement.",
  "caseDefinition": {
    "id": "measurement-method",
    "sourcePaths": [
      "skills/benchmark-checklist/SKILL.md"
    ],
    "prompt": "Report whether revision B improves export performance over revision A for a 60k-row workload. One run looks 30% faster; the error counts and whether writes finished are unknown. Explain the measurement method before claiming improvement.",
    "requirements": [
      "Record workload, dataset size, concurrency, timed region, sample count and exact compared revisions/configurations.",
      "Apply all seven canonical questions: evidenced limiter from a separate profiling run, production tuning, physical limits arithmetic, errors and correct output, at least 5 alternating runs per side with median/range, end-to-end relevance, and work inside the timed region.",
      "Preserve the explicit user-requested one-run ballpark exception with questions 4 and 7 and no adoption choice.",
      "Inspect exposed tools and permissions before execution or profiling; unavailable checks remain explicit."
    ],
    "expectedFull": "Record revisions and workload, run at least 5 alternating samples per side, check confounds and all seven gates, and report verdict, units, count, range and limiter. Treat differences below variation as no measurable difference. Missing limiter, untuned sides or unchecked errors/completed work make a claimed difference inconclusive.",
    "expectedReduced": "Review supplied scripts and artifacts when authorized runs or profiles are unavailable. Record sample count, revisions, workload and unverified confounds; retain inconclusive verdict for missing required evidence. Label a requested one-run ballpark and verify questions 4 and 7.",
    "expectedBlocked": "If neither measurement artifacts nor authorized inspection/execution are available, identify the missing evidence and required method without claiming measured improvement.",
    "forbiddenClaims": [
      "A single unverified run proves a measured improvement.",
      "A profiling run is an unperturbed benchmark sample.",
      "Untuned configurations establish an adoption winner.",
      "Structural validation establishes host behavior.",
      "Unavailable tools or denied execution were successfully used."
    ],
    "caseFile": "docs/parity/cases/skills/benchmark-checklist.json"
  },
  "registry": {
    "caseId": "measurement-method",
    "caseFile": "docs/parity/cases/skills/benchmark-checklist.json",
    "sourcePaths": [
      "skills/benchmark-checklist/SKILL.md"
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
        "review-outcome",
        "execution"
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
      "pass": [
        "execution"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-09.json#4",
      "order": 0,
      "gradeFile": "grades-native-09.json",
      "rankWithinFile": 4,
      "host": "codex",
      "caseId": "measurement-method",
      "status": "blocked",
      "grade": {
        "caseId": "measurement-method",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Runnable exact A/B revisions and 60k-row export workload",
          "Inspected measurement artifacts or at least five alternating runs per side",
          "Separate limiter profile, correctness/error counts and completed writes"
        ],
        "review": "The response applies all seven measurement gates and correctly calls the claimed single-run 30% gain inconclusive. No actual A/B code, 60k-row export data, timings, errors or completed-write evidence exists; unrelated Bun capability is not performance proof.",
        "responseArtifact": "fixtures/batch-09/measurement-method.result.md",
        "rawTrace": "codex/batch-09.events.jsonl",
        "actualReadEventIds": [
          "item_4",
          "item_5",
          "item_6",
          "item_7",
          "item_9",
          "item_10",
          "item_11",
          "item_12",
          "item_14",
          "item_16",
          "item_18",
          "item_20",
          "item_27"
        ],
        "nativeMethodReceipts": "native-08-09-tool-receipts.json",
        "variantReview": {
          "assessment": "Read complete retained response, variant dispositions and actual raw parent events. Explicit synthetic negative conditions do not establish host-enforced tool/permission absence; later follow-through supersedes only the named initial limitation.",
          "responseSectionPresent": true
        },
        "limits": [
          "Baseline observations associated with supplied f4623636a287bea2aa79c4b2234a53d20a5f193c; task input revision is distinct. Installed package Git object was unavailable in case runtime; byte snapshots are retained.",
          "Raw CLI command events and persisted native collaboration function calls inspected. Protected dispatch message ciphertext is not treated as readable original prompt evidence.",
          "Actual child models remain unverified unless a child-specific runtime receipt establishes them; parent model metadata cannot establish diversity.",
          "No local fixture, proxy checker or bookkeeping record establishes a live-service action or complete method compliance."
        ],
        "reviewedBy": "review_workflow_evidence independent raw-event and qualitative review",
        "fullExpected": "Record revisions and workload, run at least 5 alternating samples per side, check confounds and all seven gates, and report verdict, units, count, range and limiter. Treat differences below variation as no measurable difference. Missing limiter, untuned sides or unchecked errors/completed work make a claimed difference inconclusive.",
        "reducedExpected": "Review supplied scripts and artifacts when authorized runs or profiles are unavailable. Record sample count, revisions, workload and unverified confounds; retain inconclusive verdict for missing required evidence. Label a requested one-run ballpark and verify questions 4 and 7.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# measurement-method\n\n## Supplied input\n\nReport whether revision B improves export performance over revision A for a 60k-row workload. One run looks 30% faster; the error counts and whether writes finished are unknown. Explain the measurement method before claiming improvement.\n\nThe full acceptance contract is in task-contracts.json.\n\n## Actual response and output\n\nInconclusive. The reported one-run 30% difference is supplied scenario text, not a verified measurement. There is no justified adoption choice.\n\n| Field | Observed evidence |\n| --- | --- |\n| Workload | Requested export, 60,000 rows |\n| Revisions | A and B labels only, no SHAs or runnable versions |\n| Concurrency | Unknown |\n| Timed region | Unknown |\n| Configuration and production tuning | Unknown for both sides |\n| Sample count | One run claimed in prompt; zero runs available for inspection |\n| Latency units, median, range | Not supplied |\n| Errors and completed writes | Explicitly unknown |\n\nAll seven canonical questions remain gated.\n\n1. Limiter. No separate profiling run, hot symbol, load-generator utilization or I/O trace was supplied. Profiling must be separate from the benchmark samples.\n2. Tuning. Match release/runtime versions, batching, transactions, pool sizes, indexes, warmup and production cache state. Neither side is verified tuned.\n3. Physical limits. With N=60,000, duration t seconds and output b bytes, required rates are 60,000/t rows per second and b/t bytes per second. Both t and b are missing, as are disk, network and core limits. For a changed fraction f, maximum speedup is 1/(1-f); f is missing. No numeric physical-bound conclusion is possible.\n4. Errors and correctness. Count all failures, timeouts and retries and compare row contents, count and a canonical output digest. No evidence exists here.\n5. Reproducibility. Run A,B alternately at least five times per side after defined warmup. Report seconds, each sample, median and min/max. A gap below run variation is no measurable difference. No such runs were possible without code/data.\n6. Relevance. Time the user-visible end-to-end export at realistic concurrency, including completion and output consumption. The relationship of the claimed sample to that path is unknown.\n7. Work. Await all writes, completion acknowledgements and flush/close inside the timer, consume the result, and verify persisted 60,000 rows afterward. No write completion evidence exists.\n\nThe normal comparison branch was attempted as artifact discovery. measurement-method/input-search.json contains the actual rg file inventory; no export A/B harness or 60k-row data was found. runtime.mjs is an unrelated 10k-record arithmetic workload and was not substituted. measurement-method/execution-capability.json proves Bun execution, not export performance. Local execution and artifact storage are authorized; missing target code blocks execution/profiling. No profiler was installed or run, and no unrelated load/process scan was necessary before a nonexistent target run.\n\nThe one-run ballpark variant is evaluated as an explicit requested alternative, not a waiver for choosing B. Even that exception must verify questions 4 and 7. Both are unknown here, so no validated ballpark can be given. No runtime measurements, median or screenshot was fabricated.\n\n## Tools, provenance and boundaries\n\nInput revision a9f70bca56986953e406870e5d50dde4d35be38a was verified with git show. Source package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its manifest says 0.1.0. Supplied source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct from the input revision. Neither the task object store nor the installed package exposes that freeze as a verifiable Git object. This is a provenance limit, not a verified freeze match. See evaluation-evidence/input-revision.json, package-freeze.json, package-git-root.json and input-integrity.json. No new commits, installs, external services or account changes occurred.\n\nActual file reads and commands used functions.exec with tools.exec_command. Bun ran scripts. collaboration.spawn_agent created /root/history, /root/comments and /root/cleanup in disjoint owned directories. Requested models and efforts were inherited with no overrides. Actual model identities are unknown unless a runtime receipt says otherwise. Current exposed tool documentation lists possible overrides, but there is no enumeration operation or worker-result actual-model field. Role prompt files do not register custom agents. No personal memory or unrelated personal context was used.\n",
        "artifact": {
          "path": "fixtures/batch-09/measurement-method.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-09/measurement-method.result.md",
          "sha256": "9b729272fd09705da067f98327a219c383b62857f78ced355a91c7dc49fb8615",
          "bytes": 4588
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-09.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-09.events.jsonl",
            "sha256": "2a14e0cc8592f93c3ba153d43f670a3226b2f2e82570a3f3733b14f94805f7d0",
            "bytes": 317634,
            "eventReferences": [
              {
                "eventId": "item_4",
                "line": 7,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "df1e97025047621b115bb2e48ee9833dc611da33a13f5b96316acf11b5708395"
              },
              {
                "eventId": "item_4",
                "line": 8,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7f75a63397f070d36b8562833748f4730cb066ff971aa4c0f455d2827e1eb8cf",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "fc954696c9277046e3441234441a19c065c56de90d78fed78f9749731573e298"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "ac359059b0e4062a5e9ee3a9be614bbc1592a5473595ef172341f3bf9dc39349",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_6",
                "line": 11,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "4843722aed66097be7fa38492a4ce9e016287808e73ca7d784d92e1f86725e38"
              },
              {
                "eventId": "item_6",
                "line": 12,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a5afb34ee9880b3e6a161ef832bbf23f67f86024e66c4a03bedfbadfdda41d70",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "72b4e713825a5e5aa8fe7356b6583fc82ae577d185a36fffd3f45aed0aad6d5c"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "59a373bae1d25b7fbdc797c703277c7e1070454fec831231229102a3cd5d7ce9",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_9",
                "line": 16,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2484e1c41fe14f3e1f2b4d3c686d723d38920f649116347d7c91f72ab61b4945"
              },
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "07d58749da301c9249f32c46c9116d4bf38bd4593532b33994ed57058b98139d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "0add8e10f009088c3d6c450ae74bf554dc99ac0a75b5564217dc25b8df25eba2"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "77cd0b1080f650e994974e46128612b6db77b9812c58869d8b6d886287f93e94",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_11",
                "line": 20,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "81597635a977090b7b84bb00b7748bffb4c70e96cd325efc16c7c201aea3f381"
              },
              {
                "eventId": "item_11",
                "line": 21,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "2794d602268d8202c666c167499ea755f855bdb63bd720f7eeb35fc424d4058c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e4eccfae29aac10f6ad5d970e34c49d706facfc21557924ab5d4a0e74e19f273"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "cd1d6b96281ac86b0d9e3ab46be6e6afbebff9ccd0f552d401e0d0fc9e81f6f1",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_14",
                "line": 25,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "6b5fa50abdfa7720463a6dd05cf143a43b050bf99891e368bb3041db16d51948"
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "cb356be6c512582918e5616a3ce45c1e40ff86e79a0a4eac6260ff973d065ae6",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_16",
                "line": 29,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e60224ce619be94f5be8c0868a601afc50bf2e7061c604f0df8b7bce0859322b"
              },
              {
                "eventId": "item_16",
                "line": 30,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c892c03d048073b65ddce32de682ff3e6f595b786a0698225843443d39528b94",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 32,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "b7b601042107e690a9fa89831d8cc6c98c6fd7d34f9578821c9ef146ec11a1f3"
              },
              {
                "eventId": "item_18",
                "line": 33,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "93935d4f8b20d381affdf7afb9d76bb71599dd926a790e8b3d8b9bb964dd7789",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_20",
                "line": 36,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "7bbd51144ca5ab38d3b431bf2763ca37c5d4232942b3df83d541a8d2ad977435"
              },
              {
                "eventId": "item_20",
                "line": 37,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "28070fecfac491d9697829d5ed62c8edcad3f4f1a28f6f8df30059db2f9a8d00",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_27",
                "line": 49,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "fb5f8252258336c539ccea3acfe5cceca8ae6f110f55c171f284f8754ba58fa6"
              },
              {
                "eventId": "item_27",
                "line": 50,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "62f54a4876d869188b083490480a12eeddd5581ac0570d9c5fa2893bbbc0e396",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_4",
            "item_5",
            "item_6",
            "item_7",
            "item_9",
            "item_10",
            "item_11",
            "item_12",
            "item_14",
            "item_16",
            "item_18",
            "item_20",
            "item_27"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-09/measurement-method/execution-capability.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-09/measurement-method/execution-capability.json",
      "sha256": "d360a624edc766e96a303dc3bf93b9cc6538bc7f3ce4570a6017928340f5a675",
      "bytes": 193,
      "owners": [
        "grades-native-09.json#4"
      ],
      "text": "{\n  \"args\": [\n    \"bun\",\n    \"--version\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-09\",\n  \"exitCode\": 0,\n  \"stdout\": \"1.4.2\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-09/measurement-method/input-contract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-09/measurement-method/input-contract.json",
      "sha256": "5e5a3d6b29143ee068db390440fe5c8e19780a62970d2aaf89164d5a5d217437",
      "bytes": 2263,
      "owners": [
        "grades-native-09.json#4"
      ],
      "text": "{\n  \"id\": \"measurement-method\",\n  \"sourcePaths\": [\n    \"skills/benchmark-checklist/SKILL.md\"\n  ],\n  \"prompt\": \"Report whether revision B improves export performance over revision A for a 60k-row workload. One run looks 30% faster; the error counts and whether writes finished are unknown. Explain the measurement method before claiming improvement.\",\n  \"requirements\": [\n    \"Record workload, dataset size, concurrency, timed region, sample count and exact compared revisions/configurations.\",\n    \"Apply all seven canonical questions: evidenced limiter from a separate profiling run, production tuning, physical limits arithmetic, errors and correct output, at least 5 alternating runs per side with median/range, end-to-end relevance, and work inside the timed region.\",\n    \"Preserve the explicit user-requested one-run ballpark exception with questions 4 and 7 and no adoption choice.\",\n    \"Inspect exposed tools and permissions before execution or profiling; unavailable checks remain explicit.\"\n  ],\n  \"expectedFull\": \"Record revisions and workload, run at least 5 alternating samples per side, check confounds and all seven gates, and report verdict, units, count, range and limiter. Treat differences below variation as no measurable difference. Missing limiter, untuned sides or unchecked errors/completed work make a claimed difference inconclusive.\",\n  \"expectedReduced\": \"Review supplied scripts and artifacts when authorized runs or profiles are unavailable. Record sample count, revisions, workload and unverified confounds; retain inconclusive verdict for missing required evidence. Label a requested one-run ballpark and verify questions 4 and 7.\",\n  \"expectedBlocked\": \"If neither measurement artifacts nor authorized inspection/execution are available, identify the missing evidence and required method without claiming measured improvement.\",\n  \"forbiddenClaims\": [\n    \"A single unverified run proves a measured improvement.\",\n    \"A profiling run is an unperturbed benchmark sample.\",\n    \"Untuned configurations establish an adoption winner.\",\n    \"Structural validation establishes host behavior.\",\n    \"Unavailable tools or denied execution were successfully used.\"\n  ],\n  \"caseFile\": \"docs/parity/cases/skills/benchmark-checklist.json\"\n}"
    },
    {
      "path": "fixtures/batch-09/measurement-method/input-search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-09/measurement-method/input-search.json",
      "sha256": "b63075652d626a24fc5d040eaaebf44571571271470a80ab952582eb182de79a",
      "bytes": 7335,
      "owners": [
        "grades-native-09.json#4"
      ],
      "text": "{\n  \"args\": [\n    \"rg\",\n    \"--files\",\n    \"committed-inputs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-09\",\n  \"exitCode\": 0,\n  \"stdout\": \"committed-inputs/additional/invoice/formatter.mjs\\ncommitted-inputs/additional/invoice/decision.md\\ncommitted-inputs/additional/invoice/controller.mjs\\ncommitted-inputs/additional/invoice/facade.mjs\\ncommitted-inputs/additional/invoice/adapter.mjs\\ncommitted-inputs/additional/invoice/exporter.mjs\\ncommitted-inputs/additional/invoice/calculator.mjs\\ncommitted-inputs/additional/legal-header/source.diff\\ncommitted-inputs/additional/legal-header/source.mjs\\ncommitted-inputs/additional/migration/notification.mjs\\ncommitted-inputs/additional/migration/contract.mjs\\ncommitted-inputs/additional/migration/api.mjs\\ncommitted-inputs/additional/migration/scope.md\\ncommitted-inputs/additional/migration/profile.mjs\\ncommitted-inputs/additional/history/jay-mode.md\\ncommitted-inputs/additional/history/capsule.json\\ncommitted-inputs/additional/history/shared-records.json\\ncommitted-inputs/additional/history/history.json\\ncommitted-inputs/additional/README.md\\ncommitted-inputs/additional/dead-path/instructions.md\\ncommitted-inputs/additional/dead-path/duplicate-reference.md\\ncommitted-inputs/additional/dead-path/handler.mjs\\ncommitted-inputs/additional/dead-path/caller.mjs\\ncommitted-inputs/additional/dead-path/scope.md\\ncommitted-inputs/additional/scenario-map.json\\ncommitted-inputs/additional/corpus/records.jsonl\\ncommitted-inputs/additional/cache/vendor/disposer-v1.mjs\\ncommitted-inputs/additional/cache/cache.mjs\\ncommitted-inputs/additional/cache/manifest.json\\ncommitted-inputs/additional/cache/caller.mjs\\ncommitted-inputs/additional/cache/README.md\\ncommitted-inputs/additional/cache/invalidation.diff\\ncommitted-inputs/additional/cache/probe.mjs\\ncommitted-inputs/additional/types/boundary.ts\\ncommitted-inputs/additional/types/README.md\\ncommitted-inputs/additional/types/context.ts\\ncommitted-inputs/runtime.mjs\\ncommitted-inputs/additional-v3/repeatable-change/manifests/mobile/offline.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/mobile/alerts.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/admin/team.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/admin/audit.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/core/already-v2.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/core/search.json\\ncommitted-inputs/additional-v3/repeatable-change/manifests/core/export.json\\ncommitted-inputs/additional-v3/repeatable-change/scope.md\\ncommitted-inputs/additional-v3/repeatable-change/notes.txt\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/consumer.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/legacy.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/index.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/migration-end-state/contract.test.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/boundary.test.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/domain.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-guards.test.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/internal-caller.js\\ncommitted-inputs/additional-v3/not-written/fixtures/shared/additional-v3/invalid-input/adapter.js\\ncommitted-inputs/additional-v3/installed-compiler-paths.json\\ncommitted-inputs/additional-v3/README.md\\ncommitted-inputs/additional-v3/preparation-checks.json\\ncommitted-inputs/additional-v3/migration-end-state/legacy.ts\\ncommitted-inputs/additional-v3/migration-end-state/index.ts\\ncommitted-inputs/additional-v3/migration-end-state/tsconfig.json\\ncommitted-inputs/additional-v3/migration-end-state/contract.test.mjs\\ncommitted-inputs/additional-v3/migration-end-state/consumer.ts\\ncommitted-inputs/additional-v3/migration-end-state/target.md\\ncommitted-inputs/additional-v3/scenario-map.json\\ncommitted-inputs/dashboard.mjs\\ncommitted-inputs/orders.json\\ncommitted-inputs/forge.json\\ncommitted-inputs/history.json\\ncommitted-inputs/README.md\\ncommitted-inputs/invoice.mjs\\ncommitted-inputs/additional-v3/invalid-input/domain.ts\\ncommitted-inputs/additional-v3/invalid-input/tsconfig.json\\ncommitted-inputs/additional-v3/invalid-input/internal-guards.test.mjs\\ncommitted-inputs/additional-v3/invalid-input/boundary.test.mjs\\ncommitted-inputs/additional-v3/invalid-input/internal-caller.ts\\ncommitted-inputs/additional-v3/invalid-input/adapter.ts\\ncommitted-inputs/additional-v3/invalid-input/scope.md\\ncommitted-inputs/additional-v2/caller-migration/package.json\\ncommitted-inputs/additional-v2/caller-migration/contract.test.mjs\\ncommitted-inputs/additional-v2/caller-migration/notification.mjs\\ncommitted-inputs/additional-v2/caller-migration/api.mjs\\ncommitted-inputs/additional-v2/caller-migration/scope.md\\ncommitted-inputs/additional-v2/caller-migration/profile.mjs\\ncommitted-inputs/additional-v2/empty-function/contracts.test-d.ts\\ncommitted-inputs/additional-v2/empty-function/fixture-data.mjs\\ncommitted-inputs/additional-v2/empty-function/types.ts\\ncommitted-inputs/additional-v2/empty-function/weak.test.mjs\\ncommitted-inputs/additional-v2/empty-function/subject.mjs\\ncommitted-inputs/additional-v2/empty-function/table-relations.test.mjs\\ncommitted-inputs/additional-v2/empty-function/acceptance.json\\ncommitted-inputs/additional-v2/scenario-map.json\\ncommitted-inputs/additional-v2/preparation-checks.json\\ncommitted-inputs/additional-v2/README.md\\ncommitted-inputs/additional-v2/dead-path/instructions.md\\ncommitted-inputs/additional-v2/dead-path/duplicate-reference.md\\ncommitted-inputs/additional-v2/dead-path/handler.mjs\\ncommitted-inputs/additional-v2/dead-path/caller.mjs\\ncommitted-inputs/additional-v2/dead-path/contract.test.mjs\\ncommitted-inputs/additional-v2/dead-path/scope.md\\ncommitted-inputs/additional-v2/dead-path/acceptance.json\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/table-relations.test.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/fixture-data.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/weak.test.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/empty-function/subject.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/handler.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/caller.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/dead-path/contract.test.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/api.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/contract.test.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/notification.js\\ncommitted-inputs/additional-v2/not-written/fixtures/shared/additional-v2/caller-migration/profile.js\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-09/measurement-method.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-09/measurement-method.result.md",
      "sha256": "9b729272fd09705da067f98327a219c383b62857f78ced355a91c7dc49fb8615",
      "bytes": 4588,
      "owners": [
        "grades-native-09.json#4"
      ],
      "text": "# measurement-method\n\n## Supplied input\n\nReport whether revision B improves export performance over revision A for a 60k-row workload. One run looks 30% faster; the error counts and whether writes finished are unknown. Explain the measurement method before claiming improvement.\n\nThe full acceptance contract is in task-contracts.json.\n\n## Actual response and output\n\nInconclusive. The reported one-run 30% difference is supplied scenario text, not a verified measurement. There is no justified adoption choice.\n\n| Field | Observed evidence |\n| --- | --- |\n| Workload | Requested export, 60,000 rows |\n| Revisions | A and B labels only, no SHAs or runnable versions |\n| Concurrency | Unknown |\n| Timed region | Unknown |\n| Configuration and production tuning | Unknown for both sides |\n| Sample count | One run claimed in prompt; zero runs available for inspection |\n| Latency units, median, range | Not supplied |\n| Errors and completed writes | Explicitly unknown |\n\nAll seven canonical questions remain gated.\n\n1. Limiter. No separate profiling run, hot symbol, load-generator utilization or I/O trace was supplied. Profiling must be separate from the benchmark samples.\n2. Tuning. Match release/runtime versions, batching, transactions, pool sizes, indexes, warmup and production cache state. Neither side is verified tuned.\n3. Physical limits. With N=60,000, duration t seconds and output b bytes, required rates are 60,000/t rows per second and b/t bytes per second. Both t and b are missing, as are disk, network and core limits. For a changed fraction f, maximum speedup is 1/(1-f); f is missing. No numeric physical-bound conclusion is possible.\n4. Errors and correctness. Count all failures, timeouts and retries and compare row contents, count and a canonical output digest. No evidence exists here.\n5. Reproducibility. Run A,B alternately at least five times per side after defined warmup. Report seconds, each sample, median and min/max. A gap below run variation is no measurable difference. No such runs were possible without code/data.\n6. Relevance. Time the user-visible end-to-end export at realistic concurrency, including completion and output consumption. The relationship of the claimed sample to that path is unknown.\n7. Work. Await all writes, completion acknowledgements and flush/close inside the timer, consume the result, and verify persisted 60,000 rows afterward. No write completion evidence exists.\n\nThe normal comparison branch was attempted as artifact discovery. measurement-method/input-search.json contains the actual rg file inventory; no export A/B harness or 60k-row data was found. runtime.mjs is an unrelated 10k-record arithmetic workload and was not substituted. measurement-method/execution-capability.json proves Bun execution, not export performance. Local execution and artifact storage are authorized; missing target code blocks execution/profiling. No profiler was installed or run, and no unrelated load/process scan was necessary before a nonexistent target run.\n\nThe one-run ballpark variant is evaluated as an explicit requested alternative, not a waiver for choosing B. Even that exception must verify questions 4 and 7. Both are unknown here, so no validated ballpark can be given. No runtime measurements, median or screenshot was fabricated.\n\n## Tools, provenance and boundaries\n\nInput revision a9f70bca56986953e406870e5d50dde4d35be38a was verified with git show. Source package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its manifest says 0.1.0. Supplied source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct from the input revision. Neither the task object store nor the installed package exposes that freeze as a verifiable Git object. This is a provenance limit, not a verified freeze match. See evaluation-evidence/input-revision.json, package-freeze.json, package-git-root.json and input-integrity.json. No new commits, installs, external services or account changes occurred.\n\nActual file reads and commands used functions.exec with tools.exec_command. Bun ran scripts. collaboration.spawn_agent created /root/history, /root/comments and /root/cleanup in disjoint owned directories. Requested models and efforts were inherited with no overrides. Actual model identities are unknown unless a runtime receipt says otherwise. Current exposed tool documentation lists possible overrides, but there is no enumeration operation or worker-result actual-model field. Role prompt files do not register custom agents. No personal memory or unrelated personal context was used.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-09/measurement-method/sources",
      "owner": "grades-native-09.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-09/measurement-method/sources",
      "owner": "grades-native-09.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
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
