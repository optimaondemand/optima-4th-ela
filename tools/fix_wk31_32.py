#!/usr/bin/env python3
"""Weeks 31-32 (year-end synthesis + final project) fixes, checked against the books, Nov 20 2026:
Prince Caspian (Planning docs/PrinceCaspian_CSL.pdf), Number the Stars (Bethany's copy), Anne of Green Gables (public-domain
text, Standard Ebooks).
- Invented "quotes" credited to the books replaced with real lines: "It was not a beautiful face, but it was a face full of
  life and gladness and imagination" (not in Anne), Peter/Caspian, Anne/Diana, Annemarie/Ellen, Lucy/Aslan, Mama Johansen,
  Marilla "real blessing" DOL sentences (none in the books), "That child has bewitched us both" (Marilla's real words are
  "Matthew Cuthbert, I believe that child has bewitched you!").
- "Once a king or queen in Narnia" is The Lion, the Witch and the Wardrobe, not Prince Caspian: 32.1 copywork is now Peter's
  real line from Prince Caspian.
- Aslan's "You come of the Lord Adam..." restored on both fluency pages ("come from", "lift up" were misquotes).
- Number the Stars: "which still clutched Ellen's necklace" (not "gripped").
- "Stories never really end..." was credited to "On the power of story": now marked as written for these lessons.
- Check-ins: passages written for the check-in no longer say "Source:"; week 31's passage had Mrs. Frisby crossing a flooded
  field and Harriet making "nineteen" trips: now facts from the books.
- 32.4 editing draft: the made-up Trufflehunter quote is gone."""
import io, re, sys
def rd(fn): return io.open(fn, encoding='utf-8', newline='').read()
def wr(fn, s): io.open(fn, 'w', encoding='utf-8', newline='').write(s)
def patch(fn, pairs):
    s = rd(fn)
    for a, b, *n in pairs:
        n = n[0] if n else 1
        c = s.count(a)
        if c != n: sys.exit('%s: expected %d, found %d: %r' % (fn, n, c, a[:90]))
        s = s.replace(a, b)
    wr(fn, s); print('ok', fn)
def rx(fn, pat, rep, n=1):
    s = rd(fn); s2, c = re.subn(pat, rep, s, flags=re.S)
    if c != n: sys.exit('%s: regex expected %d, found %d: %r' % (fn, n, c, pat[:80]))
    wr(fn, s2); print('ok rx', fn)
def remodel(fn, spans):
    s = rd(fn)
    i = s.index('<div class="dol-sentence-wrap" id="dolModel">'); i = s.index('>', i) + 1
    j = s.index('</div>', i)
    out = '\n'
    for t, why in spans:
        out += ('          <span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>\n' % (why, t)) if why else '          <span>%s</span>\n' % t
    wr(fn, s[:i] + out + '        ' + s[j:]); print('ok model', fn)
def fixit(fn, raw, hint, corrected, why):
    s = rd(fn)
    i = s.index('<div class="dol-fix-label">'); i = s.index('<div class="dol-sentence-wrap"', i); i = s.index('>', i) + 1
    j = s.index('</div>', i)
    s = s[:i] + '\n          ' + raw + '\n        ' + s[j:]
    i = s.index('<div class="dol-hint">', i); j = s.index('</div>', i)
    s = s[:i] + '<div class="dol-hint">' + hint + s[j:]
    i = s.index('<strong>Corrected:</strong>', i); j = s.index('</p>', i)
    s = s[:i] + '<strong>Corrected:</strong> ' + corrected + s[j:]
    i = s.index('<p style="font-size:13px;color:#7A88A8;font-style:italic;">', i); i = s.index('>', i) + 1; j = s.index('</p>', i)
    wr(fn, s[:i] + why + s[j:]); print('ok fixit', fn)
B = lambda x: '<strong>' + x + '</strong>'
Q = lambda w: ('&ldquo;', 'Opening quotation mark begins the exact words.') if w == 'o' else ('&rdquo;', 'Closing quotation mark ends the exact words.')
L31 = {1: 'lesson-31-1-synthesis-compare.html', 2: 'lesson-31-2-synthesis-compare.html', 3: 'lesson-31-3-synthesis-compare.html', 4: 'lesson-31-4-synthesis-discussion.html'}
L32 = {1: 'lesson-32-1-project-final.html', 2: 'lesson-32-2-project-final.html', 3: 'lesson-32-3-project-final.html', 4: 'lesson-32-4-project-celebration.html'}

