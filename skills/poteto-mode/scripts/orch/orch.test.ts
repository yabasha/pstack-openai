import { afterEach, describe, expect, it } from "bun:test";
import {
  chmod,
  mkdir,
  mkdtemp,
  readFile,
  readdir,
  rm,
  symlink,
  writeFile,
} from "node:fs/promises";
import { realpathSync } from "node:fs";
import { join } from "node:path";
import {
  NotFoundError,
  UserError,
  openStore,
  parseVerdict,
  type Forge,
  type OpenStoreOptions,
  type Store,
} from "./store.ts";

const fixtureRoot = process.env.ORCH_TEST_ROOT;
if (!fixtureRoot) throw new Error("set ORCH_TEST_ROOT to a task-owned scratch directory outside the package");
await mkdir(fixtureRoot, { recursive: true });
const SCRIPT = join(import.meta.dir, "orch.ts");
const directories: string[] = [];
const handles: Store[] = [];

interface RunResult {
  readonly code: number;
  readonly stdout: string;
  readonly stderr: string;
}

async function makeDirectory(): Promise<string> {
  const directory = await mkdtemp(join(fixtureRoot, "orch-test-"));
  directories.push(directory);
  return directory;
}

function useStore(
  directory: string,
  options?: OpenStoreOptions
): Store {
  const store = openStore(directory, options);
  handles.push(store);
  return store;
}

async function initializedStore(): Promise<{
  readonly directory: string;
  readonly store: Store;
}> {
  const directory = await makeDirectory();
  const store = useStore(directory);
  await store.init();
  return { directory, store };
}

function git({
  args,
  repo,
}: {
  args: readonly string[];
  repo: string;
}): string {
  const result = Bun.spawnSync(["git", "-C", repo, ...args]);
  if (result.exitCode !== 0) {
    throw new Error(
      `git ${args.join(" ")} failed: ${result.stderr.toString()}`
    );
  }
  return result.stdout.toString().trim();
}

async function makeGitStack(directory: string): Promise<{
  readonly repo: string;
  readonly mergedSha: string;
  readonly closedSha: string;
  readonly openSha: string;
  readonly draftSha: string;
}> {
  const repo = join(directory, "repo");
  await mkdir(repo);
  git({ repo, args: ["init", "--initial-branch=main"] });
  git({ repo, args: ["config", "user.name", "Orch Test"] });
  git({ repo, args: ["config", "user.email", "orch@example.com"] });
  await writeFile(join(repo, "main.txt"), "main\n");
  git({ repo, args: ["add", "."] });
  git({ repo, args: ["commit", "-m", "main"] });

  const branches = [
    "stack/merged",
    "stack/closed",
    "stack/open",
    "stack/draft",
  ];
  for (const [index, branch] of branches.entries()) {
    git({ repo, args: ["checkout", "-b", branch] });
    await writeFile(join(repo, `stack-${index}.txt`), `${branch}\n`);
    git({ repo, args: ["add", "."] });
    git({ repo, args: ["commit", "-m", branch] });
  }
  git({ repo, args: ["checkout", "stack/open"] });

  return {
    repo,
    mergedSha: git({ repo, args: ["rev-parse", "stack/merged"] }),
    closedSha: git({ repo, args: ["rev-parse", "stack/closed"] }),
    openSha: git({ repo, args: ["rev-parse", "stack/open"] }),
    draftSha: git({ repo, args: ["rev-parse", "stack/draft"] }),
  };
}

type FixtureState = "open" | "draft" | "merged" | "closed";

const FORGE_FIXTURES: Readonly<
  Record<
    Forge,
    {
      readonly fields: string;
      readonly row: (pr: {
        number: number;
        state: FixtureState;
        head: string;
        base: string;
      }) => Record<string, unknown>;
    }
  >
