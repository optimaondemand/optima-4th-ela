#!/usr/bin/env python3
"""parent-guide-week-23.html from the week 22 guide (same look); every moment checked in Sterling Ch. 15-17."""
import io, re, sys
s = io.open('parent-guide-week-22.html', encoding='utf-8').read()
def R(a, b, n=1):
    global s
    c = s.count(a)
    if c != n: sys.exit('expected %d, found %d: %r' % (n, c, a[:80]))
    s = s.replace(a, b)

def between(start, end, new):
    global s
    i = s.index(start); j = s.index(end, i)
    s = s[:i] + new + s[j:]

s = s.replace('Coming Up in Week 23', 'Coming Up in Week 24').replace('Week 22', 'Week 23')
R('Why Not Every Man?', 'Our Time Is Coming', n=s.count('Why Not Every Man?'))
s = s.replace('Chapters 10–14', 'Chapters 15–17').replace('Ch. 10–14', 'Ch. 15–17')

between('<p>Harriet is free, but her family is not', '</p>',
  '<p>Harriet’s fame spreads across the North. She speaks at antislavery meetings, helps a crowd rescue a captured runaway named Charles Nalle, and plans with John Brown, who calls her “General Tubman.” Then the Civil War begins. Harriet sails south to Beaufort, South Carolina, where thousands of people have escaped to the Union army. She nurses the sick, teaches freedwomen to earn a living, and is there on January 1, 1863, when the Emancipation Proclamation is read aloud. In Writer’s Workshop, your student makes the research report stronger with more facts, exact names and numbers, and a quote.')
between('<div class="box-label">💛 A heads-up for families</div>', ' The full list is on the <a href="parent-guide-ft-unit.html"',
  '<div class="box-label">💛 A heads-up for families</div>In Chapter 15, a fight breaks out in Troy, New York, when a crowd frees Charles Nalle from the police: people are clubbed, and one man is struck with a hatchet. John Brown leads an armed raid on Harpers Ferry and is hanged. In Chapter 17, Harriet nurses soldiers with wounds, fever and smallpox. The book uses the words of its time, such as “master,” “contrabands” and “Negro.” Reading together, or checking in after each chapter, helps.')
R('<strong>Cause and effect in history.</strong> Your student names what made something happen, follows a chain of causes, tests whether an event really caused the next one or only came first, and decides which cause mattered most.',
  '<strong>The author’s perspective.</strong> Your student looks at how Dorothy Sterling feels about Harriet: the words she chooses, the moments she gives the most pages to, the difference between a fact and her opinion of it, and what another person telling the same story might leave out.')
R('<strong>Freedom for one is not enough.</strong> Harriet could stay safe. Instead she goes back again and again, because her people are still enslaved.',
  '<strong>Free, but not yet all the way free.</strong> In Beaufort, people who have escaped say “We’s all free,” but a soldier says they are only half free until they have land and fair pay. On January 1, 1863, freedom is promised.')
R('<p class="quote">“My people must go free.”<small>Harriet, Chapter 10</small></p>',
  '<p class="quote">“This is the first day we have ever had a country.”<small>Harriet, Chapter 17</small></p>')

rows = '''        <tr>
          <td class="day-n">23.1<span>Day 1</span></td>
          <td><span class="ch">Chapter 15 · “The Most of a Man”</span><br>Harriet speaks at meetings across the North and helps a crowd free Charles Nalle in Troy. John Brown plans with her in Canada, calls her General Tubman, and writes that she is “the most of a man” he ever met. Brown’s raid on Harpers Ferry fails, and soon the Civil War begins.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-extra">Copia: Say It Three Ways</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>How does Sterling want you to see Harriet, and how can you tell?</td>
        </tr>
        <tr>
          <td class="day-n">23.2<span>Day 2</span></td>
          <td><span class="ch">Chapter 16 · Department of the South</span><br>Harriet sails to Beaufort, South Carolina. She tells General Hunter the war can’t be won “by half measures,” with a story about a snake, and he puts her to work with the people who have escaped to the Union lines.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-poem">By Heart poem</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>What can Harriet do in Beaufort that nobody else can?</td>
        </tr>
        <tr>
          <td class="day-n">23.3<span>Day 3</span></td>
          <td><span class="ch">Chapter 16 again · a close read</span><br>Back to Harriet’s talk with General Hunter, pages 152–155, to sort facts anyone could check from what Sterling believes about them. Then the campfire, where a soldier says they are only half free.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>Which parts are facts, and which tell you what Sterling believes?</td>
        </tr>
        <tr>
          <td class="day-n">23.4<span>Day 4</span></td>
          <td><span class="ch">Chapter 17 · “Our Time Is Coming”</span><br>Harriet nurses the sick, brews herb tea for a fever ward in Florida, and builds a washhouse so freedwomen can earn money. On January 1, 1863, the Emancipation Proclamation is read in a grove outside Beaufort.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-poem">By Heart poem</span><span class="pill p-extra">A Song That Changed Its Meaning</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>What does it feel like to be this close to something you’ve waited your whole life for?</td>
        </tr>
'''
i = s.index('        <tr>\n          <td class="day-n">22.1'); j = s.index('        <tr class="extra-row">', i)
s = s[:i] + rows + s[j:]
R('A passage from Chapter 14, where Harriet says she never lost a passenger.',
  'A passage from Chapter 15, where John Brown writes to his son about Harriet.')
