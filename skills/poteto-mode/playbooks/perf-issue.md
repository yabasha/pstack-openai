### Perf issue

You own the measurement story. Plan, review, verify the numbers. Tie every fix to a measurement, don't read source instead of measuring.

Read the complete [poteto mode](../SKILL.md) and required leaves. Use [session capabilities](../../../references/host-capabilities.md), [model roles](../../../references/model-roles.md), the [assignment contract](../../../references/orchestration-contract.md) and the full [poteto role prompt](../../../references/agent-prompts/poteto-agent.md). Record actual exposed controls, execution and artifact access before using them. Missing required reads stop dependent work. Do not install controls or profilers implicitly.

1. Capture a baseline trace via the matching control skill. Discover the actual control-cli or control-ui companion and its exposed tools for the measured CLI, UI or runtime. Missing or denied matching controls leave capture blocked. Reviewing supplied traces is a reduced assessment and does not prove a new capture. Vet the baseline, and each later number, with the complete [benchmark-checklist](../../benchmark-checklist/SKILL.md) and its [explain-the-number](../../principle-explain-the-number/SKILL.md) contract. Record the exact baseline and treatment revisions, workload, data size, concurrency, timed region, configuration, tuning, cache state, warmup, sample count, errors and completed work. Keep comparable runs and their artifacts. A choice between fixes is not the checklist's one-run ballpark exception.
2. Run [how](../../how/SKILL.md) to ground hypotheses. Don't claim a perf ceiling without running it first.
   Try the performance mantras in order, cheapest first:
   1. Don't do it. Stop work whose result nothing uses rather than cheapening it.
   2. Do it, but don't do it again.
   3. Do it less.
   4. Do it later.
   5. Do it when they're not looking.
   6. Do it concurrently.
   7. Do it cheaper.

   When an earlier mantra meets the target, stop.
3. Plan the fix from the trace. If it crosses a function boundary, run the complete [architect](../../architect/SKILL.md) workflow first, including its runner prompts, candidate screening and rationale. Delegate implementation to an authorized independent worker with the complete poteto role prompt, an exact input revision and distinct owned output. Use the configured perf-issue role only when its model and effort are supported by current exposed operations. Otherwise request inherited selection and disclose rejected or unavailable selections. Record requested and observed values separately; unknown observed values prove no model diversity. If the exact selection is required but unavailable, block it. Inspect the returned artifacts and review the diff. Without authorized workers, perform authorized sequential implementation as reduced capability; independent delegation remains unsatisfied. Capture a post-fix trace on the matching measured system and vet it with the same checklist.
   Apply [sequence-verifiable-units](../../principle-sequence-verifiable-units/SKILL.md), verifying each attempt before trying the next. An unavailable check blocks advancement and stays unverified.
4. Parse and compare the artifacts, including JSON to sqlite and a diff when applicable, using available authorized execution and storage. Retain original traces and the comparison artifact. Apply all seven checklist questions. For a comparison, run each side at least five times, alternate the sides, report median and range, and treat a gap smaller than variation as no measurable difference. Keep profiling runs separate from reported timings. Name the limiter from run evidence, check physical limits, production tuning, correct outputs, error counts, actual completed work and end-to-end relevance. "Inconclusive" or wrong-surface is not a pass. Flag it. Missing limiter, an untuned side, or unchecked errors or completed work makes a claimed difference inconclusive. Incompatible workloads, revisions or configurations cannot support the proposed performance claim.
5. Cite the measurement in the PR. Keep one primary number with its unit in the body and link the runs, range, limiter and trace comparison artifact. Prepare a local draft when PR writes are unauthorized; do not claim that draft is a created PR.
6. Run the complete [Opening a PR](opening-a-pr.md) playbook only within actual authorization and exposed capabilities. Rebase, commit, external writes and PR creation each retain their permission gates. Missing delivery dependencies stop delivery-dependent work. Opening a PR does not start Babysit.

For sustained improvement against a metric rather than a one-off fix, use the [Hillclimb](hillclimb.md) playbook. Preserve this playbook's earlier-mantra stop rule for the one-off fix. Hillclimb and Opening a PR remain pending companion dependencies for tasks 18 and 21, with task 24 integration.

Reply with the baseline number, post-fix number, delta and artifact path. Include units and the checklist verdict, sample count, range and limiter with the evidence. Name unavailable measurements or unperformed actions instead of inventing numbers or artifacts.
