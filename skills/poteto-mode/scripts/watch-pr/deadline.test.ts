import { describe, expect, it } from "bun:test";
import { WatcherQueryError } from "./github.ts";
import { runQueued, runSimple } from "./policy.ts";
import { failedCheck, fakeReader, fixtureHead, passingCheck, pendingCheck } from "./fakes.test-helper.ts";
import type { GitHubReader, NonEmpty, PollingOptions, PrContext, ProgressVerdict, QueryFailure, WatchMode } from "./types.ts";
import { parsePrNumber } from "./types.ts";

const context = (number: number): PrContext => ({
  owner: "owner", repo: "repo", number: parsePrNumber(number), expectedHead: fixtureHead,
});
const options: PollingOptions = {
  timeout: 1, interval: 60, sweepInterval: 300, maxPolls: 10, maxQueryErrors: 5, allowDraft: false,
};
const modes: readonly WatchMode[] = ["single", "stack", "queued-stack"];
const retryFailure = {kind: "missing-key", retryable: true, detail: "controlled retry"} satisfies ConstructorParameters<typeof WatcherQueryError>[0];

function harness() {
  const sleeps: number[] = [];
  const events: ProgressVerdict[] = [];
  const time = {
    now: 0,
    sleeps,
    events,
    onSleep: (seconds: number) => { time.now += seconds; },
    onEmit: (_event: ProgressVerdict) => {},
  };
  const dependencies = {
    reader: fakeReader() satisfies GitHubReader,
    clock: {
      now: () => time.now,
      observedAt: () => `synthetic-${time.now}`,
      sleep: async (seconds: number) => {
        time.sleeps.push(seconds);
        time.onSleep(seconds);
      },
    },
    emit(event: ProgressVerdict) {
      time.events.push(event);
      time.onEmit(event);
    },
  };
  return { time, dependencies };
}
type Harness = ReturnType<typeof harness>;
function run(mode: WatchMode, setup: Harness, overrides: Partial<PollingOptions> = {}, contexts: NonEmpty<PrContext> = [context(1)], statusOnly = false) {
  const args = {dependencies: setup.dependencies, contexts, options: {...options, ...overrides}};
  return mode === "queued-stack" && !statusOnly
    ? runQueued(args)
    : runSimple({...args, mode, statusOnly});
}
function changingReader(setup: Harness, mode: WatchMode, first: "pending" | "retry") {
  const base = fakeReader();
  let reads = 0;
  setup.dependencies.reader = {
    ...base,
    async pullRequest(pr) {
      reads += 1;
      if (first === "retry" && setup.time.sleeps.length === 0)
        throw new WatcherQueryError(retryFailure);
      const facts = await base.pullRequest(pr);
      return mode === "queued-stack" && setup.time.sleeps.length > 0
        ? {...facts, state: "MERGED", mergedAt: "observed"}
        : facts;
    },
    async checksFastPath() {
      return {kind: "checks", checks: [setup.time.sleeps.length === 0 ? pendingCheck() : passingCheck()]};
    },
  };
  return () => reads;
}

