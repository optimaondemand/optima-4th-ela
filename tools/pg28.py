#!/usr/bin/env python3
"""parent-guide-week-28.html from the week 25 guide (same look). Prince Caspian Ch. 7-9, checked against the text."""
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

between('<title>', '</title>', '<title>Week 28 Family Guide · Prince Caspian Ch. 7–9 · 4th Grade ELA')
between('<h1>', '</h1>', '<h1>Week 28: Hard Choices')
between('<div class="sub">', '</div>', '<div class="sub"><em>Prince Caspian</em> by C. S. Lewis, Chapters 7–9')
between('<div class="chips">', '</div>', '<div class="chips">\n        <span class="chip">4 lessons</span>\n        <span class="chip">1 fluency recording</span>\n        <span class="chip">Ch. 7–9</span>\n        <span class="chip">Leadership</span>\n        <span class="chip">Check-In at week’s end</span>\n      ')
s = s.replace("assets/covers/ft.jpg');background-position:center 35%;", "assets/covers/pc.jpg');background-position:center 35%;")
s = s.replace('aria-label="Cover of Freedom Train by Dorothy Sterling"', 'aria-label="Cover of Prince Caspian by C. S. Lewis"')
s = s.replace('Week 25', 'Week 28')

sec('This Week at a Glance', '''
    <div class="card-head"><span class="ico">🧭</span><h2>This Week at a Glance</h2></div>
    <p>Caspian’s army of Old Narnians holds its council, retreats to an ancient mound called Aslan’s How, and starts losing the war. On the worst night, Caspian blows Queen Susan’s Horn, and Trumpkin goes to meet whoever answers. That is how the Dwarf’s story ends. Then the four children set out to find Caspian, and at the edge of a gorge Lucy sees Aslan when no one else does. The group votes, and she loses. Each day your student also writes a short Writing Connection.</p>
    <div class="box b-rose" style="margin-bottom:12px;"><div class="box-label">💛 A heads-up for families</div>Chapter 7 describes Caspian’s side losing battles: a Bear and a Centaur are badly hurt. Nikabrik offers to kill Doctor Cornelius, and Caspian stands up for his old tutor. No one is killed in these chapters.</div>
    <div class="glance">
      <div class="box b-sky"><div class="box-label">Reading skill</div><strong>Conflict and leadership choices.</strong> Your student names who is set against whom, what is at stake, and the moment someone has to decide.</div>
      <div class="box b-green"><div class="box-label">Big idea</div><strong>What a leader does when the choice is hard.</strong> Caspian at the council, Peter at the gorge, and Edmund standing up for his sister.</div>
    </div>
    <p class="quote">“I know the difference between giving advice and taking orders.”<small>Trumpkin, Chapter 7</small></p>
  ''')

rows = '''        <tr>
          <td class="day-n">28.1<span>Day 1</span></td>
          <td><span class="ch">Chapter 7 · Old Narnia in Danger</span><br>At the great council every group wants something different. Doctor Cornelius arrives with a warning, and the army moves to Aslan’s How. After a terrible defeat, Caspian decides to blow the Horn, and Trumpkin volunteers to go to Cair Paravel.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Copia: Say It Three Ways</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>When everyone around a leader is arguing, what should the leader do?</td>
        </tr>
        <tr>
          <td class="day-n">28.2<span>Day 2</span></td>
          <td><span class="ch">Chapter 8 · How They Left the Island</span><br>The children prove who they are to a doubtful Trumpkin: Edmund beats him with swords, Susan beats him at archery, and Lucy heals his wound with her cordial. Then they row toward Caspian along the coast.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What does leading look like when there’s no battle to fight?</td>
        </tr>
        <tr>
          <td class="day-n">28.3<span>Day 3</span></td>
          <td><span class="ch">Chapter 9 · What Lucy Saw</span><br>At the edge of a deep gorge, Lucy sees Aslan, and the others don’t. The group votes. Edmund sides with Lucy; Peter, Susan and Trumpkin vote to go the other way.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-extra">Read · Write · Mimic</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What does a vote tell you about the person who casts it?</td>
        </tr>
        <tr>
          <td class="day-n">28.4<span>Day 4</span></td>
          <td><span class="ch">Chapters 7–9 · looking back</span><br>No new chapter. Your student judges one hard choice from the week, writes a paragraph about what makes a good leader, and names the week’s strongest pillar.<br><span class="pill p-guide">Guide: Nell</span><span class="pill p-poem">Poetry Corner</span><span class="pill p-extra">Seven Pillars Watch</span></td>
          <td>What makes a good leader, and which choice this week proves it?</td>
        </tr
'''
i = s.index('        <tr>\n          <td class="day-n">25.1'); j = s.index('        <tr class="extra-row">', i)
s = s[:i] + rows.replace('</tr\n', '</tr>\n') + s[j:]
between('<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">', ' Your student reads it three times',
        '<td class="day-n">🎙️<span>Fluency</span></td>\n          <td colspan="2">A passage from Chapter 7: Trumpkin volunteers to carry the message, even though he doesn’t believe in the Horn.')
