import {readFileSync,readdirSync,existsSync,writeFileSync,mkdirSync} from 'node:fs';
import {resolve} from 'node:path';
import {createHash} from 'node:crypto';

export function buildSiteFeed(root,{workflows,readme}) {
  const read=path=>readFileSync(resolve(root,path),'utf8');
  const json=path=>JSON.parse(read(path));
  const manifest=json('plugin.json');
  if(!/^\d+\.\d+\.\d+(?:[-+][a-zA-Z0-9.-]+)?$/.test(manifest.version))throw Error('Invalid package version.');
  const upstream=json('references/upstream-metadata/plugin.json');
  const inventory=json('docs/parity/inventory.json');
  const catalog=readdirSync(resolve(root,'skills'),{withFileTypes:true}).filter(d=>d.isDirectory()&&existsSync(resolve(root,'skills',d.name,'SKILL.md'))).map(d=>{
    if(!/^[a-z][a-z0-9-]*$/.test(d.name))throw Error('Invalid skill directory: '+d.name);
    const instructions=read(`skills/${d.name}/SKILL.md`);
    const frontmatter=instructions.match(/^---\r?\n([\s\S]*?)\r?\n---(?:\r?\n|$)/);
    const metadata=frontmatter ? Bun.YAML.parse(frontmatter[1]) : {};
    const recordPath=`docs/catalog/skills/${d.name}.json`;
    const record=existsSync(resolve(root,recordPath)) ? json(recordPath) : {};
    return {name:d.name,kind:d.name.startsWith('principle-')?'principle':'skill',purpose:record.purpose||metadata.description||'Read the source instructions for this skill.',ordinaryExample:record.ordinaryExample||'Read its instructions and provide a concrete task within their scope.',outputs:record.outputs||[],capabilityLimits:record.capabilityLimits||[],instructions};
  }).sort((a,b)=>a.name.localeCompare(b.name));
  const names=new Set(catalog.map(c=>c.name));
  for(const w of workflows)for(const name of w.skills)if(!names.has(name))throw Error('Workflow references missing skill: '+name);
  const sourceCommits=[...new Set(inventory.map(r=>r.upstreamCommit).filter(Boolean))];
  if(sourceCommits.length!==1)throw Error('Expected one pinned upstream source revision.');
  const releasePath=`docs/releases/${manifest.version}.md`;
  const hosts={};
  for(const row of inventory)for(const [host,verification] of Object.entries(row.verification||{})){
    hosts[host]??={};
    const status=verification.status||'unknown';
    hosts[host][status]=(hosts[host][status]||0)+1;
  }
  const payload={schemaVersion:2,workflows,readme,catalog,
    release:{version:manifest.version,upstreamVersion:upstream.version,upstreamCommit:sourceCommits[0],skillCount:catalog.length,principleCount:catalog.filter(c=>c.kind==='principle').length,playbookCount:readdirSync(resolve(root,'skills/poteto-mode/playbooks')).filter(f=>f.endsWith('.md')).length,summary:manifest.extensions?.['com.openai']?.publication?.release_notes||manifest.description,recordPath:existsSync(resolve(root,releasePath))?releasePath:null,record:existsSync(resolve(root,releasePath))?read(releasePath):null},
    compatibility:{guidance:read('docs/compatibility.md'),hostMatrix:read('docs/testing/host-matrix.md'),inventoryStatuses:hosts,inventoryEntries:inventory.length},license:read('LICENSE')};
  const revision=createHash('sha256').update(JSON.stringify(payload)).digest('hex');
  return {...payload,revision};
}

export function writeSiteFeed(root,input,{check=false}={}) {
  const feed=buildSiteFeed(root,input);
  const path=resolve(root,'docs/site/content.json');
  const output=JSON.stringify(feed,null,2)+'\n';
  if(check){if(!existsSync(path)||readFileSync(path,'utf8')!==output)throw Error('Repository site feed is stale. Run bun tools/render_workflow_examples.mjs.');}
  else {mkdirSync(resolve(root,'docs/site'),{recursive:true});if(!existsSync(path)||readFileSync(path,'utf8')!==output)writeFileSync(path,output);}
  return feed;
}
