# Personal ChatGPT setup

Starting state for `chatgpt-setup-from-readme` is an ordinary personal ChatGPT conversation with no observed pstack loading. The personal route is unsupported here and explicitly blocked. Do not turn a local filesystem path into a universal ChatGPT installation step.

Official guidance describes packaging a skills-only plugin, installing it from a local source and testing in a new enabled conversation. It does not establish that this personal conversation exposes that route. Checked 2026-10-08. [Official complete-plugin testing](https://developers.openai.com/plugins/deploy/connect-chatgpt).

1. From [README](../../README.md), open this guide and [compatibility](../compatibility.md). Inspect actual plugin controls and tools read-only.
2. Record missing or denied loading and discovery operations. Stop the setup branch if the route is absent, or if installation, enabling or settings are not explicitly authorized. Do not add an MCP service to make this skills-only package appear supported.
3. For an authorized explanation, supply the exact relevant skill and its required references in the conversation. Follow [workflow selection](../workflows/choosing-a-workflow.md). Label this supplied-source use reduced capability. It is not installed package discovery, persistent activation, independent execution or a host pass.
4. If a supported route is later exposed and separately authorized, use the actual host controls and a fresh chat. Record `discover-package`, `enumerate-skills` and `inspect-installed-copy` with observed tool identifiers and artifact evidence. Require all 54 root names, exact installed-copy identity, package version and final frozen SHA, plus the three canonical nested Benny exclusions. Read [inventory](../parity/inventory.json) and [catalog](../skills/README.md) as comparison data only.
5. Run the [six walkthrough cases](../parity/cases/documentation-walkthroughs.json) and record actual outputs under the [host contract](../../references/host-capabilities.md). Workers, execution, persistence, models and integrations need separate exposed and successful bindings. A conversation without them leaves dependent gates blocked.

Expected visible result today is an explicit setup/discovery block and a bounded explanation if source is supplied. A future complete installed receipt can change that status only after fresh observations. The [Codex guide](codex.md) describes a different documented route. Its local path and cache rules do not establish personal ChatGPT support.

[Optional development dependencies](../testing/helper-setup.md) are separate from host installation. No generic setup permission follows from their historical snapshot approval. Refresh or removal requires an observed host control and exact authorization; neither source edits nor removing supplied text proves uninstall.
