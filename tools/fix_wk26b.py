#!/usr/bin/env python3
"""Week 26 practice labels: practice sentences about later chapters (Caspian, the Doctor, Nikabrik) were labeled as
Chapter 2/3 text; relabeled. 26.3 vocab cloze: two invented scenes swapped for ones that happen in Ch. 1."""
import io, sys
def patch(fn, pairs):
    s = io.open(fn, encoding='utf-8', newline='').read()
    for a, b in pairs:
        if s.count(a) < 1: sys.exit(fn + ': ' + a[:60])
        s = s.replace(a, b)
    io.open(fn, 'w', encoding='utf-8', newline='').write(s); print('ok', fn)
patch('lesson-26-2-pc-ch2.html', [
 ('Chapter 2. Lewis uses both conjunctions, and they are not interchangeable.', 'Practice sentences. Writers use both conjunctions, and they are not interchangeable.'),
 ('Chapter 2. Some long words are built from parts; some are just long.', 'A practice sentence. Some long words are built from parts; some are just long.')])
patch('lesson-26-4-pc-discussion.html', [
 ('A draft about Chapter 3. Some joints are right.', 'A practice draft. Some joints are right.'),
 ('A draft about Chapter 3. Some of these are spelled correctly.', 'A practice list. Some of these are spelled correctly.')])
patch('lesson-26-3-pc-ch3.html', [
 ('The soldiers dragged the Dwarf through a thick <input', 'The children pushed their way out of a thick <input'),
 ('style="width:120px;"> of bushes near the shore.', 'style="width:120px;"> of trees and bushes.'),
 ('They reached the <input class="fillin-input fillin-vocab" data-answer="junction"', 'They waited at the <input class="fillin-input fillin-vocab" data-answer="junction"'),
 ('style="width:120px;"> where the river met the sea.', 'style="width:120px;">, the station where two train lines met.')])