# 31.1: copywork (invented "Montgomery" line) -> Anne's real question; DOL fix-it -> Peter's real words
patch(L31[1], [
 ('&ldquo;It was not a beautiful face, but it was a face full of life and gladness and imagination.&rdquo;',
  '&ldquo;Marilla,&rdquo; she demanded presently, &ldquo;do you think that I shall ever have a bosom friend in Avonlea?&rdquo;'),
])
rx(L31[1], r'(&mdash; L\. M\. Montgomery, )(<em>)?Anne of Green Gables(</em>)?', r'\1\2Anne of Green Gables\3, Ch. 8')
fixit(L31[1], 'peter said to caspian i havent come to take your place you know but to put you into it',
      'Find: capitals on <em>peter</em>, <em>caspian</em> and <em>i</em>; a comma after &ldquo;Caspian&rdquo; before the quote; quotation marks; the apostrophe in <em>haven&rsquo;t</em>; commas around &ldquo;you know&rdquo;; a period inside the closing quotation mark.',
      B('P') + 'eter said to ' + B('C') + 'aspian' + B(',') + ' &ldquo;' + B('I') + ' haven' + B('&rsquo;') + 't come to take your place' + B(',') + ' you know' + B(',') + ' but to put you into it' + B('.') + '&rdquo;',
      'Peter&rsquo;s real words in <em>Prince Caspian</em>, Chapter 12. Capitals on Peter, Caspian and I; a comma before the quote; the apostrophe in haven&rsquo;t; commas set off &ldquo;you know&rdquo;; the period goes inside the closing quotation mark.')

# 31.2: epigraph label; DOL model (invented NTS line) -> Uncle Henrik's real question; fix-it -> Matthew's real words
patch(L31[2], [('<div class="quote-strip-attr">&mdash; On the power of story</div>', '<div class="quote-strip-attr">&mdash; written for these lessons</div>')])
remodel(L31[2], [('Uncle Henrik', 'A name: both words are capitalized.'), (' asked', None), (',', 'A comma comes before the quote.'), (' ', None), Q('o'),
                 ('How', 'The first word of a quotation is capitalized.'), (' brave are you', None), (',', 'A comma before the name of the person being spoken to.'),
                 (' little ', None), ('Annemarie', 'A name is always capitalized.'), ('?', 'A question mark goes inside the quotation mark.'), Q('c')])
fixit(L31[2], 'we might be some good to her said matthew suddenly and unexpectedly',
      'Find: quotation marks around Matthew&rsquo;s words, a capital W to start, a comma inside the closing quotation mark, a capital M on <em>matthew</em>, and a period at the end.',
      '&ldquo;' + B('W') + 'e might be some good to her' + B(',') + '&rdquo; said ' + B('M') + 'atthew suddenly and unexpectedly' + B('.'),
      'Matthew&rsquo;s real words in <em>Anne of Green Gables</em>, Chapter 3. The quote comes first, so the comma goes inside the closing quotation mark, then the tag &ldquo;said Matthew,&rdquo; then a period.')

# 31.3: copywork -> Anne's real rose line + notes; fix-it -> real NTS line; RWM "clutched"
patch(L31[3], [
 ('&ldquo;It was not a beautiful face, but it was a face full of life and gladness and imagination.&rdquo; &mdash; <em>Anne of Green Gables</em>',
  '&ldquo;I read in a book once that a rose by any other name would smell as sweet, but I&rsquo;ve never been able to believe it.&rdquo; &mdash; <em>Anne of Green Gables</em>, Ch. 5'),
 ('which still gripped Ellen&rsquo;s necklace.&rdquo;', 'which still clutched Ellen&rsquo;s necklace.&rdquo;'),
 ('placeholder="[Character] relaxed the clenched ___, which still gripped ___."', 'placeholder="[Character] relaxed the clenched ___, which still clutched ___."'),
])
rx(L31[3], r'Montgomery uses a contrast &mdash; &ldquo;not a beautiful face, but a face full of life\.&rdquo; The &ldquo;not ___, but ___&rdquo; structure sets two opposing ideas side by side\.',
   'Montgomery uses a contrast &mdash; what the book says, <em>but</em> what Anne believes. The &ldquo;___, but ___&rdquo; structure sets two opposing ideas side by side.')
