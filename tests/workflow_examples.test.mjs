import {test, expect} from 'bun:test';
import {mkdtempSync, mkdirSync, readFileSync, writeFileSync, copyFileSync, rmSync} from 'node:fs';
import {tmpdir} from 'node:os';
import {resolve} from 'node:path';

test('a workflow edit regenerates both outputs, detects drift, and is idempotent', () => {
  const repo=resolve(import.meta.dir,'..');
  const root=mkdtempSync(resolve(tmpdir(),'pstack-workflow-sync-'));
  try {
    mkdirSync(resolve(root,'tools'),{recursive:true});
    mkdirSync(resolve(root,'docs/workflows'),{recursive:true});
    copyFileSync(resolve(repo,'tools/render_workflow_examples.mjs'),resolve(root,'tools/render_workflow_examples.mjs'));
    copyFileSync(resolve(repo,'tools/build_site_feed.mjs'),resolve(root,'tools/build_site_feed.mjs'));
    for(const file of ['plugin.json','LICENSE','references/upstream-metadata/plugin.json','docs/parity/inventory.json','docs/compatibility.md','docs/testing/host-matrix.md']){
      mkdirSync(resolve(root,file,'..'),{recursive:true});copyFileSync(resolve(repo,file),resolve(root,file));
    }
    mkdirSync(resolve(root,'skills/poteto-mode/playbooks'),{recursive:true});
    const workflows=JSON.parse(readFileSync(resolve(repo,'docs/workflows/examples.json'),'utf8'));
    workflows[0].title='Start a small project with a sync probe';
    for(const skill of new Set(workflows.flatMap(w=>w.skills))){mkdirSync(resolve(root,'skills',skill),{recursive:true});writeFileSync(resolve(root,'skills',skill,'SKILL.md'),'fixture');}
    writeFileSync(resolve(root,'docs/workflows/examples.json'),JSON.stringify(workflows));
    writeFileSync(resolve(root,'README.md'),'# Test repository\n\nKeep this introduction.\n');
    const run=(...args)=>Bun.spawnSync([process.execPath,resolve(root,'tools/render_workflow_examples.mjs'),...args]);
    expect(run('--check').exitCode).not.toBe(0);
    expect(run().exitCode).toBe(0);
    const readSite=()=>JSON.parse(readFileSync(resolve(root,'docs/site/content.json'),'utf8'));
    const prior=readSite();
    const manifest=JSON.parse(readFileSync(resolve(root,'plugin.json'),'utf8'));
    manifest.version='99.0.0';writeFileSync(resolve(root,'plugin.json'),JSON.stringify(manifest));
    writeFileSync(resolve(root,'docs/compatibility.md'),'# Updated compatibility\n\nNo workflow pass is claimed.');
    mkdirSync(resolve(root,'skills/principle-sync-probe'),{recursive:true});
    writeFileSync(resolve(root,'skills/principle-sync-probe/SKILL.md'),'---\nname: principle-sync-probe\ndescription: Check refreshed principles.\n---\n\n# Sync probe\n\nChanged source.');
    expect(run('--check').exitCode).not.toBe(0);
    expect(run().exitCode).toBe(0);
    const updated=readSite();
    expect(updated.revision).not.toBe(prior.revision);
    expect(updated.release.version).toBe('99.0.0');
    expect(updated.release.record).toBeNull();
    expect(updated.release.principleCount).toBe(prior.release.principleCount+1);
    expect(updated.catalog.find(c=>c.name==='principle-sync-probe').instructions).toContain('Changed source.');
    expect(updated.compatibility.guidance).toContain('No workflow pass is claimed.');
    expect(run('--check').exitCode).toBe(0);
    expect(run().exitCode).toBe(0);
    const readme=readFileSync(resolve(root,'README.md'),'utf8');
    const feed=readFileSync(resolve(root,'docs/workflows/site-feed.json'),'utf8');
    expect(readme).toContain('Keep this introduction.');
    expect(readme).toContain(workflows[0].title);
    expect(JSON.parse(feed).readme).toBe(readme);
    expect(JSON.parse(feed).workflows).toEqual(workflows);
    expect(run().exitCode).toBe(0);
    expect(readFileSync(resolve(root,'docs/workflows/site-feed.json'),'utf8')).toBe(feed);
    expect(run('--check').exitCode).toBe(0);
    writeFileSync(resolve(root,'docs/workflows/site-feed.json'),'{}');
    expect(run('--check').exitCode).not.toBe(0);
  }finally{rmSync(root,{recursive:true,force:true});}
});
