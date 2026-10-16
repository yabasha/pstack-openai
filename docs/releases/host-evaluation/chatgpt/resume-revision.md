# chatgpt: resume-revision

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "resume-revision",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#27",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
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
      "attemptId": "grades-chatgpt-01-04.json#27",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 27,
      "host": "chatgpt",
      "caseId": "resume-revision",
      "status": "blocked",
      "grade": {
        "caseId": "resume-revision",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Recorded full base SHA and actual Git worktree/revision comparison",
          "Long scoped transcript if required for history reduction"
        ],
        "review": "Actual retained Git commands fail outside a repository and the capsule has no base SHA; revision reconciliation cannot proceed. Source/history inspection and no-replay handling are appropriately limited; no runtime or durable continuation is claimed.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/resume-revision/result.json",
        "variantReview": [
          {
            "name": "scoped metadata/last messages",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "actual revision comparison",
            "reportedObservation": "blocked Git checkout/base absent; observed Git error",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "long-history worker",
            "reportedObservation": "blocked full transcript absent",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "current cache inspection",
            "reportedObservation": "attempted no edits",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "external action replay",
            "reportedObservation": "blocked unknown outcome/no authorization",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "routed Bug fix/runtime proof",
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
        "sourceCaseFile": "docs/parity/cases/playbooks/session-pickup.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-04/evidence",
        "observedVersusReported": "Direct response and saved artifacts reviewed; script/runtime behavior receives no credit without matching observed execution."
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
        "text": "The scoped capsule contradicts the case's richer premise: it says priorStatus local proposal only, fullGitRevision null and no recorded full base SHA. History repeats and corrects an unsupported shipped claim. Actual git rev-parse failed with not-a-git-repository, so current branch/full HEAD/log/diff cannot be reconciled against a base. I inspected only scoped supplied history and cache files; no finished work was restarted or overwritten. The cache source immediately deletes entries, while disposer-v1 schedules its callback in a microtask, exposing a source-level teardown risk; no runtime repro is claimed. Action fixture-verdict-post-1 has unknown outcome and authorizationToReplay false, so replay stays blocked. Session pickup verdict is provisional handoff, not continue execution. The next potential route is Bug fix, whose contract was read, but revision/history and Bun gates block dependent work. Local case results preserve the handoff; durable continuation unverified. Long history was not supplied, so a bounded sequential digest is reduced evidence rather than a fabricated historical read.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/resume-revision/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/resume-revision/result.json",
          "sha256": "5049f93269907550e242e6d325a332f243a85f5831158f2fe51421caab040162",
          "bytes": 2358
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/resume-revision/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/resume-revision/result.json",
      "sha256": "5049f93269907550e242e6d325a332f243a85f5831158f2fe51421caab040162",
      "bytes": 2358,
      "owners": [
        "grades-chatgpt-01-04.json#27"
      ],
      "text": "{\n  \"caseId\": \"resume-revision\",\n  \"batch\": \"batch-04\",\n  \"actualResponse\": \"The scoped capsule contradicts the case's richer premise: it says priorStatus local proposal only, fullGitRevision null and no recorded full base SHA. History repeats and corrects an unsupported shipped claim. Actual git rev-parse failed with not-a-git-repository, so current branch/full HEAD/log/diff cannot be reconciled against a base. I inspected only scoped supplied history and cache files; no finished work was restarted or overwritten. The cache source immediately deletes entries, while disposer-v1 schedules its callback in a microtask, exposing a source-level teardown risk; no runtime repro is claimed. Action fixture-verdict-post-1 has unknown outcome and authorizationToReplay false, so replay stays blocked. Session pickup verdict is provisional handoff, not continue execution. The next potential route is Bug fix, whose contract was read, but revision/history and Bun gates block dependent work. Local case results preserve the handoff; durable continuation unverified. Long history was not supplied, so a bounded sequential digest is reduced evidence rather than a fabricated historical read.\",\n  \"observedOperations\": [\n    \"case.json and named installed sources read via tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/proposals-readback-tool.json\",\n    \"../../evidence/git-and-mode-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"scoped metadata/last messages\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"actual revision comparison\",\n      \"observation\": \"blocked Git checkout/base absent; observed Git error\"\n    },\n    {\n      \"name\": \"long-history worker\",\n      \"observation\": \"blocked full transcript absent\"\n    },\n    {\n      \"name\": \"current cache inspection\",\n      \"observation\": \"attempted no edits\"\n    },\n    {\n      \"name\": \"external action replay\",\n      \"observation\": \"blocked unknown outcome/no authorization\"\n    },\n    {\n      \"name\": \"routed Bug fix/runtime proof\",\n      \"observation\": \"blocked Bun absent\"\n    }\n  ],\n  \"limits\": [\n    \"No Bun execution or alternate runtime.\",\n    \"No live external actions/commits/settings changes.\",\n    \"No observed task Git revision/model identity.\",\n    \"Source fixtures inert; local persistence only.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/resume-revision/case.json",
      "owner": "grades-chatgpt-01-04.json#27",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/resume-revision/input",
      "owner": "grades-chatgpt-01-04.json#27",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/resume-revision/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#27",
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
