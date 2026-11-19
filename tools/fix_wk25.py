#!/usr/bin/env python3
"""Week 25 (Freedom Train: comparing sources) fixes, checked Nov 19 2026.
- Source A (Wisconsin State Journal, June 20, 1863) reads "300 black soldiers"; the lessons dropped "black".
- 25.1 intro: about 300 soldiers (Source A, the regiment's size), not 150; "largest liberation raid" softened.
- Source A's writer: a correspondent with the Union troops in South Carolina, printed without his name.
- Source C (Bradford 1869) reprints Tubman's own letter, so it also gives "seven hundred and fifty-six".
- "contraband": the Union army's word (from goods brought in against the law), not the slaveholders' term;
  Tubman's irony is "livestock". 25.1 vocab card and 25.3 cloze fixed.
- 25.2 "The raid was an international news story" and 25.3 "soldiers had to submerge" were invented: rewritten.
- 25.4 epigraph "Every great dream begins with a dreamer" is not Tubman's (no source; a modern misattribution):
  replaced with her own words as Sarah Bradford recorded them (1886).
- Check-in: invented Q5 sentence and invented "Account B" replaced with this week's real sources; prefixes and
  confused words now match the week (super- not ex-; affect/effect, accept/except, their/there, its/it's)."""
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
    io.open(fn, 'w', encoding='utf-8', newline='').write(s)
    print('ok', fn)

A_OLD = 'gallant band of 300 soldiers under the guidance'
A_NEW = 'gallant band of 300 black soldiers under the guidance'

patch('lesson-25-1-ft-sources.html', [
 (A_OLD, A_NEW),
 ('<p>On June 2, 1863, Harriet Tubman led 150 Black Union soldiers up the Combahee River in South Carolina. They freed more than 700 enslaved people &mdash; the largest liberation raid of the Civil War. Two different writers reported on the raid. Read both accounts below.</p>',
  '<p>On the night of June 1&ndash;2, 1863, Harriet Tubman guided Colonel Montgomery&rsquo;s Black Union soldiers up the Combahee River in South Carolina. More than 700 enslaved people were freed in one night. Two different writers reported on the raid. Read both accounts below.</p>'),
 ('Anonymous reporter &mdash; heard about the raid when ships docked in Beaufort, SC. Did NOT name Tubman;',
  'A reporter with the Union troops in South Carolina; the paper printed it without his name. Did NOT name Tubman;'),
 ('The writer calls people &ldquo;livestock&rdquo; and &ldquo;contrabands&rdquo; &mdash; clearly referring to enslaved people who escaped. The word is connected to people going against the system.',
  'Tubman calls the people she freed &ldquo;livestock&rdquo; and &ldquo;contrabands.&rdquo; She is talking about enslaved people who escaped to the Union army.'),
 ('<strong>band</strong> = group or order. People who went against the established order by escaping.',
  '<strong>band</strong> comes from an old word for a law or an order, like <em>ban</em>. Contraband first meant goods brought in against the law. In the Civil War, the Union army used the word for people who escaped slavery to its lines.'),
])

patch('lesson-25-2-ft-sources.html', [
 (A_OLD, A_NEW, 2),
 ('<td>Varies by passage</td>', '<td>&ldquo;seven hundred and fifty-six&rdquo; (she reprints Tubman&rsquo;s letter)</td>'),
])

patch('lesson-25-3-ft-sources.html', [
 (A_OLD, A_NEW),
 ('placeholder="______">merge in the river to avoid being seen by Confederate scouts.',
  'placeholder="______">merged torpedoes hidden under the water could sink a Union boat.'),
 ('&rdquo; &mdash; using the slaveholders&rsquo; own legal term with biting irony.',
  '&rdquo; &mdash; the Union army&rsquo;s word for people who escaped to its lines.'),
])

patch('lesson-25-4-ft-sources.html', [
 (A_OLD, A_NEW),
 ('&ldquo;Every great dream begins with a dreamer. Always remember, you have within you the strength, the patience, and the passion to reach for the stars.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Harriet Tubman</div>',
  '&ldquo;I had crossed the line. I was free; but there was no one to welcome me to the land of freedom.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Harriet Tubman, as told to Sarah Bradford (1886)</div>'),
])



patch('lesson-25-2-ft-sources.html', [
 ('The raid was an <em>international</em> news story.',
  'Her scouts carried news between the plantations and the gunboats, the way an <em>interpreter</em> carries words between two languages.'),
])

