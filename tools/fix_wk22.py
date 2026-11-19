#!/usr/bin/env python3
"""Week 22 (Freedom Train Ch. 10-14) curriculum fixes, checked against Sterling's text (IA freedomtrainstorster00ster).
Every replacement must match exactly the expected number of times or the script stops without writing."""
import io, re, sys

FILES = {1: 'lesson-22-1-ft-ch9.html', 2: 'lesson-22-2-ft-ch10.html', 3: 'lesson-22-3-ft-ch11.html', 4: 'lesson-22-4-ft-ch12.html'}
H = {d: io.open(f, encoding='utf-8', newline='').read() for d, f in FILES.items()}
ORIG = dict(H)

def rep(d, old, new, n=1):
    c = H[d].count(old)
    if c != n:
        sys.exit('day %d: expected %d of %r, found %d' % (d, n, old[:70], c))
    H[d] = H[d].replace(old, new)

def resub(d, pat, new, n=1):
    m = re.findall(pat, H[d], flags=re.S)
    if len(m) != n:
        sys.exit('day %d: expected %d of /%s/, found %d' % (d, n, pat[:60], len(m)))
    H[d] = re.sub(pat, lambda _m: new, H[d], flags=re.S)

def dol(words):
    """words: list of (text, note or None)"""
    out = []
    for t, note in words:
        if note:
            out.append('          <span class="dol-highlight-word" onclick="dolHighlight(this,\'%s\')">%s</span>' % (note, t))
        else:
            out.append('          <span>%s </span>' % t)
    return '<div class="dol-sentence-wrap" id="dolModel">\n' + '\n'.join(out) + '\n        </div>'

# ── all four days ──────────────────────────────────────────────
for d in FILES:
    # objectives: the pages teach adverbs and -ive/-al/-ic, not adjectives and -ion
    rep(d, '<strong>Grammar:</strong> I will <em>define</em> adjectives: words that describe nouns (a <em>tall</em> tree, a <em>kind</em> man).',
           '<strong>Grammar:</strong> I will <em>explain</em> how adverbs tell how, when, or where something happens (she moved <em>quietly</em>).')
    rep(d, '<strong>Spelling:</strong> I will <em>review</em> the suffix <em>-ion</em> and how it changes verbs into nouns (act &rarr; action).',
           '<strong>Spelling:</strong> I will <em>spell</em> words that end in the suffixes <em>-ive</em>, <em>-al</em>, and <em>-ic</em> (create &rarr; creative).')
    # vocabulary sentences are about the book, not quoted from it
    rep(d, 'Each word below has its actual sentence from the book above it.', 'Each word below has a sentence about the book above it.')
    # turn-in checklist: workshop line + the duplicated paste line
    rep(d, 'I wrote my Writing Connection sentence.', 'I finished today&rsquo;s Writer&rsquo;s Workshop.')
    dup = '<div class="turn-in-item" onclick="toggleCheck(this)"><div class="turn-in-check"></div><div class="turn-in-item-text">I pasted my full research project so far into the cumulative box and added today&rsquo;s new piece.</div></div>'
    resub(d, re.escape(dup) + r'\s*' + re.escape(dup), dup)
    # the Watch label
    rep(d, '💎 The Q4 lens', '💎 The big idea')

# morphology: a root is typed, not a prefix
for d in (1, 3):
    rep(d, 'Type the missing <strong>prefix</strong> at the start of each word.', 'Type the missing <strong>root</strong> to finish each word.')

# days 2-4: morphology SWYK still asked about last week's tele-/auto-
SWYK_OLD = ('<div class="swyk-prompt">Pick a word with <strong>tele-</strong> or <strong>auto-</strong>. Write the word, explain what the prefix changes, and use it in a sentence about Harriet&rsquo;s journey.</div>\n'
            '        <div class="textbox-prompt">Pick tele- or auto- and use it in a sentence.</div>')
SWYK_NEW = ('<div class="swyk-prompt">Pick a word with <strong>press</strong> or <strong>tain</strong>. Write the word, explain the root, and use it in a sentence about Harriet.</div>\n'
            '        <div class="textbox-prompt">Pick press or tain and use it in a sentence.</div>')
for d in (2, 3, 4):
    rep(d, SWYK_OLD, SWYK_NEW)
    rep(d, 'placeholder="My word is ___. The prefix means ___. My sentence is..."', 'placeholder="My word is ___. The root means ___. My sentence is..."')

