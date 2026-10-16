# Corrected candidate 0.1.3

Operative source freeze: `51f209daf83cd97d64f89881d66533bb59dc57db`. Local CLI discovery passes with 51 roots; fresh web cloud and executor discovery both pass with 51 roots. The three Benny helpers are preserved as reference documents, not skill entrypoints.

The 104 workflow observations per host below belong only to version 0.1.0, source `f4623636a287bea2aa79c4b2234a53d20a5f193c`. All 104 workflow cases on the corrected 0.1.3 freeze remain explicitly not-run; no historical grade transfers. Full release qualification remains blocked.

## Current discovery proof

```json
{
  "host": "chatgpt",
  "sourceFreeze": "51f209daf83cd97d64f89881d66533bb59dc57db",
  "packageVersion": "0.1.3",
  "pluginId": "plugins_6ad1c78a493c819197a589eb7a55361b",
  "releaseId": "pluginrel_6ad1e8be61108191858d3101cc25dc46",
  "cloudCatalogRoots": 51,
  "executorRoots": 51,
  "nestedBennyRoots": 0,
  "sourceFiles": 934,
  "cloudFiles": 935,
  "preservedSourceFiles": 933,
  "byteAndGitExecutableModeMismatches": 0,
  "manifestExceptions": [
    "normalized root publisher/interface metadata",
    "added compatibility manifest"
  ],
  "removedObsoleteNestedEntrypoints": 3,
  "scope": "Web discovery only; desktop access remains unavailable; current 104 workflow cases not-run."
}
```

# chatgpt reviewed frozen baseline

Frozen source: f4623636a287bea2aa79c4b2234a53d20a5f193c. Coverage: **104/104 graded**, **0 pending**. Both-host coverage complete: true. This is reviewed baseline coverage, not full workflow success, later-package acceptance or release readiness.

