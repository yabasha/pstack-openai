# Reviewed workflow results

Version 0.1.3, operative freeze 51f209daf83cd97d64f89881d66533bb59dc57db. All 104 workflow cases have retained independent reviews. Coverage does not mean full success.

```json
{
  "host": "codex",
  "sourceFreeze": "51f209daf83cd97d64f89881d66533bb59dc57db",
  "counts": {
    "pass": 33,
    "reduced-pass": 50,
    "blocked": 21,
    "fail": 0,
    "attempts": 122
  }
}
```

| Case | Latest result | Attempts |
|---|---|---|
| [absent-workers](../releases/host-evaluation/codex/absent-workers.md) | pass | 3 |
| [accessible-trace](../releases/host-evaluation/codex/accessible-trace.md) | blocked | 1 |
| [adversarial-review](../releases/host-evaluation/codex/adversarial-review.md) | pass | 2 |
| [alternatives](../releases/host-evaluation/codex/alternatives.md) | pass | 1 |
| [approval-before-edit](../releases/host-evaluation/codex/approval-before-edit.md) | pass | 1 |
| [arena-walkthrough](../releases/host-evaluation/codex/arena-walkthrough.md) | reduced-pass | 3 |
| [authorized-program](../releases/host-evaluation/codex/authorized-program.md) | blocked | 1 |
| [benny-duplicate-report](../releases/host-evaluation/codex/benny-duplicate-report.md) | reduced-pass | 1 |
| [benny-existing-fix-ownership](../releases/host-evaluation/codex/benny-existing-fix-ownership.md) | reduced-pass | 1 |
| [benny-existing-pr](../releases/host-evaluation/codex/benny-existing-pr.md) | blocked | 1 |
| [benny-missing-adapter](../releases/host-evaluation/codex/benny-missing-adapter.md) | reduced-pass | 1 |
| [benny-missing-coordinates](../releases/host-evaluation/codex/benny-missing-coordinates.md) | reduced-pass | 1 |
| [benny-source-thread-compensation](../releases/host-evaluation/codex/benny-source-thread-compensation.md) | blocked | 1 |
| [benny-unsupported-trigger](../releases/host-evaluation/codex/benny-unsupported-trigger.md) | reduced-pass | 1 |
| [benny-untrusted-marker](../releases/host-evaluation/codex/benny-untrusted-marker.md) | blocked | 1 |
| [boundary-design](../releases/host-evaluation/codex/boundary-design.md) | reduced-pass | 2 |
| [bounded-improvement](../releases/host-evaluation/codex/bounded-improvement.md) | reduced-pass | 2 |
| [bounded-poll](../releases/host-evaluation/codex/bounded-poll.md) | reduced-pass | 2 |
| [caller-migration](../releases/host-evaluation/codex/caller-migration.md) | pass | 1 |
| [cancelled-worker](../releases/host-evaluation/codex/cancelled-worker.md) | pass | 1 |
| [candidate-cross-review](../releases/host-evaluation/codex/candidate-cross-review.md) | reduced-pass | 2 |
| [chatgpt-setup-from-readme](../releases/host-evaluation/codex/chatgpt-setup-from-readme.md) | blocked | 1 |
| [codex-setup-from-readme](../releases/host-evaluation/codex/codex-setup-from-readme.md) | blocked | 1 |
| [comparable-revisions](../releases/host-evaluation/codex/comparable-revisions.md) | reduced-pass | 1 |
| [contiguous-verified-stack](../releases/host-evaluation/codex/contiguous-verified-stack.md) | reduced-pass | 1 |
| [dead-path](../releases/host-evaluation/codex/dead-path.md) | pass | 1 |
| [decision-trail](../releases/host-evaluation/codex/decision-trail.md) | reduced-pass | 1 |
| [denied-writes](../releases/host-evaluation/codex/denied-writes.md) | reduced-pass | 1 |
| [dense-doc](../releases/host-evaluation/codex/dense-doc.md) | pass | 1 |
| [dependent-caller](../releases/host-evaluation/codex/dependent-caller.md) | pass | 1 |
| [discriminating-eval](../releases/host-evaluation/codex/discriminating-eval.md) | reduced-pass | 3 |
| [draft-only-authorized](../releases/host-evaluation/codex/draft-only-authorized.md) | reduced-pass | 2 |
| [empty-function](../releases/host-evaluation/codex/empty-function.md) | pass | 1 |
| [existing-personal-mode](../releases/host-evaluation/codex/existing-personal-mode.md) | blocked | 1 |
| [false-success](../releases/host-evaluation/codex/false-success.md) | pass | 1 |
| [fresh-worker-mode](../releases/host-evaluation/codex/fresh-worker-mode.md) | reduced-pass | 1 |
| [grounded-explanation](../releases/host-evaluation/codex/grounded-explanation.md) | reduced-pass | 1 |
| [guides-github-absent](../releases/host-evaluation/codex/guides-github-absent.md) | reduced-pass | 1 |
| [guides-local-codex](../releases/host-evaluation/codex/guides-local-codex.md) | reduced-pass | 1 |
| [guides-optional-setup-skipped](../releases/host-evaluation/codex/guides-optional-setup-skipped.md) | pass | 1 |
| [guides-ordinary-chatgpt](../releases/host-evaluation/codex/guides-ordinary-chatgpt.md) | reduced-pass | 1 |
| [guides-worker-chatgpt](../releases/host-evaluation/codex/guides-worker-chatgpt.md) | pass | 1 |
| [history-evidence](../releases/host-evaluation/codex/history-evidence.md) | reduced-pass | 1 |
| [inherited-identical-models](../releases/host-evaluation/codex/inherited-identical-models.md) | pass | 1 |
| [interrupted-action](../releases/host-evaluation/codex/interrupted-action.md) | reduced-pass | 1 |
| [interrupted-external-write](../releases/host-evaluation/codex/interrupted-external-write.md) | reduced-pass | 1 |
| [invalid-input](../releases/host-evaluation/codex/invalid-input.md) | pass | 1 |
| [invalid-state](../releases/host-evaluation/codex/invalid-state.md) | pass | 1 |
| [large-corpus](../releases/host-evaluation/codex/large-corpus.md) | reduced-pass | 1 |
| [legal-header](../releases/host-evaluation/codex/legal-header.md) | reduced-pass | 1 |
| [measurement-method](../releases/host-evaluation/codex/measurement-method.md) | reduced-pass | 1 |
| [migration-end-state](../releases/host-evaluation/codex/migration-end-state.md) | pass | 1 |
| [migration-units](../releases/host-evaluation/codex/migration-units.md) | reduced-pass | 2 |
| [misleading-speedup](../releases/host-evaluation/codex/misleading-speedup.md) | reduced-pass | 1 |
| [missing-model-enumeration](../releases/host-evaluation/codex/missing-model-enumeration.md) | pass | 1 |
| [missing-webhook](../releases/host-evaluation/codex/missing-webhook.md) | reduced-pass | 1 |
| [new-requirement](../releases/host-evaluation/codex/new-requirement.md) | pass | 3 |
| [no-persistent-tool](../releases/host-evaluation/codex/no-persistent-tool.md) | reduced-pass | 1 |
| [owned-safe-cleanup](../releases/host-evaluation/codex/owned-safe-cleanup.md) | blocked | 2 |
| [package-support-contracts](../releases/host-evaluation/codex/package-support-contracts.md) | reduced-pass | 1 |
| [partition-and-race](../releases/host-evaluation/codex/partition-and-race.md) | reduced-pass | 1 |
| [plain-restate](../releases/host-evaluation/codex/plain-restate.md) | pass | 1 |
| [poteto-walkthrough](../releases/host-evaluation/codex/poteto-walkthrough.md) | reduced-pass | 1 |
| [preserved-behavior](../releases/host-evaluation/codex/preserved-behavior.md) | reduced-pass | 1 |
| [prose-rewrite](../releases/host-evaluation/codex/prose-rewrite.md) | pass | 1 |
| [read-only-answer](../releases/host-evaluation/codex/read-only-answer.md) | reduced-pass | 1 |
| [real-app-contract](../releases/host-evaluation/codex/real-app-contract.md) | reduced-pass | 1 |
| [real-render](../releases/host-evaluation/codex/real-render.md) | blocked | 1 |
| [red-green](../releases/host-evaluation/codex/red-green.md) | pass | 1 |
| [repeatable-change](../releases/host-evaluation/codex/repeatable-change.md) | pass | 1 |
| [repeated-failure](../releases/host-evaluation/codex/repeated-failure.md) | blocked | 1 |
| [repeated-rule](../releases/host-evaluation/codex/repeated-rule.md) | blocked | 1 |
| [replay](../releases/host-evaluation/codex/replay.md) | reduced-pass | 1 |
| [reproduce-before-fix](../releases/host-evaluation/codex/reproduce-before-fix.md) | blocked | 1 |
| [resume-revision](../releases/host-evaluation/codex/resume-revision.md) | pass | 1 |
| [reversible-step](../releases/host-evaluation/codex/reversible-step.md) | pass | 1 |
| [route-recipe](../releases/host-evaluation/codex/route-recipe.md) | reduced-pass | 1 |
| [scoped-history](../releases/host-evaluation/codex/scoped-history.md) | blocked | 1 |
| [shape-first](../releases/host-evaluation/codex/shape-first.md) | blocked | 1 |
| [shared-path-conflict](../releases/host-evaluation/codex/shared-path-conflict.md) | pass | 1 |
| [smaller-solution](../releases/host-evaluation/codex/smaller-solution.md) | blocked | 1 |
| [stack-resume](../releases/host-evaluation/codex/stack-resume.md) | blocked | 1 |
| [stale-feature-map](../releases/host-evaluation/codex/stale-feature-map.md) | blocked | 2 |
| [state-shape](../releases/host-evaluation/codex/state-shape.md) | pass | 1 |
| [supported-authoring](../releases/host-evaluation/codex/supported-authoring.md) | reduced-pass | 1 |
| [swarm-walkthrough](../releases/host-evaluation/codex/swarm-walkthrough.md) | reduced-pass | 1 |
| [symptom-repro](../releases/host-evaluation/codex/symptom-repro.md) | blocked | 1 |
| [throwaway-probe](../releases/host-evaluation/codex/throwaway-probe.md) | reduced-pass | 1 |
| [trace-load](../releases/host-evaluation/codex/trace-load.md) | pass | 1 |
| [trace-path](../releases/host-evaluation/codex/trace-path.md) | pass | 1 |
| [trace-provenance](../releases/host-evaluation/codex/trace-provenance.md) | blocked | 1 |
| [two-writers](../releases/host-evaluation/codex/two-writers.md) | pass | 1 |
| [typed-boundary](../releases/host-evaluation/codex/typed-boundary.md) | pass | 1 |
| [unavailable-persistence](../releases/host-evaluation/codex/unavailable-persistence.md) | reduced-pass | 1 |
| [uncertain-result](../releases/host-evaluation/codex/uncertain-result.md) | reduced-pass | 1 |
| [unit-state](../releases/host-evaluation/codex/unit-state.md) | blocked | 1 |
| [units-and-proof](../releases/host-evaluation/codex/units-and-proof.md) | reduced-pass | 1 |
| [unknown-actual-model](../releases/host-evaluation/codex/unknown-actual-model.md) | pass | 1 |
| [unknown-model](../releases/host-evaluation/codex/unknown-model.md) | reduced-pass | 1 |
| [unsupported-selected-model](../releases/host-evaluation/codex/unsupported-selected-model.md) | pass | 1 |
| [user-correction](../releases/host-evaluation/codex/user-correction.md) | reduced-pass | 1 |
| [user-tradeoff](../releases/host-evaluation/codex/user-tradeoff.md) | reduced-pass | 1 |
| [verifiable-feature](../releases/host-evaluation/codex/verifiable-feature.md) | reduced-pass | 2 |
| [dependency-readiness](../releases/host-evaluation/codex/dependency-readiness.md) | reduced-pass | 1 |
