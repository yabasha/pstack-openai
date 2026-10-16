# codex: user-tradeoff

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "user-tradeoff",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-native-06.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Apply principle-experience-first to an import workflow. The team can ship ten controls with rough feedback or three polished controls covering the core import loop. Recommend a scope and explain the user outcome rather than implementation convenience. Consider end users, library consumers and future maintainers. Prototype only with authorized available tools.",
  "caseDefinition": {
    "id": "user-tradeoff",
    "sourcePaths": [
      "skills/principle-experience-first/SKILL.md"
    ],
    "prompt": "Apply principle-experience-first to an import workflow. The team can ship ten controls with rough feedback or three polished controls covering the core import loop. Recommend a scope and explain the user outcome rather than implementation convenience. Consider end users, library consumers and future maintainers. Prototype only with authorized available tools.",
    "requirements": [
      "Choose the user outcome with a concrete reason rather than implementation convenience.",
      "Justify every feature, control and option; prefer fewer polished features and tighten the central workflow.",
      "Prototype before committing to design and address transitions, alignment, spacing, feedback and error states.",
      "Weigh end users, colleagues importing libraries or APIs, and future maintainers; explain impact from their perspective.",
      "Foundational thinking governs work sequence; experience governs the target.",
      "Discover tools and permissions before inspection, prototype writes or execution; report only observed operations."
    ],
    "expectedFull": "Choose three polished controls because they let users complete and recover from imports with clear feedback. Justify the controls against the core loop, consider API consumers and maintainers, and use an authorized throwaway prototype before production commitment. Explain relevant details and actual checks.",
    "expectedReduced": "With enough supplied context but unavailable prototype writes or execution, recommend the scope and describe a concrete prototype and feedback/error-state design. Label reduced capability and identify operations not performed.",
    "expectedBlocked": "If essential user or workflow context is missing, identify the missing input before committing to a design. If prototype execution is denied or unavailable, record that operation as blocked without claiming a completed prototype.",
    "forbiddenClaims": [
      "Implementation convenience alone justifies worse user outcomes.",
      "More rough features necessarily provide a better experience.",
      "Library consumers or maintainers do not count as users.",
      "A prototype or test completed without observed authorized operations.",
      "Structural validation establishes host behavioral parity."
    ],
    "caseFile": "docs/parity/cases/skills/principle-experience-first.json"
  },
  "registry": {
    "caseId": "user-tradeoff",
    "caseFile": "docs/parity/cases/skills/principle-experience-first.json",
    "sourcePaths": [
      "skills/principle-experience-first/SKILL.md"
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
      "attemptId": "grades-native-06.json#1",
      "order": 0,
      "gradeFile": "grades-native-06.json",
      "rankWithinFile": 1,
      "host": "codex",
      "caseId": "user-tradeoff",
      "status": "pass",
      "grade": {
        "caseId": "user-tradeoff",
        "host": "codex",
        "status": "pass",
        "execution": "direct",
        "rawTrace": "codex/batch-06.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_26"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "review": "Chooses three coherent choose/preview/confirm/recover controls, explains end-user/API/maintainer tradeoffs and writes disposable interactive sketch plus state model. Actual model checks exercise preview/confirm/error/reset. No production/polished-browser/usability result invented; expected full requires prototype not a measured usability study.",
        "responseArtifact": "fixtures/batch-06/user-tradeoff.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Choose three polished controls because they let users complete and recover from imports with clear feedback. Justify the controls against the core loop, consider API consumers and maintainers, and use an authorized throwaway prototype before production commitment. Explain relevant details and actual checks.",
        "reducedExpected": "With enough supplied context but unavailable prototype writes or execution, recommend the scope and describe a concrete prototype and feedback/error-state design. Label reduced capability and identify operations not performed.",
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
        "text": "# user-tradeoff\n\n## Supplied input\n\n> Apply principle-experience-first to an import workflow. The team can ship ten controls with rough feedback or three polished controls covering the core import loop. Recommend a scope and explain the user outcome rather than implementation convenience. Consider end users, library consumers and future maintainers. Prototype only with authorized available tools.\n\nNamed source files and exact copied source bytes are retained in [user-tradeoff/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff/source-manifest.json) and [user-tradeoff/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Actual recommendation\n\nShip three controls around choosing input, checking the preview and confirming import. Users need to trust what will be written and recover from a bad file. Ten partially explained options make it harder to spot mistakes before data enters the system. This is a provisional product recommendation because actual research, data formats, job duration and user context are not supplied.\n\nThe throwaway prototype has three interactive controls. Choose CSV begins the loop; Import confirms the reviewed sample; Start over recovers from a wrong file or failed validation. The preview is feedback rather than another control. Defer delimiter switches, mappings, scheduling, duplicate policies and advanced options until evidence shows the core task needs them. A required mapping or duplicate policy would change this scope, so do not hide a real data decision behind a default.\n\nFor end users, show selection, preview readiness, row errors, progress and completion in the same place. For API consumers, expose a typed validate/preview result before a separate confirm operation, with explicit errors and an import identity for safe retries. For maintainers, use one state model for empty, preview, invalid, importing, complete and failed, rather than combinations of unrelated booleans. Retain a clear separation between validation and committing records.\n\nFoundational Thinking changes sequence, defining input, preview, error and completion shapes before asynchronous logic. Experience First sets the target, a short trustworthy import loop. Foundations serve that target.\n\n## Actual prototype and checks\n\nprototype.html and import-model.mjs were written after tool and permission discovery. The browser sketch uses a 640px container, aligned left labels/table cells, 24px sections, 44px controls, visible focus, a status region, reduced-motion support and a 150ms button transition. Errors block confirm and reset restores empty state. check.mjs ran with exit0 and exercises preview, confirmation, invalid blocking and reset. check-output.txt and additional-command-results.json preserve output.\n\nRows are fixed synthetic samples. No CSV parser, data write, production integration, long-running job, real validation or asynchronous progress behavior was built. Choosing a file does not upload it. Error text is illustrative, not a diagnosis of selected file contents. importing/failed transitions, actual layout, alignment, spacing, keyboard use and visual polish have not been browser-verified. No screenshot or actual usability result exists. This is a disposable prototype for review, not evidence of a polished shipping UI.\n\n## Variants and limits\n\nAuthorized local prototype and core-loop execution ran. No production edit or external write. No browser interaction was attempted, so browser verification remains unperformed rather than denied.\n",
        "artifact": {
          "path": "fixtures/batch-06/user-tradeoff.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff.result.md",
          "sha256": "c78e872d560c742b4bb34dc8d6848c8c606fd580fe5bbe4635d86a73a73152d4",
          "bytes": 5243
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
                "eventId": "item_26",
                "line": 48,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "06d3edab487bcb80688a70fbf4b9201daabcaf416219f65c56e2755f69d81e07"
              },
              {
                "eventId": "item_26",
                "line": 49,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "5a1fc551c8ac143c175e06efc3b241d3fda7ffacc1b1dba9b58ff470971d4a4c",
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
            "item_26"
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
      "path": "fixtures/batch-06/user-tradeoff/check-output.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff/check-output.txt",
      "sha256": "22ee3fc283cb349f02bc1817a2180a59d28d3991372458bb9d08029635f434eb",
      "bytes": 103,
      "owners": [
        "grades-native-06.json#1"
      ],
      "text": "Core-loop checks cover preview, confirm, blocked invalid rows and reset. Browser rendering unverified.\n"
    },
    {
      "path": "fixtures/batch-06/user-tradeoff/check.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff/check.mjs",
      "sha256": "198f6f4fe27bea4216d8c417c332a39eed93be471cca030b7c82c7fbd5956ddf",
      "bytes": 520,
      "owners": [
        "grades-native-06.json#1"
      ],
      "text": "import {advance} from './import-model.mjs';import assert from 'node:assert/strict';\nlet s=advance({phase:'empty'},{type:'select',file:'sample.csv'});assert.equal(s.phase,'preview');assert.equal(advance(s,{type:'import'}).imported,3);s=advance(s,{type:'select',file:'bad.csv',invalid:true});assert.equal(advance(s,{type:'import'}).phase,'preview');assert.equal(advance(s,{type:'reset'}).phase,'empty');console.log('Core-loop checks cover preview, confirm, blocked invalid rows and reset. Browser rendering unverified.');\n"
    },
    {
      "path": "fixtures/batch-06/user-tradeoff/import-model.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff/import-model.mjs",
      "sha256": "3e1ecdf569a5600ebd5ea6c8f876231f8bd714b070111ca10d292aa3f5f75fab",
      "bytes": 366,
      "owners": [
        "grades-native-06.json#1"
      ],
      "text": "export function advance(state,event){\n if(event.type==='select')return {phase:'preview',file:event.file,rows:3,errors:event.invalid?['Row 2: total must be a number']:[]};\n if(event.type==='import'&&state.phase==='preview'&&!state.errors.length)return {...state,phase:'complete',imported:state.rows};\n if(event.type==='reset')return {phase:'empty'};\n return state;\n}\n"
    },
    {
      "path": "fixtures/batch-06/user-tradeoff/prototype.html",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff/prototype.html",
      "sha256": "1bb197baa678284761d7b04787612f63a0d633a9ff70327b62f8e3c65f93a9c8",
      "bytes": 2687,
      "owners": [
        "grades-native-06.json#1"
      ],
      "text": "<!doctype html><html lang=\"en\"><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width\"><title>Import preview prototype</title><style>\nbody{font:16px system-ui;background:#f3f4f6;color:#17202a;margin:0;padding:48px 24px}main{max-width:640px;margin:auto;background:white;border:1px solid #ccd1d8;border-radius:12px;padding:32px}h1{margin:0 0 12px}p{line-height:1.5}section{margin-top:24px;padding-top:24px;border-top:1px solid #ddd}button,input{font:inherit;min-height:44px}button{padding:8px 16px;margin:12px 12px 0 0;border:1px solid #174f9e;border-radius:6px;background:#174f9e;color:white;transition:background .15s}button:disabled{background:#ddd;color:#555;border-color:#aaa}button:focus-visible,input:focus-visible{outline:3px solid #1976d2;outline-offset:3px}#status{min-height:48px}table{width:100%;border-collapse:collapse}td,th{text-align:left;padding:12px 8px;border-bottom:1px solid #ddd}@media(prefers-reduced-motion:reduce){button{transition:none}}</style><main><h1>Import orders</h1><p>Choose a CSV, check the preview, then confirm. This disposable prototype uses synthetic rows and stores nothing.</p><label>Choose CSV <input id=\"file\" type=\"file\" accept=\".csv,text/csv\"></label><section><div id=\"status\" role=\"status\" aria-live=\"polite\">No file selected.</div><div id=\"preview\"></div><button id=\"confirm\" disabled>Import 3 orders</button><button id=\"reset\" disabled>Start over</button></section></main><script type=\"module\">\nimport {advance} from './import-model.mjs';let state={phase:'empty'};const file=document.querySelector('#file'),status=document.querySelector('#status'),preview=document.querySelector('#preview'),confirm=document.querySelector('#confirm'),reset=document.querySelector('#reset');\nfunction render(){confirm.disabled=state.phase!=='preview'||state.errors.length>0;reset.disabled=state.phase==='empty';status.textContent=state.phase==='empty'?'No file selected.':state.phase==='complete'?'Imported 3 synthetic orders.':state.errors.length?state.errors.join('. ')+' Choose a corrected CSV.':'Preview ready. Check the sample before importing.';preview.innerHTML=state.phase==='preview'&&!state.errors.length?'<table><tr><th>Order</th><th>Total</th></tr><tr><td>Sample 1</td><td>12</td></tr><tr><td>Sample 2</td><td>18</td></tr><tr><td>Sample 3</td><td>24</td></tr></table>':'';}\nfile.onchange=()=>{if(!file.files.length)return;state=advance(state,{type:'select',file:file.files[0].name,invalid:!file.files[0].name.endsWith('.csv')||file.files[0].size===0});render();};confirm.onclick=()=>{state=advance(state,{type:'import'});render();};reset.onclick=()=>{state=advance(state,{type:'reset'});file.value='';render();};\n</script></html>\n"
    },
    {
      "path": "fixtures/batch-06/user-tradeoff.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff.result.md",
      "sha256": "c78e872d560c742b4bb34dc8d6848c8c606fd580fe5bbe4635d86a73a73152d4",
      "bytes": 5243,
      "owners": [
        "grades-native-06.json#1"
      ],
      "text": "# user-tradeoff\n\n## Supplied input\n\n> Apply principle-experience-first to an import workflow. The team can ship ten controls with rough feedback or three polished controls covering the core import loop. Recommend a scope and explain the user outcome rather than implementation convenience. Consider end users, library consumers and future maintainers. Prototype only with authorized available tools.\n\nNamed source files and exact copied source bytes are retained in [user-tradeoff/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff/source-manifest.json) and [user-tradeoff/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/user-tradeoff/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Actual recommendation\n\nShip three controls around choosing input, checking the preview and confirming import. Users need to trust what will be written and recover from a bad file. Ten partially explained options make it harder to spot mistakes before data enters the system. This is a provisional product recommendation because actual research, data formats, job duration and user context are not supplied.\n\nThe throwaway prototype has three interactive controls. Choose CSV begins the loop; Import confirms the reviewed sample; Start over recovers from a wrong file or failed validation. The preview is feedback rather than another control. Defer delimiter switches, mappings, scheduling, duplicate policies and advanced options until evidence shows the core task needs them. A required mapping or duplicate policy would change this scope, so do not hide a real data decision behind a default.\n\nFor end users, show selection, preview readiness, row errors, progress and completion in the same place. For API consumers, expose a typed validate/preview result before a separate confirm operation, with explicit errors and an import identity for safe retries. For maintainers, use one state model for empty, preview, invalid, importing, complete and failed, rather than combinations of unrelated booleans. Retain a clear separation between validation and committing records.\n\nFoundational Thinking changes sequence, defining input, preview, error and completion shapes before asynchronous logic. Experience First sets the target, a short trustworthy import loop. Foundations serve that target.\n\n## Actual prototype and checks\n\nprototype.html and import-model.mjs were written after tool and permission discovery. The browser sketch uses a 640px container, aligned left labels/table cells, 24px sections, 44px controls, visible focus, a status region, reduced-motion support and a 150ms button transition. Errors block confirm and reset restores empty state. check.mjs ran with exit0 and exercises preview, confirmation, invalid blocking and reset. check-output.txt and additional-command-results.json preserve output.\n\nRows are fixed synthetic samples. No CSV parser, data write, production integration, long-running job, real validation or asynchronous progress behavior was built. Choosing a file does not upload it. Error text is illustrative, not a diagnosis of selected file contents. importing/failed transitions, actual layout, alignment, spacing, keyboard use and visual polish have not been browser-verified. No screenshot or actual usability result exists. This is a disposable prototype for review, not evidence of a polished shipping UI.\n\n## Variants and limits\n\nAuthorized local prototype and core-loop execution ran. No production edit or external write. No browser interaction was attempted, so browser verification remains unperformed rather than denied.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-06/user-tradeoff/input.json",
      "owner": "grades-native-06.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-tradeoff/source-manifest.json",
      "owner": "grades-native-06.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-tradeoff/source-reads.txt",
      "owner": "grades-native-06.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-tradeoff/input.json",
      "owner": "grades-native-06.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-tradeoff/source-manifest.json",
      "owner": "grades-native-06.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/user-tradeoff/source-reads.txt",
      "owner": "grades-native-06.json#1",
      "reason": "copied source/input or administrative evaluator helper"
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