describe("deadline admission and bounded waits", () => {
  for (const mode of modes) for (const first of ["pending", "retry"] as const) {
    it(`${mode} ${first} expires before a new clean observation`, async () => {
      const setup = harness();
      const reads = changingReader(setup, mode, first);
      const result = await run(mode, setup);
      expect(result).toMatchObject({kind: "TIMEOUT", terminal: true, exitCode: 5, mode});
      if (result.kind !== "TIMEOUT") throw new Error("expected timeout");
      const pending = pendingCheck();
      if (pending.kind !== "pending") throw new Error("expected pending fixture");
      expect(result.reason).toEqual(first === "retry"
        ? {kind: "status-unavailable", failure: retryFailure}
        : mode === "queued-stack"
          ? {kind: "queued-stack", frontier: context(1), unmergedCount: 1}
          : {kind: "pending-checks", pending: [pending]});
      expect(setup.time.sleeps).toEqual([1]);
      expect(setup.time.now).toBe(1);
      expect(reads()).toBe(first === "retry" ? 1 : 2);
      if (first === "retry") expect(setup.time.events).toContainEqual(expect.objectContaining({kind: "RETRY", retryInSeconds: 1}));
    });

    it(`${mode} ${first} keeps full waits when timeout is disabled`, async () => {
      const setup = harness();
      const reads = changingReader(setup, mode, first);
      expect(await run(mode, setup, {timeout: 0})).toMatchObject({kind: mode === "queued-stack" ? "COMPLETE" : "READY", exitCode: 0});
      expect(setup.time.sleeps).toEqual([60]);
      expect(reads()).toBe(first === "retry" ? (mode === "queued-stack" ? 2 : 3) : (mode === "queued-stack" ? 3 : 4));
    });

    for (const oversleep of [0, 2]) it(`${mode} ${first} denies a resumed pass at ${oversleep === 0 ? "equality" : "late wake"}`, async () => {
      const setup = harness();
      const reads = changingReader(setup, mode, first);
      setup.time.onSleep = seconds => {setup.time.now += seconds + oversleep;};
      expect(await run(mode, setup)).toMatchObject({kind: "TIMEOUT", exitCode: 5});
      expect(reads()).toBe(first === "retry" ? 1 : 2);
      expect(setup.time.sleeps).toEqual([1]);
    });
  }

  for (const mode of modes) it(`${mode} clips a wait to the remaining fractional time`, async () => {
    const setup = harness();
    setup.dependencies.reader = fakeReader({fastPath: {kind: "checks", checks: [pendingCheck()]}});
    setup.time.onEmit = event => {if (event.kind === "WAITING") setup.time.now = 0.75;};
    expect(await run(mode, setup)).toMatchObject({kind: "TIMEOUT", exitCode: 5});
    expect(setup.time.sleeps).toEqual([0.25]);
    expect(setup.time.now).toBe(1);
  });

  for (const mode of modes) it(`${mode} admits early wakes and reclips each pending wait`, async () => {
    const setup = harness();
    setup.dependencies.reader = fakeReader({fastPath: {kind: "checks", checks: [pendingCheck()]}});
    setup.time.onSleep = seconds => {setup.time.now += setup.time.sleeps.length === 1 ? seconds / 2 : seconds;};
    expect(await run(mode, setup)).toMatchObject({kind: "TIMEOUT", exitCode: 5});
    expect(setup.time.sleeps).toEqual([1, 0.5]);
    expect(setup.dependencies.reader.calls.filter(call => call === "checksFastPath")).toHaveLength(2);
  });

  for (const emissionCost of [0.25, 1, 2]) it(`recomputes retry sleep after emission consumes ${emissionCost} seconds`, async () => {
    const setup = harness();
    let reads = 0;
    setup.dependencies.reader = {...fakeReader(), async pullRequest() {reads += 1; throw new WatcherQueryError(retryFailure);}};
    setup.time.onEmit = event => {if (event.kind === "RETRY") setup.time.now += emissionCost;};
    expect(await run("single", setup)).toMatchObject({kind: "TIMEOUT", reason: {kind: "status-unavailable"}, exitCode: 5});
    expect(setup.time.events).toContainEqual(expect.objectContaining({kind: "RETRY", retryInSeconds: 1}));
    expect(setup.time.sleeps).toEqual(emissionCost < 1 ? [0.75] : []);
    expect(reads).toBe(1);
  });

  for (const mode of modes) for (const first of ["pending", "retry"] as const) it(`${mode} settles ${first} work that consumes the remaining deadline`, async () => {
    const setup = harness();
    const base = fakeReader({fastPath: {kind: "checks", checks: [pendingCheck()]}});
    let reads = 0;
    setup.dependencies.reader = {...base, async pullRequest(pr) {
      reads += 1;
      setup.time.now = 2;
      if (first === "retry") throw new WatcherQueryError(retryFailure);
      return base.pullRequest(pr);
    }};
    expect(await run(mode, setup)).toMatchObject({kind: "TIMEOUT", exitCode: 5, reason: {kind: first === "retry" ? "status-unavailable" : mode === "queued-stack" ? "queued-stack" : "pending-checks"}});
    expect(setup.time.sleeps).toEqual([]);
    expect(reads).toBe(first === "retry" ? 1 : 2);
    if (first === "retry") expect(setup.time.events).toContainEqual(expect.objectContaining({kind: "RETRY", retryInSeconds: 0}));
  });

  it("does not retry an unknown forge state at exact expiry", async () => {
    const setup = harness();
    const unknown = fakeReader({facts: {mergeable: "UNKNOWN", mergeStateStatus: "UNKNOWN"}});
    const clean = fakeReader();
    setup.dependencies.reader = {...clean, pullRequest: pr => (setup.time.now === 0 ? unknown : clean).pullRequest(pr)};
    expect(await run("single", setup, {timeout: 60})).toMatchObject({kind: "TIMEOUT", exitCode: 5, reason: {kind: "status-unavailable", failure: {kind: "mergeability-unknown"}}});
    expect(setup.time.sleeps).toEqual([60]);
    expect(unknown.calls.filter(call => call === "pullRequest")).toHaveLength(2);
    expect(clean.calls.filter(call => call === "pullRequest")).toEqual([]);
  });
});

