# Dependency readiness

The [dependency audit](../parity/dependencies.json) accounts for all 164 canonical files at `df581122cde17e6e27686b5a448bde23e4ad4318`: 51 root skills and 113 support files. The 23 playbooks are included in those 113 support files. Each source record carries the verified canonical hash, the adapted destination hash, its complete inventory dependency list, and source/destination line references for discovered dependency groups.

The audit records 32 dependency groups and 573 caller/group references. It includes examples and descriptive mentions so source requirements do not disappear during adaptation. A reference does not imply that every caller must install that dependency. Read the caller's full contract to select the branch. Local package dependencies bind the caller to the actual referenced file or directory; a readable skill is instruction content, not an execution capability.

## Use at invocation

1. Find the caller in `sourceAudit`. Read its complete current instructions and required local references. A hash mismatch makes the audit stale. A missing required file blocks dependent work.
2. Follow its `dependencyIds` into `dependencies`. Each record names the callers, required proof, available bundled binding or missing capability, setup effects and evidence. `selected-runtime` preserves the actual repository helper choice. It never means reference-only.
3. Discover the current session's exact tools through [the capability contract](../../references/host-capabilities.md). Record exposed operations separately from observed successes. No API name is assigned by this audit.
4. Execute only authorized branches. Retain action/result artifacts at the exact revision. Keep missing proof visible when a local draft or sequential fallback is useful.

Every `executionStatus` in this audit is `blocked` because this audit supplies no current caller/host execution receipts. This is a readiness gate, not a host evidence result and not a claim that the capability is absent from every possible session. Bundled contract paths are readable; their presence alone cannot clear an execution gate. Host registry statuses remain `not-run` until separate testing produces actual evidence.

## Companion gates

| Requirement | Proof and available reduction |
| --- | --- |
| `create-skill` | The external implementation is not bundled. Discover an actual authoring workflow, read its validator and observe the loop required by the caller. The authoring playbook permits a provisional draft and manual structural checklist as reduced capability. Reflect keeps application blocked when its required draft/test/iterate or description-optimization loop is absent. Automate-me uses the caller's subjective user review instead of a benchmark loop. |
| `deslop` | The external code-review companion is not bundled. Its gate remains unmet until the companion runs or an explicitly authorized replacement review completes. The bundled prose skill `unslop` does not establish this code-review proof. |
| `control-cli` / `control-ui` | Names alone cannot drive an app. Discover the real tool or authorized alternative and prove the exact revision through user actions and resulting state. Missing controls block real-surface verification. Unit tests, CI, source review and final screenshots do not replace action/result evidence. |
| Project controls and Benny adapter | Read the actual completed feature map and driver. `control-notes` and `verify-*` examples are not shipped executables. Benny requires all nine live adapter steps before repro enablement. Inert readiness fixtures do not satisfy them. |

The complete caller contracts remain authoritative: [authoring](../../skills/poteto-mode/playbooks/authoring-a-skill.md), [reflect](../../skills/reflect/SKILL.md), [mode](../../skills/poteto-mode/SKILL.md), [shipping](../../skills/poteto-mode/playbooks/shipping.md), and [Benny control adapter](../../automations/benny/skills/reproduce-and-fix-issues/references/control-adapter.md).

## Runtime branches

| Branch | Runtime and requirements | Effects and missing-capability behavior |
| --- | --- | --- |
| `orch` | Existing Bun with `--no-install`; selected `orch.ts` and `store.ts`; exact packages checked by bootstrap. Frontier reads additionally need Graphite `gt` metadata in the authoritative clone and Git SHAs. | Writes the explicitly owned durable store. Missing metadata or dependencies blocks that branch. Manual canonical TSV/JSON handling is reduced capability, never helper execution. |
| `watch-pr` | Existing Bun with `--no-install`; bootstrap; authenticated `gh` reads; Git only when repository inference needs it. | Bounded network reads and NDJSON events. Inspect `kind`, `terminal` and `reason`; exit 0 or `READY` does not prove merge. Missing dependencies or forge access blocks execution. |
| `check-plan.mjs` | Existing Bun with `--no-install`, using Node-compatible standard-library imports. | Reads the supplied plan. Structural diagnostics do not prove semantic quality or real controls. Node itself was not validated by the Bun checks. |
| `worktree-audit.sh` | Bun launches Bash, which invokes `python3 -B`; Python standard library and Git. | Read-only local audit with an explicit base and scoped JSON exports. The canonical live `gh`/`jq`/fetch/global-history branch has been replaced. No network, fetch or deletion by the adapted helper. |
| `log.sh` | Bun launches Bash; standard `dirname`, `mkdir` and `date`. | Creates parent directories and appends an owned TSV file. Inspect escaped cells and read back the log. A template is not persistence evidence. |
| Consuming repository | Its actual build, test, lint, type-check, runtime and CI contracts at the target revision. | Discover before execution. No package-manager install, hook changes or CI edits by default. A local package test does not verify the consuming app. |

