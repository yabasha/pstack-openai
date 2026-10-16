# codex: partition-and-race

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "partition-and-race",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-10.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Run a swarm with coverage slices and a race. Declare the slices and race selection rule before dispatch. Verify exact revisions with a declared sampling method; inject one result missing required evidence, a repeated miss, and a dropout, then cancel one assignment.",
  "caseDefinition": {
    "id": "partition-and-race",
    "sourcePaths": [
      "skills/swarm/SKILL.md"
    ],
    "prompt": "Run a swarm with coverage slices and a race. Declare the slices and race selection rule before dispatch. Verify exact revisions with a declared sampling method; inject one result missing required evidence, a repeated miss, and a dropout, then cancel one assignment.",
    "requirements": [
      "Independent worker spawn, wait and result inspection when available and authorized",
      "Exact SHA and measurement method in assignment and result",
      "Distinct writable outputs and existing evidence artifacts",
      "Stop, terminal inspection and artifact quarantine for cancellation"
    ],
    "expectedFull": "Declare each partition slice and first pass, rank all or best-of race rule before dispatch. Record exact SHAs and method including sample count, sample definition and order. Reject invalid evidence, retry the same assignment at most once and leave a second miss as a gap. Continue with N-1 after a dropout and disclose it. Aggregate coverage only with results for every required slice. Inspect artifacts and quarantine cancelled partial output; report table, evidenced issues, gaps, dropouts and the declared race rule.",
    "expectedReduced": "Authorized sequential slices retain revisions, method, evidence checks and visible gaps, and explicitly report reduced capability without claiming independent workers, background execution, model diversity or race parity. Missing cancellation or persistence bindings remain visible.",
    "expectedBlocked": "Unavailable or denied worker execution blocks full swarm behavior. Missing exact required model, source revision, artifact access or permission blocks the affected assignment. An unobserved stop leaves termination unverified and partial artifacts excluded.",
    "forbiddenClaims": [
      "Sequential work proves independent workers or race parity",
      "Missing SHA, method, artifacts or coverage counts as PASS",
      "More than one retry for invalid SHA or method evidence",
      "Requested models prove actual models or diversity",
      "Cancellation notification proves termination without terminal inspection",
      "Unapproved external action or cloud setup is authorized by swarm"
    ],
    "caseFile": "docs/parity/cases/skills/swarm.json"
  },
  "registry": {
    "caseId": "partition-and-race",
    "caseFile": "docs/parity/cases/skills/swarm.json",
    "sourcePaths": [
      "skills/swarm/SKILL.md"
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
        "inspect-result"
      ],
      "reduced-pass": [
        "read"
      ]
    },
    "executionModes": {
      "pass": [
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
        "execution",
        "writes"
      ],
      "reduced-pass": []
    },
    "requiredMethod": "swarm"
  },
  "attempts": [
    {
      "attemptId": "grades-native-10.json#1",
      "order": 0,
      "gradeFile": "grades-native-10.json",
      "rankWithinFile": 1,
      "host": "codex",
      "caseId": "partition-and-race",
      "status": "reduced-pass",
      "grade": {
        "caseId": "partition-and-race",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "requiredObservationsMet": [
          "read",
          "spawn",
          "wait",
          "inspect-result",
          "stop",
          "inspect-terminal",
          "quarantine-artifacts",
          "execution",
          "isolated-write",
          "review-outcome"
        ],
        "missing": [
          "Valid dashboard and orders coverage results",
          "Complete real-time assignment/action ordering and conforming full method receipt",
          "Observed permanent termination beyond an interrupted resumable turn if claimed"
        ],
        "review": "Native slice/race workers, same-assignment one-retry exhaustion, controlled dropout and real interrupt/interrupted/quarantine are corroborated by persisted calls. Required coverage deliberately remains incomplete. Retrospectively reconstructed event-order integers are corrected and disclosed; the method receipt does not make missing slices complete.",
        "responseArtifact": "fixtures/batch-10/partition-and-race.result.md",
        "rawTrace": "codex/batch-10.events.jsonl",
        "actualCommandEventIds": [
          "item_4",
          "item_5",
          "item_6",
          "item_7",
          "item_9",
          "item_10",
          "item_11",
          "item_12",
          "item_13",
          "item_15",
          "item_16",
          "item_19",
          "item_20",
          "item_24",
          "item_25",
          "item_28",
          "item_29",
          "item_30",
          "item_31",
          "item_32"
        ],
        "nativeMethodReceipts": "native-10-11-tool-receipts.json",
        "variantReview": {
          "assessment": "Complete case response and explicit real/simulated/unrun branches inspected. Source-only negative views do not prove actual host capability removal or denial. Fixed-input gaps are not plugin bugs.",
          "sectionPresent": false
        },
        "limits": [
          "Baseline observations only; source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c remains distinct from actual fixture task revisions and new candidate source.",
          "Native parent/child persisted custom-tool and collaboration records independently inspected; protected dispatch message ciphertext omitted.",
          "Independent child turn_context records now establish gpt-6.1-sol for recovered10/11 sessions. This observation was unavailable to in-run workers and establishes no model-family diversity.",
          "Parent-captured read-only responses are not fabricated worker file-write operations. Proxy guards, local receipt shape checks and scenario metadata do not establish missing full method support."
        ],
        "reviewedBy": "review_workflow_evidence independent full-response/native parent-child rollout review",
        "fullExpected": "Declare each partition slice and first pass, rank all or best-of race rule before dispatch. Record exact SHAs and method including sample count, sample definition and order. Reject invalid evidence, retry the same assignment at most once and leave a second miss as a gap. Continue with N-1 after a dropout and disclose it. Aggregate coverage only with results for every required slice. Inspect artifacts and quarantine cancelled partial output; report table, evidenced issues, gaps, dropouts and the declared race rule.",
        "reducedExpected": "Authorized sequential slices retain revisions, method, evidence checks and visible gaps, and explicitly report reduced capability without claiming independent workers, background execution, model diversity or race parity. Missing cancellation or persistence bindings remain visible.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# partition-and-race\n\n## Supplied input\n\nRun coverage slices and a race, declare both before dispatch, verify exact revisions and method, inject missing evidence twice plus dropout, then cancel an assignment. Full acceptance input is task-contracts.json id partition-and-race.\n\n## Frame and source\n\nRead the complete installed 0.1.0 skills/swarm/SKILL.md and host-capabilities, model-roles, orchestration-contract and workflow-ownership contracts through tools.exec_command. Installed path /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied association. Actual input Git commit bca2ea20c7743bf7e07239688ed6228527f199fd was verified before assignments. Package byte-copy evidence is separate in package-support-contracts/copy-identity.json and cannot independently prove freeze equality.\n\nBefore dispatch, prepare.mjs wrote and displayed plan.md and six immutable assignment.json files. Required coverage slices are invoice, dashboard and orders. Race arms race-a and race-b share the same invoice brief. Declared selection is rank-all, prioritize exact revision/method/digest and grounded observations, then lexical assignment-ID tie-break. One sample means one complete assigned fixture byte read and SHA-256 comparison with the exact Git blob. Order is verify SHA, read blob, read owned copied bytes, compare digest, report. No elapsed-time or performance measurement. Each assignment owns a distinct output directory and inherited selection. Actual model and effort remain unknown.\n\n## Native operations and inspected output\n\ncollaboration.spawn_agent returned actual independent worker identities /root/swarm_race_a, /root/swarm_race_b, /root/swarm_slice_dashboard, /root/swarm_slice_invoice, /root/swarm_slice_orders and /root/swarm_cancel_runtime. Dispatch occurred in waves within free slots, not one simultaneous six-worker batch. collaboration.wait_agent returned a native update. tools.exec_command and Bun aggregate.mjs read every returned artifact and its evidence. No sequential role switching is presented as these workers.\n\n| Assignment | Actual output | Outcome and evidence |\n| --- | --- | --- |\n| slice-invoice | slice-invoice/result.json and evidence.json | Exact revision and declared method match. 371 bytes match SHA-256 64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8. |\n| slice-dashboard attempt 0 | slice-dashboard/attempt-0.json and evidence-0.json | Deliberately missing required resultMethod. Inspected and rejected. |\n| slice-dashboard attempt 1 | slice-dashboard/attempt-1.json and evidence-1.json | Same omission. Single retry exhausted; no third retry. Coverage gap. |\n| slice-orders | slice-orders/dropout.json | Controlled logical dropout before complete sample. Continue without it; coverage gap. |\n| race-a | race-a/result.json and evidence.json | Revision, declared method and digest inspected. |\n| race-b | race-b/result.json and evidence.json | Same exact fixture and method inspected. |\n| cancel-runtime | quarantine/cancel-runtime.partial.json | Partial excluded after native interrupt and inspected interrupted state. |\n\nBoth race results accurately describe controller calling facade, adapter and calculate in the actual module. Neither executes invoice behavior. Both meet the predeclared evidence criteria. Lexical tie-break selects race-a. This selection is an output choice, not an evaluation grade. Required coverage is incomplete because dashboard and orders have no valid completion. No aggregate full-coverage claim is made.\n\n## Failure, retry and cancellation observations\n\nThe missing-method injections are real deliberately malformed result files produced by a native worker. Sidecar diagnostics exist, but required resultMethod in the result does not. After parent read/rejection of attempt 0, collaboration.followup_task delivered the one retry to the same assignment-bound worker and existing owned local state. A mistaken retry-event path was corrected from slice-dashboard/events.jsonl to partition-and-race/events.jsonl before retry execution. It did not create an extra result attempt. Parent read attempt 1, rejected it and stopped retrying. Reuse retained the same assignment and partial output ownership; a fresh-agent retry was not used.\n\nThe dropout was explicitly injected by instruction, not an unexpected crash or enforced host failure. Native worker returned blocked with no valid sample. Host worker unavailability was not simulated as reality.\n\nAfter cancel-runtime reported its partial ready, collaboration.interrupt_agent returned previous_status running. collaboration.list_agents then reported /root/swarm_cancel_runtime as interrupted. This observes a stopped agent turn; it does not prove permanent destruction of the resumable worker context. No runtime fixture process was launched. aggregate.mjs moved the partial into quarantine, confirmed the source was absent and read the quarantined bytes back. The partial is excluded from integration and the race.\n\n## Artifacts and limits\n\nplan.md, immutable per-assignment briefs, actual worker files, append-only events.jsonl, review.md and method-receipt.json are retained under partition-and-race/. Output SHA-256 values in the receipt bind inspected accepted result bytes. Durable readback was executed. These task-local records were not submitted to the installed package validator and are not a normalized full host-evidence schema.\n\nEvents were captured partly retrospectively after native actions. A final correction event explicitly supersedes inaccurate reconstructed order integers and records the action sequence from this session. Complete real-time assignment-event logging and strict simultaneous fan-out remain unsatisfied. The method receipt does not cure those limits.\n\nReal tools used functions.exec, tools.exec_command, Bun reads/writes and native collaboration spawn, follow-up, wait, interrupt and list. No external service, account, model configuration, dependency install, commit, push, PR, publication or schedule occurred. The installed discovery route was not exercised. No pass grade assigned.\n",
        "artifact": {
          "path": "fixtures/batch-10/partition-and-race.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race.result.md",
          "sha256": "50da01f8c21284371ff018ff324319eb32e5d5e92b66b54bf00820e5f51d818a",
          "bytes": 6162
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-10.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-10.events.jsonl",
            "sha256": "ec021dc2ac9a76ee6145304a5e10476b77f4a577a8f6e6764225d5a01a6de70e",
            "bytes": 436747,
            "eventReferences": []
          }
        ],
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
      "path": "fixtures/batch-10/partition-and-race/aggregate.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/aggregate.mjs",
      "sha256": "ebbfdd500112e66c0f47b99a7b2e977f610ae7c0ce3fdfa43aa38be794dba849",
      "bytes": 6632,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "import {readFile,writeFile,appendFile,mkdir,rename,stat} from 'node:fs/promises';import {createHash} from 'node:crypto';\nconst base='partition-and-race';const sha='bca2ea20c7743bf7e07239688ed6228527f199fd';const digest=b=>createHash('sha256').update(b).digest('hex');\nconst events=[{assignmentId:'race-a',kind:'spawn',workerId:'/root/swarm_race_a',order:1},{assignmentId:'race-b',kind:'spawn',workerId:'/root/swarm_race_b',order:2},{assignmentId:'race-a',kind:'completed-result-inspection',order:3},{assignmentId:'slice-dashboard',kind:'spawn',workerId:'/root/swarm_slice_dashboard',order:4},{assignmentId:'slice-invoice',kind:'spawn',workerId:'/root/swarm_slice_invoice',order:5},{assignmentId:'race-b',kind:'completed-result-inspection',order:6},{assignmentId:'slice-orders',kind:'spawn',workerId:'/root/swarm_slice_orders',order:7},{assignmentId:'slice-dashboard',kind:'single-retry',attempt:1,order:8,reason:'same assignment local partial state and ownership retained',tool:'collaboration.followup_task'},{assignmentId:'cancel-runtime',kind:'spawn',workerId:'/root/swarm_cancel_runtime',order:9},{assignmentId:'slice-invoice',kind:'completed-result-inspection',order:10},{assignmentId:'slice-orders',kind:'dropout-inspection',order:11,evidence:'slice-orders/dropout.json'},{assignmentId:'slice-dashboard',kind:'result-rejection',attempt:1,order:12,reason:'resultMethod still absent; allowance exhausted',evidence:'slice-dashboard/attempt-1.json'},{assignmentId:'cancel-runtime',kind:'stop',order:13,tool:'collaboration.interrupt_agent',observed:'previous_status running'},{assignmentId:'cancel-runtime',kind:'inspect-terminal',order:14,tool:'collaboration.list_agents',observed:'interrupted',limit:'Stopped agent turn, not proof of permanent worker destruction. No child runtime process launched.'}];\nawait appendFile(base+'/events.jsonl',events.map(x=>JSON.stringify(x)).join('\\n')+'\\n');\nawait mkdir(base+'/quarantine',{recursive:true});await rename(base+'/cancel-runtime/partial.json',base+'/quarantine/cancel-runtime.partial.json');\nconst partial=JSON.parse(await readFile(base+'/quarantine/cancel-runtime.partial.json'));if(await stat(base+'/cancel-runtime/partial.json').catch(()=>false))throw Error('partial not quarantined');\nawait appendFile(base+'/events.jsonl',JSON.stringify({assignmentId:'cancel-runtime',kind:'quarantine-artifacts',order:15,path:'quarantine/cancel-runtime.partial.json',readback:partial,excluded:true})+'\\n');\nconst accepted=[];for(const id of ['race-a','race-b','slice-invoice']){const assignment=JSON.parse(await readFile(`${base}/${id}/assignment.json`));const bytes=await readFile(`${base}/${id}/result.json`);const result=JSON.parse(bytes);const ev=await readFile(`${base}/${id}/evidence.json`);if(result.assignmentId!==id||result.inputRevision!==sha||JSON.stringify(result.resultMethod)!==JSON.stringify(assignment.method))throw Error('invalid '+id);const local=await readFile(`${base}/${id}/${assignment.file}`);if(digest(local)!==result.digest)throw Error('bad digest '+id);accepted.push({id,workerId:assignment.outputOwner,inputRevision:sha,outputPath:`${base}/${id}`,role:assignment.role,status:'completed',requestedModel:'inherit-parent',actualModel:'unknown',retryCount:0,method:assignment.method,resultRevision:result.inputRevision,resultMethod:result.resultMethod,outputSha256:digest(bytes),resultArtifact:`${base}/${id}/result.json`,evidenceArtifact:`${base}/${id}/evidence.json`,artifactRead:true});}\nfor(const n of [0,1]){const invalid=JSON.parse(await readFile(`${base}/slice-dashboard/attempt-${n}.json`));if(invalid.resultMethod||invalid.method)throw Error('injection changed');}\nconst receipt={schemaVersion:1,kind:'swarm',inputRevision:sha,packageCommit:'f4623636a287bea2aa79c4b2234a53d20a5f193c',packageFreezeBinding:'supplied, installed bytes independently hashed but commit equality unverified',assignments:accepted,reviewArtifact:'partition-and-race/review.md',reviewedBy:'/root',declaredOrder:'plan.md written and read before dispatch; events.jsonl records observed action sequence',partition:{requiredSlices:['invoice','dashboard','orders'],results:{invoice:'slice-invoice'},gaps:['dashboard repeated missing method','orders controlled dropout']},race:{rule:'rank-all',assignments:['race-a','race-b'],winner:'race-a',ruleArtifact:'partition-and-race/plan.md',reason:'both exact revision/method/digest complete and source observations valid; declared lexical tie-break selects race-a'},cancelled:['cancel-runtime'],quarantined:['partition-and-race/quarantine/cancel-runtime.partial.json'],failureExercises:[{assignmentId:'slice-dashboard',kind:'missing-method',attempt:0,evidence:'slice-dashboard/attempt-0.json'},{assignmentId:'slice-dashboard',kind:'missing-method',attempt:1,evidence:'slice-dashboard/attempt-1.json'},{assignmentId:'slice-orders',kind:'controlled-dropout',evidence:'slice-orders/dropout.json'}],limits:['Native workers observed. Actual model unknown, no diversity claim.','Logical fault injections deliberate; host did not unexpectedly fail.','Work dispatched in waves within slots, not one simultaneous N-worker batch.','Receipt is task-local observed record, not validated package host-evidence schema or case acceptance grade.','Invalid and cancelled assignments retained via events rather than normalized accepted assignment rows.']};\nawait writeFile(base+'/method-receipt.json',JSON.stringify(receipt,null,2));\nawait writeFile(base+'/review.md','# Inspected results\\n\\nRoot read every accepted result and exact revision, method, file hash and command artifact. Both invoice race observations accurately describe controller -> facade -> adapter -> calculate in the real 371-byte fixture. They are source observations, not executed invoice behavior. Both race arms meet the declared evidence criteria; lexical tie-break selects race-a. Invoice required slice has an inspected result. Dashboard intentionally lacks required resultMethod twice despite sidecar diagnostics, so both were rejected and no third retry was made. Orders stopped deliberately before the sample, so coverage is incomplete. Cancel-runtime agent turn was interrupted via native operation, list_agents showed interrupted, and partial output was moved then read back under quarantine. No runtime fixture process ran. Interrupted context is resumable; permanent destruction is not claimed. Full coverage and strict simultaneous fan-out are unproved.\\n');\nconsole.log(JSON.stringify({accepted:accepted.map(x=>x.id),winner:receipt.race.winner,gaps:receipt.partition.gaps,partialQuarantined:!!partial,receiptReadback:JSON.parse(await readFile(base+'/method-receipt.json')).kind}));\n"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/cancel-runtime/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/cancel-runtime/assignment.json",
      "sha256": "960d501e01b12c1c73b5cc1ab7629ff4b7209d3a810800819ed7e2d259bf6258",
      "bytes": 946,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"id\": \"cancel-runtime\",\n  \"scope\": \"cancellation only\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"outputOwner\": \"/root/swarm_cancel_runtime\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/cancel-runtime\",\n  \"role\": \"swarm evidence worker\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [],\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n    \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n  },\n  \"file\": \"runtime.mjs\",\n  \"variant\": \"cancel\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageVersion\": \"0.1.0\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/finalize.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/finalize.mjs",
      "sha256": "8ee00a73b96ba75810fdf1c0d7e4227d3154b022ff3ccb10b0ca89550d825170",
      "bytes": 7393,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "import {writeFile,appendFile,readFile} from 'node:fs/promises';\nawait appendFile('partition-and-race/events.jsonl',JSON.stringify({kind:'bookkeeping-correction',supersedes:'order integers in reconstructed aggregate events',reason:'Those events were captured retrospectively. Do not treat their order numbers as an observed full dispatch/completion sequence.',observedSequence:['spawn race-a','spawn race-b','spawn slice-dashboard','spawn slice-invoice','spawn slice-orders','read race-a and race-b results','inspect dashboard attempt 0 and reject','follow-up single dashboard retry','spawn cancel-runtime','spawn walkthrough explainer outside swarm','native wait','inspect dashboard attempt 1, orders dropout and invoice result','interrupt cancel-runtime','inspect interrupted agent status','quarantine partial and inspect all accepted result/evidence artifacts'],limits:'Initial immutable briefs predate dispatch. No realtime append-only spawn-event receipts or normalized full validator evidence were captured. Native calls and worker identities remain visible in session.'})+'\\n');\nawait writeFile('partition-and-race.result.md',`# partition-and-race\\n\\n## Supplied input\\n\\nRun coverage slices and a race, declare both before dispatch, verify exact revisions and method, inject missing evidence twice plus dropout, then cancel an assignment. Full acceptance input is task-contracts.json id partition-and-race.\\n\\n## Frame and source\\n\\nRead the complete installed 0.1.0 skills/swarm/SKILL.md and host-capabilities, model-roles, orchestration-contract and workflow-ownership contracts through tools.exec_command. Installed path /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied association. Actual input Git commit bca2ea20c7743bf7e07239688ed6228527f199fd was verified before assignments. Package byte-copy evidence is separate in package-support-contracts/copy-identity.json and cannot independently prove freeze equality.\\n\\nBefore dispatch, prepare.mjs wrote and displayed plan.md and six immutable assignment.json files. Required coverage slices are invoice, dashboard and orders. Race arms race-a and race-b share the same invoice brief. Declared selection is rank-all, prioritize exact revision/method/digest and grounded observations, then lexical assignment-ID tie-break. One sample means one complete assigned fixture byte read and SHA-256 comparison with the exact Git blob. Order is verify SHA, read blob, read owned copied bytes, compare digest, report. No elapsed-time or performance measurement. Each assignment owns a distinct output directory and inherited selection. Actual model and effort remain unknown.\\n\\n## Native operations and inspected output\\n\\ncollaboration.spawn_agent returned actual independent worker identities /root/swarm_race_a, /root/swarm_race_b, /root/swarm_slice_dashboard, /root/swarm_slice_invoice, /root/swarm_slice_orders and /root/swarm_cancel_runtime. Dispatch occurred in waves within free slots, not one simultaneous six-worker batch. collaboration.wait_agent returned a native update. tools.exec_command and Bun aggregate.mjs read every returned artifact and its evidence. No sequential role switching is presented as these workers.\\n\\n| Assignment | Actual output | Outcome and evidence |\\n| --- | --- | --- |\\n| slice-invoice | slice-invoice/result.json and evidence.json | Exact revision and declared method match. 371 bytes match SHA-256 64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8. |\\n| slice-dashboard attempt 0 | slice-dashboard/attempt-0.json and evidence-0.json | Deliberately missing required resultMethod. Inspected and rejected. |\\n| slice-dashboard attempt 1 | slice-dashboard/attempt-1.json and evidence-1.json | Same omission. Single retry exhausted; no third retry. Coverage gap. |\\n| slice-orders | slice-orders/dropout.json | Controlled logical dropout before complete sample. Continue without it; coverage gap. |\\n| race-a | race-a/result.json and evidence.json | Revision, declared method and digest inspected. |\\n| race-b | race-b/result.json and evidence.json | Same exact fixture and method inspected. |\\n| cancel-runtime | quarantine/cancel-runtime.partial.json | Partial excluded after native interrupt and inspected interrupted state. |\\n\\nBoth race results accurately describe controller calling facade, adapter and calculate in the actual module. Neither executes invoice behavior. Both meet the predeclared evidence criteria. Lexical tie-break selects race-a. This selection is an output choice, not an evaluation grade. Required coverage is incomplete because dashboard and orders have no valid completion. No aggregate full-coverage claim is made.\\n\\n## Failure, retry and cancellation observations\\n\\nThe missing-method injections are real deliberately malformed result files produced by a native worker. Sidecar diagnostics exist, but required resultMethod in the result does not. After parent read/rejection of attempt 0, collaboration.followup_task delivered the one retry to the same assignment-bound worker and existing owned local state. A mistaken retry-event path was corrected from slice-dashboard/events.jsonl to partition-and-race/events.jsonl before retry execution. It did not create an extra result attempt. Parent read attempt 1, rejected it and stopped retrying. Reuse retained the same assignment and partial output ownership; a fresh-agent retry was not used.\\n\\nThe dropout was explicitly injected by instruction, not an unexpected crash or enforced host failure. Native worker returned blocked with no valid sample. Host worker unavailability was not simulated as reality.\\n\\nAfter cancel-runtime reported its partial ready, collaboration.interrupt_agent returned previous_status running. collaboration.list_agents then reported /root/swarm_cancel_runtime as interrupted. This observes a stopped agent turn; it does not prove permanent destruction of the resumable worker context. No runtime fixture process was launched. aggregate.mjs moved the partial into quarantine, confirmed the source was absent and read the quarantined bytes back. The partial is excluded from integration and the race.\\n\\n## Artifacts and limits\\n\\nplan.md, immutable per-assignment briefs, actual worker files, append-only events.jsonl, review.md and method-receipt.json are retained under partition-and-race/. Output SHA-256 values in the receipt bind inspected accepted result bytes. Durable readback was executed. These task-local records were not submitted to the installed package validator and are not a normalized full host-evidence schema.\\n\\nEvents were captured partly retrospectively after native actions. A final correction event explicitly supersedes inaccurate reconstructed order integers and records the action sequence from this session. Complete real-time assignment-event logging and strict simultaneous fan-out remain unsatisfied. The method receipt does not cure those limits.\\n\\nReal tools used functions.exec, tools.exec_command, Bun reads/writes and native collaboration spawn, follow-up, wait, interrupt and list. No external service, account, model configuration, dependency install, commit, push, PR, publication or schedule occurred. The installed discovery route was not exercised. No pass grade assigned.\\n`);\nconsole.log('wrote partition-and-race.result.md');\n"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/method-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/method-receipt.json",
      "sha256": "4fe7feacf7e8c83a7a7b02b153d237b67fbff762c6aea55c55802340250e6ba9",
      "bytes": 6262,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"kind\": \"swarm\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageFreezeBinding\": \"supplied, installed bytes independently hashed but commit equality unverified\",\n  \"assignments\": [\n    {\n      \"id\": \"race-a\",\n      \"workerId\": \"/root/swarm_race_a\",\n      \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n      \"outputPath\": \"partition-and-race/race-a\",\n      \"role\": \"swarm evidence worker\",\n      \"status\": \"completed\",\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n        \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n      },\n      \"resultRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n        \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n      },\n      \"outputSha256\": \"51dd76a7b4af75f0b3c2c3391ae26d446d477d8f8c4e94436c9712c056cdf4a4\",\n      \"resultArtifact\": \"partition-and-race/race-a/result.json\",\n      \"evidenceArtifact\": \"partition-and-race/race-a/evidence.json\",\n      \"artifactRead\": true\n    },\n    {\n      \"id\": \"race-b\",\n      \"workerId\": \"/root/swarm_race_b\",\n      \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n      \"outputPath\": \"partition-and-race/race-b\",\n      \"role\": \"swarm evidence worker\",\n      \"status\": \"completed\",\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n        \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n      },\n      \"resultRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n        \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n      },\n      \"outputSha256\": \"3702d1cc8fbed73993eed06dbb78e8fe564046ef081d4eb46eb4bae4e3d3515d\",\n      \"resultArtifact\": \"partition-and-race/race-b/result.json\",\n      \"evidenceArtifact\": \"partition-and-race/race-b/evidence.json\",\n      \"artifactRead\": true\n    },\n    {\n      \"id\": \"slice-invoice\",\n      \"workerId\": \"/root/swarm_slice_invoice\",\n      \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n      \"outputPath\": \"partition-and-race/slice-invoice\",\n      \"role\": \"swarm evidence worker\",\n      \"status\": \"completed\",\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"retryCount\": 0,\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n        \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n      },\n      \"resultRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n        \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n      },\n      \"outputSha256\": \"c882481846064803810f3854e376f404b5d08536674fa566bbe7cbeb1de1189d\",\n      \"resultArtifact\": \"partition-and-race/slice-invoice/result.json\",\n      \"evidenceArtifact\": \"partition-and-race/slice-invoice/evidence.json\",\n      \"artifactRead\": true\n    }\n  ],\n  \"reviewArtifact\": \"partition-and-race/review.md\",\n  \"reviewedBy\": \"/root\",\n  \"declaredOrder\": \"plan.md written and read before dispatch; events.jsonl records observed action sequence\",\n  \"partition\": {\n    \"requiredSlices\": [\n      \"invoice\",\n      \"dashboard\",\n      \"orders\"\n    ],\n    \"results\": {\n      \"invoice\": \"slice-invoice\"\n    },\n    \"gaps\": [\n      \"dashboard repeated missing method\",\n      \"orders controlled dropout\"\n    ]\n  },\n  \"race\": {\n    \"rule\": \"rank-all\",\n    \"assignments\": [\n      \"race-a\",\n      \"race-b\"\n    ],\n    \"winner\": \"race-a\",\n    \"ruleArtifact\": \"partition-and-race/plan.md\",\n    \"reason\": \"both exact revision/method/digest complete and source observations valid; declared lexical tie-break selects race-a\"\n  },\n  \"cancelled\": [\n    \"cancel-runtime\"\n  ],\n  \"quarantined\": [\n    \"partition-and-race/quarantine/cancel-runtime.partial.json\"\n  ],\n  \"failureExercises\": [\n    {\n      \"assignmentId\": \"slice-dashboard\",\n      \"kind\": \"missing-method\",\n      \"attempt\": 0,\n      \"evidence\": \"slice-dashboard/attempt-0.json\"\n    },\n    {\n      \"assignmentId\": \"slice-dashboard\",\n      \"kind\": \"missing-method\",\n      \"attempt\": 1,\n      \"evidence\": \"slice-dashboard/attempt-1.json\"\n    },\n    {\n      \"assignmentId\": \"slice-orders\",\n      \"kind\": \"controlled-dropout\",\n      \"evidence\": \"slice-orders/dropout.json\"\n    }\n  ],\n  \"limits\": [\n    \"Native workers observed. Actual model unknown, no diversity claim.\",\n    \"Logical fault injections deliberate; host did not unexpectedly fail.\",\n    \"Work dispatched in waves within slots, not one simultaneous N-worker batch.\",\n    \"Receipt is task-local observed record, not validated package host-evidence schema or case acceptance grade.\",\n    \"Invalid and cancelled assignments retained via events rather than normalized accepted assignment rows.\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/plan.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/plan.md",
      "sha256": "c4fbca0d2043264bccd63606264e467150b0123e56a3dd3e0442c9ad17314706",
      "bytes": 1266,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "# Task phases\n\n1. Frame. Declared before swarm dispatch.\n2. Fan out. Six assignments across actual free concurrency slots.\n3. Aggregate. Inspect actual artifacts and terminal states.\n4. Report. Keep gaps and exclusions visible.\n\nRequired coverage slices invoice, dashboard and orders. One file per slice. Race arms race-a and race-b have identical invoice brief. Race selection rank-all. Rank complete revision/method/digest evidence first, then explicit observations; ties resolve lexicographically by assignment ID. Neither elapsed time nor dispatch order selects winner. All race arms must terminate and be inspected. Missing-method slice intentionally omits method on attempt 0 and same assignment retry 1; reject both, no third attempt. Orders deliberately drops out without valid result, retain gap. Cancel-runtime writes a partial then waits; stop through native interrupt, inspect terminal status and quarantine partial. No benchmark. Method is one complete fixture-byte sample per assignment. Input SHA bca2ea20c7743bf7e07239688ed6228527f199fd. Package freeze supplied f4623636a287bea2aa79c4b2234a53d20a5f193c, distinct from task input. Outputs are new, not part of input commit. No external actions, models inherited, actual model unknown unless observed.\n"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/prepare.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/prepare.mjs",
      "sha256": "799b9ef5cce2e64b38ab1a28b0a56c30ab88a8f773b7bb509175d1e2dc5c1ace",
      "bytes": 2781,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "import {readFile,writeFile,mkdir,copyFile} from 'node:fs/promises';import {resolve} from 'node:path';\nconst dir=resolve('partition-and-race');const sha='bca2ea20c7743bf7e07239688ed6228527f199fd';\nconst assignments=[['slice-invoice','coverage invoice','invoice.mjs','valid'],['slice-dashboard','coverage dashboard','dashboard.mjs','missing-method'],['slice-orders','coverage orders','orders.json','dropout'],['race-a','race invoice','invoice.mjs','valid'],['race-b','race invoice','invoice.mjs','valid'],['cancel-runtime','cancellation only','runtime.mjs','cancel']];\nconst method={sampleCount:1,sampleDefinition:'one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison',order:'verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.'};\nfor(const [id,scope,file,variant] of assignments){await mkdir(dir+'/'+id,{recursive:true});await copyFile('committed-inputs/'+file,dir+'/'+id+'/'+file);const record={id,scope,inputRevision:sha,outputOwner:'/root/swarm_'+id.replaceAll('-','_'),isolatedOutputPath:dir+'/'+id,role:'swarm evidence worker',retryCount:0,terminalStatus:'pending',evidenceLinks:[],method,file,variant,packageCommit:'f4623636a287bea2aa79c4b2234a53d20a5f193c',packageVersion:'0.1.0',requestedModel:'inherit-parent',actualModel:'unknown'};await writeFile(dir+'/'+id+'/assignment.json',JSON.stringify(record,null,2))}\nawait writeFile(dir+'/plan.md',`# Task phases\\n\\n1. Frame. Declared before swarm dispatch.\\n2. Fan out. Six assignments across actual free concurrency slots.\\n3. Aggregate. Inspect actual artifacts and terminal states.\\n4. Report. Keep gaps and exclusions visible.\\n\\nRequired coverage slices invoice, dashboard and orders. One file per slice. Race arms race-a and race-b have identical invoice brief. Race selection rank-all. Rank complete revision/method/digest evidence first, then explicit observations; ties resolve lexicographically by assignment ID. Neither elapsed time nor dispatch order selects winner. All race arms must terminate and be inspected. Missing-method slice intentionally omits method on attempt 0 and same assignment retry 1; reject both, no third attempt. Orders deliberately drops out without valid result, retain gap. Cancel-runtime writes a partial then waits; stop through native interrupt, inspect terminal status and quarantine partial. No benchmark. Method is one complete fixture-byte sample per assignment. Input SHA ${sha}. Package freeze supplied f4623636a287bea2aa79c4b2234a53d20a5f193c, distinct from task input. Outputs are new, not part of input commit. No external actions, models inherited, actual model unknown unless observed.\\n`);\nconsole.log(await readFile(dir+'/plan.md','utf8'));\n"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/quarantine/cancel-runtime.partial.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/quarantine/cancel-runtime.partial.json",
      "sha256": "05341f72059fb8be3ae0e225f5d14724385e30b04bdcf5a059395a18b7b547dd",
      "bytes": 393,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"assignmentId\": \"cancel-runtime\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"partial\": true,\n  \"command\": {\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"--verify\",\n      \"bca2ea20c7743bf7e07239688ed6228527f199fd^{commit}\"\n    ],\n    \"exitCode\": 0,\n    \"stdout\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\\n\",\n    \"stderr\": \"\"\n  },\n  \"runtimeExecuted\": false\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-a/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/race-a/assignment.json",
      "sha256": "0dc2977c921ab885bc2c866502f1d985cd6170e3c70eeaa8076e146f3e7fc20f",
      "bytes": 916,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"id\": \"race-a\",\n  \"scope\": \"race invoice\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"outputOwner\": \"/root/swarm_race_a\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/race-a\",\n  \"role\": \"swarm evidence worker\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [],\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n    \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n  },\n  \"file\": \"invoice.mjs\",\n  \"variant\": \"valid\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageVersion\": \"0.1.0\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-a/evidence.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/race-a/evidence.json",
      "sha256": "594e79a56eaa79a314586a6122eb1d69795a70f75a624677498dda7a22adb856",
      "bytes": 1638,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"receipts\": [\n    {\n      \"command\": [\n        \"git\",\n        \"rev-parse\",\n        \"bca2ea20c7743bf7e07239688ed6228527f199fd^{commit}\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"command\": [\n        \"git\",\n        \"show\",\n        \"bca2ea20c7743bf7e07239688ed6228527f199fd:committed-inputs/invoice.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\nexport function adapter(invoice){return calculate(invoice.rows)}\\nexport function facade(invoice){return adapter(invoice)}\\nexport function controller(invoice){return {total:facade(invoice)}}\\nexport function format(n){if(!Number.isFinite(n))throw new Error(\\\"nonfinite\\\");return n.toFixed(2)}\\n\",\n      \"stderr\": \"\"\n    }\n  ],\n  \"localRead\": {\n    \"path\": \"partition-and-race/race-a/invoice.mjs\",\n    \"bytes\": 371,\n    \"content\": \"export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\nexport function adapter(invoice){return calculate(invoice.rows)}\\nexport function facade(invoice){return adapter(invoice)}\\nexport function controller(invoice){return {total:facade(invoice)}}\\nexport function format(n){if(!Number.isFinite(n))throw new Error(\\\"nonfinite\\\");return n.toFixed(2)}\\n\",\n    \"digest\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\"\n  },\n  \"comparison\": {\n    \"committed\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n    \"copied\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n    \"byteIdentical\": true\n  }\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-a/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/race-a/result.json",
      "sha256": "51dd76a7b4af75f0b3c2c3391ae26d446d477d8f8c4e94436c9712c056cdf4a4",
      "bytes": 1254,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"assignmentId\": \"race-a\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"resultMethod\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n    \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n  },\n  \"digest\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n  \"comparison\": {\n    \"committed\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n    \"copied\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n    \"byteIdentical\": true\n  },\n  \"reportLabel\": \"ISSUES\",\n  \"observation\": \"controller calls facade, which only calls adapter, which only forwards invoice.rows to calculate. The facade adds one call boundary and no transformation. calculate reduces qty times unitPrice from zero; format rejects nonfinite values and applies toFixed(2).\",\n  \"evidenceLinks\": [\n    \"partition-and-race/race-a/evidence.json\"\n  ],\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageVersion\": \"0.1.0\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-b/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/race-b/assignment.json",
      "sha256": "1b5d9b62fdd16a97180dc0b9b35a0e978984bcffdae75ef197901fe334c9bd0a",
      "bytes": 916,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"id\": \"race-b\",\n  \"scope\": \"race invoice\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"outputOwner\": \"/root/swarm_race_b\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/race-b\",\n  \"role\": \"swarm evidence worker\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [],\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n    \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n  },\n  \"file\": \"invoice.mjs\",\n  \"variant\": \"valid\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageVersion\": \"0.1.0\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-b/evidence.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/race-b/evidence.json",
      "sha256": "4c9f8820e5d3be06b13b68dbfe6defdf6d5328ca5036c4402a47fde355b3395f",
      "bytes": 1579,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"runtime\": \"1.4.2\",\n  \"commands\": [\n    {\n      \"command\": [\n        \"git\",\n        \"rev-parse\",\n        \"bca2ea20c7743bf7e07239688ed6228527f199fd^{commit}\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"command\": [\n        \"git\",\n        \"show\",\n        \"bca2ea20c7743bf7e07239688ed6228527f199fd:committed-inputs/invoice.mjs\"\n      ],\n      \"exitCode\": 0,\n      \"stdout\": \"export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\nexport function adapter(invoice){return calculate(invoice.rows)}\\nexport function facade(invoice){return adapter(invoice)}\\nexport function controller(invoice){return {total:facade(invoice)}}\\nexport function format(n){if(!Number.isFinite(n))throw new Error(\\\"nonfinite\\\");return n.toFixed(2)}\\n\",\n      \"stderr\": \"\"\n    }\n  ],\n  \"copyRead\": {\n    \"path\": \"partition-and-race/race-b/invoice.mjs\",\n    \"bytes\": 371,\n    \"content\": \"export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\nexport function adapter(invoice){return calculate(invoice.rows)}\\nexport function facade(invoice){return adapter(invoice)}\\nexport function controller(invoice){return {total:facade(invoice)}}\\nexport function format(n){if(!Number.isFinite(n))throw new Error(\\\"nonfinite\\\");return n.toFixed(2)}\\n\"\n  },\n  \"comparison\": {\n    \"gitBlobSha256\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n    \"copiedSha256\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n    \"equal\": true\n  }\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-b/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/race-b/result.json",
      "sha256": "3702d1cc8fbed73993eed06dbb78e8fe564046ef081d4eb46eb4bae4e3d3515d",
      "bytes": 1172,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"assignmentId\": \"race-b\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"resultMethod\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n    \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n  },\n  \"digest\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n  \"comparison\": {\n    \"gitBlobSha256\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n    \"copiedSha256\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n    \"equal\": true\n  },\n  \"evidenceArtifact\": \"partition-and-race/race-b/evidence.json\",\n  \"observation\": \"controller -> facade -> adapter -> calculate traverses two forwarding wrappers; calculate reduces qty*unitPrice over rows from zero, while format separately rejects nonfinite values and rounds with toFixed(2).\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageVersion\": \"0.1.0\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/reject-first.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/reject-first.mjs",
      "sha256": "fb3250241ac26cdf91e392f946093f2053beb9998425c1dea5a0bca79989cc40",
      "bytes": 650,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "import {readFile,appendFile} from 'node:fs/promises';\nconst r=JSON.parse(await readFile('partition-and-race/slice-dashboard/attempt-0.json'));if(r.method||r.resultMethod)throw Error('not missing');await appendFile('partition-and-race/events.jsonl',JSON.stringify({assignmentId:'slice-dashboard',kind:'result-rejection',attempt:0,reason:'required method absent',evidence:'slice-dashboard/attempt-0.json',permissions:'unchanged local execution and isolated writes authorized',decision:'one retry, same scope input SHA output path and owner. No third attempt.'})+'\\n');console.log('Rejected attempt 0 after artifact inspection. One retry authorized.');\n"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/review.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/review.md",
      "sha256": "32f6e9c4ad4381084a3f146317f20486096d4e57c179663eaa30417c111513bb",
      "bytes": 968,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "# Inspected results\n\nRoot read every accepted result and exact revision, method, file hash and command artifact. Both invoice race observations accurately describe controller -> facade -> adapter -> calculate in the real 371-byte fixture. They are source observations, not executed invoice behavior. Both race arms meet the declared evidence criteria; lexical tie-break selects race-a. Invoice required slice has an inspected result. Dashboard intentionally lacks required resultMethod twice despite sidecar diagnostics, so both were rejected and no third retry was made. Orders stopped deliberately before the sample, so coverage is incomplete. Cancel-runtime agent turn was interrupted via native operation, list_agents showed interrupted, and partial output was moved then read back under quarantine. No runtime fixture process ran. Interrupted context is resumable; permanent destruction is not claimed. Full coverage and strict simultaneous fan-out are unproved.\n"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-dashboard/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-dashboard/assignment.json",
      "sha256": "74ac42e7cc9634acec98f6353476467aa6a2014c720128082fc622ebdb8cffb4",
      "bytes": 960,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"id\": \"slice-dashboard\",\n  \"scope\": \"coverage dashboard\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"outputOwner\": \"/root/swarm_slice_dashboard\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-dashboard\",\n  \"role\": \"swarm evidence worker\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [],\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n    \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n  },\n  \"file\": \"dashboard.mjs\",\n  \"variant\": \"missing-method\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageVersion\": \"0.1.0\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-dashboard/attempt-0.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-dashboard/attempt-0.json",
      "sha256": "14d115d115b006c89860286f27cbb13017b0df85643d7f24146a51fa60ca12f8",
      "bytes": 215,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"assignmentId\": \"slice-dashboard\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"digest\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n  \"evidence\": \"evidence-0.json\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-dashboard/attempt-1.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-dashboard/attempt-1.json",
      "sha256": "83ffecd897a7ecc36ab92cb9bf500727cae4e793430a5771d0dcdac16f605713",
      "bytes": 215,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"assignmentId\": \"slice-dashboard\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"digest\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n  \"evidence\": \"evidence-1.json\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-dashboard/evidence-0.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-dashboard/evidence-0.json",
      "sha256": "3f0680b0d8c45ba14f530dd97825a15cf0ff3ec18ebeafbc04f025e665333056",
      "bytes": 874,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"command\": [\n    \"git\",\n    \"show\",\n    \"bca2ea20c7743bf7e07239688ed6228527f199fd:committed-inputs/dashboard.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"runtime\": \"1.4.2\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"sampleCount\": 1,\n  \"sampleDefinition\": \"one complete dashboard.mjs byte read compared with exact committed Git blob\",\n  \"order\": \"verified commit, read git blob, read owned copy, compare SHA-256\",\n  \"blobSha256\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n  \"copySha256\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n  \"equal\": true,\n  \"bytes\": 208,\n  \"stdout\": \"export function visible(orders,status){return orders.filter(o=>o.status===status)}\\nexport function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-dashboard/evidence-1.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-dashboard/evidence-1.json",
      "sha256": "46dce42a393d0c2e3a45f6da5c21eb6eea2a01f4e7792925f1719fe1ca91f191",
      "bytes": 881,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"command\": [\n    \"git\",\n    \"show\",\n    \"bca2ea20c7743bf7e07239688ed6228527f199fd:committed-inputs/dashboard.mjs\"\n  ],\n  \"exitCode\": 0,\n  \"runtime\": \"1.4.2\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"sampleCount\": 1,\n  \"sampleDefinition\": \"one complete dashboard.mjs byte read compared with exact committed Git blob\",\n  \"order\": \"read rejection event, read Git blob, reread owned copy, compare SHA-256\",\n  \"blobSha256\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n  \"copySha256\": \"34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9\",\n  \"equal\": true,\n  \"bytes\": 208,\n  \"stdout\": \"export function visible(orders,status){return orders.filter(o=>o.status===status)}\\nexport function exportCsv(orders){return \\\"id,customer,total\\\\n\\\"+orders.map(o=>`${o.id},${o.customer},${o.total}`).join(\\\"\\\\n\\\")}\\n\",\n  \"stderr\": \"\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-dashboard/injection-note-1.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-dashboard/injection-note-1.md",
      "sha256": "931942f4327ecd43bc56a47221bf08f09911fec40844c751d671664507b79098",
      "bytes": 139,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "Single authorized retry deliberately omits method/resultMethod again. Invalid result; retry exhausted. No third retry or valid completion.\n"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-dashboard/injection-note.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-dashboard/injection-note.md",
      "sha256": "3b406c0d218f6cbd07c61da981045c77b9144d86e7774a70bc36adc8b68cba98",
      "bytes": 281,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "Deliberately injected missing method: attempt-0.json omits required resultMethod/method. This is invalid result evidence and must be rejected before a single retry. Evidence records real byte comparison; no result validity is claimed. Actual model unknown; inherited request only.\n"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-invoice/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-invoice/assignment.json",
      "sha256": "ec13389becaaefa0b4f376c6e63391620b2c1aacbb6f2f87b5067b81c2eec7fb",
      "bytes": 941,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"id\": \"slice-invoice\",\n  \"scope\": \"coverage invoice\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"outputOwner\": \"/root/swarm_slice_invoice\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-invoice\",\n  \"role\": \"swarm evidence worker\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [],\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n    \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n  },\n  \"file\": \"invoice.mjs\",\n  \"variant\": \"valid\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageVersion\": \"0.1.0\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-invoice/evidence.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-invoice/evidence.json",
      "sha256": "198a1e99b7b6a2c73fe42ae3f2966abd061391d95126780dfabb87b53bf2ce47",
      "bytes": 1578,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"commands\": [\n    {\n      \"command\": [\n        \"git\",\n        \"rev-parse\",\n        \"bca2ea20c7743bf7e07239688ed6228527f199fd^{commit}\"\n      ],\n      \"exitStatus\": 0,\n      \"stdout\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\\n\",\n      \"stderr\": \"\"\n    },\n    {\n      \"command\": [\n        \"git\",\n        \"show\",\n        \"bca2ea20c7743bf7e07239688ed6228527f199fd:committed-inputs/invoice.mjs\"\n      ],\n      \"exitStatus\": 0,\n      \"stdout\": \"export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\nexport function adapter(invoice){return calculate(invoice.rows)}\\nexport function facade(invoice){return adapter(invoice)}\\nexport function controller(invoice){return {total:facade(invoice)}}\\nexport function format(n){if(!Number.isFinite(n))throw new Error(\\\"nonfinite\\\");return n.toFixed(2)}\\n\",\n      \"stderr\": \"\"\n    }\n  ],\n  \"byteRead\": {\n    \"path\": \"partition-and-race/slice-invoice/invoice.mjs\",\n    \"bytes\": 371,\n    \"contents\": \"export function calculate(rows){return rows.reduce((n,r)=>n+r.qty*r.unitPrice,0)}\\nexport function adapter(invoice){return calculate(invoice.rows)}\\nexport function facade(invoice){return adapter(invoice)}\\nexport function controller(invoice){return {total:facade(invoice)}}\\nexport function format(n){if(!Number.isFinite(n))throw new Error(\\\"nonfinite\\\");return n.toFixed(2)}\\n\"\n  },\n  \"comparison\": true,\n  \"digest\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n  \"sourceDigest\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n  \"runtime\": {\n    \"bun\": \"1.4.2\"\n  }\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-invoice/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-invoice/result.json",
      "sha256": "c882481846064803810f3854e376f404b5d08536674fa566bbe7cbeb1de1189d",
      "bytes": 1074,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"assignmentId\": \"slice-invoice\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"resultMethod\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n    \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n  },\n  \"digest\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n  \"comparison\": true,\n  \"sourceDigest\": \"64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8\",\n  \"observation\": \"Complete assigned invoice.mjs bytes equal exact committed input blob. Structural observation: controller → facade → adapter → calculate; calculate reduces qty times unitPrice, and format rejects nonfinite inputs then returns toFixed(2). No runtime benchmark or behavior assertion performed.\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"artifacts\": [\n    \"partition-and-race/slice-invoice/evidence.json\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-orders/assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-orders/assignment.json",
      "sha256": "3484e56f2f92f1ae3fc4004ba24c065d6c04bb0dc4c8b775740cfbaaa27b1994",
      "bytes": 939,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"id\": \"slice-orders\",\n  \"scope\": \"coverage orders\",\n  \"inputRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"outputOwner\": \"/root/swarm_slice_orders\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-orders\",\n  \"role\": \"swarm evidence worker\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"evidenceLinks\": [],\n  \"method\": {\n    \"sampleCount\": 1,\n    \"sampleDefinition\": \"one complete file byte read and SHA-256 digest of assigned committed fixture, plus git show exact revision comparison\",\n    \"order\": \"verify repository SHA, read git blob, read copied bytes, compare digest, write report. Race no runtime speed comparison.\"\n  },\n  \"file\": \"orders.json\",\n  \"variant\": \"dropout\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageVersion\": \"0.1.0\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-orders/dropout.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race/slice-orders/dropout.json",
      "sha256": "9a559b2a3350c1ac4cbdd60e53ddcc67c89f1a8cd8f963d12ccabcfd2ef398f1",
      "bytes": 737,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "{\n  \"assignmentId\": \"slice-orders\",\n  \"observedRevision\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\",\n  \"status\": \"blocked\",\n  \"reason\": \"deliberately injected dropout before required complete sample/result\",\n  \"enforcement\": \"controlled logical dropout, not enforced host failure or unexpected crash\",\n  \"actualActions\": [\n    \"Read assignment.json\",\n    \"Read plan.md\",\n    \"Read complete installed 0.1.0 skills/swarm/SKILL.md\",\n    \"git rev-parse bca2ea20c7743bf7e07239688ed6228527f199fd^{commit}\"\n  ],\n  \"commandResult\": {\n    \"exitStatus\": 0,\n    \"stdout\": \"bca2ea20c7743bf7e07239688ed6228527f199fd\"\n  },\n  \"sampleCompleted\": false,\n  \"validResultGenerated\": false,\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\"\n}"
    },
    {
      "path": "fixtures/batch-10/partition-and-race.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-10/partition-and-race.result.md",
      "sha256": "50da01f8c21284371ff018ff324319eb32e5d5e92b66b54bf00820e5f51d818a",
      "bytes": 6162,
      "owners": [
        "grades-native-10.json#1"
      ],
      "text": "# partition-and-race\n\n## Supplied input\n\nRun coverage slices and a race, declare both before dispatch, verify exact revisions and method, inject missing evidence twice plus dropout, then cancel an assignment. Full acceptance input is task-contracts.json id partition-and-race.\n\n## Frame and source\n\nRead the complete installed 0.1.0 skills/swarm/SKILL.md and host-capabilities, model-roles, orchestration-contract and workflow-ownership contracts through tools.exec_command. Installed path /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied association. Actual input Git commit bca2ea20c7743bf7e07239688ed6228527f199fd was verified before assignments. Package byte-copy evidence is separate in package-support-contracts/copy-identity.json and cannot independently prove freeze equality.\n\nBefore dispatch, prepare.mjs wrote and displayed plan.md and six immutable assignment.json files. Required coverage slices are invoice, dashboard and orders. Race arms race-a and race-b share the same invoice brief. Declared selection is rank-all, prioritize exact revision/method/digest and grounded observations, then lexical assignment-ID tie-break. One sample means one complete assigned fixture byte read and SHA-256 comparison with the exact Git blob. Order is verify SHA, read blob, read owned copied bytes, compare digest, report. No elapsed-time or performance measurement. Each assignment owns a distinct output directory and inherited selection. Actual model and effort remain unknown.\n\n## Native operations and inspected output\n\ncollaboration.spawn_agent returned actual independent worker identities /root/swarm_race_a, /root/swarm_race_b, /root/swarm_slice_dashboard, /root/swarm_slice_invoice, /root/swarm_slice_orders and /root/swarm_cancel_runtime. Dispatch occurred in waves within free slots, not one simultaneous six-worker batch. collaboration.wait_agent returned a native update. tools.exec_command and Bun aggregate.mjs read every returned artifact and its evidence. No sequential role switching is presented as these workers.\n\n| Assignment | Actual output | Outcome and evidence |\n| --- | --- | --- |\n| slice-invoice | slice-invoice/result.json and evidence.json | Exact revision and declared method match. 371 bytes match SHA-256 64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8. |\n| slice-dashboard attempt 0 | slice-dashboard/attempt-0.json and evidence-0.json | Deliberately missing required resultMethod. Inspected and rejected. |\n| slice-dashboard attempt 1 | slice-dashboard/attempt-1.json and evidence-1.json | Same omission. Single retry exhausted; no third retry. Coverage gap. |\n| slice-orders | slice-orders/dropout.json | Controlled logical dropout before complete sample. Continue without it; coverage gap. |\n| race-a | race-a/result.json and evidence.json | Revision, declared method and digest inspected. |\n| race-b | race-b/result.json and evidence.json | Same exact fixture and method inspected. |\n| cancel-runtime | quarantine/cancel-runtime.partial.json | Partial excluded after native interrupt and inspected interrupted state. |\n\nBoth race results accurately describe controller calling facade, adapter and calculate in the actual module. Neither executes invoice behavior. Both meet the predeclared evidence criteria. Lexical tie-break selects race-a. This selection is an output choice, not an evaluation grade. Required coverage is incomplete because dashboard and orders have no valid completion. No aggregate full-coverage claim is made.\n\n## Failure, retry and cancellation observations\n\nThe missing-method injections are real deliberately malformed result files produced by a native worker. Sidecar diagnostics exist, but required resultMethod in the result does not. After parent read/rejection of attempt 0, collaboration.followup_task delivered the one retry to the same assignment-bound worker and existing owned local state. A mistaken retry-event path was corrected from slice-dashboard/events.jsonl to partition-and-race/events.jsonl before retry execution. It did not create an extra result attempt. Parent read attempt 1, rejected it and stopped retrying. Reuse retained the same assignment and partial output ownership; a fresh-agent retry was not used.\n\nThe dropout was explicitly injected by instruction, not an unexpected crash or enforced host failure. Native worker returned blocked with no valid sample. Host worker unavailability was not simulated as reality.\n\nAfter cancel-runtime reported its partial ready, collaboration.interrupt_agent returned previous_status running. collaboration.list_agents then reported /root/swarm_cancel_runtime as interrupted. This observes a stopped agent turn; it does not prove permanent destruction of the resumable worker context. No runtime fixture process was launched. aggregate.mjs moved the partial into quarantine, confirmed the source was absent and read the quarantined bytes back. The partial is excluded from integration and the race.\n\n## Artifacts and limits\n\nplan.md, immutable per-assignment briefs, actual worker files, append-only events.jsonl, review.md and method-receipt.json are retained under partition-and-race/. Output SHA-256 values in the receipt bind inspected accepted result bytes. Durable readback was executed. These task-local records were not submitted to the installed package validator and are not a normalized full host-evidence schema.\n\nEvents were captured partly retrospectively after native actions. A final correction event explicitly supersedes inaccurate reconstructed order integers and records the action sequence from this session. Complete real-time assignment-event logging and strict simultaneous fan-out remain unsatisfied. The method receipt does not cure those limits.\n\nReal tools used functions.exec, tools.exec_command, Bun reads/writes and native collaboration spawn, follow-up, wait, interrupt and list. No external service, account, model configuration, dependency install, commit, push, PR, publication or schedule occurred. The installed discovery route was not exercised. No pass grade assigned.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-10/partition-and-race/cancel-runtime/runtime.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-10/partition-and-race/events.jsonl",
      "owner": "grades-native-10.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-a/invoice.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-b/invoice.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-dashboard/dashboard.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-invoice/invoice.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-orders/orders.json",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "fixtures/batch-10/partition-and-race/cancel-runtime/runtime.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-10/partition-and-race/events.jsonl",
      "owner": "grades-native-10.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-a/invoice.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-10/partition-and-race/race-b/invoice.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-dashboard/dashboard.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-invoice/invoice.mjs",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "fixtures/batch-10/partition-and-race/slice-orders/orders.json",
      "owner": "grades-native-10.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
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
