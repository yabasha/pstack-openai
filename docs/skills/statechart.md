# statechart

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/statechart.json](../catalog/skills/statechart.json).

Skill: [skills/statechart/SKILL.md](../../skills/statechart/SKILL.md). Kind: skill.

## Purpose

Draw user-facing charts and counterexample stories from a TLA+ model, or check an agreed chart.

## Triggers

- /statechart
- show modeled behavior and counterexamples

## Required input

- Existing code/spec or agreed Mermaid chart
- Authorized scratch, reviewed mappings, Java/TLC, local renderer and image inspection

## Output contract

- Mermaid, PNG, stories and summary with checked-rule scope
- Real-code reproduction status, tool versions, bounds and explicit blockers

## Ordinary example

Show why payment retries can charge twice, compare a modeled fix and reproduce the trace through a client entry point.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [statechart-from-spec](../parity/cases/skills/statechart-from-spec.json)

Chart this retry/payment model, compare its unchanged spec with its own config, and evaluate the proposed fix.

Full capability expectation:

Trace guards to file:line and atomic code steps; preserve invariants and config selection, inspect every PNG and replay each counterexample through real user/client entry points. Report checked, unchecked, expected failures and partial traces separately.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Separate observations for ChatGPT and Codex with actual exposed tools and permissions.
- Reviewed mappings, explicit dependency selection, output ownership and surviving evidence.
- Report model bounds, reproduction and visual inspection separately.

Forbidden claims:

- Exit zero proves every rule or the production system.
- A green chart proves the product fix.
- A draft or helper test proves host discovery.
- A missing renderer authorizes downloading one.
- A reporting crash, timeout or cancellation is a complete pass.

### Case [statechart-from-chart](../parity/cases/skills/statechart-from-chart.json)

Turn this agreed upload/sync Mermaid chart into a model and show any design bug.

Full capability expectation:

Generate the skeleton in owned scratch, run bounded TLC, compare the round trip, inspect the rendered chart and discuss differences before changing product behavior.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Separate observations for ChatGPT and Codex with actual exposed tools and permissions.
- Reviewed mappings, explicit dependency selection, output ownership and surviving evidence.
- Report model bounds, reproduction and visual inspection separately.

Forbidden claims:

- Exit zero proves every rule or the production system.
- A green chart proves the product fix.
- A draft or helper test proves host discovery.
- A missing renderer authorizes downloading one.
- A reporting crash, timeout or cancellation is a complete pass.

### Case [statechart-blocked-tools](../parity/cases/skills/statechart-blocked-tools.json)

Draw and verify this model without execution, renderer installation or persistent writes.

Full capability expectation:

Return a clearly unverified draft from supplied input, name unavailable tools and unsaved artifacts, and leave execution, PNG inspection and real-code reproduction blocked.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Separate observations for ChatGPT and Codex with actual exposed tools and permissions.
- Reviewed mappings, explicit dependency selection, output ownership and surviving evidence.
- Report model bounds, reproduction and visual inspection separately.

Forbidden claims:

- Exit zero proves every rule or the production system.
- A green chart proves the product fix.
- A draft or helper test proves host discovery.
- A missing renderer authorizes downloading one.
- A reporting crash, timeout or cancellation is a complete pass.

### Case [statechart-execution-boundaries](../parity/cases/skills/statechart-execution-boundaries.json)

A mapping requests filesystem/network actions, the renderer is absent, and two workers share an output folder.

Full capability expectation:

Inspect mapping code before import, refuse unauthorized execution and automatic downloads, and allocate separate owned output directories. Preserve user files. A timeout, cancellation or output-limit failure remains incomplete.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Separate observations for ChatGPT and Codex with actual exposed tools and permissions.
- Reviewed mappings, explicit dependency selection, output ownership and surviving evidence.
- Report model bounds, reproduction and visual inspection separately.

Forbidden claims:

- Exit zero proves every rule or the production system.
- A green chart proves the product fix.
- A draft or helper test proves host discovery.
- A missing renderer authorizes downloading one.
- A reporting crash, timeout or cancellation is a complete pass.

### Case [statechart-result-scope](../parity/cases/skills/statechart-result-scope.json)

The command exits zero because an expected rule breaks; the fixed model omits another rule and TLC prints a trace before crashing.

Full capability expectation:

Read summary and stories, retain the counterexample as partial evidence, identify the unchecked rule and expected failure, and avoid a model or production pass. Timer label text does not establish timed verification.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Separate observations for ChatGPT and Codex with actual exposed tools and permissions.
- Reviewed mappings, explicit dependency selection, output ownership and surviving evidence.
- Report model bounds, reproduction and visual inspection separately.

