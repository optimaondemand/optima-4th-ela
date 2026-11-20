#!/usr/bin/env python3
"""parent-guide-pc-unit.html (Unit 5: Prince Caspian, weeks 26-30) from the Freedom Train unit guide (same look).
Content checked against the lessons and the text; Lewis's book is under copyright, so quotes stay short."""
import io
s = io.open('parent-guide-ft-unit.html', encoding='utf-8').read()
def between(start, end, new, after=0):
    global s
    i = s.index(start, after); j = s.index(end, i + len(start))
    s = s[:i] + new + s[j:]
def sec(head_text, new_inner):
    global s
    k = s.index(head_text); i = s.rindex('<section', 0, k); i = s.index('>', i) + 1; j = s.index('</section>', k)
    s = s[:i] + new_inner + s[j:]

between('<title>', '</title>', '<title>Unit 5 Family Guide · Prince Caspian · 4th Grade ELA')
between('<h1>', '</h1>', '<h1>Unit 5: Prince Caspian')
between('<div class="sub">', '</div>', '<div class="sub">Weeks 26–30 · a Narnia novel · C. S. Lewis')
between('<div class="chips">', '</div>', '<div class="chips">\n        <span class="chip">5 weeks</span>\n        <span class="chip">20 lessons</span>\n        <span class="chip">15 chapters</span>\n        <span class="chip">1 paragraph a week</span>\n        <span class="chip">1 poem learned by heart</span>\n      ')
s = s.replace("assets/covers/ft.jpg');background-position:center 35%;", "assets/covers/pc.jpg');background-position:center 35%;")
s = s.replace('aria-label="Cover of Freedom Train by Dorothy Sterling"', 'aria-label="Cover of Prince Caspian by C. S. Lewis"')

sec('About the Book', '''
    <div class="card-head"><span class="ico">📕</span><h2>About the Book</h2></div>
    <p><em>Prince Caspian</em> (1951) is the second book C. S. Lewis published about Narnia. A year after their first adventure, Peter, Susan, Edmund and Lucy are pulled out of a train station and back into Narnia. But in Narnia, hundreds of years have passed. Their castle is a ruin, the talking animals and trees have gone into hiding, and a king named Miraz rules a land that no longer believes the old stories. His young nephew, Prince Caspian, believes them, and he needs help.</p>
    <p>We read it because it is a great adventure, and because it asks big questions in a way nine-year-olds can hold: what it takes to lead, why it’s hard to trust what you can’t see, and how to stay loyal when it costs you something. It also teaches readers to track several groups of characters at once, and to read a fantasy setting for clues.</p>
    <p class="small">The book is still under copyright, so the lessons quote only short lines. Your student needs the book itself.</p>
    <p class="quote">“This must have been an orchard — long, long ago…”<small>Susan, Chapter 1</small></p>
  ''')

between('<li><span>🌟</span><strong>Freedom Watch:</strong>', '</li>',
        '<li><span>🏛️</span><strong>Seven Pillars Watch:</strong> after each chapter, your student decides which of the seven OAO pillars (honesty, respect, courtesy, responsibility, courage, service, perseverance) real moments from the book show, and names the week’s strongest pillar on Day 4')
between('<li><span>🎧</span><strong>Marcus, the guide:</strong>', '</li>',
        '<li><span>🎧</span><strong>Nell, the guide:</strong> a bookbinder who mends old books and has read the Narnia books every winter since she was nine. She introduces lessons in short clips and leads a short Word Study film each day. (She is made up for our lessons; she is not a character in the book.)')
between('<li><span>🌌</span><strong>The quilt opening:</strong>', '</li>',
        '<li><span>🗝️</span><strong>Fill the Treasure Chamber:</strong> the word-parts game. In Chapter 2 the children find their castle’s old treasure chamber; each word your student builds sets a treasure back in its niche')
s = s.replace('<li><span>🎵</span><strong>Songs With a Hidden Meaning:</strong> real spirituals, with what an overseer heard and what the singers meant</li>\n', '')
between('<li><span>✍️</span><strong>Writer’s Workshop:</strong>', '</li>',
        '<li><span>✍️</span><strong>Writing Connection:</strong> a short piece of writing every day, and one full paragraph each week')

