#!/usr/bin/env python3
"""parent-guide-week-25.html from the week 24 guide (same look). Week 25 = Freedom Train, comparing three accounts of the
Combahee River Raid (no new chapters). Every source checked: Wisconsin State Journal (June 1863), Tubman's dictated letter
(The Commonwealth, 1863; reprinted in Bradford 1869), Sarah Bradford's Scenes in the Life of Harriet Tubman (1869)."""
import io, re, sys
s = io.open('parent-guide-week-24.html', encoding='utf-8').read()
s = s.replace("Freedom Train Ch. 18–20 · 4th Grade ELA</title>", "Freedom Train: Comparing Sources · 4th Grade ELA</title>")
def between(start, end, new, after=0):
    global s
    i = s.index(start, after); j = s.index(end, i + len(start))
    s = s[:i] + new + s[j:]
def sec(head_text, new_inner):
    """replace the whole <section> whose card-head contains head_text (keeps the <section ...> tag)"""
    global s
    k = s.index(head_text); i = s.rindex('<section', 0, k); i = s.index('>', i) + 1; j = s.index('</section>', k)
    s = s[:i] + new_inner + s[j:]

between('<h1>', '</h1>', '<h1>Week 25: Who Tells the Story?')
between('<div class="sub">', '</div>', '<div class="sub"><em>Freedom Train</em> wrap-up: three real accounts of the Combahee River Raid')
between('<div class="chips">', '</div>', '<div class="chips">\n        <span class="chip">4 lessons</span>\n        <span class="chip">1 fluency recording</span>\n        <span class="chip">No new chapters</span>\n        <span class="chip">Last week of the unit</span>\n        <span class="chip">Check-In at week’s end</span>\n      ')
s = s.replace('Week 24', 'Week 25').replace(' · End of Quarter 3', '')

AT = '''
    <div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
    <p>The biography is finished, so this week your student reads history the way people first read it. On the night of June 1–2, 1863, Harriet Tubman guided Union gunboats up the Combahee River in South Carolina, and more than 700 enslaved people were freed. Your student reads three real accounts of that night: a newspaper report that never names her, a letter she dictated herself, and a book written six years later. Day by day they compare what each writer tells, leaves out, and why. In Writer’s Workshop, the research report is revised, edited, published and presented, one step a day.</p>
    <div class="box b-rose" style="margin-bottom:12px;"><div class="box-label">💛 A heads-up for families</div>These are real documents from 1863, so they use the words of their time, such as “slaves” and “contrabands.” In her own letter, Tubman calls the people she freed “livestock” on purpose, to mock how slaveholders talked about human beings; the lessons explain this. The accounts mention burning plantations and fighting. The full list is on the <a href="parent-guide-ft-unit.html" style="color:#A8434A;font-weight:700;">unit guide</a>.</div>
    <div class="glance">
      <div class="box b-sky"><div class="box-label">Reading skill</div><strong>Comparing accounts of the same event.</strong> Your student reads each account on its own, finds one fact in every source and sets the versions side by side, asks who was close to the event and who wrote later, and finally picks the account they would lean on and says why.</div>
      <div class="box b-green"><div class="box-label">Big idea</div><strong>Who tells the story matters.</strong> One newspaper called Harriet only “a black woman.” Her own letter, printed weeks later, shows her voice and her humor. Reading more than one account gives a fuller, truer picture.</div>
    </div>
    <p class="quote">“We weakened the rebels somewhat on the Combahee River…”<small>Harriet Tubman, in a letter she dictated in 1863</small></p>
  '''
sec('This Week at a Glance', AT)

