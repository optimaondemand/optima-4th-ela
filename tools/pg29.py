#!/usr/bin/env python3
"""parent-guide-week-29.html from the week 25 guide (same look). Prince Caspian Ch. 10-12, checked against the text."""
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

between('<title>', '</title>', '<title>Week 29 Family Guide · Prince Caspian Ch. 10–12 · 4th Grade ELA')
between('<h1>', '</h1>', '<h1>Week 29: The Lion Returns')
between('<div class="sub">', '</div>', '<div class="sub"><em>Prince Caspian</em> by C. S. Lewis, Chapters 10–12')
between('<div class="chips">', '</div>', '<div class="chips">\n        <span class="chip">4 lessons</span>\n        <span class="chip">1 fluency recording</span>\n        <span class="chip">Ch. 10–12</span>\n        <span class="chip">Theme</span>\n        <span class="chip">Check-In at week’s end</span>\n      ')
s = s.replace("assets/covers/ft.jpg');background-position:center 35%;", "assets/covers/pc.jpg');background-position:center 35%;")
s = s.replace('aria-label="Cover of Freedom Train by Dorothy Sterling"', 'aria-label="Cover of Prince Caspian by C. S. Lewis"')
s = s.replace('Week 25', 'Week 29')

sec('This Week at a Glance', '''
    <div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
    <p>Lucy wakes in the night and finds Aslan. He tells her to wake the others and follow him, even though they won’t be able to see him. She does. One by one, as they follow, the others begin to see him too, and Susan and Peter say they are sorry. Aslan roars, and the trees of Narnia wake. Meanwhile, in Aslan’s How, Nikabrik brings a Hag and a Werewolf to Caspian’s council and proposes calling back the White Witch. Peter, Edmund and Trumpkin arrive in time. Each day your student also writes a short Writing Connection.</p>
    <div class="box b-rose" style="margin-bottom:12px;"><div class="box-label">💛 A heads-up for families</div>Chapter 12 is the darkest so far. In a fight in the dark, Nikabrik, the Hag and the Werewolf are killed, and Caspian is bitten. Lewis keeps it brief, and Caspian speaks kindly of Nikabrik afterward.</div>
    <div class="glance">
      <div class="box b-sky"><div class="box-label">Reading skill</div><strong>Theme through repeated choices.</strong> Your student notices choices that echo each other (whom to trust, whether to admit you were wrong) and builds a theme sentence from them.</div>
      <div class="box b-green"><div class="box-label">Big idea</div><strong>Trust, and what it costs.</strong> Lucy trusts what only she can see. Others admit they were wrong. Nikabrik trusts the wrong power.</div>
    </div>
    <p class="quote">“Every year you grow, you will find me bigger.”<small>Aslan, Chapter 10</small></p>
  ''')

rows = '''        <tr>
          <td class="day-n">29.1<span>Day 1</span></td>
          <td><span class="ch">Chapter 10 · The Return of the Lion</span><br>Lucy wakes, follows a voice through the moonlit trees, and finds Aslan. He tells her she must wake the others and follow him, whether they believe her or not.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Copia: Say It Three Ways</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What does it cost to trust what only you can see?</td>
        </tr>
        <tr>
          <td class="day-n">29.2<span>Day 2</span></td>
          <td><span class="ch">Chapter 11 · The Lion Roars</span><br>The others follow Lucy through the dark, and one by one they begin to see Aslan. Susan and Peter say they are sorry. Aslan roars, and the trees wake and dance.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What do all of this week’s choices have in common?</td>
        </tr>
        <tr>
          <td class="day-n">29.3<span>Day 3</span></td>
          <td><span class="ch">Chapter 12 · Sorcery and Sudden Vengeance</span><br>In Aslan’s How, Nikabrik brings two dark guests to Caspian’s council. Peter, Edmund and Trumpkin arrive just in time. Peter meets Caspian at last.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>When people have to choose whom to trust, what does this book seem to believe?</td>
        </tr>
        <tr>
          <td class="day-n">29.4<span>Day 4</span></td>
          <td><span class="ch">Chapters 10–12 · looking back</span><br>No new chapter. Your student tests a theme sentence on a new character, drafts a theme paragraph, and names the week’s strongest pillar.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>Does your theme sentence hold for everyone?</td>
        </tr
'''
i = s.index('        <tr>\n          <td class="day-n">25.1'); j = s.index('        <tr class="extra-row">', i)
s = s[:i] + rows.replace('</tr\n', '</tr>\n') + s[j:]
between('<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">', ' Your student reads it three times',
        '<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">A passage from Chapter 10: Lucy and Aslan meet again in the moonlight.')
between('<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">', '</td>',
        '<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">A 14-point wrap-up: commas in dates and places, the Latin bases rupt, duct/duce and form, Greek and Latin word parts, and questions about theme, with real passages from Chapters 10 and 11.')

between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>precipice</b><span>a very steep cliff or drop</span></div><div class="word"><b>luminous</b><span>giving off light; glowing</span></div><div class="word"><b>revelry</b><span>wild, noisy celebration</span></div><div class="word"><b>treason</b><span>betraying your own king or country</span></div></div>\n    ')
between('<div class="box b-sky"><div class="box-label">Word parts</div>', '</div>\n      <div class="box b-gold">',
  '<div class="box b-sky"><div class="box-label">Word parts</div>Latin bases: <strong>rupt</strong> (break), <strong>duct / duce</strong> (lead), <strong>form</strong> (shape).<span class="eg">interrupt · aqueduct · formation</span>')
