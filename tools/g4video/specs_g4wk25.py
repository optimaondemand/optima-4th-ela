# Week 25 G4 ELA Word Study films (Freedom Train: comparing sources), Marcus. SILENT for now (Q4: voiced later).
# Never shows a page answer: 25.1 prefix meanings only (no portation/national/marine/natural); 25.2 rice, cotton, corn
# (not a page list); 25.3 rules with new examples; 25.4 counting commas with a new sentence.
def D(w, m): return '<div class="def"><b>%s</b><span>%s</span></div>' % (w, m)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
V['g4ela-25-1-morphology'] = dict(title='Word Study', sub='Prefixes that tell where', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧭 Word parts that tell where</div>'),
   ('Trans means across', D('trans-', 'across ➡️')),
   ('Inter means between', D('inter-', 'between ↔️')),
 ]),
 dict(at='Sub means under', items=[
   (None, D('sub-', 'under ⬇️')),
   ('Super means above or beyond', D('super-', 'above, beyond ⬆️')),
 ]),
 dict(at='Put one in front of a word', items=[
   (None, '<div class="say">The prefix tells the word <b>where it’s going</b>.</div>'),
   ('Find the part that tells where', PILL('Then sew the border patch')),
 ]),
])
V['g4ela-25-2-grammar'] = dict(title='Grammar', sub='Commas in a list', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🧺 Where does one thing stop?</div>'),
   ('Rice, cotton, and corn', '<div class="quote q3">rice<span class="hl">,</span> cotton<span class="hl">,</span> and corn</div>'),
 ]),
 dict(at='Without the commas', items=[
   (None, '<div class="quote q3">rice cotton and corn</div>'),
   ('as one thing', '<div class="ask">🤔 Is “rice cotton” one thing?</div>'),
 ]),
 dict(at='Put a comma after every item', items=[
   (None, '<div class="steps"><span><i>1️⃣</i>a comma after each item</span><span><i>2️⃣</i>keep the one before “and”</span></div>'),
 ]),
])
V['g4ela-25-3-spelling'] = dict(title='Word Study', sub='Words that sound alike', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">🔍 Real words in the wrong place</div>'),
   ('Affect is the action', '<div class="say">⚡ <b>affect</b> = the action &nbsp;·&nbsp; 🎯 <b>effect</b> = the result</div>'),
 ]),
 dict(at='It’s means it is', items=[
   (None, '<div class="say">🗣️ <b>it’s</b> = it is &nbsp;·&nbsp; 🎒 <b>its</b> = belongs to it</div>'),
 ]),
 dict(at='say the long form out loud', items=[
   (None, '<div class="ask">🗣️ Say the long form out loud.</div>'),
   ('If it sounds wrong', '<div class="say">If it sounds wrong, it is.</div>'),
 ]),
])
V['g4ela-25-4-grammar'] = dict(title='Grammar', sub='A last comma check', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✏️ Editing day</div>'),
   ('If you hear three things', '<div class="quote q3">a map<span class="hl">,</span> a lantern<span class="hl">,</span> and a coat</div>'),
   ('you need two commas', '<div class="say">3 things → <b>2 commas</b></div>'),
 ]),
 dict(at='A comma can change what a sentence means', items=[
   (None, '<div class="ask">🤔 How many things are in the list?</div>'),
   ('count your commas', '<div class="say">Then count your commas.</div>'),
 ]),
 dict(at='One more slow read', items=[
   (None, '<div class="say">🎤 One more slow read. Then present!</div>'),
 ]),
])
