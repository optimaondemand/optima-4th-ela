#!/usr/bin/env python3
"""Week 26 (Prince Caspian Ch. 1-3) fixes, checked against the text (Planning docs/PrinceCaspian_CSL.pdf), Nov 19 2026.
- 26.1 epigraph was from The Silver Chair: now Susan's orchard line (Ch. 1).
- 26.2 epigraph was a misquote from The Lion, the Witch and the Wardrobe: now Peter's line in the treasure chamber (Ch. 2).
- 26.4 epigraph misquoted the first line ("There once were" -> "Once there were").
- Peter's Rhindon line punctuated as Lewis wrote it (26.2 pause, fluency).
- 26.1 morphology fill-in blanked broken chunks (vi, tur, por, nati); now the prefix.
- 26.1 'junction' sentence was invented: now the book's line. 26.1 spelling passage relabeled (it is about Ch. 1, not from it).
- 26.2 DOL fix-it: Susan does NOT find her horn (Ch. 2: "Where's the horn?"); the list is now bow, quiver, arrows.
- 26.3 / 26.4 DOL models were stitched or invented but labeled "from Prince Caspian": relabeled.
- Check-in: Q1 no longer puts Caspian at the ruins (he is not in Ch. 1-3); Q5 and the reading passage are real Lewis lines."""
import io, sys
def patch(fn, pairs):
    s = io.open(fn, encoding='utf-8', newline='').read()
    for a, b, *n in pairs:
        n = n[0] if n else 1
        if '\r\n' in s and a not in s:
            a, b = a.replace('\n', '\r\n'), b.replace('\r\n', '\n').replace('\n', '\r\n')
        c = s.count(a)
        if c != n: sys.exit('%s: expected %d, found %d: %r' % (fn, n, c, a[:90]))
        s = s.replace(a, b)
    io.open(fn, 'w', encoding='utf-8', newline='').write(s); print('ok', fn)

