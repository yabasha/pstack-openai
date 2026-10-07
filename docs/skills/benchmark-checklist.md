# benchmark-checklist

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/benchmark-checklist.json](../catalog/skills/benchmark-checklist.json).

Skill: [skills/benchmark-checklist/SKILL.md](../../skills/benchmark-checklist/SKILL.md). Kind: workflow.

## Purpose

Vet performance measurements before reporting or acting on a speedup or regression.

## Triggers

- Running a benchmark or reporting a measured speedup or regression

## Required input

- Claim, measurement script, workload, revisions/configurations and run artifacts
- Available inspection, execution, profiling and storage permissions

## Output contract

- Verdict with units, run count, range and evidenced limiter
- Seven-question measurement review and named gaps, with linked run evidence

## Ordinary example

Vet export on a 60k-row dataset across revisions A and B using at least 5 alternating runs per side before reporting a speedup.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [measurement-method](../parity/cases/skills/benchmark-checklist.json)

Report whether revision B improves export performance over revision A for a 60k-row workload. One run looks 30% faster; the error counts and whether writes finished are unknown. Explain the measurement method before claiming improvement.

Full capability expectation:

Record revisions and workload, run at least 5 alternating samples per side, check confounds and all seven gates, and report verdict, units, count, range and limiter. Treat differences below variation as no measurable difference. Missing limiter, untuned sides or unchecked errors/completed work make a claimed difference inconclusive.

Reduced capability expectation:

Review supplied scripts and artifacts when authorized runs or profiles are unavailable. Record sample count, revisions, workload and unverified confounds; retain inconclusive verdict for missing required evidence. Label a requested one-run ballpark and verify questions 4 and 7.

Blocked capability expectation:

If neither measurement artifacts nor authorized inspection/execution are available, identify the missing evidence and required method without claiming measured improvement.

Required observations:

- Record workload, dataset size, concurrency, timed region, sample count and exact compared revisions/configurations.
- Apply all seven canonical questions: evidenced limiter from a separate profiling run, production tuning, physical limits arithmetic, errors and correct output, at least 5 alternating runs per side with median/range, end-to-end relevance, and work inside the timed region.
- Preserve the explicit user-requested one-run ballpark exception with questions 4 and 7 and no adoption choice.
- Inspect exposed tools and permissions before execution or profiling; unavailable checks remain explicit.

Forbidden claims:

- A single unverified run proves a measured improvement.
- A profiling run is an unperturbed benchmark sample.
- Untuned configurations establish an adoption winner.
- Structural validation establishes host behavior.
- Unavailable tools or denied execution were successfully used.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [skills/principle-explain-the-number/SKILL.md](../../skills/principle-explain-the-number/SKILL.md)
- [skills/poteto-mode/playbooks/opening-a-pr.md](../../skills/poteto-mode/playbooks/opening-a-pr.md)
- [skills/poteto-mode/playbooks/perf-issue.md](../../skills/poteto-mode/playbooks/perf-issue.md)
- [skills/poteto-mode/playbooks/hillclimb.md](../../skills/poteto-mode/playbooks/hillclimb.md)

## Host limits

- Missing tools or permission leave affected checks unverified; missing required evidence makes a difference inconclusive.
- One-run ballparks require an explicit user request, errors and completed-work checks; option choices require the full method.
- Source metadata does not prove host invocation enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/benchmark-checklist/SKILL.md`

Destination: [skills/benchmark-checklist/SKILL.md](../../skills/benchmark-checklist/SKILL.md).

Upstream commit: `df581122cde17e6e27686b5a448bde23e4ad4318`. SHA-256: `6a767e788a60428fa14e645ee10fe2e49896e514ff654f668b1d824deb9038e8`.

Disposition: `runtime`. Aggregate adaptation status: `pending`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
