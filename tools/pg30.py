#!/usr/bin/env python3
"""parent-guide-week-30.html from the week 25 guide (same look). Prince Caspian Ch. 13-15, checked against the text."""
import io
s = io.open('parent-guide-week-25.html', encoding='utf-8').read()
def between(start, end, new, after=0):
    global s
    i = s.index(start, after); j = s.index(end, i + len(start))
    s = s[:i] + new + s[j:]
def sec(head_text, new_inner):
    global s
    k = s.index(head_text); i = s.rindex('<section', 0, k); i = s.index('>', i) + 1; j = s.index('</section>', k)
    s = s[:i] + new_inner + s[j:]

between('<title>', '</title>', '<title>Week 30 Family Guide · Prince Caspian Ch. 13–15 · 4th Grade ELA')
between('<h1>', '</h1>', '<h1>Week 30: The Door in the Air')
between('<div class="sub">', '</div>', '<div class="sub"><em>Prince Caspian</em> by C. S. Lewis, Chapters 13–15')
between('<div class="chips">', '</div>', '<div class="chips">\n        <span class="chip">4 lessons</span>\n        <span class="chip">1 fluency recording</span>\n        <span class="chip">Ch. 13–15</span>\n        <span class="chip">The end of the book</span>\n        <span class="chip">Check-In at week’s end</span>\n      ')
s = s.replace("assets/covers/ft.jpg');background-position:center 35%;", "assets/covers/pc.jpg');background-position:center 35%;")
s = s.replace('aria-label="Cover of Freedom Train by Dorothy Sterling"', 'aria-label="Cover of Prince Caspian by C. S. Lewis"')
s = s.replace('Week 25', 'Week 30')

sec('This Week at a Glance', '''
    <div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
    <p>The last three chapters. Peter challenges Miraz to single combat so the two armies won’t have to fight. In the duel, Miraz trips and Peter steps back instead of striking; then Miraz’s own lords betray him and the battle begins, until the trees arrive. Aslan and the girls travel the country waking it up. Caspian is made King, the Telmarines are offered a door home, and the four children step back onto the train platform where the story began. Each day your student also writes a short Writing Connection, and Day 4 is the final literary response for the book.</p>
    <div class="box b-rose" style="margin-bottom:12px;"><div class="box-label">💛 A heads-up for families</div>Chapter 14 has the duel and a short battle: Miraz is killed by one of his own lords, who blames the Narnians. Chapter 15 brings a goodbye: Peter and Susan learn they will not come back to Narnia. Some children feel that one.</div>
    <div class="glance">
      <div class="box b-sky"><div class="box-label">Reading skill</div><strong>How the ending reveals theme.</strong> Your student names what the story still has to settle, watches how it gets settled, and says what the ending shows the book believes.</div>
      <div class="box b-green"><div class="box-label">Big idea</div><strong>Honour, and letting go.</strong> Peter wins the right way, Caspian is crowned because he knows he isn’t ready, and Peter and Susan say goodbye.</div>
    </div>
    <p class="quote">“If you had felt yourself sufficient, it would have been a proof that you were not.”<small>Aslan, Chapter 15</small></p>
  ''')

rows = '''        <tr>
          <td class="day-n">30.1<span>Day 1</span></td>
          <td><span class="ch">Chapter 13 · The High King in Command</span><br>Peter dictates a formal challenge to Miraz. Miraz’s lords goad him into accepting, for reasons of their own. Peter chooses his marshals and turns down Reepicheep, gently.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Copia: Say It Three Ways</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>When there is more than one way to settle a fight, what does the way you choose say about you?</td>
        </tr>
        <tr>
          <td class="day-n">30.2<span>Day 2</span></td>
          <td><span class="ch">Chapter 14 · How All Were Very Busy</span><br>The duel. Miraz trips and Peter steps back. Miraz’s lords betray him, the battle starts, and the trees join it. Meanwhile Aslan, Lucy and Susan travel through a waking country.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What matters more, who wins, or how?</td>
        </tr>
        <tr>
          <td class="day-n">30.3<span>Day 3</span></td>
          <td><span class="ch">Chapter 15 · Aslan Makes a Door in the Air</span><br>Caspian is made King. The Mice win Reepicheep his tail back. The Telmarines are offered a door home, and the children say goodbye.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>Who has changed the most since the first page, and what did it cost them?</td>
        </tr>
        <tr>
          <td class="day-n">30.4<span>Day 4</span></td>
          <td><span class="ch">The whole book · looking back</span><br>No new chapter. Your student writes a final literary response about leadership or loyalty in <em>Prince Caspian</em>, and names the book’s strongest pillar.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What does Prince Caspian believe, and what in the ending proves it?</td>
        </tr
'''
i = s.index('        <tr>\n          <td class="day-n">25.1'); j = s.index('        <tr class="extra-row">', i)
s = s[:i] + rows.replace('</tr\n', '</tr>\n') + s[j:]
between('<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">', ' Your student reads it three times',
        '<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">A passage from Chapter 15: Peter tells Lucy he won’t be coming back, and the goodbyes begin.')
between('<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">', '</td>',
        '<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">A 14-point wrap-up on the whole book: dialogue punctuation, a review of every word base, spelling rules, and questions about the ending, with real passages from Chapters 14 and 15.')

between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>challenge</b><span>an invitation to fight that must be answered</span></div><div class="word"><b>marshal</b><span>an official who oversees a contest and keeps order</span></div><div class="word"><b>sufficient</b><span>enough for what is needed</span></div><div class="word"><b>coronation</b><span>the ceremony of crowning a king or queen</span></div></div>\n    ')
between('<div class="box b-sky"><div class="box-label">Word parts</div>', '</div>\n      <div class="box b-gold">',
  '<div class="box b-sky"><div class="box-label">Word parts</div>A review of every base in the unit, plus <strong>press</strong> (push), <strong>tain</strong> (hold) and <strong>lev</strong> (lift).<span class="eg">port · tract · struct · spect · ject · script · rupt · duct · form</span>')