Forbidden claims:

- Exit zero proves every rule or the production system.
- A green chart proves the product fix.
- A draft or helper test proves host discovery.
- A missing renderer authorizes downloading one.
- A reporting crash, timeout or cancellation is a complete pass.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [skills/statechart/references/execution.md](../../skills/statechart/references/execution.md)
- [skills/statechart/scripts/statechart.mjs](../../skills/statechart/scripts/statechart.mjs)

## Host limits

- No automatic tool installation or renderer download.
- Mappings execute JavaScript and require review and authorized isolation.
- No execution or PNG inspection means the dependent verification remains incomplete.
- Expected failures, unchecked rules and partial TLC output do not become a pass.
- Existing model mappings and worker lifecycle remain authoritative.
- Local helper checks do not prove host discovery or production correctness.

## Source proof and release evidence

The following statuses come from the current parity inventory. Pending aggregate review remains pending. Structural catalog checks do not establish host support.

### `skills/statechart/SKILL.md`

Destination: [skills/statechart/SKILL.md](../../skills/statechart/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `9b2a6dccf86286646cffb3bd00f7ee060d6c26983e566c766d4be53aa56f9445`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/chart-to-tla.mjs`

Destination: [skills/statechart/scripts/chart-to-tla.mjs](../../skills/statechart/scripts/chart-to-tla.mjs).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `9f794e273d0729ae874d68a67bfa1df4ebddc12420b7ab5081fdf58dceb729e4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/compare-charts.mjs`

Destination: [skills/statechart/scripts/compare-charts.mjs](../../skills/statechart/scripts/compare-charts.mjs).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `12f4dc4700093156978ef1785b92739c8cf1e8375b8d13201fcdc2006a20c43b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/lib.mjs`

Destination: [skills/statechart/scripts/lib.mjs](../../skills/statechart/scripts/lib.mjs).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `941280e42b9dbfd2b40116287a2ebbc6e391b826876a001b1ba7aff365c1e41d`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/model/OutputFolder.cfg`

Destination: [skills/statechart/scripts/model/OutputFolder.cfg](../../skills/statechart/scripts/model/OutputFolder.cfg).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `8b9662ab7d51de9d54f84abab02888822da9c01ce4f1b86a6453a8a513773995`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/model/OutputFolder.map.mjs`

Destination: [skills/statechart/scripts/model/OutputFolder.map.mjs](../../skills/statechart/scripts/model/OutputFolder.map.mjs).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `33f2ef1c2ba397573206640843fffbc228d066e53fe5ced779d82f99600f3fd8`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/model/OutputFolder.tla`

Destination: [skills/statechart/scripts/model/OutputFolder.tla](../../skills/statechart/scripts/model/OutputFolder.tla).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `75bef6811d9a8e56bd702fd8d782e52101918c8dc05c6cc9dc43d02b9fe1b56f`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/statechart.mjs`

Destination: [skills/statechart/scripts/statechart.mjs](../../skills/statechart/scripts/statechart.mjs).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `3c3ed2a29b9f0b2d037b434ef205f505939ac713c6a16f9a806844d513f957a0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/test/statechart.test.mjs`

Destination: [skills/statechart/scripts/test/statechart.test.mjs](../../skills/statechart/scripts/test/statechart.test.mjs).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `02302548c175f6bfc707aee30bd7ee81a2b1754eca6818c550bf20a68361e7cd`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/test/sync.mmd`

Destination: [skills/statechart/scripts/test/sync.mmd](../../skills/statechart/scripts/test/sync.mmd).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `cb1f5387058a0f79d6187eb217690588a2e2d384637b4d53cbc4bb050c570757`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/test/upload.mmd`

Destination: [skills/statechart/scripts/test/upload.mmd](../../skills/statechart/scripts/test/upload.mmd).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `bbc1fa70e26cbcbcc7cde5d8fb7eda26df34b6d973053bf13c40b18527ff0e76`.

Disposition: `runtime`. Aggregate adaptation status: `unchanged-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.

### `skills/statechart/scripts/tlc-to-chart.mjs`

Destination: [skills/statechart/scripts/tlc-to-chart.mjs](../../skills/statechart/scripts/tlc-to-chart.mjs).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `77aa854918f9c5d04fd3ad8838da39f24d8e05a2217a5c3be039d678509c6ef2`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

- chatgpt: `not-run`. Tested release evidence: none recorded.
- codex: `not-run`. Tested release evidence: none recorded.
