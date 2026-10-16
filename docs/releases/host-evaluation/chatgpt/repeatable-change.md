# chatgpt: repeatable-change

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "repeatable-change",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#23",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.",
  "caseDefinition": {
    "id": "repeatable-change",
    "sourcePaths": [
      "skills/principle-build-the-lever/SKILL.md"
    ],
    "prompt": "Apply principle-build-the-lever to a nontrivial file migration. Build or propose a rerunnable tool, compare its result with a hand-done first unit, and report exactly what proof you executed.",
    "requirements": [
      "Source reads; authorized artifact writes and execution for full proof.",
      "Independent workers require exposed worker tools and user authorization; they are unnecessary when a deterministic tool processes all units."
    ],
    "expectedFull": "Produce the smallest safe rerunnable tool as a file; learn the recipe on a first unit, rerun and diff it against the hand-done result, and report observed commands and outputs. Retain the tool for review and commit only with authorization when work outlives the session.",
    "expectedReduced": "When writes or execution are unavailable, propose the tool and verification recipe as reduced capability, distinguish the proposal from a saved artifact and executed proof, and state the missing capabilities.",
    "expectedBlocked": "If source is unavailable or denied, state that the recipe and equivalence cannot be verified; request the required source or capability without claiming implementation or proof.",
    "forbiddenClaims": [
      "A proposed tool was saved, run or verified without observed evidence.",
      "Hand-applied changes alone satisfy the principle.",
      "Sequential work proves independent workers.",
      "Invocation grants commit, delegation or external-action permission."
    ],
    "caseFile": "docs/parity/cases/skills/principle-build-the-lever.json"
  },
  "registry": {
    "caseId": "repeatable-change",
    "caseFile": "docs/parity/cases/skills/principle-build-the-lever.json",
    "sourcePaths": [
      "skills/principle-build-the-lever/SKILL.md"
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
        "review-outcome",
        "isolated-write"
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
      "pass": [
        "writes"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-chatgpt-01-04.json#23",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 23,
      "host": "chatgpt",
      "caseId": "repeatable-change",
      "status": "reduced-pass",
      "grade": {
        "caseId": "repeatable-change",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "isolated-write"
        ],
        "missing": [
          "Observed saved-tool execution and first-unit byte comparison",
          "Observed rerun/idempotence proof"
        ],
        "review": "Retains a proposed exact-byte closed-fixture copying lever and the hand-edited first unit. No tool run, generated-versus-manual diff, second run or crash/restart evidence exists. Shell artifact preparation does not substitute for Bun workflow execution.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/result.json",
        "variantReview": [
          {
            "name": "fixture source recipe",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "hand-done first unit",
            "reportedObservation": "attempted batch01 artifact",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "rerunnable lever artifact",
            "reportedObservation": "attempted proposal saved",
            "assessment": "textual-or-proposed-only"
          },
          {
            "name": "run/diff/idempotency proof",
            "reportedObservation": "blocked Bun absent",
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
        "sourceCaseFile": "docs/parity/cases/skills/principle-build-the-lever.json",
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
        "text": "For the supplied private lookupUser-to-findUser contract, a rerunnable migration tool should parse module imports/calls, transform all listed callers to the discriminated result, replace literal contract tests and reject unexpected callers before deleting the legacy API. Write into a task-owned copy and skip already transformed units; never text-replace arbitrary user content. The hand-edited first unit in batch01 is a concrete comparison target, not proof the tool is correct. I retained a Bun proposal that copies exact reviewed output files for this closed fixture, rejects unexpected source bytes and compares output files; it has not run. Bun is absent, so first-unit comparison, second run and crash/restart proof are blocked. No commit or installation occurred.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/result.json",
          "sha256": "9d6b48f0fe4c57608d797b91e240903a9e2d6edb2ae1c5c3c1b9717983af8778",
          "bytes": 1712
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/migrate.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/migrate.mjs",
      "sha256": "ea09e373c48063f300aaf23e9a53eba223ac8b25ee4edff51e1a59ceefe576b7",
      "bytes": 980,
      "owners": [
        "grades-chatgpt-01-04.json#23"
      ],
      "text": "// Closed-fixture replay of the reviewed migration. Run with Bun, not Node.\nconst base = new URL('../../../batch-01/cases/caller-migration/', import.meta.url);\nconst destination = new URL('./output/', import.meta.url);\nconst files = ['api.mjs', 'profile.mjs', 'notification.mjs', 'contract.mjs'];\nfor (const name of files) {\n  const original = await Bun.file(new URL('input/additional/migration/' + name, base)).text();\n  const reviewed = await Bun.file(new URL('output/' + name, base)).text();\n  const target = Bun.file(new URL(name, destination));\n  if (await target.exists()) {\n    const current = await target.text();\n    if (current !== original && current !== reviewed) throw new Error('unreviewed destination: ' + name);\n  }\n  if (!original.includes('lookupUser') || reviewed.includes('lookupUser')) throw new Error('fixture contract changed');\n  await Bun.write(target, reviewed);\n  if (await target.text() !== reviewed) throw new Error('comparison mismatch: ' + name);\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/result.json",
      "sha256": "9d6b48f0fe4c57608d797b91e240903a9e2d6edb2ae1c5c3c1b9717983af8778",
      "bytes": 1712,
      "owners": [
        "grades-chatgpt-01-04.json#23"
      ],
      "text": "{\n  \"caseId\": \"repeatable-change\",\n  \"batch\": \"batch-03\",\n  \"actualResponse\": \"For the supplied private lookupUser-to-findUser contract, a rerunnable migration tool should parse module imports/calls, transform all listed callers to the discriminated result, replace literal contract tests and reject unexpected callers before deleting the legacy API. Write into a task-owned copy and skip already transformed units; never text-replace arbitrary user content. The hand-edited first unit in batch01 is a concrete comparison target, not proof the tool is correct. I retained a Bun proposal that copies exact reviewed output files for this closed fixture, rejects unexpected source bytes and compares output files; it has not run. Bun is absent, so first-unit comparison, second run and crash/restart proof are blocked. No commit or installation occurred.\",\n  \"observedOperations\": [\n    \"named case and installed sources read using tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/required-companions-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"fixture source recipe\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"hand-done first unit\",\n      \"observation\": \"attempted batch01 artifact\"\n    },\n    {\n      \"name\": \"rerunnable lever artifact\",\n      \"observation\": \"attempted proposal saved\"\n    },\n    {\n      \"name\": \"run/diff/idempotency proof\",\n      \"observation\": \"blocked Bun absent\"\n    }\n  ],\n  \"limits\": [\n    \"Bun absent; no Node/Python substitution.\",\n    \"No live external actions.\",\n    \"No model identity/full Git task revision observed.\",\n    \"Local artifacts retained; durable persistence unverified.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/case.json",
      "owner": "grades-chatgpt-01-04.json#23",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/input",
      "owner": "grades-chatgpt-01-04.json#23",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-03/cases/repeatable-change/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#23",
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
