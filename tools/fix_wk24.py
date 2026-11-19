#!/usr/bin/env python3
"""Week 24 (Freedom Train Ch. 18-20 + final reflection) curriculum fixes, checked against Sterling's text
(IA borrow, Nov 19 2026). Ch. 18 'Mr. Lincoln's Army' pp. 165-172 (scouting St. Marys River, the Combahee raid,
almost eight hundred people, Harriet's song); Ch. 19 'Victory' pp. 173-181 (furlough, Seward, Fortress Monroe,
Lincoln shot the night of the Fort Sumter flag raising, the baggage car); Ch. 20 'The Years of Peace' pp. 182-191.
Run from the repo root; every replacement must match exactly once."""
import io, sys
FILES = {}
def load(f):
    if f not in FILES: FILES[f] = io.open(f, encoding='utf-8', newline='').read()
    return FILES[f]
def R(f, old, new, n=1):
    s = load(f); c = s.count(old)
    if c != n: sys.exit('%s: expected %d, found %d: %r' % (f, n, c, old[:90]))
    FILES[f] = s.replace(old, new)
L1, L2, L3, L4 = 'lesson-24-1-ft-ch17.html', 'lesson-24-2-ft-lookback.html', 'lesson-24-3-ft-craft.html', 'lesson-24-4-ft-reflection.html'
CK = 'week-24-checkin.html'

# ---------- 24.1  Ch. 18 ----------
R(L1, '<div class="copywork-text">Women with pails of rice on their heads, children clinging to their skirts, pigs squealing under their arms &mdash; they came flooding to the riverbanks.</div>',
      '<div class="copywork-text">&ldquo;The women had bags on their shoulders, baskets on their heads, and young ones tagging behind, all loaded.&rdquo;</div>')
R(L1, 'Notice the dash &mdash; the author stacks three details before the main clause arrives, building suspense. Count the prepositional phrases: &ldquo;on their shoulders,&rdquo; &ldquo;to their skirts,&rdquo;',
      'XX', n=0)
R(L1, 'Notice the dash &mdash; the author stacks three details before the main clause arrives, building suspense. Count the prepositional phrases: &ldquo;on their heads,&rdquo; &ldquo;to their skirts,&rdquo; &ldquo;under their arms,&rdquo; &ldquo;to the riverbanks.&rdquo;',
      'These are Harriet&rsquo;s own words about the Combahee raid (Ch. 18, p. 171). Notice how she stacks three pictures, each one built with a prepositional phrase: &ldquo;on their shoulders,&rdquo; &ldquo;on their heads,&rdquo; and &ldquo;behind.&rdquo; Then two words, &ldquo;all loaded,&rdquo; sum them up.')
R(L1, '<p>A passage from Chapter 18. Several groups of words here are telling you <em>where</em> or <em>when</em>.</p>',
      '<p>A sentence about a night trip. Several groups of words here are telling you <em>where</em> or <em>when</em>.</p>')
R(L1, '<p>A passage from Chapter 18. Everything from this year is in play.</p>', '<p>A sentence about the people waiting. Everything from this year is in play.</p>')
R(L1, 'She is paid very little for her spy work. Yet she keeps going.', 'She is not paid for her spy work either. Yet she keeps going.')
R(L1, 'The Civil War is ending. Harriet works in hospitals in Virginia. She hears that Lincoln has been shot. Finally she heads home &mdash; but the train ride shows that the fight for true freedom is far from over. Read for how Sterling uses details to support the central idea of the entire book.',
      'After the Emancipation Proclamation, General Hunter sends Harriet behind enemy lines as a scout. Then, on a hot night in June, she guides three Union gunboats up the Combahee River, and almost eight hundred people leave slavery behind. Read for how Sterling uses details to support the central idea of the chapter.')
