#!/usr/bin/env python3
"""fix_wk32_portfolio.py - Nov 22 2026. Turns Lesson 32.3 into a real portfolio day.
Before: one 'copy your best piece' box in Part A, with the choice limited to Weeks 31-32 work.
After:  Reading tab = Where Your Writing Lives (a map of the year) + Choose Your Three (a quick pick-the-better-piece round);
        Assignment Part A = a three-piece portfolio builder (one piece from each part of the year, what each shows,
        growth from Piece 1 to Piece 3, a title and an introduction), a live showcase preview and a Download My Portfolio button.
Textarea ids journal-q1..q3 are kept so the Explorer/Scholar tiers, coaching and word counters still attach.
DATA changes (connector, scholar, wgrd, transcripts, todo) go through tools/setdata.py into BOTH places.
    python3 tools/fix_wk32_portfolio.py            (dry run)
    python3 tools/fix_wk32_portfolio.py --apply
"""
import io, json, re, sys, subprocess, os
APPLY = '--apply' in sys.argv
P = 'lesson-32-3-project-final.html'
h = io.open(P, encoding='utf-8', newline='').read()
orig = h

def swap(start, end, new, label, keep_end=True):
    global h
    i = h.find(start)
    if i < 0: sys.exit('missing start: ' + label)
    j = h.find(end, i)
    if j < 0: sys.exit('missing end: ' + label)
    h = h[:i] + new + (h[j:] if keep_end else h[j + len(end):])

def rep(old, new, label):
    global h
    if h.count(old) != 1: sys.exit('expected one match (%d): %s' % (h.count(old), label))
    h = h.replace(old, new)

