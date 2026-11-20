#!/usr/bin/env python3
"""parent-guide-week-32.html from the week 25 guide (same look). Year-end project and celebration."""
import io, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pgcommon import G
g = G()
g.between('<title>', '</title>', '<title>Week 32 Family Guide · Year-End Project and Celebration · 4th Grade ELA')
g.between('<h1>', '</h1>', '<h1>Week 32: Looking Back, Looking Forward')
g.between('<div class="sub">', '</div>', '<div class="sub">Year-End Project: the last week of 4th grade ELA')
g.between('<div class="chips">', '</div>', '<div class="chips">\n        <span class="chip">4 lessons</span>\n        <span class="chip">1 fluency recording</span>\n        <span class="chip">No new chapters</span>\n        <span class="chip">Portfolio page</span>\n        <span class="chip">Final Check-In</span>\n      ')
g.s = g.s.replace("assets/covers/ft.jpg');background-position:center 35%;", "assets/covers/pc.jpg');background-position:center 35%;")
g.s = g.s.replace('aria-label="Cover of Freedom Train by Dorothy Sterling"', 'aria-label="Cover of Prince Caspian by C. S. Lewis, the last novel of the year"')
g.s = g.s.replace('<h2>By Heart: the Unit Poem</h2>', '<h2>Poem of the Week</h2>')
g.s = g.s.replace('Week 25', 'Week 32')

g.sec('This Week at a Glance', '''
    <div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
    <p>The last week of the year. Day 1 your student revises last week’s comparison paragraph and proofreads it like an editor. Day 2 they write about themselves as a reader: who they were in August and who they are now, with proof. Day 3 they choose their best piece of writing from the year for a portfolio page and explain why. Day 4 is a celebration: one goal for next year, the pillar they want to carry into 5th grade, and the last sentence of their year.</p>
    <div class="box b-rose" style="margin-bottom:12px;"><div class="box-label">💛 A tip for families</div>Day 3 asks your student to look through a whole year of writing. If you have kept any of it at home, this is the week to bring it out.</div>
    <div class="glance">
      <div class="box b-sky"><div class="box-label">Reading skill</div><strong>Reflecting on growth.</strong> Your student names a reading skill they have now and proves it with a real example, the way they would prove something about a character.</div>
      <div class="box b-green"><div class="box-label">Big idea</div><strong>Readers keep growing.</strong> Five books, a year of word parts and a lot of writing. What comes next is up to them.</div>
    </div>
    <p class="quote">“Hold fast to dreams<br>For if dreams die<br>Life is a broken-winged bird<br>That cannot fly.”<small>Langston Hughes, “Dreams” (Day 4)</small></p>
  ''')

rows = '''        <tr>
          <td class="day-n">32.1<span>Day 1</span></td>
          <td><span class="ch">Polishing the comparison</span><br>Reading the paragraph as if someone else wrote it, changing one sentence to make it sharper, then checking capitals, usage, punctuation and spelling.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-extra">Copia: Say It Three Ways</span></td>
          <td>What makes a strong comparison paragraph, and how can you make yours stronger?</td>
        </tr>
        <tr>
          <td class="day-n">32.2<span>Day 2</span></td>
          <td><span class="ch">Reader’s growth</span><br>Me as a reader in August, me as a reader now, and the proof.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry Corner</span></td>
          <td>Who were you as a reader in August, and who are you now?</td>
        </tr>
        <tr>
          <td class="day-n">32.3<span>Day 3</span></td>
          <td><span class="ch">Portfolio and presentation</span><br>Choosing the piece of writing that best shows how your student thinks, explaining why, and writing advice to themselves back in Week 1.<br><span class="pill p-guide">Guide: Opti</span></td>
          <td>What is the most important thing you learned this year?</td>
        </tr>
        <tr>
          <td class="day-n">32.4<span>Day 4</span></td>
          <td><span class="ch">Celebration</span><br>Looking back at the whole year and forward to the next: a real reading goal, the pillar to carry forward, and the last sentence of the year.<br><span class="pill p-guide">Guide: Opti</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>If you had one minute to tell someone what this year of reading did for you, what would you say first?</td>
        </tr>
'''
g.rows(rows)
g.between('<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">', ' Your student reads it three times',
        '<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">Favorite passages again, from <em>Anne of Green Gables</em>, <em>Number the Stars</em> and <em>Prince Caspian</em>. Your student can pick a new one or polish last week’s.')
g.between('<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">', '</td>',
        '<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">The final 14-point check-in: an editing review, favorite word parts, a last conventions check, and reflecting on reading growth.')

g.between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>revise</b><span>change writing to make the ideas clearer or stronger</span></div><div class="word"><b>proofread</b><span>check writing for mistakes in capitals, usage, punctuation and spelling</span></div><div class="word"><b>portfolio</b><span>a collection of your best work</span></div><div class="word"><b>reflect</b><span>think carefully about what you did and learned</span></div></div>\n    ')
g.between('<div class="box b-sky"><div class="box-label">Word parts</div>', '</div>\n      <div class="box b-gold">',
  '<div class="box b-sky"><div class="box-label">Word parts</div><strong>Roots you can still use.</strong> Three more to take into next year.<span class="eg">press (push) · tain (hold) · lev (lift)</span>')
