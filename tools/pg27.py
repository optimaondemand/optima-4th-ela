#!/usr/bin/env python3
"""parent-guide-week-27.html from the week 25 guide (same look). Prince Caspian Ch. 4-6, checked against the text."""
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

between('<title>', '</title>', '<title>Week 27 Family Guide · Prince Caspian Ch. 4–6 · 4th Grade ELA')
between('<h1>', '</h1>', '<h1>Week 27: The Prince in Hiding')
between('<div class="sub">', '</div>', '<div class="sub"><em>Prince Caspian</em> by C. S. Lewis, Chapters 4–6')
between('<div class="chips">', '</div>', '<div class="chips">\n        <span class="chip">4 lessons</span>\n        <span class="chip">1 fluency recording</span>\n        <span class="chip">Ch. 4–6</span>\n        <span class="chip">A story inside a story</span>\n        <span class="chip">Check-In at week’s end</span>\n      ')
s = s.replace("assets/covers/ft.jpg');background-position:center 35%;", "assets/covers/pc.jpg');background-position:center 35%;")
s = s.replace('aria-label="Cover of Freedom Train by Dorothy Sterling"', 'aria-label="Cover of Prince Caspian by C. S. Lewis"')
s = s.replace('Week 25', 'Week 27')

sec('This Week at a Glance', '''
    <div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
    <p>The Dwarf the children rescued tells them a story, and for three chapters we hear it with them. Prince Caspian grows up in his uncle Miraz’s castle, where the old stories of Talking Beasts are forbidden. His tutor, Doctor Cornelius, tells him in secret that they are true. When Miraz’s own son is born, Caspian has to run for his life, and he finds the Old Narnians who have been hiding for hundreds of years. Each day your student also writes a short Writing Connection.</p>
    <div class="box b-rose" style="margin-bottom:12px;"><div class="box-label">💛 A heads-up for families</div>In Chapter 5, Doctor Cornelius tells Caspian that Miraz murdered his father, and that Miraz will now want Caspian out of the way too. Caspian escapes at night. Later, a Dwarf named Nikabrik reaches for his dagger, and two friends stop him. Nobody is hurt.</div>
    <div class="glance">
      <div class="box b-sky"><div class="box-label">Reading skill</div><strong>Keeping track of groups of characters.</strong> Your student sorts every new character onto two lists, with Caspian or against him, and asks what each group wants.</div>
      <div class="box b-green"><div class="box-label">Big idea</div><strong>The truth kept alive in secret.</strong> A nurse, a tutor, a Badger and a Centaur have all held on to the old stories when it was dangerous to.</div>
    </div>
    <p class="quote">“Certainly it is true … Their reign was the Golden Age in Narnia and the land has never forgotten them.”<small>Doctor Cornelius, Chapter 4</small></p>
  ''')

rows = '''        <tr>
          <td class="day-n">27.1<span>Day 1</span></td>
          <td><span class="ch">Chapter 4 · The Dwarf Tells of Prince Caspian</span><br>Caspian loves his nurse’s stories of Old Narnia, until his uncle sends her away. His new tutor, Doctor Cornelius, takes him up a tower at night and tells him the stories are true.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Copia: Say It Three Ways</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>Why would the truth ever need to be hidden?</td>
        </tr>
        <tr>
          <td class="day-n">27.2<span>Day 2</span></td>
          <td><span class="ch">Chapter 5 · Caspian’s Adventure in the Mountains</span><br>The Doctor wakes Caspian with terrible news and gives him Queen Susan’s horn, to use only at his greatest need. After a wild ride in a storm, Caspian wakes in a Badger’s cave with two Dwarfs, who do not agree about him.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>Who welcomes Caspian, who doesn’t, and why?</td>
        </tr>
        <tr>
          <td class="day-n">27.3<span>Day 3</span></td>
          <td><span class="ch">Chapter 6 · The People That Lived in Hiding</span><br>Caspian meets the hidden Old Narnians one by one: three sleepy bears, a squirrel, Dwarfs at a forge, a Centaur who reads the stars, a very brave Mouse, and Fauns dancing in the moonlight.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>How do you keep track of so many new characters, and what does each group want?</td>
        </tr>
        <tr>
          <td class="day-n">27.4<span>Day 4</span></td>
          <td><span class="ch">Chapters 4–6 · looking back</span><br>No new chapter. Your student lines up every group from the week, says what each wants, writes a paragraph comparing two characters, and names the week’s strongest pillar.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What changed for Caspian this week, and what made the change possible?</td>
        </tr
'''
i = s.index('        <tr>\n          <td class="day-n">25.1'); j = s.index('        <tr class="extra-row">', i)
s = s[:i] + rows.replace('</tr\n', '</tr>\n') + s[j:]
between('<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">', ' Your student reads it three times',
        '<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">A passage from Chapter 6: Glenstorm the Centaur speaks about the stars, and then the Fauns come dancing out of the wood.')