def fill(items):
    rows = []
    for i, (pre, ans, mean) in enumerate(items, 1):
        rows.append('        <div class="fillin-item">%s<input class="fillin-input" id="fill%d" data-answer="%s" maxlength="8" placeholder="______"> &mdash; %s</div>' % (pre, i, ans, mean))
    return '\n'.join(rows)
FILL_OLD = re.escape('<div class="fillin-game" id="fillinGame">') + r'\s*(?:<div class="fillin-item"><input class="fillin-input" id="fill\d" data-answer="(?:tele|auto)"[^\n]*</div>\s*){4}'
for d, items in ((2, [('com', 'press', 'to push together'), ('op', 'press', 'to push down hard; to treat someone cruelly'),
                      ('at', 'tain', 'to reach; to get to'), ('de', 'tain', 'to hold back; to keep someone from leaving')]),
                 (4, [('re', 'press', 'to push back a feeling; to hold it in'), ('ex', 'press', 'to push out your thoughts in words'),
                      ('sus', 'tain', 'to hold up; to keep something going'), ('ob', 'tain', 'to take hold of; to get')])):
    rep(d, 'Type the missing <strong>prefix</strong> at the start of each word.', 'Type the missing <strong>root</strong> to finish each word.')
    resub(d, FILL_OLD, '<div class="fillin-game" id="fillinGame">\n' + fill(items) + '\n        ')

# vocabulary: day 1's modeled word is obtain; days 2-4 had last week's autograph block
rep(1, '📌 Let&rsquo;s try it together: &ldquo;resistance&rdquo;', '📌 Let&rsquo;s try it together: &ldquo;obtain&rdquo;')
m = re.search(r'<!-- MODELED WORD -->.*?(?=<div class="callout callout-info" style="margin-top:16px;"><span class="callout-icon">🎯</span><p><strong>Your turn!</strong>)', H[1], re.S)
MODEL = m.group(0)
for d in (2, 3, 4):
    resub(d, r'<!-- MODELED WORD -->.*?(?=<div class="callout callout-info" style="margin-top:16px;"><span class="callout-icon">🎯</span><p><strong>Your turn!</strong>)', MODEL)

# grammar / spelling passages are about the chapter, not from it; 22.4 is a Ch. 14 day
rep(1, '<p>A passage from Chapter 10.', '<p>Sentences about Chapter 10.', 2)
rep(4, '<p>A draft about Chapter 12.', '<p>A draft about Chapter 14.', 2)

# ── epigraphs (each line checked in Sterling) ──────────────────
rep(1, '<div class="quote-strip-text">&ldquo;Why not every man?&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Harriet (the chapter title), Ch. 10</div>',
       '<div class="quote-strip-text">&ldquo;My people must go free.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Harriet, Ch. 10</div>')
rep(2, '<div class="quote-strip-text">&ldquo;She would not leave them behind.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; narrator (about Harriet&rsquo;s parents), Ch. 12</div>',
       '<div class="quote-strip-text">&ldquo;Between them a man could feel safe.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; narrator (Ben, about Old Rit and Harriet), Ch. 12</div>')
rep(3, '<div class="quote-strip-text">&ldquo;She was the most wanted woman in the country.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; narrator (about the reward), Ch. 13</div>',
       '<div class="quote-strip-text">&ldquo;We&rsquo;re free! We&rsquo;ve shook the lion&rsquo;s paw!&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; the people Harriet led to Canada, Ch. 13</div>')
rep(4, '<div class="quote-strip-text">&ldquo;I never lost a passenger.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Harriet (quoted), Ch. 14</div>',
       '<div class="quote-strip-text">&ldquo;I never ran my train off the track and I never lost a passenger.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Harriet, Ch. 14</div>')

# ── DOL models "from the biography": now real lines ────────────
DOLPAT = r'<div class="dol-sentence-wrap" id="dolModel">.*?\n        </div>'
resub(1, DOLPAT, dol([('Then,', 'A comma after the opening word.'), ('slowly,', 'An ADVERB &mdash; tells HOW the water changed. Commas set it off.'),
                      ('the', None), ('water', None), ('grew', None), ('shallow', None), ('again', 'An ADVERB &mdash; tells WHEN.'), ('and', None),
                      ('Harriet', 'A name &mdash; capital H.'), ('was', None), ('clambering', None), ('up', None), ('a', None), ('slippery', None),
                      ('bank.', 'Period ends the statement.')]))
