#!/usr/bin/env python3
"""fix_wk32_present.py - Nov 22 2026. Second half of the Week 32 project fix (first half: fix_wk32_portfolio.py).
1. Lighter strands on Days 3-4: blocks that are not the day's Opti strand fold into a collapsed
   "Extra word study (optional)" drawer at the bottom of the Word Study tab. Nothing is deleted, so tags stay.
     32.3 keeps Spelling (Opti video);   optional: Morphology, Vocabulary, Grammar
     32.4 keeps Vocabulary + Grammar (Opti video);   optional: Morphology, Spelling
2. 32.4 becomes a real presentation: Plan Your Talk (Reading), then Part A My Talk (three cue cards = journal-q1..q3),
   Part B My Last Line (journal-writing), Part C Rehearse and Present (practice timer, speaker checks,
   video to Canvas OR a grown-up's listener card = journal-listener).
DATA goes through tools/setdata.py into both places.
    python3 tools/fix_wk32_present.py [--apply]
"""
import io, json, re, sys, subprocess
APPLY = '--apply' in sys.argv
P3, P4 = 'lesson-32-3-project-final.html', 'lesson-32-4-project-celebration.html'

def block(h, sid):
    """start/end of the activity div carrying data-std-id=sid (balanced div count)."""
    m = re.search(r'<div class="activity [^"]*"[^>]*data-std-id="%s">' % re.escape(sid), h)
    if not m: sys.exit('no block ' + sid)
    i = m.start(); depth = 0
    for t in re.finditer(r'<div\b|</div>', h[i:]):
        depth += 1 if t.group() == '<div' else -1
        if depth == 0: return i, i + t.end()
    sys.exit('unbalanced ' + sid)

def rep(h, old, new, label):
    if h.count(old) != 1: sys.exit('expected one match (%d): %s' % (h.count(old), label))
    return h.replace(old, new)

def swap(h, start, end, new, label):
    i = h.find(start); j = h.find(end, i)
    if i < 0 or j < 0: sys.exit('missing: ' + label)
    return h[:i] + new + h[j:]

OPT_CSS = """
/* ═══════════ OPTIONAL WORD STUDY DRAWER (wk32, Nov 22 2026) ═══════════ */
.ws-optional{margin:6px 0 22px;border:2px dashed #C9D3E6;border-radius:14px;background:#F8FAFD;}
.ws-optional>summary{cursor:pointer;list-style:none;padding:14px 18px;font-weight:800;color:#3A4A6B;font-size:16px;display:flex;justify-content:space-between;align-items:center;}
.ws-optional>summary::-webkit-details-marker{display:none;}
.ws-optional>summary::after{content:'Open ▾';font-size:13px;color:#7A88A8;}
.ws-optional[open]>summary::after{content:'Close ▴';}
.ws-optional>summary small{display:block;font-weight:600;color:#7A88A8;font-size:13px;margin-top:2px;}
.ws-optional-body{padding:0 14px 6px;}
"""

def fold(h, keep_ids, opt_ids, note):
    parts = []
    for sid in opt_ids:
        s, e = block(h, sid); parts.append(h[s:e]); h = h[:s] + h[e:]
    drawer = ('<details class="ws-optional">\n    <summary><span>➕ Extra word study (optional)<small>%s</small></span></summary>\n'
              '    <div class="ws-optional-body">\n  ' % note) + '\n\n  '.join(parts) + '\n    </div>\n  </details>\n\n  '
    s, e = block(h, keep_ids[-1])
    return h[:e] + '\n\n  ' + drawer + h[e:]

# ═════════════════════════════ 32.3 ═════════════════════════════
h3 = io.open(P3, encoding='utf-8', newline='').read()
if 'ws-optional' not in h3:
    h3 = rep(h3, '/* ═══════════ RWM ═══════════ */', OPT_CSS + '\n/* ═══════════ RWM ═══════════ */', '32.3 css')
    h3 = fold(h3, ['32.3-07'], ['32.3-04', '32.3-05', '32.3-06'],
              'Today is portfolio day, so only the spelling check is required. Morphology, vocabulary and grammar are here if you want more practice.')
    h3 = rep(h3, 'Your vocabulary is sharp, your roots are solid, and your spelling SWYK is saved. Now let&rsquo;s put all that reading knowledge to work in your portfolio.',
             'Your spelling check is done. Today is mostly portfolio work, so head to Reading and start looking back at your year.', '32.3 words transition')
    h3 = rep(h3, 'I finished my Word Study and my spelling SWYK.', 'I did my spelling final check on the Word Study tab.', '32.3 checklist')

