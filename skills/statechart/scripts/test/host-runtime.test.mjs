import assert from "node:assert/strict";
import { test } from "node:test";
import { mkdtempSync, writeFileSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import path from "node:path";
import { spawnSync } from "node:child_process";
import { boundedOptions, rendererCommand } from "../host-runtime.mjs";

test("renderer selection refuses absence, relative paths and non-executable files", () => {
  const old = process.env.STATECHART_MERMAID;
  const dir = mkdtempSync(path.join(tmpdir(), "statechart-renderer-"));
  try {
    delete process.env.STATECHART_MERMAID;
    assert.throws(rendererCommand, /No renderer is downloaded/);
    process.env.STATECHART_MERMAID = "mmdc";
    assert.throws(rendererCommand, /absolute path/);
    const file = path.join(dir, "mmdc");
    writeFileSync(file, "not an executable", { mode: 0o600 });
    process.env.STATECHART_MERMAID = file;
    assert.throws(rendererCommand);
  } finally {
    if (old === undefined) delete process.env.STATECHART_MERMAID;
    else process.env.STATECHART_MERMAID = old;
    rmSync(dir, { recursive: true, force: true });
  }
});

test("selected renderer receives literal file arguments without package acquisition", () => {
  const old = process.env.STATECHART_MERMAID;
  const dir = mkdtempSync(path.join(tmpdir(), "statechart-renderer-"));
  try {
    const file = path.join(dir, "renderer with spaces");
    writeFileSync(file, "#!/bin/sh\nprintf '%s\\n' \"$@\"\n", { mode: 0o700 });
    process.env.STATECHART_MERMAID = file;
    const result = spawnSync(rendererCommand(), ["-i", "chart; literal.mmd", "-o", "chart.png"], boundedOptions());
    assert.equal(result.status, 0);
    assert.equal(result.stdout, "-i\nchart; literal.mmd\n-o\nchart.png\n");
  } finally {
    if (old === undefined) delete process.env.STATECHART_MERMAID;
    else process.env.STATECHART_MERMAID = old;
    rmSync(dir, { recursive: true, force: true });
  }
});

test("subprocess bounds cannot be removed by call-site options", () => {
  const options = boundedOptions({ timeout: 0, maxBuffer: Infinity, cwd: "/tmp" });
  assert.equal(options.timeout, 120_000);
  assert.equal(options.maxBuffer, 16 * 1024 * 1024);
  assert.equal(options.killSignal, "SIGKILL");
  assert.equal(options.cwd, "/tmp");
});