patch('lesson-26-1-pc-ch1.html', [
 ('&ldquo;You would not have called to me unless I had been calling to you.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; C. S. Lewis, <em>Prince Caspian</em></div>',
  '&ldquo;This must have been an orchard &mdash; long, long ago, before the place went wild and the wood grew up.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Susan, <em>Prince Caspian</em>, Ch. 1</div>'),
 ('pre<input class="fillin-input" id="fill1" data-answer="vi" maxlength="8" placeholder="______">ew', '<input class="fillin-input" id="fill1" data-answer="pre" maxlength="8" placeholder="______">view'),
 ('re<input class="fillin-input" id="fill2" data-answer="tur" maxlength="8" placeholder="______">n', '<input class="fillin-input" id="fill2" data-answer="re" maxlength="8" placeholder="______">turn'),
 ('trans<input class="fillin-input" id="fill3" data-answer="por" maxlength="8" placeholder="______">t', '<input class="fillin-input" id="fill3" data-answer="trans" maxlength="8" placeholder="______">port'),
 ('inter<input class="fillin-input" id="fill4" data-answer="nati" maxlength="8" placeholder="______">onal', '<input class="fillin-input" id="fill4" data-answer="inter" maxlength="8" placeholder="______">national'),
 ('&ldquo;They were standing on a platform at a junction&hellip;&rdquo;', '&ldquo;&hellip;as far as this station, which was a junction&hellip;&rdquo;'),
 ('&ldquo;They found themselves standing in a woody place &mdash;', '&ldquo;The four children, holding hands and panting, found themselves standing in a woody place &mdash;'),
 ('<p>A passage from Prince Caspian, Chapter 1. Fantasy writers build long words on purpose.</p>', '<p>A sentence about Prince Caspian, Chapter 1. Fantasy writers build long words on purpose.</p>'),
])
patch('lesson-26-2-pc-ch2.html', [
 ('&ldquo;Once a king or queen of Narnia, always a king or queen of Narnia.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; C.S. Lewis, <em>The Lion, the Witch and the Wardrobe</em></div>',
  '&ldquo;It is my sword Rhindon,&rdquo; he said; &ldquo;with it I killed the Wolf.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Peter, <em>Prince Caspian</em>, Ch. 2</div>'),
 ('Peter says &ldquo;It is my sword Rhindon. With it I killed the Wolf.&rdquo;', 'Peter says, &ldquo;It is my sword Rhindon,&rdquo; and, &ldquo;with it I killed the Wolf.&rdquo;'),
 ('susan found her presents the bow the quiver of arrows and the little ivory horn', 'susan found her presents the bow the ivory quiver and the feathered arrows'),
 ('the bow<strong>,</strong> the quiver of arrows<strong>,</strong> and the little ivory horn<strong>.</strong>', 'the bow<strong>,</strong> the ivory quiver<strong>,</strong> and the feathered arrows<strong>.</strong>'),
])
patch('lesson-26-3-pc-ch3.html', [
 ('Correct Model &mdash; from Prince Caspian, Ch. 3</div>', 'Correct Model &mdash; about Prince Caspian, Ch. 3</div>'),
])
patch('lesson-26-4-pc-discussion.html', [
 ('&ldquo;There once were four children whose names were Peter, Susan, Edmund, and Lucy.&rdquo;', '&ldquo;Once there were four children whose names were Peter, Susan, Edmund, and Lucy.&rdquo;'),
 ('Correct Model &mdash; from Prince Caspian</div>', 'Correct Model &mdash; about Prince Caspian</div>'),
])
patch('lesson-26-fluency.html', [
 ('&ldquo;It is my sword Rhindon. With it I killed the Wolf.&rdquo;</div>', '&ldquo;It is my sword Rhindon,&rdquo; he said; &ldquo;with it I killed the Wolf.&rdquo;</div>'),
 ('&ldquo;It is my sword Rhindon,&rdquo; he said. &ldquo;With it I killed the Wolf.&rdquo; There was', '&ldquo;It is my sword Rhindon,&rdquo; he said; &ldquo;with it I killed the Wolf.&rdquo; There was'),
])
CK = 'week-26-checkin.html'
patch(CK, [
 ('"Lucy saw the ruins and or Caspian could not explain them."', '"Lucy saw the ruins and or Peter could not explain them."'),
 ('"Lucy saw the ruins, and Caspian could not believe what had become of his kingdom."', '"Lucy saw the ruins, and Peter could not believe how old they looked."'),
 ('"Lucy saw the ruins Caspian and could not believe what had become of his kingdom."', '"Lucy saw the ruins Peter and could not believe how old they looked."'),
 ('<div class="excerpt">"The Narnia the children had known was transformed — where castles had stood, only ruins remained; where the land had been full of talking animals and wonder, silence had fallen."<div class="excerpt-source">Source: Prince Caspian, Ch. 1–3</div></div>',
  '<div class="excerpt">“Why, there are dozens of them,” said Susan… “This must have been an orchard — long, long ago, before the place went wild and the wood grew up.”<br>“Then this was once an inhabited island,” said Peter.<div class="excerpt-source">— C. S. Lewis, <em>Prince Caspian</em>, Ch. 1</div></div>'),
 ('What does "transformed" most likely mean?', 'What does "inhabited" most likely mean?'),
 ('<span class="opt-letter">A</span> Slowly improved over many years', '<span class="opt-letter">A</span> Covered with thick woods'),
 ('<span class="opt-letter">B</span> Completely changed in form or appearance', '<span class="opt-letter">B</span> Lived in by people'),
 ('<span class="opt-letter">C</span> Carefully preserved exactly as it had been', '<span class="opt-letter">C</span> Far out at sea'),
 ('"The trees were different. Everything was different — older, wilder, and stranger. They had come back to Narnia, but Narnia had moved on without them, as a place does when centuries pass and no one returns to care for it."<div class="excerpt-source">Source: Prince Caspian, Ch. 1–3</div>',
  '“For now all knew that it was indeed the ancient treasure chamber of Cair Paravel where they had once reigned as Kings and Queens of Narnia. There was a kind of path up the middle (as it might be in a greenhouse), and along each side at intervals stood rich suits of armor, like knights guarding the treasures.”<div class="excerpt-source">— C. S. Lewis, <em>Prince Caspian</em>, Ch. 2</div>'),
])