# ── 1. CSS ───────────────────────────────────────────────────────────────
CSS = r"""
/* ═══════════ PORTFOLIO (32.3, Nov 22 2026) ═══════════ */
.pf-map{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;margin:6px 0 14px;}
@media(max-width:720px){.pf-map{grid-template-columns:1fr;}}
.pf-third{background:#fff;border:2px solid #E2E8F4;border-radius:14px;padding:14px 14px 12px;position:relative;}
.pf-third-top{display:flex;align-items:center;gap:8px;margin-bottom:6px;}
.pf-third-icons{font-size:24px;letter-spacing:2px;}
.pf-third-wk{font-size:11px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#7A88A8;}
.pf-third-name{font-size:16px;font-weight:800;color:#0E1C42;margin-bottom:6px;}
.pf-third ul{margin:0;padding-left:18px;font-size:14px;line-height:1.6;color:#3A4A6B;}
.pf-third.t1{border-top:6px solid #F9A825;} .pf-third.t2{border-top:6px solid #55C8E8;} .pf-third.t3{border-top:6px solid #34B76F;}
.pf-why{display:flex;gap:10px;align-items:center;justify-content:center;margin:4px 0 14px;font-size:14px;color:#3A4A6B;flex-wrap:wrap;}
.pf-why b{color:#0E1C42;}
.pf-pick{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:10px 0;}
@media(max-width:720px){.pf-pick{grid-template-columns:1fr;}}
.pf-sample{background:#FFFDF6;border:2px solid #E2E8F4;border-radius:12px;padding:12px 14px;cursor:pointer;font-size:14px;line-height:1.65;color:#0E1C42;text-align:left;font-family:inherit;transition:transform .15s,border-color .15s;}
.pf-sample:hover{transform:translateY(-2px);border-color:#55C8E8;}
.pf-sample .pf-sample-tag{display:block;font-size:11px;font-weight:800;letter-spacing:.08em;color:#7A88A8;text-transform:uppercase;margin-bottom:4px;}
.pf-sample.right{border-color:#34B76F;background:#E3F8ED;} .pf-sample.wrong{border-color:#F28B82;background:#FFF1F0;}
.pf-fb{display:none;font-size:14px;line-height:1.6;padding:10px 14px;border-radius:10px;margin-top:4px;}
.pf-fb.show{display:block;} .pf-fb.good{background:#E3F8ED;color:#1E5E3A;} .pf-fb.try{background:#FFF6E0;color:#6B4A00;}
.pf-rules{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:12px 0;}
@media(max-width:720px){.pf-rules{grid-template-columns:1fr;}}
.pf-rule{background:#F4F7FC;border-radius:12px;padding:10px 12px;font-size:14px;line-height:1.5;color:#3A4A6B;}
.pf-rule b{display:block;color:#0E1C42;font-size:15px;margin-bottom:2px;}
.pf-status{display:flex;gap:8px;flex-wrap:wrap;margin:0 0 14px;}
.pf-status span{font-size:13px;font-weight:700;padding:6px 12px;border-radius:999px;background:#F4F7FC;color:#7A88A8;border:2px solid #E2E8F4;}
.pf-status span.done{background:#E3F8ED;color:#1E5E3A;border-color:#B8E8CF;}
.pf-card{border:2px solid #E2E8F4;border-radius:16px;padding:16px;margin:0 0 18px;background:#fff;}
.pf-card.t1{border-left:8px solid #F9A825;} .pf-card.t2{border-left:8px solid #55C8E8;} .pf-card.t3{border-left:8px solid #34B76F;}
.pf-card-head{display:flex;justify-content:space-between;align-items:baseline;flex-wrap:wrap;gap:6px;margin-bottom:10px;}
.pf-card-title{font-size:18px;font-weight:800;color:#0E1C42;}
.pf-card-wk{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#7A88A8;}
.pf-label{font-size:13px;font-weight:800;color:#3A4A6B;margin:10px 0 6px;}
.pf-chips{display:flex;gap:8px;flex-wrap:wrap;}
.pf-chip{font-family:inherit;font-size:14px;font-weight:700;padding:7px 14px;border-radius:999px;border:2px solid #E2E8F4;background:#fff;color:#3A4A6B;cursor:pointer;}
.pf-chip:hover{border-color:#55C8E8;}
.pf-chip.on{background:#0E1C42;border-color:#0E1C42;color:#fff;}
.pf-input{width:100%;box-sizing:border-box;font-family:inherit;font-size:15px;padding:10px 12px;border:2px solid #E2E8F4;border-radius:10px;color:#0E1C42;}
.pf-input:focus{outline:none;border-color:#55C8E8;}
.pf-card .journal-box.pf-piece{min-height:110px;background:#FFFDF6;font-family:Georgia,serif;}
.pf-showcase{border-radius:18px;background:#0E1C42;padding:22px;margin:6px 0 18px;color:#fff;}
.pf-sc-title{font-family:Georgia,serif;font-size:24px;font-weight:700;text-align:center;margin:0;color:#fff !important;}
.pf-sc-books{text-align:center;font-size:24px;letter-spacing:6px;margin:6px 0 4px;}
.pf-sc-intro{background:rgba(255,255,255,.08);border-radius:12px;padding:12px 14px;font-family:Georgia,serif;font-size:15px;line-height:1.7;margin:12px 0;white-space:pre-wrap;}
.pf-sc-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:12px;}
@media(max-width:820px){.pf-sc-grid{grid-template-columns:1fr;}}
.pf-sc-card{background:#FFFDF6;color:#0E1C42;border-radius:12px;padding:12px 14px;border-top:6px solid #F9A825;}
.pf-sc-card.t2{border-top-color:#55C8E8;} .pf-sc-card.t3{border-top-color:#34B76F;}
.pf-sc-card h4{margin:0 0 2px;font-size:15px;} .pf-sc-where{font-size:12px;color:#7A88A8;margin-bottom:6px;}
.pf-sc-piece{font-family:Georgia,serif;font-size:14px;line-height:1.6;max-height:9.6em;overflow:hidden;white-space:pre-wrap;}
.pf-sc-skills{margin:8px 0 4px;display:flex;gap:4px;flex-wrap:wrap;}
.pf-sc-skills span{font-size:11px;font-weight:800;background:#0E1C42;color:#fff;border-radius:999px;padding:3px 8px;}
.pf-sc-note{font-size:13px;line-height:1.5;color:#3A4A6B;border-top:1px dashed #E2E8F4;padding-top:6px;white-space:pre-wrap;}
.pf-sc-empty{color:#B0B8CC;font-style:italic;}
.pf-sc-actions{text-align:center;margin-top:16px;}
.pf-dl{font-family:inherit;font-size:16px;font-weight:800;padding:12px 22px;border-radius:999px;border:none;background:#F9A825;color:#0E1C42;cursor:pointer;}
.pf-dl:hover{filter:brightness(1.05);}
"""
rep('/* ═══════════ RWM ═══════════ */', CSS + '\n/* ═══════════ RWM ═══════════ */', 'css anchor')

# ── 2. Objective line ────────────────────────────────────────────────────
rep('I will <em>curate</em> my best work and present it as my year-end portfolio.',
    'I will <em>curate</em> a portfolio of three pieces from across the year that shows how I grew.', 'objective')

