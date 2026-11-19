#!/usr/bin/env python3
"""lesson-25-fluency: the 'dictated account' passage was really an adaptation of the newspaper report (Source A) with an
invented closing line, and its epigraph was not Tubman's. Now: Tubman's own words from her 1863 letter (printed by
Sanborn; reprinted in Bradford 1869), unchanged."""
import io, sys
p = 'lesson-25-fluency.html'; s = io.open(p, encoding='utf-8', newline='').read()
L = "We weakened the rebels somewhat on the Combahee River by taking and bringing away seven hundred and fifty-six head of their most valuable livestock, known up in your region as &lsquo;contrabands,&rsquo; and this, too, without the loss of a single life on our part, though we had good reasons to believe that a number of rebels bit the dust. Of these seven hundred and fifty-six contrabands, nearly or quite all the able-bodied men have joined the colored regiments here."
R = [
 ('<div class="info-detail">Tubman&rsquo;s Dictated Account</div>', '<div class="info-detail">Tubman&rsquo;s Own Letter, 1863</div>'),
 ('&ldquo;They destroyed stores of cotton and rice, and brought away nearly eight hundred people who had been enslaved.&rdquo;',
  '&ldquo;We weakened the rebels somewhat on the Combahee River&hellip;&rdquo;'),
 ('&mdash; Harriet Tubman, as told to Franklin Sanborn, <em>The Commonwealth</em>, 1863', '&mdash; Harriet Tubman, in a letter printed by Franklin Sanborn, 1863'),
 ('Your fluency passage comes from Tubman&rsquo;s own dictated account of the raid &mdash; adapted slightly for practice. Read her words with the strength and pride she spoke them.',
  'Your fluency passage is Tubman&rsquo;s own account of the raid, from a letter she dictated in 1863. Read her words with the strength, pride and dry humor she spoke them with.'),
 ('From Tubman&rsquo;s dictated account of the Combahee River Raid (adapted)', 'Harriet Tubman&rsquo;s own words about the Combahee River Raid'),
 ('Colonel Montgomery and his gallant band of soldiers dashed into the enemy&rsquo;s country. They struck a bold and effective blow. They destroyed stores of cotton and rice, and brought away nearly eight hundred people who had been enslaved. All of this was accomplished without the loss of a single life on our side. Harriet Tubman planned and led this daring raid.', L),
 ('This passage is adapted from Tubman&rsquo;s account as told to Franklin Sanborn and published in <em>The Commonwealth</em>, 1863. Read with steady confidence &mdash; these are the words of someone describing a great victory. Let your voice build through the passage, reaching its strongest on the final sentence.',
  'Tubman could not write, so she dictated this letter to a friend, and Franklin Sanborn printed it in <em>The Commonwealth</em> in 1863. Read with steady confidence. She calls free people &ldquo;livestock&rdquo; on purpose, to mock the slaveholders, so let a little of that dry humor into your voice.'),
]
for a, b in R:
    if s.count(a) != 1: sys.exit('not found once: ' + a[:70])
    s = s.replace(a, b)
io.open(p, 'w', encoding='utf-8', newline='').write(s); print('ok')
