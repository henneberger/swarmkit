"""Index the collected swarm corpus and complete the report's bibliography."""
import csv
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

def git(path, *args):
    return subprocess.check_output(['git', '-C', str(path), *args], text=True).strip()

refs = {
'hidden':'2505.11556','world':'2608.26081','copying':'2609.09150',
'gptswarm':'2402.16823','llm2swarm':'2410.11387','prune':'2410.02506',
'dropout':'2503.18891','dylan':'2310.02170','agentnet':'2504.00587',
'swarmsys':'2510.10047','swarmagentic':'2506.15672','swarmbench':'2505.04364',
'cheating':'2609.04170','maporl':'2502.18439','vote':'2508.17536',
'latentmas':'2511.20639','interlat':'2511.09149','dense':'2606.13594',
'statebridge':'2608.13317','gating':'2605.06988','terra':'2603.16910',
'labsswarm':'2603.21344','scaling':'2512.08296','equalbudget':'2604.02460',
'kimi':'2602.02276','searchswarm':'2606.09730',
'w2s':'anthropic-w2s','patterns':'anthropic-multiagent-patterns',
'oasis':'2411.11581','moltdynamics':'2602.09270','moltfunction':'2604.13052','moltsocialization':'2602.14299','moltpeer':'2602.14477','moltinformal':'2602.18832','moltillusion':'2602.07432','moltbookprotocol':'moltbook-protocol',
}
# Anchor, scope, and finding from static inspection; no experiments were run.
audit = {
'metauto-ai/gptswarm':('swarm/optimizer/edge_optimizer/optimization.py',8,'Swarm topology optimization','Policy-gradient edge optimization; execution remains constrained.'),
'yanweiyue/AgentPrune':('AgentPrune/graph/graph.py',169,'Communication component','Spatial/temporal masks; nuclear-norm term not located in inspected trainer.'),
'wangzx1219/AgentDropout':('AgentDropout/graph/graph.py',540,'Communication component','Round-dependent elimination; node-removal routine hardcodes five agents.'),
'Gen-Verse/LatentMAS':('models.py',158,'Communication component','Latent generation and cache transfer; requires model internals.'),
'deeplearning-wisc/debate-or-vote':('README.md',1,'Interaction control','Independent-vote baseline for separating sampling from communication gains.'),
'zoe-yyx/AgentNet':('AgentNet_Code/src/agentgraph.py',121,'Decentralized coordination','Success/time multiplicative edge update differs from paper EMA description.'),
'Yassellee/HiddenBench_ICML':('src/hiddenbench/simulator.py',187,'Distributed-information diagnostic','Private-profile discussion runner; named disclosure intervention not verified in code.'),
'YanwenPneg/StateBridge':('methods/state_bridge.py',211,'Communication component','Geometric alignment and continuous-prefix construction.'),
'safety-research/automated-w2s-research':('w2s_research/research_loop/tools/server_api_tools.py',254,'Research swarm','Forum and snapshot exchange between autonomous researchers.'),
'MoonshotAI/Kimi-K2.5':('README.md',43,'Orchestrated swarm','Model/report release; inspected repository does not provide PARL training implementation.'),
'doublewordai/swarm':('src/engine.py',1,'Orchestrated swarm','Independent Kimi-compatible harness; not Moonshot’s official PARL implementation.'),
'lamm-mit/SwarmWorld':('src/biofoundry/program_library.py',69,'Persistent decentralized swarm','Executable inheritance; some experiment documentation differs from latest paper setup.'),
'Search-Swarm/SearchSwarm':('harness/tool_sub_agent.py',943,'Orchestrated swarm','Concurrent worker batches and bounded briefs; no onward worker delegation.'),
'EvoMap/awesome-agent-swarm':('README.md',1,'Discovery index','Used for discovery, not as evidence of algorithm performance.'),
'davidthfarr/agent2agent':('README.md',1,'Non-LLM swarm control','Distributed-search communication simulation; implementation inventory, not reproduction.'),
'kyegomez/swarms':('swarms/structs/concurrent_workflow.py',27,'Swarm-branded implementation collection','Inspected concurrent workflow uses a thread pool; name alone does not establish emergence.'),
'cognizant-ai-lab/terralingua':('core/environment/artifact.py',1,'Persistent decentralized swarm','Persistent cultural artifacts; retention is not a truth criterion.'),
'SALT-NLP/DyLAN':('README.md',1,'Adaptive population component','Temporal contributor selection; agreement is a stopping heuristic.'),
'YaoZ720/SwarmAgenticCode':('natural_plan/_trip/pso.py',111,'Optimizer-level swarm','Textual repair velocity; centralized global best; particles are whole systems.'),
'RUC-GSAI/YuLan-SwarmIntell':('swarmbench/environment.py',134,'Decentralized swarm benchmark','Code enforces local message visibility and bounded observations.'),
'Pold87/LLM2Swarm':('DirectIntegration/controllers/main.py',267,'Robot swarm prototype','Default simulation shares all robot reports and uses remote GPT-4o.'),
}

