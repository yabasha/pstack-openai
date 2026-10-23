# make-bot-ui

Generated from the reviewed catalog record. Regenerate with `python3 -B tools/build_catalog.py --root .`.

Catalog record: [docs/catalog/skills/make-bot-ui.json](../catalog/skills/make-bot-ui.json).

Skill: [skills/make-bot-ui/SKILL.md](../../skills/make-bot-ui/SKILL.md). Kind: skill.

## Purpose

Build a custom page whose local server wakes a bot routine over a webhook and optionally serves it on Tailscale.

## Triggers

- Make Bot UI or make-bot-ui invocation.
- Build a page, dashboard or buttons for a Grok Bot webhook.
- Securely provide a webhook sender key or expose the UI on Tailscale.

## Required input

- Explicit webhook provider, routine URL and agreed JSON fields.
- Secure secret submission and server-side retrieval channel.
- Authorized local execution and network setup.

## Output contract

- Local UI and server-side webhook protocol.
- Observed routine setup, harmless probe result and verified tailnet URLs when authorized and supported.
- Explicit execution block and setup checklist when capabilities are missing.

## Ordinary example

Design buttons that POST an agreed action to a local server, which wakes the configured bot routine without exposing its sender key.

The linked cases define acceptance observations. Their prompts and expected results are not execution evidence.

### Case [missing-webhook](../parity/cases/skills/make-bot-ui.json)

Build a custom page with buttons that wake a Grok Bot over a webhook and expose it on Tailscale. No webhook provider, secure secret channel, or network setup is available. Do not request a sender key in chat.

Full capability expectation:

With all capabilities explicitly configured and authorized, create or inspect the routine, use its actual URL and secure sender key, proxy one JSON object from the local server with both authorization headers, an eight-second timeout and no retry, probe a harmless ignored action, and verify both tailnet URLs before claiming live operation.

Reduced capability expectation:

Prepare a local UI design, field contract and setup checklist without starting a listener, creating a routine, retrieving credentials or sending network requests. Execution remains blocked until setup is available.

Blocked capability expectation:

Name the missing provider, secure secret channel and network setup. Block webhook execution and live UI claims. Never require these credentials for any other skill.

Required observations:

- An explicitly authorized webhook provider and observed routine creation or existing routine URL.
- A secure secret submission and server-side retrieval channel that never exposes the sender key.
- Authorized local server execution, outbound webhook requests and tailnet setup.

Forbidden claims:

- Invented provider APIs, routine URL, secret storage path or tailnet hostname.
- Sender keys pasted into chat, browser code, output or logs.
- Installation, network writes, routine creation or messages without explicit authorization.
- Live operation or host parity from static review.
- Mandatory webhook credentials for other skills.

## Dependencies

- [references/host-capabilities.md](../../references/host-capabilities.md)
- [references/workflow-ownership.md](../../references/workflow-ownership.md)

## Host limits

- Missing provider, secure secret channel or network setup blocks execution.
- No credentials are mandatory for any other skill.
- Routine creation, installation, enrollment, listener exposure and network requests need explicit authorization.
- Canonical provider API and interface names describe source behavior; current host bindings require discovery.
- Host behavior is not-run; structural validation supplies no live-operation evidence.

## Source proof and release evidence

Current host statuses and release evidence: [current parity inventory](../parity/inventory.json), [chatgpt host report](../testing/chatgpt.md), and [codex host report](../testing/codex.md). These records can advance after the source freeze. Structural catalog checks do not establish host support.

### `skills/make-bot-ui/SKILL.md`

Destination: [skills/make-bot-ui/SKILL.md](../../skills/make-bot-ui/SKILL.md).

Upstream commit: `4ec7ffa173eaa70d3d9467a627baf0954645a353`. SHA-256: `ad19d0bc6764287ec08c2521701974e7dac941f72e4d0fe81a24f4614494586f`.

Disposition: `runtime`. Aggregate adaptation status: `adapted-reviewed`.
