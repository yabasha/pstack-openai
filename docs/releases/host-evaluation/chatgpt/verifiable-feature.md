# chatgpt: verifiable-feature

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **blocked**. All 1 retained graded attempts appear below.

[Host overview](../../../testing/chatgpt.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "chatgpt",
  "caseId": "verifiable-feature",
  "acceptedStatus": "blocked",
  "acceptedAttemptId": "grades-chatgpt-09-12.json#29",
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..06 -> durable00..05 order, never best status",
  "casePrompt": "Implement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.",
  "caseDefinition": {
    "id": "verifiable-feature",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/feature.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/arena/SKILL.md",
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md",
      "skills/principle-model-the-domain/SKILL.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md"
    ],
    "prompt": "Implement a CSV export for the currently filtered orders in a fixture dashboard. Exclude hidden orders, preserve displayed column order, escape commas and quotes, and show a useful empty-result message. Keep the design lead separate from the code owner. Compare two valid export designs through arena when the implementation shape is contested. Use an isolated local repository and fixture data. The first run permits local changes and independent workers but no push or PR creation. Repeat with worker operations unavailable and then with matching browser verification denied. Return the throughput checkpoint, ordered implementation units, evidence for the user outcome and open decisions.",
    "requirements": [
      "Read the complete mode and Feature playbook, required principle leaves and routed workflows. Record the eight playbook steps in a todo binding before task-specific items. Trace how the dashboard filters and renders orders before designing the export.",
      "Use architect for design exploration. Retain two structurally distinct alternatives and its synthesis artifacts. Choose the named export data shape and organizing structure before code-writing. Use the complete arena contract for multiple valid implementation shapes, including isolated candidate paths, inspected candidates and a fresh cross-judge.",
      "Keep all four checkpoint items, including n/a with a reason. Blocking gates precede fan-out. Split independent write targets before serializing real shared invariants. Rewrite the checkpoint at phase boundaries and keep it inline with the single code-coupled owner.",
      "Assign the exact input SHA, owned paths, full poteto-agent prompt, role and success criteria. Use inherited model roles unless supported explicit choices are observed. Inspect returned artifacts and review the diff as the lead. A no-spawn worker owns the diff directly and returns to its parent, never waits for a nested agent. Required delegation and review separation have no laziness or skip escape.",
      "Make surgical edits, re-ground upstream-derived files, propagate shared changes to every consumer and verify each. Preserve Comments rules and disclose missing deslop, no-comments or matching-control companions. Missing companion execution cannot become satisfied by assertion.",
      "Deliver small units with a check before the next. Verify the exported literal rows, column order and escaping through fixture execution, and the empty-state feedback through the matching browser surface. Compilation alone and wrong-surface checks cannot establish the requested user outcome.",
      "Run interrogate before shipping a contested design. Record worker independence and actual model limits. Prepare checked local changes and delivery order when commits, rebase, push or PR creation are unauthorized. Run complete Opening a PR when available and authorized, and retain exact missing dependency otherwise. Opening a PR never triggers Babysit implicitly.",
      "Return what was built, choices and reasons, a table of design alternatives, all four checkpoint items and open decisions. Evidence names the end-user behavior and next-maintainer implications, missing capabilities and forbidden completion claims."
    ],
    "expectedFull": "Observed independent design and code-owner operations return inspected artifacts at the assigned revision. The lead reviews the diff and preserves review separation. The checkpoint explains the blocking phase, independent targets, shared invariant and smallest safe decomposition. Ordered units carry actual matching browser and CSV execution evidence for filtering, displayed column order, escaping and empty feedback. The contested shape has arena synthesis and interrogate evidence with observed model limits. In a run with actual commit and external authorization and all companions available, delivery records show verified ordered commits and an inspected ready PR. The reply contains the built result, chosen design and reasons, alternatives table, checkpoint and open decisions. An unauthorized external gate remains explicitly unperformed even when local implementation succeeds.",
    "expectedReduced": "With worker operations unavailable, authorized sequential grounding, design alternatives and direct implementation produce a useful local diff and outcome evidence. The report calls this reduced capability and retains mandatory independent delegation, arena cross-judge and review separation as unsatisfied gates. Inherited selections and unknown models supply no diversity claim. With no external authorization, return the local checked result and ordered delivery plan without push or PR creation. Missing companions retain their specific limits. A fixture CLI check may verify CSV bytes but cannot satisfy denied browser verification.",
    "expectedBlocked": "Denied source or required missing skill stops dependent grounding or design. Missing independent operations block required review separation rather than waive it. Denied matching browser verification leaves the empty-state gate unverified, even if CSV fixtures pass. Missing opening-a-pr.md blocks PR-dependent work. Denied or unauthorized writes, commit, rebase or PR creation stay unperformed. The result reports the exact gate, available partial artifacts and open decisions without claiming complete delivery.",
    "forbiddenClaims": [
      "All four checkpoint dimensions apply, or omitted dimensions need no n/a explanation.",
      "Sequential roles are independent workers, a fresh cross-judge, parallel exploration or independent review separation.",
      "A no-spawn worker must wait on another worker, or Laziness Protocol permits skipping code-owner separation.",
      "The source grok-4.7-xhigh-fast default proves a supported or selected host model.",
      "A requested or inherited model proves the actual model or model diversity.",
      "A compile, structural validator, inconclusive check or CSV-only test proves browser behavior or the complete feature outcome.",
      "Unrun checks are green, all shared consumers were verified without observations, or ordered commits and rebases happened without authorization and evidence.",
      "A missing companion or deferred Opening a PR playbook ran successfully.",
      "A local PR draft is an actual PR, upstream autonomy authorizes external writes, or opening a PR starts Babysit.",
      "Canonical prompts are registered custom agents, source metadata guarantees background execution, or isolated helper tests prove this host case passed."
    ],
    "caseFile": "docs/parity/cases/playbooks/feature.json"
  },
  "registry": {
    "caseId": "verifiable-feature",
    "caseFile": "docs/parity/cases/playbooks/feature.json",
    "sourcePaths": [
      "skills/poteto-mode/playbooks/feature.md",
      "skills/poteto-mode/SKILL.md",
      "agents/poteto-agent.md",
      "skills/poteto-mode/playbooks/opening-a-pr.md",
      "skills/how/SKILL.md",
      "skills/how/references/explorer-prompt.md",
      "skills/how/references/explainer-prompt.md",
      "skills/architect/SKILL.md",
      "skills/architect/references/runner-prompt.md",
      "skills/architect/references/rationale-template.md",
      "skills/arena/SKILL.md",
      "skills/interrogate/SKILL.md",
      "skills/interrogate/references/reviewer-prompt.md",
      "skills/interrogate/references/rubric.md",
      "skills/principle-model-the-domain/SKILL.md",
      "skills/principle-separate-before-serializing-shared-state/SKILL.md",
      "skills/principle-sequence-verifiable-units/SKILL.md"
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
      "attemptId": "grades-chatgpt-09-12.json#29",
      "order": 0,
      "gradeFile": "grades-chatgpt-09-12.json",
      "rankWithinFile": 29,
      "host": "chatgpt",
      "caseId": "verifiable-feature",
      "status": "blocked",
      "grade": {
        "caseId": "verifiable-feature",
        "batch": "batch-12",
        "host": "chatgpt",
        "status": "blocked",
        "execution": "direct",
        "requiredObservationsMet": [
          "read",
          "review-outcome"
        ],
        "actualReadEventIds": [],
        "nativeReadCorroboration": "Parent independently observed aggregate native UI worker/read/command activity. Exact per-call arguments/results exported in archive are model captures, not independently verified native event IDs.",
        "review": "Real source trace and two design alternatives/checkpoint useful, but no architecture workers/CSV output/browser proof/local checked diff. Full requested feature and reduced local-implementation outcome unperformed under missing Bun/driver.",
        "actualResponse": "The inspected dashboard visible(orders,status) filters by status. exportCsv serializes whichever rows callers supply and directly interpolates customer text, so source inspection identifies quoting and selection responsibilities. A provisional export shape is orderedColumns plus visibleRows captured from the displayed view. Alternative A passes that snapshot to a pure serializer. Alternative B re-queries a centralized export projection by filter key. A keeps rendered/exported membership aligned; B adds a second consistency boundary and needs snapshot/version semantics. These are untested source proposals, not independent architect/Arena candidates or a chosen implemented design. Throughput checkpoint: blocking steps are exact task revision, architecture review and Bun/real app verification; independent workstreams are serializer and UI evidence only after shared contract; shared mutable state stays with one code owner and read-only order fixture; smallest safe decomposition is serializer proof before UI wiring. Ordered units are trace, architecture, literal-row regression tests, escaping, filter integration, empty-state browser check, independent contested-design review, local delivery. Bun is absent and no runnable fixture browser app/driver exists, so no code, CSV execution or empty-state interaction was verified. No push, commit or PR. Next maintainer must verify hidden-row exclusion, displayed columns and literal bytes through the actual exported file.",
        "variants": [
          {
            "name": "complete Feature steps/how source trace",
            "state": "attempted",
            "reason": "Mode/Feature/how contracts and actual dashboard/orders source inspected"
          },
          {
            "name": "architect distinct alternatives and rationale",
            "state": "attempted",
            "reason": "Two explicitly untested source proposals, no full independent exploration claim"
          },
          {
            "name": "Arena candidates/fresh judge/synthesis",
            "state": "blocked",
            "reason": "Exact task Git SHA absent; runtime verification gates unavailable; no candidate worker results for this case"
          },
          {
            "name": "design lead vs single code owner",
            "state": "attempted",
            "reason": "Ownership rule retained; no code worker assignment falsely recorded"
          },
          {
            "name": "ordered small implementation units",
            "state": "attempted",
            "reason": "Explicit source-grounded delivery sequence, not executed implementation"
          },
          {
            "name": "literal CSV rows/column order/comma quote escape",
            "state": "blocked",
            "reason": "Bun absent; no fixture execution"
          },
          {
            "name": "empty-result useful feedback matching browser",
            "state": "blocked",
            "reason": "No runnable dashboard/render/driver; no wrong-surface proxy"
          },
          {
            "name": "interrogate contested design",
            "state": "blocked",
            "reason": "No implemented/synthesized exact-revision design to ship/review"
          },
          {
            "name": "deslop no-comments matching controls companions",
            "state": "blocked",
            "reason": "No own diff/review run; missing deslop/control gates not asserted satisfied"
          },
          {
            "name": "worker unavailable variant",
            "state": "attempted",
            "reason": "Sequential proposals only; required review separation remains blocked"
          },
          {
            "name": "browser verification denied variant",
            "state": "blocked",
            "reason": "Actual empty-state proof unavailable and cannot be replaced with unit/type checks"
          },
          {
            "name": "Opening a PR/commits/rebase/push",
            "state": "blocked",
            "reason": "External writes and commits unauthorized, checks unrun"
          }
        ],
        "evidence": [
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/verifiable-feature/case.json",
          "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/verifiable-feature/evidence/source-read-status.tsv"
        ],
        "missing": [
          {
            "variant": "Arena candidates/fresh judge/synthesis",
            "reason": "Exact task Git SHA absent; runtime verification gates unavailable; no candidate worker results for this case"
          },
          {
            "variant": "literal CSV rows/column order/comma quote escape",
            "reason": "Bun absent; no fixture execution"
          },
          {
            "variant": "empty-result useful feedback matching browser",
            "reason": "No runnable dashboard/render/driver; no wrong-surface proxy"
          },
          {
            "variant": "interrogate contested design",
            "reason": "No implemented/synthesized exact-revision design to ship/review"
          },
          {
            "variant": "deslop no-comments matching controls companions",
            "reason": "No own diff/review run; missing deslop/control gates not asserted satisfied"
          },
          {
            "variant": "browser verification denied variant",
            "reason": "Actual empty-state proof unavailable and cannot be replaced with unit/type checks"
          },
          {
            "variant": "Opening a PR/commits/rebase/push",
            "reason": "External writes and commits unauthorized, checks unrun"
          }
        ],
        "limits": [
          "No Bun runtime available; no Node/Python substitute.",
          "All original named source read failures retained. Documented role alternatives explicitly separate.",
          "Task Git SHA unavailable and package freeze not independently verified host revision.",
          "No live external accounts/messages/trackers/PRs/schedules/credentials/settings.",
          "Initial raw host receipt export incomplete, some large outputs truncated; full source bytes retained but not claimed complete raw metadata.",
          "Earlier batch-00 Node/Python deviation preserved.",
          "Native UI corroboration is aggregate. Exact captured stdout/exit statuses remain reported unless separately corroborated.",
          "No Bun scripts executed here; Node/Python deviation from earlier run retained and not repeated.",
          "Source fallback from missing agents/* to documented references/agent-prompts can legitimately establish source access; does not establish host registration."
        ],
        "fullExpected": "Observed independent design and code-owner operations return inspected artifacts at the assigned revision. The lead reviews the diff and preserves review separation. The checkpoint explains the blocking phase, independent targets, shared invariant and smallest safe decomposition. Ordered units carry actual matching browser and CSV execution evidence for filtering, displayed column order, escaping and empty feedback. The contested shape has arena synthesis and interrogate evidence with observed model limits. In a run with actual commit and external authorization and all companions available, delivery records show verified ordered commits and an inspected ready PR. The reply contains the built result, chosen design and reasons, alternatives table, checkpoint and open decisions. An unauthorized external gate remains explicitly unperformed even when local implementation succeeds.",
        "reducedExpected": "With worker operations unavailable, authorized sequential grounding, design alternatives and direct implementation produce a useful local diff and outcome evidence. The report calls this reduced capability and retains mandatory independent delegation, arena cross-judge and review separation as unsatisfied gates. Inherited selections and unknown models supply no diversity claim. With no external authorization, return the local checked result and ordered delivery plan without push or PR creation. Missing companions retain their specific limits. A fixture CLI check may verify CSV bytes but cannot satisfy denied browser verification.",
        "concreteFixCandidates": [
          "Provide missing concrete fixture/runtime/authorized capability and rerun. Correct fail-closed handling is not a confirmed skill bug."
        ],
        "nativeObservations": [
          {
            "observation": "response",
            "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
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
        "text": "The inspected dashboard visible(orders,status) filters by status. exportCsv serializes whichever rows callers supply and directly interpolates customer text, so source inspection identifies quoting and selection responsibilities. A provisional export shape is orderedColumns plus visibleRows captured from the displayed view. Alternative A passes that snapshot to a pure serializer. Alternative B re-queries a centralized export projection by filter key. A keeps rendered/exported membership aligned; B adds a second consistency boundary and needs snapshot/version semantics. These are untested source proposals, not independent architect/Arena candidates or a chosen implemented design. Throughput checkpoint: blocking steps are exact task revision, architecture review and Bun/real app verification; independent workstreams are serializer and UI evidence only after shared contract; shared mutable state stays with one code owner and read-only order fixture; smallest safe decomposition is serializer proof before UI wiring. Ordered units are trace, architecture, literal-row regression tests, escaping, filter integration, empty-state browser check, independent contested-design review, local delivery. Bun is absent and no runnable fixture browser app/driver exists, so no code, CSV execution or empty-state interaction was verified. No push, commit or PR. Next maintainer must verify hidden-row exclusion, displayed columns and literal bytes through the actual exported file.",
        "artifact": {
          "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/verifiable-feature/result.json",
          "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/verifiable-feature/result.json",
          "sha256": "d3d94be561d1f0efb05e155c912e4a5e806315b1ec2ac1964427ca94015d93b5",
          "bytes": 4684
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
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
            "sha256": "7055437f341d58caac31e043099641b2579ad0ed167b3da14a08a06a46c5e68d",
            "bytes": 25602
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/verifiable-feature/case.json",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/verifiable-feature/case.json",
            "sha256": "f7b76c76909a3ed24eaf4412315f282f2e202166abf58557f79fa5c465704f2e",
            "bytes": 4075
          },
          {
            "path": "chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/verifiable-feature/evidence/source-read-status.tsv",
            "originalExternalPath": "/Users/digital-hawk/Herd/pstack-workflow-evaluation-20261016/chatgpt/remaining/remaining-evaluation/batches/batch-12/cases/verifiable-feature/evidence/source-read-status.tsv",
            "sha256": "1f04a5491d858bbc6d79fcf8768a7c694a4ca9ac3a8bc380cce1d18287c7b73b",
            "bytes": 695
          }
        ],
        "eventReferencesAsGraded": {
          "actualReadEventIds": [],
          "actualExecutionEventIds": [],
          "reportedReadLocators": [],
          "nativeObservations": [
            {
              "observation": "response",
              "evidence": "chatgpt/remaining/remaining-evaluation/batches/batch-12/results.json",
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
