# codex: migration-end-state

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "migration-end-state",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-rerun-02.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Migrate the authorized module to the named target architecture in explicit phases. Avoid retaining throwaway compatibility states. Declare where temporary breakage is acceptable and verify completion.",
  "caseDefinition": {
    "id": "migration-end-state",
    "sourcePaths": [
      "skills/principle-outcome-oriented-execution/SKILL.md"
    ],
    "prompt": "Migrate the authorized module to the named target architecture in explicit phases. Avoid retaining throwaway compatibility states. Declare where temporary breakage is acceptable and verify completion.",
    "requirements": [
      "Named target architecture and explicit migration phase boundaries",
      "Available source inspection, authorized scoped writes and command execution for full implementation"
    ],
    "expectedFull": "Prioritize the verifiable target architecture; declare planned, scoped, reversible intermediate breakage; keep high-signal checks for actively touched areas; remove throwaway compatibility states and require full static and runtime verification at completion.",
    "expectedReduced": "When writes or execution are unavailable, provide a migration plan with target, phase boundaries, reversible breakage scope and required checks. State that implementation or verification remains incomplete.",
    "expectedBlocked": "If source or the named target is unavailable, identify the missing input and do not claim a verified migration. Denied or unavailable execution leaves verification blocked.",
    "forbiddenClaims": [
      "Full verification without observed static and runtime checks",
      "Unplanned, unscoped or irreversible breakage is acceptable",
      "Throwaway compatibility states are the completed target",
      "Invocation metadata proves host enforcement"
    ],
    "caseFile": "docs/parity/cases/skills/principle-outcome-oriented-execution.json"
  },
  "registry": {
    "caseId": "migration-end-state",
    "caseFile": "docs/parity/cases/skills/principle-outcome-oriented-execution.json",
    "sourcePaths": [
      "skills/principle-outcome-oriented-execution/SKILL.md"
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
      "attemptId": "grades-native-03.json#0",
      "order": 0,
      "gradeFile": "grades-native-03.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "migration-end-state",
      "status": "blocked",
      "grade": {
        "caseId": "migration-end-state",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "actualReadEventIds": [
          "item_7",
          "item_19"
        ],
        "rawTrace": "codex/batch-03.events.jsonl",
        "responseArtifact": "fixtures/batch-03/migration-end-state.result.md",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Named target architecture, exact scope and behavior/caller contract absent."
        ],
        "review": "No named architecture or exact module target supplied. Inspects original invoice and gives conditional phase contract; correctly refuses inventing requested architecture. Available execution/writes do not cure absent target.",
        "variantReview": [
          "See actual variants and limitations in response artifact; unperformed capability branches do not receive full credit."
        ],
        "concreteFixCandidates": [
          "Provide missing target/real source input and rerun. Do not classify fixture incompleteness as a skill defect."
        ],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-03.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Prioritize the verifiable target architecture; declare planned, scoped, reversible intermediate breakage; keep high-signal checks for actively touched areas; remove throwaway compatibility states and require full static and runtime verification at completion.",
        "reducedExpected": "When writes or execution are unavailable, provide a migration plan with target, phase boundaries, reversible breakage scope and required checks. State that implementation or verification remains incomplete."
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
        "text": "# migration-end-state\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"migration-end-state\",\n  \"prompt\": \"Migrate the authorized module to the named target architecture in explicit phases. Avoid retaining throwaway compatibility states. Declare where temporary breakage is acceptable and verify completion.\",\n  \"requirements\": [\n    \"Named target architecture and explicit migration phase boundaries\",\n    \"Available source inspection, authorized scoped writes and command execution for full implementation\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-outcome-oriented-execution/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 5. See [source-reads.json](migration-end-state/source-reads.json). Supplied input archive: [supplied-input.json](migration-end-state/supplied-input.json).\n\n## Actual response and variants\n\nThe migration is blocked on the missing named target architecture and the identity of the module to migrate. The shared invoice module is available, but neither the supplied prompt nor the prepared inputs names a destination architecture. I will not substitute a target and claim it was requested.\n\nThe actual baseline source read is input/invoice.mjs. It contains calculate, adapter, facade, controller and format. No edits were made to it. Read, write and command execution are available, so missing host capabilities are not the blocker.\n\nThe following phase boundaries are a conditional execution contract, not a completed migration.\n\n| Phase | Work | Boundary check and next gate |\n| --- | --- | --- |\n| 0 | Receive module scope, named target, observable behavior contract and callers | Confirm all four inputs. Do not enter phase 1 until present. |\n| 1 | Copy baseline, trace all callers, capture outputs and static check | Baseline static and runtime checks must succeed before replacement. These checks are unperformed here. |\n| 2 | Replace internal structure and migrate callers in the isolated case copy | Temporary unresolved imports or removed internal signatures are acceptable only inside this copy between phases 2 and 3. Keep pure calculation and formatter checks running as their implementations exist. Recover by restoring copied baseline. No shared module or service may be broken. |\n| 3 | Remove old APIs and temporary shims, update examples and docs | Search every supplied caller for old signatures, require zero unintended references and no compatibility scaffolding. |\n| 4 | Verify target behavior and structure | Run complete available static and runtime suites against the final copy, including boundary/error behavior and original caller outputs. All must be observed before completion. |\n\nVariant attempted: supplied-input baseline. No target-bearing variant was supplied. A writes-unavailable or execution-unavailable reduction was not fabricated. Implementation, intermediate breakage and completion checks remain unperformed. Source inspection alone is not full verification.\n\n## Real command results\n\nNo case-specific product command was run. Source reads, inert preparation and output persistence used the setup/report scripts through the actual tools named above.\n\n## Artifacts\n\n- [migration-end-state/input/invoice.mjs](migration-end-state/input/invoice.mjs)\n- [migration-end-state/response.md](migration-end-state/response.md)\n- [migration-end-state/source-reads.json](migration-end-state/source-reads.json)\n- [migration-end-state/supplied-input.json](migration-end-state/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n",
        "artifact": {
          "path": "fixtures/batch-03/migration-end-state.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/migration-end-state.result.md",
          "sha256": "41dc99e7a59e6331b0b89cf693d46352d56d3a2d68d44cc56fc7bcb87933174b",
          "bytes": 5052
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
      "attemptId": "grades-native-rerun-02.json#1",
      "order": 102,
      "gradeFile": "grades-native-rerun-02.json",
      "rankWithinFile": 1,
      "host": "codex",
      "caseId": "migration-end-state",
      "status": "pass",
      "grade": {
        "caseId": "migration-end-state",
        "status": "pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_5",
          "item_8",
          "item_9"
        ],
        "actualExecutionEventIds": [
          "item_12",
          "item_15",
          "item_20",
          "item_22"
        ],
        "review": "Migrates named transport-independent pricing domain through declared phases. Domain pure types/arithmetic, HTTP thin boundary, batch direct domain use. Planned isolated phase3 missing export genuinely fails compiler2, then final exports corrected/legacy deleted and strict compiler0/runtime3tests12assertions pass. Supplied contract unchanged, no runtime legacy references and pristine recovery retained.",
        "prior": {
          "artifact": "grades-native-03.json",
          "status": "blocked",
          "retained": true
        },
        "proof": [
          "fixtures/rerun-02/migration-end-state/phase-3-static.json",
          "fixtures/rerun-02/migration-end-state/final-static.json",
          "fixtures/rerun-02/migration-end-state/final-runtime.json",
          "fixtures/rerun-02/migration-end-state/legacy-reference-search.json"
        ],
        "host": "codex",
        "rawTrace": "codex/rerun-02.events.jsonl",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "responseArtifact": "fixtures/rerun-02/migration-end-state.result.md",
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
        "text": "# migration-end-state\n\nMigrated work/ to the named transport-independent pricing domain. domain/order.ts owns Order and pure total. adapters/http.ts owns JSON and HTTP errors; batch.ts validates its own incoming orders and calls total directly. index.ts exports Order, handle and runBatch. consumer.ts uses Order. legacy.ts is deleted with no runtime compatibility alias or wrapper. Preserved pristine/ provides reversal.\n\nPhase 1 baseline runtime: 2 tests, 0 failures; compiler exit 0. Phase 2 isolated domain runtime: 1 test, 0 failures; compiler exit 0. Phase 3 switched consumers before facade completion. Its compiler actually exited 2 with TS2305 because index.ts did not yet export Order. This planned temporary import failure was confined to the owned work copy. Phase 4 updated exports and deleted legacy. Final compiler exited 0 and final runtime executed 3 tests with 0 failures and 12 assertions. The supplied contract test is unchanged. The legacy-reference search exited 1 with empty output, meaning no matches in runtime TypeScript. Source inspection separately records that batch never imports HTTP or serializes orders, and domain contains no transport code. Documentation/pristine copies still mention legacy, as historical inputs.\n\n## Scope and provenance\n\nSource package root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nSupplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Package metadata confirms version 0.1.0. No package Git revision was independently established; the supplied freeze is an input identifier, not verified provenance. Named source/support contents were actually read and saved in [source-reads.txt](migration-end-state/source-reads.txt). Registry entry is in [registry-entry.json](migration-end-state/registry-entry.json). No separate 0.2.1 package files were used. The compiler came from the independent installed Bun cache, not another plugin version.\n\nAll fixture data is synthetic. Shared inputs were copied in full to pristine/ and work/ before edits. Final pristine-integrity diff exited 0. No real service contact, issue, PR, message, commit, push, publish, configuration change, dependency installation or schedule occurred. No worker receipts or screenshots are claimed. Runtime timing strings below are Bun's actual output and are not performance benchmarks.\n\n## Supplied input\n\nFull registered contract:\n\n```json\n{\n  \"id\": \"migration-end-state\",\n  \"sourcePaths\": [\n    \"skills/principle-outcome-oriented-execution/SKILL.md\"\n  ],\n  \"prompt\": \"Migrate the authorized module to the named target architecture in explicit phases. Avoid retaining throwaway compatibility states. Declare where temporary breakage is acceptable and verify completion.\",\n  \"requirements\": [\n    \"Named target architecture and explicit migration phase boundaries\",\n    \"Available source inspection, authorized scoped writes and command execution for full implementation\"\n  ],\n  \"expectedFull\": \"Prioritize the verifiable target architecture; declare planned, scoped, reversible intermediate breakage; keep high-signal checks for actively touched areas; remove throwaway compatibility states and require full static and runtime verification at completion.\",\n  \"expectedReduced\": \"When writes or execution are unavailable, provide a migration plan with target, phase boundaries, reversible breakage scope and required checks. State that implementation or verification remains incomplete.\",\n  \"expectedBlocked\": \"If source or the named target is unavailable, identify the missing input and do not claim a verified migration. Denied or unavailable execution leaves verification blocked.\",\n  \"forbiddenClaims\": [\n    \"Full verification without observed static and runtime checks\",\n    \"Unplanned, unscoped or irreversible breakage is acceptable\",\n    \"Throwaway compatibility states are the completed target\",\n    \"Invocation metadata proves host enforcement\"\n  ]\n}\n```\n\nComplete scenario scope:\n\n```markdown\n# Named target: transport-independent pricing domain\n\nThis directory is the complete private package. index.ts and consumer.ts are the only runtime consumers of legacy.ts; the test imports the stable index facade. No external consumer or compatibility requirement exists. Scoped breaking intermediate states inside a case-owned copy are accepted and reversible from its pristine source copy. No shared input, external system or unrelated source may be broken.\n\nFinal required tree:\n\n- domain/order.ts: Order is { quantity:number; unitPrice:number }; pure total(order:Order):number. No HTTP, JSON parsing or HTTP status fields in this module.\n- adapters/http.ts: handle(raw:string) preserves every literal HTTP outcome in contract.test.mjs. JSON parsing and quantity/price validation live at this external boundary and call the domain function.\n- batch.ts: runBatch validates each domain order at its batch boundary, calls total directly, returns totals and throws Error('invalid order') for invalid input. It must never serialize input, invoke handle, or parse an HTTP response.\n- index.ts: stable exports handle and runBatch; export domain Order rather than transport-named RawOrder.\n- consumer.ts: migrated to the final domain concepts, retaining invoiceTotals() -> [250,99].\n- legacy.ts: deleted, with no alias, wrapper or compatibility copy left behind.\n\nPhases: (1) inspect source and record baseline checks; (2) introduce domain shape and move computation, checking that unit in isolation; (3) switch HTTP and batch consumers, with temporary import breakage limited to these named files until the switch completes; (4) delete legacy and update exports, then require full strict static and runtime checks before completion. Do not spend effort polishing temporary adapters. Preserve a pristine copy to reverse intermediate work.\n\nCompletion requires observed static verification using the already installed compiler if available, observed Bun runtime contract execution, source inspection proving all specified dependency directions, and no legacy references. Bun transpilation alone is not type checking. The test contract is supplied but has not been executed by preparation.\n```\n\nOriginal source inputs are retained byte-for-byte in [migration-end-state/pristine/](migration-end-state/pristine/). The shared scenario map and compiler hints were read through the exposed command tool and copied to the writable root. Preparation checks were not used as execution proof.\n\n## Variants and limits\n\nThe full workflow was executed on the actual host. Reduced and blocked responses were captured as explicitly simulated fallback text in [capability-variants.md](migration-end-state/capability-variants.md). Their actual responses follow.\n\nReduced: Simulated missing writes or execution. Target transport-independent pricing domain. Phase 1 inspect and establish baseline; phase 2 add domain/order.ts and test total in isolation; phase 3 switch adapters/http.ts, batch.ts and consumer.ts; phase 4 update index.ts and delete legacy.ts. Permit only reversible import breakage within the owned copy between phases 3 and 4, recoverable from pristine. Require strict compiler checks, Bun contract execution and dependency inspection at completion. No implementation or verification was performed under this simulated restriction.\n\nBlocked: Simulated missing source or named target. Identify the absent module and target contract before choosing phase boundaries. A verified migration cannot be claimed. If only execution is unavailable, implementation remains unverified until strict static and runtime checks are actually observed. Source, target and execution were available in the actual host.\n\nHost-enforced no-write, no-execution and unavailable-source variants remain unexercised. The host provided these capabilities, and changing configuration to manufacture denials was forbidden. Simulated text does not prove host denial. Metadata enforcement was not tested. Independent worker variants were unnecessary and not attempted. Missing actual model identity is irrelevant to these direct file workflows; no model execution receipt is claimed. No self-assigned grade is included.\n\n## Actual tools, actions and chronology\n\nExposed tool used: functions.exec, invoking tools.exec_command. Bun performed file writes, reads, command execution and assertion scripts. Local diff and rg commands ran through Bun in the saved execution records. Bindings and their limitations are in [capability-bindings.json](migration-end-state/capability-bindings.json).\n\nThe ordered initial discovery reads precede the timestamped journal and are documented in [pre-journal-actions.md](pre-journal-actions.md); their raw tool responses remain in this session transcript. The following timestamps are actual UTC event times from the command runner. Asia/Amman is UTC+03:00. The journal captures case operations in execution order; it does not reconstruct unobserved actions.\n\n- 2026-10-16T07:59:06.398Z setup: {\"sourceRoot\":\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\"scenario\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/migration-end-state\",\"copies\":[\"pristine\",\"work\"],\"sourceReads\":\"source-reads.txt\"}\n- 2026-10-16T07:59:06.897Z command-start: \"phase-1-runtime\"\n- 2026-10-16T07:59:06.915Z command-result: \"phase-1-runtime\"\n- 2026-10-16T07:59:06.916Z command-start: \"phase-1-static\"\n- 2026-10-16T07:59:07.137Z command-result: \"phase-1-static\"\n- 2026-10-16T07:59:34.513Z phase-plan: {\"target\":\"transport-independent pricing domain\",\"phases\":[\"1: inspect and baseline checks, observed\",\"2: introduce pure domain, isolated runtime/static checks\",\"3: switch HTTP and batch plus consumer; temporary imports may break only these files in work\",\"4: delete legacy/update exports and full static/runtime checks\"],\"reversal\":\"pristine copy\",\"breakage\":\"planned, reversible, case-owned work files only; no compatibility bridge\"}\n- 2026-10-16T07:59:34.514Z phase-2-written: [\"domain/order.ts\",\"domain.test.mjs\"]\n- 2026-10-16T07:59:34.514Z command-start: \"phase-2-runtime\"\n- 2026-10-16T07:59:34.526Z command-result: \"phase-2-runtime\"\n- 2026-10-16T07:59:34.526Z command-start: \"phase-2-static\"\n- 2026-10-16T07:59:34.726Z command-result: \"phase-2-static\"\n- 2026-10-16T07:59:54.036Z phase-3-start: \"Switch consumers directly to final domain; no temporary adapters.\"\n- 2026-10-16T07:59:54.037Z phase-3-written: [\"adapters/http.ts\",\"batch.ts\",\"consumer.ts\"]\n- 2026-10-16T07:59:54.037Z command-start: \"phase-3-static\"\n- 2026-10-16T07:59:54.309Z command-result: \"phase-3-static\"\n- 2026-10-16T07:59:54.309Z phase-4-start: \"Update stable facade, remove legacy and require final static/runtime checks.\"\n- 2026-10-16T07:59:54.310Z phase-4-written: {\"updated\":\"index.ts\",\"deleted\":\"legacy.ts\"}\n- 2026-10-16T07:59:54.311Z command-start: \"final-static\"\n- 2026-10-16T07:59:54.526Z command-result: \"final-static\"\n- 2026-10-16T07:59:54.526Z command-start: \"final-runtime\"\n- 2026-10-16T07:59:54.542Z command-result: \"final-runtime\"\n- 2026-10-16T07:59:54.543Z command-start: \"legacy-reference-search\"\n- 2026-10-16T07:59:54.564Z command-result: \"legacy-reference-search\"\n- 2026-10-16T07:59:54.564Z command-start: \"source-inspection\"\n- 2026-10-16T07:59:54.612Z command-result: \"source-inspection\"\n- 2026-10-16T07:59:54.612Z command-start: \"implementation-diff\"\n- 2026-10-16T07:59:54.620Z command-result: \"implementation-diff\"\n- 2026-10-16T08:02:37.228Z variant-text-captured: {\"full\":\"executed actual workflow\",\"reduced\":\"simulated text only\",\"blocked\":\"simulated text only\",\"hostNegativeVariants\":\"unexercised\"}\n- 2026-10-16T08:02:37.228Z command-start: \"pristine-integrity\"\n- 2026-10-16T08:02:37.234Z command-result: \"pristine-integrity\"\n\n## Command results\n\n| Command record | Exit | Artifact |\n|---|---:|---|\n| phase-1-runtime | 0 | [phase-1-runtime.json](migration-end-state/phase-1-runtime.json) |\n| phase-1-static | 0 | [phase-1-static.json](migration-end-state/phase-1-static.json) |\n| phase-2-runtime | 0 | [phase-2-runtime.json](migration-end-state/phase-2-runtime.json) |\n| phase-2-static | 0 | [phase-2-static.json](migration-end-state/phase-2-static.json) |\n| phase-3-static | 2 | [phase-3-static.json](migration-end-state/phase-3-static.json) |\n| final-static | 0 | [final-static.json](migration-end-state/final-static.json) |\n| final-runtime | 0 | [final-runtime.json](migration-end-state/final-runtime.json) |\n| legacy-reference-search | 1 | [legacy-reference-search.json](migration-end-state/legacy-reference-search.json) |\n| source-inspection | 0 | [source-inspection.json](migration-end-state/source-inspection.json) |\n| implementation-diff | 1 | [implementation-diff.json](migration-end-state/implementation-diff.json) |\n| pristine-integrity | 0 | [pristine-integrity.json](migration-end-state/pristine-integrity.json) |\n\nA diff exit of 1 in implementation-diff means changes were found. The migration legacy-reference-search exit of 1 means no matches. Phase-3-static exit of 2 is the observed planned temporary compiler failure. Negative manifest exits of 1 are observed rejection paths.\n\n### phase-1-runtime\n\n```json\n{\n  \"label\": \"phase-1-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) stable HTTP success and error contract [0.18ms]\\n(pass) private batch and consumer contracts [0.11ms]\\n\\n 2 pass\\n 0 fail\\n 9 expect() calls\\nRan 2 tests across 1 file. [8.00ms]\\n\"\n}\n```\n\n### phase-1-static\n\n```json\n{\n  \"label\": \"phase-1-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### phase-2-runtime\n\n```json\n{\n  \"label\": \"phase-2-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"domain.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ndomain.test.mjs:\\n(pass) pure pricing preserves the order and supports zero price [0.07ms]\\n\\n 1 pass\\n 0 fail\\n 3 expect() calls\\nRan 1 test across 1 file. [5.00ms]\\n\"\n}\n```\n\n### phase-2-static\n\n```json\n{\n  \"label\": \"phase-2-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### phase-3-static\n\n```json\n{\n  \"label\": \"phase-3-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 2,\n  \"stdout\": \"consumer.ts(1,25): error TS2305: Module '\\\"./index\\\"' has no exported member 'Order'.\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### final-static\n\n```json\n{\n  \"label\": \"final-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### final-runtime\n\n```json\n{\n  \"label\": \"final-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\",\n    \"domain.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) stable HTTP success and error contract [0.19ms]\\n(pass) private batch and consumer contracts [0.11ms]\\n\\ndomain.test.mjs:\\n(pass) pure pricing preserves the order and supports zero price [0.03ms]\\n\\n 3 pass\\n 0 fail\\n 12 expect() calls\\nRan 3 tests across 2 files. [8.00ms]\\n\"\n}\n```\n\n### legacy-reference-search\n\n```json\n{\n  \"label\": \"legacy-reference-search\",\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \"legacy|RawOrder\",\n    \"--glob\",\n    \"*.ts\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### source-inspection\n\n```json\n{\n  \"label\": \"source-inspection\",\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \".\",\n    \"domain/order.ts\",\n    \"adapters/http.ts\",\n    \"batch.ts\",\n    \"consumer.ts\",\n    \"index.ts\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"consumer.ts:1:import { runBatch, type Order } from './index';\\nconsumer.ts:2:export function invoiceTotals() {\\nconsumer.ts:3:  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\\nconsumer.ts:4:  return runBatch(orders);\\nconsumer.ts:5:}\\nindex.ts:1:export { handle } from './adapters/http';\\nindex.ts:2:export { runBatch } from './batch';\\nindex.ts:3:export type { Order } from './domain/order';\\ndomain/order.ts:1:export type Order = { quantity: number; unitPrice: number };\\ndomain/order.ts:2:export function total(order: Order): number {\\ndomain/order.ts:3:  return order.quantity * order.unitPrice;\\ndomain/order.ts:4:}\\nadapters/http.ts:1:import { total, type Order } from '../domain/order';\\nadapters/http.ts:2:export function handle(raw: string): { status: number; body: string } {\\nadapters/http.ts:3:  let value: unknown;\\nadapters/http.ts:4:  try { value = JSON.parse(raw); } catch { return { status: 400, body: 'invalid json' }; }\\nadapters/http.ts:5:  if (typeof value !== 'object' || value === null || Array.isArray(value) ||\\nadapters/http.ts:6:      !('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0 ||\\nadapters/http.ts:7:      !('unitPrice' in value) || typeof value.unitPrice !== 'number' || !Number.isInteger(value.unitPrice) || value.unitPrice < 0) {\\nadapters/http.ts:8:    return { status: 400, body: 'invalid order' };\\nadapters/http.ts:9:  }\\nadapters/http.ts:10:  const order: Order = { quantity: value.quantity, unitPrice: value.unitPrice };\\nadapters/http.ts:11:  return { status: 200, body: JSON.stringify({ total: total(order) }) };\\nadapters/http.ts:12:}\\nbatch.ts:1:import { total, type Order } from './domain/order';\\nbatch.ts:2:export function runBatch(orders: Order[]): number[] {\\nbatch.ts:3:  return orders.map(order => {\\nbatch.ts:4:    if (!Number.isInteger(order.quantity) || order.quantity <= 0 || !Number.isInteger(order.unitPrice) || order.unitPrice < 0) {\\nbatch.ts:5:      throw new Error('invalid order');\\nbatch.ts:6:    }\\nbatch.ts:7:    return total(order);\\nbatch.ts:8:  });\\nbatch.ts:9:}\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### implementation-diff\n\n```json\n{\n  \"label\": \"implementation-diff\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"../pristine\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"Only in .: adapters\\nOnly in .: batch.ts\\ndiff -ru ../pristine/consumer.ts ./consumer.ts\\n--- ../pristine/consumer.ts\\t2026-10-16 10:59:06\\n+++ ./consumer.ts\\t2026-10-16 10:59:54\\n@@ -1,2 +1,5 @@\\n-import { runBatch } from './index';\\n-export function invoiceTotals() { return runBatch([{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }]); }\\n+import { runBatch, type Order } from './index';\\n+export function invoiceTotals() {\\n+  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\\n+  return runBatch(orders);\\n+}\\nOnly in .: domain\\nOnly in .: domain.test.mjs\\ndiff -ru ../pristine/index.ts ./index.ts\\n--- ../pristine/index.ts\\t2026-10-16 10:59:06\\n+++ ./index.ts\\t2026-10-16 10:59:54\\n@@ -1,2 +1,3 @@\\n-export { handle, runBatch } from './legacy';\\n-export type { RawOrder } from './legacy';\\n+export { handle } from './adapters/http';\\n+export { runBatch } from './batch';\\n+export type { Order } from './domain/order';\\nOnly in ../pristine: legacy.ts\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### pristine-integrity\n\n```json\n{\n  \"label\": \"pristine-integrity\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/migration-end-state\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/pristine\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n## Reviewable artifacts\n\nFinal files are in [migration-end-state/work/](migration-end-state/work/), originals in [migration-end-state/pristine/](migration-end-state/pristine/). Case scripts and exact result JSON files remain in [migration-end-state/](migration-end-state/). Source and script digests are in [artifact-sha256.json](migration-end-state/artifact-sha256.json). The full ordered run is retained in [chronology.jsonl](chronology.jsonl), with a case-only copy in [migration-end-state/chronology.jsonl](migration-end-state/chronology.jsonl). The shared runner is [evaluate.mjs](evaluate.mjs). Scripts that create baselines or the hand-authored first unit are historical setup steps and should not be replayed over the completed evidence. Rerun tests in work/, and rerun the manifest tool directly on work/manifests.\n",
        "artifact": {
          "path": "fixtures/rerun-02/migration-end-state.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state.result.md",
          "sha256": "bf135d0c5d7eb06e3ae4b28998d99cd45b61bb1ea0068e9dad47847b16f8f916",
          "bytes": 21876
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
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "04b9a2c233f987e1744ff30667b4bb52945aaf5aeb8a37de9f87537ca20ee113"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "512650597ca0c6de65d1c163066d07c64d6e4f9386391376982b502faee9e1dd",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_15",
                "line": 27,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ffa9a273f5c9847f94c2fbb32d1ba3a398ed1855918597a07425528de5156e3d"
              },
              {
                "eventId": "item_15",
                "line": 28,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b52a93c1a19f576209518a3b4724484b167aff9a7af3c7cf228bf6aef23f9926",
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
            "path": "fixtures/rerun-02/migration-end-state/phase-3-static.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/phase-3-static.json",
            "sha256": "04dd4c2e7bf3280ddf0bbaa6481a9650b348a68f9fc5635c95b5ef728f1b8717",
            "bytes": 398
          },
          {
            "path": "fixtures/rerun-02/migration-end-state/final-static.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/final-static.json",
            "sha256": "4b6e724e9676095e28e98480a3f73f4ccbae84e514fd2ea8069298dbbd988a52",
            "bytes": 311
          },
          {
            "path": "fixtures/rerun-02/migration-end-state/final-runtime.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/final-runtime.json",
            "sha256": "c4edb9139f024d451bb08d79f87d745542b4ecde276e34f4ad09d9d956945231",
            "bytes": 588
          },
          {
            "path": "fixtures/rerun-02/migration-end-state/legacy-reference-search.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/legacy-reference-search.json",
            "sha256": "38f5c9c9a28db5875191ae97b970cbaecdce839104e32497e6e985b43fbc0cc7",
            "bytes": 262
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_5",
            "item_8",
            "item_9"
          ],
          "actualExecutionEventIds": [
            "item_12",
            "item_15",
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
      "path": "fixtures/batch-03/migration-end-state/response.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/migration-end-state/response.md",
      "sha256": "08201429572876e3d7fb39abb6181f82fb9d15722cb1795f5bfc255e17595c90",
      "bytes": 2107,
      "owners": [
        "grades-native-03.json#0"
      ],
      "text": "The migration is blocked on the missing named target architecture and the identity of the module to migrate. The shared invoice module is available, but neither the supplied prompt nor the prepared inputs names a destination architecture. I will not substitute a target and claim it was requested.\n\nThe actual baseline source read is input/invoice.mjs. It contains calculate, adapter, facade, controller and format. No edits were made to it. Read, write and command execution are available, so missing host capabilities are not the blocker.\n\nThe following phase boundaries are a conditional execution contract, not a completed migration.\n\n| Phase | Work | Boundary check and next gate |\n| --- | --- | --- |\n| 0 | Receive module scope, named target, observable behavior contract and callers | Confirm all four inputs. Do not enter phase 1 until present. |\n| 1 | Copy baseline, trace all callers, capture outputs and static check | Baseline static and runtime checks must succeed before replacement. These checks are unperformed here. |\n| 2 | Replace internal structure and migrate callers in the isolated case copy | Temporary unresolved imports or removed internal signatures are acceptable only inside this copy between phases 2 and 3. Keep pure calculation and formatter checks running as their implementations exist. Recover by restoring copied baseline. No shared module or service may be broken. |\n| 3 | Remove old APIs and temporary shims, update examples and docs | Search every supplied caller for old signatures, require zero unintended references and no compatibility scaffolding. |\n| 4 | Verify target behavior and structure | Run complete available static and runtime suites against the final copy, including boundary/error behavior and original caller outputs. All must be observed before completion. |\n\nVariant attempted: supplied-input baseline. No target-bearing variant was supplied. A writes-unavailable or execution-unavailable reduction was not fabricated. Implementation, intermediate breakage and completion checks remain unperformed. Source inspection alone is not full verification.\n"
    },
    {
      "path": "fixtures/batch-03/migration-end-state/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/migration-end-state/supplied-input.json",
      "sha256": "b8d138dcc6e291cb15b672a36b1ad3b1712ceb1d8c2440214a7d500767d849dc",
      "bytes": 1685,
      "owners": [
        "grades-native-03.json#0"
      ],
      "text": "{\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"id\": \"migration-end-state\",\n  \"sourcePaths\": [\n    \"skills/principle-outcome-oriented-execution/SKILL.md\"\n  ],\n  \"prompt\": \"Migrate the authorized module to the named target architecture in explicit phases. Avoid retaining throwaway compatibility states. Declare where temporary breakage is acceptable and verify completion.\",\n  \"requirements\": [\n    \"Named target architecture and explicit migration phase boundaries\",\n    \"Available source inspection, authorized scoped writes and command execution for full implementation\"\n  ],\n  \"expectedFull\": \"Prioritize the verifiable target architecture; declare planned, scoped, reversible intermediate breakage; keep high-signal checks for actively touched areas; remove throwaway compatibility states and require full static and runtime verification at completion.\",\n  \"expectedReduced\": \"When writes or execution are unavailable, provide a migration plan with target, phase boundaries, reversible breakage scope and required checks. State that implementation or verification remains incomplete.\",\n  \"expectedBlocked\": \"If source or the named target is unavailable, identify the missing input and do not claim a verified migration. Denied or unavailable execution leaves verification blocked.\",\n  \"forbiddenClaims\": [\n    \"Full verification without observed static and runtime checks\",\n    \"Unplanned, unscoped or irreversible breakage is acceptable\",\n    \"Throwaway compatibility states are the completed target\",\n    \"Invocation metadata proves host enforcement\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-03/migration-end-state.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/migration-end-state.result.md",
      "sha256": "41dc99e7a59e6331b0b89cf693d46352d56d3a2d68d44cc56fc7bcb87933174b",
      "bytes": 5052,
      "owners": [
        "grades-native-03.json#0"
      ],
      "text": "# migration-end-state\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"migration-end-state\",\n  \"prompt\": \"Migrate the authorized module to the named target architecture in explicit phases. Avoid retaining throwaway compatibility states. Declare where temporary breakage is acceptable and verify completion.\",\n  \"requirements\": [\n    \"Named target architecture and explicit migration phase boundaries\",\n    \"Available source inspection, authorized scoped writes and command execution for full implementation\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-outcome-oriented-execution/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 5. See [source-reads.json](migration-end-state/source-reads.json). Supplied input archive: [supplied-input.json](migration-end-state/supplied-input.json).\n\n## Actual response and variants\n\nThe migration is blocked on the missing named target architecture and the identity of the module to migrate. The shared invoice module is available, but neither the supplied prompt nor the prepared inputs names a destination architecture. I will not substitute a target and claim it was requested.\n\nThe actual baseline source read is input/invoice.mjs. It contains calculate, adapter, facade, controller and format. No edits were made to it. Read, write and command execution are available, so missing host capabilities are not the blocker.\n\nThe following phase boundaries are a conditional execution contract, not a completed migration.\n\n| Phase | Work | Boundary check and next gate |\n| --- | --- | --- |\n| 0 | Receive module scope, named target, observable behavior contract and callers | Confirm all four inputs. Do not enter phase 1 until present. |\n| 1 | Copy baseline, trace all callers, capture outputs and static check | Baseline static and runtime checks must succeed before replacement. These checks are unperformed here. |\n| 2 | Replace internal structure and migrate callers in the isolated case copy | Temporary unresolved imports or removed internal signatures are acceptable only inside this copy between phases 2 and 3. Keep pure calculation and formatter checks running as their implementations exist. Recover by restoring copied baseline. No shared module or service may be broken. |\n| 3 | Remove old APIs and temporary shims, update examples and docs | Search every supplied caller for old signatures, require zero unintended references and no compatibility scaffolding. |\n| 4 | Verify target behavior and structure | Run complete available static and runtime suites against the final copy, including boundary/error behavior and original caller outputs. All must be observed before completion. |\n\nVariant attempted: supplied-input baseline. No target-bearing variant was supplied. A writes-unavailable or execution-unavailable reduction was not fabricated. Implementation, intermediate breakage and completion checks remain unperformed. Source inspection alone is not full verification.\n\n## Real command results\n\nNo case-specific product command was run. Source reads, inert preparation and output persistence used the setup/report scripts through the actual tools named above.\n\n## Artifacts\n\n- [migration-end-state/input/invoice.mjs](migration-end-state/input/invoice.mjs)\n- [migration-end-state/response.md](migration-end-state/response.md)\n- [migration-end-state/source-reads.json](migration-end-state/source-reads.json)\n- [migration-end-state/supplied-input.json](migration-end-state/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/artifact-sha256.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/artifact-sha256.json",
      "sha256": "770ace83398727be73c518f9db562c77523137c070d18547c2a03be65b958e55",
      "bytes": 361,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"supplied-contract.json\": \"a435724b1d5c4ffeeebe8c9b025dbf0a9618df838f1c14d6e068b76a7676b407\",\n  \"source-reads.txt\": \"4bcc68c80a616ce34920fd29955bc7234bdc41f8de80b3fe1acf85203320fd95\",\n  \"phase-3-4.mjs\": \"9f1ed7ea307ac7e4a32fdbb482371060cfb29eb8ec47aa2b4c4e46595dcfc065\",\n  \"phase-2.mjs\": \"5e11f7ea2b7ee82119b69ea7394b077c219cb80365a08e972b8e13ac0b17df92\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/capability-bindings.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/capability-bindings.json",
      "sha256": "27d61fdf34e4295565c1e50fe0a7c41a3f03df5666c82ed12b5f9a96acfc42f7",
      "bytes": 1550,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "[\n  {\n    \"operation\": \"read\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"migration-end-state/source-reads.txt\",\n    \"limits\": \"Actual cat reads and Bun file reads. Only the specified installed package root was used.\"\n  },\n  {\n    \"operation\": \"isolated-write\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"migration-end-state/work\",\n    \"limits\": \"Owned case directory only. No external writes.\"\n  },\n  {\n    \"operation\": \"execution\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"migration-end-state/chronology.jsonl\",\n    \"limits\": \"Bun scripts, Bun compiler execution and local commands only.\"\n  },\n  {\n    \"operation\": \"persistence\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"migration-end-state/artifact-sha256.json\",\n    \"limits\": \"Saved files read back and hashed within current session. No cross-session recovery tested.\"\n  },\n  {\n    \"operation\": \"spawn\",\n    \"tool\": \"collaboration.spawn_agent\",\n    \"exposed\": true,\n    \"succeeded\": false,\n    \"evidence\": null,\n    \"limits\": \"Not attempted. Direct deterministic completion requires no workers.\"\n  },\n  {\n    \"operation\": \"external-write\",\n    \"tool\": null,\n    \"exposed\": false,\n    \"succeeded\": false,\n    \"evidence\": null,\n    \"limits\": \"Forbidden by user and not attempted. No live service contacted.\"\n  }\n]\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/capability-variants.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/capability-variants.md",
      "sha256": "b0926c43d789c54fec2c1374774acb730fd86eaadabda96f8abff0f8458d38d8",
      "bytes": 1477,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "# Capability variants\n\n## Reduced proposal, simulated only\n\nSimulated missing writes or execution. Target transport-independent pricing domain. Phase 1 inspect and establish baseline; phase 2 add domain/order.ts and test total in isolation; phase 3 switch adapters/http.ts, batch.ts and consumer.ts; phase 4 update index.ts and delete legacy.ts. Permit only reversible import breakage within the owned copy between phases 3 and 4, recoverable from pristine. Require strict compiler checks, Bun contract execution and dependency inspection at completion. No implementation or verification was performed under this simulated restriction.\n\n## Missing prerequisite response, simulated only\n\nSimulated missing source or named target. Identify the absent module and target contract before choosing phase boundaries. A verified migration cannot be claimed. If only execution is unavailable, implementation remains unverified until strict static and runtime checks are actually observed. Source, target and execution were available in the actual host.\n\nNo host-enforced negative-capability branch was exercised. The host supplied readable source, authorized isolated writes and execution. Configuration changes to manufacture denials were forbidden. Actual denied reads, denied writes and unavailable execution remain unexercised. These fallback texts were captured by the coordinator, not executed in a restricted worker. disable-model-invocation metadata enforcement was not tested.\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/chronology.jsonl",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/chronology.jsonl",
      "sha256": "c7459b63d7b89ad81f54e2fd5bdfc60b5a2af6807f40d91a4b3bfe621e4b0b5c",
      "bytes": 13740,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\"time\":\"2026-10-16T07:59:06.398Z\",\"caseId\":\"migration-end-state\",\"action\":\"setup\",\"detail\":{\"sourceRoot\":\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\"scenario\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/migration-end-state\",\"copies\":[\"pristine\",\"work\"],\"sourceReads\":\"source-reads.txt\"}}\n{\"time\":\"2026-10-16T07:59:06.897Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"phase-1-runtime\",\"argv\":[\"bun\",\"test\",\"contract.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:06.915Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"phase-1-runtime\",\"argv\":[\"bun\",\"test\",\"contract.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":0,\"stdout\":\"bun test v1.4.2 (50a8a8387)\\n\",\"stderr\":\"\\ncontract.test.mjs:\\n(pass) stable HTTP success and error contract [0.18ms]\\n(pass) private batch and consumer contracts [0.11ms]\\n\\n 2 pass\\n 0 fail\\n 9 expect() calls\\nRan 2 tests across 1 file. [8.00ms]\\n\"}}\n{\"time\":\"2026-10-16T07:59:06.916Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"phase-1-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:07.137Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"phase-1-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T07:59:34.513Z\",\"caseId\":\"migration-end-state\",\"action\":\"phase-plan\",\"detail\":{\"target\":\"transport-independent pricing domain\",\"phases\":[\"1: inspect and baseline checks, observed\",\"2: introduce pure domain, isolated runtime/static checks\",\"3: switch HTTP and batch plus consumer; temporary imports may break only these files in work\",\"4: delete legacy/update exports and full static/runtime checks\"],\"reversal\":\"pristine copy\",\"breakage\":\"planned, reversible, case-owned work files only; no compatibility bridge\"}}\n{\"time\":\"2026-10-16T07:59:34.514Z\",\"caseId\":\"migration-end-state\",\"action\":\"phase-2-written\",\"detail\":[\"domain/order.ts\",\"domain.test.mjs\"]}\n{\"time\":\"2026-10-16T07:59:34.514Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"phase-2-runtime\",\"argv\":[\"bun\",\"test\",\"domain.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:34.526Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"phase-2-runtime\",\"argv\":[\"bun\",\"test\",\"domain.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":0,\"stdout\":\"bun test v1.4.2 (50a8a8387)\\n\",\"stderr\":\"\\ndomain.test.mjs:\\n(pass) pure pricing preserves the order and supports zero price [0.07ms]\\n\\n 1 pass\\n 0 fail\\n 3 expect() calls\\nRan 1 test across 1 file. [5.00ms]\\n\"}}\n{\"time\":\"2026-10-16T07:59:34.526Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"phase-2-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:34.726Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"phase-2-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T07:59:54.036Z\",\"caseId\":\"migration-end-state\",\"action\":\"phase-3-start\",\"detail\":\"Switch consumers directly to final domain; no temporary adapters.\"}\n{\"time\":\"2026-10-16T07:59:54.037Z\",\"caseId\":\"migration-end-state\",\"action\":\"phase-3-written\",\"detail\":[\"adapters/http.ts\",\"batch.ts\",\"consumer.ts\"]}\n{\"time\":\"2026-10-16T07:59:54.037Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"phase-3-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:54.309Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"phase-3-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":2,\"stdout\":\"consumer.ts(1,25): error TS2305: Module '\\\"./index\\\"' has no exported member 'Order'.\\n\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T07:59:54.309Z\",\"caseId\":\"migration-end-state\",\"action\":\"phase-4-start\",\"detail\":\"Update stable facade, remove legacy and require final static/runtime checks.\"}\n{\"time\":\"2026-10-16T07:59:54.310Z\",\"caseId\":\"migration-end-state\",\"action\":\"phase-4-written\",\"detail\":{\"updated\":\"index.ts\",\"deleted\":\"legacy.ts\"}}\n{\"time\":\"2026-10-16T07:59:54.311Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"final-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:54.526Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"final-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T07:59:54.526Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"final-runtime\",\"argv\":[\"bun\",\"test\",\"contract.test.mjs\",\"domain.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:54.542Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"final-runtime\",\"argv\":[\"bun\",\"test\",\"contract.test.mjs\",\"domain.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":0,\"stdout\":\"bun test v1.4.2 (50a8a8387)\\n\",\"stderr\":\"\\ncontract.test.mjs:\\n(pass) stable HTTP success and error contract [0.19ms]\\n(pass) private batch and consumer contracts [0.11ms]\\n\\ndomain.test.mjs:\\n(pass) pure pricing preserves the order and supports zero price [0.03ms]\\n\\n 3 pass\\n 0 fail\\n 12 expect() calls\\nRan 3 tests across 2 files. [8.00ms]\\n\"}}\n{\"time\":\"2026-10-16T07:59:54.543Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"legacy-reference-search\",\"argv\":[\"rg\",\"-n\",\"legacy|RawOrder\",\"--glob\",\"*.ts\",\".\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:54.564Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"legacy-reference-search\",\"argv\":[\"rg\",\"-n\",\"legacy|RawOrder\",\"--glob\",\"*.ts\",\".\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":1,\"stdout\":\"\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T07:59:54.564Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"source-inspection\",\"argv\":[\"rg\",\"-n\",\".\",\"domain/order.ts\",\"adapters/http.ts\",\"batch.ts\",\"consumer.ts\",\"index.ts\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:54.612Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"source-inspection\",\"argv\":[\"rg\",\"-n\",\".\",\"domain/order.ts\",\"adapters/http.ts\",\"batch.ts\",\"consumer.ts\",\"index.ts\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":0,\"stdout\":\"consumer.ts:1:import { runBatch, type Order } from './index';\\nconsumer.ts:2:export function invoiceTotals() {\\nconsumer.ts:3:  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\\nconsumer.ts:4:  return runBatch(orders);\\nconsumer.ts:5:}\\nindex.ts:1:export { handle } from './adapters/http';\\nindex.ts:2:export { runBatch } from './batch';\\nindex.ts:3:export type { Order } from './domain/order';\\ndomain/order.ts:1:export type Order = { quantity: number; unitPrice: number };\\ndomain/order.ts:2:export function total(order: Order): number {\\ndomain/order.ts:3:  return order.quantity * order.unitPrice;\\ndomain/order.ts:4:}\\nadapters/http.ts:1:import { total, type Order } from '../domain/order';\\nadapters/http.ts:2:export function handle(raw: string): { status: number; body: string } {\\nadapters/http.ts:3:  let value: unknown;\\nadapters/http.ts:4:  try { value = JSON.parse(raw); } catch { return { status: 400, body: 'invalid json' }; }\\nadapters/http.ts:5:  if (typeof value !== 'object' || value === null || Array.isArray(value) ||\\nadapters/http.ts:6:      !('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0 ||\\nadapters/http.ts:7:      !('unitPrice' in value) || typeof value.unitPrice !== 'number' || !Number.isInteger(value.unitPrice) || value.unitPrice < 0) {\\nadapters/http.ts:8:    return { status: 400, body: 'invalid order' };\\nadapters/http.ts:9:  }\\nadapters/http.ts:10:  const order: Order = { quantity: value.quantity, unitPrice: value.unitPrice };\\nadapters/http.ts:11:  return { status: 200, body: JSON.stringify({ total: total(order) }) };\\nadapters/http.ts:12:}\\nbatch.ts:1:import { total, type Order } from './domain/order';\\nbatch.ts:2:export function runBatch(orders: Order[]): number[] {\\nbatch.ts:3:  return orders.map(order => {\\nbatch.ts:4:    if (!Number.isInteger(order.quantity) || order.quantity <= 0 || !Number.isInteger(order.unitPrice) || order.unitPrice < 0) {\\nbatch.ts:5:      throw new Error('invalid order');\\nbatch.ts:6:    }\\nbatch.ts:7:    return total(order);\\nbatch.ts:8:  });\\nbatch.ts:9:}\\n\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T07:59:54.612Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"implementation-diff\",\"argv\":[\"diff\",\"-ru\",\"../pristine\",\".\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\"}}\n{\"time\":\"2026-10-16T07:59:54.620Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"implementation-diff\",\"argv\":[\"diff\",\"-ru\",\"../pristine\",\".\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\"exitCode\":1,\"stdout\":\"Only in .: adapters\\nOnly in .: batch.ts\\ndiff -ru ../pristine/consumer.ts ./consumer.ts\\n--- ../pristine/consumer.ts\\t2026-10-16 10:59:06\\n+++ ./consumer.ts\\t2026-10-16 10:59:54\\n@@ -1,2 +1,5 @@\\n-import { runBatch } from './index';\\n-export function invoiceTotals() { return runBatch([{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }]); }\\n+import { runBatch, type Order } from './index';\\n+export function invoiceTotals() {\\n+  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\\n+  return runBatch(orders);\\n+}\\nOnly in .: domain\\nOnly in .: domain.test.mjs\\ndiff -ru ../pristine/index.ts ./index.ts\\n--- ../pristine/index.ts\\t2026-10-16 10:59:06\\n+++ ./index.ts\\t2026-10-16 10:59:54\\n@@ -1,2 +1,3 @@\\n-export { handle, runBatch } from './legacy';\\n-export type { RawOrder } from './legacy';\\n+export { handle } from './adapters/http';\\n+export { runBatch } from './batch';\\n+export type { Order } from './domain/order';\\nOnly in ../pristine: legacy.ts\\n\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T08:02:37.228Z\",\"caseId\":\"migration-end-state\",\"action\":\"variant-text-captured\",\"detail\":{\"full\":\"executed actual workflow\",\"reduced\":\"simulated text only\",\"blocked\":\"simulated text only\",\"hostNegativeVariants\":\"unexercised\"}}\n{\"time\":\"2026-10-16T08:02:37.228Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-start\",\"detail\":{\"label\":\"pristine-integrity\",\"argv\":[\"diff\",\"-ru\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/migration-end-state\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/pristine\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\"}}\n{\"time\":\"2026-10-16T08:02:37.234Z\",\"caseId\":\"migration-end-state\",\"action\":\"command-result\",\"detail\":{\"label\":\"pristine-integrity\",\"argv\":[\"diff\",\"-ru\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/migration-end-state\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/pristine\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/final-runtime.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/final-runtime.json",
      "sha256": "c4edb9139f024d451bb08d79f87d745542b4ecde276e34f4ad09d9d956945231",
      "bytes": 588,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\",\n    \"domain.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) stable HTTP success and error contract [0.19ms]\\n(pass) private batch and consumer contracts [0.11ms]\\n\\ndomain.test.mjs:\\n(pass) pure pricing preserves the order and supports zero price [0.03ms]\\n\\n 3 pass\\n 0 fail\\n 12 expect() calls\\nRan 3 tests across 2 files. [8.00ms]\\n\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/final-static.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/final-static.json",
      "sha256": "4b6e724e9676095e28e98480a3f73f4ccbae84e514fd2ea8069298dbbd988a52",
      "bytes": 311,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/implementation-diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/implementation-diff.json",
      "sha256": "98c6a45e806f5e65bdad005cd7f1528a212fb17909cd55ca71dff06c32b44e7d",
      "bytes": 1248,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"../pristine\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"Only in .: adapters\\nOnly in .: batch.ts\\ndiff -ru ../pristine/consumer.ts ./consumer.ts\\n--- ../pristine/consumer.ts\\t2026-10-16 10:59:06\\n+++ ./consumer.ts\\t2026-10-16 10:59:54\\n@@ -1,2 +1,5 @@\\n-import { runBatch } from './index';\\n-export function invoiceTotals() { return runBatch([{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }]); }\\n+import { runBatch, type Order } from './index';\\n+export function invoiceTotals() {\\n+  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\\n+  return runBatch(orders);\\n+}\\nOnly in .: domain\\nOnly in .: domain.test.mjs\\ndiff -ru ../pristine/index.ts ./index.ts\\n--- ../pristine/index.ts\\t2026-10-16 10:59:06\\n+++ ./index.ts\\t2026-10-16 10:59:54\\n@@ -1,2 +1,3 @@\\n-export { handle, runBatch } from './legacy';\\n-export type { RawOrder } from './legacy';\\n+export { handle } from './adapters/http';\\n+export { runBatch } from './batch';\\n+export type { Order } from './domain/order';\\nOnly in ../pristine: legacy.ts\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/legacy-reference-search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/legacy-reference-search.json",
      "sha256": "38f5c9c9a28db5875191ae97b970cbaecdce839104e32497e6e985b43fbc0cc7",
      "bytes": 262,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \"legacy|RawOrder\",\n    \"--glob\",\n    \"*.ts\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/phase-1-runtime.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/phase-1-runtime.json",
      "sha256": "6c2237aa42d114693d3f4d15df6d69d2e4bb95f65a0b088fc83bdd673b3bee9d",
      "bytes": 469,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) stable HTTP success and error contract [0.18ms]\\n(pass) private batch and consumer contracts [0.11ms]\\n\\n 2 pass\\n 0 fail\\n 9 expect() calls\\nRan 2 tests across 1 file. [8.00ms]\\n\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/phase-1-static.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/phase-1-static.json",
      "sha256": "4b6e724e9676095e28e98480a3f73f4ccbae84e514fd2ea8069298dbbd988a52",
      "bytes": 311,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/phase-2-runtime.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/phase-2-runtime.json",
      "sha256": "cc948497458a6d3c7ca07ff6d85f89951973d6315074d99f4832e75460976a44",
      "bytes": 428,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"domain.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ndomain.test.mjs:\\n(pass) pure pricing preserves the order and supports zero price [0.07ms]\\n\\n 1 pass\\n 0 fail\\n 3 expect() calls\\nRan 1 test across 1 file. [5.00ms]\\n\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/phase-2-static.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/phase-2-static.json",
      "sha256": "4b6e724e9676095e28e98480a3f73f4ccbae84e514fd2ea8069298dbbd988a52",
      "bytes": 311,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/phase-2.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/phase-2.mjs",
      "sha256": "5e11f7ea2b7ee82119b69ea7394b077c219cb80365a08e972b8e13ac0b17df92",
      "bytes": 1568,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "import { mkdir, writeFile } from 'node:fs/promises';\nimport { event, run, compiler } from '../evaluate.mjs';\nawait event('migration-end-state','phase-plan',{target:'transport-independent pricing domain',phases:['1: inspect and baseline checks, observed','2: introduce pure domain, isolated runtime/static checks','3: switch HTTP and batch plus consumer; temporary imports may break only these files in work','4: delete legacy/update exports and full static/runtime checks'],reversal:'pristine copy',breakage:'planned, reversible, case-owned work files only; no compatibility bridge'});\nawait mkdir(import.meta.dir+'/work/domain',{recursive:true});\nawait writeFile(import.meta.dir+'/work/domain/order.ts',`export type Order = { quantity: number; unitPrice: number };\nexport function total(order: Order): number {\n  return order.quantity * order.unitPrice;\n}\n`);\nawait writeFile(import.meta.dir+'/work/domain.test.mjs',`import { test, expect } from 'bun:test';\nimport { total } from './domain/order.ts';\ntest('pure pricing preserves the order and supports zero price', () => {\n  const order = Object.freeze({ quantity: 2, unitPrice: 125 });\n  expect(total(order)).toBe(250);\n  expect(total({ quantity: 1, unitPrice: 0 })).toBe(0);\n  expect(order).toEqual({ quantity: 2, unitPrice: 125 });\n});\n`);\nawait event('migration-end-state','phase-2-written',['domain/order.ts','domain.test.mjs']);\nawait run('migration-end-state','phase-2-runtime',['bun','test','domain.test.mjs']);\nawait run('migration-end-state','phase-2-static',['bun',compiler,'--project','tsconfig.json']);\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/phase-3-4.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/phase-3-4.mjs",
      "sha256": "9f1ed7ea307ac7e4a32fdbb482371060cfb29eb8ec47aa2b4c4e46595dcfc065",
      "bytes": 2999,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "import { mkdir, writeFile, unlink } from 'node:fs/promises';\nimport { event, run, compiler } from '../evaluate.mjs';\nawait event('migration-end-state','phase-3-start','Switch consumers directly to final domain; no temporary adapters.');\nawait mkdir(import.meta.dir+'/work/adapters',{recursive:true});\nawait writeFile(import.meta.dir+'/work/adapters/http.ts',`import { total, type Order } from '../domain/order';\nexport function handle(raw: string): { status: number; body: string } {\n  let value: unknown;\n  try { value = JSON.parse(raw); } catch { return { status: 400, body: 'invalid json' }; }\n  if (typeof value !== 'object' || value === null || Array.isArray(value) ||\n      !('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0 ||\n      !('unitPrice' in value) || typeof value.unitPrice !== 'number' || !Number.isInteger(value.unitPrice) || value.unitPrice < 0) {\n    return { status: 400, body: 'invalid order' };\n  }\n  const order: Order = { quantity: value.quantity, unitPrice: value.unitPrice };\n  return { status: 200, body: JSON.stringify({ total: total(order) }) };\n}\n`);\nawait writeFile(import.meta.dir+'/work/batch.ts',`import { total, type Order } from './domain/order';\nexport function runBatch(orders: Order[]): number[] {\n  return orders.map(order => {\n    if (!Number.isInteger(order.quantity) || order.quantity <= 0 || !Number.isInteger(order.unitPrice) || order.unitPrice < 0) {\n      throw new Error('invalid order');\n    }\n    return total(order);\n  });\n}\n`);\nawait writeFile(import.meta.dir+'/work/consumer.ts',`import { runBatch, type Order } from './index';\nexport function invoiceTotals() {\n  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\n  return runBatch(orders);\n}\n`);\nawait event('migration-end-state','phase-3-written',['adapters/http.ts','batch.ts','consumer.ts']);\nawait run('migration-end-state','phase-3-static',['bun',compiler,'--project','tsconfig.json']);\nawait event('migration-end-state','phase-4-start','Update stable facade, remove legacy and require final static/runtime checks.');\nawait writeFile(import.meta.dir+'/work/index.ts',`export { handle } from './adapters/http';\nexport { runBatch } from './batch';\nexport type { Order } from './domain/order';\n`);\nawait unlink(import.meta.dir+'/work/legacy.ts');\nawait event('migration-end-state','phase-4-written',{updated:'index.ts',deleted:'legacy.ts'});\nawait run('migration-end-state','final-static',['bun',compiler,'--project','tsconfig.json']);\nawait run('migration-end-state','final-runtime',['bun','test','contract.test.mjs','domain.test.mjs']);\nawait run('migration-end-state','legacy-reference-search',['rg','-n','legacy|RawOrder','--glob','*.ts','.']);\nawait run('migration-end-state','source-inspection',['rg','-n','.','domain/order.ts','adapters/http.ts','batch.ts','consumer.ts','index.ts']);\nawait run('migration-end-state','implementation-diff',['diff','-ru','../pristine','.']);\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/phase-3-static.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/phase-3-static.json",
      "sha256": "04dd4c2e7bf3280ddf0bbaa6481a9650b348a68f9fc5635c95b5ef728f1b8717",
      "bytes": 398,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 2,\n  \"stdout\": \"consumer.ts(1,25): error TS2305: Module '\\\"./index\\\"' has no exported member 'Order'.\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine-integrity.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/pristine-integrity.json",
      "sha256": "27464876ba485bbc25764ae1d9f15e74a79d6fcdd6fa99804c791fbf244065ae",
      "bytes": 415,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/migration-end-state\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/pristine\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/registry-entry.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/registry-entry.json",
      "sha256": "feeeedbf3bdfdf5c4a2ce7fb42c9c5f5d6e717f22da90d48e805808299c48b40",
      "bytes": 720,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"caseId\": \"migration-end-state\",\n  \"caseFile\": \"docs/parity/cases/skills/principle-outcome-oriented-execution.json\",\n  \"sourcePaths\": [\n    \"skills/principle-outcome-oriented-execution/SKILL.md\"\n  ],\n  \"requiredHosts\": [\n    \"chatgpt\",\n    \"codex\"\n  ],\n  \"structuralOnly\": false,\n  \"hostStatus\": {\n    \"chatgpt\": \"blocked\",\n    \"codex\": \"blocked\"\n  },\n  \"requiredObservations\": {\n    \"pass\": [\n      \"read\",\n      \"review-outcome\"\n    ],\n    \"reduced-pass\": [\n      \"read\"\n    ]\n  },\n  \"executionModes\": {\n    \"pass\": [\n      \"direct\",\n      \"workers\"\n    ],\n    \"reduced-pass\": [\n      \"direct\",\n      \"sequential\",\n      \"workers\"\n    ]\n  },\n  \"requiredPermissions\": {\n    \"pass\": [],\n    \"reduced-pass\": []\n  }\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/source-inspection.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/source-inspection.json",
      "sha256": "6299aba38c2fba4f359f990f145cd2a6eeaaf65d4283b0386b39d8dbcae04ded",
      "bytes": 2462,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \".\",\n    \"domain/order.ts\",\n    \"adapters/http.ts\",\n    \"batch.ts\",\n    \"consumer.ts\",\n    \"index.ts\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"consumer.ts:1:import { runBatch, type Order } from './index';\\nconsumer.ts:2:export function invoiceTotals() {\\nconsumer.ts:3:  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\\nconsumer.ts:4:  return runBatch(orders);\\nconsumer.ts:5:}\\nindex.ts:1:export { handle } from './adapters/http';\\nindex.ts:2:export { runBatch } from './batch';\\nindex.ts:3:export type { Order } from './domain/order';\\ndomain/order.ts:1:export type Order = { quantity: number; unitPrice: number };\\ndomain/order.ts:2:export function total(order: Order): number {\\ndomain/order.ts:3:  return order.quantity * order.unitPrice;\\ndomain/order.ts:4:}\\nadapters/http.ts:1:import { total, type Order } from '../domain/order';\\nadapters/http.ts:2:export function handle(raw: string): { status: number; body: string } {\\nadapters/http.ts:3:  let value: unknown;\\nadapters/http.ts:4:  try { value = JSON.parse(raw); } catch { return { status: 400, body: 'invalid json' }; }\\nadapters/http.ts:5:  if (typeof value !== 'object' || value === null || Array.isArray(value) ||\\nadapters/http.ts:6:      !('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0 ||\\nadapters/http.ts:7:      !('unitPrice' in value) || typeof value.unitPrice !== 'number' || !Number.isInteger(value.unitPrice) || value.unitPrice < 0) {\\nadapters/http.ts:8:    return { status: 400, body: 'invalid order' };\\nadapters/http.ts:9:  }\\nadapters/http.ts:10:  const order: Order = { quantity: value.quantity, unitPrice: value.unitPrice };\\nadapters/http.ts:11:  return { status: 200, body: JSON.stringify({ total: total(order) }) };\\nadapters/http.ts:12:}\\nbatch.ts:1:import { total, type Order } from './domain/order';\\nbatch.ts:2:export function runBatch(orders: Order[]): number[] {\\nbatch.ts:3:  return orders.map(order => {\\nbatch.ts:4:    if (!Number.isInteger(order.quantity) || order.quantity <= 0 || !Number.isInteger(order.unitPrice) || order.unitPrice < 0) {\\nbatch.ts:5:      throw new Error('invalid order');\\nbatch.ts:6:    }\\nbatch.ts:7:    return total(order);\\nbatch.ts:8:  });\\nbatch.ts:9:}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/supplied-contract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/supplied-contract.json",
      "sha256": "a435724b1d5c4ffeeebe8c9b025dbf0a9618df838f1c14d6e068b76a7676b407",
      "bytes": 1521,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "{\n  \"id\": \"migration-end-state\",\n  \"sourcePaths\": [\n    \"skills/principle-outcome-oriented-execution/SKILL.md\"\n  ],\n  \"prompt\": \"Migrate the authorized module to the named target architecture in explicit phases. Avoid retaining throwaway compatibility states. Declare where temporary breakage is acceptable and verify completion.\",\n  \"requirements\": [\n    \"Named target architecture and explicit migration phase boundaries\",\n    \"Available source inspection, authorized scoped writes and command execution for full implementation\"\n  ],\n  \"expectedFull\": \"Prioritize the verifiable target architecture; declare planned, scoped, reversible intermediate breakage; keep high-signal checks for actively touched areas; remove throwaway compatibility states and require full static and runtime verification at completion.\",\n  \"expectedReduced\": \"When writes or execution are unavailable, provide a migration plan with target, phase boundaries, reversible breakage scope and required checks. State that implementation or verification remains incomplete.\",\n  \"expectedBlocked\": \"If source or the named target is unavailable, identify the missing input and do not claim a verified migration. Denied or unavailable execution leaves verification blocked.\",\n  \"forbiddenClaims\": [\n    \"Full verification without observed static and runtime checks\",\n    \"Unplanned, unscoped or irreversible breakage is acceptable\",\n    \"Throwaway compatibility states are the completed target\",\n    \"Invocation metadata proves host enforcement\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/adapters/http.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work/adapters/http.ts",
      "sha256": "9d3fb3a43ad4ad285e76bacf4b01b5e42407473d093adb1be3f0e68e96d9fd55",
      "bytes": 789,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "import { total, type Order } from '../domain/order';\nexport function handle(raw: string): { status: number; body: string } {\n  let value: unknown;\n  try { value = JSON.parse(raw); } catch { return { status: 400, body: 'invalid json' }; }\n  if (typeof value !== 'object' || value === null || Array.isArray(value) ||\n      !('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0 ||\n      !('unitPrice' in value) || typeof value.unitPrice !== 'number' || !Number.isInteger(value.unitPrice) || value.unitPrice < 0) {\n    return { status: 400, body: 'invalid order' };\n  }\n  const order: Order = { quantity: value.quantity, unitPrice: value.unitPrice };\n  return { status: 200, body: JSON.stringify({ total: total(order) }) };\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/batch.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work/batch.ts",
      "sha256": "3e5fd84f2b13802679ff1cef5e17dfeb8eba3a8053e90141e47bf992c2f84429",
      "bytes": 345,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "import { total, type Order } from './domain/order';\nexport function runBatch(orders: Order[]): number[] {\n  return orders.map(order => {\n    if (!Number.isInteger(order.quantity) || order.quantity <= 0 || !Number.isInteger(order.unitPrice) || order.unitPrice < 0) {\n      throw new Error('invalid order');\n    }\n    return total(order);\n  });\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/consumer.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work/consumer.ts",
      "sha256": "d27cd82345f29232134b41c38da534f0c844213e038f4ee7a4409adc6dd58150",
      "bytes": 204,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "import { runBatch, type Order } from './index';\nexport function invoiceTotals() {\n  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\n  return runBatch(orders);\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/domain/order.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work/domain/order.ts",
      "sha256": "9c6df133f7923c6f4001a82a92ca091828d344aacb6b07c695df85ab6938f05d",
      "bytes": 152,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "export type Order = { quantity: number; unitPrice: number };\nexport function total(order: Order): number {\n  return order.quantity * order.unitPrice;\n}\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/domain.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work/domain.test.mjs",
      "sha256": "8e6c15733cf313c25794d9e0110e83e00baef773ad520cb1b91b3dd9da44d584",
      "bytes": 373,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { total } from './domain/order.ts';\ntest('pure pricing preserves the order and supports zero price', () => {\n  const order = Object.freeze({ quantity: 2, unitPrice: 125 });\n  expect(total(order)).toBe(250);\n  expect(total({ quantity: 1, unitPrice: 0 })).toBe(0);\n  expect(order).toEqual({ quantity: 2, unitPrice: 125 });\n});\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/index.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work/index.ts",
      "sha256": "036b056369ffc6d579e467551a379d5bab485b4d55f2f10f8b3850a857e8167e",
      "bytes": 123,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "export { handle } from './adapters/http';\nexport { runBatch } from './batch';\nexport type { Order } from './domain/order';\n"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state.result.md",
      "sha256": "bf135d0c5d7eb06e3ae4b28998d99cd45b61bb1ea0068e9dad47847b16f8f916",
      "bytes": 21876,
      "owners": [
        "grades-native-rerun-02.json#1"
      ],
      "text": "# migration-end-state\n\nMigrated work/ to the named transport-independent pricing domain. domain/order.ts owns Order and pure total. adapters/http.ts owns JSON and HTTP errors; batch.ts validates its own incoming orders and calls total directly. index.ts exports Order, handle and runBatch. consumer.ts uses Order. legacy.ts is deleted with no runtime compatibility alias or wrapper. Preserved pristine/ provides reversal.\n\nPhase 1 baseline runtime: 2 tests, 0 failures; compiler exit 0. Phase 2 isolated domain runtime: 1 test, 0 failures; compiler exit 0. Phase 3 switched consumers before facade completion. Its compiler actually exited 2 with TS2305 because index.ts did not yet export Order. This planned temporary import failure was confined to the owned work copy. Phase 4 updated exports and deleted legacy. Final compiler exited 0 and final runtime executed 3 tests with 0 failures and 12 assertions. The supplied contract test is unchanged. The legacy-reference search exited 1 with empty output, meaning no matches in runtime TypeScript. Source inspection separately records that batch never imports HTTP or serializes orders, and domain contains no transport code. Documentation/pristine copies still mention legacy, as historical inputs.\n\n## Scope and provenance\n\nSource package root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nSupplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Package metadata confirms version 0.1.0. No package Git revision was independently established; the supplied freeze is an input identifier, not verified provenance. Named source/support contents were actually read and saved in [source-reads.txt](migration-end-state/source-reads.txt). Registry entry is in [registry-entry.json](migration-end-state/registry-entry.json). No separate 0.2.1 package files were used. The compiler came from the independent installed Bun cache, not another plugin version.\n\nAll fixture data is synthetic. Shared inputs were copied in full to pristine/ and work/ before edits. Final pristine-integrity diff exited 0. No real service contact, issue, PR, message, commit, push, publish, configuration change, dependency installation or schedule occurred. No worker receipts or screenshots are claimed. Runtime timing strings below are Bun's actual output and are not performance benchmarks.\n\n## Supplied input\n\nFull registered contract:\n\n```json\n{\n  \"id\": \"migration-end-state\",\n  \"sourcePaths\": [\n    \"skills/principle-outcome-oriented-execution/SKILL.md\"\n  ],\n  \"prompt\": \"Migrate the authorized module to the named target architecture in explicit phases. Avoid retaining throwaway compatibility states. Declare where temporary breakage is acceptable and verify completion.\",\n  \"requirements\": [\n    \"Named target architecture and explicit migration phase boundaries\",\n    \"Available source inspection, authorized scoped writes and command execution for full implementation\"\n  ],\n  \"expectedFull\": \"Prioritize the verifiable target architecture; declare planned, scoped, reversible intermediate breakage; keep high-signal checks for actively touched areas; remove throwaway compatibility states and require full static and runtime verification at completion.\",\n  \"expectedReduced\": \"When writes or execution are unavailable, provide a migration plan with target, phase boundaries, reversible breakage scope and required checks. State that implementation or verification remains incomplete.\",\n  \"expectedBlocked\": \"If source or the named target is unavailable, identify the missing input and do not claim a verified migration. Denied or unavailable execution leaves verification blocked.\",\n  \"forbiddenClaims\": [\n    \"Full verification without observed static and runtime checks\",\n    \"Unplanned, unscoped or irreversible breakage is acceptable\",\n    \"Throwaway compatibility states are the completed target\",\n    \"Invocation metadata proves host enforcement\"\n  ]\n}\n```\n\nComplete scenario scope:\n\n```markdown\n# Named target: transport-independent pricing domain\n\nThis directory is the complete private package. index.ts and consumer.ts are the only runtime consumers of legacy.ts; the test imports the stable index facade. No external consumer or compatibility requirement exists. Scoped breaking intermediate states inside a case-owned copy are accepted and reversible from its pristine source copy. No shared input, external system or unrelated source may be broken.\n\nFinal required tree:\n\n- domain/order.ts: Order is { quantity:number; unitPrice:number }; pure total(order:Order):number. No HTTP, JSON parsing or HTTP status fields in this module.\n- adapters/http.ts: handle(raw:string) preserves every literal HTTP outcome in contract.test.mjs. JSON parsing and quantity/price validation live at this external boundary and call the domain function.\n- batch.ts: runBatch validates each domain order at its batch boundary, calls total directly, returns totals and throws Error('invalid order') for invalid input. It must never serialize input, invoke handle, or parse an HTTP response.\n- index.ts: stable exports handle and runBatch; export domain Order rather than transport-named RawOrder.\n- consumer.ts: migrated to the final domain concepts, retaining invoiceTotals() -> [250,99].\n- legacy.ts: deleted, with no alias, wrapper or compatibility copy left behind.\n\nPhases: (1) inspect source and record baseline checks; (2) introduce domain shape and move computation, checking that unit in isolation; (3) switch HTTP and batch consumers, with temporary import breakage limited to these named files until the switch completes; (4) delete legacy and update exports, then require full strict static and runtime checks before completion. Do not spend effort polishing temporary adapters. Preserve a pristine copy to reverse intermediate work.\n\nCompletion requires observed static verification using the already installed compiler if available, observed Bun runtime contract execution, source inspection proving all specified dependency directions, and no legacy references. Bun transpilation alone is not type checking. The test contract is supplied but has not been executed by preparation.\n```\n\nOriginal source inputs are retained byte-for-byte in [migration-end-state/pristine/](migration-end-state/pristine/). The shared scenario map and compiler hints were read through the exposed command tool and copied to the writable root. Preparation checks were not used as execution proof.\n\n## Variants and limits\n\nThe full workflow was executed on the actual host. Reduced and blocked responses were captured as explicitly simulated fallback text in [capability-variants.md](migration-end-state/capability-variants.md). Their actual responses follow.\n\nReduced: Simulated missing writes or execution. Target transport-independent pricing domain. Phase 1 inspect and establish baseline; phase 2 add domain/order.ts and test total in isolation; phase 3 switch adapters/http.ts, batch.ts and consumer.ts; phase 4 update index.ts and delete legacy.ts. Permit only reversible import breakage within the owned copy between phases 3 and 4, recoverable from pristine. Require strict compiler checks, Bun contract execution and dependency inspection at completion. No implementation or verification was performed under this simulated restriction.\n\nBlocked: Simulated missing source or named target. Identify the absent module and target contract before choosing phase boundaries. A verified migration cannot be claimed. If only execution is unavailable, implementation remains unverified until strict static and runtime checks are actually observed. Source, target and execution were available in the actual host.\n\nHost-enforced no-write, no-execution and unavailable-source variants remain unexercised. The host provided these capabilities, and changing configuration to manufacture denials was forbidden. Simulated text does not prove host denial. Metadata enforcement was not tested. Independent worker variants were unnecessary and not attempted. Missing actual model identity is irrelevant to these direct file workflows; no model execution receipt is claimed. No self-assigned grade is included.\n\n## Actual tools, actions and chronology\n\nExposed tool used: functions.exec, invoking tools.exec_command. Bun performed file writes, reads, command execution and assertion scripts. Local diff and rg commands ran through Bun in the saved execution records. Bindings and their limitations are in [capability-bindings.json](migration-end-state/capability-bindings.json).\n\nThe ordered initial discovery reads precede the timestamped journal and are documented in [pre-journal-actions.md](pre-journal-actions.md); their raw tool responses remain in this session transcript. The following timestamps are actual UTC event times from the command runner. Asia/Amman is UTC+03:00. The journal captures case operations in execution order; it does not reconstruct unobserved actions.\n\n- 2026-10-16T07:59:06.398Z setup: {\"sourceRoot\":\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\"scenario\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/migration-end-state\",\"copies\":[\"pristine\",\"work\"],\"sourceReads\":\"source-reads.txt\"}\n- 2026-10-16T07:59:06.897Z command-start: \"phase-1-runtime\"\n- 2026-10-16T07:59:06.915Z command-result: \"phase-1-runtime\"\n- 2026-10-16T07:59:06.916Z command-start: \"phase-1-static\"\n- 2026-10-16T07:59:07.137Z command-result: \"phase-1-static\"\n- 2026-10-16T07:59:34.513Z phase-plan: {\"target\":\"transport-independent pricing domain\",\"phases\":[\"1: inspect and baseline checks, observed\",\"2: introduce pure domain, isolated runtime/static checks\",\"3: switch HTTP and batch plus consumer; temporary imports may break only these files in work\",\"4: delete legacy/update exports and full static/runtime checks\"],\"reversal\":\"pristine copy\",\"breakage\":\"planned, reversible, case-owned work files only; no compatibility bridge\"}\n- 2026-10-16T07:59:34.514Z phase-2-written: [\"domain/order.ts\",\"domain.test.mjs\"]\n- 2026-10-16T07:59:34.514Z command-start: \"phase-2-runtime\"\n- 2026-10-16T07:59:34.526Z command-result: \"phase-2-runtime\"\n- 2026-10-16T07:59:34.526Z command-start: \"phase-2-static\"\n- 2026-10-16T07:59:34.726Z command-result: \"phase-2-static\"\n- 2026-10-16T07:59:54.036Z phase-3-start: \"Switch consumers directly to final domain; no temporary adapters.\"\n- 2026-10-16T07:59:54.037Z phase-3-written: [\"adapters/http.ts\",\"batch.ts\",\"consumer.ts\"]\n- 2026-10-16T07:59:54.037Z command-start: \"phase-3-static\"\n- 2026-10-16T07:59:54.309Z command-result: \"phase-3-static\"\n- 2026-10-16T07:59:54.309Z phase-4-start: \"Update stable facade, remove legacy and require final static/runtime checks.\"\n- 2026-10-16T07:59:54.310Z phase-4-written: {\"updated\":\"index.ts\",\"deleted\":\"legacy.ts\"}\n- 2026-10-16T07:59:54.311Z command-start: \"final-static\"\n- 2026-10-16T07:59:54.526Z command-result: \"final-static\"\n- 2026-10-16T07:59:54.526Z command-start: \"final-runtime\"\n- 2026-10-16T07:59:54.542Z command-result: \"final-runtime\"\n- 2026-10-16T07:59:54.543Z command-start: \"legacy-reference-search\"\n- 2026-10-16T07:59:54.564Z command-result: \"legacy-reference-search\"\n- 2026-10-16T07:59:54.564Z command-start: \"source-inspection\"\n- 2026-10-16T07:59:54.612Z command-result: \"source-inspection\"\n- 2026-10-16T07:59:54.612Z command-start: \"implementation-diff\"\n- 2026-10-16T07:59:54.620Z command-result: \"implementation-diff\"\n- 2026-10-16T08:02:37.228Z variant-text-captured: {\"full\":\"executed actual workflow\",\"reduced\":\"simulated text only\",\"blocked\":\"simulated text only\",\"hostNegativeVariants\":\"unexercised\"}\n- 2026-10-16T08:02:37.228Z command-start: \"pristine-integrity\"\n- 2026-10-16T08:02:37.234Z command-result: \"pristine-integrity\"\n\n## Command results\n\n| Command record | Exit | Artifact |\n|---|---:|---|\n| phase-1-runtime | 0 | [phase-1-runtime.json](migration-end-state/phase-1-runtime.json) |\n| phase-1-static | 0 | [phase-1-static.json](migration-end-state/phase-1-static.json) |\n| phase-2-runtime | 0 | [phase-2-runtime.json](migration-end-state/phase-2-runtime.json) |\n| phase-2-static | 0 | [phase-2-static.json](migration-end-state/phase-2-static.json) |\n| phase-3-static | 2 | [phase-3-static.json](migration-end-state/phase-3-static.json) |\n| final-static | 0 | [final-static.json](migration-end-state/final-static.json) |\n| final-runtime | 0 | [final-runtime.json](migration-end-state/final-runtime.json) |\n| legacy-reference-search | 1 | [legacy-reference-search.json](migration-end-state/legacy-reference-search.json) |\n| source-inspection | 0 | [source-inspection.json](migration-end-state/source-inspection.json) |\n| implementation-diff | 1 | [implementation-diff.json](migration-end-state/implementation-diff.json) |\n| pristine-integrity | 0 | [pristine-integrity.json](migration-end-state/pristine-integrity.json) |\n\nA diff exit of 1 in implementation-diff means changes were found. The migration legacy-reference-search exit of 1 means no matches. Phase-3-static exit of 2 is the observed planned temporary compiler failure. Negative manifest exits of 1 are observed rejection paths.\n\n### phase-1-runtime\n\n```json\n{\n  \"label\": \"phase-1-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) stable HTTP success and error contract [0.18ms]\\n(pass) private batch and consumer contracts [0.11ms]\\n\\n 2 pass\\n 0 fail\\n 9 expect() calls\\nRan 2 tests across 1 file. [8.00ms]\\n\"\n}\n```\n\n### phase-1-static\n\n```json\n{\n  \"label\": \"phase-1-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### phase-2-runtime\n\n```json\n{\n  \"label\": \"phase-2-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"domain.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ndomain.test.mjs:\\n(pass) pure pricing preserves the order and supports zero price [0.07ms]\\n\\n 1 pass\\n 0 fail\\n 3 expect() calls\\nRan 1 test across 1 file. [5.00ms]\\n\"\n}\n```\n\n### phase-2-static\n\n```json\n{\n  \"label\": \"phase-2-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### phase-3-static\n\n```json\n{\n  \"label\": \"phase-3-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 2,\n  \"stdout\": \"consumer.ts(1,25): error TS2305: Module '\\\"./index\\\"' has no exported member 'Order'.\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### final-static\n\n```json\n{\n  \"label\": \"final-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### final-runtime\n\n```json\n{\n  \"label\": \"final-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"contract.test.mjs\",\n    \"domain.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\ncontract.test.mjs:\\n(pass) stable HTTP success and error contract [0.19ms]\\n(pass) private batch and consumer contracts [0.11ms]\\n\\ndomain.test.mjs:\\n(pass) pure pricing preserves the order and supports zero price [0.03ms]\\n\\n 3 pass\\n 0 fail\\n 12 expect() calls\\nRan 3 tests across 2 files. [8.00ms]\\n\"\n}\n```\n\n### legacy-reference-search\n\n```json\n{\n  \"label\": \"legacy-reference-search\",\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \"legacy|RawOrder\",\n    \"--glob\",\n    \"*.ts\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### source-inspection\n\n```json\n{\n  \"label\": \"source-inspection\",\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \".\",\n    \"domain/order.ts\",\n    \"adapters/http.ts\",\n    \"batch.ts\",\n    \"consumer.ts\",\n    \"index.ts\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"consumer.ts:1:import { runBatch, type Order } from './index';\\nconsumer.ts:2:export function invoiceTotals() {\\nconsumer.ts:3:  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\\nconsumer.ts:4:  return runBatch(orders);\\nconsumer.ts:5:}\\nindex.ts:1:export { handle } from './adapters/http';\\nindex.ts:2:export { runBatch } from './batch';\\nindex.ts:3:export type { Order } from './domain/order';\\ndomain/order.ts:1:export type Order = { quantity: number; unitPrice: number };\\ndomain/order.ts:2:export function total(order: Order): number {\\ndomain/order.ts:3:  return order.quantity * order.unitPrice;\\ndomain/order.ts:4:}\\nadapters/http.ts:1:import { total, type Order } from '../domain/order';\\nadapters/http.ts:2:export function handle(raw: string): { status: number; body: string } {\\nadapters/http.ts:3:  let value: unknown;\\nadapters/http.ts:4:  try { value = JSON.parse(raw); } catch { return { status: 400, body: 'invalid json' }; }\\nadapters/http.ts:5:  if (typeof value !== 'object' || value === null || Array.isArray(value) ||\\nadapters/http.ts:6:      !('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0 ||\\nadapters/http.ts:7:      !('unitPrice' in value) || typeof value.unitPrice !== 'number' || !Number.isInteger(value.unitPrice) || value.unitPrice < 0) {\\nadapters/http.ts:8:    return { status: 400, body: 'invalid order' };\\nadapters/http.ts:9:  }\\nadapters/http.ts:10:  const order: Order = { quantity: value.quantity, unitPrice: value.unitPrice };\\nadapters/http.ts:11:  return { status: 200, body: JSON.stringify({ total: total(order) }) };\\nadapters/http.ts:12:}\\nbatch.ts:1:import { total, type Order } from './domain/order';\\nbatch.ts:2:export function runBatch(orders: Order[]): number[] {\\nbatch.ts:3:  return orders.map(order => {\\nbatch.ts:4:    if (!Number.isInteger(order.quantity) || order.quantity <= 0 || !Number.isInteger(order.unitPrice) || order.unitPrice < 0) {\\nbatch.ts:5:      throw new Error('invalid order');\\nbatch.ts:6:    }\\nbatch.ts:7:    return total(order);\\nbatch.ts:8:  });\\nbatch.ts:9:}\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### implementation-diff\n\n```json\n{\n  \"label\": \"implementation-diff\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"../pristine\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"Only in .: adapters\\nOnly in .: batch.ts\\ndiff -ru ../pristine/consumer.ts ./consumer.ts\\n--- ../pristine/consumer.ts\\t2026-10-16 10:59:06\\n+++ ./consumer.ts\\t2026-10-16 10:59:54\\n@@ -1,2 +1,5 @@\\n-import { runBatch } from './index';\\n-export function invoiceTotals() { return runBatch([{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }]); }\\n+import { runBatch, type Order } from './index';\\n+export function invoiceTotals() {\\n+  const orders: Order[] = [{ quantity: 2, unitPrice: 125 }, { quantity: 1, unitPrice: 99 }];\\n+  return runBatch(orders);\\n+}\\nOnly in .: domain\\nOnly in .: domain.test.mjs\\ndiff -ru ../pristine/index.ts ./index.ts\\n--- ../pristine/index.ts\\t2026-10-16 10:59:06\\n+++ ./index.ts\\t2026-10-16 10:59:54\\n@@ -1,2 +1,3 @@\\n-export { handle, runBatch } from './legacy';\\n-export type { RawOrder } from './legacy';\\n+export { handle } from './adapters/http';\\n+export { runBatch } from './batch';\\n+export type { Order } from './domain/order';\\nOnly in ../pristine: legacy.ts\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### pristine-integrity\n\n```json\n{\n  \"label\": \"pristine-integrity\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/migration-end-state\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/migration-end-state/pristine\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n## Reviewable artifacts\n\nFinal files are in [migration-end-state/work/](migration-end-state/work/), originals in [migration-end-state/pristine/](migration-end-state/pristine/). Case scripts and exact result JSON files remain in [migration-end-state/](migration-end-state/). Source and script digests are in [artifact-sha256.json](migration-end-state/artifact-sha256.json). The full ordered run is retained in [chronology.jsonl](chronology.jsonl), with a case-only copy in [migration-end-state/chronology.jsonl](migration-end-state/chronology.jsonl). The shared runner is [evaluate.mjs](evaluate.mjs). Scripts that create baselines or the hand-authored first unit are historical setup steps and should not be replayed over the completed evidence. Rerun tests in work/, and rerun the manifest tool directly on work/manifests.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-03/migration-end-state/input",
      "owner": "grades-native-03.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/migration-end-state/source",
      "owner": "grades-native-03.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/migration-end-state/source-reads.json",
      "owner": "grades-native-03.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-03/migration-end-state/input",
      "owner": "grades-native-03.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/migration-end-state/source",
      "owner": "grades-native-03.json#0",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/migration-end-state/source-reads.json",
      "owner": "grades-native-03.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/consumer.ts",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/consumer.ts",
      "sha256": "8d8643c6ed3d985fa737fd32d45f2ef8b633233fefb28e61c695e6f76621f42a",
      "bytes": 156
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/contract.test.mjs",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/contract.test.mjs",
      "sha256": "b4c462080c43283cdc7b8ba9d10a9abccd9a7847c9c7950ea1cb06d56bfacfdc",
      "bytes": 761
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/index.ts",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/index.ts",
      "sha256": "bb735ce533faf28a4e7dee68defc6f82ab620def17d5860c61717ed5a70bdfd3",
      "bytes": 87
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/legacy.ts",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/legacy.ts",
      "sha256": "82a0d9fcad0c89d4f1dc1ad5887479b227c618b39670afff65e9d31c48d3d8d8",
      "bytes": 809
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/target.md",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/target.md",
      "sha256": "2dac75262c7caf2410ec9b92002827fe54a0a2906ffa10df3f3293bab7a5c8fc",
      "bytes": 2183
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/tsconfig.json",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/source-reads.txt",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/contract.test.mjs",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/contract.test.mjs",
      "sha256": "b4c462080c43283cdc7b8ba9d10a9abccd9a7847c9c7950ea1cb06d56bfacfdc",
      "bytes": 761
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/target.md",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/target.md",
      "sha256": "2dac75262c7caf2410ec9b92002827fe54a0a2906ffa10df3f3293bab7a5c8fc",
      "bytes": 2183
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/tsconfig.json",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/consumer.ts",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/consumer.ts",
      "sha256": "8d8643c6ed3d985fa737fd32d45f2ef8b633233fefb28e61c695e6f76621f42a",
      "bytes": 156
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/contract.test.mjs",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/contract.test.mjs",
      "sha256": "b4c462080c43283cdc7b8ba9d10a9abccd9a7847c9c7950ea1cb06d56bfacfdc",
      "bytes": 761
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/index.ts",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/index.ts",
      "sha256": "bb735ce533faf28a4e7dee68defc6f82ab620def17d5860c61717ed5a70bdfd3",
      "bytes": 87
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/legacy.ts",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/legacy.ts",
      "sha256": "82a0d9fcad0c89d4f1dc1ad5887479b227c618b39670afff65e9d31c48d3d8d8",
      "bytes": 809
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/target.md",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/target.md",
      "sha256": "2dac75262c7caf2410ec9b92002827fe54a0a2906ffa10df3f3293bab7a5c8fc",
      "bytes": 2183
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/pristine/tsconfig.json",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/source-reads.txt",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/contract.test.mjs",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/contract.test.mjs",
      "sha256": "b4c462080c43283cdc7b8ba9d10a9abccd9a7847c9c7950ea1cb06d56bfacfdc",
      "bytes": 761
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/target.md",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/target.md",
      "sha256": "2dac75262c7caf2410ec9b92002827fe54a0a2906ffa10df3f3293bab7a5c8fc",
      "bytes": 2183
    },
    {
      "path": "fixtures/rerun-02/migration-end-state/work/tsconfig.json",
      "owner": "grades-native-rerun-02.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
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
