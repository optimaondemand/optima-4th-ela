# Week 28 G4 ELA Word Study films (Prince Caspian Ch. 7-9), Nell. SILENT for now (Q4: voiced later).
# Never a page answer: 28.1 respect/eject/scribe (page answers: inspect, reject, manuscript, spectacle; check-in: spectacles);
# 28.2 "Because Peter was worn out, he answered shortly." (not the page's Ch. 8 spotter); 28.3 opposite/oppose (page: definite,
# composition, separate, council); 28.4 "Because it was raining." (not a 28.4 tap line).
def D(w, m): return '<div class="def"><b>%s</b><span>%s</span></div>' % (w, m)
V = {}
V['g4ela-28-1-morphology'] = dict(title='Word Study', sub='Look, throw and write', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🏛️ Three more Latin bases</div>'),
   ('Spect means look', D('spect', 'look 👀')), ('Ject means throw', D('ject', 'throw 🤾'))]),
 dict(at='so to respect someone', items=[(None, '<div class="say">re<b>spect</b> = look up to</div>'),
   ('so eject means throw out', '<div class="say">e<b>ject</b> = throw out</div>')]),
 dict(at='Script and scribe mean write', items=[(None, D('script · scribe', 'write ✍️')),
   ('a scribe is a person', '<div class="say">a <b>scribe</b> = a person whose job is writing</div>')]),
 dict(at='Find the base', items=[(None, '<div class="ask">🤔 Find the base. The word starts to explain itself.</div>')]),
])
V['g4ela-28-2-grammar'] = dict(title='Grammar', sub='Sentences that lean', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🪜 Little words that make a clause lean</div>'),
   ('because, although, when or if', '<div class="say"><b>because · although · when · if</b></div>')]),
 dict(at='Because Peter was worn out', items=[(None, '<div class="quote q3"><span class="hl">Because</span> Peter was worn out, he answered shortly.</div>')]),
 dict(at='The because part can’t stand alone', items=[(None, '<div class="say">“Because Peter was worn out.” ❌ can’t stand alone</div>'),
   ('put a comma after it', '<div class="ask">✏️ Leaning part first? Put a comma after it.</div>')]),
])
V['g4ela-28-3-spelling'] = dict(title='Word Study', sub='Find the loud cousin', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🔇 Schwa: the lazy “uh”</div>'),
   ('find a cousin of the word', '<div class="say">Find a cousin where the vowel is loud.</div>')]),
 dict(at='Opposite sounds like uh', items=[(None, '<div class="huge">opp·<span class="gold">?</span>·site</div>')]),
 dict(at='But oppose says its o clearly', items=[(None, '<div class="huge">op·<span class="gold">POSE</span></div>'),
   ('So opposite has an o', '<div class="huge">opp<span class="gold">o</span>site</div>')]),
])
V['g4ela-28-4-grammar'] = dict(title='Grammar', sub='Pieces and joints', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Editing day</div>'),
   ('Does it stand on its own?', '<div class="ask">🤔 Does it stand on its own?</div>')]),
 dict(at='Because it was raining', items=[(None, '<div class="quote q3">Because it was raining. ❌</div>'),
   ('That’s a piece', '<div class="say">a piece, not a sentence</div>')]),
 dict(at='Does it run two sentences together', items=[(None, '<div class="say">two sentences, no joint? ❌</div>'),
   ('Fix the piece', '<div class="steps"><span><i>1️⃣</i>fix the piece</span><span><i>2️⃣</i>mend the joint</span><span><i>3️⃣</i>say why</span></div>')]),
])
