# Helper setup

`ensureDependenciesInstalled(): void` checks the local manifest, resolved lock entries and installed package metadata. Missing files, unreadable files or mismatched versions throw a setup-required error. An uncaught error exits the helper with a nonzero status. The check never installs dependencies, launches subprocesses, restarts a helper or writes files.

The initial pins are `commander@14.0.0`, `bun-types@1.3.14` and `typescript@7.0.2`. The canonical lockfile is preserved with those exact resolutions. Its workspace devDependency requests still say `latest`. Lockfile regeneration requires separate setup authorization and has not been performed.

## Explicit setup procedure

Obtain authorization for network access and dependency installation before running this procedure. Copy the helper scripts, manifest and lockfile into a task-owned writable directory under `/Users/digital-hawk/Herd`. Never perform setup in an installed plugin cache. Use an already available Bun runtime. If Bun is unavailable, stop and report blocked.

In that writable copy, run `bun install` once to reconcile the workspace requests with the pinned manifest. This command contacts the configured package registry, downloads packages, writes Bun's package cache and `node_modules`, and may rewrite `bun.lock`. Review the lockfile diff. Confirm that all three direct versions remain the exact pins above and retain the resolved transitive dependency integrity records. Then run `bun install --frozen-lockfile` in the same authorized copy to verify the reconciled lock. Neither installation command belongs in an ordinary helper invocation.

Run `bun --no-install test skills/poteto-mode/scripts/bootstrap.test.ts` from the writable project copy. Run each dependent helper with `bun --no-install` and record `Bun.version` from a successful run. Missing packages remain blocked; do not use `bunx` or runtime auto-install to continue.

## Observed checks and limits

Bun `1.4.2` with build `50a8a8387` successfully ran the isolated bootstrap metadata-check fixtures on 2026-10-07. Five tests passed, including missing dependencies, lock mismatch, installed version mismatch and read-only package failure. Every fixture asserted zero helper subprocess calls and an unchanged package tree. The positive fixture uses synthetic package metadata and does not prove that third-party packages can execute.

The real pinned dependency copy is unavailable. Its bootstrap invocation exited with status 1 and a setup-required error. Installation, lock reconciliation, frozen-lock verification, full helper execution and dependency-backed typechecking remain blocked pending separately authorized setup. No host behavior is claimed by these structural tests.