R(L1, 'Harriet gives up her trip to Charleston to work in the hospitals instead. <strong>Why does she make this choice?</strong>',
      'General Hunter asks Harriet if she knows the penalty for spying. She answers, &ldquo;I&rsquo;ve faced death before, sir. But never in a better cause.&rdquo; <strong>What does her answer tell you about her?</strong>')
R(L1, 'The chapter ends with a conductor forcing Harriet into the baggage car. <strong>Why does Sterling end the chapter this way? What is she saying about &lsquo;victory&rsquo;?</strong>',
      'The chapter ends with Harriet singing from the gunboat while the rowboats fill again and again. <strong>Why does Sterling end the chapter with a song? What does it show about the raid?</strong>')
R(L1, 'Harriet gives up going to the flag-raising at Fort Sumter to work in Virginia hospitals instead. <strong>What does this choice tell you about her character?</strong>',
      'Harriet scouts behind enemy lines, then guides the gunboats past the hidden torpedoes. <strong>What does this work tell you about her character?</strong>')
R(L1, '<div class="textbox-prompt">Think about what she gives up vs. what she gains.</div>',
      '<div class="textbox-prompt">Think about what she risks, and why the Union needs her and her nine scouts.</div>')
R(L1, 'placeholder="Harriet\'s choice shows..."', 'placeholder="Harriet\'s work shows..."')
R(L1, '<strong>Name ONE moment that feels like a real victory and ONE moment that doesn&rsquo;t feel like victory at all.</strong>',
      '<strong>Name THREE details Sterling gives about the night of the raid. What central idea do they support?</strong>')
R(L1, '<div class="textbox-prompt">Look for contrasts &mdash; wins and losses in the same chapter.</div>',
      '<div class="textbox-prompt">Look for a number, a sound, and a picture: the picket posts, the flames, the people running to the riverbanks.</div>')
R(L1, 'placeholder="A real victory is... But it doesn\'t feel like victory when..."', 'placeholder="Three details are... Together they show..."')
R(L1, 'Sterling ends the book with a conductor forcing Harriet into the baggage car. <strong>What central idea is Sterling trying to leave the reader with?</strong>',
      'Sterling ends the chapter with Harriet singing, &ldquo;Come along! Come along! Don&rsquo;t be alarmed.&rdquo; <strong>What central idea is Sterling trying to leave the reader with?</strong>')
R(L1, '<div class="textbox-prompt">Why would Sterling choose THIS as the ending image?</div>',
      '<div class="textbox-prompt">Why would Sterling end on a song instead of on the battle?</div>')
R(L1, 'placeholder="Sterling\'s central idea is... She ends with the train because..."', 'placeholder="Sterling\'s central idea is... She ends with the song because..."')
R(L1, '<em>Tubman used songs code directions the North Star.</em>', '<em>Tubman sang song say goodbye to her family.</em>')
R(L1, '<em>Tubman used songs as a code for directions toward the North Star.</em>', '<em>Tubman sang a song to say goodbye to her family.</em>')

# ---------- 24.2  Ch. 19 ----------
R(L2, '<p>Chapter 19. Prepositional phrases stack up here.</p>', '<p>Prepositional phrases stack up here.</p>')
R(L2, '<p>Chapter 19. Suffix changes and syllable splits together.</p>', '<p>Suffix changes and syllable splits together.</p>')
R(L2, 'Lee surrenders at Appomattox on April 9, 1865. That same night, Lincoln is shot at Ford&rsquo;s Theater. Harriet works as Matron at Fortress Monroe hospital, organizes the patients &ldquo;like a whirlwind,&rdquo; and finally boards a train home &mdash; with a War Department pass in her hand.',
      'Harriet goes home on furlough, falls ill, then heads to Virginia to clean up the hospital at Fortress Monroe &ldquo;like a whirlwind.&rdquo; Lee surrenders at Appomattox. A few nights later, the night the flag rises again over Fort Sumter, Lincoln is shot at Ford&rsquo;s Theater. By midsummer the hospital is running smoothly, and Harriet boards a train home &mdash; with a War Department pass in her hand.')