between('<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">', '</td>',
        '<td class="day-n">📋<span>Check-In</span></td>\n          <td colspan="2">A 14-point wrap-up: complex sentences, the Latin bases spect, ject and script/scribe, the schwa sound, and questions about Peter’s choice at the gorge, with real passages from Chapters 7 and 9.')

between('<div class="words">', '<div class="skills">',
  '<div class="words"><div class="word"><b>council</b><span>a group gathered to talk and decide</span></div><div class="word"><b>entrenchments</b><span>ditches and banks dug for defense</span></div><div class="word"><b>consorts</b><span>companions, especially of a king or queen</span></div><div class="word"><b>gorge</b><span>a deep, narrow valley with steep sides</span></div></div>\n    ')
between('<div class="box b-sky"><div class="box-label">Word parts</div>', '</div>\n      <div class="box b-gold">',
  '<div class="box b-sky"><div class="box-label">Word parts</div>Latin bases: <strong>spect</strong> (look), <strong>ject</strong> (throw), <strong>script / scribe</strong> (write).<span class="eg">respect · eject · scribe</span>')
between('<div class="box b-gold"><div class="box-label">Spelling</div>', '</div>\n      <div class="box b-green">',
  '<div class="box b-gold"><div class="box-label">Spelling</div><strong>The schwa sound.</strong> The lazy “uh” in an unstressed syllable can’t be heard, so find a related word where that vowel is loud.<span class="eg">opposite (from oppose)</span>')
between('<div class="box b-green"><div class="box-label">Grammar</div>', '</div>\n    </div>',
  '<div class="box b-green"><div class="box-label">Grammar</div><strong>Complex sentences.</strong> A clause that starts with <em>because, although, when</em> or <em>if</em> can’t stand alone; it leans on the main clause. When it comes first, a comma follows it.<span class="eg">If we start at once, we can be at the head of Glasswater before dark.</span>')

sec('New in the Lessons', '''
    <div class="card-head"><span class="ico">✨</span><h2>New in the Lessons</h2></div>
    <p>Nell, the Seven Pillars Watch and the reading lens continue. This week:</p>
    <div class="extras">
      <div class="box b-plum"><div class="box-label">⚖️ Catching the choice</div>Note boxes on the Reading tab ask your student to record each side of an argument and the moment someone decides: the council, the rowing, the vote at the gorge.</div>
      <div class="box b-gold"><div class="box-label">🎭 Two short original poems</div>“The Summons” (Day 2) and “What I Saw” (Day 4) were written for these lessons, about being called and about being right when no one believes you.</div>
      <div class="box b-sky"><div class="box-label">🗝️ No treasure game this week</div>This week’s word-base activities are tap-and-choose, so the treasure chamber rests until a fill-in week.</div>
    </div>
  ''')

sec('Your Student’s Research Report', '''
    <div class="card-head"><span class="ico">✍️</span><h2>Writing This Week</h2><span class="tag">Writing Connection</span></div>
    <p>This week builds toward a claim paragraph. Day 1 is two or three sentences about a time a group couldn’t agree; Days 2 and 3 practice Lewis’s sentence patterns (a string of “Do you remember…” questions, and one plain sentence that shows a choice); Day 4 is a full paragraph (five to seven sentences) about what makes a good leader, with two pieces of evidence from Chapters 7–9.</p>
  ''')