g.between('<div class="box b-gold"><div class="box-label">Spelling</div>', '</div>\n      <div class="box b-green">',
  '<div class="box b-gold"><div class="box-label">Spelling</div><strong>The last check.</strong> Touch each long word, find the part you know, check the ending. If a word looks strange, it probably is.<span class="eg">re + view · hope + ful · stop + p + ed</span>')
g.between('<div class="box b-green"><div class="box-label">Grammar</div>', '</div>\n    </div>',
  '<div class="box b-green"><div class="box-label">Grammar</div><strong>Proofread like an editor.</strong> Four quick passes catch more than one long one: capitals, usage, punctuation, spelling.<span class="eg">This year I read five novels, studied word roots, and practiced writing.</span>')

g.sec('New in the Lessons', '''
    <div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
    <p>Opti guides the last four lessons, with a short Word Study film each day. This week:</p>
    <div class="extras">
      <div class="box b-plum"><div class="box-label">📝 Before and after</div>Day 1 asks for one sentence before revising and the same sentence after, side by side, so your student can see what changed.</div>
      <div class="box b-gold"><div class="box-label">📜 Two last poems</div>Robert Frost’s “Nothing Gold Can Stay” (Day 2) and Langston Hughes’s “Dreams” (Day 4).</div>
      <div class="box b-green"><div class="box-label">🏛️ The pillar I’ll carry forward</div>On Day 4 your student picks the pillar they want to take into 5th grade.</div>
    </div>
  ''')

g.sec('Your Student’s Research Report', '''
    <div class="card-head"><span class="ico">✍️</span><h2>Writing This Week</h2><span class="tag">Year-End Project</span></div>
    <p>Four short pieces that finish the year: the polished comparison paragraph (Day 1), a reader’s-growth reflection with proof (Day 2), a portfolio page explaining the best piece of the year (Day 3), and a reading goal plus the last sentence of the year (Day 4).</p>
  ''')

g.between('<div class="poem">', '</div>\n      <div>',
  '<div class="poem">Hold fast to dreams<br>For when dreams go<br>Life is a barren field<br>Frozen with snow.<small>Langston Hughes, “Dreams,” second stanza</small>')
g.between('<p>On Days 2 and 4 your student says the four lines again.', '</p>',
  '<p>Hughes writes a goal for life in eight short lines. Your student writes a goal for next year on the same day.')
g.between('<p><strong>How to help:</strong>', '</p>',
  '<p><strong>How to help:</strong> Share one of your own dreams from when you were their age, and ask about theirs.')

g.between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">What did you change in your comparison paragraph?</span><span class="listen">Listen for: one specific sentence, and why the new one is stronger.</span></li><li><span class="q">What can you do as a reader now that you couldn’t in August?</span><span class="listen">Listen for: a named skill, like finding a theme or using word parts.</span></li><li><span class="q">Can you prove it?</span><span class="listen">Listen for: a real example from their reading or writing.</span></li><li><span class="q">Which piece did you choose for your portfolio, and why?</span><span class="listen">Listen for: what it shows about how they think, not just its length.</span></li><li><span class="q">What is your reading goal for next year?</span><span class="listen">Listen for: something real and specific.</span></li><li><span class="q">Which pillar will you carry into 5th grade?</span><span class="listen">Listen for: a pillar and why it matters to them.</span></li>')
g.between('<ul class="check"><li><strong>Each lesson:</strong>', '</ul>',
  '<ul class="check"><li><strong>Each lesson:</strong> note-catchers and writing responses, submitted in Canvas</li><li><strong>Writing:</strong> the polished comparison paragraph and the portfolio page</li><li><strong>Fluency:</strong> a recording of one favorite passage</li><li><strong>Check-In:</strong> the final one, at the end of the week</li>')
g.between('<strong>Done well looks like:</strong>', '</p>',
  '<strong>Done well looks like:</strong> a reflection that names a real skill, proves it with an example, and sounds like your student.')
g.between('<ul class="check"><li><strong>Tell the same story two ways.</strong>', '</ul>',
  '<ul class="check"><li><strong>Celebrate the year</strong> with a small treat and a toast to five books.</li><li><strong>Plan summer reading together:</strong> a trip to the library, or a sequel to one of this year’s books.</li><li><strong>Ask your student to read you their last sentence of the year</strong>, and keep it somewhere you’ll both see it.</li>')
g.between('<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>\n    <p><strong>Your student’s writing from the year</strong> (in Canvas or the reading journal) · <strong>A device that records audio</strong> for the fluency reading</p>\n  ')
g.between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 26</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up Next</h2></div>\n    <p><strong>5th grade.</strong> Thank you for reading alongside your student all year. Keep the books coming over the summer.</p>\n  ')
g.s = g.s.replace('<a href="parent-guide-ft-unit.html" style="color:#1F6FA8;font-weight:700;">See the whole Freedom Train unit →</a><br><br>', '')
io.open('parent-guide-week-32.html', 'w', encoding='utf-8').write(g.s)
print('ok', g.s.count('Freedom Train unit'), g.s.count('Week 25'), g.s.count('25.'), g.s.count('Ch. '))
