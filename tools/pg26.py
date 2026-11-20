#!/usr/bin/env python3
"""parent-guide-week-26.html from the week 25 guide (same look). Prince Caspian Ch. 1-3, checked against the text."""
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

between('<title>', '</title>', '<title>Week 26 Family Guide · Prince Caspian Ch. 1–3 · 4th Grade ELA')
between('<h1>', '</h1>', '<h1>Week 26: Back to Narnia')
between('<div class="sub">', '</div>', '<div class="sub"><em>Prince Caspian</em> by C. S. Lewis, Chapters 1–3')
between('<div class="chips">', '</div>', '<div class="chips">\n        <span class="chip">4 lessons</span>\n        <span class="chip">1 fluency recording</span>\n        <span class="chip">Ch. 1–3</span>\n        <span class="chip">A new book</span>\n        <span class="chip">Check-In at week’s end</span>\n      ')
s = s.replace("assets/covers/ft.jpg');background-position:center 35%;", "assets/covers/pc.jpg');background-position:center 35%;")
s = s.replace('aria-label="Cover of Freedom Train by Dorothy Sterling"', 'aria-label="Cover of Prince Caspian by C. S. Lewis"')
s = s.replace('Week 25', 'Week 26')

sec('This Week at a Glance', '''
    <div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
    <p>A new book begins. Peter, Susan, Edmund and Lucy are waiting at a train station when they are pulled away to a wild island. They find an old orchard and a ruined castle, and work out that it is their own Cair Paravel from their first adventure in Narnia: hundreds of Narnian years have passed while only one passed in England. Then they rescue a Dwarf from two soldiers, and he tells them he is a messenger of “King Caspian.” Each day your student also writes a short Writing Connection.</p>
    <div class="box b-rose" style="margin-bottom:12px;"><div class="box-label">💛 A heads-up for families</div>In Chapter 3, two soldiers are about to drown a tied-up Dwarf. Susan shoots an arrow that knocks one soldier into the water; both soldiers get away, and nobody is killed. The full list for the book is on the <a href="parent-guide-pc-unit.html" style="color:#A8434A;font-weight:700;">unit guide</a>.</div>
    <div class="glance">
      <div class="box b-sky"><div class="box-label">Reading skill</div><strong>Reading a fantasy setting.</strong> Your student collects place clues (what the children see and touch) and time clues (what has crumbled or grown wild), then says where and when the children are in one sentence.</div>
      <div class="box b-green"><div class="box-label">Big idea</div><strong>Coming back to a place that has changed.</strong> The children remember a castle full of life. They find a ruin, and have to figure out what happened while they were gone.</div>
    </div>
    <p class="quote">“This must have been an orchard — long, long ago…”<small>Susan, Chapter 1</small></p>
  ''')

rows = '''        <tr>
          <td class="day-n">26.1<span>Day 1</span></td>
          <td><span class="ch">Chapter 1 · The Island</span><br>The children are pulled from a train station into a thick wood on an island. Hungry and thirsty, they find a stream, an orchard gone wild, and an old stone wall.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Copia: Say It Three Ways</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What kind of place have they arrived at, and what clues tell you?</td>
        </tr>
        <tr>
          <td class="day-n">26.2<span>Day 2</span></td>
          <td><span class="ch">Chapter 2 · The Ancient Treasure House</span><br>Susan finds a little golden chess-knight. Peter lays out the clues: this is Cair Paravel. Behind the ivy they find the door to the treasure chamber, and their old gifts. Susan’s horn is missing.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">By Heart poem</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What new details do you learn about this place, and how is the children’s understanding of it changing?</td>
        </tr>
        <tr>
          <td class="day-n">26.3<span>Day 3</span></td>
          <td><span class="ch">Chapter 3 · The Dwarf</span><br>Edmund works out that Narnian time runs differently. Then the children save a Dwarf from two soldiers. He tells them he is a messenger of King Caspian.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What does this rescue tell us about the children, and about the world they’ve returned to?</td>
        </tr>
        <tr>
          <td class="day-n">26.4<span>Day 4</span></td>
          <td><span class="ch">Chapters 1–3 · looking back</span><br>No new chapter. Your student traces how the setting grew from Chapter 1 to Chapter 3, picks one treasure and what it means, and names the week’s strongest pillar.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">By Heart poem</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What kind of story do you think this is going to be, and what clues have you seen so far?</td>
        </tr
'''
i = s.index('        <tr>\n          <td class="day-n">25.1'); j = s.index('        <tr class="extra-row">', i)
s = s[:i] + rows.replace('</tr\n', '</tr>\n') + s[j:]
between('<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">', ' Your student reads it three times',
        '<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">A passage from Chapter 2, when Peter holds up his old sword and sounds like the High King again.')