# ═════════════════════════════ 32.4 ═════════════════════════════
h4 = io.open(P4, encoding='utf-8', newline='').read()
h4 = rep(h4, '/* ═══════════ RWM ═══════════ */' if '/* ═══════════ RWM ═══════════ */' in h4 else '.tab-transition-voice {',
         (OPT_CSS + """
/* ═══════════ PRESENTATION (32.4) ═══════════ */
.pr-cards{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin:8px 0 14px;}
@media(max-width:760px){.pr-cards{grid-template-columns:1fr 1fr;}}
.pr-cue{background:#FFFDF6;border:2px solid #E2E8F4;border-radius:12px;padding:12px;font-size:14px;line-height:1.5;color:#3A4A6B;position:relative;}
.pr-cue b{display:block;color:#0E1C42;font-size:15px;margin-bottom:2px;}
.pr-cue .pr-n{position:absolute;top:-10px;left:10px;background:#0E1C42;color:#fff;font-size:12px;font-weight:800;border-radius:999px;padding:2px 9px;}
.pr-cue .pr-t{display:block;font-size:12px;color:#7A88A8;margin-top:6px;font-weight:700;}
.pr-notice{display:grid;grid-template-columns:repeat(3,1fr);gap:10px;margin:10px 0;}
@media(max-width:760px){.pr-notice{grid-template-columns:1fr;}}
.pr-notice div{background:#F4F7FC;border-radius:12px;padding:10px 12px;font-size:14px;line-height:1.5;color:#3A4A6B;}
.pr-notice b{display:block;color:#0E1C42;}
.pr-card{border:2px solid #E2E8F4;border-radius:16px;padding:14px 16px;margin:0 0 16px;background:#fff;border-left:8px solid #55C8E8;}
.pr-card-top{font-size:12px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;color:#7A88A8;margin-bottom:4px;}
.pr-timer{display:flex;align-items:center;gap:14px;flex-wrap:wrap;background:#0E1C42;color:#fff;border-radius:16px;padding:14px 18px;margin:8px 0 12px;}
.pr-clock{font-family:'Courier New',monospace;font-size:34px;font-weight:700;min-width:110px;}
.pr-btn{font-family:inherit;font-size:15px;font-weight:800;padding:9px 16px;border-radius:999px;border:none;cursor:pointer;background:#F9A825;color:#0E1C42;}
.pr-btn.ghost{background:transparent;color:#fff;border:2px solid rgba(255,255,255,.4);}
.pr-band{font-size:14px;font-weight:700;opacity:.9;}
.pr-band.ok{color:#8BE3B0;} .pr-band.short{color:#FFE9B8;} .pr-band.long{color:#FFB4AB;}
.pr-tries{font-size:13px;opacity:.75;margin-left:auto;}
.pr-checks{display:flex;gap:8px;flex-wrap:wrap;margin:4px 0 14px;}
.pr-chk{font-family:inherit;font-size:14px;font-weight:700;padding:7px 14px;border-radius:999px;border:2px solid #E2E8F4;background:#fff;color:#3A4A6B;cursor:pointer;}
.pr-chk.on{background:#E3F8ED;border-color:#34B76F;color:#1E5E3A;}
.pr-paths{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:8px 0;}
@media(max-width:760px){.pr-paths{grid-template-columns:1fr;}}
.pr-path{font-family:inherit;text-align:left;cursor:pointer;border:2px solid #E2E8F4;border-radius:14px;background:#fff;padding:14px;font-size:14px;line-height:1.55;color:#3A4A6B;}
.pr-path b{display:block;font-size:16px;color:#0E1C42;margin-bottom:4px;}
.pr-path.on{border-color:#0E1C42;box-shadow:0 0 0 3px #D6F2FB;}
.pr-pane{display:none;margin-top:10px;} .pr-pane.show{display:block;}
.pr-steps{margin:6px 0 0 18px;padding:0;font-size:14px;line-height:1.7;color:#3A4A6B;}
""" + ('\n/* ═══════════ RWM ═══════════ */' if '/* ═══════════ RWM ═══════════ */' in h4 else '\n.tab-transition-voice {')), '32.4 css')

