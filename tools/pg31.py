#!/usr/bin/env python3
"""parent-guide-week-31.html from the week 25 guide (same look). Year-end synthesis: comparing themes across the five books."""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pgcommon import G
g = G()
g.between('<title>', '</title>', '<title>Week 31 Family Guide · Year-End Synthesis · 4th Grade ELA')
g.between('<h1>', '</h1>', '<h1>Week 31: Five Books, Side by Side')
g.between('<div class="sub">', '</div>', '<div class="sub">Year-End Synthesis: comparing themes across the year’s novels')
g.between('<div class="chips">', '</div>', '<div class="chips">\n        <span class="chip">4 lessons</span>\n        <span class="chip">1 fluency recording</span>\n        <span class="chip">No new chapters</span>\n        <span class="chip">Comparison paragraph</span>\n        <span class="chip">Check-In at week’s end</span>\n      ')
g.s = g.s.replace("assets/covers/ft.jpg');background-position:center 35%;", "assets/covers/pc.jpg');background-position:center 35%;")
g.s = g.s.replace('aria-label="Cover of Freedom Train by Dorothy Sterling"', 'aria-label="Cover of Prince Caspian by C. S. Lewis, the last novel of the year"')
g.s = g.s.replace('<h2>By Heart: the Unit Poem</h2>', '<h2>Poem of the Week</h2>')
g.s = g.s.replace('Week 25', 'Week 31')

g.sec('This Week at a Glance', '''
    <div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
    <p>No new reading this week. Your student puts the year’s five books side by side: <em>Mrs. Frisby and the Rats of NIMH</em>, <em>Anne of Green Gables</em>, <em>Number the Stars</em>, <em>Freedom Train</em> and <em>Prince Caspian</em>. Day 1 they choose a theme, Day 2 they find it in two characters from two different books, Day 3 they write a comparison paragraph with evidence from both, and Day 4 they say what the books together taught them about people. Opti, the owl from the start of the year, is the guide again.</p>
    <div class="box b-rose" style="margin-bottom:12px;"><div class="box-label">💛 A tip for families</div>Keep the books (or the reading journal) within reach this week. The best evidence is a real moment your student can point to, not a memory of one.</div>
    <div class="glance">
      <div class="box b-sky"><div class="box-label">Reading skill</div><strong>Comparing themes across texts.</strong> Your student shows how two characters in different stories share a big idea, and how they show it in different ways.</div>
      <div class="box b-green"><div class="box-label">Big idea</div><strong>Stories teach us about people.</strong> Courage, loyalty and belonging look different in a rat, a red-haired orphan, a Danish girl, Harriet Tubman and a young king.</div>
    </div>
    <p class="quote">“That’s all that brave means—not thinking about the dangers. Just thinking about what you must do.”<small>Uncle Henrik, <em>Number the Stars</em></small></p>
  ''')

rows = '''        <tr>
          <td class="day-n">31.1<span>Day 1</span></td>
          <td><span class="ch">Comparing themes</span><br>What is a theme? Your student picks one (courage, loyalty, belonging…) and lists the books and moments where it shows up.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Copia: Say It Three Ways</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What big ideas show up in more than one story?</td>
        </tr>
        <tr>
          <td class="day-n">31.2<span>Day 2</span></td>
          <td><span class="ch">Identifying themes</span><br>Two characters from two books who show the same theme: one real moment for each, then how they are alike and different.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>How can two characters show the same idea in different ways?</td>
        </tr>
        <tr>
          <td class="day-n">31.3<span>Day 3</span></td>
          <td><span class="ch">Applying themes</span><br>The comparison paragraph: a theme sentence, evidence from each book, and how the two are alike and different.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>How do you prove two characters share a theme?</td>
        </tr>
        <tr>
          <td class="day-n">31.4<span>Day 4</span></td>
          <td><span class="ch">Final reflection</span><br>Stepping back from the whole week: what the theme says about real people, in one sentence your student would sign. They also choose the year’s strongest pillar.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What did you discover about people from all five books together?</td>
        </tr>
'''
g.rows(rows)
g.between('<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">', ' Your student reads it three times',
        '<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">Your student’s choice of three favorite passages: one each from <em>Anne of Green Gables</em>, <em>Number the Stars</em> and <em>Prince Caspian</em>.')
g.between('<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">', '</td>',
        '<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">A 14-point check-in: a grammar spiral review, word parts from the whole year, spelling patterns in final writing, and comparing themes across the books.')

g.between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>theme</b><span>a big idea about life that a story keeps showing</span></div><div class="word"><b>solemnly</b><span>in a serious, sincere way</span></div><div class="word"><b>allegiance</b><span>loyalty to a person, cause or country</span></div><div class="word"><b>indignant</b><span>angry because something is unfair</span></div></div>\n    ')
g.between('<div class="box b-sky"><div class="box-label">Word parts</div>', '</div>\n      <div class="box b-gold">',
  '<div class="box b-sky"><div class="box-label">Word parts</div><strong>A year of word parts.</strong> Find a part you know in a long word and the word starts to explain itself.<span class="eg">port (carry) · spect (look) · rupt (break) · pre (before)</span>')
