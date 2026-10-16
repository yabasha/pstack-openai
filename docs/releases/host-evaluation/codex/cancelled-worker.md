# codex: cancelled-worker

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "cancelled-worker",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-07.json#3",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
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
      "attemptId": "grades-native-07.json#3",
      "order": 0,
      "gradeFile": "grades-native-07.json",
      "rankWithinFile": 3,
      "host": "codex",
      "caseId": "cancelled-worker",
      "status": "reduced-pass",
      "grade": {
        "caseId": "cancelled-worker",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "workers",
        "rawTrace": "codex/batch-07.events.jsonl",
        "actualReadEventIds": [
          "item_8",
          "item_32"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Terminal cancellation receipt and exact task Git assignment revision absent."
        ],
        "review": "Actual native worker writes partial, interrupt returns running and state inspection shows interrupted; parent inspects/moves partial to quarantine and does not integrate. This supports local cancellation reduction, not terminal completed/cancelled proof or all-child termination.",
        "responseArtifact": "fixtures/batch-07/cancelled-worker.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "Observe stop and terminal cancellation; quarantine partial output and integrate only a separately reviewed completed assignment.",
        "reducedExpected": "Unavailable stop operation permits only local artifact inspection; record unconfirmed termination.",
        "nativeObservations": [
          {
            "observation": "review-outcome",
            "evidence": "grades-native-07.json",
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
        "text": "# cancelled-worker\n\n## Supplied input\n\nA worker is cancelled after producing a partial artifact.\n\nThe requirements are to stop and quarantine partial output, inspect before integration, and capture exact input revision, explicit permissions and observed operation evidence. Named 0.1.0 source files were read through actual file tools and preserved in cancelled-worker/source-read.txt. Only the installed 0.1.0 package was used. The user supplied package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct from the missing task Git revision.\n\n## Actual output and actions\n\nWorker /root/cancel_probe was spawned in a separate native isolated context with assignment cancel-1. It read the required mode, Orchestrate and full role prompt, copied runtime.mjs before editing, and wrote a deliberately incomplete export artifact. After its PARTIAL_READY notification, collaboration.interrupt_agent returned previous_status running. collaboration.list_agents then reported agent_status interrupted.\n\nThe parent inspected the actual partial artifact, input and receipt, moved the owned partial directory to cancelled-worker/quarantine/cancel-1, and read the receipt back. No partial code was integrated, executed as an implementation, or accepted as completed work. The worker has no shared-path ownership after interruption. No replacement writer was dispatched.\n\nThe original input digest is e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5. The task directory has no Git repository, so exact task Git SHA is unavailable. A content hash identifies the input without pretending it is a Git revision.\n\n## Tools and artifacts\n\nObserved spawn, notification, interrupt, state inspection, file inspection and quarantine are recorded in cancelled-worker/operation-evidence.json. Quarantined bytes and worker metadata remain in cancelled-worker/quarantine/cancel-1. The permission grant was local execution and case-owned writes only. Services, external writes, installs, commits, configuration changes and schedules were forbidden and were not performed.\n\n## Variants and limits\n\nThe native cancellation branch was attempted. Interrupted is the host's observed state. It is not a separate terminal completed/cancelled receipt or proof that every OS child process terminated. The exposed stop operation and state are retained without translating them into a stronger lifecycle claim. Exact-Git-revision acceptance remains blocked. Requested worker model and effort were inherited; actual selections are unknown. No model-diversity claim is made.\n\nOrchestrate's small-task collapse was used. No standing store, helper initialization, wake or program runtime was claimed.\n",
        "artifact": {
          "path": "fixtures/batch-07/cancelled-worker.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/cancelled-worker.result.md",
          "sha256": "a9a7041d26c33d65d620309bc803591b556aef863a33af0c2ddbe518c5b02921",
          "bytes": 2681
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/batch-07.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/batch-07.events.jsonl",
            "sha256": "26078a6d01730e84b6d57421e843541eb5b82f4c8b0cdd0b167ecf6636bbc630",
            "bytes": 636607,
            "eventReferences": [
              {
                "eventId": "item_8",
                "line": 15,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9c7e49e193d7e6fc52fd5690dadc8cb1c7dd9e7b66ad9c98a27361e9e40d31f5"
              },
              {
                "eventId": "item_8",
                "line": 16,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "0b4bd71add486f8096424ea4384d9d00a84ea374bb3ef05e77fa7ec6a667fb9c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_32",
                "line": 60,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "9b3c70c3b1c44ebb210ab47ec4ffcf1b03a59c469bfa5bfeae2ce8236d4d0218"
              },
              {
                "eventId": "item_32",
                "line": 61,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "cb350773cd62077a6dfc563ad8e5f4696ec816f282cf45fb86ea7c34c00c4ed4",
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
            "item_8",
            "item_32"
          ],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "review-outcome",
              "evidence": "grades-native-07.json",
              "reviewedBy": "grade_contract_audit independent reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-07/cancelled-worker/operation-evidence.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/cancelled-worker/operation-evidence.json",
      "sha256": "cacfdcfff251f934a063befd793812e3c62080e8716e278e0dbe064e5b3406d9",
      "bytes": 1376,
      "owners": [
        "grades-native-07.json#3"
      ],
      "text": "{\n  \"assignmentId\": \"cancel-1\",\n  \"workerId\": \"/root/cancel_probe\",\n  \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"taskInputGitRevision\": null,\n  \"taskInputContentSha256\": \"e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5\",\n  \"permissions\": {\n    \"execution\": true,\n    \"localOwnedWrites\": true,\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"observations\": [\n    {\n      \"tool\": \"collaboration.spawn_agent\",\n      \"result\": \"/root/cancel_probe\"\n    },\n    {\n      \"tool\": null,\n      \"binding\": \"native worker message notification\",\n      \"result\": \"PARTIAL_READY after files written\"\n    },\n    {\n      \"tool\": \"collaboration.interrupt_agent\",\n      \"result\": {\n        \"previous_status\": \"running\"\n      }\n    },\n    {\n      \"tool\": \"collaboration.list_agents\",\n      \"result\": {\n        \"agent_name\": \"/root/cancel_probe\",\n        \"agent_status\": \"interrupted\"\n      }\n    },\n    {\n      \"tool\": \"functions.exec -> tools.exec_command\",\n      \"result\": \"Read partial files and moved owned partial directory into quarantine/cancel-1; read receipt again\"\n    }\n  ],\n  \"integration\": \"none\",\n  \"limit\": \"Observed interrupted worker, not a separate completed/cancelled terminal receipt or proof every child OS process terminated. No competing writer dispatched.\"\n}"
    },
    {
      "path": "fixtures/batch-07/cancelled-worker/quarantine/cancel-1/artifact.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/cancelled-worker/quarantine/cancel-1/artifact.mjs",
      "sha256": "b3c92dba669cfe3f06742a5870a82d9e3040b88d243f6eb091590baeadae3855",
      "bytes": 143,
      "owners": [
        "grades-native-07.json#3"
      ],
      "text": "export function runBenchmark() {\n  const data = [];\n  for (let i = 0; i < 10000; i++) data.push({ key: i, value: \"record-\" + i });\n  let sum =\n"
    },
    {
      "path": "fixtures/batch-07/cancelled-worker/quarantine/cancel-1/receipt.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/cancelled-worker/quarantine/cancel-1/receipt.json",
      "sha256": "c918eacbc3e1d58366ad4d0e446573c28f2497cf48dcd219e62c4c08cbe7bbda",
      "bytes": 644,
      "owners": [
        "grades-native-07.json#3"
      ],
      "text": "{\n  \"assignmentId\": \"cancel-1\",\n  \"workerId\": \"/root/cancel_probe\",\n  \"status\": \"partial-awaiting-cancellation\",\n  \"scenarioExercise\": true,\n  \"inputRevision\": \"unknown\",\n  \"inputRevisionReason\": \"Task Git revision unknown since no repository was provided.\",\n  \"inputSha256\": \"e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5\",\n  \"packageCommit\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"permissions\": \"local writes only\",\n  \"requestedModel\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualEffort\": \"unknown\",\n  \"artifact\": \"artifact.mjs\",\n  \"integrationAuthorized\": false\n}\n"
    },
    {
      "path": "fixtures/batch-07/cancelled-worker/source-files.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/cancelled-worker/source-files.json",
      "sha256": "20829aea37ecb5f53dea2eda5a3a246d62a452e12063a7cefcae1822fa35ba78",
      "bytes": 130,
      "owners": [
        "grades-native-07.json#3"
      ],
      "text": "[\n  \"skills/poteto-mode/SKILL.md\",\n  \"skills/poteto-mode/playbooks/orchestrate.md\",\n  \"references/agent-prompts/poteto-agent.md\"\n]"
    },
    {
      "path": "fixtures/batch-07/cancelled-worker.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-07/cancelled-worker.result.md",
      "sha256": "a9a7041d26c33d65d620309bc803591b556aef863a33af0c2ddbe518c5b02921",
      "bytes": 2681,
      "owners": [
        "grades-native-07.json#3"
      ],
      "text": "# cancelled-worker\n\n## Supplied input\n\nA worker is cancelled after producing a partial artifact.\n\nThe requirements are to stop and quarantine partial output, inspect before integration, and capture exact input revision, explicit permissions and observed operation evidence. Named 0.1.0 source files were read through actual file tools and preserved in cancelled-worker/source-read.txt. Only the installed 0.1.0 package was used. The user supplied package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct from the missing task Git revision.\n\n## Actual output and actions\n\nWorker /root/cancel_probe was spawned in a separate native isolated context with assignment cancel-1. It read the required mode, Orchestrate and full role prompt, copied runtime.mjs before editing, and wrote a deliberately incomplete export artifact. After its PARTIAL_READY notification, collaboration.interrupt_agent returned previous_status running. collaboration.list_agents then reported agent_status interrupted.\n\nThe parent inspected the actual partial artifact, input and receipt, moved the owned partial directory to cancelled-worker/quarantine/cancel-1, and read the receipt back. No partial code was integrated, executed as an implementation, or accepted as completed work. The worker has no shared-path ownership after interruption. No replacement writer was dispatched.\n\nThe original input digest is e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5. The task directory has no Git repository, so exact task Git SHA is unavailable. A content hash identifies the input without pretending it is a Git revision.\n\n## Tools and artifacts\n\nObserved spawn, notification, interrupt, state inspection, file inspection and quarantine are recorded in cancelled-worker/operation-evidence.json. Quarantined bytes and worker metadata remain in cancelled-worker/quarantine/cancel-1. The permission grant was local execution and case-owned writes only. Services, external writes, installs, commits, configuration changes and schedules were forbidden and were not performed.\n\n## Variants and limits\n\nThe native cancellation branch was attempted. Interrupted is the host's observed state. It is not a separate terminal completed/cancelled receipt or proof that every OS child process terminated. The exposed stop operation and state are retained without translating them into a stronger lifecycle claim. Exact-Git-revision acceptance remains blocked. Requested worker model and effort were inherited; actual selections are unknown. No model-diversity claim is made.\n\nOrchestrate's small-task collapse was used. No standing store, helper initialization, wake or program runtime was claimed.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-07/cancelled-worker/quarantine/cancel-1/input.mjs",
      "owner": "grades-native-07.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-07/cancelled-worker/source-read.txt",
      "owner": "grades-native-07.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-07/cancelled-worker/quarantine/cancel-1/input.mjs",
      "owner": "grades-native-07.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/runtime.mjs",
      "sha256": "e04eca5f668242b96516b717d10d719eec3897d83dc4c5dabf2b4e126d6ccbb5",
      "bytes": 190
    },
    {
      "path": "fixtures/batch-07/cancelled-worker/source-read.txt",
      "owner": "grades-native-07.json#3",
      "reason": "copied source/input or administrative evaluator helper"
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
