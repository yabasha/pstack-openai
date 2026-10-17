import { createHash } from "node:crypto";
import { copyFileSync, lstatSync, mkdirSync, mkdtempSync, readFileSync, realpathSync, rmSync } from "node:fs";
import { tmpdir } from "node:os";
import { dirname, isAbsolute, join, relative, resolve } from "node:path";
import { fileURLToPath } from "node:url";

const root = resolve(dirname(fileURLToPath(import.meta.url)), "..");
const manifest = JSON.parse(readFileSync(join(root, "plugin.json"), "utf8"));
const output = resolve(process.argv[2] ?? join(root, "..", "pstack-openai-releases"));
const sha256 = (bytes) => createHash("sha256").update(bytes).digest("hex");

function run(command, options = {}) {
  const result = Bun.spawnSync(command, { cwd: root, ...options });
  if (result.exitCode !== 0) {
    throw new Error(`${command[0]} failed: ${result.stderr.toString()}${result.stdout.toString()}`);
  }
  return result.stdout;
}

if (!/^\d+\.\d+\.\d+(?:-[0-9A-Za-z.-]+)?$/.test(manifest.version)) {
  throw new Error("A semantic package version is required.");
}
const outputRelative = relative(root, output);
if (!outputRelative || (!outputRelative.startsWith("..") && !isAbsolute(outputRelative))) {
  throw new Error("Write release artifacts outside the source directory.");
}

const ui = manifest.extensions["com.openai"].interface;
for (const [key, limit] of [["displayName", 30], ["shortDescription", 30], ["longDescription", 4000], ["developerName", 80]]) {
  if (typeof ui[key] !== "string" || !ui[key].trim() || ui[key].length > limit) {
    throw new Error(`Invalid listing field: ${key}`);
  }
}
const prompts = typeof ui.defaultPrompt === "string" ? [ui.defaultPrompt] : ui.defaultPrompt;
if (!Array.isArray(prompts) || prompts.length < 1 || prompts.length > 3 ||
    prompts.some((p) => typeof p !== "string" || !p.trim() || p.length > 128 || /[\r\n]/.test(p)) ||
    new Set(prompts.map((p) => p.trim().replace(/\s+/g, " "))).size !== prompts.length) {
  throw new Error("Invalid listing starter prompts.");
}

// New preparation files are explicit so unrelated untracked files never enter a release.
const additions = ["CHANGELOG.md", "docs/publication.md", "tools/package_release.mjs"];
const tracked = run(["git", "ls-files", "-z"]).toString().split("\0").filter(Boolean);
const paths = [...new Set([...tracked, ...additions])].filter((path) =>
  !path.startsWith(".superpowers/")
).sort();
const entries = [];
for (const path of paths) {
  if (path.split("/").some((part) => [".git", "node_modules", ".DS_Store", ".app.json"].includes(part)) ||
      path.split("/").some((part) => part === ".env" || part.startsWith(".env.")) || /[\r\n]/.test(path)) {
    throw new Error(`Unsafe release member: ${path}`);
  }
  const full = join(root, path);
  if (!lstatSync(full).isFile() || relative(root, realpathSync(full)).startsWith("..")) {
    throw new Error(`Release member is not a contained regular file: ${path}`);
  }
  const bytes = readFileSync(full);
  if (path.endsWith("plugin.json")) {
    const data = JSON.parse(bytes.toString());
    if (data.apps != null || data.extensions?.["com.openai"]?.apps != null) {
      throw new Error(`Public uploads cannot contain app bindings: ${path}`);
    }
  }
  if (!path.endsWith(".png") && /-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----|\bgh[pousr]_[A-Za-z0-9]{30,}|\bsk-(?:proj-)?[A-Za-z0-9_-]{30,}/.test(bytes.toString())) {
    throw new Error(`Credential-like content requires review: ${path}`);
  }
  entries.push({ path, bytes: bytes.length, sha256: sha256(bytes) });
}

for (const key of ["logo", "composerIcon"]) {
  const path = ui[key]?.replace(/^\.\//, "");
  if (!entries.some((entry) => entry.path === path)) throw new Error(`Missing ${key} asset`);
  const bytes = readFileSync(join(root, path));
  const size = bytes.readUInt32BE(16);
  if (bytes.subarray(0, 8).toString("hex") !== "89504e470d0a1a0a" ||
      size !== bytes.readUInt32BE(20) || size < (key === "logo" ? 256 : 48) || size > 4096 || bytes.length > 5 * 1024 * 1024) {
    throw new Error(`Invalid square PNG ${key} asset`);
  }
}

mkdirSync(output, { recursive: true });
const staging = mkdtempSync(join(tmpdir(), "pstack-release-"));
try {
  const archive = join(staging, `${manifest.name}-${manifest.version}-candidate.zip`);
  run(["zip", "-X", "-q", archive, "-@"], { stdin: new TextEncoder().encode(paths.join("\n") + "\n") });
  run(["unzip", "-tqq", archive]);
  const packageRoot = join(staging, "package");
  mkdirSync(packageRoot);
  run(["unzip", "-q", archive, "-d", packageRoot]);
  run(["python3", "-B", join(packageRoot, "tools/validate_package.py"), "--root", packageRoot,
    "--inventory", join(packageRoot, "docs/parity/inventory.json")]);
  const archived = run(["unzip", "-Z1", archive]).toString().trim().split("\n").sort();
  if (JSON.stringify(archived) !== JSON.stringify(paths)) throw new Error("Archive inventory mismatch");
  const packagedManifest = JSON.parse(run(["unzip", "-p", archive, "plugin.json"]).toString());
  if (JSON.stringify(packagedManifest) !== JSON.stringify(manifest)) throw new Error("Archived manifest mismatch");
  run(["python3", "-B", "-c", `
import hashlib, json, sys, zipfile
expected = json.load(sys.stdin)
with zipfile.ZipFile(sys.argv[1]) as archive:
    for entry in expected:
        content = archive.read(entry['path'])
        if len(content) != entry['bytes'] or hashlib.sha256(content).hexdigest() != entry['sha256']:
            raise SystemExit('Archived file changed during packaging: ' + entry['path'])
`, archive], { stdin: new TextEncoder().encode(JSON.stringify(entries)) });
  const digest = sha256(readFileSync(archive));
  const destination = join(output, `${manifest.name}-${manifest.version}-${digest.slice(0, 12)}-candidate.zip`);
  copyFileSync(archive, destination);
  const missingURLs = ["websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"].filter((key) => !ui[key]);
  const inventory = {
    kind: "pstack-publication-candidate", name: manifest.name, version: manifest.version,
    sourceCommit: run(["git", "rev-parse", "HEAD"]).toString().trim(),
    sourceHasChanges: Boolean(run(["git", "status", "--porcelain"]).toString().trim()),
    sha256: digest, submissionReady: false, missingURLs,
    note: "Preparation archive only. Resolve docs/publication.md before upload. Historical evidence is included and remains bound to its original revision.",
    files: entries,
  };
  await Bun.write(`${destination}.inventory.json`, JSON.stringify(inventory, null, 2) + "\n");
  await Bun.write(`${destination}.sha256`, `${digest}  ${destination.split("/").at(-1)}\n`);
  console.log(JSON.stringify({ archive: destination, files: paths.length, bytes: lstatSync(destination).size, sha256: digest, submissionReady: false, missingURLs }, null, 2));
} finally {
  rmSync(staging, { recursive: true, force: true });
}