R(L2, 'When the war ends, freedom is finally <em>liberated</em> into law. All four roots live in this chapter.',
      'Harriet comes home on a government <em>transport</em>, and the war she fought ends in <em>liberty</em> for her people. Each root names something in this chapter.')

# ---------- 24.3  Ch. 20 ----------
R(L3, '<div class="copywork-text">&ldquo;Ben said, &lsquo;It&rsquo;s time for sittin&rsquo;, Hat,&rsquo; but Harriet was always on her feet.&rdquo;</div>',
      '<div class="copywork-text">From his porch rocker, Ben called, &ldquo;It&rsquo;s time for sittin&rsquo;, Hat. Come over here and just listen to the grass grow.&rdquo;</div>')
R(L3, 'harriet marched beside elizabeth cady stanton at meetings for the suffrage movement', 'harriet spoke beside elizabeth cady stanton at meetings for women&rsquo;s rights')
R(L3, '<strong>Harriet</strong> marched beside <strong>Elizabeth Cady Stanton</strong> at meetings for the suffrage movement.',
      '<strong>Harriet</strong> spoke beside <strong>Elizabeth Cady Stanton</strong> at meetings for women&rsquo;s rights.')
R(L3, 'The prepositional phrases &ldquo;beside Elizabeth Cady Stanton&rdquo; and &ldquo;at meetings for the suffrage movement&rdquo; show where and when',
      'The prepositional phrases &ldquo;beside Elizabeth Cady Stanton,&rdquo; &ldquo;at meetings&rdquo; and &ldquo;for women&rsquo;s rights&rdquo; show where and what for')
R(L3, '4. By the time Harriet died at over 90 years old, she had outlived almost everyone she knew; only true <input class="fillin-input" id="vc4" data-answer="centenarians" maxlength="14" placeholder="________"> are rarer in history.',
      '4. Old Rit and Ben lived so long that they proudly called themselves <input class="fillin-input" id="vc4" data-answer="centenarians" maxlength="14" placeholder="________">.')
R(L3, '<div class="rwm-sentence">&ldquo;When they lay her down, the North Star was shining.&rdquo;</div>',
      '<div class="rwm-sentence">&ldquo;It was dusk, and the North Star was shining in the darkening sky, when her eyes closed for the last time.&rdquo;<div style="margin-top:10px;font-family:\'Nunito\',sans-serif;font-style:normal;font-size:13px;color:#7A88A8;font-weight:700;">&mdash; Dorothy Sterling, <em>Freedom Train</em>, the last sentence of the book, p. 191</div></div>')
R(L3, 'This sentence starts with a <strong>subordinate clause</strong> &mdash; &ldquo;When they lay her down&rdquo; &mdash; and it cannot stand alone; it just sets the moment. Then the main clause arrives: &ldquo;the North Star was shining.&rdquo; Sterling saves the star for last, and the star is the image she opened the whole book with. That is how you write a conclusion that circles back to your main idea. How does ending on the North Star change the feeling, compared with just saying &ldquo;she died&rdquo;?',
      'Sterling sets the scene first: <strong>It was dusk, and the North Star was shining</strong>. Only at the very end, in a <strong>when</strong> clause, does she tell you Harriet died. The star comes first on purpose. In Chapter 1, little Harriet asks Daddy Ben the name of &ldquo;the one that never moves,&rdquo; and all through the book she follows it north. Ending on that same star is how a conclusion circles back to the main idea. How does it change the feeling, compared with just saying &ldquo;she died&rdquo;?')
R(L3, 'Write your own sentence using the same pattern: a &ldquo;when&rdquo; clause + a main clause that ends on an image or detail.',
      'Write your own sentence using the same pattern: set the scene with an image first, then end with a &ldquo;when&rdquo; clause that tells what happened.')
R(L3, '<div class="rwm-frame">When ___ [time/moment], ___ [what was happening].</div>',
      '<div class="rwm-frame">It was ___, and ___ was ___, when ___.</div>')

