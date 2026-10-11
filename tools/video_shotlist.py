# Writes tools/video-shotlist.js: every G4 ELA video slot
# with its repo path, whether the .mp4 already exists, and the clip script. Feeds the Video Studio page.
import json,os,re,glob,gzip,base64,html
R=os.path.expanduser('~/mnt/optima-4th-ela')
os.chdir(R)
man=json.load(open('video-manifest.json'))
titles={}
# On-screen cards for the Video Studio: what each section of the lesson shows,
# so a film can put it on screen (DOL sentences, word parts, the grammar and
# spelling rule, the reading move, Pause & Think stops, chapter questions,
# the writing focus, and the chapter's picture).
def _t(h): return html.unescape(re.sub(r'\s+',' ',re.sub(r'<[^>]+>',' ',h))).strip()
PLATES=set(os.listdir('assets/plates')) if os.path.isdir('assets/plates') else set()
def plateFor(f,src,title):
    m=re.match(r'lesson-(\d+)-(\d+)-([a-z]+)',f)
    if not m: return ''
    book=m[3]
    ch=re.search(r'\(Ch\.\s*([\d\s&,-]+)\)',title)
    if ch:
        nums=re.findall(r'\d+',ch[1]); n=book+'-ch'+'-'.join(nums)+'.png'
        if n in PLATES: return 'plates/'+n
    for ext in ('jpg','png'):
        n=f'{book}-{m[1]}-{m[2]}.{ext}'
        if n in PLATES: return 'plates/'+n
    return ''
def cardsFor(f,src,key):
    C={}
    m=re.match(r'lesson-(\d+)-(\d+)',f)
    if m and os.path.exists(f'data/lesson-{m[1]}-{m[2]}.json'):
        D=json.load(open(f'data/lesson-{m[1]}-{m[2]}.json',encoding='utf-8'))
        n=D.get('notes',{})
        for k in ('wgrd','wordParts','grammar','spelling'):
            if n.get(k): C[k]=n[k]
        dol=D.get('dol') or {}
        C['dol']=[{'raw':v.get('raw',''),'fixed':v.get('fixed',''),'why':v.get('why','')} for k,v in sorted(dol.items()) if isinstance(v,dict) and v.get('raw')]
    C['pauses']=[_t(x) for x in re.findall(r'class="socratic-q">(.*?)</p>',src,re.S)]
    C['chapterQs']=[_t(x) for x in re.findall(r'<div class="q-text"><span class="q-num">\d+</span>(.*?)</div>',src,re.S)]
    fm=re.search(r'Today(?:’|&rsquo;|\')s focus:\s*(?:</[^>]+>)?(.*?)</div>',src,re.S)
    if fm: C['focus']=_t(fm[1])
    nm=re.search(r'<!-- NOW YOU TRY -->(.*?)<!--',src,re.S)
    if nm:
        nt=re.sub(r'^.*?Now you try\.?\s*','',_t(nm[1]))
        nt=re.sub(r'\s*Write below\.?\s*$','',nt)
        nt=re.sub(r'^Use what Sam showed you\.\s*Borrow a sentence frame if you want\.\s*','',nt)
        if nt: C['nowTry']=nt[:400]
    rs=re.search(r'class="rwm-sentence">(.*?)</div>',src,re.S)
    if rs: C['rwm']=_t(rs[1])
    tt=re.search(r'<title>([^<]*)',src); C['plate']=plateFor(f,src,html.unescape(tt[1]) if tt else '')
    return {k:v for k,v in C.items() if v}
for f in glob.glob('lesson-*.html'):
    m=re.match(r'lesson-(\d+)-(\d+|fluency)',f)
    if not m: continue
    key=f"{m[1]}-{m[2]}"
    t=re.search(r'<title>([^<]*)',open(f,encoding='utf-8',errors='ignore').read())
    t=html.unescape(t[1]) if t else f
    t=t.replace('Optima Academy Online — ','').replace(' (Sparkle)','')
    src=open(f,encoding='utf-8',errors='ignore').read()
    n=re.search(r'class="vp-notes">(.*?)</div>',src,re.S)
    notes=''
    if n:
        notes=html.unescape(re.sub(r'<[^>]+>','',n[1])).strip()
        notes=re.sub(r'^Teacher recording notes:\s*','',notes)
        notes=re.sub(r'\s+',' ',notes)
    words=[]
    for fm in re.finditer(r'class="flip-card-front">(.*?)class="fc-def">(.*?)</div>',src,re.S):
        em=re.search(r'class="fc-emoji">(.*?)</div>',fm[1],re.S); wd=re.search(r'class="fc-word">(.*?)</div>',fm[1],re.S)
        if wd: words.append({'w':html.unescape(re.sub(r'<[^>]+>','',wd[1])).strip(),'d':html.unescape(re.sub(r'<[^>]+>','',fm[2])).strip(),'e':html.unescape(em[1]).strip() if em else ''})
    titles[key]={'title':t,'file':f,'notes':notes,'words':words,'cards':cardsFor(f,src,key)}
