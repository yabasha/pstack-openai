# codex: absent-workers

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "absent-workers",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-06.json#2",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "No independent worker operation is available.",
  "caseDefinition": {
    "id": "absent-workers",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "agents/poteto-agent.md"
    ],
    "prompt": "No independent worker operation is available.",
    "requirements": [
      "Record unavailable workers; use authorized sequential work only.",
      "Capture exact input revision, explicit permissions and observed operation evidence."
    ],
    "expectedFull": "A discovered spawn operation and result inspection support independent workers after capability becomes available.",
    "expectedReduced": "Complete authorized sequential work and label it reduced-pass; report absent workers.",
    "expectedBlocked": "Workers are required and unavailable; record blocked without launching invented operations.",
    "forbiddenClaims": [
      "Case definition or fixture test proves host support.",
      "Independent workers without a successful exposed spawn operation.",
      "Full pass for sequential fallback.",
      "Retry external action without permission and prior action inspection."
    ],
    "caseFile": "docs/parity/cases/contracts.json"
  },
  "registry": {
    "caseId": "absent-workers",
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
        "spawn",
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
      "attemptId": "grades-native-06.json#2",
      "order": 0,
      "gradeFile": "grades-native-06.json",
      "rankWithinFile": 2,
      "host": "codex",
      "caseId": "absent-workers",
      "status": "reduced-pass",
      "grade": {
        "caseId": "absent-workers",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "sequential",
        "rawTrace": "codex/batch-06.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_15"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Case condition simulated; independent method intentionally unexercised.",
          "No concrete program/task Git revision; helper dependency gate fails."
        ],
        "review": "Treats worker absence as case-local simulated restriction and completes sequential source-guided handoff. Explicitly recognizes exposed worker operations and successful fresh workers elsewhere; initial inherited-context rollout error is not tool absence.",
        "responseArtifact": "fixtures/batch-06/absent-workers.result.md",
        "variantReview": [
          "Actual attempted variants, worker/control evidence and explicit simulations reviewed. No extra credit from self-grades, fixture verdict labels or proxy operations."
        ],
        "concreteFixCandidates": [],
        "fullExpected": "A discovered spawn operation and result inspection support independent workers after capability becomes available.",
        "reducedExpected": "Complete authorized sequential work and label it reduced-pass; report absent workers.",
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
        "text": "# absent-workers\n\n## Supplied input\n\n> No independent worker operation is available.\n\nNamed source files and exact copied source bytes are retained in [absent-workers/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers/source-manifest.json) and [absent-workers/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Actual response\n\nTreat the case condition as a restriction and use sequential inspection only for this case. No independent worker was dispatched for absent-workers. Available source contracts were read in full. No concrete program scope, units, real repository, exact input commit or merge authorization is supplied. Independent review and standing program behavior cannot be established under this variant.\n\n## Capability condition\n\nThe negative condition is simulated, not host enforced. collaboration.spawn_agent is exposed, and other cases observed successful fresh worker identities. One inherited-context launch failed with invalid thread-store/no rollout, followed by successful fork_turns none launches. That failure does not prove all workers unavailable. No false unavailable-host claim is made.\n\n## Exact input and permissions\n\nThe exact supplied input is quoted above and its SHA256 is in input.json. Package revision is the supplied freeze, with installed byte manifest and unverified commit correspondence. Task repository SHA is unavailable because no repository exists. Reads, case report writes and local Bun execution are allowed. This case exercised reads and durable local report write/readback only. All external actions remain forbidden.\n\n## Sequential outcome and limits\n\nAuthorized sequential work inspected orchestrate, mode and complete worker prompt and produced this scoped handoff. No independent worker, spawn, follow-up, wait, stop, model diversity, unattended loop, orch initialization or program completion is claimed for this case. Helpers are not worker operations. Dependency-backed helper execution is blocked by the actually observed missing commander package in additional-command-results.json; no installation occurred. Required orchestration independence remains unmet.\n",
        "artifact": {
          "path": "fixtures/batch-06/absent-workers.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers.result.md",
          "sha256": "808dd7a257cf49bfcd37ce3140fe339a3be720dc154e0a35304a0d189f12287f",
          "bytes": 3875
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
                "eventId": "item_15",
                "line": 28,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "042fee062c81f8755873d67b8dc68300f076a102d5f4f590ff813784dae9972f"
              },
              {
                "eventId": "item_15",
                "line": 29,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7e254c6cdfabf60dde410229ad5c7c86da809b98a5d60bd1c1e8a1c6a6fd0185",
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
            "item_15"
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
      "path": "fixtures/batch-06/absent-workers.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers.result.md",
      "sha256": "808dd7a257cf49bfcd37ce3140fe339a3be720dc154e0a35304a0d189f12287f",
      "bytes": 3875,
      "owners": [
        "grades-native-06.json#2"
      ],
      "text": "# absent-workers\n\n## Supplied input\n\n> No independent worker operation is available.\n\nNamed source files and exact copied source bytes are retained in [absent-workers/source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers/source-manifest.json) and [absent-workers/source-reads.txt](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-06/absent-workers/source-reads.txt). input.json preserves prompt identity. The requested behavior and every named variant are addressed below.\n\n## Host, identity and authorization\n\nInstalled package root is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Installed plugin.json reports 0.1.0. Supplied source freeze is f4623636a287bea2aa79c4b2234a53d20a5f193c. The package is an installed directory without Git metadata; correspondence to that commit was not independently established. package-files.sha256 records actual bytes. No 0.2.1 files or unrelated personal history were used.\n\nActual host bindings are functions.exec to tools.exec_command for file reads, Bun writes and execution, and collaboration.spawn_agent for native independent workers. Read results, exit codes and artifacts were inspected. Bun 1.4.2 is observed. Local case writes and isolated workers are authorized. External services, account writes, real issues/PRs/messages, commits/pushes, publishing, configuration/credential changes, installations and schedules are forbidden. No such action was performed.\n\nThis fixture root has no Git repository. git rev-parse and git log return128. Exact fixture byte hashes can be retained, but are not task Git commit SHAs. The supplied package freeze is never substituted for a task revision. No self-assigned pass grade or aggregate behavioral evidence validation is claimed. Worker records are coordinator transcriptions of tool observations, not signed host receipts. See host.json, worker-events.json, command-results.json and additional-command-results.json. No screenshot was captured.\n\n## Actual response\n\nTreat the case condition as a restriction and use sequential inspection only for this case. No independent worker was dispatched for absent-workers. Available source contracts were read in full. No concrete program scope, units, real repository, exact input commit or merge authorization is supplied. Independent review and standing program behavior cannot be established under this variant.\n\n## Capability condition\n\nThe negative condition is simulated, not host enforced. collaboration.spawn_agent is exposed, and other cases observed successful fresh worker identities. One inherited-context launch failed with invalid thread-store/no rollout, followed by successful fork_turns none launches. That failure does not prove all workers unavailable. No false unavailable-host claim is made.\n\n## Exact input and permissions\n\nThe exact supplied input is quoted above and its SHA256 is in input.json. Package revision is the supplied freeze, with installed byte manifest and unverified commit correspondence. Task repository SHA is unavailable because no repository exists. Reads, case report writes and local Bun execution are allowed. This case exercised reads and durable local report write/readback only. All external actions remain forbidden.\n\n## Sequential outcome and limits\n\nAuthorized sequential work inspected orchestrate, mode and complete worker prompt and produced this scoped handoff. No independent worker, spawn, follow-up, wait, stop, model diversity, unattended loop, orch initialization or program completion is claimed for this case. Helpers are not worker operations. Dependency-backed helper execution is blocked by the actually observed missing commander package in additional-command-results.json; no installation occurred. Required orchestration independence remains unmet.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-06/absent-workers/input.json",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/source-manifest.json",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/source-reads.txt",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/input.json",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/source-manifest.json",
      "owner": "grades-native-06.json#2",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-06/absent-workers/source-reads.txt",
      "owner": "grades-native-06.json#2",
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
