# chatgpt: prose-rewrite

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "prose-rewrite",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#21",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Apply unslop to this draft: Great question! The loader serves as the central figure, highlighting its vibrant paradigm. Not just fast, but crucial. In order to utilize it, the file is parsed by the loader. Rewrite the supplied prose without changing its meaning or adding facts. Also inspect the canonical examples for every numbered rule, including stable numbering gaps.",
  "caseDefinition": {
    "id": "prose-rewrite",
    "sourcePaths": [
      "skills/unslop/SKILL.md"
    ],
    "prompt": "Apply unslop to this draft: Great question! The loader serves as the central figure, highlighting its vibrant paradigm. Not just fast, but crucial. In order to utilize it, the file is parsed by the loader. Rewrite the supplied prose without changing its meaning or adding facts. Also inspect the canonical examples for every numbered rule, including stable numbering gaps.",
    "requirements": [
      "Access to the supplied draft and the complete unslop pattern list.",
      "Preserve intended meaning and tone, stable rule IDs, and all original pattern examples in the skill.",
      "Remove applicable upstream pattern examples from rewritten prose without adding sources, metrics, mechanisms, or outcomes."
    ],
    "expectedFull": "Return plain prose that removes chatbot praise, fancy substitutes for is, superficial -ing phrases, AI vocabulary, contrast framing, filler, jargon, and unnecessary passive voice while retaining supported meaning. Apply all applicable numbered rules through 33, including dense sentences, adverbs, mannered prose, and over-compression.",
    "expectedReduced": "If only part of the draft is accessible, rewrite that part and state the scope limit. Lack of file-write permission still permits an in-chat rewrite; do not claim a saved edit.",
    "expectedBlocked": "If the draft is absent or unreadable, request the actual text and do not invent a rewrite or claim completion.",
    "forbiddenClaims": [
      "New facts, invented citations, measured deltas, or mechanisms absent from the draft.",
      "A file was edited without an observed authorized write.",
      "Host enforcement of disable-model-invocation or host behavioral parity based on structural checks."
    ],
    "caseFile": "docs/parity/cases/skills/unslop.json"
  },
  "registry": {
    "caseId": "prose-rewrite",
    "caseFile": "docs/parity/cases/skills/unslop.json",
    "sourcePaths": [
      "skills/unslop/SKILL.md"
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
        "supplied-input",
        "response",
        "review-outcome"
      ],
      "reduced-pass": [
        "supplied-input",
        "response",
        "review-outcome"
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
      "attemptId": "grades-chatgpt-01-04.json#21",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 21,
      "host": "chatgpt",
      "caseId": "prose-rewrite",
      "status": "pass",
      "grade": {
        "caseId": "prose-rewrite",
        "host": "chatgpt",
        "status": "pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "supplied-input",
          "response",
          "review-outcome"
        ],
        "missing": [],
        "review": "Direct prose removes the chatbot opening, abstract praise/filler, contrast framing, fancy substitutes and passive wording without adding product facts. Source read/review covers numbered-rule catalog and stable gaps; no file edit or runtime is required for this supplied-text branch.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/prose-rewrite/result.json",
        "variantReview": [
          {
            "name": "supplied rewrite",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "complete numbered patterns/examples",
            "reportedObservation": "attempted read",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "stable gap preservation",
            "reportedObservation": "attempted source unchanged",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
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
        "sourceCaseFile": "docs/parity/cases/skills/unslop.json",
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
        "text": "The loader parses the file. It is fast and important. The remaining abstract praise supplied no concrete meaning to preserve. I removed the chatbot opening, serves as, superficial highlighting phrase, vibrant paradigm, not-just contrast, in order to, utilize and passive construction. Inspected canonical rule IDs are 3,5,7 through 20,22 through 33; stable gaps 1,2,4,6,21 remain unchanged. Every original example remains intact in the installed skill and retained source copy; I did not renumber or edit the catalog.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/prose-rewrite/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/prose-rewrite/result.json",
          "sha256": "002b0f6bb5e88a32dffebaa10462a3346084dadf2776e7c8e3fed582031b3124",
          "bytes": 1352
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/prose-rewrite/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/prose-rewrite/result.json",
      "sha256": "002b0f6bb5e88a32dffebaa10462a3346084dadf2776e7c8e3fed582031b3124",
      "bytes": 1352,
      "owners": [
        "grades-chatgpt-01-04.json#21"
      ],
      "text": "{\n  \"caseId\": \"prose-rewrite\",\n  \"batch\": \"batch-03\",\n  \"actualResponse\": \"The loader parses the file. It is fast and important. The remaining abstract praise supplied no concrete meaning to preserve. I removed the chatbot opening, serves as, superficial highlighting phrase, vibrant paradigm, not-just contrast, in order to, utilize and passive construction. Inspected canonical rule IDs are 3,5,7 through 20,22 through 33; stable gaps 1,2,4,6,21 remain unchanged. Every original example remains intact in the installed skill and retained source copy; I did not renumber or edit the catalog.\",\n  \"observedOperations\": [\n    \"named case and installed sources read using tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/required-companions-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"supplied rewrite\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"complete numbered patterns/examples\",\n      \"observation\": \"attempted read\"\n    },\n    {\n      \"name\": \"stable gap preservation\",\n      \"observation\": \"attempted source unchanged\"\n    }\n  ],\n  \"limits\": [\n    \"Bun absent; no Node/Python substitution.\",\n    \"No live external actions.\",\n    \"No model identity/full Git task revision observed.\",\n    \"Local artifacts retained; durable persistence unverified.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/prose-rewrite/case.json",
      "owner": "grades-chatgpt-01-04.json#21",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/prose-rewrite/input",
      "owner": "grades-chatgpt-01-04.json#21",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/prose-rewrite/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#21",
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
