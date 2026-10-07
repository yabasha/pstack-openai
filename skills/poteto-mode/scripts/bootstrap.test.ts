import { test, expect, spyOn } from "bun:test";
import { mkdirSync, readFileSync, writeFileSync, readdirSync, chmodSync, rmSync } from "node:fs";
import { join } from "node:path";

const scratch = join(import.meta.dir, "../../../.superpowers/sdd/2026-10-07-pstack-openai/task-12-fixtures");
const pins = { commander: "14.0.0", "bun-types": "1.3.14", typescript: "7.0.2" };
function snapshot(root: string): string {
  return JSON.stringify(readdirSync(root, { recursive: true }).sort().map(path => {
    const file = join(root, String(path));
    try { return [path, readFileSync(file).toString("base64")]; } catch { return [path]; }
  }));
}
async function check(name: string, options: { missing?: boolean; lockMismatch?: boolean; installedMismatch?: boolean; readonly?: boolean } = {}) {
  const root = join(scratch, name);
  rmSync(root, { recursive: true, force: true });
  mkdirSync(root, { recursive: true });
  writeFileSync(join(root, "bootstrap.ts"), readFileSync(join(import.meta.dir, "bootstrap.ts")));
  writeFileSync(join(root, "package.json"), readFileSync(join(import.meta.dir, "package.json")));
  let lock = readFileSync(join(import.meta.dir, "bun.lock"), "utf8");
  if (options.lockMismatch) lock = lock.replace("commander@14.0.0", "commander@13.0.0");
  writeFileSync(join(root, "bun.lock"), lock);
  if (!options.missing) for (const [name, version] of Object.entries(pins)) {
    const dir = join(root, "node_modules", name);
    mkdirSync(dir, { recursive: true });
    writeFileSync(join(dir, "package.json"), JSON.stringify({ name, version: options.installedMismatch ? "0.0.0" : version }));
  }
  if (options.readonly) chmodSync(root, 0o555);
  const before = snapshot(root);
  // Inert failure prevents the baseline from ever reaching installation or restart.
  const spawn = spyOn(Bun, "spawnSync").mockImplementation(() => { throw new Error("forbidden subprocess"); });
  let failure: unknown;
  try {
    const helper = await import(join(root, "bootstrap.ts"));
    helper.ensureDependenciesInstalled();
  } catch (error) { failure = error; }
  finally {
    const calls = spawn.mock.calls.length;
    spawn.mockRestore();
    if (options.readonly) chmodSync(root, 0o755);
    expect(snapshot(root)).toBe(before);
    expect(calls).toBe(0);
  }
  return failure;
}
test("missing_dependencies_do_not_install", async () => expect(String(await check("missing", { missing: true }))).toContain("setup required"));
test("mismatched_lock_does_not_restart", async () => expect(String(await check("lock", { lockMismatch: true }))).toContain("setup required"));
test("read_only_package_does_not_write", async () => expect(String(await check("readonly", { missing: true, readonly: true }))).toContain("setup required"));
test("mismatched_installed_version_requires_setup", async () => expect(String(await check("version", { installedMismatch: true }))).toContain("setup required"));
test("matching_metadata_succeeds_without_writes", async () => expect(await check("available")).toBeUndefined());
