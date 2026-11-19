#!/usr/bin/env python3
"""parent-guide-week-24.html from the week 23 guide (same look); every moment checked in Sterling Ch. 18-20.
Week 24 is the last week of the Freedom Train chapters and the end of Q3."""
import io, sys
s = io.open('parent-guide-week-23.html', encoding='utf-8').read()
def R(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: sys.exit('expected %d, found %d: %r' % (n, c, a[:80]))
    s = s.replace(a, b)

def between(start, end, new):
    global s
    i = s.index(start); j = s.index(end, i)
    s = s[:i] + new + s[j:]

# Coming Up first, so the global Week 23 -> 24 swap doesn't touch it
between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 24</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 25</h2></div>\n    <p><strong><em>Freedom Train</em>, comparing sources.</strong> The chapters are done. Next week your student reads other accounts of the Combahee River raid and sets them beside Sterling’s, and the research report gets published and presented.</p>\n  ')
s = s.replace('Week 23', 'Week 24')
R('Our Time Is Coming', 'The North Star', n=s.count('Our Time Is Coming'))
s = s.replace('Chapters 15–17', 'Chapters 18–20').replace('Ch. 15–17', 'Ch. 18–20')
R('<span class="chip">Check-In at week’s end</span>', '<span class="chip">Last week of Quarter 3</span><span class="chip">Check-In at week’s end</span>')

between('<p>Harriet’s fame spreads across the North', '</p>',
  '<p>The last three chapters. Harriet scouts behind Rebel lines and guides three Union gunboats up the Combahee River, and almost eight hundred people climb aboard. The war ends, but on the train home three men throw her into the baggage car. In Auburn she supports two freedmen’s schools, opens a home for old people, and speaks for women’s right to vote. On Day 4 your student looks back over the whole book. In Writer’s Workshop, the research report gets revised, edited and finished with a conclusion. This is the last week of the third quarter.')
between('<div class="box-label">💛 A heads-up for families</div>', ' The full list is on the <a href="parent-guide-ft-unit.html"',
  '<div class="box-label">💛 A heads-up for families</div>In Chapter 18, the Union boats burn plantations and barns and trade fire with Confederate soldiers. In Chapter 19, the Fifty-fourth Massachusetts attacks Fort Wagner, President Lincoln is shot, and Harriet is hurt when three men drag her into the baggage car. In Chapter 20, Harriet’s first husband, John Tubman, is shot in an argument, and the book ends with Harriet’s death in 1913. The book uses the words of its time, such as “master,” “contrabands” and “Negro.” Reading together, or checking in after each chapter, helps.')
R('<strong>The author’s perspective.</strong> Your student looks at how Dorothy Sterling feels about Harriet: the words she chooses, the moments she gives the most pages to, the difference between a fact and her opinion of it, and what another person telling the same story might leave out.',
  '<strong>How details support the central idea.</strong> Your student says a chapter’s big idea in one sentence, gathers details that prove it, and sets aside the ones that don’t. On Day 4 the same move covers the whole book: one moment from the beginning, one from the middle, one from the end.')
R('<strong>Free, but not yet all the way free.</strong> In Beaufort, people who have escaped say “We’s all free,” but a soldier says they are only half free until they have land and fair pay. On January 1, 1863, freedom is promised.',
  '<strong>Victory is real, but the work isn’t finished.</strong> The war is won and slavery ends, but Harriet is still thrown off a train seat and still waiting for her pay. She keeps working for freedom for the rest of her life.')
R('<p class="quote">“This is the first day we have ever had a country.”<small>Harriet, Chapter 17</small></p>',
  '<p class="quote">“It was dusk, and the North Star was shining in the darkening sky, when her eyes closed for the last time.”<small>The last sentence of <em>Freedom Train</em>, Chapter 20</small></p>')

rows = '''        <tr>
          <td class="day-n">24.1<span>Day 1</span></td>
          <td><span class="ch">Chapter 18 · Mr. Lincoln’s Army</span><br>General Hunter sends Harriet behind enemy lines to scout. Then she guides three gunboats up the Combahee River, past the hidden torpedoes. People run to the riverbanks, and almost eight hundred climb aboard the “Lincoln boats.” When frightened hands hold the rowboats back, Harriet sings them a song.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-extra">Copywork in Harriet’s words</span><span class="pill p-extra">Harriet’s Song on the River</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>Which details does Sterling choose to show you what that night meant?</td>
        </tr>
        <tr>
          <td class="day-n">24.2<span>Day 2</span></td>
          <td><span class="ch">Chapter 19 · Victory</span><br>Harriet goes home on furlough, then runs a hospital at Fortress Monroe. Lee surrenders, and Lincoln is shot. On the train home, three men throw her into the baggage car, even though she holds a War Department pass.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-poem">By Heart poem</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>What does victory really mean, and who gets to have it?</td>
        </tr>
        <tr>
          <td class="day-n">24.3<span>Day 3</span></td>
          <td><span class="ch">Chapter 20 · The Years of Peace</span><br>Back in Auburn, Harriet sells vegetables and chickens to support two freedmen’s schools, marries Nelson Davis, gets a letter from Queen Victoria, and buys twenty-five acres for a home for old people. The book ends with the North Star.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-extra">Read · Write · Mimic: the last sentence</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>What does Harriet keep doing when nobody is watching anymore?</td>
        </tr>
        <tr>
          <td class="day-n">24.4<span>Day 4</span></td>
          <td><span class="ch">The whole book · looking back</span><br>No new chapter. Your student flips back to find one moment from the beginning, one from the middle and one from the end, checks that they point to the same big idea, and holds Chapter 1 beside the last page.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-poem">By Heart poem</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>What does Harriet’s life mean, taken all together?</td>
        </tr>
'''
i = s.index('        <tr>\n          <td class="day-n">23.1'); j = s.index('        <tr class="extra-row">', i)
s = s[:i] + rows + s[j:]
R('A passage from Chapter 15, where John Brown writes to his son about Harriet.',
  'A passage from Chapter 19, where Harriet’s father, Ben, says he is proud of her: “Did the Lord pay Moses for leading His children out of Egypt?”')
R('A 14-point wrap-up on the week: comparative adverbs, word parts and vocabulary, schwa and stress in long words, reading questions about Sterling’s perspective, and a fact-plus-meaning sentence to write.',
  'A 14-point wrap-up on the whole book: prepositional phrases, word parts and vocabulary, suffix spelling rules, the book’s central idea and the details that support it, a concluding sentence, and a final reflection.')
between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>fortifications</b><span>walls and defenses built to protect a place</span></div><div class="word"><b>furlough</b><span>time off from duty to go home for a while</span></div><div class="word"><b>pension</b><span>a regular payment to a veteran or a retired worker</span></div><div class="word"><b>temperance</b><span>the movement to cut down on or ban alcohol</span></div></div>\n    ')
R('<strong>lev</strong> means “lift.” <strong>sist</strong> means “stand.”<span class="eg">elevate · lever · resist · persist</span>',
  'A year-end review: <strong>port</strong> (carry), <strong>rupt</strong> (break), <strong>struct</strong> (build), <strong>dict</strong> (say), then <strong>pens</strong> (pay), <strong>fid</strong> (trust) and <strong>lect</strong> (choose).<span class="eg">transport · erupt · pension · confident · elect</span>')
R('<strong>Schwa and stress.</strong> In a long word, a vowel in a quiet syllable fades to “uh.” To spell it, say a related word where that syllable is loud.<span class="eg">abolition → abolish · definition → define</span>',
  '<strong>The year’s suffix rules.</strong> Double the last letter after a short vowel, drop a silent e, change y to i. The end of the base word tells you which rule to use.<span class="eg">stop → stopping · bake → baking · cry → cried</span>')
R('<strong>Comparative adverbs</strong> compare how two things were done. Short ones take -er; most -ly ones take more. Never both.<span class="eg">ran faster · listened more carefully · not “more louder”</span>',
  '<strong>Prepositional phrases</strong> start with a word like in, on, under or through and end with a noun. They tell where, when or how. Too many in one sentence bury the verb.<span class="eg">in the baggage car · through the woods · before dawn</span>')
R('The third-quarter lesson pages work the same way as last week. This week’s extras:',
  'The lesson pages work the same way as last week. This week’s extras:')
R('A short job at the end of the Reading tab: one sentence on Day 1, a sort on Day 2 (“moving freedom forward, or holding it back?”), a log on Day 3, and a slider on Day 4. Every moment in it is taken from the book.',
  'A short job at the end of the Reading tab: one sentence on Day 1, a sort on Day 2 (“a real victory, or not finished yet?”), a log on Day 3, and a slider on Day 4 that looks at the whole book. Every moment in it is taken from the book.')
between('<div class="box b-plum"><div class="box-label">🧵', '<div class="box b-rose"><div class="box-label">🎧',
  '<div class="box b-plum"><div class="box-label">🧵 Sew the Quilt</div>The word-parts game closes out the year: on Day 1 the roots from all year (port, rupt, struct, dict), and on Day 3 this week’s (pens, fid, lect). Four patches a day.</div>\n      <div class="box b-green"><div class="box-label">🎵 Harriet’s Song on the River</div>On Day 1, the card shows “Come Along,” the song Harriet sings on the Combahee when frightened people won’t let go of the rowboats. At the end of each verse they throw up their hands and shout “Glory!”, and the oarsmen push off.</div>\n      ')
R('<div class="box b-sky"><div class="box-label">✎ Copia: Say It Three Ways</div>On Day 1, your student rewrites “Harriet told her story to the crowd” three ways: a new opening, a stronger verb, and an added detail.</div>',
  '<div class="box b-sky"><div class="box-label">✍️ Copywork and the last sentence</div>On Day 1, your student copies Harriet’s own words about the raid: “The women had bags on their shoulders, baskets on their heads, and young ones tagging behind, all loaded.” On Day 3, they study the book’s last sentence and write one built the same way.</div>')
R('<span class="done">Wk 22 · Draft</span><span class="now">Wk 23 · Add facts and examples</span><span>Wk 24 · Revise and edit</span>',
  '<span class="done">Wk 22 · Draft</span><span class="done">Wk 23 · Add facts and examples</span><span class="now">Wk 24 · Revise, edit, conclude</span>')
between('<p>This week your student makes the draft stronger', '</p>',
  '<p>This week your student polishes the report. Day 1: read it out loud and fix at least two sentences that sound wrong. Sam, the example writer, hears “Tubman sang song say goodbye to her family” and fixes it to “Tubman sang a song to say goodbye to her family.” Day 2: a four-pass edit (prepositional phrases, vague words, run-ons, and an ending that answers the question). Day 4: a three-part conclusion that restates the main idea, sums up the best evidence and ends with a lasting thought. Each day’s work goes into <strong>My Research Report</strong>.')
R('<p>On Days 2 and 4 your student practices the same four lines, with a little less help on the screen each time. The whole poem, read aloud, is still a tap away.</p>',
  '<p>On Days 2 and 4 your student practices the same four lines for the last time in this unit. By Day 4 they should be able to say them with almost no help on the screen.</p>')
R('Then ask how the caged bird’s song is like the song the crowd sings on January 1, 1863, and how it is different.',
  'Then ask whether the caged bird ever gets free, and whether Harriet does.')
between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">What did Harriet do on the Combahee River?</span><span class="listen">Listen for: she scouted first, then guided three gunboats up the river past the torpedoes, and almost eight hundred people came aboard.</span></li><li><span class="q">Why did Colonel Montgomery ask Harriet for a song?</span><span class="listen">Listen for: frightened people held on to the rowboats so they couldn’t push off. Her song calmed them, they shouted “Glory!”, and the boats got away.</span></li><li><span class="q">Why was Harriet’s mother upset when she came home on furlough?</span><span class="listen">Listen for: Harriet had been gone too long and had no pay to show for it. Her father, Ben, said he was proud of her.</span></li><li><span class="q">What happened on the train ride home?</span><span class="listen">Listen for: the conductor and three men threw her into the baggage car, even with her War Department pass. The war was won, but she still wasn’t treated as an equal.</span></li><li><span class="q">What did Harriet do in Auburn after the war?</span><span class="listen">Listen for: one of these: supported two freedmen’s schools by selling vegetables and chickens, took in guests who were old or sick, bought land for a home for old people, spoke for women’s right to vote.</span></li><li><span class="q">How does the book end, and how does it connect to Chapter 1?</span><span class="listen">Listen for: the North Star is shining when Harriet dies. In Chapter 1, her father showed her that same star.</span></li>')
R('<strong>Research report:</strong> one stronger body paragraph a day: an extra fact, exact details, a quote, then all three',
  '<strong>Research report:</strong> two fixed sentences, a four-pass edit, and a finished conclusion')
R('<strong>Fluency:</strong> a recording of a passage from Chapter 15', '<strong>Fluency:</strong> a recording of a passage from Chapter 19')
R('chapter answers that say what Sterling thinks of Harriet and point to the exact word or moment that shows it.',
  'an answer that states the book’s big idea in one sentence and backs it with details from the beginning, the middle and the end.')
between('<ul class="check"><li><strong>Find Beaufort, South Carolina</strong>', '</ul>',
  '<ul class="check"><li><strong>Look at the North Star together</strong> on a clear night (find the Big Dipper and follow the two stars at the end of its bowl), and talk about why Sterling ends the book with it.</li><li><strong>Ask your student to tell Harriet’s whole life in one minute</strong>: beginning, middle and end.</li><li><strong>Find Auburn, New York</strong> on a map, and the Combahee River in South Carolina.</li>')
R('Optima Academy Online · 4th Grade ELA · Week 24 Family Guide', 'Optima Academy Online · 4th Grade ELA · Week 24 Family Guide · End of Quarter 3')
io.open('parent-guide-week-24.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('Week 23'), s.count('Week 24'), s.count('Week 25'))
