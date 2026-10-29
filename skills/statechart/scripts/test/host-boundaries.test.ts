import assert from "node:assert/strict";
import { spawnSync } from "node:child_process";
import { createHash } from "node:crypto";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { test } from "node:test";

const here = import.meta.dirname;
const cli = path.join(here, "../statechart.ts");
const corpus = path.join(here, "corpus/Login");
const hash = (bytes: Buffer) => createHash("sha256").update(bytes).digest("hex");
function fixture() {
  const scratch = fs.mkdtempSync(path.join(os.tmpdir(), "statechart-port-boundary-"));
  const input = path.join(scratch, "Login");
  fs.cpSync(corpus, input, { recursive: true });
  return { scratch, input, out: path.join(scratch, "out") };
}
function run(f: ReturnType<typeof fixture>, {view, preload, env = {}}: {view?: string; preload?: string; env?: NodeJS.ProcessEnv} = {}) {
  return spawnSync(process.execPath, ["--no-install", ...(preload ? ["--preload", preload] : []), cli, path.join(f.input, "Login.tla"), "--out", f.out, ...(view ? ["--view", view] : [])], {
    encoding: "utf8", timeout: 30_000, maxBuffer: 16 * 1024 * 1024,
    env: {...process.env, JAVA: path.join(here, "java.ts"), TLA2TOOLS: path.join(here, "java.ts"), STATECHART_REPLAY: corpus, ...env},
  });
}

test("the compiler binds snapshots before a view changes the original inputs", () => {
  const f = fixture();
  try {
    const model = path.join(f.input, "Login.tla"), config = path.join(f.input, "Login.cfg");
    const original = new Map([[model, hash(fs.readFileSync(model))], [config, hash(fs.readFileSync(config))]]);
    const module = path.join(f.input, "Extra.tla");
    fs.writeFileSync(module, "---- MODULE Extra ----\nValue == 1\n====\n");
    original.set(module, hash(fs.readFileSync(module)));
    const view = path.join(f.input, "view.mjs");
    fs.writeFileSync(view, `import fs from "node:fs";\nfs.writeFileSync(${JSON.stringify(model)}, "changed model");\nfs.writeFileSync(${JSON.stringify(config)}, "changed config");\n` + fs.readFileSync(path.join(corpus, "view.mjs"), "utf8"));
    original.set(view, hash(fs.readFileSync(view)));
    const r = run(f, {view});
    assert.equal(r.status, 0, r.stderr);
    const manifest = JSON.parse(fs.readFileSync(path.join(f.out, "input-manifest.json"), "utf8"));
    for (const entry of manifest.inputs) assert.equal(entry.sha256, original.get(entry.source));
    assert.equal(manifest.inputs.length, 4);
    assert.notEqual(hash(fs.readFileSync(model)), original.get(model));
  } finally { fs.rmSync(f.scratch, {recursive: true, force: true}); }
});

for (const statement of ['import "./other.mjs";', 'import "unapproved-package";', 'await import("node:fs");'])
  test(`view snapshot rejects unsupported import: ${statement}`, () => {
    const f = fixture();
    try {
      const view = path.join(f.input, "view.mjs");
      fs.writeFileSync(view, statement + '\nexport const state = () => "State";\n');
      const r = run(f, {view});
      assert.equal(r.status, 2);
      assert.match(r.stderr, /imports|bundle/i);
      assert.equal(fs.existsSync(f.out), false);
    } finally { fs.rmSync(f.scratch, {recursive: true, force: true}); }
  });

test("whole-run expiry reports incomplete exit 2 and publishes no output", () => {
  const f = fixture();
  try {
    const preload = path.join(f.scratch, "deadline.mjs");
    fs.writeFileSync(preload, 'const original = globalThis.setTimeout; globalThis.setTimeout = (fn, ms, ...args) => original(fn, ms === 300000 ? 1 : ms, ...args);\n');
    const r = run(f, {preload});
    assert.equal(r.status, 2, r.stderr);
    assert.match(r.stderr, /Whole-run deadline.*incomplete/);
    assert.equal(fs.existsSync(f.out), false);
  } finally { fs.rmSync(f.scratch, {recursive: true, force: true}); }
});

test("missing explicit local toolchain blocks execution without dependency installation", () => {
  const f = fixture();
  try {
    const r = run(f, {env: {JAVA: "", TLA2TOOLS: ""}});
    assert.equal(r.status, 2);
    assert.match(r.stderr, /separately reviewed local files.*No dependencies are installed/);
    assert.equal(fs.existsSync(f.out), false);
  } finally { fs.rmSync(f.scratch, {recursive: true, force: true}); }
});

test("combined subprocess output above 16 MiB is incomplete and never published", () => {
  const f = fixture();
  try {
    const java = path.join(f.scratch, "flood-java");
    fs.writeFileSync(java, '#!/usr/bin/env bun\nprocess.stdout.write("x".repeat(20 * 1024 * 1024));\nsetInterval(() => {}, 1000);\n', {mode: 0o755});
    const r = run(f, {env: {JAVA: java}});
    assert.equal(r.status, 2, r.stderr);
    assert.match(r.stderr, /output exceeded 16 MiB; result incomplete/);
    assert.equal(fs.existsSync(f.out), false);
  } finally { fs.rmSync(f.scratch, {recursive: true, force: true}); }
});