WK = [
 (26, 'Chapters 1–3', 'Back to Narnia', 'Pulled from a train station onto an island, the children find a ruined castle and work out that it is their own Cair Paravel, hundreds of Narnian years later. They rescue a Dwarf named Trumpkin.',
  [('Reading', 'reading a fantasy setting'), ('Grammar', 'and / or'), ('Spelling', 'long words, part by part'), ('Word parts', 'pre-, re-, trans-, inter-')], True),
 (27, 'Chapters 4–6', 'Caspian’s story', 'Trumpkin tells how young Caspian learned the old stories from his tutor, fled his uncle Miraz, and found the Old Narnians hiding in the woods.',
  [('Reading', 'tracking groups of characters'), ('Grammar', 'but / so'), ('Spelling', 'suffix rules'), ('Word roots', 'port, tract, struct')], False),
 (28, 'Chapters 7–9', 'Leaders and choices', 'Caspian blows Susan’s lost horn for help, and Trumpkin goes to meet whoever answers: the four children. On the way to Caspian, Lucy sees Aslan, and the others don’t believe her.',
  [('Reading', 'conflict and leadership'), ('Grammar', 'complex sentences'), ('Spelling', 'the schwa sound'), ('Word roots', 'spect, ject, script')], False),
 (29, 'Chapters 10–12', 'Believing', 'Aslan returns. Lucy follows him even when the others can’t see him, and one by one they do. Peter and Edmund reach Caspian just as a darker plan is made inside Aslan’s How.',
  [('Reading', 'theme'), ('Grammar', 'commas in dates and places'), ('Spelling', 'Greek and Latin parts'), ('Word roots', 'rupt, duct, form')], False),
 (30, 'Chapters 13–15', 'The rightful king', 'Peter challenges Miraz to single combat, the trees and Aslan come, and Caspian becomes king. The children go home.',
  [('Reading', 'how the ending lands'), ('Grammar', 'dialogue punctuation'), ('Spelling', 'year-end review'), ('Word roots', 'unit review')], False),
]
rows = ''
for w, ch, th, summ, sk, link in WK:
    rows += ('      <div class="wk"><div class="wk-n"><b>%d</b><span>Week</span></div><div class="wk-body">\n'
             '        <div class="wk-top"><span class="wk-ch">%s</span><span class="theme">%s</span></div>\n'
             '        <p class="wk-sum">%s</p>\n        <div class="skills">%s</div>\n%s      </div></div>\n') % (
        w, ch, th, summ, ''.join('<span class="sk"><i>%s</i>%s</span>' % x for x in sk),
        ('        <a class="wk-link" href="parent-guide-week-%d.html">Open the Week %d guide →</a>\n' % (w, w)) if link else '')
between('<div class="weeks">', '    </div>\n  </section>', '<div class="weeks">\n' + rows)

sec('Your Student’s Research Report', '''
    <div class="card-head"><span class="ico">✍️</span><h2>Writing in This Unit</h2><span class="tag">Writing Connection</span></div>
    <p>There is no long essay in this unit. Instead, your student writes a little every day, and each week ends with one full paragraph that uses that week’s grammar.</p>
    <div class="path path6">
      <div class="step"><b>Wk 26</b>What Lewis does well</div>
      <div class="step"><b>Wk 27</b>Compare two characters</div>
      <div class="step draft"><b>Wk 28</b>A claim about leadership</div>
      <div class="step draft"><b>Wk 29</b>A theme paragraph</div>
      <div class="step pub"><b>Wk 30</b>Peter’s choices</div>
    </div>
    <p class="small" style="margin-top:12px;">Writing saves in the browser on the computer your student uses, so <strong>if your student switches computers, help them keep a copy somewhere else too</strong>.</p>
  ''')

between('<div class="poem">', '</div>\n      <div>',
  '<div class="poem">The stones still stand where towers fell,<br>The river hums a half-lost spell,<br>The trees lean close as if to say,<br>“We knew you’d find your way back someday.”<small>“The Forest Remembers,” a short poem written for our Prince Caspian lessons</small>')
between('<p>Dunbar, the son of', '</p>',
  '<p>Four lines about a land that remembers the people who loved it, just as Narnia remembers the four children. Your student meets the poem in Week 26 and learns it by heart, with a few more words fading from the screen each time.')
