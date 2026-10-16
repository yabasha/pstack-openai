# Corrected candidate 0.1.3

Operative source freeze: `51f209daf83cd97d64f89881d66533bb59dc57db`. Local CLI discovery passes with 51 roots; fresh web cloud and executor discovery both pass with 51 roots. The three Benny helpers are preserved as reference documents, not skill entrypoints.

The 104 workflow observations per host below belong only to version 0.1.0, source `f4623636a287bea2aa79c4b2234a53d20a5f193c`. All 104 workflow cases on the corrected 0.1.3 freeze remain explicitly not-run; no historical grade transfers. Full release qualification remains blocked.

## Current discovery proof

```json
{
  "host": "codex",
  "sourceFreeze": "51f209daf83cd97d64f89881d66533bb59dc57db",
  "packageVersion": "0.1.3",
  "rootSkillCount": 51,
  "nestedBennyRootCount": 0,
  "sourceFiles": 934,
  "installedFiles": 934,
  "byteAndGitExecutableModeMismatches": 0,
  "observedOperations": [
    "plugin/read",
    "skills/list"
  ],
  "discoverySource": "fresh isolated CLI0.162.1 app-server",
  "scope": "Discovery only; current 104 workflow cases not-run."
}
```

# codex reviewed frozen baseline

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Coverage: **104/104 graded**, **0 pending**. Both-host coverage complete: true. This is reviewed baseline coverage, not full workflow success, later-package acceptance or release readiness.

```json
{
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "host": "codex",
  "counts": {
    "expected": 104,
    "graded": 104,
    "missing": 0,
    "pass": 27,
    "reduced-pass": 57,
    "blocked": 20,
    "fail": 0
  },
  "complete": true,
  "acceptanceRule": "All baseline grades, then rerun01..06, then durable00..05; stable filename order within phase, latest graded row accepted regardless of status. Nested rejected attempts precede their containing accepted row."
}
```

[Capture manifest, common fixtures and machine-readable 208 observations](../releases/remaining-controller-report.md)

All responses, reviews, variants, limits, historical failures and case-owned text artifacts are retained in the linked pages. The latest graded attempt is selected deterministically, even if worse than an earlier grade. Cloud UI corroboration is distinct from exact model-captured logs.

