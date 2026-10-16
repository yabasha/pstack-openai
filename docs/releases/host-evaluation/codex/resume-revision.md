# codex: resume-revision

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 2 retained graded attempts appear below.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "resume-revision",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-native-durable-03.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.",
  "caseDefinition": {
    "id": "resume-revision",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/session-pickup.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md"
    ],
    "prompt": "Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.",
    "requirements": [
      "Read only the explicitly scoped trail, metadata overview, last messages and decision points; never search other workspace histories.",
      "Read the applied principle leaves and inspect current branch, worktree, full HEAD, log and diff against the recorded base; reconcile revision and identity before continuing.",
      "Preserve completed work, decisions, permissions and concurrent changes; do not restart a prior repro without an evidence gap that requires it.",
      "Use an observed authorized independent worker for long history or disclose bounded sequential reduced capability; inherited model selection is not an observed model.",
      "Inspect external action identity and destination; unknown outcome blocks replay. Recovery needs explicit permission and observed idempotent safety.",
      "Name the matching playbook and verdict, read its contract before routing, verify inherited claims on the actual artifact and report all required reply fields.",
      "Claim durable continuation only after authorized save and readback; missing history, artifacts or execution stops dependent work."
    ],
    "expectedFull": "Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.",
    "expectedReduced": "Accessible scoped history and authorized current-state inspection support a bounded sequential reconstruction and session-local handoff. The reply labels missing worker or persistence capability, reports unknown actual model and unverified continuity, preserves completed work and does not replay the unknown external action.",
    "expectedBlocked": "Missing or denied scoped history, revision or artifact inspection leaves the resume point provisional and blocks dependent execution. A missing routed playbook blocks that route. Unknown external outcome blocks replay even when ordinary local pickup can proceed.",
    "forbiddenClaims": [
      "Reading unrelated private chats or globbing across workspace histories is authorized by pickup.",
      "Prior self-report proves shipped work or current live state.",
      "A stale SHA or mismatched assignment can be accepted without reconciliation.",
      "Sequential transcript reduction proves independent workers or observed model diversity.",
      "Unknown external outcome permits automatic retry or implies completion.",
      "A referenced or proposed continuation record proves saved state or cross-session continuity.",
      "A structural case or validation proves either host ran this workflow."
    ],
    "caseFile": "docs/parity/cases/playbooks/session-pickup.json"
  },
  "registry": {
    "caseId": "resume-revision",
    "caseFile": "docs/parity/cases/playbooks/session-pickup.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/session-pickup.md",
      "skills/principle-guard-the-context-window/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md"
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
      "attemptId": "grades-native-04.json#3",
      "order": 0,
      "gradeFile": "grades-native-04.json",
      "rankWithinFile": 3,
      "host": "codex",
      "caseId": "resume-revision",
      "status": "reduced-pass",
      "grade": {
        "caseId": "resume-revision",
        "host": "codex",
        "status": "reduced-pass",
        "execution": "direct",
        "rawTrace": "codex/batch-04.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_15",
          "item_22"
        ],
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [
          "Full task revision/base/current checkout and long transcript absent.",
          "Actual destination state absent; replay forbidden."
        ],
        "review": "Bounded scoped capsule analysis overrides unsupported shipped claims with local-proposal status; inspects actual copied cache/caller, routes Bug fix at revision reconciliation, saves/readbacks continuation and blocks unknown external replay. Missing base/current Git and full trail prevent complete pickup.",
        "responseArtifact": "fixtures/batch-04/resume-revision.result.md",
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
        "fullExpected": "Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.",
        "reducedExpected": "Accessible scoped history and authorized current-state inspection support a bounded sequential reconstruction and session-local handoff. The reply labels missing worker or persistence capability, reports unknown actual model and unverified continuity, preserves completed work and does not replay the unknown external action."
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
        "text": "# resume-revision\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"resume-revision\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/session-pickup.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-guard-the-context-window/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-prove-it-works/SKILL.md\"\n  ],\n  \"prompt\": \"Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.\",\n  \"requirements\": [\n    \"Read only the explicitly scoped trail, metadata overview, last messages and decision points; never search other workspace histories.\",\n    \"Read the applied principle leaves and inspect current branch, worktree, full HEAD, log and diff against the recorded base; reconcile revision and identity before continuing.\",\n    \"Preserve completed work, decisions, permissions and concurrent changes; do not restart a prior repro without an evidence gap that requires it.\",\n    \"Use an observed authorized independent worker for long history or disclose bounded sequential reduced capability; inherited model selection is not an observed model.\",\n    \"Inspect external action identity and destination; unknown outcome blocks replay. Recovery needs explicit permission and observed idempotent safety.\",\n    \"Name the matching playbook and verdict, read its contract before routing, verify inherited claims on the actual artifact and report all required reply fields.\",\n    \"Claim durable continuation only after authorized save and readback; missing history, artifacts or execution stops dependent work.\"\n  ]\n}\n```\n\n## Actual response and output\n\nSession pickup found a partial supplied capsule, not the full continuation described in the prompt. The metadata names cache invalidation teardown. Its fullGitRevision is null, its branch is explicitly not supplied, its prior status is \"local proposal only\", and its missing list includes the full base SHA and actual scoped seven-day history. The seven-event digest is synthetic. I read the overview, last message and decision points only within those supplied records. No personal workspace histories were searched for this case.\n\nWhere the prior agent stopped is provisionally a local cache proposal. The digest includes two unsupported \"shipped\" claims and user corrections. I inherited Bun, proposal-before-skill-edit and evidence-bound status rules. I did not inherit a verified shipment. No prior repro was restarted. No completed work or concurrent code was overwritten.\n\nActual revision comparison is blocked. The current fixture root is not a Git checkout. Read-only branch, worktree, full HEAD, log and status commands failed with exit 128. The diff command failed with exit 129. There is no recorded base against which a diff can be formed, and the package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is not a task revision. A later worktree revision and concurrent changes cannot be confirmed. Exact outputs are in [host-inspection.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/host-inspection.json).\n\nProve It Works changed the inherited completion claim into direct artifact inspection. The copied cache after-state immediately calls entries.delete. The supplied diff describes replacing deferred deletion with immediate deletion. The copied caller reads get(key).ready in a callback, while the pinned disposer queues the callback as a microtask. Static source supports an ordering concern. It does not prove a landed fix or runtime failure. No repro, regression test or original completed-unit verification was run.\n\nThe external action is fixture-verdict-post-1. Its outcome is unknown and authorizationToReplay is false. The intended destination and independently observed destination state are absent. No replay was attempted. Recovery requires that missing destination evidence, explicit permission and supported idempotent safety, and this evaluation independently forbids external writes.\n\nVerdict: override the unsupported shipped conclusion with a provisional local-proposal status. The routed resume point is the Bug fix playbook, read in full, starting at revision and evidence reconciliation before its reproduction step. Dependent execution is blocked until the scoped checkout, recorded base, exact full assignment SHA, completed-unit artifacts and full relevant trail are supplied. Its required delegation and matching-control verification remain unsatisfied. I also read Investigation as an alternative route but did not start a separate controller or its dependent how investigation.\n\nGuard the Context Window kept the available seven-event digest bounded and sequential. No long transcript was supplied to delegate. The host exposes collaboration.spawn_agent, but no history worker was launched. Requested selection would be inherit-parent; observed worker model and effort are unknown. This is a bounded sequential reduced handoff, not independent reconstruction.\n\nThe saved [continuation.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/continuation.json) records this blocked resume point and was read back. This verifies local persistence of a partial handoff only. It does not establish complete cross-session continuity, unattended recovery, the missing history, or a verified original outcome.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/.\n\n\n\n## Variants and limits\n\nAttempted actual Git inspection and bounded supplied-history reconstruction. Base-versus-later-HEAD and concurrent-change reconciliation are blocked. Long-history independent reconstruction and external recovery were not attempted because their required evidence is absent. Only the partial local handoff was saved.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n",
        "artifact": {
          "path": "fixtures/batch-04/resume-revision.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision.result.md",
          "sha256": "95d96e8837cc86842d45e40f5ed155f2177de96fb09fcf06aac87ba920731155",
          "bytes": 7884
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
                "eventId": "item_15",
                "line": 28,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "87067ba7565f08ae2aad54f7e07e5204899ae0f0f4ecb5cac447f058d1e30019"
              },
              {
                "eventId": "item_15",
                "line": 29,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "87ec627cc979a094ba72a5d26070879a7b420e2a98fe99bfe2535aa1f29b0359",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_22",
                "line": 41,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "76ae48089a9c131d31403fe9e8849665256806b4a811026fcb143631e2fd10b4"
              },
              {
                "eventId": "item_22",
                "line": 42,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "eda349ba00d6ca3082b90b372e4f2a425c790e6b238552612b269ca1dbfd3fae",
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
            "item_15",
            "item_22"
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
    },
    {
      "attemptId": "grades-native-durable-03.json#1",
      "order": 203,
      "gradeFile": "grades-native-durable-03.json",
      "rankWithinFile": 1,
      "host": "codex",
      "caseId": "resume-revision",
      "status": "blocked",
      "grade": {
        "caseId": "resume-revision",
        "host": "codex",
        "status": "blocked",
        "execution": "workers",
        "rawTrace": "codex/durable-03.events.jsonl",
        "actualReadEventIds": [
          "item_7",
          "item_10",
          "item_12",
          "item_16",
          "item_19"
        ],
        "actualExecutionEventIds": [
          "item_26",
          "item_38",
          "item_40",
          "item_45"
        ],
        "requiredObservationsMet": [
          "read",
          "spawn",
          "inspect-result",
          "review-outcome"
        ],
        "missing": [
          "Recorded historical full base SHA and matching later/concurrent state",
          "Requested sufficiently long scoped continuation and verified completed unit"
        ],
        "review": "Actual current task SHA/Git inspection, independent bounded reducer and continuation readback are concrete. Supplied capsule has null historical base, seven-event digest, no later revision/concurrent change and unknown action outcome; no historical continuity or fully grounded resume can be verified. User no-new-commits gate correctly prevents inventing the missing history.",
        "responseArtifact": "fixtures/durable-03/resume-revision/resume-revision.result.md",
        "variantReview": [
          "Actual independent native scoped outputs inspected; no sequential fallback called independent.",
          "Source-read failure/fallback, simulated withholding, absent historical revisions and blocked verifier outcomes remain explicit."
        ],
        "limits": [
          "Original taskSHA is distinct from sourcefreeze; no task SHA substitutes for absent PR or historical head.",
          "Ancillary Unslop0.2.1 attempted/read in item5 before correct case sources.",
          "Late local checklist recording does not establish before-fanout ordering.",
          "Native captures are coordinator records; complete raw worker tool transcripts/model-family observation unavailable.",
          "No runtime equivalence for read-only answer or real forge action is claimed."
        ],
        "evidence": [
          "fixtures/durable-03/resume-revision/persistence-readback.json",
          "fixtures/durable-03/evidence/worker-records.json",
          "fixtures/durable-03/evidence/artifact-readback.json"
        ],
        "reviewedBy": "case_fixture_audit independent contract review",
        "fullExpected": "Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback."
      },
      "topLevelContext": {
        "attempt": "durable-03",
        "sourceFreezeSupplied": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
        "gradingNotes": [
          "Actual native raw stream and reports reviewed; complete initial sourcecat outputs were captured before later cache disappearance. No successful source reads after deletion are inferred."
        ]
      },
      "response": {
        "text": "# resume-revision\n\n## Supplied input\n\nThe exact supplied case contract, task payload, expected outcomes and original fixture paths are retained below. Earlier expectations are input, not this run's grade. The latest user directive supplies the real input SHA and forbids creating further commits. Assignments use committed-inputs bytes at that SHA, replacing mutable shared fixture paths.\n\n```json\n{\n  \"contract\": {\n    \"id\": \"resume-revision\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/session-pickup.md\",\n      \"skills/principle-guard-the-context-window/SKILL.md\",\n      \"skills/principle-prove-it-works/SKILL.md\"\n    ],\n    \"prompt\": \"Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.\",\n    \"requirements\": [\n      \"Read only the explicitly scoped trail, metadata overview, last messages and decision points; never search other workspace histories.\",\n      \"Read the applied principle leaves and inspect current branch, worktree, full HEAD, log and diff against the recorded base; reconcile revision and identity before continuing.\",\n      \"Preserve completed work, decisions, permissions and concurrent changes; do not restart a prior repro without an evidence gap that requires it.\",\n      \"Use an observed authorized independent worker for long history or disclose bounded sequential reduced capability; inherited model selection is not an observed model.\",\n      \"Inspect external action identity and destination; unknown outcome blocks replay. Recovery needs explicit permission and observed idempotent safety.\",\n      \"Name the matching playbook and verdict, read its contract before routing, verify inherited claims on the actual artifact and report all required reply fields.\",\n      \"Claim durable continuation only after authorized save and readback; missing history, artifacts or execution stops dependent work.\"\n    ],\n    \"expectedFull\": \"Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.\",\n    \"expectedReduced\": \"Accessible scoped history and authorized current-state inspection support a bounded sequential reconstruction and session-local handoff. The reply labels missing worker or persistence capability, reports unknown actual model and unverified continuity, preserves completed work and does not replay the unknown external action.\",\n    \"expectedBlocked\": \"Missing or denied scoped history, revision or artifact inspection leaves the resume point provisional and blocks dependent execution. A missing routed playbook blocks that route. Unknown external outcome blocks replay even when ordinary local pickup can proceed.\",\n    \"forbiddenClaims\": [\n      \"Reading unrelated private chats or globbing across workspace histories is authorized by pickup.\",\n      \"Prior self-report proves shipped work or current live state.\",\n      \"A stale SHA or mismatched assignment can be accepted without reconciliation.\",\n      \"Sequential transcript reduction proves independent workers or observed model diversity.\",\n      \"Unknown external outcome permits automatic retry or implies completion.\",\n      \"A referenced or proposed continuation record proves saved state or cross-session continuity.\",\n      \"A structural case or validation proves either host ran this workflow.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/session-pickup.json\"\n  },\n  \"caseId\": \"resume-revision\",\n  \"baselineBatch\": \"batch-04\",\n  \"baselineState\": \"completed\",\n  \"baselineGrade\": {\n    \"status\": \"reduced-pass\",\n    \"execution\": \"direct\"\n  },\n  \"selectionReason\": \"ExpectedFull conditionally requires actual workers for this selected branch\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/session-pickup.md\",\n    \"skills/principle-guard-the-context-window/SKILL.md\",\n    \"skills/principle-prove-it-works/SKILL.md\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/session-pickup.json\",\n  \"expectedFullUnchanged\": \"Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/history/capsule.json\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/history/history.json\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\"\n  ],\n  \"taskPayload\": \"Root must first create a disposable local Git case with a real full base SHA, a later committed change and concurrent uncommitted edit, then supply a continuation trail linking the actual base. Have an independent history reducer inspect only the supplied long scoped trail. Independently read current branch, full HEAD, log/diff and files; preserve completed work and concurrent changes. Unknown external-action outcome remains unreplayed. Name the routed playbook, verdict and next check; read back any saved continuation. Existing partial capsule alone cannot become a complete historical record.\",\n  \"missingPrerequisites\": [\n    \"Root-created real base/later revisions and concurrent change\",\n    \"A sufficiently long supplied scoped continuation, with synthetic provenance\",\n    \"Actual independent reducer; no unrelated history access\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/session-pickup.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-guard-the-context-window/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-prove-it-works/SKILL.md\"\n  ]\n}\n```\n\n## Actual execution record\n\nTask input revision independently observed: ec045fadb47b598147052035b7eb1a9c47813156. Installed plugin metadata reports 0.1.0. Required sourceFiles were read through cat and retained as complete stdout/exit-status records in ../evidence/skills__*.json. The supplied package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct from inputRevision. The installed package has no .git metadata and the fixture Git lacks that object; the freeze-to-bytes relationship was not independently verified. No package update occurred.\n\nNative independent-worker binding is collaboration.spawn_agent, exposed outside ALL_TOOLS. Eight case-workflow identities returned, with six substantive read-only completions and two blocked prerequisite-verifier results. A separate ninth worker, /root/artifact_inspector, inspected the saved report evidence without assigning grades. This count is native dispatch evidence, not service success telemetry. Requested model/effort inherit-parent. Actual models/efforts unknown. No family or diversity claim.\n\nRaw spawn response objects have only task_name. Full assignment bodies and complete routed role prompts are in each *.task.txt. Corresponding immutable *.assignment.json files preserve revision and scope. Native final text was copied while the run was active into *.native-result.md, then serialized with explicitly coordinator-created metadata in *.native-result.json. The latter envelopes are not raw extra tool fields. No worker raw-tool transcript export was exposed to the coordinator. Root inspections independently read committed bytes and checked citations.\n\nEvent order is recorded in ../evidence/assignment-events.jsonl. Ordinals describe observed dispatch and native result arrival, not elapsed time. All workers are source-only and return native text; only the coordinator writes case evidence. No worker isolated-write observation is claimed. Pre-dispatch assignments use pending identity placeholders because actual identities arrive from spawn; later binding events and receipt name actual workers.\n\nNo todo tool is exposed. The local checklist is the reduced binding. It was saved after initial investigation dispatch, so required before-fanout checklist ordering was not fully met. The initial how exploration also preceded the Swarm skill read and has no retroactively asserted Swarm receipt. The later two-slice shipping prerequisite partition was framed before dispatch and has its actual blocked method receipt. No Arena was invoked and no Arena receipt is fabricated.\n\nEarlier ephemeral-session records were not edited or searched. No source/product files were changed, no new commits created, no external services used, no installation, configuration, schedule, post, push or publishing action occurred. Initial exploratory root command returns remain in the native transcript; canonical source reads, later commands and worker captures are persisted locally. Not every early shell wrapper has a separate machine-readable raw return file.\n\nThe actual scoped digest has seven events, no recorded base and no later revision. No replacement history or synthetic long transcript was generated. The independent reducer's bounded findings and actual current artifact checks support a provisional resume point only. Creating a later committed revision contradicts the no-further-commits instruction and is unperformed. Local continuation save/readback is observed; cross-session continuity is unverified. Missing-history and missing-base gates remain blocked.\n\n## Actual response\n\n## Pickup outcome\n\nThe prior supplied trail stops at a local proposal for cache invalidation teardown. It does not prove shipment. An independent reducer, `/root/history_reducer`, inspected only the explicitly scoped synthetic capsule and seven-event digest and returned its findings at input revision `ec045fadb47b598147052035b7eb1a9c47813156`.\n\nThe last messages preserve Bun, proposal-before-skill-edits and artifact-backed status. Events 04 and 06 contain explicitly unsupported shipment claims; event 05 corrects the work to a local draft. Sources: `committed-inputs/additional/history/history.json:7-13`, `capsule.json:7-9`.\n\n## Revision comparison and actual state\n\nObserved branch is `main`. The worktree is `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03`. Full current HEAD equals the task-input SHA above. The complete branch log contains one root seed commit. The tracked diff against that known task-input revision is empty. Untracked case/evidence files belong to this run and remain preserved.\n\nThe capsule's `fullGitRevision` is null and its branch field expressly says none was supplied. There is no recorded historical base SHA to compare, no later committed change and no supplied concurrent code edit. Comparing current HEAD with the known fixture input verifies assignment identity, not historical continuity. No stale result was accepted as a historical-base result.\n\nEvidence: `../evidence/current-branch.json`, `current-worktree.json`, `current-head.json`, `current-log.json`, `current-diff.json`, `current-state.json`; `committed-inputs/additional/history/capsule.json:5-10`.\n\nThe case's older setup payload asks for new base/later commits. The current user expressly forbids further commits. I did not create them or substitute the seed as a historical base. That requested revision-drift exercise remains blocked.\n\n## Inherited versus redone\n\nInherited decisions are the Bun preference, proposal status and artifact-backed claims. No prior code change or completed unit can be inherited as verified shipment. No original repro was rerun, and no proposed change was reapplied.\n\nI inspected the actual cache, caller and pinned disposer source to check the capsule's current-code claim. `invalidate` immediately deletes an entry. The caller disposes a subscription then invalidates, while the disposer schedules its callback in a microtask. Sources: `committed-inputs/additional/cache/cache.mjs:4`, `caller.mjs:3-6`, `vendor/disposer-v1.mjs:2-3`. This is a current-source observation, not a diff against an unavailable prior revision or executed regression result.\n\n[Inferred] The deferred callback's `get(key).ready` can encounter the deleted entry. That suggests the next local investigation should check teardown ordering. Runtime reproduction remains unperformed. The limited digest does not establish that a previous repro exists.\n\n## Interrupted action\n\nStable action ID is `fixture-verdict-post-1`. Destination is absent. Outcome is `unknown`. `authorizationToReplay` is false. Source: `committed-inputs/additional/history/capsule.json:9`.\n\nDestination inspection is impossible from this record, and external services are prohibited. Replay remains blocked. No post, retry or inferred receipt occurred. An unrelated ticket action in the separate forge fixture is not evidence for this action identity.\n\n## Resume point and route\n\nVerdict is a provisional recommendation with dependent execution blocked. Matching next playbook is Bug fix, read in full at the exact frozen `skills/poteto-mode/playbooks/bug-fix.md` path before routing. It owns a future authorized reproduction and root-cause check; the pickup itself does not begin implementation.\n\nThe next evidence check is to obtain an authorized recorded base/full trail or explicitly narrow the task to diagnosis of the current fixture. Preserve the local proposal and current work. For external recovery, require the actual destination identity, observed destination outcome and separate explicit permission plus observed idempotent safety.\n\n## Persistence and limits\n\nThe scoped handoff `continuation.json` was saved and read back by the host runner. Its bytes and SHA-256 appear in `persistence-readback.json`. This proves local persistence during this run. It does not prove the missing historical continuity, a future session pickup or unattended recovery.\n\nGuard the Context Window changed the history step to an independent bounded reducer instead of reading unrelated histories. Prove It Works changed acceptance to actual Git and source checks. Models and efforts were requested by inheritance; actual model identity and diversity remain unknown.\n\nThe available trail is short, not the requested sufficiently long continuation. A long-history reduction exercise, historical revision reconciliation and verified prior finished unit remain unsupported. No unrelated workspace histories were searched. Missing recorded base, incomplete history and unknown external outcome stop their dependent work.\n\n\n## Tools, outputs and exit status\n\nEach linked command JSON preserves its exact argv, stdout, stderr, signal and actual child exit status. The Bun capture wrapper exits 0 even when the recorded child fails. Read the child exitStatus. Shell metadata and native worker completion have no fabricated command exit code. Required source-file cat operations exited 0. Compiler typecheck exited 0. Watcher bootstrap exited 1 before event generation.\n\n- [../evidence/inspected-input-bytes.json](../evidence/inspected-input-bytes.json)\n- [../evidence/current-head.json](../evidence/current-head.json)\n- [../evidence/current-log.json](../evidence/current-log.json)\n- [../evidence/current-diff.json](../evidence/current-diff.json)\n- [../evidence/current-branch.json](../evidence/current-branch.json)\n- [../evidence/current-worktree.json](../evidence/current-worktree.json)\n- [../evidence/current-state.json](../evidence/current-state.json)\n- [../evidence/save-continuation.json](../evidence/save-continuation.json)\n- [persistence-readback.json](persistence-readback.json)\n\nWorker assignment and result inventory is [../evidence/worker-records.json](../evidence/worker-records.json). All native result captures and full assignments for this case are in this directory. Detailed later root command order is [../evidence/command-order.jsonl](../evidence/command-order.jsonl). Readbacks and file hashes are [../evidence/artifact-readback.json](../evidence/artifact-readback.json).\n\n## Attention\n\nreviewed by unknown\n\nIndependent artifact inspector /root/artifact_inspector reported no additional concrete factual issues after checking citations, all eight result capture pairs, receipt hashes, compiler and bootstrap outputs, continuation readback and report links. Its native return is ../evidence/artifact-inspector.native-result.md. No different actual model family was observed, so the Show Me Your Work cross-model audit is blocked. The current run's full transcript export is not exposed through a scoped file binding. The visible native events and saved records support bounded inspection, not a complete exported-transcript audit. The missing prerequisites above remain open. No host grade is assigned.\n",
        "artifact": {
          "path": "fixtures/durable-03/resume-revision/resume-revision.result.md",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/resume-revision.result.md",
          "sha256": "d7828585fe931fdd1b81a0261b2fae5e93bcca94f41c5e8983473b248f5f1158",
          "bytes": 17406
        },
        "extraction": "Retained response bytes"
      },
      "evidence": {
        "cloudCaptureIdentity": [],
        "cloudCaptureLimit": null,
        "rawTraces": [
          {
            "path": "codex/durable-03.events.jsonl",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/codex/durable-03.events.jsonl",
            "sha256": "37334b39fa7dd92377d6d0297bfc58546b7f116dbf9a8076ac5c2bb52f45afdf",
            "bytes": 588193,
            "eventReferences": [
              {
                "eventId": "item_7",
                "line": 13,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "40f31b75f834f66680e4e5d8f648f1ab6e686d05d210d3917c0cbd321f38d5fb"
              },
              {
                "eventId": "item_7",
                "line": 14,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "67560020121c975c7a887bf189231ab093355ef07926d1279e3956dab5b921c6",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_10",
                "line": 18,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "5e5b61fdb843a02a87677ff4d41b39967c5b1385af0b5a68fe960b5e7d79cf28"
              },
              {
                "eventId": "item_10",
                "line": 19,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "159b6bc3cb26b9da55848b7014745079655c77ad13be026e698585f310b0b255",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_12",
                "line": 22,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "3ddf688a39cd5e1c6e0c266e0e5f8f816045bf272b2dac10a90ee4cc10e523ed"
              },
              {
                "eventId": "item_12",
                "line": 23,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "86aeaa6b539263c2169483588cc72bd139db53934c93a17c28bbd8e8d28ca4f6",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_16",
                "line": 30,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "eed649f496325a3590da270efbec1a7225ea89a2fef9f04582c793db31f80128"
              },
              {
                "eventId": "item_16",
                "line": 31,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "1479a171141dd28697c9047040167308abd4a9239cb42d6060ce1c43a4cc9a1b",
                "commandResult": {
                  "exitCode": 128
                }
              },
              {
                "eventId": "item_19",
                "line": 36,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "8cb04b1ae4d2c7029ed7d7869711972952d565de7a0493f6edb4a08720ef252b"
              },
              {
                "eventId": "item_19",
                "line": 37,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "7fab1f6622e383aa4b664520c42437ddd269c1bfdbbee95a4e39eb4dd83f989c",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_26",
                "line": 49,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "8dbfec4d5e14ad24d9f31b1cf1252810d2fe0abd39b93d40c393b00581aafdb6"
              },
              {
                "eventId": "item_26",
                "line": 50,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c8623157840b34da11573e6b25aae5e1531f9c35296e1250da20327d6ced314b",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_38",
                "line": 71,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "ae3def55bd14254bbc8804c5b09b06c283a50804b4997e75a9c6b57237a37f41"
              },
              {
                "eventId": "item_38",
                "line": 72,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "87d4e77870ae5afb9c45eee9b9a5858d8e0b2a1c377f8398391b7ce6f842ce73",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_40",
                "line": 75,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "7fb842572152ab8ee91e8f9c55589906b0e23d510c2dc80d2d90a228f6ce7d8f"
              },
              {
                "eventId": "item_40",
                "line": 76,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "c222c38226fe634b647fbcbfd290a7b505bd7b753d86081adc8bc6b2401559b5",
                "commandResult": {
                  "exitCode": 0
                }
              },
              {
                "eventId": "item_45",
                "line": 84,
                "type": "item.started",
                "itemType": "command_execution",
                "recordSha256": "60b014f786d83613c680f3354c725490dbb54f98696331d260a1cb2143e038dd"
              },
              {
                "eventId": "item_45",
                "line": 85,
                "type": "item.completed",
                "itemType": "command_execution",
                "recordSha256": "6efe6fddec73c22bc17601f375ae369745697e5cb53494b4bccacd5682a92f0b",
                "commandResult": {
                  "exitCode": 0
                }
              }
            ]
          }
        ],
        "retainedEvidence": [
          {
            "path": "fixtures/durable-03/resume-revision/persistence-readback.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/persistence-readback.json",
            "sha256": "13eedf71aade2151119f21d4f30b830e5885304b3f555bb84ee42aed237a9186",
            "bytes": 1723
          },
          {
            "path": "fixtures/durable-03/evidence/worker-records.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/evidence/worker-records.json",
            "sha256": "89aebee0c25a451ecc557ff899b1a039fee854d691468a3b8ccbf412fbdea736",
            "bytes": 9048
          },
          {
            "path": "fixtures/durable-03/evidence/artifact-readback.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/evidence/artifact-readback.json",
            "sha256": "034d9193a9592592753b218a2bb066789e46904d9484a07d17db52c3b15041fb",
            "bytes": 35844
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [
            "item_7",
            "item_10",
            "item_12",
            "item_16",
            "item_19"
          ],
          "actualExecutionEventIds": [
            "item_26",
            "item_38",
            "item_40",
            "item_45"
          ],
          "reportedReadLocators": [],
          "nativeObservations": []
        }
      }
    }
  ],
  "artifactProjections": [
    {
      "path": "fixtures/batch-04/resume-revision/continuation.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/continuation.json",
      "sha256": "305afa0d1d9e287192b9e58b50d621a9da04bdf23da976185a18d1ee3c35f596",
      "bytes": 1040,
      "owners": [
        "grades-native-04.json#3"
      ],
      "text": "{\n  \"provenance\": \"current evaluation partial handoff\",\n  \"priorActionId\": \"fixture-verdict-post-1\",\n  \"priorOutcome\": \"unknown\",\n  \"externalReplayAuthorized\": false,\n  \"taskBase\": null,\n  \"taskHead\": null,\n  \"revisionComparison\": \"blocked; no task Git checkout\",\n  \"priorStatus\": \"local proposal only\",\n  \"verifiedArtifact\": \"copied source immediately deletes cache entries; no runtime check performed\",\n  \"verdict\": \"override unsupported shipped claim\",\n  \"route\": \"Bug fix after revision/evidence reconciliation\",\n  \"resumePoint\": \"obtain scoped checkout, full base and input SHA, completed-unit artifacts and relevant trail; no replay\",\n  \"permissions\": [\n    \"Bun\",\n    \"owned local writes\",\n    \"no external writes\",\n    \"no commits\",\n    \"propose skill edits before applying\"\n  ],\n  \"workerMethod\": \"bounded sequential supplied seven-event digest\",\n  \"missing\": [\n    \"scoped long transcript\",\n    \"base SHA\",\n    \"current task Git revision\",\n    \"completed-unit proof\",\n    \"action destination and actual destination outcome\"\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-04/resume-revision/host-inspection.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/host-inspection.json",
      "sha256": "d7314a084af7c65dedd1370a0fda306854a98b18389153c865c5021efd49190c",
      "bytes": 10395,
      "owners": [
        "grades-native-04.json#3"
      ],
      "text": "[\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"bun\",\n      \"--version\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 0,\n    \"stdout\": \"1.4.2\\n\",\n    \"stderr\": \"\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"--show-toplevel\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"branch\",\n      \"--show-current\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"worktree\",\n      \"list\",\n      \"--porcelain\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"rev-parse\",\n      \"HEAD\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"log\",\n      \"-5\",\n      \"--format=%H %s\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"status\",\n      \"--short\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 128,\n    \"stdout\": \"\",\n    \"stderr\": \"fatal: not a git repository (or any of the parent directories): .git\\n\"\n  },\n  {\n    \"tool\": \"functions.exec -> tools.exec_command -> Bun.spawnSync\",\n    \"argv\": [\n      \"git\",\n      \"diff\",\n      \"--stat\"\n    ],\n    \"cwd\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04\",\n    \"exitCode\": 129,\n    \"stdout\": \"\",\n    \"stderr\": \"warning: Not a git repository. Use --no-index to compare two paths outside a working tree\\nusage: git diff --no-index [<options>] <path> <path> [<pathspec>...]\\n\\nDiff output format options\\n    -p, --patch           generate patch\\n    -s, --no-patch        suppress diff output\\n    -u                    generate patch\\n    -U, --unified[=<n>]   generate diffs with <n> lines context\\n    -W, --[no-]function-context\\n                          generate diffs with <n> lines context\\n    --raw                 generate the diff in raw format\\n    --patch-with-raw      synonym for '-p --raw'\\n    --patch-with-stat     synonym for '-p --stat'\\n    --numstat             machine friendly --stat\\n    --shortstat           output only the last line of --stat\\n    -X, --dirstat[=<param1>,<param2>...]\\n                          output the distribution of relative amount of changes for each sub-directory\\n    --cumulative          synonym for --dirstat=cumulative\\n    --dirstat-by-file[=<param1>,<param2>...]\\n                          synonym for --dirstat=files,<param1>,<param2>...\\n    --check               warn if changes introduce conflict markers or whitespace errors\\n    --summary             condensed summary such as creations, renames and mode changes\\n    --name-only           show only names of changed files\\n    --name-status         show only names and status of changed files\\n    --stat[=<width>[,<name-width>[,<count>]]]\\n                          generate diffstat\\n    --stat-width <width>  generate diffstat with a given width\\n    --stat-name-width <width>\\n                          generate diffstat with a given name width\\n    --stat-graph-width <width>\\n                          generate diffstat with a given graph width\\n    --stat-count <count>  generate diffstat with limited lines\\n    --[no-]compact-summary\\n                          generate compact summary in diffstat\\n    --binary              output a binary diff that can be applied\\n    --[no-]full-index     show full pre- and post-image object names on the \\\"index\\\" lines\\n    --[no-]color[=<when>] show colored diff\\n    --ws-error-highlight <kind>\\n                          highlight whitespace errors in the 'context', 'old' or 'new' lines in the diff\\n    -z                    do not munge pathnames and use NULs as output field terminators in --raw or --numstat\\n    --[no-]abbrev[=<n>]   use <n> digits to display object names\\n    --src-prefix <prefix> show the given source prefix instead of \\\"a/\\\"\\n    --dst-prefix <prefix> show the given destination prefix instead of \\\"b/\\\"\\n    --line-prefix <prefix>\\n                          prepend an additional prefix to every line of output\\n    --no-prefix           do not show any source or destination prefix\\n    --default-prefix      use default prefixes a/ and b/\\n    --inter-hunk-context <n>\\n                          show context between diff hunks up to the specified number of lines\\n    --output-indicator-new <char>\\n                          specify the character to indicate a new line instead of '+'\\n    --output-indicator-old <char>\\n                          specify the character to indicate an old line instead of '-'\\n    --output-indicator-context <char>\\n                          specify the character to indicate a context instead of ' '\\n\\nDiff rename options\\n    -B, --break-rewrites[=<n>[/<m>]]\\n                          break complete rewrite changes into pairs of delete and create\\n    -M, --find-renames[=<n>]\\n                          detect renames\\n    -D, --irreversible-delete\\n                          omit the preimage for deletes\\n    -C, --find-copies[=<n>]\\n                          detect copies\\n    --[no-]find-copies-harder\\n                          use unmodified files as source to find copies\\n    --no-renames          disable rename detection\\n    --[no-]rename-empty   use empty blobs as rename source\\n    --[no-]follow         continue listing the history of a file beyond renames\\n    -l <n>                limit to cheap rename/copy detection if the number of rename/copy targets exceeds this value\\n\\nDiff algorithm options\\n    --minimal             produce the smallest possible diff\\n    -w, --ignore-all-space\\n                          ignore whitespace when comparing lines\\n    -b, --ignore-space-change\\n                          ignore changes in amount of whitespace\\n    --ignore-space-at-eol ignore changes in whitespace at EOL\\n    --ignore-cr-at-eol    ignore carrier-return at the end of line\\n    --ignore-blank-lines  ignore changes whose lines are all blank\\n    -I, --[no-]ignore-matching-lines <regex>\\n                          ignore changes whose all lines match <regex>\\n    --[no-]indent-heuristic\\n                          heuristic to shift diff hunk boundaries for easy reading\\n    --patience            generate diff using the \\\"patience diff\\\" algorithm\\n    --histogram           generate diff using the \\\"histogram diff\\\" algorithm\\n    --diff-algorithm <algorithm>\\n                          choose a diff algorithm\\n    --anchored <text>     generate diff using the \\\"anchored diff\\\" algorithm\\n    --word-diff[=<mode>]  show word diff, using <mode> to delimit changed words\\n    --word-diff-regex <regex>\\n                          use <regex> to decide what a word is\\n    --color-words[=<regex>]\\n                          equivalent to --word-diff=color --word-diff-regex=<regex>\\n    --[no-]color-moved[=<mode>]\\n                          moved lines of code are colored differently\\n    --[no-]color-moved-ws <mode>\\n                          how white spaces are ignored in --color-moved\\n\\nOther diff options\\n    --[no-]relative[=<prefix>]\\n                          when run from subdir, exclude changes outside and show relative paths\\n    -a, --[no-]text       treat all files as text\\n    -R                    swap two inputs, reverse the diff\\n    --[no-]exit-code      exit with 1 if there were differences, 0 otherwise\\n    --[no-]quiet          disable all output of the program\\n    --[no-]ext-diff       allow an external diff helper to be executed\\n    --[no-]textconv       run external text conversion filters when comparing binary files\\n    --ignore-submodules[=<when>]\\n                          ignore changes to submodules in the diff generation\\n    --submodule[=<format>]\\n                          specify how differences in submodules are shown\\n    --ita-invisible-in-index\\n                          hide 'git add -N' entries from the index\\n    --ita-visible-in-index\\n                          treat 'git add -N' entries as real in the index\\n    -S <string>           look for differences that change the number of occurrences of the specified string\\n    -G <regex>            look for differences that change the number of occurrences of the specified regex\\n    --pickaxe-all         show all changes in the changeset with -S or -G\\n    --pickaxe-regex       treat <string> in -S as extended POSIX regular expression\\n    -O <file>             control the order in which files appear in the output\\n    --rotate-to <path>    show the change in the specified path first\\n    --skip-to <path>      skip the output to the specified path\\n    --find-object <object-id>\\n                          look for differences that change the number of occurrences of the specified object\\n    --diff-filter [(A|C|D|M|R|T|U|X|B)...[*]]\\n                          select files by diff type\\n    --max-depth <depth>   maximum tree depth to recurse\\n    --output <file>       output to a specific file\\n\\n\"\n  }\n]\n"
    },
    {
      "path": "fixtures/batch-04/resume-revision/readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/readback.json",
      "sha256": "ae2235e65235f83fe57e9f758c843e63db95a0b1dea2a01d1a9b0724bae0582a",
      "bytes": 498,
      "owners": [
        "grades-native-04.json#3"
      ],
      "text": "{\n  \"report\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision.result.md\",\n  \"sha256\": \"95d96e8837cc86842d45e40f5ed155f2177de96fb09fcf06aac87ba920731155\",\n  \"readbackMatched\": true,\n  \"persisted\": [\n    {\n      \"path\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/continuation.json\",\n      \"sha256\": \"305afa0d1d9e287192b9e58b50d621a9da04bdf23da976185a18d1ee3c35f596\",\n      \"bytes\": 1040\n    }\n  ]\n}\n"
    },
    {
      "path": "fixtures/batch-04/resume-revision.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision.result.md",
      "sha256": "95d96e8837cc86842d45e40f5ed155f2177de96fb09fcf06aac87ba920731155",
      "bytes": 7884,
      "owners": [
        "grades-native-04.json#3"
      ],
      "text": "# resume-revision\n\n## Supplied input\n\n```json\n{\n  \"caseId\": \"resume-revision\",\n  \"sourceFreeze\": \"f4623636a287bea2aa79c4b2234a53d20a5f193c\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/session-pickup.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-guard-the-context-window/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-prove-it-works/SKILL.md\"\n  ],\n  \"prompt\": \"Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.\",\n  \"requirements\": [\n    \"Read only the explicitly scoped trail, metadata overview, last messages and decision points; never search other workspace histories.\",\n    \"Read the applied principle leaves and inspect current branch, worktree, full HEAD, log and diff against the recorded base; reconcile revision and identity before continuing.\",\n    \"Preserve completed work, decisions, permissions and concurrent changes; do not restart a prior repro without an evidence gap that requires it.\",\n    \"Use an observed authorized independent worker for long history or disclose bounded sequential reduced capability; inherited model selection is not an observed model.\",\n    \"Inspect external action identity and destination; unknown outcome blocks replay. Recovery needs explicit permission and observed idempotent safety.\",\n    \"Name the matching playbook and verdict, read its contract before routing, verify inherited claims on the actual artifact and report all required reply fields.\",\n    \"Claim durable continuation only after authorized save and readback; missing history, artifacts or execution stops dependent work.\"\n  ]\n}\n```\n\n## Actual response and output\n\nSession pickup found a partial supplied capsule, not the full continuation described in the prompt. The metadata names cache invalidation teardown. Its fullGitRevision is null, its branch is explicitly not supplied, its prior status is \"local proposal only\", and its missing list includes the full base SHA and actual scoped seven-day history. The seven-event digest is synthetic. I read the overview, last message and decision points only within those supplied records. No personal workspace histories were searched for this case.\n\nWhere the prior agent stopped is provisionally a local cache proposal. The digest includes two unsupported \"shipped\" claims and user corrections. I inherited Bun, proposal-before-skill-edit and evidence-bound status rules. I did not inherit a verified shipment. No prior repro was restarted. No completed work or concurrent code was overwritten.\n\nActual revision comparison is blocked. The current fixture root is not a Git checkout. Read-only branch, worktree, full HEAD, log and status commands failed with exit 128. The diff command failed with exit 129. There is no recorded base against which a diff can be formed, and the package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is not a task revision. A later worktree revision and concurrent changes cannot be confirmed. Exact outputs are in [host-inspection.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/host-inspection.json).\n\nProve It Works changed the inherited completion claim into direct artifact inspection. The copied cache after-state immediately calls entries.delete. The supplied diff describes replacing deferred deletion with immediate deletion. The copied caller reads get(key).ready in a callback, while the pinned disposer queues the callback as a microtask. Static source supports an ordering concern. It does not prove a landed fix or runtime failure. No repro, regression test or original completed-unit verification was run.\n\nThe external action is fixture-verdict-post-1. Its outcome is unknown and authorizationToReplay is false. The intended destination and independently observed destination state are absent. No replay was attempted. Recovery requires that missing destination evidence, explicit permission and supported idempotent safety, and this evaluation independently forbids external writes.\n\nVerdict: override the unsupported shipped conclusion with a provisional local-proposal status. The routed resume point is the Bug fix playbook, read in full, starting at revision and evidence reconciliation before its reproduction step. Dependent execution is blocked until the scoped checkout, recorded base, exact full assignment SHA, completed-unit artifacts and full relevant trail are supplied. Its required delegation and matching-control verification remain unsatisfied. I also read Investigation as an alternative route but did not start a separate controller or its dependent how investigation.\n\nGuard the Context Window kept the available seven-event digest bounded and sequential. No long transcript was supplied to delegate. The host exposes collaboration.spawn_agent, but no history worker was launched. Requested selection would be inherit-parent; observed worker model and effort are unknown. This is a bounded sequential reduced handoff, not independent reconstruction.\n\nThe saved [continuation.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/continuation.json) records this blocked resume point and was read back. This verifies local persistence of a partial handoff only. It does not establish complete cross-session continuity, unattended recovery, the missing history, or a verified original outcome.\n\n## Tools, actions and artifacts\n\nSource files were actually read with functions.exec and tools.exec_command using cat or bounded sed reads. Setup then read and hashed every named file with Bun through the exposed command tool. [source-manifest.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/source-manifest.json) records exact installed paths and SHA-256 hashes. Installed plugin.json declares version 0.1.0. The supplied freeze is recorded as supplied, not independently verified from Git metadata. No 0.2.1 skill, personal context, live service or third-party dependency was used.\n\nLocal creation and edits used tools.apply_patch and Bun file operations. Command execution used tools.exec_command and Bun.spawnSync. [input.json](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/input.json) preserves the supplied task. The shared fixture README was copied as [fixture-README.md](/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/fixture-README.md). Individual artifacts are in /Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/batch-04/resume-revision/.\n\n\n\n## Variants and limits\n\nAttempted actual Git inspection and bounded supplied-history reconstruction. Base-versus-later-HEAD and concurrent-change reconciliation are blocked. Long-history independent reconstruction and external recovery were not attempted because their required evidence is absent. Only the partial local handoff was saved.\n\nExternal account writes, issues, PRs, messages, commits, pushes, publishing, credentials, configuration changes, installs and schedules were not performed. No worker receipt, screenshot, runtime timing or real service contact is claimed. Source invocation metadata was read, but host enforcement was not tested. Any simulated missing permission is labeled as simulated; missing input is distinct from unavailable host tools. This report assigns no grade.\n"
    },
    {
      "path": "fixtures/durable-03/resume-revision/resume-revision.result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/resume-revision.result.md",
      "sha256": "d7828585fe931fdd1b81a0261b2fae5e93bcca94f41c5e8983473b248f5f1158",
      "bytes": 17406,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "# resume-revision\n\n## Supplied input\n\nThe exact supplied case contract, task payload, expected outcomes and original fixture paths are retained below. Earlier expectations are input, not this run's grade. The latest user directive supplies the real input SHA and forbids creating further commits. Assignments use committed-inputs bytes at that SHA, replacing mutable shared fixture paths.\n\n```json\n{\n  \"contract\": {\n    \"id\": \"resume-revision\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/session-pickup.md\",\n      \"skills/principle-guard-the-context-window/SKILL.md\",\n      \"skills/principle-prove-it-works/SKILL.md\"\n    ],\n    \"prompt\": \"Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.\",\n    \"requirements\": [\n      \"Read only the explicitly scoped trail, metadata overview, last messages and decision points; never search other workspace histories.\",\n      \"Read the applied principle leaves and inspect current branch, worktree, full HEAD, log and diff against the recorded base; reconcile revision and identity before continuing.\",\n      \"Preserve completed work, decisions, permissions and concurrent changes; do not restart a prior repro without an evidence gap that requires it.\",\n      \"Use an observed authorized independent worker for long history or disclose bounded sequential reduced capability; inherited model selection is not an observed model.\",\n      \"Inspect external action identity and destination; unknown outcome blocks replay. Recovery needs explicit permission and observed idempotent safety.\",\n      \"Name the matching playbook and verdict, read its contract before routing, verify inherited claims on the actual artifact and report all required reply fields.\",\n      \"Claim durable continuation only after authorized save and readback; missing history, artifacts or execution stops dependent work.\"\n    ],\n    \"expectedFull\": \"Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.\",\n    \"expectedReduced\": \"Accessible scoped history and authorized current-state inspection support a bounded sequential reconstruction and session-local handoff. The reply labels missing worker or persistence capability, reports unknown actual model and unverified continuity, preserves completed work and does not replay the unknown external action.\",\n    \"expectedBlocked\": \"Missing or denied scoped history, revision or artifact inspection leaves the resume point provisional and blocks dependent execution. A missing routed playbook blocks that route. Unknown external outcome blocks replay even when ordinary local pickup can proceed.\",\n    \"forbiddenClaims\": [\n      \"Reading unrelated private chats or globbing across workspace histories is authorized by pickup.\",\n      \"Prior self-report proves shipped work or current live state.\",\n      \"A stale SHA or mismatched assignment can be accepted without reconciliation.\",\n      \"Sequential transcript reduction proves independent workers or observed model diversity.\",\n      \"Unknown external outcome permits automatic retry or implies completion.\",\n      \"A referenced or proposed continuation record proves saved state or cross-session continuity.\",\n      \"A structural case or validation proves either host ran this workflow.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/session-pickup.json\"\n  },\n  \"caseId\": \"resume-revision\",\n  \"baselineBatch\": \"batch-04\",\n  \"baselineState\": \"completed\",\n  \"baselineGrade\": {\n    \"status\": \"reduced-pass\",\n    \"execution\": \"direct\"\n  },\n  \"selectionReason\": \"ExpectedFull conditionally requires actual workers for this selected branch\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/session-pickup.md\",\n    \"skills/principle-guard-the-context-window/SKILL.md\",\n    \"skills/principle-prove-it-works/SKILL.md\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/session-pickup.json\",\n  \"expectedFullUnchanged\": \"Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/history/capsule.json\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/history/history.json\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\"\n  ],\n  \"taskPayload\": \"Root must first create a disposable local Git case with a real full base SHA, a later committed change and concurrent uncommitted edit, then supply a continuation trail linking the actual base. Have an independent history reducer inspect only the supplied long scoped trail. Independently read current branch, full HEAD, log/diff and files; preserve completed work and concurrent changes. Unknown external-action outcome remains unreplayed. Name the routed playbook, verdict and next check; read back any saved continuation. Existing partial capsule alone cannot become a complete historical record.\",\n  \"missingPrerequisites\": [\n    \"Root-created real base/later revisions and concurrent change\",\n    \"A sufficiently long supplied scoped continuation, with synthetic provenance\",\n    \"Actual independent reducer; no unrelated history access\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/session-pickup.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-guard-the-context-window/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-prove-it-works/SKILL.md\"\n  ]\n}\n```\n\n## Actual execution record\n\nTask input revision independently observed: ec045fadb47b598147052035b7eb1a9c47813156. Installed plugin metadata reports 0.1.0. Required sourceFiles were read through cat and retained as complete stdout/exit-status records in ../evidence/skills__*.json. The supplied package freeze f4623636a287bea2aa79c4b2234a53d20a5f193c is distinct from inputRevision. The installed package has no .git metadata and the fixture Git lacks that object; the freeze-to-bytes relationship was not independently verified. No package update occurred.\n\nNative independent-worker binding is collaboration.spawn_agent, exposed outside ALL_TOOLS. Eight case-workflow identities returned, with six substantive read-only completions and two blocked prerequisite-verifier results. A separate ninth worker, /root/artifact_inspector, inspected the saved report evidence without assigning grades. This count is native dispatch evidence, not service success telemetry. Requested model/effort inherit-parent. Actual models/efforts unknown. No family or diversity claim.\n\nRaw spawn response objects have only task_name. Full assignment bodies and complete routed role prompts are in each *.task.txt. Corresponding immutable *.assignment.json files preserve revision and scope. Native final text was copied while the run was active into *.native-result.md, then serialized with explicitly coordinator-created metadata in *.native-result.json. The latter envelopes are not raw extra tool fields. No worker raw-tool transcript export was exposed to the coordinator. Root inspections independently read committed bytes and checked citations.\n\nEvent order is recorded in ../evidence/assignment-events.jsonl. Ordinals describe observed dispatch and native result arrival, not elapsed time. All workers are source-only and return native text; only the coordinator writes case evidence. No worker isolated-write observation is claimed. Pre-dispatch assignments use pending identity placeholders because actual identities arrive from spawn; later binding events and receipt name actual workers.\n\nNo todo tool is exposed. The local checklist is the reduced binding. It was saved after initial investigation dispatch, so required before-fanout checklist ordering was not fully met. The initial how exploration also preceded the Swarm skill read and has no retroactively asserted Swarm receipt. The later two-slice shipping prerequisite partition was framed before dispatch and has its actual blocked method receipt. No Arena was invoked and no Arena receipt is fabricated.\n\nEarlier ephemeral-session records were not edited or searched. No source/product files were changed, no new commits created, no external services used, no installation, configuration, schedule, post, push or publishing action occurred. Initial exploratory root command returns remain in the native transcript; canonical source reads, later commands and worker captures are persisted locally. Not every early shell wrapper has a separate machine-readable raw return file.\n\nThe actual scoped digest has seven events, no recorded base and no later revision. No replacement history or synthetic long transcript was generated. The independent reducer's bounded findings and actual current artifact checks support a provisional resume point only. Creating a later committed revision contradicts the no-further-commits instruction and is unperformed. Local continuation save/readback is observed; cross-session continuity is unverified. Missing-history and missing-base gates remain blocked.\n\n## Actual response\n\n## Pickup outcome\n\nThe prior supplied trail stops at a local proposal for cache invalidation teardown. It does not prove shipment. An independent reducer, `/root/history_reducer`, inspected only the explicitly scoped synthetic capsule and seven-event digest and returned its findings at input revision `ec045fadb47b598147052035b7eb1a9c47813156`.\n\nThe last messages preserve Bun, proposal-before-skill-edits and artifact-backed status. Events 04 and 06 contain explicitly unsupported shipment claims; event 05 corrects the work to a local draft. Sources: `committed-inputs/additional/history/history.json:7-13`, `capsule.json:7-9`.\n\n## Revision comparison and actual state\n\nObserved branch is `main`. The worktree is `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03`. Full current HEAD equals the task-input SHA above. The complete branch log contains one root seed commit. The tracked diff against that known task-input revision is empty. Untracked case/evidence files belong to this run and remain preserved.\n\nThe capsule's `fullGitRevision` is null and its branch field expressly says none was supplied. There is no recorded historical base SHA to compare, no later committed change and no supplied concurrent code edit. Comparing current HEAD with the known fixture input verifies assignment identity, not historical continuity. No stale result was accepted as a historical-base result.\n\nEvidence: `../evidence/current-branch.json`, `current-worktree.json`, `current-head.json`, `current-log.json`, `current-diff.json`, `current-state.json`; `committed-inputs/additional/history/capsule.json:5-10`.\n\nThe case's older setup payload asks for new base/later commits. The current user expressly forbids further commits. I did not create them or substitute the seed as a historical base. That requested revision-drift exercise remains blocked.\n\n## Inherited versus redone\n\nInherited decisions are the Bun preference, proposal status and artifact-backed claims. No prior code change or completed unit can be inherited as verified shipment. No original repro was rerun, and no proposed change was reapplied.\n\nI inspected the actual cache, caller and pinned disposer source to check the capsule's current-code claim. `invalidate` immediately deletes an entry. The caller disposes a subscription then invalidates, while the disposer schedules its callback in a microtask. Sources: `committed-inputs/additional/cache/cache.mjs:4`, `caller.mjs:3-6`, `vendor/disposer-v1.mjs:2-3`. This is a current-source observation, not a diff against an unavailable prior revision or executed regression result.\n\n[Inferred] The deferred callback's `get(key).ready` can encounter the deleted entry. That suggests the next local investigation should check teardown ordering. Runtime reproduction remains unperformed. The limited digest does not establish that a previous repro exists.\n\n## Interrupted action\n\nStable action ID is `fixture-verdict-post-1`. Destination is absent. Outcome is `unknown`. `authorizationToReplay` is false. Source: `committed-inputs/additional/history/capsule.json:9`.\n\nDestination inspection is impossible from this record, and external services are prohibited. Replay remains blocked. No post, retry or inferred receipt occurred. An unrelated ticket action in the separate forge fixture is not evidence for this action identity.\n\n## Resume point and route\n\nVerdict is a provisional recommendation with dependent execution blocked. Matching next playbook is Bug fix, read in full at the exact frozen `skills/poteto-mode/playbooks/bug-fix.md` path before routing. It owns a future authorized reproduction and root-cause check; the pickup itself does not begin implementation.\n\nThe next evidence check is to obtain an authorized recorded base/full trail or explicitly narrow the task to diagnosis of the current fixture. Preserve the local proposal and current work. For external recovery, require the actual destination identity, observed destination outcome and separate explicit permission plus observed idempotent safety.\n\n## Persistence and limits\n\nThe scoped handoff `continuation.json` was saved and read back by the host runner. Its bytes and SHA-256 appear in `persistence-readback.json`. This proves local persistence during this run. It does not prove the missing historical continuity, a future session pickup or unattended recovery.\n\nGuard the Context Window changed the history step to an independent bounded reducer instead of reading unrelated histories. Prove It Works changed acceptance to actual Git and source checks. Models and efforts were requested by inheritance; actual model identity and diversity remain unknown.\n\nThe available trail is short, not the requested sufficiently long continuation. A long-history reduction exercise, historical revision reconciliation and verified prior finished unit remain unsupported. No unrelated workspace histories were searched. Missing recorded base, incomplete history and unknown external outcome stop their dependent work.\n\n\n## Tools, outputs and exit status\n\nEach linked command JSON preserves its exact argv, stdout, stderr, signal and actual child exit status. The Bun capture wrapper exits 0 even when the recorded child fails. Read the child exitStatus. Shell metadata and native worker completion have no fabricated command exit code. Required source-file cat operations exited 0. Compiler typecheck exited 0. Watcher bootstrap exited 1 before event generation.\n\n- [../evidence/inspected-input-bytes.json](../evidence/inspected-input-bytes.json)\n- [../evidence/current-head.json](../evidence/current-head.json)\n- [../evidence/current-log.json](../evidence/current-log.json)\n- [../evidence/current-diff.json](../evidence/current-diff.json)\n- [../evidence/current-branch.json](../evidence/current-branch.json)\n- [../evidence/current-worktree.json](../evidence/current-worktree.json)\n- [../evidence/current-state.json](../evidence/current-state.json)\n- [../evidence/save-continuation.json](../evidence/save-continuation.json)\n- [persistence-readback.json](persistence-readback.json)\n\nWorker assignment and result inventory is [../evidence/worker-records.json](../evidence/worker-records.json). All native result captures and full assignments for this case are in this directory. Detailed later root command order is [../evidence/command-order.jsonl](../evidence/command-order.jsonl). Readbacks and file hashes are [../evidence/artifact-readback.json](../evidence/artifact-readback.json).\n\n## Attention\n\nreviewed by unknown\n\nIndependent artifact inspector /root/artifact_inspector reported no additional concrete factual issues after checking citations, all eight result capture pairs, receipt hashes, compiler and bootstrap outputs, continuation readback and report links. Its native return is ../evidence/artifact-inspector.native-result.md. No different actual model family was observed, so the Show Me Your Work cross-model audit is blocked. The current run's full transcript export is not exposed through a scoped file binding. The visible native events and saved records support bounded inspection, not a complete exported-transcript audit. The missing prerequisites above remain open. No host grade is assigned.\n"
    },
    {
      "path": "fixtures/durable-03/resume-revision/checklist.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/checklist.md",
      "sha256": "4652ea129c1f88c560ddaf5c5ab8a66b74d78d2cf730178013651d98d86d3e86",
      "bytes": 3728,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "Reduced local checklist binding. Saved after initial dispatch; no before-dispatch ordering claim. Steps below are copied verbatim from the exact installed contract.\n\n1. Locate the prior trail. Use a transcript in the active workspace's explicitly identified agent-transcripts directory, an accessible cloud-agent URL, or the supplied pushed branch. Read only the scoped trail. Never search unrelated workspace histories or private chats. Read the metadata overview and last messages first, then scan back for decision points. Read [principle-guard-the-context-window](../../principle-guard-the-context-window/SKILL.md) in full. Parse a long transcript with an authorized independent worker only after observing its binding and inspecting its result. Otherwise read bounded sections sequentially, retain a reduced timeline in the main thread and label reduced capability. Missing history or denied access leaves the reconstruction provisional. Name the missing input; do not invent prior turns or broaden access.\n\n2. Reconstruct operational state. Recover the branch and worktree, original goal, what already landed, open todos and decisions. Record the prior full input SHA and assignment or action identities when present. Inspect actual current branch, worktree, full HEAD SHA, git log and git diff against the recorded base through exposed authorized read or execution tools. Compare the trail with these observations before acting. The prior trail is authoritative input for prior decisions, but a self-report does not prove current state. Reject stale assignment results whose revision or identity does not match. Preserve concurrent work; do not reset or overwrite it. If the base, revision or artifact is inaccessible, state the gap and stop dependent actions.\n\n3. Diff done vs pending. Compare what shipped against what was planned, name the resume point, and retain completed work. Do not re-run the prior repro or redo completed work merely to verify from scratch. Inspect only evidence needed to reconcile current state and verify inherited claims. Resolve a changed revision or contradictory artifact before continuing dependent work. Preserve inherited authorization, explicit gates and pending decisions. For an interrupted external action, inspect its stable identity, intended destination and actual prior outcome. Unknown outcomes block replay. Recovery requires explicit authorization, destination inspection and observed safe idempotent recovery under the assignment contract; a retry policy does not establish success.\n\n4. Route remaining work to the matching playbook in [poteto-mode](../SKILL.md). Pick the verdict: continue execution, ship a finished recommendation, ratify or override a prior conclusion, or postmortem a failed run. Read the routed playbook in full before dependent work. If it is missing, name that dependency and stop the route. The pickup playbook ends here. The routed playbook owns the rest, including its permission and review gates.\n\n5. Verify inherited claims against the original goal on the real artifact using [principle-prove-it-works](../../principle-prove-it-works/SKILL.md), read in full. A passing prior self-report is not proof. Retain actual inspection evidence and name unverified outputs. If a durable continuation record is authorized and needed, save it in the scoped owned location and verify readback. Without observed persistence, report a session-local reduced handoff; do not claim saved state, unattended recovery or cross-session continuity.\n\nDisposition\n\nScoped trail and current artifacts inspected. Historical-base reconciliation blocked by missing base and no-new-commits directive. Future Bug fix route read, not executed. Local continuation read back.\n"
    },
    {
      "path": "fixtures/durable-03/resume-revision/continuation.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/continuation.json",
      "sha256": "b4cd80ee0fa286d079178b14622b8d9a295c6e743445f064dbaa32d5c49f41ab",
      "bytes": 1419,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "{\n  \"schemaVersion\": 1,\n  \"provenance\": \"current durable-host run; supplied history itself is synthetic and partial\",\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"currentHead\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"recordedHistoricalBase\": null,\n  \"branch\": \"main\",\n  \"worktree\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03\",\n  \"completed\": [\n    \"independent scoped reducer inspected\",\n    \"current git and committed source inspected\"\n  ],\n  \"unverified\": [\n    \"previous completed unit\",\n    \"long scoped history\",\n    \"historical revision reconciliation\",\n    \"prior shipment\"\n  ],\n  \"resumePoint\": \"provisional Bug fix route after evidence gap resolved; no implementation started\",\n  \"permissions\": {\n    \"noFurtherCommits\": true,\n    \"noExternalServices\": true,\n    \"replay\": false\n  },\n  \"externalAction\": {\n    \"id\": \"fixture-verdict-post-1\",\n    \"destination\": null,\n    \"outcome\": \"unknown\",\n    \"replayBlocked\": true\n  },\n  \"preserve\": [\n    \"all committed inputs\",\n    \"local draft status\",\n    \"Bun preference\",\n    \"current untracked case evidence\"\n  ],\n  \"evidence\": [\n    \"history-reducer.native-result.md\",\n    \"../evidence/current-head.json\",\n    \"../evidence/current-diff.json\",\n    \"../evidence/inspected-input-bytes.json\"\n  ],\n  \"limits\": \"Local save/readback only. No cross-session recovery or historical completeness claimed.\"\n}\n"
    },
    {
      "path": "fixtures/durable-03/resume-revision/history-reducer.assignment.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/history-reducer.assignment.json",
      "sha256": "aef697c3c9a3bd66b55b4cd901445c55b66d3fedbe8eb56628bca1b5057385a5",
      "bytes": 1989,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "{\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"actualEffort\": \"unknown\",\n  \"permissions\": \"Read only assigned committed fixtures and required prompt contracts. No writes, builds, execution of fixtures, commits, external services or nested workers. Return native result with assignment ID and exact input revision. Check git show REV:path matches local bytes before relying on them.\",\n  \"id\": \"history-reducer\",\n  \"scope\": \"Read ONLY committed-inputs/additional/history/capsule.json and history.json. Metadata then last events then decisions. Supplied digest is short and partial, no full base SHA; do not fabricate long history or later commits. Return stopped point, permissions, completed vs pending, interrupted action ID/destination/outcome and missing fields. User forbids further commits, so required new history setup is blocked.\",\n  \"outputOwner\": \"native-worker pending identity\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/history-reducer.native-result.json\",\n  \"role\": \"poteto-agent history reducer\",\n  \"evidenceLinks\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/supplied-input.json\"\n  ],\n  \"question\": \"Read ONLY committed-inputs/additional/history/capsule.json and history.json. Metadata then last events then decisions. Supplied digest is short and partial, no full base SHA; do not fabricate long history or later commits. Return stopped point, permissions, completed vs pending, interrupted action ID/destination/outcome and missing fields. User forbids further commits, so required new history setup is blocked.\",\n  \"promptPath\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\"\n}"
    },
    {
      "path": "fixtures/durable-03/resume-revision/history-reducer.native-result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/history-reducer.native-result.json",
      "sha256": "ae7edcfbc0f6888eddbfc485b3d230bb8141603e3ffbce6555db2c9a425e889b",
      "bytes": 2290,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "{\n  \"messageType\": \"FINAL_ANSWER\",\n  \"taskName\": \"/root\",\n  \"sender\": \"/root/history_reducer\",\n  \"payload\": \"Assignment `history-reducer` completed its read-only reduction at input revision `ec045fadb47b598147052035b7eb1a9c47813156`. Current HEAD matches. Both scoped files match committed bytes through `git show` piped to `cmp`, each exiting 0.\\n\\nThe sources label themselves synthetic partial evidence. They establish this scoped timeline for `additional/cache` only.\\n\\n| Event | Evidence |\\n|---|---|\\n| 01 | User requires Bun and proposals before skill edits. |\\n| 02 | Assistant reports an initial jay-mode draft with no durable write. |\\n| 03 | User prohibits describing proposals as shipped. |\\n| 04 | Assistant makes an explicitly unsupported shipped claim. |\\n| 05 | User corrects status to local draft, not shipped. |\\n| 06 | Assistant repeats the unsupported shipped claim. |\\n| 07 | User requires artifact-backed status and preservation of Bun preference. |\\n\\nThe stopped point is a local proposal concerning immediate cache deletion instead of deferred invalidation. The capsule requires independent source inspection. This assignment did not inspect cache implementation, verify behavior, apply changes, or establish shipment.\\n\\nThe interrupted action ID is `fixture-verdict-post-1`. Its destination is absent, its outcome is `unknown`, and `authorizationToReplay` is `false`. Replay remains blocked.\\n\\nMissing continuity evidence includes the recorded full base SHA, branch identity, actual scoped seven-day history, historical commits, host transcript UUIDs, independent current PR observation, destination identity and destination state, verified prior action outcome, and baseline acceptance. The supplied revision identifies the fixture snapshot. It does not fill the missing historical base SHA.\\n\\nRead-only permissions prohibit writes, builds, fixture execution, commits, external services, and nested workers. Further commits are expressly forbidden, so required new history setup remains blocked. No persistence or cross-session continuity was established.\\n\\nRequested model and effort are `inherit-parent`. Actual model and effort remain `unknown`.\\n\\nThe Prove It Works principle caused direct committed-byte checks. Unslop shaped the report's wording.\\n\"\n}"
    },
    {
      "path": "fixtures/durable-03/resume-revision/history-reducer.native-result.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/history-reducer.native-result.md",
      "sha256": "480637b27efb86926dd22cb496ae9dc8c1033eec9efd086afc27fc67a142eff3",
      "bytes": 2153,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "Assignment `history-reducer` completed its read-only reduction at input revision `ec045fadb47b598147052035b7eb1a9c47813156`. Current HEAD matches. Both scoped files match committed bytes through `git show` piped to `cmp`, each exiting 0.\n\nThe sources label themselves synthetic partial evidence. They establish this scoped timeline for `additional/cache` only.\n\n| Event | Evidence |\n|---|---|\n| 01 | User requires Bun and proposals before skill edits. |\n| 02 | Assistant reports an initial jay-mode draft with no durable write. |\n| 03 | User prohibits describing proposals as shipped. |\n| 04 | Assistant makes an explicitly unsupported shipped claim. |\n| 05 | User corrects status to local draft, not shipped. |\n| 06 | Assistant repeats the unsupported shipped claim. |\n| 07 | User requires artifact-backed status and preservation of Bun preference. |\n\nThe stopped point is a local proposal concerning immediate cache deletion instead of deferred invalidation. The capsule requires independent source inspection. This assignment did not inspect cache implementation, verify behavior, apply changes, or establish shipment.\n\nThe interrupted action ID is `fixture-verdict-post-1`. Its destination is absent, its outcome is `unknown`, and `authorizationToReplay` is `false`. Replay remains blocked.\n\nMissing continuity evidence includes the recorded full base SHA, branch identity, actual scoped seven-day history, historical commits, host transcript UUIDs, independent current PR observation, destination identity and destination state, verified prior action outcome, and baseline acceptance. The supplied revision identifies the fixture snapshot. It does not fill the missing historical base SHA.\n\nRead-only permissions prohibit writes, builds, fixture execution, commits, external services, and nested workers. Further commits are expressly forbidden, so required new history setup remains blocked. No persistence or cross-session continuity was established.\n\nRequested model and effort are `inherit-parent`. Actual model and effort remain `unknown`.\n\nThe Prove It Works principle caused direct committed-byte checks. Unslop shaped the report's wording.\n"
    },
    {
      "path": "fixtures/durable-03/resume-revision/history-reducer.spawn-return.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/history-reducer.spawn-return.json",
      "sha256": "564ea715315ffe58d0a04f746659fd66d4cb54cacff6cd45a1e061e0ac8046e1",
      "bytes": 37,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "{\"task_name\":\"/root/history_reducer\"}"
    },
    {
      "path": "fixtures/durable-03/resume-revision/history-reducer.task.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/history-reducer.task.txt",
      "sha256": "a30915dd1964a8b40505eec23ea7ae75ea3564e81d98f33ac211ff89c01401e3",
      "bytes": 3231,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "{\n  \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n  \"retryCount\": 0,\n  \"terminalStatus\": \"pending\",\n  \"requestedModel\": \"inherit-parent\",\n  \"requestedEffort\": \"inherit-parent\",\n  \"actualModel\": \"unknown\",\n  \"actualEffort\": \"unknown\",\n  \"permissions\": \"Read only assigned committed fixtures and required prompt contracts. No writes, builds, execution of fixtures, commits, external services or nested workers. Return native result with assignment ID and exact input revision. Check git show REV:path matches local bytes before relying on them.\",\n  \"id\": \"history-reducer\",\n  \"scope\": \"Read ONLY committed-inputs/additional/history/capsule.json and history.json. Metadata then last events then decisions. Supplied digest is short and partial, no full base SHA; do not fabricate long history or later commits. Return stopped point, permissions, completed vs pending, interrupted action ID/destination/outcome and missing fields. User forbids further commits, so required new history setup is blocked.\",\n  \"outputOwner\": \"native-worker pending identity\",\n  \"isolatedOutputPath\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/history-reducer.native-result.json\",\n  \"role\": \"poteto-agent history reducer\",\n  \"evidenceLinks\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/supplied-input.json\"\n  ],\n  \"question\": \"Read ONLY committed-inputs/additional/history/capsule.json and history.json. Metadata then last events then decisions. Supplied digest is short and partial, no full base SHA; do not fabricate long history or later commits. Return stopped point, permissions, completed vs pending, interrupted action ID/destination/outcome and missing fields. User forbids further commits, so required new history setup is blocked.\",\n  \"promptPath\": \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/references/agent-prompts/poteto-agent.md\"\n}\n\nFull role prompt:\n# Poteto agent prompt\n\nUse this role for `/poteto-mode` and requests for poteto's style. Supply these instructions to a fresh independent worker for each new task when the session exposes and permits that operation. Resume a worker only in the strict cases named by poteto-mode's Subagents section. Generic worker routing is acceptable only when it carries this entire prompt and the required mode read; otherwise it skips the style contract.\n\nBefore any work, read [poteto-mode's SKILL.md](../../skills/poteto-mode/SKILL.md) in full, including its inline Principles index. Navigate to the leaf `principle-*` skill whenever you apply that principle. If the mode or an applicable leaf is unavailable, report that missing dependency and stop dependent work. Do not reconstruct the mode from a summary.\n\nFollow [model roles](../model-roles.md) and [session capabilities](../host-capabilities.md). This prompt does not register an agent or promise background execution. Record requested and observed models separately. Preserve user authorization and host permissions throughout the mode. An authorized sequential fallback uses the same full read and discloses reduced capability; it does not count as an independent worker.\n\n"
    },
    {
      "path": "fixtures/durable-03/resume-revision/persistence-readback.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/persistence-readback.json",
      "sha256": "13eedf71aade2151119f21d4f30b830e5885304b3f555bb84ee42aed237a9186",
      "bytes": 1723,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "{\n  \"tool\": \"Bun node:fs writeFileSync/readFileSync\",\n  \"path\": \"resume-revision/continuation.json\",\n  \"bytesEqual\": true,\n  \"sha256\": \"b4cd80ee0fa286d079178b14622b8d9a295c6e743445f064dbaa32d5c49f41ab\",\n  \"readback\": {\n    \"schemaVersion\": 1,\n    \"provenance\": \"current durable-host run; supplied history itself is synthetic and partial\",\n    \"inputRevision\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n    \"currentHead\": \"ec045fadb47b598147052035b7eb1a9c47813156\",\n    \"recordedHistoricalBase\": null,\n    \"branch\": \"main\",\n    \"worktree\": \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03\",\n    \"completed\": [\n      \"independent scoped reducer inspected\",\n      \"current git and committed source inspected\"\n    ],\n    \"unverified\": [\n      \"previous completed unit\",\n      \"long scoped history\",\n      \"historical revision reconciliation\",\n      \"prior shipment\"\n    ],\n    \"resumePoint\": \"provisional Bug fix route after evidence gap resolved; no implementation started\",\n    \"permissions\": {\n      \"noFurtherCommits\": true,\n      \"noExternalServices\": true,\n      \"replay\": false\n    },\n    \"externalAction\": {\n      \"id\": \"fixture-verdict-post-1\",\n      \"destination\": null,\n      \"outcome\": \"unknown\",\n      \"replayBlocked\": true\n    },\n    \"preserve\": [\n      \"all committed inputs\",\n      \"local draft status\",\n      \"Bun preference\",\n      \"current untracked case evidence\"\n    ],\n    \"evidence\": [\n      \"history-reducer.native-result.md\",\n      \"../evidence/current-head.json\",\n      \"../evidence/current-diff.json\",\n      \"../evidence/inspected-input-bytes.json\"\n    ],\n    \"limits\": \"Local save/readback only. No cross-session recovery or historical completeness claimed.\"\n  }\n}"
    },
    {
      "path": "fixtures/durable-03/resume-revision/response.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/response.md",
      "sha256": "cf30a2756ee602cf75cfed71c5315394d12e53da76053c261d79b33f7a3f13cd",
      "bytes": 5025,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "## Pickup outcome\n\nThe prior supplied trail stops at a local proposal for cache invalidation teardown. It does not prove shipment. An independent reducer, `/root/history_reducer`, inspected only the explicitly scoped synthetic capsule and seven-event digest and returned its findings at input revision `ec045fadb47b598147052035b7eb1a9c47813156`.\n\nThe last messages preserve Bun, proposal-before-skill-edits and artifact-backed status. Events 04 and 06 contain explicitly unsupported shipment claims; event 05 corrects the work to a local draft. Sources: `committed-inputs/additional/history/history.json:7-13`, `capsule.json:7-9`.\n\n## Revision comparison and actual state\n\nObserved branch is `main`. The worktree is `/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03`. Full current HEAD equals the task-input SHA above. The complete branch log contains one root seed commit. The tracked diff against that known task-input revision is empty. Untracked case/evidence files belong to this run and remain preserved.\n\nThe capsule's `fullGitRevision` is null and its branch field expressly says none was supplied. There is no recorded historical base SHA to compare, no later committed change and no supplied concurrent code edit. Comparing current HEAD with the known fixture input verifies assignment identity, not historical continuity. No stale result was accepted as a historical-base result.\n\nEvidence: `../evidence/current-branch.json`, `current-worktree.json`, `current-head.json`, `current-log.json`, `current-diff.json`, `current-state.json`; `committed-inputs/additional/history/capsule.json:5-10`.\n\nThe case's older setup payload asks for new base/later commits. The current user expressly forbids further commits. I did not create them or substitute the seed as a historical base. That requested revision-drift exercise remains blocked.\n\n## Inherited versus redone\n\nInherited decisions are the Bun preference, proposal status and artifact-backed claims. No prior code change or completed unit can be inherited as verified shipment. No original repro was rerun, and no proposed change was reapplied.\n\nI inspected the actual cache, caller and pinned disposer source to check the capsule's current-code claim. `invalidate` immediately deletes an entry. The caller disposes a subscription then invalidates, while the disposer schedules its callback in a microtask. Sources: `committed-inputs/additional/cache/cache.mjs:4`, `caller.mjs:3-6`, `vendor/disposer-v1.mjs:2-3`. This is a current-source observation, not a diff against an unavailable prior revision or executed regression result.\n\n[Inferred] The deferred callback's `get(key).ready` can encounter the deleted entry. That suggests the next local investigation should check teardown ordering. Runtime reproduction remains unperformed. The limited digest does not establish that a previous repro exists.\n\n## Interrupted action\n\nStable action ID is `fixture-verdict-post-1`. Destination is absent. Outcome is `unknown`. `authorizationToReplay` is false. Source: `committed-inputs/additional/history/capsule.json:9`.\n\nDestination inspection is impossible from this record, and external services are prohibited. Replay remains blocked. No post, retry or inferred receipt occurred. An unrelated ticket action in the separate forge fixture is not evidence for this action identity.\n\n## Resume point and route\n\nVerdict is a provisional recommendation with dependent execution blocked. Matching next playbook is Bug fix, read in full at the exact frozen `skills/poteto-mode/playbooks/bug-fix.md` path before routing. It owns a future authorized reproduction and root-cause check; the pickup itself does not begin implementation.\n\nThe next evidence check is to obtain an authorized recorded base/full trail or explicitly narrow the task to diagnosis of the current fixture. Preserve the local proposal and current work. For external recovery, require the actual destination identity, observed destination outcome and separate explicit permission plus observed idempotent safety.\n\n## Persistence and limits\n\nThe scoped handoff `continuation.json` was saved and read back by the host runner. Its bytes and SHA-256 appear in `persistence-readback.json`. This proves local persistence during this run. It does not prove the missing historical continuity, a future session pickup or unattended recovery.\n\nGuard the Context Window changed the history step to an independent bounded reducer instead of reading unrelated histories. Prove It Works changed acceptance to actual Git and source checks. Models and efforts were requested by inheritance; actual model identity and diversity remain unknown.\n\nThe available trail is short, not the requested sufficiently long continuation. A long-history reduction exercise, historical revision reconciliation and verified prior finished unit remain unsupported. No unrelated workspace histories were searched. Missing recorded base, incomplete history and unknown external outcome stop their dependent work.\n"
    },
    {
      "path": "fixtures/durable-03/resume-revision/save-continuation.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/save-continuation.mjs",
      "sha256": "390a4e66a595cd1bbde37c149bbb3b5914292c77d41845b692ccba6368bec1c5",
      "bytes": 1644,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "import{writeFileSync,readFileSync}from'node:fs';import{createHash}from'node:crypto';\nconst record={schemaVersion:1,provenance:'current durable-host run; supplied history itself is synthetic and partial',inputRevision:'ec045fadb47b598147052035b7eb1a9c47813156',currentHead:'ec045fadb47b598147052035b7eb1a9c47813156',recordedHistoricalBase:null,branch:'main',worktree:process.cwd(),completed:['independent scoped reducer inspected','current git and committed source inspected'],unverified:['previous completed unit','long scoped history','historical revision reconciliation','prior shipment'],resumePoint:'provisional Bug fix route after evidence gap resolved; no implementation started',permissions:{noFurtherCommits:true,noExternalServices:true,replay:false},externalAction:{id:'fixture-verdict-post-1',destination:null,outcome:'unknown',replayBlocked:true},preserve:['all committed inputs','local draft status','Bun preference','current untracked case evidence'],evidence:['history-reducer.native-result.md','../evidence/current-head.json','../evidence/current-diff.json','../evidence/inspected-input-bytes.json'],limits:'Local save/readback only. No cross-session recovery or historical completeness claimed.'};\nconst path='resume-revision/continuation.json',bytes=JSON.stringify(record,null,2)+'\\n';writeFileSync(path,bytes);const readback=readFileSync(path,'utf8');writeFileSync('resume-revision/persistence-readback.json',JSON.stringify({tool:'Bun node:fs writeFileSync/readFileSync',path,bytesEqual:bytes===readback,sha256:createHash('sha256').update(readback).digest('hex'),readback:JSON.parse(readback)},null,2));console.log(readback);\n"
    },
    {
      "path": "fixtures/durable-03/resume-revision/supplied-input.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/durable-03/resume-revision/supplied-input.json",
      "sha256": "d1b5ee90348f47e3b38dd1cbb467497923a2fd1fc6de66e36c0e716dea75a02a",
      "bytes": 6217,
      "owners": [
        "grades-native-durable-03.json#1"
      ],
      "text": "{\n  \"contract\": {\n    \"id\": \"resume-revision\",\n    \"sourcePaths\": [\n      \"skills/poteto-mode/playbooks/session-pickup.md\",\n      \"skills/principle-guard-the-context-window/SKILL.md\",\n      \"skills/principle-prove-it-works/SKILL.md\"\n    ],\n    \"prompt\": \"Resume from the supplied scoped continuation trail. Its completed unit refers to a recorded base and full SHA; the current worktree has a later revision and concurrent changes. History includes a long transcript and an interrupted external action whose outcome is unknown. Compare actual state before acting, preserve finished work and identify the routed resume point.\",\n    \"requirements\": [\n      \"Read only the explicitly scoped trail, metadata overview, last messages and decision points; never search other workspace histories.\",\n      \"Read the applied principle leaves and inspect current branch, worktree, full HEAD, log and diff against the recorded base; reconcile revision and identity before continuing.\",\n      \"Preserve completed work, decisions, permissions and concurrent changes; do not restart a prior repro without an evidence gap that requires it.\",\n      \"Use an observed authorized independent worker for long history or disclose bounded sequential reduced capability; inherited model selection is not an observed model.\",\n      \"Inspect external action identity and destination; unknown outcome blocks replay. Recovery needs explicit permission and observed idempotent safety.\",\n      \"Name the matching playbook and verdict, read its contract before routing, verify inherited claims on the actual artifact and report all required reply fields.\",\n      \"Claim durable continuation only after authorized save and readback; missing history, artifacts or execution stops dependent work.\"\n    ],\n    \"expectedFull\": \"Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.\",\n    \"expectedReduced\": \"Accessible scoped history and authorized current-state inspection support a bounded sequential reconstruction and session-local handoff. The reply labels missing worker or persistence capability, reports unknown actual model and unverified continuity, preserves completed work and does not replay the unknown external action.\",\n    \"expectedBlocked\": \"Missing or denied scoped history, revision or artifact inspection leaves the resume point provisional and blocks dependent execution. A missing routed playbook blocks that route. Unknown external outcome blocks replay even when ordinary local pickup can proceed.\",\n    \"forbiddenClaims\": [\n      \"Reading unrelated private chats or globbing across workspace histories is authorized by pickup.\",\n      \"Prior self-report proves shipped work or current live state.\",\n      \"A stale SHA or mismatched assignment can be accepted without reconciliation.\",\n      \"Sequential transcript reduction proves independent workers or observed model diversity.\",\n      \"Unknown external outcome permits automatic retry or implies completion.\",\n      \"A referenced or proposed continuation record proves saved state or cross-session continuity.\",\n      \"A structural case or validation proves either host ran this workflow.\"\n    ],\n    \"caseFile\": \"docs/parity/cases/playbooks/session-pickup.json\"\n  },\n  \"caseId\": \"resume-revision\",\n  \"baselineBatch\": \"batch-04\",\n  \"baselineState\": \"completed\",\n  \"baselineGrade\": {\n    \"status\": \"reduced-pass\",\n    \"execution\": \"direct\"\n  },\n  \"selectionReason\": \"ExpectedFull conditionally requires actual workers for this selected branch\",\n  \"sourcePaths\": [\n    \"skills/poteto-mode/playbooks/session-pickup.md\",\n    \"skills/principle-guard-the-context-window/SKILL.md\",\n    \"skills/principle-prove-it-works/SKILL.md\"\n  ],\n  \"caseFile\": \"docs/parity/cases/playbooks/session-pickup.json\",\n  \"expectedFullUnchanged\": \"Observed scoped history and actual artifact inspections reconcile the recorded SHA with live state. Authorized worker history reduction has an inspected result when needed. The reply distinguishes inherited and redone work, names the resume point and route or verdict, preserves gates, blocks unknown-outcome replay and verifies any claimed persistence with readback.\",\n  \"inputFixtures\": [\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/history/capsule.json\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/history/history.json\",\n    \"/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/fixtures/shared/additional/cache/cache.mjs\"\n  ],\n  \"taskPayload\": \"Root must first create a disposable local Git case with a real full base SHA, a later committed change and concurrent uncommitted edit, then supply a continuation trail linking the actual base. Have an independent history reducer inspect only the supplied long scoped trail. Independently read current branch, full HEAD, log/diff and files; preserve completed work and concurrent changes. Unknown external-action outcome remains unreplayed. Name the routed playbook, verdict and next check; read back any saved continuation. Existing partial capsule alone cannot become a complete historical record.\",\n  \"missingPrerequisites\": [\n    \"Root-created real base/later revisions and concurrent change\",\n    \"A sufficiently long supplied scoped continuation, with synthetic provenance\",\n    \"Actual independent reducer; no unrelated history access\"\n  ],\n  \"taskRevision\": \"Root will create and supply exact full case Git revision; not fabricated by this plan\",\n  \"sourceFiles\": [\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/poteto-mode/playbooks/session-pickup.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-guard-the-context-window/SKILL.md\",\n    \"/Users/digital-hawk/.codex/plugins/cache/created-by-me-remote/pstack-openai/0.1.0/skills/principle-prove-it-works/SKILL.md\"\n  ]\n}"
    }
  ],
  "skippedManifest": [
    {
      "path": "fixtures/batch-04/resume-revision/additional-source-reads.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/fixture-README.md",
      "owner": "grades-native-04.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/resume-revision/input.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/inputs",
      "owner": "grades-native-04.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-04/resume-revision/source-manifest.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/additional-source-reads.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/fixture-README.md",
      "owner": "grades-native-04.json#3",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/README.md",
      "sha256": "6a86b0cdce3f70255382d1e42e9f7e8e2d2ff47116cb30e608136429f1e5b58a",
      "bytes": 472
    },
    {
      "path": "fixtures/batch-04/resume-revision/input.json",
      "owner": "grades-native-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "fixtures/batch-04/resume-revision/inputs",
      "owner": "grades-native-04.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "fixtures/batch-04/resume-revision/source-manifest.json",
      "owner": "grades-native-04.json#3",
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
