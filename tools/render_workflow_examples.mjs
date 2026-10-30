import {readFileSync, writeFileSync, existsSync} from 'node:fs';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';
import {writeSiteFeed} from './build_site_feed.mjs';

const root = resolve(import.meta.dir, '..');
const workflows = JSON.parse(readFileSync(resolve(root, 'docs/workflows/examples.json'), 'utf8'));
const start = '<!-- workflow-examples:start -->';
const end = '<!-- workflow-examples:end -->';
const levels = ['Simple', 'Intermediate', 'Advanced'];
const link = name => `[\`${name}\`](skills/${name}/SKILL.md)`;
const lines = [start, '', '## Workflow examples', '',
  'Choose a scenario and send its prompts in order. Review each result before continuing. These examples describe intended outputs, not observed host results. Check [compatibility](docs/compatibility.md) for available tools and current verification limits.', '',
  'Keep one controller responsible for the task. Workers, isolation, tool installation, external actions, and publication require the relevant host capabilities and authorization.', '',
  ...levels.map(level => `- [${level}](#${level.toLowerCase()}-workflows): ${workflows.filter(w => w.level === level).map(w => w.title[0].toLowerCase() + w.title.slice(1)).join('; ')}.`), ''];
const ids = new Set();
for (const level of levels) {
  lines.push(`### ${level} workflows`, '');
  for (const w of workflows.filter(w => w.level === level)) {
    if (ids.has(w.id)) throw new Error(`Duplicate workflow: ${w.id}`);
    ids.add(w.id);
    for (const name of w.skills) if (!existsSync(resolve(root, `skills/${name}/SKILL.md`))) throw new Error(`Missing skill: ${name}`);
    lines.push(`#### ${w.title}`, '', w.goal, '', `Skills: ${w.skills.map(link).join(', ')}.`, '');
    for (const [i, step] of w.steps.entries()) {
      lines.push(`**${i + 1}. ${step.title}**`, '', '```text', step.prompt, '```', '', `Expected output: ${step.output}`, '');
    }
    lines.push(`Principle in practice: ${w.principle}`, '', `Completion check: ${w.done}`, '');
  }
}
if (ids.size !== workflows.length) throw new Error('Every workflow must have a supported difficulty level.');
lines.push('The [website workflow section](https://pstack-openai.yabasha.chatgpt.site/#workflows) uses the same [workflow source](docs/workflows/examples.json). Changes pushed to `main` automatically regenerate this README and the site feed through [GitHub Actions](.github/workflows/sync-workflows.yml). The site loads that feed on page load and checks every five minutes while open. It keeps its published snapshot if the feed is unavailable. For local edits, run `bun tools/render_workflow_examples.mjs`; use `bun tools/render_workflow_examples.mjs --check` to detect drift. See [automatic sync](docs/workflows/automatic-sync.md) for scope and recovery.', '', end);
const block = lines.join('\n');
const path = resolve(root, 'README.md');
const current = readFileSync(path, 'utf8');
const begin = current.indexOf(start);
const finish = current.indexOf(end);
if ((begin < 0) !== (finish < 0) || (begin >= 0 && finish < begin)) throw new Error('Invalid workflow markers.');
const next = begin < 0 ? current.trimEnd() + '\n\n' + block + '\n' : current.slice(0, begin) + block + current.slice(finish + end.length);
const payload = {schemaVersion: 1, workflows, readme: next};
const revision = createHash('sha256').update(JSON.stringify(payload)).digest('hex');
const feed = JSON.stringify({...payload, revision}, null, 2) + '\n';
const feedPath = resolve(root, 'docs/workflows/site-feed.json');
if (process.argv.includes('--check')) {
  if (next !== current) throw new Error('README workflows are stale. Run bun tools/render_workflow_examples.mjs.');
  if (!existsSync(feedPath) || readFileSync(feedPath, 'utf8') !== feed) throw new Error('Site feed is stale. Run bun tools/render_workflow_examples.mjs.');
} else {
  if (next !== current) writeFileSync(path, next);
  if (!existsSync(feedPath) || readFileSync(feedPath, 'utf8') !== feed) writeFileSync(feedPath, feed);
}
console.log(`${workflows.length} workflows match the README and site feed (${revision.slice(0, 7)}).`);
writeSiteFeed(root,{workflows,readme:next},{check:process.argv.includes('--check')});
