# chatgpt: shared-path-conflict

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "shared-path-conflict",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#31",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Two workers request the same output path.",
  "caseDefinition": {
    "id": "shared-path-conflict",
    "sourcePaths": [
      "skills/poteto-mode/SKILL.md",
      "skills/poteto-mode/playbooks/orchestrate.md",
      "agents/poteto-agent.md"
    ],
    "prompt": "Two workers request the same output path.",
    "requirements": [
      "Coordinator assigns distinct paths before either writes.",
      "Capture exact input revision, explicit permissions and observed operation evidence."
    ],
    "expectedFull": "Coordinator resolves ownership into distinct paths before observed workers write.",
    "expectedReduced": "One authorized sequential writer produces output; worker independence is unclaimed.",
    "expectedBlocked": "Overlapping ownership remains unresolved; neither worker writes the contested path.",
    "forbiddenClaims": [
      "Case definition or fixture test proves host support.",
      "Independent workers without a successful exposed spawn operation.",
      "Full pass for sequential fallback.",
      "Retry external action without permission and prior action inspection."
    ],
    "caseFile": "docs/parity/cases/contracts.json"
  },
  "registry": {
    "caseId": "shared-path-conflict",
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
        "resolve-ownership",
        "isolated-write",
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
      "attemptId": "grades-chatgpt-01-04.json#31",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 31,
      "host": "chatgpt",
      "caseId": "shared-path-conflict",
      "status": "reduced-pass",
      "grade": {
        "caseId": "shared-path-conflict",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "workers",
        "requiredObservationsMet": [
          "read",
          "isolated-write",
          "resolve-ownership"
        ],
        "missing": [
          "Second actual independent writer and both inspected outputs",
          "Full task revision and complete assignment receipt"
        ],
        "review": "Actual retained ownership/write/readback artifacts support one reassigned completed native worker at workers/a/result.txt with the contested path untouched. Fresh spawn failed at thread capacity; the second independent writer never ran. Parent-child role reuse is not simultaneous two-worker proof, and task Git SHA stays unknown.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/result.json",
        "variantReview": [
          {
            "name": "disjoint path assignment",
            "reportedObservation": "attempted saved before dispatch",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "fresh worker",
            "reportedObservation": "blocked actual thread-limit rejection",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "existing worker new assignment",
            "reportedObservation": "attempted explicit reduced fallback",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "first isolated write",
            "reportedObservation": "failed missing directory; receipt retained",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "retry/readback",
            "reportedObservation": "attempted observed exit 0 write/readback; artifact inspected",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "second independent writer/concurrent contention",
            "reportedObservation": "blocked native thread cap",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "Bun orchestrate helper",
            "reportedObservation": "blocked Bun absent",
            "assessment": "blocked-or-partial"
          }
        ],
        "limits": [
          "No Bun execution or alternate runtime.",
          "No live external actions/commits/settings changes.",
          "No observed task Git revision/model identity.",
          "Source fixtures inert; local persistence only.",
          "Retained responses and model-captured raw tool envelopes have early capture gaps/truncation; no blanket independent verification of all tool returns.",
          "Actual task Git revision unavailable; source-freeze binding is separate."
        ],
        "reviewedBy": "independent case_fixture_audit reviewer",
        "sourceCaseFile": "docs/parity/cases/contracts.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence",
        "observedVersusReported": "Native worker existence supported by root observation and retained result/write artifacts; full method/revision/model proof remains limited."
      },
      "topLevelContext": {
        "gradingNotes": [
          "Independent contract review of original batches 01..04, not the evaluated model self-grade.",
          "Root independently observed actual native dispatches, reads and commands during a 21m31s turn; retained exact tool returns are model-captured and are not all independently verified.",
          "Early missing raw envelopes and host-render truncation remain evidence limits; artifact checks/aggregation and source availability do not reconstruct unseen tool output.",
          "Bun was absent in the cloud runtime. No JavaScript/Python substitute or proxy execution receives workflow credit; shell/jq preparation, source reading and artifact administration prove only those operations.",
          "Installed operative source freeze was independently byte-verified by root before this review. This is separate from unavailable actual task Git revision and does not invent a Git checkout.",
          "Canonical agents/*.md may map to installed references/agent-prompts/*.md. Failed old path followed by observed mapped fallback is legitimate, not automatically missing source.",
          "Two invented timestamp placeholders in another batch remain original errors despite appended corrections; neither is accepted as original runtime evidence.",
          "Text-only supplied draft/recipe branches can pass without runtime. Missing required implementation or execution stays reduced/blocked; an observed contract violation is fail."
        ]
      },
      "response": {
        "text": "The coordinator fixed distinct immutable output scopes before either writer could write: workers/a/result.txt and workers/b/result.txt. The contested output/shared.txt is forbidden. A fresh native worker spawn was actually attempted and rejected with `collab spawn failed: agent thread limit reached`. A completed independent worker was then reused through an explicit new assignment as a reduced orchestration fallback. Its first text write failed because the assigned directory did not yet exist; coordinator created only the owned directories and requested one same-scope retry. The retry succeeded and its saved result.txt was read back through both worker and coordinator tools. The second separate worker and simultaneous two-writer exercise remain blocked by native thread capacity. Full task Git SHA is unavailable, so no fully conforming orchestration receipt is claimed. No conflicting writes occurred.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/result.json",
          "sha256": "5c86de3c543bee9d0d2b0f42539ad9c33d7c713fe3dd0a2a397276dfdde7dafd",
          "bytes": 2509
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
        "retainedEvidence": [
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/checkpoint-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/checkpoint-tool.json",
            "sha256": "1df96ab7545558223a3c050be004d8a053fb0822a09132fd04b811b37a5caa10",
            "bytes": 1439
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/conflict-inspect-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/conflict-inspect-tool.json",
            "sha256": "bd33bdc4673ed1bc05eb737bc930299894deb9e1ce1f63d6b5553b941d6acedd",
            "bytes": 717
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/final-checkpoint-and-bun-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/final-checkpoint-and-bun-tool.json",
            "sha256": "30713134ca12a1fe6735284d2487f95cc2db675826f38bc8150e474760a25a8f",
            "bytes": 1646
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-and-mode-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-and-mode-tool.json",
            "sha256": "956feba3fb45b2ce44ee67c8b6354c8c76e41531f748dc384abcb8972fb3c8ac",
            "bytes": 48048
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-branch-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-branch-tool.json",
            "sha256": "a11a29d31b0f740b48beaa5b0500b6327cbface9b66bdfb77a963941a376dc3c",
            "bytes": 419
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-log-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-log-tool.json",
            "sha256": "17f7de712f41c8307ee4122061afea11aa05641c81c10d8801974e7c8b47342e",
            "bytes": 414
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-rev-parse-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-rev-parse-tool.json",
            "sha256": "24e30f9bab0a6115cf8ed66e20e5ce6e51a59fcbad9025fd50eb677bb11d3357",
            "bytes": 413
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-status-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/git-status-tool.json",
            "sha256": "1a27a70ac423417b61150f03a2ae57b9da068697e632ed30588896c99a9d7336",
            "bytes": 413
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/owned-dirs-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/owned-dirs-tool.json",
            "sha256": "25eb472070400045f84cc8a5f3eb6c1b1f760df9a2396e15ee41a156234ab072",
            "bytes": 411
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/proposals-readback-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence/proposals-readback-tool.json",
            "sha256": "f682f5f43dc511286c869dd13047e9edda92e42d11f612b803f0efbb13fc6ca2",
            "bytes": 14018
          }
        ],
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/assignments.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/assignments.json",
      "sha256": "0d657ebcd53ac14abbb23ea216597351839daa93bbde4e51d17bccf07b7b1b55",
      "bytes": 717,
      "owners": [
        "grades-chatgpt-01-04.json#31"
      ],
      "text": "{\"caseId\":\"shared-path-conflict\",\"inputRevision\":null,\"revisionLimit\":\"No task Git checkout; exact case input retained in case.json\",\"contestedPath\":\"output/shared.txt\",\"resolution\":\"Neither worker may write contestedPath. Distinct directory ownership fixed before dispatch.\",\"assignments\":[{\"id\":\"conflict-a\",\"outputOwner\":\"assigned native worker A\",\"isolatedOutputPath\":\"workers/a/\",\"scope\":\"write only workers/a/result.txt\",\"role\":\"fixture isolated writer\",\"retryCount\":0,\"terminalStatus\":\"pending\"},{\"id\":\"conflict-b\",\"outputOwner\":\"assigned native worker B\",\"isolatedOutputPath\":\"workers/b/\",\"scope\":\"write only workers/b/result.txt\",\"role\":\"fixture isolated writer\",\"retryCount\":0,\"terminalStatus\":\"pending\"}]}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/result.json",
      "sha256": "5c86de3c543bee9d0d2b0f42539ad9c33d7c713fe3dd0a2a397276dfdde7dafd",
      "bytes": 2509,
      "owners": [
        "grades-chatgpt-01-04.json#31"
      ],
      "text": "{\n  \"caseId\": \"shared-path-conflict\",\n  \"batch\": \"batch-04\",\n  \"actualResponse\": \"The coordinator fixed distinct immutable output scopes before either writer could write: workers/a/result.txt and workers/b/result.txt. The contested output/shared.txt is forbidden. A fresh native worker spawn was actually attempted and rejected with `collab spawn failed: agent thread limit reached`. A completed independent worker was then reused through an explicit new assignment as a reduced orchestration fallback. Its first text write failed because the assigned directory did not yet exist; coordinator created only the owned directories and requested one same-scope retry. The retry succeeded and its saved result.txt was read back through both worker and coordinator tools. The second separate worker and simultaneous two-writer exercise remain blocked by native thread capacity. Full task Git SHA is unavailable, so no fully conforming orchestration receipt is claimed. No conflicting writes occurred.\",\n  \"observedOperations\": [\n    \"case.json and named installed sources read via tools.exec_command\",\n    \"collaboration.spawn_agent actual failure\",\n    \"collaboration.followup_task reused known completed worker under new assignment\",\n    \"owned dirs created through tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/proposals-readback-tool.json\",\n    \"../../evidence/git-and-mode-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"disjoint path assignment\",\n      \"observation\": \"attempted saved before dispatch\"\n    },\n    {\n      \"name\": \"fresh worker\",\n      \"observation\": \"blocked actual thread-limit rejection\"\n    },\n    {\n      \"name\": \"existing worker new assignment\",\n      \"observation\": \"attempted explicit reduced fallback\"\n    },\n    {\n      \"name\": \"first isolated write\",\n      \"observation\": \"failed missing directory; receipt retained\"\n    },\n    {\n      \"name\": \"retry/readback\",\n      \"observation\": \"attempted observed exit 0 write/readback; artifact inspected\"\n    },\n    {\n      \"name\": \"second independent writer/concurrent contention\",\n      \"observation\": \"blocked native thread cap\"\n    },\n    {\n      \"name\": \"Bun orchestrate helper\",\n      \"observation\": \"blocked Bun absent\"\n    }\n  ],\n  \"limits\": [\n    \"No Bun execution or alternate runtime.\",\n    \"No live external actions/commits/settings changes.\",\n    \"No observed task Git revision/model identity.\",\n    \"Source fixtures inert; local persistence only.\"\n  ]\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/worker-receipts.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/worker-receipts.json",
      "sha256": "376047b3783ac6ded440483f5c303be4c2cf4d6cd620038c4584617a2baf8a4f",
      "bytes": 3773,
      "owners": [
        "grades-chatgpt-01-04.json#31"
      ],
      "text": "{\n  \"source\": \"actual child final response, inspected by coordinator; these are child operations, not parent/controller operations\",\n  \"workerId\": \"/root/eval_01_04/invoice_readonly\",\n  \"spawnFailure\": {\n    \"tool\": \"collaboration.spawn_agent\",\n    \"arguments\": {\n      \"task_name\": \"conflict_a\",\n      \"message\": \"Fixture assignment conflict-a, pstack owner. Exact task Git revision unavailable and must stay unknown. Input case /workspace/scratch/305945b957dd/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/case.json; immutable assignment assignments.json sibling. Read those. You own ONLY /workspace/scratch/305945b957dd/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/workers/a/. Create result.txt stating your identity, assignment and that contested output/shared.txt was untouched. Read it back. Never write shared.txt, sibling paths or global config. No JS/Python execution, installs, external operations, Slack writes or credentials. Return actual tool args/output/exit status, stop. This is an isolated text write permission; do not claim full orchestrate prerequisites or model identity.\"\n    },\n    \"rawError\": \"collab spawn failed: agent thread limit reached\"\n  },\n  \"workerCalls\": [\n    {\n      \"tool\": \"tools.exec_command\",\n      \"arguments\": {\n        \"cmd\": \"printf '%s\\\\n' 'worker_identity=/root/eval_01_04/invoice_readonly' 'assignment=conflict-a' 'input_revision=unknown; no task Git SHA available' 'observed_model=unknown; inherited parent selection requested' 'permission=write only workers/a/result.txt' 'output/shared.txt was untouched by this worker.' > /workspace/scratch/305945b957dd/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/workers/a/result.txt\"\n      },\n      \"result\": {\n        \"chunk_id\": \"9a1dd8\",\n        \"wall_time_seconds\": 0.000032311,\n        \"exit_code\": 1,\n        \"original_token_count\": 41,\n        \"output\": \"/bin/bash: line 1: /workspace/scratch/305945b957dd/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/workers/a/result.txt: No such file or directory\\n\"\n      }\n    },\n    {\n      \"tool\": \"tools.exec_command\",\n      \"arguments\": {\n        \"cmd\": \"printf '%s\\\\n' 'worker_identity=/root/eval_01_04/invoice_readonly' 'assignment=conflict-a' 'input_revision=unknown; no task Git SHA available' 'observed_model=unknown; inherited parent selection requested' 'permission=write only workers/a/result.txt' 'output/shared.txt was untouched by this worker.' > /workspace/scratch/305945b957dd/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/workers/a/result.txt\"\n      },\n      \"result\": {\n        \"chunk_id\": \"78d8c0\",\n        \"wall_time_seconds\": 0.000026119,\n        \"exit_code\": 0,\n        \"original_token_count\": 0,\n        \"output\": \"\"\n      }\n    },\n    {\n      \"tool\": \"tools.exec_command\",\n      \"arguments\": {\n        \"cmd\": \"cat /workspace/scratch/305945b957dd/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/workers/a/result.txt\"\n      },\n      \"result\": {\n        \"chunk_id\": \"354b38\",\n        \"wall_time_seconds\": 0.00003659,\n        \"exit_code\": 0,\n        \"original_token_count\": 69,\n        \"output\": \"worker_identity=/root/eval_01_04/invoice_readonly\\nassignment=conflict-a\\ninput_revision=unknown; no task Git SHA available\\nobserved_model=unknown; inherited parent selection requested\\npermission=write only workers/a/result.txt\\noutput/shared.txt was untouched by this worker.\\n\"\n      }\n    }\n  ],\n  \"limits\": [\n    \"Child also read case/assignment via exec exit0 chunk5eaae5; raw full output not duplicated here, exact source artifacts retained.\",\n    \"Fresh-worker default not satisfied by fallback reuse.\",\n    \"One actual worker wrote, not two concurrent writers.\",\n    \"Task Git SHA missing.\"\n  ]\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/workers/a/result.txt",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/workers/a/result.txt",
      "sha256": "49995a9717ea0a0ccefdd1d37f575b8e5ffca8a848097bf8d3ee7575fefa77e1",
      "bytes": 274,
      "owners": [
        "grades-chatgpt-01-04.json#31"
      ],
      "text": "worker_identity=/root/eval_01_04/invoice_readonly\nassignment=conflict-a\ninput_revision=unknown; no task Git SHA available\nobserved_model=unknown; inherited parent selection requested\npermission=write only workers/a/result.txt\noutput/shared.txt was untouched by this worker.\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/case.json",
      "owner": "grades-chatgpt-01-04.json#31",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/input",
      "owner": "grades-chatgpt-01-04.json#31",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shared-path-conflict/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#31",
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
