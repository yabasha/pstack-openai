#!/usr/bin/env bun
import fs from "node:fs";
import process from "node:process";
import path from "node:path";

const RULE =
	"Tests alone are not sufficient verification. Full verification requires unit evidence, live evidence, and performance evidence or justified non-applicability.";
const SUB_BLOCKS = [
	"Depends on.",
	"Files.",
	"Build.",
	"You see.",
	"Verify, unit.",
	"Verify, live.",
	"Verify, perf.",
	"Review gate.",
	"Merge.",
];
const PROGRAM_H3 = ["Arm the program", "Spawn owners", "PR mechanics", "Verdict and merge", "Boot recipe"];
const PROGRAM_MARKERS = ["baseline", "status message"];
const HOW_TO_READ_MARKERS = [
	"One box is one unit of work",
	"names the evidence",
	"Check a box only when its evidence exists",
	"playbooks/",
	RULE,
];
const PERF_ITEMS = ["Metric.", "Probe.", "Baseline.", "Rule."];
const BOX = /^\s*- \[[ x]\] (.*)$/;

const file = process.argv[2];
if (!file || process.argv.length !== 3) {
	console.error("Usage: bun --no-install check-plan.mjs <pstack-plan.md>");
	process.exit(2);
}

let raw;
try { raw = fs.readFileSync(file, "utf8").split(/\r?\n/); }
catch (error) { console.error(`${file}: cannot read plan (${error.code})`); process.exit(2); }
const problems = [];
const fail = (line, message) => problems.push(`${file}:${line}: ${message}`);

let start = 0;
if (raw[0] === "---") {
	start = raw.indexOf("---", 1) + 1;
}

const lines = [];
let fence = false;
for (let i = start; i < raw.length; i++) {
	const text = raw[i];
	const n = i + 1;
	if (/^```/.test(text)) fence = !fence;
	lines.push({ n, text, code: fence });
	if (fence) continue;
	const prose = text
		.replace(/`[^`]*`/g, "`")
		.replace(/!\[[^\]]*\]\([^)]*\)/g, "")
		.replace(/\]\([^)]*\)/g, "]");
	if (/[\u2013\u2014]/.test(prose)) fail(n, "long dash");
	if (/[\u2018\u2019\u201c\u201d]/.test(prose)) fail(n, "curly quote");
	if (/: \S/.test(prose)) fail(n, "mid-sentence colon");
}

const h2 = (l) => (!l.code && l.text.startsWith("## ") ? l.text.slice(3).trim() : null);
const sections = [];
for (const l of lines) {
	const title = h2(l);
	if (title !== null) sections.push({ title, n: l.n, body: [] });
	else if (sections.length) sections.at(-1).body.push(l);
}
const find = (title) => sections.find((s) => s.title === title);
const bodyText = (s) => s.body.map((l) => l.text).join("\n");
const boxes = (ls) => ls.filter((l) => !l.code && BOX.test(l.text)).map((l) => ({ n: l.n, text: l.text.match(BOX)[1] }));
// This is a pstack template validator. It never edits a plan or validates
// implementation plans owned by another workflow.
if (!find("How to read this") || !find("Program checklist")) {
	console.error(`${file}:1: not a pstack multi-phase plan; leave other workflow plans unchanged`);
	process.exit(1);
}
const capabilities = find("Capabilities");
const capabilityText = capabilities ? bodyText(capabilities) : "";
const declared = {};
for (const name of ["Independent workers", "Live control", "Scheduling", "Remote", "Model selection"]) {
	const line = capabilities?.body.find((l) => !l.code && l.text.startsWith(`${name} `));
	const match = line?.text.match(/^(.*?) (available|unavailable)\. Evidence `([^`<>]+)`\./);
	if (!match) fail(line?.n ?? 1, `${name}: missing capability evidence and available/unavailable declaration`);
	else declared[name] = { available: match[2] === "available", text: line.text, n: line.n };
}
const capacity = Number(declared["Independent workers"]?.text.match(/Capacity (\d+)\./)?.[1] ?? 0);
if (declared["Independent workers"]?.available && capacity < 1) fail(declared["Independent workers"].n, "available independent workers require observed capacity");
for (const [name, pattern] of [["Scheduling", /\/loop\s|scheduled audit/i], ["Remote", /cloud VM|remote creation/i], ["Model selection", /Ten lanes on `|explicit model|grok-4/i]]) {
	for (const line of lines) if (!line.code && pattern.test(line.text) && !declared[name]?.available) fail(line.n, `${name} claim lacks available capability evidence`);
}

