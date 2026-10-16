# codex: verifiable-feature

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Accepted latest reviewed result: **pending**. No independent grade is available; this page is an explicitly pending allocation.

[Host overview](../../../testing/codex.md) · [Capture manifest and shared fixtures](../../remaining-controller-report.md#capture-manifest)

The fenced JSON contains the actual prompt, retained response, full independent grader record, all attempts and case-owned text implementation/test/log bytes. Artifact contents establish inspectable bytes; runtime proof remains limited by the original traces and reviews. Shared unchanged inputs and reconstructible source copies are referenced in the skip manifest.

```json
{
  "schemaVersion": 1,
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "reportScope": "Reviewed original f462 baseline only; does not accept a later package/version",
  "host": "codex",
  "caseId": "verifiable-feature",
  "acceptedStatus": "pending",
  "acceptedAttemptId": null,
  "acceptanceRule": "Latest graded attempt in deterministic baseline -> rerun01..04 -> durable00..05 order, never best status",
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
  "attempts": [],
  "artifactProjections": [],
  "skippedManifest": [],
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
