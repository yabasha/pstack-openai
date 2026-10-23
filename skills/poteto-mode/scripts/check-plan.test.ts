import { mkdtempSync, rmSync, writeFileSync } from "node:fs";
import { join } from "node:path";
import { expect, test } from "bun:test";

const checker = join(import.meta.dir, "check-plan.mjs");
const rule = "Tests alone are not sufficient verification. Full verification requires unit evidence, live evidence, and performance evidence or justified non-applicability.";
const validPlan = [
  "# Demo", "", "## How to read this",
  "One box is one unit of work and names the evidence. Check a box only when its evidence exists. See playbooks/.", rule,
  "## Capabilities",
  "Independent workers available. Evidence `workers.log`. Capacity 1.",
  "Live control available. Evidence `control.log`.",
  "Scheduling unavailable. Evidence `schedule.log`.",
  "Remote unavailable. Evidence `remote.log`.",
  "Model selection unavailable. Evidence `model.log`.",
  "## Program checklist",
  ...["Arm the program", "Spawn owners", "PR mechanics", "Verdict and merge", "Boot recipe"].map(title => `### ${title}\n- [ ] Save \`program.log\`.`),
  "Read recorded baseline. Post a status message only on change.",
  "## Change output (PR1)", "**Depends on.** None.",
  "**Files.**\n- [ ] Edit `app.ts`.",
  "**Build.**\n- [ ] Change output. Save `diff.log`.",
  "**You see.**\n- [ ] Output matches. Save `output.log`.",
  `**Verify, unit.** ${rule}\n- [ ] Run tests. Save \`unit.log\`. Pass when tests pass.`,
  `**Verify, live.** ${rule} Status full. Lanes 1.\n- [ ] Lane 1. Regression against trunk and head. Save \`live.log\`. Pass when output matches.`,
  `**Verify, perf.** ${rule}\nNot applicable. Reason documentation-only change has no runtime path. Evidence \`scope.log\`.`,
  "**Review gate.** Independent review available. Interaction not applicable. Reason CLI output only. Evidence `scope.log`.\n- [ ] Independent reviewer checks `diff.log`. Save `review.log`. Pass when no findings remain.",
  "**Merge.**\n- [ ] Verdict at exact head. Save `verdict.log`.",
  "## Close the program\n- [ ] Report evidence and limits.",
  "## Appendix A. Prototype evidence\nRecorded separately.", "",
].join("\n");
function runPlan(example: string, expectedExit: number) {
  const directory = mkdtempSync(join(import.meta.dir, ".check-plan-test-"));
  const file = join(directory, "plan.md");
  writeFileSync(file, validPlan + example);
  try {
    const result = Bun.spawnSync([process.execPath, "--no-install", checker, file]);
    expect(result.exitCode, result.stderr.toString()).toBe(expectedExit);
    expect(Bun.file(file).size).toBe(new TextEncoder().encode(validPlan + example).length);
    return result.stderr.toString();
  } finally { rmSync(directory, {recursive: true, force: true}); }
}
test("accepts ordinary, indented and longer closing fences", () => {
  runPlan("", 0);
  for (const indent of ["", " ", "  ", "   "]) runPlan(`${indent}\`\`\`markdown\n## Example only\n${indent}\`\`\`\n`, 0);
  runPlan("```markdown\n## Example only\n````\n", 0);
});
test("accepts nested backticks and tilde info strings", () => {
  runPlan("````markdown\n```markdown\n## Example only\n```\n````\n", 0);
  runPlan("~~~markdown `info`\n## Example only\n ~~~\n", 0);
});
test("keeps mismatched, shorter and suffixed closers inside the fence", () => {
  for (const middle of ["~~~", "```", "``` info"]) runPlan(`\`\`\`\`markdown\n${middle}\n## Example only\n\`\`\`\`\n`, 0);
});
test("rejects headings and prose after a proper close", () => {
  for (const suffix of ["  ", "\t"]) expect(runPlan(`\`\`\`markdown\n## Example only\n\`\`\`${suffix}\n## Example only\n`, 1)).toContain('"## Example only" after Close the program is not an appendix');
  expect(runPlan("```markdown\nThis prose has a colon: inside code\n```\nThis prose has a colon: bad.\n", 1)).toContain("mid-sentence colon");
});
test("rejects backtick info strings containing a backtick", () => {
  expect(runPlan("```markdown `invalid`\n## Example only\n```\n", 1)).toContain('"## Example only" after Close the program is not an appendix');
});