# ── 3. Reading tab: activities 2 + 3 ─────────────────────────────────────
READ = """<div class="activity bl-green" data-std="ELA.4.C.2.1 ELA.K12.EE.6.1" data-std-id="32.3-09">
    <div class="activity-head"><div class="activity-num" style="background:#34B76F;">2</div><div><div class="activity-title">🗺️ Where Your Writing Lives</div><div class="activity-sub">Three parts of the year. One piece from each.</div></div></div>
    <div class="activity-body">
      <p>A portfolio is not your one best paragraph. It is a small collection that shows a <strong>change</strong>. One piece shows what you can do. Three pieces, from the start, middle and end of the year, show how you <em>grew</em>.</p>
      <div class="pf-why"><b>Piece 1</b> what I could do early &rarr; <b>Piece 2</b> what I was learning &rarr; <b>Piece 3</b> what I can do now</div>
      <div class="pf-map">
        <div class="pf-third t1">
          <div class="pf-third-top"><span class="pf-third-icons">🐭 👩&zwj;🦰</span></div>
          <div class="pf-third-wk">Weeks 1&ndash;14</div>
          <div class="pf-third-name">Frisby and Anne</div>
          <ul><li>Your Frisby end-of-book assessment (Week 5)</li><li>Any Writing Connection from <em>Anne of Green Gables</em> (Weeks 7&ndash;14)</li><li>A journal response you remember working hard on</li></ul>
        </div>
        <div class="pf-third t2">
          <div class="pf-third-top"><span class="pf-third-icons">⭐ 🚆</span></div>
          <div class="pf-third-wk">Weeks 15&ndash;25</div>
          <div class="pf-third-name">Number the Stars and Freedom Train</div>
          <ul><li>Your <em>Number the Stars</em> Final Project (Week 19)</li><li>Your <em>Freedom Train</em> Final Reflection (Week 24)</li><li>Comparing Sources (Week 25)</li></ul>
        </div>
        <div class="pf-third t3">
          <div class="pf-third-top"><span class="pf-third-icons">🦁 📚</span></div>
          <div class="pf-third-wk">Weeks 26&ndash;32</div>
          <div class="pf-third-name">Prince Caspian and the Year-End</div>
          <ul><li>Your leadership paragraph (Week 28)</li><li>Your theme paragraph (Week 29)</li><li>Your comparison paragraph, revised this week</li></ul>
        </div>
      </div>
      <div class="callout callout-info">
        <span class="callout-icon">📂</span>
        <p><strong>Where to find it:</strong> open your past submissions in Canvas (every lesson&rsquo;s copied work or PDF is there) and flip through your reading journal. Those lists are ideas, not rules. Any piece from that part of the year counts.</p>
      </div>
    </div>
  </div>

  <div class="activity bl-cyan" data-std="ELA.4.C.2.1 ELA.K12.EE.6.1" data-std-id="32.3-10">
    <div class="activity-head"><div class="activity-num" style="background:#55C8E8;">3</div><div><div class="activity-title">🏗️ Choose Your Three</div><div class="activity-sub">Choose like a museum curator: the piece that proves something.</div></div></div>
    <div class="activity-body">
      <p>A museum curator does not hang every painting. She picks the ones that tell the story. Try it. Both of these were written about <em>Number the Stars</em>. Which one belongs in a portfolio?</p>
      <div class="pf-pick" id="pfPick">
        <button type="button" class="pf-sample" data-ok="0" onclick="pfPickSample(this)"><span class="pf-sample-tag">Sample A</span>Number the Stars is about Annemarie and Ellen. They live in Copenhagen. The soldiers are everywhere. Ellen stays with Annemarie&rsquo;s family. Then they go to Uncle Henrik&rsquo;s house. Then Annemarie runs through the woods. It was a good book and I liked it a lot.</button>
        <button type="button" class="pf-sample" data-ok="1" onclick="pfPickSample(this)"><span class="pf-sample-tag">Sample B</span>Annemarie does not think she is brave. But when the soldiers stop her in the woods, she acts like a silly little girl so they will not look closely at the basket. That shows courage can look ordinary.</button>
      </div>
      <div class="pf-fb" id="pfPickFb"></div>
      <div class="pf-rules">
        <div class="pf-rule"><b>1. Not the longest</b>Pick the piece that shows a skill: evidence, word choice, voice, organization.</div>
        <div class="pf-rule"><b>2. Point at the sentence</b>Find the one sentence inside the piece that proves the skill.</div>
        <div class="pf-rule"><b>3. Show the change</b>Piece 3 should do something Piece 1 could not do yet.</div>
      </div>
      <div class="thinking-stop">💭 Find your three pieces now, one from each part of the year. Then build your portfolio on the Assignment tab.</div>
    </div>
  </div>

  <div class="tab-next-wrap">
    <p class="tab-transition-voice">You know where to look and how to choose. Now head to the Assignment tab and build your portfolio.</p>
    <button class="tab-next-btn" onclick="switchTab('assignment')">Continue to 📬 Assignment &rarr;</button>
  </div>
"""
swap('<div class="activity bl-green" data-std="ELA.4.C.2.1 ELA.K12.EE.6.1" data-std-id="32.3-09">',
     '</div><!-- /tab-reading -->', READ, 'reading block')

