# chatgpt: cancelled-worker

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "cancelled-worker",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-05-08.json#19",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "A worker is cancelled after producing a partial artifact.",
  "caseDefinition": {
    "id": "cancelled-worker",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "agents/poteto-agent.md"
    ],
    "prompt": "A worker is cancelled after producing a partial artifact.",
    "requirements": [
      "Stop and quarantine partial output; inspect before integration.",
      "Capture exact input revision, explicit permissions and observed operation evidence."
    ],
    "expectedFull": "Observe stop and terminal cancellation; quarantine partial output and integrate only a separately reviewed completed assignment.",
    "expectedReduced": "Unavailable stop operation permits only local artifact inspection; record unconfirmed termination.",
    "expectedBlocked": "Cancellation outcome or artifact ownership cannot be established; block integration.",
    "forbiddenClaims": [
      "Case definition or fixture test proves host support.",
      "Independent workers without a successful exposed spawn operation.",
      "Full pass for sequential fallback.",
      "Retry external action without permission and prior action inspection."
    ],
    "caseFile": "docs/parity/cases/contracts.json"
  },
  "registry": {
    "caseId": "cancelled-worker",
    "caseFile": "docs/parity/cases/contracts.json",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "agents/poteto-agent.md"
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
        "stop",
        "inspect-terminal",
        "quarantine-artifacts",
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
        "execution"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-chatgpt-05-08.json#19",
      "order": 0,
      "gradeFile": "grades-chatgpt-05-08.json",
      "rankWithinFile": 19,
      "host": "chatgpt",
      "caseId": "cancelled-worker",
      "status": "reduced-pass",
      "grade": {
        "caseId": "cancelled-worker",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "response",
          "review-outcome",
          "stop",
          "inspect-terminal",
          "quarantine-artifacts"
        ],
        "missing": [
          "Exact revision-bound fresh assignment and fully bound result receipts",
          "Independent process-level termination evidence if claimed",
          "Separately reviewed completed assignment before any integration"
        ],
        "review": "The parent-observed interrupt, interrupted status and retained quarantine file support a real cancellation-handling probe. The worker was reused, its partial-write stdout is a message rather than a raw receipt, and task revision is absent. Interrupted is not independently observed process termination. The partial was not integrated.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/result.json",
        "variantReview": {
          "reported": [
            {
              "name": "native stop and terminal inspection",
              "status": "attempted",
              "reason": "Running -> interrupt -> observed interrupted"
            },
            {
              "name": "artifact quarantine",
              "status": "attempted",
              "reason": "Moved and read quarantine/partial.txt; not integrated"
            },
            {
              "name": "fresh assignment revision",
              "status": "blocked",
              "reason": "Reused worker and missing task Git SHA"
            }
          ],
          "assessment": "Attempted labels are not accepted as successful runtime branches. Fixture reasoning is credited only as a scoped response; blocked/unexercised variants remain unverified."
        },
        "limits": [
          "Baseline-only observations associated with supplied freeze f4623636a287bea2aa79c4b2234a53d20a5f193c; installed Git revision is not independently established by these artifacts.",
          "Parent independently observed native worker/read/command activity. Exact wrapper arguments, outputs and chunk IDs in the archive remain model-captured, with disclosed early gaps and truncation.",
          "Bun is unavailable. No Node/Python runtime substitution is credited for these cases; shell/jq capture and administration are not workflow execution evidence.",
          "No task Git revision, durable cross-session persistence, live service actions or actual model-family diversity is inferred from content hashes, fixture records, parent dispatch or local file presence.",
          "No Bun; no Node/Python substitution",
          "No live account writes",
          "Git task revision unknown",
          "Prior broad tool outputs truncated; retained per-source raw receipts supersede for source content",
          "Not every early tool call has local full raw capture; host transcript retains them"
        ],
        "reviewedBy": "review_workflow_evidence independent archive/contract review",
        "expectedFull": "Observe stop and terminal cancellation; quarantine partial output and integrate only a separately reviewed completed assignment.",
        "expectedReduced": "Unavailable stop operation permits only local artifact inspection; record unconfirmed termination."
      },
      "topLevelContext": {
        "packageCommit": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "scope": "ChatGPT baseline batches05–08, 32 unique workflow cases",
        "gradingPolicy": "Qualitative full/reduced/blocked outcomes plus actual native observation limits; corrected uncertain-result execution/persistence grants enforced. Model-captured wrappers are not independently raw-event verified; no self-grade imported."
      },
      "response": {
        "text": "An actual reused native worker wrote harmless partial.txt and sent a milestone. I interrupted the running worker, then list_agents observed interrupted state. I moved its artifact into quarantine and read it back; it is excluded from accepted output. This proves exposed stop and observed interrupted status, not process-level termination or fresh-worker orchestration. Task Git SHA remains unknown. Initial no-probe result is superseded by retained cancellation-receipts.json.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/result.json",
          "sha256": "f7525a4c4efc7b2a3fc6f83bbea7165e8804b6031eb3cd0182294deaf1fd0fe5",
          "bytes": 1985
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/cancellation-receipts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/cancellation-receipts.json",
      "sha256": "6c4290c39959ad08da12e3fd93e1b9522ac818ff028b2b4ba23d44472fa62dfc",
      "bytes": 2301,
      "owners": [
        "grades-chatgpt-05-08.json#19"
      ],
      "text": "{\n  \"assignmentId\": \"cancel-partial-a\",\n  \"inputRevision\": null,\n  \"inputArtifactSha256\": \"6ef42285eecd1bef7789167f6297283ebd8fae65a93092d5a84d232163885d88\",\n  \"worker\": \"/root/eval_05_08/cache_a\",\n  \"freshWorker\": false,\n  \"milestone\": {\n    \"kind\": \"worker message\",\n    \"raw\": \"Cancellation milestone cancel-partial-a: tools.exec_command mkdir/printf/cat succeeded exit_code 0, chunk_id 47e900, stdout exactly \\\"PARTIAL, NOT ACCEPTED\\\\n\\\". File /workspace/scratch/305945b957dd/remaining-evaluation/batches/batch-07/cases/cancelled-worker/partial/partial.txt exists and read back. Partial is NOT accepted for integration. Entering wait until interrupted; no further writes.\"\n  },\n  \"stop\": {\n    \"tool\": \"collaboration.interrupt_agent\",\n    \"arguments\": {\n      \"target\": \"cache_a\"\n    },\n    \"result\": {\n      \"previous_status\": \"running\"\n    }\n  },\n  \"inspectTerminal\": {\n    \"tool\": \"collaboration.list_agents\",\n    \"arguments\": {\n      \"path_prefix\": \"/root/eval_05_08/cache_a\"\n    },\n    \"result\": {\n      \"agents\": [\n        {\n          \"agent_name\": \"/root/eval_05_08/cache_a\",\n          \"agent_status\": \"interrupted\"\n        }\n      ]\n    }\n  },\n  \"quarantine\": {\n    \"tool\": \"tools.exec_command\",\n    \"arguments\": {\n      \"cmd\": \"mkdir -p remaining-evaluation/batches/batch-07/cases/cancelled-worker/quarantine\\nmv remaining-evaluation/batches/batch-07/cases/cancelled-worker/partial/partial.txt remaining-evaluation/batches/batch-07/cases/cancelled-worker/quarantine/partial.txt\\ncat remaining-evaluation/batches/batch-07/cases/cancelled-worker/quarantine/partial.txt\\nsha256sum remaining-evaluation/batches/batch-07/cases/cancelled-worker/quarantine/partial.txt\",\n      \"max_output_tokens\": 1000\n    },\n    \"result\": {\n      \"chunk_id\": \"89d045\",\n      \"wall_time_seconds\": 0.000035498,\n      \"exit_code\": 0,\n      \"original_token_count\": 43,\n      \"output\": \"PARTIAL, NOT ACCEPTED\\n988eea4d817b264dc04c2882543c3930df1f704f104deafe9c8f08f170f916ad  remaining-evaluation/batches/batch-07/cases/cancelled-worker/quarantine/partial.txt\\n\"\n    }\n  },\n  \"limits\": [\n    \"Reused worker; no freshness claim\",\n    \"Worker's write stdout is a returned message, not copied raw tool object\",\n    \"Observed interrupted state, not completed/cancelled enum\",\n    \"No partial artifact integrated\"\n  ]\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/evidence/source-status.tsv",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/evidence/source-status.tsv",
      "sha256": "42faf2ff93c4beaa19263bf980281cb45a853164e09388b467e3481ff6693d09",
      "bytes": 101,
      "owners": [
        "grades-chatgpt-05-08.json#19"
      ],
      "text": "0\tskills/poteto-mode/SKILL.md\n0\tskills/poteto-mode/playbooks/orchestrate.md\n1\tagents/poteto-agent.md\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/quarantine/partial.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/quarantine/partial.txt",
      "sha256": "988eea4d817b264dc04c2882543c3930df1f704f104deafe9c8f08f170f916ad",
      "bytes": 22,
      "owners": [
        "grades-chatgpt-05-08.json#19"
      ],
      "text": "PARTIAL, NOT ACCEPTED\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/result.json",
      "sha256": "f7525a4c4efc7b2a3fc6f83bbea7165e8804b6031eb3cd0182294deaf1fd0fe5",
      "bytes": 1985,
      "owners": [
        "grades-chatgpt-05-08.json#19"
      ],
      "text": "{\n  \"caseId\": \"cancelled-worker\",\n  \"batch\": \"batch-07\",\n  \"actualResponse\": \"An actual reused native worker wrote harmless partial.txt and sent a milestone. I interrupted the running worker, then list_agents observed interrupted state. I moved its artifact into quarantine and read it back; it is excluded from accepted output. This proves exposed stop and observed interrupted status, not process-level termination or fresh-worker orchestration. Task Git SHA remains unknown. Initial no-probe result is superseded by retained cancellation-receipts.json.\",\n  \"variants\": [\n    {\n      \"name\": \"native stop and terminal inspection\",\n      \"status\": \"attempted\",\n      \"reason\": \"Running -> interrupt -> observed interrupted\"\n    },\n    {\n      \"name\": \"artifact quarantine\",\n      \"status\": \"attempted\",\n      \"reason\": \"Moved and read quarantine/partial.txt; not integrated\"\n    },\n    {\n      \"name\": \"fresh assignment revision\",\n      \"status\": \"blocked\",\n      \"reason\": \"Reused worker and missing task Git SHA\"\n    }\n  ],\n  \"observedOperations\": [\n    \"tools.exec_command named installed sources, cases and fixtures reads\",\n    \"tools.apply_patch isolated result/trail/synthesis writes\",\n    \"collaboration.followup_task new isolated cancellation assignment\",\n    \"collaboration.interrupt_agent\",\n    \"collaboration.list_agents interrupted observation\",\n    \"tools.exec_command quarantine and readback\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"input/\",\n    \"work/\",\n    \"evidence/source-status.tsv\",\n    \"../../fixture-read-receipt.json\",\n    \"../../../batch-05/source-read-receipts.json\",\n    \"cancellation-receipts.json\",\n    \"quarantine/partial.txt\"\n  ],\n  \"limits\": [\n    \"No Bun; no Node/Python substitution\",\n    \"No live account writes\",\n    \"Git task revision unknown\",\n    \"Prior broad tool outputs truncated; retained per-source raw receipts supersede for source content\",\n    \"Not every early tool call has local full raw capture; host transcript retains them\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/case.json",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/evidence/sources",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/input",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/README.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/README.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/README.md",
      "sha256": "d196849f4d82de3618f0e530cdddc68d486b3b2cd7ec807fa1a98412ddc4532c",
      "bytes": 797
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/cache/README.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/README.md",
      "sha256": "b6a51fa497d6924aa1d0cbbbf066c7630ea27601027424b994e24c3f8e293551",
      "bytes": 509
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/cache/cache.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/cache.mjs",
      "sha256": "e634749df91c057ba245f99e1e1f4cf95e0a07a9abbb929e37e1f012a9881be9",
      "bytes": 199
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/cache/caller.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/caller.mjs",
      "sha256": "9566a520d6763d359c4b43cd5705df6333c8bf4a4afb96aec7ac3ca2e2145490",
      "bytes": 309
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/cache/invalidation.diff",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/invalidation.diff",
      "sha256": "0f2f4bee7dba00d4cb422f289fe8a6213fd891f08026892e65839113253752b7",
      "bytes": 365
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/cache/manifest.json",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/manifest.json",
      "sha256": "5ed74232104c678e92d295f38648ee32dc80207816ed801ae845dbc80502fe29",
      "bytes": 253
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/cache/probe.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/probe.mjs",
      "sha256": "fa8cdce0fe97a6e3ed1b071aceab4365938b862c335cfccdb94508173a7fd002",
      "bytes": 395
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/cache/vendor/disposer-v1.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/cache/vendor/disposer-v1.mjs",
      "sha256": "d33e8d36600ad5df008657e478e39f9100a347098b4176f37923e5056cb3427f",
      "bytes": 196
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/corpus/records.jsonl",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/corpus/records.jsonl",
      "sha256": "bba536a5394a6ddb455eddd0d9f04f67426bc5f9ef08325d543aab696a94a061",
      "bytes": 46932
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/dead-path/caller.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/caller.mjs",
      "sha256": "1bb6a07b1f008c9bb78a5bf7ff291bee6ed622754138a755a8139b1f62fa0931",
      "bytes": 114
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/dead-path/duplicate-reference.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/duplicate-reference.md",
      "sha256": "0be0105728e3b3bc10f73c6e3e002312b56a10bcc6614d4a004578c1cd976974",
      "bytes": 35
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/dead-path/handler.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/handler.mjs",
      "sha256": "a86227bd0095ace24cce86fe3c7c2f1b17eace7b95e659bdf01d2e1ded216af6",
      "bytes": 361
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/dead-path/instructions.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/instructions.md",
      "sha256": "d29bd69e17b40515d3a869a2ad1a4e6e59a984eab51da3e737bc49126ae0e228",
      "bytes": 137
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/dead-path/scope.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/dead-path/scope.md",
      "sha256": "1bcff725b72dbcd6b4894eb89e32c92bf142df387fcf88e45681e2a89feed510",
      "bytes": 511
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/history/capsule.json",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/capsule.json",
      "sha256": "68475aad9893f5968ac61b2c68b9e1dda09450d5a631bce1fbb5394e562b5568",
      "bytes": 691
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/history/history.json",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/history.json",
      "sha256": "6dbfde39a52d5c14c522aac3f74bd300ac4ce62f5411a6540410a5d16b424b13",
      "bytes": 1362
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/history/jay-mode.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/jay-mode.md",
      "sha256": "477ba7aaaeab112324c1ee03db183869bc46ec8f4bdc4b8b76dceeb6ca563f3f",
      "bytes": 372
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/history/shared-records.json",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/history/shared-records.json",
      "sha256": "7859c51afe5feade4176ed6f0c4c9a6aff7141e83df0a32f71c455d70a1b94c1",
      "bytes": 950
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/invoice/adapter.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/adapter.mjs",
      "sha256": "a3c0a1bdc969b23f6e82e7b31795f0a40159fa701f4512c1fb17ecfb6932040c",
      "bytes": 122
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/invoice/calculator.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/calculator.mjs",
      "sha256": "1a8c31477dd32fa77ca6af108ce3fa682f2b7232261eba1c1261511bb8c0afff",
      "bytes": 221
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/invoice/controller.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/controller.mjs",
      "sha256": "90f31483ab24712ecdc0a99e37fec9395a0ca492221d5256a96dedbebeeb5862",
      "bytes": 135
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/invoice/decision.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/decision.md",
      "sha256": "324b01aaa0666f9fa01e466892f932873012baaf82bfc2f22427544426a01dee",
      "bytes": 1193
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/invoice/exporter.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/exporter.mjs",
      "sha256": "b877fb99b3f10c68823e9bcd3250d86f58a573122f3d65053d56baa2d1bcba4d",
      "bytes": 191
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/invoice/facade.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/facade.mjs",
      "sha256": "6afdc0fb708cea863258bee1eaeeff319dbbbe4e6d0bde0a74a2c4b6649a873d",
      "bytes": 123
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/invoice/formatter.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/invoice/formatter.mjs",
      "sha256": "405007871ab7b0d2fbe1363eff4d19a26d7f316e77cf8fbf818cf051101d9fa7",
      "bytes": 475
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/legal-header/source.diff",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.diff",
      "sha256": "da37375054eb4140f6b2ba19dac4c5de3846183029177d58473b38d320cf8436",
      "bytes": 671
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/legal-header/source.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/legal-header/source.mjs",
      "sha256": "7579a6b456d0cd513fd8f55d69096119304833f0dc5dfca7f66c727ec002df91",
      "bytes": 553
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/migration/api.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/api.mjs",
      "sha256": "822054af940ca854899daa9456c70e16afccf154022a5ace1b975370b61282e7",
      "bytes": 93
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/migration/contract.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/contract.mjs",
      "sha256": "1aaaa839570217e43ff11a5682fdd6e993f3e4b0348dde368e81fef4e992e1da",
      "bytes": 314
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/migration/notification.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/notification.mjs",
      "sha256": "ddea89cd41e91d59492cbe204184f94329f929b611d98de248c7e9bf6e9636ee",
      "bytes": 126
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/migration/profile.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/profile.mjs",
      "sha256": "2dc0f40e598ba73e5f1f15f3b583c6b9f246a96d45d3c9dd6c682b2b9b88d465",
      "bytes": 157
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/migration/scope.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/scenario-map.json",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/scenario-map.json",
      "sha256": "a732248ad7fdf1f003452602cd92f3571201ce6b2839569246f02155311a9a0b",
      "bytes": 2593
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/types/README.md",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/README.md",
      "sha256": "201077abbec770f3cc8b4484ae8e894df8900001f5ef56ed06a6debadc79a588",
      "bytes": 503
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/types/boundary.ts",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/boundary.ts",
      "sha256": "5e98773209677f72d526c420f60a406972988e8fc0067963f781fe5955188e42",
      "bytes": 516
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/additional/types/context.ts",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/types/context.ts",
      "sha256": "862482654b2368e523227131527e316178a5f27e31470c176476ec811b7b5f58",
      "bytes": 995
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/dashboard.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/dashboard.mjs",
      "sha256": "34ce510c07f0391617a02e552ef0e184b1fa9d0cf718c72dfd23d67b6fd2a1b9",
      "bytes": 208
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/forge.json",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/forge.json",
      "sha256": "0eb3d994dc21b2fb0874b09d581f88e8d5cdd3a2364e9040263c64c7b801250c",
      "bytes": 1183
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/history.json",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/history.json",
      "sha256": "f424ba7bfc6117543f624df1eb29973a2be71b782c5324f57c27c8c649f45930",
      "bytes": 488
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/invoice.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/invoice.mjs",
      "sha256": "64adb438025e87e8e1a9d217d26ea510fdd11a8c7e27f25b74de70481396d1d8",
      "bytes": 371
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/orders.json",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/orders.json",
      "sha256": "561bca1cb0c759f9785ae826d8285fab84f0d419760917709a7f44968d10ee93",
      "bytes": 269
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-07/cases/cancelled-worker/work/runtime.mjs",
      "owner": "grades-chatgpt-05-08.json#19",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
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