h4 = fold(h4, ['32.4-05', '32.4-06'], ['32.4-04', '32.4-07'],
          'Today is presentation day, so vocabulary and grammar are the only required word study. Morphology and spelling are here if you want one more round.')
h4 = rep(h4, 'You&rsquo;ve completed your vocabulary choice board and reviewed the year&rsquo;s word study. Now get your celebration ready &mdash; who you will tell, and what you will say.',
         'Your word and your best sentence are ready. Now plan your talk: who will hear it, and what you will say.', '32.4 words transition')

# objectives + path
h4 = rep(h4, 'I will <em>reflect</em> on the year&rsquo;s five books and get ready to tell someone how I grew as a reader.',
         'I will <em>present</em> my portfolio out loud and tell how I grew as a reader, with clear volume and pacing.', '32.4 objective')
h4 = rep(h4, '<span class="todays-path-step">📖 Novel shelf reflection</span>', '<span class="todays-path-step">🎤 Plan your talk</span>', 'path 3')
h4 = rep(h4, '<span class="todays-path-step">📬 Final reflection &amp; submit</span>', '<span class="todays-path-step">📬 Rehearse, present &amp; submit</span>', 'path 4')

# Reading activity 2
s, e = block(h4, '32.4-09')
h4 = h4[:s] + """<div class="activity bl-green" data-std="ELA.4.C.2.1 ELA.K12.EE.6.1" data-std-id="32.4-09">
    <div class="activity-head"><div class="activity-num" style="background:#34B76F;">2</div><div><div class="activity-title">🎤 Plan Your Talk</div><div class="activity-sub">One to two minutes. Four cue cards. Your portfolio is the visual.</div></div></div>
    <div class="activity-body">
      <p>Yesterday you built your portfolio. Today you present it. Keep the PDF from Lesson 32.3 open on your screen, or print it and hold it up. Your talk follows four cue cards, about 30 seconds each.</p>
      <div class="pr-cards">
        <div class="pr-cue"><span class="pr-n">1</span><b>Open</b>Say your portfolio&rsquo;s title and who you were as a reader in Week 1.<span class="pr-t">about 20 seconds</span></div>
        <div class="pr-cue"><span class="pr-n">2</span><b>Show the change</b>Read one sentence from Piece 1 and one from Piece 3. Say what changed.<span class="pr-t">about 40 seconds</span></div>
        <div class="pr-cue"><span class="pr-n">3</span><b>Look forward</b>Your reading goal for next year, and why you picked it.<span class="pr-t">about 20 seconds</span></div>
        <div class="pr-cue"><span class="pr-n">4</span><b>Last line</b>End with the last sentence of your 4th grade ELA year.<span class="pr-t">about 10 seconds</span></div>
      </div>
      <div class="socratic-box">
        <div class="socratic-label">🎤 Pick Your Listener</div>
        <p class="socratic-q">Who will hear this? A grown-up at home, a younger kid, or your teacher watching the video. Picture <strong>one real person</strong>. Which words in your talk would you change for them?</p>
      </div>
      <p style="margin-top:14px;"><strong>Three things every listener notices</strong>, even when they are not trying to:</p>
      <div class="pr-notice">
        <div><b>🔊 Volume</b>Loud enough for the back of the room, even if the room is your kitchen.</div>
        <div><b>🐢 Pace</b>Slower than talking to a friend. Stop for a breath after each card.</div>
        <div><b>👀 Looking up</b>Glance at your card, then look at your listener while you say it.</div>
      </div>
      <div class="thinking-stop">💭 Say Card 1 out loud once, right now. Then go write your cards on the Assignment tab.</div>
    </div>
  </div>""" + h4[e:]
h4 = rep(h4, 'You know who is listening and what you will say. Now write it down and close out the year strong.',
         'You know the shape of your talk and who is listening. Now write your cue cards, practice, and present.', '32.4 reading transition')

# Assignment: submit callout
h4 = rep(h4, '<p><strong>This is the part you submit.</strong> Answer in complete sentences. Draw on the five books you read this year &mdash; <em>Mrs. Frisby and the Rats of NIMH</em>, <em>Anne of Green Gables</em>, <em>Number the Stars</em>, <em>Freedom Train</em>, and <em>Prince Caspian</em> &mdash; as your evidence. When you finish, copy or download your work at the bottom.</p>',
         '<p><strong>This is the part you submit.</strong> Write your cue cards in full sentences, practice out loud, then present. You turn in two things: your cue cards (copy or download at the bottom) and your presentation (a video, or your grown-up&rsquo;s listener card).</p>', '32.4 callout')