# ── 4. Assignment Part A ─────────────────────────────────────────────────
THIRDS = [
  (1, 't1', 'Weeks 1&ndash;14', [('frisby', '🐭 Mrs. Frisby'), ('anne', '👩&zwj;🦰 Anne')],
   'Week 5 &middot; Frisby assessment',
   'What does Piece 1 show you could already do early in the year? Point at the one sentence that proves it.',
   'Name the skill. Then copy or point to the sentence that shows it.',
   'Early in the year I could already... The sentence that shows it is...'),
  (2, 't2', 'Weeks 15&ndash;25', [('nts', '⭐ Number the Stars'), ('ft', '🚆 Freedom Train')],
   'Week 19 &middot; Number the Stars Final Project',
   'What does Piece 2 show you were learning to do in the middle of the year? Point at the sentence that proves it.',
   'Pick a different skill from Piece 1, or show the same skill getting stronger.',
   'In the middle of the year I was learning to... You can see it when I wrote...'),
  (3, 't3', 'Weeks 26&ndash;32', [('pc', '🦁 Prince Caspian'), ('ye', '📚 Year-End comparison')],
   'Week 31 &middot; comparison paragraph, revised',
   'What can you do in Piece 3 that you could not do yet in Piece 1? Put the two pieces side by side and name the change.',
   'This is the growth answer. Use one detail from Piece 1 and one from Piece 3.',
   'In Piece 1 I... Now in Piece 3 I... The change is...'),
]
SKILLS = ['Evidence', 'Word choice', 'Voice', 'Organization', 'Comparing', 'Revising']

def card(n, cls, wk, books, where_ph, q, hint, ph):
    chips = ''.join('<button type="button" class="pf-chip" data-pf="book%d" data-v="%s" onclick="pfChip(this,false)">%s</button>' % (n, k, lab) for k, lab in books)
    sk = ''.join('<button type="button" class="pf-chip" data-pf="skill%d" data-v="%s" onclick="pfChip(this,true)">%s</button>' % (n, s, s) for s in SKILLS)
    return """
      <div class="pf-card %(cls)s">
        <div class="pf-card-head"><div class="pf-card-title">Piece %(n)d</div><div class="pf-card-wk">%(wk)s</div></div>
        <div class="pf-label">Which book?</div>
        <div class="pf-chips">%(chips)s</div>
        <div class="pf-label">Where is it from? (week and lesson)</div>
        <input type="text" class="pf-input" id="pf-where-%(n)d" data-label="Piece %(n)d: Where it is from" placeholder="%(where_ph)s" oninput="pfSaveInput(this)">
        <div class="pf-label">Copy your piece. If it is long, copy the best part (3&ndash;6 sentences).</div>
        <textarea class="journal-box pf-piece" id="pf-piece-%(n)d" data-label="Piece %(n)d: My Writing" placeholder="Copy your writing here exactly as you wrote it." oninput="autoSave(this,'dot-pf%(n)d');pfRender();gatherAnswers();"></textarea>
        <div class="pf-label">What does it show? Tap one or two.</div>
        <div class="pf-chips">%(sk)s</div>
        <div class="q-block" style="margin-top:14px;"><div class="q-text"><span class="q-num">%(n)d</span>%(q)s</div><div class="q-hint">%(hint)s</div></div>
        <textarea class="journal-box" id="journal-q%(n)d" data-label="Piece %(n)d: What It Shows" placeholder="%(ph)s" oninput="autoSave(this,'dot-q%(n)d');pfRender();gatherAnswers();"></textarea>
      </div>""" % dict(n=n, cls=cls, wk=wk, chips=chips, where_ph=where_ph, sk=sk, q=q, hint=hint, ph=ph)