describe("admitted work retains terminal precedence", () => {
  for (const mode of modes) {
    it(`${mode} accepts readiness or completion crossing the deadline`, async () => {
      const setup = harness();
      const base = fakeReader({facts: mode === "queued-stack" ? {state: "MERGED", mergedAt: "observed"} : {}});
      setup.dependencies.reader = {...base, async pullRequest(pr) {setup.time.now = 2; return base.pullRequest(pr);}};
      expect(await run(mode, setup)).toMatchObject({kind: mode === "queued-stack" ? "COMPLETE" : "READY", exitCode: 0});
      expect(setup.time.sleeps).toEqual([]);
    });
    it(`${mode} returns a terminal status-only observation crossing the deadline`, async () => {
      const setup = harness();
      const base = fakeReader({fastPath: {kind: "checks", checks: [pendingCheck()]}});
      setup.dependencies.reader = {...base, async pullRequest(pr) {setup.time.now = 2; return base.pullRequest(pr);}};
      expect(await run(mode, setup, {}, [context(1)], true)).toMatchObject({kind: "STATUS", terminal: true, exitCode: 0, reason: "status-only", mode});
      expect(setup.time.sleeps).toEqual([]);
    });
    for (const blocker of ["conflict", "threads", "checks", "gate"] as const) it(`${mode} retains admitted ${blocker} blocker past expiry`, async () => {
      const setup = harness();
      const base = fakeReader({
        facts: blocker === "conflict" ? {mergeable: "CONFLICTING"} : blocker === "gate" ? {isDraft: true} : {},
        fastPath: {kind: "checks", checks: [blocker === "checks" ? failedCheck() : passingCheck()]},
        threads: blocker === "threads" ? [{id: "thread", firstComment: null, isBugbot: false, bugbotReviewPasses: 0}] : [],
      });
      setup.dependencies.reader = {...base, async pullRequest(pr) {setup.time.now = 2; return base.pullRequest(pr);}};
      expect(await run(mode, setup)).toMatchObject({kind: "BLOCKER", exitCode: blocker === "conflict" ? 2 : blocker === "threads" ? 3 : blocker === "checks" ? 4 : 6});
      expect(setup.time.sleeps).toEqual([]);
    });
  }

  it("keeps tier-major stack blockers after an admitted pass crosses expiry", async () => {
    const setup = harness();
    const failed = fakeReader({fastPath: {kind: "checks", checks: [failedCheck()]}});
    const conflict = fakeReader({facts: {mergeable: "CONFLICTING"}});
    setup.dependencies.reader = {...failed, async pullRequest(pr) {setup.time.now = 2; return (pr.number === 2 ? conflict : failed).pullRequest(pr);}};
    expect(await run("stack", setup, {}, [context(1), context(2)])).toMatchObject({kind: "BLOCKER", exitCode: 2, blocker: {kind: "merge-conflicts", pr: {number: 2}}});
  });
});