# ---------- 24.4  final reflection ----------
R(L4, '<p>A draft about Chapter 20. Some sentences are clear. Some are buried under phrases.</p>', '<p>A draft about a night escape. Some sentences are clear. Some are buried under phrases.</p>', n=load(L4).count('<p>A draft about Chapter 20. Some sentences are clear. Some are buried under phrases.</p>'))
R(L4, '<p>A draft about Chapter 20. Some are spelled correctly.</p>', '<p>A draft. Some are spelled correctly.</p>', n=load(L4).count('<p>A draft about Chapter 20. Some are spelled correctly.</p>'))

# ---------- check-in ----------
R(CK, 'In Chapters 17&#8211;20, Harriet&#8217;s story reaches its fullest meaning.', 'In Chapters 18&#8211;20, Harriet&#8217;s story reaches its fullest meaning.')
R(CK, 'Read the passage. What does <strong>legacy</strong> most likely mean?', 'Read the passage. What does <strong>furlough</strong> most likely mean?')
R(CK, '&#8220;Harriet Tubman&#8217;s legacy endures &#8212; her choices shaped history, and her courage became a model for everyone who came after her and faced injustice.&#8221;<div class="excerpt-source">&#8212; <em>Freedom Train</em>, Ch. 17&#8211;20</div>',
      '&#8220;After repeated urging, Harriet agreed to a furlough. She traveled North on a government transport, arriving in Auburn to find her mother and father ailing and full of reproaches.&#8221;<div class="excerpt-source">&#8212; <em>Freedom Train</em>, Ch. 19, p. 174</div>')
R(CK, '<span class="opt-letter">A</span>A legal document signed before a person dies', '<span class="opt-letter">A</span>A reward of money for good work')
R(CK, '<span class="opt-letter">B</span>Something handed down from the past; lasting impact or influence', '<span class="opt-letter">B</span>A leave from duty to go home for a while')
R(CK, '<span class="opt-letter">C</span>A journey made across a long distance', '<span class="opt-letter">C</span>A long trip by sea')
R(CK, 'Use the word <strong>enduring</strong> (as an adjective) in a sentence about Harriet that shows what it means.', 'Use the word <strong>pension</strong> in a sentence about Harriet that shows what it means.')
R(CK, "data-label=\"Q6: Sentence using 'enduring' as an adjective showing its meaning\"", "data-label=\"Q6: Sentence using 'pension' showing its meaning\"")
R(CK, '&#8220;By the end of the book, the central idea had earned its place: Harriet Tubman did not just survive &#8212; she transformed what survival could mean. Every detail Sterling chose &#8212; the routes, the names, the dates, the dangers &#8212; pointed toward this single truth.&#8221;',
      '&#8220;For Harriet there was always &#8216;something to do.&#8217; Within a year of the surrender at Appomattox she was supporting two freedmen&#8217;s schools in the South, buying clothes and books for the students with money earned in domestic work and through the sale of vegetables and chickens.&#8221;')
R(CK, '<div class="excerpt-source">&#8212; <em>Freedom Train</em>, Ch. 17&#8211;20</div>', '<div class="excerpt-source">&#8212; <em>Freedom Train</em>, Ch. 20, p. 183</div>')
R(CK, 'Choose two details from Chapters 17&#8211;20 that best support', 'Choose two details from Chapters 18&#8211;20 that best support')
R(CK, 'data-label="Q11: Two details from Ch. 17–20 that support', 'data-label="Q11: Two details from Ch. 18–20 that support')
FILES[CK] = load(CK).replace("What does 'legacy' mean?", "What does 'furlough' mean?").replace('"Q5: legacy"', '"Q5: furlough"').replace('(Ch. 17–20)', '(Ch. 18–20)')

for f, s in FILES.items():
    if '--apply' in sys.argv: io.open(f, 'w', encoding='utf-8', newline='').write(s)
    print(('written ' if '--apply' in sys.argv else 'ok ') + f)
