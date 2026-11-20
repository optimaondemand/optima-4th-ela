# Week 27 G4 ELA Word Study films (Prince Caspian Ch. 4-6), Nell. SILENT for now (Q4: voiced later).
# Never a page answer: 27.1 says and shows porter/tractor/structure (the page's fill-ins are transport/extract/construct/import);
# 27.2 shows Lewis's Ch. 5 sentence (the page asks students to tap its but; the film names the job, not the tap);
# 27.3 shows the begin/visit worked example the page itself gives (the fill-ins also include forget/travel);
# 27.4 uses a new pair (Caspian was tired, but/so he rode on), not a 27.4 tap item.
def D(w, m): return '<div class="def"><b>%s</b><span>%s</span></div>' % (w, m)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
V['g4ela-27-1-morphology'] = dict(title='Word Study', sub='Bases that carry, pull and build', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🏛️ Old Latin bases</div>'),
   ('Port means carry', D('port', 'carry 📦')), ('Tract means pull', D('tract', 'pull 🪢'))]),
 dict(at='Struct means build', items=[(None, D('struct', 'build 🧱')),
   ('Find the base', '<div class="say"><b>port</b>er · <b>tract</b>or · <b>struct</b>ure</div>')]),
 dict(at='ask what it does', items=[(None, '<div class="ask">🤔 What does the base do in the word?</div>'),
   ('set a treasure back', PILL('Then set a treasure back in its place'))]),
])
V['g4ela-27-2-grammar'] = dict(title='Grammar', sub='But and so', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🚪 Two tiny hinges</div>'),
   ('But says', '<div class="say"><b>but</b> = here comes a surprise</div>')]),
 dict(at='Caspian’s heart was sinking', items=[(None, '<div class="quote q3">Caspian’s heart was sinking<span class="hl">, but</span> he tried to take it all in.</div>')]),
 dict(at='So says', items=[(None, '<div class="say"><b>so</b> = here’s what happened because of it</div>'),
   ('Put a comma before each', '<div class="ask">✏️ comma before <b>but</b> and <b>so</b> when they join two whole sentences</div>')]),
])
V['g4ela-27-3-spelling'] = dict(title='Word Study', sub='Listen for the beat', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🥁 Say it. Where is the strong beat?</div>'),
   ('Be-GIN', '<div class="huge">be·<span class="gold">GIN</span></div>')]),
 dict(at='If the beat is on the last part', items=[(None, '<div class="steps"><span><i>1️⃣</i>beat on the last part</span><span><i>2️⃣</i>one vowel + one consonant</span></div>'),
   ('double the consonant', '<div class="say">be·gin + <b>n</b> + ing</div>')]),
 dict(at='VIS-it', items=[(None, '<div class="huge"><span class="gold">VIS</span>·it</div>'),
   ('so no double', '<div class="say">beat at the front: no double</div>')]),
])
V['g4ela-27-4-grammar'] = dict(title='Grammar', sub='The right hinge', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Editing day</div>'),
   ('ask if the logic is right', '<div class="say"><b>but</b> = surprise · <b>so</b> = because of it</div>')]),
 dict(at='Caspian was tired, but', items=[(None, '<div class="quote q3">Caspian was tired<span class="hl">, but</span> he rode on. ✅</div>')]),
 dict(at='Caspian was tired, so', items=[(None, '<div class="quote q3">Caspian was tired<span class="hl">, so</span> he rode on. ❌</div>'),
   ('One small word', '<div class="say">One small word. The meaning flips.</div>')]),
])