PARTS = """<!-- Part A -->
  <div class="activity bl-cyan" data-std="ELA.4.C.2.1 ELA.K12.EE.6.1" data-std-id="32.4-10">
    <div class="activity-head"><div class="activity-num" style="background:#55C8E8;">A</div><div><div class="activity-title">🎤 Part A: My Talk</div><div class="activity-sub">Three cue cards. Write them the way you will say them.</div></div></div>
    <div class="activity-body">
      <div class="q-block"><div class="q-text"><span class="q-num">1</span><strong>Card 1 &middot; Open.</strong> Say your portfolio&rsquo;s title. Then tell your listener who you were as a reader in Week 1.</div><div class="q-hint">Two or three sentences. &ldquo;My portfolio is called ___. When I started 4th grade, I ___.&rdquo;</div></div>
      <textarea class="journal-box" id="journal-q1" data-label="Card 1: Open" placeholder="My portfolio is called... When I started 4th grade, I read... and I wrote..." oninput="autoSave(this,'dot-q1');gatherAnswers();"></textarea>

      <div class="q-block" style="margin-top:16px;"><div class="q-text"><span class="q-num">2</span><strong>Card 2 &middot; Show the change.</strong> Copy one sentence from Piece 1 and one from Piece 3 of your portfolio. Then say, in your own words, what you can do now that you could not do then.</div><div class="q-hint">You will read both sentences out loud, so pick ones that sound different. Then name the change: more evidence? stronger words? a clearer point?</div></div>
      <textarea class="journal-box" id="journal-q2" data-label="Card 2: Show the Change" placeholder="In Week ___, I wrote: &quot;...&quot; This spring, I wrote: &quot;...&quot; The difference is..." oninput="autoSave(this,'dot-q2');gatherAnswers();"></textarea>

      <div class="q-block" style="margin-top:16px;"><div class="q-text"><span class="q-num">3</span><strong>Card 3 &middot; Look forward.</strong> Tell your listener your reading goal for next year and why you chose it.</div><div class="q-hint">Make it specific. &ldquo;I want to try a mystery because I liked the suspense in <em>Number the Stars</em>&rdquo; beats &ldquo;I want to read more.&rdquo;</div></div>
      <textarea class="journal-box" id="journal-q3" data-label="Card 3: Look Forward" placeholder="Next year, my reading goal is... I chose it because this year I found out that I..." oninput="autoSave(this,'dot-q3');gatherAnswers();"></textarea>
    </div>
  </div>

  <!-- Part C -->
  <div class="activity bl-gold" data-std="ELA.K12.EE.6.1" data-std-id="32.4-11">
    <div class="activity-head"><div class="activity-num" style="background:#C7922C;">B</div><div><div class="activity-title">✍️ Part B: My Last Line</div><div class="activity-sub">Card 4. The last sentence of your talk, and of 4th grade ELA.</div></div></div>
    <div class="activity-body">
      <div class="q-block"><div class="q-text"><span class="q-num">4</span>Write <strong>one sentence</strong> to end your talk. It is also the last sentence of your 4th grade ELA year. Make it true, and make it one you would want to remember.</div><div class="q-hint">Not what a teacher wants to hear. What is actually true for you. Say it slowly when you get there.</div></div>
      <textarea class="journal-box" id="journal-writing" data-label="Card 4: My Last Line" style="min-height:80px;" placeholder="This year in ELA, I learned that..." oninput="autoSave(this,'dot-writing');gatherAnswers();"></textarea>
    </div>
  </div>

  <!-- Part C: present -->
  <div class="activity bl-green" data-std="ELA.4.C.2.1" data-std-id="32.4-12">
    <div class="activity-head"><div class="activity-num" style="background:#34B76F;">C</div><div><div class="activity-title">📹 Part C: Rehearse and Present</div><div class="activity-sub">Practice once with the timer. Then present it for real.</div></div></div>
    <div class="activity-body">
      <div class="pr-card-top">Step 1 &middot; Rehearse</div>
      <p>Open your portfolio PDF. Tap Start, give your whole talk out loud, then tap Stop. Aim for one to two minutes.</p>
      <div class="pr-timer">
        <div class="pr-clock" id="prClock">0:00</div>
        <button type="button" class="pr-btn" id="prGo" onclick="prToggle()">▶ Start</button>
        <button type="button" class="pr-btn ghost" onclick="prReset()">Reset</button>
        <span class="pr-band" id="prBand">Aim for 1:00 to 2:00</span>
        <span class="pr-tries" id="prTries"></span>
      </div>
      <p style="font-size:14px;color:#3A4A6B;margin-bottom:6px;">After you practice, tap each one you did:</p>
      <div class="pr-checks">
        <button type="button" class="pr-chk" data-c="Loud enough" onclick="prCheck(this)">🔊 Loud enough</button>
        <button type="button" class="pr-chk" data-c="Not too fast" onclick="prCheck(this)">🐢 Not too fast</button>
        <button type="button" class="pr-chk" data-c="Looked up" onclick="prCheck(this)">👀 Looked up</button>
        <button type="button" class="pr-chk" data-c="Sounded like me" onclick="prCheck(this)">🙂 Sounded like me</button>
      </div>

      <div class="pr-card-top" style="margin-top:8px;">Step 2 &middot; Present. Pick one way.</div>
      <div class="pr-paths">
        <button type="button" class="pr-path" data-p="video" onclick="prPath(this)"><b>📹 Record a video</b>Record your talk (1&ndash;2 minutes) with your portfolio on screen or in your hands. Turn in the video on Canvas.</button>
        <button type="button" class="pr-path" data-p="listener" onclick="prPath(this)"><b>👪 Present to a grown-up</b>Give your talk to a grown-up at home. They answer two questions, and you type their answers here.</button>
      </div>
      <div class="pr-pane" id="prPane-video">
        <ol class="pr-steps"><li>Find a quiet spot with light on your face.</li><li>Hold the device steady, or lean it on something.</li><li>Record your whole talk in one take. If you stumble, keep going.</li><li>Watch it once. Then turn in the video on Canvas with your cue cards.</li></ol>
      </div>
      <div class="pr-pane" id="prPane-listener">
        <p style="font-size:14px;color:#3A4A6B;">After your talk, ask your grown-up these two questions. Type what they say, in their words.</p>
        <div class="q-block"><div class="q-text"><span class="q-num">👪</span><strong>Listener card.</strong> (1) What is one way this reader grew this year? (2) Which line from the talk will you remember?</div><div class="q-hint">Write their name at the end, like a signature.</div></div>
        <textarea class="journal-box" id="journal-listener" data-label="Listener Card" placeholder="1. One way you grew: ...&#10;2. The line I will remember: ...&#10;&#8212; (grown-up's name)" oninput="autoSave(this,'dot-listener');gatherAnswers();"></textarea>
      </div>
    </div>
  </div>

  """
