# Prepare an upstream update for review

Run this procedure from the package root. Keep the accepted baseline at `df581122cde17e6e27686b5a448bde23e4ad4318` until a separate reviewed update explicitly changes it. Use an exact lowercase 40-character candidate commit from https://github.com/cursor/plugins.

1. Obtain authorization to fetch public source data. Set `CANDIDATE` to the exact commit. The commands below contact only https://api.github.com/repos/cursor/plugins and https://codeload.github.com/cursor/plugins. They do not fetch a Git remote, install dependencies, or execute downloaded code.
2. Run the check through Bun:

   ```sh
   bun --no-install -e 'const r = Bun.spawnSync(["python3", "-B", "-m", "tools.sync_upstream", "check", "--candidate", process.env.CANDIDATE], {stdout: "inherit", stderr: "inherit"}); process.exit(r.exitCode)'
   ```

3. Open `.upstream/reviews/<candidate>/summary.md` and `report.json`. Check the complete file and skill changes, hashes, possible renames, conflicts, and source notice changes. Check the caller list against the current inventory. An empty dependency list proves no caller coverage.
4. To generate drafts, intentionally move the existing review bundle to a separate retained location, then repeat the command with `prepare` instead of `check`. You can also run `prepare` directly. Both commands perform the same source verification. Existing bundles are never overwritten, including partially written bundles from an interrupted run.
5. Review the original, candidate, and adapted copies under `sources/`. Use `draft.patch` and `drafts/` as proposals. Drafts exist only where the current adapted bytes exactly match the old source bytes. Concurrent upstream and local edits produce conflict records. Added files, deleted files, and possible renames always need explicit decisions.
6. Record one intentional disposition for every entry in `resolutions.json`. Add a rationale and the reviewed callers. Review both sides of every possible rename and review license changes before accepting any update. Preserve the original bundle before annotating a copy because `report.json` records artifact hashes.
7. Hand the annotated copy to the separate resolution and acceptance workflow. This tool has no apply, accept, migration, or pin-update command. A completed annotation cannot authorize package writes. Before any later writer acts, it must validate the versioned schema, exact source identities, owned destinations, current adapted hashes, complete dispositions, and dependent callers against fresh package state. Semantic adaptations need review even when a draft has no textual conflict.

Run the offline structural tests with:

```sh
bun --no-install -e 'const r = Bun.spawnSync(["python3", "-B", "-m", "unittest", "tests.test_upstream_check", "-v"], {stdout: "inherit", stderr: "inherit"}); process.exit(r.exitCode)'
```

The bundle contains version 1 JSON Schemas for the report and resolution formats, the working package commit, complete original and candidate manifests, changed source copies, adapted hashes, a draft patch, conflict files, and notice differences. The canonical manifest retains all 164 baseline source hashes. The fetcher verifies the approved baseline archive digest, candidate commit identity, descendant lineage, and every candidate subtree blob against the reported Git tree. It rejects incomplete trees, oversized archives, links, special members, traversal, duplicate paths, and unsafe destination paths.

The commands write only a new `.upstream/reviews/<candidate>/` directory. They preserve tracked package files, the accepted pin, customizations, settings, and secrets. Local fixtures exercise the public fetch contract without network access. Structural results do not establish host behavior; both host statuses remain `not-run` until separately observed.
