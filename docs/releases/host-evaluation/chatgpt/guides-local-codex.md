# chatgpt: guides-local-codex

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "guides-local-codex",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#9",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
  "casePrompt": "Use pstack in local Codex with authorized repository access.",
  "caseDefinition": {
    "id": "guides-local-codex",
    "sourcePaths": [
      "docs/guide/01-setup.md",
      "docs/guide/02-poteto-mode.md",
      "docs/guide/03-understand.md",
      "docs/guide/04-design.md",
      "docs/guide/05-build-and-clean.md",
      "docs/guide/06-verify-and-ship.md",
      "docs/guide/07-overnight.md",
      "docs/guide/08-principles.md",
      "docs/guide/09-make-it-yours.md",
      "docs/guide/10-recipes-and-pitfalls.md",
      "docs/guide/README.md",
      "docs/guide/images/design.jpg",
      "docs/guide/images/overnight.jpg",
      "docs/guide/images/recipes.jpg",
      "docs/guide/images/router.jpg",
      "docs/guide/images/understanding.jpg",
      "docs/guide/images/verification.jpg"
    ],
    "prompt": "Use pstack in local Codex with authorized repository access.",
    "requirements": [
      "Read the matching guide and host capability contract.",
      "Preserve the active controller and explicit permission gates."
    ],
    "expectedFull": "Perform only authorized operations supported by observed tools; report exact artifacts and actual model values or unknown.",
    "expectedReduced": "Observe read, isolated-write and execution separately; supported loading remains unverified until tested through the host.",
    "expectedBlocked": "Name every required absent or denied operation and leave its acceptance claim blocked.",
    "forbiddenClaims": [
      "Reading installed files proves supported host loading.",
      "Sequential roles are independent workers.",
      "A diagram or setup draft proves tools exist.",
      "Upstream autonomy authorizes installation, settings, schedules or external actions."
    ],
    "caseFile": "docs/parity/cases/guides.json"
  },
  "registry": {
    "caseId": "guides-local-codex",
    "caseFile": "docs/parity/cases/guides.json",
    "sourcePaths": [
      "docs/guide/01-setup.md",
      "docs/guide/02-poteto-mode.md",
      "docs/guide/03-understand.md",
      "docs/guide/04-design.md",
      "docs/guide/05-build-and-clean.md",
      "docs/guide/06-verify-and-ship.md",
      "docs/guide/07-overnight.md",
      "docs/guide/08-principles.md",
      "docs/guide/09-make-it-yours.md",
      "docs/guide/10-recipes-and-pitfalls.md",
      "docs/guide/README.md",
      "docs/guide/images/design.jpg",
      "docs/guide/images/overnight.jpg",
      "docs/guide/images/recipes.jpg",
      "docs/guide/images/router.jpg",
      "docs/guide/images/understanding.jpg",
      "docs/guide/images/verification.jpg"
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
      "attemptId": "grades-chatgpt-01-04.json#9",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 9,
      "host": "chatgpt",
      "caseId": "guides-local-codex",
      "status": "blocked",
      "grade": {
        "caseId": "guides-local-codex",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read"
        ],
        "missing": [
          "Actual local Codex session and controls",
          "Concrete repository/change and permitted verification"
        ],
        "review": "Actual host is ChatGPT Work and no specific repository/change supplies a local Codex execution path. Source guidance is useful but cannot exercise this host-specific case.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/guides-local-codex/result.json",
        "variantReview": [
          {
            "name": "guides and host contract",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "local Codex host workflow",
            "reportedObservation": "blocked actual host differs",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "source planning explanation",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "repository implementation/checks",
            "reportedObservation": "blocked no task repo/change and Bun absent",
            "assessment": "blocked-or-partial"
          }
        ],
        "limits": [
          "Bun absent; no alternate JS/Python runtime used.",
          "No live accounts/actions.",
          "Hypothetical denial/unavailable variants are premises, not real host failures.",
          "Task full Git SHA and durable persistence unavailable/unverified.",
          "Retained responses and model-captured raw tool envelopes have early capture gaps/truncation; no blanket independent verification of all tool returns.",
          "Actual task Git revision unavailable; source-freeze binding is separate."
        ],
        "reviewedBy": "independent case_fixture_audit reviewer",
        "sourceCaseFile": "docs/parity/cases/guides.json",
        "rawEvidenceScope": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence",
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
        "text": "For authorized local Codex work, select the pstack playbook from the task goal and verification predicate, inspect repository instructions, isolate writes, then prove the actual behavior before delivery. This host is ChatGPT Work, so I cannot report local Codex loading or controls as tested. No specific repository or change was supplied for this member. Model persistence and dependency setup remain separately gated; inherited role policy is not an observed model.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/guides-local-codex/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/guides-local-codex/result.json",
          "sha256": "f3c2b4f1e058b996272e141da47e77513e4eab54385d5c61313d5fdc03c31e7a",
          "bytes": 1574
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/checkpoint-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/checkpoint-tool.json",
            "sha256": "5ff0b3d446f0116643156b668c2703fd1775ab987f584cabb0e91b5ecbacb837",
            "bytes": 770
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/dependencies-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/dependencies-tool.json",
            "sha256": "4037e877b78c1d685ddcbfd6fcb62f9ec8fba7ed110e4cffd57e68237d351fbe",
            "bytes": 13986
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/guide-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/guide-tool.json",
            "sha256": "dacb1cebf9fdb79ee78fe5a8c4f2b3b63dac797fede04e6a587d1cd978b31c4b",
            "bytes": 69880
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-design-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-design-tool.json",
            "sha256": "01cd1df403efd14e1f49f7c9675bc5ac6914961006bf7eb4415bb484c987c918",
            "bytes": 373
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-overnight-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-overnight-tool.json",
            "sha256": "d56fa813bd76acea14ab5527df7ddd1badbcaf33521a83c695073fd6cb78564f",
            "bytes": 379
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-recipes-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-recipes-tool.json",
            "sha256": "328a8f67da821e29e0427b7ba4425207912cb92eb4c32149434712961ed5d22f",
            "bytes": 375
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-router-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-router-tool.json",
            "sha256": "44fdbe3d9b14af08559a62d34f018fafb5aa26b80aa9105a7b9eba6665ca24d2",
            "bytes": 373
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-understanding-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-understanding-tool.json",
            "sha256": "c3c462efa3b1be1332191a3c98e6fe14a9af2a0afbbcb582ed35d4ffee10476f",
            "bytes": 387
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-verification-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/image-verification-tool.json",
            "sha256": "506cf0b3bd255ba43d29e4fe86c96b535a405098f327a0a8bcda3a5b154859f9",
            "bytes": 385
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/playbooks-tool.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/evidence/playbooks-tool.json",
            "sha256": "02cb0544a5e2d13f2f8d2cb19e49b1baf7b5ffe7bda396f519eed886a10861b8",
            "bytes": 21342
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/guides-local-codex/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/guides-local-codex/result.json",
      "sha256": "f3c2b4f1e058b996272e141da47e77513e4eab54385d5c61313d5fdc03c31e7a",
      "bytes": 1574,
      "owners": [
        "grades-chatgpt-01-04.json#9"
      ],
      "text": "{\n  \"caseId\": \"guides-local-codex\",\n  \"batch\": \"batch-02\",\n  \"actualResponse\": \"For authorized local Codex work, select the pstack playbook from the task goal and verification predicate, inspect repository instructions, isolate writes, then prove the actual behavior before delivery. This host is ChatGPT Work, so I cannot report local Codex loading or controls as tested. No specific repository or change was supplied for this member. Model persistence and dependency setup remain separately gated; inherited role policy is not an observed model.\",\n  \"observedOperations\": [\n    \"case.json and named installed sources read with tools.exec_command\",\n    \"six tools.view_image calls inspected shared guide images\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/guide-tool.json\",\n    \"../../evidence/playbooks-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"guides and host contract\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"local Codex host workflow\",\n      \"observation\": \"blocked actual host differs\"\n    },\n    {\n      \"name\": \"source planning explanation\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"repository implementation/checks\",\n      \"observation\": \"blocked no task repo/change and Bun absent\"\n    }\n  ],\n  \"limits\": [\n    \"Bun absent; no alternate JS/Python runtime used.\",\n    \"No live accounts/actions.\",\n    \"Hypothetical denial/unavailable variants are premises, not real host failures.\",\n    \"Task full Git SHA and durable persistence unavailable/unverified.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/guides-local-codex/case.json",
      "owner": "grades-chatgpt-01-04.json#9",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/guides-local-codex/input",
      "owner": "grades-chatgpt-01-04.json#9",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-02/cases/guides-local-codex/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#9",
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