```json
{
  "sourceFreeze": "f4623636a287bea2aa79c4b2234a53d20a5f193c",
  "host": "chatgpt",
  "counts": {
    "expected": 104,
    "graded": 104,
    "missing": 0,
    "pass": 6,
    "reduced-pass": 63,
    "blocked": 35,
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
| [absent-workers](../releases/host-evaluation/chatgpt/absent-workers.md) | reduced-pass | grades-chatgpt-05-08.json#8 | 1 |
| [accessible-trace](../releases/host-evaluation/chatgpt/accessible-trace.md) | blocked | grades-chatgpt-05-08.json#9 | 1 |
| [adversarial-review](../releases/host-evaluation/chatgpt/adversarial-review.md) | reduced-pass | grades-chatgpt-05-08.json#10 | 1 |
| [alternatives](../releases/host-evaluation/chatgpt/alternatives.md) | pass | grades-chatgpt-00.json#0 | 1 |
| [approval-before-edit](../releases/host-evaluation/chatgpt/approval-before-edit.md) | reduced-pass | grades-chatgpt-05-08.json#11 | 1 |
| [arena-walkthrough](../releases/host-evaluation/chatgpt/arena-walkthrough.md) | reduced-pass | grades-chatgpt-05-08.json#12 | 1 |
| [authorized-program](../releases/host-evaluation/chatgpt/authorized-program.md) | blocked | grades-chatgpt-05-08.json#13 | 1 |
| [benny-duplicate-report](../releases/host-evaluation/chatgpt/benny-duplicate-report.md) | reduced-pass | grades-chatgpt-00.json#1 | 1 |
| [benny-existing-fix-ownership](../releases/host-evaluation/chatgpt/benny-existing-fix-ownership.md) | reduced-pass | grades-chatgpt-00.json#2 | 1 |
| [benny-existing-pr](../releases/host-evaluation/chatgpt/benny-existing-pr.md) | blocked | grades-chatgpt-00.json#3 | 1 |
| [benny-missing-adapter](../releases/host-evaluation/chatgpt/benny-missing-adapter.md) | reduced-pass | grades-chatgpt-00.json#4 | 1 |
| [benny-missing-coordinates](../releases/host-evaluation/chatgpt/benny-missing-coordinates.md) | reduced-pass | grades-chatgpt-00.json#5 | 1 |
| [benny-source-thread-compensation](../releases/host-evaluation/chatgpt/benny-source-thread-compensation.md) | blocked | grades-chatgpt-00.json#6 | 1 |
| [benny-unsupported-trigger](../releases/host-evaluation/chatgpt/benny-unsupported-trigger.md) | reduced-pass | grades-chatgpt-00.json#7 | 1 |
| [benny-untrusted-marker](../releases/host-evaluation/chatgpt/benny-untrusted-marker.md) | reduced-pass | grades-chatgpt-01-04.json#0 | 1 |
| [boundary-design](../releases/host-evaluation/chatgpt/boundary-design.md) | reduced-pass | grades-chatgpt-05-08.json#16 | 1 |
| [bounded-improvement](../releases/host-evaluation/chatgpt/bounded-improvement.md) | blocked | grades-chatgpt-05-08.json#17 | 1 |
| [bounded-poll](../releases/host-evaluation/chatgpt/bounded-poll.md) | reduced-pass | grades-chatgpt-05-08.json#18 | 1 |
| [caller-migration](../releases/host-evaluation/chatgpt/caller-migration.md) | reduced-pass | grades-chatgpt-01-04.json#1 | 1 |
| [cancelled-worker](../releases/host-evaluation/chatgpt/cancelled-worker.md) | reduced-pass | grades-chatgpt-05-08.json#19 | 1 |
| [candidate-cross-review](../releases/host-evaluation/chatgpt/candidate-cross-review.md) | reduced-pass | grades-chatgpt-05-08.json#20 | 1 |
| [chatgpt-setup-from-readme](../releases/host-evaluation/chatgpt/chatgpt-setup-from-readme.md) | reduced-pass | grades-chatgpt-01-04.json#2 | 1 |
| [codex-setup-from-readme](../releases/host-evaluation/chatgpt/codex-setup-from-readme.md) | reduced-pass | grades-chatgpt-01-04.json#3 | 1 |
| [comparable-revisions](../releases/host-evaluation/chatgpt/comparable-revisions.md) | blocked | grades-chatgpt-05-08.json#21 | 1 |
| [contiguous-verified-stack](../releases/host-evaluation/chatgpt/contiguous-verified-stack.md) | reduced-pass | grades-chatgpt-05-08.json#22 | 1 |
| [dead-path](../releases/host-evaluation/chatgpt/dead-path.md) | reduced-pass | grades-chatgpt-rerun-01.json#0 | 2 |
| [decision-trail](../releases/host-evaluation/chatgpt/decision-trail.md) | reduced-pass | grades-chatgpt-05-08.json#23 | 1 |
| [denied-writes](../releases/host-evaluation/chatgpt/denied-writes.md) | reduced-pass | grades-chatgpt-01-04.json#5 | 1 |
| [dense-doc](../releases/host-evaluation/chatgpt/dense-doc.md) | pass | grades-chatgpt-01-04.json#6 | 1 |
| [dependent-caller](../releases/host-evaluation/chatgpt/dependent-caller.md) | reduced-pass | grades-chatgpt-05-08.json#24 | 1 |
| [discriminating-eval](../releases/host-evaluation/chatgpt/discriminating-eval.md) | blocked | grades-chatgpt-05-08.json#25 | 1 |
| [draft-only-authorized](../releases/host-evaluation/chatgpt/draft-only-authorized.md) | reduced-pass | grades-chatgpt-05-08.json#26 | 1 |
| [empty-function](../releases/host-evaluation/chatgpt/empty-function.md) | reduced-pass | grades-chatgpt-01-04.json#7 | 1 |
| [existing-personal-mode](../releases/host-evaluation/chatgpt/existing-personal-mode.md) | blocked | grades-chatgpt-05-08.json#27 | 1 |
| [false-success](../releases/host-evaluation/chatgpt/false-success.md) | blocked | grades-chatgpt-05-08.json#28 | 1 |
| [fresh-worker-mode](../releases/host-evaluation/chatgpt/fresh-worker-mode.md) | reduced-pass | grades-chatgpt-05-08.json#29 | 1 |
| [grounded-explanation](../releases/host-evaluation/chatgpt/grounded-explanation.md) | reduced-pass | grades-chatgpt-05-08.json#30 | 1 |
| [guides-github-absent](../releases/host-evaluation/chatgpt/guides-github-absent.md) | reduced-pass | grades-chatgpt-01-04.json#8 | 1 |
| [guides-local-codex](../releases/host-evaluation/chatgpt/guides-local-codex.md) | blocked | grades-chatgpt-01-04.json#9 | 1 |
| [guides-optional-setup-skipped](../releases/host-evaluation/chatgpt/guides-optional-setup-skipped.md) | reduced-pass | grades-chatgpt-01-04.json#10 | 1 |
| [guides-ordinary-chatgpt](../releases/host-evaluation/chatgpt/guides-ordinary-chatgpt.md) | reduced-pass | grades-chatgpt-01-04.json#11 | 1 |
| [guides-worker-chatgpt](../releases/host-evaluation/chatgpt/guides-worker-chatgpt.md) | reduced-pass | grades-chatgpt-05-08.json#31 | 1 |
| [history-evidence](../releases/host-evaluation/chatgpt/history-evidence.md) | reduced-pass | grades-chatgpt-09-12.json#0 | 1 |
| [inherited-identical-models](../releases/host-evaluation/chatgpt/inherited-identical-models.md) | reduced-pass | grades-chatgpt-09-12.json#1 | 1 |
| [interrupted-action](../releases/host-evaluation/chatgpt/interrupted-action.md) | reduced-pass | grades-chatgpt-01-04.json#12 | 1 |
| [interrupted-external-write](../releases/host-evaluation/chatgpt/interrupted-external-write.md) | reduced-pass | grades-chatgpt-01-04.json#13 | 1 |
| [invalid-input](../releases/host-evaluation/chatgpt/invalid-input.md) | blocked | grades-chatgpt-01-04.json#14 | 1 |
| [invalid-state](../releases/host-evaluation/chatgpt/invalid-state.md) | reduced-pass | grades-chatgpt-01-04.json#15 | 1 |
| [large-corpus](../releases/host-evaluation/chatgpt/large-corpus.md) | reduced-pass | grades-chatgpt-09-12.json#2 | 1 |
| [legal-header](../releases/host-evaluation/chatgpt/legal-header.md) | reduced-pass | grades-chatgpt-09-12.json#3 | 1 |
| [measurement-method](../releases/host-evaluation/chatgpt/measurement-method.md) | reduced-pass | grades-chatgpt-09-12.json#4 | 1 |
| [migration-end-state](../releases/host-evaluation/chatgpt/migration-end-state.md) | blocked | grades-chatgpt-01-04.json#16 | 1 |
| [migration-units](../releases/host-evaluation/chatgpt/migration-units.md) | reduced-pass | grades-chatgpt-01-04.json#17 | 1 |
| [misleading-speedup](../releases/host-evaluation/chatgpt/misleading-speedup.md) | reduced-pass | grades-chatgpt-01-04.json#18 | 1 |
| [missing-model-enumeration](../releases/host-evaluation/chatgpt/missing-model-enumeration.md) | reduced-pass | grades-chatgpt-09-12.json#5 | 1 |
| [missing-webhook](../releases/host-evaluation/chatgpt/missing-webhook.md) | blocked | grades-chatgpt-01-04.json#19 | 1 |
| [new-requirement](../releases/host-evaluation/chatgpt/new-requirement.md) | blocked | grades-chatgpt-01-04.json#20 | 1 |
| [no-persistent-tool](../releases/host-evaluation/chatgpt/no-persistent-tool.md) | blocked | grades-chatgpt-09-12.json#6 | 1 |
| [owned-safe-cleanup](../releases/host-evaluation/chatgpt/owned-safe-cleanup.md) | blocked | grades-chatgpt-09-12.json#7 | 1 |
| [package-support-contracts](../releases/host-evaluation/chatgpt/package-support-contracts.md) | reduced-pass | grades-chatgpt-09-12.json#8 | 1 |
| [partition-and-race](../releases/host-evaluation/chatgpt/partition-and-race.md) | blocked | grades-chatgpt-09-12.json#9 | 1 |
| [plain-restate](../releases/host-evaluation/chatgpt/plain-restate.md) | pass | grades-chatgpt-plain-restate.json#0 | 1 |
| [poteto-walkthrough](../releases/host-evaluation/chatgpt/poteto-walkthrough.md) | reduced-pass | grades-chatgpt-09-12.json#10 | 1 |
| [preserved-behavior](../releases/host-evaluation/chatgpt/preserved-behavior.md) | blocked | grades-chatgpt-09-12.json#11 | 1 |
| [prose-rewrite](../releases/host-evaluation/chatgpt/prose-rewrite.md) | pass | grades-chatgpt-01-04.json#21 | 1 |
| [read-only-answer](../releases/host-evaluation/chatgpt/read-only-answer.md) | reduced-pass | grades-chatgpt-01-04.json#22 | 1 |
| [real-app-contract](../releases/host-evaluation/chatgpt/real-app-contract.md) | blocked | grades-chatgpt-09-12.json#12 | 1 |
| [real-render](../releases/host-evaluation/chatgpt/real-render.md) | blocked | grades-chatgpt-09-12.json#13 | 1 |
| [red-green](../releases/host-evaluation/chatgpt/red-green.md) | blocked | grades-chatgpt-09-12.json#14 | 1 |
| [repeatable-change](../releases/host-evaluation/chatgpt/repeatable-change.md) | reduced-pass | grades-chatgpt-01-04.json#23 | 1 |
| [repeated-failure](../releases/host-evaluation/chatgpt/repeated-failure.md) | blocked | grades-chatgpt-01-04.json#24 | 1 |
| [repeated-rule](../releases/host-evaluation/chatgpt/repeated-rule.md) | reduced-pass | grades-chatgpt-01-04.json#25 | 1 |
| [replay](../releases/host-evaluation/chatgpt/replay.md) | reduced-pass | grades-chatgpt-01-04.json#26 | 1 |
| [reproduce-before-fix](../releases/host-evaluation/chatgpt/reproduce-before-fix.md) | blocked | grades-chatgpt-09-12.json#15 | 1 |
| [resume-revision](../releases/host-evaluation/chatgpt/resume-revision.md) | blocked | grades-chatgpt-01-04.json#27 | 1 |
| [reversible-step](../releases/host-evaluation/chatgpt/reversible-step.md) | blocked | grades-chatgpt-01-04.json#28 | 1 |
| [route-recipe](../releases/host-evaluation/chatgpt/route-recipe.md) | pass | grades-chatgpt-01-04.json#29 | 1 |
| [scoped-history](../releases/host-evaluation/chatgpt/scoped-history.md) | reduced-pass | grades-chatgpt-09-12.json#16 | 1 |
| [shape-first](../releases/host-evaluation/chatgpt/shape-first.md) | reduced-pass | grades-chatgpt-01-04.json#30 | 1 |
| [shared-path-conflict](../releases/host-evaluation/chatgpt/shared-path-conflict.md) | reduced-pass | grades-chatgpt-01-04.json#31 | 1 |
| [smaller-solution](../releases/host-evaluation/chatgpt/smaller-solution.md) | blocked | grades-chatgpt-05-08.json#0 | 1 |
| [stack-resume](../releases/host-evaluation/chatgpt/stack-resume.md) | reduced-pass | grades-chatgpt-09-12.json#17 | 1 |
| [stale-feature-map](../releases/host-evaluation/chatgpt/stale-feature-map.md) | blocked | grades-chatgpt-09-12.json#18 | 1 |
| [state-shape](../releases/host-evaluation/chatgpt/state-shape.md) | reduced-pass | grades-chatgpt-state-shape.json#0 | 1 |
| [supported-authoring](../releases/host-evaluation/chatgpt/supported-authoring.md) | reduced-pass | grades-chatgpt-09-12.json#19 | 1 |
| [swarm-walkthrough](../releases/host-evaluation/chatgpt/swarm-walkthrough.md) | reduced-pass | grades-chatgpt-09-12.json#20 | 1 |
| [symptom-repro](../releases/host-evaluation/chatgpt/symptom-repro.md) | blocked | grades-chatgpt-05-08.json#1 | 1 |
| [throwaway-probe](../releases/host-evaluation/chatgpt/throwaway-probe.md) | blocked | grades-chatgpt-09-12.json#21 | 1 |
| [trace-load](../releases/host-evaluation/chatgpt/trace-load.md) | reduced-pass | grades-chatgpt-05-08.json#2 | 1 |
| [trace-path](../releases/host-evaluation/chatgpt/trace-path.md) | reduced-pass | grades-chatgpt-09-12.json#22 | 1 |
| [trace-provenance](../releases/host-evaluation/chatgpt/trace-provenance.md) | blocked | grades-chatgpt-09-12.json#23 | 1 |
| [two-writers](../releases/host-evaluation/chatgpt/two-writers.md) | pass | grades-chatgpt-05-08.json#3 | 1 |
| [typed-boundary](../releases/host-evaluation/chatgpt/typed-boundary.md) | reduced-pass | grades-chatgpt-05-08.json#4 | 1 |
| [unavailable-persistence](../releases/host-evaluation/chatgpt/unavailable-persistence.md) | reduced-pass | grades-chatgpt-05-08.json#5 | 1 |
| [uncertain-result](../releases/host-evaluation/chatgpt/uncertain-result.md) | blocked | grades-chatgpt-05-08.json#6 | 1 |
| [unit-state](../releases/host-evaluation/chatgpt/unit-state.md) | blocked | grades-chatgpt-09-12.json#25 | 1 |
| [units-and-proof](../releases/host-evaluation/chatgpt/units-and-proof.md) | reduced-pass | grades-chatgpt-09-12.json#26 | 1 |
| [unknown-actual-model](../releases/host-evaluation/chatgpt/unknown-actual-model.md) | reduced-pass | grades-chatgpt-09-12.json#27 | 1 |
| [unknown-model](../releases/host-evaluation/chatgpt/unknown-model.md) | reduced-pass | grades-chatgpt-05-08.json#7 | 1 |
| [unsupported-selected-model](../releases/host-evaluation/chatgpt/unsupported-selected-model.md) | blocked | grades-chatgpt-09-12.json#28 | 1 |
| [user-correction](../releases/host-evaluation/chatgpt/user-correction.md) | reduced-pass | grades-chatgpt-05-08.json#14 | 1 |
| [user-tradeoff](../releases/host-evaluation/chatgpt/user-tradeoff.md) | reduced-pass | grades-chatgpt-05-08.json#15 | 1 |
| [verifiable-feature](../releases/host-evaluation/chatgpt/verifiable-feature.md) | blocked | grades-chatgpt-09-12.json#29 | 1 |
| [dependency-readiness](../releases/host-evaluation/chatgpt/dependency-readiness.md) | blocked | grades-chatgpt-09-12.json#24 | 1 |