PARTA = """<!-- Part A -->
  <div class="activity bl-cyan" data-std="ELA.4.C.2.1 ELA.K12.EE.6.1" data-std-id="32.3-11">
    <div class="activity-head"><div class="activity-num" style="background:#55C8E8;">A</div><div><div class="activity-title">🎓 Part A: My Portfolio</div><div class="activity-sub">Three pieces, one year. This is what you turn in.</div></div></div>
    <div class="activity-body">
      <div class="pf-status" id="pfStatus"><span data-s="1">Piece 1</span><span data-s="2">Piece 2</span><span data-s="3">Piece 3</span><span data-s="i">Introduction</span></div>
      <div class="q-block" style="display:none"><div class="q-text"></div></div><!-- anchor: Explorer/Scholar picker lands here, above all three pieces -->
%(cards)s
      <div class="pf-card">
        <div class="pf-card-head"><div class="pf-card-title">🖋️ Your Portfolio Introduction</div><div class="pf-card-wk">The first page</div></div>
        <div class="pf-label">Give your portfolio a title.</div>
        <input type="text" class="pf-input" id="pf-title" data-label="Portfolio Title" placeholder="A Year of Reading: From Frisby to Caspian" oninput="pfSaveInput(this)">
        <div class="q-block" style="margin-top:14px;"><div class="q-text"><span class="q-num">4</span>Write 3&ndash;5 sentences to whoever opens your portfolio. Who were you as a reader in Week 1? Who are you now? End with one piece of advice for your Week 1 self.</div><div class="q-hint">This is the welcome sign on the door. Make the reader want to look at your three pieces.</div></div>
        <textarea class="journal-box" id="journal-intro" data-label="Portfolio Introduction" placeholder="When I started 4th grade, I read... Now I... If I could tell my Week 1 self one thing, it would be..." oninput="autoSave(this,'dot-intro');pfRender();gatherAnswers();"></textarea>
      </div>

      <div class="pf-label" style="font-size:15px;">✨ Your portfolio, so far</div>
      <div class="pf-showcase" id="pfShowcase"></div>
    </div>
  </div>

  """ % dict(cards=''.join(card(*t) for t in THIRDS))
swap('<!-- Part A -->', '<!-- Part C -->', PARTA, 'part A')

# ── 5. Checklist ─────────────────────────────────────────────────────────
swap('<div class="turn-in-checklist" id="checklistItems">', '</div>\n    </div>\n  </div>\n\n</div><!-- /tab-assignment -->',
"""<div class="turn-in-checklist" id="checklistItems">
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I finished my Word Study and my spelling SWYK.</div></div>
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I chose three pieces, one from each part of the year, and copied them in.</div></div>
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I said what each piece shows, and what I can do now that I could not do in Piece 1.</div></div>
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I gave my portfolio a title and wrote the introduction, with advice for my Week 1 self.</div></div>
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I tapped Download My Portfolio and turned in the PDF on Canvas.</div></div>
      """, 'checklist')

# ── 6. Gather + PDF ──────────────────────────────────────────────────────
rep("""  output+='\\n📖 CHAPTER THINKING\\n────────────────────────────────\\n';
  ['journal-q1','journal-q2','journal-q3'].forEach(function(id){
    var el=document.getElementById(id); if(!el)return;
    output+='\\n'+(el.getAttribute('data-label')||id)+'\\n'+(el.value.trim()||'(no answer)')+'\\n';
  });""",
"""  output+='\\n🎓 MY PORTFOLIO\\n────────────────────────────────\\n';
  output+=pfGatherText();""", 'gather')

rep("""    {title:'📖 CROSS-NOVEL THINKING',ids:['journal-q1','journal-q2','journal-q3']},""",
    """    {title:'🎓 MY PORTFOLIO',ids:['pf-title','journal-intro','pf-where-1','pf-piece-1','journal-q1','pf-where-2','pf-piece-2','journal-q2','pf-where-3','pf-piece-3','journal-q3']},""", 'pdf sections')