between('<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">', '</td>',
        '<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">A 14-point wrap-up: and / or, the prefixes pre-, re-, trans- and inter-, splitting long words, and questions about the fantasy setting, with real passages from Chapters 1 and 2.')

between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>junction</b><span>a place where things meet, especially where train lines split</span></div><div class="word"><b>thicket</b><span>a dense group of bushes or small trees</span></div><div class="word"><b>brambles</b><span>thorny bushes with prickly stems</span></div><div class="word"><b>inhabited</b><span>lived in</span></div></div>\n    ')
between('<div class="box b-sky"><div class="box-label">Word parts</div>', '</div>\n      <div class="box b-gold">',
  '<div class="box b-sky"><div class="box-label">Word parts</div>Prefixes that tell when and where: <strong>pre-</strong> (before), <strong>re-</strong> (again, back), <strong>trans-</strong> (across), <strong>inter-</strong> (between).<span class="eg">preview · return · transport · international</span>')
between('<div class="box b-gold"><div class="box-label">Spelling</div>', '</div>\n      <div class="box b-green">',
  '<div class="box b-gold"><div class="box-label">Spelling</div><strong>Long words, part by part.</strong> Peel off the prefix and suffix first; what’s left is a word you know, and the syllables split easily.<span class="eg">un · familiar · transport · ed</span>')
between('<div class="box b-green"><div class="box-label">Grammar</div>', '</div>\n    </div>',
  '<div class="box b-green"><div class="box-label">Grammar</div><strong>And and or.</strong> <em>And</em> joins ideas that are both true; <em>or</em> offers a choice. Too many <em>ands</em> in a row make every idea sound the same.<span class="eg">stay in the castle or ride into the woods</span>')

sec('New in the Lessons', '''
    <div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
    <p>The lesson pages work the same way as in Freedom Train. New for this book:</p>
    <div class="extras">
      <div class="box b-rose"><div class="box-label">🎧 Nell, the new guide</div>Nell is a bookbinder who mends old books and has read the Narnia books every winter since she was nine. She welcomes each lesson and leads a short captioned film on the Word Study tab. (She is made up for our lessons; she is not in the book.)</div>
      <div class="box b-plum"><div class="box-label">🗝️ Fill the Treasure Chamber</div>On Days 1 and 3, each word your student builds sets a treasure back in the castle’s old treasure chamber, four a day, until every torch is lit.</div>
      <div class="box b-gold"><div class="box-label">🏛️ Seven Pillars Watch, after reading</div>Real moments from the chapter, and your student taps which of the seven OAO pillars each one shows: honesty, respect, courtesy, responsibility, courage, service or perseverance. On Day 4, they name the week’s strongest pillar and prove it.</div>
      <div class="box b-sky"><div class="box-label">🔍 Reading lens</div>Before reading, your student picks one of three lenses and reads through it. One line at the end of the questions asks what it helped them notice.</div>
      <div class="box b-green"><div class="box-label">🪶 A new poem to learn</div>“The Forest Remembers,” four lines about a land that remembers the people who loved it.</div>
      <div class="box b-sky"><div class="box-label">✎ Copia: Say It Three Ways</div>On Day 1, your student rewrites “The children found an old stone wall” three ways: a new opening, a stronger verb, and an added detail.</div>
    </div>
  ''')

