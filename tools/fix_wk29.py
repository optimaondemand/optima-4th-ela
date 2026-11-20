#!/usr/bin/env python3
"""Week 29 (Prince Caspian Ch. 10-12) fixes, checked against the text (Planning docs/PrinceCaspian_CSL.pdf), Nov 19 2026.
- 29.1: epigraph with Lewis's dialogue tag; DOL fix-it now has a real introductory phrase for its comma (it put a comma before
  "because"); precipice sentence is Lewis's (Ch. 9); luminous/sentient no longer show made-up "quotes"; Beruna is in Narnia, not
  Kent (date/place practice now uses Dover, Kent); spelling passage relabeled; chapter summary: Lucy is not breathed on (she feels
  lion-strength from his mane) and the gorge is Ch. 11.
- 29.2: epigraph completed; DOL fix-it was an invented Peter quote with a comma splice: now Peter's real words; Susan's model says
  "to Lucy in a very small voice" (she did not whisper to Aslan); the grammar spotter's "Narnia timeline" dates are made up, now
  said so; sentinel is the Ch. 12 badgers, not Trumpkin; the RWM sentence was invented: now Lewis's own semicolon sentence (Ch. 11).
- 29.3: DOL model put an invented shout in Edmund's mouth: now the Badger's real "Lies! All lies!"; DOL fix-it misquoted
  Trufflehunter: now his real Ch. 5 words; Peter's line quoted in full; Trufflehunter's "we hold on" is said to Peter after the
  fight, not against Nikabrik's plan; made-up dates flagged as practice.
- 29.4: DOL model was an invented Trumpkin quote: now his real "Wraiths and wreckage!"; Caspian speaks of Nikabrik (Nikabrik is
  dead); Peter confesses to Aslan, not Caspian; "If—" was published in 1910; made-up dates flagged as practice.
- Fluency: Lucy's line and Aslan's last line as Lewis wrote them.
- Check-in: Q5 and the reading passage were invented "Source: Prince Caspian" passages (one had Peter's forces disrupting Miraz,
  which is Ch. 13-14): now real Ch. 10 and Ch. 11 lines; model sentence now Aslan's real words. Q5 key stays B."""
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
MADEUP = ' (Narnia has no calendar, so these dates are made up for practice.)'

