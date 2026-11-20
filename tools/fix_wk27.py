#!/usr/bin/env python3
"""Week 27 (Prince Caspian Ch. 4-6) fixes, checked against the text (Planning docs/PrinceCaspian_CSL.pdf), Nov 19 2026.
- Epigraphs: 27.1 was Aslan's Ch. 15 line, misquoted; 27.2 "We have nothing if not belief" is not Lewis; 27.3 "Courage, dear heart"
  is from The Voyage of the Dawn Treader; 27.4 was an invented "adapted" opening. Now real lines from Ch. 4, 5, 6 and 6.
- 27.1: Cornelius tells Caspian that Miraz is a usurper and murdered his father in Ch. 5, not Ch. 4: Q3 rewritten to what Ch. 4
  does reveal (the old stories are true; Cornelius is half-Dwarf). The usurper worked example now quotes Lewis (Ch. 5).
  DOL model and spelling passage relabeled (written for the lesson, not quoted).
- 27.2: grammar "in the published text" used invented sentences (and had Caspian blowing the horn, which is Ch. 7): now two real
  Ch. 5 sentences.
- 27.3: copywork restored to Lewis's wording ("I watch the skies, Badger, ..."); DOL label; vocab clues relabeled; the assignment
  RWM passage was stitched from invented lines: now Lewis's three real visit openers from Ch. 6.
- 27.4: poem attribution; epigraph.
- Fluency: second paragraph was invented ("adapted"): now Lewis's own Faun passage from Ch. 6.
- Check-in: the intro and the reading/writing items put the Pevensies "making their way through ruins" during Ch. 4-6; in fact
  they sit and listen to Trumpkin's story. Q5 and the reading passage were invented "Source: Prince Caspian" lines: now real.
  Q1 no longer labels the wrong answer "(run-on)"; Q2 sentences match the book."""
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

def spot(gid, text, hits):
    out = []
    for w in text.split(' '):
        ok = 'true' if w.strip('.,;:') in hits else 'false'
        out.append('<span class="spotter-word" onclick="_oaoSpotAll(this,\'%s\')" data-correct="%s">%s</span>' % (gid, ok, w))
    return ' '.join(out)

patch('lesson-27-1-pc-ch4.html', [
 ('&ldquo;You come from the Lord Adam and the Lady Eve. And that is both honor enough to erect the head of the poorest beggar, and shame enough to bow the shoulders of the greatest emperor on earth.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; C. S. Lewis</div>',
  '&ldquo;Certainly it is true,&rdquo; said Cornelius. &ldquo;Their reign was the Golden Age in Narnia and the land has never forgotten them.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Doctor Cornelius, <em>Prince Caspian</em>, Ch. 4</div>'),
 ('<div class="dol-model-label">&#x2705; Correct Model &mdash; from Prince Caspian</div>', '<div class="dol-model-label">&#x2705; Correct Model &mdash; a sentence about Chapter 4</div>'),
 ('&ldquo;I wish &mdash; I wish &mdash; I wish I could have lived in the Old Days.&rdquo; &mdash; Prince Caspian</div>', '&ldquo;I wish &mdash; I wish &mdash; I wish I could have lived in the Old Days,&rdquo; said Caspian. &mdash; <em>Prince Caspian</em>, Ch. 4</div>'),
 ('<div class="activity-sub">Words from Chapter 4</div>', '<div class="activity-sub">Words for Chapters 4 and 5</div>'),
 ('&ldquo;Doctor Cornelius revealed that Miraz was a usurper &mdash; he had killed Caspian&rsquo;s father and stolen the throne.&rdquo;',
  '&ldquo;Everyone except your Majesty knows that Miraz is a usurper. When he first began to rule he did not even pretend to be the King: he called himself Lord Protector.&rdquo; (Doctor Cornelius, Chapter 5)'),
 ('<p>A passage from Chapter 4. Watch what happens to a base word when a suffix arrives.</p>', '<p>A sentence written about Chapter 4. Watch what happens to a base word when a suffix arrives.</p>'),
 ('<span class="q-num">3</span>Doctor Cornelius reveals that Miraz is a usurper &mdash; he killed Caspian&rsquo;s father and took the throne. How do you think Caspian feels when he hears this? Use a detail from the chapter to support your answer.',
  '<span class="q-num">3</span>On top of the tower, Doctor Cornelius tells Caspian that the old stories are true and that he himself is a half-Dwarf. How do you think Caspian feels when he hears this? Use a detail from the chapter to support your answer.'),
])
patch('lesson-27-2-pc-ch5.html', [
 ('&ldquo;We have nothing if not belief.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; C.S. Lewis</div>',
  '&ldquo;Take it, King Caspian: but do not use it except at your greatest need.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Doctor Cornelius, <em>Prince Caspian</em>, Ch. 5</div>'),
 ('<p>Chapter 5. Contrast and consequence, side by side.</p>', '<p>Two sentences from Chapter 5, exactly as Lewis wrote them.</p>'),
])
s = io.open('lesson-27-2-pc-ch5.html', encoding='utf-8').read()
i = s.index('<div class="spotter-sentence" id="g4w27b" style="line-height:2.6;">') ; i = s.index('>', i) + 1
j = s.index('<div class="spotter-result" id="g4w27b-result">', i)
s = s[:i] + spot('g4w27b', "Caspian's heart was sinking, but he tried to take it all in. He kept his seat, but he knew that his life hung by a thread during the wild career that followed.", {'but'}).replace("Caspian's", 'Caspian&rsquo;s') + s[j:]
io.open('lesson-27-2-pc-ch5.html', 'w', encoding='utf-8', newline='').write(s); print('ok spotter')

