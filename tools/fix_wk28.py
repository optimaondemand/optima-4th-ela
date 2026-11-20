#!/usr/bin/env python3
"""Week 28 (Prince Caspian Ch. 7-9) fixes, checked against the text (Planning docs/PrinceCaspian_CSL.pdf), Nov 19 2026.
- 28.1: the council decode sentence was invented: now Lewis's line. Spelling passage relabeled (written for the lesson).
  DOL fix-it had Nikabrik arguing against the Horn (in Ch. 7 he says Caspian will wait too long): now his real objection, to Cornelius.
- 28.2: DOL had Trumpkin rowing all night (Peter and Edmund row; the oars are too big for Lucy). Epigraph restored to Lewis's wording ("don't we," said Lucy, "if Aslan wants us?"). The grammar spotter called its
  sentences "the real sentence shape from Chapter 8"; they were invented and from Ch. 14: now two real Ch. 8 sentences.
- 28.3: copywork restored in full (it had two cuts). Pause & Think #1 mixed Lucy's night among the trees with seeing Aslan (that is next day, at the gorge).
- 28.4: DOL had Susan "silent on the path" (she voted aloud, "I'm dead tired"); the editing pass had Caspian fleeing "with Doctor
  Cornelius" (he went alone); Edmund spoke up before Peter's vote, not after.
- Fluency: the second half was invented ("You are braver than you know"): now Lewis's own Ch. 7 passage.
- Check-in: Peter's challenge to Miraz is Ch. 13, not 7-9 (Q2, reading passage, model sentence all used it, and all three
  "Source: Prince Caspian" passages were invented). Now real Ch. 7 and Ch. 9 lines; Q5 uses "spectacles" (Ch. 7). Q5 key stays B."""
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
        ok = 'true' if w in hits else 'false'
        out.append('<span class="spotter-word" onclick="_oaoSpotAll(this,\'%s\')" data-correct="%s">%s</span>' % (gid, ok, w))
    return ' '.join(out)
def respot(fn, gid, text, hits):
    s = io.open(fn, encoding='utf-8', newline='').read()
    i = s.index('<div class="spotter-sentence" id="%s"' % gid); i = s.index('>', i) + 1
    j = s.index('<div class="spotter-result" id="%s-result">' % gid, i)
    s = s[:i] + spot(gid, text, hits) + s[j:]
    io.open(fn, 'w', encoding='utf-8', newline='').write(s); print('ok spotter', gid)

patch('lesson-28-1-pc-ch7.html', [
 ('&ldquo;And so a great <strong>council</strong> was held, and the beasts and creatures of Old Narnia debated what they should do.&rdquo;',
  '&ldquo;But Caspian and the Centaurs and the Dwarfs overruled all these suggestions and insisted on holding a real <strong>council</strong> of war at once.&rdquo;'),
 ('<p>A passage from Chapter 7. One vowel in each long word has gone soft and lazy.</p>', '<p>A sentence written about Chapter 7. One vowel in each long word has gone soft and lazy.</p>'),
 ('because nikabrik distrusted the humans he argued against calling them although caspian had already blown the horn',
  'because nikabrik distrusted doctor cornelius he reached for his sword although caspian called the doctor his greatest friend'),
 ('<strong>B</strong>ecause <strong>N</strong>ikabrik distrusted the humans<strong>,</strong> he argued against calling them although <strong>C</strong>aspian had already blown the <strong>H</strong>orn<strong>.</strong>',
  '<strong>B</strong>ecause <strong>N</strong>ikabrik distrusted <strong>D</strong>octor <strong>C</strong>ornelius<strong>,</strong> he reached for his sword although <strong>C</strong>aspian called the <strong>D</strong>octor his greatest friend<strong>.</strong>'),
])
patch('lesson-28-2-pc-ch8.html', [
 ('&ldquo;But we want to be here, don&rsquo;t we, if Aslan wants us?&rdquo;', '&ldquo;But we want to be here, don&rsquo;t we,&rdquo; said Lucy, &ldquo;if Aslan wants us?&rdquo;'),
 ('since trumpkin had rowed all night the children rested on the shore even though the battle was waiting',
  'because the oars were too big for her lucy could not take a turn at rowing although she offered'),
 ('<strong>S</strong>ince <strong>T</strong>rumpkin had rowed all night<strong>,</strong> the children rested on the shore even though the battle was waiting<strong>.</strong>',
  '<strong>B</strong>ecause the oars were too big for her<strong>,</strong> <strong>L</strong>ucy could not take a turn at rowing although she offered<strong>.</strong>'),
 ('capital <strong>T</strong> on the proper name, a comma after the opening dependent clause that begins with <strong>Since</strong>, no comma before the <strong>even though</strong> clause at the end',
  'capital <strong>L</strong> on the proper name, a comma after the opening dependent clause that begins with <strong>Because</strong>, no comma before the <strong>although</strong> clause at the end'),
 ('<p>This is the real sentence shape from Chapter 8, not a practice sentence.</p>', '<p>Two sentences from Chapter 8, exactly as Lewis wrote them.</p>'),
])
respot('lesson-28-2-pc-ch8.html', 'g4w28spot',
       '&ldquo;If we start at once, we can be at the head of Glasswater before dark.&rdquo; &ldquo;The oars are too big for you,&rdquo; said Peter shortly, not because he was cross but because he had no strength to spare for talking.',
       {'&ldquo;If', 'because'})
