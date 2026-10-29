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

The [baseline paths](docs/parity/baseline-paths.txt) record all 169 current source files, including 54 root skills, 24 principle leaves, 23 poteto playbooks and three nested Benny skills. Principles are included in the root count; all 115 other files, including playbooks, remain accounted for. The [inventory](docs/parity/inventory.json) retains every current source file digest and records its reviewed destination and dependencies. Both host verification statuses remain not-run. Local structural closure does not establish installed discovery, worker support or workflow behavior.

The comparison port contains 26 root skills and remains a reference. Its archive and notice informed lineage checks; reviewed adaptations preserve the complete canonical baseline. See [NOTICE.md](NOTICE.md) and the [support map](docs/parity/support-map.md) for retained attribution and additional port-file provenance.

## Package metadata and logo

> Original metadata filename, retained as source provenance only: `.cursor-plugin/plugin.json`.

The reviewed root [plugin.json](plugin.json) replaces that source metadata. The original identity is `pstack`, version `0.15.15`, author Lauren Tan, MIT. Its homepage is https://github.com/cursor/plugins/tree/main/pstack and repository is https://github.com/cursor/plugins. Original keywords are pstack, poteto-mode, workflow, principles, agent-style, subagents, unslop; category is developer-tools; tags are workflow, principles, review, planning. Its display name is pstack, logo is `assets/logo.png`, skills path is `./skills/`, and agents path is `./agents/`. Its description reads "if you want to go fast, go deep first. pstack helps you write less, but higher quality code. rigorous agent workflows you can parallelize with confidence."

The initial import used `pstack-openai`, version `0.1.0`, MIT, and identified itself as an unofficial port. The current [manifest](plugin.json) remains version `0.1.3` during publication preparation and identifies yabasha as the port publisher. Lauren Tan retains credit for the original skills and principles in [NOTICE.md](NOTICE.md). The repository is `https://github.com/yabasha/pstack-openai`; public access and listing pages remain tracked in the [publication checklist](docs/publication.md). The portable root `skills/` convention replaces the explicit skills path. Presentation metadata lives at `extensions.com.openai.interface`. No agent registration, hooks, MCP server, app mapping, or compatibility overlay is added.

`assets/logo.png` is a byte-for-byte copy from the canonical archive above, covered by its MIT notice. SHA-256 is `672f6791589ef758b0ced2c4c477913fa2758623c438e265639a0d539ce90695`. `docs/parity/adaptations/02-manifest.json` records both source digests and reviewed dispositions. Host checks remain not-run.

Manifest review used https://developers.openai.com/plugins/build/plugins and https://agent-plugins.org/schemas/1.0.0/plugin.schema.json, fetched 2026-10-07 and supplied in the task's cached research. The schema forbids a root skills field; packaging documentation discovers skills from root `skills/` and requires extension asset paths to start with `./`. These are structural conventions, not evidence that either host loaded this package.

## Reviewed reconciliation

The [helper reconciliation](docs/parity/reconciliations/task12-lock.json) records the three reviewed bootstrap/package/lock files whose original implementation supplied no adaptation fragment. The lock was initially byte-identical to canonical source. Separately reviewed commit `2805c1eadec5906286a3ba129147ee1669052fe9` changed only the two workspace requests to the existing exact manifest pins. All 25 package resolutions, conditions, transitive requests and integrities remain byte-identical. The canonical lock SHA-256 remains `667d9cf7222e9aae3fa42a4be383e657784216e9df115da02227fbc5ac7bbe46`; the adapted destination SHA-256 is `530b7fb6cba7f0b2a6cfc862dbcfe9020c333d45e7e0f448133006583ffdc1f2`.

The [template reconciliation](docs/parity/reconciliations/task16-template.json) retains both historical rows and assigns the unchanged decision-log template to its original single current owner. The [support map](docs/parity/support-map.md) also records the relocated orchestration prompt dependency and local dependency closure. Historical fragment rationales retain the implementation-time limits; the map distinguishes closed local paths from current runtime limits.

The operative copy has no installed helper dependencies. Historical isolated tests at `37b68c8e842b275f310ead112c0ecb7fa0ade308` do not prove this candidate or either host. No host installation or loading follows from the metadata reconciliation.

## Unaccepted candidate e5136d82418d2db3165ea1050d17577cd618cc05

Candidate version 0.2.0. Archive SHA-256 30d6c97a55e4b08f6f75d6314b465bb3fe8c9a118149fc17fb1713bd7827014e. Review SHA-256 b9a52e1464c4738c53166f71cf6567dff260a035a4908b97ccfa4eb0a43330dc.
The inventory stages this candidate. The accepted baseline above remains historical evidence. Structural checks, helper regression tests, and affected host cases must run before separate acceptance.

## Accepted source baseline, 2026-10-15

Port 0.2.0 accepts official pstack 0.15.25 at `e5136d82418d2db3165ea1050d17577cd618cc05` after user authorization and reviewed validation. The [acceptance receipt](docs/parity/upstream-manifests/accepted.json) binds the exact manifest and [source acceptance evidence](docs/releases/0.2.0.md). Installed-host and workflow evidence remain separate. The unaccepted-candidate section above records the earlier staging event.

