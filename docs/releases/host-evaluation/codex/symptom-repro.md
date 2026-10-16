# codex: symptom-repro

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "symptom-repro",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-05.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "A service crashes on a missing value after restart. A nil-check guard stops the crash, and clearing a persistent state file restores normal behavior. Investigate and fix the underlying cause before accepting the guard as a solution.",
  "caseDefinition": {
    "id": "symptom-repro",
    "sourcePaths": [
      "skills/principle-fix-root-causes/SKILL.md"
    ],
    "prompt": "A service crashes on a missing value after restart. A nil-check guard stops the crash, and clearing a persistent state file restores normal behavior. Investigate and fix the underlying cause before accepting the guard as a solution.",
    "requirements": [
      "Reproduce the symptom before fixing it and ask why until the underlying cause is identified.",
      "Reject a nil-check guard that merely silences the crash and fix the faulty code instead of explaining a workaround in a long comment.",
      "Search for the same faulty pattern and fix its other instances within authorized scope.",
      "When evidence is insufficient, instrument the system and read the actual error instead of guessing.",
      "For restart failures, inspect persistent config, caches, lock files and serialized state first; prioritize state validation if clearing state restores behavior.",
      "Respect tool availability and permissions, including persistent-state changes."
    ],
    "expectedFull": "Reproduce the failure, trace why the value is missing and investigate stale persistent state before code for the restart symptom. If clearing state restores behavior, prioritize state validation as the fix. Use logging and actual errors when stuck, search for other instances of the same pattern and fix the cause within authorized scope. Reject guards and explanatory comments that hide the bug.",
    "expectedReduced": "With read-only access or partial execution, inspect available errors, code and persistent-state evidence. Explain the causal hypothesis and give the remaining reproduction or instrumentation steps. Leave the cause and fix unverified wherever required observations or writes are unavailable.",
    "expectedBlocked": "If reproduction or required inspection is unavailable or denied, state the missing capability or permission and request the needed evidence. Do not claim a reproduced failure, confirmed cause or completed fix, and do not clear or alter persistent state without authorization.",
    "forbiddenClaims": [
      "A nil-check that hides the crash proves the underlying bug is fixed.",
      "A proposed reproduction or logging step is an observed result.",
      "Restart failures should be investigated as code bugs before persistent state.",
      "Clearing state proves a permanent fix without state validation.",
      "Missing or denied tools authorize bypassing permissions."
    ],
    "caseFile": "docs/parity/cases/skills/principle-fix-root-causes.json"
  },
  "registry": {
    "caseId": "symptom-repro",
    "caseFile": "docs/parity/cases/skills/principle-fix-root-causes.json",
    "sourcePaths": [
      "skills/principle-fix-root-causes/SKILL.md"
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
      "attemptId": "grades-native-05.json#1",
      "order": 0,
      "gradeFile": "grades-native-05.json",
      "rankWithinFile": 1,
      "host": "codex",
      "caseId": "symptom-repro",
      "status": "blocked",
      "grade": {
        "caseId": "symptom-repro",
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
          "Restart/service/state/error inputs absent."
        ],
        "review": "No executable service, restart command, serializer, failing blob or error supplied. Correctly refuses nil-check/clear-state workaround and provides evidence-first investigation steps, no invented cause.",
        "responseArtifact": "fixtures/batch-05/symptom-repro.result.md",
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
        "fullExpected": "Reproduce the failure, trace why the value is missing and investigate stale persistent state before code for the restart symptom. If clearing state restores behavior, prioritize state validation as the fix. Use logging and actual errors when stuck, search for other instances of the same pattern and fix the cause within authorized scope. Reject guards and explanatory comments that hide the bug.",
        "reducedExpected": "With read-only access or partial execution, inspect available errors, code and persistent-state evidence. Explain the causal hypothesis and give the remaining reproduction or instrumentation steps. Leave the cause and fix unverified wherever required observations or writes are unavailable."
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
        "text": "# symptom-repro\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"symptom-repro\",\n  \"prompt\": \"A service crashes on a missing value after restart. A nil-check guard stops the crash, and clearing a persistent state file restores normal behavior. Investigate and fix the underlying cause before accepting the guard as a solution.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Reproduce the symptom before fixing it and ask why until the underlying cause is identified.\",\n    \"Reject a nil-check guard that merely silences the crash and fix the faulty code instead of explaining a workaround in a long comment.\",\n    \"Search for the same faulty pattern and fix its other instances within authorized scope.\",\n    \"When evidence is insufficient, instrument the system and read the actual error instead of guessing.\",\n    \"For restart failures, inspect persistent config, caches, lock files and serialized state first; prioritize state validation if clearing state restores behavior.\",\n    \"Respect tool availability and permissions, including persistent-state changes.\"\n  ]\n}\n```\n\n## Actual response and output\n\nThe restart failure was not reproduced. No service implementation, launch command, persistent state file, config, cache, lock file, state serializer or actual error log was supplied. The prepared synthetic fixture inventory and search provide no such runtime. No persistent service state was cleared or edited, no nil-check was accepted, and no root cause or fix is confirmed.\n\nFix Root Causes changes the investigation order. Inspect a copied failing persisted blob and its version before changing business logic. Run the same service against that copy, capture its actual exception and failing field, then compare fresh and restarted state. Trace the writer and reader until the missing value is explained. Stale schema, incomplete writes and failed hydration remain hypotheses. Clearing state reportedly restoring behavior is scenario input, not an observation in this run.\n\nThe next executable investigation needs the restart command, serializer and loader, failing blob and expected schema. Instrument load-time schema version and failed field without logging secrets, search the confirmed faulty pattern across authorized sources, and test valid restart, legacy state and invalid state. Validate or migrate at the persistence boundary when the evidence supports it. Quarantine or reset invalid data only under the applicable permission. A guard inside the service that silently skips work would leave that defect unverified.\n\n## Variants attempted and limits\n\nPrimary reproduction attempt stopped at missing executable service and persisted-state evidence. No nil-check or state-clearing variant was executed. The reported restart behavior remains supplied scenario text.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\"PriceFacade\\|PriceAdapter\\|PriceService\\|state\\\\.json\\|lastX\\|restart\\|persistent\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"] | 1 | [symptom-repro/fixture-search.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro/fixture-search.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n",
        "artifact": {
          "path": "fixtures/batch-05/symptom-repro.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro.result.md",
          "sha256": "c8c01b313b5a365ecff4a947afd65a0c42a452934a0f75867e8c8ac8576187e7",
          "bytes": 5573
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
      "path": "fixtures/batch-05/symptom-repro/fixture-search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro/fixture-search.json",
      "sha256": "8e05c71274a8c7cb9d2ccb02410782c17d27b20b1129d916c68b1ddae7f79493",
      "bytes": 360,
      "owners": [
        "grades-native-05.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \"PriceFacade|PriceAdapter|PriceService|state\\\\.json|lastX|restart|persistent\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/symptom-repro/input-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro/input-manifest.json",
      "sha256": "9e9cf608cc7819d8e5fca8b0f0b7b2a4b592e6df275bbf7a43b6613b59f068c1",
      "bytes": 246,
      "owners": [
        "grades-native-05.json#1"
      ],
      "text": "{\n  \"inputSha256\": \"72cf1a32ea91c528769b1ad873053c2712d55367241457ebb56d959f221435b9\",\n  \"taskGitSha\": null,\n  \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageFreezeIndependentlyVerified\": false,\n  \"fixtures\": []\n}\n"
    },
    {
      "path": "fixtures/batch-05/symptom-repro/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro/registered-case.json",
      "sha256": "b2076faec13e7227d7ba44f243dea5c6fbf53bf680069a0a956cdf9c6daab3b2",
      "bytes": 2495,
      "owners": [
        "grades-native-05.json#1"
      ],
      "text": "{\n  \"id\": \"symptom-repro\",\n  \"sourcePaths\": [\n    \"skills/principle-fix-root-causes/SKILL.md\"\n  ],\n  \"prompt\": \"A service crashes on a missing value after restart. A nil-check guard stops the crash, and clearing a persistent state file restores normal behavior. Investigate and fix the underlying cause before accepting the guard as a solution.\",\n  \"requirements\": [\n    \"Reproduce the symptom before fixing it and ask why until the underlying cause is identified.\",\n    \"Reject a nil-check guard that merely silences the crash and fix the faulty code instead of explaining a workaround in a long comment.\",\n    \"Search for the same faulty pattern and fix its other instances within authorized scope.\",\n    \"When evidence is insufficient, instrument the system and read the actual error instead of guessing.\",\n    \"For restart failures, inspect persistent config, caches, lock files and serialized state first; prioritize state validation if clearing state restores behavior.\",\n    \"Respect tool availability and permissions, including persistent-state changes.\"\n  ],\n  \"expectedFull\": \"Reproduce the failure, trace why the value is missing and investigate stale persistent state before code for the restart symptom. If clearing state restores behavior, prioritize state validation as the fix. Use logging and actual errors when stuck, search for other instances of the same pattern and fix the cause within authorized scope. Reject guards and explanatory comments that hide the bug.\",\n  \"expectedReduced\": \"With read-only access or partial execution, inspect available errors, code and persistent-state evidence. Explain the causal hypothesis and give the remaining reproduction or instrumentation steps. Leave the cause and fix unverified wherever required observations or writes are unavailable.\",\n  \"expectedBlocked\": \"If reproduction or required inspection is unavailable or denied, state the missing capability or permission and request the needed evidence. Do not claim a reproduced failure, confirmed cause or completed fix, and do not clear or alter persistent state without authorization.\",\n  \"forbiddenClaims\": [\n    \"A nil-check that hides the crash proves the underlying bug is fixed.\",\n    \"A proposed reproduction or logging step is an observed result.\",\n    \"Restart failures should be investigated as code bugs before persistent state.\",\n    \"Clearing state proves a permanent fix without state validation.\",\n    \"Missing or denied tools authorize bypassing permissions.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/symptom-repro.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro.result.md",
      "sha256": "c8c01b313b5a365ecff4a947afd65a0c42a452934a0f75867e8c8ac8576187e7",
      "bytes": 5573,
      "owners": [
        "grades-native-05.json#1"
      ],
      "text": "# symptom-repro\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"symptom-repro\",\n  \"prompt\": \"A service crashes on a missing value after restart. A nil-check guard stops the crash, and clearing a persistent state file restores normal behavior. Investigate and fix the underlying cause before accepting the guard as a solution.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Reproduce the symptom before fixing it and ask why until the underlying cause is identified.\",\n    \"Reject a nil-check guard that merely silences the crash and fix the faulty code instead of explaining a workaround in a long comment.\",\n    \"Search for the same faulty pattern and fix its other instances within authorized scope.\",\n    \"When evidence is insufficient, instrument the system and read the actual error instead of guessing.\",\n    \"For restart failures, inspect persistent config, caches, lock files and serialized state first; prioritize state validation if clearing state restores behavior.\",\n    \"Respect tool availability and permissions, including persistent-state changes.\"\n  ]\n}\n```\n\n## Actual response and output\n\nThe restart failure was not reproduced. No service implementation, launch command, persistent state file, config, cache, lock file, state serializer or actual error log was supplied. The prepared synthetic fixture inventory and search provide no such runtime. No persistent service state was cleared or edited, no nil-check was accepted, and no root cause or fix is confirmed.\n\nFix Root Causes changes the investigation order. Inspect a copied failing persisted blob and its version before changing business logic. Run the same service against that copy, capture its actual exception and failing field, then compare fresh and restarted state. Trace the writer and reader until the missing value is explained. Stale schema, incomplete writes and failed hydration remain hypotheses. Clearing state reportedly restoring behavior is scenario input, not an observation in this run.\n\nThe next executable investigation needs the restart command, serializer and loader, failing blob and expected schema. Instrument load-time schema version and failed field without logging secrets, search the confirmed faulty pattern across authorized sources, and test valid restart, legacy state and invalid state. Validate or migrate at the persistence boundary when the evidence supports it. Quarantine or reset invalid data only under the applicable permission. A guard inside the service that silently skips work would leave that defect unverified.\n\n## Variants attempted and limits\n\nPrimary reproduction attempt stopped at missing executable service and persisted-state evidence. No nil-check or state-clearing variant was executed. The reported restart behavior remains supplied scenario text.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\"PriceFacade\\|PriceAdapter\\|PriceService\\|state\\\\.json\\|lastX\\|restart\\|persistent\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"] | 1 | [symptom-repro/fixture-search.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/symptom-repro/fixture-search.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-05/symptom-repro/input.json",
      "owner": "grades-native-05.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/symptom-repro/source-manifest.json",
      "owner": "grades-native-05.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/symptom-repro/source-read",
      "owner": "grades-native-05.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/symptom-repro/input.json",
      "owner": "grades-native-05.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/symptom-repro/source-manifest.json",
      "owner": "grades-native-05.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/symptom-repro/source-read",
      "owner": "grades-native-05.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
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