h4 = swap(h4, '<!-- Part A -->', '<!-- Gathered Answers -->', PARTS, '32.4 parts')

h4 = swap(h4, '<div class="turn-in-checklist" id="checklistItems">', '</div>\n    </div>\n  </div>\n\n</div><!-- /tab-assignment -->',
"""<div class="turn-in-checklist" id="checklistItems">
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I finished my vocabulary and grammar on the Word Study tab.</div></div>
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I wrote my three cue cards and my last line.</div></div>
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I practiced my talk out loud with the timer.</div></div>
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I presented, and turned in my video or my grown-up&rsquo;s listener card on Canvas with my cue cards.</div></div>
        <div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">🎉 I finished 4th grade ELA!</div></div>
      """, '32.4 checklist')

# gather + pdf
h4 = rep(h4, "  output+='\\n📖 CHAPTER THINKING\\n────────────────────────────────\\n';\n  ['journal-q1','journal-q2','journal-q3'].forEach",
             "  output+='\\n🎤 MY TALK\\n────────────────────────────────\\n';\n  ['journal-q1','journal-q2','journal-q3'].forEach", 'gather head')
h4 = rep(h4, "  output+='\\n✍️ WRITING CONNECTION\\n────────────────────────────────\\n';\n  var wEl=document.getElementById('journal-writing');",
             "  output+='\\n✍️ MY LAST LINE\\n────────────────────────────────\\n';\n  var wEl=document.getElementById('journal-writing');", 'gather writing')
h4 = rep(h4, "  output+='\\n🎮 PRACTICE ACTIVITIES\\n────────────────────────────────\\n';",
             "  output+=(typeof prGatherText==='function'?prGatherText():'');\n  output+='\\n🎮 PRACTICE ACTIVITIES (optional)\\n────────────────────────────────\\n';", 'gather present')