CK = 'week-25-checkin.html'
patch(CK, [
 ('<strong>ex-</strong> (out) &nbsp;/&nbsp; <strong>sub-</strong> (under)',
  '<strong>super-</strong> (above, beyond) &nbsp;/&nbsp; <strong>sub-</strong> (under)'),
 ('<div class="excerpt">"The work of abolitionists and the courage of freedom seekers were intersecting forces — each giving the other strength and direction."<div class="excerpt-source">Source: Primary source study materials, Week 25</div></div>\n        <div class="q-text">What does "intersecting" most likely mean?</div>',
  '<div class="excerpt">“…destroying millions of dollars worth of commissary stores, cotton and lordly dwellings…”<div class="excerpt-source">— Source A, <em>Wisconsin State Journal</em>, June 1863</div></div>\n        <div class="q-text">The raiders destroyed the Confederate army’s <strong>commissary</strong> stores. What does <strong>commissary</strong> most likely mean?</div>'),
 ('<span class="opt-letter">A</span> Competing against each other in opposite directions</li>', '<span class="opt-letter">A</span> A church where soldiers prayed</li>'),
 ('<span class="opt-letter">B</span> Crossing and connecting with each other</li>', '<span class="opt-letter">B</span> A place where food and supplies for an army are kept</li>'),
 ('<span class="opt-letter">C</span> Moving separately without any connection</li>', '<span class="opt-letter">C</span> A boat that carries soldiers up a river</li>'),
 ('Use "export" and "submerge" in two sentences that show their meanings.<p class="hint">Hint: ex- = out, sub- = under</p>',
  'Use "transport" and "submerge" in two sentences that show their meanings.<p class="hint">Hint: trans- = across, sub- = under</p>'),
 ('1. The map showed the (principal / principle) route north.<br>2. The abolitionists had a strong (affect / effect) on public opinion.<br>3. She could not (accept / except) the idea that some people were enslaved.<br>4. They (passed / past) the safe house just before dawn.',
  '1. Source B shows (their / there) side of the story.<br>2. The raid had a strong (affect / effect) on the war.<br>3. She could not (accept / except) the idea that some people were enslaved.<br>4. The army kept (its / it’s) supplies in the commissary.'),
 ('Explain the difference between "principal" and "principle." Use each in a sentence.',
  'Explain the difference between "affect" and "effect." Use each in a sentence.'),
 ('<em>"The abolitionists excepted the risk because their principals were worth fighting for."</em>',
  '<em>"The reporter excepted the story, and it’s effect on readers was strong."</em>'),
 ('<div class="excerpt">"Account A (Primary): \'I never ran my train off the track and I never lost a passenger.\' — Harriet Tubman. Account B (Secondary): \'Tubman\'s record was remarkable — in nearly a dozen missions, she guided approximately seventy people to freedom, and not one was recaptured.\'"<div class="excerpt-source">Source: Primary and secondary source study, Week 25</div></div>',
  '<div class="excerpt"><strong>Account A:</strong> “Montgomery’s gallant band of 300 black soldiers under the guidance of a black woman, dashed into the enemies’ country… brought off near 800 slaves and thousands of dollars worth of property, without losing a man or receiving a scratch.”<div class="excerpt-source">— <em>Wisconsin State Journal</em>, June 1863, a reporter who did not name Tubman</div><br><strong>Account B:</strong> “We weakened the rebels somewhat on the Combahee River by taking and bringing away seven hundred and fifty-six head of their most valuable livestock, known up in your region as ‘contrabands,’ and this, too, without the loss of a single life on our part…”<div class="excerpt-source">— Harriet Tubman’s own words, printed by Franklin Sanborn in <em>The Commonwealth</em>, Boston, 1863</div></div>'),
 ('Why might a primary source and a secondary source give you different impressions of the same person or event, even if both are accurate? Use at least one detail from the excerpts above.',
  'Both accounts were written in 1863, but they give you different pictures of the same raid. Why? Use at least one detail from each account.'),
])

patch(CK, [
 ('The primary source shows us Tubman in her own voice — direct, confident, and certain. The secondary source steps back and measures the record. Together, they build a fuller picture than either could alone.',
  'The newspaper shows the raid from the outside — fast, dramatic, and without her name. Tubman’s letter shows it from the inside, with her own sharp humor. Together, they build a fuller picture than either could alone.'),
])
