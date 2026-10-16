# codex: repeatable-change

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "repeatable-change",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-rerun-02.json#2",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.",
  "caseDefinition": {
    "id": "repeatable-change",
    "sourcePaths": [
      "skills/principle-build-the-lever/SKILL.md"
    ],
    "prompt": "Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.",
    "requirements": [
      "Source reads; authorized artifact writes and execution for full proof.",
      "Independent workers require exposed worker tools and user authorization; they are unnecessary when a deterministic tool processes all units."
    ],
    "expectedFull": "Produce the smallest safe rerunnable tool as a file; learn the recipe on a first unit, rerun and diff it against the hand-done result, and report observed commands and outputs. Retain the tool for review and commit only with authorization when work outlives the session.",
    "expectedReduced": "When writes or execution are unavailable, propose the tool and verification recipe as reduced capability, distinguish the proposal from a saved artifact and executed proof, and state the missing capabilities.",
    "expectedBlocked": "If source is unavailable or denied, state that the recipe and equivalence cannot be verified; request the required source or capability without claiming implementation or proof.",
    "forbiddenClaims": [
      "A proposed tool was saved, run or verified without observed evidence.",
      "Hand-applied changes alone satisfy the principle.",
      "Sequential work proves independent workers.",
      "Invocation grants commit, delegation or external-action permission."
    ],
    "caseFile": "docs/parity/cases/skills/principle-build-the-lever.json"
  },
  "registry": {
    "caseId": "repeatable-change",
    "caseFile": "docs/parity/cases/skills/principle-build-the-lever.json",
    "sourcePaths": [
      "skills/principle-build-the-lever/SKILL.md"
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
        "isolated-write"
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
        "writes"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-03.json#7",
      "order": 0,
      "gradeFile": "grades-native-03.json",
      "rankWithinFile": 7,
      "host": "codex",
      "caseId": "repeatable-change",
      "status": "fail",
      "grade": {
        "caseId": "repeatable-change",
        "host": "codex",
        "status": "fail",
        "execution": "direct",
        "actualReadEventIds": [
          "item_7",
          "item_19"
        ],
        "rawTrace": "codex/batch-03.events.jsonl",
        "responseArtifact": "fixtures/batch-03/repeatable-change.result.md",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Required hand-first-before-tool-authoring chronology not followed."
        ],
        "review": "Real deterministic migration script, literal-reference comparison, rerun/version2 equivalence and invalid-input rejection are observed. However the model authors the tool before materializing the hand-done first unit. Source explicitly requires first manual unit to learn recipe, then tool. Report admits reversed chronology. Available inputs/writes/execution make this a method-compliance failure, not a blocked fixture or runtime failure.",
        "variantReview": [
          "Migration, legacy rerun, already-v2 and invalid-input checks completed; first manual unit chronology failed."
        ],
        "concreteFixCandidates": [
          "Evaluation execution: create and inspect manual first-unit artifact before writing tool; record event order; rerun this case. Existing skill already states correct sequence, so this alone does not justify a source-text fix."
        ],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-03.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Produce the smallest safe rerunnable tool as a file; learn the recipe on a first unit, rerun and diff it against the hand-done result, and report observed commands and outputs. Retain the tool for review and commit only with authorization when work outlives the session.",
        "reducedExpected": "When writes or execution are unavailable, propose the tool and verification recipe as reduced capability, distinguish the proposal from a saved artifact and executed proof, and state the missing capabilities."
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
        "text": "# repeatable-change\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"repeatable-change\",\n  \"prompt\": \"Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.\",\n  \"requirements\": [\n    \"Source reads; authorized artifact writes and execution for full proof.\",\n    \"Independent workers require exposed worker tools and user authorization; they are unnecessary when a deterministic tool processes all units.\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-build-the-lever/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 5. See [source-reads.json](repeatable-change/source-reads.json). Supplied input archive: [supplied-input.json](repeatable-change/supplied-input.json).\n\n## Actual response and variants\n\nBuilt and executed migrate.mjs, a deterministic JSON migration tool. The copied orders fixture was split into three synthetic legacy files. The chosen target renames total to totalAmount and adds schemaVersion 2, preserving all other supplied fields and numeric values. This target is a local evaluation choice, not a supplied production schema.\n\nThe manual first-unit reference is manual/1.json. The initial tool file was authored before that reference was materialized; the reference was written before the first migration execution. Thus the run proves independent literal-reference equivalence and rerunnability, but does not demonstrate the skill's ideal hand-first-before-tool-authoring chronology. This limitation is explicit rather than reconstructed as a prior action.\n\nActual execution and proof:\n\n| Command receipt | Observed result |\n| --- | --- |\n| migration-first.command.json | Processed 1.json, 2.json and 3.json, exit 0. |\n| comparison.command.json | Literal first-unit bytes matched the manual reference. All 3 records preserved id, status, customer and total value; no legacy total remained. Exit 0. |\n| migration-rerun.command.json | Reprocessed all 3 legacy files, exit 0. Coordinator compared before/after bytes and found no change. |\n| migration-v2-input.command.json | Accepted already-migrated records into a separate output directory, exit 0. Coordinator compared all output bytes and found no change. |\n| reject-invalid.command.json | Rejected a nonnumeric total with exit 1 and exact diagnostic. No invalid output was produced, as checked by coordinator. |\n\nThe tool prevalidates the batch before writing, rejects conflicting schema shapes, sorts filenames, and uses temporary-file rename per output. Writes are limited to caller-selected directories. Its current CLI trusts authorized local paths; it is not an untrusted-input sandbox. Per-file atomic replacement is not transactionality across a whole batch or crash durability. No crash or concurrent-writer test was performed. Rerunning converges under the observed normal execution conditions.\n\nVariants attempted: first migration, repeat of legacy input, already-v2 input, invalid input. The deterministic tool processed every unit, so no workers were needed. Source, writes and execution were available. Tool, manual reference, input/output files, stdout/stderr, exit statuses and equality observations are saved. Commits were forbidden and unperformed.\n\n## Real command results\n\n```\n[\n  {\n    \"artifact\": \"repeatable-change/comparison.command.json\",\n    \"label\": \"comparison\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/check.mjs\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"Three records preserve id, status, customer and numeric total. First-unit bytes equal manual reference.\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"repeatable-change/migration-first.command.json\",\n    \"label\": \"migration-first\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/migrate.mjs\",\n      \"repeatable-change/legacy\",\n      \"repeatable-change/output\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"processed\\\":3,\\\"files\\\":[\\\"1.json\\\",\\\"2.json\\\",\\\"3.json\\\"]}\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"repeatable-change/migration-rerun.command.json\",\n    \"label\": \"migration-rerun\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/migrate.mjs\",\n      \"repeatable-change/legacy\",\n      \"repeatable-change/output\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"processed\\\":3,\\\"files\\\":[\\\"1.json\\\",\\\"2.json\\\",\\\"3.json\\\"]}\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"repeatable-change/migration-v2-input.command.json\",\n    \"label\": \"migration-v2-input\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/migrate.mjs\",\n      \"repeatable-change/output\",\n      \"repeatable-change/v2-output\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"processed\\\":3,\\\"files\\\":[\\\"1.json\\\",\\\"2.json\\\",\\\"3.json\\\"]}\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"repeatable-change/reject-invalid.command.json\",\n    \"label\": \"reject-invalid\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/migrate.mjs\",\n      \"repeatable-change/invalid\",\n      \"repeatable-change/rejected-output\"\n    ],\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \" 9 |   const current=record.schemaVersion===2;\\n10 |   const {total,...rest}=record;\\n11 |   if(current) {\\n12 |     if('total' in record || !Number.isFinite(record.totalAmount)) throw new Error(`Invalid v2 ${name}`);\\n13 |   } else if(record.schemaVersion!==undefined || !Number.isFinite(total) || 'totalAmount' in record) {\\n14 |     throw new Error(`Invalid legacy ${name}`);\\n                   ^\\nerror: Invalid legacy bad.json\\n      at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/migrate.mjs:14:15\\n\\nBun v1.4.2 (macOS arm64)\\n\",\n    \"expectedExitCode\": 1\n  }\n]\n```\n\n## Artifacts\n\n- [repeatable-change/check.mjs](repeatable-change/check.mjs)\n- [repeatable-change/comparison.command.json](repeatable-change/comparison.command.json)\n- [repeatable-change/idempotence.json](repeatable-change/idempotence.json)\n- [repeatable-change/input/orders.json](repeatable-change/input/orders.json)\n- [repeatable-change/invalid-rejection.json](repeatable-change/invalid-rejection.json)\n- [repeatable-change/invalid/bad.json](repeatable-change/invalid/bad.json)\n- [repeatable-change/legacy/1.json](repeatable-change/legacy/1.json)\n- [repeatable-change/legacy/2.json](repeatable-change/legacy/2.json)\n- [repeatable-change/legacy/3.json](repeatable-change/legacy/3.json)\n- [repeatable-change/manual/1.json](repeatable-change/manual/1.json)\n- [repeatable-change/migrate.mjs](repeatable-change/migrate.mjs)\n- [repeatable-change/migration-first.command.json](repeatable-change/migration-first.command.json)\n- [repeatable-change/migration-rerun.command.json](repeatable-change/migration-rerun.command.json)\n- [repeatable-change/migration-v2-input.command.json](repeatable-change/migration-v2-input.command.json)\n- [repeatable-change/output/1.json](repeatable-change/output/1.json)\n- [repeatable-change/output/2.json](repeatable-change/output/2.json)\n- [repeatable-change/output/3.json](repeatable-change/output/3.json)\n- [repeatable-change/reject-invalid.command.json](repeatable-change/reject-invalid.command.json)\n- [repeatable-change/response.md](repeatable-change/response.md)\n- [repeatable-change/source-reads.json](repeatable-change/source-reads.json)\n- [repeatable-change/supplied-input.json](repeatable-change/supplied-input.json)\n- [repeatable-change/v2-output/1.json](repeatable-change/v2-output/1.json)\n- [repeatable-change/v2-output/2.json](repeatable-change/v2-output/2.json)\n- [repeatable-change/v2-output/3.json](repeatable-change/v2-output/3.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n",
        "artifact": {
          "path": "fixtures/batch-03/repeatable-change.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change.result.md",
          "sha256": "c58888c375faf95981df782a3a3c0b6abc540a6a2e080dd3392d37c197e8f189",
          "bytes": 9378
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
    },
    {
      "attemptId": "grades-native-rerun-02.json#2",
      "order": 102,
      "gradeFile": "grades-native-rerun-02.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "repeatable-change",
      "status": "pass",
      "grade": {
        "caseId": "repeatable-change",
        "status": "pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_5",
          "item_8",
          "item_9"
        ],
        "actualExecutionEventIds": [
          "item_16",
          "item_18",
          "item_20",
          "item_22"
        ],
        "review": "Raw native item16 materializes literal manual first-unit result before item18 writes tool. Tool output byte-matches manual exemplar, migrates six manifests/retains already-v2, reruns changed0 with byte equality, rejects three invalid inputs without overwrite. Corrects prior method chronology failure rather than erasing it.",
        "prior": {
          "artifact": "grades-native-03.json",
          "status": "fail",
          "retained": true
        },
        "proof": [
          "fixtures/rerun-02/repeatable-change/manual-byte-comparison.json",
          "fixtures/rerun-02/repeatable-change/complete-migration.json",
          "fixtures/rerun-02/repeatable-change/complete-rerun.json",
          "fixtures/rerun-02/repeatable-change/idempotence-comparison.json",
          "fixtures/rerun-02/repeatable-change/negative-unknown.json",
          "fixtures/rerun-02/repeatable-change/negative-malformed.json",
          "fixtures/rerun-02/repeatable-change/negative-invalid-fields.json"
        ],
        "host": "codex",
        "rawTrace": "codex/rerun-02.events.jsonl",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "responseArtifact": "fixtures/rerun-02/repeatable-change.result.md",
        "variantReview": [
          "Full actual source/write/execution branch completed. Capability-negative text is explicitly simulated, not actual denied-host execution."
        ],
        "limits": [
          "Source freeze supplied; installed version0.1.0 and actual source bytes observed.",
          "No worker/service/metadata enforcement claim.",
          "Prior results untouched."
        ],
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "attempt": "rerun-02"
      },
      "response": {
        "text": "# repeatable-change\n\nSaved the literal hand-authored manual/search.json before creating migrate.mjs. Saved the original separately in pristine/ and first-unit/. The tool validates inputs before writing, handles v1 conversion, preserves optional tags and field order, and leaves valid v2 bytes intact. It preflights selected files before overwriting any of them. This is a deterministic direct workflow; independent workers are unnecessary and none were spawned.\n\nExecuted the tool on the pristine first-unit copy, then diffed generated and manual bytes: exit 0 with no diff. The complete owned tree scan found 7 manifests and changed 6. Independently specified expected bytes were asserted for all six transformed manifests, including escaped text, omitted tags, empty tags and both statuses. Notes, scope and already-v2 bytes were compared to pristine and were unchanged. The complete rerun scanned 7 and changed 0; before/after SHA-256 snapshots and diff confirm the entire owned work tree was unchanged. Unknown-version, malformed-JSON and invalid-field inputs each exited 1 with a clear file-specific error; their original bytes remained unchanged. Tool and proof scripts are retained without a commit.\n\n## Scope and provenance\n\nSource package root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nSupplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Package metadata confirms version 0.1.0. No package Git revision was independently established; the supplied freeze is an input identifier, not verified provenance. Named source/support contents were actually read and saved in [source-reads.txt](repeatable-change/source-reads.txt). Registry entry is in [registry-entry.json](repeatable-change/registry-entry.json). No separate 0.2.1 package files were used. The compiler came from the independent installed Bun cache, not another plugin version.\n\nAll fixture data is synthetic. Shared inputs were copied in full to pristine/ and work/ before edits. Final pristine-integrity diff exited 0. No real service contact, issue, PR, message, commit, push, publish, configuration change, dependency installation or schedule occurred. No worker receipts or screenshots are claimed. Runtime timing strings below are Bun's actual output and are not performance benchmarks.\n\n## Supplied input\n\nFull registered contract:\n\n```json\n{\n  \"id\": \"repeatable-change\",\n  \"sourcePaths\": [\n    \"skills/principle-build-the-lever/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.\",\n  \"requirements\": [\n    \"Source reads; authorized artifact writes and execution for full proof.\",\n    \"Independent workers require exposed worker tools and user authorization; they are unnecessary when a deterministic tool processes all units.\"\n  ],\n  \"expectedFull\": \"Produce the smallest safe rerunnable tool as a file; learn the recipe on a first unit, rerun and diff it against the hand-done result, and report observed commands and outputs. Retain the tool for review and commit only with authorization when work outlives the session.\",\n  \"expectedReduced\": \"When writes or execution are unavailable, propose the tool and verification recipe as reduced capability, distinguish the proposal from a saved artifact and executed proof, and state the missing capabilities.\",\n  \"expectedBlocked\": \"If source is unavailable or denied, state that the recipe and equivalence cannot be verified; request the required source or capability without claiming implementation or proof.\",\n  \"forbiddenClaims\": [\n    \"A proposed tool was saved, run or verified without observed evidence.\",\n    \"Hand-applied changes alone satisfy the principle.\",\n    \"Sequential work proves independent workers.\",\n    \"Invocation grants commit, delegation or external-action permission.\"\n  ]\n}\n```\n\nComplete scenario scope:\n\n```markdown\n# Manifest migration recipe\n\nThis is a private synthetic multi-directory manifest migration. All target files match manifests/**/*.json. Each v1 object has exactly version, key, label, enabled and optional tags. Convert version:1 to version:2, key to id, label to displayName and enabled boolean to status:'enabled' or 'disabled'. Preserve tags exactly and emit keys in this order: version,id,displayName,status,tags (omit tags when absent). Output JSON uses two-space indentation and one final newline. Already-v2 manifests remain byte-for-byte unchanged. README and notes are not migration targets. Unknown versions or malformed inputs must cause a clear error before overwriting that file.\n\nFirst copy manifests/core/search.json to an owned manual/ directory and hand-apply the recipe. Preserve a pristine copy of that original separately. Only after the manual result exists, write the smallest deterministic rerunnable tool as a real file. Run it on the pristine first-unit copy and compare bytes to the manual result. Then migrate the complete owned manifest tree, inspect outputs and run the tool again to check no changes. Do not overwrite the manual exemplar or shared originals. Retain the tool and actual command outputs; no commit or external action is authorized by this fixture.\n\nThe supplied files are initial inputs only. A completed transformed output, tool, test pass or equivalence receipt is intentionally absent.\n```\n\nOriginal source inputs are retained byte-for-byte in [repeatable-change/pristine/](repeatable-change/pristine/). The shared scenario map and compiler hints were read through the exposed command tool and copied to the writable root. Preparation checks were not used as execution proof.\n\n## Variants and limits\n\nThe full workflow was executed on the actual host. Reduced and blocked responses were captured as explicitly simulated fallback text in [capability-variants.md](repeatable-change/capability-variants.md). Their actual responses follow.\n\nReduced: Simulated missing writes or execution. Proposed tool: a Bun script that traverses manifests/**/*.json, validates version and fields, renames the v1 fields in the required order, preserves tags and leaves v2 bytes untouched. First hand-transform search.json, then generate from a separate pristine copy, diff the bytes, migrate the owned tree, snapshot bytes and rerun to prove idempotence. Under this simulated restriction no tool was saved, run or verified. The actual-host tool belongs to the separate executed variant.\n\nBlocked: Simulated missing source. Without the source manifests and recipe, do not claim a verified transformation or equivalence. Required inputs are the v1/v2 schema, formatting rules, file scope and a pristine first unit. In the actual host these inputs were available; this text does not prove a denied read.\n\nHost-enforced no-write, no-execution and unavailable-source variants remain unexercised. The host provided these capabilities, and changing configuration to manufacture denials was forbidden. Simulated text does not prove host denial. Metadata enforcement was not tested. Independent worker variants were unnecessary and not attempted. Missing actual model identity is irrelevant to these direct file workflows; no model execution receipt is claimed. No self-assigned grade is included.\n\n## Actual tools, actions and chronology\n\nExposed tool used: functions.exec, invoking tools.exec_command. Bun performed file writes, reads, command execution and assertion scripts. Local diff and rg commands ran through Bun in the saved execution records. Bindings and their limitations are in [capability-bindings.json](repeatable-change/capability-bindings.json).\n\nThe ordered initial discovery reads precede the timestamped journal and are documented in [pre-journal-actions.md](pre-journal-actions.md); their raw tool responses remain in this session transcript. The following timestamps are actual UTC event times from the command runner. Asia/Amman is UTC+03:00. The journal captures case operations in execution order; it does not reconstruct unobserved actions.\n\n- 2026-10-16T07:59:06.415Z setup: {\"sourceRoot\":\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\"scenario\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/repeatable-change\",\"copies\":[\"pristine\",\"work\"],\"sourceReads\":\"source-reads.txt\"}\n- 2026-10-16T08:00:02.662Z manual-start: \"Copied original into manual/search.json and first-unit/search.json. No migration tool exists yet.\"\n- 2026-10-16T08:00:02.663Z manual-result: {\"file\":\"manual/search.json\",\"method\":\"literal hand-authored transformation, not generated from input\",\"bytes\":\"{\\n  \\\"version\\\": 2,\\n  \\\"id\\\": \\\"search\\\",\\n  \\\"displayName\\\": \\\"Search\\\",\\n  \\\"status\\\": \\\"enabled\\\",\\n  \\\"tags\\\": [\\n    \\\"core\\\",\\n    \\\"user\\\"\\n  ]\\n}\\n\"}\n- 2026-10-16T08:00:44.304Z tool-written: {\"file\":\"migrate.mjs\",\"manualAlreadyExists\":true}\n- 2026-10-16T08:00:44.304Z command-start: \"first-unit-execution\"\n- 2026-10-16T08:00:44.316Z command-result: \"first-unit-execution\"\n- 2026-10-16T08:00:44.316Z command-start: \"manual-byte-comparison\"\n- 2026-10-16T08:00:44.321Z command-result: \"manual-byte-comparison\"\n- 2026-10-16T08:00:44.322Z command-start: \"complete-migration\"\n- 2026-10-16T08:00:44.335Z command-result: \"complete-migration\"\n- 2026-10-16T08:00:44.337Z command-start: \"complete-rerun\"\n- 2026-10-16T08:00:44.350Z command-result: \"complete-rerun\"\n- 2026-10-16T08:00:44.351Z command-start: \"idempotence-comparison\"\n- 2026-10-16T08:00:44.356Z command-result: \"idempotence-comparison\"\n- 2026-10-16T08:00:44.358Z independent-output-assertions: {\"sixExpectedManifestBytes\":true,\"notesScopeAndV2Unchanged\":true,\"completeTreeIdempotent\":true}\n- 2026-10-16T08:00:44.358Z command-start: \"negative-unknown\"\n- 2026-10-16T08:00:44.370Z command-result: \"negative-unknown\"\n- 2026-10-16T08:00:44.370Z negative-file-preserved: {\"variant\":\"unknown\",\"bytes\":\"{\\\"version\\\":9}\\n\"}\n- 2026-10-16T08:00:44.370Z command-start: \"negative-malformed\"\n- 2026-10-16T08:00:44.381Z command-result: \"negative-malformed\"\n- 2026-10-16T08:00:44.381Z negative-file-preserved: {\"variant\":\"malformed\",\"bytes\":\"{\"}\n- 2026-10-16T08:00:44.382Z command-start: \"negative-invalid-fields\"\n- 2026-10-16T08:00:44.395Z command-result: \"negative-invalid-fields\"\n- 2026-10-16T08:00:44.396Z negative-file-preserved: {\"variant\":\"invalid-fields\",\"bytes\":\"{\\\"version\\\":1,\\\"key\\\":\\\"bad\\\",\\\"label\\\":\\\"Bad\\\",\\\"enabled\\\":\\\"yes\\\"}\\n\"}\n- 2026-10-16T08:00:44.396Z proof-complete: \"All executed comparisons and semantic assertions completed without an exception. No commit.\"\n- 2026-10-16T08:02:37.235Z variant-text-captured: {\"full\":\"executed actual workflow\",\"reduced\":\"simulated text only\",\"blocked\":\"simulated text only\",\"hostNegativeVariants\":\"unexercised\"}\n- 2026-10-16T08:02:37.235Z command-start: \"pristine-integrity\"\n- 2026-10-16T08:02:37.242Z command-result: \"pristine-integrity\"\n\n## Command results\n\n| Command record | Exit | Artifact |\n|---|---:|---|\n| first-unit-execution | 0 | [first-unit-execution.json](repeatable-change/first-unit-execution.json) |\n| manual-byte-comparison | 0 | [manual-byte-comparison.json](repeatable-change/manual-byte-comparison.json) |\n| complete-migration | 0 | [complete-migration.json](repeatable-change/complete-migration.json) |\n| complete-rerun | 0 | [complete-rerun.json](repeatable-change/complete-rerun.json) |\n| idempotence-comparison | 0 | [idempotence-comparison.json](repeatable-change/idempotence-comparison.json) |\n| negative-unknown | 1 | [negative-unknown.json](repeatable-change/negative-unknown.json) |\n| negative-malformed | 1 | [negative-malformed.json](repeatable-change/negative-malformed.json) |\n| negative-invalid-fields | 1 | [negative-invalid-fields.json](repeatable-change/negative-invalid-fields.json) |\n| pristine-integrity | 0 | [pristine-integrity.json](repeatable-change/pristine-integrity.json) |\n\nA diff exit of 1 in implementation-diff means changes were found. The migration legacy-reference-search exit of 1 means no matches. Phase-3-static exit of 2 is the observed planned temporary compiler failure. Negative manifest exits of 1 are observed rejection paths.\n\n### first-unit-execution\n\n```json\n{\n  \"label\": \"first-unit-execution\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"first-unit/search.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"migrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/first-unit/search.json\\n{\\\"scanned\\\":1,\\\"changed\\\":1}\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### manual-byte-comparison\n\n```json\n{\n  \"label\": \"manual-byte-comparison\",\n  \"argv\": [\n    \"diff\",\n    \"-u\",\n    \"manual/search.json\",\n    \"first-unit/search.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### complete-migration\n\n```json\n{\n  \"label\": \"complete-migration\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"work/manifests\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"migrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/export.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/search.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json\\n{\\\"scanned\\\":7,\\\"changed\\\":6}\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### complete-rerun\n\n```json\n{\n  \"label\": \"complete-rerun\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"work/manifests\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"unchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/export.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/search.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json\\n{\\\"scanned\\\":7,\\\"changed\\\":0}\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### idempotence-comparison\n\n```json\n{\n  \"label\": \"idempotence-comparison\",\n  \"argv\": [\n    \"diff\",\n    \"-u\",\n    \"before-rerun-sha256.json\",\n    \"after-rerun-sha256.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### negative-unknown\n\n```json\n{\n  \"label\": \"negative-unknown\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"negative/unknown/input.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/unknown/input.json: unknown manifest version\\n\"\n}\n```\n\n### negative-malformed\n\n```json\n{\n  \"label\": \"negative-malformed\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"negative/malformed/input.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/malformed/input.json: JSON Parse error: Expected '}'\\n\"\n}\n```\n\n### negative-invalid-fields\n\n```json\n{\n  \"label\": \"negative-invalid-fields\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"negative/invalid-fields/input.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/invalid-fields/input.json: malformed manifest fields\\n\"\n}\n```\n\n### pristine-integrity\n\n```json\n{\n  \"label\": \"pristine-integrity\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/repeatable-change\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/pristine\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n## Reviewable artifacts\n\nFinal files are in [repeatable-change/work/](repeatable-change/work/), originals in [repeatable-change/pristine/](repeatable-change/pristine/). Case scripts and exact result JSON files remain in [repeatable-change/](repeatable-change/). Source and script digests are in [artifact-sha256.json](repeatable-change/artifact-sha256.json). The full ordered run is retained in [chronology.jsonl](chronology.jsonl), with a case-only copy in [repeatable-change/chronology.jsonl](repeatable-change/chronology.jsonl). The shared runner is [evaluate.mjs](evaluate.mjs). Scripts that create baselines or the hand-authored first unit are historical setup steps and should not be replayed over the completed evidence. Rerun tests in work/, and rerun the manifest tool directly on work/manifests.\n",
        "artifact": {
          "path": "fixtures/rerun-02/repeatable-change.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change.result.md",
          "sha256": "2ec9df3d473d1e47150bf1ab66acdc19918f8cce6d8fcfc408cdaad8f6322cdb",
          "bytes": 18661
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/rerun-02.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/rerun-02.events.jsonl",
            "sha256": "f42579b80cc8800de7c5cbaa7b9672abc9b54a90e1b758077ff5f6dd2d9dd5d4",
            "bytes": 344099,
            "eventReferences": [
              {
                "eventId": "item_5",
                "line": 9,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "04a376697453a87164e5f798d5181f0cd76387bbb438108f1b08bda80e43fe09"
              },
              {
                "eventId": "item_5",
                "line": 10,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d8fbcecc8ccafb95693f891d69d121edd338ad2dd05cee59e2186a6cdc0a2221",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_8",
                "line": 14,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f2e50701fce53933b7c90be3457ee3bba2b52653d1dbcbf0c6d0d9048aac0357"
              },
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4b73f1027ec2d891bf72350790c23be825e009773859c0a913893a4554b8a821",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_9",
                "line": 16,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "b75b94e21f05d5426e1c676534c3c20ffdc9d699edafa9004405fac492709d71"
              },
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "e601b055bb8074a2e06a2a1ae069f76306e5d919ec59b7843d6974d3995121f9",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_16",
                "line": 29,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "857d190c2e84870efd52e391e967680058404b1c9da0d017bc0cc183a106c430"
              },
              {
                "eventId": "item_16",
                "line": 30,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c4a4389a9b819453756f97e99b607666a41542f933a97840522e11ccec46055f",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_18",
                "line": 32,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3df241a6f45fbd2fba2029663b42ce355fd2d372be626da3bee3dc7809e28d22"
              },
              {
                "eventId": "item_18",
                "line": 33,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "90bf14b962ca3484f0c82d56ab14c5c7d813aa72faafbadd4aa5af2f14d72d1d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_20",
                "line": 36,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "d130a6134486687279747d3f08335c12fb5e182ca7a6e4caad0081d4603f80a2"
              },
              {
                "eventId": "item_20",
                "line": 37,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "9523054f1016b78e0c8781fe43bf09517257aa0f3558b82c122b45eae3bb82ea",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_22",
                "line": 39,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "e581af9df8ff8d256f76f52a77e05243fb7bc880cc854c8c04fd00a949dbbe9f"
              },
              {
                "eventId": "item_22",
                "line": 40,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "2fc24daebccecbdd9df6e5c95ee0a46be8cf72b416f5792f7c3c0dda21516d94",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/rerun-02/repeatable-change/manual-byte-comparison.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/manual-byte-comparison.json",
            "sha256": "b314107f630d5807cda9337f3e7f592b17a126a8b66177217b425c016b3dc79e",
            "bytes": 255
          },
          {
            "path": "fixtures/rerun-02/repeatable-change/complete-migration.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/complete-migration.json",
            "sha256": "a3df19ac121d0c921514349d088a78b8123429d43f728979a442402614dddc09",
            "bytes": 1242
          },
          {
            "path": "fixtures/rerun-02/repeatable-change/complete-rerun.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/complete-rerun.json",
            "sha256": "1b8fd11702ee04ae37461da1a75a7b6d2bf0375b556ecde7d6f1af18f23e63e9",
            "bytes": 1248
          },
          {
            "path": "fixtures/rerun-02/repeatable-change/idempotence-comparison.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/idempotence-comparison.json",
            "sha256": "f6c222a89685a1dde760983c117211c44fe063ea54f9d43b8c7df802b6709f00",
            "bytes": 262
          },
          {
            "path": "fixtures/rerun-02/repeatable-change/negative-unknown.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative-unknown.json",
            "sha256": "88bab8d94b00cc318e193bccaf0c5d7a3da58fffe89110c6aee8d5705c814731",
            "bytes": 394
          },
          {
            "path": "fixtures/rerun-02/repeatable-change/negative-malformed.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative-malformed.json",
            "sha256": "81c30d5ed4428f64c70a2246e91556963ac5b6dbf4968422c5dcb1e6fa219a60",
            "bytes": 404
          },
          {
            "path": "fixtures/rerun-02/repeatable-change/negative-invalid-fields.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative-invalid-fields.json",
            "sha256": "d8640c4050b59bb0e3e06652d0a79a4c7e835d9069b210730adf702fd26032d1",
            "bytes": 409
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_5",
            "item_8",
            "item_9"
          ],
          "actualExecutionEventIds": [
            "item_16",
            "item_18",
            "item_20",
            "item_22"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-03/repeatable-change/check.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/check.mjs",
      "sha256": "2b1bcfd475687a9685ca9d1aef4167247e6efc89d52814e6aece0515abd27dc9",
      "bytes": 678,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "import assert from 'node:assert/strict';\nconst root = new URL('./',import.meta.url).pathname;\nconst records=await Bun.file(root+'input/orders.json').json();\nfor(const record of records) {\n  const got=await Bun.file(root+`output/${record.id}.json`).json();\n  assert.equal(got.totalAmount,record.total);\n  assert.equal(got.schemaVersion,2);\n  assert.ok(!('total' in got));\n  for(const key of ['id','status','customer'])assert.equal(got[key],record[key]);\n}\nassert.equal(await Bun.file(root+'manual/1.json').text(),await Bun.file(root+'output/1.json').text());\nconsole.log('Three records preserve id, status, customer and numeric total. First-unit bytes equal manual reference.');\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/comparison.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/comparison.command.json",
      "sha256": "3583b1fbd3d3779186fee37e2e5a29dc742900115604efe6bb73a481221ac6ec",
      "bytes": 292,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"label\": \"comparison\",\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"repeatable-change/check.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"Three records preserve id, status, customer and numeric total. First-unit bytes equal manual reference.\\n\",\n  \"stderr\": \"\",\n  \"expectedExitCode\": 0\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/idempotence.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/idempotence.json",
      "sha256": "653a57897d9b9d22c1f8dec478df745de5506bbee9e9f058d1ef6d91a1698e46",
      "bytes": 73,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"rerunBytesEqual\": true,\n  \"v2InputBytesEqual\": true,\n  \"files\": 3\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/invalid/bad.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/invalid/bad.json",
      "sha256": "b5868873d5865d04404625f5d7c0108c7fd1146061910eb083ebbdb26dcf969a",
      "bytes": 23,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\"id\":99,\"total\":\"bad\"}"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/invalid-rejection.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/invalid-rejection.json",
      "sha256": "a83470baa2a6ddac1ed5ae2ccc8f74f875bb8c9c1edffa74096d31b814261b0c",
      "bytes": 29,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\"invalidOutputAbsent\":true}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/legacy/1.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/legacy/1.json",
      "sha256": "2fc50d23ce81e39cfe6e87fd7d3565ef9c70484ba25a90a19c3699d48dc4bb54",
      "bytes": 78,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 1,\n  \"status\": \"open\",\n  \"customer\": \"Ada, Inc.\",\n  \"total\": 12.5\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/legacy/2.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/legacy/2.json",
      "sha256": "fddd3ce33e8cb38389fe4777f5c4fc9af472b417d2948f9c77f2b0dd7211da2f",
      "bytes": 74,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 2,\n  \"status\": \"closed\",\n  \"customer\": \"Hidden\",\n  \"total\": 4\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/legacy/3.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/legacy/3.json",
      "sha256": "0e24628b5d6c51a65a5728ed82ab6f4fe74e7105543753e7c144a92a1db33b4e",
      "bytes": 76,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 3,\n  \"status\": \"open\",\n  \"customer\": \"Say \\\"Hi\\\"\",\n  \"total\": 0\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/manual/1.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/manual/1.json",
      "sha256": "174cfed4db346e7448a6330b81b6c878bee858a43d98a8662207c3471f1ed681",
      "bytes": 106,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 1,\n  \"status\": \"open\",\n  \"customer\": \"Ada, Inc.\",\n  \"totalAmount\": 12.5,\n  \"schemaVersion\": 2\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/migrate.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/migrate.mjs",
      "sha256": "f036b6270c52404572c3128dbdf7a3f1235fd23c34053451d9b3fa6553f06808",
      "bytes": 1230,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "import { mkdir, readdir, rename } from 'node:fs/promises';\nimport { resolve } from 'node:path';\nconst [input, output] = process.argv.slice(2);\nif (!input || !output || resolve(input)===resolve(output)) throw new Error('Provide distinct input and output directories');\nconst names = (await readdir(input)).filter(name=>name.endsWith('.json')).sort();\nconst converted=[];\nfor(const name of names) {\n  const record=await Bun.file(resolve(input,name)).json();\n  const current=record.schemaVersion===2;\n  const {total,...rest}=record;\n  if(current) {\n    if('total' in record || !Number.isFinite(record.totalAmount)) throw new Error(`Invalid v2 ${name}`);\n  } else if(record.schemaVersion!==undefined || !Number.isFinite(total) || 'totalAmount' in record) {\n    throw new Error(`Invalid legacy ${name}`);\n  }\n  converted.push([name,current?record:{...rest,totalAmount:total,schemaVersion:2}]);\n}\nawait mkdir(output,{recursive:true});\nfor(const [name,record] of converted) {\n  const destination=resolve(output,name);\n  await Bun.write(destination+'.tmp',JSON.stringify(record,null,2)+'\\n');\n  await rename(destination+'.tmp',destination);\n}\nconsole.log(JSON.stringify({processed:converted.length,files:converted.map(([name])=>name)}));\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/migration-first.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/migration-first.command.json",
      "sha256": "9dc919b699c4c949edc47120560e73088e24b958b5ca28c526e06e1815fd6922",
      "bytes": 322,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"label\": \"migration-first\",\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"repeatable-change/migrate.mjs\",\n    \"repeatable-change/legacy\",\n    \"repeatable-change/output\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"processed\\\":3,\\\"files\\\":[\\\"1.json\\\",\\\"2.json\\\",\\\"3.json\\\"]}\\n\",\n  \"stderr\": \"\",\n  \"expectedExitCode\": 0\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/migration-rerun.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/migration-rerun.command.json",
      "sha256": "ea4fba4bb184828eaad0c0e2fa21a120500c64b934af38064aada250d0031fba",
      "bytes": 322,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"label\": \"migration-rerun\",\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"repeatable-change/migrate.mjs\",\n    \"repeatable-change/legacy\",\n    \"repeatable-change/output\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"processed\\\":3,\\\"files\\\":[\\\"1.json\\\",\\\"2.json\\\",\\\"3.json\\\"]}\\n\",\n  \"stderr\": \"\",\n  \"expectedExitCode\": 0\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/migration-v2-input.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/migration-v2-input.command.json",
      "sha256": "1d4991cc966a0425f966f38e323d59c4738461d81b656a2a12dfe229b3e3917e",
      "bytes": 328,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"label\": \"migration-v2-input\",\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"repeatable-change/migrate.mjs\",\n    \"repeatable-change/output\",\n    \"repeatable-change/v2-output\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"processed\\\":3,\\\"files\\\":[\\\"1.json\\\",\\\"2.json\\\",\\\"3.json\\\"]}\\n\",\n  \"stderr\": \"\",\n  \"expectedExitCode\": 0\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/output/1.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/output/1.json",
      "sha256": "174cfed4db346e7448a6330b81b6c878bee858a43d98a8662207c3471f1ed681",
      "bytes": 106,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 1,\n  \"status\": \"open\",\n  \"customer\": \"Ada, Inc.\",\n  \"totalAmount\": 12.5,\n  \"schemaVersion\": 2\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/output/2.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/output/2.json",
      "sha256": "a8b65003142bf7f376dd43ae6195f6aeb511b33a7235ed2e6a1c32831c0ff53d",
      "bytes": 102,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 2,\n  \"status\": \"closed\",\n  \"customer\": \"Hidden\",\n  \"totalAmount\": 4,\n  \"schemaVersion\": 2\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/output/3.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/output/3.json",
      "sha256": "3e4d74ab0b02b30d8be21d816c6bda06500999832885f7ae6f5435ae4c05cc33",
      "bytes": 104,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 3,\n  \"status\": \"open\",\n  \"customer\": \"Say \\\"Hi\\\"\",\n  \"totalAmount\": 0,\n  \"schemaVersion\": 2\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/reject-invalid.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/reject-invalid.command.json",
      "sha256": "8fd7a9ae4222dd286b14b90e49fc6a41e383742d02c80ff5811cc8e4dc06975b",
      "bytes": 854,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"label\": \"reject-invalid\",\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"repeatable-change/migrate.mjs\",\n    \"repeatable-change/invalid\",\n    \"repeatable-change/rejected-output\"\n  ],\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \" 9 |   const current=record.schemaVersion===2;\\n10 |   const {total,...rest}=record;\\n11 |   if(current) {\\n12 |     if('total' in record || !Number.isFinite(record.totalAmount)) throw new Error(`Invalid v2 ${name}`);\\n13 |   } else if(record.schemaVersion!==undefined || !Number.isFinite(total) || 'totalAmount' in record) {\\n14 |     throw new Error(`Invalid legacy ${name}`);\\n                   ^\\nerror: Invalid legacy bad.json\\n      at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/migrate.mjs:14:15\\n\\nBun v1.4.2 (macOS arm64)\\n\",\n  \"expectedExitCode\": 1\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/response.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/response.md",
      "sha256": "7d26cbfe3b0ee5f31addc175bc9c112d5606adc2c55376e392e926af7c3fc184",
      "bytes": 2439,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "Built and executed migrate.mjs, a deterministic JSON migration tool. The copied orders fixture was split into three synthetic legacy files. The chosen target renames total to totalAmount and adds schemaVersion 2, preserving all other supplied fields and numeric values. This target is a local evaluation choice, not a supplied production schema.\n\nThe manual first-unit reference is manual/1.json. The initial tool file was authored before that reference was materialized; the reference was written before the first migration execution. Thus the run proves independent literal-reference equivalence and rerunnability, but does not demonstrate the skill's ideal hand-first-before-tool-authoring chronology. This limitation is explicit rather than reconstructed as a prior action.\n\nActual execution and proof:\n\n| Command receipt | Observed result |\n| --- | --- |\n| migration-first.command.json | Processed 1.json, 2.json and 3.json, exit 0. |\n| comparison.command.json | Literal first-unit bytes matched the manual reference. All 3 records preserved id, status, customer and total value; no legacy total remained. Exit 0. |\n| migration-rerun.command.json | Reprocessed all 3 legacy files, exit 0. Coordinator compared before/after bytes and found no change. |\n| migration-v2-input.command.json | Accepted already-migrated records into a separate output directory, exit 0. Coordinator compared all output bytes and found no change. |\n| reject-invalid.command.json | Rejected a nonnumeric total with exit 1 and exact diagnostic. No invalid output was produced, as checked by coordinator. |\n\nThe tool prevalidates the batch before writing, rejects conflicting schema shapes, sorts filenames, and uses temporary-file rename per output. Writes are limited to caller-selected directories. Its current CLI trusts authorized local paths; it is not an untrusted-input sandbox. Per-file atomic replacement is not transactionality across a whole batch or crash durability. No crash or concurrent-writer test was performed. Rerunning converges under the observed normal execution conditions.\n\nVariants attempted: first migration, repeat of legacy input, already-v2 input, invalid input. The deterministic tool processed every unit, so no workers were needed. Source, writes and execution were available. Tool, manual reference, input/output files, stdout/stderr, exit statuses and equality observations are saved. Commits were forbidden and unperformed.\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/supplied-input.json",
      "sha256": "e9c35486d8189a16c804f94c544a7301c38d1b37a24d07475686a0b0742cda70",
      "bytes": 1739,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"id\": \"repeatable-change\",\n  \"sourcePaths\": [\n    \"skills/principle-build-the-lever/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.\",\n  \"requirements\": [\n    \"Source reads; authorized artifact writes and execution for full proof.\",\n    \"Independent workers require exposed worker tools and user authorization; they are unnecessary when a deterministic tool processes all units.\"\n  ],\n  \"expectedFull\": \"Produce the smallest safe rerunnable tool as a file; learn the recipe on a first unit, rerun and diff it against the hand-done result, and report observed commands and outputs. Retain the tool for review and commit only with authorization when work outlives the session.\",\n  \"expectedReduced\": \"When writes or execution are unavailable, propose the tool and verification recipe as reduced capability, distinguish the proposal from a saved artifact and executed proof, and state the missing capabilities.\",\n  \"expectedBlocked\": \"If source is unavailable or denied, state that the recipe and equivalence cannot be verified; request the required source or capability without claiming implementation or proof.\",\n  \"forbiddenClaims\": [\n    \"A proposed tool was saved, run or verified without observed evidence.\",\n    \"Hand-applied changes alone satisfy the principle.\",\n    \"Sequential work proves independent workers.\",\n    \"Invocation grants commit, delegation or external-action permission.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/v2-output/1.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/v2-output/1.json",
      "sha256": "174cfed4db346e7448a6330b81b6c878bee858a43d98a8662207c3471f1ed681",
      "bytes": 106,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 1,\n  \"status\": \"open\",\n  \"customer\": \"Ada, Inc.\",\n  \"totalAmount\": 12.5,\n  \"schemaVersion\": 2\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/v2-output/2.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/v2-output/2.json",
      "sha256": "a8b65003142bf7f376dd43ae6195f6aeb511b33a7235ed2e6a1c32831c0ff53d",
      "bytes": 102,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 2,\n  \"status\": \"closed\",\n  \"customer\": \"Hidden\",\n  \"totalAmount\": 4,\n  \"schemaVersion\": 2\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/v2-output/3.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/v2-output/3.json",
      "sha256": "3e4d74ab0b02b30d8be21d816c6bda06500999832885f7ae6f5435ae4c05cc33",
      "bytes": 104,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "{\n  \"id\": 3,\n  \"status\": \"open\",\n  \"customer\": \"Say \\\"Hi\\\"\",\n  \"totalAmount\": 0,\n  \"schemaVersion\": 2\n}\n"
    },
    {
      "path": "fixtures/batch-03/repeatable-change.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change.result.md",
      "sha256": "c58888c375faf95981df782a3a3c0b6abc540a6a2e080dd3392d37c197e8f189",
      "bytes": 9378,
      "owners": [
        "grades-native-03.json#7"
      ],
      "text": "# repeatable-change\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"repeatable-change\",\n  \"prompt\": \"Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.\",\n  \"requirements\": [\n    \"Source reads; authorized artifact writes and execution for full proof.\",\n    \"Independent workers require exposed worker tools and user authorization; they are unnecessary when a deterministic tool processes all units.\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-build-the-lever/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 5. See [source-reads.json](repeatable-change/source-reads.json). Supplied input archive: [supplied-input.json](repeatable-change/supplied-input.json).\n\n## Actual response and variants\n\nBuilt and executed migrate.mjs, a deterministic JSON migration tool. The copied orders fixture was split into three synthetic legacy files. The chosen target renames total to totalAmount and adds schemaVersion 2, preserving all other supplied fields and numeric values. This target is a local evaluation choice, not a supplied production schema.\n\nThe manual first-unit reference is manual/1.json. The initial tool file was authored before that reference was materialized; the reference was written before the first migration execution. Thus the run proves independent literal-reference equivalence and rerunnability, but does not demonstrate the skill's ideal hand-first-before-tool-authoring chronology. This limitation is explicit rather than reconstructed as a prior action.\n\nActual execution and proof:\n\n| Command receipt | Observed result |\n| --- | --- |\n| migration-first.command.json | Processed 1.json, 2.json and 3.json, exit 0. |\n| comparison.command.json | Literal first-unit bytes matched the manual reference. All 3 records preserved id, status, customer and total value; no legacy total remained. Exit 0. |\n| migration-rerun.command.json | Reprocessed all 3 legacy files, exit 0. Coordinator compared before/after bytes and found no change. |\n| migration-v2-input.command.json | Accepted already-migrated records into a separate output directory, exit 0. Coordinator compared all output bytes and found no change. |\n| reject-invalid.command.json | Rejected a nonnumeric total with exit 1 and exact diagnostic. No invalid output was produced, as checked by coordinator. |\n\nThe tool prevalidates the batch before writing, rejects conflicting schema shapes, sorts filenames, and uses temporary-file rename per output. Writes are limited to caller-selected directories. Its current CLI trusts authorized local paths; it is not an untrusted-input sandbox. Per-file atomic replacement is not transactionality across a whole batch or crash durability. No crash or concurrent-writer test was performed. Rerunning converges under the observed normal execution conditions.\n\nVariants attempted: first migration, repeat of legacy input, already-v2 input, invalid input. The deterministic tool processed every unit, so no workers were needed. Source, writes and execution were available. Tool, manual reference, input/output files, stdout/stderr, exit statuses and equality observations are saved. Commits were forbidden and unperformed.\n\n## Real command results\n\n```\n[\n  {\n    \"artifact\": \"repeatable-change/comparison.command.json\",\n    \"label\": \"comparison\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/check.mjs\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"Three records preserve id, status, customer and numeric total. First-unit bytes equal manual reference.\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"repeatable-change/migration-first.command.json\",\n    \"label\": \"migration-first\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/migrate.mjs\",\n      \"repeatable-change/legacy\",\n      \"repeatable-change/output\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"processed\\\":3,\\\"files\\\":[\\\"1.json\\\",\\\"2.json\\\",\\\"3.json\\\"]}\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"repeatable-change/migration-rerun.command.json\",\n    \"label\": \"migration-rerun\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/migrate.mjs\",\n      \"repeatable-change/legacy\",\n      \"repeatable-change/output\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"processed\\\":3,\\\"files\\\":[\\\"1.json\\\",\\\"2.json\\\",\\\"3.json\\\"]}\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"repeatable-change/migration-v2-input.command.json\",\n    \"label\": \"migration-v2-input\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/migrate.mjs\",\n      \"repeatable-change/output\",\n      \"repeatable-change/v2-output\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"processed\\\":3,\\\"files\\\":[\\\"1.json\\\",\\\"2.json\\\",\\\"3.json\\\"]}\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"repeatable-change/reject-invalid.command.json\",\n    \"label\": \"reject-invalid\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"repeatable-change/migrate.mjs\",\n      \"repeatable-change/invalid\",\n      \"repeatable-change/rejected-output\"\n    ],\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \" 9 |   const current=record.schemaVersion===2;\\n10 |   const {total,...rest}=record;\\n11 |   if(current) {\\n12 |     if('total' in record || !Number.isFinite(record.totalAmount)) throw new Error(`Invalid v2 ${name}`);\\n13 |   } else if(record.schemaVersion!==undefined || !Number.isFinite(total) || 'totalAmount' in record) {\\n14 |     throw new Error(`Invalid legacy ${name}`);\\n                   ^\\nerror: Invalid legacy bad.json\\n      at /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/repeatable-change/migrate.mjs:14:15\\n\\nBun v1.4.2 (macOS arm64)\\n\",\n    \"expectedExitCode\": 1\n  }\n]\n```\n\n## Artifacts\n\n- [repeatable-change/check.mjs](repeatable-change/check.mjs)\n- [repeatable-change/comparison.command.json](repeatable-change/comparison.command.json)\n- [repeatable-change/idempotence.json](repeatable-change/idempotence.json)\n- [repeatable-change/input/orders.json](repeatable-change/input/orders.json)\n- [repeatable-change/invalid-rejection.json](repeatable-change/invalid-rejection.json)\n- [repeatable-change/invalid/bad.json](repeatable-change/invalid/bad.json)\n- [repeatable-change/legacy/1.json](repeatable-change/legacy/1.json)\n- [repeatable-change/legacy/2.json](repeatable-change/legacy/2.json)\n- [repeatable-change/legacy/3.json](repeatable-change/legacy/3.json)\n- [repeatable-change/manual/1.json](repeatable-change/manual/1.json)\n- [repeatable-change/migrate.mjs](repeatable-change/migrate.mjs)\n- [repeatable-change/migration-first.command.json](repeatable-change/migration-first.command.json)\n- [repeatable-change/migration-rerun.command.json](repeatable-change/migration-rerun.command.json)\n- [repeatable-change/migration-v2-input.command.json](repeatable-change/migration-v2-input.command.json)\n- [repeatable-change/output/1.json](repeatable-change/output/1.json)\n- [repeatable-change/output/2.json](repeatable-change/output/2.json)\n- [repeatable-change/output/3.json](repeatable-change/output/3.json)\n- [repeatable-change/reject-invalid.command.json](repeatable-change/reject-invalid.command.json)\n- [repeatable-change/response.md](repeatable-change/response.md)\n- [repeatable-change/source-reads.json](repeatable-change/source-reads.json)\n- [repeatable-change/supplied-input.json](repeatable-change/supplied-input.json)\n- [repeatable-change/v2-output/1.json](repeatable-change/v2-output/1.json)\n- [repeatable-change/v2-output/2.json](repeatable-change/v2-output/2.json)\n- [repeatable-change/v2-output/3.json](repeatable-change/v2-output/3.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/after-rerun-sha256.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/after-rerun-sha256.json",
      "sha256": "3e364d78fc3b8642d24f1b97a533758a148c732e3f8cc962bacea20b25367e80",
      "bytes": 876,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"manifests/admin/audit.json\": \"979b1fcb8ef17e6bcbc2f7d8be9447207bb595efce09e2a9318555709c3291c1\",\n  \"manifests/admin/team.json\": \"be497301b6eb8a67153a754926bc98906913eab6823e37d784390a6a9cad34dc\",\n  \"manifests/core/already-v2.json\": \"e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef\",\n  \"manifests/core/export.json\": \"d9e651b812edef7cd3d5530475b1405ac889f652f177ebb92e1aa2f94cc3deb7\",\n  \"manifests/core/search.json\": \"8eb2eedf290ce4df97b6fb12de796cd74788f4871212feafec138be06545ad74\",\n  \"manifests/mobile/alerts.json\": \"24138ac519edc807247edce3f204d9bfdcb6f49cdc57955f5b581b27cfbbeb6e\",\n  \"manifests/mobile/offline.json\": \"f51840cd7f3df4a14b0aaef0f31331ce9acf7f51954773ae26794258cb59b62f\",\n  \"notes.txt\": \"81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe\",\n  \"scope.md\": \"caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/artifact-sha256.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/artifact-sha256.json",
      "sha256": "2aedbd6b6ee383a1e7e56abbd0610ada5479dc38a9a8088a820bedb4873df0be",
      "bytes": 447,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"prove.mjs\": \"2a00551576d2fdcfc46505295ee0d8529338ecda17211b75c192890121512f64\",\n  \"supplied-contract.json\": \"d079f1cfe4c1d1d42d1a86f1c5fd32133d662a6e39f21ed80862c550dfe21bf3\",\n  \"source-reads.txt\": \"6bbfa3e022eb2ea5d076f4b383d58de497395467073b70bcc21ce63404d8a0a1\",\n  \"manual-first.mjs\": \"ba956db3b4f093d813b3e9f0c9459546924ef50b806cd9ace77e45a2a08e57b3\",\n  \"migrate.mjs\": \"0e7abaca9765bb501834cdd62985492ebe4d76b8c7a63ffe5a55dc0bdd95dd06\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/before-rerun-sha256.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/before-rerun-sha256.json",
      "sha256": "3e364d78fc3b8642d24f1b97a533758a148c732e3f8cc962bacea20b25367e80",
      "bytes": 876,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"manifests/admin/audit.json\": \"979b1fcb8ef17e6bcbc2f7d8be9447207bb595efce09e2a9318555709c3291c1\",\n  \"manifests/admin/team.json\": \"be497301b6eb8a67153a754926bc98906913eab6823e37d784390a6a9cad34dc\",\n  \"manifests/core/already-v2.json\": \"e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef\",\n  \"manifests/core/export.json\": \"d9e651b812edef7cd3d5530475b1405ac889f652f177ebb92e1aa2f94cc3deb7\",\n  \"manifests/core/search.json\": \"8eb2eedf290ce4df97b6fb12de796cd74788f4871212feafec138be06545ad74\",\n  \"manifests/mobile/alerts.json\": \"24138ac519edc807247edce3f204d9bfdcb6f49cdc57955f5b581b27cfbbeb6e\",\n  \"manifests/mobile/offline.json\": \"f51840cd7f3df4a14b0aaef0f31331ce9acf7f51954773ae26794258cb59b62f\",\n  \"notes.txt\": \"81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe\",\n  \"scope.md\": \"caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/capability-bindings.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/capability-bindings.json",
      "sha256": "294304b4a5b93d9bf26f3f9288cc13a100c14cb9c1f44b6881fc576e4b178c23",
      "bytes": 1542,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "[\n  {\n    \"operation\": \"read\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"repeatable-change/source-reads.txt\",\n    \"limits\": \"Actual cat reads and Bun file reads. Only the specified installed package root was used.\"\n  },\n  {\n    \"operation\": \"isolated-write\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"repeatable-change/work\",\n    \"limits\": \"Owned case directory only. No external writes.\"\n  },\n  {\n    \"operation\": \"execution\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"repeatable-change/chronology.jsonl\",\n    \"limits\": \"Bun scripts, Bun compiler execution and local commands only.\"\n  },\n  {\n    \"operation\": \"persistence\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"repeatable-change/artifact-sha256.json\",\n    \"limits\": \"Saved files read back and hashed within current session. No cross-session recovery tested.\"\n  },\n  {\n    \"operation\": \"spawn\",\n    \"tool\": \"collaboration.spawn_agent\",\n    \"exposed\": true,\n    \"succeeded\": false,\n    \"evidence\": null,\n    \"limits\": \"Not attempted. Direct deterministic completion requires no workers.\"\n  },\n  {\n    \"operation\": \"external-write\",\n    \"tool\": null,\n    \"exposed\": false,\n    \"succeeded\": false,\n    \"evidence\": null,\n    \"limits\": \"Forbidden by user and not attempted. No live service contacted.\"\n  }\n]\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/capability-variants.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/capability-variants.md",
      "sha256": "8ffc529201422c6aceff9ada4c47f0ac17731a54bb2077e8bc16abee6bb5c6d1",
      "bytes": 1370,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "# Capability variants\n\n## Reduced proposal, simulated only\n\nSimulated missing writes or execution. Proposed tool: a Bun script that traverses manifests/**/*.json, validates version and fields, renames the v1 fields in the required order, preserves tags and leaves v2 bytes untouched. First hand-transform search.json, then generate from a separate pristine copy, diff the bytes, migrate the owned tree, snapshot bytes and rerun to prove idempotence. Under this simulated restriction no tool was saved, run or verified. The actual-host tool belongs to the separate executed variant.\n\n## Missing prerequisite response, simulated only\n\nSimulated missing source. Without the source manifests and recipe, do not claim a verified transformation or equivalence. Required inputs are the v1/v2 schema, formatting rules, file scope and a pristine first unit. In the actual host these inputs were available; this text does not prove a denied read.\n\nNo host-enforced negative-capability branch was exercised. The host supplied readable source, authorized isolated writes and execution. Configuration changes to manufacture denials were forbidden. Actual denied reads, denied writes and unavailable execution remain unexercised. These fallback texts were captured by the coordinator, not executed in a restricted worker. disable-model-invocation metadata enforcement was not tested.\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/chronology.jsonl",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/chronology.jsonl",
      "sha256": "876e583ca6471680bb2a1904cd82d575012e3651a54d1ebfd70e646c14db0e4d",
      "bytes": 10911,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\"time\":\"2026-10-16T07:59:06.415Z\",\"caseId\":\"repeatable-change\",\"action\":\"setup\",\"detail\":{\"sourceRoot\":\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\"scenario\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/repeatable-change\",\"copies\":[\"pristine\",\"work\"],\"sourceReads\":\"source-reads.txt\"}}\n{\"time\":\"2026-10-16T08:00:02.662Z\",\"caseId\":\"repeatable-change\",\"action\":\"manual-start\",\"detail\":\"Copied original into manual/search.json and first-unit/search.json. No migration tool exists yet.\"}\n{\"time\":\"2026-10-16T08:00:02.663Z\",\"caseId\":\"repeatable-change\",\"action\":\"manual-result\",\"detail\":{\"file\":\"manual/search.json\",\"method\":\"literal hand-authored transformation, not generated from input\",\"bytes\":\"{\\n  \\\"version\\\": 2,\\n  \\\"id\\\": \\\"search\\\",\\n  \\\"displayName\\\": \\\"Search\\\",\\n  \\\"status\\\": \\\"enabled\\\",\\n  \\\"tags\\\": [\\n    \\\"core\\\",\\n    \\\"user\\\"\\n  ]\\n}\\n\"}}\n{\"time\":\"2026-10-16T08:00:44.304Z\",\"caseId\":\"repeatable-change\",\"action\":\"tool-written\",\"detail\":{\"file\":\"migrate.mjs\",\"manualAlreadyExists\":true}}\n{\"time\":\"2026-10-16T08:00:44.304Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-start\",\"detail\":{\"label\":\"first-unit-execution\",\"argv\":[\"bun\",\"migrate.mjs\",\"first-unit/search.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\"}}\n{\"time\":\"2026-10-16T08:00:44.316Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-result\",\"detail\":{\"label\":\"first-unit-execution\",\"argv\":[\"bun\",\"migrate.mjs\",\"first-unit/search.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\"exitCode\":0,\"stdout\":\"migrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/first-unit/search.json\\n{\\\"scanned\\\":1,\\\"changed\\\":1}\\n\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T08:00:44.316Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-start\",\"detail\":{\"label\":\"manual-byte-comparison\",\"argv\":[\"diff\",\"-u\",\"manual/search.json\",\"first-unit/search.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\"}}\n{\"time\":\"2026-10-16T08:00:44.321Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-result\",\"detail\":{\"label\":\"manual-byte-comparison\",\"argv\":[\"diff\",\"-u\",\"manual/search.json\",\"first-unit/search.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T08:00:44.322Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-start\",\"detail\":{\"label\":\"complete-migration\",\"argv\":[\"bun\",\"migrate.mjs\",\"work/manifests\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\"}}\n{\"time\":\"2026-10-16T08:00:44.335Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-result\",\"detail\":{\"label\":\"complete-migration\",\"argv\":[\"bun\",\"migrate.mjs\",\"work/manifests\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\"exitCode\":0,\"stdout\":\"migrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/export.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/search.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json\\n{\\\"scanned\\\":7,\\\"changed\\\":6}\\n\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T08:00:44.337Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-start\",\"detail\":{\"label\":\"complete-rerun\",\"argv\":[\"bun\",\"migrate.mjs\",\"work/manifests\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\"}}\n{\"time\":\"2026-10-16T08:00:44.350Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-result\",\"detail\":{\"label\":\"complete-rerun\",\"argv\":[\"bun\",\"migrate.mjs\",\"work/manifests\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\"exitCode\":0,\"stdout\":\"unchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/export.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/search.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json\\n{\\\"scanned\\\":7,\\\"changed\\\":0}\\n\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T08:00:44.351Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-start\",\"detail\":{\"label\":\"idempotence-comparison\",\"argv\":[\"diff\",\"-u\",\"before-rerun-sha256.json\",\"after-rerun-sha256.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\"}}\n{\"time\":\"2026-10-16T08:00:44.356Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-result\",\"detail\":{\"label\":\"idempotence-comparison\",\"argv\":[\"diff\",\"-u\",\"before-rerun-sha256.json\",\"after-rerun-sha256.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T08:00:44.358Z\",\"caseId\":\"repeatable-change\",\"action\":\"independent-output-assertions\",\"detail\":{\"sixExpectedManifestBytes\":true,\"notesScopeAndV2Unchanged\":true,\"completeTreeIdempotent\":true}}\n{\"time\":\"2026-10-16T08:00:44.358Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-start\",\"detail\":{\"label\":\"negative-unknown\",\"argv\":[\"bun\",\"migrate.mjs\",\"negative/unknown/input.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\"}}\n{\"time\":\"2026-10-16T08:00:44.370Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-result\",\"detail\":{\"label\":\"negative-unknown\",\"argv\":[\"bun\",\"migrate.mjs\",\"negative/unknown/input.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\"exitCode\":1,\"stdout\":\"\",\"stderr\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/unknown/input.json: unknown manifest version\\n\"}}\n{\"time\":\"2026-10-16T08:00:44.370Z\",\"caseId\":\"repeatable-change\",\"action\":\"negative-file-preserved\",\"detail\":{\"variant\":\"unknown\",\"bytes\":\"{\\\"version\\\":9}\\n\"}}\n{\"time\":\"2026-10-16T08:00:44.370Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-start\",\"detail\":{\"label\":\"negative-malformed\",\"argv\":[\"bun\",\"migrate.mjs\",\"negative/malformed/input.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\"}}\n{\"time\":\"2026-10-16T08:00:44.381Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-result\",\"detail\":{\"label\":\"negative-malformed\",\"argv\":[\"bun\",\"migrate.mjs\",\"negative/malformed/input.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\"exitCode\":1,\"stdout\":\"\",\"stderr\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/malformed/input.json: JSON Parse error: Expected '}'\\n\"}}\n{\"time\":\"2026-10-16T08:00:44.381Z\",\"caseId\":\"repeatable-change\",\"action\":\"negative-file-preserved\",\"detail\":{\"variant\":\"malformed\",\"bytes\":\"{\"}}\n{\"time\":\"2026-10-16T08:00:44.382Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-start\",\"detail\":{\"label\":\"negative-invalid-fields\",\"argv\":[\"bun\",\"migrate.mjs\",\"negative/invalid-fields/input.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\"}}\n{\"time\":\"2026-10-16T08:00:44.395Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-result\",\"detail\":{\"label\":\"negative-invalid-fields\",\"argv\":[\"bun\",\"migrate.mjs\",\"negative/invalid-fields/input.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\"exitCode\":1,\"stdout\":\"\",\"stderr\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/invalid-fields/input.json: malformed manifest fields\\n\"}}\n{\"time\":\"2026-10-16T08:00:44.396Z\",\"caseId\":\"repeatable-change\",\"action\":\"negative-file-preserved\",\"detail\":{\"variant\":\"invalid-fields\",\"bytes\":\"{\\\"version\\\":1,\\\"key\\\":\\\"bad\\\",\\\"label\\\":\\\"Bad\\\",\\\"enabled\\\":\\\"yes\\\"}\\n\"}}\n{\"time\":\"2026-10-16T08:00:44.396Z\",\"caseId\":\"repeatable-change\",\"action\":\"proof-complete\",\"detail\":\"All executed comparisons and semantic assertions completed without an exception. No commit.\"}\n{\"time\":\"2026-10-16T08:02:37.235Z\",\"caseId\":\"repeatable-change\",\"action\":\"variant-text-captured\",\"detail\":{\"full\":\"executed actual workflow\",\"reduced\":\"simulated text only\",\"blocked\":\"simulated text only\",\"hostNegativeVariants\":\"unexercised\"}}\n{\"time\":\"2026-10-16T08:02:37.235Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-start\",\"detail\":{\"label\":\"pristine-integrity\",\"argv\":[\"diff\",\"-ru\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/repeatable-change\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/pristine\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\"}}\n{\"time\":\"2026-10-16T08:02:37.242Z\",\"caseId\":\"repeatable-change\",\"action\":\"command-result\",\"detail\":{\"label\":\"pristine-integrity\",\"argv\":[\"diff\",\"-ru\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/repeatable-change\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/pristine\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/complete-migration.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/complete-migration.json",
      "sha256": "a3df19ac121d0c921514349d088a78b8123429d43f728979a442402614dddc09",
      "bytes": 1242,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"work/manifests\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"migrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/export.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/search.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json\\n{\\\"scanned\\\":7,\\\"changed\\\":6}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/complete-rerun.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/complete-rerun.json",
      "sha256": "1b8fd11702ee04ae37461da1a75a7b6d2bf0375b556ecde7d6f1af18f23e63e9",
      "bytes": 1248,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"work/manifests\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"unchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/export.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/search.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json\\n{\\\"scanned\\\":7,\\\"changed\\\":0}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/first-unit/search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/first-unit/search.json",
      "sha256": "8eb2eedf290ce4df97b6fb12de796cd74788f4871212feafec138be06545ad74",
      "bytes": 127,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"version\": 2,\n  \"id\": \"search\",\n  \"displayName\": \"Search\",\n  \"status\": \"enabled\",\n  \"tags\": [\n    \"core\",\n    \"user\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/first-unit-execution.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/first-unit-execution.json",
      "sha256": "79dec599c95df8870cb18f8b3f5d15083744c02137629b7db88dbbabd44c3752",
      "bytes": 398,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"first-unit/search.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"migrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/first-unit/search.json\\n{\\\"scanned\\\":1,\\\"changed\\\":1}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/idempotence-comparison.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/idempotence-comparison.json",
      "sha256": "f6c222a89685a1dde760983c117211c44fe063ea54f9d43b8c7df802b6709f00",
      "bytes": 262,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-u\",\n    \"before-rerun-sha256.json\",\n    \"after-rerun-sha256.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/inspected-outputs.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/inspected-outputs.txt",
      "sha256": "405eadae52098e7d51b010521c11a8407cb6eea9926f8a73ce90b24c1b105bd8",
      "bytes": 797,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "FILE core/search.json\n{\n  \"version\": 2,\n  \"id\": \"search\",\n  \"displayName\": \"Search\",\n  \"status\": \"enabled\",\n  \"tags\": [\n    \"core\",\n    \"user\"\n  ]\n}\nFILE core/export.json\n{\n  \"version\": 2,\n  \"id\": \"export\",\n  \"displayName\": \"CSV Export\",\n  \"status\": \"disabled\",\n  \"tags\": [\n    \"core\"\n  ]\n}\nFILE admin/audit.json\n{\n  \"version\": 2,\n  \"id\": \"audit\",\n  \"displayName\": \"Audit & Review\",\n  \"status\": \"enabled\"\n}\nFILE admin/team.json\n{\n  \"version\": 2,\n  \"id\": \"team\",\n  \"displayName\": \"Team \\\"Alpha\\\"\",\n  \"status\": \"disabled\",\n  \"tags\": []\n}\nFILE mobile/offline.json\n{\n  \"version\": 2,\n  \"id\": \"offline\",\n  \"displayName\": \"Offline Mode\",\n  \"status\": \"enabled\",\n  \"tags\": [\n    \"mobile\"\n  ]\n}\nFILE mobile/alerts.json\n{\n  \"version\": 2,\n  \"id\": \"alerts\",\n  \"displayName\": \"Alerts\",\n  \"status\": \"disabled\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/manual/search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/manual/search.json",
      "sha256": "8eb2eedf290ce4df97b6fb12de796cd74788f4871212feafec138be06545ad74",
      "bytes": 127,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"version\": 2,\n  \"id\": \"search\",\n  \"displayName\": \"Search\",\n  \"status\": \"enabled\",\n  \"tags\": [\n    \"core\",\n    \"user\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/manual-byte-comparison.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/manual-byte-comparison.json",
      "sha256": "b314107f630d5807cda9337f3e7f592b17a126a8b66177217b425c016b3dc79e",
      "bytes": 255,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-u\",\n    \"manual/search.json\",\n    \"first-unit/search.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/manual-first.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/manual-first.mjs",
      "sha256": "ba956db3b4f093d813b3e9f0c9459546924ef50b806cd9ace77e45a2a08e57b3",
      "bytes": 1008,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "import { mkdir, copyFile, writeFile, readFile } from 'node:fs/promises';\nimport { event } from '../evaluate.mjs';\nawait mkdir(import.meta.dir+'/manual',{recursive:true});\nawait mkdir(import.meta.dir+'/first-unit',{recursive:true});\nawait copyFile(import.meta.dir+'/pristine/manifests/core/search.json',import.meta.dir+'/manual/search.json');\nawait copyFile(import.meta.dir+'/pristine/manifests/core/search.json',import.meta.dir+'/first-unit/search.json');\nawait event('repeatable-change','manual-start','Copied original into manual/search.json and first-unit/search.json. No migration tool exists yet.');\nawait writeFile(import.meta.dir+'/manual/search.json',`{\n  \"version\": 2,\n  \"id\": \"search\",\n  \"displayName\": \"Search\",\n  \"status\": \"enabled\",\n  \"tags\": [\n    \"core\",\n    \"user\"\n  ]\n}\n`);\nawait event('repeatable-change','manual-result',{file:'manual/search.json',method:'literal hand-authored transformation, not generated from input',bytes:await readFile(import.meta.dir+'/manual/search.json','utf8')});\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/migrate.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/migrate.mjs",
      "sha256": "0e7abaca9765bb501834cdd62985492ebe4d76b8c7a63ffe5a55dc0bdd95dd06",
      "bytes": 2262,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "import { readdir, readFile, writeFile, stat } from 'node:fs/promises';\nimport { join, resolve } from 'node:path';\nasync function files(path) {\n  if (!(await stat(path)).isDirectory()) return [path];\n  const found = [];\n  for (const entry of (await readdir(path, { withFileTypes: true })).sort((a,b)=>a.name.localeCompare(b.name))) {\n    const next = join(path, entry.name);\n    if (entry.isDirectory()) found.push(...await files(next));\n    else if (entry.isFile() && entry.name.endsWith('.json')) found.push(next);\n  }\n  return found;\n}\nfunction migrate(value) {\n  if (typeof value !== 'object' || value === null || Array.isArray(value)) throw new Error('expected manifest object');\n  if (value.version !== 1 && value.version !== 2) throw new Error('unknown manifest version');\n  const v1 = value.version === 1;\n  const fields = v1 ? ['version','key','label','enabled','tags'] : ['version','id','displayName','status','tags'];\n  if (Object.keys(value).some(key=>!fields.includes(key)) ||\n      typeof value[v1 ? 'key' : 'id'] !== 'string' || typeof value[v1 ? 'label' : 'displayName'] !== 'string' ||\n      (v1 ? typeof value.enabled !== 'boolean' : !['enabled','disabled'].includes(value.status)) ||\n      ('tags' in value && !Array.isArray(value.tags))) throw new Error('malformed manifest fields');\n  if (!v1) return null;\n  return {version:2,id:value.key,displayName:value.label,status:value.enabled?'enabled':'disabled',...('tags' in value ? {tags:value.tags} : {})};\n}\ntry {\n  const target = process.argv[2];\n  if (!target) throw new Error('usage: bun migrate.mjs <manifest directory or file>');\n  const plans = [];\n  for (const file of await files(resolve(target))) {\n    try {\n      const converted = migrate(JSON.parse(await readFile(file,'utf8')));\n      plans.push({file,output:converted===null?null:JSON.stringify(converted,null,2)+'\\n'});\n    } catch (error) { throw new Error(file+': '+error.message); }\n  }\n  for (const {file,output} of plans) {\n    if (output!==null) await writeFile(file,output);\n    console.log((output===null?'unchanged ':'migrated ')+file);\n  }\n  console.log(JSON.stringify({scanned:plans.length,changed:plans.filter(p=>p.output!==null).length}));\n} catch (error) {\n  console.error(error.message);\n  process.exitCode = 1;\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/negative-invalid-fields.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative-invalid-fields.json",
      "sha256": "d8640c4050b59bb0e3e06652d0a79a4c7e835d9069b210730adf702fd26032d1",
      "bytes": 409,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"negative/invalid-fields/input.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/invalid-fields/input.json: malformed manifest fields\\n\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/negative-malformed.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative-malformed.json",
      "sha256": "81c30d5ed4428f64c70a2246e91556963ac5b6dbf4968422c5dcb1e6fa219a60",
      "bytes": 404,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"negative/malformed/input.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/malformed/input.json: JSON Parse error: Expected '}'\\n\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/negative-unknown.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative-unknown.json",
      "sha256": "88bab8d94b00cc318e193bccaf0c5d7a3da58fffe89110c6aee8d5705c814731",
      "bytes": 394,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"negative/unknown/input.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/unknown/input.json: unknown manifest version\\n\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine-integrity.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/pristine-integrity.json",
      "sha256": "9d5eb2225ab2ee87ac37afbac41a00820316714a7e439a1acd440315973a517f",
      "bytes": 411,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/repeatable-change\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/pristine\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/prove.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/prove.mjs",
      "sha256": "2a00551576d2fdcfc46505295ee0d8529338ecda17211b75c192890121512f64",
      "bytes": 3396,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "import { readFile, writeFile, mkdir, readdir } from 'node:fs/promises';\nimport { createHash } from 'node:crypto';\nimport { join } from 'node:path';\nimport assert from 'node:assert/strict';\nimport { event, run } from '../evaluate.mjs';\nconst id='repeatable-change', base=import.meta.dir;\nawait event(id,'tool-written',{file:'migrate.mjs',manualAlreadyExists:!!(await readFile(join(base,'manual/search.json')))});\nasync function checked(label,argv,cwd=base,exit=0) { const r=await run(id,label,argv,cwd); assert.equal(r.exitCode,exit); return r; }\nawait checked('first-unit-execution',['bun','migrate.mjs','first-unit/search.json']);\nawait checked('manual-byte-comparison',['diff','-u','manual/search.json','first-unit/search.json']);\nawait checked('complete-migration',['bun','migrate.mjs','work/manifests']);\nasync function snapshot(path,prefix='') {\n  const out={};\n  for (const e of (await readdir(path,{withFileTypes:true})).sort((a,b)=>a.name.localeCompare(b.name))) {\n    const rel=prefix+e.name;\n    if(e.isDirectory()) Object.assign(out,await snapshot(join(path,e.name),rel+'/'));\n    else out[rel]=createHash('sha256').update(await readFile(join(path,e.name))).digest('hex');\n  }\n  return out;\n}\nconst before=await snapshot(join(base,'work'));\nawait writeFile(join(base,'before-rerun-sha256.json'),JSON.stringify(before,null,2)+'\\n');\nawait checked('complete-rerun',['bun','migrate.mjs','work/manifests']);\nconst after=await snapshot(join(base,'work'));\nawait writeFile(join(base,'after-rerun-sha256.json'),JSON.stringify(after,null,2)+'\\n');\nassert.deepEqual(after,before);\nawait checked('idempotence-comparison',['diff','-u','before-rerun-sha256.json','after-rerun-sha256.json']);\nconst rows=[['core/search','search','Search',true,['core','user']],['core/export','export','CSV Export',false,['core']],['admin/audit','audit','Audit & Review',true],['admin/team','team','Team \"Alpha\"',false,[]],['mobile/offline','offline','Offline Mode',true,['mobile']],['mobile/alerts','alerts','Alerts',false]];\nlet inspected='';\nfor(const [path,idValue,label,enabled,tags] of rows) {\n const actual=await readFile(join(base,'work/manifests',path+'.json'),'utf8');\n const expected={version:2,id:idValue,displayName:label,status:enabled?'enabled':'disabled',...(tags===undefined?{}:{tags})};\n assert.equal(actual,JSON.stringify(expected,null,2)+'\\n');\n inspected+='FILE '+path+'.json\\n'+actual;\n}\nfor(const p of ['notes.txt','scope.md','manifests/core/already-v2.json']) {\n assert.deepEqual(await readFile(join(base,'work',p)),await readFile(join(base,'pristine',p)));\n}\nawait writeFile(join(base,'inspected-outputs.txt'),inspected);\nawait event(id,'independent-output-assertions',{sixExpectedManifestBytes:true,notesScopeAndV2Unchanged:true,completeTreeIdempotent:true});\nfor(const [name,bytes] of [['unknown','{\"version\":9}\\n'],['malformed','{'],['invalid-fields','{\"version\":1,\"key\":\"bad\",\"label\":\"Bad\",\"enabled\":\"yes\"}\\n']]) {\n await mkdir(join(base,'negative',name),{recursive:true});\n const path=join('negative',name,'input.json');\n await writeFile(join(base,path),bytes);\n await checked('negative-'+name,['bun','migrate.mjs',path],base,1);\n assert.equal(await readFile(join(base,path),'utf8'),bytes);\n await event(id,'negative-file-preserved',{variant:name,bytes});\n}\nawait event(id,'proof-complete','All executed comparisons and semantic assertions completed without an exception. No commit.');\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/registry-entry.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/registry-entry.json",
      "sha256": "0a0636a7a6484d1c36aed9c7e887d1ade40f79849bda61b3d2efa3ac8266fdd6",
      "bytes": 740,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"caseId\": \"repeatable-change\",\n  \"caseFile\": \"docs/parity/cases/skills/principle-build-the-lever.json\",\n  \"sourcePaths\": [\n    \"skills/principle-build-the-lever/SKILL.md\"\n  ],\n  \"requiredHosts\": [\n    \"chatgpt\",\n    \"codex\"\n  ],\n  \"structuralOnly\": false,\n  \"hostStatus\": {\n    \"chatgpt\": \"blocked\",\n    \"codex\": \"blocked\"\n  },\n  \"requiredObservations\": {\n    \"pass\": [\n      \"read\",\n      \"review-outcome\",\n      \"isolated-write\"\n    ],\n    \"reduced-pass\": [\n      \"read\"\n    ]\n  },\n  \"executionModes\": {\n    \"pass\": [\n      \"direct\",\n      \"workers\"\n    ],\n    \"reduced-pass\": [\n      \"direct\",\n      \"sequential\",\n      \"workers\"\n    ]\n  },\n  \"requiredPermissions\": {\n    \"pass\": [\n      \"writes\"\n    ],\n    \"reduced-pass\": []\n  }\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/supplied-contract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/supplied-contract.json",
      "sha256": "d079f1cfe4c1d1d42d1a86f1c5fd32133d662a6e39f21ed80862c550dfe21bf3",
      "bytes": 1575,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"id\": \"repeatable-change\",\n  \"sourcePaths\": [\n    \"skills/principle-build-the-lever/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.\",\n  \"requirements\": [\n    \"Source reads; authorized artifact writes and execution for full proof.\",\n    \"Independent workers require exposed worker tools and user authorization; they are unnecessary when a deterministic tool processes all units.\"\n  ],\n  \"expectedFull\": \"Produce the smallest safe rerunnable tool as a file; learn the recipe on a first unit, rerun and diff it against the hand-done result, and report observed commands and outputs. Retain the tool for review and commit only with authorization when work outlives the session.\",\n  \"expectedReduced\": \"When writes or execution are unavailable, propose the tool and verification recipe as reduced capability, distinguish the proposal from a saved artifact and executed proof, and state the missing capabilities.\",\n  \"expectedBlocked\": \"If source is unavailable or denied, state that the recipe and equivalence cannot be verified; request the required source or capability without claiming implementation or proof.\",\n  \"forbiddenClaims\": [\n    \"A proposed tool was saved, run or verified without observed evidence.\",\n    \"Hand-applied changes alone satisfy the principle.\",\n    \"Sequential work proves independent workers.\",\n    \"Invocation grants commit, delegation or external-action permission.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json",
      "sha256": "979b1fcb8ef17e6bcbc2f7d8be9447207bb595efce09e2a9318555709c3291c1",
      "bytes": 94,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"version\": 2,\n  \"id\": \"audit\",\n  \"displayName\": \"Audit & Review\",\n  \"status\": \"enabled\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json",
      "sha256": "be497301b6eb8a67153a754926bc98906913eab6823e37d784390a6a9cad34dc",
      "bytes": 108,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"version\": 2,\n  \"id\": \"team\",\n  \"displayName\": \"Team \\\"Alpha\\\"\",\n  \"status\": \"disabled\",\n  \"tags\": []\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/manifests/core/export.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/export.json",
      "sha256": "d9e651b812edef7cd3d5530475b1405ac889f652f177ebb92e1aa2f94cc3deb7",
      "bytes": 120,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"version\": 2,\n  \"id\": \"export\",\n  \"displayName\": \"CSV Export\",\n  \"status\": \"disabled\",\n  \"tags\": [\n    \"core\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/manifests/core/search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/search.json",
      "sha256": "8eb2eedf290ce4df97b6fb12de796cd74788f4871212feafec138be06545ad74",
      "bytes": 127,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"version\": 2,\n  \"id\": \"search\",\n  \"displayName\": \"Search\",\n  \"status\": \"enabled\",\n  \"tags\": [\n    \"core\",\n    \"user\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json",
      "sha256": "24138ac519edc807247edce3f204d9bfdcb6f49cdc57955f5b581b27cfbbeb6e",
      "bytes": 88,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"version\": 2,\n  \"id\": \"alerts\",\n  \"displayName\": \"Alerts\",\n  \"status\": \"disabled\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json",
      "sha256": "f51840cd7f3df4a14b0aaef0f31331ce9acf7f51954773ae26794258cb59b62f",
      "bytes": 124,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "{\n  \"version\": 2,\n  \"id\": \"offline\",\n  \"displayName\": \"Offline Mode\",\n  \"status\": \"enabled\",\n  \"tags\": [\n    \"mobile\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change.result.md",
      "sha256": "2ec9df3d473d1e47150bf1ab66acdc19918f8cce6d8fcfc408cdaad8f6322cdb",
      "bytes": 18661,
      "owners": [
        "grades-native-rerun-02.json#2"
      ],
      "text": "# repeatable-change\n\nSaved the literal hand-authored manual/search.json before creating migrate.mjs. Saved the original separately in pristine/ and first-unit/. The tool validates inputs before writing, handles v1 conversion, preserves optional tags and field order, and leaves valid v2 bytes intact. It preflights selected files before overwriting any of them. This is a deterministic direct workflow; independent workers are unnecessary and none were spawned.\n\nExecuted the tool on the pristine first-unit copy, then diffed generated and manual bytes: exit 0 with no diff. The complete owned tree scan found 7 manifests and changed 6. Independently specified expected bytes were asserted for all six transformed manifests, including escaped text, omitted tags, empty tags and both statuses. Notes, scope and already-v2 bytes were compared to pristine and were unchanged. The complete rerun scanned 7 and changed 0; before/after SHA-256 snapshots and diff confirm the entire owned work tree was unchanged. Unknown-version, malformed-JSON and invalid-field inputs each exited 1 with a clear file-specific error; their original bytes remained unchanged. Tool and proof scripts are retained without a commit.\n\n## Scope and provenance\n\nSource package root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nSupplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Package metadata confirms version 0.1.0. No package Git revision was independently established; the supplied freeze is an input identifier, not verified provenance. Named source/support contents were actually read and saved in [source-reads.txt](repeatable-change/source-reads.txt). Registry entry is in [registry-entry.json](repeatable-change/registry-entry.json). No separate 0.2.1 package files were used. The compiler came from the independent installed Bun cache, not another plugin version.\n\nAll fixture data is synthetic. Shared inputs were copied in full to pristine/ and work/ before edits. Final pristine-integrity diff exited 0. No real service contact, issue, PR, message, commit, push, publish, configuration change, dependency installation or schedule occurred. No worker receipts or screenshots are claimed. Runtime timing strings below are Bun's actual output and are not performance benchmarks.\n\n## Supplied input\n\nFull registered contract:\n\n```json\n{\n  \"id\": \"repeatable-change\",\n  \"sourcePaths\": [\n    \"skills/principle-build-the-lever/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.\",\n  \"requirements\": [\n    \"Source reads; authorized artifact writes and execution for full proof.\",\n    \"Independent workers require exposed worker tools and user authorization; they are unnecessary when a deterministic tool processes all units.\"\n  ],\n  \"expectedFull\": \"Produce the smallest safe rerunnable tool as a file; learn the recipe on a first unit, rerun and diff it against the hand-done result, and report observed commands and outputs. Retain the tool for review and commit only with authorization when work outlives the session.\",\n  \"expectedReduced\": \"When writes or execution are unavailable, propose the tool and verification recipe as reduced capability, distinguish the proposal from a saved artifact and executed proof, and state the missing capabilities.\",\n  \"expectedBlocked\": \"If source is unavailable or denied, state that the recipe and equivalence cannot be verified; request the required source or capability without claiming implementation or proof.\",\n  \"forbiddenClaims\": [\n    \"A proposed tool was saved, run or verified without observed evidence.\",\n    \"Hand-applied changes alone satisfy the principle.\",\n    \"Sequential work proves independent workers.\",\n    \"Invocation grants commit, delegation or external-action permission.\"\n  ]\n}\n```\n\nComplete scenario scope:\n\n```markdown\n# Manifest migration recipe\n\nThis is a private synthetic multi-directory manifest migration. All target files match manifests/**/*.json. Each v1 object has exactly version, key, label, enabled and optional tags. Convert version:1 to version:2, key to id, label to displayName and enabled boolean to status:'enabled' or 'disabled'. Preserve tags exactly and emit keys in this order: version,id,displayName,status,tags (omit tags when absent). Output JSON uses two-space indentation and one final newline. Already-v2 manifests remain byte-for-byte unchanged. README and notes are not migration targets. Unknown versions or malformed inputs must cause a clear error before overwriting that file.\n\nFirst copy manifests/core/search.json to an owned manual/ directory and hand-apply the recipe. Preserve a pristine copy of that original separately. Only after the manual result exists, write the smallest deterministic rerunnable tool as a real file. Run it on the pristine first-unit copy and compare bytes to the manual result. Then migrate the complete owned manifest tree, inspect outputs and run the tool again to check no changes. Do not overwrite the manual exemplar or shared originals. Retain the tool and actual command outputs; no commit or external action is authorized by this fixture.\n\nThe supplied files are initial inputs only. A completed transformed output, tool, test pass or equivalence receipt is intentionally absent.\n```\n\nOriginal source inputs are retained byte-for-byte in [repeatable-change/pristine/](repeatable-change/pristine/). The shared scenario map and compiler hints were read through the exposed command tool and copied to the writable root. Preparation checks were not used as execution proof.\n\n## Variants and limits\n\nThe full workflow was executed on the actual host. Reduced and blocked responses were captured as explicitly simulated fallback text in [capability-variants.md](repeatable-change/capability-variants.md). Their actual responses follow.\n\nReduced: Simulated missing writes or execution. Proposed tool: a Bun script that traverses manifests/**/*.json, validates version and fields, renames the v1 fields in the required order, preserves tags and leaves v2 bytes untouched. First hand-transform search.json, then generate from a separate pristine copy, diff the bytes, migrate the owned tree, snapshot bytes and rerun to prove idempotence. Under this simulated restriction no tool was saved, run or verified. The actual-host tool belongs to the separate executed variant.\n\nBlocked: Simulated missing source. Without the source manifests and recipe, do not claim a verified transformation or equivalence. Required inputs are the v1/v2 schema, formatting rules, file scope and a pristine first unit. In the actual host these inputs were available; this text does not prove a denied read.\n\nHost-enforced no-write, no-execution and unavailable-source variants remain unexercised. The host provided these capabilities, and changing configuration to manufacture denials was forbidden. Simulated text does not prove host denial. Metadata enforcement was not tested. Independent worker variants were unnecessary and not attempted. Missing actual model identity is irrelevant to these direct file workflows; no model execution receipt is claimed. No self-assigned grade is included.\n\n## Actual tools, actions and chronology\n\nExposed tool used: functions.exec, invoking tools.exec_command. Bun performed file writes, reads, command execution and assertion scripts. Local diff and rg commands ran through Bun in the saved execution records. Bindings and their limitations are in [capability-bindings.json](repeatable-change/capability-bindings.json).\n\nThe ordered initial discovery reads precede the timestamped journal and are documented in [pre-journal-actions.md](pre-journal-actions.md); their raw tool responses remain in this session transcript. The following timestamps are actual UTC event times from the command runner. Asia/Amman is UTC+03:00. The journal captures case operations in execution order; it does not reconstruct unobserved actions.\n\n- 2026-10-16T07:59:06.415Z setup: {\"sourceRoot\":\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\"scenario\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/repeatable-change\",\"copies\":[\"pristine\",\"work\"],\"sourceReads\":\"source-reads.txt\"}\n- 2026-10-16T08:00:02.662Z manual-start: \"Copied original into manual/search.json and first-unit/search.json. No migration tool exists yet.\"\n- 2026-10-16T08:00:02.663Z manual-result: {\"file\":\"manual/search.json\",\"method\":\"literal hand-authored transformation, not generated from input\",\"bytes\":\"{\\n  \\\"version\\\": 2,\\n  \\\"id\\\": \\\"search\\\",\\n  \\\"displayName\\\": \\\"Search\\\",\\n  \\\"status\\\": \\\"enabled\\\",\\n  \\\"tags\\\": [\\n    \\\"core\\\",\\n    \\\"user\\\"\\n  ]\\n}\\n\"}\n- 2026-10-16T08:00:44.304Z tool-written: {\"file\":\"migrate.mjs\",\"manualAlreadyExists\":true}\n- 2026-10-16T08:00:44.304Z command-start: \"first-unit-execution\"\n- 2026-10-16T08:00:44.316Z command-result: \"first-unit-execution\"\n- 2026-10-16T08:00:44.316Z command-start: \"manual-byte-comparison\"\n- 2026-10-16T08:00:44.321Z command-result: \"manual-byte-comparison\"\n- 2026-10-16T08:00:44.322Z command-start: \"complete-migration\"\n- 2026-10-16T08:00:44.335Z command-result: \"complete-migration\"\n- 2026-10-16T08:00:44.337Z command-start: \"complete-rerun\"\n- 2026-10-16T08:00:44.350Z command-result: \"complete-rerun\"\n- 2026-10-16T08:00:44.351Z command-start: \"idempotence-comparison\"\n- 2026-10-16T08:00:44.356Z command-result: \"idempotence-comparison\"\n- 2026-10-16T08:00:44.358Z independent-output-assertions: {\"sixExpectedManifestBytes\":true,\"notesScopeAndV2Unchanged\":true,\"completeTreeIdempotent\":true}\n- 2026-10-16T08:00:44.358Z command-start: \"negative-unknown\"\n- 2026-10-16T08:00:44.370Z command-result: \"negative-unknown\"\n- 2026-10-16T08:00:44.370Z negative-file-preserved: {\"variant\":\"unknown\",\"bytes\":\"{\\\"version\\\":9}\\n\"}\n- 2026-10-16T08:00:44.370Z command-start: \"negative-malformed\"\n- 2026-10-16T08:00:44.381Z command-result: \"negative-malformed\"\n- 2026-10-16T08:00:44.381Z negative-file-preserved: {\"variant\":\"malformed\",\"bytes\":\"{\"}\n- 2026-10-16T08:00:44.382Z command-start: \"negative-invalid-fields\"\n- 2026-10-16T08:00:44.395Z command-result: \"negative-invalid-fields\"\n- 2026-10-16T08:00:44.396Z negative-file-preserved: {\"variant\":\"invalid-fields\",\"bytes\":\"{\\\"version\\\":1,\\\"key\\\":\\\"bad\\\",\\\"label\\\":\\\"Bad\\\",\\\"enabled\\\":\\\"yes\\\"}\\n\"}\n- 2026-10-16T08:00:44.396Z proof-complete: \"All executed comparisons and semantic assertions completed without an exception. No commit.\"\n- 2026-10-16T08:02:37.235Z variant-text-captured: {\"full\":\"executed actual workflow\",\"reduced\":\"simulated text only\",\"blocked\":\"simulated text only\",\"hostNegativeVariants\":\"unexercised\"}\n- 2026-10-16T08:02:37.235Z command-start: \"pristine-integrity\"\n- 2026-10-16T08:02:37.242Z command-result: \"pristine-integrity\"\n\n## Command results\n\n| Command record | Exit | Artifact |\n|---|---:|---|\n| first-unit-execution | 0 | [first-unit-execution.json](repeatable-change/first-unit-execution.json) |\n| manual-byte-comparison | 0 | [manual-byte-comparison.json](repeatable-change/manual-byte-comparison.json) |\n| complete-migration | 0 | [complete-migration.json](repeatable-change/complete-migration.json) |\n| complete-rerun | 0 | [complete-rerun.json](repeatable-change/complete-rerun.json) |\n| idempotence-comparison | 0 | [idempotence-comparison.json](repeatable-change/idempotence-comparison.json) |\n| negative-unknown | 1 | [negative-unknown.json](repeatable-change/negative-unknown.json) |\n| negative-malformed | 1 | [negative-malformed.json](repeatable-change/negative-malformed.json) |\n| negative-invalid-fields | 1 | [negative-invalid-fields.json](repeatable-change/negative-invalid-fields.json) |\n| pristine-integrity | 0 | [pristine-integrity.json](repeatable-change/pristine-integrity.json) |\n\nA diff exit of 1 in implementation-diff means changes were found. The migration legacy-reference-search exit of 1 means no matches. Phase-3-static exit of 2 is the observed planned temporary compiler failure. Negative manifest exits of 1 are observed rejection paths.\n\n### first-unit-execution\n\n```json\n{\n  \"label\": \"first-unit-execution\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"first-unit/search.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"migrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/first-unit/search.json\\n{\\\"scanned\\\":1,\\\"changed\\\":1}\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### manual-byte-comparison\n\n```json\n{\n  \"label\": \"manual-byte-comparison\",\n  \"argv\": [\n    \"diff\",\n    \"-u\",\n    \"manual/search.json\",\n    \"first-unit/search.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### complete-migration\n\n```json\n{\n  \"label\": \"complete-migration\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"work/manifests\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"migrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/export.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/search.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json\\nmigrated /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json\\n{\\\"scanned\\\":7,\\\"changed\\\":6}\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### complete-rerun\n\n```json\n{\n  \"label\": \"complete-rerun\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"work/manifests\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"unchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/audit.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/admin/team.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/export.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/core/search.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/alerts.json\\nunchanged /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/work/manifests/mobile/offline.json\\n{\\\"scanned\\\":7,\\\"changed\\\":0}\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### idempotence-comparison\n\n```json\n{\n  \"label\": \"idempotence-comparison\",\n  \"argv\": [\n    \"diff\",\n    \"-u\",\n    \"before-rerun-sha256.json\",\n    \"after-rerun-sha256.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### negative-unknown\n\n```json\n{\n  \"label\": \"negative-unknown\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"negative/unknown/input.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/unknown/input.json: unknown manifest version\\n\"\n}\n```\n\n### negative-malformed\n\n```json\n{\n  \"label\": \"negative-malformed\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"negative/malformed/input.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/malformed/input.json: JSON Parse error: Expected '}'\\n\"\n}\n```\n\n### negative-invalid-fields\n\n```json\n{\n  \"label\": \"negative-invalid-fields\",\n  \"argv\": [\n    \"bun\",\n    \"migrate.mjs\",\n    \"negative/invalid-fields/input.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/negative/invalid-fields/input.json: malformed manifest fields\\n\"\n}\n```\n\n### pristine-integrity\n\n```json\n{\n  \"label\": \"pristine-integrity\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/repeatable-change\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/repeatable-change/pristine\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n## Reviewable artifacts\n\nFinal files are in [repeatable-change/work/](repeatable-change/work/), originals in [repeatable-change/pristine/](repeatable-change/pristine/). Case scripts and exact result JSON files remain in [repeatable-change/](repeatable-change/). Source and script digests are in [artifact-sha256.json](repeatable-change/artifact-sha256.json). The full ordered run is retained in [chronology.jsonl](chronology.jsonl), with a case-only copy in [repeatable-change/chronology.jsonl](repeatable-change/chronology.jsonl). The shared runner is [evaluate.mjs](evaluate.mjs). Scripts that create baselines or the hand-authored first unit are historical setup steps and should not be replayed over the completed evidence. Rerun tests in work/, and rerun the manifest tool directly on work/manifests.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-03/repeatable-change/input",
      "owner": "grades-native-03.json#7",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/source",
      "owner": "grades-native-03.json#7",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/source-reads.json",
      "owner": "grades-native-03.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/input",
      "owner": "grades-native-03.json#7",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/source",
      "owner": "grades-native-03.json#7",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/repeatable-change/source-reads.json",
      "owner": "grades-native-03.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/negative/invalid-fields/input.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/negative/malformed/input.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/negative/unknown/input.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/admin/audit.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/audit.json",
      "sha256": "f1fe37db4c10a1cbe853dc6bd6b3b1552e1553e77fc2dd784dc29a8f0cb5bb89",
      "bytes": 68
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/admin/team.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/team.json",
      "sha256": "38c17fac7484013aa87731b186320a4063d5a88483bad6f8d800ba82d61244c9",
      "bytes": 78
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/core/already-v2.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "sha256": "e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef",
      "bytes": 74
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/core/export.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/export.json",
      "sha256": "397f46dea18161080687041f785a21939fbb767369e9c4d5ca19d4ce75132c0b",
      "bytes": 82
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/core/search.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/search.json",
      "sha256": "23c1414ffb2f5e6b818318b418006bb91028260038177a270092610f625f924a",
      "bytes": 84
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/mobile/alerts.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "sha256": "8b6281181e6ae1cd4aee60f022303450c065d3ac028b174d95efe55672248ee7",
      "bytes": 62
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/mobile/offline.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "sha256": "f71540be3ed66918ba50265eb11f8e795a9de3c358be8a1f72961725253aa61a",
      "bytes": 86
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/notes.txt",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/notes.txt",
      "sha256": "81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe",
      "bytes": 108
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/scope.md",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/scope.md",
      "sha256": "caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52",
      "bytes": 1434
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/source-reads.txt",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "sha256": "e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef",
      "bytes": 74
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/notes.txt",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/notes.txt",
      "sha256": "81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe",
      "bytes": 108
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/scope.md",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/scope.md",
      "sha256": "caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52",
      "bytes": 1434
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/negative/invalid-fields/input.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/negative/malformed/input.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/negative/unknown/input.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/admin/audit.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/audit.json",
      "sha256": "f1fe37db4c10a1cbe853dc6bd6b3b1552e1553e77fc2dd784dc29a8f0cb5bb89",
      "bytes": 68
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/admin/team.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/admin/team.json",
      "sha256": "38c17fac7484013aa87731b186320a4063d5a88483bad6f8d800ba82d61244c9",
      "bytes": 78
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/core/already-v2.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "sha256": "e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef",
      "bytes": 74
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/core/export.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/export.json",
      "sha256": "397f46dea18161080687041f785a21939fbb767369e9c4d5ca19d4ce75132c0b",
      "bytes": 82
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/core/search.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/search.json",
      "sha256": "23c1414ffb2f5e6b818318b418006bb91028260038177a270092610f625f924a",
      "bytes": 84
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/mobile/alerts.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/alerts.json",
      "sha256": "8b6281181e6ae1cd4aee60f022303450c065d3ac028b174d95efe55672248ee7",
      "bytes": 62
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/manifests/mobile/offline.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/mobile/offline.json",
      "sha256": "f71540be3ed66918ba50265eb11f8e795a9de3c358be8a1f72961725253aa61a",
      "bytes": 86
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/notes.txt",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/notes.txt",
      "sha256": "81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe",
      "bytes": 108
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/pristine/scope.md",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/scope.md",
      "sha256": "caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52",
      "bytes": 1434
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/source-reads.txt",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/manifests/core/already-v2.json",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/manifests/core/already-v2.json",
      "sha256": "e8e57a81b0f53c6add6fd827961d08385b36028a4af9edcbe3d1cd94c2a58bef",
      "bytes": 74
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/notes.txt",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/notes.txt",
      "sha256": "81e7f617bdfbebb6c0700e86510c19ea89636d2a141648a12947bfd49e3fa2fe",
      "bytes": 108
    },
    {
      "path": "fixtures/rerun-02/repeatable-change/work/scope.md",
      "owner": "grades-native-rerun-02.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/repeatable-change/scope.md",
      "sha256": "caa12f4aeca3956c1efdfbec32cce9f76edee18e82ae21e88c8d6eaa373dee52",
      "bytes": 1434
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