h4 = rep(h4, "    {title:'📖 LOOKING BACK, LOOKING FORWARD',ids:['journal-q1','journal-q2','journal-q3']},",
             "    {title:'🎤 MY TALK',ids:['journal-q1','journal-q2','journal-q3']},\n    {title:'✍️ MY LAST LINE',ids:['journal-writing']},\n    {title:'📹 HOW I PRESENTED',ids:['journal-listener']},", 'pdf sections')
h4 = rep(h4, "    {title:'✍️ WRITING CONNECTION',ids:['journal-writing']},\n", '', 'pdf old writing')

PRJS = r"""
/* ═══════════ PRESENTATION (32.4) ═══════════ */
function prK(s){return (typeof _lessonKey!=='undefined'?_lessonKey:'g4-32-4')+'-'+s;}
function prGet(s,d){try{var v=localStorage.getItem(prK(s));return v===null?d:JSON.parse(v);}catch(e){return d;}}
function prSet(s,v){try{localStorage.setItem(prK(s),JSON.stringify(v));}catch(e){}}
var _prT=null,_prStart=0,_prSecs=0;
function prFmt(s){return Math.floor(s/60)+':'+('0'+Math.floor(s%60)).slice(-2);}
function prBand(s){var b=document.getElementById('prBand');if(!b)return;
  if(!s){b.className='pr-band';b.textContent='Aim for 1:00 to 2:00';return;}
  if(s<60){b.className='pr-band short';b.textContent='A little short. Add a detail to Card 2.';}
  else if(s<=120){b.className='pr-band ok';b.textContent='Just right.';}
  else{b.className='pr-band long';b.textContent='A bit long. Trim a sentence or two.';}}
function prPaintTries(){var t=prGet('tries',[]),el=document.getElementById('prTries');if(el)el.textContent=t.length?('Practice runs: '+t.map(prFmt).join(', ')):'';}
function prToggle(){
  var go=document.getElementById('prGo'),clk=document.getElementById('prClock');
  if(_prT){clearInterval(_prT);_prT=null;go.textContent='▶ Start';
    var t=prGet('tries',[]);t.push(Math.round(_prSecs));if(t.length>5)t.shift();prSet('tries',t);prPaintTries();prBand(_prSecs);gatherAnswers();return;}
  _prStart=Date.now();_prSecs=0;go.textContent='■ Stop';prBand(0);
  _prT=setInterval(function(){_prSecs=(Date.now()-_prStart)/1000;clk.textContent=prFmt(_prSecs);},250);
}
function prReset(){if(_prT){clearInterval(_prT);_prT=null;}_prSecs=0;document.getElementById('prClock').textContent='0:00';document.getElementById('prGo').textContent='▶ Start';prBand(0);}
function prCheck(b){var c=prGet('checks',[]),v=b.getAttribute('data-c'),i=c.indexOf(v);if(i>=0)c.splice(i,1);else c.push(v);prSet('checks',c);prPaint();gatherAnswers();}
function prPath(b){prSet('path',b.getAttribute('data-p'));prPaint();gatherAnswers();}
function prPaint(){
  var c=prGet('checks',[]),p=prGet('path','');
  document.querySelectorAll('.pr-chk').forEach(function(b){b.classList.toggle('on',c.indexOf(b.getAttribute('data-c'))>=0);});
  document.querySelectorAll('.pr-path').forEach(function(b){b.classList.toggle('on',b.getAttribute('data-p')===p);});
  ['video','listener'].forEach(function(k){var e=document.getElementById('prPane-'+k);if(e)e.classList.toggle('show',k===p);});
}
function prGatherText(){
  var t=prGet('tries',[]),c=prGet('checks',[]),p=prGet('path',''),l=document.getElementById('journal-listener');
  var o='\n📹 HOW I PRESENTED\n────────────────────────────────\n';
  o+='Practice runs: '+(t.length?t.map(prFmt).join(', '):'(none yet)')+'\n';
  o+='Speaker checks: '+(c.length?c.join(', '):'(none yet)')+'\n';
  o+='How I presented: '+(p==='video'?'Video (turned in on Canvas)':p==='listener'?'To a grown-up at home':'(not chosen yet)')+'\n';
  if(p==='listener')o+='\nListener Card\n'+((l&&l.value.trim())||'(no answer)')+'\n';
  return o;
}
(function(){prPaint();prPaintTries();})();
"""
h4 = rep(h4, '/* DOWNLOAD PDF */\nfunction downloadJournal(){', PRJS + '\n/* DOWNLOAD PDF */\nfunction downloadJournal(){', 'js anchor')