## Unaccepted candidate 99743e9c151c8537cbbf1f98bb38f34ef3368453

Candidate version 0.2.1. Archive SHA-256 5122bc6ef8d8f9a216915d90af410c987196e799e78974f14e7c7af5f3560088. Review SHA-256 805f692cc98d8679869f018b79b761706946e70f5313df2a822bdae0ce08bc7e.
The inventory stages this candidate. The accepted baseline above remains historical evidence. Structural checks, helper regression tests, and affected host cases must run before separate acceptance.

## Accepted source baseline, 2026-10-16

Port 0.2.1 accepts official pstack 0.15.25 at `99743e9c151c8537cbbf1f98bb38f34ef3368453` after the user-authorized sync and reviewed validation. The [acceptance receipt](docs/parity/upstream-manifests/accepted.json) binds the exact manifest, applied package revision and [source validation evidence](docs/releases/0.2.1.md). Earlier candidate and acceptance sections retain their historical scope. Installed refresh and workflow behavior remain separate observations.

## Unaccepted candidate 182f2ce414e83224915c190d2f63239c1608d0a5

Candidate version 0.2.2. Archive SHA-256 d56799a571f6e624f501568dc768fe31a41b691403525c872d41daae41b25417. Review SHA-256 b16809c21461cd7fcf5223a99e6e5fa6c338db0438b36b6dfc677b9310b85c41.
The inventory stages this candidate. The accepted baseline above remains historical evidence. Structural checks, helper regression tests, and affected host cases must run before separate acceptance.

## Accepted source baseline, 2026-10-17

Port 0.2.2 accepts official pstack 0.15.25 at `182f2ce414e83224915c190d2f63239c1608d0a5` after explicit user acceptance of the reviewed minimal sync. The [acceptance receipt](docs/parity/upstream-manifests/accepted.json) binds the exact source manifest, package identity and [source validation record](docs/releases/0.2.2.md). The Claude adapter remains quoted reference-only source; portable runtime behavior is unchanged. Prior candidate and acceptance sections retain their historical scope. Integration, installed refresh and skill discovery are recorded separately in task-owned artifacts and do not establish full workflow support.

## Unaccepted candidate d457567332aa6989e753ea289f30ea2bfbc80bc0

Candidate version 0.2.3. Archive SHA-256 aabcbe225ee504014ba4931908357889d9b34f28b0afb050ae84ad19f3daa101. Review SHA-256 45c2ce6d09b6bd414d878e3e9a801fc2dddba1d98a56f3184c04a941ab222954.
The inventory stages this candidate. The accepted baseline above remains historical evidence. Structural checks, helper regression tests, and affected host cases must run before separate acceptance.

## Unaccepted 0.2.3 amendment: PR #729

Source `d457567332aa6989e753ea289f30ea2bfbc80bc0` is superseded for this unaccepted candidate by `88d47514b82e7c44f00f2b2a72ff6dd12158038c`, upstream 0.15.29. The package version remains 0.2.3. All 172 canonical files were archive/tree verified; archive SHA-256 `df98989c5e6b3128ce3633eb68b4e31a79aabfe415c79d5e37f9b4906f94d2d9`. Eight canonical files changed, with no membership change. Sharpen now returns expert framing and a rewrite, without executing the input task. The accepted receipt remains `182f2ce414e83224915c190d2f63239c1608d0a5`. This is an explicitly requested candidate amendment, not source acceptance, plugin refresh or another invocation of the full update apply command.

## Statechart candidate amendment

PRs #741, #776 and #779 amend the unaccepted 0.2.3 source to `4ec7ffa173eaa70d3d9467a627baf0954645a353`, upstream 0.15.30. All 184 canonical files were archive/tree verified, including 57 root skills, 24 principles and 23 playbooks. The PR729 sharpen amendment remains included. The final statechart implementation includes the six correctness fixes. Rendering uses an explicitly selected reviewed local executable; subprocesses are bounded. The generated Claude tree remains derived and its adapter stays reference-only. The accepted 0.2.2 receipt is unchanged; no acceptance, integration or refresh occurred. See the amendment manifest and [statechart execution](skills/statechart/references/execution.md).

## Source acceptance for 0.2.3

The user explicitly accepted source `4ec7ffa173eaa70d3d9467a627baf0954645a353` on 2026-10-23, Asia/Amman. The [immutable source evidence](docs/releases/0.2.3.md) and strict accepted receipt bind the reviewed manifest and package ancestor. This supersedes the earlier unaccepted-candidate status while preserving its history. Linux PID-namespace coverage and full ChatGPT candidate loading/workflow verification remain incomplete. Integration, refresh and installed discovery are observed separately.

## Unaccepted candidate c742dd61706fbacc1b95f1a20b7b988cf096ce6c

Candidate version 0.2.4. Archive SHA-256 4f899c71d737afe7662ff515df0518b193562e4f9ec370ffb2d7d837aaf436ef. Review SHA-256 e3f1da4285004f7f6c189115f0340afa07b501efdfa336ec7e2e39151dc5a1c6.
The inventory stages this candidate. The accepted baseline above remains historical evidence. Structural checks, helper regression tests, and affected host cases must run before separate acceptance.
