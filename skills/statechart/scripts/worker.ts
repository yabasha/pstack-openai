import { createHash } from "node:crypto";
import { Buffer } from "node:buffer";
import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { inspect } from "node:util";
import { checkView } from "./frontends/view.ts";
import { compile } from "./pipeline.ts";
import { check, messageOf } from "./run.ts";

const [stage, specFile, configFile, viewFile] = process.argv.slice(2);
try {
  const inputs = path.join(stage, "inputs");
  fs.mkdirSync(inputs);
  const manifest: {source: string; snapshot: string; sha256: string}[] = [];
  const snapshot = (source: string, name: string) => {
    if (!fs.lstatSync(source).isFile()) throw new Error("Inputs must be regular files: " + source);
    const bytes = fs.readFileSync(source);
    const file = path.join(inputs, name);
    fs.writeFileSync(file, bytes, {flag: "wx"});
    manifest.push({source: path.resolve(source), snapshot: name, sha256: createHash("sha256").update(bytes).digest("hex")});
    return file;
  };
  const folder = path.dirname(path.resolve(specFile));
  for (const name of fs.readdirSync(folder).sort()) {
    const file = path.join(folder, name);
    if (name.endsWith(".tla") && fs.lstatSync(file).isFile()) snapshot(file, name);
  }
  const spec = path.join(inputs, path.basename(specFile));
  if (!fs.existsSync(spec)) throw new Error("Spec must be a regular .tla file.");
  fs.mkdirSync(path.join(inputs, "config"));
  const config = snapshot(configFile, "config/" + path.basename(configFile));
  let viewPath: string | undefined;
  if (viewFile) {
    viewPath = snapshot(viewFile, "view" + path.extname(viewFile));
    if (/\bimport\s*\(|\brequire\s*\(/.test(fs.readFileSync(viewPath, "utf8"))) throw new Error("Dynamic view imports are unsupported; bundle the reviewed view before execution.");
    for (const entry of new Bun.Transpiler({loader: viewFile.endsWith(".ts") ? "ts" : "js"}).scanImports(fs.readFileSync(viewPath, "utf8")))
      if (!entry.path.startsWith("node:")) throw new Error("View imports must be reviewed node: builtins. Bundle relative or package imports into the reviewed view before execution: " + entry.path);
  }
  const view = checkView(viewPath ? await import(pathToFileURL(viewPath).href) : {}, inspect);
  const { files, exit } = compile(await check(spec, config), view);
  for (const item of manifest)
    if (createHash("sha256").update(fs.readFileSync(path.join(inputs, item.snapshot))).digest("hex") !== item.sha256)
      throw new Error("Input snapshot changed during execution; result incomplete: " + item.source);
  const draft = path.join(stage, "draft");
  fs.mkdirSync(draft);
  fs.writeFileSync(path.join(draft, "input-manifest.json"), JSON.stringify({schemaVersion: 1, inputs: manifest}, null, 2)+"\n", {flag: "wx"});
  for (const [name, parts] of files) {
    const fd = fs.openSync(path.join(draft, name), "wx");
    try {
      for (const part of parts) fs.writeSync(fd, typeof part === "string" ? Buffer.from(part) : part);
      fs.writeSync(fd, "\n");
    } finally { fs.closeSync(fd); }
  }
  fs.renameSync(draft, path.join(stage, "done"));
  process.exit(exit);
} catch (error) { console.error(messageOf(error)); process.exit(2); }