rows = '''        <tr>
          <td class="day-n">25.1<span>Day 1</span></td>
          <td><span class="ch">Two accounts of one night</span><br>Source A, a newspaper report from June 1863, praises the raid but never names Harriet. Source B is her own dictated letter. Your student lists what only each one tells.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-extra">Copia: Say It Three Ways</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>Why does it matter who tells a story?</td>
        </tr>
        <tr>
          <td class="day-n">25.2<span>Day 2</span></td>
          <td><span class="ch">A third source</span><br>Source C, Sarah Bradford’s 1869 book about Harriet, joins the first two. A side-by-side table shows who wrote each one, when, and how many people each says were freed.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-poem">By Heart poem</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>When writers tell the same story differently, what can we learn from the differences?</td>
        </tr>
        <tr>
          <td class="day-n">25.3<span>Day 3</span></td>
          <td><span class="ch">Putting it together</span><br>Your student sorts the writers: who was close to the raid, and who wrote later? Then they write what three accounts show that one alone could not, and study Harriet’s own sentence in Read · Write · Mimic.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>What do you understand now that you could never have understood from just one source?</td>
        </tr>
        <tr>
          <td class="day-n">25.4<span>Day 4</span></td>
          <td><span class="ch">Choosing an account</span><br>Your student picks the account they would trust most about that night, says why, and names one thing none of the sources can tell. Then they present their research report.<br><span class="pill p-guide">Guide: Marcus</span><span class="pill p-poem">By Heart poem</span><span class="pill p-extra">Freedom Watch</span></td>
          <td>What have you learned about how different writers tell the same story, and why it matters?</td>
        </tr>
'''
i = s.index('        <tr>\n          <td class="day-n">24.1'); j = s.index('        <tr class="extra-row">', i)
s = s[:i] + rows + s[j:]
between('<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">', ' Your student reads it three times',
        '<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">Harriet Tubman’s own letter about the raid, word for word.')
between('<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">', '</td>',
        '<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">A 14-point wrap-up: commas in a series, prefixes that tell where, words that sound alike, and questions comparing the newspaper report with Harriet’s own letter.')

between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>gallant</b><span>brave and noble</span></div><div class="word"><b>commissary</b><span>a place where an army keeps its food and supplies</span></div><div class="word"><b>rebeldom</b><span>the Confederate states; the land of the rebellion</span></div><div class="word"><b>contraband</b><span>the Union army’s word for people who escaped slavery to its lines</span></div></div>\n    ')
between('<div class="box b-sky"><div class="box-label">Word parts</div>', '</div>\n      <div class="box b-gold">',
  '<div class="box b-sky"><div class="box-label">Word parts</div>Prefixes that tell <em>where</em>: <strong>trans-</strong> (across), <strong>inter-</strong> (between), <strong>sub-</strong> (under), <strong>super-</strong> (above, beyond).<span class="eg">transportation · international · submarine · supernatural</span>')
between('<div class="box b-gold"><div class="box-label">Spelling</div>', '</div>\n      <div class="box b-green">',
  '<div class="box b-gold"><div class="box-label">Spelling</div><strong>Words that sound alike.</strong> A spellchecker misses them because they are real words. Say the long form out loud to check.<span class="eg">affect / effect · its / it’s · their / there / they’re · accept / except</span>')
between('<div class="box b-green"><div class="box-label">Grammar</div>', '</div>\n    </div>',
  '<div class="box b-green"><div class="box-label">Grammar</div><strong>Commas in a series</strong> separate three or more things in a list, including the comma before <em>and</em>, so the reader knows where each one stops.<span class="eg">bread, cheese, and a knife</span>')

EX = '''
    <div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
    <p>The lesson pages work the same way as last week. This week’s extras:</p>
    <div class="extras">
      <div class="box b-gold"><div class="box-label">⭐ Freedom Watch, after reading</div>The moments now come from the real 1863 accounts: one sentence on Day 1 about Harriet’s own words, a sort on Day 2 (“moving freedom forward, or holding it back?”), a log on Day 3, and a slider on Day 4: how much does it matter who gets to tell the story?</div>
      <div class="box b-sky"><div class="box-label">🔍 Reading lens</div>Before reading the sources, your student picks one of three lenses and reads through it. One line at the end of the questions asks what the lens helped them notice.</div>
      <div class="box b-plum"><div class="box-label">🧵 Sew the Border</div>The quilt was finished last week. On Days 1 and 3, the word-parts game sews its border with four prefixes that tell where: <strong>trans-</strong>, <strong>inter-</strong>, <strong>sub-</strong> and <strong>super-</strong>.</div>
      <div class="box b-green"><div class="box-label">🖼️ The raid in pictures</div>The Combahee River picture from Chapter 18 sits at the top of Days 1–3, and Harriet’s porch in Auburn closes the unit on Day 4.</div>
      <div class="box b-rose"><div class="box-label">🎬 Word Study films</div>A short film on the Word Study tab each day, with captions, about the day’s word work.</div>
      <div class="box b-sky"><div class="box-label">✎ Copia: Say It Three Ways</div>On Day 1, your student rewrites “The newspaper left out her name” three ways: a new opening, a stronger verb, and an added detail.</div>
    </div>
  '''
