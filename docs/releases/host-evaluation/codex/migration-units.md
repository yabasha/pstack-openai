# codex: migration-units

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "migration-units",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-03.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Plan a multi-step schema migration and its commit delivery. Give each ordered unit a specific check, show when the next unit can begin, and handle an unavailable test runner or unauthorized Git operation.",
  "caseDefinition": {
    "id": "migration-units",
    "sourcePaths": [
      "skills/principle-sequence-verifiable-units/SKILL.md"
    ],
    "prompt": "Plan a multi-step schema migration and its commit delivery. Give each ordered unit a specific check, show when the next unit can begin, and handle an unavailable test runner or unauthorized Git operation.",
    "requirements": [
      "Each ordered unit ends in a specific check.",
      "Start from a known-good baseline and verify one change before the next.",
      "Order independently landable commits and PRs so a reviewer can replay the argument.",
      "Preserve authorization and observed execution limits."
    ],
    "expectedFull": "Inspect a clean trunk baseline and rebase when authorized. Every ordered migration unit identifies its known-good start, one change and concrete check; advance only on green. Delivery uses a failing test before its fix, or another justified order such as subtraction before reshape, baseline before treatment or scaffold before feature. Every commit lands on its own. Use the prove-it-works and build-the-lever principles to keep checks real and cheap.",
    "expectedReduced": "When execution or Git writes are unavailable or unauthorized, provide a reduced ordered migration and delivery plan with a concrete check per unit. State which checks and Git operations were not performed; do not treat an unrun check as green.",
    "expectedBlocked": "Block advancement past a failed or unavailable required check and identify the missing capability or permission. Preserve the current unit for diagnosis.",
    "forbiddenClaims": [
      "An unrun or failed check is green.",
      "A batch check replaces verification of each unit.",
      "A delivery plan proves independently landable commits or actual host execution.",
      "The principle authorizes rebase, commit or PR writes without permission."
    ],
    "caseFile": "docs/parity/cases/skills/principle-sequence-verifiable-units.json"
  },
  "registry": {
    "caseId": "migration-units",
    "caseFile": "docs/parity/cases/skills/principle-sequence-verifiable-units.json",
    "sourcePaths": [
      "skills/principle-sequence-verifiable-units/SKILL.md"
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
      "attemptId": "grades-native-03.json#1",
      "order": 0,
      "gradeFile": "grades-native-03.json",
      "rankWithinFile": 1,
      "host": "codex",
      "caseId": "migration-units",
      "status": "reduced-pass",
      "grade": {
        "caseId": "migration-units",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_7",
          "item_19"
        ],
        "rawTrace": "codex/batch-03.events.jsonl",
        "responseArtifact": "fixtures/batch-03/migration-units.result.md",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Database/schema/consumer inputs and integration runner absent.",
          "Git delivery unperformed under explicit prohibition."
        ],
        "review": "Provides ordered baseline/expand/backfill/consumer/contract plan with concrete per-unit checks and green-before-next gates. Only JSON baseline actually runs; DB checks and proposed PRs remain unperformed. Git operations are forbidden and no clean trunk claimed.",
        "variantReview": [
          "See actual variants and limitations in response artifact; unperformed capability branches do not receive full credit."
        ],
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-03.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Inspect a clean trunk baseline and rebase when authorized. Every ordered migration unit identifies its known-good start, one change and concrete check; advance only on green. Delivery uses a failing test before its fix, or another justified order such as subtraction before reshape, baseline before treatment or scaffold before feature. Every commit lands on its own. Use the prove-it-works and build-the-lever principles to keep checks real and cheap.",
        "reducedExpected": "When execution or Git writes are unavailable or unauthorized, provide a reduced ordered migration and delivery plan with a concrete check per unit. State which checks and Git operations were not performed; do not treat an unrun check as green."
      },
      "topLevelContext": {
        "gradingNotes": [
          "Native raw events, actual result reports and saved source/artifacts reviewed. Model selfgrades and integrity scripts are not workflow proof.",
          "Local subprocesses are not independent AI workers; no worker/service method credit from proxies.",
          "Native agent startup errors are observed failures, not proof operation absent.",
          "Conditional simulated capability branches are not host-enforced denials.",
          "Missing fixtures are blockers, not skill defects.",
          "Read-event IDs are local to raw trace."
        ]
      },
      "response": {
        "text": "# migration-units\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"migration-units\",\n  \"prompt\": \"Plan a multi-step schema migration and its commit delivery. Give each ordered unit a specific check, show when the next unit can begin, and handle an unavailable test runner or unauthorized Git operation.\",\n  \"requirements\": [\n    \"Each ordered unit ends in a specific check.\",\n    \"Start from a known-good baseline and verify one change before the next.\",\n    \"Order independently landable commits and PRs so a reviewer can replay the argument.\",\n    \"Preserve authorization and observed execution limits.\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-sequence-verifiable-units/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 5. See [source-reads.json](migration-units/source-reads.json). Supplied input archive: [supplied-input.json](migration-units/supplied-input.json).\n\n## Actual response and variants\n\nA reduced delivery plan is available. Git operations are unauthorized. No schema engine, database, application consumer or target schema was supplied, so this plan uses an explicitly proposed fixture example: move the numeric orders.total field to orders.totalAmount without changing its units or value. This is not an actual database migration.\n\nAn observed local baseline check verified three unique order IDs and finite totals. See baseline.command.json, exit 0. This establishes only the JSON fixture baseline. A clean trunk, database snapshot, consumer baseline and remote main were not inspected. No rebase was attempted.\n\n| Ordered unit and proposed delivery | Known-good start and one change | Specific check | When the next unit may begin |\n| --- | --- | --- | --- |\n| 0. Baseline evidence | Copy supplied JSON and validate its shape | Assert 3 rows, 3 unique IDs, all finite totals. Observed locally. Production schema/consumer tests remain absent. | Fixture planning can proceed; real implementation waits for database and consumer baseline. |\n| 1. Expand schema, PR 1 | Add nullable totalAmount without changing readers | On a disposable database, inspect column type/nullability and rerun old-reader integration tests. Unrun. | Only when both schema and old reader checks succeed. |\n| 2. Backfill, PR 2 atop 1 | Copy total into totalAmount in bounded rerunnable batches | Compare row counts and exact per-ID values; no missing amounts; rerun batch and assert zero value changes. Unrun. | Only when all comparisons and rerun succeed. |\n| 3. Switch writers/readers, PR 3 atop 2 | Use totalAmount at all application boundaries | Exercise create/update/read/export against new schema, compare literal outputs and assert no legacy reads. Unrun. | Only after all consumer tests succeed and old deployed consumers are gone. |\n| 4. Contract schema, PR 4 atop 3 | Require totalAmount and drop total | Inspect non-null constraint, reject missing amount, scan all code for legacy reference, run complete integration suite and restore drill. Unrun. | Finish only when every check succeeds. |\n\nThe expand phase is durable schema evolution needed for separately deployable consumers, not a permanent compatibility API. Record its removal condition in PR 1. If no mixed consumer deployment is required, combine expansion, backfill, consumer switch and contraction in one isolated offline release rather than retaining a throwaway state.\n\nBaseline-before-treatment is the delivery argument here. Each proposed PR contains a functional migration plus its checks and remains usable with all earlier PRs. A deliberately failing test is evidence on the development branch; do not land red required CI merely to tell a story. These PRs are proposed, not created or proven independently landable.\n\nVariants attempted:\n\n| Variant | Response and actual operations |\n| --- | --- |\n| Available Bun baseline | Executed baseline.command.json with exit 0; no later migration unit executed. |\n| Test runner unavailable | Scenario-only reduction. Host Bun works; no runner was disabled. Keep the current unit and mark its required integration check unverified. Stop before the next unit. A JSON assertion does not replace a database test runner. |\n| Git unauthorized | Actually constrained by user instruction. Rebase, commit, push and PR creation were not attempted. Preserve this ordered plan and local receipts for a later authorized owner. |\n\nBuild-the-lever and prove-it-works are referenced by the source principle; no claim is made that an unrun migration or delivery check succeeded. The actual baseline command is retained for rerun.\n\n## Real command results\n\n```\n[\n  {\n    \"artifact\": \"migration-units/baseline.command.json\",\n    \"label\": \"baseline\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"-e\",\n      \"const a=await Bun.file('migration-units/input/orders.json').json();if(a.length!==3||new Set(a.map(x=>x.id)).size!==3||a.some(x=>!Number.isFinite(x.total)))throw Error('invalid baseline');console.log('Baseline: 3 unique ids and finite totals.');\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"Baseline: 3 unique ids and finite totals.\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  }\n]\n```\n\n## Artifacts\n\n- [migration-units/baseline.command.json](migration-units/baseline.command.json)\n- [migration-units/input/orders.json](migration-units/input/orders.json)\n- [migration-units/response.md](migration-units/response.md)\n- [migration-units/source-reads.json](migration-units/source-reads.json)\n- [migration-units/supplied-input.json](migration-units/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n",
        "artifact": {
          "path": "fixtures/batch-03/migration-units.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/migration-units.result.md",
          "sha256": "7282571db2a98bb428c92d1870d098783dca189fb4eccc8ed52f281331c8a0cc",
          "bytes": 7093
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-03.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-03.events.jsonl",
            "sha256": "9ab1f5caa570a77bd03c01b4413d290260b4093d57c18425197bc35ec14a38dc",
            "bytes": 455585,
            "eventReferences": [
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "8220fc576bc45232f6f2f51be6a0ada9ec46ac7d07e0e808013cd475f2547027"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "66fbde52aad7e2d4a5315fd556d83dac6ea7136ee3916cfeb4bde0aaa546b576",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "034ef504598ef9a3e9fc53b89295cca14edf990ee9b7c70b2fcc207694ae8e59"
              },
              {
                "eventId": "item_19",
                "line": 37,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "91f6911ca226fbd09214b54adab325e3eb5fe977d9a5676afdf0e11a381d3577",
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
            "item_7",
            "item_19"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-03.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-03/migration-units/baseline.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/migration-units/baseline.command.json",
      "sha256": "d7089d4ad7fd1b1667cbc8a8a5bf00d8bd1e18f9f7a18ce51d0dda7d57a3e2ca",
      "bytes": 455,
      "owners": [
        "grades-native-03.json#1"
      ],
      "text": "{\n  \"label\": \"baseline\",\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"const a=await Bun.file('migration-units/input/orders.json').json();if(a.length!==3||new Set(a.map(x=>x.id)).size!==3||a.some(x=>!Number.isFinite(x.total)))throw Error('invalid baseline');console.log('Baseline: 3 unique ids and finite totals.');\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"Baseline: 3 unique ids and finite totals.\\n\",\n  \"stderr\": \"\",\n  \"expectedExitCode\": 0\n}\n"
    },
    {
      "path": "fixtures/batch-03/migration-units/response.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/migration-units/response.md",
      "sha256": "99ae0454fa1f55d6b1eba90063c9e91c6f8acda2399ca2bcf8836a596e855110",
      "bytes": 3625,
      "owners": [
        "grades-native-03.json#1"
      ],
      "text": "A reduced delivery plan is available. Git operations are unauthorized. No schema engine, database, application consumer or target schema was supplied, so this plan uses an explicitly proposed fixture example: move the numeric orders.total field to orders.totalAmount without changing its units or value. This is not an actual database migration.\n\nAn observed local baseline check verified three unique order IDs and finite totals. See baseline.command.json, exit 0. This establishes only the JSON fixture baseline. A clean trunk, database snapshot, consumer baseline and remote main were not inspected. No rebase was attempted.\n\n| Ordered unit and proposed delivery | Known-good start and one change | Specific check | When the next unit may begin |\n| --- | --- | --- | --- |\n| 0. Baseline evidence | Copy supplied JSON and validate its shape | Assert 3 rows, 3 unique IDs, all finite totals. Observed locally. Production schema/consumer tests remain absent. | Fixture planning can proceed; real implementation waits for database and consumer baseline. |\n| 1. Expand schema, PR 1 | Add nullable totalAmount without changing readers | On a disposable database, inspect column type/nullability and rerun old-reader integration tests. Unrun. | Only when both schema and old reader checks succeed. |\n| 2. Backfill, PR 2 atop 1 | Copy total into totalAmount in bounded rerunnable batches | Compare row counts and exact per-ID values; no missing amounts; rerun batch and assert zero value changes. Unrun. | Only when all comparisons and rerun succeed. |\n| 3. Switch writers/readers, PR 3 atop 2 | Use totalAmount at all application boundaries | Exercise create/update/read/export against new schema, compare literal outputs and assert no legacy reads. Unrun. | Only after all consumer tests succeed and old deployed consumers are gone. |\n| 4. Contract schema, PR 4 atop 3 | Require totalAmount and drop total | Inspect non-null constraint, reject missing amount, scan all code for legacy reference, run complete integration suite and restore drill. Unrun. | Finish only when every check succeeds. |\n\nThe expand phase is durable schema evolution needed for separately deployable consumers, not a permanent compatibility API. Record its removal condition in PR 1. If no mixed consumer deployment is required, combine expansion, backfill, consumer switch and contraction in one isolated offline release rather than retaining a throwaway state.\n\nBaseline-before-treatment is the delivery argument here. Each proposed PR contains a functional migration plus its checks and remains usable with all earlier PRs. A deliberately failing test is evidence on the development branch; do not land red required CI merely to tell a story. These PRs are proposed, not created or proven independently landable.\n\nVariants attempted:\n\n| Variant | Response and actual operations |\n| --- | --- |\n| Available Bun baseline | Executed baseline.command.json with exit 0; no later migration unit executed. |\n| Test runner unavailable | Scenario-only reduction. Host Bun works; no runner was disabled. Keep the current unit and mark its required integration check unverified. Stop before the next unit. A JSON assertion does not replace a database test runner. |\n| Git unauthorized | Actually constrained by user instruction. Rebase, commit, push and PR creation were not attempted. Preserve this ordered plan and local receipts for a later authorized owner. |\n\nBuild-the-lever and prove-it-works are referenced by the source principle; no claim is made that an unrun migration or delivery check succeeded. The actual baseline command is retained for rerun.\n"
    },
    {
      "path": "fixtures/batch-03/migration-units/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/migration-units/supplied-input.json",
      "sha256": "f869c4e5c5f01194d73ba445f1302e87b4e7cdb4559543bb819514e34d7decf2",
      "bytes": 2015,
      "owners": [
        "grades-native-03.json#1"
      ],
      "text": "{\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"id\": \"migration-units\",\n  \"sourcePaths\": [\n    \"skills/principle-sequence-verifiable-units/SKILL.md\"\n  ],\n  \"prompt\": \"Plan a multi-step schema migration and its commit delivery. Give each ordered unit a specific check, show when the next unit can begin, and handle an unavailable test runner or unauthorized Git operation.\",\n  \"requirements\": [\n    \"Each ordered unit ends in a specific check.\",\n    \"Start from a known-good baseline and verify one change before the next.\",\n    \"Order independently landable commits and PRs so a reviewer can replay the argument.\",\n    \"Preserve authorization and observed execution limits.\"\n  ],\n  \"expectedFull\": \"Inspect a clean trunk baseline and rebase when authorized. Every ordered migration unit identifies its known-good start, one change and concrete check; advance only on green. Delivery uses a failing test before its fix, or another justified order such as subtraction before reshape, baseline before treatment or scaffold before feature. Every commit lands on its own. Use the prove-it-works and build-the-lever principles to keep checks real and cheap.\",\n  \"expectedReduced\": \"When execution or Git writes are unavailable or unauthorized, provide a reduced ordered migration and delivery plan with a concrete check per unit. State which checks and Git operations were not performed; do not treat an unrun check as green.\",\n  \"expectedBlocked\": \"Block advancement past a failed or unavailable required check and identify the missing capability or permission. Preserve the current unit for diagnosis.\",\n  \"forbiddenClaims\": [\n    \"An unrun or failed check is green.\",\n    \"A batch check replaces verification of each unit.\",\n    \"A delivery plan proves independently landable commits or actual host execution.\",\n    \"The principle authorizes rebase, commit or PR writes without permission.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-03/migration-units.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/migration-units.result.md",
      "sha256": "7282571db2a98bb428c92d1870d098783dca189fb4eccc8ed52f281331c8a0cc",
      "bytes": 7093,
      "owners": [
        "grades-native-03.json#1"
      ],
      "text": "# migration-units\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"migration-units\",\n  \"prompt\": \"Plan a multi-step schema migration and its commit delivery. Give each ordered unit a specific check, show when the next unit can begin, and handle an unavailable test runner or unauthorized Git operation.\",\n  \"requirements\": [\n    \"Each ordered unit ends in a specific check.\",\n    \"Start from a known-good baseline and verify one change before the next.\",\n    \"Order independently landable commits and PRs so a reviewer can replay the argument.\",\n    \"Preserve authorization and observed execution limits.\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-sequence-verifiable-units/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 5. See [source-reads.json](migration-units/source-reads.json). Supplied input archive: [supplied-input.json](migration-units/supplied-input.json).\n\n## Actual response and variants\n\nA reduced delivery plan is available. Git operations are unauthorized. No schema engine, database, application consumer or target schema was supplied, so this plan uses an explicitly proposed fixture example: move the numeric orders.total field to orders.totalAmount without changing its units or value. This is not an actual database migration.\n\nAn observed local baseline check verified three unique order IDs and finite totals. See baseline.command.json, exit 0. This establishes only the JSON fixture baseline. A clean trunk, database snapshot, consumer baseline and remote main were not inspected. No rebase was attempted.\n\n| Ordered unit and proposed delivery | Known-good start and one change | Specific check | When the next unit may begin |\n| --- | --- | --- | --- |\n| 0. Baseline evidence | Copy supplied JSON and validate its shape | Assert 3 rows, 3 unique IDs, all finite totals. Observed locally. Production schema/consumer tests remain absent. | Fixture planning can proceed; real implementation waits for database and consumer baseline. |\n| 1. Expand schema, PR 1 | Add nullable totalAmount without changing readers | On a disposable database, inspect column type/nullability and rerun old-reader integration tests. Unrun. | Only when both schema and old reader checks succeed. |\n| 2. Backfill, PR 2 atop 1 | Copy total into totalAmount in bounded rerunnable batches | Compare row counts and exact per-ID values; no missing amounts; rerun batch and assert zero value changes. Unrun. | Only when all comparisons and rerun succeed. |\n| 3. Switch writers/readers, PR 3 atop 2 | Use totalAmount at all application boundaries | Exercise create/update/read/export against new schema, compare literal outputs and assert no legacy reads. Unrun. | Only after all consumer tests succeed and old deployed consumers are gone. |\n| 4. Contract schema, PR 4 atop 3 | Require totalAmount and drop total | Inspect non-null constraint, reject missing amount, scan all code for legacy reference, run complete integration suite and restore drill. Unrun. | Finish only when every check succeeds. |\n\nThe expand phase is durable schema evolution needed for separately deployable consumers, not a permanent compatibility API. Record its removal condition in PR 1. If no mixed consumer deployment is required, combine expansion, backfill, consumer switch and contraction in one isolated offline release rather than retaining a throwaway state.\n\nBaseline-before-treatment is the delivery argument here. Each proposed PR contains a functional migration plus its checks and remains usable with all earlier PRs. A deliberately failing test is evidence on the development branch; do not land red required CI merely to tell a story. These PRs are proposed, not created or proven independently landable.\n\nVariants attempted:\n\n| Variant | Response and actual operations |\n| --- | --- |\n| Available Bun baseline | Executed baseline.command.json with exit 0; no later migration unit executed. |\n| Test runner unavailable | Scenario-only reduction. Host Bun works; no runner was disabled. Keep the current unit and mark its required integration check unverified. Stop before the next unit. A JSON assertion does not replace a database test runner. |\n| Git unauthorized | Actually constrained by user instruction. Rebase, commit, push and PR creation were not attempted. Preserve this ordered plan and local receipts for a later authorized owner. |\n\nBuild-the-lever and prove-it-works are referenced by the source principle; no claim is made that an unrun migration or delivery check succeeded. The actual baseline command is retained for rerun.\n\n## Real command results\n\n```\n[\n  {\n    \"artifact\": \"migration-units/baseline.command.json\",\n    \"label\": \"baseline\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"-e\",\n      \"const a=await Bun.file('migration-units/input/orders.json').json();if(a.length!==3||new Set(a.map(x=>x.id)).size!==3||a.some(x=>!Number.isFinite(x.total)))throw Error('invalid baseline');console.log('Baseline: 3 unique ids and finite totals.');\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"Baseline: 3 unique ids and finite totals.\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  }\n]\n```\n\n## Artifacts\n\n- [migration-units/baseline.command.json](migration-units/baseline.command.json)\n- [migration-units/input/orders.json](migration-units/input/orders.json)\n- [migration-units/response.md](migration-units/response.md)\n- [migration-units/source-reads.json](migration-units/source-reads.json)\n- [migration-units/supplied-input.json](migration-units/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-03/migration-units/input",
      "owner": "grades-native-03.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/migration-units/source",
      "owner": "grades-native-03.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/migration-units/source-reads.json",
      "owner": "grades-native-03.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-03/migration-units/input",
      "owner": "grades-native-03.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/migration-units/source",
      "owner": "grades-native-03.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/migration-units/source-reads.json",
      "owner": "grades-native-03.json#1",
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
