# codex: invalid-state

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "invalid-state",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-02.json#7",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Review a typed task model { completed: boolean; completedAt?: Date }, interchangeable UserId and OrderId strings, an unchecked JSON payload, and a switch over task states. Make invalid typed states unrepresentable or identify the actual language limit. Explain where a non-empty list is needed for head and why sum can keep a plain list.",
  "caseDefinition": {
    "id": "invalid-state",
    "sourcePaths": [
      "skills/principle-type-system-discipline/SKILL.md"
    ],
    "prompt": "Review a typed task model { completed: boolean; completedAt?: Date }, interchangeable UserId and OrderId strings, an unchecked JSON payload, and a switch over task states. Make invalid typed states unrepresentable or identify the actual language limit. Explain where a non-empty list is needed for head and why sum can keep a plain list.",
    "requirements": [
      "Inspect the model and relevant language/compiler constraints.",
      "Use authorized file access and compiler execution when available; do not install tools incidentally."
    ],
    "expectedFull": "Replace contradictory optional fields with explicit open and done variants or one authoritative completion value. Construct constrained values, brand semantic IDs, parse external data at boundaries, avoid unsupported casts, require exhaustive handling, and derive types from owned schemas where available. Strengthen types where an operation is partial, keeping total sum on plain lists. Verify with the available compiler that an invalid state or missing variant fails, or identify the actual language limit and the remaining validation requirement.",
    "expectedReduced": "When source, writes, or compiler execution are unavailable, provide the proposed typed model and explain actual language limits. State which invalid states the construction excludes, which checks remain runtime checks, and which edits or compiler checks were not performed.",
    "expectedBlocked": "If the relevant language or source cannot be established sufficiently to assess the invariant, report the missing inputs or denied capability and leave the result unverified.",
    "forbiddenClaims": [
      "An unchecked cast proves validity.",
      "Every language can encode every invariant.",
      "A proposed type model or structural package check proves compiler rejection or host behavior.",
      "Unavailable writes or checks succeeded."
    ],
    "caseFile": "docs/parity/cases/skills/principle-type-system-discipline.json"
  },
  "registry": {
    "caseId": "invalid-state",
    "caseFile": "docs/parity/cases/skills/principle-type-system-discipline.json",
    "sourcePaths": [
      "skills/principle-type-system-discipline/SKILL.md"
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
      "attemptId": "grades-native-02.json#7",
      "order": 0,
      "gradeFile": "grades-native-02.json",
      "rankWithinFile": 7,
      "host": "codex",
      "caseId": "invalid-state",
      "status": "reduced-pass",
      "grade": {
        "caseId": "invalid-state",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_10",
          "item_13",
          "item_25"
        ],
        "rawTrace": "codex/batch-02.events.jsonl",
        "responseArtifact": "fixtures/batch-02/invalid-state.result.md",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Required invalid-state/missing-variant compiler rejection unobserved."
        ],
        "review": "Creates tagged task states, distinct ID brands, boundary parsers, exhaustive never check, non-empty head and total sum. Runtime examples execute; negative compiler probes remain saved/unexecuted because tsc absent. Date mutability, structural extra fields and assertion bypass are accurately identified as language limits.",
        "variantReview": [
          "See actual variants and limitations in response artifact; unperformed capability branches do not receive full credit."
        ],
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-02.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Replace contradictory optional fields with explicit open and done variants or one authoritative completion value. Construct constrained values, brand semantic IDs, parse external data at boundaries, avoid unsupported casts, require exhaustive handling, and derive types from owned schemas where available. Strengthen types where an operation is partial, keeping total sum on plain lists. Verify with the available compiler that an invalid state or missing variant fails, or identify the actual language limit and the remaining validation requirement.",
        "reducedExpected": "When source, writes, or compiler execution are unavailable, provide the proposed typed model and explain actual language limits. State which invalid states the construction excludes, which checks remain runtime checks, and which edits or compiler checks were not performed."
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
        "text": "# invalid-state\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"invalid-state\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-type-system-discipline/SKILL.md\"\n  ],\n  \"prompt\": \"Review a typed task model { completed: boolean; completedAt?: Date }, interchangeable UserId and OrderId strings, an unchecked JSON payload, and a switch over task states. Make invalid typed states unrepresentable or identify the actual language limit. Explain where a non-empty list is needed for head and why sum can keep a plain list.\",\n  \"requirements\": [\n    \"Inspect the model and relevant language/compiler constraints.\",\n    \"Use authorized file access and compiler execution when available; do not install tools incidentally.\"\n  ],\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\"\n}\n```\n\nThe user authorized local evaluation reads, scoped fixture writes and Bun execution. External account writes, live services, real messages/issues/PRs, commits/pushes, publication, credentials/configuration changes, installs and schedules are forbidden. No unrelated personal context or memory was consulted.\n\n## Source access\n\nAll named source files were actually read from /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 using exposed exec_command file reads. Guide JPGs were also inspected through view_image. The complete named bytes were then read with Bun.file and saved under this case's sources/ with SHA256 and byte count in source-manifest.json. Shared identical source reads serve all four guide cases; each has its own copied evidence. Additional contracts were read from the same 0.1.0 root. No source file from version 0.2.1 was used. Direct file access does not establish package loading or registration. Git inspection of the package failed; the freeze is supplied rather than independently verified.\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-type-system-discipline/SKILL.md (5641 bytes; SHA256 65649b9c31d43b481ab4cf299ce51441b5077d2cfb964369b151df0889b484e9)\n\n## Actual response and output\n\nI chose TypeScript for the supplied typed-model example; no original project language or compiler configuration was provided. Task is now {kind:'open'} | {kind:'done';at:Date}. A done task must carry at in well-typed code, and taskLabel uses a never assignment to require exhaustive handling. UserId and OrderId have distinct brands. parseTask and ID constructors validate unknown external values before producing domain types. The synthetic ID formats are explicit fixture choices. No authoritative schema or schema library was supplied to derive from.\n\nType System Discipline changed head to require readonly [T,...T[]]. It keeps sum on readonly number[] because sum([]) returns 0. A total alternative for head is to return T | undefined on a plain list. Negative compiler probes cover missing done timestamp, the old contradictory shape, exchanged IDs, empty head and a newly added unhandled cancelled variant.\n\nObserved runtime output: {\"invalidTaskInputsRejected\":6,\"open\":{\"kind\":\"open\"},\"done\":\"2026-10-16T00:00:00.000Z\",\"idBoundaryChecks\":4,\"head\":7,\"emptySum\":0,\"sum\":5,\"compilerCheck\":\"not run; no tsc discovered; Bun transpilation is not type checking\"}. The command exited 0. Compiler discovery exited 1 with no tsc on PATH. The package has no installed dependencies. The negative probes are saved but unexecuted by a type checker. I do not claim compiler rejection. A future authorized compiler check can run tsc with strict, noEmit, noUncheckedIndexedAccess and exactOptionalPropertyTypes on model.ts and negative-probes.ts separately.\n\nTypeScript erases types at runtime. Brands and never do not validate JSON, and assertions or any can bypass them. Date also permits Invalid Date and is mutable; the parser checks validity but plain Date does not prove that invariant for all later mutations. Structural object types are not exact objects, so variables may contain extra fields. The parser reconstructs canonical task variants and drops irrelevant wire fields. A private immutable timestamp representation plus boundary validation would strengthen timestamp validity if required. Positive integer ranges and Date validity are runtime refinements, not built-in TypeScript guarantees.\n\n## Variants attempted\n\nRuntime parser, brand-constructor, non-empty head and empty sum variants executed. Negative compile probes saved. Compiler-rejection variant blocked by missing tsc. No tools installed.\n\n## Real tools and actions\n\nfunctions.exec with tools.exec_command and tools.apply_patch, Bun.file for scoped reads/writes/readback, Bun.spawnSync for the command records below. Guide images also used tools.view_image. No external tool operation ran.\n\nThe evaluation controller remains /root using the explicitly requested pstack source workflow. No concurrent controller was started. Requested model policy is inherit-parent where applicable; actual model and effort are unknown.\n\n```json\n[\n  {\n    \"artifact\": \"commands/compiler-discovery.json\",\n    \"argv\": [\n      \"zsh\",\n      \"-c\",\n      \"command -v tsc\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.211Z\",\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  },\n  {\n    \"artifact\": \"commands/runtime-check.json\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/check.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"invalidTaskInputsRejected\\\":6,\\\"open\\\":{\\\"kind\\\":\\\"open\\\"},\\\"done\\\":\\\"2026-10-16T00:00:00.000Z\\\",\\\"idBoundaryChecks\\\":4,\\\"head\\\":7,\\\"emptySum\\\":0,\\\"sum\\\":5,\\\"compilerCheck\\\":\\\"not run; no tsc discovered; Bun transpilation is not type checking\\\"}\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Artifacts and limits\n\n- [check.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/check.mjs)\n- [commands/compiler-discovery.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/commands/compiler-discovery.json)\n- [commands/runtime-check.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/commands/runtime-check.json)\n- [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/input.json)\n- [model.ts](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/model.ts)\n- [negative-probes.ts](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/negative-probes.ts)\n- [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/source-manifest.json)\n\nCase-owned source copies are under /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/sources. The inventory records task-created paths, not a Git dirty-state claim. Synthetic data is not real-service evidence. Failed, unperformed, simulated and reduced operations remain labelled above. This report assigns no grade.\n",
        "artifact": {
          "path": "fixtures/batch-02/invalid-state.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state.result.md",
          "sha256": "b9716d3609db7a65575de5555d6c1111af8891efe2f253036d5b73a831b35372",
          "bytes": 7342
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
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-02/invalid-state/artifact-inventory.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/artifact-inventory.json",
      "sha256": "f07fbd6cd9d1a529ae72dcc792ae6b24fc26562081c0e317cf424bfe7c96318c",
      "bytes": 169,
      "owners": [
        "grades-native-02.json#7"
      ],
      "text": "[\n  \"check.mjs\",\n  \"commands/compiler-discovery.json\",\n  \"commands/runtime-check.json\",\n  \"input.json\",\n  \"model.ts\",\n  \"negative-probes.ts\",\n  \"source-manifest.json\"\n]\n"
    },
    {
      "path": "fixtures/batch-02/invalid-state/check.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/check.mjs",
      "sha256": "45eb033990c28a60b636925409f77cf8993a1daab57cda320f0e618f1f2e3745",
      "bytes": 1152,
      "owners": [
        "grades-native-02.json#7"
      ],
      "text": "import {strict as assert} from 'node:assert';\nimport {parseTask,parseUserId,parseOrderId,taskLabel,head,sum} from './model.ts';\n\nfor (const input of [null,{}, {completed:true}, {kind:'done'}, {kind:'done',at:'not-a-date'}, {kind:'cancelled'}]) assert.equal(parseTask(input).kind,'error');\nconst open=parseTask(JSON.parse('{\"kind\":\"open\",\"at\":\"ignored-wire-field\"}'));\nassert.deepEqual(open,{kind:'ok',value:{kind:'open'}});\nassert.equal(taskLabel(open.value),'open');\nconst done=parseTask(JSON.parse('{\"kind\":\"done\",\"at\":\"2026-10-16T00:00:00Z\"}'));\nassert.equal(done.kind,'ok');\nassert.equal(taskLabel(done.value),'2026-10-16T00:00:00.000Z');\nassert.equal(parseUserId('user-1').kind,'ok');\nassert.equal(parseUserId('order-1').kind,'error');\nassert.equal(parseOrderId('order-1').kind,'ok');\nassert.equal(parseOrderId('user-1').kind,'error');\nassert.equal(head([7,8]),7);\nassert.equal(sum([]),0);\nassert.equal(sum([2,3]),5);\nconsole.log(JSON.stringify({invalidTaskInputsRejected:6,open:open.value,done:taskLabel(done.value),idBoundaryChecks:4,head:7,emptySum:0,sum:5,compilerCheck:'not run; no tsc discovered; Bun transpilation is not type checking'}));\n"
    },
    {
      "path": "fixtures/batch-02/invalid-state/commands/compiler-discovery.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/commands/compiler-discovery.json",
      "sha256": "8f8056dc2b2a1e1398a9e8d258b27c175845664441d1e147bf696c92239774a9",
      "bytes": 245,
      "owners": [
        "grades-native-02.json#7"
      ],
      "text": "{\n  \"argv\": [\n    \"zsh\",\n    \"-c\",\n    \"command -v tsc\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n  \"startedAt\": \"2026-10-16T07:42:24.211Z\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-02/invalid-state/commands/runtime-check.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/commands/runtime-check.json",
      "sha256": "0f8843aa80c524ee8a57ab9cb07efc116039d3f6ec93a73f496bbbb558928246",
      "bytes": 550,
      "owners": [
        "grades-native-02.json#7"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/check.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"invalidTaskInputsRejected\\\":6,\\\"open\\\":{\\\"kind\\\":\\\"open\\\"},\\\"done\\\":\\\"2026-10-16T00:00:00.000Z\\\",\\\"idBoundaryChecks\\\":4,\\\"head\\\":7,\\\"emptySum\\\":0,\\\"sum\\\":5,\\\"compilerCheck\\\":\\\"not run; no tsc discovered; Bun transpilation is not type checking\\\"}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-02/invalid-state/model.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/model.ts",
      "sha256": "dc5a216fa4a07b2a75c455513cdeb87273db3b9fbbe6564c6fd353f52bcf1e44",
      "bytes": 1812,
      "owners": [
        "grades-native-02.json#7"
      ],
      "text": "export type Task = { kind: 'open' } | { kind: 'done'; at: Date };\nexport type UserId = string & { readonly __brand: 'UserId' };\nexport type OrderId = string & { readonly __brand: 'OrderId' };\nexport type NonEmpty<T> = readonly [T, ...T[]];\ntype Result<T> = { kind: 'ok'; value: T } | { kind: 'error'; message: string };\n\nexport function parseUserId(input: unknown): Result<UserId> {\n\tif (typeof input !== 'string' || !/^user-[1-9]\\d*$/.test(input)) return { kind: 'error', message: 'invalid user id' };\n\treturn { kind: 'ok', value: input as UserId };\n}\n\nexport function parseOrderId(input: unknown): Result<OrderId> {\n\tif (typeof input !== 'string' || !/^order-[1-9]\\d*$/.test(input)) return { kind: 'error', message: 'invalid order id' };\n\treturn { kind: 'ok', value: input as OrderId };\n}\n\nexport function parseTask(input: unknown): Result<Task> {\n\tif (typeof input !== 'object' || input === null || !('kind' in input)) return { kind: 'error', message: 'task must be an object with kind' };\n\tif (input.kind === 'open') return { kind: 'ok', value: { kind: 'open' } };\n\tif (input.kind !== 'done' || !('at' in input) || typeof input.at !== 'string') return { kind: 'error', message: 'done task requires a timestamp string' };\n\tconst at = new Date(input.at);\n\tif (!Number.isFinite(at.getTime())) return { kind: 'error', message: 'invalid timestamp' };\n\treturn { kind: 'ok', value: { kind: 'done', at } };\n}\n\nexport function taskLabel(task: Task): string {\n\tswitch (task.kind) {\n\t\tcase 'open': return 'open';\n\t\tcase 'done': return task.at.toISOString();\n\t\tdefault: {\n\t\t\tconst exhaustive: never = task;\n\t\t\treturn exhaustive;\n\t\t}\n\t}\n}\n\nexport function head<T>(values: NonEmpty<T>): T { return values[0]; }\nexport function sum(values: readonly number[]): number { return values.reduce((total,value)=>total+value,0); }\n"
    },
    {
      "path": "fixtures/batch-02/invalid-state/negative-probes.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/negative-probes.ts",
      "sha256": "f25adc90f3f35a4de3c3fe8333c5e7c2f3f09d6cbde7218f2744cf2780f5c9a7",
      "bytes": 609,
      "owners": [
        "grades-native-02.json#7"
      ],
      "text": "import { head, type Task, type UserId, type OrderId } from './model';\n\nconst missingTimestamp: Task = { kind: 'done' };\nconst oldContradiction: Task = { completed: true };\ndeclare const userId: UserId;\nconst orderId: OrderId = userId;\nconst emptyHead = head([]);\ntype ExtendedTask = Task | { kind: 'cancelled' };\nfunction incomplete(task: ExtendedTask): string {\n\tswitch(task.kind) {\n\t\tcase 'open': return 'open';\n\t\tcase 'done': return task.at.toISOString();\n\t\tdefault: {\n\t\t\tconst exhaustive: never = task;\n\t\t\treturn exhaustive;\n\t\t}\n\t}\n}\nvoid [missingTimestamp,oldContradiction,orderId,emptyHead,incomplete];\n"
    },
    {
      "path": "fixtures/batch-02/invalid-state.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state.result.md",
      "sha256": "b9716d3609db7a65575de5555d6c1111af8891efe2f253036d5b73a831b35372",
      "bytes": 7342,
      "owners": [
        "grades-native-02.json#7"
      ],
      "text": "# invalid-state\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"invalid-state\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-type-system-discipline/SKILL.md\"\n  ],\n  \"prompt\": \"Review a typed task model { completed: boolean; completedAt?: Date }, interchangeable UserId and OrderId strings, an unchecked JSON payload, and a switch over task states. Make invalid typed states unrepresentable or identify the actual language limit. Explain where a non-empty list is needed for head and why sum can keep a plain list.\",\n  \"requirements\": [\n    \"Inspect the model and relevant language/compiler constraints.\",\n    \"Use authorized file access and compiler execution when available; do not install tools incidentally.\"\n  ],\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\"\n}\n```\n\nThe user authorized local evaluation reads, scoped fixture writes and Bun execution. External account writes, live services, real messages/issues/PRs, commits/pushes, publication, credentials/configuration changes, installs and schedules are forbidden. No unrelated personal context or memory was consulted.\n\n## Source access\n\nAll named source files were actually read from /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0 using exposed exec_command file reads. Guide JPGs were also inspected through view_image. The complete named bytes were then read with Bun.file and saved under this case's sources/ with SHA256 and byte count in source-manifest.json. Shared identical source reads serve all four guide cases; each has its own copied evidence. Additional contracts were read from the same 0.1.0 root. No source file from version 0.2.1 was used. Direct file access does not establish package loading or registration. Git inspection of the package failed; the freeze is supplied rather than independently verified.\n\n- /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-type-system-discipline/SKILL.md (5641 bytes; SHA256 65649b9c31d43b481ab4cf299ce51441b5077d2cfb964369b151df0889b484e9)\n\n## Actual response and output\n\nI chose TypeScript for the supplied typed-model example; no original project language or compiler configuration was provided. Task is now {kind:'open'} | {kind:'done';at:Date}. A done task must carry at in well-typed code, and taskLabel uses a never assignment to require exhaustive handling. UserId and OrderId have distinct brands. parseTask and ID constructors validate unknown external values before producing domain types. The synthetic ID formats are explicit fixture choices. No authoritative schema or schema library was supplied to derive from.\n\nType System Discipline changed head to require readonly [T,...T[]]. It keeps sum on readonly number[] because sum([]) returns 0. A total alternative for head is to return T | undefined on a plain list. Negative compiler probes cover missing done timestamp, the old contradictory shape, exchanged IDs, empty head and a newly added unhandled cancelled variant.\n\nObserved runtime output: {\"invalidTaskInputsRejected\":6,\"open\":{\"kind\":\"open\"},\"done\":\"2026-10-16T00:00:00.000Z\",\"idBoundaryChecks\":4,\"head\":7,\"emptySum\":0,\"sum\":5,\"compilerCheck\":\"not run; no tsc discovered; Bun transpilation is not type checking\"}. The command exited 0. Compiler discovery exited 1 with no tsc on PATH. The package has no installed dependencies. The negative probes are saved but unexecuted by a type checker. I do not claim compiler rejection. A future authorized compiler check can run tsc with strict, noEmit, noUncheckedIndexedAccess and exactOptionalPropertyTypes on model.ts and negative-probes.ts separately.\n\nTypeScript erases types at runtime. Brands and never do not validate JSON, and assertions or any can bypass them. Date also permits Invalid Date and is mutable; the parser checks validity but plain Date does not prove that invariant for all later mutations. Structural object types are not exact objects, so variables may contain extra fields. The parser reconstructs canonical task variants and drops irrelevant wire fields. A private immutable timestamp representation plus boundary validation would strengthen timestamp validity if required. Positive integer ranges and Date validity are runtime refinements, not built-in TypeScript guarantees.\n\n## Variants attempted\n\nRuntime parser, brand-constructor, non-empty head and empty sum variants executed. Negative compile probes saved. Compiler-rejection variant blocked by missing tsc. No tools installed.\n\n## Real tools and actions\n\nfunctions.exec with tools.exec_command and tools.apply_patch, Bun.file for scoped reads/writes/readback, Bun.spawnSync for the command records below. Guide images also used tools.view_image. No external tool operation ran.\n\nThe evaluation controller remains /root using the explicitly requested pstack source workflow. No concurrent controller was started. Requested model policy is inherit-parent where applicable; actual model and effort are unknown.\n\n```json\n[\n  {\n    \"artifact\": \"commands/compiler-discovery.json\",\n    \"argv\": [\n      \"zsh\",\n      \"-c\",\n      \"command -v tsc\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"startedAt\": \"2026-10-16T07:42:24.211Z\",\n    \"exitCode\": 1,\n    \"stdout\": \"\",\n    \"stderr\": \"\"\n  },\n  {\n    \"artifact\": \"commands/runtime-check.json\",\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/check.mjs\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02\",\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"invalidTaskInputsRejected\\\":6,\\\"open\\\":{\\\"kind\\\":\\\"open\\\"},\\\"done\\\":\\\"2026-10-16T00:00:00.000Z\\\",\\\"idBoundaryChecks\\\":4,\\\"head\\\":7,\\\"emptySum\\\":0,\\\"sum\\\":5,\\\"compilerCheck\\\":\\\"not run; no tsc discovered; Bun transpilation is not type checking\\\"}\\n\",\n    \"stderr\": \"\"\n  }\n]\n```\n\n## Artifacts and limits\n\n- [check.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/check.mjs)\n- [commands/compiler-discovery.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/commands/compiler-discovery.json)\n- [commands/runtime-check.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/commands/runtime-check.json)\n- [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/input.json)\n- [model.ts](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/model.ts)\n- [negative-probes.ts](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/negative-probes.ts)\n- [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/source-manifest.json)\n\nCase-owned source copies are under /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-02/invalid-state/sources. The inventory records task-created paths, not a Git dirty-state claim. Synthetic data is not real-service evidence. Failed, unperformed, simulated and reduced operations remain labelled above. This report assigns no grade.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-02/invalid-state/input.json",
      "owner": "grades-native-02.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/invalid-state/source-manifest.json",
      "owner": "grades-native-02.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/invalid-state/sources",
      "owner": "grades-native-02.json#7",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-02/invalid-state/input.json",
      "owner": "grades-native-02.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/invalid-state/source-manifest.json",
      "owner": "grades-native-02.json#7",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-02/invalid-state/sources",
      "owner": "grades-native-02.json#7",
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
