# codex: smaller-solution

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "smaller-solution",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-05.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Apply principle-laziness-protocol to this authorized refactor. A pricing entry point calls PriceFacade, which only forwards to PriceAdapter, which only forwards to PriceService. Only PriceService implements the required rounding and tax behavior. Remove an unnecessary abstraction while preserving that behavior. Inspect callers before editing and report checks actually run.",
  "caseDefinition": {
    "id": "smaller-solution",
    "sourcePaths": [
      "skills/principle-laziness-protocol/SKILL.md"
    ],
    "prompt": "Apply principle-laziness-protocol to this authorized refactor. A pricing entry point calls PriceFacade, which only forwards to PriceAdapter, which only forwards to PriceService. Only PriceService implements the required rounding and tax behavior. Remove an unnecessary abstraction while preserving that behavior. Inspect callers before editing and report checks actually run.",
    "requirements": [
      "Read the implementation and callers before choosing deletion.",
      "Preserve rounding, tax behavior and required public contracts.",
      "Prefer deletion, keep the call hierarchy flat, consolidate repeated decisions and minimize the diff.",
      "Question signal threading and remove tiny pass-throughs, representation leaks and duplicated choices.",
      "File read, authorized write and execution capabilities are needed to implement and verify the change."
    ],
    "expectedFull": "Remove redundant forwarding layers where caller contracts permit, preserve required behavior, and report the smallest diff with observed verification. Apply the more-than-3-files-or-layers flattening test without treating a rich interface as a deep call chain.",
    "expectedReduced": "If writes or execution are unavailable, give a specific read-only deletion proposal based on available source. Label reduced capability and state which edits and checks were not performed.",
    "expectedBlocked": "If relevant source cannot be read or supplied, state that the abstraction and behavior cannot be assessed; request the missing implementation and callers without claiming a refactor.",
    "forbiddenClaims": [
      "Behavior preserved without relevant evidence.",
      "Edits or checks completed when unavailable or denied.",
      "New abstraction or signal threading justified only by elegance.",
      "Structural validation proves host behavioral parity."
    ],
    "caseFile": "docs/parity/cases/skills/principle-laziness-protocol.json"
  },
  "registry": {
    "caseId": "smaller-solution",
    "caseFile": "docs/parity/cases/skills/principle-laziness-protocol.json",
    "sourcePaths": [
      "skills/principle-laziness-protocol/SKILL.md"
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
      "attemptId": "grades-native-05.json#0",
      "order": 0,
      "gradeFile": "grades-native-05.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "smaller-solution",
      "status": "blocked",
      "grade": {
        "caseId": "smaller-solution",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "rawTrace": "codex/batch-05.events.jsonl",
        "actualReadEventIds": [
          "item_5",
          "item_18",
          "item_21"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Concrete pricing implementation/callers/tax-rounding contract absent."
        ],
        "review": "No PriceFacade/Adapter/Service or rounding/tax/caller source supplied. Refuses unsupported deletion despite working host capabilities. Conditional advice does not complete concrete refactor.",
        "responseArtifact": "fixtures/batch-05/smaller-solution.result.md",
        "variantReview": [
          "Actual attempted variants and explicitly simulated conditions inspected in response artifact. No synthetic service/worker receipt credited."
        ],
        "concreteFixCandidates": [
          "Supply missing concrete inputs and rerun. Fixture incompleteness is not a skill source defect."
        ],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-05.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Remove redundant forwarding layers where caller contracts permit, preserve required behavior, and report the smallest diff with observed verification. Apply the more-than-3-files-or-layers flattening test without treating a rich interface as a deep call chain.",
        "reducedExpected": "If writes or execution are unavailable, give a specific read-only deletion proposal based on available source. Label reduced capability and state which edits and checks were not performed."
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Baseline case definitions used, with corrected full observation contracts for uncertain-result/shared-path-conflict.",
          "Native raw command events and saved outputs reviewed; model check-script assertions are not workflow grades.",
          "Worker tools exposed does not establish success. Missing assignment prerequisites is not absent tool or startup failure.",
          "Proxy local payment/recovery behavior never establishes service execution.",
          "OS process concurrency is appropriate for two-writers case and is not AI-worker independence."
        ]
      },
      "response": {
        "text": "# smaller-solution\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"smaller-solution\",\n  \"prompt\": \"Apply principle-laziness-protocol to this authorized refactor. A pricing entry point calls PriceFacade, which only forwards to PriceAdapter, which only forwards to PriceService. Only PriceService implements the required rounding and tax behavior. Remove an unnecessary abstraction while preserving that behavior. Inspect callers before editing and report checks actually run.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Read the implementation and callers before choosing deletion.\",\n    \"Preserve rounding, tax behavior and required public contracts.\",\n    \"Prefer deletion, keep the call hierarchy flat, consolidate repeated decisions and minimize the diff.\",\n    \"Question signal threading and remove tiny pass-throughs, representation leaks and duplicated choices.\",\n    \"File read, authorized write and execution capabilities are needed to implement and verify the change.\"\n  ]\n}\n```\n\n## Actual response and output\n\nThe pricing refactor cannot be assessed from the available implementation inputs. The fixture inventory and symbol search found no PriceFacade, PriceAdapter, PriceService, pricing entry point, tax rules, rounding rules, caller contracts or pricing checks. The supplied prose describes a candidate deletion but does not establish source compatibility. I made no pricing edit and ran no pricing behavior check.\n\nLaziness Protocol favors removing forwarding layers and connecting the entry point to the service after inspecting all callers. Preserve a required public facade if it has external consumers, and delete only private forwarding code. Keep tax and rounding decisions in PriceService. Do not introduce a threaded signal or another abstraction. This is conditional advice, not a source-grounded deletion selection.\n\nThe concrete prerequisites are the implementation, complete callers, public API obligations and executable tax and rounding expectations. File reads, isolated writes and Bun execution work on this host. Missing source blocks this case rather than unavailable tools.\n\n## Variants attempted and limits\n\nPrimary implementation attempt stopped at missing pricing source and contracts. A conditional deletion recommendation is provided. No write-denial or execution-denial variant was simulated.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\"PriceFacade\\|PriceAdapter\\|PriceService\\|state\\\\.json\\|lastX\\|restart\\|persistent\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"] | 1 | [smaller-solution/fixture-search.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution/fixture-search.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n",
        "artifact": {
          "path": "fixtures/batch-05/smaller-solution.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution.result.md",
          "sha256": "cb764416c411ec1a9d3d713010a346dd9436f0d0202c1a8eb11299b96ceab546",
          "bytes": 5137
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-05.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-05.events.jsonl",
            "sha256": "925a4d9ac08a8ba6c24c8c2a85e8f196bf1e248b86a901ef3f1c96be0f70ccd6",
            "bytes": 387623,
            "eventReferences": [
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "0e1c174a01a24d51c3dab280caceff344af0fefc6a644c6b97d10af9eeb71a02"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8a2b73027e46ae006ea751859775e7b3f6b53099dbe51f5b2d2e50874664d426",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 34,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "efa76720dfe3a51901c606b1ad43073218ec7b8edbbcce7870ba1d1e0affda10"
              },
              {
                "eventId": "item_18",
                "line": 35,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "daf33dfe6a92e6e8d9a399e9e75461540f72f6a3e3cc13a4a36b7a56511f7816",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_21",
                "line": 39,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "cc3a8ef608252c066015d484f344c7e3c26008e1620e93f30de58829200c6d33"
              },
              {
                "eventId": "item_21",
                "line": 40,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "63cafe17b0f3962f3e54076d20d8e25814fc8be615c5a2334df434533a21d2e5",
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
            "item_5",
            "item_18",
            "item_21"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-05.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-05/smaller-solution/fixture-search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution/fixture-search.json",
      "sha256": "fa22a076907c59541c28c319d0363531e04b2f2d8c389c0cd959deecc986e557",
      "bytes": 363,
      "owners": [
        "grades-native-05.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \"PriceFacade|PriceAdapter|PriceService|state\\\\.json|lastX|restart|persistent\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/smaller-solution/input-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution/input-manifest.json",
      "sha256": "503eb4de456b319e92b35f3b8121eeb7db7bbc7e13c74dd59e4979fb13afd68b",
      "bytes": 246,
      "owners": [
        "grades-native-05.json#0"
      ],
      "text": "{\n  \"inputSha256\": \"d4fc8e89b14df6f97f8e303e377e7660ee6b4af666d73f390737b54e2e4bc7c3\",\n  \"taskGitSha\": null,\n  \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageFreezeIndependentlyVerified\": false,\n  \"fixtures\": []\n}\n"
    },
    {
      "path": "fixtures/batch-05/smaller-solution/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution/registered-case.json",
      "sha256": "b8ab42b7dedfe1a40a8cf44dcfcba07d11bf25d5a29675732fd730e6e99213b3",
      "bytes": 1959,
      "owners": [
        "grades-native-05.json#0"
      ],
      "text": "{\n  \"id\": \"smaller-solution\",\n  \"sourcePaths\": [\n    \"skills/principle-laziness-protocol/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-laziness-protocol to this authorized refactor. A pricing entry point calls PriceFacade, which only forwards to PriceAdapter, which only forwards to PriceService. Only PriceService implements the required rounding and tax behavior. Remove an unnecessary abstraction while preserving that behavior. Inspect callers before editing and report checks actually run.\",\n  \"requirements\": [\n    \"Read the implementation and callers before choosing deletion.\",\n    \"Preserve rounding, tax behavior and required public contracts.\",\n    \"Prefer deletion, keep the call hierarchy flat, consolidate repeated decisions and minimize the diff.\",\n    \"Question signal threading and remove tiny pass-throughs, representation leaks and duplicated choices.\",\n    \"File read, authorized write and execution capabilities are needed to implement and verify the change.\"\n  ],\n  \"expectedFull\": \"Remove redundant forwarding layers where caller contracts permit, preserve required behavior, and report the smallest diff with observed verification. Apply the more-than-3-files-or-layers flattening test without treating a rich interface as a deep call chain.\",\n  \"expectedReduced\": \"If writes or execution are unavailable, give a specific read-only deletion proposal based on available source. Label reduced capability and state which edits and checks were not performed.\",\n  \"expectedBlocked\": \"If relevant source cannot be read or supplied, state that the abstraction and behavior cannot be assessed; request the missing implementation and callers without claiming a refactor.\",\n  \"forbiddenClaims\": [\n    \"Behavior preserved without relevant evidence.\",\n    \"Edits or checks completed when unavailable or denied.\",\n    \"New abstraction or signal threading justified only by elegance.\",\n    \"Structural validation proves host behavioral parity.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/smaller-solution.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution.result.md",
      "sha256": "cb764416c411ec1a9d3d713010a346dd9436f0d0202c1a8eb11299b96ceab546",
      "bytes": 5137,
      "owners": [
        "grades-native-05.json#0"
      ],
      "text": "# smaller-solution\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"smaller-solution\",\n  \"prompt\": \"Apply principle-laziness-protocol to this authorized refactor. A pricing entry point calls PriceFacade, which only forwards to PriceAdapter, which only forwards to PriceService. Only PriceService implements the required rounding and tax behavior. Remove an unnecessary abstraction while preserving that behavior. Inspect callers before editing and report checks actually run.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Read the implementation and callers before choosing deletion.\",\n    \"Preserve rounding, tax behavior and required public contracts.\",\n    \"Prefer deletion, keep the call hierarchy flat, consolidate repeated decisions and minimize the diff.\",\n    \"Question signal threading and remove tiny pass-throughs, representation leaks and duplicated choices.\",\n    \"File read, authorized write and execution capabilities are needed to implement and verify the change.\"\n  ]\n}\n```\n\n## Actual response and output\n\nThe pricing refactor cannot be assessed from the available implementation inputs. The fixture inventory and symbol search found no PriceFacade, PriceAdapter, PriceService, pricing entry point, tax rules, rounding rules, caller contracts or pricing checks. The supplied prose describes a candidate deletion but does not establish source compatibility. I made no pricing edit and ran no pricing behavior check.\n\nLaziness Protocol favors removing forwarding layers and connecting the entry point to the service after inspecting all callers. Preserve a required public facade if it has external consumers, and delete only private forwarding code. Keep tax and rounding decisions in PriceService. Do not introduce a threaded signal or another abstraction. This is conditional advice, not a source-grounded deletion selection.\n\nThe concrete prerequisites are the implementation, complete callers, public API obligations and executable tax and rounding expectations. File reads, isolated writes and Bun execution work on this host. Missing source blocks this case rather than unavailable tools.\n\n## Variants attempted and limits\n\nPrimary implementation attempt stopped at missing pricing source and contracts. A conditional deletion recommendation is provided. No write-denial or execution-denial variant was simulated.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\"PriceFacade\\|PriceAdapter\\|PriceService\\|state\\\\.json\\|lastX\\|restart\\|persistent\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"] | 1 | [smaller-solution/fixture-search.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/smaller-solution/fixture-search.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-05/smaller-solution/input.json",
      "owner": "grades-native-05.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/smaller-solution/source-manifest.json",
      "owner": "grades-native-05.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/smaller-solution/source-read",
      "owner": "grades-native-05.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/smaller-solution/input.json",
      "owner": "grades-native-05.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/smaller-solution/source-manifest.json",
      "owner": "grades-native-05.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/smaller-solution/source-read",
      "owner": "grades-native-05.json#0",
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