between('<p><strong>How to help:</strong> Ask to hear it now and then.', '</p>',
  '<p><strong>How to help:</strong> Ask to hear it now and then. By Week 30 they should be able to say all four lines to you.')

between('<div class="box b-gold"><div class="box-label">Every week</div>', '</div>',
  '<div class="box b-gold"><div class="box-label">Every week</div>A fluency recording, a Day 4 paragraph, and a <strong>Check-In</strong> covering grammar, word parts, spelling and reading.')
between('<div class="box b-green"><div class="box-label">End of unit</div>', '</div>',
  '<div class="box b-green"><div class="box-label">End of unit</div>The Week 30 paragraph about Peter, and the Check-In on the book’s ending. The year-end comparison in Weeks 31–32 draws on this book too.')

sec('Good to Know Ahead of Time', '''
    <div class="card-head"><span class="ico">💛</span><h2>Good to Know Ahead of Time</h2></div>
    <div class="grid2">
      <div class="box b-rose"><div class="box-label">The whole unit · battles</div>Narnia is at war. There are sword fights and a battle at the end, told for young readers without gore. A few characters die, mostly in battle.</div>
      <div class="box b-rose"><div class="box-label">Faith and Aslan</div>Aslan, the great lion, is at the heart of the book. Lewis was a Christian, and many readers see Christian ideas in Aslan. The lessons treat the book as literature: trust, belief and courage, in the story’s own terms.</div>
      <div class="box b-plum"><div class="box-label">Week 26 · Chapter 3</div>Two soldiers are about to drown a tied-up Dwarf. Susan shoots an arrow that knocks one into the water; nobody is killed.</div>
      <div class="box b-plum"><div class="box-label">Week 27 · Chapters 4–5</div>Caspian’s tutor tells him that his uncle Miraz murdered Caspian’s father to take the throne, and that Caspian is now in danger.</div>
      <div class="box b-plum"><div class="box-label">Week 29 · Chapter 12</div>Some of Caspian’s own side try to call up an evil witch to help them. It is a short, dark scene, and a fight follows.</div>
      <div class="box b-plum"><div class="box-label">Week 30 · Chapters 13–15</div>Peter fights Miraz one on one, and a battle follows. The ending is joyful.</div>
    </div>
  ''')

between('<li>Ask “What is this chapter mostly about?” and “How do you know?”</li>', '</ul>',
  '<li>Ask “What is this chapter mostly about?” and “How do you know?”</li>\n          <li>Keep a simple list of who is on Caspian’s side and who is with Miraz. There are a lot of characters.</li>\n          <li>Ask which pillar a character showed today, and why.</li>\n          <li>Be the audience for the fluency reading and the poem.</li>\n        ')
between('<li>Doing the research for them.', '</ul>',
  '<li>Telling them what happens next. The lessons ask for predictions before each chapter.</li>\n          <li>Showing the movie first. It changes many parts of the story, and the questions are about the book.</li>\n        ')
sec('Family Bookshelf', '''
    <div class="card-head"><span class="ico">📚</span><h2>Family Bookshelf</h2><span class="tag">Optional</span></div>
    <p class="small">For students who want more, or for reading aloud together.</p>
    <div class="books">
      <div class="book"><b>The Lion, the Witch and the Wardrobe</b><span>C. S. Lewis. The children’s first trip to Narnia, which Prince Caspian looks back on.</span></div>
      <div class="book"><b>The Voyage of the Dawn Treader</b><span>C. S. Lewis. The next adventure, with Caspian as king, Edmund and Lucy, and Reepicheep the mouse.</span></div>
      <div class="book"><b>The Hobbit</b><span>J. R. R. Tolkien. A grand fantasy by Lewis’s close friend, for strong readers or reading aloud.</span></div>
      <div class="book"><b>Castles</b><span>Any good illustrated nonfiction book about medieval castles, to picture Cair Paravel and Miraz’s castle.</span></div>
    </div>
  ''')
between('<p class="foot">', '<br>', '<p class="foot">Optima Academy Online · 4th Grade ELA · Unit 5 Family Guide')
io.open('parent-guide-pc-unit.html', 'w', encoding='utf-8').write(s)
print('ok', s.count('Freedom'), s.count('Harriet'), s.count('Marcus'), s.count('Sterling'))