> = {
  gh: {
    fields: "number,state,headRefName,baseRefName",
    row: ({ number, state, head, base }) => ({
      number,
      state: state === "draft" ? "OPEN" : state.toUpperCase(),
      headRefName: head,
      baseRefName: base,
    }),
  },
  origin: {
    fields: "number,status,headRef,baseRef",
    row: ({ number, state, head, base }) => ({
      number,
      status: state,
      headRef: head,
      baseRef: base,
    }),
  },
};

function forgeRows(
  forge: Forge,
  prs: readonly {
    number: number;
    state: FixtureState;
    head: string;
    base: string;
  }[]
): string {
  return JSON.stringify(prs.map((pr) => FORGE_FIXTURES[forge].row(pr)));
}

async function withFakeForge<T>({
  directory,
  forge,
  operation,
  currentRows,
  childRows,
}: {
  directory: string;
  forge: Forge;
  operation: () => Promise<T>;
  currentRows?: string;
  childRows?: string;
}): Promise<T> {
  const bin = join(directory, "bin");
  const outputPath = join(directory, "forge-output.txt");
  const childOutputPath = join(directory, "forge-child-output.txt");
  await writeFile(childOutputPath, childRows ?? forgeRows(forge, [
    {number: 14, state: "draft", head: "stack/draft", base: "stack/open"},
    {number: 15, state: "closed", head: "stack/abandoned", base: "stack/open"},
  ]));
  await mkdir(bin, { recursive: true });
  await writeFile(
    outputPath,
    `${
      currentRows ??
      forgeRows(forge, [
        {
          number: 11,
          state: "open",
          head: "stack/open",
          base: "stack/closed",
        },
      ])
    }\n`
  );
  const { fields } = FORGE_FIXTURES[forge];
  const list = (filter: string, branch: string): string =>
    `pr list ${filter} ${branch} --state all${forge === "gh" ? " --limit 300" : ""} --json ${fields}`;
  const fake = join(bin, forge);
  await writeFile(
    fake,
    `#!/usr/bin/env bash
set -euo pipefail
if [ "$(pwd -P)" != "${realpathSync(join(directory, "repo"))}" ]; then
  printf '${forge} ran outside the fixture repo: %s\\n' "$(pwd -P)" >&2
  exit 2
fi
case "$*" in
  "${list("--head", "stack/open")}")
    cat "${outputPath}"
    ;;
  "${list("--head", "stack/closed")}")
    printf '%s\\n' '${forgeRows(forge, [{ number: 13, state: "closed", head: "stack/closed", base: "stack/merged" }])}'
    ;;
  "${list("--head", "stack/merged")}")
    printf '%s\\n' '${forgeRows(forge, [{ number: 10, state: "merged", head: "stack/merged", base: "main" }])}'
    ;;
  "${list("--base", "stack/open")}")
    cat "${childOutputPath}"
    ;;
  "${list("--base", "stack/draft")}")
    printf '[]\\n'
    ;;
  *)
    printf 'unexpected ${forge} arguments: %s\\n' "$*" >&2
    exit 2
    ;;
esac
`
  );
  await chmod(fake, 0o755);

  const originalPath = process.env.PATH;
  process.env.PATH = `${bin}:${originalPath ?? ""}`;
  try {
    return await operation();
  } finally {
    if (originalPath === undefined) {
      delete process.env.PATH;
    } else {
      process.env.PATH = originalPath;
    }
  }
}

function runCli(
  args: readonly string[],
  env: Readonly<Record<string, string | undefined>> = process.env
): RunResult {
  const result = Bun.spawnSync([process.execPath, "--no-install", SCRIPT, ...args], { env });
  return {
    code: result.exitCode,
    stdout: result.stdout.toString(),
    stderr: result.stderr.toString(),
  };
}

afterEach(async () => {
  for (const store of handles.splice(0).reverse()) {
    await store.close();
  }
  for (const directory of directories.splice(0)) {
    await rm(directory, { recursive: true, force: true });
  }
});