audit.update({'camel-ai/oasis': ('oasis/social_platform/recsys.py', 168, 'Social-swarm simulation', 'Feed algorithms alter agent exposure; simulator scale does not prove knowledge creation.'), 'giordano-demarzo/moltbook-api-crawler': ('analysis_scripts/figure2_distributions.py', 1, 'Open social-swarm analysis', 'Activity distribution analysis; API caps limit full comment-history recovery.'), 'tianyi-lab/Moltbook_Socialization': ('agent_socialization/individual_semantic_drift/agent_semantic_drift.py', 1, 'Open social-swarm analysis', 'Semantic drift measures social adaptation, not independently tested skill transfer.'), 'searchsim-org/moltbook-analysis': ('README.md', 1, 'Social knowledge-diffusion audit', 'Advertised diffusion scripts absent in inspected checkout; do not claim reproduction.'), 'human-vc/moltbook-audit': ('RUNBOOK_rigor.md', 1, 'Social collective-benefit audit', 'Rigor runbook disavows earlier headline using unimplemented baseline.')})


refs.update({'conventions': '2410.08948', 'topologycollapse': '2608.15519', 'scalelimits': '2608.22884', 'microphysics': '2604.15236', 'minimalculture': '2606.30668', 'socialnorms': '2510.14401', 'generational': '2406.00392', 'behavioral': '2605.08463', 'einstein': 'einsteinarena', 'fieldexperiment': 'social-experiment', 'antipatterns': 'coordination-antipatterns', 'gensyn': 'gensyn-ai/collaborative-autoresearch-demo', 'swarmfeed': 'swarmclawai/swarmfeed', 'topocode': 'Darwin-Agent/topological-collapse-agent-societies'})
audit.update({'togethercomputer/EinsteinArena-new-SOTA': ('kissing-number/README.md', 1, 'Open collaborative-discovery artifacts', '604-vector construction independently verified here; result archive is not the social-platform implementation.'), 'Ariel-Flint-Ashery/AI-norms': ('prompting.py', 1, 'Decentralized convention formation', 'Local naming-game memory; arbitrary convention adoption is not factual discovery.'), 'Darwin-Agent/topological-collapse-agent-societies': ('llm_relay_benchmark/run_limited_relay_benchmark.py', 280, 'Population topology and evidence relay', 'Later deterministic evidence-relay tests exceed paper scope; prose does not propagate; chronology anomalies limit audit.'), 'gensyn-ai/collaborative-autoresearch-demo': ('skills/autoresearch-network/research_network.py', 391, 'Peer experiment and method sharing', 'Thresholded adoption and sender/round deduplication; local rerun is instructed, not helper-enforced.'), 'swarmclawai/swarmfeed': ('packages/api/src/lib/feed-algorithm.ts', 155, 'Social-swarm attention substrate', 'Engagement/reputation scoring and diversification; hosted service discontinued.'), 'wuzengqing001225/scale_limits_agent_societies': ('README.md', 1, 'Scale limits of social mechanisms', 'Rule-based experiments plus separate LLM response probes; some predictions fail.'), 'FLAIROx/cultural-accumulation': ('goal_seq/in_context_accumulation.py', 226, 'Non-LLM cultural-learning precursor', 'Generation loop passes demonstrations onward; trained checkpoints required for experiments.'), 'desplega-ai/agent-swarm': ('README.md', 1, 'Orchestrated swarm engineering', 'Companion to coordination postmortem; illustrative blog hooks not verified as enforced.'), 'hauertlab/swarm_llm': ('core/tools.py', 163, 'Minimal social swarm with decaying memory', 'Shared-store messaging tools; culture persistence is not correctness or isolated-search advantage.')})

