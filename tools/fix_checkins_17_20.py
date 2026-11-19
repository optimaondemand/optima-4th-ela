#!/usr/bin/env python3
"""Weeks 17-20 check-in pages: replace invented 'book passages' with real ones.
17-19 now match the QTIs fixed on Oct 11 2026 (passages checked against the NTS page images).
20: real Freedom Train passages (Sterling Ch. 3 pp. 37-38, Ch. 4 p. 40).
Run from the repo root:  python3 tools/fix_checkins_17_20.py"""
import io, re, sys

def patch(fn, pairs):
    s = io.open(fn, encoding='utf-8', newline='').read()
    for a, b in pairs:
        if a not in s and '\r\n' in s:
            a, b = a.replace('\n', '\r\n'), b.replace('\r\n', '\n').replace('\n', '\r\n')
        n = s.count(a)
        if n < 1: sys.exit('%s: not found: %r' % (fn, a[:90]))
        s = s.replace(a, b)
    io.open(fn, 'w', encoding='utf-8', newline='').write(s)
    print('ok', fn)

def opts(q, a, b, c):
    return ''.join('<li onclick="selectOption(this)" data-qid="%s"><span class="opt-letter">%s</span>%s</li>' % (q, L, t)
                   for L, t in zip('ABC', (a, b, c)))

def swap_opts(s_old3, new):
    return s_old3, new

# ---------- week 17 ----------
patch('week-17-checkin.html', [
 ('Read the sentence. What does <strong>audacious</strong> most likely mean?</div>',
  'Read the sentence from Chapter 5. The officer is holding a baby picture of Lise, who had dark hair. What does <strong>unwavering</strong> most likely mean?</div>'),
 ('<div class="excerpt">"It was an audacious plan — bold to the point of recklessness — but they had no other choice. They would simply have to hope that the soldiers believed the lie."<div class="excerpt-source">— <em>Number the Stars</em>, Ch. 5–8</div></div>',
  '<div class="excerpt">“…and stared at Ellen for a long, unwavering moment.”<div class="excerpt-source">— Lois Lowry, <em>Number the Stars</em>, Ch. 5</div></div>\r\n      <div class="hint"><em>un-</em> means “not.” To <em>waver</em> is to move back and forth.</div>'),
 ('<span class="opt-letter">A</span>Careful and well thought out in every detail</li>', '<span class="opt-letter">A</span>Quick and nervous</li>'),
 ('<span class="opt-letter">B</span>Surprisingly bold and daring, almost reckless</li>', '<span class="opt-letter">B</span>Steady, without looking away</li>'),
 ('<span class="opt-letter">C</span>Quiet and secret, known only to a few</li>', '<span class="opt-letter">C</span>Kind and gentle</li>'),
 ("What does 'audacious' mean?", "What does 'unwavering' mean?"),
 ('"label":"Q5: audacious"', '"label":"Q5: unwavering"'),
 ('Each word below comes from <em>Number the Stars</em>. Break it into its parts (prefix + base OR base + suffix) and explain what each part means.',
  'Break each word into its parts (prefix, base, suffix) and explain what each part means.'),
 ('''      "She had not thought of herself as brave. She had only done what needed to be done — what anyone would have done if they were her. But standing there in the dark, she realized that was exactly what courage was."
      <div class="excerpt-source">— <em>Number the Stars</em>, Ch. 5–8</div>''',
  '''      Soldiers are already inside the apartment.<br><br>“Ellen,” she whispered urgently, “take your necklace off!”
      <div class="excerpt-source">— Lois Lowry, <em>Number the Stars</em>, Ch. 5</div>'''),
 ('According to this passage, how does Annemarie think about her own courage? What does she realize?',
  'What does Annemarie do next with the necklace, and what does that action show about her?'),
 ('''Weak: "Annemarie was brave. 'She ran through the dark woods.'"<br><br>Strong: "Annemarie shows courage when she runs alone through the dark woods, proving that she is willing to risk her safety to help Ellen's family."''',
  '''Weak: Annemarie was brave. “Take your necklace off!”<br><br>Strong: Annemarie shows courage when she whispers to Ellen, “take your necklace off!” with soldiers in the next room, which proves she can think fast when she is afraid.'''),
 ('includes a detail from the story, and explains', 'includes a detail from Ch. 5–8, and explains'),
])