The source Node shebang and `node:` imports do not establish a Node-host pass. Python is an explicit dependency of the adapted audit, not an implicit replacement for every helper. Shell and Git availability must be checked in the executing environment. Do not install any runtime to clear a readiness gate automatically.

## Other discovered branches

Forge selection uses Origin only after observing availability and repository resolution, otherwise a separately verified `gh` binding. A Git remote named `origin` is not Origin CLI. Shipping does not require Graphite; `orch frontier` does. Keep those branches separate.

Repository tools must prove scoped read/history access and each permitted write. Workers need observed lifecycle operations and enforced ownership. Requested model names or role prompts establish neither independence nor model diversity. Active-history access and durable persistence require their own evidence. Missing loops or wake operations do not authorize a recurring schedule.

The `why` sources cover code archaeology, tickets, long-form documents, team chat, infrastructure telemetry, error tracking and analytics warehouses. Git/forge reads and MCP-backed categories require actual tool discovery and source results. Linear, Notion, Slack, Datadog, Sentry and Databricks playbooks are concrete examples, not installed connectors. Unavailable categories remain explicit gaps. Benny additionally requires configured channel, tracker, repository and event-trigger operations; a time schedule cannot silently replace a channel trigger.

Profiling and trace analysis need the appropriate runtime capture, parser, SQLite conversion, storage and source mapping. Supplied traces can support reduced analysis without proving a new capture. Visual parity needs actual rendering and numeric image-diff artifacts, preserving baseline bytes. Webhook UI execution needs a real provider, secure secret-submission and server retrieval, authorized listener and observed wake. Tailscale needs an observed online node and authorized reachability checks. Each missing capability blocks its branch.

No hooks, custom agents, plugins, integrations, credentials, global settings, listeners or schedules are installed or enabled by this audit. Source autonomy wording does not override permission or action-specific authorization.

## Historical helper setup

The separately approved validation snapshot was `37b68c8e842b275f310ead112c0ecb7fa0ade308` at `/Users/digital-hawk/Herd/pstack-openai-helper-verification`. Existing Bun 1.4.2 installed exact commander 14.0.0, bun-types 1.3.14 and TypeScript 7.0.2 using the npm registry, disabled lifecycle scripts and a task-owned cache. All 25 lock package records and integrity values stayed unchanged. Only two workspace requests changed from `latest` to the existing pins. The reconciled lock SHA-256 is `530b7fb6cba7f0b2a6cfc862dbcfe9020c333d45e7e0f448133006583ffdc1f2`.

That snapshot passed bootstrap, 85 tests with 316 assertions and strict TypeScript with exit 0. Its tests used injected watcher transports, fake Graphite and owned fixture repositories. No live `gh` ran. The [helper setup record](helper-setup.md) preserves the exact commands, effects and limits.

Those results belong to that snapshot. The operative candidate has no installed dependency metadata. Its dependency-backed helpers remain blocked until an authorized prepared copy passes its own checks. The historical approval does not authorize a new install, host loading, plugin enablement, integrations, credentials or changed resolutions.

## Validation and host applicability

`tests/test_dependencies.py` checks source coverage, adapted hashes, inventory dependencies, critical callers and blocked control gates. Mutation checks remove a dependency or a control caller and reject an invented execution pass. These tests inspect contracts; they never prove model compliance or real app control.

Run them through Bun:

```sh
bun --no-install -e 'const p=Bun.spawnSync(["python3","-B","-m","unittest","tests.test_dependencies","-v"]);process.stdout.write(p.stdout);process.stderr.write(p.stderr);process.exit(p.exitCode)'
```

The [dependency-readiness acceptance case](../parity/cases/dependencies.json) requires both hosts because tool discovery, truthful blocking and authorized fallback behavior need observation in each host. It is not a structural-only registry entry. Both statuses start at `not-run`; no host result is generated by the tests above. Full evidence must observe execution and inspect its result. A reduced run must retain every unmet gate; unavailable execution uses blocked evidence. Never copy the historical snapshot's results into host passes.
