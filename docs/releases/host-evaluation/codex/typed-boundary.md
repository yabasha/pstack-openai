# codex: typed-boundary

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "typed-boundary",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-05.json#4",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Review and refactor this TypeScript using the repository existing Zod schemas. UserSchema owns id and name, and ChecksMessage is a generated schema type. Code: type State = { loading: boolean; user?: User; error?: string }; const user = JSON.parse(payload) as User; function newest(xs: Session[]): Session { return xs.at(0)!; } function sum(xs: number[]) { return xs.reduce((a,b)=>a+b,0); } const config = { theme: \"dark\", cols: 3 } as Config; function isUser(x: unknown): x is User { return typeof x === \"object\" && x !== null && \"id\" in x; } Read patterns.md and explain additional source practices applicable to typed boundaries, generated types, guards, variant handling, hot paths, real tests, and telemetry.",
  "caseDefinition": {
    "id": "typed-boundary",
    "sourcePaths": [
      "skills/typescript-best-practices/SKILL.md",
      "skills/typescript-best-practices/references/patterns.md"
    ],
    "prompt": "Review and refactor this TypeScript using the repository existing Zod schemas. UserSchema owns id and name, and ChecksMessage is a generated schema type. Code: type State = { loading: boolean; user?: User; error?: string }; const user = JSON.parse(payload) as User; function newest(xs: Session[]): Session { return xs.at(0)!; } function sum(xs: number[]) { return xs.reduce((a,b)=>a+b,0); } const config = { theme: \"dark\", cols: 3 } as Config; function isUser(x: unknown): x is User { return typeof x === \"object\" && x !== null && \"id\" in x; } Read patterns.md and explain additional source practices applicable to typed boundaries, generated types, guards, variant handling, hot paths, real tests, and telemetry.",
    "requirements": [
      "Read the complete leaf, patterns reference, type-system-discipline principle and boundary-discipline principle.",
      "Apply the concrete rules to provided code; reuse existing schema validation and derive types rather than duplicating an interface or adding a dependency.",
      "Read repository symbols before saved edits and run available authorized checks; report unavailable checks."
    ],
    "expectedFull": "Use unknown at entry, UserSchema.parse or safeParse at the boundary and infer the domain type. Replace optional bags with a kind-discriminated union and use inline never exhaustiveness. Verify all guard claims or use existing schema validation. Use NonEmpty<Session> or a Session | undefined result for newest; keep number[] for total sum. Prefer satisfies for config and derive shapes with Pick/Omit/Parameters/ReturnType/Awaited/typeof. Preserve readonly __brand branding and validation before casts, constructive non-empty/pair/start-duration models, the narrowing hierarchy, isX/hasX naming, forward-compatible wire parsing, versioned persisted JSON with try/catch and no deep revalidation. Use object args except hot paths; real framework tests and running UI checks where available; structured diagnostics without shipped console.log. Retain and use the complete patterns reference; report observed check results only.",
    "expectedReduced": "If writes or execution are denied or unavailable, provide the refactor and explain which checks or saves remain unperformed. If a required principle or patterns reference is unavailable, identify the missing dependency and label the review partial. Do not install a schema library or invent repository definitions.",
    "expectedBlocked": "If neither provided TypeScript nor repository input can be read, state the missing input and stop before claiming a review or refactor. Identify denied read access explicitly.",
    "forbiddenClaims": [
      "Generic typing advice replacing concrete source practices or omitting patterns.md.",
      "Unchecked casts, a lying guard, any for external data, duplicate schema interfaces, or a new schema dependency for one guard.",
      "Unnecessary NonEmpty types for total operations or changed hot-path allocation exceptions.",
      "Claims of saved edits, compile/test/UI success, metadata enforcement, or host parity without observed evidence."
    ],
    "caseFile": "docs/parity/cases/skills/typescript-best-practices.json"
  },
  "registry": {
    "caseId": "typed-boundary",
    "caseFile": "docs/parity/cases/skills/typescript-best-practices.json",
    "sourcePaths": [
      "skills/typescript-best-practices/SKILL.md",
      "skills/typescript-best-practices/references/patterns.md"
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
      "attemptId": "grades-native-05.json#4",
      "order": 0,
      "gradeFile": "grades-native-05.json",
      "rankWithinFile": 4,
      "host": "codex",
      "caseId": "typed-boundary",
      "status": "reduced-pass",
      "grade": {
        "caseId": "typed-boundary",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-05.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_9"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Actual requested existing Zod package/integration unavailable; local parse interface only.",
          "Compiler and actual exhaustiveness rejection unobserved."
        ],
        "review": "Actual fixture refactor reuses local UserSchema parse/type inference, validates unknown JSON, replaces optional bag, removes unsafe at(0) assertion, uses satisfies and repairs lying guard. Complete patterns discussed. Local validator is explicitly stand-in, so no actual repository Zod integration/compiler behavior is credited.",
        "responseArtifact": "fixtures/batch-05/typed-boundary.result.md",
        "variantReview": [
          "Actual attempted variants and explicitly simulated conditions inspected in response artifact. No synthetic service/worker receipt credited."
        ],
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-05.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "Use unknown at entry, UserSchema.parse or safeParse at the boundary and infer the domain type. Replace optional bags with a kind-discriminated union and use inline never exhaustiveness. Verify all guard claims or use existing schema validation. Use NonEmpty<Session> or a Session | undefined result for newest; keep number[] for total sum. Prefer satisfies for config and derive shapes with Pick/Omit/Parameters/ReturnType/Awaited/typeof. Preserve readonly __brand branding and validation before casts, constructive non-empty/pair/start-duration models, the narrowing hierarchy, isX/hasX naming, forward-compatible wire parsing, versioned persisted JSON with try/catch and no deep revalidation. Use object args except hot paths; real framework tests and running UI checks where available; structured diagnostics without shipped console.log. Retain and use the complete patterns reference; report observed check results only.",
        "reducedExpected": "If writes or execution are denied or unavailable, provide the refactor and explain which checks or saves remain unperformed. If a required principle or patterns reference is unavailable, identify the missing dependency and label the review partial. Do not install a schema library or invent repository definitions."
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
        "text": "# typed-boundary\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"typed-boundary\",\n  \"prompt\": \"Review and refactor this TypeScript using the repository existing Zod schemas. UserSchema owns id and name, and ChecksMessage is a generated schema type. Code: type State = { loading: boolean; user?: User; error?: string }; const user = JSON.parse(payload) as User; function newest(xs: Session[]): Session { return xs.at(0)!; } function sum(xs: number[]) { return xs.reduce((a,b)=>a+b,0); } const config = { theme: \\\"dark\\\", cols: 3 } as Config; function isUser(x: unknown): x is User { return typeof x === \\\"object\\\" && x !== null && \\\"id\\\" in x; } Read patterns.md and explain additional source practices applicable to typed boundaries, generated types, guards, variant handling, hot paths, real tests, and telemetry.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Read the complete leaf, patterns reference, type-system-discipline principle and boundary-discipline principle.\",\n    \"Apply the concrete rules to provided code; reuse existing schema validation and derive types rather than duplicating an interface or adding a dependency.\",\n    \"Read repository symbols before saved edits and run available authorized checks; report unavailable checks.\"\n  ]\n}\n```\n\n## Actual response and output\n\nI read boundary.ts, context.ts and the fixture README before editing the case-owned copy. context.ts already derives User with Output<typeof UserSchema>. I reused that type and UserSchema.parse, replaced the optional State bag with loading, ready and error variants, parsed JSON into unknown, and replaced the config cast with satisfies Config. isUser now validates both id and name through the same schema. newest returns Session | undefined and accepts an empty array explicitly. sum keeps number[] and sum([])=0. No dependency was added.\n\nThe actual fixture has a local parse interface, not installed Zod. The saved code therefore executes the supplied validator stand-in. In a real Zod repository, derive User with z.infer<typeof UserSchema>, use parse at the input boundary and safeParse when rejection is an expected branch. The supplied interface has no safeParse, so the existing boolean guard uses parse with try/catch. No duplicate User interface or hand-written property guard was added. No saved State consumer exists in the supplied scope; changing its contract may require migration in a larger repository. newest retains the existing first-item ordering assumption and does not sort sessions.\n\nThe baseline actually accepted {id:'u1'} in isUser and decoded {id:42}. After editing, real Bun assertions rejected five invalid shapes and malformed JSON, accepted a valid user, returned undefined for newest([]), and preserved summation and config values. Bun transpiles TypeScript but does not prove its types. Compiler discovery returned tsc=null. No compiler, actual Zod integration, framework or running UI check was available or claimed.\n\nAdditional practices from the complete patterns reference follow.\n\n- Derive smaller generated shapes with Pick<ChecksMessage, 'revision' | 'checks'>. The supplied ChecksMessage does not contain totalCount, so do not copy that generic example blindly. Prefer Pick, Omit, Parameters, ReturnType, Awaited and typeof to a parallel interface.\n- Handle State by its kind. A switch's default arm should assign the remaining value to an inline never local. This makes a new variant visible to the compiler when a compiler is available. Prefer discriminant narrowing, then in, typeof or instanceof, then a truthful isX or hasX guard. Casts remain a last resort after validation.\n- Validate external unknown once and trust the domain type inside. Forward-compatible wire parsing can ignore unknown fields using the actual protocol library option. Persisted JSON needs a versioned blob, guarded parse and an explicit migration or rejection policy. Do not repeat validation down the call chain.\n- Strengthen newest to [Session, ...Session[]] only if its callers require a guaranteed answer and can establish nonemptiness at entry. Keep plain arrays for total functions such as sum. Pairs can encode even length. Start plus duration avoids independently synchronized endpoints, but a plain number still permits a negative duration and needs boundary validation. Do not claim that example alone forbids negatives.\n- Brand semantic primitives only when they can otherwise be confused, using the source's readonly __brand convention. Validate before constructing or casting the brand. A brand alone performs no runtime validation.\n- Prefer object arguments for meaningful named inputs. Preserve positional arguments in measured tight parser, tokenizer or frame paths where allocations matter. No hot path or allocation result was measured here.\n- Run real framework test primitives when present, include leak or disposal checks where relevant, and verify UI in a running build. These local assertions call real modules without mocks. They do not supply missing framework or UI evidence.\n- Use structured logger events with a correlation id and useful nonsecret context. Do not ship console.log telemetry. Console output here belongs only to evaluation probes. No logger or real telemetry system was supplied or contacted.\n\n## Variants attempted and limits\n\nOriginal and refactored boundaries ran against valid input, empty arrays and selected malformed inputs. Actual Zod and compiler variants could not run because they are absent. The fixture validator is explicitly a stand-in.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\".\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before\"] | 0 | [typed-boundary/callers-before.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/callers-before.json) |\n| [\"diff\",\"-ru\",\"before\",\"work\"] | 1 | [typed-boundary/diff.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/diff.json) |\n| [\"bun\",\"--no-install\",\"probe.ts\",\"work\"] | 0 | [typed-boundary/after.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/after.json) |\n| [\"bun\",\"--no-install\",\"probe.ts\",\"before\"] | 0 | [typed-boundary/baseline.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/baseline.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"console.log(JSON.stringify({tsc:Bun.which(\\\"tsc\\\"),bun:Bun.version}));\"] | 0 | [typed-boundary/compiler-discovery.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/compiler-discovery.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### after.json\n\nExit 0.\n\n```text\n{\"validDecoded\":{\"id\":\"u1\",\"name\":\"Ada\"},\"invalidShapesRejected\":5,\"malformedJson\":\"SyntaxError\",\"emptyNewest\":\"undefined\",\"sumEmpty\":0,\"config\":{\"theme\":\"dark\",\"cols\":3}}\n\n```\n\n### baseline.json\n\nExit 0.\n\n```text\n{\"missingNameAccepted\":true,\"invalidDecoded\":{\"id\":42},\"emptyNewest\":null,\"sumEmpty\":0}\n\n```\n\n### compiler-discovery.json\n\nExit 0.\n\n```text\n{\"tsc\":null,\"bun\":\"1.4.2\"}\n\n```\n\n",
        "artifact": {
          "path": "fixtures/batch-05/typed-boundary.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary.result.md",
          "sha256": "6338d26877ecdf9f961803930c92812b9043a3307f71685d40b0fb16caa16b38",
          "bytes": 9490
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
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f1c48be46010119dbe06f2cbc85ca2abe322d6b84492564e3fa7211fb839d21c"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "b57fbafa7d63dfa2af17d30aeb1adf47dc514ff1e1166376fc9bced16aad71f5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_9",
                "line": 17,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f9593bde002eb29160b8fd56851d67734d97a1442e3c4e732bce4986c26f9a4d"
              },
              {
                "eventId": "item_9",
                "line": 18,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "0763655241272747bda613e8a7bca3fda7f229be1b108338d12665a77ed48712",
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
            "item_9"
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
      "path": "fixtures/batch-05/typed-boundary/after.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/after.json",
      "sha256": "3b2380c5246ef0646a2f675b725145d7da249b6eef7b84935daa9bdb50d62b01",
      "bytes": 436,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"probe.ts\",\n    \"work\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"validDecoded\\\":{\\\"id\\\":\\\"u1\\\",\\\"name\\\":\\\"Ada\\\"},\\\"invalidShapesRejected\\\":5,\\\"malformedJson\\\":\\\"SyntaxError\\\",\\\"emptyNewest\\\":\\\"undefined\\\",\\\"sumEmpty\\\":0,\\\"config\\\":{\\\"theme\\\":\\\"dark\\\",\\\"cols\\\":3}}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/baseline.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/baseline.json",
      "sha256": "344d8d4a12f3ee3b9bd429ce060269338703d024cd8c032e96e61dcfee47a81a",
      "bytes": 334,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"probe.ts\",\n    \"before\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"missingNameAccepted\\\":true,\\\"invalidDecoded\\\":{\\\"id\\\":42},\\\"emptyNewest\\\":null,\\\"sumEmpty\\\":0}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/callers-before.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/callers-before.json",
      "sha256": "fba9604a85b15c0aa0d29161a73a3a186a58cc246df172b4e8e743c115e952e7",
      "bytes": 5098,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "{\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \".\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary\",\n  \"exitCode\": 0,\n  \"stdout\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/boundary.ts:1:import type { User, Session, Config } from './context';\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/boundary.ts:2:export type State = { loading: boolean; user?: User; error?: string };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/boundary.ts:3:export function decode(payload: string) { return JSON.parse(payload) as User; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/boundary.ts:4:export function newest(xs: Session[]): Session { return xs.at(0)!; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/boundary.ts:5:export function sum(xs: number[]) { return xs.reduce((a,b) => a+b, 0); }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/boundary.ts:6:export const config = { theme: 'dark', cols: 3 } as Config;\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/boundary.ts:7:export function isUser(x: unknown): x is User { return typeof x === 'object' && x !== null && 'id' in x; }\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/README.md:1:For typed-boundary: existing shared context.ts provides the actual fixture UserSchema symbols and generated ChecksMessage. The repository has no installed Zod in this fixture, so literal Zod-package integration remains unavailable. Reuse the supplied parse contract, derive User, preserve sum([]) = 0 and make newest empty behavior explicit. Do not install a validator. Schema is a local stand-in and must not be described as executed Zod. Review patterns.md in the tested package as the case requires.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:1:// Self-contained declarations for reading/refactoring the supplied boundary example.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:2:// These are fixture declarations of an existing validator interface, not an installed Zod package.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:3:export type Schema<T> = { parse(value: unknown): T };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:4:export const UserSchema: Schema<{ id: string; name: string }> = {\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:5:  parse(value) {\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:6:    if (typeof value !== 'object' || value === null || !('id' in value) || !('name' in value)\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:7:      || typeof value.id !== 'string' || typeof value.name !== 'string') throw new Error('invalid user');\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:8:    return { id: value.id, name: value.name };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:9:  },\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:10:};\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:11:export type Output<S extends Schema<unknown>> = ReturnType<S['parse']>;\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:12:export type User = Output<typeof UserSchema>;\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:13:export type Session = { id: string; createdAt: number };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:14:export type Config = { theme: 'dark' | 'light'; cols: number };\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:15:// Generated schema contract: consumers import this type rather than duplicating it.\\n/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before/context.ts:16:export type ChecksMessage = { kind: 'checks'; revision: string; checks: readonly string[] };\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/compiler-discovery.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/compiler-discovery.json",
      "sha256": "c5c1f2b47dda5f6344688be9444328e0cb6220a792dc615ab2da1461b44539fd",
      "bytes": 327,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"console.log(JSON.stringify({tsc:Bun.which(\\\"tsc\\\"),bun:Bun.version}));\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"tsc\\\":null,\\\"bun\\\":\\\"1.4.2\\\"}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/diff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/diff.json",
      "sha256": "9a9848b7d07d1920e0a8434a7c4521904ff6104fd01efd6b190e15bcc423d564",
      "bytes": 1488,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "{\n  \"argv\": [\n    \"diff\",\n    \"-ru\",\n    \"before\",\n    \"work\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary\",\n  \"exitCode\": 1,\n  \"stdout\": \"diff -ru before/boundary.ts work/boundary.ts\\n--- before/boundary.ts\\t2026-10-16 10:42:33\\n+++ work/boundary.ts\\t2026-10-16 10:50:55\\n@@ -1,7 +1,17 @@\\n import type { User, Session, Config } from './context';\\n-export type State = { loading: boolean; user?: User; error?: string };\\n-export function decode(payload: string) { return JSON.parse(payload) as User; }\\n-export function newest(xs: Session[]): Session { return xs.at(0)!; }\\n+import { UserSchema } from './context';\\n+export type State =\\n+  | { kind: 'loading' }\\n+  | { kind: 'ready'; user: User }\\n+  | { kind: 'error'; error: string };\\n+export function decode(payload: string): User {\\n+  const value: unknown = JSON.parse(payload);\\n+  return UserSchema.parse(value);\\n+}\\n+export function newest(xs: Session[]): Session | undefined { return xs.at(0); }\\n export function sum(xs: number[]) { return xs.reduce((a,b) => a+b, 0); }\\n-export const config = { theme: 'dark', cols: 3 } as Config;\\n-export function isUser(x: unknown): x is User { return typeof x === 'object' && x !== null && 'id' in x; }\\n+export const config = { theme: 'dark', cols: 3 } satisfies Config;\\n+export function isUser(x: unknown): x is User {\\n+  try { UserSchema.parse(x); return true; }\\n+  catch { return false; }\\n+}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/input-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/input-manifest.json",
      "sha256": "e31ae10048596eb7b95f73d7898c16dad952e8dcd47d9e889a4fd2a359821a3f",
      "bytes": 641,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "{\n  \"inputSha256\": \"45c37b527bd3e4f4f9f6ac8e8036691adc045ef68a96b498bf1a9b855c119b80\",\n  \"taskGitSha\": null,\n  \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageFreezeIndependentlyVerified\": false,\n  \"fixtures\": [\n    {\n      \"path\": \"before/context.ts\",\n      \"sha256\": \"862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58\"\n    },\n    {\n      \"path\": \"before/README.md\",\n      \"sha256\": \"201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588\"\n    },\n    {\n      \"path\": \"before/boundary.ts\",\n      \"sha256\": \"5e98773209677f72d526c420f60a406972988e8fc0067963f781fe5955188e42\"\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/probe.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/probe.ts",
      "sha256": "0c0c82e6b3381595a41e855c43c73b85c993d72664cacb81b9109df9b183db60",
      "bytes": 1067,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "import assert from 'node:assert/strict';\nconst dir=process.argv[2];\nconst m=await import(`./${dir}/boundary.ts`);\nconst valid={id:'u1',name:'Ada'};\nassert.deepEqual(m.decode(JSON.stringify(valid)),valid);\nassert.equal(m.sum([]),0);\nassert.equal(m.sum([1,-2,4]),3);\nassert.deepEqual(m.newest([{id:'s1',createdAt:2},{id:'s2',createdAt:1}]),{id:'s1',createdAt:2});\nassert.equal(m.newest([]),undefined);\nif(dir==='before') {\n  console.log(JSON.stringify({missingNameAccepted:m.isUser({id:'u1'}),invalidDecoded:m.decode('{\"id\":42}'),emptyNewest:m.newest([])??null,sumEmpty:m.sum([])}));\n} else {\n  for(const x of [null,{}, {id:'u1'}, {id:42,name:'Ada'}, {id:'u1',name:42}]) {\n    assert.equal(m.isUser(x),false);\n    assert.throws(()=>m.decode(JSON.stringify(x)),{message:'invalid user'});\n  }\n  assert.equal(m.isUser(valid),true);\n  assert.throws(()=>m.decode('{'),SyntaxError);\n  console.log(JSON.stringify({validDecoded:m.decode(JSON.stringify(valid)),invalidShapesRejected:5,malformedJson:'SyntaxError',emptyNewest:'undefined',sumEmpty:m.sum([]),config:m.config}));\n}\n"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/registered-case.json",
      "sha256": "2c61e1787d6e1b56c3300f2a87102a7fec4141d2f0dbe79ad13daee3006f1bfe",
      "bytes": 3269,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "{\n  \"id\": \"typed-boundary\",\n  \"sourcePaths\": [\n    \"skills/typescript-best-practices/SKILL.md\",\n    \"skills/typescript-best-practices/references/patterns.md\"\n  ],\n  \"prompt\": \"Review and refactor this TypeScript using the repository existing Zod schemas. UserSchema owns id and name, and ChecksMessage is a generated schema type. Code: type State = { loading: boolean; user?: User; error?: string }; const user = JSON.parse(payload) as User; function newest(xs: Session[]): Session { return xs.at(0)!; } function sum(xs: number[]) { return xs.reduce((a,b)=>a+b,0); } const config = { theme: \\\"dark\\\", cols: 3 } as Config; function isUser(x: unknown): x is User { return typeof x === \\\"object\\\" && x !== null && \\\"id\\\" in x; } Read patterns.md and explain additional source practices applicable to typed boundaries, generated types, guards, variant handling, hot paths, real tests, and telemetry.\",\n  \"requirements\": [\n    \"Read the complete leaf, patterns reference, type-system-discipline principle and boundary-discipline principle.\",\n    \"Apply the concrete rules to provided code; reuse existing schema validation and derive types rather than duplicating an interface or adding a dependency.\",\n    \"Read repository symbols before saved edits and run available authorized checks; report unavailable checks.\"\n  ],\n  \"expectedFull\": \"Use unknown at entry, UserSchema.parse or safeParse at the boundary and infer the domain type. Replace optional bags with a kind-discriminated union and use inline never exhaustiveness. Verify all guard claims or use existing schema validation. Use NonEmpty<Session> or a Session | undefined result for newest; keep number[] for total sum. Prefer satisfies for config and derive shapes with Pick/Omit/Parameters/ReturnType/Awaited/typeof. Preserve readonly __brand branding and validation before casts, constructive non-empty/pair/start-duration models, the narrowing hierarchy, isX/hasX naming, forward-compatible wire parsing, versioned persisted JSON with try/catch and no deep revalidation. Use object args except hot paths; real framework tests and running UI checks where available; structured diagnostics without shipped console.log. Retain and use the complete patterns reference; report observed check results only.\",\n  \"expectedReduced\": \"If writes or execution are denied or unavailable, provide the refactor and explain which checks or saves remain unperformed. If a required principle or patterns reference is unavailable, identify the missing dependency and label the review partial. Do not install a schema library or invent repository definitions.\",\n  \"expectedBlocked\": \"If neither provided TypeScript nor repository input can be read, state the missing input and stop before claiming a review or refactor. Identify denied read access explicitly.\",\n  \"forbiddenClaims\": [\n    \"Generic typing advice replacing concrete source practices or omitting patterns.md.\",\n    \"Unchecked casts, a lying guard, any for external data, duplicate schema interfaces, or a new schema dependency for one guard.\",\n    \"Unnecessary NonEmpty types for total operations or changed hot-path allocation exceptions.\",\n    \"Claims of saved edits, compile/test/UI success, metadata enforcement, or host parity without observed evidence.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/work/boundary.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/work/boundary.ts",
      "sha256": "1b18fab0a648cc119566180780512174550d75d5ea83391ff27ebbf4e163884f",
      "bytes": 682,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "import type { User, Session, Config } from './context';\nimport { UserSchema } from './context';\nexport type State =\n  | { kind: 'loading' }\n  | { kind: 'ready'; user: User }\n  | { kind: 'error'; error: string };\nexport function decode(payload: string): User {\n  const value: unknown = JSON.parse(payload);\n  return UserSchema.parse(value);\n}\nexport function newest(xs: Session[]): Session | undefined { return xs.at(0); }\nexport function sum(xs: number[]) { return xs.reduce((a,b) => a+b, 0); }\nexport const config = { theme: 'dark', cols: 3 } satisfies Config;\nexport function isUser(x: unknown): x is User {\n  try { UserSchema.parse(x); return true; }\n  catch { return false; }\n}\n"
    },
    {
      "path": "fixtures/batch-05/typed-boundary.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary.result.md",
      "sha256": "6338d26877ecdf9f961803930c92812b9043a3307f71685d40b0fb16caa16b38",
      "bytes": 9490,
      "owners": [
        "grades-native-05.json#4"
      ],
      "text": "# typed-boundary\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"typed-boundary\",\n  \"prompt\": \"Review and refactor this TypeScript using the repository existing Zod schemas. UserSchema owns id and name, and ChecksMessage is a generated schema type. Code: type State = { loading: boolean; user?: User; error?: string }; const user = JSON.parse(payload) as User; function newest(xs: Session[]): Session { return xs.at(0)!; } function sum(xs: number[]) { return xs.reduce((a,b)=>a+b,0); } const config = { theme: \\\"dark\\\", cols: 3 } as Config; function isUser(x: unknown): x is User { return typeof x === \\\"object\\\" && x !== null && \\\"id\\\" in x; } Read patterns.md and explain additional source practices applicable to typed boundaries, generated types, guards, variant handling, hot paths, real tests, and telemetry.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Read the complete leaf, patterns reference, type-system-discipline principle and boundary-discipline principle.\",\n    \"Apply the concrete rules to provided code; reuse existing schema validation and derive types rather than duplicating an interface or adding a dependency.\",\n    \"Read repository symbols before saved edits and run available authorized checks; report unavailable checks.\"\n  ]\n}\n```\n\n## Actual response and output\n\nI read boundary.ts, context.ts and the fixture README before editing the case-owned copy. context.ts already derives User with Output<typeof UserSchema>. I reused that type and UserSchema.parse, replaced the optional State bag with loading, ready and error variants, parsed JSON into unknown, and replaced the config cast with satisfies Config. isUser now validates both id and name through the same schema. newest returns Session | undefined and accepts an empty array explicitly. sum keeps number[] and sum([])=0. No dependency was added.\n\nThe actual fixture has a local parse interface, not installed Zod. The saved code therefore executes the supplied validator stand-in. In a real Zod repository, derive User with z.infer<typeof UserSchema>, use parse at the input boundary and safeParse when rejection is an expected branch. The supplied interface has no safeParse, so the existing boolean guard uses parse with try/catch. No duplicate User interface or hand-written property guard was added. No saved State consumer exists in the supplied scope; changing its contract may require migration in a larger repository. newest retains the existing first-item ordering assumption and does not sort sessions.\n\nThe baseline actually accepted {id:'u1'} in isUser and decoded {id:42}. After editing, real Bun assertions rejected five invalid shapes and malformed JSON, accepted a valid user, returned undefined for newest([]), and preserved summation and config values. Bun transpiles TypeScript but does not prove its types. Compiler discovery returned tsc=null. No compiler, actual Zod integration, framework or running UI check was available or claimed.\n\nAdditional practices from the complete patterns reference follow.\n\n- Derive smaller generated shapes with Pick<ChecksMessage, 'revision' | 'checks'>. The supplied ChecksMessage does not contain totalCount, so do not copy that generic example blindly. Prefer Pick, Omit, Parameters, ReturnType, Awaited and typeof to a parallel interface.\n- Handle State by its kind. A switch's default arm should assign the remaining value to an inline never local. This makes a new variant visible to the compiler when a compiler is available. Prefer discriminant narrowing, then in, typeof or instanceof, then a truthful isX or hasX guard. Casts remain a last resort after validation.\n- Validate external unknown once and trust the domain type inside. Forward-compatible wire parsing can ignore unknown fields using the actual protocol library option. Persisted JSON needs a versioned blob, guarded parse and an explicit migration or rejection policy. Do not repeat validation down the call chain.\n- Strengthen newest to [Session, ...Session[]] only if its callers require a guaranteed answer and can establish nonemptiness at entry. Keep plain arrays for total functions such as sum. Pairs can encode even length. Start plus duration avoids independently synchronized endpoints, but a plain number still permits a negative duration and needs boundary validation. Do not claim that example alone forbids negatives.\n- Brand semantic primitives only when they can otherwise be confused, using the source's readonly __brand convention. Validate before constructing or casting the brand. A brand alone performs no runtime validation.\n- Prefer object arguments for meaningful named inputs. Preserve positional arguments in measured tight parser, tokenizer or frame paths where allocations matter. No hot path or allocation result was measured here.\n- Run real framework test primitives when present, include leak or disposal checks where relevant, and verify UI in a running build. These local assertions call real modules without mocks. They do not supply missing framework or UI evidence.\n- Use structured logger events with a correlation id and useful nonsecret context. Do not ship console.log telemetry. Console output here belongs only to evaluation probes. No logger or real telemetry system was supplied or contacted.\n\n## Variants attempted and limits\n\nOriginal and refactored boundaries ran against valid input, empty arrays and selected malformed inputs. Actual Zod and compiler variants could not run because they are absent. The fixture validator is explicitly a stand-in.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"rg\",\"-n\",\".\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/before\"] | 0 | [typed-boundary/callers-before.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/callers-before.json) |\n| [\"diff\",\"-ru\",\"before\",\"work\"] | 1 | [typed-boundary/diff.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/diff.json) |\n| [\"bun\",\"--no-install\",\"probe.ts\",\"work\"] | 0 | [typed-boundary/after.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/after.json) |\n| [\"bun\",\"--no-install\",\"probe.ts\",\"before\"] | 0 | [typed-boundary/baseline.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/baseline.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"console.log(JSON.stringify({tsc:Bun.which(\\\"tsc\\\"),bun:Bun.version}));\"] | 0 | [typed-boundary/compiler-discovery.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/typed-boundary/compiler-discovery.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### after.json\n\nExit 0.\n\n```text\n{\"validDecoded\":{\"id\":\"u1\",\"name\":\"Ada\"},\"invalidShapesRejected\":5,\"malformedJson\":\"SyntaxError\",\"emptyNewest\":\"undefined\",\"sumEmpty\":0,\"config\":{\"theme\":\"dark\",\"cols\":3}}\n\n```\n\n### baseline.json\n\nExit 0.\n\n```text\n{\"missingNameAccepted\":true,\"invalidDecoded\":{\"id\":42},\"emptyNewest\":null,\"sumEmpty\":0}\n\n```\n\n### compiler-discovery.json\n\nExit 0.\n\n```text\n{\"tsc\":null,\"bun\":\"1.4.2\"}\n\n```\n\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-05/typed-boundary/before",
      "owner": "grades-native-05.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/input.json",
      "owner": "grades-native-05.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/source-manifest.json",
      "owner": "grades-native-05.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/source-read",
      "owner": "grades-native-05.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/work/README.md",
      "owner": "grades-native-05.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "fixtures/batch-05/typed-boundary/work/context.ts",
      "owner": "grades-native-05.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
    },
    {
      "path": "fixtures/batch-05/typed-boundary/before",
      "owner": "grades-native-05.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/input.json",
      "owner": "grades-native-05.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/source-manifest.json",
      "owner": "grades-native-05.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/source-read",
      "owner": "grades-native-05.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/typed-boundary/work/README.md",
      "owner": "grades-native-05.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "fixtures/batch-05/typed-boundary/work/context.ts",
      "owner": "grades-native-05.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
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
