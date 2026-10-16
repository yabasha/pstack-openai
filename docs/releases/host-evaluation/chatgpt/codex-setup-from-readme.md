# chatgpt: codex-setup-from-readme

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "codex-setup-from-readme",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#3",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Start in a fresh Codex chat without approved installation. Follow README to Codex setup and inspect the documented marketplace route without loading.",
  "caseDefinition": {
    "id": "codex-setup-from-readme",
    "sourcePaths": [
      "docs/guide/01-setup.md"
    ],
    "prompt": "Start in a fresh Codex chat without approved installation. Follow README to Codex setup and inspect the documented marketplace route without loading.",
    "requirements": [
      "Starting state and exact action are in the prompt. README must link docs/setup/codex.md and the destination must exist.",
      "Read the full linked workflow and required contracts before dependent work.",
      "Record exact frozen package SHA, version, host tools, permission decisions and visible results. Do not install or alter settings without exact separate authorization.",
      "Inspect resulting artifacts and assignment revisions; source reads alone cannot establish installed discovery."
    ],
    "expectedFull": "After separately authorized supported loading, observe actual package discovery, exact installed-copy identity and all 51 root skills with three Benny exclusions. With required authorized tools, follow every documented phase and retain inspected artifact evidence at the exact frozen SHA.",
    "expectedReduced": "Readable marketplace instructions support a bounded walkthrough only. Without authorized loading and actual installed-copy discovery, report that setup remains unobserved.",
    "expectedBlocked": "Name absent or denied loading, discovery, execution, writes, independent review or setup. Leave affected gates blocked or not-run; produce only separately authorized read-only guidance. A documented loading route is unverified until exercised in a fresh host case.",
    "forbiddenClaims": [
      "Links or direct source reads prove installed discovery.",
      "Sequential roles are independent workers.",
      "An isolated helper snapshot proves this candidate or host passed.",
      "A resolution file, owner marker or upstream autonomy grants approval.",
      "Apply automatically accepts an update or refreshes a host."
    ],
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json"
  },
  "registry": {
    "caseId": "codex-setup-from-readme",
    "caseFile": "docs/parity/cases/documentation-walkthroughs.json",
    "sourcePaths": [
      "docs/guide/01-setup.md"
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
      "attemptId": "grades-chatgpt-01-04.json#3",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 3,
      "host": "chatgpt",
      "caseId": "codex-setup-from-readme",
      "status": "reduced-pass",
      "grade": {
        "caseId": "codex-setup-from-readme",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Actual fresh Codex host/UI inspection",
          "Authorized loading and exact installed-copy discovery"
        ],
        "review": "Reads the documented marketplace route without pretending this ChatGPT Work run is fresh Codex. Supported loading/discovery stays unperformed, as required for a source-only reduced walkthrough.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/codex-setup-from-readme/result.json",
        "variantReview": [
          {
            "name": "README route",
            "reportedObservation": "attempted read",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "documented marketplace explanation",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "fresh Codex/UI inspection",
            "reportedObservation": "blocked different actual host",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "install/enable/restart",
            "reportedObservation": "blocked explicitly unauthorized",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "51-name installed receipt",
            "reportedObservation": "blocked no discovery operation observed",
            "assessment": "blocked-or-partial"
          }
        ],
        "limits": [
          "No script execution: command -v bun exit 1.",
          "No external service/account operations.",
          "No observed package Git SHA or model identity.",
          "Local artifacts only; durable persistence untested.",
          "Retained responses and model-captured raw tool envelopes have early capture gaps/truncation; no blanket independent verification of all tool returns.",
          "Actual task Git revision unavailable; source-freeze binding is separate."
        ],
        "reviewedBy": "independent case_fixture_audit reviewer",
        "sourceCaseFile": "docs/parity/cases/documentation-walkthroughs.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence",
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
        "text": "README links docs/setup/codex.md and that document exists. The documented route uses .agents/plugins/marketplace.json and relative source.path, desktop restart, Plugins Directory selection, installation and a new enabled chat. None of that was performed: exact setup permission is absent and this is ChatGPT Work, not a fresh Codex desktop chat. Cache source reads do not prove all 51 registered names or final frozen SHA. No settings, package installation or configuration was altered.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/codex-setup-from-readme/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/codex-setup-from-readme/result.json",
          "sha256": "3911d3bf3ec817fe4fb5c5b1075e0759d68940d4bc3e4240c2b4edc210aae635",
          "bytes": 1500
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/actual-diffs-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/actual-diffs-tool.json",
            "sha256": "9c56bf96534fec4fb5a250108c99470239ddde7df96ae7833e3dd8d1ae0b371e",
            "bytes": 6155
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/read3-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/read3-tool.json",
            "sha256": "660fa99f9c84d5ec913f03e7c1fc3bb5f2b5fd9121f35275ca5d029277ea37fa",
            "bytes": 40695
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/read4-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/read4-tool.json",
            "sha256": "b0333000e00eba1939a09afc0c196151f2cd24ac784c4fe0a1ad605675532d94",
            "bytes": 48493
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/write1-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/evidence/write1-tool.json",
            "sha256": "617547cd73494b82fb01aa9d3e43fc21405f0d67cd9bfccd01cb191d0579ff5f",
            "bytes": 2795
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/codex-setup-from-readme/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/codex-setup-from-readme/result.json",
      "sha256": "3911d3bf3ec817fe4fb5c5b1075e0759d68940d4bc3e4240c2b4edc210aae635",
      "bytes": 1500,
      "owners": [
        "grades-chatgpt-01-04.json#3"
      ],
      "text": "{\n  \"caseId\": \"codex-setup-from-readme\",\n  \"batch\": \"batch-01\",\n  \"actualResponse\": \"README links docs/setup/codex.md and that document exists. The documented route uses .agents/plugins/marketplace.json and relative source.path, desktop restart, Plugins Directory selection, installation and a new enabled chat. None of that was performed: exact setup permission is absent and this is ChatGPT Work, not a fresh Codex desktop chat. Cache source reads do not prove all 51 registered names or final frozen SHA. No settings, package installation or configuration was altered.\",\n  \"observedOperations\": [\n    \"case/source files read through tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"README route\",\n      \"observation\": \"attempted read\"\n    },\n    {\n      \"name\": \"documented marketplace explanation\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"fresh Codex/UI inspection\",\n      \"observation\": \"blocked different actual host\"\n    },\n    {\n      \"name\": \"install/enable/restart\",\n      \"observation\": \"blocked explicitly unauthorized\"\n    },\n    {\n      \"name\": \"51-name installed receipt\",\n      \"observation\": \"blocked no discovery operation observed\"\n    }\n  ],\n  \"limits\": [\n    \"No script execution: command -v bun exit 1.\",\n    \"No external service/account operations.\",\n    \"No observed package Git SHA or model identity.\",\n    \"Local artifacts only; durable persistence untested.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/codex-setup-from-readme/case.json",
      "owner": "grades-chatgpt-01-04.json#3",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/codex-setup-from-readme/input",
      "owner": "grades-chatgpt-01-04.json#3",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/codex-setup-from-readme/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#3",
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
