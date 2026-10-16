# chatgpt: typed-boundary

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "typed-boundary",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-05-08.json#4",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
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
      "attemptId": "grades-chatgpt-05-08.json#4",
      "order": 0,
      "gradeFile": "grades-chatgpt-05-08.json",
      "rankWithinFile": 4,
      "host": "chatgpt",
      "caseId": "typed-boundary",
      "status": "reduced-pass",
      "grade": {
        "caseId": "typed-boundary",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "response",
          "review-outcome",
          "isolated-write"
        ],
        "missing": [
          "Bun typecheck and behavior checks",
          "Actual existing Zod integration rather than the explicitly synthetic parser context",
          "Complete verified application of all patterns-reference practices"
        ],
        "review": "The saved typed refactor concretely replaces optional state bags, unchecked parsing/assertions, dishonest guards and config casts. It preserves number[] for total sum and discloses the local parser stand-in and absent compiler/runtime.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/result.json",
        "variantReview": {
          "reported": [
            [
              "schema and symbols read",
              "attempted",
              "context.ts and patterns read"
            ],
            [
              "isolated text refactor",
              "attempted",
              "work/additional/types/boundary.ts saved/read back"
            ],
            [
              "typecheck and behavior",
              "blocked",
              "Bun absent"
            ],
            [
              "real Zod integration",
              "blocked",
              "Fixture explicitly has no Zod dependency"
            ]
          ],
          "assessment": "Attempted labels are not accepted as successful runtime branches. Fixture reasoning is credited only as a scoped response; blocked/unexercised variants remain unverified."
        },
        "limits": [
          "Baseline-only observations associated with supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c; installed Git revision is not independently established by these artifacts.",
          "Parent independently observed native worker/read/command activity. Exact wrapper arguments, outputs and chunk IDs in the archive remain model-captured, with disclosed early gaps and truncation.",
          "Bun is unavailable. No Node/Python runtime substitution is credited for these cases; shell/jq capture and administration are not workflow execution evidence.",
          "No task Git revision, durable cross-session persistence, live service actions or actual model-family diversity is inferred from content hashes, fixture records, parent dispatch or local file presence.",
          "No Bun; no Node/Python substitution in this continuation",
          "Earlier Node/Python deviation remains part of prior evaluation",
          "Task Git SHA unknown; input content SHA is not revision",
          "Local artifacts retained; durable persistence not established",
          "Early broad reads had truncated outputs in host transcript; later per-source/per-batch raw receipts retained"
        ],
        "reviewedBy": "review_workflow_evidence independent archive/contract review",
        "expectedFull": "Use unknown at entry, UserSchema.parse or safeParse at the boundary and infer the domain type. Replace optional bags with a kind-discriminated union and use inline never exhaustiveness. Verify all guard claims or use existing schema validation. Use NonEmpty<Session> or a Session | undefined result for newest; keep number[] for total sum. Prefer satisfies for config and derive shapes with Pick/Omit/Parameters/ReturnType/Awaited/typeof. Preserve readonly __brand branding and validation before casts, constructive non-empty/pair/start-duration models, the narrowing hierarchy, isX/hasX naming, forward-compatible wire parsing, versioned persisted JSON with try/catch and no deep revalidation. Use object args except hot paths; real framework tests and running UI checks where available; structured diagnostics without shipped console.log. Retain and use the complete patterns reference; report observed check results only.",
        "expectedReduced": "If writes or execution are denied or unavailable, provide the refactor and explain which checks or saves remain unperformed. If a required principle or patterns reference is unavailable, identify the missing dependency and label the review partial. Do not install a schema library or invent repository definitions."
      },
      "topLevelContext": {
        "packageCommit": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "scope": "ChatGPT baseline batches05–08, 32 unique workflow cases",
        "gradingPolicy": "Qualitative full/reduced/blocked outcomes plus actual native observation limits; corrected uncertain-result execution/persistence grants enforced. Model-captured wrappers are not independently raw-event verified; no self-grade imported."
      },
      "response": {
        "text": "The case-owned boundary now uses loading/ready/error discriminants, UserSchema.parse(JSON.parse(payload)), an explicit Session | undefined result for newest, satisfies Config, and the existing schema for isUser. sum keeps number[] and its zero identity. User stays schema-derived; ChecksView uses Pick<ChecksMessage>. The supplied context is a local parser stand-in, not installed Zod. Parse wire data once, version persisted blobs, switch exhaustively over variants, avoid object allocations on measured hot paths, use real behavior tests and structured telemetry. Compiler, runtime, real Zod integration and UI checks remain unperformed because Bun and an installed Zod package are absent.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/result.json",
          "sha256": "100d754f315f155a6633ce234db618a4899c46d5b301cbcf2d40ddff51a521c2",
          "bytes": 1974
        },
        "extraction": "Actual response field when present; otherwise complete retained JSON"
      },
      "evidence": {
        "cloudCaptureIdentity": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/root-tool-log.json",
            "sha256": "667b5681288f125d3857df0388ae65288954542d8545c2b44a420635baa66c49",
            "bytes": 430462
          }
        ],
        "cloudCaptureLimit": "Shared model-captured log identity; attribution/actual operation credit remains limited to independently reviewed case locators and UI corroboration, not every log record.",
        "rawTraces": [],
        "retainedEvidence": [],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/evidence/source-status.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/evidence/source-status.tsv",
      "sha256": "a834d88cbf982384b03e85baab2c7d077bf5992e3b96ae7d78108ae3893a4513",
      "bytes": 102,
      "owners": [
        "grades-chatgpt-05-08.json#4"
      ],
      "text": "0\tskills/typescript-best-practices/SKILL.md\n0\tskills/typescript-best-practices/references/patterns.md\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/result.json",
      "sha256": "100d754f315f155a6633ce234db618a4899c46d5b301cbcf2d40ddff51a521c2",
      "bytes": 1974,
      "owners": [
        "grades-chatgpt-05-08.json#4"
      ],
      "text": "{\n  \"caseId\": \"typed-boundary\",\n  \"batch\": \"batch-05\",\n  \"actualResponse\": \"The case-owned boundary now uses loading/ready/error discriminants, UserSchema.parse(JSON.parse(payload)), an explicit Session | undefined result for newest, satisfies Config, and the existing schema for isUser. sum keeps number[] and its zero identity. User stays schema-derived; ChecksView uses Pick<ChecksMessage>. The supplied context is a local parser stand-in, not installed Zod. Parse wire data once, version persisted blobs, switch exhaustively over variants, avoid object allocations on measured hot paths, use real behavior tests and structured telemetry. Compiler, runtime, real Zod integration and UI checks remain unperformed because Bun and an installed Zod package are absent.\",\n  \"variants\": [\n    [\n      \"schema and symbols read\",\n      \"attempted\",\n      \"context.ts and patterns read\"\n    ],\n    [\n      \"isolated text refactor\",\n      \"attempted\",\n      \"work/additional/types/boundary.ts saved/read back\"\n    ],\n    [\n      \"typecheck and behavior\",\n      \"blocked\",\n      \"Bun absent\"\n    ],\n    [\n      \"real Zod integration\",\n      \"blocked\",\n      \"Fixture explicitly has no Zod dependency\"\n    ]\n  ],\n  \"observedOperations\": [\n    \"tools.exec_command source/case/fixture reads and caller search\",\n    \"tools.apply_patch retained isolated artifacts\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"input/\",\n    \"work/\",\n    \"evidence/source-status.tsv\",\n    \"../../source-read-receipts.json\",\n    \"../../support-read-receipts.json\",\n    \"../../fixture-read-receipt.json\"\n  ],\n  \"limits\": [\n    \"No Bun; no Node/Python substitution in this continuation\",\n    \"Earlier Node/Python deviation remains part of prior evaluation\",\n    \"Task Git SHA unknown; input content SHA is not revision\",\n    \"Local artifacts retained; durable persistence not established\",\n    \"Early broad reads had truncated outputs in host transcript; later per-source/per-batch raw receipts retained\"\n  ]\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/types/boundary.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/types/boundary.ts",
      "sha256": "3a0481cec33f679bc569084f1501503c744475b46dc6203924fa27b6ea1027d8",
      "bytes": 750,
      "owners": [
        "grades-chatgpt-05-08.json#4"
      ],
      "text": "import { UserSchema } from './context';\nimport type { User, Session, Config, ChecksMessage } from './context';\nexport type State = { kind: 'loading' } | { kind: 'ready'; user: User } | { kind: 'error'; error: string };\nexport function decode(payload: string): User { const value: unknown = JSON.parse(payload); return UserSchema.parse(value); }\nexport function newest(xs: Session[]): Session | undefined { return xs.at(0); }\nexport function sum(xs: number[]) { return xs.reduce((a,b) => a+b, 0); }\nexport const config = { theme: 'dark', cols: 3 } satisfies Config;\nexport function isUser(x: unknown): x is User { try { UserSchema.parse(x); return true; } catch { return false; } }\nexport type ChecksView = Pick<ChecksMessage, 'revision' | 'checks'>;\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/case.json",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/evidence/sources",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/input",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/README.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/README.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/README.md",
      "sha256": "d196849f4d82de3618f0e530cdddc68d486b3b2cd7ec807fa1a98412ddc4532c",
      "bytes": 797
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/cache/README.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/README.md",
      "sha256": "b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551",
      "bytes": 509
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/cache/cache.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/cache/caller.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/cache/invalidation.diff",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/invalidation.diff",
      "sha256": "0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7",
      "bytes": 365
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/cache/manifest.json",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/cache/probe.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/cache/vendor/disposer-v1.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/corpus/records.jsonl",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/corpus/records.jsonl",
      "sha256": "bba536a5394a6ddb455eddd0d9f04f67426bc5f9ef08325d543aab696a94a061",
      "bytes": 46932
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/dead-path/caller.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/dead-path/duplicate-reference.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/dead-path/handler.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/dead-path/instructions.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/dead-path/scope.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/history/capsule.json",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/capsule.json",
      "sha256": "68475aad9893f5968ac61b2c68b9e1dda09450d5a631bce1fbb5394e562b5568",
      "bytes": 691
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/history/history.json",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/history/jay-mode.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/jay-mode.md",
      "sha256": "477ba7aaaeab112324c1ee03db183869bc46ec8f4bdc4b8b76dceeb6ca563f3f",
      "bytes": 372
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/history/shared-records.json",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/shared-records.json",
      "sha256": "7859c51afe5feade4176ed6f0c4c9a6aff7141e83df0a32f71c455d70a1b94c1",
      "bytes": 950
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/invoice/adapter.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/invoice/calculator.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/invoice/controller.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/invoice/decision.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/invoice/exporter.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/invoice/facade.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/invoice/formatter.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/legal-header/source.diff",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.diff",
      "sha256": "da37375054eb4140f6b2ba19dac4c5de3846183029177d58473b38d320cf8436",
      "bytes": 671
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/legal-header/source.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.mjs",
      "sha256": "7579a6b456d0cd513fd8f55d69096119304833f0dc5dfca7f66c727ec002df91",
      "bytes": 553
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/migration/api.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/migration/contract.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/contract.mjs",
      "sha256": "1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da",
      "bytes": 314
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/migration/notification.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/migration/profile.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/migration/scope.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/scenario-map.json",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/scenario-map.json",
      "sha256": "a732248ad7fdf1f003452602cd92f3571201ce6b2839569246f02155311a9a0b",
      "bytes": 2593
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/types/README.md",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/additional/types/context.ts",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/dashboard.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/forge.json",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/history.json",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/invoice.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/orders.json",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-05/cases/typed-boundary/work/runtime.mjs",
      "owner": "grades-chatgpt-05-08.json#4",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
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