const h1 = lines.findIndex((l) => !l.code && l.text.startsWith("# "));
if (h1 === -1) fail(1, "no H1 title");
const howToRead = find("How to read this");
if (!howToRead) fail(1, 'no "## How to read this" section');
if (h1 !== -1 && howToRead) {
	const intro = lines.slice(h1 + 1).filter((l) => l.n < howToRead.n && l.text.trim() !== "");
	if (intro.length >= 10) fail(lines[h1].n, `intro is ${intro.length} lines, under ten required`);
	for (const marker of HOW_TO_READ_MARKERS) {
		if (!bodyText(howToRead).includes(marker)) fail(howToRead.n, `How to read this lacks "${marker}"`);
	}
}

const program = find("Program checklist");
if (!program) fail(1, 'no "## Program checklist" section');
else {
	const h3s = program.body.filter((l) => !l.code && l.text.startsWith("### ")).map((l) => l.text.slice(4).trim());
	let cursor = 0;
	for (const name of PROGRAM_H3) {
		const at = h3s.findIndex((t, i) => i >= cursor && t.startsWith(name));
		if (at === -1) fail(program.n, `Program checklist lacks "### ${name}" in order`);
		else cursor = at + 1;
	}
	for (const marker of PROGRAM_MARKERS) {
		if (!bodyText(program).includes(marker)) fail(program.n, `Program checklist lacks "${marker}"`);
	}
}

const close = find("Close the program");
if (!close) fail(1, 'no "## Close the program" section');
const programIndex = sections.indexOf(program);
const closeIndex = sections.indexOf(close);
const prSections = programIndex === -1 || closeIndex === -1 ? [] : sections.slice(programIndex + 1, closeIndex);
if (prSections.length === 0) fail(1, "no PR sections between Program checklist and Close the program");

