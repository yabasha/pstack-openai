# chatgpt: route-recipe

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "route-recipe",
  "acceptedStatus": "pass",
  "acceptedAttemptId": "grades-chatgpt-01-04.json#29",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Which pstack workflow should I use to reproduce an app bug and prove the fix? Give me a prompt; do not start the work.",
  "caseDefinition": {
    "id": "route-recipe",
    "sourcePaths": [
      "skills/poteto-help/SKILL.md",
      "skills/poteto-help/references/prompting.md",
      "skills/poteto-help/references/recipes.md"
    ],
    "prompt": "Which pstack workflow should I use to reproduce an app bug and prove the fix? Give me a prompt; do not start the work.",
    "requirements": [
      "Read the selected local leaf and Bug fix playbook before recommending their details.",
      "Provide at most one concrete prompt, the source link, and the relevant verification requirement.",
      "Check whether the referenced playbook and app verification tool exist; disclose pending or missing dependencies.",
      "For any customization follow-up, explain source options but gate personal-mode drafting and custom skill edits on reviewed dispositions for the complete baseline and observed supported behavior or explicit blocks for each host, independently of authorization."
    ],
    "expectedFull": "Route to the existing reviewed Bug fix playbook under poteto-mode, provide one reproduction-and-verification recipe and a source link, and do not start a help-only run.",
    "expectedReduced": "When app verification is unavailable, offer only the checks actually supported, label the reduction, and do not promise a video or independent workers. If the playbook is pending, identify its source route as pending rather than claim an existing port.",
    "expectedBlocked": "When the selected local playbook cannot be read, report that routing cannot yet establish an existing ported recipe. Give the pinned source reference and explain the missing local dependency without starting work.",
    "forbiddenClaims": [
      "A recipe proves host behavior passed.",
      "Cursor modes, slash commands, model rules or loop APIs are registered on this host.",
      "Missing local playbooks are existing reviewed ports.",
      "A help question authorizes execution, installation, external writes or scheduling.",
      "User authorization alone permits personal customization before complete baseline review and per-host evidence or explicit blocks."
    ],
    "caseFile": "docs/parity/cases/skills/poteto-help.json"
  },
  "registry": {
    "caseId": "route-recipe",
    "caseFile": "docs/parity/cases/skills/poteto-help.json",
    "sourcePaths": [
      "skills/poteto-help/SKILL.md",
      "skills/poteto-help/references/prompting.md",
      "skills/poteto-help/references/recipes.md"
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
      "attemptId": "grades-chatgpt-01-04.json#29",
      "order": 0,
      "gradeFile": "grades-chatgpt-01-04.json",
      "rankWithinFile": 29,
      "host": "chatgpt",
      "caseId": "route-recipe",
      "status": "pass",
      "grade": {
        "caseId": "route-recipe",
        "host": "chatgpt",
        "status": "pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "missing": [],
        "review": "Fulfills the help-only request with one poteto-mode Bug fix reproduction-and-verification prompt and source link. Reads the existing playbook, discloses absent app harness/Bun, gates customization on complete baseline and actual support, and starts no repro. Runtime is not required for this requested recipe.",
        "responseArtifact": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/route-recipe/result.json",
        "variantReview": [
          {
            "name": "source route/prompt",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "local playbook existence",
            "reportedObservation": "attempted",
            "assessment": "Artifact/source claim assessed within overall review; no automatic execution credit"
          },
          {
            "name": "app verification tool",
            "reportedObservation": "blocked no target/harness supplied",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "repro/build",
            "reportedObservation": "blocked help-only instruction",
            "assessment": "blocked-or-partial"
          },
          {
            "name": "customization follow-up",
            "reportedObservation": "blocked baseline gate; none performed",
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
        "sourceCaseFile": "docs/parity/cases/skills/poteto-help.json",
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
        "text": "Use poteto-mode's Bug fix playbook. One prompt: `/poteto-mode reproduce <exact app symptom> with the project's verified app-control harness. If it reproduces on the named base revision, fix the root cause and show the same flow succeeding, with before-and-after evidence. Do not commit, push or open a PR without authorization.` Source: https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/poteto-mode/playbooks/bug-fix.md . The local Bug fix playbook exists and was read. No project verify-* harness or target app was supplied; runtime, matching control companion and Bun execution remain blocked. This is help only; no repro started. For customization later, source automate-me/reflect/authoring routes exist, but personal mode drafting or skill edits require reviewed complete-baseline dispositions and actual support or explicit blocks for each host, separately from write authorization.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/route-recipe/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/route-recipe/result.json",
          "sha256": "aa53a5572ea62e2669408c39aa29fc47d885b6f9a1d4de04142dbffa07024412",
          "bytes": 2023
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
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/route-recipe/result.json",
      "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/route-recipe/result.json",
      "sha256": "aa53a5572ea62e2669408c39aa29fc47d885b6f9a1d4de04142dbffa07024412",
      "bytes": 2023,
      "owners": [
        "grades-chatgpt-01-04.json#29"
      ],
      "text": "{\n  \"caseId\": \"route-recipe\",\n  \"batch\": \"batch-04\",\n  \"actualResponse\": \"Use poteto-mode's Bug fix playbook. One prompt: `/poteto-mode reproduce <exact app symptom> with the project's verified app-control harness. If it reproduces on the named base revision, fix the root cause and show the same flow succeeding, with before-and-after evidence. Do not commit, push or open a PR without authorization.` Source: https://github.com/cursor/plugins/blob/df581122cde17e6e27686b5a448bde23e4ad4318/pstack/skills/poteto-mode/playbooks/bug-fix.md . The local Bug fix playbook exists and was read. No project verify-* harness or target app was supplied; runtime, matching control companion and Bun execution remain blocked. This is help only; no repro started. For customization later, source automate-me/reflect/authoring routes exist, but personal mode drafting or skill edits require reviewed complete-baseline dispositions and actual support or explicit blocks for each host, separately from write authorization.\",\n  \"observedOperations\": [\n    \"case.json and named installed sources read via tools.exec_command\"\n  ],\n  \"evidence\": [\n    \"case.json\",\n    \"source-reads.txt\",\n    \"input\",\n    \"../../evidence/proposals-readback-tool.json\",\n    \"../../evidence/git-and-mode-tool.json\"\n  ],\n  \"variants\": [\n    {\n      \"name\": \"source route/prompt\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"local playbook existence\",\n      \"observation\": \"attempted\"\n    },\n    {\n      \"name\": \"app verification tool\",\n      \"observation\": \"blocked no target/harness supplied\"\n    },\n    {\n      \"name\": \"repro/build\",\n      \"observation\": \"blocked help-only instruction\"\n    },\n    {\n      \"name\": \"customization follow-up\",\n      \"observation\": \"blocked baseline gate; none performed\"\n    }\n  ],\n  \"limits\": [\n    \"No Bun execution or alternate runtime.\",\n    \"No live external actions/commits/settings changes.\",\n    \"No observed task Git revision/model identity.\",\n    \"Source fixtures inert; local persistence only.\"\n  ]\n}\n"
    }
  ],
  "skippedManifest": [
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/route-recipe/case.json",
      "owner": "grades-chatgpt-01-04.json#29",
      "reason": "copied source/input or administrative evaluator helper"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/route-recipe/input",
      "owner": "grades-chatgpt-01-04.json#29",
      "reason": "input/source/before/support/dependency/Git tree omitted"
    },
    {
      "path": "chatgpt/remaining/remaining-evaluation/batches/batch-04/cases/route-recipe/source-reads.txt",
      "owner": "grades-chatgpt-01-04.json#29",
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