describe("deadline and budget precedence", () => {
  for (const mode of modes) for (const timeout of [0, 1]) {
    for (const oversleep of [0, 2]) it(`${mode} preserves poll exhaustion with timeout ${timeout} and oversleep ${oversleep}`, async () => {
      const setup = harness();
      setup.dependencies.reader = fakeReader({fastPath: {kind: "checks", checks: [pendingCheck()]}});
      setup.time.onSleep = seconds => {setup.time.now += seconds + oversleep;};
      expect(await run(mode, setup, {timeout, maxPolls: 1})).toMatchObject({kind: "BLOCKER", exitCode: 7, blocker: {failures: 0, failure: {kind: "poll-budget"}}});
      expect(setup.time.sleeps).toEqual([timeout === 0 ? 60 : 1]);
    });
    for (const retryable of [false, true]) it(`${mode} keeps terminal query errors with timeout ${timeout} and retryable ${retryable}`, async () => {
      const setup = harness();
      const failure: QueryFailure = retryable ? retryFailure : {kind: "authentication-missing", retryable: false, detail: "controlled terminal failure"};
      setup.dependencies.reader = {...fakeReader(), async pullRequest() {setup.time.now = 2; throw new WatcherQueryError(failure);}};
      expect(await run(mode, setup, {timeout, maxQueryErrors: 1})).toMatchObject({kind: "BLOCKER", exitCode: 7, blocker: {failures: 1, failure}});
      expect(setup.time.sleeps).toEqual([]);
    });
  }
  for (const mode of modes) it(`${mode} disabled timeout preserves increasing backoff and query budget`, async () => {
    const setup = harness();
    setup.dependencies.reader = {...fakeReader(), async pullRequest() {throw new WatcherQueryError(retryFailure);}};
    expect(await run(mode, setup, {timeout: 0, maxQueryErrors: 5})).toMatchObject({kind: "BLOCKER", exitCode: 7, blocker: {failures: 5, failure: retryFailure}});
    expect(setup.time.sleeps).toEqual([60, 120, 240, 300]);
  });
});

describe("queued continuation deadlines", () => {
  for (const firstMerged of [false, true]) it(`times out a partial sweep after an observed ${firstMerged ? "merged" : "open"} member`, async () => {
    const setup = harness();
    const base = fakeReader({facts: firstMerged ? {state: "MERGED", mergedAt: "observed"} : {}});
    const reads: number[] = [];
    setup.dependencies.reader = {...base, async pullRequest(pr) {reads.push(pr.number); setup.time.now = 1; return base.pullRequest(pr);}};
    expect(await run("queued-stack", setup, {}, [context(1), context(2), context(3)])).toMatchObject({kind: "TIMEOUT", exitCode: 5, reason: {kind: "queued-stack", frontier: context(firstMerged ? 2 : 1), unmergedCount: firstMerged ? 2 : 3}});
    expect(reads).toEqual(firstMerged ? [1] : [1, 1]);
    expect(setup.time.sleeps).toEqual([]);
  });

  for (const timeout of [0, 1]) it(`queued ADVANCE rechecks admission with timeout ${timeout}`, async () => {
    const setup = harness();
    const base = fakeReader();
    const reads: number[] = [];
    setup.dependencies.reader = {...base, async pullRequest(pr) {
      reads.push(pr.number);
      const facts = await base.pullRequest(pr);
      return setup.time.sleeps.length > 0 ? {...facts, state: "MERGED", mergedAt: "observed"} : facts;
    }};
    setup.time.onEmit = event => {if (event.kind === "ADVANCE") setup.time.now = 1;};
    const result = await run("queued-stack", setup, {timeout, interval: 0.25}, [context(1), context(2)]);
    expect(result).toMatchObject(timeout === 0 ? {kind: "COMPLETE", exitCode: 0} : {kind: "TIMEOUT", exitCode: 5, reason: {kind: "queued-stack", frontier: context(2), unmergedCount: 1}});
    expect(reads).toEqual(timeout === 0 ? [1, 1, 2, 2, 1, 2] : [1, 1, 2, 2, 1]);
    expect(setup.time.events).toContainEqual(expect.objectContaining({kind: "ADVANCE", frontier: context(2)}));
    expect(setup.time.sleeps).toEqual([0.25]);
  });

  it("successful queued snapshots reset query errors and skip cached merges", async () => {
    const setup = harness();
    const base = fakeReader({facts: {state: "MERGED", mergedAt: "observed"}});
    const reads: number[] = [];
    const attempts = new Map<number, number>();
    setup.dependencies.reader = {...base, async pullRequest(pr) {
      reads.push(pr.number);
      const count = (attempts.get(pr.number) ?? 0) + 1;
      attempts.set(pr.number, count);
      if (count === 1) throw new WatcherQueryError(retryFailure);
      return base.pullRequest(pr);
    }};
    expect(await run("queued-stack", setup, {timeout: 0, maxQueryErrors: 2}, [context(1), context(2)])).toMatchObject({kind: "COMPLETE", exitCode: 0});
    expect(reads).toEqual([1, 1, 2, 2]);
    expect(setup.time.sleeps).toEqual([60, 60]);
    expect(setup.time.events.filter(event => event.kind === "RETRY").map(event => event.consecutiveFailures)).toEqual([1, 1]);
  });
});
