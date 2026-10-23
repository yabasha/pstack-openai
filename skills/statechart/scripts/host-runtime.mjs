import fs from "node:fs";
import path from "node:path";

export function boundedOptions(extra = {}) {
  return { ...extra, encoding: "utf8", timeout: 120_000, killSignal: "SIGKILL", maxBuffer: 16 * 1024 * 1024 };
}

export function rendererCommand() {
  const command = process.env.STATECHART_MERMAID;
  if (!command || !path.isAbsolute(command))
    throw new Error("PNG rendering blocked: set STATECHART_MERMAID to an absolute path to a reviewed local mmdc executable. No renderer is downloaded.");
  const resolved = fs.realpathSync(command);
  if (!fs.statSync(resolved).isFile()) throw new Error("STATECHART_MERMAID must name a local executable file.");
  fs.accessSync(resolved, fs.constants.X_OK);
  return resolved;
}
