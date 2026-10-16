# chatgpt: repeated-rule

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "repeated-rule",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#25",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "We have corrected the same mistake twice: generated release records omit the source revision. Apply principle-encode-lessons-in-structure. Replace the repeated prose warning with a concrete validator or structural check, explain where it belongs, and close the correction loop within the available authorization.",
  "caseDefinition": {
    "id": "repeated-rule",
    "sourcePaths": [
      "skills/principle-encode-lessons-in-structure/SKILL.md"
    ],
    "prompt": "We have corrected the same mistake twice: generated release records omit the source revision. Apply principle-encode-lessons-in-structure. Replace the repeated prose warning with a concrete validator or structural check, explain where it belongs, and close the correction loop within the available authorization.",
    "requirements": [
      "Propose a concrete validator or structural check that rejects a release record without its source revision instead of repeating a prose warning.",
      "Choose the strongest feasible mechanism, considering an unrepresentable state, CI lint or banned API, canonical helper and runtime check in that order.",
      "Capture the correction, distinguish a one-off from a recurring or systemic issue, route it to the appropriate durable layer and apply it or create a concrete todo.",
      "Delete redundant instructions when a structural fix enforces the rule; retain a prominent instruction and failure example when enforcement requires judgment.",
      "Report implementation, persistence and checks only when authorized and observed."
    ],
    "expectedFull": "The response proposes or implements an enforceable source-revision requirement at the strongest feasible layer, with a specific rejection condition and failure example. It routes the recurring correction to a validator or skill, closes the loop through authorized implementation or a concrete todo, and removes the redundant prose warning once enforcement exists. It reports only observed implementation and checks.",
    "expectedReduced": "If writes, execution or durable persistence are unavailable, provide the concrete validator condition, its integration point and a specific implementation todo as a reduced proposal. State which changes, checks or saves remain unperformed.",
    "expectedBlocked": "If the record format or required revision rule is unavailable, identify those missing inputs and keep any validator proposal provisional. Do not claim implemented enforcement or saved corrections.",
    "forbiddenClaims": [
      "Repeating the prose warning alone closes a recurring correction.",
      "An unimplemented validator enforces the rule.",
      "A claimed save without write and readback proves persistence.",
      "Structural package validation proves behavioral parity.",
      "Invocation metadata proves host enforcement.",
      "The principle grants authorization for global settings, installs or external actions."
    ],
    "caseFile": "docs/parity/cases/skills/principle-encode-lessons-in-structure.json"
  },
  "registry": {
    "caseId": "repeated-rule",
    "caseFile": "docs/parity/cases/skills/principle-encode-lessons-in-structure.json",
    "sourcePaths": [
      "skills/principle-encode-lessons-in-structure/SKILL.md"
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
      "attemptId": "grades-chatgpt-01-04.json#25",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 25,
      "host": "chatgpt",
      "caseId": "repeated-rule",
      "status": "reduced-pass",
      "grade": {
        "caseId": "repeated-rule",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "isolated-write"
        ],
        "missing": [
          "Authoritative release record schema and generator/CI integration",
          "Observed old-omission rejection and enforcement verification"
        ],
        "review": "A concrete parser rejection proposal, behavior test and implementation todo are retained with honest limits. Authoritative schema/generator/CI are missing and no failing-old-case test ran, so this is not enforced prevention or a completed correction loop.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/result.json",
        "variantReview": [
          {
            "name": "capture/route correction",
            "reportedObservation": "attempted local todo",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "validator artifact and test",
            "reportedObservation": "attempted write/readback",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "type/CI/generator integration",
            "reportedObservation": "blocked source absent",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "missing/invalid/valid revision runtime",
            "reportedObservation": "blocked Bun absent",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "remove redundant instruction",
            "reportedObservation": "blocked enforcement unverified",
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
        "sourceCaseFile": "docs/parity/cases/skills/principle-encode-lessons-in-structure.json",
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
        "text": "The repeated omission is a recurring correction, not a one-off. I retained a concrete parseReleaseRecord proposal rejecting a missing or malformed sourceRevision plus a Bun behavior test and correction-todo.md. Rank enforcement as required domain type, CI banned construction/schema lint, canonical helper, then runtime guard. This fixture is plain JavaScript and no actual generator/CI integration is supplied, so the parser is a candidate boundary guard rather than enforced architecture. The full lowercase 40-character SHA format is explicitly a proposed Git convention, pending the authoritative record schema. Integrate at every release construction boundary, prove the old omission fails, then delete redundant prose. Tests did not run because Bun is absent; local save/readback is observed and durable persistence is unverified.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/result.json",
          "sha256": "f8fb0d55878532ce3d21f3200f108ea8f444e71ccc6737293a3b5b57d9184544",
          "bytes": 2045
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/correction-todo.md",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/correction-todo.md",
      "sha256": "0fac7877245d24b318fd8225f37636e30a3c5477e6d588744a18a4238ae6ed24",
      "bytes": 946,
      "owners": [
        "grades-chatgpt-01-04.json#25"
      ],
      "text": "Recurring correction: generated release records twice omitted source revision.\n\nRoute: generator boundary and its canonical record construction, backed by CI.\nThe fixture is untyped JavaScript, so a compile-time unrepresentable state cannot protect arbitrary JSON. No actual release generator or CI definition was supplied. The retained runtime parser is a concrete candidate, not integrated enforcement.\n\nTodo: discover authoritative revision format and generator, derive a required branded revision type in a typed codebase, ban raw record construction or add CI schema validation, route canonical construction through the parser, and prove the original missing-revision fixture fails. Only after that observed enforcement remove redundant prose instructions. Keep judgment guidance if full provenance cannot be validated mechanically.\n\nLocal fixture file saved. Bun unavailable; tests unrun. Durable persistence and CI integration unverified.\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/release-record.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/release-record.mjs",
      "sha256": "0e37f808695063db6452c3b57fbd557c33ad4aea7123fe95288ba1e55be3a3c5",
      "bytes": 435,
      "owners": [
        "grades-chatgpt-01-04.json#25"
      ],
      "text": "export function parseReleaseRecord(value) {\n  if (value === null || typeof value !== 'object' || Array.isArray(value)) throw new Error('release record required');\n  if (typeof value.sourceRevision !== 'string' || !/^[a-f0-9]{40}$/.test(value.sourceRevision)) {\n    throw new Error('sourceRevision must contain the full 40-character lowercase Git SHA');\n  }\n  return Object.freeze({ ...value, sourceRevision: value.sourceRevision });\n}\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/release-record.test.mjs",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/release-record.test.mjs",
      "sha256": "66d99dd67c1bb9b19db2f3c19976466767cf7c264456149e571c1a7d3a871ce9",
      "bytes": 495,
      "owners": [
        "grades-chatgpt-01-04.json#25"
      ],
      "text": "import { test, expect } from 'bun:test';\nimport { parseReleaseRecord } from './release-record.mjs';\ntest('release record boundary rejects missing revision and preserves actual revision', () => {\n expect(() => parseReleaseRecord({ version: 'fixture' })).toThrow('sourceRevision');\n expect(() => parseReleaseRecord({ sourceRevision: 'short' })).toThrow('sourceRevision');\n expect(parseReleaseRecord({ version: 'fixture', sourceRevision: 'a'.repeat(40) }).sourceRevision).toBe('a'.repeat(40));\n});\n"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/result.json",
      "sha256": "f8fb0d55878532ce3d21f3200f108ea8f444e71ccc6737293a3b5b57d9184544",
      "bytes": 2045,
      "owners": [
        "grades-chatgpt-01-04.json#25"
      ],
      "text": "{\n  \"caseId\": \"repeated-rule\",\n  \"batch\": \"batch-04\",\n  \"actualResponse\": \"The repeated omission is a recurring correction, not a one-off. I retained a concrete parseReleaseRecord proposal rejecting a missing or malformed sourceRevision plus a Bun behavior test and correction-todo.md. Rank enforcement as required domain type, CI banned construction/schema lint, canonical helper, then runtime guard. This fixture is plain JavaScript and no actual generator/CI integration is supplied, so the parser is a candidate boundary guard rather than enforced architecture. The full lowercase 40-character SHA format is explicitly a proposed Git convention, pending the authoritative record schema. Integrate at every release construction boundary, prove the old omission fails, then delete redundant prose. Tests did not run because Bun is absent; local save/readback is observed and durable persistence is unverified.\",\n  \"observedOperations\": [\n    \"case.json and named installed sources read via tools.exec_command\",\n    \"proposal artifacts written through tools.apply_patch and read back\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/proposals-readback-tool.json\",\n    \"../../evidence/git-and-mode-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"capture/route correction\",\n      \"observation\": \"attempted local todo\"\n    },\n    {\n      \"name\": \"validator artifact and test\",\n      \"observation\": \"attempted write/readback\"\n    },\n    {\n      \"name\": \"type/CI/generator integration\",\n      \"observation\": \"blocked source absent\"\n    },\n    {\n      \"name\": \"missing/invalid/valid revision runtime\",\n      \"observation\": \"blocked Bun absent\"\n    },\n    {\n      \"name\": \"remove redundant instruction\",\n      \"observation\": \"blocked enforcement unverified\"\n    }\n  ],\n  \"limits\": [\n    \"No Bun execution or alternate runtime.\",\n    \"No live external actions/commits/settings changes.\",\n    \"No observed task Git revision/model identity.\",\n    \"Source fixtures inert; local persistence only.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/case.json",
      "owner": "grades-chatgpt-01-04.json#25",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/input",
      "owner": "grades-chatgpt-01-04.json#25",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/repeated-rule/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#25",
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
