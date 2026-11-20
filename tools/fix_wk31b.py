#!/usr/bin/env python3
"""31.1 said "three great novels" (the year has five books: four novels and a biography); 31.3's Big Question was left over
from Prince Caspian Ch. 15 and did not match a comparison-paragraph lesson."""
import io, sys
def patch(fn, a, b):
    s = io.open(fn, encoding='utf-8', newline='').read()
    if s.count(a) != 1: sys.exit('%s: %d %r' % (fn, s.count(a), a[:60]))
    io.open(fn, 'w', encoding='utf-8', newline='').write(s.replace(a, b)); print('ok', fn)
patch('lesson-31-1-synthesis-compare.html', 'You have read three great novels this year.', 'You have read five books this year: four novels and one biography.')
patch('lesson-31-3-synthesis-compare.html', 'The war is won, Caspian is crowned, and Reepicheep gets his tail back. But then comes the hardest part. Today ask yourself: <strong>What do you carry with you when you have to say goodbye to a place you love?</strong>',
      'You have a theme and two characters who show it. Today you build the bridge between them. Today ask yourself: <strong>How do I prove that two characters from two different books share the same big idea?</strong>')
