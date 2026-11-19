# Week 23 G4 ELA Word Study films (Freedom Train Ch. 15-17), Marcus clips.
# Never shows an answer the page asks for: elevator (not the page words except resist, which the clip says),
# faster horse, abolition/abolish (the page's own model), more slower / sang sweeter (not the 23.4 tap items).
def D(w, m): return '<div class="def"><b>%s</b><span>%s</span></div>' % (w, m)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
V['g4ela-23-1-morphology'] = dict(title='Word Study', sub='lev + sist', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧵 Two new roots</div>'),
   ('Lev means lift', D('lev', 'lift')),
   ('Think of an elevator', '<div class="say">🛗 An <u>elev</u>ator <b>lifts</b> you up.</div>'),
 ]),
 dict(at='Sist means stand', items=[
   (None, D('sist', 'stand')),
   ('When you resist', '<div class="say">✋ When you re<u>sist</u>, you <b>stand</b> against something.</div>'),
 ]),
 dict(at='Every word today', items=[
   (None, '<div class="bins"><span>⬆️ lift</span><span>🧍 stand</span></div>'),
   ('Ask which one', '<div class="ask">🤔 Lifting or standing?</div>'),
   ('then sew the patch', PILL('Then sew the patch')),
 ]),
])
V['g4ela-23-2-grammar'] = dict(title='Grammar', sub='Adjective or adverb?', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🐎 One word, two jobs</div>'),
   ('Faster can describe a horse', '<div class="quote q3">a <span class="hl">faster</span> horse</div>'),
   ('or it can describe how the horse runs', '<div class="quote q3">The horse runs <span class="hl">faster</span>.</div>'),
 ]),
 dict(at='When it describes a thing', items=[
   (None, '<div class="say">faster <b>horse</b> → describes a thing → <b>adjective</b></div>'),
   ('When it tells how someone did something', '<div class="say"><b>runs</b> faster → tells how → <b>adverb</b></div>'),
 ]),
 dict(at='So don’t just spot', items=[
   (None, '<div class="say">Don’t just spot the comparing words.</div>'),
   ('Ask what each one is describing', '<div class="ask">🤔 What is it describing?</div>'),
 ]),
])
V['g4ela-23-3-spelling'] = dict(title='Word Study', sub='Lazy vowels', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">😴 The trick for lazy vowels</div>'),
   ('In abolition', '<div class="huge">ab·<span class="gold">o</span>·LI·tion</div>'),
   ('you can barely hear the o', '<div class="say">The <b>o</b> fades to a lazy “uh.”</div>'),
 ]),
 dict(at='So find a relative', items=[
   (None, '<div class="lab">🔎 Find a relative where it’s stressed</div>'),
   ('Abolish', '<div class="huge">a·<span class="gold">BOL</span>·ish</div>'),
   ('Now the o is loud and clear', '<div class="say">Now the <b>o</b> is loud and clear!</div>'),
 ]),
 dict(at='Say the relative', items=[
   (None, '<div class="steps"><span><i>🗣️</i>say the relative</span><span><i>✏️</i>spell the long word</span></div>'),
 ]),
])
V['g4ela-23-4-grammar'] = dict(title='Grammar', sub='Editing day', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✂️ Editing day</div>'),
   ('Some comparing words are already right', '<div class="say">✅ Right already? Leave it alone.</div>'),
 ]),
 dict(at='Look for two mistakes', items=[
   (None, '<div class="lab">Two mistakes to hunt</div>'),
   ('One is doubling up', '<div class="swap"><s>more</s> slower → <b>slower</b></div>'),
   ('The other is an adjective', '<div class="swap">sang <s>sweeter</s> → sang <b>more sweetly</b></div>'),
 ]),
 dict(at='Fix those', items=[
   (None, '<div class="say">🗣️ Read the sentence out loud to check.</div>'),
 ]),
])
