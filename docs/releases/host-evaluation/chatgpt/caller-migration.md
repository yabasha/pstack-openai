# chatgpt: caller-migration

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "caller-migration",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#1",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Replace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.",
  "caseDefinition": {
    "id": "caller-migration",
    "sourcePaths": [
      "skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md"
    ],
    "prompt": "Replace an internal API with the agreed new contract. Inventory all callers, migrate them, update contract tests and delete the old API in one reviewed unit. Verify that no external consumers need backward compatibility and that coordinated breaking changes are acceptable. If source, writes or execution are unavailable, state the limits.",
    "requirements": [
      "Source and caller usage evidence",
      "No external compatibility requirement and coordinated breaking changes accepted",
      "Authorized writes for migration and deletion",
      "Execution for observed checks"
    ],
    "expectedFull": "Inventory all callers, migrate every caller and remove the old API in the same reviewed refactor unit. Update tests to assert the new contract and delete tests protecting only obsolete implementation details. Use temporary adapters only as exceptional time-boxed measures. Confirm applicability and report observed checks.",
    "expectedReduced": "With source available but writes or execution unavailable, provide a coordinated caller migration and API deletion proposal as reduced capability. State which changes and checks were not performed.",
    "expectedBlocked": "If source or caller evidence is missing, or external compatibility or coordinated breaking-change requirements are unresolved, block claims that immediate deletion is safe or complete and identify the missing evidence or decision.",
    "forbiddenClaims": [
      "Old API preserved solely because internal callers still exist",
      "Partial migration presented as completed caller migration",
      "Default permanent compatibility adapter",
      "Deletion claimed safe without checking external consumers and applicability",
      "Unperformed writes or checks claimed complete",
      "Structural validation claimed as host behavior or metadata enforcement"
    ],
    "caseFile": "docs/parity/cases/skills/principle-migrate-callers-then-delete-legacy-apis.json"
  },
  "registry": {
    "caseId": "caller-migration",
    "caseFile": "docs/parity/cases/skills/principle-migrate-callers-then-delete-legacy-apis.json",
    "sourcePaths": [
      "skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md"
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
      "attemptId": "grades-chatgpt-01-04.json#1",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 1,
      "host": "chatgpt",
      "caseId": "caller-migration",
      "status": "reduced-pass",
      "grade": {
        "caseId": "caller-migration",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "isolated-write"
        ],
        "missing": [
          "Bun baseline/new-contract execution",
          "Observed behavioral equivalence"
        ],
        "review": "Retained successful write receipt and actual diff show findUser migration, all supplied callers and contract edits, with no legacy export left. Author explicitly withholds behavioral completion. Runtime baseline/new-contract checks never ran because Bun was absent.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/result.json",
        "variantReview": [
          {
            "name": "source inventory",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "coordinated breaking applicability",
            "reportedObservation": "attempted fixture scope read",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "migration and legacy removal",
            "reportedObservation": "attempted isolated edits",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "baseline/new contract execution",
            "reportedObservation": "blocked Bun absent",
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
        "sourceCaseFile": "docs/parity/cases/skills/principle-migrate-callers-then-delete-legacy-apis.json",
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
        "text": "The supplied scope explicitly lists every private consumer, disclaims external compatibility obligations and accepts coordinated breaking changes. I copied the migration fixture, replaced lookupUser with findUser({users,id}), migrated profileLabel and recipient and the literal contract tests, then removed the legacy export in the same case-owned unit. Static search found no lookupUser in executable output modules. Unknown and null missing-user behavior are represented in tests. Bun is absent, so neither baseline nor new contract executed; behavioral equivalence and completion remain unverified.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/result.json",
          "sha256": "d2fd757bdf00a7c1e11fa351f7d382be4755540171e1bc2fd53322060ce392d2",
          "bytes": 1562
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/output/api.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/output/api.mjs",
      "sha256": "c11e3f1a70c5792a266052792862e271cf716defc5f6c966e248d9ee976e7b25",
      "bytes": 172,
      "owners": [
        "grades-chatgpt-01-04.json#1"
      ],
      "text": "export function findUser({ users, id }) {\n  const user = users.find(user => user.id === id);\n  return user === undefined ? { kind: 'missing' } : { kind: 'found', user };\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/output/contract.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/output/contract.mjs",
      "sha256": "9fcc4f5f9b40ade7bc23919a138c302ce3f97ce2a74cf555c1d56cfe0b190cf1",
      "bytes": 663,
      "owners": [
        "grades-chatgpt-01-04.json#1"
      ],
      "text": "import { expect, test } from 'bun:test';\nimport { findUser } from './api.mjs';\nimport { profileLabel } from './profile.mjs';\nimport { recipient } from './notification.mjs';\ntest('found and missing behavior', () => {\n const users = [{ id: 'u1', name: 'Ada', email: 'ada@example.invalid' }];\n expect(findUser({ users, id: 'u1' })).toEqual({ kind: 'found', user: users[0] });\n expect(findUser({ users, id: 'absent' })).toEqual({ kind: 'missing' });\n expect(profileLabel(users, 'u1')).toBe('Ada');\n expect(profileLabel(users, 'absent')).toBe('Unknown');\n expect(recipient(users, 'u1')).toBe('ada@example.invalid');\n expect(recipient(users, 'absent')).toBe(null);\n});\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/output/notification.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/output/notification.mjs",
      "sha256": "013f24fb2266188e87205088e5ba4ff672958414c377b21deb3435eb10837614",
      "bytes": 182,
      "owners": [
        "grades-chatgpt-01-04.json#1"
      ],
      "text": "import { findUser } from './api.mjs';\nexport function recipient(users, id) {\n  const result = findUser({ users, id });\n  return result.kind === 'found' ? result.user.email : null;\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/output/profile.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/output/profile.mjs",
      "sha256": "c5514fa479b90c4a781e2f9ca790d980b584d68838640d720961d99c80ecfaf5",
      "bytes": 189,
      "owners": [
        "grades-chatgpt-01-04.json#1"
      ],
      "text": "import { findUser } from './api.mjs';\nexport function profileLabel(users, id) {\n  const result = findUser({ users, id });\n  return result.kind === 'found' ? result.user.name : 'Unknown';\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/result.json",
      "sha256": "d2fd757bdf00a7c1e11fa351f7d382be4755540171e1bc2fd53322060ce392d2",
      "bytes": 1562,
      "owners": [
        "grades-chatgpt-01-04.json#1"
      ],
      "text": "{\n  \"caseId\": \"caller-migration\",\n  \"batch\": \"batch-01\",\n  \"actualResponse\": \"The supplied scope explicitly lists every private consumer, disclaims external compatibility obligations and accepts coordinated breaking changes. I copied the migration fixture, replaced lookupUser with findUser({users,id}), migrated profileLabel and recipient and the literal contract tests, then removed the legacy export in the same case-owned unit. Static search found no lookupUser in executable output modules. Unknown and null missing-user behavior are represented in tests. Bun is absent, so neither baseline nor new contract executed; behavioral equivalence and completion remain unverified.\",\n  \"observedOperations\": [\n    \"case/source files read through tools.exec_command\",\n    \"case-owned artifact writes through tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"source inventory\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"coordinated breaking applicability\",\n      \"observation\": \"attempted fixture scope read\"\n    },\n    {\n      \"name\": \"migration and legacy removal\",\n      \"observation\": \"attempted isolated edits\"\n    },\n    {\n      \"name\": \"baseline/new contract execution\",\n      \"observation\": \"blocked Bun absent\"\n    }\n  ],\n  \"limits\": [\n    \"No script execution: command -v bun exit 1.\",\n    \"No external service/account operations.\",\n    \"No observed package Git SHA or model identity.\",\n    \"Local artifacts only; durable persistence untested.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/case.json",
      "owner": "grades-chatgpt-01-04.json#1",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/input",
      "owner": "grades-chatgpt-01-04.json#1",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/output/scope.md",
      "owner": "grades-chatgpt-01-04.json#1",
      "reason": "Unchanged shared synthetic fixture text included once in controller report",
      "sharedFixture": "fixtures/shared/additional/migration/scope.md",
      "sha256": "e8fb30ecb9f6e88b2bb9d5cbe00ac8bfe59531b4c683fdee2f70f7777fa8a905",
      "bytes": 695
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-01/cases/caller-migration/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#1",
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