# ---------- week 18 ----------
patch('week-18-checkin.html', [
 ('''"It's impossible — they won't believe us and we didn't have time to plan."''', '''"It's impossible. They won't believe us, and we didn't have time to plan."'''),
 ('Read the sentence. What does <strong>ominous</strong> most likely mean?</div>',
  'Read the sentence from Chapter 9. Uncle Henrik is milking the cow while Annemarie tells him he is lying. What does <strong>deftly</strong> most likely mean?</div>'),
 ('<div class="excerpt">"The sound of boots in the hallway was ominous — heavy and slow, each step suggesting that something terrible was about to happen."<div class="excerpt-source">— <em>Number the Stars</em>, Ch. 9–12</div></div>',
  '<div class="excerpt">“His strong hands continued, deftly pressing like a pulse against the cow.”<div class="excerpt-source">— Lois Lowry, <em>Number the Stars</em>, Ch. 9</div></div>'),
 ('<span class="opt-letter">A</span>Cheerful and full of good news</li>', '<span class="opt-letter">A</span>Clumsily and slowly</li>'),
 ('<span class="opt-letter">B</span>Threatening; suggesting that something bad is coming</li>', '<span class="opt-letter">B</span>Skillfully and smoothly</li>'),
 ('<span class="opt-letter">C</span>Quiet and easy to ignore</li>', '<span class="opt-letter">C</span>Angrily and roughly</li>'),
 ("What does 'ominous' mean?", "What does 'deftly' mean?"),
 ('"label":"Q5: ominous"', '"label":"Q5: deftly"'),
 ('Use the word <strong>concealed</strong> in a sentence', 'Use the word <strong>concede</strong> in a sentence'),
 ("Sentence using 'concealed'", "Sentence using 'concede'"),
 ('''      "The Star of David appeared everywhere in these chapters — on Ellen's necklace, hidden under Annemarie's pillow, mentioned in the dark. It was not just jewelry. It meant something larger: that some people were marked as different, and that those marks carried danger."
      <div class="excerpt-source">— <em>Number the Stars</em>, Ch. 9–12</div>''',
  '''      Peter has just read a psalm aloud, and Annemarie is thinking about it.<br><br>“Outside, she knew, the sky was speckled with stars.”<br>“How could anyone number them one by one, as the psalm said?”
      <div class="excerpt-source">— Lois Lowry, <em>Number the Stars</em>, Ch. 10</div>'''),
 ('Based on this passage, what might the Star of David symbolize in this story? Use details from the passage in your answer.',
  'What might the stars stand for in this story? Use a detail from the lines or the chapter.'),
 ('What the Star of David symbolizes', 'What the stars stand for'),
 ('In Ch. 9–12, what other symbols or repeated ideas did you notice? Choose one and explain what you think it represents in the story.',
  'In Ch. 9–12, what other symbol or repeated idea did you notice (for example, Ellen’s necklace or the casket)? Choose one and explain what you think it represents in the story.'),
 ('''"The necklace is not just jewelry — it stands for Ellen's identity, her family, and the danger that comes with being Jewish in 1943 Denmark."''',
  '''The necklace is not just jewelry. It stands for Ellen’s identity, her family, and the danger of being Jewish in Denmark in 1943.'''),
 ('represents — using the pattern "not just ___, but ___."', 'represents, using the pattern “not just ___. It stands for ___.”'),
 ('about courage or loyalty through the symbols in Ch. 9–12?', 'about courage or loyalty in Ch. 9–12?'),
])

