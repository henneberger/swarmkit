"""Archive public research sources and shallow-clone repositories; never execute downloaded code."""
import concurrent.futures, datetime, hashlib, html, json, os, pathlib, re, subprocess, urllib.request
from html.parser import HTMLParser

ROOT = pathlib.Path(__file__).resolve().parents[1]
class Extract(HTMLParser):
    def __init__(self):
        super().__init__(); self.parts=[]; self.skip=0; self.meta={}
    def handle_starttag(self, tag, attrs):
        a=dict(attrs)
        if tag in ('script','style'): self.skip+=1
        if tag=='meta': self.meta.setdefault(a.get('name',a.get('property','')),[]).append(a.get('content',''))
        if tag in ('p','div','h1','h2','h3','li','br','section'): self.parts.append('\n')
    def handle_endtag(self, tag):
        if tag in ('script','style'): self.skip=max(0,self.skip-1)
    def handle_data(self, data):
        if not self.skip: self.parts.append(data)
    def text(self): return re.sub(r'\n\s*\n+', '\n\n', ''.join(self.parts))

def download(url, dest):
    if dest.exists() and dest.stat().st_size: return {'url':url,'path':str(dest.relative_to(ROOT)),'cached':True,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}
    req=urllib.request.Request(url,headers={'User-Agent':'ResearchArchive/1.0 (personal literature review)'})
    try:
        with urllib.request.urlopen(req,timeout=70) as r: data=r.read(); final=r.url
        if dest.suffix=='.pdf' and not data.startswith(b'%PDF'): raise ValueError('Not a PDF')
        dest.parent.mkdir(parents=True,exist_ok=True); dest.write_bytes(data)
        return {'url':url,'resolved_url':final,'path':str(dest.relative_to(ROOT)),'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    except Exception as e: return {'url':url,'error':str(e)}

def paper(item):
    ident=item['id']; base=ROOT/'sources/papers'/ident; base.mkdir(parents=True,exist_ok=True)
    out=dict(item); out['artifacts']=[]
    a=download('https://arxiv.org/abs/'+ident,base/'abstract.html'); out['artifacts'].append(a)
    if 'error' not in a:
        p=Extract(); p.feed((base/'abstract.html').read_text(errors='replace'))
        out['metadata']=p.meta; (base/'abstract.txt').write_text(p.text())
    a=download('https://arxiv.org/pdf/'+ident,base/'paper.pdf'); out['artifacts'].append(a)
    if 'error' not in a:
        r=subprocess.run(['pdftotext','-layout',str(base/'paper.pdf'),str(base/'paper.txt')],capture_output=True,text=True)
        out['text_extraction_ok']=r.returncode==0
    (base/'record.json').write_text(json.dumps(out,indent=2)); return out

def post(item):
    base=ROOT/'sources/posts'/item['id']; base.mkdir(parents=True,exist_ok=True)
    out=dict(item); a=download(item['url'],base/'page.html'); out['artifact']=a
    if 'error' not in a:
        p=Extract(); p.feed((base/'page.html').read_text(errors='replace')); (base/'page.txt').write_text(p.text()); out['metadata']=p.meta
    (base/'record.json').write_text(json.dumps(out,indent=2)); return out

def repo(item):
    out=dict(item); target=ROOT/'repositories'/item['repo'].replace('/','__')
    if not (target/'.git').exists():
        try:
            r=subprocess.run(['git','clone','--depth','1',item.get('url','https://github.com/'+item['repo'])+'.git',str(target)],capture_output=True,text=True,timeout=240,env={**os.environ,'GIT_TERMINAL_PROMPT':'0','GIT_LFS_SKIP_SMUDGE':'1'})
            if r.returncode: out['error']=r.stderr[-1500:]; return out
        except Exception as e: out['error']=str(e); return out
    out['path']=str(target.relative_to(ROOT)); out['commit']=subprocess.check_output(['git','-C',str(target),'rev-parse','HEAD'],text=True).strip()
    out['commit_date']=subprocess.check_output(['git','-C',str(target),'show','-s','--format=%cI','HEAD'],text=True).strip()
    out['licenses']=[str(p.relative_to(target)) for p in target.glob('*') if p.is_file() and p.name.lower().startswith(('license','copying'))]
    return out

if __name__=='__main__':
    import argparse
    ap=argparse.ArgumentParser(); ap.add_argument('kind',choices=['papers','posts','repos']); args=ap.parse_args()
    plan=json.loads((ROOT/'sources/collection-plan.json').read_text()); fn={'papers':paper,'posts':post,'repos':repo}[args.kind]
    results=[]
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        for result in pool.map(fn,plan[args.kind]):
            results.append(result); print(result.get('id',result.get('repo')), 'ERROR' if 'error' in result else 'done',flush=True)
            (ROOT/'sources'/f'{args.kind}-manifest.json').write_text(json.dumps({'retrieved_at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'items':results},indent=2))
