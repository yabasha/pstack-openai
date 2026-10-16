# codex: replay

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "replay",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-04.json#2",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "An interrupted job may already have sent a payment request. Design recovery for a retry, including partial local state, stale locks and a destination whose prior outcome is unknown.",
  "caseDefinition": {
    "id": "replay",
    "sourcePaths": [
      "skills/principle-make-operations-idempotent/SKILL.md"
    ],
    "prompt": "An interrupted job may already have sent a payment request. Design recovery for a retry, including partial local state, stale locks and a destination whose prior outcome is unknown.",
    "requirements": [
      "Inspect the stable prior action identity and destination outcome before recovery.",
      "Preserve explicit authorization and observed capabilities for external writes.",
      "Exercise repeated runs and crashes at each possible point; reconcile partial state."
    ],
    "expectedFull": "The retry converges to the same end state through reconciliation and a destination-appropriate idempotency mechanism. It adopts live sessions, removes stale artifacts by content equivalence, detects stale PID locks and regenerates fresh scheduling input. Completed external actions are recognized without blind replay; unknown outcomes block replay.",
    "expectedReduced": "Without destination inspection or authorized execution, provide a reduced recovery design and state which checks and actions were not performed. Unknown prior outcomes still block external replay.",
    "expectedBlocked": "If action identity, destination outcome or external permission cannot be established, block replay and identify the missing requirement.",
    "forbiddenClaims": [
      "Blind external replay is safe because the local operation is idempotent.",
      "Unknown action outcomes count as completion.",
      "A proposed reconciliation design proves host execution or unattended recovery."
    ],
    "caseFile": "docs/parity/cases/skills/principle-make-operations-idempotent.json"
  },
  "registry": {
    "caseId": "replay",
    "caseFile": "docs/parity/cases/skills/principle-make-operations-idempotent.json",
    "sourcePaths": [
      "skills/principle-make-operations-idempotent/SKILL.md"
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
      "attemptId": "grades-native-04.json#2",
      "order": 0,
      "gradeFile": "grades-native-04.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "replay",
      "status": "reduced-pass",
      "grade": {
        "caseId": "replay",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-04.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_16"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Real payment identity/destination/authorization and destination-specific recovery unobserved."
        ],
        "review": "Useful identity-bound reconcile-before-retry design, unknown outcomes block replay. Real child exits/reruns exercise11 local interruption points but local files are a synthetic destination/idempotency proxy only. No payment/service result credited.",
        "responseArtifact": "fixtures/batch-04/replay.result.md",
        "variantReview": [
          "Actual attempted variants and explicitly simulated conditions inspected in response artifact. No synthetic service/worker receipt credited."
        ],
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-04.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ],
        "fullExpected": "The retry converges to the same end state through reconciliation and a destination-appropriate idempotency mechanism. It adopts live sessions, removes stale artifacts by content equivalence, detects stale PID locks and regenerates fresh scheduling input. Completed external actions are recognized without blind replay; unknown outcomes block replay.",
        "reducedExpected": "Without destination inspection or authorized execution, provide a reduced recovery design and state which checks and actions were not performed. Unknown prior outcomes still block external replay."
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
        "text": "# replay\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"replay\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-make-operations-idempotent/SKILL.md\"\n  ],\n  \"prompt\": \"An interrupted job may already have sent a payment request. Design recovery for a retry, including partial local state, stale locks and a destination whose prior outcome is unknown.\",\n  \"requirements\": [\n    \"Inspect the stable prior action identity and destination outcome before recovery.\",\n    \"Preserve explicit authorization and observed capabilities for external writes.\",\n    \"Exercise repeated runs and crashes at each possible point; reconcile partial state.\"\n  ]\n}\n```\n\n## Actual response and output\n\nMake Operations Idempotent changed recovery into reconciliation before retry. No real payment action identity, destination, local payment journal, lock record or destination lookup capability was supplied. External writes are forbidden. Actual payment recovery is blocked.\n\nThe recovery contract is to load the original stable action ID, destination, canonical payload hash and explicit permission. Never mint a new ID on retry. Inspect the destination by that identity. A confirmed matching completed request is adopted locally without another send. A confirmed absence permits retry only with separate explicit authorization and a destination-supported atomic idempotency key bound to that payload. A pending or unknown result stays unresolved and blocks resend. Conflicting payloads or identities block recovery. Destination retention and consistency guarantees must be checked before interpreting \"not found\" as absence.\n\nLocal reconciliation inspects partial intent and completion state, including orphan temporary writes. It adopts the destination receipt before marking local completion. Production locks need atomic exclusive acquisition, an owner nonce, host and process-start identity, bounded leases and a reviewed stale-owner takeover policy. PID liveness alone is unsafe across hosts or PID reuse. A lock is not payment deduplication.\n\nI implemented and ran [recover.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs) and [check.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/check.mjs) as an explicitly synthetic local model. Its stable identity is synthetic-payment-1, its destination is local-fixture://payments and its payload hash is a fixed synthetic string. These are agent-authored method inputs, not recovered payment records. The model inspects these records before mutation. All child command outputs are retained in [process-receipts.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/process-receipts.json).\n\nEleven abrupt child-process exits cover before the lock, temporary and final lock writes, temporary and final intent writes, before dispatch, temporary and final destination writes, temporary and final completion writes, and after unlock. Each interrupted run exited 73. Two retries after each exit converged to one local payment entry and a completed journal. Dead child PID locks were inspected and removed. Unknown destination state exited 3 without dispatch. A simulated permission denial exited 4. A live parent PID lock exited 5. Additional identity and partial-state variants are recorded below if present in command receipts.\n\nThe child exits are actual host execution. Destination behavior, idempotency and permission denial are simulated with local files. Host write capability was available, so the negative permission variant is not host enforcement. The model is sequential and does not prove atomic concurrent lock takeover, remote idempotency, power-loss durability, fsync behavior, network timeout recovery or every possible OS instruction-level crash. No service was contacted and no payment was sent.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/.\n\n\nCommand: `bun --no-install check.mjs`. Exit 0. Full receipt: [checks.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/checks.receipt.json).\n\n```text\nProcess interruption and two retries converged: before-lock\nProcess interruption and two retries converged: after-temp-lock\nProcess interruption and two retries converged: after-lock\nProcess interruption and two retries converged: after-temp-intent\nProcess interruption and two retries converged: after-intent\nProcess interruption and two retries converged: before-dispatch\nProcess interruption and two retries converged: after-temp-destination\nProcess interruption and two retries converged: after-destination\nProcess interruption and two retries converged: after-temp-done\nProcess interruption and two retries converged: after-local-done\nProcess interruption and two retries converged: after-unlock\nUnknown outcome blocked without a local dispatch.\nSimulated denied local permission blocked. Host writes remain available.\nLive parent PID lock blocked.\nOnly local files were used. No payment service contacted.\n```\n\n\n## Variants and limits\n\nEleven process-exit variants each ran twice afterward. Unknown outcome, simulated denied permission and live lock variants ran. Real prior action and destination inspection were impossible without inputs and are not replaced by the model. See process-receipts.json for every child exit and output.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n",
        "artifact": {
          "path": "fixtures/batch-04/replay.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay.result.md",
          "sha256": "1f616e9aa6faa9b6f727733f58c47409e4840b20e1856940f3b5569e8e6ce3d9",
          "bytes": 7088
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-04.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-04.events.jsonl",
            "sha256": "614c212bfe1cb1201ad58cdd814f4bcd05080cd9c2ba5fc9f09a7127c3730143",
            "bytes": 382761,
            "eventReferences": [
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2a159b40b8943f8e35e80aeb982c727f5235c07b8f9f62bafd5c1b084f05c0ea"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "860d291d8f06560ed8b5603aad27548aaaa20dfd9f90ee7b725cf03b178f1526",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_16",
                "line": 30,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "1eef65cc2c879da4e6f58cce88164b97f432a970d5ad5291c6cbb50fc6f1ded7"
              },
              {
                "eventId": "item_16",
                "line": 31,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "f0a5241569d17e12c3ea3d7ccc008ecf878ea914c8abd9f209fe3370fade3b1a",
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
            "item_16"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-04.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-04/replay/check.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/check.mjs",
      "sha256": "946885179753907e2b91ffce21ac59d7def642778a6d43064990e9e14713d25d",
      "bytes": 2390,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "import { mkdir, rm } from 'node:fs/promises';\nimport assert from 'node:assert/strict';\nconst base=import.meta.dir+'/runs';await rm(base,{recursive:true,force:true});await mkdir(base,{recursive:true});\nconst receipts=[];\nasync function seed(name,knowledge='known',authorized=true){const dir=base+'/'+name;await mkdir(dir);await Bun.write(dir+'/action.json',JSON.stringify({id:'synthetic-payment-1',destination:'local-fixture://payments',payloadHash:'synthetic-fixed-payload',localSimulationAuthorized:authorized,externalWriteAuthorized:false}));await Bun.write(dir+'/destination.json',JSON.stringify({knowledge,payments:[]}));return dir}\nfunction run(dir,cut){const argv=['bun','--no-install',import.meta.dir+'/recover.mjs',dir,...(cut?[cut]:[])];const p=Bun.spawnSync(argv);const receipt={argv,exitCode:p.exitCode,stdout:p.stdout.toString(),stderr:p.stderr.toString()};receipts.push(receipt);return receipt}\nfor(const cut of ['before-lock','after-temp-lock','after-lock','after-temp-intent','after-intent','before-dispatch','after-temp-destination','after-destination','after-temp-done','after-local-done','after-unlock']){\n const dir=await seed(cut);assert.equal(run(dir,cut).exitCode,73);assert.equal(run(dir).exitCode,0);assert.equal(run(dir).exitCode,0);\n assert.equal((await Bun.file(dir+'/destination.json').json()).payments.length,1);assert.equal((await Bun.file(dir+'/local.json').json()).state,'done');\n console.log('Process interruption and two retries converged: '+cut);\n}\nconst unknown=await seed('unknown','unknown');const bytes=await Bun.file(unknown+'/destination.json').text();assert.equal(run(unknown).exitCode,3);assert.equal(await Bun.file(unknown+'/destination.json').text(),bytes);assert.equal(await Bun.file(unknown+'/local.json').exists(),false);console.log('Unknown outcome blocked without a local dispatch.');\nconst denied=await seed('no-permission','known',false);assert.equal(run(denied).exitCode,4);console.log('Simulated denied local permission blocked. Host writes remain available.');\nconst live=await seed('live-lock');await Bun.write(live+'/lock.json',JSON.stringify({pid:process.pid,host:'local-model'}));assert.equal(run(live).exitCode,5);console.log('Live parent PID lock blocked.');\nawait Bun.write(import.meta.dir+'/process-receipts.json',JSON.stringify(receipts,null,2)+'\\n');\nconsole.log('Only local files were used. No payment service contacted.');\n"
    },
    {
      "path": "fixtures/batch-04/replay/checks.receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/checks.receipt.json",
      "sha256": "c4efb8589676cc5641fb0eef6fb88d9957bf3a11d0040cb1e872246d32fb7f78",
      "bytes": 1208,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\n  \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"check.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay\",\n  \"exitCode\": 0,\n  \"stdout\": \"Process interruption and two retries converged: before-lock\\nProcess interruption and two retries converged: after-temp-lock\\nProcess interruption and two retries converged: after-lock\\nProcess interruption and two retries converged: after-temp-intent\\nProcess interruption and two retries converged: after-intent\\nProcess interruption and two retries converged: before-dispatch\\nProcess interruption and two retries converged: after-temp-destination\\nProcess interruption and two retries converged: after-destination\\nProcess interruption and two retries converged: after-temp-done\\nProcess interruption and two retries converged: after-local-done\\nProcess interruption and two retries converged: after-unlock\\nUnknown outcome blocked without a local dispatch.\\nSimulated denied local permission blocked. Host writes remain available.\\nLive parent PID lock blocked.\\nOnly local files were used. No payment service contacted.\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-04/replay/process-receipts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/process-receipts.json",
      "sha256": "3800b207d599a49c428fa08d98519434a697ddadeb874c7b5d9210cdd7568736",
      "bytes": 29114,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "[\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-lock\",\n      \"before-lock\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT before-lock\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-lock\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-lock\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-lock\",\n      \"after-temp-lock\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT after-temp-lock\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-lock\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-lock\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-lock\",\n      \"after-lock\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT after-lock\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-lock\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nRemoved stale local-model lock after dead PID inspection\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-lock\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-intent\",\n      \"after-temp-intent\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT after-temp-intent\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-intent\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nRemoved stale local-model lock after dead PID inspection\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-intent\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-intent\",\n      \"after-intent\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT after-intent\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-intent\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"intent\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nRemoved stale local-model lock after dead PID inspection\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-intent\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-dispatch\",\n      \"before-dispatch\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT before-dispatch\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-dispatch\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"intent\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nRemoved stale local-model lock after dead PID inspection\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-dispatch\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-destination\",\n      \"after-temp-destination\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT after-temp-destination\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-destination\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"intent\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nRemoved stale local-model lock after dead PID inspection\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-destination\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-destination\",\n      \"after-destination\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT after-destination\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-destination\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"intent\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRemoved stale local-model lock after dead PID inspection\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-destination\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-done\",\n      \"after-temp-done\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT after-temp-done\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-done\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"intent\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRemoved stale local-model lock after dead PID inspection\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-done\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-local-done\",\n      \"after-local-done\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT after-local-done\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-local-done\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRemoved stale local-model lock after dead PID inspection\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-local-done\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-unlock\",\n      \"after-unlock\"\n    ],\n    \"exitCode\": 73,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nINJECTED PROCESS EXIT after-unlock\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-unlock\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-unlock\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"state\\\":\\\"done\\\"},\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\"}]},\\\"synthetic\\\":true}\\nRECONCILED local synthetic model; payment count 1\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/unknown\"\n    ],\n    \"exitCode\": 3,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"unknown\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nBLOCKED unknown destination outcome; no dispatch\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/no-permission\"\n    ],\n    \"exitCode\": 4,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":false,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nBLOCKED no local simulation permission\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"argv\": [\n      \"bun\",\n      \"--no-install\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs\",\n      \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/live-lock\"\n    ],\n    \"exitCode\": 5,\n    \"stdout\": \"{\\\"inspectedAction\\\":{\\\"id\\\":\\\"synthetic-payment-1\\\",\\\"destination\\\":\\\"local-fixture://payments\\\",\\\"payloadHash\\\":\\\"synthetic-fixed-payload\\\",\\\"localSimulationAuthorized\\\":true,\\\"externalWriteAuthorized\\\":false},\\\"inspectedLocal\\\":null,\\\"inspectedDestination\\\":{\\\"knowledge\\\":\\\"known\\\",\\\"payments\\\":[]},\\\"synthetic\\\":true}\\nBLOCKED live owner\\n\",\n    \"stderr\": \"\"\n  }\n]\n"
    },
    {
      "path": "fixtures/batch-04/replay/readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/readback.json",
      "sha256": "dcbfd20864f2fbf704d94c7ef4ba1cf3c8132b28eb3efe615c4eb3e58893e781",
      "bytes": 240,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\n  \"report\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay.result.md\",\n  \"sha256\": \"1f616e9aa6faa9b6f727733f58c47409e4840b20e1856940f3b5569e8e6ce3d9\",\n  \"readbackMatched\": true,\n  \"persisted\": []\n}\n"
    },
    {
      "path": "fixtures/batch-04/replay/recover.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs",
      "sha256": "2e7e33f76445856d2c3818d1f5e4b0acb0b398b7a96bc6f4c1da2427c508d4bc",
      "bytes": 2532,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "import { readFileSync, writeFileSync, renameSync, existsSync, unlinkSync } from 'node:fs';\nimport path from 'node:path';\nconst dir=process.argv[2],crash=process.argv[3];\nif(!dir)throw Error('local model directory required');\nconst file=name=>path.join(dir,name+'.json');\nconst read=name=>existsSync(file(name))?JSON.parse(readFileSync(file(name),'utf8')):null;\nconst save=(name,value,label=name)=>{writeFileSync(file(name)+'.tmp',JSON.stringify(value));cut('after-temp-'+label);renameSync(file(name)+'.tmp',file(name));};\nconst cut=point=>{if(crash===point){console.log('INJECTED PROCESS EXIT '+point);process.exit(73)}};\nconst action=read('action');\nif(!action?.id||!action.destination||!action.payloadHash)throw Error('missing stable identity');\nconst dest=read('destination');\nconsole.log(JSON.stringify({inspectedAction:action,inspectedLocal:read('local'),inspectedDestination:dest,synthetic:true}));\nif(dest?.knowledge==='unknown'){console.log('BLOCKED unknown destination outcome; no dispatch');process.exit(3)}\nif(!action.localSimulationAuthorized){console.log('BLOCKED no local simulation permission');process.exit(4)}\nconst lock=read('lock');\nif(lock){\n if(lock.host!=='local-model'||!Number.isInteger(lock.pid)){console.log('BLOCKED ambiguous lock');process.exit(5)}\n let alive=true;try{process.kill(lock.pid,0)}catch(e){if(e.code==='ESRCH')alive=false;else throw e}\n if(alive){console.log('BLOCKED live owner');process.exit(5)}\n unlinkSync(file('lock'));console.log('Removed stale local-model lock after dead PID inspection');\n}\ncut('before-lock');save('lock',{pid:process.pid,host:'local-model'});cut('after-lock');\nconst prior=read('local');if(prior&&(prior.id!==action.id||prior.payloadHash!==action.payloadHash))throw Error('local identity mismatch');\nsave('local',{id:action.id,payloadHash:action.payloadHash,state:'intent'},'intent');cut('after-intent');\nif(dest?.knowledge!=='known'||!Array.isArray(dest.payments))throw Error('destination inspection incomplete');\nconst existing=dest.payments.find(p=>p.id===action.id);\nif(existing&&existing.payloadHash!==action.payloadHash)throw Error('destination identity mismatch');\ncut('before-dispatch');\nif(!existing){dest.payments.push({id:action.id,payloadHash:action.payloadHash});save('destination',dest)}\ncut('after-destination');\nsave('local',{id:action.id,payloadHash:action.payloadHash,state:'done'},'done');cut('after-local-done');\nunlinkSync(file('lock'));cut('after-unlock');\nconsole.log('RECONCILED local synthetic model; payment count '+dest.payments.length);\n"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-destination/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-destination/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-destination/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-destination/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-destination/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-destination/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-intent/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-intent/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-intent/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-intent/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-intent/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-intent/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-local-done/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-local-done/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-local-done/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-local-done/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-local-done/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-local-done/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-lock/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-lock/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-lock/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-lock/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-lock/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-lock/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-destination/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-destination/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-destination/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-destination/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-destination/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-destination/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-done/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-done/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-done/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-done/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-done/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-done/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-intent/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-intent/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-intent/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-intent/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-intent/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-intent/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-lock/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-lock/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-lock/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-lock/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-temp-lock/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-temp-lock/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-unlock/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-unlock/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-unlock/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-unlock/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/after-unlock/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/after-unlock/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/before-dispatch/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-dispatch/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/before-dispatch/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-dispatch/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/before-dispatch/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-dispatch/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/before-lock/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-lock/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/before-lock/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-lock/destination.json",
      "sha256": "ce44bccaacd8b162a6e0010a59e6a1049323a4f80edb3df35f616641ecd5f349",
      "bytes": 103,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\"}]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/before-lock/local.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/before-lock/local.json",
      "sha256": "6c0fdcdc5e67bdcc95e687df1b13dc52eecf7dd5225975faa14a05dfe1bb45dc",
      "bytes": 83,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"payloadHash\":\"synthetic-fixed-payload\",\"state\":\"done\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/live-lock/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/live-lock/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/live-lock/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/live-lock/destination.json",
      "sha256": "5a4e173d26a0b86058ef70c65c3938a00e540eb345ffa23f1eadf1542f760d44",
      "bytes": 35,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/live-lock/lock.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/live-lock/lock.json",
      "sha256": "91efb061528196ca9f3183c9eb29b9e1bf29d4dd71fe0464c80779ba7aade827",
      "bytes": 34,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"pid\":64022,\"host\":\"local-model\"}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/no-permission/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/no-permission/action.json",
      "sha256": "c11c0fdd3a3a11b2b2cdbe817670889019940ee5c002ed0e31b0065a03685e58",
      "bytes": 175,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":false,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/no-permission/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/no-permission/destination.json",
      "sha256": "5a4e173d26a0b86058ef70c65c3938a00e540eb345ffa23f1eadf1542f760d44",
      "bytes": 35,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"known\",\"payments\":[]}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/unknown/action.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/unknown/action.json",
      "sha256": "66d0128b1360527011bafbcf40a7a89e99bd9ec59d134c88543d8f06f953f05d",
      "bytes": 174,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"id\":\"synthetic-payment-1\",\"destination\":\"local-fixture://payments\",\"payloadHash\":\"synthetic-fixed-payload\",\"localSimulationAuthorized\":true,\"externalWriteAuthorized\":false}"
    },
    {
      "path": "fixtures/batch-04/replay/runs/unknown/destination.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/runs/unknown/destination.json",
      "sha256": "223fcd33892d2a4242ae8a17b79102dec2f185a496e312634e7d91726b2fb161",
      "bytes": 37,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "{\"knowledge\":\"unknown\",\"payments\":[]}"
    },
    {
      "path": "fixtures/batch-04/replay.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay.result.md",
      "sha256": "1f616e9aa6faa9b6f727733f58c47409e4840b20e1856940f3b5569e8e6ce3d9",
      "bytes": 7088,
      "owners": [
        "grades-native-04.json#2"
      ],
      "text": "# replay\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"replay\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-make-operations-idempotent/SKILL.md\"\n  ],\n  \"prompt\": \"An interrupted job may already have sent a payment request. Design recovery for a retry, including partial local state, stale locks and a destination whose prior outcome is unknown.\",\n  \"requirements\": [\n    \"Inspect the stable prior action identity and destination outcome before recovery.\",\n    \"Preserve explicit authorization and observed capabilities for external writes.\",\n    \"Exercise repeated runs and crashes at each possible point; reconcile partial state.\"\n  ]\n}\n```\n\n## Actual response and output\n\nMake Operations Idempotent changed recovery into reconciliation before retry. No real payment action identity, destination, local payment journal, lock record or destination lookup capability was supplied. External writes are forbidden. Actual payment recovery is blocked.\n\nThe recovery contract is to load the original stable action ID, destination, canonical payload hash and explicit permission. Never mint a new ID on retry. Inspect the destination by that identity. A confirmed matching completed request is adopted locally without another send. A confirmed absence permits retry only with separate explicit authorization and a destination-supported atomic idempotency key bound to that payload. A pending or unknown result stays unresolved and blocks resend. Conflicting payloads or identities block recovery. Destination retention and consistency guarantees must be checked before interpreting \"not found\" as absence.\n\nLocal reconciliation inspects partial intent and completion state, including orphan temporary writes. It adopts the destination receipt before marking local completion. Production locks need atomic exclusive acquisition, an owner nonce, host and process-start identity, bounded leases and a reviewed stale-owner takeover policy. PID liveness alone is unsafe across hosts or PID reuse. A lock is not payment deduplication.\n\nI implemented and ran [recover.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/recover.mjs) and [check.mjs](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/check.mjs) as an explicitly synthetic local model. Its stable identity is synthetic-payment-1, its destination is local-fixture://payments and its payload hash is a fixed synthetic string. These are agent-authored method inputs, not recovered payment records. The model inspects these records before mutation. All child command outputs are retained in [process-receipts.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/process-receipts.json).\n\nEleven abrupt child-process exits cover before the lock, temporary and final lock writes, temporary and final intent writes, before dispatch, temporary and final destination writes, temporary and final completion writes, and after unlock. Each interrupted run exited 73. Two retries after each exit converged to one local payment entry and a completed journal. Dead child PID locks were inspected and removed. Unknown destination state exited 3 without dispatch. A simulated permission denial exited 4. A live parent PID lock exited 5. Additional identity and partial-state variants are recorded below if present in command receipts.\n\nThe child exits are actual host execution. Destination behavior, idempotency and permission denial are simulated with local files. Host write capability was available, so the negative permission variant is not host enforcement. The model is sequential and does not prove atomic concurrent lock takeover, remote idempotency, power-loss durability, fsync behavior, network timeout recovery or every possible OS instruction-level crash. No service was contacted and no payment was sent.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/.\n\n\nCommand: `bun --no-install check.mjs`. Exit 0. Full receipt: [checks.receipt.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/replay/checks.receipt.json).\n\n```text\nProcess interruption and two retries converged: before-lock\nProcess interruption and two retries converged: after-temp-lock\nProcess interruption and two retries converged: after-lock\nProcess interruption and two retries converged: after-temp-intent\nProcess interruption and two retries converged: after-intent\nProcess interruption and two retries converged: before-dispatch\nProcess interruption and two retries converged: after-temp-destination\nProcess interruption and two retries converged: after-destination\nProcess interruption and two retries converged: after-temp-done\nProcess interruption and two retries converged: after-local-done\nProcess interruption and two retries converged: after-unlock\nUnknown outcome blocked without a local dispatch.\nSimulated denied local permission blocked. Host writes remain available.\nLive parent PID lock blocked.\nOnly local files were used. No payment service contacted.\n```\n\n\n## Variants and limits\n\nEleven process-exit variants each ran twice afterward. Unknown outcome, simulated denied permission and live lock variants ran. Real prior action and destination inspection were impossible without inputs and are not replaced by the model. See process-receipts.json for every child exit and output.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-04/replay/additional-source-reads.json",
      "owner": "grades-native-04.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/replay/fixture-README.md",
      "owner": "grades-native-04.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/replay/input.json",
      "owner": "grades-native-04.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/replay/source-manifest.json",
      "owner": "grades-native-04.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/replay/additional-source-reads.json",
      "owner": "grades-native-04.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/replay/fixture-README.md",
      "owner": "grades-native-04.json#2",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/replay/input.json",
      "owner": "grades-native-04.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/replay/source-manifest.json",
      "owner": "grades-native-04.json#2",
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
