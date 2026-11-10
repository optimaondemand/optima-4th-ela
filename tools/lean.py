#!/usr/bin/env python3
"""Fewer words on the page (G3 ELA pilot feedback, Nov 10 2026, applied to G4 ahead of review: "a lot of
reading for 3rd grade"). Cuts the boxes that repeat the What to do line or
stack extra think-questions; Opti reads what is left. Same cuts every week.

    python tools/g3sparkle/lean.py lesson-18-1-wb.html [...]

Idempotent; prints what it cut per file. Never touches DATA, answers,
games or anything a student types into."""
import re, sys, io

RULES = [
  # (WGRD "How to Do It" stays: a standing G3-5 piece. With read-to-me it
  #  folds behind Opti's read-along instead of being cut.)
  # Morphology: "Hunt the two word parts" box
  ('morph-hunt', r'\s*<div class="key-concept"><div class="key-concept-label">(?:&#x1F50D;|🔍) Hunt [^<]*</div>\s*<p>.*?</p>\s*</div>', ''),
  # Vocabulary: the lead-in line before the three steps
  ('vocab-lead', r'\s*<p>When you meet a word you don\'t know, use these three steps <em>in order</em>:</p>', ''),
  # Vocabulary: the empty "Let's try it together" box becomes a one-line heading
  ('vocab-model-h', r'<div class="key-concept">\s*<div class="key-concept-label">📌 Let\'s try it together: "([^"]+)"</div>\s*</div>',
   r'<div class="g3-model-h">Watch how we figure out <b>\1</b>:</div>'),
  # Grammar / spelling: the notice-first box repeats the What to do line
  ('notice-first', r'(<!-- (?:grammar|spell)-notice-first -->)\s*<div class="key-concept[^"]*"[^>]*>\s*<div class="key-concept-label"[^>]*>[^<]*</div>\s*<p>.*?</p>\s*</div>', r'\1'),
  # ── G4 (Nov 10 2026) ──
  # Writer's Workshop: "Now you try" repeats the box right under it
  ('ww-now-you-try', r'\s*<div class="callout callout-info"[^>]*><span class="callout-icon">📝</span><p[^>]*><strong>Now you try\.</strong> Use what Sam showed you\. Borrow a sentence frame if you want\.</p></div>', ''),
  # Writer's Workshop: the book link folds behind one line
  ('ww-book-fold', r'<div class="callout callout-info"([^>]*)><span class="callout-icon">📖</span><p([^>]*)><strong>(\w+) did it too\.</strong>(.*?)</p></div>',
   r'<details class="nav-fold"><summary>📖 How \3 did it too</summary><div class="callout callout-info"\1><span class="callout-icon">📖</span><p\2>\4</p></div></details>'),
  # ── G4 with "What to do" boxes (DATA.todo): the old instruction lines that now repeat it ──
  ('dol-intro', r'\s*<p>The first sentence is <strong>correct</strong>\. Tap the parts you notice are done right &mdash; capital letters, punctuation, quotation marks, anything that follows the rules\. Then use it as a model to fix the second sentence\.</p>', ''),
  ('read-first', r'\s*<div class="callout callout-info"[^>]*><span class="callout-icon">&#x23F8;&#xFE0F;</span><p><strong>Read these first\.</strong> Look them over before you open your book, then stop and answer each one when you reach that part\.</p></div>', ''),
  ('directions', r'<div class="callout callout-info"><span class="callout-icon">🎯</span><p><strong>Directions:</strong>[^<]*</p></div>', ''),
  # Vocabulary: the "Your turn!" line in fewer words
  ('vocab-your-turn', r'<strong>Your turn!</strong> Each word below has a sentence above it\. Read the sentence, look for word parts, and guess what the word means\. Then tap the card to check\.',
   r'<strong>Your turn!</strong> Read each sentence, guess what the word means, then tap the card to check.'),
  # DOL: the hint under the model repeats the What to do line
  # (G4 copy: the DOL hint stays. G4 has no "What to do" line, so the hint is the only instruction.)
]

def one_question(h):
    """Think-question lists (socratic 'Try these first', 'Think it through',
    'answer these in your head') keep their first question only."""
    n = 0
    def keep_first_li(m):
        nonlocal n
        lis = re.findall(r'<li>.*?</li>', m.group(2), re.S)
        if len(lis) <= 1: return m.group(0)
        n += 1
        return m.group(1) + '\n' + lis[0] + '\n' + m.group(3)
    h = re.sub(r'(<div class="callout callout-info"[^>]*><span class="callout-icon">[^<]*</span><p><strong>(?:Think it through\.|Say each word below\. Then answer these in your head:)</strong></p>\s*<(?:ol|ul)[^>]*>)(.*?)(</(?:ol|ul)></div>)',
               keep_first_li, h, flags=re.S)
    h = re.sub(r'answer these in your head:', 'answer this in your head:', h)
    def keep_first_q(m):
        nonlocal n
        qs = re.findall(r'<p class="socratic-q">.*?</p>', m.group(2), re.S)
        if len(qs) <= 1: return m.group(0)
        n += 1
        return m.group(1).replace('Try these first:', 'Try this first:') + '\n' + qs[0] + '\n' + m.group(3)
    h = re.sub(r'(<div class="socratic-box"><div class="socratic-label">[^<]*Try these first:</div>)(.*?)(</div>)', keep_first_q, h, flags=re.S)
    return h, n

# What to do lines that named the cut questions
TODO = [('Think about the three questions.', 'Think about the question.')]

for f in sys.argv[1:]:
    h = io.open(f, encoding='utf-8').read(); log = []
    for name, pat, rep in RULES:
        h, c = re.subn(pat, rep, h, flags=re.S)
        if c: log.append('%s x%d' % (name, c))
    h, c = one_question(h)
    if c: log.append('one-question x%d' % c)
    for a, b in TODO:
        c = h.count(a)
        if c: h = h.replace(a, b); log.append('todo x%d' % c)
    io.open(f, 'w', encoding='utf-8').write(h)
    print(f, ', '.join(log) or 'nothing to cut')
