# codex: swarm-walkthrough

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "swarm-walkthrough",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-11.json#4",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Start with an authorized disposable local artifact and exact input SHA. Follow README to Swarm and partition a three-file source review.",
  "caseDefinition": {
    "id": "swarm-walkthrough",
    "sourcePaths": [
      "skills/swarm/SKILL.md"
    ],
    "prompt": "Start with an authorized disposable local artifact and exact input SHA. Follow README to Swarm and partition a three-file source review.",
    "requirements": [
      "Starting state and exact action are in the prompt. README must link docs/workflows/swarm.md and the destination must exist.",
      "Read the full linked workflow and required contracts before dependent work.",
      "Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.",
      "Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.",
      "Declare partition/race/mixed shape, N and first pass/rank all/best-of when relevant before dispatch. Include full SHA and method; reject incomplete results, allow at most one inspected retry and retain uncovered slices as gaps."
    ],
    "expectedFull": "Three independent authorized slice results cover the three fixture files at the exact SHA and method. The coordinator inspects terminal artifacts and returns one consolidated table with evidenced issues and explicit gaps/dropouts. Cancellation requires observed stop, terminal inspection and quarantine.",
    "expectedReduced": "Sequential review of the declared three-file partition may return reduced findings with exact revisions, inspected artifacts and visible missing slices. It proves neither independent workers nor a race.",
    "expectedBlocked": "Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.",
    "forbiddenClaims": [
      "Links or direct source reads prove installed discovery.",
      "Sequential roles are independent workers.",
      "An isolated helper snapshot proves this candidate or host passed.",
      "A resolution file, owner marker or upstream autonomy grants approval.",
      "Apply automatically accepts an update or refreshes a host."
    ],
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json"
  },
  "registry": {
    "caseId": "swarm-walkthrough",
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json",
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
    "requiredMethod": "swarm-partition",
    "requiredSliceCount": 3
  },
  "attempts": [
    {
      "attemptId": "grades-native-11.json#4",
      "order": 0,
      "gradeFile": "grades-native-11.json",
      "rankWithinFile": 4,
      "host": "codex",
      "caseId": "swarm-walkthrough",
      "status": "reduced-pass",
      "grade": {
        "caseId": "swarm-walkthrough",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "review-outcome"
        ],
        "missing": [
          "Conforming swarm-partition method receipt and correctly attributed output production operations",
          "Fresh installed-loading observation"
        ],
        "review": "Three actual exact-revision read-only slice workers and inspected complete results cover all three sources. The saved receipt is not the strict accepted shape (extra assignment fields/noncanonical role values), and its output files were parent captures rather than assignment-bound worker writes. No invented isolated-write operation is credited merely to satisfy requiredMethod.",
        "responseArtifact": "fixtures/batch-11/swarm-walkthrough.result.md",
        "rawTrace": "codex/batch-11.events.jsonl",
        "actualCommandEventIds": [
          "item_5",
          "item_7",
          "item_9",
          "item_10",
          "item_11",
          "item_13",
          "item_14",
          "item_15",
          "item_16",
          "item_17",
          "item_25",
          "item_26",
          "item_27",
          "item_30",
          "item_31",
          "item_40"
        ],
        "nativeMethodReceipts": "native-10-11-tool-receipts.json",
        "variantReview": {
          "assessment": "Complete case response and explicit real/simulated/unrun branches inspected. Source-only negative views do not prove actual host capability removal or denial. Fixed-input gaps are not plugin bugs.",
          "sectionPresent": true
        },
        "limits": [
          "Baseline observations only; source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c remains distinct from actual fixture task revisions and new candidate source.",
          "Native parent/child persisted custom-tool and collaboration records independently inspected; protected dispatch message ciphertext omitted.",
          "Independent child turn_context records now establish gpt-6.1-sol for recovered10/11 sessions. This observation was unavailable to in-run workers and establishes no model-family diversity.",
          "Parent-captured read-only responses are not fabricated worker file-write operations. Proxy guards, local receipt shape checks and scenario metadata do not establish missing full method support."
        ],
        "reviewedBy": "review_workflow_evidence independent full-response/native parent-child rollout review",
        "fullExpected": "Three independent authorized slice results cover the three fixture files at the exact SHA and method. The coordinator inspects terminal artifacts and returns one consolidated table with evidenced issues and explicit gaps/dropouts. Cancellation requires observed stop, terminal inspection and quarantine.",
        "reducedExpected": "Sequential review of the declared three-file partition may return reduced findings with exact revisions, inspected artifacts and visible missing slices. It proves neither independent workers nor a race.",
        "concreteFixCandidates": []
      },
      "topLevelContext": {
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c"
      },
      "response": {
        "text": "# swarm-walkthrough\n\nThree independently dispatched reviewers covered the three declared source slices. I inspected each terminal result, its exact input SHA, method, cited code and byte-identity evidence. This is a source review, not a host acceptance grade or runtime correctness result.\n\nSupplied prompt and complete contract are in swarm-walkthrough/supplied-input.json. Input Git revision was independently verified as 69a848296f870402cb15b85e93dff671fa32059d before worker assignment. Copied inputs are under swarm-walkthrough/input. The package source freeze supplied by the user is f4623636a287bea2aa79c4b2234a53d20a5f193c, distinct from that input revision. plugin.json reports 0.1.0. The installed package has no .git, so package-manifest.json identifies observed bytes without claiming independently established package commit identity.\n\nThe actual installed README links docs/workflows/swarm.md and the destination exists. I read the full linked workflow, Swarm skill, host capabilities, model roles, orchestration and workflow-ownership contracts before dispatch. Direct path reads were successful. The 0.1.0 package is not in the host's supplied skill catalog, which lists a separate version. No registered discovery or fresh host loading was exercised, so installed discovery remains unverified. No install or settings change was attempted.\n\nFrame, Fan out, Aggregate and Report phases are in swarm-walkthrough/phases.md. Declared shape was partition, N=3. A race selection rule is not applicable. Immutable assignment records were written and read before dispatch in swarm-walkthrough/assignments.json, each with a disjoint capture path and exact revision. Each method was one complete source read and import/caller check, in source/context/findings order. Three independent collaboration.spawn_agent operations returned /root/swarm_slice_1, /root/swarm_slice_2 and /root/swarm_slice_3. The first slice ran while other case owners used remaining slots. Slices 2 and 3 ran together after slots freed. This was capacity-bounded dispatch, not one simultaneous three-worker launch.\n\n| Slice | Inspected terminal artifact | Findings and limits |\n| --- | --- | --- |\n| controller.mjs | swarm-walkthrough/results/slice-1.md | No proven defect. Passes invoice through facade and wraps numeric total. Upstream validation contract absent. |\n| adapter.mjs | swarm-walkthrough/results/slice-2.md | No proven defect. Existing calculate export receives invoice.rows. No unresolved import found. |\n| calculator.mjs | swarm-walkthrough/results/slice-3.md | No proven defect. Reduces quantity times unit price and preserves observable latest-total state required by decision.md. |\n\nPASS appears only as the package-required worker source-review label. It is not my grade of this evaluation. Every reviewer recorded the full input SHA and exact method. No result was rejected, retried, cancelled or quarantined. No slice was uncovered. Assignment scopes and input revision did not change. The parent captured read-only worker responses to distinct artifacts and computed hashes in the method receipt. No independent worker write is claimed.\n\nActual tools were functions.exec with tools.exec_command for file/Git/Bun reads, tools.apply_patch for local parent-owned artifacts, and collaboration.spawn_agent with terminal returned messages for workers and inspection. Requested models and efforts were inherit-parent. Actual models and efforts were not exposed, so no model diversity is claimed. Source equality was checked through git show and byte comparisons or Git blob identity, not inferred from branch names.\n\nThe method receipt retains assignments, dispatch/completion order, inspected result hashes, report paths and source read method. Local persistence was read back. No separate inspect-method API exists; the actual operation is Bun reading the receipt through exec_command, retained in final-checks.json. No background/cloud branch binding, installer, host registration, production behavior, cancellation or automatic pickup is established.\n\nNo negative capability variants were requested. No external account writes, real issues, PRs, messages, commits, pushes, publishing, configuration changes, installs or schedules occurred. Only the supplied package root was read for instructions. No personal context was used.\n",
        "artifact": {
          "path": "fixtures/batch-11/swarm-walkthrough.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/swarm-walkthrough.result.md",
          "sha256": "b143e971f8528260627f7bb4eaa012d5a1dddb0e3bbbe0365b2834d9f8911e4d",
          "bytes": 4327
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-11.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-11.events.jsonl",
            "sha256": "d9eb5e472194d4af6018e565f347cd441fc759312bcf941a390e1931e80193c4",
            "bytes": 434933,
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
      "path": "fixtures/batch-11/swarm-walkthrough/assignments.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/swarm-walkthrough/assignments.json",
      "sha256": "cd026b80ecdb897899372b90d2c1f1628c418d3ab0acc43f482e1eb8442abf6f",
      "bytes": 2261,
      "owners": [
        "grades-native-11.json#4"
      ],
      "text": "[\n  {\n    \"id\": \"slice-1\",\n    \"scope\": \"read-only review of committed-inputs/additional/invoice/controller.mjs\",\n    \"inputRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n    \"outputOwner\": \"swarm_slice_1\",\n    \"isolatedOutputPath\": \"swarm-walkthrough/results/slice-1.md\",\n    \"role\": \"swarm source reviewer\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"committed-inputs/additional/invoice/controller.mjs\"\n    ],\n    \"method\": {\n      \"sampleCount\": 1,\n      \"sampleDefinition\": \"one full source read and import/caller check at the frozen input revision\",\n      \"order\": \"source read, caller/import context, evidenced findings\"\n    },\n    \"requestedModel\": \"inherit-parent\",\n    \"actualModel\": \"unknown\"\n  },\n  {\n    \"id\": \"slice-2\",\n    \"scope\": \"read-only review of committed-inputs/additional/invoice/adapter.mjs\",\n    \"inputRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n    \"outputOwner\": \"swarm_slice_2\",\n    \"isolatedOutputPath\": \"swarm-walkthrough/results/slice-2.md\",\n    \"role\": \"swarm source reviewer\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"committed-inputs/additional/invoice/adapter.mjs\"\n    ],\n    \"method\": {\n      \"sampleCount\": 1,\n      \"sampleDefinition\": \"one full source read and import/caller check at the frozen input revision\",\n      \"order\": \"source read, caller/import context, evidenced findings\"\n    },\n    \"requestedModel\": \"inherit-parent\",\n    \"actualModel\": \"unknown\"\n  },\n  {\n    \"id\": \"slice-3\",\n    \"scope\": \"read-only review of committed-inputs/additional/invoice/calculator.mjs\",\n    \"inputRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n    \"outputOwner\": \"swarm_slice_3\",\n    \"isolatedOutputPath\": \"swarm-walkthrough/results/slice-3.md\",\n    \"role\": \"swarm source reviewer\",\n    \"retryCount\": 0,\n    \"terminalStatus\": \"pending\",\n    \"evidenceLinks\": [\n      \"committed-inputs/additional/invoice/calculator.mjs\"\n    ],\n    \"method\": {\n      \"sampleCount\": 1,\n      \"sampleDefinition\": \"one full source read and import/caller check at the frozen input revision\",\n      \"order\": \"source read, caller/import context, evidenced findings\"\n    },\n    \"requestedModel\": \"inherit-parent\",\n    \"actualModel\": \"unknown\"\n  }\n]"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/method-receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/swarm-walkthrough/method-receipt.json",
      "sha256": "87f917f0871ff00f2f86818c2b74b63964e55365f516902ff9c02ca4954945f1",
      "bytes": 5448,
      "owners": [
        "grades-native-11.json#4"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"kind\": \"swarm\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageCommitVerification\": \"supplied only; exact read-byte identities in package-manifest.json\",\n  \"inputRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n  \"declaredOrder\": 1,\n  \"assignments\": [\n    {\n      \"id\": \"slice-1\",\n      \"scope\": \"read-only review of committed-inputs/additional/invoice/controller.mjs\",\n      \"inputRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n      \"outputOwner\": \"/root/swarm_slice_1\",\n      \"isolatedOutputPath\": \"swarm-walkthrough/results/slice-1.md\",\n      \"role\": \"swarm source reviewer\",\n      \"retryCount\": 0,\n      \"terminalStatus\": \"pending\",\n      \"evidenceLinks\": [\n        \"committed-inputs/additional/invoice/controller.mjs\"\n      ],\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one full source read and import/caller check at the frozen input revision\",\n        \"order\": \"source read, caller/import context, evidenced findings\"\n      },\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"workerId\": \"/root/swarm_slice_1\",\n      \"outputPath\": \"swarm-walkthrough/results/slice-1.md\",\n      \"status\": \"completed\",\n      \"startedOrder\": 2,\n      \"completedOrder\": 3,\n      \"taskArtifact\": \"swarm-walkthrough/assignments.json\",\n      \"rubricProvided\": true,\n      \"resultRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one full source read and import/caller check at the frozen input revision\",\n        \"order\": \"source read, caller/import context, evidenced findings\"\n      },\n      \"outputSha256\": \"f3ddf2d865403350e2dad3949ad57489ef5d7c391e30d6f366bc514cf3164038\"\n    },\n    {\n      \"id\": \"slice-2\",\n      \"scope\": \"read-only review of committed-inputs/additional/invoice/adapter.mjs\",\n      \"inputRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n      \"outputOwner\": \"/root/swarm_slice_2\",\n      \"isolatedOutputPath\": \"swarm-walkthrough/results/slice-2.md\",\n      \"role\": \"swarm source reviewer\",\n      \"retryCount\": 0,\n      \"terminalStatus\": \"pending\",\n      \"evidenceLinks\": [\n        \"committed-inputs/additional/invoice/adapter.mjs\"\n      ],\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one full source read and import/caller check at the frozen input revision\",\n        \"order\": \"source read, caller/import context, evidenced findings\"\n      },\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"workerId\": \"/root/swarm_slice_2\",\n      \"outputPath\": \"swarm-walkthrough/results/slice-2.md\",\n      \"status\": \"completed\",\n      \"startedOrder\": 4,\n      \"completedOrder\": 6,\n      \"taskArtifact\": \"swarm-walkthrough/assignments.json\",\n      \"rubricProvided\": true,\n      \"resultRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one full source read and import/caller check at the frozen input revision\",\n        \"order\": \"source read, caller/import context, evidenced findings\"\n      },\n      \"outputSha256\": \"659e670e304e80bf2221ce1ce69ce8c01491e7e1a9286c728d06f8fc54cd437e\"\n    },\n    {\n      \"id\": \"slice-3\",\n      \"scope\": \"read-only review of committed-inputs/additional/invoice/calculator.mjs\",\n      \"inputRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n      \"outputOwner\": \"/root/swarm_slice_3\",\n      \"isolatedOutputPath\": \"swarm-walkthrough/results/slice-3.md\",\n      \"role\": \"swarm source reviewer\",\n      \"retryCount\": 0,\n      \"terminalStatus\": \"pending\",\n      \"evidenceLinks\": [\n        \"committed-inputs/additional/invoice/calculator.mjs\"\n      ],\n      \"method\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one full source read and import/caller check at the frozen input revision\",\n        \"order\": \"source read, caller/import context, evidenced findings\"\n      },\n      \"requestedModel\": \"inherit-parent\",\n      \"actualModel\": \"unknown\",\n      \"workerId\": \"/root/swarm_slice_3\",\n      \"outputPath\": \"swarm-walkthrough/results/slice-3.md\",\n      \"status\": \"completed\",\n      \"startedOrder\": 5,\n      \"completedOrder\": 7,\n      \"taskArtifact\": \"swarm-walkthrough/assignments.json\",\n      \"rubricProvided\": true,\n      \"resultRevision\": \"69a848296f870402cb15b85e93dff671fa32059d\",\n      \"resultMethod\": {\n        \"sampleCount\": 1,\n        \"sampleDefinition\": \"one full source read and import/caller check at the frozen input revision\",\n        \"order\": \"source read, caller/import context, evidenced findings\"\n      },\n      \"outputSha256\": \"7e21b2a817a318dcb89268a40ffba721b4077670d22c2759af5083237d53b563\"\n    }\n  ],\n  \"reviewArtifact\": \"swarm-walkthrough.result.md\",\n  \"reviewedBy\": \"/root\",\n  \"partition\": {\n    \"requiredSlices\": [\n      \"controller.mjs\",\n      \"adapter.mjs\",\n      \"calculator.mjs\"\n    ],\n    \"results\": {\n      \"controller.mjs\": \"slice-1\",\n      \"adapter.mjs\": \"slice-2\",\n      \"calculator.mjs\": \"slice-3\"\n    },\n    \"gaps\": []\n  },\n  \"race\": null,\n  \"cancelled\": [],\n  \"quarantined\": [],\n  \"failureExercises\": [],\n  \"limits\": [\n    \"Read-only workers returned native messages; parent captured summaries to distinct artifacts.\",\n    \"No model identity observed.\",\n    \"Capacity-bound dispatch; not all three launched simultaneously.\",\n    \"This is a method record, not an acceptance grade or registered-discovery receipt.\"\n  ]\n}"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/phases.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/swarm-walkthrough/phases.md",
      "sha256": "5ac4f5cac0cb8ceed71dcf2ce786694ab8c3bda5393d3e0a56b508c8df71dce5",
      "bytes": 387,
      "owners": [
        "grades-native-11.json#4"
      ],
      "text": "1. Frame. Done predicate is three inspected results at the exact input revision. Partition shape, N=3. No race selection rule applies.\n2. Fan out. Three disjoint read-only slices. Parent captures returned artifacts.\n3. Aggregate. Inspect identity, SHA, method, evidence and output digest. Reject incomplete outputs, at most one inspected retry.\n4. Report. Consolidate findings and gaps.\n"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/results/slice-1.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/swarm-walkthrough/results/slice-1.md",
      "sha256": "f3ddf2d865403350e2dad3949ad57489ef5d7c391e30d6f366bc514cf3164038",
      "bytes": 1601,
      "owners": [
        "grades-native-11.json#4"
      ],
      "text": "PASS: no proven defect in assigned controller scope from this source review.\n\nAssignment slice-1. Worker /root/swarm_slice_1. Input revision 69a848296f870402cb15b85e93dff671fa32059d.\n\nMethod sampleCount 1. sampleDefinition one full source read and import/caller check at the frozen input revision. order source read, caller/import context, evidenced findings.\n\nRequested model inherit-parent. Actual model unknown. Shape partition, N=3. Covers slice-1 only.\n\ncommitted-inputs/additional/invoice/controller.mjs:1 imports the existing named invoiceFacade export from facade.mjs. Line 2 passes its input through and returns { total: ... }. Frozen downstream source establishes invoiceFacade to invoiceAdapter to calculate(invoice.rows). Scoped caller search found no controller callers beyond its definition. Upstream validation and consumer expectations remain unknown.\n\nFiles read at frozen revision were controller.mjs, facade.mjs, adapter.mjs, calculator.mjs, decision.md, installed 0.1.0 Swarm skill and four assigned support contracts, and assignment record. The decision record's formatting requirements do not establish that this controller must format its numeric total.\n\nObserved git show exited 0. Bun compared frozen controller bytes to working-copy bytes and returned equal true. Controller SHA-256 90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862.\n\nNo runtime execution, tests, writes, services, git mutations or external actions occurred. PASS is a source-review report label, not an evaluation grade or runtime correctness claim. Parent captured the returned result here.\n"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/results/slice-2.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/swarm-walkthrough/results/slice-2.md",
      "sha256": "659e670e304e80bf2221ce1ce69ce8c01491e7e1a9286c728d06f8fc54cd437e",
      "bytes": 1786,
      "owners": [
        "grades-native-11.json#4"
      ],
      "text": "PASS, scoped source review only. No proven issue in assigned adapter slice.\n\nAssignment slice-2. Worker /root/swarm_slice_2. Input revision 69a848296f870402cb15b85e93dff671fa32059d. Partition N=3, not a race.\n\nMethod sampleCount 1. sampleDefinition one full source read and import/caller check at the frozen input revision. order source read, caller/import context, evidenced findings. Requested model inherit-parent. Actual model and effort unknown.\n\ncommitted-inputs/additional/invoice/adapter.mjs:1 imports the existing calculate export from calculator.mjs:2. adapter.mjs:2 passes invoice.rows and returns the result. facade.mjs:1-2 calls invoiceAdapter. controller.mjs:1-2 reaches it through the facade. No unresolved import or changed data shape was found. No input-validation requirement was supplied, so no defect is claimed merely from absent validation.\n\ngit show exited 0 for adapter and all inspected context. Bun compared committed and working bytes, all five matched. SHA-256 values were adapter a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c, facade 6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d, calculator 1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff, controller 90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862, decision 324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee.\n\nFull files read were those five inputs, assignments.json, installed 0.1.0 Swarm skill and all four support contracts. Operations were functions.exec and exec_command for source, rg, git show, numbered adapter read and Bun comparison. No writes, app execution, service, install or git mutation. Parent captured terminal response. This source-review label establishes neither runtime behavior nor host parity.\n"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/results/slice-3.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/swarm-walkthrough/results/slice-3.md",
      "sha256": "7e21b2a817a318dcb89268a40ffba721b4077670d22c2759af5083237d53b563",
      "bytes": 1579,
      "owners": [
        "grades-native-11.json#4"
      ],
      "text": "PASS, source review with no proven defect. This is a worker report label, not a case acceptance grade.\n\nAssignment slice-3. Worker /root/swarm_slice_3. Input revision 69a848296f870402cb15b85e93dff671fa32059d. Shape partition N=3.\n\nMethod sampleCount 1. sampleDefinition one full source read and import/caller check at the frozen input revision. order source read, caller/import context, evidenced findings. Requested model inherit-parent. Actual model unknown.\n\ngit show read committed calculator. git hash-object and committed blob identity both returned 165f88df3f98fde1286768d02e51fd48cc97aeff, so bytes match.\n\ncalculator.mjs:1 stores latest total in module state. decision.md:7 describes that observable state. calculate at line 2 reduces qty * unitPrice from zero on line 3, updates cachedTotal and returns it on line 4. inspectCachedTotal at line 6 exposes the latest value. Scoped symbol search found no repository caller of inspectCachedTotal, which says nothing about external consumers. adapter.mjs:1-2 imports calculate and forwards invoice.rows. Controller and facade add no calculation behavior.\n\nFull files read were installed 0.1.0 Swarm skill, four support contracts, assignments.json, frozen calculator, adapter, controller, facade and decision, and current calculator. Tools were functions.exec with exec_command, git show, hash-object, rev-parse, cat, nl and rg. Observed commands exited 0. No file writes, fixture execution, services, dependencies or Git mutations. Runtime correctness and model diversity remain unverified. Parent captured terminal report.\n"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/swarm-walkthrough/supplied-input.json",
      "sha256": "8160fc7106fb9f8f8fc8a962d233cf917cae410ea16da66d41d7cd325ae4f5b6",
      "bytes": 2263,
      "owners": [
        "grades-native-11.json#4"
      ],
      "text": "{\n  \"id\": \"swarm-walkthrough\",\n  \"sourcePaths\": [\n    \"skills/swarm/SKILL.md\"\n  ],\n  \"prompt\": \"Start with an authorized disposable local artifact and exact input SHA. Follow README to Swarm and partition a three-file source review.\",\n  \"requirements\": [\n    \"Starting state and exact action are in the prompt. README must link docs/workflows/swarm.md and the destination must exist.\",\n    \"Read the full linked workflow and required contracts before dependent work.\",\n    \"Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.\",\n    \"Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery.\",\n    \"Declare partition/race/mixed shape, N and first pass/rank all/best-of when relevant before dispatch. Include full SHA and method; reject incomplete results, allow at most one inspected retry and retain uncovered slices as gaps.\"\n  ],\n  \"expectedFull\": \"Three independent authorized slice results cover the three fixture files at the exact SHA and method. The coordinator inspects terminal artifacts and returns one consolidated table with evidenced issues and explicit gaps/dropouts. Cancellation requires observed stop, terminal inspection and quarantine.\",\n  \"expectedReduced\": \"Sequential review of the declared three-file partition may return reduced findings with exact revisions, inspected artifacts and visible missing slices. It proves neither independent workers nor a race.\",\n  \"expectedBlocked\": \"Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.\",\n  \"forbiddenClaims\": [\n    \"Links or direct source reads prove installed discovery.\",\n    \"Sequential roles are independent workers.\",\n    \"An isolated helper snapshot proves this candidate or host passed.\",\n    \"A resolution file, owner marker or upstream autonomy grants approval.\",\n    \"Apply automatically accepts an update or refreshes a host.\"\n  ],\n  \"caseFile\": \"docs/parity/cases/documentation-walkthroughs.json\"\n}"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-11/swarm-walkthrough.result.md",
      "sha256": "b143e971f8528260627f7bb4eaa012d5a1dddb0e3bbbe0365b2834d9f8911e4d",
      "bytes": 4327,
      "owners": [
        "grades-native-11.json#4"
      ],
      "text": "# swarm-walkthrough\n\nThree independently dispatched reviewers covered the three declared source slices. I inspected each terminal result, its exact input SHA, method, cited code and byte-identity evidence. This is a source review, not a host acceptance grade or runtime correctness result.\n\nSupplied prompt and complete contract are in swarm-walkthrough/supplied-input.json. Input Git revision was independently verified as 69a848296f870402cb15b85e93dff671fa32059d before worker assignment. Copied inputs are under swarm-walkthrough/input. The package source freeze supplied by the user is f4623636a287bea2aa79c4b2234a53d20a5f193c, distinct from that input revision. plugin.json reports 0.1.0. The installed package has no .git, so package-manifest.json identifies observed bytes without claiming independently established package commit identity.\n\nThe actual installed README links docs/workflows/swarm.md and the destination exists. I read the full linked workflow, Swarm skill, host capabilities, model roles, orchestration and workflow-ownership contracts before dispatch. Direct path reads were successful. The 0.1.0 package is not in the host's supplied skill catalog, which lists a separate version. No registered discovery or fresh host loading was exercised, so installed discovery remains unverified. No install or settings change was attempted.\n\nFrame, Fan out, Aggregate and Report phases are in swarm-walkthrough/phases.md. Declared shape was partition, N=3. A race selection rule is not applicable. Immutable assignment records were written and read before dispatch in swarm-walkthrough/assignments.json, each with a disjoint capture path and exact revision. Each method was one complete source read and import/caller check, in source/context/findings order. Three independent collaboration.spawn_agent operations returned /root/swarm_slice_1, /root/swarm_slice_2 and /root/swarm_slice_3. The first slice ran while other case owners used remaining slots. Slices 2 and 3 ran together after slots freed. This was capacity-bounded dispatch, not one simultaneous three-worker launch.\n\n| Slice | Inspected terminal artifact | Findings and limits |\n| --- | --- | --- |\n| controller.mjs | swarm-walkthrough/results/slice-1.md | No proven defect. Passes invoice through facade and wraps numeric total. Upstream validation contract absent. |\n| adapter.mjs | swarm-walkthrough/results/slice-2.md | No proven defect. Existing calculate export receives invoice.rows. No unresolved import found. |\n| calculator.mjs | swarm-walkthrough/results/slice-3.md | No proven defect. Reduces quantity times unit price and preserves observable latest-total state required by decision.md. |\n\nPASS appears only as the package-required worker source-review label. It is not my grade of this evaluation. Every reviewer recorded the full input SHA and exact method. No result was rejected, retried, cancelled or quarantined. No slice was uncovered. Assignment scopes and input revision did not change. The parent captured read-only worker responses to distinct artifacts and computed hashes in the method receipt. No independent worker write is claimed.\n\nActual tools were functions.exec with tools.exec_command for file/Git/Bun reads, tools.apply_patch for local parent-owned artifacts, and collaboration.spawn_agent with terminal returned messages for workers and inspection. Requested models and efforts were inherit-parent. Actual models and efforts were not exposed, so no model diversity is claimed. Source equality was checked through git show and byte comparisons or Git blob identity, not inferred from branch names.\n\nThe method receipt retains assignments, dispatch/completion order, inspected result hashes, report paths and source read method. Local persistence was read back. No separate inspect-method API exists; the actual operation is Bun reading the receipt through exec_command, retained in final-checks.json. No background/cloud branch binding, installer, host registration, production behavior, cancellation or automatic pickup is established.\n\nNo negative capability variants were requested. No external account writes, real issues, PRs, messages, commits, pushes, publishing, configuration changes, installs or schedules occurred. Only the supplied package root was read for instructions. No personal context was used.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-11/swarm-walkthrough/attempt-events.jsonl",
      "owner": "grades-native-11.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/input",
      "owner": "grades-native-11.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/source-reads.json",
      "owner": "grades-native-11.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/attempt-events.jsonl",
      "owner": "grades-native-11.json#4",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/input",
      "owner": "grades-native-11.json#4",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-11/swarm-walkthrough/source-reads.json",
      "owner": "grades-native-11.json#4",
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