sec('Your Student’s Research Report', '''
    <div class="card-head"><span class="ico">✍️</span><h2>Writing This Week</h2><span class="tag">Writing Connection</span></div>
    <p>No long essay in this unit. Each day ends with a short Writing Connection: Day 1 compares the train station with the island, Day 2 describes a place that changed, Day 3 retells a moment from Trumpkin’s point of view, and Day 4 names one thing C. S. Lewis does well as a writer, with an example.</p>
  ''')

between('<div class="poem">', '</div>\n      <div>',
  '<div class="poem">The stones still stand where towers fell,<br>The river hums a half-lost spell,<br>The trees lean close as if to say,<br>“We knew you’d find your way back someday.”<small>“The Forest Remembers,” written for our Prince Caspian lessons</small>')
between('<p>On Days 2 and 4 your student says the four lines again.', '</p>',
  '<p>A new poem for a new book. On Day 2 your student reads it and starts learning it; on Day 4 a few words fade from the screen.')
between('<p><strong>How to help:</strong>', '</p>',
  '<p><strong>How to help:</strong> Ask your student who “you” is in the last line. Then ask how the poem fits the children coming back to Cair Paravel.')

between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">How did the children get to Narnia this time?</span><span class="listen">Listen for: they were sitting at a train station and felt a pull; then they were standing in a thick wood.</span></li><li><span class="q">How did they figure out the ruin was Cair Paravel?</span><span class="listen">Listen for: Peter’s clues, such as the shape of the hall, the well, the chess-knight, and the orchard.</span></li><li><span class="q">Why did the castle look so old if they had only been gone a year?</span><span class="listen">Listen for: Edmund’s idea that time in Narnia runs differently, so hundreds of years passed there.</span></li><li><span class="q">What gifts did they find in the treasure chamber? What was missing?</span><span class="listen">Listen for: Lucy’s cordial, Susan’s bow, Peter’s sword and shield; Susan’s horn was gone.</span></li><li><span class="q">Who did the children rescue, and what did he tell them?</span><span class="listen">Listen for: a Dwarf the soldiers were about to drown; he is a messenger of King Caspian.</span></li><li><span class="q">Which pillar did you see most this week?</span><span class="listen">Listen for: a pillar and a real moment from Chapters 1–3.</span></li>')
between('<ul class="check"><li><strong>Each lesson:</strong>', '</ul>',
  '<ul class="check"><li><strong>Each lesson:</strong> 3 chapter questions plus word-study and writing responses, submitted in Canvas</li><li><strong>Writing Connection:</strong> a short piece each day</li><li><strong>Fluency:</strong> a recording of a passage from Chapter 2</li><li><strong>Check-In:</strong> at the end of the week</li>')
between('<strong>Done well looks like:</strong>', '</p>',
  '<strong>Done well looks like:</strong> answers that point to a specific detail the children saw, heard or found, and say what it tells the reader about Narnia now.')
between('<ul class="check"><li><strong>Tell the same story two ways.</strong>', '</ul>',
  '<ul class="check"><li><strong>Visit a place from long ago</strong> (an old house, a park, a photo of where you grew up) and talk about what time changed.</li><li><strong>Ask your student to predict</strong> who King Caspian is, and write it down to check later.</li><li><strong>Look at pictures of real castle ruins</strong> and find the hall, the tower and the well.</li>')
between('<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>\n    <p><strong><em>Prince Caspian</em></strong> by C. S. Lewis · <strong>A device that records audio</strong> for the fluency reading</p>\n  ')
between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 26</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 27</h2></div>\n    <p><strong><em>Prince Caspian</em>, Chapters 4–6.</strong> The Dwarf tells the story of Prince Caspian: his tutor, his uncle Miraz, his escape, and the Old Narnians hiding in the woods.</p>\n  ')
s = s.replace('href="parent-guide-ft-unit.html"', 'href="parent-guide-pc-unit.html"').replace('See the whole Freedom Train unit →', 'See the whole Prince Caspian unit →')
import re
s = re.sub(r'\n\s*<td colspan="2">A 14-point wrap-up on the whole book:.*?</td>', '', s, count=1)
io.open('parent-guide-week-26.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('Freedom'), s.count('Harriet'), s.count('Marcus'), s.count('25.'))
