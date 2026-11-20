#!/usr/bin/env python3
"""Week 30 (Prince Caspian Ch. 13-15) fixes, checked against the text (Planning docs/PrinceCaspian_CSL.pdf), Nov 19 2026.
- 30.1: copywork intro said "Aslan speaks to Lucy" (it is Edmund and Peter); summary: Reepicheep is turned down because "some
  humans are afraid of mice" and it would not be fair to Miraz, not for being small; spelling passage relabeled.
- 30.2: DOL answer had a comma before "and" in a compound predicate, and shortened Trumpkin's shout; morphology box showed last
  week's bases (rupt/duct/form) under a press/tain/lev title; grammar lines were called Lewis's Ch. 14 dialogue (invented); Peter's
  "Give my love to - to everyone" quoted as written.
- 30.3: DOL model was an invented Aslan line ("You have great hearts" is to the Mice, as part of a longer speech): now his real
  "Welcome, Prince"; DOL answer was 29.3's (Nikabrik) pasted in: now Caspian's real words; copywork notes were 29.3's (about
  Peter): now about Aslan's line; Susan practice line now her real Ch. 11 words.
- 30.4: DOL was 29.4's pasted in (with an invented Trumpkin quote): now real Ch. 13 lines; the "roots from this unit" box listed
  roots never taught (reg, domin, voc): now the unit's real bases; dictate and marshal defined as in 30.1; epigraph tag;
  grammar lines relabeled practice.
- Check-in: Q2 and Q5, the reading passage and the model sentence were invented (one had the Stone Table cracking, which is The
  Lion, the Witch and the Wardrobe). Now real Ch. 13-15 lines. Q5 key stays B."""
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
def remodel(fn, spans):
    s = io.open(fn, encoding='utf-8', newline='').read()
    i = s.index('<div class="dol-sentence-wrap" id="dolModel">'); i = s.index('>', i) + 1
    j = s.index('</div>', i)
    out = '\n'
    for t, why in spans:
        out += ('          <span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>\n' % (why, t)) if why else '          <span>%s</span>\n' % t
    s = s[:i] + out + '        ' + s[j:]
    io.open(fn, 'w', encoding='utf-8', newline='').write(s); print('ok model', fn)
def fixit(fn, raw_old, raw_new, hint_new, corrected_new, why_new):
    """Replace the DOL fix-it sentence, its hint, its corrected answer and its explanation."""
    s = io.open(fn, encoding='utf-8', newline='').read()
    assert s.count(raw_old) == 1, (fn, raw_old); s = s.replace(raw_old, raw_new)
    i = s.index('<div class="dol-hint">', s.index(raw_new)); j = s.index('</div>', i)
    s = s[:i] + '<div class="dol-hint">' + hint_new + s[j:]
    i = s.index('<strong>Corrected:</strong>', i); j = s.index('</p>', i)
    s = s[:i] + '<strong>Corrected:</strong> ' + corrected_new + s[j:]
    i = s.index('<p style="font-size:13px;color:#7A88A8;font-style:italic;">', i); i = s.index('>', i) + 1; j = s.index('</p>', i)
    s = s[:i] + why_new + s[j:]
    io.open(fn, 'w', encoding='utf-8', newline='').write(s); print('ok fixit', fn)