R('A 14-point wrap-up on the week: adverbs, word parts and vocabulary, -ive/-al/-ic spelling, reading questions about cause and effect, and a short cause-and-effect sentence to write.',
  'A 14-point wrap-up on the week: comparative adverbs, word parts and vocabulary, schwa and stress in long words, reading questions about Sterling’s perspective, and a fact-plus-meaning sentence to write.')
between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>elevate</b><span>to lift up; to raise to a higher level</span></div><div class="word"><b>resist</b><span>to stand against; to refuse to give in</span></div><div class="word"><b>persist</b><span>to keep going; to refuse to stop</span></div><div class="word"><b>abolitionist</b><span>a person who worked to end slavery</span></div></div>\n    ')
R('<strong>press</strong> means “push.” <strong>tain</strong> means “hold.”<span class="eg">express · impress · contain · obtain</span>',
  '<strong>lev</strong> means “lift.” <strong>sist</strong> means “stand.”<span class="eg">elevate · lever · resist · persist</span>')
R('<strong>The suffixes -ive, -al and -ic</strong> turn a word into a describing word. Sometimes a letter drops first, like a silent e.<span class="eg">act → active · music → musical · hero → heroic</span>',
  '<strong>Schwa and stress.</strong> In a long word, a vowel in a quiet syllable fades to “uh.” To spell it, say a related word where that syllable is loud.<span class="eg">abolition → abolish · definition → define</span>')
R('<strong>Adverbs</strong> tell how, when or where something happens. A strong verb can often do the job of two adverbs, and some adverbs add nothing at all.<span class="eg">moved quietly · came back again · waited outside</span>',
  '<strong>Comparative adverbs</strong> compare how two things were done. Short ones take -er; most -ly ones take more. Never both.<span class="eg">ran faster · listened more carefully · not “more louder”</span>')
R('Week 23 is part of the third quarter, so the lesson pages work a little differently from here on. Look for these:',
  'The third-quarter lesson pages work the same way as last week. This week’s extras:')
R('The Freedom Watch is now a short job at the end of the Reading tab: one sentence on Day 1, a sort on Day 2 (“helping someone get free, or not?”), a log on Day 3, and a slider on Day 4. Every moment in it is taken from the book.',
  'A short job at the end of the Reading tab: one sentence on Day 1, a sort on Day 2 (“moving freedom forward, or holding it back?”), a log on Day 3, and a slider on Day 4. Every moment in it is taken from the book.')
R('such as “Pick the event” or “Ask why,”', 'such as “Pick the event” or “Ask why,”')
between('<div class="box b-plum"><div class="box-label">🧵', '<div class="box b-rose"><div class="box-label">🎧',
  '<div class="box b-plum"><div class="box-label">🧵 Sew the Quilt</div>The word-parts game goes on with new roots, <strong>lev</strong> (lift) and <strong>sist</strong> (stand). It is tied to the flag a woman in the Beaufort camp pieces together from scraps of old clothing in Chapter 16. Four patches a day.</div>\n      <div class="box b-green"><div class="box-label">🎵 A Song That Changed Its Meaning</div>On Day 4, the card shows “My Country, ’Tis of Thee,” the song the crowd sings on January 1, 1863. Most of them had never been included in its “land of liberty.” That morning, Harriet says, “This is the first day we have ever had a country.”</div>\n      ')
R('Two clips from Marcus in every lesson, a welcome and what to notice before reading, plus a short clip on the Word Study tab about the day’s word work.',
  'Two clips from Marcus in every lesson, a welcome and what to notice before reading, plus a short film on the Word Study tab about the day’s word work.')