JS = r"""
/* ═══════════ PORTFOLIO BUILDER (32.3) ═══════════ */
var PF_BOOKS={frisby:['🐭','Mrs. Frisby and the Rats of NIMH'],anne:['👩‍🦰','Anne of Green Gables'],nts:['⭐','Number the Stars'],ft:['🚆','Freedom Train'],pc:['🦁','Prince Caspian'],ye:['📚','Year-End comparison']};
var PF_WEEKS=['Weeks 1–14','Weeks 15–25','Weeks 26–32'];
function pfK(s){return (typeof _lessonKey!=='undefined'?_lessonKey:'g4-32-3')+'-'+s;}
function pfGet(s,d){try{var v=localStorage.getItem(pfK(s));return v===null?d:JSON.parse(v);}catch(e){return d;}}
function pfSet(s,v){try{localStorage.setItem(pfK(s),JSON.stringify(v));}catch(e){}}
function pfEsc(s){return String(s||'').replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');}
function pfVal(id){var e=document.getElementById(id);return e?e.value.trim():'';}
function pfChip(b,multi){
  var key=b.getAttribute('data-pf'),v=b.getAttribute('data-v'),cur=pfGet(key,multi?[]:'');
  if(multi){var i=cur.indexOf(v);if(i>=0)cur.splice(i,1);else{cur.push(v);if(cur.length>2)cur.shift();}}
  else cur=(cur===v?'':v);
  pfSet(key,cur);pfPaintChips();pfRender();gatherAnswers();
}
function pfPaintChips(){
  document.querySelectorAll('.pf-chip').forEach(function(b){
    var key=b.getAttribute('data-pf'),v=b.getAttribute('data-v'),cur=pfGet(key,key.indexOf('skill')===0?[]:'');
    b.classList.toggle('on',Array.isArray(cur)?cur.indexOf(v)>=0:cur===v);
  });
}
function pfSaveInput(el){try{localStorage.setItem(pfK(el.id),el.value);}catch(e){} pfRender();gatherAnswers();}
function pfPiece(n){
  var b=pfGet('book'+n,''),bk=PF_BOOKS[b]||null;
  return {n:n,book:bk,where:pfVal('pf-where-'+n),text:pfVal('pf-piece-'+n),skills:pfGet('skill'+n,[]),note:pfVal('journal-q'+n)};
}
function pfRender(){
  var sc=document.getElementById('pfShowcase');if(!sc)return;
  var title=pfVal('pf-title'),intro=pfVal('journal-intro'),h='';
  h+='<p class="pf-sc-title">'+(title?pfEsc(title):'<span style="opacity:.55">Your portfolio title</span>')+'</p>';
  h+='<div class="pf-sc-books">🐭 👩‍🦰 ⭐ 🚆 🦁</div>';
  h+='<div class="pf-sc-intro">'+(intro?pfEsc(intro):'<span style="opacity:.55">Your introduction will show here.</span>')+'</div>';
  h+='<div class="pf-sc-grid">';
  for(var n=1;n<=3;n++){
    var p=pfPiece(n);
    h+='<div class="pf-sc-card t'+n+'"><h4>'+(p.book?p.book[0]+' '+pfEsc(p.book[1]):'Piece '+n)+'</h4>';
    h+='<div class="pf-sc-where">'+(p.where?pfEsc(p.where):PF_WEEKS[n-1])+'</div>';
    h+='<div class="pf-sc-piece">'+(p.text?pfEsc(p.text):'<span class="pf-sc-empty">Your writing goes here.</span>')+'</div>';
    if(p.skills.length)h+='<div class="pf-sc-skills">'+p.skills.map(function(s){return '<span>'+pfEsc(s)+'</span>';}).join('')+'</div>';
    h+='<div class="pf-sc-note">'+(p.note?pfEsc(p.note):'<span class="pf-sc-empty">What it shows goes here.</span>')+'</div></div>';
  }
  h+='</div><div class="pf-sc-actions"><button type="button" class="pf-dl" onclick="pfDownload()">📄 Download My Portfolio</button></div>';
  sc.innerHTML=h;
  var st=document.getElementById('pfStatus');
  if(st)st.querySelectorAll('span').forEach(function(s){
    var k=s.getAttribute('data-s'),ok;
    if(k==='i')ok=!!(title&&intro);else{var p=pfPiece(+k);ok=!!(p.book&&p.text&&p.note);}
    s.classList.toggle('done',ok);s.textContent=(ok?'✓ ':'')+(k==='i'?'Introduction':'Piece '+k);
  });
}
function pfGatherText(){
  var o='\nPortfolio Title\n'+(pfVal('pf-title')||'(no answer)')+'\n';
  o+='\nPortfolio Introduction\n'+(pfVal('journal-intro')||'(no answer)')+'\n';
  for(var n=1;n<=3;n++){
    var p=pfPiece(n);
    o+='\n— PIECE '+n+' ('+PF_WEEKS[n-1]+') —\n';
    o+='Book: '+(p.book?p.book[1]:'(not chosen)')+'\n';
    o+='Where it is from: '+(p.where||'(no answer)')+'\n';
    o+='What it shows: '+(p.skills.length?p.skills.join(', '):'(not chosen)')+'\n';
    o+='My writing:\n'+(p.text||'(no answer)')+'\n';
    o+='Why it belongs here:\n'+(p.note||'(no answer)')+'\n';
  }
  return o;
}
function pfDownload(){
  gatherAnswers();
  var title=pfVal('pf-title')||'My 4th Grade Reading Portfolio',intro=pfVal('journal-intro');
  var css='body{font-family:Georgia,serif;color:#0E1C42;max-width:760px;margin:30px auto;padding:0 24px;line-height:1.7;}'+
    '.cover{text-align:center;border:3px solid #0E1C42;border-radius:18px;padding:40px 30px;margin-bottom:28px;}'+
    '.cover h1{font-size:30px;margin:6px 0;} .books{font-size:30px;letter-spacing:8px;} .sub{font-family:Arial,sans-serif;font-size:12px;letter-spacing:.12em;text-transform:uppercase;color:#7A88A8;}'+
    '.intro{font-size:16px;text-align:left;margin-top:20px;white-space:pre-wrap;}'+
    '.pc{border-radius:14px;border:2px solid #E2E8F4;border-left:10px solid #F9A825;padding:18px 20px;margin:0 0 22px;page-break-inside:avoid;}'+
    '.pc.t2{border-left-color:#55C8E8;} .pc.t3{border-left-color:#34B76F;}'+
    '.pc h2{margin:0;font-size:20px;} .wk{font-family:Arial,sans-serif;font-size:12px;color:#7A88A8;letter-spacing:.08em;text-transform:uppercase;}'+
    '.txt{background:#FFFDF6;border-radius:10px;padding:12px 14px;margin:10px 0;white-space:pre-wrap;font-size:15px;}'+
    '.sk span{font-family:Arial,sans-serif;font-size:11px;font-weight:bold;background:#0E1C42;color:#fff;border-radius:999px;padding:3px 9px;margin-right:4px;}'+
    '.note{font-size:14px;color:#3A4A6B;white-space:pre-wrap;margin-top:8px;} .lab{font-family:Arial,sans-serif;font-size:11px;font-weight:bold;letter-spacing:.08em;text-transform:uppercase;color:#7A88A8;}'+
    '.na{color:#B0B8CC;font-style:italic;} .foot{font-family:Arial,sans-serif;font-size:11px;color:#7A88A8;text-align:center;margin-top:30px;}';
  var h='<!DOCTYPE html><html><head><meta charset="UTF-8"><title>'+pfEsc(title)+'</title><style>'+css+'</style></head><body>';
  h+='<div class="cover"><div class="sub">4th Grade ELA &middot; Year-End Portfolio</div><h1>'+pfEsc(title)+'</h1><div class="books">🐭 👩‍🦰 ⭐ 🚆 🦁</div>';
  h+='<div class="intro">'+(intro?pfEsc(intro):'<span class="na">(no introduction yet)</span>')+'</div></div>';
  for(var n=1;n<=3;n++){
    var p=pfPiece(n);
    h+='<div class="pc t'+n+'"><div class="wk">Piece '+n+' &middot; '+PF_WEEKS[n-1]+(p.where?' &middot; '+pfEsc(p.where):'')+'</div>';
    h+='<h2>'+(p.book?p.book[0]+' '+pfEsc(p.book[1]):'<span class="na">(book not chosen)</span>')+'</h2>';
    h+='<div class="txt">'+(p.text?pfEsc(p.text):'<span class="na">(no writing yet)</span>')+'</div>';
    if(p.skills.length)h+='<div class="sk">'+p.skills.map(function(s){return '<span>'+pfEsc(s)+'</span>';}).join('')+'</div>';
    h+='<div class="lab" style="margin-top:10px;">'+(n===3?'How I grew':'What it shows')+'</div><div class="note">'+(p.note?pfEsc(p.note):'<span class="na">(no answer yet)</span>')+'</div></div>';
  }
  h+='<div class="foot">Optima Academy Online &middot; 4th Grade ELA &middot; Lesson 32.3</div></body></html>';
  var win=window.open('','_blank');if(!win)return;win.document.write(h);win.document.close();setTimeout(function(){win.print();},400);
}
function pfPickSample(b){
  var ok=b.getAttribute('data-ok')==='1',fb=document.getElementById('pfPickFb');
  document.querySelectorAll('#pfPick .pf-sample').forEach(function(x){x.classList.remove('right','wrong');});
  b.classList.add(ok?'right':'wrong');
  fb.className='pf-fb show '+(ok?'good':'try');
  fb.innerHTML=ok?'<strong>That is the curator&rsquo;s pick.</strong> Sample B is shorter, but it makes a point (courage can look ordinary) and proves it with one moment from the book. That last sentence is the one you would point at.'
                 :'<strong>Look again.</strong> Sample A is longer, but it only retells what happened. Which sentence proves a skill? None of them yet. Try the other one.';
}
(function pfInit(){
  ['pf-title','pf-where-1','pf-where-2','pf-where-3'].forEach(function(id){
    var e=document.getElementById(id);if(!e)return;
    try{var v=localStorage.getItem(pfK(id));if(v)e.value=v;}catch(x){}
  });
  pfPaintChips();
  setTimeout(function(){pfRender();},0);
})();
"""
rep('/* DOWNLOAD PDF */\nfunction downloadJournal(){', JS + '\n/* DOWNLOAD PDF */\nfunction downloadJournal(){', 'js anchor')

