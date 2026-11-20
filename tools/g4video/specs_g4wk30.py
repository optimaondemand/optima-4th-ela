# Week 30 G4 ELA Word Study films (Prince Caspian Ch. 13-15), Nell. SILENT for now (Q4: voiced later).
# Never a page answer: 30.1 lists base meanings only (the page prints them beside each blank); 30.2 the dialogue rule with a
# made-up line; 30.3 hopeful (page words: separation, celebration, restoration, forgettable); 30.4 the checklist, no lines.
def D(w, m): return '<div class="def"><b>%s</b><span>%s</span></div>' % (w, m)
V = {}
V['g4ela-30-1-morphology'] = dict(title='Word Study', sub='Every base in the unit', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🏛️ The whole unit, in one breath</div>'),
   ('Port, carry', '<div class="steps"><span><i>📦</i>port · carry</span><span><i>🪢</i>tract · pull</span><span><i>🧱</i>struct · build</span></div>')]),
 dict(at='Spect, look', items=[(None, '<div class="steps"><span><i>👀</i>spect · look</span><span><i>🤾</i>ject · throw</span><span><i>✍️</i>script · write</span></div>')]),
 dict(at='Rupt, break', items=[(None, '<div class="steps"><span><i>💥</i>rupt · break</span><span><i>🧭</i>duct · lead</span><span><i>🔷</i>form · shape</span></div>')]),
 dict(at='Take a long word apart', items=[(None, '<div class="ask">🤔 Take a long word apart. It tells you what it means.</div>')]),
])
V['g4ela-30-2-grammar'] = dict(title='Grammar', sub='Dialogue marks', scenes=[
 dict(at=None, items=[(None, '<div class="lab">💬 Talk on the page</div>'),
   ('Quotation marks go around the exact words', '<div class="say">“ the exact words ”</div>')]),
 dict(at='The comma or the end mark goes inside', items=[(None, '<div class="quote q3">“Over here<span class="hl">,”</span> said Lucy.</div>')]),
 dict(at='Then the tag', items=[(None, '<div class="say">said Trumpkin · cried Edmund</div>')]),
 dict(at='A fast shout can be just a fragment', items=[(None, '<div class="quote q3">“Up<span class="hl">!”</span> cried the Bear.</div>')]),
])
V['g4ela-30-3-spelling'] = dict(title='Word Study', sub='Stack the rules', scenes=[
 dict(at=None, items=[(None, '<div class="lab">🧱 A hard word is easy rules, stacked</div>')]),
 dict(at='Hopeful', items=[(None, '<div class="huge">hope + ful</div>'),
   ('the e stays', '<div class="say">ful starts with a consonant, so the e stays</div>')]),
 dict(at='Take the word apart', items=[(None, '<div class="steps"><span><i>1️⃣</i>take it apart</span><span><i>2️⃣</i>one rule at a time</span><span><i>3️⃣</i>put it back together</span></div>'),
   ('put it back together', '<div class="huge">hope<span class="gold">ful</span></div>')]),
])
V['g4ela-30-4-grammar'] = dict(title='Grammar', sub='Check every line of talk', scenes=[
 dict(at=None, items=[(None, '<div class="lab">✏️ Last editing day for this book</div>')]),
 dict(at='Are the exact words inside quotation marks', items=[(None, '<div class="steps"><span><i>1️⃣</i>words inside “ ”</span></div>')]),
 dict(at='Is the comma or end mark inside too', items=[(None, '<div class="steps"><span><i>1️⃣</i>words inside “ ”</span><span><i>2️⃣</i>, ! ? inside too</span></div>')]),
 dict(at='Does the tag join with a comma', items=[(None, '<div class="steps"><span><i>1️⃣</i>words inside “ ”</span><span><i>2️⃣</i>, ! ? inside too</span><span><i>3️⃣</i>tag joins with a comma</span></div>'),
   ('Fix each one', '<div class="ask">✏️ Fix each one. Say why.</div>')]),
])