g.between('<div class="box b-gold"><div class="box-label">Spelling</div>', '</div>\n      <div class="box b-green">',
  '<div class="box b-gold"><div class="box-label">Spelling</div><strong>Check the pattern.</strong> Before handing in writing, check the rules one at a time: drop the silent e, change y to i, double the consonant.<span class="eg">hope → hoping · happy → happier · stop → stopped</span>')
g.between('<div class="box b-green"><div class="box-label">Grammar</div>', '</div>\n    </div>',
  '<div class="box b-green"><div class="box-label">Grammar</div><strong>Every mark has a job.</strong> Capitals start and name; commas join or separate; quotation marks hold someone’s exact words.<span class="eg">Although Harriet and Anne faced different struggles, they both refused to give up.</span>')

g.sec('New in the Lessons', '''
    <div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
    <p>Opti is back as the guide for the last two weeks, with a short Word Study film each day. The Seven Pillars Watch and the reading lens continue. This week:</p>
    <div class="extras">
      <div class="box b-plum"><div class="box-label">📝 Note-catchers</div>Each day’s Reading tab has boxes to plan in: my theme, two characters side by side, the paragraph plan, and what I discovered.</div>
      <div class="box b-gold"><div class="box-label">📜 Two poems about choices and books</div>The first stanza of Robert Frost’s “The Road Not Taken” (Day 2) and Emily Dickinson’s “There is no Frigate like a Book” (Day 4).</div>
      <div class="box b-green"><div class="box-label">🏛️ The year’s strongest pillar</div>Days 1–3 bring real moments from three books to sort by pillar; on Day 4 your student picks the pillar the characters showed most all year.</div>
    </div>
  ''')

g.sec('Your Student’s Research Report', '''
    <div class="card-head"><span class="ico">✍️</span><h2>Writing This Week</h2><span class="tag">Comparison paragraph</span></div>
    <p>One paragraph, built across the week. It opens with a theme sentence, gives a real moment from each of two books as evidence, explains how the characters are alike and how they are different, and ends by saying what the theme shows about people. Next week your student polishes it for the year-end portfolio.</p>
  ''')

g.between('<div class="poem">', '</div>\n      <div>',
  '<div class="poem">There is no Frigate like a Book<br>To take us Lands away,<br>Nor any Coursers like a Page<br>Of prancing Poetry –<small>Emily Dickinson, first stanza</small>')
g.between('<p>On Days 2 and 4 your student says the four lines again.', '</p>',
  '<p>A frigate is a sailing ship and a courser is a fast horse. Dickinson is saying a book carries you farther than either.')
g.between('<p><strong>How to help:</strong>', '</p>',
  '<p><strong>How to help:</strong> Ask which of the five books took your student the farthest away, and why.')

g.between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">What theme did you choose?</span><span class="listen">Listen for: a big idea about life, like courage, loyalty or belonging, not just a topic.</span></li><li><span class="q">Which two characters show it?</span><span class="listen">Listen for: two characters from two different books.</span></li><li><span class="q">What is one moment that proves it for each?</span><span class="listen">Listen for: a specific thing the character did or said.</span></li><li><span class="q">How are the two characters different, even though they share the theme?</span><span class="listen">Listen for: different times, places, dangers or reasons for acting.</span></li><li><span class="q">What do the books together say about people?</span><span class="listen">Listen for: one clear sentence your student believes.</span></li><li><span class="q">Which pillar did the characters show most this year?</span><span class="listen">Listen for: a pillar and a real moment from any of the five books.</span></li>')
g.between('<ul class="check"><li><strong>Each lesson:</strong>', '</ul>',
  '<ul class="check"><li><strong>Each lesson:</strong> note-catchers, word-study and writing responses, submitted in Canvas</li><li><strong>Writing:</strong> the comparison paragraph, planned on Day 3</li><li><strong>Fluency:</strong> a recording of one favorite passage</li><li><strong>Check-In:</strong> at the end of the week</li>')
g.between('<strong>Done well looks like:</strong>', '</p>',
  '<strong>Done well looks like:</strong> a clear theme sentence, a real moment from each book, and a sentence that explains how the two characters are alike and different.')
g.between('<ul class="check"><li><strong>Tell the same story two ways.</strong>', '</ul>',
  '<ul class="check"><li><strong>Ask your student</strong> which character from this year they would most like to meet, and what they would ask.</li><li><strong>Share a theme from your own favorite book or movie</strong> and see if your student can find it in one of theirs.</li><li><strong>Line up the five books</strong> on a shelf or table for the week, so the evidence is close by.</li>')
g.between('<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>\n    <p><strong>The year’s books</strong> (or the reading journal) · <strong>A device that records audio</strong> for the fluency reading</p>\n  ')
g.between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 26</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 32</h2></div>\n    <p><strong>The last week of 4th grade ELA.</strong> Your student polishes the comparison paragraph, writes about how they grew as a reader, builds a portfolio page, and sets a reading goal for next year.</p>\n  ')
g.s = g.s.replace('<a href="parent-guide-ft-unit.html" style="color:#1F6FA8;font-weight:700;">See the whole Freedom Train unit →</a><br><br>', '')
io.open('parent-guide-week-31.html', 'w', encoding='utf-8').write(g.s)
print('ok', g.s.count('Freedom Train unit'), g.s.count('Week 25'), g.s.count('25.'), g.s.count('Ch. '))