fixit(L31[3], 'go now and get into your nightgowns it will be a long night',
      'Find: quotation marks around the words, a capital G, commas around &ldquo;now,&rdquo; a period after &ldquo;nightgowns,&rdquo; a capital I to start the second sentence, and a period inside the closing quotation mark.',
      '&ldquo;' + B('G') + 'o' + B(',') + ' now' + B(',') + ' and get into your nightgowns' + B('.') + ' ' + B('I') + 't will be a long night' + B('.') + '&rdquo;',
      'Real words from <em>Number the Stars</em>, Chapter 4. Two sentences inside one pair of quotation marks; commas set off &ldquo;now&rdquo;; each sentence starts with a capital and ends with a period.')

# 31.4: fix-it -> Peter's real words (Ch. 15)
fixit(L31[4], 'peter said he says were getting too old',
      'Find: capital P on <em>peter</em>, a comma after &ldquo;said,&rdquo; quotation marks, a capital H, the apostrophe in <em>we&rsquo;re</em>, and a period inside the closing quotation mark.',
      B('P') + 'eter said' + B(',') + ' &ldquo;' + B('H') + 'e says we' + B('&rsquo;') + 're getting too old' + B('.') + '&rdquo;',
      'Peter&rsquo;s real words to Lucy in <em>Prince Caspian</em>, Chapter 15. We&rsquo;re is a contraction of we are, so it needs an apostrophe (were is a different word).')

# fluency pages: Aslan's line as Lewis wrote it
for fn in ('lesson-31-fluency.html', 'lesson-32-fluency.html'):
    rx(fn, r'&ldquo;You come from the Lord Adam and the Lady Eve\. And that is both honor enough to lift up the head',
       '&ldquo;You come of the Lord Adam and the Lady Eve,&rdquo; said Aslan. &ldquo;And that is both honour enough to erect the head')

# 32.1: DOL model -> Uncle Henrik's real line; fix-it -> Marilla's real words; copywork -> Peter (PC), not LWW
remodel(L32[1], [('He', 'The first word of the sentence is capitalized.'), (' interrupted her', None), (',', 'Commas set off the extra detail.'), (' smiling', None),
                 (',', 'A comma comes before the quote.'), (' ', None), Q('o'), ('That&rsquo;s', 'The first word of a quotation is capitalized; the apostrophe shows That is.'),
                 (' all that brave means', None), ('&mdash;', 'A dash adds the explanation.'), ('not thinking about the dangers', None),
                 ('.', 'The period goes inside the closing quotation mark.'), Q('c')])
fixit(L32[1], 'matthew cuthbert i believe that child has bewitched you said marilla',
      'Find: quotation marks around Marilla&rsquo;s words, capitals on <em>matthew cuthbert</em> and <em>i</em>, a comma after the name of the person spoken to, an exclamation point inside the quotation marks, a capital M on <em>marilla</em>.',
      '&ldquo;' + B('M') + 'atthew ' + B('C') + 'uthbert' + B(',') + ' ' + B('I') + ' believe that child has bewitched you' + B('!') + '&rdquo; said ' + B('M') + 'arilla' + B('.'),
      'Marilla&rsquo;s real words in <em>Anne of Green Gables</em>, Chapter 3. A comma follows the name of the person spoken to; the exclamation point goes inside the quotation marks; the tag &ldquo;said Marilla&rdquo; ends with a period.')
patch(L32[1], [
 ('&ldquo;Once a king or queen in Narnia, always a king or queen.&rdquo;</p>', '&ldquo;I haven&rsquo;t come to take your place, you know, but to put you into it.&rdquo;</p>'),
 ('&mdash; C. S. Lewis, <em>Prince Caspian</em></p>', '&mdash; Peter to Caspian, <em>Prince Caspian</em>, Ch. 12</p>'),
 ('Lewis builds this sentence with a satisfying parallel structure: &ldquo;Once a king or queen&hellip; always a king or queen.&rdquo; The repeated phrase creates a sense of permanence &mdash; some things do not change.',
  'Lewis builds this sentence on a turn: &ldquo;not to take &hellip; but to put.&rdquo; Two opposite actions with the same object, your place, show exactly what kind of king Peter is.'),
])

# 32.2: label; fix-it -> Mama's real words (NTS)
patch(L32[2], [('<div class="quote-strip-attr">&mdash; On the power of story</div>', '<div class="quote-strip-attr">&mdash; written for these lessons</div>')])
fixit(L32[2], 'put this packet underneath do you understand hurry',
      'Find: quotation marks, a capital P, a semicolon after &ldquo;underneath,&rdquo; a question mark after &ldquo;understand,&rdquo; a capital H, and a period inside the closing quotation mark.',
      '&ldquo;' + B('P') + 'ut this packet underneath' + B(';') + ' do you understand' + B('?') + ' ' + B('H') + 'urry' + B('.') + '&rdquo;',
      'Mama&rsquo;s real words in <em>Number the Stars</em>. Three short pieces, each with its own mark, all inside one pair of quotation marks.')