const report = [];
for (const pr of prSections) {
	const heads = [];
	for (const l of pr.body) {
		if (l.code) continue;
		const m = l.text.match(/^\*\*([^*]+)\*\*(.*)$/);
		if (m && SUB_BLOCKS.includes(m[1])) heads.push({ name: m[1], n: l.n, rest: m[2].trim(), lines: [] });
		else if (heads.length) heads.at(-1).lines.push(l);
	}
	const names = heads.map((h) => h.name);
	if (names.join("|") !== SUB_BLOCKS.join("|")) {
		fail(pr.n, `${pr.title}: sub-blocks are [${names.join(", ")}], expected [${SUB_BLOCKS.join(", ")}]`);
	}
	const block = (name) => heads.find((h) => h.name === name);
	const counts = {};
	for (const h of heads) counts[h.name] = boxes(h.lines).length;

	const depends = block("Depends on.");
	if (depends && depends.rest === "") fail(depends.n, `${pr.title}: Depends on names nothing`);
	for (const name of ["Files.", "Build.", "You see.", "Verify, unit.", "Merge."]) {
		const b = block(name);
		if (b && boxes(b.lines).length === 0) fail(b.n, `${pr.title}: ${name} has no box`);
	}
	for (const name of ["Verify, unit.", "Verify, live.", "Verify, perf."]) {
		const b = block(name);
		if (b && !b.rest.startsWith(RULE)) fail(b.n, `${pr.title}: ${name} does not open with the rule`);
	}

	const live = block("Verify, live.");
	if (live) {
		const status = live.rest.match(/Status (full|reduced|blocked)\./)?.[1];
		const laneCount = Number(live.rest.match(/Lanes (\d+)\./)?.[1] ?? -1);
		if (!status) fail(live.n, `${pr.title}: live requires Status full, reduced, or blocked`);
		if (status === "full" && (!declared["Live control"]?.available || !declared["Independent workers"]?.available)) fail(live.n, `${pr.title}: full live verification requires control and independent workers`);
		if (status === "full" && laneCount > capacity) fail(live.n, `${pr.title}: live lane count exceeds observed worker capacity`);
		if ((status === "reduced" || status === "blocked") && !/Reason .+\. Evidence `[^`<>]+`\./.test(live.rest)) fail(live.n, `${pr.title}: reduced or blocked live requires reason and evidence`);
		if ((status === "reduced" || status === "blocked") && /full success|fully verified|every lane.*PASS/i.test(bodyText(pr))) fail(live.n, `${pr.title}: reduced or blocked live cannot claim full success`);
		const lanes = boxes(live.lines).map((b) => ({ ...b, m: b.text.match(/^Lane (\d+)\. /) }));
		const numbers = lanes.filter((b) => b.m).map((b) => Number(b.m[1]));
		if (!Number.isInteger(laneCount) || laneCount < 0 || laneCount > 100 || numbers.length !== laneCount || numbers.some((n, i) => n !== i + 1) || (status !== "blocked" && laneCount === 0)) fail(live.n, `${pr.title}: lanes must be ordered 1 through declared count`);
		for (const lane of lanes) {
			if (!lane.m) fail(lane.n, `${pr.title}: live box is not a lane`);
			else if (!/Save `[^`<>]+`/.test(lane.text)) fail(lane.n, `${pr.title}: lane ${lane.m[1]} names no evidence artifact`);
			else if (!lane.text.includes("Pass when")) fail(lane.n, `${pr.title}: lane ${lane.m[1]} has no pass predicate`);
			const original = live.lines.find((l) => l.n === lane.n)?.text ?? "";
			if (/^\s*- \[x\]/.test(original)) {
				const receipt = lane.text.match(/Observed head `([a-f0-9]{40})`\. Evidence `([^`<>]+)`\./);
				if (!receipt) fail(lane.n, `${pr.title}: checked live requires observed head and evidence receipt, a checkbox is not proof`);
				else {
					const artifact = path.resolve(path.dirname(path.resolve(file)), receipt[2]);
					try { if (!fs.statSync(artifact).isFile() || fs.statSync(artifact).size === 0) throw new Error("empty"); }
					catch { fail(lane.n, `${pr.title}: checked live evidence receipt is missing or empty`); }
				}
			}
		}
		if (status === "blocked" && live.lines.some((l) => /^\s*- \[x\]/.test(l.text))) fail(live.n, `${pr.title}: blocked live cannot have checked success boxes`);
		if (laneCount > 0 && !/Regression.*trunk.*head/i.test(lanes[0]?.text ?? "")) fail(live.n, `${pr.title}: first lane must name regression against trunk and head`);
	}

	const perf = block("Verify, perf.");
	if (perf) {
		const text = perf.lines.map((l) => l.text).join("\n");
		const items = boxes(perf.lines).map((b) => b.text.split(" ")[0]);
		if (/Not applicable\./.test(text)) {
			if (!/Not applicable\. Reason .+\. Evidence `[^`<>]+`\./.test(text) || items.length) fail(perf.n, `${pr.title}: performance non-applicability needs separate reason and evidence, without success boxes`);
		} else if (items.join("|") !== PERF_ITEMS.join("|")) fail(perf.n, `${pr.title}: perf boxes are [${items.join(", ")}], expected [${PERF_ITEMS.join(", ")}]`);
	}

	const gate = block("Review gate.");
	if (gate) {
		const gateBoxes = boxes(gate.lines);
		const applicable = /(?:^|\. )Interaction applicable\./.test(gate.rest);
		const notApplicable = /(?:^|\. )Interaction not applicable\. Reason .+\. Evidence `[^`<>]+`\./.test(gate.rest);
		if (applicable === notApplicable) fail(gate.n, `${pr.title}: explicit interaction applicability required, with reason and evidence for non-applicability`);
		if (!declared["Independent workers"]?.available && !/Reduced review\. Reason .+\. Evidence `[^`<>]+`\./.test(gate.rest)) fail(gate.n, `${pr.title}: unavailable workers require explicit reduced review`);
		if (declared["Independent workers"]?.available && (!/Independent review available\./.test(gate.rest) || !/Independent reviewer/.test(gate.lines.map((l) => l.text).join("\n")))) fail(gate.n, `${pr.title}: independent review required when workers available`);
		if (gate.rest.startsWith("None.")) {
			if (gateBoxes.length) fail(gate.n, `${pr.title}: Review gate says None but has boxes`);
			if (applicable) fail(gate.n, `${pr.title}: applicable interaction cannot omit operator screenshot and video review`);
		} else {
			const text = gate.lines.map((l) => l.text).join("\n");
			if (gateBoxes.length === 0) fail(gate.n, `${pr.title}: Review gate has no box`);
			if (!/Save `[^`<>]+`/.test(text)) fail(gate.n, `${pr.title}: Review gate names no evidence artifact`);
			if (applicable) for (const word of ["screenshot", "video", "operator"]) if (!text.includes(word)) fail(gate.n, `${pr.title}: Review gate lacks "${word}"`);
		}
	}

	const total = boxes(pr.body).length;
	const cells = SUB_BLOCKS.filter((s) => s !== "Depends on.").map((s) => `${s.replace(/[ ,.]+/g, "-").replace(/-$/, "").toLowerCase()}=${counts[s] ?? 0}`);
	report.push(`${pr.title}  boxes=${total}  ${cells.join(" ")}`);
}

if (closeIndex !== -1) {
	const tail = sections.slice(closeIndex + 1);
	for (const s of tail) {
		if (!s.title.startsWith("Appendix")) fail(s.n, `"## ${s.title}" after Close the program is not an appendix`);
	}
	if (!tail.some((s) => s.title.includes("Prototype evidence"))) fail(close.n, 'no "## Appendix ... Prototype evidence" section');
}

for (const line of report) console.log(line);
console.log(`${prSections.length} PR sections, ${problems.length} problems`);
for (const p of problems) console.error(p);
process.exit(problems.length ? 1 : 0);
