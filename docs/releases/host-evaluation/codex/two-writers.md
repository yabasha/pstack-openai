# codex: two-writers

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "two-writers",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-05.json#3",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "An indexer and a metrics worker each update their own lastX field in state.json. Prevent concurrent write races and assess whether locking is needed.",
  "caseDefinition": {
    "id": "two-writers",
    "sourcePaths": [
      "skills/principle-separate-before-serializing-shared-state/SKILL.md"
    ],
    "prompt": "An indexer and a metrics worker each update their own lastX field in state.json. Prevent concurrent write races and assess whether locking is needed.",
    "requirements": [
      "Identify the shared mutable target.",
      "Isolate writable output before considering locking.",
      "Merge independent facts only at the read or reporting boundary; serialize structurally only for a real single-object invariant."
    ],
    "expectedFull": "Assign indexer-state.json and metrics-state.json to distinct writers before considering a lock. Explain why separate fields in one state.json still share mutation. If one canonical write target is a real invariant, use lockfiles, sequential phases, a single writer or atomic compare-and-swap. Observe authorized operations before claiming implementation.",
    "expectedReduced": "If concurrent workers or writes are unavailable, provide the isolated-output design and label any authorized sequential fallback reduced capability. State which execution and concurrency checks were not performed.",
    "expectedBlocked": "If required writes or execution are denied or unavailable, block implementation and identify the missing capability or permission. Preserve the isolation-first recommendation.",
    "forbiddenClaims": [
      "Instructions or conventions prevent concurrent write races.",
      "Locking is the default before checking whether sharing is necessary.",
      "Different fields in one state.json are isolated write targets.",
      "A design or sequential fallback proves concurrent worker execution or race prevention."
    ],
    "caseFile": "docs/parity/cases/skills/principle-separate-before-serializing-shared-state.json"
  },
  "registry": {
    "caseId": "two-writers",
    "caseFile": "docs/parity/cases/skills/principle-separate-before-serializing-shared-state.json",
    "sourcePaths": [
      "skills/principle-separate-before-serializing-shared-state/SKILL.md"
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
      "attemptId": "grades-native-05.json#3",
      "order": 0,
      "gradeFile": "grades-native-05.json",
      "rankWithinFile": 3,
      "host": "codex",
      "caseId": "two-writers",
      "status": "pass",
      "grade": {
        "caseId": "two-writers",
        "host": "codex",
        "status": "pass",
        "execution": "direct",
        "rawTrace": "codex/batch-05.events.jsonl",
        "actualReadEventIds": [
          "item_5",
          "item_9",
          "item_21"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "review": "Correctly splits whole shared state file into distinct role-owned files and combines only at read boundary. Real overlapping Bun child processes each perform100 writes, output retains100/100. Deterministic original lost-update interleaving is not misrepresented as actual concurrent race. These are appropriate OS workers for this case, not claimed AI agents. Single-object and multiple-instance limitations explicit.",
        "responseArtifact": "fixtures/batch-05/two-writers.result.md",
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
        "fullExpected": "Assign indexer-state.json and metrics-state.json to distinct writers before considering a lock. Explain why separate fields in one state.json still share mutation. If one canonical write target is a real invariant, use lockfiles, sequential phases, a single writer or atomic compare-and-swap. Observe authorized operations before claiming implementation.",
        "reducedExpected": "If concurrent workers or writes are unavailable, provide the isolated-output design and label any authorized sequential fallback reduced capability. State which execution and concurrency checks were not performed."
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
        "text": "# two-writers\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"two-writers\",\n  \"prompt\": \"An indexer and a metrics worker each update their own lastX field in state.json. Prevent concurrent write races and assess whether locking is needed.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Identify the shared mutable target.\",\n    \"Isolate writable output before considering locking.\",\n    \"Merge independent facts only at the read or reporting boundary; serialize structurally only for a real single-object invariant.\"\n  ]\n}\n```\n\n## Actual response and output\n\nThe shared mutable target is the whole state.json document. Separate lastX fields still collide because each read-modify-write can replace the other writer's update. Separate Before Serializing Shared State changes the design to indexer-state.json owned by the indexer and metrics-state.json owned by metrics. Only report.mjs combines the independent facts on read. No shared aggregate file is written.\n\nThere is no original indexer or metrics implementation in the prepared inputs. I authored an explicitly synthetic local implementation from the supplied scenario and executed it. The probe first demonstrated the lost update with a scripted read/read/write/write interleaving, yielding lastIndex=0 and lastMetrics=1. That part is a deterministic interleaving, not an observed simultaneous race. It then launched two actual Bun child processes with distinct owned targets. Each completed 100 snapshot writes. The read boundary returned lastIndex=100 and lastMetrics=100. Child process identities, outputs and exit codes are preserved in children.json. These processes are OS workers, not independent LLM agents.\n\nNo lock is needed between these two independent single-writer outputs. Each process writes a role-owned temporary file and renames it to its own target, preventing cross-role overwrite and avoiding a partially published JSON document under the ordinary local filesystem assumptions. The two-file read is not a coherent transaction across both facts. Multiple concurrent instances of the same role, durability after power failure and adversarial filesystem behavior are untested. If a real invariant requires one coherent object, use a single aggregate writer or lock the entire read-modify-write transaction. Atomic rename alone does not prevent a shared-target lost update.\n\nThe authored demonstration establishes local process execution and selected behavior. It does not establish integration with an absent production service or prove every possible concurrency schedule.\n\n## Variants attempted and limits\n\nThe authored fixture ran a scripted shared-target interleaving and actual overlapping Bun processes with separated outputs. A shared-object lock variant was assessed but not implemented because no canonical-object invariant was supplied. No original service integration was available.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"bun\",\"--no-install\",\"probe.mjs\"] | 0 | [two-writers/after.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/after.json) |\n| [\"rg\",\"-n\",\"PriceFacade\\|PriceAdapter\\|PriceService\\|state\\\\.json\\|lastX\\|restart\\|persistent\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"] | 1 | [two-writers/fixture-search.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/fixture-search.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### after.json\n\nExit 0.\n\n```text\n{\"scriptedSharedInterleaving\":{\"lastIndex\":0,\"lastMetrics\":1},\"independentProcessWrites\":{\"lastIndex\":100,\"lastMetrics\":100},\"children\":[{\"role\":\"indexer\",\"pid\":63660,\"exitCode\":0},{\"role\":\"metrics\",\"pid\":63661,\"exitCode\":0}]}\n\n```\n\n",
        "artifact": {
          "path": "fixtures/batch-05/two-writers.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers.result.md",
          "sha256": "01c1b2927eccb1f93430cea2a2bda52f0aa5d9f3f56459e1f781650372a6c47a",
          "bytes": 6090
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
            "item_9",
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
      "path": "fixtures/batch-05/two-writers/after.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/after.json",
      "sha256": "bec0d44d63850f28e9a953944495bfaa84e7b63f54ae6e1df65aaa2373c5bd37",
      "bytes": 477,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"probe.mjs\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"scriptedSharedInterleaving\\\":{\\\"lastIndex\\\":0,\\\"lastMetrics\\\":1},\\\"independentProcessWrites\\\":{\\\"lastIndex\\\":100,\\\"lastMetrics\\\":100},\\\"children\\\":[{\\\"role\\\":\\\"indexer\\\",\\\"pid\\\":63660,\\\"exitCode\\\":0},{\\\"role\\\":\\\"metrics\\\",\\\"pid\\\":63661,\\\"exitCode\\\":0}]}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/two-writers/children.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/children.json",
      "sha256": "26a748bf10c8887782b16790a92fac19f8f31fdd3068291a67b7145f80020ff2",
      "bytes": 375,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "[\n  {\n    \"role\": \"indexer\",\n    \"pid\": 63660,\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"role\\\":\\\"indexer\\\",\\\"field\\\":\\\"lastIndex\\\",\\\"finalValue\\\":100,\\\"pid\\\":63660}\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"role\": \"metrics\",\n    \"pid\": 63661,\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"role\\\":\\\"metrics\\\",\\\"field\\\":\\\"lastMetrics\\\",\\\"finalValue\\\":100,\\\"pid\\\":63661}\\n\",\n    \"stderr\": \"\"\n  }\n]\n"
    },
    {
      "path": "fixtures/batch-05/two-writers/fixture-search.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/fixture-search.json",
      "sha256": "ec798001469f71b2edf189054f1da8aee15e66bca7aa295f3beaa11df4bb2627",
      "bytes": 358,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "{\n  \"argv\": [\n    \"rg\",\n    \"-n\",\n    \"PriceFacade|PriceAdapter|PriceService|state\\\\.json|lastX|restart|persistent\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers\",\n  \"exitCode\": 1,\n  \"stdout\": \"\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/two-writers/input-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/input-manifest.json",
      "sha256": "1ddb3c6adddd8edb6933762caf4f4ca8366db3a00b34cdebc4e15d7329684989",
      "bytes": 246,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "{\n  \"inputSha256\": \"94b2fc2128c1b6d01efc6fbd82820c48021e3300e6f84f7b894f0d7ff8cad2d7\",\n  \"taskGitSha\": null,\n  \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageFreezeIndependentlyVerified\": false,\n  \"fixtures\": []\n}\n"
    },
    {
      "path": "fixtures/batch-05/two-writers/output/indexer-state.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/output/indexer-state.json",
      "sha256": "4309ee781711e08fdfe6f493cd66f9ae5e8fee692fc028765992397e42a3dfb1",
      "bytes": 18,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "{\"lastIndex\":100}\n"
    },
    {
      "path": "fixtures/batch-05/two-writers/output/metrics-state.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/output/metrics-state.json",
      "sha256": "4a06fae6abd8d54dc494d9cc70816201cafa1e6f99eeb537a90efeaed8c65ae2",
      "bytes": 20,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "{\"lastMetrics\":100}\n"
    },
    {
      "path": "fixtures/batch-05/two-writers/output/state-demonstration.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/output/state-demonstration.json",
      "sha256": "5c3a92f25c1b72b6241910a85edcc6f955295e4d76668b41c854bef4cac3be12",
      "bytes": 31,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "{\"lastIndex\":0,\"lastMetrics\":1}"
    },
    {
      "path": "fixtures/batch-05/two-writers/probe.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/probe.mjs",
      "sha256": "cd44880f3e0c4de029ef14db672c809270f7e9153ca0ac9d783ce0a539f74f98",
      "bytes": 1447,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "import assert from 'node:assert/strict';\nimport {mkdir} from 'node:fs/promises';\nimport {readReport} from './report.mjs';\nawait mkdir(new URL('./output/',import.meta.url),{recursive:true});\nconst shared=new URL('./output/state-demonstration.json',import.meta.url);\nawait Bun.write(shared,JSON.stringify({lastIndex:0,lastMetrics:0}));\nconst indexSnapshot=await Bun.file(shared).json();\nconst metricsSnapshot=await Bun.file(shared).json();\nawait Bun.write(shared,JSON.stringify({...indexSnapshot,lastIndex:1}));\nawait Bun.write(shared,JSON.stringify({...metricsSnapshot,lastMetrics:1}));\nconst lost=await Bun.file(shared).json();\nassert.deepEqual(lost,{lastIndex:0,lastMetrics:1});\nconst children=['indexer','metrics'].map(role=>({role,p:Bun.spawn(['bun','--no-install','worker.mjs',role],{cwd:import.meta.dir,stdout:'pipe',stderr:'pipe'})}));\nconst receipts=await Promise.all(children.map(async({role,p})=>({role,pid:p.pid,exitCode:await p.exited,stdout:await new Response(p.stdout).text(),stderr:await new Response(p.stderr).text()})));\nfor(const r of receipts) assert.equal(r.exitCode,0);\nconst merged=await readReport();\nassert.deepEqual(merged,{lastIndex:100,lastMetrics:100});\nawait Bun.write(new URL('./children.json',import.meta.url),JSON.stringify(receipts,null,2)+'\\n');\nconsole.log(JSON.stringify({scriptedSharedInterleaving:lost,independentProcessWrites:merged,children:receipts.map(r=>({role:r.role,pid:r.pid,exitCode:r.exitCode}))}));\n"
    },
    {
      "path": "fixtures/batch-05/two-writers/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/registered-case.json",
      "sha256": "a80450290fe05590d7dd4641cf89342efc4a61fc1e4f67d28b2525d4b8884d3c",
      "bytes": 1697,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "{\n  \"id\": \"two-writers\",\n  \"sourcePaths\": [\n    \"skills/principle-separate-before-serializing-shared-state/SKILL.md\"\n  ],\n  \"prompt\": \"An indexer and a metrics worker each update their own lastX field in state.json. Prevent concurrent write races and assess whether locking is needed.\",\n  \"requirements\": [\n    \"Identify the shared mutable target.\",\n    \"Isolate writable output before considering locking.\",\n    \"Merge independent facts only at the read or reporting boundary; serialize structurally only for a real single-object invariant.\"\n  ],\n  \"expectedFull\": \"Assign indexer-state.json and metrics-state.json to distinct writers before considering a lock. Explain why separate fields in one state.json still share mutation. If one canonical write target is a real invariant, use lockfiles, sequential phases, a single writer or atomic compare-and-swap. Observe authorized operations before claiming implementation.\",\n  \"expectedReduced\": \"If concurrent workers or writes are unavailable, provide the isolated-output design and label any authorized sequential fallback reduced capability. State which execution and concurrency checks were not performed.\",\n  \"expectedBlocked\": \"If required writes or execution are denied or unavailable, block implementation and identify the missing capability or permission. Preserve the isolation-first recommendation.\",\n  \"forbiddenClaims\": [\n    \"Instructions or conventions prevent concurrent write races.\",\n    \"Locking is the default before checking whether sharing is necessary.\",\n    \"Different fields in one state.json are isolated write targets.\",\n    \"A design or sequential fallback proves concurrent worker execution or race prevention.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/two-writers/report.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/report.mjs",
      "sha256": "66b89df57126032e63d36d3c97d068ebe095a33b7da6646e68bb92e97b8102ed",
      "bytes": 317,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "export async function readReport() {\n  const [indexer,metrics]=await Promise.all([\n    Bun.file(new URL('./output/indexer-state.json',import.meta.url)).json(),\n    Bun.file(new URL('./output/metrics-state.json',import.meta.url)).json(),\n  ]);\n  return {lastIndex:indexer.lastIndex,lastMetrics:metrics.lastMetrics};\n}\n"
    },
    {
      "path": "fixtures/batch-05/two-writers/worker.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/worker.mjs",
      "sha256": "65e6e15d9c9d456467b76a0be5b0f5cf18537e46d11fe098b32ab7323e9e775c",
      "bytes": 535,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "import { rename } from 'node:fs/promises';\nconst role=process.argv[2];\nif(!['indexer','metrics'].includes(role)) throw new Error('unknown role');\nconst field=role==='indexer'?'lastIndex':'lastMetrics';\nconst target=new URL(`./output/${role}-state.json`,import.meta.url);\nconst temp=new URL(`./output/${role}-${process.pid}.tmp`,import.meta.url);\nfor(let i=1;i<=100;i++) {\n  await Bun.write(temp,JSON.stringify({[field]:i})+'\\n');\n  await rename(temp,target);\n}\nconsole.log(JSON.stringify({role,field,finalValue:100,pid:process.pid}));\n"
    },
    {
      "path": "fixtures/batch-05/two-writers.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers.result.md",
      "sha256": "01c1b2927eccb1f93430cea2a2bda52f0aa5d9f3f56459e1f781650372a6c47a",
      "bytes": 6090,
      "owners": [
        "grades-native-05.json#3"
      ],
      "text": "# two-writers\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"two-writers\",\n  \"prompt\": \"An indexer and a metrics worker each update their own lastX field in state.json. Prevent concurrent write races and assess whether locking is needed.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Identify the shared mutable target.\",\n    \"Isolate writable output before considering locking.\",\n    \"Merge independent facts only at the read or reporting boundary; serialize structurally only for a real single-object invariant.\"\n  ]\n}\n```\n\n## Actual response and output\n\nThe shared mutable target is the whole state.json document. Separate lastX fields still collide because each read-modify-write can replace the other writer's update. Separate Before Serializing Shared State changes the design to indexer-state.json owned by the indexer and metrics-state.json owned by metrics. Only report.mjs combines the independent facts on read. No shared aggregate file is written.\n\nThere is no original indexer or metrics implementation in the prepared inputs. I authored an explicitly synthetic local implementation from the supplied scenario and executed it. The probe first demonstrated the lost update with a scripted read/read/write/write interleaving, yielding lastIndex=0 and lastMetrics=1. That part is a deterministic interleaving, not an observed simultaneous race. It then launched two actual Bun child processes with distinct owned targets. Each completed 100 snapshot writes. The read boundary returned lastIndex=100 and lastMetrics=100. Child process identities, outputs and exit codes are preserved in children.json. These processes are OS workers, not independent LLM agents.\n\nNo lock is needed between these two independent single-writer outputs. Each process writes a role-owned temporary file and renames it to its own target, preventing cross-role overwrite and avoiding a partially published JSON document under the ordinary local filesystem assumptions. The two-file read is not a coherent transaction across both facts. Multiple concurrent instances of the same role, durability after power failure and adversarial filesystem behavior are untested. If a real invariant requires one coherent object, use a single aggregate writer or lock the entire read-modify-write transaction. Atomic rename alone does not prevent a shared-target lost update.\n\nThe authored demonstration establishes local process execution and selected behavior. It does not establish integration with an absent production service or prove every possible concurrency schedule.\n\n## Variants attempted and limits\n\nThe authored fixture ran a scripted shared-target interleaving and actual overlapping Bun processes with separated outputs. A shared-object lock variant was assessed but not implemented because no canonical-object invariant was supplied. No original service integration was available.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"bun\",\"--no-install\",\"probe.mjs\"] | 0 | [two-writers/after.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/after.json) |\n| [\"rg\",\"-n\",\"PriceFacade\\|PriceAdapter\\|PriceService\\|state\\\\.json\\|lastX\\|restart\\|persistent\",\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared\"] | 1 | [two-writers/fixture-search.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/two-writers/fixture-search.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### after.json\n\nExit 0.\n\n```text\n{\"scriptedSharedInterleaving\":{\"lastIndex\":0,\"lastMetrics\":1},\"independentProcessWrites\":{\"lastIndex\":100,\"lastMetrics\":100},\"children\":[{\"role\":\"indexer\",\"pid\":63660,\"exitCode\":0},{\"role\":\"metrics\",\"pid\":63661,\"exitCode\":0}]}\n\n```\n\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-05/two-writers/input.json",
      "owner": "grades-native-05.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/two-writers/source-manifest.json",
      "owner": "grades-native-05.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/two-writers/source-read",
      "owner": "grades-native-05.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/two-writers/input.json",
      "owner": "grades-native-05.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/two-writers/source-manifest.json",
      "owner": "grades-native-05.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/two-writers/source-read",
      "owner": "grades-native-05.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
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