patch('lesson-30-1-pc-ch13.html', [
 ('<p>Aslan speaks to Lucy with authority and tenderness at once. Copy this passage carefully', '<p>Edmund asks a nervous question, and Peter answers it with a joke. Copy this passage carefully'),
 ('<p>A passage from Chapter 13. Every pattern from this year is somewhere in it.</p>', '<p>A sentence written for this lesson. Every pattern from this year is somewhere in it.</p>'),
 ('Reepicheep volunteers but is told he is too small.', 'Reepicheep asks to be a marshal, and Peter gently says no: some humans are afraid of mice, and it would not be fair to Miraz.'),
])
patch('lesson-30-2-pc-ch14.html', [
 ('Find: capital T on &ldquo;trumpkin&rdquo; (proper noun), comma after &ldquo;delight&rdquo; (separates the clauses), quotation marks around Trumpkin&rsquo;s shout, capital letters inside the quote, exclamation marks to show strong feeling.',
  'Find: capital T on &ldquo;trumpkin&rdquo; (proper noun), a comma after &ldquo;shouted&rdquo; before the quote, quotation marks around Trumpkin&rsquo;s shout, capital letters inside the quote, exclamation marks to show strong feeling.'),
 ('<strong>T</strong>rumpkin danced with delight, and shouted, &#x201C;The High King! Up, Old Narnia!&#x201D;', '<strong>T</strong>rumpkin danced with delight and shouted, &#x201C;The High King! Up, Old Narnia!&#x201D;'),
 ('Comma after &ldquo;delight&rdquo; to separate the clauses. Opening', 'No comma after &ldquo;delight&rdquo;: &ldquo;danced&rdquo; and &ldquo;shouted&rdquo; share one subject, so there is only one clause. A comma after &ldquo;shouted&rdquo; introduces the quote. Opening'),
 (' Compare with the model: both sentences use commas to separate the main clause from something that follows.', ' (Lewis has Trumpkin shout &ldquo;The High King! The High King! Up, Old Narnia!&rdquo;)'),
 ('<p><strong>rupt</strong> = break &nbsp;|&nbsp; <strong>duct / duc</strong> = lead &nbsp;|&nbsp; <strong>form</strong> = shape</p>', '<p><strong>press</strong> = push &nbsp;|&nbsp; <strong>tain</strong> = hold &nbsp;|&nbsp; <strong>lev</strong> = lift</p>'),
 ('Examples: <em>erupt</em> (break out), <em>conduct</em> (lead together), <em>reform</em> (shape again)', 'Examples: <em>impress</em> (press into), <em>maintain</em> (hold steady), <em>levitate</em> (lift into the air)'),
 ('<p>Chapter 14. Lewis punctuates dialogue in more than one shape.</p>', '<p>Practice lines in the style of the book. Some are punctuated correctly.</p>'),
 ('&ldquo;Give my love to everyone at home, Ed, if he gets me.&rdquo;', '&ldquo;Give my love to &mdash; to everyone at home, Ed, if he gets me.&rdquo;'),
])
remodel('lesson-30-3-pc-ch15.html', [
 ('&ldquo;', 'Opening quotation mark begins Aslan&rsquo;s exact words.'),
 ('Welcome', 'The first word of a quotation is capitalized.'),
 (',', 'A comma separates the greeting from the name of the person spoken to.'),
 (' ', None),
 ('Prince', 'Here Prince is used as a name for Caspian, so it is capitalized.'),
 (',', 'This comma ends the speech and joins it to the tag. It goes inside the closing quotation mark.'),
 ('&rdquo;', 'Closing quotation mark ends Aslan&rsquo;s words.'),
 (' said ', None),
 ('Aslan', '&quot;Aslan&quot; is a proper noun &mdash; always capitalized.'),
 ('.', 'A period ends the sentence.'),
])
patch('lesson-30-3-pc-ch15.html', [
 ('Proper Nouns, Quotation Marks, and Commas</div>', 'Proper Nouns, Quotation Marks, and Commas (Lewis&rsquo;s own words, Chapter 15)</div>', 1),
])
fixit('lesson-30-3-pc-ch15.html', 'caspian knelt and kissed the lions paw and said i dont think i am sufficient sir',
      'caspian kissed the lions paw and said i dont think i do sir',
      'Find the errors: <em>caspian</em> &rarr; Caspian (proper noun); <em>lions</em> &rarr; Lion&rsquo;s (possessive; Lewis capitalizes Lion when it names Aslan); missing comma after &ldquo;said&rdquo;; missing quotation marks; <em>i</em> &rarr; I; <em>dont</em> &rarr; don&rsquo;t; <em>sir</em> &rarr; Sir (a title used as a name); missing period inside the closing quotation mark.',
      '<strong>C</strong>aspian kissed the <strong>L</strong>ion&rsquo;s paw and said<strong>,</strong> &ldquo;<strong>I</strong> <strong>don&rsquo;t</strong> think <strong>I</strong> do, <strong>S</strong>ir<strong>.</strong>&rdquo;',
      'Caspian&rsquo;s real answer in Chapter 15 is &ldquo;I &mdash; I don&rsquo;t think I do, Sir.&rdquo; Capitals on Caspian, Lion&rsquo;s, I and Sir; an apostrophe in Lion&rsquo;s (possession) and don&rsquo;t (contraction); a comma after &ldquo;said&rdquo; before the quote; the period goes inside the closing quotation mark.')
