import { readFileSync } from "node:fs";
import { join } from "node:path";

const pins = { commander: "14.0.0", "bun-types": "1.3.14", typescript: "7.0.2" } as const;

// Keep the caller API, but setup is always an explicit operator action.
export function ensureDependenciesInstalled(): void {
  try {
    const manifest = JSON.parse(readFileSync(join(import.meta.dir, "package.json"), "utf8"));
    // Bun's text lockfile is JSON with trailing commas.
    const lock = JSON.parse(readFileSync(join(import.meta.dir, "bun.lock"), "utf8").replace(/,\s*([}\]])/g, "$1"));
    for (const [name, version] of Object.entries(pins)) {
      const requested = manifest.dependencies?.[name] ?? manifest.devDependencies?.[name];
      if (requested !== version) throw new Error(`${name} must be pinned to ${version}`);
      if (lock.packages?.[name]?.[0] !== `${name}@${version}`) throw new Error(`${name} lock resolution must be ${version}`);
      const installed = JSON.parse(readFileSync(join(import.meta.dir, "node_modules", name, "package.json"), "utf8"));
      if (installed.name !== name || installed.version !== version) throw new Error(`${name} installed version must be ${version}`);
    }
  } catch (error) {
    throw new Error("Helper setup required: prepare a writable dependency copy using docs/testing/helper-setup.md. " + String(error));
  }
}