between('<div class="box b-gold"><div class="box-label">Spelling</div>', '</div>\n      <div class="box b-green">',
  '<div class="box b-gold"><div class="box-label">Spelling</div><strong>Cumulative review.</strong> A hard word is two or three easy rules stacked up. Take it apart and use them one at a time.<span class="eg">hope + ful · forget + t + able</span>')
between('<div class="box b-green"><div class="box-label">Grammar</div>', '</div>\n    </div>',
  '<div class="box b-green"><div class="box-label">Grammar</div><strong>Dialogue punctuation.</strong> Quotation marks go around the exact words; the comma or end mark goes inside them; the tag joins with a comma.<span class="eg">“Well!” said Peter. “We have had a time.”</span>')

sec('New in the Lessons', '''
    <div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
    <p>Nell, the Seven Pillars Watch and the reading lens continue. This week:</p>
    <div class="extras">
      <div class="box b-plum"><div class="box-label">🏁 Then and now</div>Note boxes on the Reading tab ask your student to compare who characters were at the start of the book with who they are at the end, and what the change cost.</div>
      <div class="box b-gold"><div class="box-label">📜 Two Tennyson poems</div>A few lines of “The Charge of the Light Brigade” (Day 2) and the first stanza of “Crossing the Bar” (Day 4).</div>
      <div class="box b-green"><div class="box-label">🏛️ The book’s strongest pillar</div>On Day 4 your student picks the pillar the characters showed most across the whole book.</div>
    </div>
  ''')

sec('Your Student’s Research Report', '''
    <div class="card-head"><span class="ico">✍️</span><h2>Writing This Week</h2><span class="tag">Writing Connection</span></div>
    <p>The book’s last writing. Day 1 is three or four sentences on why Peter’s challenge letter uses such formal words; Days 2 and 3 practice Lewis’s patterns (Trumpkin’s excited fragment, and Aslan’s balanced “both … enough to …, and … enough to …”); Day 4 is the final literary response, a five-to-seven-sentence paragraph with three pieces of evidence from the whole book.</p>
  ''')

between('<div class="poem">', '</div>\n      <div>',
  '<div class="poem">The stones still stand where towers fell,<br>The river hums a half-lost spell,<br>The trees lean close as if to say,<br>“We knew you’d find your way back someday.”<small>“The Forest Remembers,” written for our Prince Caspian lessons</small>')
between('<p>On Days 2 and 4 your student says the four lines again.', '</p>',
  '<p>The unit poem stays the same all five weeks. This week the lessons also include two short original poems on Days 2 and 4.')
between('<p><strong>How to help:</strong>', '</p>',
  '<p><strong>How to help:</strong> Ask your student to say the whole poem for you one last time. It is the last week with it.')

between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">Why did Peter fight Miraz himself instead of with the whole army?</span><span class="listen">Listen for: Caspian was wounded, and one fight could spare many lives.</span></li><li><span class="q">What did Peter do when Miraz tripped?</span><span class="listen">Listen for: he stepped back and waited for Miraz to get up.</span></li><li><span class="q">Who really killed Miraz?</span><span class="listen">Listen for: his own lords, Glozelle and Sopespian, who then blamed the Narnians.</span></li><li><span class="q">Why did Aslan say Caspian was ready to be King?</span><span class="listen">Listen for: Caspian said he didn’t feel sufficient, and Aslan said that was the proof.</span></li><li><span class="q">How did the Mice win Reepicheep his tail back?</span><span class="listen">Listen for: they were ready to cut off their own tails so he wouldn’t be alone.</span></li><li><span class="q">Which pillar did the characters show most in the whole book?</span><span class="listen">Listen for: a pillar and a real moment from anywhere in <em>Prince Caspian</em>.</span></li>')
between('<ul class="check"><li><strong>Each lesson:</strong>', '</ul>',
  '<ul class="check"><li><strong>Each lesson:</strong> 3 chapter questions plus word-study and writing responses, submitted in Canvas</li><li><strong>Writing:</strong> the final literary response on Day 4</li><li><strong>Fluency:</strong> a recording of a passage from Chapter 15</li><li><strong>Check-In:</strong> at the end of the week</li>')
between('<strong>Done well looks like:</strong>', '</p>',
  '<strong>Done well looks like:</strong> a clear claim about what the book believes, three moments from the book that prove it, and a last sentence that says why it matters.')
between('<ul class="check"><li><strong>Tell the same story two ways.</strong>', '</ul>',
  '<ul class="check"><li><strong>Ask your student</strong> who changed the most in the book, and how.</li><li><strong>Talk about a goodbye</strong> in your family: a move, a graduation, a last visit. Was it, like Peter says, rather different from what you thought?</li><li><strong>Celebrate finishing a book</strong> with a small treat, the way the Narnians feast at the end</li>')
between('<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>\n    <p><strong><em>Prince Caspian</em></strong> by C. S. Lewis · <strong>A device that records audio</strong> for the fluency reading</p>\n  ')
between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 26</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 31</h2></div>\n    <p><strong>Synthesis week.</strong> Your student compares the books from this year side by side, with Opti as the guide again.</p>\n  ')
s = s.replace('href="parent-guide-ft-unit.html"', 'href="parent-guide-pc-unit.html"').replace('See the whole Freedom Train unit →', 'See the whole Prince Caspian unit →')
import re
io.open('parent-guide-week-30.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('Freedom'), s.count('Harriet'), s.count('Marcus'), s.count('25.'))