patch('lesson-29-1-pc-ch10.html', [
 ('&ldquo;That is because you are older, little one.&rdquo; &ldquo;Not because you are?&rdquo;', '&ldquo;That is because you are older, little one,&rdquo; answered he. &ldquo;Not because you are?&rdquo;'),
 ('lucy crept out of the camp at night because she herd aslan calling her name in the forrest', 'at night lucy crept out of the camp because she herd aslan calling her name in the forrest'),
 ('Find the missing capital on &ldquo;lucy,&rdquo; fix &ldquo;herd&rdquo; → &ldquo;heard,&rdquo; fix &ldquo;forrest&rdquo; → &ldquo;forest,&rdquo; and add the missing comma after &ldquo;night.&rdquo;',
  'Find the missing capitals on &ldquo;at&rdquo; and &ldquo;lucy,&rdquo; fix &ldquo;herd&rdquo; → &ldquo;heard,&rdquo; fix &ldquo;forrest&rdquo; → &ldquo;forest,&rdquo; and add the missing comma after &ldquo;night.&rdquo;'),
 ('<strong>L</strong>ucy crept out of the camp at night<strong>,</strong> because she <strong>heard</strong>', '<strong>A</strong>t night<strong>,</strong> <strong>L</strong>ucy crept out of the camp because she <strong>heard</strong>'),
 ('Capital L on &ldquo;Lucy&rdquo; (proper noun &mdash; character name). Add comma after &ldquo;night&rdquo; because the introductory phrase comes before the main clause.',
  'Capital A to start the sentence and capital L on &ldquo;Lucy&rdquo; (proper noun). Add a comma after &ldquo;At night&rdquo; because the introductory phrase comes before the main clause.'),
 ('&ldquo;They were on the edge of a <strong>precipice</strong>.&rdquo; <em>What clues does the sentence give you? Edge suggests something steep or dangerous.</em>',
  '&ldquo;They had come, without seeing it, almost to the edge of a small <strong>precipice</strong> from which they looked down into a gorge with a river at the bottom.&rdquo; (Chapter 9) <em>What clues does the sentence give you? Edge and looked down suggest something steep or dangerous.</em>'),
 ('Giving off light; glowing — &ldquo;His face was luminous in the moonlight&rdquo;', 'Giving off light; glowing'),
 ('Able to feel or perceive things; aware &mdash; &ldquo;Every tree felt sentient&rdquo;', 'Able to feel or perceive things; aware'),
 ('Beruna Kent', 'Dover Kent', 2), ('Beruna, Kent', 'Dover, Kent', 3),
 ('<p>A passage from Chapter 10. Most of these long words were built in Greek or Latin first.</p>', '<p>A sentence written for this lesson. Most of these long words were built in Greek or Latin first.</p>'),
 ('He breathes on her and tells her she must wake the others and follow him, even though they can&rsquo;t see him yet. One by one, they reluctantly follow Lucy into the dark forest. Aslan leads them down a gorge and up the other side.',
  'She buries her face in his mane and feels lion-strength go into her. He tells her she must wake the others and follow him, even though they can&rsquo;t see him yet. Lucy goes back and wakes Edmund first, and he can&rsquo;t see Aslan at all.'),
])
patch('lesson-29-2-pc-ch11.html', [
 ('I&rsquo;ve been leading them wrong ever since we started.&rdquo;</div>', 'I&rsquo;ve been leading them wrong ever since we started and especially yesterday morning.&rdquo;</div>'),
 ('<span> looked up at the great lion and whispered</span>', '<span> said to Lucy in a very small voice</span>'),
 ('peter knelt before aslan and said i have been leading them wrong can you forgive me', 'oh aslan said king peter im so glad'),
 ('Find: capital P on &ldquo;peter&rdquo; (start of sentence + name), capital A on &ldquo;aslan&rdquo; (proper noun), opening quotation mark before &ldquo;i,&rdquo; capital I on &ldquo;i,&rdquo; comma after &ldquo;wrong,&rdquo; question mark after &ldquo;me,&rdquo; closing quotation mark, period at end.',
  'Find: capitals on &ldquo;oh,&rdquo; &ldquo;aslan,&rdquo; &ldquo;king peter&rdquo; and &ldquo;im,&rdquo; the apostrophe in &ldquo;im,&rdquo; and the quotation marks and commas around the two parts of what Peter says.'),
 ('<strong>P</strong>eter knelt before <strong>A</strong>slan and said, &#x201C;<strong>I</strong> have been leading them wrong, can you forgive me?&#x201D;.',
  '&#x201C;<strong>O</strong>h, <strong>A</strong>slan,&#x201D; said <strong>K</strong>ing <strong>P</strong>eter, &#x201C;<strong>I</strong>&rsquo;m so glad.&#x201D;'),
 ('Capital P on &ldquo;Peter&rdquo; (proper noun, sentence start). Capital A on &ldquo;Aslan&rdquo; (proper noun). Comma after &ldquo;said&rdquo; before the quote. Opening and closing quotation marks around Peter&rsquo;s words. Capital I on &ldquo;I.&rdquo; Comma after &ldquo;wrong&rdquo; to separate the two parts of the dialogue. Question mark after &ldquo;me&rdquo; inside the quotes.',
  'These are Peter&rsquo;s real words in Chapter 11. Capitals on Oh, Aslan, King Peter and I&rsquo;m. Quotation marks go around each part Peter says; the commas after &ldquo;Aslan&rdquo; and &ldquo;Peter&rdquo; separate his words from &ldquo;said King Peter.&rdquo; The period goes inside the closing quotation mark.'),
 ('<strong>Sentinel</strong> &mdash; a guard or watchman standing watch; Trumpkin standing guard before Aslan wins him over.', '<strong>Sentinel</strong> &mdash; a guard or watchman standing watch; the two sentinel badgers at the door of Aslan&rsquo;s How in Chapter 12.'),
 ('<p>Dates and places from the Narnia timeline, punctuated by different hands.</p>', '<p>Practice sentences, punctuated by different hands.' + MADEUP + '</p>'),
 ('&ldquo;The trees were all around them; they were closing in, towering overhead.&rdquo;',
  '&ldquo;But as they drew nearer they looked less like trees; and when the whole crowd, bowing and curtsying and waving thin long arms to Aslan, were all around Lucy, she saw that it was a crowd of human shapes.&rdquo;'),
 ('What is happening here? The trees of Narnia are waking up around the children. Why would Lewis describe this moment so simply &mdash; just two short clauses &mdash; instead of giving it a long, dramatic description?',
  'What is happening here? Aslan has roared, and the trees of Narnia are coming toward him. What does Lucy think she is seeing at first, and what does she see when they reach her?'),
 ('Notice the semicolon. Lewis joins two clauses that could each stand alone as a sentence, so this is a <strong>compound</strong> sentence, not a complex one. A complex sentence would hook one part onto the other with a word like <em>as</em> or <em>because</em>, making one part depend on the other. Lewis does not do that here. He sets the two halves side by side as equals &mdash; trees all around, trees closing in overhead &mdash; and the semicolon keeps them in one breath. How does that side-by-side shape make the trees feel like they are moving in on you?',
  'Notice the semicolon. Before it, Lewis gives you the view from far away: <em>they looked less like trees</em>. After it, a <em>when</em> clause carries you closer and closer, through the bowing and the waving arms, and only at the very end do you learn what they really are: <em>a crowd of human shapes</em>. The semicolon is the pause between the far look and the near one. Why does Lewis save the surprise for the last words?'),
 ('Write your own compound sentence. Two halves that could each stand alone, joined by a semicolon, both looking at the same place from a slightly different angle.',
  'Write your own sentence about something seen from far away and then up close. Put the far view before a semicolon, and save the surprise for the last words.'),
 ('[First observation]; [second observation that adds to the first].', '[From far away it looked like ___]; and when [it came closer], [I saw that it was ___].'),
])
remodel('lesson-29-3-pc-ch12.html', [
 ('Nikabrik', '&quot;Nikabrik&quot; is a proper noun &mdash; always capitalized.'),
 (' praised the power of the ', None),
 ('White Witch', 'The White Witch is a name, so both words are capitalized.'),
 (',', 'A comma before &quot;and&quot; separates two independent clauses joined by a coordinating conjunction.'),
 (' and the ', None),
 ('Badger', 'Here &quot;the Badger&quot; names Trufflehunter, so Lewis capitalizes it.'),
 (' said', None),
 (',', 'Comma before a direct quote separates the speaker from the spoken words.'),
 (' ', None),
 ('&ldquo;', 'Opening quotation mark begins the character&rsquo;s exact words.'),
 ('Lies', 'The first word of a quotation is capitalized.'),
 ('!', 'An exclamation point shows strong feeling.'),
 (' All lies', None),
 ('!', 'An exclamation point ends the strong statement.'),
 ('&rdquo;', 'Closing quotation mark ends the character&rsquo;s exact words.'),
])
patch('lesson-29-3-pc-ch12.html', [
 ('nikabrik wanted to call up the white witch but trufflehunter the badger said we dont change we hold on', 'nikabrik wanted caspian dead but trufflehunter the badger said we dont change we hold on'),
 ('Find: 3 missing capital letters (nikabrik, witch &rarr; Witch, trufflehunter), missing comma before &ldquo;but,&rdquo; missing apostrophe in &ldquo;dont,&rdquo; and missing quotation marks around the speech.',
  'Find: 3 missing capital letters (nikabrik, caspian, trufflehunter), missing comma before &ldquo;but,&rdquo; missing apostrophe in &ldquo;dont,&rdquo; and missing quotation marks around the speech, which is two sentences.'),
 ('<strong>N</strong>ikabrik wanted to call up the <strong>W</strong>hite Witch<strong>,</strong> but <strong>T</strong>rufflehunter the badger said, &ldquo;We don&rsquo;t change, we hold on.&rdquo;',
  '<strong>N</strong>ikabrik wanted <strong>C</strong>aspian dead<strong>,</strong> but <strong>T</strong>rufflehunter the badger said, &ldquo;We don&rsquo;t change. We hold on.&rdquo;'),
 ('Capital W on &ldquo;Witch&rdquo; (part of proper name White Witch).', 'Capital C on &ldquo;Caspian&rdquo; (proper noun).'),
 ('Quotation marks around the exact words Trufflehunter speaks.', 'Quotation marks around Trufflehunter&rsquo;s exact words from Chapter 5: two short sentences.'),
 ('&ldquo;not to take your place, but to put you into it.&rdquo;', '&ldquo;not to take your place &hellip; but to put you into it.&rdquo;'),
 ('&ldquo;I haven&rsquo;t come to take your place, but to put you into it.&rdquo;', '&ldquo;I haven&rsquo;t come to take your place, you know, but to put you into it.&rdquo;', 2),
 ('Who says this? Trufflehunter the badger, pushing back against Nikabrik&rsquo;s dark plan.', 'Who says this? Trufflehunter the badger, after the fight, when Peter thanks him for never doubting them.'),
 ('How does this contrast with what Nikabrik wants to do?', 'How does this contrast with what Nikabrik chose to do?'),
 ('<p>Punctuation in dates and places is not style &mdash; it is how the reader groups the words.</p>', '<p>Punctuation in dates and places is not style &mdash; it is how the reader groups the words.' + MADEUP + '</p>'),
])
remodel('lesson-29-4-pc-discussion.html', [
 ('&ldquo;', 'Opening quotation mark begins the character&rsquo;s exact words.'),
 ('Wraiths and wreckage', 'The first word of a quotation is capitalized.'),
 ('!', 'An exclamation point shows strong feeling. It goes inside the closing quotation mark.'),
 ('&rdquo;', 'Closing quotation mark ends the character&rsquo;s exact words.'),
 (' gasped ', None),
 ('Trumpkin', '&quot;Trumpkin&quot; is a proper noun &mdash; always capitalized.'),
 (' in the ghost of a voice', None),
 ('.', 'A period ends the whole sentence.'),
])
patch('lesson-29-4-pc-discussion.html', [
 ('caspian looked at nikabrik sadly and said he had gone sour inside from long suffering and hateing', 'caspian spoke sadly of nikabrik and said he had gone sour inside from long suffering and hateing'),
 ('<strong>C</strong>aspian looked at <strong>N</strong>ikabrik sadly and said', '<strong>C</strong>aspian spoke sadly of <strong>N</strong>ikabrik and said'),
 ('Rudyard Kipling (1895)', 'Rudyard Kipling (published 1910)'),
 ('<p>A draft for the Narnia timeline. Some lines are punctuated correctly.</p>', '<p>A practice draft. Some lines are punctuated correctly.' + MADEUP + '</p>'),
 ('Peter admits his mistakes to Caspian.', 'Peter admits his mistakes to Aslan.'),
])
patch('lesson-29-fluency.html', [
 ('&ldquo;You&rsquo;re bigger, Aslan,&rdquo; said Lucy.', '&ldquo;Aslan,&rdquo; said Lucy, &ldquo;you&rsquo;re bigger.&rdquo;'),
 ('You have work to do, and much time has been lost.&rdquo;', 'You have work in hand, and much time has been lost today.&rdquo;'),
])
patch('week-29-checkin.html', [
 ('2. "The battle was won on April 14 1941 near the great stone table."', '2. "The children left for school on April 14 1941 from London England."'),
 ('"The arrival of Peter\'s forces disrupted Miraz\'s plans — breaking apart the order his commanders had expected and forcing a response no one had prepared for."<div class="excerpt-source">Source: Prince Caspian, Ch. 10–12</div>',
  '"The trees parted to let them through and for one second assumed their human forms completely."<div class="excerpt-source">C. S. Lewis, <em>Prince Caspian</em>, Ch. 10</div>'),
 ('What does "disrupted" most likely mean?', 'The base <em>form</em> means "shape." What are the trees\' "human forms"?'),
 ('<span class="opt-letter">A</span> Confirmed and strengthened</li>', '<span class="opt-letter">A</span> Their human names</li>'),
 ('<span class="opt-letter">B</span> Broken apart or thrown into disorder</li>', '<span class="opt-letter">B</span> Their human shapes</li>'),
 ('<span class="opt-letter">C</span> Delayed for a short time</li>', '<span class="opt-letter">C</span> Their human voices</li>'),
 ('"Again and again in these chapters, characters must choose between staying safe and doing what is right. The pattern repeats — in Caspian\'s choice, in Peter\'s challenge, in Lucy\'s willingness to follow Aslan alone. A theme is what a story keeps coming back to."<div class="excerpt-source">Source: Prince Caspian, Ch. 10–12</div>',
  '"Lucy," said Susan in a very small voice. "Yes?" said Lucy. "I see him now. I\'m sorry." "That\'s all right." "But I\'ve been far worse than you know. I really believed it was him — he, I mean — yesterday. … I mean, deep down inside. Or I could have, if I\'d let myself."<div class="excerpt-source">C. S. Lewis, <em>Prince Caspian</em>, Ch. 11</div>'),
 ('What repeated choice does the passage describe? What theme does this suggest?', 'What choice is Susan admitting she made? Where else in Ch. 9–12 does a character face the same kind of choice?'),
 ('"Although each character faces a different situation, they all make the same kind of choice — the one that costs something. That is Lewis\'s theme: that goodness requires sacrifice, and that the cost is part of what makes it matter."',
  '"It is hard for you, little one," said Aslan. "But things never happen the same way twice." — <em>Prince Caspian</em>, Ch. 10'),
 ('Notice how "although" introduces contrast and then the theme statement brings it together. Write your own complex sentence that introduces a contrast and ends with a theme statement about',
  'Notice how Aslan admits the hard part first, then turns with "but" to something true about life. Write your own sentence that admits something hard and then, after "but" or "although," says what you think Lewis is showing about'),
])