# ---------- week 19 ----------
patch('week-19-checkin.html', [
 ('<strong>1.</strong> They were/where going to meet at the harbor. (were / where)', '<strong>1.</strong> They (were / where) going to meet at the harbor.'),
 ('<strong>2.</strong> It was to/too dark to see the boat. (to / too)', '<strong>2.</strong> It was (to / too) dark to see the boat.'),
 ('<strong>3.</strong> Annemarie knew/new that she had to be brave. (knew / new)', '<strong>3.</strong> Annemarie (knew / new) that she had to be brave.'),
 ('Choose the correct homophone in each blank:', 'Write the correct word for each sentence:'),
 ('Write a sentence about the escape scene using at least one homophone pair correctly (e.g., there/their/they\'re, to/too/two, or your choice).',
  'Write a sentence about Annemarie’s run to the boat using at least one homophone correctly (there/their/they’re, to/too/two, or your choice).'),
 ('Read the sentence. What does <strong>commemorates</strong> most likely mean?</div>',
  'Read the sentence from the Afterword. Lowry is writing about G. F. Duckwitz, the German official who warned the Danes about the Nazi plan. What does <strong>compassion</strong> most likely mean?</div>'),
 ('<div class="excerpt">"The Afterword explains that a museum in Denmark today commemorates the rescue — preserving the stories of the ordinary people who risked everything to save their neighbors."',
  '<div class="excerpt">“…he was a man of compassion and courage.”'),
 ('<span class="opt-letter">A</span>Destroys evidence of a past event</li>', '<span class="opt-letter">A</span>Great wealth and power</li>'),
 ('<span class="opt-letter">B</span>Honors and keeps the memory of something important</li>', '<span class="opt-letter">B</span>Caring about other people’s suffering and wanting to help</li>'),
 ('<span class="opt-letter">C</span>Explains why something was a mistake</li>', '<span class="opt-letter">C</span>Following every rule exactly</li>'),
 ("What does 'commemorates' mean?", "What does 'compassion' mean?"),
 ('"label":"Q5: commemorates"', '"label":"Q5: compassion"'),
 ('Use the word <strong>transformed</strong> in a sentence', 'Use the word <strong>reflect</strong> in a sentence'),
 ("Sentence using 'transformed'", "Sentence using 'reflect'"),
 ('Choose the correct homophone to complete each sentence:', 'Write the correct word for each sentence:'),
 ('<strong>2.</strong> They walked _______ the harbor without speaking. (through / threw)', '<strong>2.</strong> They walked _______ the woods without speaking. (through / threw)'),
 ('<strong>3.</strong> The _______ was calm as the boat set sail. (sea / see)', '<strong>3.</strong> The _______ was calm as the boat set out. (sea / see)'),
 ('"They\'re were many families who helped during the war. The rescue took place over their weeks in October 1943."', '"Their were many families who helped during the war."'),
 ('One word is used incorrectly (wrong homophone). Find it and write the correct word.', 'One word is the wrong homophone. Find it and write the correct word.'),
 ('''      "The Afterword explained that the story was fiction, but the rescue was real. More than 7,000 Danish Jews were saved by their neighbors — fishermen, teachers, ordinary people who simply refused to look away."
      <div class="excerpt-source">— <em>Number the Stars</em> Afterword</div>''',
  '''      “Annemarie Johansen is a child of my imagination…”<br>“…nearly seven thousand people— was smuggled across the sea to Sweden.”
      <div class="excerpt-source">— Lois Lowry, <em>Number the Stars</em>, Afterword</div>'''),
 ('compassion and courage.”<div class="excerpt-source">— <em>Number the Stars</em> Afterword</div>',
  'compassion and courage.”<div class="excerpt-source">— Lois Lowry, <em>Number the Stars</em>, Afterword</div>'),
 ('How does reading the Afterword (a historical source) change or deepen', 'How does reading the Afterword change or deepen'),
])

# ---------- week 20 ----------
patch('week-20-checkin.html', [
 ('Read the passage. What does <strong>resolute</strong> most likely mean?</div>',
  'Read the passage from Chapter 4. Harriet is about fifteen and works in the fields. What does <strong>sullen</strong> most likely mean?</div>'),
 ('<div class="excerpt">"She was resolute — her mind was made up and no argument, no threat, and no obstacle would make her change it."<div class="excerpt-source">— <em>Freedom Train</em>, Ch. 1–4</div></div>',
  '<div class="excerpt">“Although she was a valuable field hand, performing the tasks of an able-bodied man, her sullen expression and rocklike chin made Master uncomfortable. There was a rebellious spirit here which had to be watched and curbed.”<div class="excerpt-source">— Dorothy Sterling, <em>Freedom Train</em>, Ch. 4, p. 40</div></div>'),
 ('<span class="opt-letter">A</span>Unsure and easily changed</li>', '<span class="opt-letter">A</span>Cheerful and eager to please</li>'),
 ('<span class="opt-letter">B</span>Firmly determined; not willing to give in</li>', '<span class="opt-letter">B</span>Gloomy and quietly angry</li>'),
 ('<span class="opt-letter">C</span>Quiet and unlikely to argue</li>', '<span class="opt-letter">C</span>Sleepy and confused</li>'),
 ("What does 'resolute' mean?", "What does 'sullen' mean?"),
 ('"label":"Q5: resolute"', '"label":"Q5: sullen"'),
 ('<strong>abolishon</strong> &nbsp;/&nbsp; Maryland &nbsp;/&nbsp; Harriet', '<strong>abolishon</strong> &nbsp;/&nbsp; <strong>Maryland</strong> &nbsp;/&nbsp; <strong>Harriet</strong>'),
 ('''      "From the first pages, it was clear that this book had a central idea: that Harriet Tubman was not merely a person who escaped slavery — she was a person who refused to let others remain enslaved while she was free."
      <div class="excerpt-source">— <em>Freedom Train</em>, Ch. 1–4</div>''',
  '''      “This was how Harriet, who did not have a last name, received her schooling on the Eastern Shore of Maryland thirty years before the Civil War. … But Harriet’s school had taught her one important lesson until she knew it with her body, with her mind, and with her heart: ‘Let my people go!’”
      <div class="excerpt-source">— Dorothy Sterling, <em>Freedom Train</em>, Ch. 3, pp. 37–38</div>'''),
])