patch('lesson-30-3-pc-ch15.html', [
 ('<p>Read Peter&rsquo;s words to Caspian below. Notice how gracious and generous he sounds.', '<p>Read Aslan&rsquo;s words to Caspian below. Notice how he answers Caspian&rsquo;s shame.'),
 ('Peter uses a contrast &mdash; &ldquo;not to take your place, but to put you into it.&rdquo; This is called an <em>antithesis</em>: two opposite ideas set side by side to make a point. It makes Peter&rsquo;s generosity and humility stand out clearly.',
  'Aslan uses a contrast &mdash; &ldquo;honour enough&rdquo; and &ldquo;shame enough,&rdquo; the poorest beggar and the greatest emperor. This is called an <em>antithesis</em>: two opposite ideas set side by side to make a point. Every person is both, so no one is too low to stand tall and no one too high to bow.'),
 ('As you copy, ask: <em>Why does Peter say this to Caspian? What does it tell you about Peter&rsquo;s character? What would it feel like to hear these words if you were Caspian?</em>',
  'As you copy, ask: <em>Caspian has just learned his people came from pirates. Why does Aslan say this to him now? What would it feel like to hear these words if you were Caspian?</em>'),
 ('<em>Susan said I dont believe you Lucy and I never will</em>', '<em>Susan said I see him now Lucy Im sorry</em>'),
])
remodel('lesson-30-4-pc-discussion.html', [
 ('Doctor Cornelius', 'A title and a name, both capitalized.'),
 (' dipped his pen and waited', None),
 ('.', 'A period ends the first sentence.'),
 (' ', None),
 ('Peter', '&quot;Peter&quot; is a proper noun &mdash; always capitalized.'),
 (' dictated as follows', None),
 (':', 'A colon tells the reader that what follows (the letter) is what Peter dictated.'),
])
patch('lesson-30-4-pc-discussion.html', [
 ('Capitalization, Commas &amp; Dialogue Punctuation</div>', 'Capitalization, Commas &amp; Dialogue Punctuation (Lewis&rsquo;s own words, Chapter 13)</div>'),
])
fixit('lesson-30-4-pc-discussion.html', 'caspian looked at nikabrik sadly and said he had gone sour inside from long suffering and hateing',
      'sire said reepicheep my life is ever at your command but my honour is my own',
      'Find: quotation marks around each part Reepicheep says, capitals on <em>sire</em>, <em>reepicheep</em> and <em>my</em>, commas around &ldquo;said Reepicheep,&rdquo; a comma before &ldquo;but,&rdquo; and a period inside the last quotation mark.',
      '&ldquo;<strong>S</strong>ire<strong>,</strong>&rdquo; said <strong>R</strong>eepicheep<strong>.</strong> &ldquo;<strong>M</strong>y life is ever at your command<strong>,</strong> but my honour is my own<strong>.</strong>&rdquo;',
      'Reepicheep&rsquo;s real words in Chapter 13 (Lewis spells honour the British way). Each part of his speech gets its own quotation marks; the comma after &ldquo;Sire&rdquo; goes inside the quotation mark; &ldquo;said Reepicheep&rdquo; ends with a period because the next part starts a new sentence; a comma comes before &ldquo;but&rdquo;; the final period goes inside the closing quotation mark.')
