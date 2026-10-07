# Helper dependency setup

Bootstrap checks the local [manifest](../../skills/poteto-mode/scripts/package.json), [lock](../../skills/poteto-mode/scripts/bun.lock) and installed package metadata. Missing, unreadable or mismatched files cause a setup-required error and nonzero exit. [ensureDependenciesInstalled](../../skills/poteto-mode/scripts/bootstrap.ts) never installs, spawns, restarts or writes. Use Bun with runtime auto-install disabled.

## Exact historical approved scope

The separately approved validation copy was the complete committed snapshot `37b68c8e842b275f310ead112c0ecb7fa0ade308` at `/Users/digital-hawk/Herd/pstack-openai-helper-verification`. It was created only after verifying that directory was absent. Its install working directory was `/Users/digital-hawk/Herd/pstack-openai-helper-verification/skills/poteto-mode/scripts`. Its cache was `/Users/digital-hawk/Herd/pstack-openai-helper-verification/.bun-cache`.

The pins are commander 14.0.0, bun-types 1.3.14 and typescript 7.0.2. Reconciliation changed only the two workspace devDependency requests from latest to the existing exact pins. All 25 package records, transitive requests, platform conditions and integrity values remained byte-identical. These include @types/node 26.1.2, undici-types 8.3.0 and TypeScript platform packages 7.0.2. The operative lock now includes the reviewed request reconciliation. It has SHA-256 `530b7fb6cba7f0b2a6cfc862dbcfe9020c333d45e7e0f448133006583ffdc1f2`. The original lock hash was `667d9cf7222e9aae3fa42a4be383e657784216e9df115da02227fbc5ac7bbe46`.

## Procedure for a separately authorized copy

No generic new setup authorization follows from that historical approval. Before future setup, agree an exact immutable source SHA, complete writable copy, absent destination, scripts cwd, task-owned cache and allowed writes. Do not install in a host cache or operative invocation. Use existing Bun. Missing Bun or unavailable exact pins stops the procedure. No substitutes or material resolution/integrity changes are allowed without new review.

A reconciliation install, only if specifically needed and authorized, must use `bun install --ignore-scripts --registry=https://registry.npmjs.org --cache-dir=<approved-task-cache>` from the approved scripts cwd. Review any manifest/lock diff before frozen verification. Preserve every direct pin and all 25 transitive/integrity records. The current operative lock already has reconciled requests, so ordinary execution does not regenerate it.

For the historically approved snapshot, the actual frozen install command was:

```sh
bun install --frozen-lockfile --ignore-scripts --registry=https://registry.npmjs.org --cache-dir=/Users/digital-hawk/Herd/pstack-openai-helper-verification/.bun-cache
```

It ran from the exact scripts cwd above. It contacted the explicit registry, downloaded packages and wrote snapshot node_modules and its cache. Lifecycle scripts were disabled. No global settings/cache, credentials or operative source writes were approved. A future exact-copy approval must specify its own scope rather than reuse these paths or overwrite this snapshot.

## Historical observed validation

Bun 1.4.2 revision `50a8a838737a8f0e226d1c115788aa18192a2f18` completed the reviewed frozen install. These commands then ran from that snapshot's scripts cwd:

```sh
bun --no-install -e 'import {ensureDependenciesInstalled} from "./bootstrap.ts"; ensureDependenciesInstalled()'
ORCH_TEST_ROOT=/Users/digital-hawk/Herd/pstack-openai-helper-test-scratch bun --no-install test bootstrap.test.ts orch watch-pr
bun --no-install node_modules/typescript/bin/tsc --project watch-pr/tsconfig.json --noEmit --strict
```

Bootstrap passed. The suites passed 85 tests with 316 assertions and zero failures across five files. Strict TypeScript exited 0 without diagnostics. Tests used inert bootstrap spies, injected watcher transports, fake Graphite and owned fixture repositories. No live gh ran. All 299 tracked snapshot files matched the source commit except the reviewed two-request lock reconciliation. Tests and installation preserved the reviewed lock bytes.

The operative candidate has no installed dependencies. Snapshot results support only that source snapshot, not this caller, the current package or either host. Missing current metadata leaves dependency-backed helpers blocked. Development dependency setup is separate from plugin loading, enabling, integration, credentials and host behavior. See [Codex setup](../setup/codex.md), [ChatGPT setup](../setup/chatgpt.md) and [compatibility](../compatibility.md).