sec('New in the Lessons', EX)

between('<div class="essay">', '</div>',
  '<div class="essay"><span class="done">Wk 20 · Choose a question</span><span class="done">Wk 21 · Gather notes</span><span class="done">Wk 22 · Draft</span><span class="done">Wk 23 · Add facts and examples</span><span class="done">Wk 24 · Revise, edit, conclude</span><span class="now">Wk 25 · Publish and present</span>')
k = s.index('Your Student’s Research Report')
between('<p>', '</p>',
  '<p>The report is finished this week, one step a day. Day 1: make two changes that strengthen the ideas, order or word choice. Day 2: an editing pass for capitals, end marks, commas in a series and words that sound alike. Day 3: a clean, final copy. Day 4: your student presents it aloud, to you or on a recording, and picks one picture to show at the most important sentence. Each day’s work goes into <strong>My Research Report</strong>.', after=k)

between('<p>On Days 2 and 4 your student practices', '</p>',
  '<p>On Days 2 and 4 your student says the four lines again. By now they should know them by heart.')
between('<p><strong>How to help:</strong>', '</p>',
  '<p><strong>How to help:</strong> Ask your student to say the lines to you without looking. Then ask why Dunbar never names the bird’s cage, and why one 1863 newspaper never named Harriet.')

between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">What happened on the Combahee River?</span><span class="listen">Listen for: Harriet guided Union gunboats up the river at night, and more than 700 enslaved people were freed.</span></li><li><span class="q">What did the newspaper call Harriet instead of her name?</span><span class="listen">Listen for: “a black woman,” and a “she-Moses.”</span></li><li><span class="q">Why did Harriet call the people she freed “livestock” in her letter?</span><span class="listen">Listen for: she was mocking the slaveholders, who treated people as property.</span></li><li><span class="q">Which account would you trust most about that night? Why?</span><span class="listen">Listen for: a reason about who wrote it, when, and how close they were.</span></li><li><span class="q">What is one thing none of the sources can tell us?</span><span class="listen">Listen for: anything the writers could not see or know, such as what one freed person felt.</span></li><li><span class="q">Harriet could not read or write. How did her own words get printed?</span><span class="listen">Listen for: she dictated her letter, and Franklin Sanborn printed it.</span></li>')

between('<ul class="check"><li><strong>Each lesson:</strong>', '</ul>',
  '<ul class="check"><li><strong>Each lesson:</strong> 3 or 4 source questions plus word-study and writing responses, submitted in Canvas</li><li><strong>Research report:</strong> revised, edited, published, and presented with one visual</li><li><strong>Fluency:</strong> a recording of Harriet Tubman’s own letter about the raid</li><li><strong>Check-In:</strong> at the end of the week</li>')
between('<strong>Done well looks like:</strong>', '</p>',
  '<strong>Done well looks like:</strong> answers that name which source a detail comes from and explain why the difference between the accounts matters.')
between('<ul class="check"><li><strong>Look at the North Star', '</ul>',
  '<ul class="check"><li><strong>Tell the same story two ways.</strong> You and your student each describe one family event, then compare: what did each of you include or leave out?</li><li><strong>Find the Combahee River</strong> on a map of South Carolina, near Beaufort.</li><li><strong>Read Harriet’s letter aloud together</strong> and talk about why she chose the word “livestock.”</li>')
between('<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>\n    <p><strong>No book needed this week.</strong> The three accounts are on the lesson pages. <strong>A device that records audio</strong> for the fluency reading and the presentation.</p>\n  ')
between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 25</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 26</h2></div>\n    <p><strong>A new book: <em>Prince Caspian</em> by C. S. Lewis, Chapters 1–3.</strong> Four children are pulled back into Narnia and find a ruined castle. A new guide, Nell the bookbinder, leads the unit, and the word game becomes Fill the Treasure Chamber. See the <a href="parent-guide-pc-unit.html" style="color:#1F6FA8;font-weight:700;">Prince Caspian unit guide</a>.</p>\n  ')
io.open('parent-guide-week-25.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('Week 24'), s.count('Week 25'), s.count('24.'), len(s))