between('<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">', '</td>',
        '<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">A 14-point wrap-up: but and so, the Latin bases port, tract and struct, suffix spelling rules, and questions about keeping track of groups of characters, with real passages from Chapters 5 and 6.')

between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>tutor</b><span>a private teacher who teaches one student or a few</span></div><div class="word"><b>usurper</b><span>someone who takes a throne without the right to it</span></div><div class="word"><b>astronomy</b><span>the study of the stars, planets and sky</span></div><div class="word"><b>sternly</b><span>in a strict, serious way</span></div></div>\n    ')
between('<div class="box b-sky"><div class="box-label">Word parts</div>', '</div>\n      <div class="box b-gold">',
  '<div class="box b-sky"><div class="box-label">Word parts</div>Latin bases: <strong>port</strong> (carry), <strong>tract</strong> (pull), <strong>struct</strong> (build).<span class="eg">porter · tractor · structure</span>')
between('<div class="box b-gold"><div class="box-label">Spelling</div>', '</div>\n      <div class="box b-green">',
  '<div class="box b-gold"><div class="box-label">Spelling</div><strong>Suffix rules.</strong> Drop the silent e, change y to i, and double the last consonant when the last syllable has the beat.<span class="eg">hoping · emptier · beginning · visiting</span>')
between('<div class="box b-green"><div class="box-label">Grammar</div>', '</div>\n    </div>',
  '<div class="box b-green"><div class="box-label">Grammar</div><strong>But and so.</strong> <em>But</em> brings a surprise; <em>so</em> tells what happened because of it. A comma goes before each when it joins two whole sentences.<span class="eg">Caspian’s heart was sinking, but he tried to take it all in.</span>')

sec('New in the Lessons', '''
    <div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
    <p>Everything from last week continues: Nell, Fill the Treasure Chamber (on Days 1 and 3, with this week’s Latin bases), the Seven Pillars Watch after reading, and the reading lens. New this week:</p>
    <div class="extras">
      <div class="box b-plum"><div class="box-label">📋 Two lists while reading</div>On the Reading tab, note boxes ask your student to sort characters: with Caspian, against him, or not sure yet.</div>
      <div class="box b-gold"><div class="box-label">🎭 Two short original poems</div>“The Night Ride” (Day 2) and “The Ones Who Stay” (Day 4) were written for these lessons, about Caspian’s escape and about loyalty.</div>
    </div>
  ''')

sec('Your Student’s Research Report', '''
    <div class="card-head"><span class="ico">✍️</span><h2>Writing This Week</h2><span class="tag">Writing Connection</span></div>
    <p>This week builds toward a comparison paragraph. Day 1 compares Miraz and Doctor Cornelius in two or three sentences; Day 3 practices moving a reader from one scene to the next, the way Lewis does; Day 4 is a full paragraph (five to seven sentences) comparing two characters, with <em>but</em> and <em>so</em> and a detail from the book.</p>
  ''')