describe("Store", () => {
  it("initializes an idempotent plain-file store and releases its lock", async () => {
    const directory = await makeDirectory();
    const store = useStore(directory);

    expect(await store.init()).toEqual({ store: directory });
    const firstUnits = await readFile(join(directory, "units.tsv"), "utf8");
    const firstLedger = await readFile(
      join(directory, "ledger.tsv"),
      "utf8"
    );

    expect(await store.init()).toEqual({ store: directory });
    expect(await readFile(join(directory, "units.tsv"), "utf8")).toBe(
      firstUnits
    );
    expect(await readFile(join(directory, "ledger.tsv"), "utf8")).toBe(
      firstLedger
    );
    expect((await readdir(directory)).sort()).toEqual([
      ".orch.lock",
      "frontier.json",
      "gates.md",
      "inbox",
      "ledger.tsv",
      "preferences.md",
      "units.tsv",
    ]);

    await store.close();
    expect(await readdir(directory)).not.toContain(".orch.lock");
  });

  it("composes unit add, set, get, list, and counts", async () => {
    const { store } = await initializedStore();

    expect(
      await store.units.add({
        id: "u1",
        track: "build",
        brief: "briefs/u1.md",
      })
    ).toMatchObject({ id: "u1", state: "pending" });
    expect(
      await store.units.add({ id: "=SUM(A1)", track: "+build" })
    ).toMatchObject({ id: "'=SUM(A1)", track: "'+build" });

    const updated = await store.units.set({
      id: "u1",
      state: "done",
      branch: "poteto/u1",
      pr: 184530,
      sha: "abc123",
    });
    expect(updated).toEqual({
      id: "u1",
      track: "build",
      state: "done",
      branch: "poteto/u1",
      pr: "184530",
      sha: "abc123",
      brief: "briefs/u1.md",
    });
    expect(await store.units.get("u1")).toEqual(updated);
    expect(
      await store.units.list({ state: "done", track: "build" })
    ).toEqual([updated]);
    expect(await store.units.counts()).toEqual({ done: 1, pending: 1 });
    await expect(
      store.units.add({ id: "u1", track: "build" })
    ).rejects.toThrow("unit u1 already exists");
    await expect(
      store.units.set({ id: "missing", state: "done" })
    ).rejects.toBeInstanceOf(NotFoundError);
  });

  it("records, replaces, checks, and summarizes typed ledger verdicts", async () => {
    const { store } = await initializedStore();

    try {
      await store.ledger.check({ pr: 184530, sha: "abc123" });
      throw new Error("expected ledger check to fail");
    } catch (error) {
      expect(error).toBeInstanceOf(NotFoundError);
      if (error instanceof NotFoundError) {
        expect(error.output).toEqual({
          compact: "NOT-VERIFIED",
          json: {
            pr: "184530",
            sha: "abc123",
            verdict: "NOT-VERIFIED",
          },
        });
      }
    }
    expect(() => parseVerdict("looks-good")).toThrow("verdict must be");

    const recorded = await store.ledger.record({
      pr: 184530,
      sha: "abc123",
      verdict: "unit-test-verified",
      evidence: "reports/verify.md",
      verifier: "opus",
    });
    expect(await store.ledger.check({ pr: 184530, sha: "abc123" })).toEqual(
      recorded
    );
    expect(await store.ledger.summary()).toEqual({
      "unit-test-verified": 1,
    });

    await store.ledger.record({
      pr: 184530,
      sha: "abc123",
      verdict: "live-ui-verified",
      evidence: "reports/live.md",
    });
    expect(await store.ledger.summary()).toEqual({
      "live-ui-verified": 1,
    });
  });

  it("pushes, peeks, and atomically drains inbox pointers", async () => {
    const { directory, store } = await initializedStore();

    const first = await store.inbox.push({
      agent: "worker-1",
      unit: "u1",
      status: "done",
      report: "reports/u1.md",
    });
    expect(first.pointer).toMatchObject({ unit: "u1", status: "done" });
    expect(first.filename).toEndWith(".tsv");
    await store.inbox.push({
      agent: "worker-2",
      unit: "u2",
      status: "failed",
    });

    expect(await store.inbox.count()).toBe(2);
    expect(await store.inbox.peek()).toHaveLength(2);
    expect(await store.inbox.count()).toBe(2);
    expect(await store.inbox.drain()).toHaveLength(2);
    expect(await store.inbox.count()).toBe(0);
    expect(await readdir(join(directory, "inbox"))).toEqual([]);
    expect(
      (await readdir(directory)).filter((name) =>
        name.startsWith(".inbox-drain-")
      )
    ).toEqual([]);
  });

  it("requires explicit reviewed force to replace a stale lock", async () => {
    const { directory } = await initializedStore();
    const exited = Bun.spawn([process.execPath, "--no-install", "-e", "process.exit(0)"]);
    await exited.exited;
    await writeFile(join(directory, ".orch.lock"), `${exited.pid}\n`);

    const stale: string[] = [];
    const recovered = useStore(directory, {
      force: true,
      onStaleLock: (holder) => stale.push(holder),
    });
    expect(
      await recovered.units.add({ id: "u1", track: "build" })
    ).toMatchObject({ id: "u1" });
    expect(stale).toEqual([String(exited.pid)]);
    await recovered.close();
    expect(await readdir(directory)).not.toContain(".orch.lock");
  });

  it("blocks a writer and steals the pid lock only with force", async () => {
    const { directory, store } = await initializedStore();
    await store.close();
    await writeFile(join(directory, ".orch.lock"), `${process.pid}\n`);

    const blocked = useStore(directory);
    await expect(
      blocked.units.add({ id: "u1", track: "build" })
    ).rejects.toThrow(`store lock held by pid ${process.pid}`);

    const stolen: string[] = [];
    const forced = useStore(directory, {
      force: true,
      onLockStolen: (holder) => stolen.push(holder),
    });
    expect(
      await forced.units.add({ id: "u1", track: "build" })
    ).toMatchObject({ id: "u1" });
    expect(stolen).toEqual([String(process.pid)]);
    await forced.close();
    expect(await readdir(directory)).not.toContain(".orch.lock");
  });

  it("parks gates, stores standing orders, and renders status", async () => {
    const { directory, store } = await initializedStore();
    await store.units.add({ id: "u1", track: "build" });
    expect(
      await store.gates.park({
        id: "release",
        question: "Ship now?",
        options: "ship,wait",
        defaultAnswer: "wait",
      })
    ).toMatchObject({ kind: "open", id: "release" });
    expect(
      await store.standing.add({ line: "Never force push." })
    ).toEqual({ number: 1, line: "Never force push." });

    const first = await store.status.render();
    expect(first.changed).toBe("first render");
    expect(first.summary.openGateIds).toEqual(["release"]);
    expect(await readFile(join(directory, "status.md"), "utf8")).toContain(
      "| release | open | Ship now? |"
    );
    expect((await store.status.render()).changed).toBe("no derived changes");

    expect(
      await store.gates.resolve({ id: "release", answer: "ship" })
    ).toMatchObject({ kind: "resolved", answer: "ship" });
    expect((await store.status.render()).changed).toBe("open gates 1->0");
    expect(await store.gates.list()).toEqual([]);
    expect(await store.standing.show()).toEqual([
      { number: 1, line: "Never force push." },
    ]);
  });

  for (const forge of ["gh", "origin"] as const) {
    it(`resolves the ordered frontier from the ${forge} base chain and validates an optional pin`, async () => {
      const { directory, store } = await initializedStore();
      const stack = await makeGitStack(directory);
      const forgeParams = forge === "gh" ? {} : { forge };

      await withFakeForge({
        directory,
        forge,
        operation: async () => {
          expect(
            await store.frontier.set({ repo: stack.repo, ...forgeParams })
          ).toEqual({
            generation: 1,
            prs: [
              {
                pr: 10,
                branches: "stack/merged",
                sha: stack.mergedSha,
                state: "MERGED",
              },
              {
                pr: 13,
                branches: "stack/closed",
                sha: stack.closedSha,
                state: "CLOSED",
              },
              {
                pr: 11,
                branches: "stack/open",
                sha: stack.openSha,
                state: "OPEN",
              },
              {
                pr: 14,
                branches: "stack/draft",
                sha: stack.draftSha,
                state: "OPEN",
              },
            ],
            lowestUnmerged: 11,
          });
          expect(
            (
              await store.frontier.set({
                repo: stack.repo,
                ...forgeParams,
                prs: [10, 13, 11, 14],
              })
            ).generation
          ).toBe(2);
          expect((await store.frontier.show()).generation).toBe(2);
          await expect(
            store.frontier.set({
              repo: stack.repo,
              ...forgeParams,
              prs: [10, 11, 12],
            })
          ).rejects.toThrow(
            "frontier pin mismatch: missing from resolved chain: 12; extra in resolved chain: 13,14"
          );
          await expect(
            store.frontier.set({
              repo: stack.repo,
              ...forgeParams,
              prs: [13, 10, 11, 14],
            })
          ).rejects.toThrow(
            "frontier pin mismatch: order differs: expected 13,10,11,14; resolved 10,13,11,14"
          );
          await expect(
            store.frontier.set({
              repo: stack.repo,
              ...forgeParams,
              prs: [10, 10],
            })
          ).rejects.toThrow("--prs must not contain duplicates");
        },
      });
    });

    it(`selects the unique open ${forge} PR despite closed branch history`, async () => {
      const {directory, store} = await initializedStore();
      const stack = await makeGitStack(directory);
      await withFakeForge({directory, forge, currentRows: forgeRows(forge, [
        {number: 9, state: "closed", head: "stack/open", base: "main"},
        {number: 11, state: "open", head: "stack/open", base: "stack/closed"},
      ]), operation: async () => {
        const result = await store.frontier.set({repo: stack.repo, forge});
        expect(result.prs.map(row => row.pr)).toEqual([10, 13, 11, 14]);
      }});
    });

    for (const state of ["open", "closed"] satisfies FixtureState[]) {
      it(`rejects ambiguous ${state} ${forge} branch history without changing frontier`, async () => {
        const {directory, store} = await initializedStore();
        const stack = await makeGitStack(directory);
        const before = await readFile(join(directory, "frontier.json"), "utf8");
        await withFakeForge({directory, forge, currentRows: forgeRows(forge, [
          {number: 9, state, head: "stack/open", base: "main"},
          {number: 11, state, head: "stack/open", base: "stack/closed"},
        ]), operation: async () => {
          await expect(store.frontier.set({repo: stack.repo, forge})).rejects.toThrow(
            state === "open" ? "multiple open pull requests" : "ambiguous historical pull requests"
          );
          expect(await readFile(join(directory, "frontier.json"), "utf8")).toBe(before);
        }});
      });
    }

    it(`rejects unparseable ${forge} output loudly`, async () => {
      const { directory, store } = await initializedStore();
      const stack = await makeGitStack(directory);

      await withFakeForge({
        directory,
        forge,
        currentRows: "this line is not forge output",
        operation: async () => {
          await expect(
            store.frontier.set({ repo: stack.repo, forge })
          ).rejects.toThrow(
            `${forge} pr list --head stack/open output is not valid JSON`
          );
        },
      });
    });
  }

  for (const filter of ["head", "children"]) {
    it(`rejects capped gh ${filter} discovery without changing frontier`, async () => {
      const {directory, store} = await initializedStore();
      const stack = await makeGitStack(directory);
      const before = await readFile(join(directory, "frontier.json"), "utf8");
      const capped = forgeRows("gh", Array.from({length: 300}, (_, index) => ({
        number: index + 100, state: "closed", head: "old-" + index, base: "stack/open",
      })));
      await withFakeForge({directory, forge: "gh",
        ...(filter === "head" ? {currentRows: capped} : {childRows: capped}),
        operation: async () => {
          await expect(store.frontier.set({repo: stack.repo})).rejects.toThrow("300-row discovery limit");
          expect(await readFile(join(directory, "frontier.json"), "utf8")).toBe(before);
        },
      });
    });
  }

  it("names the missing pull request when a chain branch has none", async () => {
    const { directory, store } = await initializedStore();
    const stack = await makeGitStack(directory);

    await withFakeForge({
      directory,
      forge: "gh",
      currentRows: "[]",
      operation: async () => {
        await expect(store.frontier.set({ repo: stack.repo })).rejects.toThrow(
          "branch stack/open has no pull request; open one with gh pr create"
        );
      },
    });
  });

  it("rejects malformed TSV, verdict, frontier, and inbox data", async () => {
    const { directory, store } = await initializedStore();

    await writeFile(join(directory, "units.tsv"), "wrong\n");
    await expect(store.units.list()).rejects.toThrow(
      "units.tsv has an invalid header"
    );
    await writeFile(
      join(directory, "units.tsv"),
      "id\ttrack\tstate\tbranch\tpr\tsha\tbrief\nshort\trow\n"
    );
    await expect(store.units.list()).rejects.toThrow(
      "units.tsv has a malformed row"
    );

    await writeFile(
      join(directory, "ledger.tsv"),
      "pr\tsha\tverdict\tevidence\tverifier\tts\n1\tsha\tinvalid\treport\tme\tnow\n"
    );
    await expect(store.ledger.summary()).rejects.toThrow(
      "ledger.tsv has invalid verdict invalid"
    );

    await writeFile(join(directory, "frontier.json"), '{"generation":"1"}\n');
    await expect(store.frontier.show()).rejects.toThrow(
      "frontier.json has an invalid shape"
    );

    await writeFile(join(directory, "inbox", "bad.tsv"), "too\tshort\n");
    await expect(store.inbox.peek()).rejects.toThrow(
      "inbox pointer bad.tsv is malformed"
    );
  });

  it("rejects operations after close", async () => {
    const { store } = await initializedStore();
    await store.close();
    await expect(store.units.list()).rejects.toThrow("store is closed");
    await expect(store.status.render()).rejects.toBeInstanceOf(UserError);
  });
});