# standards: titles, Part A tags, new block 32.4-12
m = re.search(r'(<script type="application/json" id="oao-standards">)(.*?)(</script>)', h4, re.S)
S = json.loads(m.group(2)); B = {b['id']: b for b in S['blocks']}
B['32.4-09']['title'] = '🎤 Plan Your Talk'
c21 = {k: B['32.4-09'][k] for k in B['32.4-09'] if k not in ('id', 'title')}
B['32.4-10'].update(dict(c21, title='🎤 Part A: My Talk'))
B['32.4-11']['title'] = '✍️ Part B: My Last Line'
if '32.4-12' not in B:
    S['blocks'].append(dict({'id': '32.4-12', 'title': '📹 Part C: Rehearse and Present'}, **{k: v for k, v in c21.items()}))
for st in ('FL', 'TX', 'AR', 'MO', 'AL', 'TN'):
    for b in S['blocks']:
        for code in (b.get(st) or []):
            if isinstance(S['lesson_tags'].get(st), list) and code not in S['lesson_tags'][st]: S['lesson_tags'][st].append(code)
h4 = h4[:m.start(2)] + json.dumps(S, ensure_ascii=False) + h4[m.end(2):]

D4 = json.load(io.open('data/lesson-32-4.json', encoding='utf-8'))
todo4 = [t for t in D4['todo'] if t['find'] not in ('Getting Ready to Celebrate', 'Part A', 'Final Sentence')]
todo4 += [{"find": "Plan Your Talk", "steps": ["Read the four cue cards.", "Pick your listener.", "Say Card 1 out loud once."]},
          {"find": "My Talk", "steps": ["Write Card 1, Card 2 and Card 3 the way you will say them.", "On Card 2, copy one sentence from Piece 1 and one from Piece 3."]},
          {"find": "My Last Line", "steps": ["Write one true sentence to end your talk."]},
          {"find": "Rehearse and Present", "steps": ["Tap Start, give your talk out loud, tap Stop.", "Tap the speaker checks you did.", "Pick video or grown-up, and present.", "Turn in your video or listener card, plus your cue cards."]}]
patch4 = {
 "connector": "The last day. Yesterday you built your portfolio. Today you present it: one to two minutes, out loud, to a real listener.",
 "scholar": {"journal-q1": "… and name the first book you read this year.",
             "journal-q2": "… and say which week the change started.",
             "journal-q3": "… and say how you will know you met it."},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "counters": {"journal-q1": 24, "journal-q2": 40, "journal-q3": 24},
 "wgrd": {"catcher": {"title": "My talk on one card", "intro": "Four cards, about two minutes.",
                      "fields": [{"label": "Card 1: Open", "hint": "", "rows": 1}, {"label": "Card 2: Show the change", "hint": "", "rows": 2},
                                 {"label": "Card 3: Look forward", "hint": "", "rows": 1}],
                      "end": {"label": "Card 4: My last line", "hint": ""}},
          "useAt": ["journal-q1", "journal-q2", "journal-q3"]},
 "transcripts": dict(D4['transcripts'],
     welcome="Hoo! It’s Opti. The last day of 4th grade ELA. Today you present your portfolio, out loud, to a real listener. Today’s question: what can you do now that you couldn’t do in September?",
     read="Four cue cards. Open with your title and who you were in Week 1. Read one sentence from Piece 1 and one from Piece 3, and say what changed. Share your goal. Then end with your last line. Slow down, and look up."),
 "todo": todo4,
}

if APPLY:
    io.open(P3, 'w', encoding='utf-8', newline='').write(h3)
    io.open(P4, 'w', encoding='utf-8', newline='').write(h4)
    io.open('/tmp/pr_patch.json', 'w', encoding='utf-8').write(json.dumps(patch4, ensure_ascii=False))
    r = subprocess.run([sys.executable, 'tools/setdata.py', P4, 'data/lesson-32-4.json', '/tmp/pr_patch.json', '--apply'], capture_output=True, text=True)
    print(r.stdout, r.stderr); print('written both')
else:
    print('dry run ok')
# Applied after the run (Nov 22): activity-num badges in each Word Study tab renumbered 1..n in page order, so kept blocks start at 1.
