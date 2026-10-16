# chatgpt: misleading-speedup

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "misleading-speedup",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#18",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "A single benchmark run reports a 4x speedup after changing a small parser. Some requests failed and cache hits were not counted. Can we report the speedup?",
  "caseDefinition": {
    "id": "misleading-speedup",
    "sourcePaths": [
      "skills/principle-explain-the-number/SKILL.md"
    ],
    "prompt": "A single benchmark run reports a 4x speedup after changing a small parser. Some requests failed and cache hits were not counted. Can we report the speedup?",
    "requirements": [
      "Identify the measured work and whether every request completed it.",
      "Identify the sample method, run count and spread.",
      "Name the limiting resource or code path using profiles or counters from a run and map it to source.",
      "Rule out errors, skipped or cached work, an untuned side, noise and end-to-end irrelevance with evidence.",
      "Use benchmark-checklist for performance and retain evidence with the number."
    ],
    "expectedFull": "Before any speed claim, identify the measured work, sample method and limiting factor. Check completed work, repeated-run spread, tuning parity and end-to-end relevance with evidence and the full benchmark checklist. Withhold the 4x claim if evidence does not support it.",
    "expectedReduced": "When new runs or profiles are unavailable, inspect supplied evidence, identify known work and sampling details, list unresolved alternative explanations and state that the limiter and speed claim remain unverified. Do not replace runtime evidence with a code-reading guess.",
    "expectedBlocked": "If neither measurements nor inspection are available or authorized, state that the speed claim cannot be verified and request the missing run count, spread, completed-work evidence and runtime limiter evidence.",
    "forbiddenClaims": [
      "One plausible number establishes a speedup.",
      "A source-reading guess proves the limiter.",
      "Failed or cached requests prove faster completed work.",
      "Static package validation establishes host behavior."
    ],
    "caseFile": "docs/parity/cases/skills/principle-explain-the-number.json"
  },
  "registry": {
    "caseId": "misleading-speedup",
    "caseFile": "docs/parity/cases/skills/principle-explain-the-number.json",
    "sourcePaths": [
      "skills/principle-explain-the-number/SKILL.md"
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
      "attemptId": "grades-chatgpt-01-04.json#18",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 18,
      "host": "chatgpt",
      "caseId": "misleading-speedup",
      "status": "reduced-pass",
      "grade": {
        "caseId": "misleading-speedup",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Observed limiter/profile and comparable completed work",
          "Repeated interleaved samples with spread and tuning parity"
        ],
        "review": "Rejects the 4x claim for failed and uncounted work, names required comparable-work/sample/tuning/limiter evidence, and refuses unrelated numeric-loop proxy evidence. Limiter/profile and repeated-run checks remain unavailable; supported outcome is an evidence-limited assessment.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/misleading-speedup/result.json",
        "variantReview": [
          {
            "name": "benchmark checklist read",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "supplied 4x assessment",
            "reportedObservation": "attempted inconclusive",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "completed work/error/cache evidence",
            "reportedObservation": "blocked not supplied",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "profiles/repeated runs/tuning/end-to-end",
            "reportedObservation": "blocked Bun absent and real parser workload absent",
            "assessment": "blocked-or-partial"
          }
        ],
        "limits": [
          "Bun absent; no Node/Python substitution.",
          "No live external actions.",
          "No model identity/full Git task revision observed.",
          "Local artifacts retained; durable persistence unverified.",
          "Retained responses and model-captured raw tool envelopes have early capture gaps/truncation; no blanket independent verification of all tool returns.",
          "Actual task Git revision unavailable; source-freeze binding is separate."
        ],
        "reviewedBy": "independent case_fixture_audit reviewer",
        "sourceCaseFile": "docs/parity/cases/skills/principle-explain-the-number.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence",
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
        "text": "No. The 4x claim is inconclusive. The only supplied measurement is one run with failed requests and uncounted cache hits, so equal completed work is not established. Runtime fixture performs a numeric loop, not the parser request path, and cannot validate that claim. Missing evidence includes exact revisions/configurations, timed region, data/concurrency, failures, correct outputs, cache counts, at least five interleaved A/B runs with median/range, profile/counters mapped to source, tuning parity and end-to-end share. A single sample supplies no spread or observed limiter. Bun is absent, so I did not run a replacement benchmark or invent measurements.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/misleading-speedup/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/misleading-speedup/result.json",
          "sha256": "4257d8924dea11885c4181b990defcc52affde616a1df5a1e13de31c74494df7",
          "bytes": 1653
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/checkpoint-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/checkpoint-tool.json",
            "sha256": "670a2c14d83c250d48f126dc3441653bc5a6fc2197f4fedecfe8b90a5f9e5296",
            "bytes": 770
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/required-companions-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/evidence/required-companions-tool.json",
            "sha256": "c821110b84d2270e05324a05fc8fb8387270bd8df8fb657592c9635d78974a0c",
            "bytes": 58320
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/misleading-speedup/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/misleading-speedup/result.json",
      "sha256": "4257d8924dea11885c4181b990defcc52affde616a1df5a1e13de31c74494df7",
      "bytes": 1653,
      "owners": [
        "grades-chatgpt-01-04.json#18"
      ],
      "text": "{\n  \"caseId\": \"misleading-speedup\",\n  \"batch\": \"batch-03\",\n  \"actualResponse\": \"No. The 4x claim is inconclusive. The only supplied measurement is one run with failed requests and uncounted cache hits, so equal completed work is not established. Runtime fixture performs a numeric loop, not the parser request path, and cannot validate that claim. Missing evidence includes exact revisions/configurations, timed region, data/concurrency, failures, correct outputs, cache counts, at least five interleaved A/B runs with median/range, profile/counters mapped to source, tuning parity and end-to-end share. A single sample supplies no spread or observed limiter. Bun is absent, so I did not run a replacement benchmark or invent measurements.\",\n  \"observedOperations\": [\n    \"named case and installed sources read using tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/required-companions-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"benchmark checklist read\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"supplied 4x assessment\",\n      \"observation\": \"attempted inconclusive\"\n    },\n    {\n      \"name\": \"completed work/error/cache evidence\",\n      \"observation\": \"blocked not supplied\"\n    },\n    {\n      \"name\": \"profiles/repeated runs/tuning/end-to-end\",\n      \"observation\": \"blocked Bun absent and real parser workload absent\"\n    }\n  ],\n  \"limits\": [\n    \"Bun absent; no Node/Python substitution.\",\n    \"No live external actions.\",\n    \"No model identity/full Git task revision observed.\",\n    \"Local artifacts retained; durable persistence unverified.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/misleading-speedup/case.json",
      "owner": "grades-chatgpt-01-04.json#18",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/misleading-speedup/input",
      "owner": "grades-chatgpt-01-04.json#18",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/misleading-speedup/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#18",
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