describe("orch CLI", () => {
  it("prints commander help and rejects invalid parsing with exit 1", async () => {
    const help = runCli(["--help"]);
    expect(help.code).toBe(0);
    expect(help.stdout).toContain("Commands:");
    expect(help.stdout).toContain("unit");
    expect(help.stdout).toContain("ledger");

    const frontierHelp = runCli(["frontier", "set", "--help"]);
    expect(frontierHelp.code).toBe(0);
    expect(frontierHelp.stdout).toContain("--repo <dir>");
    expect(frontierHelp.stdout).toContain("--forge <forge>");
    expect(frontierHelp.stdout).toContain("--prs <n,...>");

    const directory = await makeDirectory();
    const invalid = runCli(["--store", directory, "unit", "add", "u1"]);
    expect(invalid.code).toBe(1);
    expect(invalid.stderr).toContain("required option '--track <track>'");

    const badForge = runCli([
      "--store",
      directory,
      "frontier",
      "set",
      "--repo",
      directory,
      "--forge",
      "gt",
    ]);
    expect(badForge.code).toBe(1);
    expect(badForge.stderr).toContain("Allowed choices are gh, origin");
  });

  it("accepts ORCH_STORE and emits complete JSON", async () => {
    const directory = await makeDirectory();
    const env = { ...process.env, ORCH_STORE: directory };
    expect(runCli(["init"], env).code).toBe(0);

    const added = runCli(
      ["unit", "add", "u1", "--track", "build", "--json"],
      env
    );
    expect(added.code).toBe(0);
    expect(JSON.parse(added.stdout)).toEqual({
      id: "u1",
      track: "build",
      state: "pending",
      branch: "",
      pr: "",
      sha: "",
      brief: "",
    });
  });

  it("maps user and not-found outcomes to the preserved exit codes", async () => {
    const directory = await makeDirectory();
    expect(runCli(["--store", directory, "init"]).code).toBe(0);

    const missingRepo = runCli([
      "--store",
      directory,
      "frontier",
      "set",
    ]);
    expect(missingRepo.code).toBe(1);
    expect(missingRepo.stderr).toContain(
      "set --repo <dir> or ORCH_REPO"
    );

    const userError = runCli([
      "--store",
      directory,
      "unit",
      "add",
      "",
      "--track",
      "build",
    ]);
    expect(userError.code).toBe(1);
    expect(userError.stderr).toContain("unit id must not be empty");

    const missingUnit = runCli([
      "--store",
      directory,
      "unit",
      "get",
      "missing",
    ]);
    expect(missingUnit.code).toBe(2);
    expect(missingUnit.stderr).toContain("unit missing not found");

    const missingLedger = runCli([
      "--store",
      directory,
      "--json",
      "ledger",
      "check",
      "184530",
      "abc123",
    ]);
    expect(missingLedger.code).toBe(2);
    expect(JSON.parse(missingLedger.stdout)).toEqual({
      pr: "184530",
      sha: "abc123",
      verdict: "NOT-VERIFIED",
    });
    expect(missingLedger.stderr).toBe("");
  });
});