patch('lesson-28-3-pc-ch9.html', [
 ('&ldquo;When we first discovered Narnia&hellip; it was Lucy who discovered it first and none of us would believe her. I was the worst of the lot&hellip; Yet she was right after all.',
  '&ldquo;When we first discovered Narnia a year ago &mdash; or a thousand years ago, whichever it is &mdash; it was Lucy who discovered it first and none of us would believe her. I was the worst of the lot, I know. Yet she was right after all.'),
 ('Lucy walks into the moonlit clearing and sees the trees begin to dance. She thinks she sees Aslan. <strong>',
  'In the night, Lucy walks among the trees and feels they are almost awake. The next day, at the gorge, she sees Aslan, and no one else does. <strong>'),
])
patch('lesson-28-4-pc-discussion.html', [
 ('because susan doubted what lucy had seen she stayed silent on the path so the group lost hours of daylight',
  'because susan was dead tired she voted to go down so the group turned downstream'),
 ('<strong>B</strong>ecause <strong>S</strong>usan doubted what <strong>L</strong>ucy had seen<strong>,</strong> she stayed silent on the path<strong>,</strong> so the group lost hours of daylight<strong>.</strong>',
  '<strong>B</strong>ecause <strong>S</strong>usan was dead tired<strong>,</strong> she voted to go down<strong>,</strong> so the group turned downstream<strong>.</strong>'),
 ('data-correct="false">Caspian fled into the woods with Doctor Cornelius.</span>', 'data-correct="false">Caspian fled into the woods alone.</span>'),
 ('What did Edmund show by standing up for Lucy, even when the vote had already been taken?', 'What did Edmund show by standing up for Lucy, even though the vote went against her?'),
])
patch('lesson-28-fluency.html', [
 ('&ldquo;Then in the name of Aslan,&rdquo; said Caspian, &ldquo;we will wind Queen Susan&rsquo;s Horn.&rdquo; But someone must be sent to meet the help when it arrives at Lantern Waste &mdash; or at Cair Paravel. That is a dangerous journey. Who will volunteer?',
  '&ldquo;I won&rsquo;t go,&rdquo; said Nikabrik. &ldquo;With all these Humans and beasts about, there must be a Dwarf here to see that the Dwarfs are fairly treated.&rdquo;'),
 ('&ldquo;I will,&rdquo; said Trumpkin.', '&ldquo;Thimbles and thunderstorms!&rdquo; cried Trumpkin in a rage. &ldquo;Is that how you speak to the King? Send me, Sire, I&rsquo;ll go.&rdquo;<br><br>\n        &ldquo;But I thought you didn&rsquo;t believe in the Horn, Trumpkin,&rdquo; said Caspian.'),
 ('Trumpkin bowed low, and the council was silent for a moment. Then Caspian said quietly, &ldquo;Thank you, Trumpkin. You are braver than you know.&rdquo;',
  '&ldquo;I will never forget this, Trumpkin,&rdquo; said Caspian.'),
 ('adapted from Chapter 7', 'from Chapter 7'),
])
patch('week-28-checkin.html', [
 ("This week the action picked up — Peter stepped forward as a leader, Lucy struggled to be believed, and Caspian faced enemies on every side.",
  "This week the Old Narnians held their council and Caspian blew the Horn, the Dwarf finished his story, the children set out to find Caspian, and Lucy saw Aslan when no one else did."),
 ('1. "Peter challenged Miraz. He wanted to give Caspian\'s army time to prepare."', '1. "Trumpkin did not believe in the Horn. He went to Cair Paravel anyway."'),
 ('"Peter inspected the terrain carefully before committing the army to any plan — studying every slope, every tree line, and every possible point of attack."<div class="excerpt-source">Source: Prince Caspian, Ch. 7–9</div>',
  '"Then after stooping down and peering carefully through his spectacles, he broke into a laugh."<div class="excerpt-source">Doctor Cornelius meets Reepicheep, <em>Prince Caspian</em>, Ch. 7</div>'),
 ('What does "inspected" most likely mean?', 'The base <em>spect</em> means "look." What are "spectacles"?'),
 ('<span class="opt-letter">A</span> Glanced at quickly without much thought</li>', '<span class="opt-letter">A</span> A loud, sudden noise</li>'),
 ('<span class="opt-letter">B</span> Looked over carefully and thoroughly</li>', '<span class="opt-letter">B</span> Glasses you look through</li>'),
 ('<span class="opt-letter">C</span> Drew a detailed map of</li>', '<span class="opt-letter">C</span> A set of writing tools</li>'),
 ('"Peter knew the attack was a risk. He also knew that doing nothing was a risk too. A leader does not get to choose between safe and dangerous — only between different kinds of danger."<div class="excerpt-source">Source: Prince Caspian, Ch. 7–9</div>',
  '"Down," said Peter after a long pause. "I know Lucy may be right after all, but I can\'t help it. We must do one or the other." So they set off to their right along the edge, downstream. And Lucy came last of the party, crying bitterly.<div class="excerpt-source">C. S. Lewis, <em>Prince Caspian</em>, Ch. 9</div>'),
 ('"Peter challenged Miraz not because he believed he would win, but because he believed the challenge was necessary. That is the difference between courage and confidence — one knows it might fail, and chooses anyway."',
  '"No more I do, your Majesty. But what\'s that got to do with it? I might as well die on a wild goose chase as die here. You are my King." — Trumpkin, <em>Prince Caspian</em>, Ch. 7'),
 ('Notice how this model gives a reason and then explains what that reason reveals.', 'Trumpkin does not believe in the Horn, yet he gives his reason for going in a few short, plain sentences.'),
])