resub(2, DOLPAT, dol([('Tightly', 'An ADVERB &mdash; tells HOW she held the reins. Capital T starts the sentence.'), ('grasping', None), ('the', None),
                      ('reins,', 'A comma after the opening phrase.'), ('Harriet', 'A name &mdash; capital H.'), ('drove', None),
                      ('on,', 'A comma before the words that add more.'), ('faster and yet faster.', 'ADVERBS &mdash; tell HOW she drove. Period at the end.')]))
resub(3, DOLPAT, dol([('Again', 'An ADVERB &mdash; tells WHEN. Capital A starts the sentence.'), ('Harriet', 'A name &mdash; capital H.'), ('repeated', None),
                      ('her', None), ('message,', 'A comma before the words that add more.'), ('shaking', None), ('his', None), ('shoulder', None),
                      ('as', None), ('she', None), ('talked.', 'Period ends the statement.')]))
resub(4, DOLPAT, dol([('Fearless,', 'Capital F starts the sentence. A comma after the opening word.'), ('she', None), ('was', None),
                      ('never', 'An ADVERB &mdash; tells HOW OFTEN.'), ('reckless.', 'Period ends the statement.')]))

# ── 22.1 ──
rep(1, '<div class="textbox-prompt">Her family is still enslaved.</div>', '<div class="textbox-prompt">Look at who Harriet keeps going back for in this chapter.</div>')

# ── 22.2: Ch. 11 & 12 ──
rep(2, 'Harriet builds a cart. She moves at her parents&rsquo; pace. She refuses to leave anyone behind, even when speed would have helped her.',
       'Harriet sits in the Anti-Slavery office until she has the money. She builds a cart from junk-heap wheels so her old parents can ride instead of walk.')
rep(2, 'Her parents have been waiting for her since she was a child.', 'Look at what Harriet does to get the money and the cart.')
RWM2 = ('<div class="rwm-sentence">&ldquo;I&rsquo;m not going to leave here, and I&rsquo;m not going to eat or drink till I get money enough to take me down after the old people.&rdquo;'
        '<div style="margin-top:10px;font-family:\'Nunito\',sans-serif;font-style:normal;font-size:13px;color:#7A88A8;font-weight:700;">&mdash; Harriet, at the Anti-Slavery Society office, <em>Freedom Train</em>, Ch. 12</div></div>\n'
        '    <div class="rwm-step">\n      <div class="rwm-step-label">📖 Read like a Reader</div>\n'
        '      <div class="rwm-step-text">Old Ben is in jail, and Harriet needs money fast to rescue him and Old Rit. Nobody in the office has any to give. <strong>What does this sentence tell you about how far Harriet will go for her parents?</strong></div>')
resub(2, r'<div class="rwm-sentence">&ldquo;She would not leave them behind\.&rdquo;.*?<div class="rwm-step-label">📖 Read like a Reader</div>\s*<div class="rwm-step-text">.*?</div>', RWM2)
H[2] = re.sub(r'(<div class="rwm-step-label">✏️ Read like a Writer</div>\s*<div class="rwm-step-text">).*?(</div>)',
              lambda m: m.group(1) + 'Sterling lets Harriet say it herself, and Harriet says it as a refusal. <strong>I&rsquo;m not going to</strong> comes twice, so the second one lands harder than the first. Then one small word, <strong>till</strong>, names the only thing that will make her move. A writer who wants you to feel how stubborn a person is can stack up what that person will <em>not</em> do, and then name the one condition that ends it.' + m.group(2),
              H[2], count=1, flags=re.S)
H[2] = re.sub(r'(<div class="rwm-step-label">🖊️ Mimic</div>\s*<div class="rwm-step-text">).*?(</div>\s*<div class="rwm-frame">).*?(</div>)',
              lambda m: m.group(1) + 'Write one sentence where a person refuses to give up until they get what someone else needs. Use <em>I&rsquo;m not going to</em> twice, then <em>till</em>.' + m.group(2) + '&ldquo;I&rsquo;m not going to ___, and I&rsquo;m not going to ___ till ___.&rdquo;' + m.group(3),
              H[2], count=1, flags=re.S)

# ── 22.3: Ch. 13 is the Fugitive Slave Law and Canada; the reward is in Ch. 14 ──
rep(3, 'The Underground Railroad now stretches to Canada. The reward for catching Harriet is enormous. What does she do? She keeps going back.',
       'A new law makes the North unsafe for anyone who ran away. So Harriet leads her people all the way to Canada. Then what does she do? She keeps going back.')