describe("portable bookkeeping boundaries", () => {
  it("rejects a preexisting inbox symlink before initialization", async () => {
    const directory = await makeDirectory();
    const target = await makeDirectory();
    await symlink(target, join(directory, "inbox"));
    await expect(useStore(directory).init()).rejects.toThrow("inbox must not be a symbolic link");
    expect(await readdir(target)).toEqual([]);
    expect(await readdir(directory)).toEqual(["inbox"]);
  });

  it("rejects a replaced inbox symlink before pointer writes or drain", async () => {
    const { directory, store } = await initializedStore();
    const target = await makeDirectory();
    await writeFile(join(target, "sentinel.txt"), "preserve\n");
    await rm(join(directory, "inbox"), { recursive: true });
    await symlink(target, join(directory, "inbox"));
    const before = await readdir(target);
    await expect(store.inbox.push({ agent: "worker", unit: "u1", status: "done" })).rejects.toThrow("inbox must not be a symbolic link");
    await expect(store.inbox.drain()).rejects.toThrow("inbox must not be a symbolic link");
    expect(await readdir(target)).toEqual(before);
    expect(await readFile(join(target, "sentinel.txt"), "utf8")).toBe("preserve\n");
  });

  it("explicit_writable_store", async () => {
    expect(() => openStore("")).toThrow("explicit");
    const internal = useStore(join(import.meta.dir, "forbidden-store"));
    await expect(internal.init()).rejects.toThrow("outside the package");
    const { directory, store } = await initializedStore();
    expect(await readFile(join(directory, "units.tsv"), "utf8")).toStartWith("id\ttrack");
    await store.close();
    await chmod(directory, 0o555);
    try {
      await expect(useStore(directory).init()).rejects.toThrow("writable");
    } finally {
      await chmod(directory, 0o755);
    }
  });

  it("two_isolated_assignments", async () => {
    const first = await initializedStore();
    const second = await initializedStore();
    await Promise.all([
      first.store.units.add({ id: "assignment-a", track: "build", brief: "a.md" }),
      second.store.units.add({ id: "assignment-b", track: "review", brief: "b.md" }),
    ]);
    expect(await readFile(join(first.directory, "units.tsv"), "utf8")).not.toContain("assignment-b");
    expect(await readFile(join(second.directory, "units.tsv"), "utf8")).not.toContain("assignment-a");
  });

  it("stale_lock_requires_review", async () => {
    const { directory, store } = await initializedStore();
    await store.close();
    const exited = Bun.spawn([process.execPath, "--no-install", "-e", "process.exit(0)"]);
    await exited.exited;
    const lock = String(exited.pid) + "\n";
    await writeFile(join(directory, ".orch.lock"), lock);
    const before = await readFile(join(directory, "units.tsv"), "utf8");
    await expect(useStore(directory).units.add({ id: "unsafe", track: "build" })).rejects.toThrow("requires review");
    expect(await readFile(join(directory, ".orch.lock"), "utf8")).toBe(lock);
    expect(await readFile(join(directory, "units.tsv"), "utf8")).toBe(before);

  });

  it("invalid_revision_cannot_pass", async () => {
    const { store } = await initializedStore();
    await store.ledger.record({ pr: 1, sha: "abc123", verdict: "unit-test-verified", evidence: "report.md" });
    await expect(store.ledger.check({ pr: 1, sha: "different" })).rejects.toThrow("NOT-VERIFIED");
    expect((await store.ledger.check({ pr: 1, sha: "abc123" })).verdict).toBe("unit-test-verified");
  });

  it("crash_preserves_last_valid_record", async () => {
    const { directory, store } = await initializedStore();
    await store.units.add({ id: "valid", track: "build" });
    await store.close();
    const before = await readFile(join(directory, "units.tsv"), "utf8");
    const child = Bun.spawn([process.execPath, "--no-install", "-e",
      'import { openStore } from ' + JSON.stringify(join(import.meta.dir, "store.ts")) + '; const s = openStore(' + JSON.stringify(directory) + '); await s.units.add({id:"committed",track:"build"}); await Bun.write(' + JSON.stringify(join(directory, ".units.tsv.interrupted.tmp")) + ', "partial"); process.exit(9);'
    ]);
    expect(await child.exited).toBe(9);
    const after = await readFile(join(directory, "units.tsv"), "utf8");
    expect(after).toStartWith(before);
    expect(after).toContain("committed\tbuild");
    expect(after).not.toContain("partial");
    expect(await useStore(directory).units.list()).toHaveLength(2);
    await expect(useStore(directory).units.add({ id: "replay", track: "build" })).rejects.toThrow("requires review");
    expect(await readFile(join(directory, "units.tsv"), "utf8")).toBe(after);
  });
});

