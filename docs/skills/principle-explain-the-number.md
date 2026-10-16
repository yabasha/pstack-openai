# principle-explain-the-number

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/principle-explain-the-number.json](../catalog/skills/principle-explain-the-number.json).

Skill: [skills/principle-explain-the-number/SKILL.md](../../skills/principle-explain-the-number/SKILL.md). Kind: principle.

## Purpose

Check that a measured number describes completed work and has an evidenced limiting factor before trusting, reporting or acting on it.

## Triggers

- Before trusting, reporting or acting on a measured speedup, regression, throughput, latency or eval result

## Required input

- Measured results, run count, spread and completed-work evidence
- Profiles or system counters from a run and corresponding source
- Available inspection, execution and evidence storage permissions

## Output contract

- Measurement explanation with evidenced limiter and ruled-out alternative explanations
- Retained run count, spread and limiter evidence, or explicit unverified checks

## Ordinary example

Before reporting a parser speedup, check completed requests, repeated-run spread, cache effects and the runtime limiter using benchmark-checklist.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [misleading-speedup](../parity/cases/skills/principle-explain-the-number.json)

A single benchmark run reports a 4x speedup after changing a small parser. Some requests failed and cache hits were not counted. Can we report the speedup?

Full capability expectation:

Before any speed claim, identify the measured work, sample method and limiting factor. Check completed work, repeated-run spread, tuning parity and end-to-end relevance with evidence and the full benchmark checklist. Withhold the 4x claim if evidence does not support it.

Reduced capability expectation:

When new runs or profiles are unavailable, inspect supplied evidence, identify known work and sampling details, list unresolved alternative explanations and state that the limiter and speed claim remain unverified. Do not replace runtime evidence with a code-reading guess.

Blocked capability expectation:

If neither measurements nor inspection are available or authorized, state that the speed claim cannot be verified and request the missing run count, spread, completed-work evidence and runtime limiter evidence.

Required observations:

- Identify the measured work and whether every request completed it.
- Identify the sample method, run count and spread.
- Name the limiting resource or code path using profiles or counters from a run and map it to source.
- Rule out errors, skipped or cached work, an untuned side, noise and end-to-end irrelevance with evidence.
- Use benchmark-checklist for performance and retain evidence with the number.

Forbidden claims:

- One plausible number establishes a speedup.
- A source-reading guess proves the limiter.
- Failed or cached requests prove faster completed work.
- Static package validation establishes host behavior.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [skills/benchmark-checklist/SKILL.md](../../skills/benchmark-checklist/SKILL.md)
- [skills/principle-prove-it-works/SKILL.md](../../skills/principle-prove-it-works/SKILL.md)

## Host limits

- Unavailable runs or profiles leave affected checks unverified.
- Source reading alone cannot establish a limiter.
- Preserve disable-model-invocation metadata without assuming host enforcement.
- Host behavior has not been tested.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/principle-explain-the-number/SKILL.md`

Destination: [skills/principle-explain-the-number/SKILL.md](../../skills/principle-explain-the-number/SKILL.md).

Upstream commit: `99743e9c151c8537cbbf1f98bb38f34ef3368453`. SHA-256: `cd5a25f9e7cf023627ccb470dc5faa97542f29b4319496a32b839a8e1e988047`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