R('On Day 1, your student rewrites “Harriet led her people north” three ways: a new opening, a stronger verb, and a where or a how.',
  'On Day 1, your student rewrites “Harriet told her story to the crowd” three ways: a new opening, a stronger verb, and an added detail.')
R('<span class="done">Wk 21 · Gather notes</span><span class="now">Wk 22 · Draft</span><span>Wk 23 · Add facts and examples</span>',
  '<span class="done">Wk 21 · Gather notes</span><span class="done">Wk 22 · Draft</span><span class="now">Wk 23 · Add facts and examples</span>')
between('<p>This week your student starts drafting', '</p>',
  '<p>This week your student makes the draft stronger, one move a day. Day 1: add one more fact to each body paragraph. Day 2: swap vague words for exact names, dates and numbers. Day 3: add a short quote, set up and explained (a “quote sandwich”). Day 4: rewrite one body paragraph with all three moves. Sam, the example writer, uses songs Harriet really sang in <em>Freedom Train</em>, with page numbers. Each day’s work goes into <strong>My Research Report</strong>.')
R('Then ask how Harriet is like the caged bird this week, and how she is different by the end.',
  'Then ask how the caged bird’s song is like the song the crowd sings on January 1, 1863, and how it is different.')
between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">What did John Brown call Harriet, and why?</span><span class="listen">Listen for: “General Tubman.” He was so impressed by her courage and leadership that he wrote she was “the most of a man” he ever met.</span></li><li><span class="q">How did Harriet help free Charles Nalle?</span><span class="listen">Listen for: she slipped past the guards, sent boys to ring the fire bell for a bigger crowd, and held on to Nalle through the fight until he got away to Canada.</span></li><li><span class="q">What was Harriet’s snake story about?</span><span class="listen">Listen for: treating each bite won’t help while the snake keeps biting. The snake is slavery; Mr. Lincoln has to set the slaves free.</span></li><li><span class="q">Why did a soldier say they were only “half free”?</span><span class="listen">Listen for: they had escaped, but they still had no land to farm and no soldier’s pay.</span></li><li><span class="q">What happened on January 1, 1863?</span><span class="listen">Listen for: the Emancipation Proclamation was read aloud, everyone sang “My country, ’tis of thee,” and Harriet said it was the first day they ever had a country.</span></li><li><span class="q">How does Dorothy Sterling feel about Harriet? How can you tell?</span><span class="listen">Listen for: she admires her, and a word or moment from the book that shows it.</span></li>')
R('<strong>Each lesson:</strong> 3 chapter questions (4 on Day 2) plus word-study and writing responses, submitted in Canvas',
  '<strong>Each lesson:</strong> 3 chapter questions plus word-study and writing responses, submitted in Canvas')
R('<strong>Research report draft:</strong> a thesis, an introduction, and two body paragraphs, added one a day',
  '<strong>Research report:</strong> one stronger body paragraph a day: an extra fact, exact details, a quote, then all three')
R('<strong>Fluency:</strong> a recording of a passage from Chapter 14', '<strong>Fluency:</strong> a recording of a passage from Chapter 15')
R('chapter answers that name a cause and its effect, using words like because, so and as a result, with details from the book.',
  'chapter answers that say what Sterling thinks of Harriet and point to the exact word or moment that shows it.')
between('<ul class="check"><li><strong>Trace the route to Canada</strong>', '</ul>',
  '<ul class="check"><li><strong>Find Beaufort, South Carolina</strong> on a map, and trace Harriet’s trip there by sea from New York.</li><li><strong>Read the first lines of the Emancipation Proclamation</strong> together, and ask your student who it freed and who it did not free yet.</li><li><strong>Sing “My Country, ’Tis of Thee”</strong> and talk about why it sounded different to the crowd in Beaufort.</li>')
between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 24</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 24</h2></div>\n    <p><strong><em>Freedom Train</em>, Chapters 18–20.</strong> Harriet scouts behind enemy lines and guides the Union gunboats up the Combahee River, the war ends, and she goes home to Auburn. Your student revises and edits the research report, and the unit ends with a look back at the whole book.</p>\n  ')
io.open('parent-guide-week-23.html', 'w', encoding='utf-8').write(s)
g = io.open('parent-guide-week-22.html', encoding='utf-8').read()
a = 'The Civil War begins, and Harriet goes south again, this time to help the Union Army as a nurse, scout and spy.'
if a in g:
    g = g.replace(a, 'The Civil War begins, and Harriet goes south again, this time to work for the Union Army in South Carolina.')
    io.open('parent-guide-week-22.html', 'w', encoding='utf-8').write(g)
print('ok', s.count('Week 22'), s.count('Week 23'))
