# Pinned source lineage

Import inspection date: 2026-10-07, Asia/Amman.

| Source | Canonical baseline | Comparison port |
| --- | --- | --- |
| Repository | https://github.com/cursor/plugins | https://github.com/FetchUpstream/pstack-plugin |
| Subtree | `pstack/` | Repository root |
| Version | `0.15.15` | `0.2.0` |
| Commit | `df581122cde17e6e27686b5a448bde23e4ad4318` | `ba2205db1f83295154e31abc762f533954f581bb` |
| Archive | https://codeload.github.com/cursor/plugins/tar.gz/df581122cde17e6e27686b5a448bde23e4ad4318 | https://codeload.github.com/FetchUpstream/pstack-plugin/tar.gz/ba2205db1f83295154e31abc762f533954f581bb |
| SHA-256 | `7e76b77c76fca022e17483cdaba0f3efa583043d98ac604d59a20bc22bf5091f` | `4bbbb50a4f97abb85554610870cb7bac68bfb00c3e629813eb27b605f9b66812` |
| License | MIT, Copyright (c) 2026 Lauren Tan | MIT, retains Lauren Tan attribution and its own notice |

Both downloaded archives matched the approved digests before extraction. Extraction rejected absolute paths, parent traversal, links, and non-regular members. Source files were read as data; downloaded scripts were not executed.

The [baseline paths](docs/parity/baseline-paths.txt) record all 164 canonical files, including 51 root skills, 24 principle leaves, 23 poteto playbooks and three nested Benny skills. Principles are included in the root count; all 113 other files, including playbooks, remain accounted for. The [inventory](docs/parity/inventory.json) retains every original file digest and records its reviewed destination and dependencies. Both host verification statuses remain not-run. Local structural closure does not establish installed discovery, worker support or workflow behavior.

The comparison port contains 26 root skills and remains a reference. Its archive and notice informed lineage checks; reviewed adaptations preserve the complete canonical baseline. See [NOTICE.md](NOTICE.md) and the [support map](docs/parity/support-map.md) for retained attribution and additional port-file provenance.

## Package metadata and logo

> Original metadata filename, retained as source provenance only: `.cursor-plugin/plugin.json`.

The reviewed root [plugin.json](plugin.json) replaces that source metadata. The original identity is `pstack`, version `0.15.15`, author Lauren Tan, MIT. Its homepage is https://github.com/cursor/plugins/tree/main/pstack and repository is https://github.com/cursor/plugins. Original keywords are pstack, poteto-mode, workflow, principles, agent-style, subagents, unslop; category is developer-tools; tags are workflow, principles, review, planning. Its display name is pstack, logo is `assets/logo.png`, skills path is `./skills/`, and agents path is `./agents/`. Its description reads "if you want to go fast, go deep first. pstack helps you write less, but higher quality code. rigorous agent workflows you can parallelize with confidence."

The candidate uses `pstack-openai`, version `0.1.0`, MIT, and identifies itself as an unofficial port. No public repository or website for this port is asserted. The portable root `skills/` convention replaces the explicit skills path. Presentation metadata lives at `extensions.com.openai.interface`. No agent registration, hooks, MCP server, app mapping, or compatibility overlay is added.

`assets/logo.png` is a byte-for-byte copy from the canonical archive above, covered by its MIT notice. SHA-256 is `672f6791589ef758b0ced2c4c477913fa2758623c438e265639a0d539ce90695`. `docs/parity/adaptations/02-manifest.json` records both source digests and reviewed dispositions. Host checks remain not-run.

Manifest review used https://developers.openai.com/plugins/build/plugins and https://agent-plugins.org/schemas/1.0.0/plugin.schema.json, fetched 2026-10-07 and supplied in the task's cached research. The schema forbids a root skills field; packaging documentation discovers skills from root `skills/` and requires extension asset paths to start with `./`. These are structural conventions, not evidence that either host loaded this package.

## Reviewed reconciliation

The [helper reconciliation](docs/parity/reconciliations/task12-lock.json) records the three reviewed bootstrap/package/lock files whose original implementation supplied no adaptation fragment. The lock was initially byte-identical to canonical source. Separately reviewed commit `2805c1eadec5906286a3ba129147ee1669052fe9` changed only the two workspace requests to the existing exact manifest pins. All 25 package resolutions, conditions, transitive requests and integrities remain byte-identical. The canonical lock SHA-256 remains `667d9cf7222e9aae3fa42a4be383e657784216e9df115da02227fbc5ac7bbe46`; the adapted destination SHA-256 is `530b7fb6cba7f0b2a6cfc862dbcfe9020c333d45e7e0f448133006583ffdc1f2`.

The [template reconciliation](docs/parity/reconciliations/task16-template.json) retains both historical rows and assigns the unchanged decision-log template to its original single current owner. The [support map](docs/parity/support-map.md) also records the relocated orchestration prompt dependency and local dependency closure. Historical fragment rationales retain the implementation-time limits; the map distinguishes closed local paths from current runtime limits.

The operative copy has no installed helper dependencies. Historical isolated tests at `37b68c8e842b275f310ead112c0ecb7fa0ade308` do not prove this candidate or either host. No host installation or loading follows from the metadata reconciliation.