between('<div class="poem">', '</div>\n      <div>',
  '<div class="poem">The stones still stand where towers fell,<br>The river hums a half-lost spell,<br>The trees lean close as if to say,<br>“We knew you’d find your way back someday.”<small>“The Forest Remembers,” written for our Prince Caspian lessons</small>')
between('<p>On Days 2 and 4 your student says the four lines again.', '</p>',
  '<p>The unit poem stays the same all five weeks. This week the lessons also include two short original poems on Days 2 and 4.')
between('<p><strong>How to help:</strong>', '</p>',
  '<p><strong>How to help:</strong> Ask your student how the first two lines fit the Old Narnians, who have been hiding for hundreds of years.')

between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">Who is telling the story in these chapters, and who is listening?</span><span class="listen">Listen for: the Dwarf (Trumpkin) is telling it to Peter, Susan, Edmund and Lucy.</span></li><li><span class="q">Why did Miraz send Caspian’s nurse away?</span><span class="listen">Listen for: she told Caspian stories about Old Narnia, which Miraz had forbidden.</span></li><li><span class="q">Why did Caspian have to run away?</span><span class="listen">Listen for: Miraz’s wife had a son, so Miraz wanted his own son to be King and Caspian out of the way.</span></li><li><span class="q">What did Doctor Cornelius give Caspian, and what did he say about it?</span><span class="listen">Listen for: Queen Susan’s horn, to use only at his greatest need (and a purse of gold).</span></li><li><span class="q">Which Old Narnian did you like best, and why?</span><span class="listen">Listen for: a named character (Trufflehunter, Reepicheep, Glenstorm…) and a reason from the book.</span></li><li><span class="q">Which pillar did you see most this week?</span><span class="listen">Listen for: a pillar and a real moment from Chapters 4–6.</span></li>')
between('<ul class="check"><li><strong>Each lesson:</strong>', '</ul>',
  '<ul class="check"><li><strong>Each lesson:</strong> 3 chapter questions plus word-study and writing responses, submitted in Canvas</li><li><strong>Writing:</strong> a comparison paragraph on Day 4</li><li><strong>Fluency:</strong> a recording of a passage from Chapter 6</li><li><strong>Check-In:</strong> at the end of the week</li>')
between('<strong>Done well looks like:</strong>', '</p>',
  '<strong>Done well looks like:</strong> answers that name the character, say which side they are on, and give the moment in the book that shows it.')
between('<ul class="check"><li><strong>Tell the same story two ways.</strong>', '</ul>',
  '<ul class="check"><li><strong>Go outside on a clear night</strong> and find two bright planets or stars, the way Caspian and his tutor did from the tower.</li><li><strong>Make a family “who’s who”</strong> chart of the Old Narnians so far, with one word for each.</li><li><strong>Tell a story inside a story:</strong> one person tells, the other listens and asks questions, like the children listening to the Dwarf.</li>')
between('<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>\n    <p><strong><em>Prince Caspian</em></strong> by C. S. Lewis · <strong>A device that records audio</strong> for the fluency reading</p>\n  ')
between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 26</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 28</h2></div>\n    <p><strong><em>Prince Caspian</em>, Chapters 7–9.</strong> The Old Narnians hold their council, Caspian blows the horn, and the Dwarf’s story ends. Then the four children set out to find Caspian, and Lucy sees something the others don’t.</p>\n  ')
s = s.replace('href="parent-guide-ft-unit.html"', 'href="parent-guide-pc-unit.html"').replace('See the whole Freedom Train unit →', 'See the whole Prince Caspian unit →')
import re
s = re.sub(r'\n\s*<td colspan="2">A 14-point wrap-up on the whole book:.*?</td>', '', s, count=1)
io.open('parent-guide-week-27.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('Freedom'), s.count('Harriet'), s.count('Marcus'), s.count('25.'))