papers=[]
for record in sorted((ROOT/'sources/papers').glob('*/record.json')):
    r=json.loads(record.read_text()); m=r['metadata']; folder=record.parent
    item={'kind':'paper','id':r['id'],'label':r.get('label'),'title':m.get('citation_title',[''])[0],
          'authors':m.get('citation_author',[]),'first_posted':m.get('citation_date',[''])[0],
          'reviewed_revision_date':m.get('citation_online_date',[''])[0],
          'url':m.get('og:url',[f"https://arxiv.org/abs/{r['id']}"])[0],
          'path':str(folder.relative_to(ROOT)),'cited_in_report':r['id'] in refs.values(),
          'pdf_sha256':hashlib.sha256((folder/'paper.pdf').read_bytes()).hexdigest(),
          'pdf_downloaded':(folder/'paper.pdf').exists(),'text_extracted':(folder/'paper.txt').exists()}
    papers.append(item)
posts=[]
for record in sorted((ROOT/'sources/posts').glob('*/record.json')):
    r=json.loads(record.read_text());m=r.get('metadata',{})
    posts.append({'kind':'post','id':r['id'],'url':r['url'],
                  'title':m.get('og:title',[r['id']])[0],
                  'path':str(record.parent.relative_to(ROOT)),
                  'sha256':hashlib.sha256((record.parent/'page.html').read_bytes()).hexdigest(),
                  'cited_in_report':r['id'] in refs.values()})
repos=[]
for folder in sorted((ROOT/'repositories').iterdir()):
    if not (folder/'.git').is_dir(): continue
    remote=re.sub(r'\.git$', '', git(folder,'remote','get-url','origin')); remote=remote.replace('git@github.com:', 'https://github.com/').replace('git@bitbucket.org:', 'https://bitbucket.org/'); name=re.sub(r'^https?://[^/]+/', '', remote)
    anchor,line,scope,finding=audit[name]
    assert (folder/anchor).exists(),(name,anchor)
    commit=git(folder,'rev-parse','HEAD')
    repos.append({'kind':'repository','repo':name,'url':remote,'path':str(folder.relative_to(ROOT)),
        'commit':commit,'commit_date':git(folder,'show','-s','--format=%cI','HEAD'),
        'shallow':git(folder,'rev-parse','--is-shallow-repository')=='true',
        'license_files':[p.name for p in folder.iterdir() if p.is_file() and ('license' in p.name.lower() or 'copying' in p.name.lower())],
        'scope':scope,'code_anchor':f'{anchor}#L{line}','finding':finding,'experiments_reproduced':False,'artifact_verified':name=='togethercomputer/EinsteinArena-new-SOTA'})
failures=[{'url':'https://github.com/gdemarzo/agent-wiki-copying','status':'clone_failed','reason':'Advertised repository was unavailable during collection.'},
          {'paper':'2510.10047','status':'official_code_not_located','reason':'No verified official SwarmSys implementation located.'}]
catalog={'retrieved_on':'2026-09-09','scope':'Agentic swarms; supporting interaction components and diagnostic controls explicitly classified. No knowledge-graph corpus.',
 'coverage':'Broad primary-source survey, not an exhaustive census. Public artifacts only; unavailable code recorded. PDFs and HTML are snapshots; repositories are shallow clones.',
 'method':'Parallel source review, citation tracing, latest arXiv metadata/PDF checks, and static inspection of selected implementation paths. No swarm benchmark reproduction or paid inference. One EinsteinArena construction independently verified with exact arithmetic.',
 'papers':papers,'posts':posts,'repositories':repos,'unavailable':failures,'artifact_verification':'sources/einstein-artifact-verification.json','packages':[]}
(ROOT/'sources/catalog.json').write_text(json.dumps(catalog,indent=2,ensure_ascii=False)+'\n')
with (ROOT/'sources/catalog.csv').open('w') as f:
    w=csv.writer(f);w.writerow(['kind','name','url','local_path','version_or_commit','scope'])
    for r in papers: w.writerow(['paper',r['title'],r['url'],r['path'],r['url'].split('/')[-1],'report source' if r['cited_in_report'] else 'supporting archive'])
    for r in posts: w.writerow(['post',r['title'],r['url'],r['path'],'2026-09-09 snapshot','primary blog/platform'])
    for r in repos:w.writerow(['repository',r['repo'],r['url'],r['path'],r['commit'],r['scope']])
