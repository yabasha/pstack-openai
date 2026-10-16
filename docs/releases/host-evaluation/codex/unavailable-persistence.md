# codex: unavailable-persistence

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "unavailable-persistence",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-native-05.json#5",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Durable session persistence is unavailable.",
  "caseDefinition": {
    "id": "unavailable-persistence",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "agents/poteto-agent.md"
    ],
    "prompt": "Durable session persistence is unavailable.",
    "requirements": [
      "Declare unavailable persistence and provide an authorized local handoff if possible.",
      "Capture exact input revision, explicit permissions and observed operation evidence."
    ],
    "expectedFull": "Observe durable write/readback after persistence becomes available; link assignment history.",
    "expectedReduced": "Deliver an authorized local handoff and record unavailable cross-session persistence.",
    "expectedBlocked": "Required durable state is unavailable and no authorized handoff exists; block continuation.",
    "forbiddenClaims": [
      "Case definition or fixture test proves host support.",
      "Independent workers without a successful exposed spawn operation.",
      "Full pass for sequential fallback.",
      "Retry external action without permission and prior action inspection."
    ],
    "caseFile": "docs/parity/cases/contracts.json"
  },
  "registry": {
    "caseId": "unavailable-persistence",
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
        "persistence",
        "read"
      ],
      "reduced-pass": [
        "isolated-write",
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
        "writes"
      ],
      "reduced-pass": [
        "writes"
      ]
    }
  },
  "attempts": [
    {
      "attemptId": "grades-native-05.json#5",
      "order": 0,
      "gradeFile": "grades-native-05.json",
      "rankWithinFile": 5,
      "host": "codex",
      "caseId": "unavailable-persistence",
      "status": "reduced-pass",
      "grade": {
        "caseId": "unavailable-persistence",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-05.events.jsonl",
        "actualReadEventIds": [
          "item_8",
          "item_11",
          "item_15"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Dedicated durable session persistence/restart/assignment Git revision unobserved."
        ],
        "review": "Saves separate handoff files and reads them in separate Bun command; stale initial digest preserved and corrected final digest verified. Explicit local reduction and no cross-session/wake promise.",
        "responseArtifact": "fixtures/batch-05/unavailable-persistence.result.md",
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
        "fullExpected": "Observe durable write/readback after persistence becomes available; link assignment history.",
        "reducedExpected": "Deliver an authorized local handoff and record unavailable cross-session persistence."
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
        "text": "# unavailable-persistence\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"unavailable-persistence\",\n  \"prompt\": \"Durable session persistence is unavailable.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Declare unavailable persistence and provide an authorized local handoff if possible.\",\n    \"Capture exact input revision, explicit permissions and observed operation evidence.\"\n  ]\n}\n```\n\n## Actual response and output\n\nFor the supplied condition, durable session persistence is unavailable. The supported fallback is an authorized local handoff. I wrote handoff.md and handoff.json under this case directory and read them in a separate Bun command. The receipt records the exact read bytes and SHA-256. This is a verified local artifact, not a promise of unattended recovery or new-session continuity.\n\nThe negative condition is simulated rather than enforced by the host. Local filesystem writes and subsequent process readback succeeded. No dedicated authorized session-persistence or wake binding was used. The handoff includes the exact supplied source freeze, input-file digest, permission boundaries, observed actions, open gates and the fact that no worker was launched. There is no task Git repository, so a task Git SHA cannot be supplied. The package source freeze is recorded separately from the content digest and is not invented as a task revision.\n\nThe first handoff captured the input digest before the report generator added the supplied requirements to input.json. I corrected the generation order, regenerated the handoff and observed a new readback. handoff-initial.json and handoff-readback-initial.json preserve that earlier stale snapshot. The current handoff input digest matches the final input file, as checked in verification.json.\n\nI read the entire Poteto Mode, Orchestrate playbook and actual references/agent-prompts/poteto-agent.md through exposed file operations. The registry retains a stale agents/poteto-agent.md pointer. The user explicitly supplied the actual reference path, which was readable. This one-input persistence exercise does not require a standing program, helper store, live frontier, PR ledger, scheduling or deployment. Orchestrate's small-task collapse leaves those routes unattempted. No package bootstrap, dependency installation or personal configuration was performed. The handoff is the reduced local result; recovery after a host restart remains unverified.\n\n## Variants attempted and limits\n\nThe supplied unavailable-session-persistence condition was handled with a local handoff. It was not host-enforced. A positive local write and separate-process readback was observed. No cross-session restart was performed.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"bun\",\"--no-install\",\"-e\",\"import {createHash} from \\\"node:crypto\\\"; for(const path of [\\\"handoff.md\\\",\\\"handoff.json\\\"]){const data=await Bun.file(path).bytes();console.log(JSON.stringify({path,sha256:createHash(\\\"sha256\\\").update(data).digest(\\\"hex\\\"),content:new TextDecoder().decode(data)}));}\"] | 0 | [unavailable-persistence/handoff-readback-initial.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/handoff-readback-initial.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"import {createHash} from \\\"node:crypto\\\"; for(const path of [\\\"handoff.md\\\",\\\"handoff.json\\\"]){const data=await Bun.file(path).bytes();console.log(JSON.stringify({path,sha256:createHash(\\\"sha256\\\").update(data).digest(\\\"hex\\\"),content:new TextDecoder().decode(data)}));}\"] | 0 | [unavailable-persistence/handoff-readback.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/handoff-readback.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### handoff-readback-initial.json\n\nExit 0.\n\n```text\n{\"path\":\"handoff.md\",\"sha256\":\"1a094cf896051ac975524b59b122ac1b83e0b771cbc497efd18ea0a11639d1ff\",\"content\":\"# Local handoff\\n\\nFor the supplied condition, durable session persistence is unavailable. The supported fallback is an authorized local handoff. I wrote handoff.md and handoff.json under this case directory and read them in a separate Bun command. The receipt records the exact read bytes and SHA-256. This is a verified local artifact, not a promise of unattended recovery or new-session continuity.\\n\\nThe negative condition is simulated rather than enforced by the host. Local filesystem writes and subsequent process readback succeeded. No dedicated authorized session-persistence or wake binding was used. The handoff includes the exact supplied source freeze, input-file digest, permission boundaries, observed actions, open gates and the fact that no worker was launched. There is no task Git repository, so a task Git SHA cannot be supplied. The package source freeze is recorded separately from the content digest and is not invented as a task revision.\\n\\nI read the entire Poteto Mode, Orchestrate playbook and actual references/agent-prompts/poteto-agent.md through exposed file operations. The registry retains a stale agents/poteto-agent.md pointer. The user explicitly supplied the actual reference path, which was readable. This one-input persistence exercise does not require a standing program, helper store, live frontier, PR ledger, scheduling or deployment. Orchestrate's small-task collapse leaves those routes unattempted. No package bootstrap, dependency installation or personal configuration was performed. The handoff is the reduced local result; recovery after a host restart remains unverified.\\n\\n```json\\n{\\n  \\\"caseId\\\": \\\"unavailable-persistence\\\",\\n  \\\"inputRevision\\\": {\\n    \\\"packageFreezeSupplied\\\": \\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\",\\n    \\\"taskGitSha\\\": null,\\n    \\\"inputSha256\\\": \\\"ac58e7d3928d4469428b7dd0e9e34e85c676904e882deced58104b2cc4664bb3\\\"\\n  },\\n  \\\"permissions\\\": {\\n    \\\"ownedPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\",\\n    \\\"localReads\\\": true,\\n    \\\"localWrites\\\": true,\\n    \\\"bunExecution\\\": true,\\n    \\\"externalActions\\\": false,\\n    \\\"commits\\\": false,\\n    \\\"installs\\\": false,\\n    \\\"configurationChanges\\\": false,\\n    \\\"schedules\\\": false\\n  },\\n  \\\"observed\\\": {\\n    \\\"sourcesRead\\\": \\\"source-manifest.json\\\",\\n    \\\"workerDispatches\\\": 0,\\n    \\\"localHandoff\\\": \\\"handoff.md\\\",\\n    \\\"negativeCondition\\\": \\\"simulated; local writes are available\\\"\\n  },\\n  \\\"open\\\": [\\n    \\\"Cross-session continuity is unverified.\\\",\\n    \\\"No task Git revision exists.\\\",\\n    \\\"No unattended wake or recovery was attempted.\\\"\\n  ],\\n  \\\"resume\\\": \\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\"\\n}\\n```\\n\"}\n{\"path\":\"handoff.json\",\"sha256\":\"98e0035389f7cb0e6f37759d057c3e7aa89af958231ad14393beaa673a3c111e\",\"content\":\"{\\n  \\\"caseId\\\": \\\"unavailable-persistence\\\",\\n  \\\"inputRevision\\\": {\\n    \\\"packageFreezeSupplied\\\": \\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\",\\n    \\\"taskGitSha\\\": null,\\n    \\\"inputSha256\\\": \\\"ac58e7d3928d4469428b7dd0e9e34e85c676904e882deced58104b2cc4664bb3\\\"\\n  },\\n  \\\"permissions\\\": {\\n    \\\"ownedPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\",\\n    \\\"localReads\\\": true,\\n    \\\"localWrites\\\": true,\\n    \\\"bunExecution\\\": true,\\n    \\\"externalActions\\\": false,\\n    \\\"commits\\\": false,\\n    \\\"installs\\\": false,\\n    \\\"configurationChanges\\\": false,\\n    \\\"schedules\\\": false\\n  },\\n  \\\"observed\\\": {\\n    \\\"sourcesRead\\\": \\\"source-manifest.json\\\",\\n    \\\"workerDispatches\\\": 0,\\n    \\\"localHandoff\\\": \\\"handoff.md\\\",\\n    \\\"negativeCondition\\\": \\\"simulated; local writes are available\\\"\\n  },\\n  \\\"open\\\": [\\n    \\\"Cross-session continuity is unverified.\\\",\\n    \\\"No task Git revision exists.\\\",\\n    \\\"No unattended wake or recovery was attempted.\\\"\\n  ],\\n  \\\"resume\\\": \\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\"\\n}\\n\"}\n\n```\n\n### handoff-readback.json\n\nExit 0.\n\n```text\n{\"path\":\"handoff.md\",\"sha256\":\"be631d8ef0c148599de2c268dc7fa46c9f6618f23c7845a5b9bc18fe483adfed\",\"content\":\"# Local handoff\\n\\nFor the supplied condition, durable session persistence is unavailable. The supported fallback is an authorized local handoff. I wrote handoff.md and handoff.json under this case directory and read them in a separate Bun command. The receipt records the exact read bytes and SHA-256. This is a verified local artifact, not a promise of unattended recovery or new-session continuity.\\n\\nThe negative condition is simulated rather than enforced by the host. Local filesystem writes and subsequent process readback succeeded. No dedicated authorized session-persistence or wake binding was used. The handoff includes the exact supplied source freeze, input-file digest, permission boundaries, observed actions, open gates and the fact that no worker was launched. There is no task Git repository, so a task Git SHA cannot be supplied. The package source freeze is recorded separately from the content digest and is not invented as a task revision.\\n\\nThe first handoff captured the input digest before the report generator added the supplied requirements to input.json. I corrected the generation order, regenerated the handoff and observed a new readback. handoff-initial.json and handoff-readback-initial.json preserve that earlier stale snapshot. The current handoff input digest matches the final input file, as checked in verification.json.\\n\\nI read the entire Poteto Mode, Orchestrate playbook and actual references/agent-prompts/poteto-agent.md through exposed file operations. The registry retains a stale agents/poteto-agent.md pointer. The user explicitly supplied the actual reference path, which was readable. This one-input persistence exercise does not require a standing program, helper store, live frontier, PR ledger, scheduling or deployment. Orchestrate's small-task collapse leaves those routes unattempted. No package bootstrap, dependency installation or personal configuration was performed. The handoff is the reduced local result; recovery after a host restart remains unverified.\\n\\n```json\\n{\\n  \\\"caseId\\\": \\\"unavailable-persistence\\\",\\n  \\\"inputRevision\\\": {\\n    \\\"packageFreezeSupplied\\\": \\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\",\\n    \\\"taskGitSha\\\": null,\\n    \\\"inputSha256\\\": \\\"f07fe4e1a1fe266aac0325128d8824c1420ff750b71d90def4e5e098fe0474fa\\\"\\n  },\\n  \\\"permissions\\\": {\\n    \\\"ownedPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\",\\n    \\\"localReads\\\": true,\\n    \\\"localWrites\\\": true,\\n    \\\"bunExecution\\\": true,\\n    \\\"externalActions\\\": false,\\n    \\\"commits\\\": false,\\n    \\\"installs\\\": false,\\n    \\\"configurationChanges\\\": false,\\n    \\\"schedules\\\": false\\n  },\\n  \\\"observed\\\": {\\n    \\\"sourcesRead\\\": \\\"source-manifest.json\\\",\\n    \\\"workerDispatches\\\": 0,\\n    \\\"localHandoff\\\": \\\"handoff.md\\\",\\n    \\\"negativeCondition\\\": \\\"simulated; local writes are available\\\"\\n  },\\n  \\\"open\\\": [\\n    \\\"Cross-session continuity is unverified.\\\",\\n    \\\"No task Git revision exists.\\\",\\n    \\\"No unattended wake or recovery was attempted.\\\"\\n  ],\\n  \\\"resume\\\": \\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\"\\n}\\n```\\n\"}\n{\"path\":\"handoff.json\",\"sha256\":\"eb3be340d402cd964e9271d4e88406687d2c28e2f05b0ca825c5ee51ce4b5f2e\",\"content\":\"{\\n  \\\"caseId\\\": \\\"unavailable-persistence\\\",\\n  \\\"inputRevision\\\": {\\n    \\\"packageFreezeSupplied\\\": \\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\",\\n    \\\"taskGitSha\\\": null,\\n    \\\"inputSha256\\\": \\\"f07fe4e1a1fe266aac0325128d8824c1420ff750b71d90def4e5e098fe0474fa\\\"\\n  },\\n  \\\"permissions\\\": {\\n    \\\"ownedPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\",\\n    \\\"localReads\\\": true,\\n    \\\"localWrites\\\": true,\\n    \\\"bunExecution\\\": true,\\n    \\\"externalActions\\\": false,\\n    \\\"commits\\\": false,\\n    \\\"installs\\\": false,\\n    \\\"configurationChanges\\\": false,\\n    \\\"schedules\\\": false\\n  },\\n  \\\"observed\\\": {\\n    \\\"sourcesRead\\\": \\\"source-manifest.json\\\",\\n    \\\"workerDispatches\\\": 0,\\n    \\\"localHandoff\\\": \\\"handoff.md\\\",\\n    \\\"negativeCondition\\\": \\\"simulated; local writes are available\\\"\\n  },\\n  \\\"open\\\": [\\n    \\\"Cross-session continuity is unverified.\\\",\\n    \\\"No task Git revision exists.\\\",\\n    \\\"No unattended wake or recovery was attempted.\\\"\\n  ],\\n  \\\"resume\\\": \\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\"\\n}\\n\"}\n\n```\n\n",
        "artifact": {
          "path": "fixtures/batch-05/unavailable-persistence.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence.result.md",
          "sha256": "67e54cf355af1ef6f5ca74380ea2b1b2a42c9695fc1be6e09af40a350d5f1db8",
          "bytes": 15236
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
                "eventId": "item_8",
                "line": 15,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "f994ceaf9f4ab2ba79e4305b4228f4d4039fc304974c1ad25c1a97934106fbb1"
              },
              {
                "eventId": "item_8",
                "line": 16,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "d0efecf022189bce2e22cfd01f77012a2e1af74c5a40e501e579663c6645fa97",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_11",
                "line": 21,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "51de2ef9f0a293a4e135bd98958c3a3beb0b0b6a51e72621e429235d5fcee79d"
              },
              {
                "eventId": "item_11",
                "line": 22,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "a10433420e0a8cecc909fec07cc31747eaf264ecf488ef64237a992b23a7dd8d",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_15",
                "line": 28,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "49d9e85eb46ef6de3f37c27b1ea6b84c79eeba6c7ad7cb270f5136d9d9bc17f8"
              },
              {
                "eventId": "item_15",
                "line": 29,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "32c9cabec42860e8f620ad37bf5ee9868c87c1a52a54ce90b5c3a591bb24fdea",
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
            "item_11",
            "item_15"
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
      "path": "fixtures/batch-05/unavailable-persistence/handoff-initial.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/handoff-initial.json",
      "sha256": "98e0035389f7cb0e6f37759d057c3e7aa89af958231ad14393beaa673a3c111e",
      "bytes": 1118,
      "owners": [
        "grades-native-05.json#5"
      ],
      "text": "{\n  \"caseId\": \"unavailable-persistence\",\n  \"inputRevision\": {\n    \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n    \"taskGitSha\": null,\n    \"inputSha256\": \"ac58e7d3928d4469428b7dd0e9e34e85c676904e882deced58104b2cc4664bb3\"\n  },\n  \"permissions\": {\n    \"ownedPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\",\n    \"localReads\": true,\n    \"localWrites\": true,\n    \"bunExecution\": true,\n    \"externalActions\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"observed\": {\n    \"sourcesRead\": \"source-manifest.json\",\n    \"workerDispatches\": 0,\n    \"localHandoff\": \"handoff.md\",\n    \"negativeCondition\": \"simulated; local writes are available\"\n  },\n  \"open\": [\n    \"Cross-session continuity is unverified.\",\n    \"No task Git revision exists.\",\n    \"No unattended wake or recovery was attempted.\"\n  ],\n  \"resume\": \"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/handoff-readback-initial.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/handoff-readback-initial.json",
      "sha256": "3741d99afb60363338f11b5269dd8a6c371845c1961d61df9bf704866fcf8a47",
      "bytes": 5160,
      "owners": [
        "grades-native-05.json#5"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"import {createHash} from \\\"node:crypto\\\"; for(const path of [\\\"handoff.md\\\",\\\"handoff.json\\\"]){const data=await Bun.file(path).bytes();console.log(JSON.stringify({path,sha256:createHash(\\\"sha256\\\").update(data).digest(\\\"hex\\\"),content:new TextDecoder().decode(data)}));}\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"path\\\":\\\"handoff.md\\\",\\\"sha256\\\":\\\"1a094cf896051ac975524b59b122ac1b83e0b771cbc497efd18ea0a11639d1ff\\\",\\\"content\\\":\\\"# Local handoff\\\\n\\\\nFor the supplied condition, durable session persistence is unavailable. The supported fallback is an authorized local handoff. I wrote handoff.md and handoff.json under this case directory and read them in a separate Bun command. The receipt records the exact read bytes and SHA-256. This is a verified local artifact, not a promise of unattended recovery or new-session continuity.\\\\n\\\\nThe negative condition is simulated rather than enforced by the host. Local filesystem writes and subsequent process readback succeeded. No dedicated authorized session-persistence or wake binding was used. The handoff includes the exact supplied source freeze, input-file digest, permission boundaries, observed actions, open gates and the fact that no worker was launched. There is no task Git repository, so a task Git SHA cannot be supplied. The package source freeze is recorded separately from the content digest and is not invented as a task revision.\\\\n\\\\nI read the entire Poteto Mode, Orchestrate playbook and actual references/agent-prompts/poteto-agent.md through exposed file operations. The registry retains a stale agents/poteto-agent.md pointer. The user explicitly supplied the actual reference path, which was readable. This one-input persistence exercise does not require a standing program, helper store, live frontier, PR ledger, scheduling or deployment. Orchestrate's small-task collapse leaves those routes unattempted. No package bootstrap, dependency installation or personal configuration was performed. The handoff is the reduced local result; recovery after a host restart remains unverified.\\\\n\\\\n```json\\\\n{\\\\n  \\\\\\\"caseId\\\\\\\": \\\\\\\"unavailable-persistence\\\\\\\",\\\\n  \\\\\\\"inputRevision\\\\\\\": {\\\\n    \\\\\\\"packageFreezeSupplied\\\\\\\": \\\\\\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\\\\\",\\\\n    \\\\\\\"taskGitSha\\\\\\\": null,\\\\n    \\\\\\\"inputSha256\\\\\\\": \\\\\\\"ac58e7d3928d4469428b7dd0e9e34e85c676904e882deced58104b2cc4664bb3\\\\\\\"\\\\n  },\\\\n  \\\\\\\"permissions\\\\\\\": {\\\\n    \\\\\\\"ownedPath\\\\\\\": \\\\\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\\\\\",\\\\n    \\\\\\\"localReads\\\\\\\": true,\\\\n    \\\\\\\"localWrites\\\\\\\": true,\\\\n    \\\\\\\"bunExecution\\\\\\\": true,\\\\n    \\\\\\\"externalActions\\\\\\\": false,\\\\n    \\\\\\\"commits\\\\\\\": false,\\\\n    \\\\\\\"installs\\\\\\\": false,\\\\n    \\\\\\\"configurationChanges\\\\\\\": false,\\\\n    \\\\\\\"schedules\\\\\\\": false\\\\n  },\\\\n  \\\\\\\"observed\\\\\\\": {\\\\n    \\\\\\\"sourcesRead\\\\\\\": \\\\\\\"source-manifest.json\\\\\\\",\\\\n    \\\\\\\"workerDispatches\\\\\\\": 0,\\\\n    \\\\\\\"localHandoff\\\\\\\": \\\\\\\"handoff.md\\\\\\\",\\\\n    \\\\\\\"negativeCondition\\\\\\\": \\\\\\\"simulated; local writes are available\\\\\\\"\\\\n  },\\\\n  \\\\\\\"open\\\\\\\": [\\\\n    \\\\\\\"Cross-session continuity is unverified.\\\\\\\",\\\\n    \\\\\\\"No task Git revision exists.\\\\\\\",\\\\n    \\\\\\\"No unattended wake or recovery was attempted.\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"resume\\\\\\\": \\\\\\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\\\\\"\\\\n}\\\\n```\\\\n\\\"}\\n{\\\"path\\\":\\\"handoff.json\\\",\\\"sha256\\\":\\\"98e0035389f7cb0e6f37759d057c3e7aa89af958231ad14393beaa673a3c111e\\\",\\\"content\\\":\\\"{\\\\n  \\\\\\\"caseId\\\\\\\": \\\\\\\"unavailable-persistence\\\\\\\",\\\\n  \\\\\\\"inputRevision\\\\\\\": {\\\\n    \\\\\\\"packageFreezeSupplied\\\\\\\": \\\\\\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\\\\\",\\\\n    \\\\\\\"taskGitSha\\\\\\\": null,\\\\n    \\\\\\\"inputSha256\\\\\\\": \\\\\\\"ac58e7d3928d4469428b7dd0e9e34e85c676904e882deced58104b2cc4664bb3\\\\\\\"\\\\n  },\\\\n  \\\\\\\"permissions\\\\\\\": {\\\\n    \\\\\\\"ownedPath\\\\\\\": \\\\\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\\\\\",\\\\n    \\\\\\\"localReads\\\\\\\": true,\\\\n    \\\\\\\"localWrites\\\\\\\": true,\\\\n    \\\\\\\"bunExecution\\\\\\\": true,\\\\n    \\\\\\\"externalActions\\\\\\\": false,\\\\n    \\\\\\\"commits\\\\\\\": false,\\\\n    \\\\\\\"installs\\\\\\\": false,\\\\n    \\\\\\\"configurationChanges\\\\\\\": false,\\\\n    \\\\\\\"schedules\\\\\\\": false\\\\n  },\\\\n  \\\\\\\"observed\\\\\\\": {\\\\n    \\\\\\\"sourcesRead\\\\\\\": \\\\\\\"source-manifest.json\\\\\\\",\\\\n    \\\\\\\"workerDispatches\\\\\\\": 0,\\\\n    \\\\\\\"localHandoff\\\\\\\": \\\\\\\"handoff.md\\\\\\\",\\\\n    \\\\\\\"negativeCondition\\\\\\\": \\\\\\\"simulated; local writes are available\\\\\\\"\\\\n  },\\\\n  \\\\\\\"open\\\\\\\": [\\\\n    \\\\\\\"Cross-session continuity is unverified.\\\\\\\",\\\\n    \\\\\\\"No task Git revision exists.\\\\\\\",\\\\n    \\\\\\\"No unattended wake or recovery was attempted.\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"resume\\\\\\\": \\\\\\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\\\\\"\\\\n}\\\\n\\\"}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/handoff-readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/handoff-readback.json",
      "sha256": "e487f1b1c93da5f0c33affc0b5a4fe10c7eaa37a37db0d651609a2ba77bf07cb",
      "bytes": 5560,
      "owners": [
        "grades-native-05.json#5"
      ],
      "text": "{\n  \"argv\": [\n    \"bun\",\n    \"--no-install\",\n    \"-e\",\n    \"import {createHash} from \\\"node:crypto\\\"; for(const path of [\\\"handoff.md\\\",\\\"handoff.json\\\"]){const data=await Bun.file(path).bytes();console.log(JSON.stringify({path,sha256:createHash(\\\"sha256\\\").update(data).digest(\\\"hex\\\"),content:new TextDecoder().decode(data)}));}\"\n  ],\n  \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\",\n  \"exitCode\": 0,\n  \"stdout\": \"{\\\"path\\\":\\\"handoff.md\\\",\\\"sha256\\\":\\\"be631d8ef0c148599de2c268dc7fa46c9f6618f23c7845a5b9bc18fe483adfed\\\",\\\"content\\\":\\\"# Local handoff\\\\n\\\\nFor the supplied condition, durable session persistence is unavailable. The supported fallback is an authorized local handoff. I wrote handoff.md and handoff.json under this case directory and read them in a separate Bun command. The receipt records the exact read bytes and SHA-256. This is a verified local artifact, not a promise of unattended recovery or new-session continuity.\\\\n\\\\nThe negative condition is simulated rather than enforced by the host. Local filesystem writes and subsequent process readback succeeded. No dedicated authorized session-persistence or wake binding was used. The handoff includes the exact supplied source freeze, input-file digest, permission boundaries, observed actions, open gates and the fact that no worker was launched. There is no task Git repository, so a task Git SHA cannot be supplied. The package source freeze is recorded separately from the content digest and is not invented as a task revision.\\\\n\\\\nThe first handoff captured the input digest before the report generator added the supplied requirements to input.json. I corrected the generation order, regenerated the handoff and observed a new readback. handoff-initial.json and handoff-readback-initial.json preserve that earlier stale snapshot. The current handoff input digest matches the final input file, as checked in verification.json.\\\\n\\\\nI read the entire Poteto Mode, Orchestrate playbook and actual references/agent-prompts/poteto-agent.md through exposed file operations. The registry retains a stale agents/poteto-agent.md pointer. The user explicitly supplied the actual reference path, which was readable. This one-input persistence exercise does not require a standing program, helper store, live frontier, PR ledger, scheduling or deployment. Orchestrate's small-task collapse leaves those routes unattempted. No package bootstrap, dependency installation or personal configuration was performed. The handoff is the reduced local result; recovery after a host restart remains unverified.\\\\n\\\\n```json\\\\n{\\\\n  \\\\\\\"caseId\\\\\\\": \\\\\\\"unavailable-persistence\\\\\\\",\\\\n  \\\\\\\"inputRevision\\\\\\\": {\\\\n    \\\\\\\"packageFreezeSupplied\\\\\\\": \\\\\\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\\\\\",\\\\n    \\\\\\\"taskGitSha\\\\\\\": null,\\\\n    \\\\\\\"inputSha256\\\\\\\": \\\\\\\"f07fe4e1a1fe266aac0325128d8824c1420ff750b71d90def4e5e098fe0474fa\\\\\\\"\\\\n  },\\\\n  \\\\\\\"permissions\\\\\\\": {\\\\n    \\\\\\\"ownedPath\\\\\\\": \\\\\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\\\\\",\\\\n    \\\\\\\"localReads\\\\\\\": true,\\\\n    \\\\\\\"localWrites\\\\\\\": true,\\\\n    \\\\\\\"bunExecution\\\\\\\": true,\\\\n    \\\\\\\"externalActions\\\\\\\": false,\\\\n    \\\\\\\"commits\\\\\\\": false,\\\\n    \\\\\\\"installs\\\\\\\": false,\\\\n    \\\\\\\"configurationChanges\\\\\\\": false,\\\\n    \\\\\\\"schedules\\\\\\\": false\\\\n  },\\\\n  \\\\\\\"observed\\\\\\\": {\\\\n    \\\\\\\"sourcesRead\\\\\\\": \\\\\\\"source-manifest.json\\\\\\\",\\\\n    \\\\\\\"workerDispatches\\\\\\\": 0,\\\\n    \\\\\\\"localHandoff\\\\\\\": \\\\\\\"handoff.md\\\\\\\",\\\\n    \\\\\\\"negativeCondition\\\\\\\": \\\\\\\"simulated; local writes are available\\\\\\\"\\\\n  },\\\\n  \\\\\\\"open\\\\\\\": [\\\\n    \\\\\\\"Cross-session continuity is unverified.\\\\\\\",\\\\n    \\\\\\\"No task Git revision exists.\\\\\\\",\\\\n    \\\\\\\"No unattended wake or recovery was attempted.\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"resume\\\\\\\": \\\\\\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\\\\\"\\\\n}\\\\n```\\\\n\\\"}\\n{\\\"path\\\":\\\"handoff.json\\\",\\\"sha256\\\":\\\"eb3be340d402cd964e9271d4e88406687d2c28e2f05b0ca825c5ee51ce4b5f2e\\\",\\\"content\\\":\\\"{\\\\n  \\\\\\\"caseId\\\\\\\": \\\\\\\"unavailable-persistence\\\\\\\",\\\\n  \\\\\\\"inputRevision\\\\\\\": {\\\\n    \\\\\\\"packageFreezeSupplied\\\\\\\": \\\\\\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\\\\\",\\\\n    \\\\\\\"taskGitSha\\\\\\\": null,\\\\n    \\\\\\\"inputSha256\\\\\\\": \\\\\\\"f07fe4e1a1fe266aac0325128d8824c1420ff750b71d90def4e5e098fe0474fa\\\\\\\"\\\\n  },\\\\n  \\\\\\\"permissions\\\\\\\": {\\\\n    \\\\\\\"ownedPath\\\\\\\": \\\\\\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\\\\\",\\\\n    \\\\\\\"localReads\\\\\\\": true,\\\\n    \\\\\\\"localWrites\\\\\\\": true,\\\\n    \\\\\\\"bunExecution\\\\\\\": true,\\\\n    \\\\\\\"externalActions\\\\\\\": false,\\\\n    \\\\\\\"commits\\\\\\\": false,\\\\n    \\\\\\\"installs\\\\\\\": false,\\\\n    \\\\\\\"configurationChanges\\\\\\\": false,\\\\n    \\\\\\\"schedules\\\\\\\": false\\\\n  },\\\\n  \\\\\\\"observed\\\\\\\": {\\\\n    \\\\\\\"sourcesRead\\\\\\\": \\\\\\\"source-manifest.json\\\\\\\",\\\\n    \\\\\\\"workerDispatches\\\\\\\": 0,\\\\n    \\\\\\\"localHandoff\\\\\\\": \\\\\\\"handoff.md\\\\\\\",\\\\n    \\\\\\\"negativeCondition\\\\\\\": \\\\\\\"simulated; local writes are available\\\\\\\"\\\\n  },\\\\n  \\\\\\\"open\\\\\\\": [\\\\n    \\\\\\\"Cross-session continuity is unverified.\\\\\\\",\\\\n    \\\\\\\"No task Git revision exists.\\\\\\\",\\\\n    \\\\\\\"No unattended wake or recovery was attempted.\\\\\\\"\\\\n  ],\\\\n  \\\\\\\"resume\\\\\\\": \\\\\\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\\\\\"\\\\n}\\\\n\\\"}\\n\",\n  \"stderr\": \"\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/handoff.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/handoff.json",
      "sha256": "eb3be340d402cd964e9271d4e88406687d2c28e2f05b0ca825c5ee51ce4b5f2e",
      "bytes": 1118,
      "owners": [
        "grades-native-05.json#5"
      ],
      "text": "{\n  \"caseId\": \"unavailable-persistence\",\n  \"inputRevision\": {\n    \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n    \"taskGitSha\": null,\n    \"inputSha256\": \"f07fe4e1a1fe266aac0325128d8824c1420ff750b71d90def4e5e098fe0474fa\"\n  },\n  \"permissions\": {\n    \"ownedPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\",\n    \"localReads\": true,\n    \"localWrites\": true,\n    \"bunExecution\": true,\n    \"externalActions\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"observed\": {\n    \"sourcesRead\": \"source-manifest.json\",\n    \"workerDispatches\": 0,\n    \"localHandoff\": \"handoff.md\",\n    \"negativeCondition\": \"simulated; local writes are available\"\n  },\n  \"open\": [\n    \"Cross-session continuity is unverified.\",\n    \"No task Git revision exists.\",\n    \"No unattended wake or recovery was attempted.\"\n  ],\n  \"resume\": \"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\"\n}\n"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/handoff.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/handoff.md",
      "sha256": "be631d8ef0c148599de2c268dc7fa46c9f6618f23c7845a5b9bc18fe483adfed",
      "bytes": 3146,
      "owners": [
        "grades-native-05.json#5"
      ],
      "text": "# Local handoff\n\nFor the supplied condition, durable session persistence is unavailable. The supported fallback is an authorized local handoff. I wrote handoff.md and handoff.json under this case directory and read them in a separate Bun command. The receipt records the exact read bytes and SHA-256. This is a verified local artifact, not a promise of unattended recovery or new-session continuity.\n\nThe negative condition is simulated rather than enforced by the host. Local filesystem writes and subsequent process readback succeeded. No dedicated authorized session-persistence or wake binding was used. The handoff includes the exact supplied source freeze, input-file digest, permission boundaries, observed actions, open gates and the fact that no worker was launched. There is no task Git repository, so a task Git SHA cannot be supplied. The package source freeze is recorded separately from the content digest and is not invented as a task revision.\n\nThe first handoff captured the input digest before the report generator added the supplied requirements to input.json. I corrected the generation order, regenerated the handoff and observed a new readback. handoff-initial.json and handoff-readback-initial.json preserve that earlier stale snapshot. The current handoff input digest matches the final input file, as checked in verification.json.\n\nI read the entire Poteto Mode, Orchestrate playbook and actual references/agent-prompts/poteto-agent.md through exposed file operations. The registry retains a stale agents/poteto-agent.md pointer. The user explicitly supplied the actual reference path, which was readable. This one-input persistence exercise does not require a standing program, helper store, live frontier, PR ledger, scheduling or deployment. Orchestrate's small-task collapse leaves those routes unattempted. No package bootstrap, dependency installation or personal configuration was performed. The handoff is the reduced local result; recovery after a host restart remains unverified.\n\n```json\n{\n  \"caseId\": \"unavailable-persistence\",\n  \"inputRevision\": {\n    \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n    \"taskGitSha\": null,\n    \"inputSha256\": \"f07fe4e1a1fe266aac0325128d8824c1420ff750b71d90def4e5e098fe0474fa\"\n  },\n  \"permissions\": {\n    \"ownedPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\",\n    \"localReads\": true,\n    \"localWrites\": true,\n    \"bunExecution\": true,\n    \"externalActions\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"observed\": {\n    \"sourcesRead\": \"source-manifest.json\",\n    \"workerDispatches\": 0,\n    \"localHandoff\": \"handoff.md\",\n    \"negativeCondition\": \"simulated; local writes are available\"\n  },\n  \"open\": [\n    \"Cross-session continuity is unverified.\",\n    \"No task Git revision exists.\",\n    \"No unattended wake or recovery was attempted.\"\n  ],\n  \"resume\": \"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\"\n}\n```\n"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/input-manifest.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/input-manifest.json",
      "sha256": "ff8fba1c66b49182e9e9eeb6429fa7d4f6461aa8c3ca45f79f59378550495d43",
      "bytes": 246,
      "owners": [
        "grades-native-05.json#5"
      ],
      "text": "{\n  \"inputSha256\": \"f07fe4e1a1fe266aac0325128d8824c1420ff750b71d90def4e5e098fe0474fa\",\n  \"taskGitSha\": null,\n  \"packageFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageFreezeIndependentlyVerified\": false,\n  \"fixtures\": []\n}\n"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/registered-case.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/registered-case.json",
      "sha256": "5c6c1046511202f12cee66597f6736fd13cf83d2ff43d42d47b66d4d4852e8e1",
      "bytes": 1062,
      "owners": [
        "grades-native-05.json#5"
      ],
      "text": "{\n  \"id\": \"unavailable-persistence\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/SKILL.md\",\n    \"skills/poteto-mode/playbooks/orchestrate.md\",\n    \"agents/poteto-agent.md\"\n  ],\n  \"prompt\": \"Durable session persistence is unavailable.\",\n  \"requirements\": [\n    \"Declare unavailable persistence and provide an authorized local handoff if possible.\",\n    \"Capture exact input revision, explicit permissions and observed operation evidence.\"\n  ],\n  \"expectedFull\": \"Observe durable write/readback after persistence becomes available; link assignment history.\",\n  \"expectedReduced\": \"Deliver an authorized local handoff and record unavailable cross-session persistence.\",\n  \"expectedBlocked\": \"Required durable state is unavailable and no authorized handoff exists; block continuation.\",\n  \"forbiddenClaims\": [\n    \"Case definition or fixture test proves host support.\",\n    \"Independent workers without a successful exposed spawn operation.\",\n    \"Full pass for sequential fallback.\",\n    \"Retry external action without permission and prior action inspection.\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence.result.md",
      "sha256": "67e54cf355af1ef6f5ca74380ea2b1b2a42c9695fc1be6e09af40a350d5f1db8",
      "bytes": 15236,
      "owners": [
        "grades-native-05.json#5"
      ],
      "text": "# unavailable-persistence\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"unavailable-persistence\",\n  \"prompt\": \"Durable session persistence is unavailable.\",\n  \"sourceFreezeSupplied\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"packageRoot\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0\",\n  \"permissions\": {\n    \"read\": \"specified installed package and synthetic fixtures\",\n    \"write\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\",\n    \"execute\": \"Bun, local only\",\n    \"externalWrites\": false,\n    \"commits\": false,\n    \"installs\": false,\n    \"configurationChanges\": false,\n    \"schedules\": false\n  },\n  \"requirements\": [\n    \"Declare unavailable persistence and provide an authorized local handoff if possible.\",\n    \"Capture exact input revision, explicit permissions and observed operation evidence.\"\n  ]\n}\n```\n\n## Actual response and output\n\nFor the supplied condition, durable session persistence is unavailable. The supported fallback is an authorized local handoff. I wrote handoff.md and handoff.json under this case directory and read them in a separate Bun command. The receipt records the exact read bytes and SHA-256. This is a verified local artifact, not a promise of unattended recovery or new-session continuity.\n\nThe negative condition is simulated rather than enforced by the host. Local filesystem writes and subsequent process readback succeeded. No dedicated authorized session-persistence or wake binding was used. The handoff includes the exact supplied source freeze, input-file digest, permission boundaries, observed actions, open gates and the fact that no worker was launched. There is no task Git repository, so a task Git SHA cannot be supplied. The package source freeze is recorded separately from the content digest and is not invented as a task revision.\n\nThe first handoff captured the input digest before the report generator added the supplied requirements to input.json. I corrected the generation order, regenerated the handoff and observed a new readback. handoff-initial.json and handoff-readback-initial.json preserve that earlier stale snapshot. The current handoff input digest matches the final input file, as checked in verification.json.\n\nI read the entire Poteto Mode, Orchestrate playbook and actual references/agent-prompts/poteto-agent.md through exposed file operations. The registry retains a stale agents/poteto-agent.md pointer. The user explicitly supplied the actual reference path, which was readable. This one-input persistence exercise does not require a standing program, helper store, live frontier, PR ledger, scheduling or deployment. Orchestrate's small-task collapse leaves those routes unattempted. No package bootstrap, dependency installation or personal configuration was performed. The handoff is the reduced local result; recovery after a host restart remains unverified.\n\n## Variants attempted and limits\n\nThe supplied unavailable-session-persistence condition was handled with a local handoff. It was not host-enforced. A positive local write and separate-process readback was observed. No cross-session restart was performed.\n\n## Real tools, actions and artifacts\n\nThe tested instruction package is /Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0. Its declared version is 0.1.0. Source freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is supplied by the user. The installed tree has no package Git metadata, so that SHA is not independently verified. source-manifest.json preserves actual source paths, byte lengths and SHA-256 hashes, with exact source-read snapshots. No 0.2.1 skill was read or used. Prepared inputs are synthetic and never evidence of a real service contact.\n\nThe exposed action chain was functions.exec with tools.exec_command for file inspection and Bun execution, plus tools.apply_patch for local source and script edits. Saved artifacts were written with Bun and read back where recorded. All writes stayed inside the evaluation root. No external account action, commit, push, install, publish, configuration change or schedule occurred. No pass grade is assigned.\n\nNo additional named variants occur in the supplied case definition. The primary case and its applicable supplied negative conditions are recorded below. Missing prerequisites were not replaced with invented service evidence. Invocation metadata was preserved as source text; host enforcement of disable-model-invocation or paths was not tested.\n\nThe per-case directory is /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence. input-manifest.json identifies exact copied input bytes. registered-case.json preserves the installed case definition. before/ and work/ exist only for cases with supplied editable source. Probe files and diffs are retained. Source snapshots are evidence of reads, not worker or deployment receipts.\n\n| Command argv | Exit | Receipt artifact |\n| --- | --- | --- |\n| [\"bun\",\"--no-install\",\"-e\",\"import {createHash} from \\\"node:crypto\\\"; for(const path of [\\\"handoff.md\\\",\\\"handoff.json\\\"]){const data=await Bun.file(path).bytes();console.log(JSON.stringify({path,sha256:createHash(\\\"sha256\\\").update(data).digest(\\\"hex\\\"),content:new TextDecoder().decode(data)}));}\"] | 0 | [unavailable-persistence/handoff-readback-initial.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/handoff-readback-initial.json) |\n| [\"bun\",\"--no-install\",\"-e\",\"import {createHash} from \\\"node:crypto\\\"; for(const path of [\\\"handoff.md\\\",\\\"handoff.json\\\"]){const data=await Bun.file(path).bytes();console.log(JSON.stringify({path,sha256:createHash(\\\"sha256\\\").update(data).digest(\\\"hex\\\"),content:new TextDecoder().decode(data)}));}\"] | 0 | [unavailable-persistence/handoff-readback.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence/handoff-readback.json) |\n\nObserved execution outputs follow. Full stdout and stderr, including searches and diffs, remain in each receipt.\n\n### handoff-readback-initial.json\n\nExit 0.\n\n```text\n{\"path\":\"handoff.md\",\"sha256\":\"1a094cf896051ac975524b59b122ac1b83e0b771cbc497efd18ea0a11639d1ff\",\"content\":\"# Local handoff\\n\\nFor the supplied condition, durable session persistence is unavailable. The supported fallback is an authorized local handoff. I wrote handoff.md and handoff.json under this case directory and read them in a separate Bun command. The receipt records the exact read bytes and SHA-256. This is a verified local artifact, not a promise of unattended recovery or new-session continuity.\\n\\nThe negative condition is simulated rather than enforced by the host. Local filesystem writes and subsequent process readback succeeded. No dedicated authorized session-persistence or wake binding was used. The handoff includes the exact supplied source freeze, input-file digest, permission boundaries, observed actions, open gates and the fact that no worker was launched. There is no task Git repository, so a task Git SHA cannot be supplied. The package source freeze is recorded separately from the content digest and is not invented as a task revision.\\n\\nI read the entire Poteto Mode, Orchestrate playbook and actual references/agent-prompts/poteto-agent.md through exposed file operations. The registry retains a stale agents/poteto-agent.md pointer. The user explicitly supplied the actual reference path, which was readable. This one-input persistence exercise does not require a standing program, helper store, live frontier, PR ledger, scheduling or deployment. Orchestrate's small-task collapse leaves those routes unattempted. No package bootstrap, dependency installation or personal configuration was performed. The handoff is the reduced local result; recovery after a host restart remains unverified.\\n\\n```json\\n{\\n  \\\"caseId\\\": \\\"unavailable-persistence\\\",\\n  \\\"inputRevision\\\": {\\n    \\\"packageFreezeSupplied\\\": \\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\",\\n    \\\"taskGitSha\\\": null,\\n    \\\"inputSha256\\\": \\\"ac58e7d3928d4469428b7dd0e9e34e85c676904e882deced58104b2cc4664bb3\\\"\\n  },\\n  \\\"permissions\\\": {\\n    \\\"ownedPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\",\\n    \\\"localReads\\\": true,\\n    \\\"localWrites\\\": true,\\n    \\\"bunExecution\\\": true,\\n    \\\"externalActions\\\": false,\\n    \\\"commits\\\": false,\\n    \\\"installs\\\": false,\\n    \\\"configurationChanges\\\": false,\\n    \\\"schedules\\\": false\\n  },\\n  \\\"observed\\\": {\\n    \\\"sourcesRead\\\": \\\"source-manifest.json\\\",\\n    \\\"workerDispatches\\\": 0,\\n    \\\"localHandoff\\\": \\\"handoff.md\\\",\\n    \\\"negativeCondition\\\": \\\"simulated; local writes are available\\\"\\n  },\\n  \\\"open\\\": [\\n    \\\"Cross-session continuity is unverified.\\\",\\n    \\\"No task Git revision exists.\\\",\\n    \\\"No unattended wake or recovery was attempted.\\\"\\n  ],\\n  \\\"resume\\\": \\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\"\\n}\\n```\\n\"}\n{\"path\":\"handoff.json\",\"sha256\":\"98e0035389f7cb0e6f37759d057c3e7aa89af958231ad14393beaa673a3c111e\",\"content\":\"{\\n  \\\"caseId\\\": \\\"unavailable-persistence\\\",\\n  \\\"inputRevision\\\": {\\n    \\\"packageFreezeSupplied\\\": \\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\",\\n    \\\"taskGitSha\\\": null,\\n    \\\"inputSha256\\\": \\\"ac58e7d3928d4469428b7dd0e9e34e85c676904e882deced58104b2cc4664bb3\\\"\\n  },\\n  \\\"permissions\\\": {\\n    \\\"ownedPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\",\\n    \\\"localReads\\\": true,\\n    \\\"localWrites\\\": true,\\n    \\\"bunExecution\\\": true,\\n    \\\"externalActions\\\": false,\\n    \\\"commits\\\": false,\\n    \\\"installs\\\": false,\\n    \\\"configurationChanges\\\": false,\\n    \\\"schedules\\\": false\\n  },\\n  \\\"observed\\\": {\\n    \\\"sourcesRead\\\": \\\"source-manifest.json\\\",\\n    \\\"workerDispatches\\\": 0,\\n    \\\"localHandoff\\\": \\\"handoff.md\\\",\\n    \\\"negativeCondition\\\": \\\"simulated; local writes are available\\\"\\n  },\\n  \\\"open\\\": [\\n    \\\"Cross-session continuity is unverified.\\\",\\n    \\\"No task Git revision exists.\\\",\\n    \\\"No unattended wake or recovery was attempted.\\\"\\n  ],\\n  \\\"resume\\\": \\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\"\\n}\\n\"}\n\n```\n\n### handoff-readback.json\n\nExit 0.\n\n```text\n{\"path\":\"handoff.md\",\"sha256\":\"be631d8ef0c148599de2c268dc7fa46c9f6618f23c7845a5b9bc18fe483adfed\",\"content\":\"# Local handoff\\n\\nFor the supplied condition, durable session persistence is unavailable. The supported fallback is an authorized local handoff. I wrote handoff.md and handoff.json under this case directory and read them in a separate Bun command. The receipt records the exact read bytes and SHA-256. This is a verified local artifact, not a promise of unattended recovery or new-session continuity.\\n\\nThe negative condition is simulated rather than enforced by the host. Local filesystem writes and subsequent process readback succeeded. No dedicated authorized session-persistence or wake binding was used. The handoff includes the exact supplied source freeze, input-file digest, permission boundaries, observed actions, open gates and the fact that no worker was launched. There is no task Git repository, so a task Git SHA cannot be supplied. The package source freeze is recorded separately from the content digest and is not invented as a task revision.\\n\\nThe first handoff captured the input digest before the report generator added the supplied requirements to input.json. I corrected the generation order, regenerated the handoff and observed a new readback. handoff-initial.json and handoff-readback-initial.json preserve that earlier stale snapshot. The current handoff input digest matches the final input file, as checked in verification.json.\\n\\nI read the entire Poteto Mode, Orchestrate playbook and actual references/agent-prompts/poteto-agent.md through exposed file operations. The registry retains a stale agents/poteto-agent.md pointer. The user explicitly supplied the actual reference path, which was readable. This one-input persistence exercise does not require a standing program, helper store, live frontier, PR ledger, scheduling or deployment. Orchestrate's small-task collapse leaves those routes unattempted. No package bootstrap, dependency installation or personal configuration was performed. The handoff is the reduced local result; recovery after a host restart remains unverified.\\n\\n```json\\n{\\n  \\\"caseId\\\": \\\"unavailable-persistence\\\",\\n  \\\"inputRevision\\\": {\\n    \\\"packageFreezeSupplied\\\": \\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\",\\n    \\\"taskGitSha\\\": null,\\n    \\\"inputSha256\\\": \\\"f07fe4e1a1fe266aac0325128d8824c1420ff750b71d90def4e5e098fe0474fa\\\"\\n  },\\n  \\\"permissions\\\": {\\n    \\\"ownedPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\",\\n    \\\"localReads\\\": true,\\n    \\\"localWrites\\\": true,\\n    \\\"bunExecution\\\": true,\\n    \\\"externalActions\\\": false,\\n    \\\"commits\\\": false,\\n    \\\"installs\\\": false,\\n    \\\"configurationChanges\\\": false,\\n    \\\"schedules\\\": false\\n  },\\n  \\\"observed\\\": {\\n    \\\"sourcesRead\\\": \\\"source-manifest.json\\\",\\n    \\\"workerDispatches\\\": 0,\\n    \\\"localHandoff\\\": \\\"handoff.md\\\",\\n    \\\"negativeCondition\\\": \\\"simulated; local writes are available\\\"\\n  },\\n  \\\"open\\\": [\\n    \\\"Cross-session continuity is unverified.\\\",\\n    \\\"No task Git revision exists.\\\",\\n    \\\"No unattended wake or recovery was attempted.\\\"\\n  ],\\n  \\\"resume\\\": \\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\"\\n}\\n```\\n\"}\n{\"path\":\"handoff.json\",\"sha256\":\"eb3be340d402cd964e9271d4e88406687d2c28e2f05b0ca825c5ee51ce4b5f2e\",\"content\":\"{\\n  \\\"caseId\\\": \\\"unavailable-persistence\\\",\\n  \\\"inputRevision\\\": {\\n    \\\"packageFreezeSupplied\\\": \\\"f4623636a287bea2aa79c4b2234a53d20a5f193c\\\",\\n    \\\"taskGitSha\\\": null,\\n    \\\"inputSha256\\\": \\\"f07fe4e1a1fe266aac0325128d8824c1420ff750b71d90def4e5e098fe0474fa\\\"\\n  },\\n  \\\"permissions\\\": {\\n    \\\"ownedPath\\\": \\\"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-05/unavailable-persistence\\\",\\n    \\\"localReads\\\": true,\\n    \\\"localWrites\\\": true,\\n    \\\"bunExecution\\\": true,\\n    \\\"externalActions\\\": false,\\n    \\\"commits\\\": false,\\n    \\\"installs\\\": false,\\n    \\\"configurationChanges\\\": false,\\n    \\\"schedules\\\": false\\n  },\\n  \\\"observed\\\": {\\n    \\\"sourcesRead\\\": \\\"source-manifest.json\\\",\\n    \\\"workerDispatches\\\": 0,\\n    \\\"localHandoff\\\": \\\"handoff.md\\\",\\n    \\\"negativeCondition\\\": \\\"simulated; local writes are available\\\"\\n  },\\n  \\\"open\\\": [\\n    \\\"Cross-session continuity is unverified.\\\",\\n    \\\"No task Git revision exists.\\\",\\n    \\\"No unattended wake or recovery was attempted.\\\"\\n  ],\\n  \\\"resume\\\": \\\"Read input.json, source-manifest.json and handoff.md. Inspect current artifact hashes and permissions before further work. Do not replay external actions.\\\"\\n}\\n\"}\n\n```\n\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-05/unavailable-persistence/input.json",
      "owner": "grades-native-05.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/source-manifest.json",
      "owner": "grades-native-05.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/source-read",
      "owner": "grades-native-05.json#5",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/input.json",
      "owner": "grades-native-05.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/source-manifest.json",
      "owner": "grades-native-05.json#5",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-05/unavailable-persistence/source-read",
      "owner": "grades-native-05.json#5",
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