between('<div class="poem">', '</div>\n      <div>',
  '<div class="poem">The stones still stand where towers fell,<br>The river hums a half-lost spell,<br>The trees lean close as if to say,<br>“We knew you’d find your way back someday.”<small>“The Forest Remembers,” written for our Prince Caspian lessons</small>')
between('<p>On Days 2 and 4 your student says the four lines again.', '</p>',
  '<p>The unit poem stays the same all five weeks. This week the lessons also include two short original poems on Days 2 and 4.')
between('<p><strong>How to help:</strong>', '</p>',
  '<p><strong>How to help:</strong> Ask your student which lines fit Lucy at the gorge.')

between('<ol class="ask">', '</ol>',
  '<ol class="ask"><li><span class="q">What did the different groups want at the council?</span><span class="listen">Listen for: the Bears wanted supper first, the Mice wanted to attack at once, the Moles wanted to dig, the Fauns wanted to dance.</span></li><li><span class="q">Why did Caspian wait so long to blow the Horn?</span><span class="listen">Listen for: he was told to use it only at his greatest need, and he worried there might be a worse need later.</span></li><li><span class="q">Why did Trumpkin go to Cair Paravel if he didn’t believe in the Horn?</span><span class="listen">Listen for: Caspian was his King; he gave his advice, then followed orders.</span></li><li><span class="q">How did the children prove to Trumpkin who they were?</span><span class="listen">Listen for: Edmund’s sword fight, Susan’s archery, Lucy healing his shoulder.</span></li><li><span class="q">How did each person vote at the gorge, and was Peter right?</span><span class="listen">Listen for: Edmund voted with Lucy; Peter, Susan and Trumpkin voted to go down. Any opinion, with a reason.</span></li><li><span class="q">Which pillar did you see most this week?</span><span class="listen">Listen for: a pillar and a real moment from Chapters 7–9.</span></li>')
between('<ul class="check"><li><strong>Each lesson:</strong>', '</ul>',
  '<ul class="check"><li><strong>Each lesson:</strong> 3 chapter questions plus word-study and writing responses, submitted in Canvas</li><li><strong>Writing:</strong> a claim paragraph about leadership on Day 4</li><li><strong>Fluency:</strong> a recording of a passage from Chapter 7</li><li><strong>Check-In:</strong> at the end of the week</li>')
between('<strong>Done well looks like:</strong>', '</p>',
  '<strong>Done well looks like:</strong> answers that name the choice, say what the person was up against, and point to the moment in the book that proves the answer.')
between('<ul class="check"><li><strong>Tell the same story two ways.</strong>', '</ul>',
  '<ul class="check"><li><strong>Hold a family council</strong> about something small (dinner, a weekend plan). Afterward, talk about who decided and how.</li><li><strong>Try a fair vote</strong> where everyone gives a reason first, like the children at the gorge.</li><li><strong>Talk about a time</strong> someone in the family was right when no one believed them</li>')
between('<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🎒</span><h2>Have on Hand</h2></div>\n    <p><strong><em>Prince Caspian</em></strong> by C. S. Lewis · <strong>A device that records audio</strong> for the fluency reading</p>\n  ')
between('<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 26</h2></div>', '</section>',
  '<div class="card-head"><span class="ico">🔭</span><h2>Coming Up in Week 29</h2></div>\n    <p><strong><em>Prince Caspian</em>, Chapters 10–12.</strong> Lucy wakes in the night and finds Aslan. The children follow him, one by one, and some of them see him at last. Meanwhile, in Aslan’s How, Nikabrik brings two strange guests to Caspian’s council.</p>\n  ')
s = s.replace('href="parent-guide-ft-unit.html"', 'href="parent-guide-pc-unit.html"').replace('See the whole Freedom Train unit →', 'See the whole Prince Caspian unit →')
import re
s = re.sub(r'\n\s*<td colspan="2">A 14-point wrap-up on the whole book:.*?</td>', '', s, count=1)
io.open('parent-guide-week-28.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('Freedom'), s.count('Harriet'), s.count('Marcus'), s.count('25.'))
