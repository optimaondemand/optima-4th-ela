# Week 26 G4 ELA Word Study films (Prince Caspian Ch. 1-3), Nell. SILENT for now (Q4: voiced later).
# Never a page answer: 26.1 prefix meanings only (no preview/return/transport/international);
# 26.2 bread and cheese (not a page sentence); 26.3 unhappy (not familiar/transport/discover/desert);
# 26.4 and and and (a new sentence).
def D(w, m): return '<div class="def"><b>%s</b><span>%s</span></div>' % (w, m)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
V['g4ela-26-1-morphology'] = dict(title='Word Study', sub='Prefixes of time and place', scenes=[
 dict(at=None, items=[(None, '<div class="lab">⏳ Word parts that tell when and where</div>'),
   ('Pre means before', D('pre-', 'before ⏮️')), ('Re means again', D('re-', 'again, back 🔁'))]),
 dict(at='Trans means across', items=[(None, D('trans-', 'across ➡️')), ('Inter means between', D('inter-', 'between ↔️'))]),
 dict(at='Find the part at the front', items=[(None, '<div class="ask">🤔 What does the front part add?</div>'),
   ('set one more treasure back', PILL('Then set a treasure back in its place'))]),
])
V['g4ela-26-2-grammar'] = dict(title='Grammar', sub='And or or?', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔗 Two small words, two big jobs</div>'),
   ('And says both things are true', '<div class="say"><b>and</b> = both</div>'), ('Or says choose one', '<div class="say"><b>or</b> = choose one</div>')]),
 dict(at='The bread and the cheese', items=[(None, '<div class="quote q3">the bread <span class="hl">and</span> the cheese 🍞🧀</div>'),
   ('The bread or the cheese', '<div class="quote q3">the bread <span class="hl">or</span> the cheese 🍞❓🧀</div>')]),
 dict(at='When you see or', items=[(None, '<div class="ask">🤔 When you see <b>or</b>: what is the choice?</div>')]),
])
V['g4ela-26-3-spelling'] = dict(title='Word Study', sub='Take long words apart', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✂️ Long words come apart</div>'),
   ('Peel off the beginning and the ending first', '<div class="steps"><span><i>1️⃣</i>peel off the beginning</span><span><i>2️⃣</i>peel off the ending</span></div>')]),
 dict(at='Unhappy', items=[(None, '<div class="huge"><span class="gold">un</span>·happy</div>'),
   ('there’s happy', '<div class="say">What’s left is a word you know: <b>happy</b></div>')]),
 dict(at='Then the syllables almost split themselves', items=[(None, '<div class="huge">un·hap·py</div>')]),
])
V['g4ela-26-4-grammar'] = dict(title='Grammar', sub='The right joining word', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Editing day</div>'),
   ('Ask if it’s doing the right job', '<div class="say"><b>and</b> adds · <b>or</b> offers a choice</div>')]),
 dict(at='And if a sentence has', items=[(None, '<div class="quote q3">It was cold <span class="hl">and</span> wet <span class="hl">and</span> dark <span class="hl">and</span> late <span class="hl">and</span> quiet.</div>')]),
 dict(at='it’s time to cut a few', items=[(None, '<div class="quote q3">It was cold, wet, and dark.</div>'),
   ('let one idea lead', '<div class="say">✂️ Cut a few. Let one idea lead.</div>')]),
])
