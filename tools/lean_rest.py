#!/usr/bin/env python3
"""Fewer words for sparkled G4 ELA weeks WITHOUT What-to-do boxes (weeks 8+), Nov 10 2026.
Uses the safe subset of tools/lean.py: vocab lead-in, vocab model heading, Writer's Workshop
"Now you try" and book-link fold, shorter "Your turn!", one think-question per box.
Keeps every instruction line (with one-step-at-a-time on, the page's own lines ARE the steps).

    python tools/lean_rest.py lesson-8-1-anne-ch6.html [...] --apply
"""
import re, sys, io, importlib.util, os
spec = importlib.util.spec_from_file_location('lean', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lean.py'))
src = io.open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'lean.py'), encoding='utf-8').read()
src = src.split('\nfor f in sys.argv[1:]:')[0]          # rules + one_question only
ns = {}; exec(src, ns)
KEEP = {'vocab-lead', 'vocab-model-h', 'ww-now-you-try', 'ww-book-fold', 'vocab-your-turn'}
APPLY = '--apply' in sys.argv
for f in [a for a in sys.argv[1:] if not a.startswith('--')]:
    h0 = h = io.open(f, encoding='utf-8', newline='').read(); log = []
    for name, pat, rep in ns['RULES']:
        if name not in KEEP: continue
        h, c = re.subn(pat, rep, h, flags=re.S)
        if c: log.append('%s x%d' % (name, c))
    h, c = ns['one_question'](h)
    if c: log.append('one-question x%d' % c)
    if APPLY and h != h0: io.open(f, 'w', encoding='utf-8', newline='').write(h)
    print(os.path.basename(f), len(h) - len(h0), ', '.join(log) or '-')