rep(3, 'As you read Ch. 13, sort real causes from things that only happen afterward. The Underground Railroad now reaches all the way to Canada, and the reward for catching Harriet has grown enormous &mdash; test whether one of those <strong>caused</strong> the other. Then look at the danger of the lion&rsquo;s paw and her choice to keep going back. Does the growing danger cause her to stop, or is something else driving her?',
       'As you read Ch. 13, sort real causes from things that only happen afterward. In 1850 Congress passes the Fugitive Slave Law, and soon the Underground Railroad runs all the way to Canada &mdash; test whether the first <strong>caused</strong> the second. Then look at Harriet&rsquo;s new home in St. Catharines and her choice to keep going back. Is it the law that keeps her going, or something else?')
rep(3, '<div class="activity-sub">When the danger gets bigger, she gets braver</div>', '<div class="activity-sub">When the safe place moves farther away, she goes farther</div>')
rep(3, '<p>Slave catchers want Harriet. The reward is enormous. Most people would stop. Harriet keeps going.</p>',
       '<p>The North is not safe anymore. Harriet could stay in Canada. She keeps going back.</p>')
rep(3, 'The reward grows. The risk grows. The danger of the &lsquo;lion&rsquo;s paw&rsquo; grows. Harriet does not slow down.',
       'Harriet builds a home for her family in St. Catharines. But it cannot be her home while there is still slavery in the South, so she sets off again.')
rep(3, 'Open your biography to <strong>Chapter 13: The Lion&rsquo;s Paw</strong>. Slave catchers want Harriet. The reward for catching her is huge. The Underground Railroad now stretches all the way to Canada. Harriet keeps going back. Read for the &lsquo;lion&rsquo;s paw&rsquo; &mdash; what the chapter title means &mdash; and why Harriet refuses to stop.',
       'Open your biography to <strong>Chapter 13: The Lion&rsquo;s Paw</strong>. A new law lets slave catchers chase runaways even in the North. So the Underground Railroad stretches all the way to Canada. Read for the &lsquo;lion&rsquo;s paw&rsquo; &mdash; what the chapter title means &mdash; and why Harriet keeps going back.')
rep(3, 'The reward for catching Harriet has grown enormous. <strong>What is the &lsquo;Lion&rsquo;s Paw&rsquo;? Why is the danger growing?</strong>',
       'A new law lets slave catchers hunt runaways in the North. <strong>Why does Harriet stop trusting &lsquo;Uncle Sam&rsquo; with her people?</strong>')
rep(3, 'Most people would stop. Harriet doesn&rsquo;t. <strong>What does that tell us about her?</strong>',
       'Harriet&rsquo;s family is safe in St. Catharines. <strong>Why does she keep leaving it?</strong>')
rep(3, '<div class="textbox-prompt">Canada is a free country. The U.S. north isn&rsquo;t fully safe anymore.</div>',
       '<div class="textbox-prompt">Look at where Harriet&rsquo;s party gets off the train at the Falls.</div>')
rep(3, '<strong>What is the &lsquo;Lion&rsquo;s Paw&rsquo;?</strong> (Hint: it&rsquo;s a metaphor for danger.) Explain what it stands for in the chapter.',
       '<strong>What is the &lsquo;Lion&rsquo;s Paw&rsquo;?</strong> (Hint: it&rsquo;s a metaphor. The lion is the British lion.) Explain what it stands for in the chapter.')
rep(3, '<div class="textbox-prompt">Think about lions: powerful, dangerous, hard to escape.</div>',
       '<div class="textbox-prompt">Look at the song the runaways sing, and what Harriet says about the British lion.</div>')
rep(3, '<strong>Cause and effect:</strong> The reward for catching Harriet grew bigger. What was the EFFECT on Harriet&rsquo;s work?',
       '<strong>Cause and effect:</strong> In 1850 Congress passed the Fugitive Slave Law. What was the EFFECT on Harriet&rsquo;s work?')
rep(3, '<div class="textbox-prompt">Most people would stop. Harriet didn&rsquo;t.</div>', '<div class="textbox-prompt">Where did Harriet start taking the people she led?</div>')
rep(3, 'placeholder="When the reward grew, Harriet... This shows that..."', 'placeholder="Because of the law, Harriet... This shows that..."')
rep(3, 'placeholder="The Lion&rsquo;s Paw is a metaphor for..."', 'placeholder="The Lion&rsquo;s Paw stands for..."')
RWM3_S = ('<div class="rwm-sentence">&ldquo;Beyond the Falls was the new land.&rdquo;'
          '<div style="margin-top:10px;font-family:\'Nunito\',sans-serif;font-style:normal;font-size:13px;color:#7A88A8;font-weight:700;">&mdash; narrator, <em>Freedom Train</em>, Ch. 13</div></div>')
