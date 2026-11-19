# Week 22 G4 ELA Word Study films (Freedom Train Ch. 10-14), Marcus clips.
# Never shows an answer the page asks for: examples are imagine/music, "moved slowly and quietly past the guard",
# "really dark", "ran very fast" (not in the page's own tasks).
def D(w, m): return '<div class="def"><b>%s</b><span>%s</span></div>' % (w, m)
PILL = lambda t: '<span class="pill">👆 %s</span>' % t
V = {}
V['g4ela-22-1-morphology'] = dict(title='Word Study', sub='press + tain', scenes=[
 dict(at=None, layout='cols', items=[
   (None, '<div class="lab">🧵 Two new roots this week</div>'),
   ('One means push', D('press', 'push')),
   ('One means hold', D('tain', 'hold')),
 ]),
 dict(at='Think of a printing press', items=[
   (None, '<div class="say">🖨️ A printing <u>press</u> <b>pushes</b> ink onto paper.</div>'),
   ('or a jar that holds jam', '<div class="say">🫙 A jar <b>holds</b> jam.</div>'),
 ]),
 dict(at='Every word in the quilt', items=[
   (None, '<div class="bins"><span>👉 push</span><span>✊ hold</span></div>'),
   ('Ask which one', '<div class="ask">🤔 Pushing or holding?</div>'),
   ('then sew', PILL('Then sew the patch')),
 ]),
])
V['g4ela-22-2-spelling'] = dict(title='Word Study', sub='-ive · -al · -ic', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✨ Endings that make describing words</div>'),
   ('These endings', '<div class="chips"><span>-ive</span><span>-al</span><span>-ic</span></div>'),
 ]),
 dict(at='Here’s the tricky part', items=[
   (None, '<div class="lab">⚠️ The tricky part</div>'),
   ('Some starting words end in a silent e', '<div class="swap">imagin<s>e</s> + ive → <b>imaginative</b></div>'),
   ('Some lose nothing at all', '<div class="swap">music + al → <b>musical</b></div>'),
 ]),
 dict(at='So don’t trust your ears', items=[
   (None, '<div class="say">👂 Don’t trust your ears.</div>'),
   ('Look hard at the starting word', '<div class="steps"><span><i>👀</i>look at the start word</span><span><i>🔨</i>build</span></div>'),
 ]),
])
V['g4ela-22-3-grammar'] = dict(title='Grammar', sub='One strong verb', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✍️ A writer’s trick</div>'),
   ('When a sentence needs two little helper words', '<div class="quote q3">He <span class="t1">moved</span> <span class="t2">slowly</span> and <span class="t2">quietly</span> past the guard.</div>'),
   ('the verb underneath is usually too weak', '<div class="say">The verb is doing too little.</div>'),
 ], hl=[('two little helper words', '.t2'), ('the verb underneath', '.t1')]),
 dict(at='Swap in one strong verb', items=[
   (None, '<div class="swap"><s>moved slowly and quietly</s> → <b>crept</b></div>'),
   ('and the helpers can go', '<div class="quote good q3">He <span class="hl">crept</span> past the guard.</div>'),
 ]),
 dict(at='Say both versions out loud', items=[
   (None, '<div class="say">🗣️ Say both versions out loud.</div>'),
   ('Which one sounds like', '<div class="ask">🤫 Which one sounds like sneaking past a guard?</div>'),
 ]),
])
V['g4ela-22-4-grammar'] = dict(title='Grammar', sub='The editor’s cut', scenes=[
 dict(at=None, items=[
   (None, '<div class="lab">✂️ Today you’re the editor</div>'),
   ('Some little words', '<div class="chips"><span>very</span><span>really</span><span>quite</span></div>'),
   ('but say nothing at all', '<div class="say">They sound big. They say nothing.</div>'),
 ]),
 dict(at='Read each sentence without', items=[
   (None, '<div class="quote q3">The night was <s>really</s> dark.</div>'),
   ('If nothing is lost, cut it', '<div class="say">Nothing lost? ✂️ <b>Cut it.</b></div>'),
 ]),
 dict(at='If the verb feels weak', items=[
   (None, '<div class="quote q3">He ran <s>very fast</s>.</div>'),
   ('find a stronger one', '<div class="quote good q3">He <span class="hl">sprinted</span>.</div>'),
 ]),
])