async function packageTree(): Promise<Record<string, string>> {
  const root = join(import.meta.dir, "../../../..");
  const result: Record<string, string> = {};
  const visit = async (directory: string): Promise<void> => {
    for (const entry of await readdir(directory, { withFileTypes: true })) {
      if ([".git", ".superpowers", "node_modules"].includes(entry.name)) continue;
      const path = join(directory, entry.name);
      if (entry.isDirectory()) await visit(path);
      else if (entry.isFile()) result[path] = new Bun.CryptoHasher("sha256").update(await Bun.file(path).arrayBuffer()).digest("hex");
    }
  };
  await visit(root);
  return result;
}


describe("orch CLI portable boundaries", () => {
  it("owned init JSON leaves the package tree unchanged", async () => {
    const directory = await makeDirectory();
    const before = await packageTree();
    const result = runCli(["--store", directory, "--json", "init"]);
    expect(result.code).toBe(0);
    expect(JSON.parse(result.stdout)).toEqual({ store: directory });
    expect(await packageTree()).toEqual(before);
  });
  it("stale lock requires review in CLI output", async () => {
    const { directory, store } = await initializedStore();
    await store.close();
    const exited = Bun.spawn([process.execPath, "--no-install", "-e", "process.exit(0)"]);
    await exited.exited;
    const lock = String(exited.pid) + "\n";
    await writeFile(join(directory, ".orch.lock"), lock);
    const result = runCli(["--store", directory, "unit", "add", "unsafe", "--track", "build"]);
    expect(result.code).toBe(1);
    expect(result.stderr).toContain("requires review");
    expect(await readFile(join(directory, ".orch.lock"), "utf8")).toBe(lock);
  });
});
