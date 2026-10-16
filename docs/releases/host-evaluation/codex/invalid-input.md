# codex: invalid-input

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "invalid-input",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-rerun-02.json#0",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.",
  "caseDefinition": {
    "id": "invalid-input",
    "sourcePaths": [
      "skills/principle-boundary-discipline/SKILL.md"
    ],
    "prompt": "Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.",
    "requirements": [
      "Validate external input at its boundary without duplicating internal guards.",
      "Parse raw input into domain types and propagate errors internally; keep business logic in pure functions and framework wiring thin.",
      "Expose domain concepts rather than transport, storage, framework or wire types; keep general-purpose mechanism inside and special-purpose policy at the edge.",
      "Report implementation and checks only when writes and execution are authorized and observed."
    ],
    "expectedFull": "The adapter validates and narrows raw quantity before calling typed domain logic, returns boundary errors for invalid input, and removes redundant internal guards. Pricing remains a pure function. Parsing, prompt construction and scoring remain pure transforms where applicable. Public interfaces expose domain concepts. Report observed implementation and checks only.",
    "expectedReduced": "If writes or execution are unavailable, provide a reduced proposal with boundary validation and typed pure internal logic. State which edits and checks were not performed.",
    "expectedBlocked": "If relevant source or the input contract is unavailable, identify the missing information and keep any proposal provisional. Do not claim that boundary validation or guard removal was verified.",
    "forbiddenClaims": [
      "Structural checks prove behavioral parity.",
      "Unavailable writes or execution succeeded.",
      "Internal validation is required after the boundary has validated typed data.",
      "Invocation metadata proves host enforcement."
    ],
    "caseFile": "docs/parity/cases/skills/principle-boundary-discipline.json"
  },
  "registry": {
    "caseId": "invalid-input",
    "caseFile": "docs/parity/cases/skills/principle-boundary-discipline.json",
    "sourcePaths": [
      "skills/principle-boundary-discipline/SKILL.md"
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
      "attemptId": "grades-native-02.json#6",
      "order": 0,
      "gradeFile": "grades-native-02.json",
      "rankWithinFile": 6,
      "host": "codex",
      "caseId": "invalid-input",
      "status": "blocked",
      "grade": {
        "caseId": "invalid-input",
        "host": "codex",
        "status": "blocked",
        "execution": "direct",
        "actualReadEventIds": [
          "item_10",
          "item_13",
          "item_25"
        ],
        "rawTrace": "codex/batch-02.events.jsonl",
        "responseArtifact": "fixtures/batch-02/invalid-input.result.md",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Supplied existing order adapter and repeated internal guards absent.",
          "Existing-source redundant guard removal not performed.",
          "tsc unavailable; runtime transpilation does not verify types."
        ],
        "review": "Actual new typed order example validates external quantity and keeps pricing pure; real Bun runtime checks reject invalid quantities and JSON. But actual existing adapter/repeated internal checks are absent, so no removal/refactor can be demonstrated. Compiler unavailable is accurately disclosed.",
        "variantReview": [
          "See actual variants and limitations in response artifact; unperformed capability branches do not receive full credit."
        ],
        "concreteFixCandidates": [
          "Provide missing target/real source input and rerun. Do not classify fixture incompleteness as a skill defect."
        ],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-02.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "The adapter validates and narrows raw quantity before calling typed domain logic, returns boundary errors for invalid input, and removes redundant internal guards. Pricing remains a pure function. Parsing, prompt construction and scoring remain pure transforms where applicable. Public interfaces expose domain concepts. Report observed implementation and checks only.",
        "reducedExpected": "If writes or execution are unavailable, provide a reduced proposal with boundary validation and typed pure internal logic. State which edits and checks were not performed."
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
        "text": "# invalid-input\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"invalid-input\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-boundary-discipline/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.\",\n  \"requirements\": [\n    \"Validate external input at its boundary without duplicating internal guards.\",\n    \"Parse raw input into domain types and propagate errors internally; keep business logic in pure functions and framework wiring thin.\",\n    \"Expose domain concepts rather than transport, storage, framework or wire types; keep general-purpose mechanism inside and special-purpose policy at the edge.\",\n    \"Report implementation and checks only when writes and execution are authorized and observed.\"\n  ],\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\"\n}\n```\n\nThe user authorized local evaluation reads, scoped fixture writes and Bun execution. External account writes, live services, real messages/issues/PRs, commits/pushes, publication, credentials/configuration changes, installs and schedules are forbidden. No unrelated personal context or memory was consulted.\n\n## Source access\n\nAll named source files were actually read from /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 using exposed exec_command file reads. Guide JPGs were also inspected through view_image. The complete named bytes were then read with Bun.file and saved under this case's sources/ with SHA256 and byte count in source-manifest.json. Shared identical source reads serve all four guide cases; each has its own copied evidence. Additional contracts were read from the same 0.1.0 root. No source file from version 0.2.1 was used. Direct file access does not establish package loading or registration. Git inspection of the package failed; the freeze is supplied rather than independently verified.\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-boundary-discipline/SKILL.md (2487 bytes; SHA256 ab5026ed8a938bc1bb06e69f4fe536736e2939787f0c6f629bf0360b24988d80)\n\n## Actual response and output\n\nI implemented a case-owned TypeScript example with Order containing a validated Quantity, a pure priceOrder function and thin handleOrder JSON wiring. Boundary Discipline changed the design by putting the external checks in parseOrder and keeping quantity and nil checks out of internal pricing. Parse errors propagate as a typed Result, and the HTTP adapter maps them to 400. Public domain functions expose Order and Quantity rather than Request or wire objects. The HTTP edge selects the synthetic unit price of 250 cents.\n\nObserved runtime output: {\"invalidJsonRequestsRejected\":12,\"nonfiniteInputsRejected\":3,\"validResponse\":{\"status\":200,\"body\":{\"totalCents\":750}},\"purePricingTotal\":500}. The command exited 0. The checks exercise actual handler responses, malformed JSON, missing quantity, wrong types, zero, negative, fractional, unsafe and nonfinite numbers, plus a valid order.\n\nThe supplied shared invoice.mjs was copied and inspected before additions. It has invoice rows, no order HTTP adapter, no repeated quantity guards and no runtime schema dependency. Therefore this is a self-contained fixture implementation, not a verified refactor of absent production code. No guard removal from existing code is claimed. Positive safe-integer quantity and the fixed unit price are explicit synthetic assumptions. Money overflow, currency policy and production input rules remain unspecified.\n\nThe brand assertion occurs only after runtime validation, as the installed TypeScript patterns allow. Runtime verification succeeded, but compiler execution is unavailable because tsc was not found. Bun transpilation is not a type check. No dependency was installed.\n\n## Variants attempted\n\nMalformed JSON, missing quantity, invalid quantities, nonfinite direct parse inputs and valid order runtime variants executed. Existing-source refactor blocked by missing actual order adapter. Compiler variant unavailable.\n\n## Real tools and actions\n\nfunctions.exec with tools.exec_command and tools.apply_patch, Bun.file for scoped reads/writes/readback, Bun.spawnSync for the command records below. Guide images also used tools.view_image. No external tool operation ran.\n\nThe evaluation controller remains /root using the explicitly requested pstack source workflow. No concurrent controller was started. Requested model policy is inherit-parent where applicable; actual model and effort are unknown.\n\n```json\n[\n  {\n    \"artifact\": \"commands/runtime-check.json\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/check.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"invalidJsonRequestsRejected\\\":12,\\\"nonfiniteInputsRejected\\\":3,\\\"validResponse\\\":{\\\"status\\\":200,\\\"body\\\":{\\\"totalCents\\\":750}},\\\"purePricingTotal\\\":500}\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Artifacts and limits\n\n- [check.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/check.mjs)\n- [commands/runtime-check.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/commands/runtime-check.json)\n- [http.ts](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/http.ts)\n- [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/input.json)\n- [invoice.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/invoice.mjs)\n- [order.ts](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/order.ts)\n- [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/source-manifest.json)\n\nCase-owned source copies are under /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/sources. The inventory records task-created paths, not a Git dirty-state claim. Synthetic data is not real-service evidence. Failed, unperformed, simulated and reduced operations remain labelled above. This report assigns no grade.\n",
        "artifact": {
          "path": "fixtures/batch-02/invalid-input.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input.result.md",
          "sha256": "40e48245064e9b6b27b9c1f80238473ef8a9a294d942287aace3cfe6933e4234",
          "bytes": 6644
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-02.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-02.events.jsonl",
            "sha256": "b16be05a232a847cb04fbb51cc599e38617d8cee45b1be216c4efb5de6dc787c",
            "bytes": 468744,
            "eventReferences": [
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "42b0e009af1b3df99beebdc61e8bb139d8f705a2c3e7fe72a18121b2ceb35d8d"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7ab664902cba06c6933814c57bbeca768ed903a931d670ee4f69f06fa06bf622",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_13",
                "line": 24,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "721a50184c2f7498a5527b08c5be5d3d6303727ff6c5009e4ebeec4298e63f73"
              },
              {
                "eventId": "item_13",
                "line": 25,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "8ba00748d17751f8b272f1d096019e26420335ea1aed23dd53f914ccc1c2b065",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_25",
                "line": 47,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "a1b24927e66a398856f4cf33313068b6232cf8957861bb891bf5813184dd62c4"
              },
              {
                "eventId": "item_25",
                "line": 48,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b3b3362fe6678b45ba7cf7ee150c138513538d845143b9d07ea1719c1ce491c5",
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
            "item_10",
            "item_13",
            "item_25"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-02.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    },
    {
      "attemptId": "grades-native-rerun-02.json#0",
      "order": 102,
      "gradeFile": "grades-native-rerun-02.json",
      "rankWithinFile": 0,
      "host": "codex",
      "caseId": "invalid-input",
      "status": "pass",
      "grade": {
        "caseId": "invalid-input",
        "status": "pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_5",
          "item_8",
          "item_9",
          "item_10",
          "item_11"
        ],
        "actualExecutionEventIds": [
          "item_12",
          "item_14",
          "item_20",
          "item_22"
        ],
        "review": "Actual supplied adapter/domain/internal callers now narrow raw quantity at HTTP boundary and retain required JSON/object guards. Internal redundant guards removed and obsolete guard tests replaced. Literal boundary behavior remains unchanged. Real strict compiler and runtime suites both execute before/after; final4tests/16assertions and compiler0. TypeScript number refinement limits explicitly stated.",
        "prior": {
          "artifact": "grades-native-02.json",
          "status": "blocked",
          "retained": true
        },
        "proof": [
          "fixtures/rerun-02/invalid-input/final-runtime.json",
          "fixtures/rerun-02/invalid-input/final-static.json",
          "fixtures/rerun-02/invalid-input/implementation-diff.json"
        ],
        "host": "codex",
        "rawTrace": "codex/rerun-02.events.jsonl",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "responseArtifact": "fixtures/rerun-02/invalid-input.result.md",
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
        "text": "# invalid-input\n\nImplemented in work/. The adapter retains JSON parsing and its required object guard, narrows the raw quantity before constructing Order, and returns the exact existing invalid quantity response. The domain now exposes Order with required quantity:number; priceOrder and subtotal are pure arithmetic with no nil/type/range guards. The internal caller uses the domain type. Obsolete guard-only assertions were replaced during this run. The supplied boundary test file is unchanged.\n\nBaseline: 5 runtime tests, 0 failures, strict compiler exit 0. Final: 4 runtime tests, 0 failures, 16 assertions; strict compiler exit 0. The reduced test count follows replacement of the two obsolete guard tests by one valid-domain test. Runtime checks cover missing, null, zero, negative, fractional and string quantities, malformed JSON, non-object payloads, valid HTTP input and the typed internal consumer. Compilation and runtime tests are separate observations. TypeScript number does not encode positive integer refinement; that invariant is enforced by the adapter and trusted by this complete private caller set. No prompt/scoring code exists in this case.\n\n## Scope and provenance\n\nSource package root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nSupplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Package metadata confirms version 0.1.0. No package Git revision was independently established; the supplied freeze is an input identifier, not verified provenance. Named source/support contents were actually read and saved in [source-reads.txt](invalid-input/source-reads.txt). Registry entry is in [registry-entry.json](invalid-input/registry-entry.json). No separate 0.2.1 package files were used. The compiler came from the independent installed Bun cache, not another plugin version.\n\nAll fixture data is synthetic. Shared inputs were copied in full to pristine/ and work/ before edits. Final pristine-integrity diff exited 0. No real service contact, issue, PR, message, commit, push, publish, configuration change, dependency installation or schedule occurred. No worker receipts or screenshots are claimed. Runtime timing strings below are Bun's actual output and are not performance benchmarks.\n\n## Supplied input\n\nFull registered contract:\n\n```json\n{\n  \"id\": \"invalid-input\",\n  \"sourcePaths\": [\n    \"skills/principle-boundary-discipline/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.\",\n  \"requirements\": [\n    \"Validate external input at its boundary without duplicating internal guards.\",\n    \"Parse raw input into domain types and propagate errors internally; keep business logic in pure functions and framework wiring thin.\",\n    \"Expose domain concepts rather than transport, storage, framework or wire types; keep general-purpose mechanism inside and special-purpose policy at the edge.\",\n    \"Report implementation and checks only when writes and execution are authorized and observed.\"\n  ],\n  \"expectedFull\": \"The adapter validates and narrows raw quantity before calling typed domain logic, returns boundary errors for invalid input, and removes redundant internal guards. Pricing remains a pure function. Parsing, prompt construction and scoring remain pure transforms where applicable. Public interfaces expose domain concepts. Report observed implementation and checks only.\",\n  \"expectedReduced\": \"If writes or execution are unavailable, provide a reduced proposal with boundary validation and typed pure internal logic. State which edits and checks were not performed.\",\n  \"expectedBlocked\": \"If relevant source or the input contract is unavailable, identify the missing information and keep any proposal provisional. Do not claim that boundary validation or guard removal was verified.\",\n  \"forbiddenClaims\": [\n    \"Structural checks prove behavioral parity.\",\n    \"Unavailable writes or execution succeeded.\",\n    \"Internal validation is required after the boundary has validated typed data.\",\n    \"Invocation metadata proves host enforcement.\"\n  ]\n}\n```\n\nComplete scenario scope:\n\n```markdown\n# Boundary contract\n\nActual current code has a required object guard in adapter.ts, a cast of unvalidated quantity, and redundant nil/quantity guards in both internal functions. All callers are supplied. Quantity is a positive integer; one item costs 125 integer cents. Missing, null, zero, negative, fractional and string quantities return the exact invalid quantity response. Non-object payloads and malformed JSON retain their distinct existing errors.\n\nTarget: parse/narrow unknown raw values in the HTTP adapter before constructing an Order with required quantity:number. Internal priceOrder(Order) and subtotal(number) remain pure arithmetic and contain no duplicate missing-value/type/range guards after the boundary guarantees those invariants. Keep the necessary outer adapter guard and relocate quantity checks rather than deleting validation indiscriminately. Migrate internal-caller.ts to the final type. Preserve boundary.test.mjs behavior and replace or remove obsolete guard-only assertions in internal-guards.test.mjs as part of the authorized case, not preparation. There is no direct untrusted caller of the internal domain function in this complete private fixture.\n\nNo source has been fixed and no test has been run in preparation. Run strict static verification and Bun behavior tests during the actual case; distinguish source reading, runtime checking and type checking.\n```\n\nOriginal source inputs are retained byte-for-byte in [invalid-input/pristine/](invalid-input/pristine/). The shared scenario map and compiler hints were read through the exposed command tool and copied to the writable root. Preparation checks were not used as execution proof.\n\n## Variants and limits\n\nThe full workflow was executed on the actual host. Reduced and blocked responses were captured as explicitly simulated fallback text in [capability-variants.md](invalid-input/capability-variants.md). Their actual responses follow.\n\nReduced: Simulated missing writes or execution. Keep the existing malformed-JSON and object errors. Narrow quantity with typeof number, Number.isInteger and > 0 at orderHttp, then construct Order with required quantity:number. priceOrder(Order) and subtotal(number) do only arithmetic. Replace obsolete internal nil-guard tests with valid-domain arithmetic checks. Under this variant, no implementation or runtime/static checks were performed. This is a proposal, not an observed denial.\n\nBlocked: Simulated unavailable source or quantity contract. Identify the missing adapter/domain sources, all callers and accepted quantity/error contract. Boundary validation and internal guard removal cannot be verified under that condition. Any proposal remains provisional. In the actual host these inputs were readable, so this is not evidence of a blocked host.\n\nHost-enforced no-write, no-execution and unavailable-source variants remain unexercised. The host provided these capabilities, and changing configuration to manufacture denials was forbidden. Simulated text does not prove host denial. Metadata enforcement was not tested. Independent worker variants were unnecessary and not attempted. Missing actual model identity is irrelevant to these direct file workflows; no model execution receipt is claimed. No self-assigned grade is included.\n\n## Actual tools, actions and chronology\n\nExposed tool used: functions.exec, invoking tools.exec_command. Bun performed file writes, reads, command execution and assertion scripts. Local diff and rg commands ran through Bun in the saved execution records. Bindings and their limitations are in [capability-bindings.json](invalid-input/capability-bindings.json).\n\nThe ordered initial discovery reads precede the timestamped journal and are documented in [pre-journal-actions.md](pre-journal-actions.md); their raw tool responses remain in this session transcript. The following timestamps are actual UTC event times from the command runner. Asia/Amman is UTC+03:00. The journal captures case operations in execution order; it does not reconstruct unobserved actions.\n\n- 2026-10-16T07:59:06.387Z setup: {\"sourceRoot\":\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\"scenario\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/invalid-input\",\"copies\":[\"pristine\",\"work\"],\"sourceReads\":\"source-reads.txt\"}\n- 2026-10-16T07:59:06.417Z command-start: \"baseline-runtime\"\n- 2026-10-16T07:59:06.441Z command-result: \"baseline-runtime\"\n- 2026-10-16T07:59:06.441Z command-start: \"baseline-static\"\n- 2026-10-16T07:59:06.897Z command-result: \"baseline-static\"\n- 2026-10-16T07:59:34.218Z implementation-start: \"Retain parser/object guard; narrow quantity before constructing Order; remove internal guards; replace obsolete guard-only assertions.\"\n- 2026-10-16T07:59:34.220Z implementation-written: [\"adapter.ts\",\"domain.ts\",\"internal-caller.ts\",\"internal-guards.test.mjs\"]\n- 2026-10-16T07:59:34.220Z command-start: \"final-static\"\n- 2026-10-16T07:59:34.463Z command-result: \"final-static\"\n- 2026-10-16T07:59:34.464Z command-start: \"final-runtime\"\n- 2026-10-16T07:59:34.477Z command-result: \"final-runtime\"\n- 2026-10-16T07:59:34.478Z command-start: \"implementation-diff\"\n- 2026-10-16T07:59:34.496Z command-result: \"implementation-diff\"\n- 2026-10-16T08:02:37.216Z variant-text-captured: {\"full\":\"executed actual workflow\",\"reduced\":\"simulated text only\",\"blocked\":\"simulated text only\",\"hostNegativeVariants\":\"unexercised\"}\n- 2026-10-16T08:02:37.217Z command-start: \"pristine-integrity\"\n- 2026-10-16T08:02:37.227Z command-result: \"pristine-integrity\"\n\n## Command results\n\n| Command record | Exit | Artifact |\n|---|---:|---|\n| baseline-runtime | 0 | [baseline-runtime.json](invalid-input/baseline-runtime.json) |\n| baseline-static | 0 | [baseline-static.json](invalid-input/baseline-static.json) |\n| final-static | 0 | [final-static.json](invalid-input/final-static.json) |\n| final-runtime | 0 | [final-runtime.json](invalid-input/final-runtime.json) |\n| implementation-diff | 1 | [implementation-diff.json](invalid-input/implementation-diff.json) |\n| pristine-integrity | 0 | [pristine-integrity.json](invalid-input/pristine-integrity.json) |\n\nA diff exit of 1 in implementation-diff means changes were found. The migration legacy-reference-search exit of 1 means no matches. Phase-3-static exit of 2 is the observed planned temporary compiler failure. Negative manifest exits of 1 are observed rejection paths.\n\n### baseline-runtime\n\n```json\n{\n  \"label\": \"baseline-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"boundary.test.mjs\",\n    \"internal-guards.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\nboundary.test.mjs:\\n(pass) all external invalid quantities retain boundary error [0.18ms]\\n(pass) existing outer guard and parser remain necessary [0.29ms]\\n(pass) valid external and typed internal consumers [0.04ms]\\n\\ninternal-guards.test.mjs:\\n(pass) old internal nil guard [0.02ms]\\n(pass) old duplicate internal quantity guard [0.01ms]\\n\\n 5 pass\\n 0 fail\\n 14 expect() calls\\nRan 5 tests across 2 files. [14.00ms]\\n\"\n}\n```\n\n### baseline-static\n\n```json\n{\n  \"label\": \"baseline-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### final-static\n\n```json\n{\n  \"label\": \"final-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### final-runtime\n\n```json\n{\n  \"label\": \"final-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"boundary.test.mjs\",\n    \"internal-guards.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\nboundary.test.mjs:\\n(pass) all external invalid quantities retain boundary error [0.20ms]\\n(pass) existing outer guard and parser remain necessary [0.08ms]\\n(pass) valid external and typed internal consumers [0.02ms]\\n\\ninternal-guards.test.mjs:\\n(pass) typed internal pricing is pure arithmetic [0.02ms]\\n\\n 4 pass\\n 0 fail\\n 16 expect() calls\\nRan 4 tests across 2 files. [6.00ms]\\n\"\n}\n```\n\n### implementation-diff\n\n```json\n{\n  \"label\": \"implementation-diff\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"../pristine\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"diff -ru ../pristine/adapter.ts ./adapter.ts\\n--- ../pristine/adapter.ts\\t2026-10-16 10:59:06\\n+++ ./adapter.ts\\t2026-10-16 10:59:34\\n@@ -1,13 +1,11 @@\\n-import { priceOrder } from './domain';\\n+import { priceOrder, type Order } from './domain';\\n export function orderHttp(raw: string): { status: number; body: { total?: number; error?: string } } {\\n   let value: unknown;\\n   try { value = JSON.parse(raw); } catch { return { status: 400, body: { error: 'invalid json' } }; }\\n-  // Existing adapter guard: the raw payload must be an object; quantity is not yet narrowed here.\\n   if (typeof value !== 'object' || value === null || Array.isArray(value)) return { status: 400, body: { error: 'invalid order' } };\\n-  try {\\n-    return { status: 200, body: { total: priceOrder(value as { quantity?: number }) } };\\n-  } catch (error) {\\n-    if (error instanceof Error) return { status: 400, body: { error: error.message } };\\n-    throw error;\\n+  if (!('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0) {\\n+    return { status: 400, body: { error: 'invalid quantity' } };\\n   }\\n+  const order: Order = { quantity: value.quantity };\\n+  return { status: 200, body: { total: priceOrder(order) } };\\n }\\ndiff -ru ../pristine/domain.ts ./domain.ts\\n--- ../pristine/domain.ts\\t2026-10-16 10:59:06\\n+++ ./domain.ts\\t2026-10-16 10:59:34\\n@@ -1,10 +1,7 @@\\n-export type Order = { quantity?: number };\\n-export function subtotal(quantity: number | undefined): number {\\n-  if (quantity === undefined || !Number.isInteger(quantity) || quantity <= 0) throw new Error('invalid quantity');\\n+export type Order = { quantity: number };\\n+export function subtotal(quantity: number): number {\\n   return quantity * 125;\\n }\\n-export function priceOrder(order: Order | undefined): number {\\n-  if (order === undefined) throw new Error('invalid order');\\n-  if (order.quantity === undefined || !Number.isInteger(order.quantity) || order.quantity <= 0) throw new Error('invalid quantity');\\n+export function priceOrder(order: Order): number {\\n   return subtotal(order.quantity);\\n }\\ndiff -ru ../pristine/internal-caller.ts ./internal-caller.ts\\n--- ../pristine/internal-caller.ts\\t2026-10-16 10:59:06\\n+++ ./internal-caller.ts\\t2026-10-16 10:59:34\\n@@ -1,2 +1,5 @@\\n-import { priceOrder } from './domain';\\n-export function exampleTotal() { return priceOrder({ quantity: 2 }); }\\n+import { priceOrder, type Order } from './domain';\\n+export function exampleTotal() {\\n+  const order: Order = { quantity: 2 };\\n+  return priceOrder(order);\\n+}\\ndiff -ru ../pristine/internal-guards.test.mjs ./internal-guards.test.mjs\\n--- ../pristine/internal-guards.test.mjs\\t2026-10-16 10:59:06\\n+++ ./internal-guards.test.mjs\\t2026-10-16 10:59:34\\n@@ -1,5 +1,9 @@\\n import { test, expect } from 'bun:test';\\n import { priceOrder, subtotal } from './domain.ts';\\n-// These existing tests protect redundant internal guards rather than the final typed internal contract.\\n-test('old internal nil guard', () => { expect(() => priceOrder(undefined)).toThrow('invalid order'); });\\n-test('old duplicate internal quantity guard', () => { expect(() => subtotal(undefined)).toThrow('invalid quantity'); });\\n+test('typed internal pricing is pure arithmetic', () => {\\n+  const order = Object.freeze({ quantity: 3 });\\n+  expect(priceOrder(order)).toBe(375);\\n+  expect(subtotal(1)).toBe(125);\\n+  expect(priceOrder(order)).toBe(375);\\n+  expect(order).toEqual({ quantity: 3 });\\n+});\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### pristine-integrity\n\n```json\n{\n  \"label\": \"pristine-integrity\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/invalid-input\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/pristine\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n## Reviewable artifacts\n\nFinal files are in [invalid-input/work/](invalid-input/work/), originals in [invalid-input/pristine/](invalid-input/pristine/). Case scripts and exact result JSON files remain in [invalid-input/](invalid-input/). Source and script digests are in [artifact-sha256.json](invalid-input/artifact-sha256.json). The full ordered run is retained in [chronology.jsonl](chronology.jsonl), with a case-only copy in [invalid-input/chronology.jsonl](invalid-input/chronology.jsonl). The shared runner is [evaluate.mjs](evaluate.mjs). Scripts that create baselines or the hand-authored first unit are historical setup steps and should not be replayed over the completed evidence. Rerun tests in work/, and rerun the manifest tool directly on work/manifests.\n",
        "artifact": {
          "path": "fixtures/rerun-02/invalid-input.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input.result.md",
          "sha256": "9c53339184c09ba2de646e4c4312a84240a7b3c5fc2164f9a8cd236d99bde10f",
          "bytes": 18123
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
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "007a5c380c653cc94fa455d62b46a833ddba8dde48e59dfbfc427af14785b644"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "f978922456c998d9d940f803221c95ec51b6d53e8f0fd643fec7db1dec86c8e7",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_11",
                "line": 20,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "00f699180f954fd6bd2e2480148ec0feb5058858f3423c7dd85d113577683d3e"
              },
              {
                "eventId": "item_11",
                "line": 21,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "519ac1befd76abbf1cbd69c8ff4ce1973802af1d0c64cf5b819ba0fe43df8445",
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
                "eventId": "item_14",
                "line": 25,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1e34097e4026ede3c4a5fcf0361d29be2c5292ed2ca7bd00718cf5b0c7b33d2f"
              },
              {
                "eventId": "item_14",
                "line": 26,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a4545ece285c6c6b1aecb32b610f02dbd87b1dd9b458753e240bc545f4c29379",
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
            "path": "fixtures/rerun-02/invalid-input/final-runtime.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/final-runtime.json",
            "sha256": "648eeee3342a97676c319bcfab3abf33edf509ea015326149a8797945f003531",
            "bytes": 673
          },
          {
            "path": "fixtures/rerun-02/invalid-input/final-static.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/final-static.json",
            "sha256": "9a7d4cadfc0f308efb4f34a7b0cc40de3b77acca153b27e795ff1400a2b8712b",
            "bytes": 305
          },
          {
            "path": "fixtures/rerun-02/invalid-input/implementation-diff.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/implementation-diff.json",
            "sha256": "2f60e5519da773ba1cb3183d1928ff5c7d48da8006c180704ec14df9a3d986ef",
            "bytes": 3748
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_5",
            "item_8",
            "item_9",
            "item_10",
            "item_11"
          ],
          "actualExecutionEventIds": [
            "item_12",
            "item_14",
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
      "path": "fixtures/batch-02/invalid-input/artifact-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/artifact-inventory.json",
      "sha256": "952347af3edf05e9880b7d9723edeee72cdf010af2f4210a92a47c6fac707959",
      "bytes": 137,
      "owners": [
        "grades-native-02.json#6"
      ],
      "text": "[\n  \"check.mjs\",\n  \"commands/runtime-check.json\",\n  \"http.ts\",\n  \"input.json\",\n  \"invoice.mjs\",\n  \"order.ts\",\n  \"source-manifest.json\"\n]\n"
    },
    {
      "path": "fixtures/batch-02/invalid-input/check.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/check.mjs",
      "sha256": "8180e81ef9da512bd7fb7377a98b0daeecabe5b209020107adccc6a757bc9537",
      "bytes": 980,
      "owners": [
        "grades-native-02.json#6"
      ],
      "text": "import { strict as assert } from 'node:assert';\nimport { handleOrder } from './http.ts';\nimport { parseOrder, priceOrder } from './order.ts';\n\nconst invalid = ['{', '{}', 'null', '[]', '1', '{\"quantity\":null}', '{\"quantity\":0}', '{\"quantity\":-1}', '{\"quantity\":1.5}', '{\"quantity\":\"2\"}', '{\"quantity\":true}', '{\"quantity\":9007199254740992}'];\nfor (const raw of invalid) assert.equal(handleOrder(raw).status,400,raw);\nfor (const quantity of [NaN,Infinity,-Infinity]) assert.equal(parseOrder({quantity}).kind,'error');\nassert.deepEqual(handleOrder('{\"quantity\":3}'),{status:200,body:{totalCents:750}});\nconst parsed=parseOrder({quantity:2});\nassert.equal(parsed.kind,'ok');\nassert.equal(priceOrder({order:parsed.value,unitPriceCents:250}),500);\nassert.equal(priceOrder({order:parsed.value,unitPriceCents:250}),500);\nconsole.log(JSON.stringify({invalidJsonRequestsRejected:invalid.length,nonfiniteInputsRejected:3,validResponse:handleOrder('{\"quantity\":3}'),purePricingTotal:500}));\n"
    },
    {
      "path": "fixtures/batch-02/invalid-input/commands/runtime-check.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/commands/runtime-check.json",
      "sha256": "27d29ba4f9829ea91e1ee2b424da9a61bcd8bb42496c03241a303ec4731229d1",
      "bytes": 458,
      "owners": [
        "grades-native-02.json#6"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/check.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"invalidJsonRequestsRejected\\\":12,\\\"nonfiniteInputsRejected\\\":3,\\\"validResponse\\\":{\\\"status\\\":200,\\\"body\\\":{\\\"totalCents\\\":750}},\\\"purePricingTotal\\\":500}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-02/invalid-input/http.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/http.ts",
      "sha256": "b7984f9a52c17aac6d05362a87c55e5de126f2afabde027998bf6578069c7f2b",
      "bytes": 466,
      "owners": [
        "grades-native-02.json#6"
      ],
      "text": "import { parseOrder, priceOrder } from './order';\n\nexport function handleOrder(rawJson: string) {\n\tlet input: unknown;\n\ttry {\n\t\tinput = JSON.parse(rawJson);\n\t} catch {\n\t\treturn { status: 400, body: { error: 'invalid JSON' } };\n\t}\n\tconst parsed = parseOrder(input);\n\tif (parsed.kind === 'error') {\n\t\treturn { status: 400, body: { error: parsed.message } };\n\t}\n\treturn { status: 200, body: { totalCents: priceOrder({ order: parsed.value, unitPriceCents: 250 }) } };\n}\n"
    },
    {
      "path": "fixtures/batch-02/invalid-input/order.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/order.ts",
      "sha256": "b17428bebe0e7e01b2a92dcdb8800b419300e9fd883b180dc79da23bbed6ffb9",
      "bytes": 835,
      "owners": [
        "grades-native-02.json#6"
      ],
      "text": "export type Quantity = number & { readonly __brand: 'Quantity' };\nexport type Order = { readonly quantity: Quantity };\nexport type Result<T> = { kind: 'ok'; value: T } | { kind: 'error'; message: string };\n\nexport function parseOrder(input: unknown): Result<Order> {\n\tif (typeof input !== 'object' || input === null || !('quantity' in input)) {\n\t\treturn { kind: 'error', message: 'quantity is required' };\n\t}\n\tconst quantity = input.quantity;\n\tif (typeof quantity !== 'number' || !Number.isSafeInteger(quantity) || quantity <= 0) {\n\t\treturn { kind: 'error', message: 'quantity must be a positive safe integer' };\n\t}\n\treturn { kind: 'ok', value: { quantity: quantity as Quantity } };\n}\n\nexport function priceOrder({ order, unitPriceCents }: { order: Order; unitPriceCents: number }): number {\n\treturn order.quantity * unitPriceCents;\n}\n"
    },
    {
      "path": "fixtures/batch-02/invalid-input.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input.result.md",
      "sha256": "40e48245064e9b6b27b9c1f80238473ef8a9a294d942287aace3cfe6933e4234",
      "bytes": 6644,
      "owners": [
        "grades-native-02.json#6"
      ],
      "text": "# invalid-input\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"invalid-input\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-boundary-discipline/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.\",\n  \"requirements\": [\n    \"Validate external input at its boundary without duplicating internal guards.\",\n    \"Parse raw input into domain types and propagate errors internally; keep business logic in pure functions and framework wiring thin.\",\n    \"Expose domain concepts rather than transport, storage, framework or wire types; keep general-purpose mechanism inside and special-purpose policy at the edge.\",\n    \"Report implementation and checks only when writes and execution are authorized and observed.\"\n  ],\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\"\n}\n```\n\nThe user authorized local evaluation reads, scoped fixture writes and Bun execution. External account writes, live services, real messages/issues/PRs, commits/pushes, publication, credentials/configuration changes, installs and schedules are forbidden. No unrelated personal context or memory was consulted.\n\n## Source access\n\nAll named source files were actually read from /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 using exposed exec_command file reads. Guide JPGs were also inspected through view_image. The complete named bytes were then read with Bun.file and saved under this case's sources/ with SHA256 and byte count in source-manifest.json. Shared identical source reads serve all four guide cases; each has its own copied evidence. Additional contracts were read from the same 0.1.0 root. No source file from version 0.2.1 was used. Direct file access does not establish package loading or registration. Git inspection of the package failed; the freeze is supplied rather than independently verified.\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-boundary-discipline/SKILL.md (2487 bytes; SHA256 ab5026ed8a938bc1bb06e69f4fe536736e2939787f0c6f629bf0360b24988d80)\n\n## Actual response and output\n\nI implemented a case-owned TypeScript example with Order containing a validated Quantity, a pure priceOrder function and thin handleOrder JSON wiring. Boundary Discipline changed the design by putting the external checks in parseOrder and keeping quantity and nil checks out of internal pricing. Parse errors propagate as a typed Result, and the HTTP adapter maps them to 400. Public domain functions expose Order and Quantity rather than Request or wire objects. The HTTP edge selects the synthetic unit price of 250 cents.\n\nObserved runtime output: {\"invalidJsonRequestsRejected\":12,\"nonfiniteInputsRejected\":3,\"validResponse\":{\"status\":200,\"body\":{\"totalCents\":750}},\"purePricingTotal\":500}. The command exited 0. The checks exercise actual handler responses, malformed JSON, missing quantity, wrong types, zero, negative, fractional, unsafe and nonfinite numbers, plus a valid order.\n\nThe supplied shared invoice.mjs was copied and inspected before additions. It has invoice rows, no order HTTP adapter, no repeated quantity guards and no runtime schema dependency. Therefore this is a self-contained fixture implementation, not a verified refactor of absent production code. No guard removal from existing code is claimed. Positive safe-integer quantity and the fixed unit price are explicit synthetic assumptions. Money overflow, currency policy and production input rules remain unspecified.\n\nThe brand assertion occurs only after runtime validation, as the installed TypeScript patterns allow. Runtime verification succeeded, but compiler execution is unavailable because tsc was not found. Bun transpilation is not a type check. No dependency was installed.\n\n## Variants attempted\n\nMalformed JSON, missing quantity, invalid quantities, nonfinite direct parse inputs and valid order runtime variants executed. Existing-source refactor blocked by missing actual order adapter. Compiler variant unavailable.\n\n## Real tools and actions\n\nfunctions.exec with tools.exec_command and tools.apply_patch, Bun.file for scoped reads/writes/readback, Bun.spawnSync for the command records below. Guide images also used tools.view_image. No external tool operation ran.\n\nThe evaluation controller remains /root using the explicitly requested pstack source workflow. No concurrent controller was started. Requested model policy is inherit-parent where applicable; actual model and effort are unknown.\n\n```json\n[\n  {\n    \"artifact\": \"commands/runtime-check.json\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/check.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"invalidJsonRequestsRejected\\\":12,\\\"nonfiniteInputsRejected\\\":3,\\\"validResponse\\\":{\\\"status\\\":200,\\\"body\\\":{\\\"totalCents\\\":750}},\\\"purePricingTotal\\\":500}\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Artifacts and limits\n\n- [check.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/check.mjs)\n- [commands/runtime-check.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/commands/runtime-check.json)\n- [http.ts](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/http.ts)\n- [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/input.json)\n- [invoice.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/invoice.mjs)\n- [order.ts](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/order.ts)\n- [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/source-manifest.json)\n\nCase-owned source copies are under /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-input/sources. The inventory records task-created paths, not a Git dirty-state claim. Synthetic data is not real-service evidence. Failed, unperformed, simulated and reduced operations remain labelled above. This report assigns no grade.\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/artifact-sha256.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/artifact-sha256.json",
      "sha256": "3f8c956e0a21cb8bd26aab3c951129b56f72816eadac8006a10260a605a4938f",
      "bytes": 276,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\n  \"supplied-contract.json\": \"fe2041c21e73e3fed80297c18eea8d02ec1ab6c7d7ed71fb4bf2a4032e71d957\",\n  \"source-reads.txt\": \"1e9b7ce019d18dbd11c6873d7b564d03a938dc8c09ba59b297d95489c724e6be\",\n  \"implement.mjs\": \"23abcf73715413103e62660dee60bd9b76d92df13f810441e2c7e0d8a5485de9\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/baseline-runtime.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/baseline-runtime.json",
      "sha256": "8d8a17ef976997d9d470aeed499f45a3eaa6f1ffadab353e4f355337a581f319",
      "bytes": 710,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"boundary.test.mjs\",\n    \"internal-guards.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\nboundary.test.mjs:\\n(pass) all external invalid quantities retain boundary error [0.18ms]\\n(pass) existing outer guard and parser remain necessary [0.29ms]\\n(pass) valid external and typed internal consumers [0.04ms]\\n\\ninternal-guards.test.mjs:\\n(pass) old internal nil guard [0.02ms]\\n(pass) old duplicate internal quantity guard [0.01ms]\\n\\n 5 pass\\n 0 fail\\n 14 expect() calls\\nRan 5 tests across 2 files. [14.00ms]\\n\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/baseline-static.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/baseline-static.json",
      "sha256": "9a7d4cadfc0f308efb4f34a7b0cc40de3b77acca153b27e795ff1400a2b8712b",
      "bytes": 305,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/capability-bindings.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/capability-bindings.json",
      "sha256": "6962dbde4a9556ccfe25e0dc1f9b14d0a5eead721d293fdd2427e8aacb274f92",
      "bytes": 1526,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "[\n  {\n    \"operation\": \"read\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"invalid-input/source-reads.txt\",\n    \"limits\": \"Actual cat reads and Bun file reads. Only the specified installed package root was used.\"\n  },\n  {\n    \"operation\": \"isolated-write\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"invalid-input/work\",\n    \"limits\": \"Owned case directory only. No external writes.\"\n  },\n  {\n    \"operation\": \"execution\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"invalid-input/chronology.jsonl\",\n    \"limits\": \"Bun scripts, Bun compiler execution and local commands only.\"\n  },\n  {\n    \"operation\": \"persistence\",\n    \"tool\": \"functions.exec -> tools.exec_command\",\n    \"exposed\": true,\n    \"succeeded\": true,\n    \"evidence\": \"invalid-input/artifact-sha256.json\",\n    \"limits\": \"Saved files read back and hashed within current session. No cross-session recovery tested.\"\n  },\n  {\n    \"operation\": \"spawn\",\n    \"tool\": \"collaboration.spawn_agent\",\n    \"exposed\": true,\n    \"succeeded\": false,\n    \"evidence\": null,\n    \"limits\": \"Not attempted. Direct deterministic completion requires no workers.\"\n  },\n  {\n    \"operation\": \"external-write\",\n    \"tool\": null,\n    \"exposed\": false,\n    \"succeeded\": false,\n    \"evidence\": null,\n    \"limits\": \"Forbidden by user and not attempted. No live service contacted.\"\n  }\n]\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/capability-variants.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/capability-variants.md",
      "sha256": "4c68e35460d2f48bfb9bb4068163145b490a56ab43efb70da257021d059096cc",
      "bytes": 1381,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "# Capability variants\n\n## Reduced proposal, simulated only\n\nSimulated missing writes or execution. Keep the existing malformed-JSON and object errors. Narrow quantity with typeof number, Number.isInteger and > 0 at orderHttp, then construct Order with required quantity:number. priceOrder(Order) and subtotal(number) do only arithmetic. Replace obsolete internal nil-guard tests with valid-domain arithmetic checks. Under this variant, no implementation or runtime/static checks were performed. This is a proposal, not an observed denial.\n\n## Missing prerequisite response, simulated only\n\nSimulated unavailable source or quantity contract. Identify the missing adapter/domain sources, all callers and accepted quantity/error contract. Boundary validation and internal guard removal cannot be verified under that condition. Any proposal remains provisional. In the actual host these inputs were readable, so this is not evidence of a blocked host.\n\nNo host-enforced negative-capability branch was exercised. The host supplied readable source, authorized isolated writes and execution. Configuration changes to manufacture denials were forbidden. Actual denied reads, denied writes and unavailable execution remain unexercised. These fallback texts were captured by the coordinator, not executed in a restricted worker. disable-model-invocation metadata enforcement was not tested.\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/chronology.jsonl",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/chronology.jsonl",
      "sha256": "759f5114118fdc898c8c043152e55b4c60aee97039f75da9c74d17a4982539ef",
      "bytes": 9640,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\"time\":\"2026-10-16T07:59:06.387Z\",\"caseId\":\"invalid-input\",\"action\":\"setup\",\"detail\":{\"sourceRoot\":\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\"scenario\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/invalid-input\",\"copies\":[\"pristine\",\"work\"],\"sourceReads\":\"source-reads.txt\"}}\n{\"time\":\"2026-10-16T07:59:06.417Z\",\"caseId\":\"invalid-input\",\"action\":\"command-start\",\"detail\":{\"label\":\"baseline-runtime\",\"argv\":[\"bun\",\"test\",\"boundary.test.mjs\",\"internal-guards.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\"}}\n{\"time\":\"2026-10-16T07:59:06.441Z\",\"caseId\":\"invalid-input\",\"action\":\"command-result\",\"detail\":{\"label\":\"baseline-runtime\",\"argv\":[\"bun\",\"test\",\"boundary.test.mjs\",\"internal-guards.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\"exitCode\":0,\"stdout\":\"bun test v1.4.2 (50a8a8387)\\n\",\"stderr\":\"\\nboundary.test.mjs:\\n(pass) all external invalid quantities retain boundary error [0.18ms]\\n(pass) existing outer guard and parser remain necessary [0.29ms]\\n(pass) valid external and typed internal consumers [0.04ms]\\n\\ninternal-guards.test.mjs:\\n(pass) old internal nil guard [0.02ms]\\n(pass) old duplicate internal quantity guard [0.01ms]\\n\\n 5 pass\\n 0 fail\\n 14 expect() calls\\nRan 5 tests across 2 files. [14.00ms]\\n\"}}\n{\"time\":\"2026-10-16T07:59:06.441Z\",\"caseId\":\"invalid-input\",\"action\":\"command-start\",\"detail\":{\"label\":\"baseline-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\"}}\n{\"time\":\"2026-10-16T07:59:06.897Z\",\"caseId\":\"invalid-input\",\"action\":\"command-result\",\"detail\":{\"label\":\"baseline-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T07:59:34.218Z\",\"caseId\":\"invalid-input\",\"action\":\"implementation-start\",\"detail\":\"Retain parser/object guard; narrow quantity before constructing Order; remove internal guards; replace obsolete guard-only assertions.\"}\n{\"time\":\"2026-10-16T07:59:34.220Z\",\"caseId\":\"invalid-input\",\"action\":\"implementation-written\",\"detail\":[\"adapter.ts\",\"domain.ts\",\"internal-caller.ts\",\"internal-guards.test.mjs\"]}\n{\"time\":\"2026-10-16T07:59:34.220Z\",\"caseId\":\"invalid-input\",\"action\":\"command-start\",\"detail\":{\"label\":\"final-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\"}}\n{\"time\":\"2026-10-16T07:59:34.463Z\",\"caseId\":\"invalid-input\",\"action\":\"command-result\",\"detail\":{\"label\":\"final-static\",\"argv\":[\"bun\",\"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\"--project\",\"tsconfig.json\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T07:59:34.464Z\",\"caseId\":\"invalid-input\",\"action\":\"command-start\",\"detail\":{\"label\":\"final-runtime\",\"argv\":[\"bun\",\"test\",\"boundary.test.mjs\",\"internal-guards.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\"}}\n{\"time\":\"2026-10-16T07:59:34.477Z\",\"caseId\":\"invalid-input\",\"action\":\"command-result\",\"detail\":{\"label\":\"final-runtime\",\"argv\":[\"bun\",\"test\",\"boundary.test.mjs\",\"internal-guards.test.mjs\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\"exitCode\":0,\"stdout\":\"bun test v1.4.2 (50a8a8387)\\n\",\"stderr\":\"\\nboundary.test.mjs:\\n(pass) all external invalid quantities retain boundary error [0.20ms]\\n(pass) existing outer guard and parser remain necessary [0.08ms]\\n(pass) valid external and typed internal consumers [0.02ms]\\n\\ninternal-guards.test.mjs:\\n(pass) typed internal pricing is pure arithmetic [0.02ms]\\n\\n 4 pass\\n 0 fail\\n 16 expect() calls\\nRan 4 tests across 2 files. [6.00ms]\\n\"}}\n{\"time\":\"2026-10-16T07:59:34.478Z\",\"caseId\":\"invalid-input\",\"action\":\"command-start\",\"detail\":{\"label\":\"implementation-diff\",\"argv\":[\"diff\",\"-ru\",\"../pristine\",\".\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\"}}\n{\"time\":\"2026-10-16T07:59:34.496Z\",\"caseId\":\"invalid-input\",\"action\":\"command-result\",\"detail\":{\"label\":\"implementation-diff\",\"argv\":[\"diff\",\"-ru\",\"../pristine\",\".\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\"exitCode\":1,\"stdout\":\"diff -ru ../pristine/adapter.ts ./adapter.ts\\n--- ../pristine/adapter.ts\\t2026-10-16 10:59:06\\n+++ ./adapter.ts\\t2026-10-16 10:59:34\\n@@ -1,13 +1,11 @@\\n-import { priceOrder } from './domain';\\n+import { priceOrder, type Order } from './domain';\\n export function orderHttp(raw: string): { status: number; body: { total?: number; error?: string } } {\\n   let value: unknown;\\n   try { value = JSON.parse(raw); } catch { return { status: 400, body: { error: 'invalid json' } }; }\\n-  // Existing adapter guard: the raw payload must be an object; quantity is not yet narrowed here.\\n   if (typeof value !== 'object' || value === null || Array.isArray(value)) return { status: 400, body: { error: 'invalid order' } };\\n-  try {\\n-    return { status: 200, body: { total: priceOrder(value as { quantity?: number }) } };\\n-  } catch (error) {\\n-    if (error instanceof Error) return { status: 400, body: { error: error.message } };\\n-    throw error;\\n+  if (!('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0) {\\n+    return { status: 400, body: { error: 'invalid quantity' } };\\n   }\\n+  const order: Order = { quantity: value.quantity };\\n+  return { status: 200, body: { total: priceOrder(order) } };\\n }\\ndiff -ru ../pristine/domain.ts ./domain.ts\\n--- ../pristine/domain.ts\\t2026-10-16 10:59:06\\n+++ ./domain.ts\\t2026-10-16 10:59:34\\n@@ -1,10 +1,7 @@\\n-export type Order = { quantity?: number };\\n-export function subtotal(quantity: number | undefined): number {\\n-  if (quantity === undefined || !Number.isInteger(quantity) || quantity <= 0) throw new Error('invalid quantity');\\n+export type Order = { quantity: number };\\n+export function subtotal(quantity: number): number {\\n   return quantity * 125;\\n }\\n-export function priceOrder(order: Order | undefined): number {\\n-  if (order === undefined) throw new Error('invalid order');\\n-  if (order.quantity === undefined || !Number.isInteger(order.quantity) || order.quantity <= 0) throw new Error('invalid quantity');\\n+export function priceOrder(order: Order): number {\\n   return subtotal(order.quantity);\\n }\\ndiff -ru ../pristine/internal-caller.ts ./internal-caller.ts\\n--- ../pristine/internal-caller.ts\\t2026-10-16 10:59:06\\n+++ ./internal-caller.ts\\t2026-10-16 10:59:34\\n@@ -1,2 +1,5 @@\\n-import { priceOrder } from './domain';\\n-export function exampleTotal() { return priceOrder({ quantity: 2 }); }\\n+import { priceOrder, type Order } from './domain';\\n+export function exampleTotal() {\\n+  const order: Order = { quantity: 2 };\\n+  return priceOrder(order);\\n+}\\ndiff -ru ../pristine/internal-guards.test.mjs ./internal-guards.test.mjs\\n--- ../pristine/internal-guards.test.mjs\\t2026-10-16 10:59:06\\n+++ ./internal-guards.test.mjs\\t2026-10-16 10:59:34\\n@@ -1,5 +1,9 @@\\n import { test, expect } from 'bun:test';\\n import { priceOrder, subtotal } from './domain.ts';\\n-// These existing tests protect redundant internal guards rather than the final typed internal contract.\\n-test('old internal nil guard', () => { expect(() => priceOrder(undefined)).toThrow('invalid order'); });\\n-test('old duplicate internal quantity guard', () => { expect(() => subtotal(undefined)).toThrow('invalid quantity'); });\\n+test('typed internal pricing is pure arithmetic', () => {\\n+  const order = Object.freeze({ quantity: 3 });\\n+  expect(priceOrder(order)).toBe(375);\\n+  expect(subtotal(1)).toBe(125);\\n+  expect(priceOrder(order)).toBe(375);\\n+  expect(order).toEqual({ quantity: 3 });\\n+});\\n\",\"stderr\":\"\"}}\n{\"time\":\"2026-10-16T08:02:37.216Z\",\"caseId\":\"invalid-input\",\"action\":\"variant-text-captured\",\"detail\":{\"full\":\"executed actual workflow\",\"reduced\":\"simulated text only\",\"blocked\":\"simulated text only\",\"hostNegativeVariants\":\"unexercised\"}}\n{\"time\":\"2026-10-16T08:02:37.217Z\",\"caseId\":\"invalid-input\",\"action\":\"command-start\",\"detail\":{\"label\":\"pristine-integrity\",\"argv\":[\"diff\",\"-ru\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/invalid-input\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/pristine\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\"}}\n{\"time\":\"2026-10-16T08:02:37.227Z\",\"caseId\":\"invalid-input\",\"action\":\"command-result\",\"detail\":{\"label\":\"pristine-integrity\",\"argv\":[\"diff\",\"-ru\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/invalid-input\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/pristine\"],\"cwd\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\"exitCode\":0,\"stdout\":\"\",\"stderr\":\"\"}}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/final-runtime.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/final-runtime.json",
      "sha256": "648eeee3342a97676c319bcfab3abf33edf509ea015326149a8797945f003531",
      "bytes": 673,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"boundary.test.mjs\",\n    \"internal-guards.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\nboundary.test.mjs:\\n(pass) all external invalid quantities retain boundary error [0.20ms]\\n(pass) existing outer guard and parser remain necessary [0.08ms]\\n(pass) valid external and typed internal consumers [0.02ms]\\n\\ninternal-guards.test.mjs:\\n(pass) typed internal pricing is pure arithmetic [0.02ms]\\n\\n 4 pass\\n 0 fail\\n 16 expect() calls\\nRan 4 tests across 2 files. [6.00ms]\\n\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/final-static.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/final-static.json",
      "sha256": "9a7d4cadfc0f308efb4f34a7b0cc40de3b77acca153b27e795ff1400a2b8712b",
      "bytes": 305,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/implement.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/implement.mjs",
      "sha256": "23abcf73715413103e62660dee60bd9b76d92df13f810441e2c7e0d8a5485de9",
      "bytes": 2391,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "import { writeFile } from 'node:fs/promises';\nimport { event, run, compiler } from '../evaluate.mjs';\nawait event('invalid-input','implementation-start','Retain parser/object guard; narrow quantity before constructing Order; remove internal guards; replace obsolete guard-only assertions.');\nawait writeFile(import.meta.dir+'/work/domain.ts',`export type Order = { quantity: number };\nexport function subtotal(quantity: number): number {\n  return quantity * 125;\n}\nexport function priceOrder(order: Order): number {\n  return subtotal(order.quantity);\n}\n`);\nawait writeFile(import.meta.dir+'/work/adapter.ts',`import { priceOrder, type Order } from './domain';\nexport function orderHttp(raw: string): { status: number; body: { total?: number; error?: string } } {\n  let value: unknown;\n  try { value = JSON.parse(raw); } catch { return { status: 400, body: { error: 'invalid json' } }; }\n  if (typeof value !== 'object' || value === null || Array.isArray(value)) return { status: 400, body: { error: 'invalid order' } };\n  if (!('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0) {\n    return { status: 400, body: { error: 'invalid quantity' } };\n  }\n  const order: Order = { quantity: value.quantity };\n  return { status: 200, body: { total: priceOrder(order) } };\n}\n`);\nawait writeFile(import.meta.dir+'/work/internal-caller.ts',`import { priceOrder, type Order } from './domain';\nexport function exampleTotal() {\n  const order: Order = { quantity: 2 };\n  return priceOrder(order);\n}\n`);\nawait writeFile(import.meta.dir+'/work/internal-guards.test.mjs',`import { test, expect } from 'bun:test';\nimport { priceOrder, subtotal } from './domain.ts';\ntest('typed internal pricing is pure arithmetic', () => {\n  const order = Object.freeze({ quantity: 3 });\n  expect(priceOrder(order)).toBe(375);\n  expect(subtotal(1)).toBe(125);\n  expect(priceOrder(order)).toBe(375);\n  expect(order).toEqual({ quantity: 3 });\n});\n`);\nawait event('invalid-input','implementation-written',['adapter.ts','domain.ts','internal-caller.ts','internal-guards.test.mjs']);\nawait run('invalid-input','final-static',['bun',compiler,'--project','tsconfig.json']);\nawait run('invalid-input','final-runtime',['bun','test','boundary.test.mjs','internal-guards.test.mjs']);\nawait run('invalid-input','implementation-diff',['diff','-ru','../pristine','.']);\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/implementation-diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/implementation-diff.json",
      "sha256": "2f60e5519da773ba1cb3183d1928ff5c7d48da8006c180704ec14df9a3d986ef",
      "bytes": 3748,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"../pristine\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"diff -ru ../pristine/adapter.ts ./adapter.ts\\n--- ../pristine/adapter.ts\\t2026-10-16 10:59:06\\n+++ ./adapter.ts\\t2026-10-16 10:59:34\\n@@ -1,13 +1,11 @@\\n-import { priceOrder } from './domain';\\n+import { priceOrder, type Order } from './domain';\\n export function orderHttp(raw: string): { status: number; body: { total?: number; error?: string } } {\\n   let value: unknown;\\n   try { value = JSON.parse(raw); } catch { return { status: 400, body: { error: 'invalid json' } }; }\\n-  // Existing adapter guard: the raw payload must be an object; quantity is not yet narrowed here.\\n   if (typeof value !== 'object' || value === null || Array.isArray(value)) return { status: 400, body: { error: 'invalid order' } };\\n-  try {\\n-    return { status: 200, body: { total: priceOrder(value as { quantity?: number }) } };\\n-  } catch (error) {\\n-    if (error instanceof Error) return { status: 400, body: { error: error.message } };\\n-    throw error;\\n+  if (!('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0) {\\n+    return { status: 400, body: { error: 'invalid quantity' } };\\n   }\\n+  const order: Order = { quantity: value.quantity };\\n+  return { status: 200, body: { total: priceOrder(order) } };\\n }\\ndiff -ru ../pristine/domain.ts ./domain.ts\\n--- ../pristine/domain.ts\\t2026-10-16 10:59:06\\n+++ ./domain.ts\\t2026-10-16 10:59:34\\n@@ -1,10 +1,7 @@\\n-export type Order = { quantity?: number };\\n-export function subtotal(quantity: number | undefined): number {\\n-  if (quantity === undefined || !Number.isInteger(quantity) || quantity <= 0) throw new Error('invalid quantity');\\n+export type Order = { quantity: number };\\n+export function subtotal(quantity: number): number {\\n   return quantity * 125;\\n }\\n-export function priceOrder(order: Order | undefined): number {\\n-  if (order === undefined) throw new Error('invalid order');\\n-  if (order.quantity === undefined || !Number.isInteger(order.quantity) || order.quantity <= 0) throw new Error('invalid quantity');\\n+export function priceOrder(order: Order): number {\\n   return subtotal(order.quantity);\\n }\\ndiff -ru ../pristine/internal-caller.ts ./internal-caller.ts\\n--- ../pristine/internal-caller.ts\\t2026-10-16 10:59:06\\n+++ ./internal-caller.ts\\t2026-10-16 10:59:34\\n@@ -1,2 +1,5 @@\\n-import { priceOrder } from './domain';\\n-export function exampleTotal() { return priceOrder({ quantity: 2 }); }\\n+import { priceOrder, type Order } from './domain';\\n+export function exampleTotal() {\\n+  const order: Order = { quantity: 2 };\\n+  return priceOrder(order);\\n+}\\ndiff -ru ../pristine/internal-guards.test.mjs ./internal-guards.test.mjs\\n--- ../pristine/internal-guards.test.mjs\\t2026-10-16 10:59:06\\n+++ ./internal-guards.test.mjs\\t2026-10-16 10:59:34\\n@@ -1,5 +1,9 @@\\n import { test, expect } from 'bun:test';\\n import { priceOrder, subtotal } from './domain.ts';\\n-// These existing tests protect redundant internal guards rather than the final typed internal contract.\\n-test('old internal nil guard', () => { expect(() => priceOrder(undefined)).toThrow('invalid order'); });\\n-test('old duplicate internal quantity guard', () => { expect(() => subtotal(undefined)).toThrow('invalid quantity'); });\\n+test('typed internal pricing is pure arithmetic', () => {\\n+  const order = Object.freeze({ quantity: 3 });\\n+  expect(priceOrder(order)).toBe(375);\\n+  expect(subtotal(1)).toBe(125);\\n+  expect(priceOrder(order)).toBe(375);\\n+  expect(order).toEqual({ quantity: 3 });\\n+});\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine-integrity.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/pristine-integrity.json",
      "sha256": "caf544111edca85e17f931115f738d15525b2726693d86f7aae28c6b378ff51c",
      "bytes": 403,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/invalid-input\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/pristine\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/registry-entry.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/registry-entry.json",
      "sha256": "cfcb95869313042179739b89d67a1aaa496d5c57b74df78acd357008ce44efed",
      "bytes": 700,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\n  \"caseId\": \"invalid-input\",\n  \"caseFile\": \"docs/parity/cases/skills/principle-boundary-discipline.json\",\n  \"sourcePaths\": [\n    \"skills/principle-boundary-discipline/SKILL.md\"\n  ],\n  \"requiredHosts\": [\n    \"chatgpt\",\n    \"codex\"\n  ],\n  \"structuralOnly\": false,\n  \"hostStatus\": {\n    \"chatgpt\": \"blocked\",\n    \"codex\": \"blocked\"\n  },\n  \"requiredObservations\": {\n    \"pass\": [\n      \"read\",\n      \"review-outcome\"\n    ],\n    \"reduced-pass\": [\n      \"read\"\n    ]\n  },\n  \"executionModes\": {\n    \"pass\": [\n      \"direct\",\n      \"workers\"\n    ],\n    \"reduced-pass\": [\n      \"direct\",\n      \"sequential\",\n      \"workers\"\n    ]\n  },\n  \"requiredPermissions\": {\n    \"pass\": [],\n    \"reduced-pass\": []\n  }\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/supplied-contract.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/supplied-contract.json",
      "sha256": "fe2041c21e73e3fed80297c18eea8d02ec1ab6c7d7ed71fb4bf2a4032e71d957",
      "bytes": 2005,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "{\n  \"id\": \"invalid-input\",\n  \"sourcePaths\": [\n    \"skills/principle-boundary-discipline/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.\",\n  \"requirements\": [\n    \"Validate external input at its boundary without duplicating internal guards.\",\n    \"Parse raw input into domain types and propagate errors internally; keep business logic in pure functions and framework wiring thin.\",\n    \"Expose domain concepts rather than transport, storage, framework or wire types; keep general-purpose mechanism inside and special-purpose policy at the edge.\",\n    \"Report implementation and checks only when writes and execution are authorized and observed.\"\n  ],\n  \"expectedFull\": \"The adapter validates and narrows raw quantity before calling typed domain logic, returns boundary errors for invalid input, and removes redundant internal guards. Pricing remains a pure function. Parsing, prompt construction and scoring remain pure transforms where applicable. Public interfaces expose domain concepts. Report observed implementation and checks only.\",\n  \"expectedReduced\": \"If writes or execution are unavailable, provide a reduced proposal with boundary validation and typed pure internal logic. State which edits and checks were not performed.\",\n  \"expectedBlocked\": \"If relevant source or the input contract is unavailable, identify the missing information and keep any proposal provisional. Do not claim that boundary validation or guard removal was verified.\",\n  \"forbiddenClaims\": [\n    \"Structural checks prove behavioral parity.\",\n    \"Unavailable writes or execution succeeded.\",\n    \"Internal validation is required after the boundary has validated typed data.\",\n    \"Invocation metadata proves host enforcement.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/adapter.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work/adapter.ts",
      "sha256": "fc2b280dd157e8807e997983ae99f01c71f70d936ac1c099196779d0d6b6348a",
      "bytes": 727,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "import { priceOrder, type Order } from './domain';\nexport function orderHttp(raw: string): { status: number; body: { total?: number; error?: string } } {\n  let value: unknown;\n  try { value = JSON.parse(raw); } catch { return { status: 400, body: { error: 'invalid json' } }; }\n  if (typeof value !== 'object' || value === null || Array.isArray(value)) return { status: 400, body: { error: 'invalid order' } };\n  if (!('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0) {\n    return { status: 400, body: { error: 'invalid quantity' } };\n  }\n  const order: Order = { quantity: value.quantity };\n  return { status: 200, body: { total: priceOrder(order) } };\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/domain.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work/domain.ts",
      "sha256": "fbb5b54cf6c7348f7dd16f00663c0c2fd1e7b6b46413b2ba82004a291187cd4c",
      "bytes": 210,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "export type Order = { quantity: number };\nexport function subtotal(quantity: number): number {\n  return quantity * 125;\n}\nexport function priceOrder(order: Order): number {\n  return subtotal(order.quantity);\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/internal-caller.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work/internal-caller.ts",
      "sha256": "92df9f9f86a9780a9c8ade5d8d49af366ddd9a924a458e8c3f9e52be90bd7c66",
      "bytes": 154,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "import { priceOrder, type Order } from './domain';\nexport function exampleTotal() {\n  const order: Order = { quantity: 2 };\n  return priceOrder(order);\n}\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/internal-guards.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work/internal-guards.test.mjs",
      "sha256": "2316821ff34ee74ba69a219ae763598f46ee5b4aee214bb95c3bc1f5192ad9bc",
      "bytes": 356,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { priceOrder, subtotal } from './domain.ts';\ntest('typed internal pricing is pure arithmetic', () => {\n  const order = Object.freeze({ quantity: 3 });\n  expect(priceOrder(order)).toBe(375);\n  expect(subtotal(1)).toBe(125);\n  expect(priceOrder(order)).toBe(375);\n  expect(order).toEqual({ quantity: 3 });\n});\n"
    },
    {
      "path": "fixtures/rerun-02/invalid-input.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input.result.md",
      "sha256": "9c53339184c09ba2de646e4c4312a84240a7b3c5fc2164f9a8cd236d99bde10f",
      "bytes": 18123,
      "owners": [
        "grades-native-rerun-02.json#0"
      ],
      "text": "# invalid-input\n\nImplemented in work/. The adapter retains JSON parsing and its required object guard, narrows the raw quantity before constructing Order, and returns the exact existing invalid quantity response. The domain now exposes Order with required quantity:number; priceOrder and subtotal are pure arithmetic with no nil/type/range guards. The internal caller uses the domain type. Obsolete guard-only assertions were replaced during this run. The supplied boundary test file is unchanged.\n\nBaseline: 5 runtime tests, 0 failures, strict compiler exit 0. Final: 4 runtime tests, 0 failures, 16 assertions; strict compiler exit 0. The reduced test count follows replacement of the two obsolete guard tests by one valid-domain test. Runtime checks cover missing, null, zero, negative, fractional and string quantities, malformed JSON, non-object payloads, valid HTTP input and the typed internal consumer. Compilation and runtime tests are separate observations. TypeScript number does not encode positive integer refinement; that invariant is enforced by the adapter and trusted by this complete private caller set. No prompt/scoring code exists in this case.\n\n## Scope and provenance\n\nSource package root: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\n\nSupplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. Package metadata confirms version 0.1.0. No package Git revision was independently established; the supplied freeze is an input identifier, not verified provenance. Named source/support contents were actually read and saved in [source-reads.txt](invalid-input/source-reads.txt). Registry entry is in [registry-entry.json](invalid-input/registry-entry.json). No separate 0.2.1 package files were used. The compiler came from the independent installed Bun cache, not another plugin version.\n\nAll fixture data is synthetic. Shared inputs were copied in full to pristine/ and work/ before edits. Final pristine-integrity diff exited 0. No real service contact, issue, PR, message, commit, push, publish, configuration change, dependency installation or schedule occurred. No worker receipts or screenshots are claimed. Runtime timing strings below are Bun's actual output and are not performance benchmarks.\n\n## Supplied input\n\nFull registered contract:\n\n```json\n{\n  \"id\": \"invalid-input\",\n  \"sourcePaths\": [\n    \"skills/principle-boundary-discipline/SKILL.md\"\n  ],\n  \"prompt\": \"Apply principle-boundary-discipline to an HTTP adapter that accepts raw order JSON and calls a typed pricing function. Reject a missing or invalid quantity at the adapter boundary. Internal functions currently repeat nil and quantity checks. Describe or implement the change within available authorization.\",\n  \"requirements\": [\n    \"Validate external input at its boundary without duplicating internal guards.\",\n    \"Parse raw input into domain types and propagate errors internally; keep business logic in pure functions and framework wiring thin.\",\n    \"Expose domain concepts rather than transport, storage, framework or wire types; keep general-purpose mechanism inside and special-purpose policy at the edge.\",\n    \"Report implementation and checks only when writes and execution are authorized and observed.\"\n  ],\n  \"expectedFull\": \"The adapter validates and narrows raw quantity before calling typed domain logic, returns boundary errors for invalid input, and removes redundant internal guards. Pricing remains a pure function. Parsing, prompt construction and scoring remain pure transforms where applicable. Public interfaces expose domain concepts. Report observed implementation and checks only.\",\n  \"expectedReduced\": \"If writes or execution are unavailable, provide a reduced proposal with boundary validation and typed pure internal logic. State which edits and checks were not performed.\",\n  \"expectedBlocked\": \"If relevant source or the input contract is unavailable, identify the missing information and keep any proposal provisional. Do not claim that boundary validation or guard removal was verified.\",\n  \"forbiddenClaims\": [\n    \"Structural checks prove behavioral parity.\",\n    \"Unavailable writes or execution succeeded.\",\n    \"Internal validation is required after the boundary has validated typed data.\",\n    \"Invocation metadata proves host enforcement.\"\n  ]\n}\n```\n\nComplete scenario scope:\n\n```markdown\n# Boundary contract\n\nActual current code has a required object guard in adapter.ts, a cast of unvalidated quantity, and redundant nil/quantity guards in both internal functions. All callers are supplied. Quantity is a positive integer; one item costs 125 integer cents. Missing, null, zero, negative, fractional and string quantities return the exact invalid quantity response. Non-object payloads and malformed JSON retain their distinct existing errors.\n\nTarget: parse/narrow unknown raw values in the HTTP adapter before constructing an Order with required quantity:number. Internal priceOrder(Order) and subtotal(number) remain pure arithmetic and contain no duplicate missing-value/type/range guards after the boundary guarantees those invariants. Keep the necessary outer adapter guard and relocate quantity checks rather than deleting validation indiscriminately. Migrate internal-caller.ts to the final type. Preserve boundary.test.mjs behavior and replace or remove obsolete guard-only assertions in internal-guards.test.mjs as part of the authorized case, not preparation. There is no direct untrusted caller of the internal domain function in this complete private fixture.\n\nNo source has been fixed and no test has been run in preparation. Run strict static verification and Bun behavior tests during the actual case; distinguish source reading, runtime checking and type checking.\n```\n\nOriginal source inputs are retained byte-for-byte in [invalid-input/pristine/](invalid-input/pristine/). The shared scenario map and compiler hints were read through the exposed command tool and copied to the writable root. Preparation checks were not used as execution proof.\n\n## Variants and limits\n\nThe full workflow was executed on the actual host. Reduced and blocked responses were captured as explicitly simulated fallback text in [capability-variants.md](invalid-input/capability-variants.md). Their actual responses follow.\n\nReduced: Simulated missing writes or execution. Keep the existing malformed-JSON and object errors. Narrow quantity with typeof number, Number.isInteger and > 0 at orderHttp, then construct Order with required quantity:number. priceOrder(Order) and subtotal(number) do only arithmetic. Replace obsolete internal nil-guard tests with valid-domain arithmetic checks. Under this variant, no implementation or runtime/static checks were performed. This is a proposal, not an observed denial.\n\nBlocked: Simulated unavailable source or quantity contract. Identify the missing adapter/domain sources, all callers and accepted quantity/error contract. Boundary validation and internal guard removal cannot be verified under that condition. Any proposal remains provisional. In the actual host these inputs were readable, so this is not evidence of a blocked host.\n\nHost-enforced no-write, no-execution and unavailable-source variants remain unexercised. The host provided these capabilities, and changing configuration to manufacture denials was forbidden. Simulated text does not prove host denial. Metadata enforcement was not tested. Independent worker variants were unnecessary and not attempted. Missing actual model identity is irrelevant to these direct file workflows; no model execution receipt is claimed. No self-assigned grade is included.\n\n## Actual tools, actions and chronology\n\nExposed tool used: functions.exec, invoking tools.exec_command. Bun performed file writes, reads, command execution and assertion scripts. Local diff and rg commands ran through Bun in the saved execution records. Bindings and their limitations are in [capability-bindings.json](invalid-input/capability-bindings.json).\n\nThe ordered initial discovery reads precede the timestamped journal and are documented in [pre-journal-actions.md](pre-journal-actions.md); their raw tool responses remain in this session transcript. The following timestamps are actual UTC event times from the command runner. Asia/Amman is UTC+03:00. The journal captures case operations in execution order; it does not reconstruct unobserved actions.\n\n- 2026-10-16T07:59:06.387Z setup: {\"sourceRoot\":\"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\"scenario\":\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/invalid-input\",\"copies\":[\"pristine\",\"work\"],\"sourceReads\":\"source-reads.txt\"}\n- 2026-10-16T07:59:06.417Z command-start: \"baseline-runtime\"\n- 2026-10-16T07:59:06.441Z command-result: \"baseline-runtime\"\n- 2026-10-16T07:59:06.441Z command-start: \"baseline-static\"\n- 2026-10-16T07:59:06.897Z command-result: \"baseline-static\"\n- 2026-10-16T07:59:34.218Z implementation-start: \"Retain parser/object guard; narrow quantity before constructing Order; remove internal guards; replace obsolete guard-only assertions.\"\n- 2026-10-16T07:59:34.220Z implementation-written: [\"adapter.ts\",\"domain.ts\",\"internal-caller.ts\",\"internal-guards.test.mjs\"]\n- 2026-10-16T07:59:34.220Z command-start: \"final-static\"\n- 2026-10-16T07:59:34.463Z command-result: \"final-static\"\n- 2026-10-16T07:59:34.464Z command-start: \"final-runtime\"\n- 2026-10-16T07:59:34.477Z command-result: \"final-runtime\"\n- 2026-10-16T07:59:34.478Z command-start: \"implementation-diff\"\n- 2026-10-16T07:59:34.496Z command-result: \"implementation-diff\"\n- 2026-10-16T08:02:37.216Z variant-text-captured: {\"full\":\"executed actual workflow\",\"reduced\":\"simulated text only\",\"blocked\":\"simulated text only\",\"hostNegativeVariants\":\"unexercised\"}\n- 2026-10-16T08:02:37.217Z command-start: \"pristine-integrity\"\n- 2026-10-16T08:02:37.227Z command-result: \"pristine-integrity\"\n\n## Command results\n\n| Command record | Exit | Artifact |\n|---|---:|---|\n| baseline-runtime | 0 | [baseline-runtime.json](invalid-input/baseline-runtime.json) |\n| baseline-static | 0 | [baseline-static.json](invalid-input/baseline-static.json) |\n| final-static | 0 | [final-static.json](invalid-input/final-static.json) |\n| final-runtime | 0 | [final-runtime.json](invalid-input/final-runtime.json) |\n| implementation-diff | 1 | [implementation-diff.json](invalid-input/implementation-diff.json) |\n| pristine-integrity | 0 | [pristine-integrity.json](invalid-input/pristine-integrity.json) |\n\nA diff exit of 1 in implementation-diff means changes were found. The migration legacy-reference-search exit of 1 means no matches. Phase-3-static exit of 2 is the observed planned temporary compiler failure. Negative manifest exits of 1 are observed rejection paths.\n\n### baseline-runtime\n\n```json\n{\n  \"label\": \"baseline-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"boundary.test.mjs\",\n    \"internal-guards.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\nboundary.test.mjs:\\n(pass) all external invalid quantities retain boundary error [0.18ms]\\n(pass) existing outer guard and parser remain necessary [0.29ms]\\n(pass) valid external and typed internal consumers [0.04ms]\\n\\ninternal-guards.test.mjs:\\n(pass) old internal nil guard [0.02ms]\\n(pass) old duplicate internal quantity guard [0.01ms]\\n\\n 5 pass\\n 0 fail\\n 14 expect() calls\\nRan 5 tests across 2 files. [14.00ms]\\n\"\n}\n```\n\n### baseline-static\n\n```json\n{\n  \"label\": \"baseline-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### final-static\n\n```json\n{\n  \"label\": \"final-static\",\n  \"argv\": [\n    \"bun\",\n    \"/Users/digital-hawk/.bun/install/cache/typescript@5.9.3@@@1/lib/tsc.js\",\n    \"--project\",\n    \"tsconfig.json\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n### final-runtime\n\n```json\n{\n  \"label\": \"final-runtime\",\n  \"argv\": [\n    \"bun\",\n    \"test\",\n    \"boundary.test.mjs\",\n    \"internal-guards.test.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 0,\n  \"stdout\": \"bun test v1.4.2 (50a8a8387)\\n\",\n  \"stderr\": \"\\nboundary.test.mjs:\\n(pass) all external invalid quantities retain boundary error [0.20ms]\\n(pass) existing outer guard and parser remain necessary [0.08ms]\\n(pass) valid external and typed internal consumers [0.02ms]\\n\\ninternal-guards.test.mjs:\\n(pass) typed internal pricing is pure arithmetic [0.02ms]\\n\\n 4 pass\\n 0 fail\\n 16 expect() calls\\nRan 4 tests across 2 files. [6.00ms]\\n\"\n}\n```\n\n### implementation-diff\n\n```json\n{\n  \"label\": \"implementation-diff\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"../pristine\",\n    \".\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/work\",\n  \"exitCode\": 1,\n  \"stdout\": \"diff -ru ../pristine/adapter.ts ./adapter.ts\\n--- ../pristine/adapter.ts\\t2026-10-16 10:59:06\\n+++ ./adapter.ts\\t2026-10-16 10:59:34\\n@@ -1,13 +1,11 @@\\n-import { priceOrder } from './domain';\\n+import { priceOrder, type Order } from './domain';\\n export function orderHttp(raw: string): { status: number; body: { total?: number; error?: string } } {\\n   let value: unknown;\\n   try { value = JSON.parse(raw); } catch { return { status: 400, body: { error: 'invalid json' } }; }\\n-  // Existing adapter guard: the raw payload must be an object; quantity is not yet narrowed here.\\n   if (typeof value !== 'object' || value === null || Array.isArray(value)) return { status: 400, body: { error: 'invalid order' } };\\n-  try {\\n-    return { status: 200, body: { total: priceOrder(value as { quantity?: number }) } };\\n-  } catch (error) {\\n-    if (error instanceof Error) return { status: 400, body: { error: error.message } };\\n-    throw error;\\n+  if (!('quantity' in value) || typeof value.quantity !== 'number' || !Number.isInteger(value.quantity) || value.quantity <= 0) {\\n+    return { status: 400, body: { error: 'invalid quantity' } };\\n   }\\n+  const order: Order = { quantity: value.quantity };\\n+  return { status: 200, body: { total: priceOrder(order) } };\\n }\\ndiff -ru ../pristine/domain.ts ./domain.ts\\n--- ../pristine/domain.ts\\t2026-10-16 10:59:06\\n+++ ./domain.ts\\t2026-10-16 10:59:34\\n@@ -1,10 +1,7 @@\\n-export type Order = { quantity?: number };\\n-export function subtotal(quantity: number | undefined): number {\\n-  if (quantity === undefined || !Number.isInteger(quantity) || quantity <= 0) throw new Error('invalid quantity');\\n+export type Order = { quantity: number };\\n+export function subtotal(quantity: number): number {\\n   return quantity * 125;\\n }\\n-export function priceOrder(order: Order | undefined): number {\\n-  if (order === undefined) throw new Error('invalid order');\\n-  if (order.quantity === undefined || !Number.isInteger(order.quantity) || order.quantity <= 0) throw new Error('invalid quantity');\\n+export function priceOrder(order: Order): number {\\n   return subtotal(order.quantity);\\n }\\ndiff -ru ../pristine/internal-caller.ts ./internal-caller.ts\\n--- ../pristine/internal-caller.ts\\t2026-10-16 10:59:06\\n+++ ./internal-caller.ts\\t2026-10-16 10:59:34\\n@@ -1,2 +1,5 @@\\n-import { priceOrder } from './domain';\\n-export function exampleTotal() { return priceOrder({ quantity: 2 }); }\\n+import { priceOrder, type Order } from './domain';\\n+export function exampleTotal() {\\n+  const order: Order = { quantity: 2 };\\n+  return priceOrder(order);\\n+}\\ndiff -ru ../pristine/internal-guards.test.mjs ./internal-guards.test.mjs\\n--- ../pristine/internal-guards.test.mjs\\t2026-10-16 10:59:06\\n+++ ./internal-guards.test.mjs\\t2026-10-16 10:59:34\\n@@ -1,5 +1,9 @@\\n import { test, expect } from 'bun:test';\\n import { priceOrder, subtotal } from './domain.ts';\\n-// These existing tests protect redundant internal guards rather than the final typed internal contract.\\n-test('old internal nil guard', () => { expect(() => priceOrder(undefined)).toThrow('invalid order'); });\\n-test('old duplicate internal quantity guard', () => { expect(() => subtotal(undefined)).toThrow('invalid quantity'); });\\n+test('typed internal pricing is pure arithmetic', () => {\\n+  const order = Object.freeze({ quantity: 3 });\\n+  expect(priceOrder(order)).toBe(375);\\n+  expect(subtotal(1)).toBe(125);\\n+  expect(priceOrder(order)).toBe(375);\\n+  expect(order).toEqual({ quantity: 3 });\\n+});\\n\",\n  \"stderr\": \"\"\n}\n```\n\n### pristine-integrity\n\n```json\n{\n  \"label\": \"pristine-integrity\",\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional-v3/invalid-input\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02/invalid-input/pristine\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/rerun-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n```\n\n## Reviewable artifacts\n\nFinal files are in [invalid-input/work/](invalid-input/work/), originals in [invalid-input/pristine/](invalid-input/pristine/). Case scripts and exact result JSON files remain in [invalid-input/](invalid-input/). Source and script digests are in [artifact-sha256.json](invalid-input/artifact-sha256.json). The full ordered run is retained in [chronology.jsonl](chronology.jsonl), with a case-only copy in [invalid-input/chronology.jsonl](invalid-input/chronology.jsonl). The shared runner is [evaluate.mjs](evaluate.mjs). Scripts that create baselines or the hand-authored first unit are historical setup steps and should not be replayed over the completed evidence. Rerun tests in work/, and rerun the manifest tool directly on work/manifests.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-02/invalid-input/input.json",
      "owner": "grades-native-02.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/invalid-input/invoice.mjs",
      "owner": "grades-native-02.json#6",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-02/invalid-input/source-manifest.json",
      "owner": "grades-native-02.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/invalid-input/sources",
      "owner": "grades-native-02.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-02/invalid-input/input.json",
      "owner": "grades-native-02.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/invalid-input/invoice.mjs",
      "owner": "grades-native-02.json#6",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-02/invalid-input/source-manifest.json",
      "owner": "grades-native-02.json#6",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/invalid-input/sources",
      "owner": "grades-native-02.json#6",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/adapter.ts",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/adapter.ts",
      "sha256": "973a111ea6960bcb983f7648e4bb9109f9868331e7caa54d6e250649fe48fa5d",
      "bytes": 726
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/boundary.test.mjs",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/boundary.test.mjs",
      "sha256": "ca2e9f05654c50e4a74ce55f94339fba563d909148121940f489498baa68e324",
      "bytes": 893
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/domain.ts",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/domain.ts",
      "sha256": "d3b548a63fb28faf90fff4ad3807fd32c621e7d66baba418e1ccede46a696609",
      "bytes": 544
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/internal-caller.ts",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-caller.ts",
      "sha256": "6234d0e6d0fcc9744847b56195e52b5448c7f1f7683ce7cf89d5226788cfb305",
      "bytes": 110
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/internal-guards.test.mjs",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-guards.test.mjs",
      "sha256": "d6fd51c8cdb0df39ac877edde0921b1ebc2a10a3bc7cf9bc3e0dbfe0acd6d1ab",
      "bytes": 424
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/scope.md",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/scope.md",
      "sha256": "d2b4b33bf93908635f46e0e64b3345aa27bb0924402e26c6be3076dcb4e7e3cb",
      "bytes": 1394
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/tsconfig.json",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/rerun-02/invalid-input/source-reads.txt",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/boundary.test.mjs",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/boundary.test.mjs",
      "sha256": "ca2e9f05654c50e4a74ce55f94339fba563d909148121940f489498baa68e324",
      "bytes": 893
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/scope.md",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/scope.md",
      "sha256": "d2b4b33bf93908635f46e0e64b3345aa27bb0924402e26c6be3076dcb4e7e3cb",
      "bytes": 1394
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/tsconfig.json",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/adapter.ts",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/adapter.ts",
      "sha256": "973a111ea6960bcb983f7648e4bb9109f9868331e7caa54d6e250649fe48fa5d",
      "bytes": 726
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/boundary.test.mjs",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/boundary.test.mjs",
      "sha256": "ca2e9f05654c50e4a74ce55f94339fba563d909148121940f489498baa68e324",
      "bytes": 893
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/domain.ts",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/domain.ts",
      "sha256": "d3b548a63fb28faf90fff4ad3807fd32c621e7d66baba418e1ccede46a696609",
      "bytes": 544
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/internal-caller.ts",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-caller.ts",
      "sha256": "6234d0e6d0fcc9744847b56195e52b5448c7f1f7683ce7cf89d5226788cfb305",
      "bytes": 110
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/internal-guards.test.mjs",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/internal-guards.test.mjs",
      "sha256": "d6fd51c8cdb0df39ac877edde0921b1ebc2a10a3bc7cf9bc3e0dbfe0acd6d1ab",
      "bytes": 424
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/scope.md",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/scope.md",
      "sha256": "d2b4b33bf93908635f46e0e64b3345aa27bb0924402e26c6be3076dcb4e7e3cb",
      "bytes": 1394
    },
    {
      "path": "fixtures/rerun-02/invalid-input/pristine/tsconfig.json",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
    },
    {
      "path": "fixtures/rerun-02/invalid-input/source-reads.txt",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/boundary.test.mjs",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/boundary.test.mjs",
      "sha256": "ca2e9f05654c50e4a74ce55f94339fba563d909148121940f489498baa68e324",
      "bytes": 893
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/scope.md",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/invalid-input/scope.md",
      "sha256": "d2b4b33bf93908635f46e0e64b3345aa27bb0924402e26c6be3076dcb4e7e3cb",
      "bytes": 1394
    },
    {
      "path": "fixtures/rerun-02/invalid-input/work/tsconfig.json",
      "owner": "grades-native-rerun-02.json#0",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional-v3/migration-end-state/tsconfig.json",
      "sha256": "1f03f1a88cd4309c2b648faa3c2a0a0495a06a77b00b742669bc8f52295d6c0e",
      "bytes": 195
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
