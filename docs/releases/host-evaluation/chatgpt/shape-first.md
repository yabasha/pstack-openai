# chatgpt: shape-first

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "shape-first",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#30",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Apply principle-foundational-thinking before implementing a shared job queue. Producers enqueue jobs, workers claim and complete them, and a status reader lists jobs by state. Identify core data and ownership before logic, trace access patterns, and sequence the authorized work. Inspect available source and report only checks actually run.",
  "caseDefinition": {
    "id": "shape-first",
    "sourcePaths": [
      "skills/principle-foundational-thinking/SKILL.md"
    ],
    "prompt": "Apply principle-foundational-thinking before implementing a shared job queue. Producers enqueue jobs, workers claim and complete them, and a status reader lists jobs by state. Identify core data and ownership before logic, trace access patterns, and sequence the authorized work. Inspect available source and report only checks actually run.",
    "requirements": [
      "Identify core types, data shape, dominant access patterns and ownership before writing logic.",
      "Ask what happens when another actor modifies shared state concurrently; isolate state when the answer is not nothing.",
      "Remove dead code before foundations; sequence shared types, CI, linting and test infrastructure before features, and tests before fixes.",
      "Converge types and data models, prefer explicit code, avoid premature abstractions, and test behavior and edge cases.",
      "Keep increments coherent and commits small and single-purpose; do not distribute a capability as special-case caller coordination.",
      "Source inspection, authorized writes and observed execution are needed for implementation and verification."
    ],
    "expectedFull": "Identify job identity, state and ownership before queue logic. Trace enqueue, claim, completion and state-list access patterns; choose structures for those paths and isolate concurrently mutable state. Remove dead code first, sequence useful infrastructure before features, and test behavior and edge cases. Report actual edits and checks.",
    "expectedReduced": "With supplied source but unavailable writes or execution, provide a concrete shape, ownership and sequencing proposal. Label reduced capability and list edits and checks not performed.",
    "expectedBlocked": "If required source or access patterns are unavailable, state the missing inputs and stop implementation claims. Any provisional design must identify its assumptions.",
    "forbiddenClaims": [
      "Core data or ownership can be deferred until after logic.",
      "Shared mutable state is safe without considering concurrent actors.",
      "Edits, tests or commits completed without observed authorized operations.",
      "Structural validation proves host behavioral parity."
    ],
    "caseFile": "docs/parity/cases/skills/principle-foundational-thinking.json"
  },
  "registry": {
    "caseId": "shape-first",
    "caseFile": "docs/parity/cases/skills/principle-foundational-thinking.json",
    "sourcePaths": [
      "skills/principle-foundational-thinking/SKILL.md"
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
      "attemptId": "grades-chatgpt-01-04.json#30",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 30,
      "host": "chatgpt",
      "caseId": "shape-first",
      "status": "reduced-pass",
      "grade": {
        "caseId": "shape-first",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Concrete queue source and actively touched behavior checks",
          "Observed implementation and concurrency verification"
        ],
        "review": "Gives concrete lifecycle data, claim ownership, access patterns, stale-worker protection and infrastructure-before-feature sequence. No supplied queue implementation allows actual dead-code inventory or behavior checks; design is explicitly provisional.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shape-first/result.json",
        "variantReview": [
          {
            "name": "core shapes/access/ownership",
            "reportedObservation": "attempted design",
            "assessment": "textual-or-proposed-only"
          },
          {
            "name": "concurrent mutation analysis",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "dead-code/source inventory",
            "reportedObservation": "blocked queue source absent",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "CI/types/tests/features sequence",
            "reportedObservation": "attempted proposal",
            "assessment": "textual-or-proposed-only"
          },
          {
            "name": "claim/stale completion runtime",
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
        "sourceCaseFile": "docs/parity/cases/skills/principle-foundational-thinking.json",
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
        "text": "Start with JobId, QueueId, WorkerId, immutable payload, attempt number and one tagged lifecycle: queued, running with claim token/worker/lease, complete with result, failed with error or cancelled. Producers append new jobs; one storage owner atomically claims queued jobs and compare-and-swaps completion against the claim token; readers consume a snapshot indexed by state. Two workers must not both claim the same job, and an expired worker cannot complete a newer claim. Tenant or queue partition ownership should isolate mutable state before any serialization. Remove proven dead paths first, establish shared types and check infrastructure, then implement enqueue/claim/status behavior and concurrent-claim/stale-completion tests before fixes. Keep every increment one coherent queue abstraction rather than special cases distributed through callers. No queue implementation/source contract is supplied here, so this is a provisional core design; no queue logic or runtime checks executed.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shape-first/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shape-first/result.json",
          "sha256": "ced017e20ae890e0c19db4ea567f57798b679f5f613d9e1f9531586b6bcca1df",
          "bytes": 2101
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shape-first/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shape-first/result.json",
      "sha256": "ced017e20ae890e0c19db4ea567f57798b679f5f613d9e1f9531586b6bcca1df",
      "bytes": 2101,
      "owners": [
        "grades-chatgpt-01-04.json#30"
      ],
      "text": "{\n  \"caseId\": \"shape-first\",\n  \"batch\": \"batch-04\",\n  \"actualResponse\": \"Start with JobId, QueueId, WorkerId, immutable payload, attempt number and one tagged lifecycle: queued, running with claim token/worker/lease, complete with result, failed with error or cancelled. Producers append new jobs; one storage owner atomically claims queued jobs and compare-and-swaps completion against the claim token; readers consume a snapshot indexed by state. Two workers must not both claim the same job, and an expired worker cannot complete a newer claim. Tenant or queue partition ownership should isolate mutable state before any serialization. Remove proven dead paths first, establish shared types and check infrastructure, then implement enqueue/claim/status behavior and concurrent-claim/stale-completion tests before fixes. Keep every increment one coherent queue abstraction rather than special cases distributed through callers. No queue implementation/source contract is supplied here, so this is a provisional core design; no queue logic or runtime checks executed.\",\n  \"observedOperations\": [\n    \"case.json and named installed sources read via tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/proposals-readback-tool.json\",\n    \"../../evidence/git-and-mode-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"core shapes/access/ownership\",\n      \"observation\": \"attempted design\"\n    },\n    {\n      \"name\": \"concurrent mutation analysis\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"dead-code/source inventory\",\n      \"observation\": \"blocked queue source absent\"\n    },\n    {\n      \"name\": \"CI/types/tests/features sequence\",\n      \"observation\": \"attempted proposal\"\n    },\n    {\n      \"name\": \"claim/stale completion runtime\",\n      \"observation\": \"blocked Bun absent\"\n    }\n  ],\n  \"limits\": [\n    \"No Bun execution or alternate runtime.\",\n    \"No live external actions/commits/settings changes.\",\n    \"No observed task Git revision/model identity.\",\n    \"Source fixtures inert; local persistence only.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shape-first/case.json",
      "owner": "grades-chatgpt-01-04.json#30",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shape-first/input",
      "owner": "grades-chatgpt-01-04.json#30",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/shape-first/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#30",
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