report=ROOT/'SWARMS_REPORT.md'
text=report.read_text().split('\n## Sources\n',1)[0]+'\n## Sources\n\n<!-- REFERENCES -->\n\n## Appendix: implementation map\n\n<!-- REPOSITORIES -->\n'
byid={r['id']:r for r in papers+posts}
byid.update({r['repo']:r for r in repos})
bibliography=[]
for label in dict.fromkeys(re.findall(r'\[\^([^\]]+)\]',text)):
    if label not in refs:raise ValueError(label)
    r=byid[refs[label]]
    if r['kind']=='paper':
        authors='; '.join(r['authors'][:3])+(' et al.' if len(r['authors'])>3 else '')
        desc=f"{authors}. [{r['title']}]({r['url']}). First posted {r['first_posted']}; reviewed revision {r['reviewed_revision_date']}. [Local PDF]({r['path']}/paper.pdf)."
    elif r['kind']=='repository':
        desc=f"[{r['repo']}]({r['url']}). Source snapshot `{r['commit'][:12]}`; [local clone]({r['path']}). See implementation appendix for inspected code."
    else:desc=f"[{r['title']}]({r['url']}). Primary author/organization post; retrieved 9 September 2026. [Local snapshot]({r['path']}/page.html)."
    bibliography.append(f'[^{label}]: {desc}')
text=text.replace('<!-- REFERENCES -->','\n\n'.join(bibliography))
rows=['These are inspected source paths. One EinsteinArena output artifact was independently verified; swarm experiments were not reproduced. Links pin the collected commits; local clones preserve those commits.','',
 '| Project | Role in this review | Implementation finding |', '|---|---|---|']
for r in repos:
    route="src" if "bitbucket.org" in r["url"] else "blob"
    url=f"{r['url']}/{route}/{r['commit']}/{r['code_anchor']}"
    rows.append(f"| [{r['repo']}]({url}) · [local]({r['path']}) | {r['scope']} | {r['finding']} |")
rows+=['','SwarmSys official code was not located. The repository advertised by the copying study could not be cloned; this is recorded in the catalog rather than replaced with unrelated code.',
'','### Collection and coverage',
f"\nThe workspace contains **{len(papers)} paper PDFs with extracted text, {len(posts)} blog/platform snapshots, and {len(repos)} source-repository clones**. The [catalog](sources/catalog.json) records source versions, snapshot hashes, clone commits, local paths, and unavailable artifacts; [CSV](sources/catalog.csv) provides a compact index. Some archived papers are supporting interaction controls rather than complete swarm systems. They are not treated as evidence of swarm emergence.",
'\nSearches followed swarm-specific terms, named systems, and source references across GitHub, arXiv, and first-party research blogs. Inclusion prioritized a population interaction mechanism, swarm evaluation, or a direct control needed to assess collective knowledge. General knowledge-graph research and generic agent-workflow tutorials were excluded. This is a broad, auditable survey, not a claim to have enumerated every relevant project. Recent preprints have limited independent replication.',
'\nThe original six blog snapshots cover Anthropic’s research-swarm engineering, its weak-to-strong researcher and August peer-swarm study, Google’s scaling analysis, Kimi’s agent-swarm release, and OpenHands’ practical swarm framing. Blog implementation claims were compared with papers or source code where available. The narrative relies primarily on studies with a concrete mechanism and evaluation.']
rows += ['','### Blog and platform archive','','| Source | Local snapshot |','|---|---|']
for r in posts:
    rows.append(f"| [{r['title']}]({r['url']}) | [snapshot]({r['path']}/page.html) · [text]({r['path']}/page.txt) |")
rows += ['', 'No verified official Moltbook server repository was established. Source repositories are shallow clones with Git LFS downloads disabled; large external datasets and checkpoints are not implied to be downloaded.', '', 'The latest expansion added controlled convention formation, social-mechanism scaling, memory turnover, cultural accumulation, peer experimental sharing, feed algorithms, and checkable collaborative outputs. The search and selection record is in [expansion-scan.json](sources/expansion-scan.json).']
text=text.replace('<!-- REPOSITORIES -->','\n'.join(rows));report.write_text(text)
print(json.dumps({'papers':len(papers),'posts':len(posts),'repositories':len(repos),'references':len(bibliography)}))