def exists(p): return os.path.exists('assets/video/'+p+'.mp4')
lessons=[]
for k,v in man.items():
    m=re.match(r'g4ela-(\d+)-(\w+)',k); w=int(m[1]); d=m[2]
    key=f"{w}-{d}"
    L={'w':w,'d':d,'title':titles.get(key,{}).get('title',f'Lesson {w}.{d}'),'file':titles.get(key,{}).get('file',''),
       'clips':[{'id':'lesson','label':'Lesson video','path':k,'done':exists(k) or v['status']=='ready','script':titles.get(key,{}).get('notes',''),'notes':True}]}
    dj=f'data/lesson-{w}-{d}.json'
    if os.path.exists(dj):
        D=json.load(open(dj)); tr=D.get('transcripts',{})
        for sid,s in D.get('media',{}).items():
            if s.get('kind') not in ('audio','video') or not s.get('path'): continue
            L['clips'].append({'id':sid,'label':s.get('label',sid),'path':s['path'],'done':exists(s['path']),'script':tr.get(sid,'')})
    lessons.append(L)
lessons.sort(key=lambda L:(L['w'],99 if L['d']=='fluency' else int(L['d'])))
# a week's vocabulary words (they're taught on day 1): every lesson in the week gets them, for the studio's word cards
wk={}
for k,v in titles.items():
    for x in v.get('words',[]):
        lst=wk.setdefault(k.split('-')[0],[])
        if all(y['w'].lower()!=x['w'].lower() for y in lst): lst.append(x)
for L in lessons: L['cards']=titles.get(f"{L['w']}-{L['d']}",{}).get('cards',{})
for L in lessons: L['words']=titles.get(f"{L['w']}-{L['d']}",{}).get('words') or wk.get(str(L['w']),[])
poems=[('Hope Is the Thing with Feathers','hope-is-the-thing-with-feathers','Mrs. Frisby'),('Who Has Seen the Wind?','who-has-seen-the-wind','Anne of Green Gables'),('There Will Come Soft Rains','there-will-come-soft-rains','Number the Stars'),('Sympathy','sympathy','Freedom Train'),('The Forest Remembers','forest-remembers','Prince Caspian')]
def poemScript(slug):
    f=os.path.join(R,'Planning docs','teacher-video-scripts',f'g4-teacher-scripts-poem-{slug}.md')
    if not os.path.exists(f): return ''
    t=open(f,encoding='utf-8').read()
    m=re.search(r'^## [^\n]*\n(.*)',t,re.S|re.M)
    return (m.group(1) if m else t).strip()
# a poem with a whole-poem film for its first poetry day (Number the Stars)
fullpoems=[('There Will Come Soft Rains','there-will-come-soft-rains','Number the Stars')]
extra={'poems':[{'id':'poem','label':f'{t} ({b})','path':'poem/'+s,'done':exists('poem/'+s),'script':''} for t,s,b in poems]+
 [{'id':'poem-full','label':f'{t}: whole poem, first poetry day ({b})','path':'poem/'+s+'-full','done':exists('poem/'+s+'-full'),'script':poemScript(s)} for t,s,b in fullpoems],
 'teacher':[{'id':'scrapbook','label':'Anne Character Growth Scrapbook — teacher video','path':'teacher/g4ela-anne-scrapbook','done':exists('teacher/g4ela-anne-scrapbook'),'script':''}]}
teacher={}
for f in sorted(glob.glob(os.path.join(R,'Planning docs','teacher-video-scripts','g4-teacher-scripts-*.md'))):
    k=re.search(r'g4-teacher-scripts-(\d+-(?:\d|fluency))\.md$',f)
    if k: teacher[k.group(1)]=open(f,encoding='utf-8').read()
extra['teacherDocs']=teacher
out=json.dumps({'lessons':lessons,**extra},ensure_ascii=False,separators=(',',':'))
open(os.path.join(R,'tools','video-shotlist.js'),'w',encoding='utf-8').write('/* generated by tools/video_shotlist.py: rerun it after adding lessons or clips */\nwindow.SHOTLIST='+out+';\n')
print(len(out), sum(len(L['clips']) for L in lessons), sum(c['done'] for L in lessons for c in L['clips']))
