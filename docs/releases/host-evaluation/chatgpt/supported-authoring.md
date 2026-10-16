# chatgpt: supported-authoring

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **reduced-pass**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "supported-authoring",
  "acceptedStatus": "reduced-pass",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#19",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Author or modify a skill with this playbook. Inspect the available authoring workflow and its validator. Preserve the skill voice, validate structural contracts, and report unknown trigger performance without assuming create-skill is installed or PR writes are authorized.",
  "caseDefinition": {
    "id": "supported-authoring",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/authoring-a-skill.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/principle-encode-lessons-in-structure/SKILL.md"
    ],
    "prompt": "Author or modify a skill with this playbook. Inspect the available authoring workflow and its validator. Preserve the skill voice, validate structural contracts, and report unknown trigger performance without assuming create-skill is installed or PR writes are authorized.",
    "requirements": [
      "Inspect exposed capabilities and the available authoring workflow instructions and actual validator before use; identify the missing create-skill dependency.",
      "Preserve voice ownership, decision-changing prose, confusing-rule explanations, scope-matched tone, structural-source pointers, path delegation and proposals for recurring uncaptured workflows.",
      "Check name and description frontmatter, referenced files and cross-skill links; run structural test cases with fixtures and skip subjective tests.",
      "Apply Opening a PR only when its dependency, capabilities and authorization permit; preserve the skill artifact when PR delivery is deferred.",
      "Reply with skill summary, key design decisions and validation notes; distinguish observed results from unknown trigger performance."
    ],
    "expectedFull": "An available supported authoring workflow runs after its instructions and validator are inspected. The authored skill passes the observed structural checks and structural test cases. Subjective tests are skipped. The reply identifies the actual workflow, states create-skill is absent unless discovered, leaves unknown trigger performance unverified and reports observed authorized PR delivery or its explicit deferral.",
    "expectedReduced": "With authorized writes but no supported authoring workflow, produce only a provisional skill draft and manual checklist. Preserve the missing create-skill block, unexecuted validation and unknown trigger performance. If authoring and validation succeed but PR delivery is unavailable, retain the validated local skill and report the deferred PR dependency.",
    "expectedBlocked": "Without an available authoring workflow and without authorization or capability for a provisional draft, report the missing create-skill dependency and unavailable operation. Unavailable validation or PR delivery remains explicitly blocked or deferred; no completion claim substitutes for it.",
    "forbiddenClaims": [
      "create-skill shipped or executed without discovery and observed evidence.",
      "A provisional draft or manual checklist proves supported authoring execution or validator success.",
      "Structural checks prove trigger performance, subjective quality or host behavioral parity.",
      "A PR was created, commits made or external writes performed without authorization and observed results.",
      "Path delegation to another skill proves independent worker execution."
    ],
    "caseFile": "docs/parity/cases/playbooks/authoring-a-skill.json"
  },
  "registry": {
    "caseId": "supported-authoring",
    "caseFile": "docs/parity/cases/playbooks/authoring-a-skill.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/authoring-a-skill.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
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
        "review-outcome",
        "execution",
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
        "execution",
        "writes"
      ],
      "reduced-pass": []
    }
  },
  "attempts": [
    {
      "attemptId": "grades-chatgpt-09-12.json#19",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 19,
      "host": "chatgpt",
      "caseId": "supported-authoring",
      "status": "reduced-pass",
      "grade": {
        "caseId": "supported-authoring",
        "batch": "batch-11",
        "host": "chatgpt",
        "status": "reduced-pass",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Actual supported alternate authoring/validator source reads and provisional draft/manual reference inspection useful. Bun absent means no init/validator/structural test; missing required create-skill remains explicit, no registration/trigger proof.",
        "actualResponse": "Created only a provisional sandbox skill draft review-fixture-status. It tells readers to distinguish proposed, local, verified and shipped claims against the supplied inert history and preserve corrections. The selected pstack Authoring playbook was read; missing create-skill remains explicit. I also successfully read the exposed host Flora skill-creator and its actual quick_validate.py through tools.skills__read. That is a capability-specific alternative, not proof create-skill ran. Its validator checks YAML/name/description/naming rules, not referenced-file existence or trigger performance. Manual inspection sees required name/description, a lowercase-hyphen name and one existing history.json reference. The reference existence probe returned exit0; no cross-skill links are introduced. Bun is absent, so init/validator scripts and structural test fixtures did not execute. Subjective/trigger tests were not performed. Voice stays terse and imperative; repeated evidence rules point at the input instead of copying it. No installation, registration, remote-skills Git change, commit, push or PR. Local draft cannot establish the required authoring loop or observed triggering.",
        "variants": [
          {
            "name": "pstack authoring caller/full delivery contract",
            "state": "attempted",
            "reason": "Actual source reads retained"
          },
          {
            "name": "host supported authoring workflow",
            "state": "attempted",
            "reason": "tools.skills__read c11/skill-creator succeeded"
          },
          {
            "name": "actual validator source",
            "state": "attempted",
            "reason": "tools.skills__read quick_validate.py succeeded"
          },
          {
            "name": "sandbox provisional draft/manual structural checks",
            "state": "attempted",
            "reason": "skill-draft/SKILL.md and copied reference inspected; existence exit0"
          },
          {
            "name": "missing create-skill loop",
            "state": "blocked",
            "reason": "Not installed/exposed as required companion; alternative not equivalent"
          },
          {
            "name": "init_skill/quick_validate/structural fixture execution",
            "state": "blocked",
            "reason": "Bun absent; Python substitute prohibited"
          },
          {
            "name": "subjective tests/trigger performance",
            "state": "blocked",
            "reason": "No real-use forward tests or trigger observation"
          },
          {
            "name": "PR delivery/registration/global skill persistence",
            "state": "blocked",
            "reason": "Unauthorized live/global writes; no artifacts installed"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/supported-authoring/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/supported-authoring/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "missing create-skill loop",
            "reason": "Not installed/exposed as required companion; alternative not equivalent"
          },
          {
            "variant": "init_skill/quick_validate/structural fixture execution",
            "reason": "Bun absent; Python substitute prohibited"
          },
          {
            "variant": "subjective tests/trigger performance",
            "reason": "No real-use forward tests or trigger observation"
          },
          {
            "variant": "PR delivery/registration/global skill persistence",
            "reason": "Unauthorized live/global writes; no artifacts installed"
          }
        ],
        "limits": [
          "Bun absent; no Node/Python runtime substitute.",
          "No live accounts/services/external writes/schedules/global settings.",
          "Task Git revision absent; supplied sourceFreeze is not verified host Git HEAD.",
          "Early raw metadata export incomplete; truncated outputs retained as returned, not reconstructed.",
          "Prior Node/Python deviation preserved.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "An available supported authoring workflow runs after its instructions and validator are inspected. The authored skill passes the observed structural checks and structural test cases. Subjective tests are skipped. The reply identifies the actual workflow, states create-skill is absent unless discovered, leaves unknown trigger performance unverified and reports observed authorized PR delivery or its explicit deferral.",
        "reducedExpected": "With authorized writes but no supported authoring workflow, produce only a provisional skill draft and manual checklist. Preserve the missing create-skill block, unexecuted validation and unknown trigger performance. If authoring and validation succeed but PR delivery is unavailable, retain the validated local skill and report the deferred PR dependency.",
        "concreteFixCandidates": [],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "reviewedBy": "grade_contract_audit"
          },
          {
            "observation": "review-outcome",
            "evidence": "grades-chatgpt-09-12.json",
            "reviewedBy": "grade_contract_audit independent qualitative reviewer"
          }
        ]
      },
      "topLevelContext": {
        "scope": "Actual ChatGPT Work remaining batches09..12,30cases",
        "gradingNotes": [
          "Independent outcome review of retained actual responses/variants/source artifacts, not exported selfgrades.",
          "Native UI aggregate reads/commands/worker activity supplied by parent; exact model-captured logs treated with explicit provenance gaps.",
          "No proxy programs/fixture verdicts count as actual service or worker results.",
          "Missing taskGit and unavailable Bun remain required-method blockers; tools themselves not declared absent.",
          "All named requested variants must be addressed before full. No full awarded in this set.",
          "Old original source path failures retained; documented fallback source reads not automatically rejected.",
          "history-evidence is included because actual cloud batch09 contains it; do not count duplicate historical case twice when aggregating target coverage."
        ]
      },
      "response": {
        "text": "Created only a provisional sandbox skill draft review-fixture-status. It tells readers to distinguish proposed, local, verified and shipped claims against the supplied inert history and preserve corrections. The selected pstack Authoring playbook was read; missing create-skill remains explicit. I also successfully read the exposed host Flora skill-creator and its actual quick_validate.py through tools.skills__read. That is a capability-specific alternative, not proof create-skill ran. Its validator checks YAML/name/description/naming rules, not referenced-file existence or trigger performance. Manual inspection sees required name/description, a lowercase-hyphen name and one existing history.json reference. The reference existence probe returned exit0; no cross-skill links are introduced. Bun is absent, so init/validator scripts and structural test fixtures did not execute. Subjective/trigger tests were not performed. Voice stays terse and imperative; repeated evidence rules point at the input instead of copying it. No installation, registration, remote-skills Git change, commit, push or PR. Local draft cannot establish the required authoring loop or observed triggering.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/supported-authoring/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/supported-authoring/result.json",
          "sha256": "9a76e29425ddedb37f505c96517ffdbf95df5dca4eb34b4e801cc1836636f2ba",
          "bytes": 3485
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
            "sha256": "a0f4eb6e5baaded49263375472ed1d7b945b1aa4459538f99c6abf2f46b3ebf5",
            "bytes": 28398
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/supported-authoring/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/supported-authoring/case.json",
            "sha256": "bf9d018a84d0c62fc8135e8e553c83266a0ff3abf78bba11ba85d4f4f6f7c429",
            "bytes": 1347
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/supported-authoring/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-11/cases/supported-authoring/evidence/source-read-status.tsv",
            "sha256": "8423071726f57e41ae8c8f4faf574ccb256cc5df39d7fe767b739ceaaa51ca12",
            "bytes": 155
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-11/results.json",
              "reviewedBy": "grade_contract_audit"
            },
            {
              "observation": "review-outcome",
              "evidence": "grades-chatgpt-09-12.json",
              "reviewedBy": "grade_contract_audit independent qualitative reviewer"
            }
          ]
        }
      }
    }
  ],
  "artifactProjections": [],
  "skippedManifest": [],
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