resub(3, r'<div class="rwm-sentence">&ldquo;She was the most wanted woman in the country\.&rdquo;.*?</div></div>', RWM3_S)
H[3] = re.sub(r'(<div class="rwm-step-label">📖 Read like a Reader</div>\s*<div class="rwm-step-text">).*?(</div>)',
              lambda m: m.group(1) + 'Harriet&rsquo;s party is on the train, crossing the bridge at Niagara Falls. On the other side is Canada, where the law cannot send them back. <strong>What does &ldquo;the new land&rdquo; mean to the people on that train?</strong>' + m.group(2), H[3], count=1, flags=re.S)
H[3] = re.sub(r'(<div class="rwm-step-label">✏️ Read like a Writer</div>\s*<div class="rwm-step-text">).*?(</div>)',
              lambda m: m.group(1) + 'The sentence just before this one is long: giant icicles, thundering water, a roar over the cliff. Then Sterling writes seven plain words and stops. She also turns the sentence around. Most sentences start with who or what (<em>The new land was beyond the Falls</em>). This one starts with the place, <strong>Beyond the Falls</strong>, and saves <strong>the new land</strong> for the very end, so the sentence finishes on the thing they have been traveling toward. A short, turned-around sentence after a long one makes a reader stop and feel the moment.' + m.group(2), H[3], count=1, flags=re.S)
H[3] = re.sub(r'(<div class="rwm-step-label">🖊️ Mimic</div>\s*<div class="rwm-step-text">).*?(</div>\s*<div class="rwm-frame">).*?(</div>)',
              lambda m: m.group(1) + 'Write one short sentence about a place someone is trying to reach. Start with where it is, and end with what it is. Keep it plain.' + m.group(2) + 'Beyond the ___ was the ___.' + m.group(3), H[3], count=1, flags=re.S)

# ── 22.4: Moses ──
rep(4, 'The people Harriet rescues and the abolitionists she works with begin calling her Moses. List the reasons that name fits &mdash; the many trips into Maryland, the dozens of people she leads out, the fact that she never loses one.',
       'The enslaved people begin calling Harriet Moses. List the reasons that name fits &mdash; the many trips into Maryland, the hundreds of people she leads out, the fact that she never loses one.')
rep(4, 'Across many trips, Harriet leads dozens of people to freedom. She never loses one. The people she rescues, and the abolitionists she works with, start calling her <em>Moses</em>',
       'Across many trips, Harriet leads hundreds of people to freedom. She never loses one. The enslaved people start calling her <em>Moses</em>')
rep(4, 'Across many trips, Harriet never loses a single person. That record is why they call her Moses &mdash; the leader who brings his people home.',
       'The enslaved people call her Moses, and the stories about her grow into legends. Harriet says she never lost a single passenger.')
rep(4, '<em>Steal Away</em> &mdash; a spiritual that sounded like ordinary praise music. But to enslaved people who knew what to listen for, the song was a coded signal: <em>I&rsquo;m here. Be ready.</em> According to Sterling&rsquo;s biography, this allowed Tubman to communicate her presence without ever speak',
       '<em>Go Down, Moses</em> &mdash; a spiritual that sounded like ordinary praise music. But to enslaved people who knew what to listen for, the song was a coded signal: <em>I&rsquo;m here. Be ready.</em> According to Sterling&rsquo;s biography, a verse sung twice or a changed word could carry a warning, so Tubman could communicate without ever speak')
rep(4, '<em>Steal Away</em>; sounded like praise music;', '<em>Go Down, Moses</em>; sounded like praise music;')

# guards: div balance unchanged, nothing invented left
for d in FILES:
    for s in ('She would not leave them behind', 'most wanted woman', 'tele-', 'autograph', 'Q4 lens'):
        if s in H[d]: sys.exit('day %d still has %r' % (d, s))
    a = (ORIG[d].count('<div'), ORIG[d].count('</div>')); b = (H[d].count('<div'), H[d].count('</div>'))
    if a[0] - a[1] != b[0] - b[1]: sys.exit('day %d div balance changed %s -> %s' % (d, a, b))
if '--apply' in sys.argv:
    for d, f in FILES.items(): io.open(f, 'w', encoding='utf-8', newline='').write(H[d])
    print('written')
else:
    print('dry run ok')