# ── 7. Standards block titles (ids and tags unchanged) ───────────────────
for old, new in [('"title": "🎓 Your Portfolio"', '"title": "🗺️ Where Your Writing Lives"'),
                 ('"title": "🏗️ Build Your Portfolio"', '"title": "🏗️ Choose Your Three"'),
                 ('"title": "📖 Part A: Chapter Thinking"', '"title": "🎓 Part A: My Portfolio"')]:
    rep(old, new, 'std title ' + old)
# Part A now carries the same writing standards as the two Reading blocks it replaced
rep('{"id": "32.3-11", "title": "🎓 Part A: My Portfolio", "FL": ["ELA.K12.EE.6.1"], "TX": [], "AR": ["4.CC.5.P"], "MO": ["4.SL.4.A.f"], "AL": ["R6"], "TN": ["4.SL.PKI.6"], "PR": "pending"}',
    '{"id": "32.3-11", "title": "🎓 Part A: My Portfolio", "FL": ["ELA.4.C.2.1", "ELA.K12.EE.6.1"], "TX": ["110.6(b)(1)(C)"], "AR": ["4.CC.3.P", "4.CC.5.P"], "MO": ["4.SL.4.A", "4.SL.4.A.f"], "AL": ["42", "R6"], "TN": ["4.SL.PKI.4", "4.SL.PKI.6"], "PR": "pending"}',
    'std 32.3-11 tags')