between('<div class="box b-gold"><div class="box-label">Spelling</div>', '</div>\n      <div class="box b-green">',
  '<div class="box b-gold"><div class="box-label">Spelling</div><strong>Word parts, review.</strong> Find the Greek or Latin part you know and spell it the same way every time.<span class="eg">port·able · spect·a·tor</span>')
between('<div class="box b-green"><div class="box-label">Grammar</div>', '</div>\n    </div>',
  '<div class="box b-green"><div class="box-label">Grammar</div><strong>Commas in dates and places.</strong> A comma between the day and the year, between a town and its bigger place, and one more after them if the sentence goes on. (Narnia has no calendar, so practice dates are made up.)<span class="eg">June 12, 1941 · Dover, Kent</span>')

sec('New in the Lessons', '''
    <div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
    <p>Nell, the Seven Pillars Watch and the reading lens continue. This week:</p>
    <div class="extras">
      <div class="box b-plum"><div class="box-label">🧵 A theme sentence, built over four days</div>Note boxes on the Reading tab collect echoing choices (Day 1), find one word for them (Day 2), turn it into a sentence (Day 3), and test it on a new character (Day 4).</div>
      <div class="box b-gold"><div class="box-label">📜 Two classic poems</div>Christina Rossetti’s “Who Has Seen the Wind?” (Day 2) and the opening of Rudyard Kipling’s “If—” (Day 4).</div>
    </div>
  ''')

sec('Your Student’s Research Report', '''
    <div class="card-head"><span class="ico">✍️</span><h2>Writing This Week</h2><span class="tag">Writing Connection</span></div>
    <p>This week builds toward a theme paragraph. Day 1 is three or four sentences about Aslan’s words, “Nobody is ever told that”; Days 2 and 3 practice Lewis’s sentence patterns (the far-then-near sentence about the trees, and Trufflehunter’s “I’m a … and we …”); Day 4 is a draft theme paragraph with two examples from Chapters 10–12.</p>
  ''')

between('<div class="poem">', '</div>\n      <div>',
  '<div class="poem">The stones still stand where towers fell,<br>The river hums a half-lost spell,<br>The trees lean close as if to say,<br>“We knew you’d find your way back someday.”<small>“The Forest Remembers,” written for our Prince Caspian lessons</small>')
between('<p>On Days 2 and 4 your student says the four lines again.', '</p>',
  '<p>The unit poem stays the same all five weeks. This week the lessons also include two short original poems on Days 2 and 4.')
between('<p><strong>How to help:</strong>', '</p>',
  '<p><strong>How to help:</strong> Ask your student how the poem fits the trees waking in Chapter 11.')

between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">What did Aslan mean when he said Lucy would find him bigger every year?</span><span class="listen">Listen for: Aslan isn’t growing; Lucy is, and as she grows she understands more of him.</span></li><li><span class="q">Why was it hard for Lucy to wake the others?</span><span class="listen">Listen for: they couldn’t see Aslan, and each time she told it, it sounded less convincing.</span></li><li><span class="q">What did Susan and Peter admit?</span><span class="listen">Listen for: Susan had believed Lucy deep down but didn’t want to; Peter had been leading them wrong.</span></li><li><span class="q">What happened when Aslan roared?</span><span class="listen">Listen for: the trees woke up and came toward him in human shapes, dancing.</span></li><li><span class="q">What did Nikabrik want to do, and why was it wrong?</span><span class="listen">Listen for: call back the White Witch; she was cruel, and Caspian and the Badger refused.</span></li><li><span class="q">Which pillar did you see most this week?</span><span class="listen">Listen for: a pillar and a real moment from Chapters 10–12.</span></li>')
between('<ul class="check"><li><strong>Each lesson:</strong>', '</ul>',
  '<ul class="check"><li><strong>Each lesson:</strong> 3 chapter questions plus word-study and writing responses, submitted in Canvas</li><li><strong>Writing:</strong> a draft theme paragraph on Day 4</li><li><strong>Fluency:</strong> a recording of a passage from Chapter 10</li><li><strong>Check-In:</strong> at the end of the week</li>')
between('<strong>Done well looks like:</strong>', '</p>',
  '<strong>Done well looks like:</strong> a theme sentence that is true about people, not only about Narnia, with two moments from the book that show it.')
between('<ul class="check"><li><strong>Tell the same story two ways.</strong>', '</ul>',
  '<ul class="check"><li><strong>Talk about a time</strong> someone in the family said “I’m sorry, I was wrong.” Was it hard?</li><li><strong>Watch the trees</strong> on a windy day and read “Who Has Seen the Wind?” together.</li><li><strong>Ask your student</strong> to say this week’s theme sentence at dinner, and test it on a family story</li>')
between('<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>\n    <p><strong><em>Prince Caspian</em></strong> by C. S. Lewis · <strong>A device that records audio</strong> for the fluency reading</p>\n  ')
between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 26</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 30</h2></div>\n    <p><strong><em>Prince Caspian</em>, Chapters 13–15, the end of the book.</strong> Peter challenges Miraz to single combat, the trees join the battle, and Aslan makes a door in the air.</p>\n  ')
s = s.replace('href="parent-guide-ft-unit.html"', 'href="parent-guide-pc-unit.html"').replace('See the whole Freedom Train unit →', 'See the whole Prince Caspian unit →')
import re
s = re.sub(r'\n\s*<td colspan="2">A 14-point wrap-up on the whole book:.*?</td>', '', s, count=1)
io.open('parent-guide-week-29.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('Freedom'), s.count('Harriet'), s.count('Marcus'), s.count('25.'))