# 32.3: fix-it -> Anne's real question
fixit(L32[3], 'marilla she demanded presently do you think that i shall ever have a bosom friend in avonlea',
      'Find: quotation marks around each part Anne says, capitals on <em>marilla</em>, <em>do</em>, <em>i</em> and <em>avonlea</em>, a comma inside the first closing quotation mark, a comma after &ldquo;presently,&rdquo; and a question mark inside the last quotation mark.',
      '&ldquo;' + B('M') + 'arilla' + B(',') + '&rdquo; she demanded presently' + B(',') + ' &ldquo;' + B('d') + 'o you think that ' + B('I') + ' shall ever have a bosom friend in ' + B('A') + 'vonlea' + B('?') + '&rdquo;',
      'Anne&rsquo;s real words in <em>Anne of Green Gables</em>, Chapter 8. The tag splits one sentence, so the second part starts with a lowercase <em>do</em>; the question mark goes inside the last quotation mark.')

# 32.4: DOL model -> Lucy's real words; fix-it -> Matthew's real words; editing draft without the made-up quote
remodel(L32[4], [Q('o'), ('Oh', 'The first word of a quotation is capitalized.'), (',', 'A comma before the name of the person spoken to.'), (' ', None),
                 ('Peter', 'A name is always capitalized.'), (',', 'The comma goes inside the closing quotation mark.'), Q('c'), (' said ', None),
                 ('Lucy', 'A name is always capitalized.'), ('.', 'A period ends the tag, because the next part is a new sentence.'), (' ', None), Q('o'),
                 ('What', 'A new sentence inside the quote starts with a capital.'), (' awful bad luck', None), ('.', 'The period goes inside the closing quotation mark.'), Q('c')])
fixit(L32[4], 'matthew said it was a girl my girl my girl that im proud of',
      'Find: capital M on <em>matthew</em>, a comma before the quote, quotation marks, a capital I, dashes before each &ldquo;my girl,&rdquo; the apostrophe in <em>I&rsquo;m</em>, and a period inside the closing quotation mark.',
      B('M') + 'atthew said' + B(',') + ' &ldquo;' + B('I') + 't was a girl' + B('&mdash;') + 'my girl' + B('&mdash;') + 'my girl that ' + B('I&rsquo;m') + ' proud of' + B('.') + '&rdquo;',
      'Matthew&rsquo;s real words in <em>Anne of Green Gables</em>, Chapter 36. The dashes make the reader pause the way Matthew does.')
patch(L32[4], [('<span class="spotter-word" onclick="_oaoSpotAll(this,\'g4w32d\')" data-correct="false">&ldquo;We have waited a long time,&rdquo; said Trufflehunter.</span>',
                '<span class="spotter-word" onclick="_oaoSpotAll(this,\'g4w32d\')" data-correct="false">Trufflehunter never stopped believing.</span>')])

# check-ins
patch('week-31-checkin.html', [
 ('Whether it was Mrs. Frisby crossing a flooded field, Anne enduring a strict guardian, or Harriet making nineteen dangerous trips',
  'Whether it was Mrs. Frisby slipping into a farmhouse with a cat inside, Anne keeping her temper in a strict new home, or Harriet going back south again and again'),
])
for fn in ('week-31-checkin.html', 'week-32-checkin.html'):
    s = rd(fn); s2, c = re.subn(r'<div class="excerpt-source">Source:[^<]*</div>', '<div class="excerpt-source">Written for this check-in</div>', s)
    wr(fn, s2); print(fn, 'sources relabeled', c)

# copywork intro on 32.3 named the wrong book (the sentence is from Number the Stars); 32.3 hint: "do" stays lowercase
patch(L32[3], [
 ('This sentence from <em>Anne of Green Gables</em> is a beautiful example of contrast.', 'This sentence from <em>Number the Stars</em> is a beautiful example of contrast.'),
 ('capitals on <em>marilla</em>, <em>do</em>, <em>i</em> and <em>avonlea</em>', 'capitals on <em>marilla</em>, <em>i</em> and <em>avonlea</em>'),
])