# ── 8. DATA patch (both places, via setdata.py) ──────────────────────────
D = json.load(io.open('data/lesson-32-3.json', encoding='utf-8'))
todo = [t for t in D['todo'] if t['find'] not in ('Your Portfolio', 'Build Your Portfolio', 'Part A')]
todo += [{"find": "Where Your Writing", "steps": ["Read the three parts of the year.", "Open your Canvas submissions and your reading journal.", "Find one piece from each part."]},
         {"find": "Choose Your Three", "steps": ["Read Sample A and Sample B.", "Tap the one a curator would pick.", "Read the three rules."]},
         {"find": "Part A", "steps": ["Pick Explorer or Scholar.", "For each piece: tap the book, say where it is from, copy it in, tap what it shows.", "Answer the question under each piece.", "Write your title and introduction.", "Tap Download My Portfolio and turn in the PDF."]}]
patch = {
 "connector": "Today you build your portfolio: three pieces of your own writing, one from each part of the year, and what each one shows. Put them side by side and you can see how you grew.",
 "scholar": {"journal-q1": "… and copy the exact sentence that proves it.",
             "journal-q2": "… and say how it is different from Piece 1.",
             "journal-q3": "… and name the week you think the change started."},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "wgrd": {"catcher": {"title": "My three pieces", "intro": "One from each part of the year.",
                      "fields": [{"label": "Piece 1 (Weeks 1–14)", "hint": "", "rows": 1},
                                 {"label": "Piece 2 (Weeks 15–25)", "hint": "", "rows": 1},
                                 {"label": "Piece 3 (Weeks 26–32)", "hint": "", "rows": 1}],
                      "end": {"label": "What changed from Piece 1 to Piece 3", "hint": ""}},
          "useAt": ["journal-q1", "journal-q2", "journal-q3"]},
 "transcripts": dict(D['transcripts'],
     welcome="Hello again, it’s Opti. Today you build your portfolio. Today’s question: what can you do now that you couldn’t do in September?",
     read="Find three pieces of your writing: one from the fall, one from the middle of the year, one from this spring. Pick the ones that show a skill, not the longest ones. Then put them side by side. What changed?"),
 "todo": todo,
}
if APPLY:
    io.open(P, 'w', encoding='utf-8', newline='').write(h)
    io.open('/tmp/pf_patch.json', 'w', encoding='utf-8').write(json.dumps(patch, ensure_ascii=False))
    r = subprocess.run([sys.executable, 'tools/setdata.py', P, 'data/lesson-32-3.json', '/tmp/pf_patch.json', '--apply'], capture_output=True, text=True)
    print(r.stdout, r.stderr)
    print('written', P, len(orig), '->', len(io.open(P, encoding='utf-8').read()))
else:
    print('dry run ok', len(orig), '->', len(h))
