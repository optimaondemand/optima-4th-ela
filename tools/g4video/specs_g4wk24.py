# Week 24 G4 ELA Word Study films (Freedom Train Ch. 18-20 + whole book), Marcus clips.
# Never shows a page answer: 24.1 roots+meanings only (no transport/erupt/instructions/predict);
# 24.2 baggage car / through the woods (not the page sentence); 24.3 rules only, no finished words;
# 24.4 a new over-stuffed sentence, not one of the page's tap sentences.
def D(w, m): return '<div class="def"><b>%s</b><span>%s</span></div>' % (w, m)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
V['g4ela-24-1-morphology'] = dict(title='Word Study', sub='Year-end roots', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧵 Last root review of the year</div>'),
   ('Port means carry', D('port', 'carry')),
   ('Rupt means break', D('rupt', 'break')),
 ]),
 dict(at='Struct means build', items=[
   (None, D('struct', 'build')),
   ('Dict means say', D('dict', 'say')),
 ]),
 dict(at='Ask what each word is doing', items=[
   (None, '<div class="bins" style="gap:18px;flex-wrap:wrap;justify-content:center;max-width:720px"><span>📦 carry</span><span>💥 break</span><span>🧱 build</span><span>🗣️ say</span></div>'),
   ('Then sew the patch', PILL('Then sew the patch')),
 ]),
])
V['g4ela-24-2-grammar'] = dict(title='Grammar', sub='Little packages', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">📦 A prepositional phrase is a little package</div>'),
   ('It starts with a word like', '<div class="say">Starts with: <b>in · on · under · through</b></div>'),
   ('and it ends with a noun', '<div class="say">Ends with: a <b>noun</b></div>'),
 ]),
 dict(at='In the baggage car', items=[
   (None, '<div class="quote q3"><span class="hl">in</span> the baggage <span class="hl">car</span></div>'),
   ('Through the woods', '<div class="quote q3"><span class="hl">through</span> the <span class="hl">woods</span></div>'),
 ]),
 dict(at='Find the first word', items=[
   (None, '<div class="steps"><span><i>1️⃣</i>find the first word</span><span><i>2️⃣</i>find the noun that closes it</span></div>'),
 ]),
])
V['g4ela-24-3-spelling'] = dict(title='Word Study', sub='Four rules', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">📅 The whole year in four words</div>'),
   ('double the last letter', '<div class="say">👯 Short vowel + one consonant → <b>double it</b></div>'),
 ]),
 dict(at='drop the silent e', items=[
   (None, '<div class="say">✂️ Silent <b>e</b> on the end → <b>drop it</b></div>'),
   ('change y to i', '<div class="say">🔁 Consonant + <b>y</b> → <b>change y to i</b></div>'),
 ]),
 dict(at='Look at the end of the base word', items=[
   (None, '<div class="ask">🔎 Look at the end of the base word first.</div>'),
   ('It tells you which rule fires', '<div class="say">It tells you which rule fires.</div>'),
 ]),
])
V['g4ela-24-4-grammar'] = dict(title='Grammar', sub='The editor’s cut', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✂️ Last grammar job: the editor’s cut</div>'),
   ('the action gets buried', '<div class="quote q3">Up the hill, past the church, over the bridge, by the old oak, <span class="hl">she climbed</span>.</div>'),
 ]),
 dict(at='Keep the ones the reader needs', items=[
   (None, '<div class="quote q3">Over the bridge, <span class="hl">she climbed</span>.</div>'),
   ('Cut the rest', '<div class="say">✂️ Keep what the reader needs. Cut the rest.</div>'),
 ]),
 dict(at='Then read it out loud', items=[
   (None, '<div class="say">🗣️ Read it out loud.</div>'),
   ('You should hear the verb again', '<div class="ask">👂 Can you hear the verb again?</div>'),
 ]),
])
