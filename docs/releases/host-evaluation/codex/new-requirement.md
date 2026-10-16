# codex: new-requirement

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "new-requirement",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-03.json#4",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Add multi-tenant ownership to an existing single-tenant design. Read the affected files, redesign the structure as if tenant ownership had been present from day one, and deliver coherent increments within authorized scope.",
  "caseDefinition": {
    "id": "new-requirement",
    "sourcePaths": [
      "skills/principle-redesign-from-first-principles/SKILL.md"
    ],
    "prompt": "Add multi-tenant ownership to an existing single-tenant design. Read the affected files, redesign the structure as if tenant ownership had been present from day one, and deliver coherent increments within authorized scope.",
    "requirements": [
      "Available affected source and current design",
      "Authorized scope and available read capability",
      "Write and execution capabilities for implementation and checks"
    ],
    "expectedFull": "Read all affected files, compare the design with a fresh design that assumes tenant ownership, redesign the affected structure instead of stacking a workaround, propagate the change through types, docs, examples and rationale, and deliver the whole redesign incrementally. Report only observed edits and checks.",
    "expectedReduced": "With source available but writes or execution unavailable, provide a concrete redesign and incremental sequence as reduced capability. Identify unperformed edits and checks and preserve authorization boundaries.",
    "expectedBlocked": "If affected source or required design context is unavailable, identify the missing inputs and keep any redesign provisional. Do not claim the current design was inspected or changed.",
    "forbiddenClaims": [
      "A workaround stacked onto existing structure satisfies the redesign",
      "Implementation or checks occurred without observed authorized operations",
      "Source review or structural checks prove host behavioral parity",
      "Unavailable source was inspected",
      "The principle grants broader write or external permissions"
    ],
    "caseFile": "docs/parity/cases/skills/principle-redesign-from-first-principles.json"
  },
  "registry": {
    "caseId": "new-requirement",
    "caseFile": "docs/parity/cases/skills/principle-redesign-from-first-principles.json",
    "sourcePaths": [
      "skills/principle-redesign-from-first-principles/SKILL.md"
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
      "attemptId": "grades-native-03.json#4",
      "order": 0,
      "gradeFile": "grades-native-03.json",
      "rankWithinFile": 4,
      "host": "codex",
      "caseId": "new-requirement",
      "status": "pass",
      "grade": {
        "caseId": "new-requirement",
        "host": "codex",
        "status": "pass",
        "execution": "direct",
        "actualReadEventIds": [
          "item_7",
          "item_19"
        ],
        "rawTrace": "codex/batch-03.events.jsonl",
        "responseArtifact": "fixtures/batch-03/new-requirement.result.md",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "review": "Inspects actual copied single-tenant dashboard and replaces both APIs with forTenant scoped view, propagated record docs/examples/rationale and executed isolation/CSV checks plus Bun build. Synthetic tenant ownership assignment is explicit; auth/storage boundaries remain outside supplied local source. Reports actual ordering without invented intermediate green revisions.",
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
        "fullExpected": "Read all affected files, compare the design with a fresh design that assumes tenant ownership, redesign the affected structure instead of stacking a workaround, propagate the change through types, docs, examples and rationale, and deliver the whole redesign incrementally. Report only observed edits and checks.",
        "reducedExpected": "With source available but writes or execution unavailable, provide a concrete redesign and incremental sequence as reduced capability. Identify unperformed edits and checks and preserve authorization boundaries."
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
        "text": "# new-requirement\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"new-requirement\",\n  \"prompt\": \"Add multi-tenant ownership to an existing single-tenant design. Read the affected files, redesign the structure as if tenant ownership had been present from day one, and deliver coherent increments within authorized scope.\",\n  \"requirements\": [\n    \"Available affected source and current design\",\n    \"Authorized scope and available read capability\",\n    \"Write and execution capabilities for implementation and checks\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-redesign-from-first-principles/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 5. See [source-reads.json](new-requirement/source-reads.json). Supplied input archive: [supplied-input.json](new-requirement/supplied-input.json).\n\n## Actual response and variants\n\nImplemented a tenant-owned local adaptation of the supplied orders dashboard. The affected prepared files are input/dashboard.mjs and input/orders.json. Original visible filters by status alone and original exportCsv exports every order. There is no tenant field, auth context, persistence layer, declared type file or other supplied caller.\n\nThe chosen record shape is {tenantId, id, status, customer, total}; order identity is tenantId plus id. A fresh design establishes scope once through forTenant(orders, tenantId). The returned visible and exportCsv methods share only that tenant's records. This replaces both unscoped entry points together instead of adding optional tenant checks to individual callers. No legacy API adapter remains.\n\nTwo local delivery increments are present: dashboard.mjs replaces the API as a coherent unit; README.md and check.mjs supply the record contract, example and verification. This is one completed implementation unit with its documentation/check increment, not a claim of separately executed intermediate green revisions. Original source was inspected before editing. The original runtime observation was captured after writing the isolated replacement but imports only the untouched input copy. The receipts preserve that actual order.\n\n| Alternative | Benefit | Failure mode / cost |\n| --- | --- | --- |\n| Tenant parameter on every existing operation | Small signature changes | Every new operation must remember its filter. Unscoped export remains easy to copy. |\n| Selected tenant-scoped view | One scope decision applies to both operations; global exports disappear | Caller must obtain tenant identity from trusted auth context; in-memory views do not enforce database access. |\n\nNo actual ownership mapping was supplied. The test explicitly assigns synthetic tenants a and b and creates an overlapping ID to check isolation. Missing ownership is excluded, never silently assigned to a default tenant. Empty or missing tenant scope throws. Unknown tenant scope returns no orders.\n\nChecks actually executed: check.mjs, exit 0; Bun build of dashboard.mjs, exit 0. Runtime assertions cover status filtering, tenant-limited export, identical IDs across tenants, unowned records, missing scope, unknown tenant and exact CSV output with commas and quotes. The CSV quoting is a disclosed adjacent correction needed for valid export of the supplied data. Raw output is in runtime-check.command.json, static-check.command.json and original-observation.command.json.\n\nVariant attempted: available source/write/execution, using copied synthetic fixtures. No denied-capability variant was requested. The real-service design remains incomplete because auth, storage, query boundaries and an ownership mapping were not supplied. README.md records those boundaries and mutable-input constraints. No live database was migrated and no production isolation outcome is claimed.\n\n## Real command results\n\n```\n[\n  {\n    \"artifact\": \"new-requirement/original-observation.command.json\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"-e\",\n      \"const {visible,exportCsv}=await import('./new-requirement/input/dashboard.mjs');const a=await Bun.file('new-requirement/input/orders.json').json();console.log(JSON.stringify({visibleIds:visible(a,'open').map(x=>x.id),csv:exportCsv(a),scope:'Original API has no tenant parameter. Fixture source only, no live data.'}));\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"visibleIds\\\":[1,3],\\\"csv\\\":\\\"id,customer,total\\\\n1,Ada, Inc.,12.5\\\\n2,Hidden,4\\\\n3,Say \\\\\\\"Hi\\\\\\\",0\\\",\\\"scope\\\":\\\"Original API has no tenant parameter. Fixture source only, no live data.\\\"}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"artifact\": \"new-requirement/runtime-check.command.json\",\n    \"label\": \"runtime-check\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"new-requirement/check.mjs\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"Tenant scope checks passed: status, export, duplicate ids across tenants, unowned records, missing scope, unknown tenant, CSV escaping.\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"new-requirement/static-check.command.json\",\n    \"label\": \"static-check\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"build\",\n      \"new-requirement/dashboard.mjs\",\n      \"--target=bun\",\n      \"--outdir=new-requirement/build\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"Bundled 1 module in 7ms\\n\\n  dashboard.js  0.69 KB  (entry point)\\n\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  }\n]\n```\n\n## Artifacts\n\n- [new-requirement/README.md](new-requirement/README.md)\n- [new-requirement/build/dashboard.js](new-requirement/build/dashboard.js)\n- [new-requirement/check.mjs](new-requirement/check.mjs)\n- [new-requirement/dashboard.mjs](new-requirement/dashboard.mjs)\n- [new-requirement/input/dashboard.mjs](new-requirement/input/dashboard.mjs)\n- [new-requirement/input/orders.json](new-requirement/input/orders.json)\n- [new-requirement/original-observation.command.json](new-requirement/original-observation.command.json)\n- [new-requirement/response.md](new-requirement/response.md)\n- [new-requirement/runtime-check.command.json](new-requirement/runtime-check.command.json)\n- [new-requirement/source-reads.json](new-requirement/source-reads.json)\n- [new-requirement/static-check.command.json](new-requirement/static-check.command.json)\n- [new-requirement/supplied-input.json](new-requirement/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n",
        "artifact": {
          "path": "fixtures/batch-03/new-requirement.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement.result.md",
          "sha256": "f0cbc1a903c229925827cbd0041ddb7da8e748f0e052e059b66be83f9ec33cb5",
          "bytes": 7847
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
      "path": "fixtures/batch-03/new-requirement/README.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement/README.md",
      "sha256": "acebc163736a8a77f16d21c00d876f988b5aea66648344142148881258cc3a57",
      "bytes": 1694,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "# Tenant-owned orders\n\nThis is an isolated synthetic adaptation of the supplied dashboard module.\nThe record shape is `{tenantId, id, status, customer, total}`. Identity is the pair of tenantId and id.\nThe caller supplies a trusted tenant identity to `forTenant(orders, tenantId)` once.\nBoth returned operations use that tenant's records. There is no global export operation.\nMissing tenant identity throws. Records without ownership do not appear in any view.\n\n```js\nimport { forTenant } from './dashboard.mjs';\nconst orders = [{tenantId:'a', id:1, status:'open', customer:'Example', total:12.5}];\nconst view = forTenant(orders, 'a');\nview.visible('open');\nview.exportCsv();\n```\n\nThe input fixture supplies no ownership mapping. The check assigns tenants solely to exercise isolation. It does not backfill any real data or establish anyone's actual ownership.\nThe CSV writer quotes fields to preserve the supplied commas and quotes. This is a small adjacent behavior change recorded explicitly.\n\nFor a database-backed service, tenant scope must come from authenticated server context and constrain queries and composite keys. An in-memory closure is not authentication, persistence isolation, row security or an authorization system. Callers must not mutate the supplied records after constructing a view. None of those service prerequisites are supplied here.\n\nThe delivered increment replaces both public operations together. The next increment supplies examples and executable checks. No compatibility adapter for unscoped exports remains. There are no other supplied callers or type declarations in this fixture.\n\nRun `bun --no-install new-requirement/check.mjs` from the evaluation root.\n"
    },
    {
      "path": "fixtures/batch-03/new-requirement/build/dashboard.js",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement/build/dashboard.js",
      "sha256": "7bc60694de3335c80a4b503f77c138f5b8f7f3f4144beea31ffdf06fa3593069",
      "bytes": 693,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "// @bun\n// new-requirement/dashboard.mjs\nfunction tenantOrders(orders, tenantId) {\n  if (typeof tenantId !== \"string\" || !tenantId.trim())\n    throw new Error(\"tenant required\");\n  return orders.filter((order) => order.tenantId === tenantId);\n}\nfunction forTenant(orders, tenantId) {\n  const owned = tenantOrders(orders, tenantId);\n  return {\n    visible(status) {\n      return owned.filter((order) => order.status === status);\n    },\n    exportCsv() {\n      const cell = (value) => `\"${String(value).replaceAll('\"', '\"\"')}\"`;\n      return `id,customer,total\n` + owned.map((order) => [order.id, order.customer, order.total].map(cell).join(\",\")).join(`\n`);\n    }\n  };\n}\nexport {\n  forTenant\n};\n"
    },
    {
      "path": "fixtures/batch-03/new-requirement/check.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement/check.mjs",
      "sha256": "52d21cc83460e7a2fe5dfe2e95bde31287361e799dcd45be200d7431a2496d20",
      "bytes": 1199,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "import assert from 'node:assert/strict';\nimport { forTenant } from './dashboard.mjs';\nconst original = await Bun.file(new URL('./input/orders.json',import.meta.url)).json();\nconst orders = original.map((order,index) => ({...order,tenantId:index === 1?'b':'a'}));\norders.push({id:1,tenantId:'b',status:'open',customer:'Other tenant',total:99});\norders.push({id:99,status:'open',customer:'Unowned',total:1});\nconst a = forTenant(orders,'a');\nassert.deepEqual(a.visible('open').map(order=>order.id),[1,3]);\nassert.deepEqual(forTenant(orders,'b').visible('open').map(order=>order.customer),['Other tenant']);\nassert.equal(a.exportCsv(),'id,customer,total\\n\"1\",\"Ada, Inc.\",\"12.5\"\\n\"3\",\"Say \"\"Hi\"\"\",\"0\"');\nassert.ok(!a.exportCsv().includes('Hidden'));\nassert.ok(!a.exportCsv().includes('Other tenant'));\nassert.ok(!a.exportCsv().includes('Unowned'));\nassert.throws(()=>forTenant(orders,''),/tenant required/);\nassert.throws(()=>forTenant(orders,undefined),/tenant required/);\nassert.equal(forTenant(orders,'unknown').exportCsv(),'id,customer,total\\n');\nconsole.log('Tenant scope checks passed: status, export, duplicate ids across tenants, unowned records, missing scope, unknown tenant, CSV escaping.');\n"
    },
    {
      "path": "fixtures/batch-03/new-requirement/dashboard.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement/dashboard.mjs",
      "sha256": "407e4f54f7f709ae9e60a53378ecb95648744598a29f8b62a58caa9e58f4956c",
      "bytes": 616,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "function tenantOrders(orders, tenantId) {\n  if (typeof tenantId !== 'string' || !tenantId.trim()) throw new Error('tenant required');\n  return orders.filter(order => order.tenantId === tenantId);\n}\n\nexport function forTenant(orders, tenantId) {\n  const owned = tenantOrders(orders, tenantId);\n  return {\n    visible(status) { return owned.filter(order => order.status === status); },\n    exportCsv() {\n      const cell = value => `\"${String(value).replaceAll('\"', '\"\"')}\"`;\n      return 'id,customer,total\\n' + owned.map(order => [order.id, order.customer, order.total].map(cell).join(',')).join('\\n');\n    }\n  };\n}\n"
    },
    {
      "path": "fixtures/batch-03/new-requirement/original-observation.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement/original-observation.command.json",
      "sha256": "050f9b642f734b17d64bac67c168169322e4b2bbbf5546465dd434ce2e336cbf",
      "bytes": 632,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "{\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"const {visible,exportCsv}=await import('./new-requirement/input/dashboard.mjs');const a=await Bun.file('new-requirement/input/orders.json').json();console.log(JSON.stringify({visibleIds:visible(a,'open').map(x=>x.id),csv:exportCsv(a),scope:'Original API has no tenant parameter. Fixture source only, no live data.'}));\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"visibleIds\\\":[1,3],\\\"csv\\\":\\\"id,customer,total\\\\n1,Ada, Inc.,12.5\\\\n2,Hidden,4\\\\n3,Say \\\\\\\"Hi\\\\\\\",0\\\",\\\"scope\\\":\\\"Original API has no tenant parameter. Fixture source only, no live data.\\\"}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-03/new-requirement/response.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement/response.md",
      "sha256": "99e5f59abbc0e4c4da817eb8e2b7a2cc5a1872201aafabdc13af4ecb82754778",
      "bytes": 2907,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "Implemented a tenant-owned local adaptation of the supplied orders dashboard. The affected prepared files are input/dashboard.mjs and input/orders.json. Original visible filters by status alone and original exportCsv exports every order. There is no tenant field, auth context, persistence layer, declared type file or other supplied caller.\n\nThe chosen record shape is {tenantId, id, status, customer, total}; order identity is tenantId plus id. A fresh design establishes scope once through forTenant(orders, tenantId). The returned visible and exportCsv methods share only that tenant's records. This replaces both unscoped entry points together instead of adding optional tenant checks to individual callers. No legacy API adapter remains.\n\nTwo local delivery increments are present: dashboard.mjs replaces the API as a coherent unit; README.md and check.mjs supply the record contract, example and verification. This is one completed implementation unit with its documentation/check increment, not a claim of separately executed intermediate green revisions. Original source was inspected before editing. The original runtime observation was captured after writing the isolated replacement but imports only the untouched input copy. The receipts preserve that actual order.\n\n| Alternative | Benefit | Failure mode / cost |\n| --- | --- | --- |\n| Tenant parameter on every existing operation | Small signature changes | Every new operation must remember its filter. Unscoped export remains easy to copy. |\n| Selected tenant-scoped view | One scope decision applies to both operations; global exports disappear | Caller must obtain tenant identity from trusted auth context; in-memory views do not enforce database access. |\n\nNo actual ownership mapping was supplied. The test explicitly assigns synthetic tenants a and b and creates an overlapping ID to check isolation. Missing ownership is excluded, never silently assigned to a default tenant. Empty or missing tenant scope throws. Unknown tenant scope returns no orders.\n\nChecks actually executed: check.mjs, exit 0; Bun build of dashboard.mjs, exit 0. Runtime assertions cover status filtering, tenant-limited export, identical IDs across tenants, unowned records, missing scope, unknown tenant and exact CSV output with commas and quotes. The CSV quoting is a disclosed adjacent correction needed for valid export of the supplied data. Raw output is in runtime-check.command.json, static-check.command.json and original-observation.command.json.\n\nVariant attempted: available source/write/execution, using copied synthetic fixtures. No denied-capability variant was requested. The real-service design remains incomplete because auth, storage, query boundaries and an ownership mapping were not supplied. README.md records those boundaries and mutable-input constraints. No live database was migrated and no production isolation outcome is claimed.\n"
    },
    {
      "path": "fixtures/batch-03/new-requirement/runtime-check.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement/runtime-check.command.json",
      "sha256": "fa306e49d72c1aea505fa0025cf5d9c2086252a66c10eee11e1bfa15c6feb2b3",
      "bytes": 325,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "{\n  \"label\": \"runtime-check\",\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"new-requirement/check.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"Tenant scope checks passed: status, export, duplicate ids across tenants, unowned records, missing scope, unknown tenant, CSV escaping.\\n\",\n  \"stderr\": \"\",\n  \"expectedExitCode\": 0\n}\n"
    },
    {
      "path": "fixtures/batch-03/new-requirement/static-check.command.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement/static-check.command.json",
      "sha256": "426f70fe229fbdcd9f94757b2efa2ec483b0b1ce54ef63925924589f17f8479f",
      "bytes": 331,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "{\n  \"label\": \"static-check\",\n  \"command\": [\n    \"bun\",\n    \"--no-install\",\n    \"build\",\n    \"new-requirement/dashboard.mjs\",\n    \"--target=bun\",\n    \"--outdir=new-requirement/build\"\n  ],\n  \"exitCode\": 0,\n  \"stdout\": \"Bundled 1 module in 7ms\\n\\n  dashboard.js  0.69 KB  (entry point)\\n\\n\",\n  \"stderr\": \"\",\n  \"expectedExitCode\": 0\n}\n"
    },
    {
      "path": "fixtures/batch-03/new-requirement/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement/supplied-input.json",
      "sha256": "f6e5cd631ed4e198f0913a4cf5a56f7f0186f416d6c1739983c98a4d0b0e9a61",
      "bytes": 1854,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "{\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"id\": \"new-requirement\",\n  \"sourcePaths\": [\n    \"skills/principle-redesign-from-first-principles/SKILL.md\"\n  ],\n  \"prompt\": \"Add multi-tenant ownership to an existing single-tenant design. Read the affected files, redesign the structure as if tenant ownership had been present from day one, and deliver coherent increments within authorized scope.\",\n  \"requirements\": [\n    \"Available affected source and current design\",\n    \"Authorized scope and available read capability\",\n    \"Write and execution capabilities for implementation and checks\"\n  ],\n  \"expectedFull\": \"Read all affected files, compare the design with a fresh design that assumes tenant ownership, redesign the affected structure instead of stacking a workaround, propagate the change through types, docs, examples and rationale, and deliver the whole redesign incrementally. Report only observed edits and checks.\",\n  \"expectedReduced\": \"With source available but writes or execution unavailable, provide a concrete redesign and incremental sequence as reduced capability. Identify unperformed edits and checks and preserve authorization boundaries.\",\n  \"expectedBlocked\": \"If affected source or required design context is unavailable, identify the missing inputs and keep any redesign provisional. Do not claim the current design was inspected or changed.\",\n  \"forbiddenClaims\": [\n    \"A workaround stacked onto existing structure satisfies the redesign\",\n    \"Implementation or checks occurred without observed authorized operations\",\n    \"Source review or structural checks prove host behavioral parity\",\n    \"Unavailable source was inspected\",\n    \"The principle grants broader write or external permissions\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-03/new-requirement.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-03/new-requirement.result.md",
      "sha256": "f0cbc1a903c229925827cbd0041ddb7da8e748f0e052e059b66be83f9ec33cb5",
      "bytes": 7847,
      "owners": [
        "grades-native-03.json#4"
      ],
      "text": "# new-requirement\n\n## Supplied input\n\n```\n{\n  \"caseId\": \"new-requirement\",\n  \"prompt\": \"Add multi-tenant ownership to an existing single-tenant design. Read the affected files, redesign the structure as if tenant ownership had been present from day one, and deliver coherent increments within authorized scope.\",\n  \"requirements\": [\n    \"Available affected source and current design\",\n    \"Authorized scope and available read capability\",\n    \"Write and execution capabilities for implementation and checks\"\n  ],\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-redesign-from-first-principles/SKILL.md\"\n  ]\n}\n```\n\n## Source and host evidence\n\nPackage used exclusively: /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Supplied source freeze: f4623636a287bea2aa79c4b2234a53d20a5f193c. The installation has no .git directory; the freeze is supplied provenance, not an independently verified commit. Per-file SHA-256 digests and complete source snapshots are retained in each case's source-reads.json and source/ directory. No 0.2.1 files were read. No personal history or live service was used.\n\nActual tools were functions.exec with tools.exec_command and tools.apply_patch. Scripts used Bun 1.4.2, with --no-install for saved scripts. File reads, scoped writes, execution and readback succeeded. Native worker startup failed as recorded below. External writes, commits, pushes, installs, configuration changes, publishing and schedules were forbidden and unperformed. disable-model-invocation metadata was read, not proven host-enforced. No grades are assigned.\n\nThe original user prompt and requirements appear below. Registry expected-outcome text is preserved in supplied-input.json as test input, not a test result.\n\nComplete source reads captured: 5. See [source-reads.json](new-requirement/source-reads.json). Supplied input archive: [supplied-input.json](new-requirement/supplied-input.json).\n\n## Actual response and variants\n\nImplemented a tenant-owned local adaptation of the supplied orders dashboard. The affected prepared files are input/dashboard.mjs and input/orders.json. Original visible filters by status alone and original exportCsv exports every order. There is no tenant field, auth context, persistence layer, declared type file or other supplied caller.\n\nThe chosen record shape is {tenantId, id, status, customer, total}; order identity is tenantId plus id. A fresh design establishes scope once through forTenant(orders, tenantId). The returned visible and exportCsv methods share only that tenant's records. This replaces both unscoped entry points together instead of adding optional tenant checks to individual callers. No legacy API adapter remains.\n\nTwo local delivery increments are present: dashboard.mjs replaces the API as a coherent unit; README.md and check.mjs supply the record contract, example and verification. This is one completed implementation unit with its documentation/check increment, not a claim of separately executed intermediate green revisions. Original source was inspected before editing. The original runtime observation was captured after writing the isolated replacement but imports only the untouched input copy. The receipts preserve that actual order.\n\n| Alternative | Benefit | Failure mode / cost |\n| --- | --- | --- |\n| Tenant parameter on every existing operation | Small signature changes | Every new operation must remember its filter. Unscoped export remains easy to copy. |\n| Selected tenant-scoped view | One scope decision applies to both operations; global exports disappear | Caller must obtain tenant identity from trusted auth context; in-memory views do not enforce database access. |\n\nNo actual ownership mapping was supplied. The test explicitly assigns synthetic tenants a and b and creates an overlapping ID to check isolation. Missing ownership is excluded, never silently assigned to a default tenant. Empty or missing tenant scope throws. Unknown tenant scope returns no orders.\n\nChecks actually executed: check.mjs, exit 0; Bun build of dashboard.mjs, exit 0. Runtime assertions cover status filtering, tenant-limited export, identical IDs across tenants, unowned records, missing scope, unknown tenant and exact CSV output with commas and quotes. The CSV quoting is a disclosed adjacent correction needed for valid export of the supplied data. Raw output is in runtime-check.command.json, static-check.command.json and original-observation.command.json.\n\nVariant attempted: available source/write/execution, using copied synthetic fixtures. No denied-capability variant was requested. The real-service design remains incomplete because auth, storage, query boundaries and an ownership mapping were not supplied. README.md records those boundaries and mutable-input constraints. No live database was migrated and no production isolation outcome is claimed.\n\n## Real command results\n\n```\n[\n  {\n    \"artifact\": \"new-requirement/original-observation.command.json\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"-e\",\n      \"const {visible,exportCsv}=await import('./new-requirement/input/dashboard.mjs');const a=await Bun.file('new-requirement/input/orders.json').json();console.log(JSON.stringify({visibleIds:visible(a,'open').map(x=>x.id),csv:exportCsv(a),scope:'Original API has no tenant parameter. Fixture source only, no live data.'}));\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"visibleIds\\\":[1,3],\\\"csv\\\":\\\"id,customer,total\\\\n1,Ada, Inc.,12.5\\\\n2,Hidden,4\\\\n3,Say \\\\\\\"Hi\\\\\\\",0\\\",\\\"scope\\\":\\\"Original API has no tenant parameter. Fixture source only, no live data.\\\"}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"artifact\": \"new-requirement/runtime-check.command.json\",\n    \"label\": \"runtime-check\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"new-requirement/check.mjs\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"Tenant scope checks passed: status, export, duplicate ids across tenants, unowned records, missing scope, unknown tenant, CSV escaping.\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  },\n  {\n    \"artifact\": \"new-requirement/static-check.command.json\",\n    \"label\": \"static-check\",\n    \"command\": [\n      \"bun\",\n      \"--no-install\",\n      \"build\",\n      \"new-requirement/dashboard.mjs\",\n      \"--target=bun\",\n      \"--outdir=new-requirement/build\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"Bundled 1 module in 7ms\\n\\n  dashboard.js  0.69 KB  (entry point)\\n\\n\",\n    \"stderr\": \"\",\n    \"expectedExitCode\": 0\n  }\n]\n```\n\n## Artifacts\n\n- [new-requirement/README.md](new-requirement/README.md)\n- [new-requirement/build/dashboard.js](new-requirement/build/dashboard.js)\n- [new-requirement/check.mjs](new-requirement/check.mjs)\n- [new-requirement/dashboard.mjs](new-requirement/dashboard.mjs)\n- [new-requirement/input/dashboard.mjs](new-requirement/input/dashboard.mjs)\n- [new-requirement/input/orders.json](new-requirement/input/orders.json)\n- [new-requirement/original-observation.command.json](new-requirement/original-observation.command.json)\n- [new-requirement/response.md](new-requirement/response.md)\n- [new-requirement/runtime-check.command.json](new-requirement/runtime-check.command.json)\n- [new-requirement/source-reads.json](new-requirement/source-reads.json)\n- [new-requirement/static-check.command.json](new-requirement/static-check.command.json)\n- [new-requirement/supplied-input.json](new-requirement/supplied-input.json)\n\nPackage sources and original shared fixtures remain untouched. All edits are in the evaluation root. Report persistence and fixture/source integrity are checked by verify.mjs.\n\nObserved artifact verification: [verification.json](verification.json) and [verification.command.json](verification.command.json). Exit 0 verifies recorded bytes and report completeness only, not case grades.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-03/new-requirement/input",
      "owner": "grades-native-03.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/new-requirement/source",
      "owner": "grades-native-03.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/new-requirement/source-reads.json",
      "owner": "grades-native-03.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-03/new-requirement/input",
      "owner": "grades-native-03.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/new-requirement/source",
      "owner": "grades-native-03.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-03/new-requirement/source-reads.json",
      "owner": "grades-native-03.json#4",
      "reason": "copied source/input or administrative evaluator helper"
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
