# statechart

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/statechart.json](../catalog/skills/statechart.json).

Skill: [skills/statechart/SKILL.md](../../skills/statechart/SKILL.md). Kind: skill.

## Purpose

Check a TLA+ model and draw flat, parent or region statecharts with truthful rule scope.

## Triggers

- /statechart
- show modeled behavior and counterexamples

## Required input

- Reviewed TLA+ spec, config and executable view
- Authorized scratch, local Java/TLC and separately approved SVG renderer

## Output contract

- report.md, tlc.out, input hashes and chart.mmd within the 500-state budget
- Unchecked-rule, bounded, reproduction and visual-inspection status

## Ordinary example

Show a retry/payment bug path, run a proposed model fix separately and reproduce the trace through a client entry point.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [statechart-from-spec](../parity/cases/skills/statechart-from-spec.json)

Check this retry/payment TLA+ model with its reviewed config and view. Run a proposed fix separately and compare stated results.

Full capability expectation:

Compile a reviewed TLA+ model/config/view into report.md and available chart.mmd; inspect scope, real-code reproduction, artifacts and separately rendered SVG. No helper test or structural check proves host loading.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Discover actual tools and permissions separately for ChatGPT and Codex.
- Use reviewed executable views, explicit local Java/TLC, hashed scratch inputs and unique owned outputs.
- Read report.md and tlc.out; report checked, unchecked, bounded and incomplete results separately.
- Render SVG with approved local dependencies and inspect it; reproduce bugs through real entry points.

Forbidden claims:

- Exit zero proves unchecked rules or production correctness.
- A helper test proves host discovery.
- A missing tool authorizes installation.
- Retired comparison, chart-to-spec or PNG flags remain supported.
- A timeout or cancellation proves a pass.

### Case [statechart-from-chart](../parity/cases/skills/statechart-from-chart.json)

A caller requests the retired from-chart command. Explain the migration to an explicitly authored TLA+ model and reviewed flat, parent or region view.

Full capability expectation:

State that from-chart, --against, --fixed, --expect-broken, --png, summary.json and stories.md are retired. Do not fabricate automatic conversion or comparison. Offer a separately reviewed model and independent compiler runs.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Discover actual tools and permissions separately for ChatGPT and Codex.
- Use reviewed executable views, explicit local Java/TLC, hashed scratch inputs and unique owned outputs.
- Read report.md and tlc.out; report checked, unchecked, bounded and incomplete results separately.
- Render SVG with approved local dependencies and inspect it; reproduce bugs through real entry points.

Forbidden claims:

- Exit zero proves unchecked rules or production correctness.
- A helper test proves host discovery.
- A missing tool authorizes installation.
- Retired comparison, chart-to-spec or PNG flags remain supported.
- A timeout or cancellation proves a pass.

### Case [statechart-blocked-tools](../parity/cases/skills/statechart-blocked-tools.json)

Draw and verify this model without execution, renderer installation or persistent writes.

Full capability expectation:

Compile a reviewed TLA+ model/config/view into report.md and available chart.mmd; inspect scope, real-code reproduction, artifacts and separately rendered SVG. No helper test or structural check proves host loading.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Discover actual tools and permissions separately for ChatGPT and Codex.
- Use reviewed executable views, explicit local Java/TLC, hashed scratch inputs and unique owned outputs.
- Read report.md and tlc.out; report checked, unchecked, bounded and incomplete results separately.
- Render SVG with approved local dependencies and inspect it; reproduce bugs through real entry points.

Forbidden claims:

- Exit zero proves unchecked rules or production correctness.
- A helper test proves host discovery.
- A missing tool authorizes installation.
- Retired comparison, chart-to-spec or PNG flags remain supported.
- A timeout or cancellation proves a pass.

### Case [statechart-execution-boundaries](../parity/cases/skills/statechart-execution-boundaries.json)

A mapping requests filesystem/network actions, the renderer is absent, and two workers share an output folder.

Full capability expectation:

Compile a reviewed TLA+ model/config/view into report.md and available chart.mmd; inspect scope, real-code reproduction, artifacts and separately rendered SVG. No helper test or structural check proves host loading.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Discover actual tools and permissions separately for ChatGPT and Codex.
- Use reviewed executable views, explicit local Java/TLC, hashed scratch inputs and unique owned outputs.
- Read report.md and tlc.out; report checked, unchecked, bounded and incomplete results separately.
- Render SVG with approved local dependencies and inspect it; reproduce bugs through real entry points.

Forbidden claims:

- Exit zero proves unchecked rules or production correctness.
- A helper test proves host discovery.
- A missing tool authorizes installation.
- Retired comparison, chart-to-spec or PNG flags remain supported.
- A timeout or cancellation proves a pass.

### Case [statechart-result-scope](../parity/cases/skills/statechart-result-scope.json)

The command exits zero because an expected rule breaks; the fixed model omits another rule and TLC prints a trace before crashing.

Full capability expectation:

Compile a reviewed TLA+ model/config/view into report.md and available chart.mmd; inspect scope, real-code reproduction, artifacts and separately rendered SVG. No helper test or structural check proves host loading.

Reduced capability expectation:

Use supplied readable inputs for a labeled draft or partial assessment. Name every unexecuted check and missing artifact; do not infer a host pass.

Blocked capability expectation:

Missing authorization, tools, safe output ownership or required observations blocks the dependent step. Do not install dependencies, run unreviewed mappings, overwrite user files or report an incomplete check as passed.

Required observations:

- Discover actual tools and permissions separately for ChatGPT and Codex.
- Use reviewed executable views, explicit local Java/TLC, hashed scratch inputs and unique owned outputs.
- Read report.md and tlc.out; report checked, unchecked, bounded and incomplete results separately.
- Render SVG with approved local dependencies and inspect it; reproduce bugs through real entry points.

Forbidden claims:

- Exit zero proves unchecked rules or production correctness.
- A helper test proves host discovery.
- A missing tool authorizes installation.
- Retired comparison, chart-to-spec or PNG flags remain supported.
- A timeout or cancellation proves a pass.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)
- [references/model-roles.md](../../references/model-roles.md)
- [references/orchestration-contract.md](../../references/orchestration-contract.md)
- [skills/statechart/references/execution.md](../../skills/statechart/references/execution.md)
- [skills/statechart/scripts/statechart.ts](../../skills/statechart/scripts/statechart.ts)

## Host limits

- No automatic dependency installation.
- Views execute code and require review and authorized isolation.
- Retired chart-to-spec, model comparison flags and integrated PNG output are unsupported.
- Helper tests do not prove loading or behavior on either host.
- Unchecked rules, partial output and failed subprocesses remain explicit.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/statechart/SKILL.md`

Destination: [skills/statechart/SKILL.md](../../skills/statechart/SKILL.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `010b7b4532406739b1c3a426d1a45f02bb618a42561fc96b3976e064a7f8384d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/references/render.md`

Destination: [skills/statechart/references/render.md](../../skills/statechart/references/render.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8cca446eb0c8f87f2ef7b97c4b149f59aacdc153134b4217c4bcde09b10ac3c4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/backends/cfg.ts`

