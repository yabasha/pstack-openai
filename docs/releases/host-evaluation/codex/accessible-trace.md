# codex: accessible-trace

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "accessible-trace",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-06.json#3",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Diagnose a fixture process with idle CPU spin, a leak or a visual glitch using matching accessible runtime telemetry. Retain a CPU profile, heap snapshot or CDP trace and map the reduced finding to fixture source. Exercise authorized live diagnostic instrumentation separately from read-only permission. Repeat with supplied telemetry only, an inaccessible artifact, absent controls, denied live mutation and unavailable workers. Use inert fixtures, no external writes or installation, and return a cited diagnosis without a fix.",
  "caseDefinition": {
    "id": "accessible-trace",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/runtime-forensics.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/playbooks/perf-issue.md"
    ],
    "prompt": "Diagnose a fixture process with idle CPU spin, a leak or a visual glitch using matching accessible runtime telemetry. Retain a CPU profile, heap snapshot or CDP trace and map the reduced finding to fixture source. Exercise authorized live diagnostic instrumentation separately from read-only permission. Repeat with supplied telemetry only, an inaccessible artifact, absent controls, denied live mutation and unavailable workers. Use inert fixtures, no external writes or installation, and return a cited diagnosis without a fix.",
    "requirements": [
      "Read the full mode, playbook, guard-the-context-window leaf and complete worker prompt. Discover actual matching controls and record capture and artifact access outcomes; absent telemetry remains explicit.",
      "Capture a real CPU profile for spin, heap snapshot for a leak or CDP trace for a glitch on the matching running process. Preserve the original artifact and capture context.",
      "Reduce the evidence to the hot function, leaked-object retainer chain to a GC root or loop firing without input. Parse large artifacts with an authorized independent worker and inspect its result under the assignment and model contracts; bounded sequential parsing is reduced capability.",
      "Prove the mechanism with authorized exposed CDP eval or a live hotfix without reloading. Read-only permission does not authorize these mutations. Record the intervention and result; unavailable proof keeps the diagnosis provisional.",
      "Map evidence to the file, symbol and allocating or scheduling line. Return signal, reduced finding, mechanism proof, source location and artifact paths with the exact throughput checkpoint: n/a, read-only forensics line. Do not implement a fix unless asked; hand back to Bug fix or Perf once the cause is known."
    ],
    "expectedFull": "Observed matching live capture yields an accessible artifact, inspected reduction and authorized live mechanism proof. The diagnosis cites runtime evidence and the allocating or scheduling source location, returns all five reply items and the exact throughput line, and hands off without implementing a fix. Large-artifact independent parsing requires observed worker creation and result inspection.",
    "expectedReduced": "Accessible supplied traces permit a cited limited assessment with no claim of fresh capture or live mechanism proof. Authorized bounded sequential parsing retains artifact citations but does not satisfy worker independence. Missing source mapping or actual model observation stays explicit; a provisional hypothesis stays provisional.",
    "expectedBlocked": "Missing required contracts stops dependent work. Absent controls, denied capture execution or inaccessible telemetry blocks live capture. Denied or unavailable live mutation blocks mechanism proof, even if a trace is readable. Unread artifacts cannot support findings. Unavailable source mapping blocks a complete mapped diagnosis; lack of fix authorization leaves implementation unperformed.",
    "forbiddenClaims": [
      "Source inspection or structural fixtures prove runtime behavior or either host passed.",
      "Absent or inaccessible telemetry is a captured or parsed artifact.",
      "A supplied trace proves fresh live capture or authorized live mechanism confirmation.",
      "Read-only permission authorizes CDP eval or a live hotfix.",
      "A provisional source hypothesis is a proven mechanism.",
      "Sequential parsing proves independent workers or unknown actual models prove model diversity.",
      "An invented source line or artifact path supports the diagnosis.",
      "The diagnosis authorizes a fix, installation or external writes."
    ],
    "caseFile": "docs/parity/cases/playbooks/runtime-forensics.json"
  },
  "registry": {
    "caseId": "accessible-trace",
    "caseFile": "docs/parity/cases/playbooks/runtime-forensics.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/runtime-forensics.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/poteto-mode/playbooks/bug-fix.md",
      "skills/poteto-mode/playbooks/perf-issue.md"
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
        "execution"
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
        "execution"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-06.json#3",
      "order": 0,
      "gradeFile": "grades-native-06.json",
      "rankWithinFile": 3,
      "host": "codex",
      "caseId": "accessible-trace",
      "status": "reduced-pass",
      "grade": {
        "caseId": "accessible-trace",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-06.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_20",
          "item_21",
          "item_22",
          "item_23"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Required matching control companion absent; custom local driver only.",
          "Exact task Git assignment revision absent."
        ],
        "review": "Actually captures Bun CPU profile for authored idle-spin fixture, maps sampled frames to source and performs separately authorized same-process local endpoint replacement without reload. Independent parser result inspected and numerical caveats retained. Missing matching control companion means strict full live-control mechanism not met; inaccessible artifact is actual ENOENT, other denied conditions simulated.",
        "responseArtifact": "fixtures/batch-06/accessible-trace.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Observed matching live capture yields an accessible artifact, inspected reduction and authorized live mechanism proof. The diagnosis cites runtime evidence and the allocating or scheduling source location, returns all five reply items and the exact throughput line, and hands off without implementing a fix. Large-artifact independent parsing requires observed worker creation and result inspection.",
        "reducedExpected": "Accessible supplied traces permit a cited limited assessment with no claim of fresh capture or live mechanism proof. Authorized bounded sequential parsing retains artifact citations but does not satisfy worker independence. Missing source mapping or actual model observation stays explicit; a provisional hypothesis stays provisional.",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-06.json",
            "reviewedBy": "grade_contract_audit independent reviewer"
          }
        ]
      },
      "topLevelContext": {
        "limits": [
          "Root command JSONL and retained child-produced artifacts inspected. Worker summary transcriptions are not signed raw method receipts.",
          "Inherited-context thread-store failure followed fresh-context success must not be described as absent worker tools.",
          "TaskGit SHA missing in these baseline fixtures remains distinct from package source freeze.",
          "No actual PR/service/scheduler behavior credited from local replay programs.",
          "No exitreceipt needed to infer batch completion here: actual native turn.completed and final response exist; paused outer orchestrator not counted as case failure."
        ]
      },
      "response": {
        "text": "# accessible-trace\n\n## Supplied input\n\n> Diagnose a fixture process with idle CPU spin, a leak or a visual glitch using matching accessible runtime telemetry. Retain a CPU profile, heap snapshot or CDP trace and map the reduced finding to fixture source. Exercise authorized live diagnostic instrumentation separately from read-only permission. Repeat with supplied telemetry only, an inaccessible artifact, absent controls, denied live mutation and unavailable workers. Use inert fixtures, no external writes or installation, and return a cited diagnosis without a fix.\n\nNamed source files and exact copied source bytes are retained in [accessible-trace/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/source-manifest.json) and [accessible-trace/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Signal and diagnosis\n\nThe copied runtime.mjs is a finite calculation. It provides no idle-spin telemetry and cannot justify an idle-spin claim. A new disposable spin.ts reproducer intentionally schedules work without user input. This replacement is explicit and does not establish a defect in supplied runtime.mjs.\n\nA real Bun CPU profile was captured from PID70311 using the command retained in capture.json. Original spin.cpuprofile is4105 bytes, SHA256 0d8a6080540c0bc9a3aa811af6667d41cc079f118c04167b809b327c64ba0687. The process ran without user input and exited0. spin.ts:4 schedules the timer; spin.ts:2 defines idleSpin and performs200000 square-root additions per callback. The profile maps timer node4 to child idleSpin node5. Original evidence pointers are /nodes/3, /nodes/4, /samples and /timeDeltas.\n\nIndependent worker /root/trace_parser reduced the original artifact. idleSpin has367 of372 sampled frames. This is sample share, not CPU utilization or a wall-time percentage. The last sample's1094401us delta spans an unsampled gap and cannot be attributed entirely to clearInterval. reduction.md retains all numerical caveats. No speedup or paired CPU-profile comparison is claimed.\n\n## Live mechanism intervention\n\ncapture.ts used a loopback-only diagnostic endpoint on the same running Bun process. At tick666 the endpoint replaced work with an empty function, without reloading. Before intervention, iterations increased from19856209109.87322 to39712418219.96809. After intervention, ticks increased to948 and1228 while iterations stayed39712418219.96809. This confirms that the timer called the replaced work function in the disposable reproducer. The original source was not fixed. No CPU-reduction magnitude is proven.\n\nThe user authorizes live diagnostic instrumentation for this variant. It is a mutation, separate from permission to inspect telemetry. The actual operation is fetch from a Bun script to a local diagnostic endpoint, not exposed CDP eval. A live runtime function was replaced without reload. Matching control-cli/control-ui companions are absent from the available skill catalog and installed package. This custom local driver supplies real observations but leaves the strict companion-controlled capture/proof gate reduced. No CDP call is claimed.\n\n## Variants attempted\n\n| Variant | Actual operation and artifact | Outcome and limit |\n|---|---|---|\n| Live capture plus separately authorized mutation | bun accessible-trace/capture.ts; spin.cpuprofile and capture.json | Real capture, same-process diagnostic replacement, process exits0; custom driver rather than required companion |\n| Supplied telemetry only | Independent parser read retained profile/capture; supplied-only.cpuprofile is an exact local copy | Real read-only parsing; no originally supplied telemetry existed, so retained live artifact substitutes explicitly; proves no fresh capture in this branch |\n| Inaccessible artifact | Bun attempted inaccessible.cpuprofile, exact error in command-results.json | Actual ENOENT exit1, not ACL denial; unread artifact remains unverified |\n| Absent controls | Catalog/package discovery finds no matching companion | Companion absence is observed; execution remains available and no profiler was installed |\n| Denied live mutation | Read-only policy branch retains diagnosis from profile only, sends no endpoint request | Simulated permission restriction, not host rejection; live mechanism remains provisional for this branch |\n| Unavailable workers | Bounded parent parse of seven nodes and372 samples; independent output retained separately | Simulated worker restriction; parent parsing is sequential reduced capability, never independent evidence |\n\nThe diagnosis is fixture-only. No heap snapshot or visual trace was needed because the chosen symptom was idle work. Large-artifact parsing contract was read even though the captured artifact is small. Actual worker input has an artifact SHA256 but no task Git commit, so exact Git assignment contract remains unmet. No full method receipt, independent model diversity or original-fixture defect claim is made.\n\nthroughput checkpoint: n/a, read-only forensics\n\nHand back to Bug fix or Perf with spin.ts:2 and scheduling line4 plus the profile and capture context. Both playbooks were read. No fix is authorized by this diagnosis and none was implemented.\n",
        "artifact": {
          "path": "fixtures/batch-06/accessible-trace.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace.result.md",
          "sha256": "53559da569cae40ff125d68627115dffe6b336d5716097b04cb172b8d54b77d1",
          "bytes": 6914
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-06.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-06.events.jsonl",
            "sha256": "29e250d426d7f6e1853f71ccc210620bd85774dbbfaa2645ed41e80fe5d27d0b",
            "bytes": 497874,
            "eventReferences": [
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "47752e596478dfe15ca960f407621e4b414297317af6fa359ed92ee8b7fbf796"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "f92e8885378702b4bd7f8c8923b9d86fe857b3100ddd122500e258c0eea90617",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_20",
                "line": 37,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "2e4adcfd8b33b29e8507ed6a18a5c3a631eab90e0ec6aac17ca8f441a2815f2b"
              },
              {
                "eventId": "item_20",
                "line": 38,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d334f54d4bfc726c80daf9c513ab237a570be5e8d9d1d48810140dcac6251519",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_21",
                "line": 39,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ffbc35a438978cea908c763de8fefac87f45b53762fcd9352d7be9251655f4f9"
              },
              {
                "eventId": "item_21",
                "line": 40,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "4b8c5e5185728ca05000907ba4dc414d5ab262b1952248558699c44547a437f5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_22",
                "line": 41,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "54cd8bcedada40958f2f89d617238d4a9bb40835dd56c9a50752739203fd1f83"
              },
              {
                "eventId": "item_22",
                "line": 42,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "2263c0eece92de598fdda73995e0a0cf0b37f7ae7d0c4cf405cd85bfc6eccc05",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_23",
                "line": 43,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3ef1ecd90a2064c1bb85f1a20f8f5355f14e24530670ea46b8e8f5063ba910e4"
              },
              {
                "eventId": "item_23",
                "line": 44,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "055b06c17bfb17100d0569d83cd078b33d8672ecc7bf26bc88ca1b3e73a9ff71",
                "commandResult": {
                  "exitCode": 129
                }
              }
            ]
          }
        ],
        "retainedEvidence": [],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_7",
            "item_20",
            "item_21",
            "item_22",
            "item_23"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-06.json",
              "reviewedBy": "grade_contract_audit independent reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-06/accessible-trace/capture.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/capture.json",
      "sha256": "1cf3ac66311853d2b14847d2b004b3235bdff106ae92f712ad83f34059e122e4",
      "bytes": 1185,
      "owners": [
        "grades-native-06.json#3"
      ],
      "text": "[\n  {\n    \"command\": [\n      \"bun\",\n      \"--cpu-prof\",\n      \"--cpu-prof-name=spin.cpuprofile\",\n      \"--cpu-prof-dir=accessible-trace\",\n      \"accessible-trace/spin.ts\"\n    ],\n    \"target\": {\n      \"pid\": 70311,\n      \"url\": \"http://127.0.0.1:53734/\",\n      \"input\": \"none; periodic timer only\"\n    }\n  },\n  {\n    \"phase\": \"before1\",\n    \"sample\": {\n      \"ticks\": 333,\n      \"iterations\": 19856209109.87322\n    }\n  },\n  {\n    \"phase\": \"before2\",\n    \"sample\": {\n      \"ticks\": 666,\n      \"iterations\": 39712418219.96809\n    }\n  },\n  {\n    \"phase\": \"live diagnostic mutation\",\n    \"sample\": {\n      \"intervention\": \"replaced work function live; no reload\",\n      \"ticks\": 666,\n      \"iterations\": 39712418219.96809\n    }\n  },\n  {\n    \"phase\": \"after1\",\n    \"sample\": {\n      \"ticks\": 948,\n      \"iterations\": 39712418219.96809\n    }\n  },\n  {\n    \"phase\": \"after2\",\n    \"sample\": {\n      \"ticks\": 1228,\n      \"iterations\": 39712418219.96809\n    }\n  },\n  {\n    \"exitCode\": 0,\n    \"stdout\": \"{\\\"pid\\\":70311,\\\"url\\\":\\\"http://127.0.0.1:53734/\\\",\\\"input\\\":\\\"none; periodic timer only\\\"}\\n{\\\"event\\\":\\\"terminated\\\",\\\"ticks\\\":1535,\\\"iterations\\\":39712418219.96809}\\n\",\n    \"stderr\": \"\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/capture.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/capture.ts",
      "sha256": "70726d59ddb8e625601d45b73df70391655f5abcfc0bdc27fe6fbc28ade28ff5",
      "bytes": 1260,
      "owners": [
        "grades-native-06.json#3"
      ],
      "text": "import {writeFile} from 'node:fs/promises';\nconst command=['bun','--cpu-prof','--cpu-prof-name=spin.cpuprofile','--cpu-prof-dir=accessible-trace','accessible-trace/spin.ts'];\nconst p=Bun.spawn(command,{stdout:'pipe',stderr:'pipe'});const reader=p.stdout.getReader();const chunk=await reader.read();const initial=new TextDecoder().decode(chunk.value);const target=JSON.parse(initial.trim());const events:any[]=[{command,target}];\nawait Bun.sleep(350);events.push({phase:'before1',sample:await(await fetch(target.url)).json()});await Bun.sleep(350);events.push({phase:'before2',sample:await(await fetch(target.url)).json()});events.push({phase:'live diagnostic mutation',sample:await(await fetch(target.url+'diagnostic-disable')).json()});await Bun.sleep(350);events.push({phase:'after1',sample:await(await fetch(target.url)).json()});await Bun.sleep(350);events.push({phase:'after2',sample:await(await fetch(target.url)).json()});\nlet rest='';for(;;){const c=await reader.read();if(c.done)break;rest+=new TextDecoder().decode(c.value);}events.push({exitCode:await p.exited,stdout:initial+rest,stderr:await new Response(p.stderr).text()});await writeFile('accessible-trace/capture.json',JSON.stringify(events,null,2));console.log(JSON.stringify(events,null,2));\n"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/reduction.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/reduction.md",
      "sha256": "e6fc349842693c6ee082b24460db5da0609137ea5f73fa0e42f12e688d3ca4cd",
      "bytes": 906,
      "owners": [
        "grades-native-06.json#3"
      ],
      "text": "Worker /root/trace_parser, trace-parser-v1. Original profile SHA256 0d8a6080540c0bc9a3aa811af6667d41cc079f118c04167b809b327c64ba0687, 4105 bytes, 7 nodes, 372 samples and deltas. idleSpin node5 has367 self samples and703400 microseconds of associated deltas. serve node3 has2 samples/3124us; timer node4 has2/3769us; clearInterval node7 has1/1094401us. Pointers /nodes/3, /nodes/4, /samples, /timeDeltas. Timer node4 child5 maps spin.ts:4 scheduling, idleSpin spin.ts:2 work. Position ticks365 at line2. 367/372 is98.6559 percent sampled frames, NOT CPU utilization or wall-time share. Final sample371 has1094401us gap; do not attribute it entirely to clearInterval. Total deltas1804694us vs duration1804833.25us. Worker inspected supplied capture.json but did not independently perform mutation. No paired CPU profile or speedup proof. Complete numerical reduction and caveats transcribed by coordinator.\n"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/spin.cpuprofile",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.cpuprofile",
      "sha256": "0d8a6080540c0bc9a3aa811af6667d41cc079f118c04167b809b327c64ba0687",
      "bytes": 4105,
      "owners": [
        "grades-native-06.json#3"
      ],
      "text": "{\"nodes\":[{\"id\":1,\"callFrame\":{\"functionName\":\"(root)\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[2,4,6]},{\"id\":2,\"callFrame\":{\"functionName\":\"(module)\",\"scriptId\":\"2\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.ts\",\"lineNumber\":0,\"columnNumber\":0},\"hitCount\":0,\"children\":[3]},{\"id\":3,\"callFrame\":{\"functionName\":\"serve\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":2},{\"id\":4,\"callFrame\":{\"functionName\":\"\",\"scriptId\":\"2\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.ts\",\"lineNumber\":3,\"columnNumber\":24},\"hitCount\":2,\"children\":[5],\"positionTicks\":[{\"line\":4,\"ticks\":2}]},{\"id\":5,\"callFrame\":{\"functionName\":\"idleSpin\",\"scriptId\":\"2\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.ts\",\"lineNumber\":1,\"columnNumber\":28},\"hitCount\":367,\"positionTicks\":[{\"line\":2,\"ticks\":365}]},{\"id\":6,\"callFrame\":{\"functionName\":\"\",\"scriptId\":\"2\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.ts\",\"lineNumber\":6,\"columnNumber\":11},\"hitCount\":0,\"children\":[7]},{\"id\":7,\"callFrame\":{\"functionName\":\"clearInterval\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":1}],\"startTime\":1792137544039465,\"endTime\":1792137545844298.2,\"samples\":[3,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7],\"timeDeltas\":[1910,1214,1753,4274,2969,3296,2902,1562,1463,1067,1664,2891,1366,1501,1067,1481,3082,1656,1384,1472,2756,3052,1232,3311,1393,2930,3234,1386,2562,3029,1064,1058,1261,1492,3050,1279,1409,2596,1660,1652,1502,1630,2614,1589,1257,1382,1678,1488,1323,1447,2847,4062,4595,2708,1326,1605,1265,1351,1529,1551,2935,1060,1737,1427,2784,2492,1240,3361,2978,2981,2829,1426,1642,2625,1421,1346,2576,942,2613,3147,1320,2476,1060,1310,3398,1822,3176,3408,3004,1352,2994,1274,1532,1609,2665,1242,1391,1763,3118,1633,1426,1390,3224,1343,2993,1773,3510,1500,1806,1343,1065,1061,1746,1692,1375,1504,1044,1066,1741,3131,2808,3291,1280,1464,1359,1423,1452,1036,1796,2453,1575,3208,2866,2933,1761,1715,4118,1354,1359,1689,1437,2461,1055,1814,1541,1364,1290,2964,2658,2427,1242,2868,1428,2985,1320,2539,1045,1064,2327,4621,2936,3366,1624,1058,1062,2358,1513,2877,1233,2911,1318,3204,1403,1053,1054,1597,1551,1059,4495,3076,1793,1513,1510,2505,1211,2650,2596,1660,1613,1570,1796,1747,2778,1059,1062,1689,2556,1062,1067,1758,1425,1729,1434,1302,3032,975,1809,2666,2942,1062,2779,2693,4270,1309,2698,1060,1591,1592,1063,1055,1062,1276,1285,1361,2417,1063,1276,1277,1369,1398,1045,2118,1535,3974,3013,1678,2901,1649,2405,1242,2717,1063,1742,2471,1311,1392,3092,1303,1603,3183,3447,1627,1060,1064,1061,1228,867,1065,1581,1605,1359,1498,2812,2787,2688,4345,1484,1712,3014,1301,1419,1674,3633,1813,3007,1629,2175,2237,1633,1664,1703,1063,1062,1773,1639,1419,1500,2345,1454,2529,2430,1806,2830,1405,1622,1054,1603,1527,1615,1629,1260,2786,2959,1371,3012,1712,1520,1643,1061,1056,2592,1399,1278,1060,1460,2777,1062,1812,1389,1509,1669,1066,1780,1415,1794,1479,3536,2959,2951,1066,1066,1063,1376,2833,1064,1063,1052,1051,1063,1061,1233,3134,2690,2498,1722,1468,1732,2512,1058,1814,2448,1179,4592,1665,1090,1698,1458,1703,1490,1751,3056,1550,1064,1056,1595,2670,1788,1798,2807,1070,1271,1094401]}"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/spin.ts",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.ts",
      "sha256": "d1f41c503e344b01aad6bf9b3e43bd4cd018f391811af743702da37724d628d8",
      "bytes": 691,
      "owners": [
        "grades-native-06.json#3"
      ],
      "text": "let iterations=0;\nlet work = function idleSpin() { for(let i=0;i<200000;i++) iterations += Math.sqrt(i); };\nlet ticks=0;\nconst timer=setInterval(()=>{ticks++;work();},0);\nconst server=Bun.serve({hostname:'127.0.0.1',port:0,fetch(req){const path=new URL(req.url).pathname;if(path==='/diagnostic-disable'){work=()=>{};return Response.json({intervention:'replaced work function live; no reload',ticks,iterations});}return Response.json({ticks,iterations});}});\nconsole.log(JSON.stringify({pid:process.pid,url:server.url.href,input:'none; periodic timer only'}));\nsetTimeout(()=>{clearInterval(timer);server.stop(true);console.log(JSON.stringify({event:'terminated',ticks,iterations}));},1800);\n"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/supplied-only.cpuprofile",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/supplied-only.cpuprofile",
      "sha256": "0d8a6080540c0bc9a3aa811af6667d41cc079f118c04167b809b327c64ba0687",
      "bytes": 4105,
      "owners": [
        "grades-native-06.json#3"
      ],
      "text": "{\"nodes\":[{\"id\":1,\"callFrame\":{\"functionName\":\"(root)\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":0,\"children\":[2,4,6]},{\"id\":2,\"callFrame\":{\"functionName\":\"(module)\",\"scriptId\":\"2\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.ts\",\"lineNumber\":0,\"columnNumber\":0},\"hitCount\":0,\"children\":[3]},{\"id\":3,\"callFrame\":{\"functionName\":\"serve\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":2},{\"id\":4,\"callFrame\":{\"functionName\":\"\",\"scriptId\":\"2\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.ts\",\"lineNumber\":3,\"columnNumber\":24},\"hitCount\":2,\"children\":[5],\"positionTicks\":[{\"line\":4,\"ticks\":2}]},{\"id\":5,\"callFrame\":{\"functionName\":\"idleSpin\",\"scriptId\":\"2\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.ts\",\"lineNumber\":1,\"columnNumber\":28},\"hitCount\":367,\"positionTicks\":[{\"line\":2,\"ticks\":365}]},{\"id\":6,\"callFrame\":{\"functionName\":\"\",\"scriptId\":\"2\",\"url\":\"file:///Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/spin.ts\",\"lineNumber\":6,\"columnNumber\":11},\"hitCount\":0,\"children\":[7]},{\"id\":7,\"callFrame\":{\"functionName\":\"clearInterval\",\"scriptId\":\"0\",\"url\":\"\",\"lineNumber\":-1,\"columnNumber\":-1},\"hitCount\":1}],\"startTime\":1792137544039465,\"endTime\":1792137545844298.2,\"samples\":[3,3,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,7],\"timeDeltas\":[1910,1214,1753,4274,2969,3296,2902,1562,1463,1067,1664,2891,1366,1501,1067,1481,3082,1656,1384,1472,2756,3052,1232,3311,1393,2930,3234,1386,2562,3029,1064,1058,1261,1492,3050,1279,1409,2596,1660,1652,1502,1630,2614,1589,1257,1382,1678,1488,1323,1447,2847,4062,4595,2708,1326,1605,1265,1351,1529,1551,2935,1060,1737,1427,2784,2492,1240,3361,2978,2981,2829,1426,1642,2625,1421,1346,2576,942,2613,3147,1320,2476,1060,1310,3398,1822,3176,3408,3004,1352,2994,1274,1532,1609,2665,1242,1391,1763,3118,1633,1426,1390,3224,1343,2993,1773,3510,1500,1806,1343,1065,1061,1746,1692,1375,1504,1044,1066,1741,3131,2808,3291,1280,1464,1359,1423,1452,1036,1796,2453,1575,3208,2866,2933,1761,1715,4118,1354,1359,1689,1437,2461,1055,1814,1541,1364,1290,2964,2658,2427,1242,2868,1428,2985,1320,2539,1045,1064,2327,4621,2936,3366,1624,1058,1062,2358,1513,2877,1233,2911,1318,3204,1403,1053,1054,1597,1551,1059,4495,3076,1793,1513,1510,2505,1211,2650,2596,1660,1613,1570,1796,1747,2778,1059,1062,1689,2556,1062,1067,1758,1425,1729,1434,1302,3032,975,1809,2666,2942,1062,2779,2693,4270,1309,2698,1060,1591,1592,1063,1055,1062,1276,1285,1361,2417,1063,1276,1277,1369,1398,1045,2118,1535,3974,3013,1678,2901,1649,2405,1242,2717,1063,1742,2471,1311,1392,3092,1303,1603,3183,3447,1627,1060,1064,1061,1228,867,1065,1581,1605,1359,1498,2812,2787,2688,4345,1484,1712,3014,1301,1419,1674,3633,1813,3007,1629,2175,2237,1633,1664,1703,1063,1062,1773,1639,1419,1500,2345,1454,2529,2430,1806,2830,1405,1622,1054,1603,1527,1615,1629,1260,2786,2959,1371,3012,1712,1520,1643,1061,1056,2592,1399,1278,1060,1460,2777,1062,1812,1389,1509,1669,1066,1780,1415,1794,1479,3536,2959,2951,1066,1066,1063,1376,2833,1064,1063,1052,1051,1063,1061,1233,3134,2690,2498,1722,1468,1732,2512,1058,1814,2448,1179,4592,1665,1090,1698,1458,1703,1490,1751,3056,1550,1064,1056,1595,2670,1788,1798,2807,1070,1271,1094401]}"
    },
    {
      "path": "fixtures/batch-06/accessible-trace.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace.result.md",
      "sha256": "53559da569cae40ff125d68627115dffe6b336d5716097b04cb172b8d54b77d1",
      "bytes": 6914,
      "owners": [
        "grades-native-06.json#3"
      ],
      "text": "# accessible-trace\n\n## Supplied input\n\n> Diagnose a fixture process with idle CPU spin, a leak or a visual glitch using matching accessible runtime telemetry. Retain a CPU profile, heap snapshot or CDP trace and map the reduced finding to fixture source. Exercise authorized live diagnostic instrumentation separately from read-only permission. Repeat with supplied telemetry only, an inaccessible artifact, absent controls, denied live mutation and unavailable workers. Use inert fixtures, no external writes or installation, and return a cited diagnosis without a fix.\n\nNamed source files and exact copied source bytes are retained in [accessible-trace/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/source-manifest.json) and [accessible-trace/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/accessible-trace/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Signal and diagnosis\n\nThe copied runtime.mjs is a finite calculation. It provides no idle-spin telemetry and cannot justify an idle-spin claim. A new disposable spin.ts reproducer intentionally schedules work without user input. This replacement is explicit and does not establish a defect in supplied runtime.mjs.\n\nA real Bun CPU profile was captured from PID70311 using the command retained in capture.json. Original spin.cpuprofile is4105 bytes, SHA256 0d8a6080540c0bc9a3aa811af6667d41cc079f118c04167b809b327c64ba0687. The process ran without user input and exited0. spin.ts:4 schedules the timer; spin.ts:2 defines idleSpin and performs200000 square-root additions per callback. The profile maps timer node4 to child idleSpin node5. Original evidence pointers are /nodes/3, /nodes/4, /samples and /timeDeltas.\n\nIndependent worker /root/trace_parser reduced the original artifact. idleSpin has367 of372 sampled frames. This is sample share, not CPU utilization or a wall-time percentage. The last sample's1094401us delta spans an unsampled gap and cannot be attributed entirely to clearInterval. reduction.md retains all numerical caveats. No speedup or paired CPU-profile comparison is claimed.\n\n## Live mechanism intervention\n\ncapture.ts used a loopback-only diagnostic endpoint on the same running Bun process. At tick666 the endpoint replaced work with an empty function, without reloading. Before intervention, iterations increased from19856209109.87322 to39712418219.96809. After intervention, ticks increased to948 and1228 while iterations stayed39712418219.96809. This confirms that the timer called the replaced work function in the disposable reproducer. The original source was not fixed. No CPU-reduction magnitude is proven.\n\nThe user authorizes live diagnostic instrumentation for this variant. It is a mutation, separate from permission to inspect telemetry. The actual operation is fetch from a Bun script to a local diagnostic endpoint, not exposed CDP eval. A live runtime function was replaced without reload. Matching control-cli/control-ui companions are absent from the available skill catalog and installed package. This custom local driver supplies real observations but leaves the strict companion-controlled capture/proof gate reduced. No CDP call is claimed.\n\n## Variants attempted\n\n| Variant | Actual operation and artifact | Outcome and limit |\n|---|---|---|\n| Live capture plus separately authorized mutation | bun accessible-trace/capture.ts; spin.cpuprofile and capture.json | Real capture, same-process diagnostic replacement, process exits0; custom driver rather than required companion |\n| Supplied telemetry only | Independent parser read retained profile/capture; supplied-only.cpuprofile is an exact local copy | Real read-only parsing; no originally supplied telemetry existed, so retained live artifact substitutes explicitly; proves no fresh capture in this branch |\n| Inaccessible artifact | Bun attempted inaccessible.cpuprofile, exact error in command-results.json | Actual ENOENT exit1, not ACL denial; unread artifact remains unverified |\n| Absent controls | Catalog/package discovery finds no matching companion | Companion absence is observed; execution remains available and no profiler was installed |\n| Denied live mutation | Read-only policy branch retains diagnosis from profile only, sends no endpoint request | Simulated permission restriction, not host rejection; live mechanism remains provisional for this branch |\n| Unavailable workers | Bounded parent parse of seven nodes and372 samples; independent output retained separately | Simulated worker restriction; parent parsing is sequential reduced capability, never independent evidence |\n\nThe diagnosis is fixture-only. No heap snapshot or visual trace was needed because the chosen symptom was idle work. Large-artifact parsing contract was read even though the captured artifact is small. Actual worker input has an artifact SHA256 but no task Git commit, so exact Git assignment contract remains unmet. No full method receipt, independent model diversity or original-fixture defect claim is made.\n\nthroughput checkpoint: n/a, read-only forensics\n\nHand back to Bug fix or Perf with spin.ts:2 and scheduling line4 plus the profile and capture context. Both playbooks were read. No fix is authorized by this diagnosis and none was implemented.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-06/accessible-trace/input.json",
      "owner": "grades-native-06.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/runtime.mjs",
      "owner": "grades-native-06.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-06/accessible-trace/source-manifest.json",
      "owner": "grades-native-06.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/source-reads.txt",
      "owner": "grades-native-06.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/input.json",
      "owner": "grades-native-06.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/runtime.mjs",
      "owner": "grades-native-06.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-06/accessible-trace/source-manifest.json",
      "owner": "grades-native-06.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/accessible-trace/source-reads.txt",
      "owner": "grades-native-06.json#3",
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