| Case | Accepted result | Latest graded attempt | Attempts |
|---|---|---|---|
| [absent-workers](../releases/host-evaluation/codex/absent-workers.md) | pass | grades-native-durable-00.json#0 | 2 |
| [accessible-trace](../releases/host-evaluation/codex/accessible-trace.md) | reduced-pass | grades-native-06.json#3 | 1 |
| [adversarial-review](../releases/host-evaluation/codex/adversarial-review.md) | reduced-pass | grades-native-durable-01.json#0 | 2 |
| [alternatives](../releases/host-evaluation/codex/alternatives.md) | pass | grades-native-00-01.json#0 | 1 |
| [approval-before-edit](../releases/host-evaluation/codex/approval-before-edit.md) | reduced-pass | grades-native-durable-01.json#1 | 2 |
| [arena-walkthrough](../releases/host-evaluation/codex/arena-walkthrough.md) | pass | grades-native-durable-02.json#0 | 2 |
| [authorized-program](../releases/host-evaluation/codex/authorized-program.md) | blocked | grades-native-06.json#7 | 1 |
| [benny-duplicate-report](../releases/host-evaluation/codex/benny-duplicate-report.md) | reduced-pass | grades-native-00-01.json#1 | 1 |
| [benny-existing-fix-ownership](../releases/host-evaluation/codex/benny-existing-fix-ownership.md) | reduced-pass | grades-native-00-01.json#2 | 1 |
| [benny-existing-pr](../releases/host-evaluation/codex/benny-existing-pr.md) | blocked | grades-native-00-01.json#6 | 1 |
| [benny-missing-adapter](../releases/host-evaluation/codex/benny-missing-adapter.md) | reduced-pass | grades-native-00-01.json#3 | 1 |
| [benny-missing-coordinates](../releases/host-evaluation/codex/benny-missing-coordinates.md) | reduced-pass | grades-native-00-01.json#4 | 1 |
| [benny-source-thread-compensation](../releases/host-evaluation/codex/benny-source-thread-compensation.md) | blocked | grades-native-00-01.json#7 | 1 |
| [benny-unsupported-trigger](../releases/host-evaluation/codex/benny-unsupported-trigger.md) | reduced-pass | grades-native-00-01.json#5 | 1 |
| [benny-untrusted-marker](../releases/host-evaluation/codex/benny-untrusted-marker.md) | reduced-pass | grades-native-00-01.json#8 | 1 |
| [boundary-design](../releases/host-evaluation/codex/boundary-design.md) | pass | grades-native-durable-02.json#1 | 2 |
| [bounded-improvement](../releases/host-evaluation/codex/bounded-improvement.md) | blocked | grades-native-07.json#1 | 1 |
| [bounded-poll](../releases/host-evaluation/codex/bounded-poll.md) | blocked | grades-native-rerun-04.json#0 | 2 |
| [caller-migration](../releases/host-evaluation/codex/caller-migration.md) | pass | grades-native-rerun-01.json#0 | 2 |
| [cancelled-worker](../releases/host-evaluation/codex/cancelled-worker.md) | reduced-pass | grades-native-durable-00.json#2 | 2 |
| [candidate-cross-review](../releases/host-evaluation/codex/candidate-cross-review.md) | pass | grades-native-durable-02.json#2 | 2 |
| [chatgpt-setup-from-readme](../releases/host-evaluation/codex/chatgpt-setup-from-readme.md) | reduced-pass | grades-native-00-01.json#10 | 1 |
| [codex-setup-from-readme](../releases/host-evaluation/codex/codex-setup-from-readme.md) | reduced-pass | grades-native-00-01.json#11 | 1 |
| [comparable-revisions](../releases/host-evaluation/codex/comparable-revisions.md) | blocked | grades-native-07.json#5 | 1 |
| [contiguous-verified-stack](../releases/host-evaluation/codex/contiguous-verified-stack.md) | blocked | grades-native-durable-03.json#2 | 2 |
| [dead-path](../releases/host-evaluation/codex/dead-path.md) | pass | grades-native-rerun-01.json#1 | 2 |
| [decision-trail](../releases/host-evaluation/codex/decision-trail.md) | reduced-pass | grades-native-durable-01.json#2 | 2 |
| [denied-writes](../releases/host-evaluation/codex/denied-writes.md) | reduced-pass | grades-native-00-01.json#13 | 1 |
| [dense-doc](../releases/host-evaluation/codex/dense-doc.md) | pass | grades-native-00-01.json#14 | 1 |
| [dependent-caller](../releases/host-evaluation/codex/dependent-caller.md) | pass | grades-native-08.json#0 | 1 |
| [discriminating-eval](../releases/host-evaluation/codex/discriminating-eval.md) | reduced-pass | grades-native-08.json#1 | 1 |
| [draft-only-authorized](../releases/host-evaluation/codex/draft-only-authorized.md) | reduced-pass | grades-native-08.json#2 | 1 |
| [empty-function](../releases/host-evaluation/codex/empty-function.md) | pass | grades-native-rerun-01.json#2 | 2 |
| [existing-personal-mode](../releases/host-evaluation/codex/existing-personal-mode.md) | blocked | grades-native-08.json#3 | 1 |
| [false-success](../releases/host-evaluation/codex/false-success.md) | reduced-pass | grades-native-08.json#4 | 1 |
| [fresh-worker-mode](../releases/host-evaluation/codex/fresh-worker-mode.md) | reduced-pass | grades-native-08.json#5 | 1 |
| [grounded-explanation](../releases/host-evaluation/codex/grounded-explanation.md) | reduced-pass | grades-native-08.json#6 | 1 |
| [guides-github-absent](../releases/host-evaluation/codex/guides-github-absent.md) | reduced-pass | grades-native-02.json#0 | 1 |
| [guides-local-codex](../releases/host-evaluation/codex/guides-local-codex.md) | reduced-pass | grades-native-02.json#1 | 1 |
| [guides-optional-setup-skipped](../releases/host-evaluation/codex/guides-optional-setup-skipped.md) | reduced-pass | grades-native-02.json#2 | 1 |
| [guides-ordinary-chatgpt](../releases/host-evaluation/codex/guides-ordinary-chatgpt.md) | reduced-pass | grades-native-02.json#3 | 1 |
| [guides-worker-chatgpt](../releases/host-evaluation/codex/guides-worker-chatgpt.md) | reduced-pass | grades-native-08.json#7 | 1 |
| [history-evidence](../releases/host-evaluation/codex/history-evidence.md) | reduced-pass | grades-native-09.json#0 | 1 |
| [inherited-identical-models](../releases/host-evaluation/codex/inherited-identical-models.md) | reduced-pass | grades-native-09.json#1 | 1 |
| [interrupted-action](../releases/host-evaluation/codex/interrupted-action.md) | reduced-pass | grades-native-durable-00.json#3 | 2 |
| [interrupted-external-write](../releases/host-evaluation/codex/interrupted-external-write.md) | reduced-pass | grades-native-02.json#5 | 1 |
| [invalid-input](../releases/host-evaluation/codex/invalid-input.md) | pass | grades-native-rerun-02.json#0 | 2 |
| [invalid-state](../releases/host-evaluation/codex/invalid-state.md) | reduced-pass | grades-native-02.json#7 | 1 |
| [large-corpus](../releases/host-evaluation/codex/large-corpus.md) | reduced-pass | grades-native-09.json#2 | 1 |
| [legal-header](../releases/host-evaluation/codex/legal-header.md) | reduced-pass | grades-native-09.json#3 | 1 |
| [measurement-method](../releases/host-evaluation/codex/measurement-method.md) | blocked | grades-native-09.json#4 | 1 |
| [migration-end-state](../releases/host-evaluation/codex/migration-end-state.md) | pass | grades-native-rerun-02.json#1 | 2 |
| [migration-units](../releases/host-evaluation/codex/migration-units.md) | reduced-pass | grades-native-03.json#1 | 1 |
| [misleading-speedup](../releases/host-evaluation/codex/misleading-speedup.md) | reduced-pass | grades-native-03.json#2 | 1 |
| [missing-model-enumeration](../releases/host-evaluation/codex/missing-model-enumeration.md) | reduced-pass | grades-native-09.json#5 | 1 |
| [missing-webhook](../releases/host-evaluation/codex/missing-webhook.md) | reduced-pass | grades-native-03.json#3 | 1 |
| [new-requirement](../releases/host-evaluation/codex/new-requirement.md) | pass | grades-native-03.json#4 | 1 |
| [no-persistent-tool](../releases/host-evaluation/codex/no-persistent-tool.md) | reduced-pass | grades-native-rerun-05.json#0 | 2 |
| [owned-safe-cleanup](../releases/host-evaluation/codex/owned-safe-cleanup.md) | reduced-pass | grades-native-09.json#7 | 1 |
| [package-support-contracts](../releases/host-evaluation/codex/package-support-contracts.md) | reduced-pass | grades-native-10.json#0 | 1 |
| [partition-and-race](../releases/host-evaluation/codex/partition-and-race.md) | reduced-pass | grades-native-10.json#1 | 1 |
| [plain-restate](../releases/host-evaluation/codex/plain-restate.md) | pass | grades-native-plain-restate.json#0 | 2 |
| [poteto-walkthrough](../releases/host-evaluation/codex/poteto-walkthrough.md) | reduced-pass | grades-native-10.json#2 | 1 |
| [preserved-behavior](../releases/host-evaluation/codex/preserved-behavior.md) | reduced-pass | grades-native-10.json#3 | 1 |
| [prose-rewrite](../releases/host-evaluation/codex/prose-rewrite.md) | pass | grades-native-03.json#5 | 1 |
| [read-only-answer](../releases/host-evaluation/codex/read-only-answer.md) | reduced-pass | grades-native-durable-03.json#0 | 2 |
| [real-app-contract](../releases/host-evaluation/codex/real-app-contract.md) | reduced-pass | grades-native-10.json#4 | 1 |
| [real-render](../releases/host-evaluation/codex/real-render.md) | blocked | grades-native-10.json#5 | 1 |
| [red-green](../releases/host-evaluation/codex/red-green.md) | pass | grades-native-10.json#6 | 1 |
| [repeatable-change](../releases/host-evaluation/codex/repeatable-change.md) | pass | grades-native-rerun-02.json#2 | 2 |
| [repeated-failure](../releases/host-evaluation/codex/repeated-failure.md) | blocked | grades-native-04.json#0 | 1 |
| [repeated-rule](../releases/host-evaluation/codex/repeated-rule.md) | pass | grades-native-04.json#1 | 1 |
| [replay](../releases/host-evaluation/codex/replay.md) | reduced-pass | grades-native-04.json#2 | 1 |
| [reproduce-before-fix](../releases/host-evaluation/codex/reproduce-before-fix.md) | blocked | grades-native-10.json#7 | 1 |
| [resume-revision](../releases/host-evaluation/codex/resume-revision.md) | blocked | grades-native-durable-03.json#1 | 2 |
| [reversible-step](../releases/host-evaluation/codex/reversible-step.md) | pass | grades-native-04.json#4 | 1 |
| [route-recipe](../releases/host-evaluation/codex/route-recipe.md) | reduced-pass | grades-native-04.json#5 | 1 |
| [scoped-history](../releases/host-evaluation/codex/scoped-history.md) | blocked | grades-native-rerun-06.json#0 | 2 |
| [shape-first](../releases/host-evaluation/codex/shape-first.md) | blocked | grades-native-04.json#6 | 1 |
| [shared-path-conflict](../releases/host-evaluation/codex/shared-path-conflict.md) | pass | grades-native-durable-00.json#1 | 2 |
| [smaller-solution](../releases/host-evaluation/codex/smaller-solution.md) | blocked | grades-native-05.json#0 | 1 |
| [stack-resume](../releases/host-evaluation/codex/stack-resume.md) | reduced-pass | grades-native-11.json#1 | 1 |
| [stale-feature-map](../releases/host-evaluation/codex/stale-feature-map.md) | blocked | grades-native-11.json#2 | 1 |
| [state-shape](../releases/host-evaluation/codex/state-shape.md) | pass | grades-native-00-01.json#16 | 1 |
| [supported-authoring](../releases/host-evaluation/codex/supported-authoring.md) | reduced-pass | grades-native-11.json#3 | 1 |
| [swarm-walkthrough](../releases/host-evaluation/codex/swarm-walkthrough.md) | reduced-pass | grades-native-11.json#4 | 1 |
| [symptom-repro](../releases/host-evaluation/codex/symptom-repro.md) | blocked | grades-native-05.json#1 | 1 |
| [throwaway-probe](../releases/host-evaluation/codex/throwaway-probe.md) | reduced-pass | grades-native-11.json#5 | 1 |
| [trace-load](../releases/host-evaluation/codex/trace-load.md) | pass | grades-native-rerun-03.json#0 | 2 |
| [trace-path](../releases/host-evaluation/codex/trace-path.md) | pass | grades-native-11.json#6 | 1 |
| [trace-provenance](../releases/host-evaluation/codex/trace-provenance.md) | blocked | grades-native-11.json#7 | 1 |
| [two-writers](../releases/host-evaluation/codex/two-writers.md) | pass | grades-native-05.json#3 | 1 |
| [typed-boundary](../releases/host-evaluation/codex/typed-boundary.md) | reduced-pass | grades-native-05.json#4 | 1 |
| [unavailable-persistence](../releases/host-evaluation/codex/unavailable-persistence.md) | reduced-pass | grades-native-05.json#5 | 1 |
| [uncertain-result](../releases/host-evaluation/codex/uncertain-result.md) | reduced-pass | grades-native-durable-05.json#0 | 2 |
| [unit-state](../releases/host-evaluation/codex/unit-state.md) | blocked | grades-native-12.json#0 | 1 |
| [units-and-proof](../releases/host-evaluation/codex/units-and-proof.md) | reduced-pass | grades-native-12.json#1 | 1 |
| [unknown-actual-model](../releases/host-evaluation/codex/unknown-actual-model.md) | pass | grades-native-12.json#2 | 1 |
| [unknown-model](../releases/host-evaluation/codex/unknown-model.md) | reduced-pass | grades-native-05.json#7 | 1 |
| [unsupported-selected-model](../releases/host-evaluation/codex/unsupported-selected-model.md) | pass | grades-native-12.json#3 | 1 |
| [user-correction](../releases/host-evaluation/codex/user-correction.md) | reduced-pass | grades-native-06.json#0 | 1 |
| [user-tradeoff](../releases/host-evaluation/codex/user-tradeoff.md) | pass | grades-native-06.json#1 | 1 |
| [verifiable-feature](../releases/host-evaluation/codex/verifiable-feature.md) | reduced-pass | grades-native-12.json#4 | 1 |
| [dependency-readiness](../releases/host-evaluation/codex/dependency-readiness.md) | reduced-pass | grades-native-12.json#5 | 1 |