Destination: [skills/statechart/scripts/backends/cfg.ts](../../skills/statechart/scripts/backends/cfg.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `aea4d8766d214e7fa08f4881f1037319655e75eb56652e1b6d5d4f13a162e3e1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/backends/mermaid.ts`

Destination: [skills/statechart/scripts/backends/mermaid.ts](../../skills/statechart/scripts/backends/mermaid.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `75704b2704a9399a39479ff704a580d5b9a1d0fede01fe771df28bf799b434b6`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/backends/plain-text.ts`

Destination: [skills/statechart/scripts/backends/plain-text.ts](../../skills/statechart/scripts/backends/plain-text.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e2bedb855eb3806ec3fe7a7bfa49baa309fb4cf0da425b5fe1e0686268ce255a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/backends/report.ts`

Destination: [skills/statechart/scripts/backends/report.ts](../../skills/statechart/scripts/backends/report.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `730b4048578ab0468e1581f16fec60b246e321161effb68e481efb373f0f2501`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/frontends/config.ts`

Destination: [skills/statechart/scripts/frontends/config.ts](../../skills/statechart/scripts/frontends/config.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5eeab1e755f20a2c83b408c6503fdc9c6b10c971d8dedad3f912bd15f9763daf`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/frontends/dot.ts`

Destination: [skills/statechart/scripts/frontends/dot.ts](../../skills/statechart/scripts/frontends/dot.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4eef9ec848557dcd01ca8dbbec75b71c0653c1b73583108bafbb6f559f6d677b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/frontends/marks.ts`

Destination: [skills/statechart/scripts/frontends/marks.ts](../../skills/statechart/scripts/frontends/marks.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `eb0120e61a4004a435c7b7c46916da9dc8b2fa8696ed0d3eb64dc953fed3ab11`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/frontends/messages.ts`

Destination: [skills/statechart/scripts/frontends/messages.ts](../../skills/statechart/scripts/frontends/messages.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `36bfc6fb3ffa86897661efb2aa67bd95b55a4da9a3e952831f6e0668826b4b92`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/frontends/spec.ts`

Destination: [skills/statechart/scripts/frontends/spec.ts](../../skills/statechart/scripts/frontends/spec.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `450cdfc8d0577a96818ca3697efebbbf70b530a4ba7e3eee03cf1ba8d3f1a0fd`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/frontends/trace.ts`

Destination: [skills/statechart/scripts/frontends/trace.ts](../../skills/statechart/scripts/frontends/trace.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `7d083cf89b81c41556fc3fd5f07019886e0f6783c632475e7181ac4b81887367`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/frontends/value.ts`

Destination: [skills/statechart/scripts/frontends/value.ts](../../skills/statechart/scripts/frontends/value.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `7c54be394b7a10f60591858a0f08fb1e8dc0941df1f38ede07fbe7719ff56da0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/frontends/verdict.ts`

Destination: [skills/statechart/scripts/frontends/verdict.ts](../../skills/statechart/scripts/frontends/verdict.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0d0a9d6b6d6da5a7c48851b86d9d041f22982404dda6288795a1715138d7008b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/frontends/view.ts`

Destination: [skills/statechart/scripts/frontends/view.ts](../../skills/statechart/scripts/frontends/view.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2c0af8939321c5aaed4b6ecac8ce6a98d0e6774d8bd15d4b02fe4f406b8c9620`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/ir.ts`

Destination: [skills/statechart/scripts/ir.ts](../../skills/statechart/scripts/ir.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5602beca4e4ac08421cfa07e4da989f0e75439f1d136cc923226909e771dc7ff`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/package.json`

Destination: [skills/statechart/scripts/package.json](../../skills/statechart/scripts/package.json).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2c36842f391275b0f343a38947560adee155fab4a744eacef1e595e9f07c4e3d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/passes/annotate.ts`

Destination: [skills/statechart/scripts/passes/annotate.ts](../../skills/statechart/scripts/passes/annotate.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `dc8eeee09c3a9a0c060f32fb1d554e01bd80e5265751cdeb041ef3e19561b92a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/passes/label.ts`

Destination: [skills/statechart/scripts/passes/label.ts](../../skills/statechart/scripts/passes/label.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b5ef402369c5e7846be1fd39165e95cbfe715fc36eb9331a0401b26523c539c9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/passes/lift.ts`

Destination: [skills/statechart/scripts/passes/lift.ts](../../skills/statechart/scripts/passes/lift.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8977dddc6c93bb2e3914d5b50760eb66876107ba51e2b8cf9e18611b4c40c89c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/passes/loop-check.ts`

Destination: [skills/statechart/scripts/passes/loop-check.ts](../../skills/statechart/scripts/passes/loop-check.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `07d459385849aa35834040bf34e279c39baba68244ec9da17c57703a6ee8e2d4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/passes/paths.ts`

Destination: [skills/statechart/scripts/passes/paths.ts](../../skills/statechart/scripts/passes/paths.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9af1066b007ef86cb05c5e278eef09f090f1e46eb91d356e5146edbd4fee4ec7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/passes/reach.ts`

Destination: [skills/statechart/scripts/passes/reach.ts](../../skills/statechart/scripts/passes/reach.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b52b38f926814937b733221b40bd31075a69a2fb91ecbce2164752a8684bc5d6`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/passes/region-check.ts`

Destination: [skills/statechart/scripts/passes/region-check.ts](../../skills/statechart/scripts/passes/region-check.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8a6e0618740a14bb7048f6563b4324958177f4685d4d6d90364cc6245b1498b4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/passes/regions.ts`

Destination: [skills/statechart/scripts/passes/regions.ts](../../skills/statechart/scripts/passes/regions.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d740ebfdbb5ec7b4984412a635a596b43af7a77b8bcb49a1463c8afa75299f72`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/pipeline.ts`

Destination: [skills/statechart/scripts/pipeline.ts](../../skills/statechart/scripts/pipeline.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8aa8d9295ab6762f7f2ffae91a0aee98b1a1314747c875edba4598fdab8ed543`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/run.ts`

Destination: [skills/statechart/scripts/run.ts](../../skills/statechart/scripts/run.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f330e0a3b0a9f8181c2e52252c4a47db3f0a64f79a7cca5490263e33a5f13c72`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/statechart`

Destination: [skills/statechart/scripts/statechart](../../skills/statechart/scripts/statechart).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `aeffb7077850fd4c225e3d18049ca6ed7b988cf48e88cd8463526a7feaa74d13`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/statechart.ts`

Destination: [skills/statechart/scripts/statechart.ts](../../skills/statechart/scripts/statechart.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1c653f05d0cd0f3298455701f36e3d7d1f837f93e6e642f7c20afb5d613c2d12`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/ConfigOracle.java`

Destination: [skills/statechart/scripts/test/ConfigOracle.java](../../skills/statechart/scripts/test/ConfigOracle.java).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4f3367314f0fc34e39777d40dd31f96451985b77834fd0e925716aa3b169a021`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/chart.test.ts`

Destination: [skills/statechart/scripts/test/chart.test.ts](../../skills/statechart/scripts/test/chart.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3f9022fcc981d17f58b5e7a9302e766241f81a477bda70c3e621d7a1d95f19c1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/charts/Braces.mmd`

Destination: [skills/statechart/scripts/test/charts/Braces.mmd](../../skills/statechart/scripts/test/charts/Braces.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `dad412ccff506f4ace1b40617bcc2f103ad0372ddc0135ab26535fc488fef8d3`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/charts/Escapes.mmd`

Destination: [skills/statechart/scripts/test/charts/Escapes.mmd](../../skills/statechart/scripts/test/charts/Escapes.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `211adde39edbb349e2d8acc2f95762bfb7da1fb030e5dc815a8982775e1cd372`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/charts/Phases.mmd`

Destination: [skills/statechart/scripts/test/charts/Phases.mmd](../../skills/statechart/scripts/test/charts/Phases.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `bf6062f6a0ee7b8d487882a1810d17951606fd536b2ee370aecc3d3914da0339`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/cli.test.ts`

Destination: [skills/statechart/scripts/test/cli.test.ts](../../skills/statechart/scripts/test/cli.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8a3b028dafe2065029a66242f7a3832d18058e772a0dfc1b2c170511ffee8e07`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/config-fuzz.test.ts`

Destination: [skills/statechart/scripts/test/config-fuzz.test.ts](../../skills/statechart/scripts/test/config-fuzz.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a258744d47529418d32de0fd47aa2d013298581b73064f7ba4d628e4d5471321`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus.test.ts`

Destination: [skills/statechart/scripts/test/corpus.test.ts](../../skills/statechart/scripts/test/corpus.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5686aa487dfec3e0a06b3c15390dbc3ab5953ced532c5eee7d5c5e2f54f492c7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Counter/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/Counter/ChartRun.out](../../skills/statechart/scripts/test/corpus/Counter/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `05cf40936af6590878a1bbe8290b9fdebe7d33503331105be352b1901584200e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Counter/Counter.cfg`

Destination: [skills/statechart/scripts/test/corpus/Counter/Counter.cfg](../../skills/statechart/scripts/test/corpus/Counter/Counter.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ee4c110b174a3bd2cc54226420ba2c979682be57c7964273b8a30d6395dc2c3f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Counter/Counter.tla`

Destination: [skills/statechart/scripts/test/corpus/Counter/Counter.tla](../../skills/statechart/scripts/test/corpus/Counter/Counter.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a277dd9ba29b50b21d87d5ebbbaff3ed87949e427ce563ddb37ede7ba728da05`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Counter/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/Counter/chart.mmd](../../skills/statechart/scripts/test/corpus/Counter/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `bcdc46dccfa6172fa9e36c3236fb1cb9221d0648534499d5fe0c51ebd13d22b0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Counter/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/Counter/graph.dot](../../skills/statechart/scripts/test/corpus/Counter/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4c12b6f39274a6227df5837a066430cc2ce5b928d0c8cf63269bd428367c7026`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Counter/report.md`

Destination: [skills/statechart/scripts/test/corpus/Counter/report.md](../../skills/statechart/scripts/test/corpus/Counter/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e52a2affff3ca2d85c6ee87a4543ca99024fa0db8a3d48070a6752520121a413`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Counter/sany.out`

Destination: [skills/statechart/scripts/test/corpus/Counter/sany.out](../../skills/statechart/scripts/test/corpus/Counter/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9041a7726d3e497fb10c5d67293d76f3318d448ce08c371a90454c43c65722c1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Counter/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/Counter/verdict-1.out](../../skills/statechart/scripts/test/corpus/Counter/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ce981c26c48bba282ebc9794a473575f3981909c4ec47bd9df9327316eae71e4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterAction/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ea9ceacfd5ea703bf19893d82f7e790f3b39441b3588c7248286710cf472495d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/CounterAction.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/CounterAction.cfg](../../skills/statechart/scripts/test/corpus/CounterAction/CounterAction.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4666d0659cf69047aa41e64a48f307cff103a6b0815d85ead5bd4c0386a0f5b7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/CounterAction.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/CounterAction.tla](../../skills/statechart/scripts/test/corpus/CounterAction/CounterAction.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `895ed84802b88a6deb9653e7baf36b1eb67b848592c91d168d84db03b73c74f5`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterAction/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d35190a320e1b9e5cb35ae583b8367d2d10bf4cc17b1f7e94e4edf0613d01730`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/graph.dot](../../skills/statechart/scripts/test/corpus/CounterAction/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `906fdbce95c4d0628441a231d9d9124d506d34f95ba08f653f3db084d13c5c1d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/report.md](../../skills/statechart/scripts/test/corpus/CounterAction/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `36d49034aab3b675026e717c876ad5da5f74468338295b399da3fd4c3b0e8d6a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/sany.out](../../skills/statechart/scripts/test/corpus/CounterAction/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e529b1c17203bbc05da9d74a48adb9ac4f06cff3f33df94ba215daa8b315dc9a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterAction/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterAction/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a5e7c90e12c0f9b3b7420db90c06a8277369a4757c7b20ece83689ac577129ce`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/verdict-2.exit](../../skills/statechart/scripts/test/corpus/CounterAction/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterAction/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ad46743f4fbbd0557be8cdbec10e127bd90e3fd9c88c50f3338f95118d9d5b49`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterAction/verdict-3.out`

Destination: [skills/statechart/scripts/test/corpus/CounterAction/verdict-3.out](../../skills/statechart/scripts/test/corpus/CounterAction/verdict-3.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9b6d49a17a5371709ee942785acf8c8742fdddaed7723d1cb3ade58686732301`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterDeadlock/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `c3ac24eafc6f680c59b976e6ddd4ec6272623e1a3641fe43707abbf208c9d9d3`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/CounterDeadlock.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/CounterDeadlock.cfg](../../skills/statechart/scripts/test/corpus/CounterDeadlock/CounterDeadlock.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `394991fa4d162ed8ea74e6e5b5473af8c246ec3db12da3737fce046c41e78692`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/CounterDeadlock.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/CounterDeadlock.tla](../../skills/statechart/scripts/test/corpus/CounterDeadlock/CounterDeadlock.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d6af2fc22ab5fbe8d64ae6202187ce807e53189a43eef1af860db55db933b132`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterDeadlock/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `928b930e2d28f94e083183cc064f1dde292a5f65fcc0dfec013b04c234e6254b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/graph.dot](../../skills/statechart/scripts/test/corpus/CounterDeadlock/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4c12b6f39274a6227df5837a066430cc2ce5b928d0c8cf63269bd428367c7026`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/report.md](../../skills/statechart/scripts/test/corpus/CounterDeadlock/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b4e4365f95f4b34abea8ffb1fde1bd39b8e8eb6f30e839d75332c6c834460c25`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/sany.out](../../skills/statechart/scripts/test/corpus/CounterDeadlock/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `7a8d40cbae42b10eaea8e6dc42f28ce31892e22c77d521e2cb8d8a6d3d0f0c33`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ae615936a1dde25fd76c7cd7a98891c2e8e8a363ea3457bf8e51b9412f0b050b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-2.exit](../../skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `25d4f2a86deb5e2574bb3210b67bb24fcc4afb19f93a7b65a057daa874a9d18e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterDeadlock/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `94f71505e927d30483f539ca838f6661df4488332075f1dfec5eabe188f3f855`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterFan/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `819af259403aab9b4eb407b8a6f04e088d9a428d8fbf6fa871c2380d44de8d21`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/CounterFan.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/CounterFan.cfg](../../skills/statechart/scripts/test/corpus/CounterFan/CounterFan.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e2de6875a48efd06a1db4aae4d7cc5b86ff9a0b4698074049c7ee52bfb49d3f7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/CounterFan.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/CounterFan.tla](../../skills/statechart/scripts/test/corpus/CounterFan/CounterFan.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1fddc670bda9ad7a900d29891aca1329a9e9f932d353ea944379f6f45bc50a5e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterFan/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2f59dcc1236cc70d4e6609139237e07b7e6645f63129b8722ef6e1d44030b0fd`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/graph.dot](../../skills/statechart/scripts/test/corpus/CounterFan/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ee3e20bd9b56b5dc2cc21b653719a588c9dbe08855e0493c262e3c673cea2805`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/report.md](../../skills/statechart/scripts/test/corpus/CounterFan/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `016771561b9b5b0a45c0d8c805723a6b8bc39396281dba6d4f6c7b3f1e151612`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/sany.out](../../skills/statechart/scripts/test/corpus/CounterFan/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5a58a05867b5cb952d4b1de562190e85b8dc1485a7201385e622a2af27519c96`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterFan/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterFan/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `546e81530ae614ae7264ae857b00e677cb01211a0194cd88583b0d80794fc260`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterFan/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterFan/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterFan/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8e6dc10d24a0ac3ddb86afd8674310c44a8d20488d38346dc8ee896807fc3320`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/ChartRun.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/ChartRun.exit](../../skills/statechart/scripts/test/corpus/CounterGuard/ChartRun.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `84b9bb077be0d8a29d0d01ef350d718b77c2ec5f40c3ab90502b1b4b5016c550`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterGuard/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `78a0d2a62cbb70c1f182a994f1661db2596115b5e53210a2f0125b1390129c29`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/CounterGuard.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/CounterGuard.cfg](../../skills/statechart/scripts/test/corpus/CounterGuard/CounterGuard.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3239ec0757c48dfbf02f914005fd2c9d114e9f2989d42e15184df887e322a301`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/CounterGuard.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/CounterGuard.tla](../../skills/statechart/scripts/test/corpus/CounterGuard/CounterGuard.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `c2d7ed7d7bd4b317764d590dbd9bb6cbe7819500c7e6707787fe3065460c99a7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterGuard/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8baa9330755dd4217aadd731b77fde833f747d09998944ada660b2708cc7d313`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/graph.dot](../../skills/statechart/scripts/test/corpus/CounterGuard/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `7b0b58221d3980d6d64cb979c22523fbfe5796e465bae79e6d19fdd9c607e547`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/report.md](../../skills/statechart/scripts/test/corpus/CounterGuard/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `454b4672f07c18e52827e9906fea37c6e701c5d87eea7ca3675163375c02b64f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/sany.out](../../skills/statechart/scripts/test/corpus/CounterGuard/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8d331316b1be40a834e166268f8abe94f884bfcfe35135b6492eacb1ee825788`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterGuard/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterGuard/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `580ce25bf18afc8bd1b9df54f4053b719acce5ca10c2794475a8fba249417eb6`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/verdict-2.exit](../../skills/statechart/scripts/test/corpus/CounterGuard/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `84b9bb077be0d8a29d0d01ef350d718b77c2ec5f40c3ab90502b1b4b5016c550`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterGuard/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterGuard/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterGuard/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3828a6b606057844dedf464e94374092293787b0f4be8b9950931de7d70946da`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterInitPast/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9323d9f012374d2392fd4f7fbe655e1ed6fce04160270c11ceada536c51ce677`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/CounterInitPast.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/CounterInitPast.cfg](../../skills/statechart/scripts/test/corpus/CounterInitPast/CounterInitPast.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f42b6456243b9a8f39599597bb630b68b02b0e66683e96896cb06d2b81af94d9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/CounterInitPast.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/CounterInitPast.tla](../../skills/statechart/scripts/test/corpus/CounterInitPast/CounterInitPast.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `745a6e54d0b9c285d797481a09d4a531004f46b04fb5ef0b7c35194fa4d6a137`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterInitPast/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `28797d6572aa78a9f49f04a3247b62a7047e660af586d8717877164f3bda73e2`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/graph.dot](../../skills/statechart/scripts/test/corpus/CounterInitPast/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `372ed91b09c1602514668fe24101315737f060e607fb959af0b55dde9efc4ed1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/report.md](../../skills/statechart/scripts/test/corpus/CounterInitPast/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `757128a547d5de236c96e47780e5ce8852d1b5873912f31fd4a964222b986295`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/sany.out](../../skills/statechart/scripts/test/corpus/CounterInitPast/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `74535350e20489c088c310d49ac2abab35c0bd3dcd7b9a500b351846da01f62f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterInitPast/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterInitPast/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a10d803555dbc95cdeae0850097f60e04ed20e467760270c8c58400b0629b6d8`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPast/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPast/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterInitPast/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9133f74a060cd7b2ff3364ca90bbcec4596c6fee035468e49e0ad1209260899c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPastHolds/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPastHolds/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterInitPastHolds/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1bf4035560dba1b655bb1577caf63df9f3dd9444380e42c9cffc721c1f6e019`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPastHolds/CounterInitPastHolds.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPastHolds/CounterInitPastHolds.cfg](../../skills/statechart/scripts/test/corpus/CounterInitPastHolds/CounterInitPastHolds.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b1ca71d25dbb08c93b0ebaf628eb536ef6c98e3e599d8146e0a0c43f5eeb800d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPastHolds/CounterInitPastHolds.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPastHolds/CounterInitPastHolds.tla](../../skills/statechart/scripts/test/corpus/CounterInitPastHolds/CounterInitPastHolds.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `97bafdcba8976d26069b89c31a549d3d7d992cf9cde10d654133d55f2ce604e7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPastHolds/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPastHolds/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterInitPastHolds/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f74c6486f80c1e9820a901a730eecb3d6f9aa88076f704b87a60bb02b8b24d01`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPastHolds/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPastHolds/graph.dot](../../skills/statechart/scripts/test/corpus/CounterInitPastHolds/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `372ed91b09c1602514668fe24101315737f060e607fb959af0b55dde9efc4ed1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPastHolds/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPastHolds/report.md](../../skills/statechart/scripts/test/corpus/CounterInitPastHolds/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `60a12f6918ea21e77def19b66ff94ff47ce834f7ddbfef4c246570d02a0c6e78`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPastHolds/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPastHolds/sany.out](../../skills/statechart/scripts/test/corpus/CounterInitPastHolds/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `91f7850c1fe9fd4507f457dea2a047abd4013182f56cda2e7aa587b7b4edaf77`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInitPastHolds/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInitPastHolds/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterInitPastHolds/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ff6df0e311060e629b11d3f5939ef4e9efb23beafb3d8db9facca963a3a86acd`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterInstance/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `12e78945b0e37f41b86705b53c09c044a06427265e23613908052a0c7661c5f6`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/CounterInstance.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/CounterInstance.cfg](../../skills/statechart/scripts/test/corpus/CounterInstance/CounterInstance.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f0d016dfb57a8661eac65d738ca9b797242c486e4fe5a0d7379e9424c7de3cc8`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/CounterInstance.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/CounterInstance.tla](../../skills/statechart/scripts/test/corpus/CounterInstance/CounterInstance.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `cbee0c802f8984ef74bb2d85e7d75635522755540e0175c51ba1cb0a099a9345`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/CounterSteps.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/CounterSteps.tla](../../skills/statechart/scripts/test/corpus/CounterInstance/CounterSteps.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ec27748a316d01d7384a402166ff3fe36c7364511fd1681797832f2a1777e8ac`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterInstance/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `649d905eb59e1a2972e56396f4aeaff6cafb40c6733c55b5829d36cb4986eb8e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/graph.dot](../../skills/statechart/scripts/test/corpus/CounterInstance/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ca06f91bdafb423be1fac388ab5b90d8f78ff96148c2120a61e085f0dc4c108b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/report.md](../../skills/statechart/scripts/test/corpus/CounterInstance/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2d6a8b73b1a6f4003bd5c3c669191ab08d04cb03fe441fad8f892b4e8d581569`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/sany.out](../../skills/statechart/scripts/test/corpus/CounterInstance/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5b8a514e26f02cf174138ba433a2a3d792c1822011e2c69907ef18f2ba5a27d8`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterInstance/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1a252402972f6057fa53cc172b52b9ffca698e18311facd0f3b06ecaaef79e17`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterInstance/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterInstance/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterInstance/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `79dd3301ed8763da38d13e871e333e1f739ef985b43d586f70c7e45c93a7157f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterJump/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e5a45da16ae7638b1bf30fd72cb482ed4b97183262ee130a73337a2fa4f28a0d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/CounterJump.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/CounterJump.cfg](../../skills/statechart/scripts/test/corpus/CounterJump/CounterJump.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a94be2a46d740142d19cf03c288547c03cb0fa7d8ab9590a78eb0de7b99ba235`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/CounterJump.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/CounterJump.tla](../../skills/statechart/scripts/test/corpus/CounterJump/CounterJump.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `62e09e72adfdc0bda81d4e4d26c3c8c56641589258b6308d4c3c0e62c882f035`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterJump/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b9829b90a85d056c88c8742e17caf5058941048dc411a48524115481a29be92f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/graph.dot](../../skills/statechart/scripts/test/corpus/CounterJump/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f829d5cb1d9027aed499564e5574c8955d91a9b3decb32179000de757c9817a1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/report.md](../../skills/statechart/scripts/test/corpus/CounterJump/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b459f42807ac3dc2d0ac0f26aa13b549525e0b946871e787ca07e58f6c8ade98`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/sany.out](../../skills/statechart/scripts/test/corpus/CounterJump/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `68b6e92c3232530a43b49e8292eb0a6e2e8e2c8e04a7e0932e59e7d38f8d4527`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterJump/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterJump/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9ceb7d389d7cd13f894db85dc00f0b1f0aaccfe7931804202ad6ab770e284461`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterJump/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterJump/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterJump/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `7e52bb5a6f8ddb55669eb03ea5dd360ba4bf7f5c3155a1078f1ba152805038d9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterLoop/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterLoop/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterLoop/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8e7aaaa8f605109e5dff38439ec5a9ff4d3b94d02612a4b1ce2763754a66cb54`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterLoop/CounterLoop.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterLoop/CounterLoop.cfg](../../skills/statechart/scripts/test/corpus/CounterLoop/CounterLoop.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f0d016dfb57a8661eac65d738ca9b797242c486e4fe5a0d7379e9424c7de3cc8`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterLoop/CounterLoop.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterLoop/CounterLoop.tla](../../skills/statechart/scripts/test/corpus/CounterLoop/CounterLoop.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `84449896e318fd129b82f574b644ea16a73c1f23e9331cdb9361d5a284e17cdc`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterLoop/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterLoop/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterLoop/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0157bf074e7aa642a0819cd6eb2352fc57c21866962f2944bf71e2c028c9bff9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterLoop/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterLoop/graph.dot](../../skills/statechart/scripts/test/corpus/CounterLoop/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6558ade4931cfbe5c28ed713504072976d401072dad6acc4506c84afb3169b99`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterLoop/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterLoop/report.md](../../skills/statechart/scripts/test/corpus/CounterLoop/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `fb9d5d76f6c1c00746f9fdc211ee26eb82c5649ed212c2fdf9e9810a4a33ab10`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterLoop/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterLoop/sany.out](../../skills/statechart/scripts/test/corpus/CounterLoop/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2a3cb63115eaaf7e19557949fc97785d112b2dcfec55dcb00583daa8926d19f7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterLoop/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterLoop/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterLoop/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1a252402972f6057fa53cc172b52b9ffca698e18311facd0f3b06ecaaef79e17`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterLoop/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterLoop/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterLoop/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `33158ae03c65371f4b028818420652deaee879b77f4e6b8da688038079e98511`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterOrder/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `07e4fc2dca6afe0d621dd26603330c59a6052d1bebb19f395ff8e30c3772e667`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/CounterOrder.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/CounterOrder.cfg](../../skills/statechart/scripts/test/corpus/CounterOrder/CounterOrder.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6f321b62ecd415eda4363ce98e05b470d277f8b169dee8658a267668e7f3fb5b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/CounterOrder.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/CounterOrder.tla](../../skills/statechart/scripts/test/corpus/CounterOrder/CounterOrder.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `173e3ba50a4b662464e1188d31d5c306c0202a03385978a8aa841cf0c2f5e8a0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterOrder/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8259183f842918dfaa6f70fb805db9db5a61f3db0af13c2cf09e9e131136d8d1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/graph.dot](../../skills/statechart/scripts/test/corpus/CounterOrder/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `7a5d0a1efcf36b579f640e283c38a2054c8740cf96bb2b332bb42e2aaff8481c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/report.md](../../skills/statechart/scripts/test/corpus/CounterOrder/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a37510137bc3d2c9bdf2be48a40aca3f36b44aa5b9be1f4f2f6cfbacfbbd2693`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/sany.out](../../skills/statechart/scripts/test/corpus/CounterOrder/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e4d8472643a723ed5b3cc8772af07d24d534edcc1a6d36b2690de2d395906ed5`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterOrder/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterOrder/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a9d4f6b1b08b5ee7505e20d9a0f90a88cf533a1a4737fd71ae70a162e520af6c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/verdict-2.exit](../../skills/statechart/scripts/test/corpus/CounterOrder/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `25d4f2a86deb5e2574bb3210b67bb24fcc4afb19f93a7b65a057daa874a9d18e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterOrder/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterOrder/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterOrder/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `57fba1d11f08153f7598c7a6843c557d4804d7ab57b59cf68eafd22116267de3`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterRules/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `c6a688529dfb153ca9206928f04563b2c0f2cb448bf1cf6cfabfeb94981f9d72`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/CounterRules.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/CounterRules.cfg](../../skills/statechart/scripts/test/corpus/CounterRules/CounterRules.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `931efa110d01b684843f905cae87fb2308b70b324ca9f51ab1bb6617595047c2`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/CounterRules.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/CounterRules.tla](../../skills/statechart/scripts/test/corpus/CounterRules/CounterRules.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `57f1be6cc35c3f8252aacc2916975045d1932fab868d961d9c461e23f666eb86`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/Moves.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/Moves.tla](../../skills/statechart/scripts/test/corpus/CounterRules/Moves.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3c58aaa6098d94f727d427d7ce65ebbc79d684c5a6d7b8e18ccdf2b9222a0a56`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterRules/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a8349b6203985b4cf3f10d581d7a15a312c19262ee7a8de8b73ba62311a817ea`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/graph.dot](../../skills/statechart/scripts/test/corpus/CounterRules/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `80b70738200d8b16e52b598fd6ddffb607f672550168cc8756c8605180210fce`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/report.md](../../skills/statechart/scripts/test/corpus/CounterRules/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6db41c347e7d680d126168093dcce483e5406c5ea4728b32149f3d8c104b1259`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/sany.out](../../skills/statechart/scripts/test/corpus/CounterRules/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6c96b7563f60ca3b1860627a5588093b401d30c13724ccb2c77cee6238c69667`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterRules/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterRules/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `47b09992efa66d8a3ed65f24d25f5227dbfb48fe2b46b1803ef07ac461122073`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/verdict-2.exit](../../skills/statechart/scripts/test/corpus/CounterRules/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterRules/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `fb0503db6628e034c70ee48dc402bc79514564a438ff2c61d02f7533faf7d64c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/verdict-3.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/verdict-3.exit](../../skills/statechart/scripts/test/corpus/CounterRules/verdict-3.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/verdict-3.out`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/verdict-3.out](../../skills/statechart/scripts/test/corpus/CounterRules/verdict-3.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8cd2712e7ec2f9f4941e1ae12c9476126f19c1a1a11d2a20291ec131e2f63819`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterRules/verdict-4.out`

Destination: [skills/statechart/scripts/test/corpus/CounterRules/verdict-4.out](../../skills/statechart/scripts/test/corpus/CounterRules/verdict-4.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b776bfd4513942329b885fdd7fce1bde2d25c063ef81ec382eba7769555a53eb`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterStart/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0cc81c2f968b23b4c8c1fd8e1c2032991a8d2d6137ab267958aeb7aee478b240`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/CounterStart.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/CounterStart.cfg](../../skills/statechart/scripts/test/corpus/CounterStart/CounterStart.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `eff943bab49dc0cad0567a0d4456671724b778d7913a2ba38de16a12386b7a58`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/CounterStart.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/CounterStart.tla](../../skills/statechart/scripts/test/corpus/CounterStart/CounterStart.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `dbbb6c141d88a7bc4dc354c89d85ce9623871070b0dc93ca7ba6c0ece2043b28`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterStart/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `fca72ed62e89b903e63a7f2a646a29cee33f72b1b60a6c96793bbcc807e09f74`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/graph.dot](../../skills/statechart/scripts/test/corpus/CounterStart/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1c259eb08cedb809a62f24d59232f229d2cc0df8f6bd97285946ce2d586daaef`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/report.md](../../skills/statechart/scripts/test/corpus/CounterStart/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `01444b757bca7435af323af5a6a31caff91388bb84ab48948b2660a80d78b8e4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/sany.out](../../skills/statechart/scripts/test/corpus/CounterStart/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `61a0c605d5ab3806d5ea8779ac00d344e4b19a2c423288b48fb893037de63425`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterStart/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterStart/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `152cbd7654bbe39c550b3122009fecfa07dabed3e658ac4845b5f5f60dc309de`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStart/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterStart/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterStart/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e4d43ce2f301d2ac1c03693981dc6a7b3c84c7af671f9b0d6bff1c4b287c6876`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStop/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterStop/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterStop/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `11bcbb21c9a5b3c5491e436c8fc61d339a7c27593fced2199132ab6cf8e4d489`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStop/CounterStop.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterStop/CounterStop.cfg](../../skills/statechart/scripts/test/corpus/CounterStop/CounterStop.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `eff943bab49dc0cad0567a0d4456671724b778d7913a2ba38de16a12386b7a58`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStop/CounterStop.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterStop/CounterStop.tla](../../skills/statechart/scripts/test/corpus/CounterStop/CounterStop.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e4486923b563ac7fb028e8513e79e3caa5e0905579d423569e9c918938e0f12c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStop/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterStop/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterStop/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0ddf7a93d1317fa0414c0c5b05dba856c268a2124c4e06caebc3f5b4ad6f393c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStop/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterStop/graph.dot](../../skills/statechart/scripts/test/corpus/CounterStop/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1c259eb08cedb809a62f24d59232f229d2cc0df8f6bd97285946ce2d586daaef`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStop/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterStop/report.md](../../skills/statechart/scripts/test/corpus/CounterStop/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5d0e28ce1ceefb740ecc85076c8be6a5a5bf00d00a8bc3a0a00b5494dfbf025d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStop/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterStop/sany.out](../../skills/statechart/scripts/test/corpus/CounterStop/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `933921ca1dcf5b7e089d2aca59ac79a50e521f22c60cebd5812be4e3e67ec58c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterStop/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterStop/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterStop/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9d4714340d24c6d5a1a22ed36b6bce0943c8eeff28fc32bd0b54fc1aba2b9331`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterTie/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `bce917da55d7f549b2902c3ebbf2a7bfc7da9d7de8e3e099a9dc6c7fa815fc37`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/CounterTie.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/CounterTie.cfg](../../skills/statechart/scripts/test/corpus/CounterTie/CounterTie.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b3d7d0ae1bba01c98903b54cefb4ba76afbb3ce07957431a03e53505ffe95510`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/CounterTie.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/CounterTie.tla](../../skills/statechart/scripts/test/corpus/CounterTie/CounterTie.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e668ff93e2213651d6bb14e14255814cb37ab61062466384b953563b2d844daa`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterTie/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0fcc808934cbf91f592eda060de978064e4854c704d1c861332f875cf7415543`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/graph.dot](../../skills/statechart/scripts/test/corpus/CounterTie/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `906fdbce95c4d0628441a231d9d9124d506d34f95ba08f653f3db084d13c5c1d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/report.md](../../skills/statechart/scripts/test/corpus/CounterTie/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9649f57adfbd71a5f4430bcde0d95234883b1daf80eff2d91a0dbd1ddf6d3739`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/sany.out](../../skills/statechart/scripts/test/corpus/CounterTie/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4ce39c0150c1cc1c9d657b927f22103fc8ecf1d0f0678137970ac98fe2a8d355`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterTie/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterTie/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `62f4153c4a5e690d868b0e623c83c272a1a15ea3b9fde47f5e4ebafb6f3766d7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/verdict-2.exit](../../skills/statechart/scripts/test/corpus/CounterTie/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterTie/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `bccbbf5d54a039d540712a11047e6a8d4ae168c1294e15de4f78e12e678ac7cd`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/verdict-3.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/verdict-3.exit](../../skills/statechart/scripts/test/corpus/CounterTie/verdict-3.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/verdict-3.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/verdict-3.out](../../skills/statechart/scripts/test/corpus/CounterTie/verdict-3.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f832750ac5552dbcc3515ec93ff959fd6f70e6462f590d7c1cd3493440f8c6f4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTie/verdict-4.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTie/verdict-4.out](../../skills/statechart/scripts/test/corpus/CounterTie/verdict-4.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `7589bdcdaf666e3b8f1df98ddd47034fe44450e0f9c00ea552c749c7544465a6`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4f0a042594b6b512195658761c84bf0054fa14fc6d52e72a78113a8230a28d93`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/CounterTieInGraph.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/CounterTieInGraph.cfg](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/CounterTieInGraph.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4a48e4418169113fdd2abb891981d4917fca6b76915e38f6bcddbc5596786195`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/CounterTieInGraph.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/CounterTieInGraph.tla](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/CounterTieInGraph.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `cf1818fc7d96bd4082f9260a42b7e792d5e6494ce7ae6c97730b63e8085e0ac0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2c3fb00ad851c1bab2516ce25838209c342cbc8c5d3d795a54bb6eac3ad5d0d0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/graph.dot](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ec76c05526f13d71d561cd67118da823cb0337af4f4d7b011d84f420aa8663ed`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/report.md](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `efb16c681db5ffef7312d550393bc62e1b3682615b06d8f2991fea29ba3938a8`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/sany.out](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `eb1991c5d584f35db0bcdb3ad4ab5444be5c84f324f177e51b95bb8b46f75324`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2cdd96422ac6aff9f266db7c2b644b02c047ce23ca85486cd5c62cb7b4f9253b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterTieInGraph/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterTieInGraph/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterTieInGraph/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `cc159ae8b3034dea7f055fe6290c0becfc8da8d879459b7ba0421fd57b750e53`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/CounterView/ChartRun.out](../../skills/statechart/scripts/test/corpus/CounterView/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1763153dd2d92f64250e983f283e622a7c7519aa21b5357c07f5931225039314`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/CounterView.cfg`

Destination: [skills/statechart/scripts/test/corpus/CounterView/CounterView.cfg](../../skills/statechart/scripts/test/corpus/CounterView/CounterView.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f7f1939032d3fb09af0d2e38907b2f8e3da73cd6f90769a801638c4c50f9ccdc`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/CounterView.tla`

Destination: [skills/statechart/scripts/test/corpus/CounterView/CounterView.tla](../../skills/statechart/scripts/test/corpus/CounterView/CounterView.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `273e549d576351809a2220003ae1b3c8cd2e687499be05fb21b3ce461d1b5162`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/CounterView/chart.mmd](../../skills/statechart/scripts/test/corpus/CounterView/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e6e0208a45a15a8af7be73b8e89ee665117414c3fc082679f35b250f2643cd05`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/CounterView/graph.dot](../../skills/statechart/scripts/test/corpus/CounterView/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `906fdbce95c4d0628441a231d9d9124d506d34f95ba08f653f3db084d13c5c1d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/report.md`

Destination: [skills/statechart/scripts/test/corpus/CounterView/report.md](../../skills/statechart/scripts/test/corpus/CounterView/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2a64bbb36844f44e97626e6c0579ba1aaa6fdaea99216b7322642ab07d1cbbb5`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/sany.out`

Destination: [skills/statechart/scripts/test/corpus/CounterView/sany.out](../../skills/statechart/scripts/test/corpus/CounterView/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1cd34d2d89ca38c44999e7376075047947927899d406c401c87308fd5ab203a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterView/verdict-1.exit](../../skills/statechart/scripts/test/corpus/CounterView/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/CounterView/verdict-1.out](../../skills/statechart/scripts/test/corpus/CounterView/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5981442a7a969e88a98934eb3244542f9c8ec99f73de9050280103f12cb0c4a2`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterView/verdict-2.exit](../../skills/statechart/scripts/test/corpus/CounterView/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/CounterView/verdict-2.out](../../skills/statechart/scripts/test/corpus/CounterView/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6237dc3d67262ecfac29bd09515e9fd81eb4c7b0340cf944fb841864c50687f0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/verdict-3.exit`

Destination: [skills/statechart/scripts/test/corpus/CounterView/verdict-3.exit](../../skills/statechart/scripts/test/corpus/CounterView/verdict-3.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/verdict-3.out`

Destination: [skills/statechart/scripts/test/corpus/CounterView/verdict-3.out](../../skills/statechart/scripts/test/corpus/CounterView/verdict-3.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `c72cdc09ad69e03d04f4ee840659aee046e0e6af39a9c839e6d8d20e3dd9762a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/verdict-4.out`

Destination: [skills/statechart/scripts/test/corpus/CounterView/verdict-4.out](../../skills/statechart/scripts/test/corpus/CounterView/verdict-4.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `27f4981b9ba54df20bc33114fea2e521cd5a476173eb307a7cf5ff4c8b3f2c91`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/CounterView/view.mjs`

Destination: [skills/statechart/scripts/test/corpus/CounterView/view.mjs](../../skills/statechart/scripts/test/corpus/CounterView/view.mjs).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5f6114fd8ca165604456048f2d7e2c29f667eb4537076647aaf3bb856f1c826e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/DieHard/ChartRun.out](../../skills/statechart/scripts/test/corpus/DieHard/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `dfd5fadfb9ea0030ecdf82c184268d09ce877336f19e3b9f2f3b95866099538a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/DieHard.cfg`

Destination: [skills/statechart/scripts/test/corpus/DieHard/DieHard.cfg](../../skills/statechart/scripts/test/corpus/DieHard/DieHard.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d75cf14954dfc65a36abbbbde7b6d52b77c4df36a4fdf64974acd51adfdd13f8`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/DieHard.tla`

Destination: [skills/statechart/scripts/test/corpus/DieHard/DieHard.tla](../../skills/statechart/scripts/test/corpus/DieHard/DieHard.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8a63111dc1aea97f4b32cc6fb7f36112775ef65b5a8a8603fbd35c493eba306d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/DieHard/chart.mmd](../../skills/statechart/scripts/test/corpus/DieHard/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `89057b576e59f437dd8c96a25edfd6891512d9b5788c5883e7d1affb6b5a9681`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/DieHard/graph.dot](../../skills/statechart/scripts/test/corpus/DieHard/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6cf64ad56b08000c6a3f05aecd54331b71192aca1de3d737afe24b157a06ee84`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/report.md`

Destination: [skills/statechart/scripts/test/corpus/DieHard/report.md](../../skills/statechart/scripts/test/corpus/DieHard/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `044c2a2b41ffe7f522af78b33f1c0fa09f822b42ae0913560db355e88b9cdb4d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/sany.out`

Destination: [skills/statechart/scripts/test/corpus/DieHard/sany.out](../../skills/statechart/scripts/test/corpus/DieHard/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `818c71c8a84a41a626740fcc61608ad77d45d8cea2175690163da289f1eda4bd`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/DieHard/verdict-1.exit](../../skills/statechart/scripts/test/corpus/DieHard/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/DieHard/verdict-1.out](../../skills/statechart/scripts/test/corpus/DieHard/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `24363932a41b49f302c1dd934c36d583e443850e3c34677a423aecf49fc9081e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/DieHard/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/DieHard/verdict-2.out](../../skills/statechart/scripts/test/corpus/DieHard/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `86b8e78b53127ebbfc013ad1423d4ca66c92d118685508dbf57307076d7cf9b5`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/ChartRun.out](../../skills/statechart/scripts/test/corpus/FirstRule/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6514873d106dda3ed051e38f2e7df8932c597c3d27e68538899ee9c2f70a9405`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/FirstRule.cfg`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/FirstRule.cfg](../../skills/statechart/scripts/test/corpus/FirstRule/FirstRule.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `422dbc8bd263458fb1706fdaa4888ca3375ca5db1394dcf6b5aaa6ad0645fede`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/FirstRule.tla`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/FirstRule.tla](../../skills/statechart/scripts/test/corpus/FirstRule/FirstRule.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9f1b2ddb4a573c4612cee6657f728117656a2dd1ab9e8e800e171ee1f3cbb1f4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/chart.mmd](../../skills/statechart/scripts/test/corpus/FirstRule/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `60b3c9d31e74b633d5d97a2847aab3bd3fb4f63813e8e0d8a3a493ff5dde1bc3`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/graph.dot](../../skills/statechart/scripts/test/corpus/FirstRule/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1b348348bf032ff81cfd796ae19f8cdcf491d5af18eab73ebfca3058a15691b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/report.md`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/report.md](../../skills/statechart/scripts/test/corpus/FirstRule/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2323122a1509c6c554a18da72a549922e364d2e89f0e5d274f1fa4b89f14c6e1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/sany.out`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/sany.out](../../skills/statechart/scripts/test/corpus/FirstRule/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `94176927597f47550c6ca1cd91807367a1e2ce968c1eceae20256d96cfba1139`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/verdict-1.exit](../../skills/statechart/scripts/test/corpus/FirstRule/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/verdict-1.out](../../skills/statechart/scripts/test/corpus/FirstRule/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f444852a2c5f029b3d76a3d1365763435e8cfeaeedab4769bf0d580dfd8a5f70`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/verdict-2.exit](../../skills/statechart/scripts/test/corpus/FirstRule/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/verdict-2.out](../../skills/statechart/scripts/test/corpus/FirstRule/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1c7209d668eeb0afccaed1e7a7dff0b4d813d4dca12a440e657a1cbf895a90cc`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/verdict-3.exit`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/verdict-3.exit](../../skills/statechart/scripts/test/corpus/FirstRule/verdict-3.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/verdict-3.out`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/verdict-3.out](../../skills/statechart/scripts/test/corpus/FirstRule/verdict-3.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3dd39a3d8eacf4e1770b22fd55bed88d03a01b44d7f592981e66279707bff3ee`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/verdict-4.exit`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/verdict-4.exit](../../skills/statechart/scripts/test/corpus/FirstRule/verdict-4.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `25d4f2a86deb5e2574bb3210b67bb24fcc4afb19f93a7b65a057daa874a9d18e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/FirstRule/verdict-4.out`

Destination: [skills/statechart/scripts/test/corpus/FirstRule/verdict-4.out](../../skills/statechart/scripts/test/corpus/FirstRule/verdict-4.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6a6efbdf26c39e43588e2c4662cefea87a869d3700096347e2064ff9db439002`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/HiddenClock/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/HiddenClock/ChartRun.out](../../skills/statechart/scripts/test/corpus/HiddenClock/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `263a6666f3bd0a91020bdc2e674285889db6160e62aeeabf81d3fd6c80ad5898`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/HiddenClock/HiddenClock.cfg`

Destination: [skills/statechart/scripts/test/corpus/HiddenClock/HiddenClock.cfg](../../skills/statechart/scripts/test/corpus/HiddenClock/HiddenClock.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1ff2a58417639cdb8fd7fe134d9acc49badc7ddefae309e8a49343550bb37dc7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/HiddenClock/HiddenClock.tla`

Destination: [skills/statechart/scripts/test/corpus/HiddenClock/HiddenClock.tla](../../skills/statechart/scripts/test/corpus/HiddenClock/HiddenClock.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1cdb3a20c553557f60fddc93d0c2a57dcd815f0028020a58110ff92ae5e6ef1b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/HiddenClock/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/HiddenClock/chart.mmd](../../skills/statechart/scripts/test/corpus/HiddenClock/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `7d29b01c2bc123ec82c9ccf12a082b2bd700afa6ae5f5e4451c08fba553b317f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/HiddenClock/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/HiddenClock/graph.dot](../../skills/statechart/scripts/test/corpus/HiddenClock/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `abfe48a392e3f5217684882942261deb1a117e63e3e3836f037a551019fff710`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/HiddenClock/report.md`

Destination: [skills/statechart/scripts/test/corpus/HiddenClock/report.md](../../skills/statechart/scripts/test/corpus/HiddenClock/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `bb7e070ee6e8b332ab4a4166c33989a5aa38bc0e0ecf75a93c8935d0680c8b82`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/HiddenClock/sany.out`

Destination: [skills/statechart/scripts/test/corpus/HiddenClock/sany.out](../../skills/statechart/scripts/test/corpus/HiddenClock/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `86bc954e5dffa1c9516ccb8064610f66668db25a34be69cc03bb4a5736c2a566`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/HiddenClock/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/HiddenClock/verdict-1.exit](../../skills/statechart/scripts/test/corpus/HiddenClock/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1a252402972f6057fa53cc172b52b9ffca698e18311facd0f3b06ecaaef79e17`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/HiddenClock/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/HiddenClock/verdict-1.out](../../skills/statechart/scripts/test/corpus/HiddenClock/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3719bbe9a22627acc9684a503de82250dba80ed9ce0859b1fb09b6d30db2553e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Login/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/Login/ChartRun.out](../../skills/statechart/scripts/test/corpus/Login/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `69e092decc546972f84ff731b24cb5d2f4d75eb373dbedde38b8aa136f2bfdb8`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Login/Login.cfg`

Destination: [skills/statechart/scripts/test/corpus/Login/Login.cfg](../../skills/statechart/scripts/test/corpus/Login/Login.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `97707bb4e8fb4a42465bade63b9be92dae0ebcc877530d588e5bdefb3687655e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Login/Login.tla`

Destination: [skills/statechart/scripts/test/corpus/Login/Login.tla](../../skills/statechart/scripts/test/corpus/Login/Login.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `25aa3c50791c7f24fe96243baeef4cc4281d9fa37f29abb78533862bd6b6e9de`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Login/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/Login/chart.mmd](../../skills/statechart/scripts/test/corpus/Login/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6cfda25977c467c106f9fb7f5602960bdd40919ac9294994ccd3bb33346faf35`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Login/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/Login/graph.dot](../../skills/statechart/scripts/test/corpus/Login/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f120b5583e931755578032d87cedf5bcadc4cb4c4ef497605b4290e1de704673`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Login/report.md`

Destination: [skills/statechart/scripts/test/corpus/Login/report.md](../../skills/statechart/scripts/test/corpus/Login/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e0132cf83d5637c96747873fa6ecdea23961b6b3b818e6db65748013580fe87d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Login/sany.out`

Destination: [skills/statechart/scripts/test/corpus/Login/sany.out](../../skills/statechart/scripts/test/corpus/Login/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e102731bbbf16d04bce331007e37f29c9f90e0f1371eb5a9cc88f65bc7d56979`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Login/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/Login/verdict-1.out](../../skills/statechart/scripts/test/corpus/Login/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `92ff242b55fc6763a13988a98481a54a1ab19eb3f0a4514d30efe3a48e45b581`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Login/view.mjs`

Destination: [skills/statechart/scripts/test/corpus/Login/view.mjs](../../skills/statechart/scripts/test/corpus/Login/view.mjs).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f59cef65025cb9aacade3fa5027c5cba15a44cabbfe64084f6dedcb173cf93e7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginGuarded/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/LoginGuarded/ChartRun.out](../../skills/statechart/scripts/test/corpus/LoginGuarded/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b9578b274bf3458ac3b721eca7638f48e97874a32765e0db95807cbb7f9609aa`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginGuarded/LoginGuarded.cfg`

Destination: [skills/statechart/scripts/test/corpus/LoginGuarded/LoginGuarded.cfg](../../skills/statechart/scripts/test/corpus/LoginGuarded/LoginGuarded.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `7877ce4ca1c561150cf6a447f61f273742f4b7112ed84f10e827b38f032ec6cd`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginGuarded/LoginGuarded.tla`

Destination: [skills/statechart/scripts/test/corpus/LoginGuarded/LoginGuarded.tla](../../skills/statechart/scripts/test/corpus/LoginGuarded/LoginGuarded.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `c62583af14b40df94a4276438edecfdf482d2b185eb6b302c3db2dfe71c129e1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginGuarded/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/LoginGuarded/chart.mmd](../../skills/statechart/scripts/test/corpus/LoginGuarded/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `298760e9f3334c9807f2c3698c1f487981e9cb67c2688e6d910a2904321383f8`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginGuarded/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/LoginGuarded/graph.dot](../../skills/statechart/scripts/test/corpus/LoginGuarded/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3e2ffcda3ccb6fa266b13f6f19d18d81d819f9e0e9809e91868edf77d9663237`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginGuarded/report.md`

Destination: [skills/statechart/scripts/test/corpus/LoginGuarded/report.md](../../skills/statechart/scripts/test/corpus/LoginGuarded/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6476c58f4938e059179774f90a7cd1829b2c7c38903223c81a193034ebae83db`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginGuarded/sany.out`

Destination: [skills/statechart/scripts/test/corpus/LoginGuarded/sany.out](../../skills/statechart/scripts/test/corpus/LoginGuarded/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e8e73f621775ea526e48dc565b3cc0010a22a90ca075e0fb0ca2f73c0522840f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginGuarded/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/LoginGuarded/verdict-1.out](../../skills/statechart/scripts/test/corpus/LoginGuarded/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `46b5c3b2cdbf05571417d8aff407d103d0d4755e8e8c0ba46186391a611a6364`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginGuarded/view.mjs`

Destination: [skills/statechart/scripts/test/corpus/LoginGuarded/view.mjs](../../skills/statechart/scripts/test/corpus/LoginGuarded/view.mjs).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9a45c5718c3eb1171b0a2271e79612e6af833038f13ab8e16b37f15947d53cca`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/ChartRun.out](../../skills/statechart/scripts/test/corpus/LoginParallel/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2dda75ca79ff432a8f74fa504c8876f01441f8196b274f4f834959c49576c87b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/LoginParallel.cfg`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/LoginParallel.cfg](../../skills/statechart/scripts/test/corpus/LoginParallel/LoginParallel.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ab2bc033be4345d363d5845fb6bf573c4b79b477bdee965625e2a4af44fd9c44`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/LoginParallel.tla`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/LoginParallel.tla](../../skills/statechart/scripts/test/corpus/LoginParallel/LoginParallel.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8f93509fca05425c054e7ec518e9653097ac9464c98fbf426fee551f940b2e51`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/chart.mmd](../../skills/statechart/scripts/test/corpus/LoginParallel/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d00f84c57486de54bde56ee75ad223e6936bd1b0334319cef60ebbee899a2480`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/graph.dot](../../skills/statechart/scripts/test/corpus/LoginParallel/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8f4d20009e23824b0bfbeddd2ca9d1c12e764599a7e179018c98d432d091ab86`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/report.md`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/report.md](../../skills/statechart/scripts/test/corpus/LoginParallel/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ed54afd8a979fb2c7eedf28b0bbdd1bfc91b360d883eacd8254483f1db5155d0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/sany.out`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/sany.out](../../skills/statechart/scripts/test/corpus/LoginParallel/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9906450ef11cc5c94325cef0b648736135708d37ee3a41841b55035f41e43309`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/verdict-1.exit](../../skills/statechart/scripts/test/corpus/LoginParallel/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/verdict-1.out](../../skills/statechart/scripts/test/corpus/LoginParallel/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `dcfd62876aa6e62fd08d8dad9b38a5f54ec86725f92c48e8328ac0461dd4be67`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/verdict-2.out](../../skills/statechart/scripts/test/corpus/LoginParallel/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `bad6cc9bf2bce357642aba04e7fd952800b718e7a518b9679764a4058465d1d0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/LoginParallel/view.mjs`

Destination: [skills/statechart/scripts/test/corpus/LoginParallel/view.mjs](../../skills/statechart/scripts/test/corpus/LoginParallel/view.mjs).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9a45c5718c3eb1171b0a2271e79612e6af833038f13ab8e16b37f15947d53cca`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/ChartRun.out](../../skills/statechart/scripts/test/corpus/MediaPlayer/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2460f0f517117836b5a02e70e4ef2f9889061f1b2cb83ac4bf8fc41532fa2b1d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/MediaPlayer.cfg`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/MediaPlayer.cfg](../../skills/statechart/scripts/test/corpus/MediaPlayer/MediaPlayer.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0f1a86e105cf1c303cedc510b4fe080175fc77eb88fe98c1eba163d04436ffad`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/MediaPlayer.tla`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/MediaPlayer.tla](../../skills/statechart/scripts/test/corpus/MediaPlayer/MediaPlayer.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ace4961900ceb44281c94879c05550123a74c5427e9fcfaf3dfb134f51c38390`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/chart.mmd](../../skills/statechart/scripts/test/corpus/MediaPlayer/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e3a6e6987bd8c6aa9fcc480a5f19e1c8c954804935f2d5f938279e6e7c2f6ceb`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/graph.dot](../../skills/statechart/scripts/test/corpus/MediaPlayer/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `881d999fa6e60ba7698ea8633f16a315be97a370aa300cdea885d04333028534`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/report.md`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/report.md](../../skills/statechart/scripts/test/corpus/MediaPlayer/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ef407dcd4e536034ec7512076364831c7f904912cba5ed6f53659db02e13d82a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/sany.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/sany.out](../../skills/statechart/scripts/test/corpus/MediaPlayer/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6385013e3e792b0404acc8ae8c42718fba4a626ff83590bb680318c08d497e88`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/verdict-1.exit](../../skills/statechart/scripts/test/corpus/MediaPlayer/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/verdict-1.out](../../skills/statechart/scripts/test/corpus/MediaPlayer/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b6f6af48489b17cc9d21ccaf851a555ec8e51d29bc76486b11801b4ae1c11b86`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/verdict-2.out](../../skills/statechart/scripts/test/corpus/MediaPlayer/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d9eaa58bbc7364560b1365ef1fe74454ab97ca093cbf05a9bb14d530145165cf`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayer/view.mjs`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayer/view.mjs](../../skills/statechart/scripts/test/corpus/MediaPlayer/view.mjs).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `019383f6b4f753b5721485f3cff9b3762e046f4cea134f26a709e9ce4c43dde9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerFixed/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerFixed/ChartRun.out](../../skills/statechart/scripts/test/corpus/MediaPlayerFixed/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1050612e030b11a1f6e1942880bfcfb634913e0123fe04133e38554553cb79f6`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerFixed/MediaPlayerFixed.cfg`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerFixed/MediaPlayerFixed.cfg](../../skills/statechart/scripts/test/corpus/MediaPlayerFixed/MediaPlayerFixed.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2d6715915152436fc1016313ef8dd55251c0f712417226c47345228527acff83`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerFixed/MediaPlayerFixed.tla`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerFixed/MediaPlayerFixed.tla](../../skills/statechart/scripts/test/corpus/MediaPlayerFixed/MediaPlayerFixed.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `59c4c86bfa1f38e0a01e8675d9936558d9a3899c3de8243483e633674a6bccfc`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerFixed/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerFixed/chart.mmd](../../skills/statechart/scripts/test/corpus/MediaPlayerFixed/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1a77aeca211f5469041f03c6d149beec17f300d6cb5e5386e5f73d6a214f73ae`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerFixed/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerFixed/graph.dot](../../skills/statechart/scripts/test/corpus/MediaPlayerFixed/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `cb6b2d85fb70cfa6aefe16e3fdcb686b60f6593ec755e04ed5c4ec15867766f7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerFixed/report.md`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerFixed/report.md](../../skills/statechart/scripts/test/corpus/MediaPlayerFixed/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ea569763d18889ff07c5be90ac6fb74ca83f4a19f1ba79000fa151c692d38d54`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerFixed/sany.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerFixed/sany.out](../../skills/statechart/scripts/test/corpus/MediaPlayerFixed/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `22f3486dbbfc11c5ae0f62e25aab9742b0875285c5de8e490f5cd84b1b948bf0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerFixed/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerFixed/verdict-1.out](../../skills/statechart/scripts/test/corpus/MediaPlayerFixed/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `442c9923009f88f8f462a2bb4533987b6797495bdfee359a74c49b1a360fe386`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerFixed/view.mjs`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerFixed/view.mjs](../../skills/statechart/scripts/test/corpus/MediaPlayerFixed/view.mjs).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `019383f6b4f753b5721485f3cff9b3762e046f4cea134f26a709e9ce4c43dde9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/ChartRun.out](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4a67e04e5c801f92ce4a9fe7bf48fdc3a800abe6754d75c0df2ac0f7fa85af68`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/MediaPlayer.tla`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/MediaPlayer.tla](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/MediaPlayer.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ace4961900ceb44281c94879c05550123a74c5427e9fcfaf3dfb134f51c38390`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/MediaPlayerProps.cfg`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/MediaPlayerProps.cfg](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/MediaPlayerProps.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d9995ff6b04506d0531f7264a85c932fe0e4ea2017608952d6908ef9ed31f828`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/MediaPlayerProps.tla`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/MediaPlayerProps.tla](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/MediaPlayerProps.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `31f510c61062eaede29be56efd920aa0cfdb9851e09cdbb0c971468c48e54985`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/chart.mmd](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `40e8330310aa4ec838ad4bf99b12e5eb0ddc7b6ec99bf21d764c05ab05217d9b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/graph.dot](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `881d999fa6e60ba7698ea8633f16a315be97a370aa300cdea885d04333028534`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/report.md`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/report.md](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5a68beff9cbd182489e784b065f588a48ec61c60f87ed70dafe80ee0fde56ef3`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/sany.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/sany.out](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `dc86d7c73175b68cf92d65d35758da6836a38e0ef3d5dba209c80b90df6a53d4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-1.exit](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-1.out](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `364c7dfbf9cabaea6f15e96811df209ee272800f5d5b671ce27532346dc3215d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-2.out](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e01f79327c1e8a2978629ad8e5486baf95dfb0dd4ffd44152b159b8d35fb0bc9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-3.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-3.out](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-3.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8f9d8deff62a9625782caff95aa89f03607aa50bd31f31b5d26f459c04757f09`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-4.exit`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-4.exit](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-4.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1a252402972f6057fa53cc172b52b9ffca698e18311facd0f3b06ecaaef79e17`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-4.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-4.out](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-4.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `04579153733514c4c7bb351a04764e1a9dc5f6815b7dc056fb51ee0dec5ef48a`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-5.exit`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-5.exit](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-5.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-5.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-5.out](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-5.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `274b0b70a9e7cf8d6c140a968b8674be5fe8073252db78ec6b823cc7f40f7538`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-6.out`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-6.out](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/verdict-6.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8f03e3f3afb0378a13715c9f90a3b59c1f46a53f295f8eb74f1b61c62d832a43`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/MediaPlayerProps/view.mjs`

Destination: [skills/statechart/scripts/test/corpus/MediaPlayerProps/view.mjs](../../skills/statechart/scripts/test/corpus/MediaPlayerProps/view.mjs).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `019383f6b4f753b5721485f3cff9b3762e046f4cea134f26a709e9ce4c43dde9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/PickWorker/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/PickWorker/ChartRun.out](../../skills/statechart/scripts/test/corpus/PickWorker/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `caeb61ac10b01bf2e6044cebd316b599793eb075fb0256aa81c696e4e5c7a7ce`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/PickWorker/PickWorker.cfg`

Destination: [skills/statechart/scripts/test/corpus/PickWorker/PickWorker.cfg](../../skills/statechart/scripts/test/corpus/PickWorker/PickWorker.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0da0617d4459668020b0bf88a29b1eee01882c88f204728eb9a38493b60bd4b3`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/PickWorker/PickWorker.tla`

Destination: [skills/statechart/scripts/test/corpus/PickWorker/PickWorker.tla](../../skills/statechart/scripts/test/corpus/PickWorker/PickWorker.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8cd92057affd06b367a85c1d87c81b827cfdfd41a2bea10989ce911ed2fd3124`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/PickWorker/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/PickWorker/chart.mmd](../../skills/statechart/scripts/test/corpus/PickWorker/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5fff795e5d0da737cdf1fef95c993ea6ca45fd9f5fb61e163d2e292c40186a64`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/PickWorker/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/PickWorker/graph.dot](../../skills/statechart/scripts/test/corpus/PickWorker/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1d60f0497f939134c6cb91f5e869445aa7da04ba8caad5128f1509a28c31f245`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/PickWorker/report.md`

Destination: [skills/statechart/scripts/test/corpus/PickWorker/report.md](../../skills/statechart/scripts/test/corpus/PickWorker/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `87546454dfa4b96d15c53dbdc6eef469e0390f14b4ff1eb370d4437508f90da8`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/PickWorker/sany.out`

Destination: [skills/statechart/scripts/test/corpus/PickWorker/sany.out](../../skills/statechart/scripts/test/corpus/PickWorker/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `866b218db376118471b5635ad1b050c14552c1cc7df37d65f9a5ce5b4734dbaf`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/PickWorker/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/PickWorker/verdict-1.out](../../skills/statechart/scripts/test/corpus/PickWorker/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e994e9457f86627fe3db72c80f63513931b75d192b3387b2ef6132c398780b55`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/Shadow/ChartRun.out](../../skills/statechart/scripts/test/corpus/Shadow/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e01704359d955974f20afee7ea1d5f4f120a5319c219929d747c9e9bc2c9b36d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/Shadow.cfg`

Destination: [skills/statechart/scripts/test/corpus/Shadow/Shadow.cfg](../../skills/statechart/scripts/test/corpus/Shadow/Shadow.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4f0262dfe7368f4c8df45c47e912fca78885a24053b31cd67c3b33f49e61f7a1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/Shadow.tla`

Destination: [skills/statechart/scripts/test/corpus/Shadow/Shadow.tla](../../skills/statechart/scripts/test/corpus/Shadow/Shadow.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `c7ed4c7ab82d7ed8515621d4ff88d349920cd1a4783a2ee47a71278af9dfe148`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/ShadowLib.tla`

Destination: [skills/statechart/scripts/test/corpus/Shadow/ShadowLib.tla](../../skills/statechart/scripts/test/corpus/Shadow/ShadowLib.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3590a4185a432b4fbaa867d7d717482a0d57e2374711bf3bb65244cc936bc666`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/ShadowSub.tla`

Destination: [skills/statechart/scripts/test/corpus/Shadow/ShadowSub.tla](../../skills/statechart/scripts/test/corpus/Shadow/ShadowSub.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b84408d4b14dc56402b7cc8e0e11589f8b0f7bb3dc3f1408afcc7518f3fb7f1f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/Shadow/chart.mmd](../../skills/statechart/scripts/test/corpus/Shadow/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `386fbbc905c7c89c4457a3d48f4b76bdf42861093188dc7369c32aef7b48658c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/Shadow/graph.dot](../../skills/statechart/scripts/test/corpus/Shadow/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1b348348bf032ff81cfd796ae19f8cdcf491d5af18eab73ebfca3058a15691b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/report.md`

Destination: [skills/statechart/scripts/test/corpus/Shadow/report.md](../../skills/statechart/scripts/test/corpus/Shadow/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `16788146e79b669a06152e69fbb0b3ef738bab2bd37c6c278137e7b96373dd97`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/sany.out`

Destination: [skills/statechart/scripts/test/corpus/Shadow/sany.out](../../skills/statechart/scripts/test/corpus/Shadow/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e7396792c0a425651e9765498b6922a95fa63c37d3fa9927137b3c35596eb310`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/Shadow/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/Shadow/verdict-1.out](../../skills/statechart/scripts/test/corpus/Shadow/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b6df6a9904d6b1fbe9fb20ae1d7f2e52aded6a7884e6e2514db4e984d6d2c4b9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/ChartRun.out](../../skills/statechart/scripts/test/corpus/SpacedNames/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `68bb08c06e2c22ec57dd84e595c2895f01bf6c7be3cadb8ae3a942c662888f0c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/SpacedNames.cfg`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/SpacedNames.cfg](../../skills/statechart/scripts/test/corpus/SpacedNames/SpacedNames.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e32044a2d32c9e2c9c9459b257ff062bd33028914d392b0ec1d25815772dfbfa`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/SpacedNames.tla`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/SpacedNames.tla](../../skills/statechart/scripts/test/corpus/SpacedNames/SpacedNames.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0685a3f78ae2d30bc883201b3c9fc16f9f590b15d02a62295da3cc48566d777b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/chart.mmd](../../skills/statechart/scripts/test/corpus/SpacedNames/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `de161c72bdfa1feff2ccbebbc39db5fee3bd4b1d789945802b310838875a2bf1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/graph.dot](../../skills/statechart/scripts/test/corpus/SpacedNames/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1f9e6cbdfd8b30ca4ec376261e8fb6114a7efe4ef1a5ec01ebeeaaddcabce211`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/report.md`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/report.md](../../skills/statechart/scripts/test/corpus/SpacedNames/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `62126c7b8928173a53952a5372c703b6c6af5155331f6b8547b21e957319540d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/sany.out`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/sany.out](../../skills/statechart/scripts/test/corpus/SpacedNames/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `415faa44484371020747737d57b69bec28640dce60adf5cbeac26d0a79f89953`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/verdict-1.exit](../../skills/statechart/scripts/test/corpus/SpacedNames/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/verdict-1.out](../../skills/statechart/scripts/test/corpus/SpacedNames/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `05335eac8e0ae5eeda209c59bf7b000c411592022f9afd452847b1d6688319d6`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/verdict-2.exit](../../skills/statechart/scripts/test/corpus/SpacedNames/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `25d4f2a86deb5e2574bb3210b67bb24fcc4afb19f93a7b65a057daa874a9d18e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/SpacedNames/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/SpacedNames/verdict-2.out](../../skills/statechart/scripts/test/corpus/SpacedNames/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `abf2a12c671af7ef26fb4a0a0f59accff35b36251c278bdde7067f00558f7e5c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/ChartRun.out](../../skills/statechart/scripts/test/corpus/TwoPhase/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `aed20dee26285d007a0529727c67ff86d52c1eaa3e1ea4c56472df4f2c5b1b92`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/TwoPhase.cfg`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/TwoPhase.cfg](../../skills/statechart/scripts/test/corpus/TwoPhase/TwoPhase.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a4e4546592e8e5d361ccbeb4808338e15fb61338fdbc84c358e9b0a41a58a704`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/TwoPhase.tla`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/TwoPhase.tla](../../skills/statechart/scripts/test/corpus/TwoPhase/TwoPhase.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `c27868893c2f4de82a0c561af6fc65d2abe233e840d9a2d830920d1487ab793d`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/chart.mmd](../../skills/statechart/scripts/test/corpus/TwoPhase/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e8761c527163b1d15d699da7f7e026337c939e51b2f82feea82a93ce1d67482c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/graph.dot](../../skills/statechart/scripts/test/corpus/TwoPhase/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0276d507b1457de02d25cacced67c19b3442764225bc183e90c8c6745ba5f680`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/report.md`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/report.md](../../skills/statechart/scripts/test/corpus/TwoPhase/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6b847fe8dc3e043d17c1ec3df7b18c7d618a1b7a351eb8f1943fa5d70a1b640b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/sany.out`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/sany.out](../../skills/statechart/scripts/test/corpus/TwoPhase/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3944566b6d4e0b3457c9b30320041e19e97d45f40a01b9a868ddeb9d7ad6304e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/verdict-1.exit](../../skills/statechart/scripts/test/corpus/TwoPhase/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/verdict-1.out](../../skills/statechart/scripts/test/corpus/TwoPhase/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f22ad5c0f211bf7ad01aa04bd2f461c9e48ed394d1814a7445b990c0f91eec75`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/verdict-2.out](../../skills/statechart/scripts/test/corpus/TwoPhase/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `bd8a217318a09cd985601e9483dcc061d502348cfc3e33a684ed35240b7cb5ba`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhase/view.mjs`

Destination: [skills/statechart/scripts/test/corpus/TwoPhase/view.mjs](../../skills/statechart/scripts/test/corpus/TwoPhase/view.mjs).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `25bc78b0ee8c7ab24ed1f0dbe78ed60adce0f086579c03bf8c97d02c448c7f26`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhaseFixed/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/TwoPhaseFixed/ChartRun.out](../../skills/statechart/scripts/test/corpus/TwoPhaseFixed/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `73094c6a6b78588569eef707f88ce7d6f7da4505a4882a2ff0cc1dcffc72b0f0`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhaseFixed/TwoPhaseFixed.cfg`

Destination: [skills/statechart/scripts/test/corpus/TwoPhaseFixed/TwoPhaseFixed.cfg](../../skills/statechart/scripts/test/corpus/TwoPhaseFixed/TwoPhaseFixed.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a4e4546592e8e5d361ccbeb4808338e15fb61338fdbc84c358e9b0a41a58a704`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhaseFixed/TwoPhaseFixed.tla`

Destination: [skills/statechart/scripts/test/corpus/TwoPhaseFixed/TwoPhaseFixed.tla](../../skills/statechart/scripts/test/corpus/TwoPhaseFixed/TwoPhaseFixed.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9d9459496de208594596804e0a70faad6390286c7b3fc2b9ae173e61d25ade57`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhaseFixed/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/TwoPhaseFixed/chart.mmd](../../skills/statechart/scripts/test/corpus/TwoPhaseFixed/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d7a0b12bfc62b60507334c045369ef53bbeba7e432f0c335a5c0a72e0b667fe7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhaseFixed/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/TwoPhaseFixed/graph.dot](../../skills/statechart/scripts/test/corpus/TwoPhaseFixed/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2a9a55c417ecf703035dce21c7ba347ad6cb3dc50a0a634a6b60f4bfb727a773`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhaseFixed/report.md`

Destination: [skills/statechart/scripts/test/corpus/TwoPhaseFixed/report.md](../../skills/statechart/scripts/test/corpus/TwoPhaseFixed/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `598a1594b7768b770d1c4df3b304ac26c2890bbf5bc9610541c5dcbd26c12d9f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhaseFixed/sany.out`

Destination: [skills/statechart/scripts/test/corpus/TwoPhaseFixed/sany.out](../../skills/statechart/scripts/test/corpus/TwoPhaseFixed/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2eb698b9b60b3ec587f382e5a6398b32da62e08e9803e1121e627a697bfaf061`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhaseFixed/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/TwoPhaseFixed/verdict-1.out](../../skills/statechart/scripts/test/corpus/TwoPhaseFixed/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a85d46fa117924eec003fe28749f71bee520016d65e3d4cad671768635157600`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TwoPhaseFixed/view.mjs`

Destination: [skills/statechart/scripts/test/corpus/TwoPhaseFixed/view.mjs](../../skills/statechart/scripts/test/corpus/TwoPhaseFixed/view.mjs).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `25bc78b0ee8c7ab24ed1f0dbe78ed60adce0f086579c03bf8c97d02c448c7f26`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/ChartRun.exit`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/ChartRun.exit](../../skills/statechart/scripts/test/corpus/TypeGuard/ChartRun.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `461144ccfd56ee3cf0f9a9d80e520c5b872166b23092d5fd838ecbdb46d64dab`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/ChartRun.out](../../skills/statechart/scripts/test/corpus/TypeGuard/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d3a2f8df56c31c081e5c0b27da754180cdb5b2a62073467421a90fc8514c4a08`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/TypeGuard.cfg`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/TypeGuard.cfg](../../skills/statechart/scripts/test/corpus/TypeGuard/TypeGuard.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ddd3b43e9455ebfe7ed7c487867352b9466bf60fb35900b84ad5281fe6763766`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/TypeGuard.tla`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/TypeGuard.tla](../../skills/statechart/scripts/test/corpus/TypeGuard/TypeGuard.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `ccda004cd0e3c40a7c39c200095a12eb3e0cc7c40f9ecabff24026c1cdfc53b4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/chart.mmd](../../skills/statechart/scripts/test/corpus/TypeGuard/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e180050487251de907e1a25c34a3acf28159d28a3166afd0786c7f8bd1bb52d5`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/graph.dot](../../skills/statechart/scripts/test/corpus/TypeGuard/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a35107023f5a7a2e9833c3c0f67b69e163a7331038510b3dafcd4f4092db7251`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/report.md`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/report.md](../../skills/statechart/scripts/test/corpus/TypeGuard/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4c954c446383fcaad78deb5ac19f70fa74fc028f90b576f1d91b2c45e09e0108`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/sany.out`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/sany.out](../../skills/statechart/scripts/test/corpus/TypeGuard/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `cf58712d31a0daab97eb960e7820c7b0c4326dfe785937eef9f7ed2476347ee3`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/verdict-1.exit](../../skills/statechart/scripts/test/corpus/TypeGuard/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/verdict-1.out](../../skills/statechart/scripts/test/corpus/TypeGuard/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `3e60feb2884f636dd1ea5cd1459fcef8a1db34e5f9f801ccfe6735203969ec84`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/verdict-2.exit](../../skills/statechart/scripts/test/corpus/TypeGuard/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `461144ccfd56ee3cf0f9a9d80e520c5b872166b23092d5fd838ecbdb46d64dab`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/TypeGuard/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/TypeGuard/verdict-2.out](../../skills/statechart/scripts/test/corpus/TypeGuard/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4ff80d714ae9e9ac57e54645b92aaac286ded5b5ce119b8d25c54ec53856bbc4`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/ChartRun.out`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/ChartRun.out](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/ChartRun.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `acd62745ae91ce9250ed32bb84a084f7a7327232f0e96a599eb49ed4f74c2388`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/UserNoDeadlock.cfg`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/UserNoDeadlock.cfg](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/UserNoDeadlock.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `2cf30ce46c41f9d6978b8080f2e0cdd627e0b034e367f98b351882fb0277b748`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/UserNoDeadlock.tla`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/UserNoDeadlock.tla](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/UserNoDeadlock.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b4ebd22cce4480f25812ea31f67447df520fb554ed9bd0114641c261f4e2b804`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/chart.mmd`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/chart.mmd](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/chart.mmd).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `730f79185a86f0345440cfbbcd05eb4b6b9b6e4653e00073708432e341c5fea7`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/graph.dot`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/graph.dot](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/graph.dot).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1b348348bf032ff81cfd796ae19f8cdcf491d5af18eab73ebfca3058a15691b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/report.md`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/report.md](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/report.md).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `53433b379971530176a5e150a14c466c4452d07c523b3207e8b6c2b55c68b0cf`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/sany.out`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/sany.out](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `b11bbc9d4985f64b11b09f48029c1c6a84089835cebf4211a56ee6e70e4c226c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-1.exit`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-1.exit](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-1.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `a1fb50e6c86fae1679ef3351296fd6713411a08cf8dd1790a4fd05fae8688164`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-1.out`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-1.out](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-1.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f014279be781ee6e9daebaccdea137b13b21f563b1ca5107bd1172d29c3a0884`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-2.exit`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-2.exit](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-2.exit).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `25d4f2a86deb5e2574bb3210b67bb24fcc4afb19f93a7b65a057daa874a9d18e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-2.out`

Destination: [skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-2.out](../../skills/statechart/scripts/test/corpus/UserNoDeadlock/verdict-2.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `cd7c28af45d5bc12ba9e0f148e25b5234b781bbb21ddb0194d5cd1b661c7b800`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/differential.test.ts`

Destination: [skills/statechart/scripts/test/differential.test.ts](../../skills/statechart/scripts/test/differential.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `d4d64a7d17b4630616e797f1b184848c2a8b7712777d9982cafee81dc6046a9f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/grid/Grid.cfg`

Destination: [skills/statechart/scripts/test/grid/Grid.cfg](../../skills/statechart/scripts/test/grid/Grid.cfg).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `41d15a4d5bef6385c00b30f2126204e74a779d835d37f1ea73669afcfb579ef5`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/grid/Grid.tla`

Destination: [skills/statechart/scripts/test/grid/Grid.tla](../../skills/statechart/scripts/test/grid/Grid.tla).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e52e75d6fccff01cfe385140cbac3339b5820faeb1e567c7edc1267fa99f989e`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/grid/sany.out`

Destination: [skills/statechart/scripts/test/grid/sany.out](../../skills/statechart/scripts/test/grid/sany.out).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e42a575f90275de315767d9f46ab0881349ebc53206e191aee57501494a5aba9`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/java.ts`

Destination: [skills/statechart/scripts/test/java.ts](../../skills/statechart/scripts/test/java.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `4fef906fe1dcfdb98dafbd3ecdae1e82589908529ffc11b6bbdcfb8aef505932`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/labels.ts`

Destination: [skills/statechart/scripts/test/labels.ts](../../skills/statechart/scripts/test/labels.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `5a884161428fc00229d9a0e896001df4b262b56a441b6b3d66d1b59b06050650`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/messages.test.ts`

Destination: [skills/statechart/scripts/test/messages.test.ts](../../skills/statechart/scripts/test/messages.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `e7ca0ea446907074452df5388719598bb297d7f8ee50145b8b8f2a41c0c4c92f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/pipeline.test.ts`

Destination: [skills/statechart/scripts/test/pipeline.test.ts](../../skills/statechart/scripts/test/pipeline.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `0f091c3e6e104fd545e113ad437df8d4856618a775073a37d41050ebf663e479`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/plain-tlc.test.ts`

Destination: [skills/statechart/scripts/test/plain-tlc.test.ts](../../skills/statechart/scripts/test/plain-tlc.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `f6b042300e66840809e26ba8fef0c7e2bc8bb6b59f3b910ea65dea176e97bf1c`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/render.test.ts`

Destination: [skills/statechart/scripts/test/render.test.ts](../../skills/statechart/scripts/test/render.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `9cb369e5f4c464ca540ccc3de4fdd76670b84e54f06955ccb46908826579ac23`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/tlc-out.test.ts`

Destination: [skills/statechart/scripts/test/tlc-out.test.ts](../../skills/statechart/scripts/test/tlc-out.test.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `8a87d6cf32e7225aa0c8031e61b8a2912d8fbb3847a7ec2cd76e26c14e931478`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/test/tlc.ts`

Destination: [skills/statechart/scripts/test/tlc.ts](../../skills/statechart/scripts/test/tlc.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `73f5cf9dca5ca55aa65d5b342405e31f6eff858ed2bc2124c3e3fbb328259cca`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/tsconfig.json`

Destination: [skills/statechart/scripts/tsconfig.json](../../skills/statechart/scripts/tsconfig.json).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `6bb2af53f7b251328e6117cd4fb761468dc4d4b96085d31a19304ccb73c32cc1`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.

### `skills/statechart/scripts/worker.ts`

Destination: [skills/statechart/scripts/worker.ts](../../skills/statechart/scripts/worker.ts).

Upstream commit: `c742dd61706fbacc1b95f1a20b7b988cf096ce6c`. SHA-256: `1f18ed5ef806982e05e8a40fc217e88257700b28b63cb4acbd647872f85f782b`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