patch('lesson-27-3-pc-ch6.html', [
 ('&ldquo;Courage, dear heart.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; C. S. Lewis</div>',
  '&ldquo;There are twelve of us, Sire,&rdquo; he said with a dashing and graceful bow, &ldquo;and I place all the resources of my people unreservedly at your Majesty&rsquo;s disposal.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Reepicheep, <em>Prince Caspian</em>, Ch. 6</div>'),
 ('<div class="dol-model-label">&#x2705; Correct Model &mdash; from Prince Caspian, Ch. 6</div>', '<div class="dol-model-label">&#x2705; Correct Model &mdash; a sentence about Chapter 6</div>'),
 ('&ldquo;The time is ripe. I watch the skies, for it is mine to watch, as it is yours to remember.&rdquo;</div>', '&ldquo;The time is ripe,&rdquo; said Glenstorm. &ldquo;I watch the skies, Badger, for it is mine to watch, as it is yours to remember.&rdquo;</div>'),
 ('<p>Read each sentence from Chapter 6. Use the <strong>context clues</strong>', '<p>Read each clue about the story. Use the <strong>context clues</strong>'),
 ('<div class="task-label">Passage from Chapter 6</div>', '<div class="task-label">Three sentences from Chapter 6</div>'),
 ('&ldquo;Then they went a little further and met a Squirrel &hellip; And then they went on till they came to a part of the wood that was thicker &hellip; And there they met the Centaur and his sons.&rdquo;',
  '&ldquo;Their next visit was to the Seven Brothers of Shuddering Wood.&rdquo; &hellip; &ldquo;Their next visit was a pleasanter one.&rdquo; &hellip; &ldquo;The next place they were to visit was quite near at hand, but they had to go a long way round in order to avoid a region in which Men lived.&rdquo;'),
 ('Notice how Lewis transitions between groups &mdash; &ldquo;Then they went on and met&hellip;&rdquo; <strong>', 'Notice how Lewis opens each new visit &mdash; &ldquo;Their next visit&hellip;&rdquo; <strong>'),
])
patch('lesson-27-4-pc-discussion.html', [
 ('&ldquo;There once lived in the land of Narnia, in a great castle called Cair Paravel, a King and a Queen.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; C. S. Lewis (adapted)</div>',
  '&ldquo;When Caspian awoke next morning he could hardly believe that it had not all been a dream; but the grass was covered with little cloven hoof-marks.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; C. S. Lewis, <em>Prince Caspian</em>, Ch. 6</div>'),
 ('<div class="poem-attr">&mdash; For the Old Narnians</div>', '<div class="poem-attr">&mdash; An Optima original poem, for the Old Narnians</div>'),
])
patch('lesson-27-fluency.html', [
 ('<div class="quote-strip-text">&ldquo;The time is ripe. I watch the skies, for it is mine to watch, as it is yours to remember.&rdquo;</div>', '<div class="quote-strip-text">&ldquo;The time is ripe,&rdquo; said Glenstorm. &ldquo;I watch the skies, Badger, for it is mine to watch, as it is yours to remember.&rdquo;</div>'),
 ('The great Centaur Glenstorm stood tall under the stars, his sons beside him. &ldquo;The time is ripe,&rdquo; he said. &ldquo;I watch the skies, for it is mine to watch,',
  '&ldquo;The time is ripe,&rdquo; said Glenstorm. &ldquo;I watch the skies, Badger, for it is mine to watch,'),
 ('Later, when the night had grown deeper, they came to a place where the trees thinned and moonlight fell silver on the grass. And there Caspian saw what he had longed all his life to see &mdash; a Faun dance. The creatures moved lightly between the tree trunks, their little horns gleaming, their hooves barely touching the ground. It was like nothing he had ever imagined. It was Old Narnia, alive and real and right in front of him.',
  'The moon was bright; Caspian had been asleep longer than he thought. Nearer and nearer came the music, a tune wild and yet dreamy, and the noise of many light feet, till at last, out from the wood into the moonlight, came dancing shapes such as Caspian had been thinking of all his life. They were not much taller than dwarfs, but far slighter and more graceful. Their curly heads had little horns, the upper part of their bodies gleamed naked in the pale light, but their legs and feet were those of goats.<br><br>\n        &ldquo;Fauns!&rdquo; cried Caspian, jumping up, and in a moment they were all round him.'),
 ('This passage is adapted from Chapter 6 of <em>Prince Caspian</em>', 'This passage is from Chapter 6 of <em>Prince Caspian</em>'),
])
patch('week-27-checkin.html', [
 ("This week the story split into two — Caspian gathering allies in the forest, and the Pevensies finding their way through unfamiliar ruins. You've been tracking multiple storylines and noticing how they're moving toward each other.",
  "This week the Dwarf told the four children Caspian's story: a prince who learned the truth about Old Narnia, ran for his life, and found the creatures who had been hiding. You've been keeping track of who is on which side."),
 ('"Caspian wanted to reclaim his kingdom but he needed allies first so he could fight." (run-on)</li>', '"Caspian wanted to reclaim his kingdom but he needed allies first so he could fight."</li>'),
 ('1. "The Dwarfs were suspicious of Caspian. He earned their trust over time."<br>2. "The horn was powerful. Caspian was afraid to use it."',
  '1. "Trufflehunter trusted Caspian. Nikabrik did not."<br>2. "Caspian\'s life was in danger. Doctor Cornelius woke him in the night."'),
 ('"Caspian extracted the story from the old Dwarf piece by piece — pulling out each detail about the Old Narnians as carefully as one removes a splinter."<div class="excerpt-source">Source: Prince Caspian, Ch. 4–6</div>',
  '"And when there was no one left who could speak a word for you, then his flatterers (as he had instructed them) begged him to become King. And of course he did."<div class="excerpt-source">Doctor Cornelius, <em>Prince Caspian</em>, Ch. 5</div>'),
 ('What does "extracted" most likely mean?', 'The base <em>struct</em> means "build." What does "instructed" most likely mean here?'),
 ('<span class="opt-letter">A</span> Erased and forgotten</li>', '<span class="opt-letter">A</span> Built a house for them</li>'),
 ('<span class="opt-letter">B</span> Pulled out or drawn out carefully</li>', '<span class="opt-letter">B</span> Told them ahead of time what to do</li>'),
 ('<span class="opt-letter">C</span> Recorded in a history book</li>', '<span class="opt-letter">C</span> Paid them with gold</li>'),
 ('"While Caspian was gathering the Old Narnians in the forest, Peter and the others were making their way through ruins they barely recognized. Two stories were unfolding at once, each one moving toward the same collision."<div class="excerpt-source">Source: Prince Caspian, Ch. 4–6</div>',
  '"It would take too long to mention all the creatures whom Caspian met that day — Clodsley Shovel the Mole, the three Hardbiters (who were badgers like Trufflehunter), Camillo the Hare, and Hogglestock the Hedgehog."<div class="excerpt-source">C. S. Lewis, <em>Prince Caspian</em>, Ch. 6</div>'),
 ("How does Lewis keep you interested in both groups of characters in Ch. 4–6? What makes each group's situation feel urgent? Use at least one specific detail per group.",
  "Caspian meets many new characters in Ch. 4–6. How does Lewis help you keep track of who is on Caspian's side and who is against him? Use at least one specific detail from the book."),
 ('"While Caspian worked to build his army in the woods, the Pevensies were being pulled toward him through time and ruin. Neither knew about the other yet — but both were moving toward the same moment."',
  '"Their next visit was a pleasanter one." — C. S. Lewis, <em>Prince Caspian</em>, Ch. 6'),
 ('Notice how "while" and "neither…yet" hold two storylines together. Write your own two-sentence summary of what two different characters or groups are doing in Ch. 4–6. Use a transition word like "while," "meanwhile," or "at the same time."',
  'Lewis moves from one visit to the next with a short sentence that makes the move itself the subject. Write two sentences that carry a reader from one of Caspian\'s visits to the next. Start one of them the way Lewis does: "Their next visit was…"'),
 ("In 2–3 sentences, explain why it matters that Lewis shows us both storylines (Caspian's and the Pevensies'). What would be lost if we only followed one group?",
  "Chapters 4–6 are a story inside a story: the Dwarf is telling it to the four children on the island. In 2–3 sentences, explain why Lewis might tell Caspian's story this way. What does it help the children (and you) understand?"),
])