patch('lesson-30-4-pc-discussion.html', [
 ('<p><strong>rupt</strong> = break &nbsp;|&nbsp; <strong>duct</strong> = lead &nbsp;|&nbsp; <strong>form</strong> = shape<br><strong>reg / rect</strong> = rule, right &nbsp;|&nbsp; <strong>domin</strong> = master &nbsp;|&nbsp; <strong>voc / vok</strong> = voice, call</p>',
  '<p><strong>port</strong> = carry &nbsp;|&nbsp; <strong>tract</strong> = pull &nbsp;|&nbsp; <strong>struct</strong> = build &nbsp;|&nbsp; <strong>spect</strong> = look &nbsp;|&nbsp; <strong>ject</strong> = throw &nbsp;|&nbsp; <strong>script / scribe</strong> = write<br><strong>rupt</strong> = break &nbsp;|&nbsp; <strong>duct / duce</strong> = lead &nbsp;|&nbsp; <strong>form</strong> = shape &nbsp;|&nbsp; <strong>press</strong> = push &nbsp;|&nbsp; <strong>tain</strong> = hold &nbsp;|&nbsp; <strong>lev</strong> = lift</p>'),
 ('Connections to the novel: <em>coronation</em> (rule), <em>proclamation</em> (voice/call), <em>dominion</em> (master), <em>corrupt</em> (broken inside), <em>sovereign</em> (one who rules above all)',
  'Words from the book: <em>spectacles</em> and <em>spectators</em> (look), <em>instructed</em> (build), <em>interrupted</em> (break), <em>forms</em> (shape), <em>inspect</em> (look)'),
 ('<strong>Dictate</strong> &mdash; to give orders that must be obeyed<br><strong>Marshal</strong> &mdash; to arrange or lead troops into order<br>',
  '<strong>Dictate</strong> &mdash; to say words aloud for someone else to write down<br><strong>Marshal</strong> &mdash; an official who oversees a contest and keeps order<br>'),
 ('<p>A draft about Chapter 15. Some dialogue is punctuated correctly.</p>', '<p>A practice draft in the style of the book. Some dialogue is punctuated correctly.</p>'),
 ('<div class="quote-strip-text">&ldquo;You come of the Lord Adam and the Lady Eve. And that is both', '<div class="quote-strip-text">&ldquo;You come of the Lord Adam and the Lady Eve,&rdquo; said Aslan. &ldquo;And that is both'),
])
patch('week-30-checkin.html', [
 ('1. Peter said I did not expect it to end this way<br>2. That is why you must trust said Aslan and then I will show you the way',
  '1. Well I think I can said Peter<br>2. Welcome Prince said Aslan Do you feel yourself sufficient to take up the Kingship of Narnia'),
 ('"When Aslan walked through Narnia again, the land was restored — not to what it had been, but to what it was meant to become. Old Narnians lifted their heads; the stone table cracked; and the world breathed again."<div class="excerpt-source">Source: Prince Caspian, Ch. 13–15</div>',
  '"The spectators were holding their breath."<div class="excerpt-source">Peter and Miraz fight, <em>Prince Caspian</em>, Ch. 14</div>'),
 ('What does "restored" most likely mean?', 'The base <em>spect</em> means "look." Who are the "spectators"?'),
 ('<span class="opt-letter">A</span> Gradually changed into something completely different</li>', '<span class="opt-letter">A</span> The people doing the fighting</li>'),
 ('<span class="opt-letter">B</span> Brought back to a former or improved condition</li>', '<span class="opt-letter">B</span> The people watching</li>'),
 ('<span class="opt-letter">C</span> Celebrated with great public ceremony</li>', '<span class="opt-letter">C</span> The people making the rules</li>'),
 ('"The end of a story is not just where the action stops — it is where the meaning lands. In these final chapters, Caspian is crowned, the Telmarines are offered a choice, and the Pevensies must leave Narnia again. Each ending answers a question the story has been asking all along."<div class="excerpt-source">Source: Prince Caspian, Ch. 13–15</div>',
  '"…the grey, gravelly surface of a platform in a country station, and a seat with luggage round it, where they were all sitting as if they had never moved from it — a little flat and dreary for a moment after all they had been through, but also, unexpectedly, nice in its own way, what with the familiar railway smell and the English sky and the summer term before them."<div class="excerpt-source">C. S. Lewis, <em>Prince Caspian</em>, Ch. 15</div>'),
 ('"Prince Caspian is not a story about winning a battle — it is a story about what it costs to believe in something when no one else does. In the end, Caspian sits on a throne he nearly lost, and the Pevensies walk away from a world they love. What endures is not the victory, but the trust that made it possible."',
  '"Well!" said Peter. "We have had a time." "Bother!" said Edmund. "I\'ve left my new torch in Narnia." — the last lines of <em>Prince Caspian</em>'),
 ('Notice how this conclusion restates the theme and ends with a meaningful reflection — not just a summary.', 'Lewis ends the whole book with two short lines of talk, not a speech about its meaning. Your ending can be just as short.'),
])
