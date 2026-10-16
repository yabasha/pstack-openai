# chatgpt: preserved-behavior

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "preserved-behavior",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#11",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Refactor a fixture invoice formatter by removing a one-caller wrapper and consolidating duplicated state. Preserve literal formatted outputs, empty inputs, rounding and errors. Capture the current outputs before edits. Rename its internal API and migrate code, string references, docs and back-references together. One fixture exposes an unrelated bug, which must stay separate. A speculative abstraction adds reader load and must be reverted. Permit local edits and execution but no external writes. Repeat with workers unavailable, execution denied and behavior coverage absent. Return the changed structure, held pin, equivalence proof, reader-load delta, shipped and reverted work.",
  "caseDefinition": {
    "id": "preserved-behavior",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/refactoring.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/playbooks/feature.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/how/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/architect/SKILL.md",
      "skills/principle-model-the-domain/SKILL.md",
      "skills/principle-foundational-thinking/SKILL.md",
      "skills/principle-redesign-from-first-principles/SKILL.md",
      "skills/principle-subtract-before-you-add/SKILL.md",
      "skills/principle-laziness-protocol/SKILL.md",
      "skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/principle-minimize-reader-load/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md"
    ],
    "prompt": "Refactor a fixture invoice formatter by removing a one-caller wrapper and consolidating duplicated state. Preserve literal formatted outputs, empty inputs, rounding and errors. Capture the current outputs before edits. Rename its internal API and migrate code, string references, docs and back-references together. One fixture exposes an unrelated bug, which must stay separate. A speculative abstraction adds reader load and must be reverted. Permit local edits and execution but no external writes. Repeat with workers unavailable, execution denied and behavior coverage absent. Return the changed structure, held pin, equivalence proof, reader-load delta, shipped and reverted work.",
    "requirements": [
      "Read the full mode and eight-step Refactoring playbook, required leaves and routed companion contracts. Record steps before task-specific todos. Route large or cross-cutting work to figure-it-out and named redesigns that change behavior to Feature. Split newly discovered bugs or features out and deliver the structural change first against its pinned contract.",
      "Use how to trace current behavior, then create and execute characterization tests, snapshots or an equivalence harness before moving structure. Write coverage first if absent. Type checks and lint are insufficient pins.",
      "Name the missing domain structure and target module layout, types and call graph. Keep clear local boring code; new shape deletes branches or invalid states. Crossing a function boundary requires complete architect exploration with its runner prompts, rationale and candidate screening.",
      "Subtract dead code, one-caller wrappers, redundant validators and orphan references before additions. Keep the smallest change that reaches the target and revert speculation.",
      "Each small move keeps the original pin green. Migrate every API caller and delete the old API in the same wave without compatibility shims or parallel paths. Inspect actual files for rename usages in strings, prose and back-references. Delegate mechanical edits with the complete poteto prompt, exact revision, ownership and observed inherited or supported configured selection. Inspect artifacts and review the diff.",
      "Verify unchanged behavior on the real artifact. Larger reshapes require old/new output diffs, baseline replay or a matching-surface smoke run through actual authorized controls. Retain outputs and failures.",
      "Assess reduced layers to trace and state to hold. Revert a diff that lowers neither. Do not invent measured reader times.",
      "Order verified subtraction, reshape and cleanup units. Rebase, commit and run complete Opening a PR only when authorized and available. Retain deferred dependencies and unperformed actions. Return all reply artifacts and no new behavior."
    ],
    "expectedFull": "Observed authorized independent mechanical delegation returns inspected artifacts at the assigned revision. The before-edit pin and each subsequent step have matching literal output evidence, including errors and rounding. All callers and textual references move together and the old API disappears. Architecture exploration runs when triggered. The actual artifact has equivalence proof and a source-grounded reader-load reduction. Bug work remains separate and speculation is reverted. With explicit delivery authorization and complete dependencies, ordered green commits and an inspected PR establish delivery. Without external authorization, external delivery remains unperformed.",
    "expectedReduced": "Unavailable workers permit authorized sequential edits and local equivalence checks with reduced capability disclosed. Independent delegation and parallel design remain unsatisfied. Denied writes allow only a source-grounded target shape and ordered proposal. No external authorization yields a checked local diff and delivery plan rather than a PR. Unknown actual models prove no diversity.",
    "expectedBlocked": "Missing source or required leaves stops dependent work. No executable behavior pin blocks structure moves and unchanged-behavior claims. Denied equivalence execution or matching controls leaves behavior unverified. Missing independent operations block required independence rather than waive it. Missing Opening a PR stops PR-dependent work. Unauthorized writes, rebase, commits or PR creation stay unperformed.",
    "forbiddenClaims": [
      "Compilation, lint or structural validation proves unchanged behavior.",
      "A pin captured after edits proves the pre-change contract.",
      "New behavior or an unrelated bug fix belongs in the structural change.",
      "Sequential roles prove independent delegation, parallel exploration or review.",
      "The historical grok-4.7-xhigh-fast default proves current model availability, selection or diversity.",
      "Requested or inherited models are actual observed models.",
      "Caller migration is complete without checking strings, prose and back-references.",
      "Compatibility shims or dual APIs satisfy the same-wave deletion gate.",
      "Unrun checks are green or reader time was measured without observation.",
      "Missing companion execution or deferred PR routing succeeded.",
      "A draft plan is a created PR, external autonomy authorizes writes, or opening a PR starts Babysit.",
      "Helper fixtures prove this host case passed."
    ],
    "caseFile": "docs/parity/cases/playbooks/refactoring.json"
  },
  "registry": {
    "caseId": "preserved-behavior",
    "caseFile": "docs/parity/cases/playbooks/refactoring.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/refactoring.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/playbooks/feature.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/how/SKILL.md",
      "skills/figure-it-out/SKILL.md",
      "skills/architect/SKILL.md",
      "skills/principle-model-the-domain/SKILL.md",
      "skills/principle-foundational-thinking/SKILL.md",
      "skills/principle-redesign-from-first-principles/SKILL.md",
      "skills/principle-subtract-before-you-add/SKILL.md",
      "skills/principle-laziness-protocol/SKILL.md",
      "skills/principle-migrate-callers-then-delete-legacy-apis/SKILL.md",
      "skills/principle-prove-it-works/SKILL.md",
      "skills/principle-minimize-reader-load/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/architect/references/design-red-flags.md"
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
        "inspect-result",
        "execution",
        "isolated-write"
      ],
      "reduced-pass": [
        "read"
      ]
    },
    "executionModes": {
      "pass": [
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
      "attemptId": "grades-chatgpt-09-12.json#11",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 11,
      "host": "chatgpt",
      "caseId": "preserved-behavior",
      "status": "blocked",
      "grade": {
        "caseId": "preserved-behavior",
        "batch": "batch-10",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Static reshape target and contract correctly read, but no characterization outputs or refactor/equivalence run. Full case requires behavior pin first; Bun absent makes actual target move unverified.",
        "actualResponse": "The inspected formatter contains one-use fixed(value), module state lastFormatted, formatInvoice, formatRows and a separate sortAmounts defect. Desired reshape is formatAmount with a local Number.toFixed(2) return after the existing finite check, migrating formatRows calls, exporter string references, prose and back-references in one wave. The display contract explicitly preserves binary floating-point toFixed behavior, [] and Error('nonfinite'). I did not move structure because the required characterization pin must run first and Bun is absent. No current outputs for 0, 1.005, -1.005, 12.345, [], NaN or Infinity were observed; no equivalence claim. Removing fixed and lastFormatted would reduce one call layer and one module mutation by static inspection, not a measured reader time. Stateful Formatter class is the speculative rejected alternative; it was not implemented, so no fictitious revert. sortAmounts stays outside scope. No refactor, commit, PR or new behavior shipped.",
        "variants": [
          {
            "name": "old literal outputs/rounding/errors pin",
            "state": "blocked",
            "reason": "Bun absent; unrun pin blocks structural movement"
          },
          {
            "name": "remove wrapper/consolidate state",
            "state": "blocked",
            "reason": "Required runtime behavior baseline unobserved"
          },
          {
            "name": "rename callers strings docs back-references",
            "state": "attempted",
            "reason": "Source/exporter/decision references inspected; coordinated migration proposed, not executed"
          },
          {
            "name": "architect two candidates/fresh judge",
            "state": "blocked",
            "reason": "Cannot proceed past required behavior pin; exact task Git revision absent"
          },
          {
            "name": "unrelated bug separation",
            "state": "attempted",
            "reason": "sortAmounts identified separately; untouched"
          },
          {
            "name": "speculative abstraction revert",
            "state": "blocked",
            "reason": "No speculative code was written; rejection is design-only, not a revert"
          },
          {
            "name": "workers unavailable variant",
            "state": "attempted",
            "reason": "Sequential source proposal only, independent delegation unsatisfied"
          },
          {
            "name": "execution denied variant",
            "state": "blocked",
            "reason": "No runtime evidence; unchanged-behavior claim withheld"
          },
          {
            "name": "behavior coverage absent variant",
            "state": "blocked",
            "reason": "Need write/run pin before edits; cannot run under missing Bun"
          },
          {
            "name": "equivalence old/new replay and delivery",
            "state": "blocked",
            "reason": "No baseline, edits, commits, rebase, push or PR authorized/executed"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/preserved-behavior/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/preserved-behavior/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "old literal outputs/rounding/errors pin",
            "reason": "Bun absent; unrun pin blocks structural movement"
          },
          {
            "variant": "remove wrapper/consolidate state",
            "reason": "Required runtime behavior baseline unobserved"
          },
          {
            "variant": "architect two candidates/fresh judge",
            "reason": "Cannot proceed past required behavior pin; exact task Git revision absent"
          },
          {
            "variant": "speculative abstraction revert",
            "reason": "No speculative code was written; rejection is design-only, not a revert"
          },
          {
            "variant": "execution denied variant",
            "reason": "No runtime evidence; unchanged-behavior claim withheld"
          },
          {
            "variant": "behavior coverage absent variant",
            "reason": "Need write/run pin before edits; cannot run under missing Bun"
          },
          {
            "variant": "equivalence old/new replay and delivery",
            "reason": "No baseline, edits, commits, rebase, push or PR authorized/executed"
          }
        ],
        "limits": [
          "Bun unavailable; no Node/Python substitute.",
          "Supplied freeze is not verified installed/task Git HEAD.",
          "No live accounts/services/writes/settings/schedules.",
          "Some initial tool raw metadata omitted from local export and some large outputs truncated, explicitly not reconstructed.",
          "Prior Node/Python deviation retained, not repeated.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Observed authorized independent mechanical delegation returns inspected artifacts at the assigned revision. The before-edit pin and each subsequent step have matching literal output evidence, including errors and rounding. All callers and textual references move together and the old API disappears. Architecture exploration runs when triggered. The actual artifact has equivalence proof and a source-grounded reader-load reduction. Bug work remains separate and speculation is reverted. With explicit delivery authorization and complete dependencies, ordered green commits and an inspected PR establish delivery. Without external authorization, external delivery remains unperformed.",
        "reducedExpected": "Unavailable workers permit authorized sequential edits and local equivalence checks with reduced capability disclosed. Independent delegation and parallel design remain unsatisfied. Denied writes allow only a source-grounded target shape and ordered proposal. No external authorization yields a checked local diff and delivery plan rather than a PR. Unknown actual models prove no diversity.",
        "concreteFixCandidates": [
          "Provide missing concrete fixture/runtime/authorized capability and rerun. Correct fail-closed handling is not a confirmed skill bug."
        ],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
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
        "text": "The inspected formatter contains one-use fixed(value), module state lastFormatted, formatInvoice, formatRows and a separate sortAmounts defect. Desired reshape is formatAmount with a local Number.toFixed(2) return after the existing finite check, migrating formatRows calls, exporter string references, prose and back-references in one wave. The display contract explicitly preserves binary floating-point toFixed behavior, [] and Error('nonfinite'). I did not move structure because the required characterization pin must run first and Bun is absent. No current outputs for 0, 1.005, -1.005, 12.345, [], NaN or Infinity were observed; no equivalence claim. Removing fixed and lastFormatted would reduce one call layer and one module mutation by static inspection, not a measured reader time. Stateful Formatter class is the speculative rejected alternative; it was not implemented, so no fictitious revert. sortAmounts stays outside scope. No refactor, commit, PR or new behavior shipped.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/preserved-behavior/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/preserved-behavior/result.json",
          "sha256": "bb66787cd82ffdb62df521e3330703b37180a2f724ab8d9b363ffd431486bce5",
          "bytes": 3494
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
            "sha256": "573460e5da46c0ef316385566ec2c9a9e86bc65be4ba7bf24d3449eec1bce3f4",
            "bytes": 24603
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/preserved-behavior/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/preserved-behavior/case.json",
            "sha256": "424d368b08e3ed18c6a9f99ab4e4ddd351c261041d20ca36590b47cf51b92d7e",
            "bytes": 3950
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/preserved-behavior/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-10/cases/preserved-behavior/evidence/source-read-status.tsv",
            "sha256": "1ab9822133e0f517d3450cc75cc661c02ed231aa0a4250e87de7a015f0b58f7a",
            "bytes": 974
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-10/results.json",
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
