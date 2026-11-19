#!/usr/bin/env python3
"""Week 23 (Freedom Train Ch. 15-17) curriculum fixes, checked against Sterling's text (IA borrow, Nov 19 2026).

Ch. 15 'The Most of a Man' pp. 134-148: the praise is John Brown's (letter to his son, p. 143), not Wendell Phillips'.
Ch. 16 'Department of the South' pp. 149-157: Beaufort, General Hunter, the snake story, contrabands. NO Combahee raid
  (that is Ch. 18, p. 168-171), no uniform, no Emancipation yet.
Ch. 17 'Our Time Is Coming' pp. 158-164: 1862 relief work, hospital, Fernandina, First South Carolinas, the
  Emancipation Proclamation read on January 1, 1863.
Also: Sam's model essay (weeks 21-23) leaned on 'Follow the Drinking Gourd' and an invented historian quote; it now uses
  the songs Sterling actually records (pp. 27, 66, 93, 97-98, 112).
Run from the repo root. Every replacement must match exactly the expected number of times."""
import io, sys

FILES = {}
def load(f):
    if f not in FILES: FILES[f] = io.open(f, encoding='utf-8', newline='').read()
    return FILES[f]
def R(f, old, new, n=1):
    s = load(f); c = s.count(old)
    if c != n: sys.exit('%s: expected %d, found %d: %r' % (f, n, c, old[:90]))
    FILES[f] = s.replace(old, new)

L1, L2, L3, L4 = 'lesson-23-1-ft-ch13.html', 'lesson-23-2-ft-ch14.html', 'lesson-23-3-ft-ch15.html', 'lesson-23-4-ft-ch16.html'
FL, CK = 'lesson-23-fluency.html', 'week-23-checkin.html'

# ---------- shared across all four lessons: vocabulary sentences ----------
for f in (L1, L2, L3, L4):
    R(f, '&ldquo;The Combahee Raid helped elevate Harriet to national fame.&rdquo;',
         '&ldquo;Reports in antislavery newspapers helped elevate Harriet to fame across the North.&rdquo;')
    R(f, '&ldquo;Frederick Douglass and Wendell Phillips were famous abolitionists who admired Harriet.&rdquo;',
         '&ldquo;John Brown was a fierce abolitionist who admired Harriet&rsquo;s courage.&rdquo;')

# ---------- 23.1  Ch. 15 ----------
R(L1, '&ldquo;The most of a man, naturally, that I ever met.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Wendell Phillips (about Harriet), Ch. 15</div>',
      '&ldquo;The most of a man, naturally, that I ever met with.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; John Brown (about Harriet), Ch. 15</div>')
R(L1, 'Abolitionists who meet Harriet are stunned. One famous one says she is &lsquo;the most of a man.&rsquo;',
      'Harriet speaks at meetings across the North. Then John Brown, the fighting abolitionist, writes that she is &lsquo;the most of a man&rsquo; he ever met.')
R(L1, "onclick=\"dolHighlight(this,'A first name &mdash; capital W.')\">Wendell</span>",
      "onclick=\"dolHighlight(this,'A first name &mdash; capital J.')\">John</span>")
R(L1, "onclick=\"dolHighlight(this,'A last name &mdash; capital P.')\">Phillips</span>",
      "onclick=\"dolHighlight(this,'A last name &mdash; capital B.')\">Brown</span>")
R(L1, '<p>A passage from Chapter 15. These adverbs are comparing how things were done.</p>',
      '<p>A sentence about Harriet&rsquo;s trips. These adverbs are comparing how things were done.</p>')
R(L1, '<p>A passage from Chapter 15. Every long word here has a stressed syllable and a lazy one.</p>',
      '<p>A sentence about the antislavery movement. Every long word here has a stressed syllable and a lazy one.</p>')
R(L1, 'Wendell Phillips, one of the most famous speakers in America, calls Harriet &lsquo;the most of a man&rsquo; he&rsquo;s ever met. That recognition is its own kind of freedom.',
      'John Brown calls her &lsquo;General Tubman&rsquo; and writes to his son that she is &lsquo;the most of a man, naturally,&rsquo; he ever met. That recognition is its own kind of freedom.')
R(L1, 'Harriet is now famous in abolitionist circles &mdash; the secret network of people fighting to end slavery. She meets Frederick Douglass, John Brown, and other leaders. They call her &lsquo;General Tubman.&rsquo; One famous abolitionist, Wendell Phillips, will later say she is &lsquo;the most of a man, naturally, that I ever met.&rsquo;',
      'Harriet is now famous among the abolitionists, the people working to end slavery. She speaks at their meetings, helps a crowd rescue Charles Nalle in Troy, and plans with John Brown, who calls her &lsquo;General Tubman.&rsquo; Brown writes that she is &lsquo;the most of a man, naturally, that I ever met with.&rsquo;')
R(L1, 'Wendell Phillips&rsquo; praise is the chapter&rsquo;s title.', 'John Brown&rsquo;s praise is the chapter&rsquo;s title.')
R(L1, '<div class="textbox-prompt">Frederick Douglass, John Brown, Wendell Phillips, William Lloyd Garrison.</div>',
      '<div class="textbox-prompt">John Brown; Ralph Waldo Emerson; Bronson Alcott and his daughter Louisa May; Senator William Seward.</div>')
R(L1, 'Wendell Phillips calls Harriet &lsquo;the most of a man.&rsquo;', 'John Brown calls Harriet &lsquo;the most of a man.&rsquo;')
R(L1, '<div class="textbox-prompt">In 1860, the word &lsquo;man&rsquo; was often used to mean &lsquo;the best a human can be.&rsquo;</div>',
      '<div class="textbox-prompt">Sterling says Brown was so impressed with her courage and leadership that he &lsquo;frequently spoke of her in masculine terms.&rsquo;</div>')
R(L1, 'placeholder="Phillips means... It was high praise because..."', 'placeholder="Brown means... It was high praise because..."')
R(L1, 'As you read Ch. 15, listen to Sterling&rsquo;s <strong>word choice</strong>. Harriet meets Frederick Douglass, John Brown, and other leaders of the movement, and they begin calling her General Tubman.',
      'As you read Ch. 15, listen to Sterling&rsquo;s <strong>word choice</strong>. Harriet speaks at antislavery meetings, helps rescue Charles Nalle, and plans with John Brown, who begins calling her General Tubman.')
# Sam (body 1 grows by one fact)
R(L1, '<em>Tubman used songs as a CODE for directions. &lsquo;Follow the Drinking Gourd&rsquo; pointed to the North Star. Singing aloud gave directions without writing them down.</em>',
      '<em>Tubman used songs to carry a hidden MESSAGE. When she ran away, she sang &lsquo;When that old chariot comes, I&rsquo;m going to leave you&rsquo; as she passed the slave quarters, so her family would know. A song could say what words could not.</em>')
R(L1, '<em>Tubman used songs as a CODE for directions. &lsquo;Follow the Drinking Gourd&rsquo; pointed to the North Star. <strong>The song also described specific landmarks &mdash; like rivers and mountains along the route.</strong> Singing aloud gave directions without writing them down.</em>',
      '<em>Tubman used songs to carry a hidden MESSAGE. When she ran away, she sang &lsquo;When that old chariot comes, I&rsquo;m going to leave you&rsquo; as she passed the slave quarters, so her family would know. <strong>Years later her mother sang &lsquo;Good news, the chariot&rsquo;s coming&rsquo; to tell Harriet&rsquo;s father, locked in jail, that rescue was on the way.</strong> A song could say what words could not.</em>')
R(L1, '<strong>BODY 1 new fact:</strong> The song described specific landmarks &mdash; rivers and mountains along the route.',
      '<strong>BODY 1 new fact:</strong> Old Rit sang &lsquo;Good news, the chariot&rsquo;s coming&rsquo; to tell Ben in jail that help was coming (Sterling, p. 112).')
R(L1, '<strong>BODY 2 new fact:</strong> Tubman sometimes changed her songs based on who was within earshot.',
      '<strong>BODY 2 new fact:</strong> Hidden in the bushes, she sang &lsquo;When that old chariot comes, who&rsquo;s going with me?&rsquo; and her brother William Henry knew her voice (Sterling, pp. 93&ndash;94).')

# ---------- 23.2  Ch. 16 ----------
R(L2, '&ldquo;She served her country at last in uniform.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; narrator, Ch. 16</div>',
      '&ldquo;Can&rsquo;t win this war by half measures.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; Harriet, to General Hunter, Ch. 16</div>')
R(L2, 'The Civil War begins. Harriet doesn&rsquo;t stay safe in the North. She goes south, in uniform, as a Union scout and nurse. Why?',
      'The Civil War begins. Harriet doesn&rsquo;t stay safe in the North. She sails south to Beaufort, South Carolina, to work for the Union army. Why?')
R(L2, 'The Civil War has begun, and Harriet joins the Department of the South as a scout, a spy, and a nurse. Does Sterling give more room to the army and its plans, or to Harriet&rsquo;s own work?',
      'The Civil War has begun, and Harriet sails to Beaufort, where General Hunter puts her to work with the thousands of people who have escaped to the Union lines. Does Sterling give more room to the army and its plans, or to Harriet and the people of Beaufort?')
R(L2, 'harriet scouted more silently than the soldiers and reported back more quickly',
      'harriet spoke more boldly than the general expected and argued more firmly for freedom')
R(L2, '<strong>Harriet</strong> scouted <strong>more silently</strong> than the soldiers and reported back <strong>more quickly</strong>.',
      '<strong>Harriet</strong> spoke <strong>more boldly</strong> than the general expected and argued <strong>more firmly</strong> for freedom.')
R(L2, '<em>more silently</em> (how she scouted vs the soldiers) and <em>more quickly</em> (how she reported vs others).',
      '<em>more boldly</em> (how she spoke vs what the general expected) and <em>more firmly</em> (how she argued).')
R(L2, '<p>Chapter 16. Comparative adjectives and comparative adverbs are easy to confuse.</p>',
      '<p>A paragraph about Harriet&rsquo;s work. Comparative adjectives and comparative adverbs are easy to confuse.</p>')
R(L2, '<p>Chapter 16. Stress falls in different places in these words.</p>', '<p>Stress falls in different places in these words.</p>')
R(L2, '<p>The Union army needs Harriet. She wears the uniform of a country that, until now, has kept her people enslaved.</p>',
      '<p>The Union army needs Harriet. She goes to work for a country that, until now, has kept her people enslaved.</p>')
R(L2, 'Harriet doesn&rsquo;t stay safe in the North. She goes south in Union blue, into the very swamps where, only a few years earlier, she could have been recaptured. She believes the country can become free.',
      'Harriet doesn&rsquo;t stay safe in the North. She sails south with a letter from the governor of Massachusetts and tells General Hunter the war can&rsquo;t be won &lsquo;by half measures.&rsquo; She believes the country can become free.')
R(L2, 'The Civil War has begun. Lincoln has freed slaves in Confederate states. The Union army needs scouts who know the southern landscape &mdash; and the people. They ask Harriet. She joins the &lsquo;Department of the South&rsquo; in South Carolina, working as a scout, spy, and nurse. Read for what she does &mdash; and how Sterling writes about her presence in uniform.',
      'The Civil War has begun. Harriet sails to Beaufort, South Carolina, headquarters of the Union army&rsquo;s Department of the South. General Hunter is glad to see her: thousands of people have run away to the Union lines, and they need someone they can trust. Read for what Harriet does &mdash; and how Sterling writes about her.')
R(L2, 'The Union army needs Harriet. <strong>What does she agree to do for them?</strong>',
      'Harriet meets General Hunter. <strong>What job does he give her?</strong>')
R(L2, '<strong>Why is Harriet specifically valuable as a scout?</strong> Use details from the chapter.',
      '<strong>Why does the General think Harriet is the right person for this job?</strong> Use details from the chapter.')
# Inside This Chapter: the snake story (the Combahee raid is Ch. 18)
R(L2, '<!-- Inside this chapter: the Combahee River Raid -->', '<!-- Inside this chapter: Harriet\'s snake story (Ch. 16, p. 153) -->')
R(L2, '<div class="activity-title">🚢 Inside This Chapter: The Combahee River Raid</div><div class="activity-sub">One night inside Ch. 16 &mdash; the raid Harriet planned.</div>',
      '<div class="activity-title">🐍 Inside This Chapter: Harriet&rsquo;s Snake Story</div><div class="activity-sub">One argument inside Ch. 16 &mdash; the one Harriet makes to the General.</div>')
R(L2, '''      <p>Ch. 16 covers a long stretch of the war. One night inside it stands out.</p>
      <div class="key-concept-label">📌 What happened</div>
      <ul>
        <li><strong>June 2, 1863.</strong> Three Union gunboats steam up the <strong>Combahee River</strong> in South Carolina.</li>
        <li><strong>Harriet planned the route.</strong> The Union army provided the boats.</li>
        <li>By morning, <strong>more than 700 enslaved people</strong> are free.</li>
      </ul>
      <p>The raid helped make Harriet famous across the country. Watch for it as you read Ch. 16. You will look at it closely in the next lesson.</p>''',
      '''      <p>Ch. 16 covers Harriet&rsquo;s first days in Beaufort. One conversation stands out.</p>
      <div class="key-concept-label">📌 What happened</div>
      <ul>
        <li>Mr. Lincoln is afraid to free the slaves or let them join the army. <strong>Harriet thinks he is wrong.</strong></li>
        <li>She tells General Hunter about <strong>a big snake</strong> that bites you again and again while the doctor treats each bite.</li>
        <li>Her point: treating the bites will never be enough. <strong>You have to kill the snake.</strong></li>
      </ul>
      <p>Watch for the snake story as you read Ch. 16. What is the snake? You will look at this conversation closely in the next lesson.</p>''')
# RWM: a real Ch. 16 sentence that blends a fact with explanation (p. 156)
R(L2, '<div class="rwm-sentence">&ldquo;She served her country at last in uniform.&rdquo;<div style="margin-top:10px;font-family:\'Nunito\',sans-serif;font-style:normal;font-size:13px;color:#7A88A8;font-weight:700;">&mdash; narrator, <em>Freedom Train</em>, Ch. 16</div></div>',
      '<div class="rwm-sentence">&ldquo;Youngsters nearby were studying their reading from McClellan&rsquo;s <em>Bayonet Exercises</em>, a soldiers&rsquo; handbook.&rdquo;<div style="margin-top:10px;font-family:\'Nunito\',sans-serif;font-style:normal;font-size:13px;color:#7A88A8;font-weight:700;">&mdash; Dorothy Sterling, <em>Freedom Train</em>, Ch. 16, p. 156</div></div>')
R(L2, 'The Civil War has begun. The Union army needs scouts who know the southern land and the southern people, so they ask Harriet, and she joins the Department of the South in South Carolina as a scout, a spy, and a nurse. <strong>Why would putting on a uniform mean something extra for her?</strong>',
      'At night in the camp outside Beaufort, families who have just escaped slavery gather around the fires. A woman spells out loud, &ldquo;Cat, bat, pat.&rdquo; Children shout lines from the only book they have. <strong>What does this sentence show about how much these children want to learn?</strong>')
R(L2, 'Look at how much of this sentence is fact and how much is Sterling explaining. The fact is small and checkable: <strong>in uniform</strong>. The explanation is two words long &mdash; <strong>at last</strong>. Those two words hold every year before this one, when the country she was born in would not let her serve it or own herself. Sterling does not spend a paragraph on that. She folds it into the middle of a sentence about a uniform. Notice <strong>her country</strong> as well &mdash; Sterling lets Harriet claim a country that had enslaved her. That is what blending facts with explanation looks like: state the fact plainly, then slip in the two or three words that tell the reader what it cost.',
      'The fact is small and checkable: the children were learning to read from a book called <strong>McClellan&rsquo;s <em>Bayonet Exercises</em></strong>. Most readers would not know what that book is, so Sterling adds four words after the comma: <strong>a soldiers&rsquo; handbook</strong>. Those four words do the explaining. Now you see it: there were no storybooks in the camp, so the children learned to read from an army manual. Sterling never says &ldquo;they had nothing&rdquo; or &ldquo;they wanted it badly.&rdquo; The short explanation tucked after the comma says it for her. That is blending facts with explanation: state the fact, then add the few words a reader needs to understand it.')
R(L2, 'Write one sentence that states a plain fact about something a person finally got to do &mdash; and fold the years of waiting into the two words <em>at last</em>. Do not explain them.',
      'Write one sentence that states a fact about something someone used or read. After a comma, add a short phrase that explains what it is, so the reader understands why it matters. Do not explain any more than that.')
R(L2, '<div class="rwm-frame">[Character] ___ [his/her] ___ at last in ___.</div>', '<div class="rwm-frame">[Someone] ___ from ___, a ___.</div>')
R(L2, 'What jobs does Harriet do for the Union army? <strong>List at least TWO and explain what each requires.</strong>',
      'What jobs does General Hunter give Harriet? <strong>Name TWO and explain why each one matters.</strong>')
R(L2, '<div class="textbox-prompt">Scout, spy, nurse, cook &mdash; she did multiple roles.</div>',
      '<div class="textbox-prompt">She is his link to the people pouring into Beaufort, and she reports to the Contraband Hospital.</div>')
R(L2, 'placeholder="Harriet works as a... and as a... Each role requires..."', 'placeholder="The General gives Harriet two jobs... Each one matters because..."')
R(L2, 'Why is Harriet especially valuable as a SCOUT in South Carolina? <strong>Use details from the chapter.</strong>',
      'General Hunter says, &ldquo;We can use you here.&rdquo; <strong>Why is Harriet the right person to help the people in Beaufort? Use details from the chapter.</strong>')
R(L2, '<div class="textbox-prompt">She knows the people. She knows the land. She has spent her life moving secretly.</div>',
      '<div class="textbox-prompt">The General says they don&rsquo;t fully trust him or any white man. &ldquo;There&rsquo;s work for a thousand Harriets.&rdquo;</div>')
R(L2, 'placeholder="Harriet is valuable as a scout because..."', 'placeholder="Harriet is the right person because..."')
R(L2, '<strong>Sterling writes about Harriet in uniform with admiration.</strong> Find ONE detail or word choice that shows how Sterling FEELS about Harriet&rsquo;s war work.',
      '<strong>Sterling writes about Harriet&rsquo;s meeting with General Hunter with admiration.</strong> Find ONE detail or word choice that shows how Sterling FEELS about Harriet&rsquo;s war work.')

R(L2, '          <span>served </span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'Part of a COMPARATIVE adverb.\')">more</span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'The adverb being compared &mdash; HOW she served.\')">bravely</span>\n          <span>than </span>\n          <span>most </span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'Period ends the sentence.\')">soldiers.</span>',
      '          <span>worked </span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'Part of a COMPARATIVE adverb.\')">more</span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'The adverb being compared &mdash; HOW she worked.\')">patiently</span>\n          <span>than </span>\n          <span>anyone </span>\n          <span>in </span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'A town &mdash; capital B. Period ends the sentence.\')">Beaufort.</span>')

# ---------- 23.3  Ch. 16 close read: the talk with General Hunter ----------
R(L3, '&ldquo;She brought them out by the hundreds.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; narrator (about the Combahee Raid), Ch. 16</div>',
      '&ldquo;There&rsquo;s work for a thousand Harriets.&rdquo;</div>\n  <div class="quote-strip-attr">&mdash; General Hunter, Ch. 16</div>')
R(L3, 'On June 2, 1863, Harriet leads a Union raid up the Combahee River. They free more than 700 enslaved people in one night. What does she do that no other commander could?',
      'General Hunter tells Harriet, &ldquo;There&rsquo;s work for a thousand Harriets.&rdquo; Thousands of people have just escaped to the Union lines. What can Harriet do for them that no officer could?')
R(L3, 'The date, the three gunboats, the Combahee River, and the more than 700 people freed by morning can all be checked. What does Sterling add on top of those facts about Harriet and about the officers around her?',
      'Beaufort, General David Hunter, the letter from Governor Andrew, and the First South Carolina regiment can all be checked. What does Sterling add on top of those facts about Harriet and about the General?')
R(L3, 'she planned the raid more carefully than the union officers had ever seen', 'she argued more boldly than the union officers expected')
R(L3, '<strong>She</strong> planned the raid <strong>more carefully</strong> than the <strong>Union</strong> officers had ever seen.',
      '<strong>She</strong> argued <strong>more boldly</strong> than the <strong>Union</strong> officers expected.')
R(L3, 'Comparative adverb <em>more carefully</em> describes HOW she planned, compared to the officers.',
      'Comparative adverb <em>more boldly</em> describes HOW she argued, compared to what the officers expected.', n=load(L3).count('Comparative adverb <em>more carefully</em> describes HOW she planned, compared to the officers.'))
R(L3, '<div class="activity-title">Freedom Watch: 700 people, one night</div>', '<div class="activity-title">Freedom Watch: free, but only half free</div>')
R(L3, '<div class="activity-sub">Freedom on a scale she could barely have imagined</div>', '<div class="activity-sub">Freedom that has started but is not finished</div>')
R(L3, '<p>The Combahee Raid frees more than 700 enslaved people in one night. Harriet planned the route. The Union army provided the boats.</p>',
      '<p>In Beaufort, thousands of people have escaped to the Union army. &ldquo;We&rsquo;s all free,&rdquo; they say. A soldier answers that they are only half free.</p>')
R(L3, 'Sometimes a lifetime of small freedoms makes possible one enormous one. Every trip on the Underground Railroad taught Harriet how to do this.',
      'Freedom is more than getting away. It is fair pay for your work, land to farm, and a school for your children.')
R(L3, 'She stands on a Union gunboat as 700 people climb aboard. She is the first woman to lead a US military operation. She doesn&rsquo;t make a speech. She just does the work.',
      'At a campfire, a soldier in Union blue says they are &lsquo;not more than half free&rsquo; until they get land and a soldier&rsquo;s pay. A woman sewing a flag answers, &lsquo;Our time is coming.&rsquo;')
R(L3, '💭 Think: If you spent years preparing for something big, what would it feel like to finally do it?',
      '💭 Think: Besides getting away, what would a person need to be all the way free?')
R(L3, 'Go back into the chapter. Read the night of the raid slowly, and pause at the prompts.',
      'Go back into the chapter. Read Harriet&rsquo;s talk with General Hunter slowly, and pause at the prompts.')
R(L3, 'Go back to <strong>Chapter 16: Department of the South</strong> and find the night of the raid. June 2, 1863. Three Union gunboats steam up the Combahee River in South Carolina. Harriet Tubman is on board &mdash; she planned the raid. By morning, more than 700 enslaved people are free. It is the first U.S. military operation led by a woman. Read for what makes Harriet different from the male officers around her &mdash; and why the raid works.',
      'Go back to <strong>Chapter 16: Department of the South</strong> and find Harriet&rsquo;s talk with General Hunter, pages 152&ndash;155. She tells him the war can&rsquo;t be won &lsquo;by half measures&rsquo; and tells him the snake story. Then he reads her his answer to Congress. Read for what Sterling lets Harriet say &mdash; and what she lets the General say.')
R(L3, 'On June 2, 1863, three gunboats go up the Combahee River. <strong>What is Harriet&rsquo;s role on board?</strong>',
      'Harriet tells the snake story. <strong>What is the snake, and what does she want Mr. Lincoln to do?</strong>')
R(L3, 'More than 700 people are freed in one night. <strong>What does this tell us about what one person&rsquo;s knowledge can do?</strong>',
      'Harriet grins at the General&rsquo;s letter and says she never thought of calling slaveowners &lsquo;fugacious.&rsquo; <strong>What does this moment show about the two of them?</strong>')
R(L3, 'Read the raid section at your own pace.', 'Read the General Hunter section at your own pace.')
# RWM: a real Ch. 16 sentence that blends fact and meaning (p. 153)
R(L3, '<div class="rwm-sentence">&ldquo;She brought them out by the hundreds.&rdquo;<div style="margin-top:10px;font-family:\'Nunito\',sans-serif;font-style:normal;font-size:13px;color:#7A88A8;font-weight:700;">&mdash; narrator (about the Combahee Raid), <em>Freedom Train</em>, Ch. 16</div></div>',
      '<div class="rwm-sentence">&ldquo;Why, one third of the population of the Confederate states are Negro slaves. Think of what a force they&rsquo;d be on our side!&rdquo;<div style="margin-top:10px;font-family:\'Nunito\',sans-serif;font-style:normal;font-size:13px;color:#7A88A8;font-weight:700;">&mdash; General Hunter, <em>Freedom Train</em>, Ch. 16, p. 153</div></div>')
R(L3, 'June 2, 1863. Three Union gunboats go up the Combahee River, and Harriet is on board &mdash; she planned the raid. By morning more than 700 people are free. <strong>How does this sentence make one night sound like the size it really was?</strong>',
      'Harriet has just told the snake story. Washington will not send General Hunter more soldiers, and Congress says he may not let escaped slaves join the army. <strong>What is the General telling Harriet he wants to do?</strong>')
R(L3, 'Sterling puts a small, ordinary verb next to an enormous number, and the gap between them is the point. <strong>Brought them out</strong> is the plainest thing you could say &mdash; it sounds like walking people through a door. Then <strong>by the hundreds</strong> lands, and suddenly the door is a river and a war. Notice that Sterling does not write <em>more than 700</em> here, even though she gives you that exact number elsewhere in the chapter. <em>By the hundreds</em> is not more precise &mdash; it is bigger to the ear, because it sounds like it kept happening. The fact is the number; the explanation is the quiet verb she chose to sit beside it.',
      'Two sentences, two jobs. The first is a <strong>fact</strong> anyone could check: <strong>one third</strong> of the people in the Confederate states were enslaved. The second tells you what the fact <strong>means</strong>: <strong>think of what a force they&rsquo;d be on our side!</strong> A number by itself can just sit there. The General makes it move by saying right away why it matters. Notice the little word <strong>Why</strong> at the start. It makes the fact sound like something so plain that he can&rsquo;t believe Washington hasn&rsquo;t seen it. Fact first, then meaning.')
R(L3, 'Write one sentence about something a person did on a huge scale. Use the plainest verb you can find, then end with a number phrase that shows the scale. Let the two sit right next to each other.',
      'Write two sentences. The first states a fact with a number in it. The second begins with &ldquo;Think of&rdquo; and tells what the fact means.')
R(L3, '<div class="rwm-frame">[Character] ___ them out by the ___.</div>', '<div class="rwm-frame">___ (a fact with a number). Think of what ___!</div>')
R(L3, 'When and where did the Combahee River Raid happen? <strong>Give the date and the location.</strong>',
      'Where is Harriet in this chapter, and who is in charge there? <strong>Give the place and the person.</strong>')
R(L3, '<div class="textbox-prompt">June 2, 1863. South Carolina.</div>', '<div class="textbox-prompt">Beaufort, South Carolina. Major General David Hunter.</div>')
R(L3, 'placeholder="The Combahee River Raid happened on... in..."', 'placeholder="Harriet is in... The person in charge is..."')
R(L3, 'How many people did the raid free? <strong>What did Harriet do that no other commander could have done?</strong>',
      'What is Harriet&rsquo;s snake story about? <strong>What does she want Mr. Lincoln to do?</strong>')
R(L3, '<div class="textbox-prompt">Over 700 people. She knew the river, the people, the signals.</div>',
      '<div class="textbox-prompt">The snake is slavery. Treating the bites one at a time will never be enough.</div>')
R(L3, 'placeholder="The raid freed... Harriet could do what others couldn&rsquo;t because..."', 'placeholder="The snake stands for... Harriet wants Mr. Lincoln to..."')
R(L3, '<strong>What does Sterling want you to feel about the Combahee Raid?</strong>', '<strong>What does Sterling want you to feel about Harriet&rsquo;s talk with General Hunter?</strong>')
# Sam: the quote comes from the book, not a cut-down line
R(L3, '<em>Tubman believed deeply in her work.</em>', '<em>Tubman also used songs as SIGNALS. She promised the runaways hiding in a swamp that she would sing if it was safe.</em>')
R(L3, '<em>Tubman believed deeply in her work. As she put it in her own words, <strong>&ldquo;I had a right to liberty.&rdquo;</strong> That simple sentence captures why she returned south again and again &mdash; she believed that right belonged to every man, woman, and child still enslaved.</em>',
      '<em>Tubman also used songs as SIGNALS. Before she went to check the road, she told the runaways hiding in a swamp, <strong>&ldquo;If the coast is clear, I&rsquo;ll sing&rdquo;</strong> (Sterling, p. 97). A song was safer than a shout: anyone on the road could hear it, but only her group knew what it meant.</em>')
R(L3, 'He set it up (&lsquo;in her own words&rsquo;), dropped the quote, then explained what it meant.',
      'He set it up (who said it, and when), dropped the quote, then explained what it meant.')
R(L3, '<div>As Tubman put it in her own words...</div>', '<div>Before she went to check the road, Tubman told the runaways hiding in a swamp...</div>')
R(L3, '<div>&ldquo;I had a right to liberty.&rdquo;</div>', '<div>&ldquo;If the coast is clear, I&rsquo;ll sing&rdquo; (Sterling, p. 97).</div>')
R(L3, '<div>That simple sentence captures why she returned south again and again.</div>',
      '<div>A song was safer than a shout: anyone could hear it, but only her group knew what it meant.</div>')

R(L3, '          <span>On </span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'A month &mdash; capital J.\')">June</span>\n          <span>2, </span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'A year &mdash; comma after.\')">1863,</span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'A name &mdash; capital H.\')">Harriet</span>\n          <span>led </span>\n          <span>a </span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'Capital U &mdash; the proper name for the federal side.\')">Union</span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'Period ends the sentence.\')">raid.</span>',
      '          <span>In </span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'A town &mdash; capital B, and a comma after it.\')">Beaufort,</span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'A state &mdash; capital S and capital C, and a comma after the state too.\')">South Carolina,</span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'A name &mdash; capital H.\')">Harriet</span>\n          <span>met </span>\n          <span>a </span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'Capital U &mdash; the proper name for the federal side.\')">Union</span>\n          <span class="dol-highlight-word" onclick="dolHighlight(this,\'Period ends the sentence.\')">general.</span>')

# ---------- 23.4  Ch. 17 ----------
R(L4, '<div class="quote-strip-attr">&mdash; spiritual / Civil-War-era saying, Ch. 17</div>',
      '<div class="quote-strip-attr">&mdash; a woman sewing a flag in Beaufort (end of Ch. 16); Sterling repeats it all through Ch. 17</div>')
R(L4, 'The war is grinding on. Emancipation is in the air. Harriet keeps working. What does it feel like to be near a victory you have spent your whole life moving toward?',
      'Harriet nurses the sick and helps freed families earn a living. Then the news comes: on January 1, 1863, Mr. Lincoln will proclaim the end of slavery in the Rebel states. What does it feel like to be near a victory you have spent your whole life moving toward?')
R(L4, 'while Harriet nurses, scouts, and organizes.', 'while Harriet nurses, cooks, and organizes.')
R(L4, 'the soldiers fought less hopefully but harriet pushed on more faithfully than before',
      'the sick soldiers rested more easily but harriet worked harder than ever')
R(L4, '<strong>The</strong> soldiers fought <strong>less hopefully,</strong> but <strong>Harriet</strong> pushed on <strong>more faithfully</strong> than before.',
      '<strong>The</strong> sick soldiers rested <strong>more easily,</strong> but <strong>Harriet</strong> worked <strong>harder</strong> than ever.')
R(L4, 'Comparative adverbs: <em>less hopefully</em> (the soldiers&rsquo; fighting), <em>more faithfully</em> (Harriet&rsquo;s pushing on).',
      'Comparative adverbs: <em>more easily</em> (how the soldiers rested), <em>harder</em> (how Harriet worked; a short adverb takes -er).')
R(L4, '<p>A draft about Chapter 16. Some comparisons are right. Some use the wrong form entirely.</p>',
      '<p>A draft about Harriet&rsquo;s work. Some comparisons are right. Some use the wrong form entirely.</p>')
R(L4, '<p>A draft about Chapter 16. Some are spelled correctly.</p>', '<p>A draft about the war years. Some are spelled correctly.</p>')
R(L4, 'The soldiers grow tired. The wounded keep coming. Harriet nurses, cooks, scouts. She doesn&rsquo;t slow down. She knows the change is coming.',
      'Harriet bathes the soldiers&rsquo; wounds, brews herb tea for a fever ward in Florida, and builds a washhouse so freedwomen can earn money. &lsquo;Our time is coming,&rsquo; the chapter keeps saying, and on January 1, 1863, it comes.')
R(L4, 'The war drags on through 1864 and into 1865. Harriet keeps nursing, scouting, organizing. Emancipation has been declared but slavery is not yet ended everywhere. Read for the small moments &mdash; conversations, songs, kindnesses &mdash; that show what Harriet is feeling as the long war moves closer to its end.',
      'It is 1862. In Beaufort, Harriet nurses the sick and teaches freedwomen to earn a living, and everyone waits for news from Washington: Mr. Lincoln will proclaim the end of slavery in the Rebel states on January 1, 1863. Read for the small moments &mdash; conversations, songs, kindnesses &mdash; that show what Harriet is feeling as that day comes closer.')
R(L4, '<div class="textbox-prompt">Nurse. Scout. Cook. Sometimes she leads.</div>',
      '<div class="textbox-prompt">Nurse at the hospital. Teacher of washing, sewing, and cooking. Baker of pies and gingerbread to sell.</div>')
# Sam: fully elaborated body 1, every fact from Sterling
R(L4, '<em>One way Tubman used songs was as a CODE for directions. The song &lsquo;Follow the Drinking Gourd,&rsquo; collected by the National Park Service from oral history, told runaways to follow the Big Dipper &mdash; the constellation that points to the North Star. The song even described specific landmarks like rivers and mountains along the route. As one historian explains, <strong>&ldquo;the song was a map you could sing.&rdquo;</strong> Singing the directions aloud meant slave catchers heard music. Runaways heard a plan.</em>',
      '<em>One way Tubman used songs was to carry a hidden MESSAGE. When she ran away, she could not say goodbye out loud, so she walked past the slave quarters singing &lsquo;When that old chariot comes, I&rsquo;m going to leave you&rsquo; (Sterling, p. 66). Years later her mother, Old Rit, used the same trick: with the sheriff standing right there, she sang &lsquo;Good news, the chariot&rsquo;s coming&rsquo; to tell Harriet&rsquo;s father in jail that rescue was on its way (Sterling, p. 112). As Sterling writes, there were people in those cabins <strong>&ldquo;who never forgot the song they heard that night.&rdquo;</strong> The sheriff heard an old woman singing a hymn. Ben heard the plan.</em>')
R(L4, 'added a third fact (landmarks), added a specific source (National Park Service), and added a quote (&lsquo;the song was a map you could sing&rsquo;).',
      'added a third fact (Old Rit&rsquo;s song at the jail), added a specific source (Sterling, with page numbers), and added a quote (&lsquo;who never forgot the song they heard that night&rsquo;).')
R(L4, '<div>Tubman used songs as a CODE for directions.</div>', '<div>Tubman used songs to carry a hidden MESSAGE.</div>')
R(L4, '<div>&lsquo;Drinking Gourd&rsquo; pointed to the North Star.</div>', '<div>She sang &lsquo;When that old chariot comes&rsquo; to say goodbye.</div>')
R(L4, '<div>collected by the National Park Service from oral history</div>', '<div>Sterling, <em>Freedom Train</em>, pp. 66 and 112</div>')
R(L4, '<div>described specific landmarks &mdash; rivers and mountains</div>', '<div>Old Rit sang &lsquo;Good news, the chariot&rsquo;s coming&rsquo; to Ben in jail.</div>')
R(L4, '<div>&ldquo;The song was a map you could sing.&rdquo;</div>', '<div>&ldquo;who never forgot the song they heard that night&rdquo;</div>')
R(L4, '<div>Slave catchers heard music. Runaways heard a plan.</div>', '<div>The sheriff heard a hymn. Ben heard the plan.</div>')

# ---------- fluency: real Ch. 15 text (p. 143) ----------
R(FL, 'From Chapter 15 — Wendell Phillips praises Harriet', 'From Chapter 15 — John Brown praises Harriet')
R(FL, '        Wendell Phillips, who had seen many soldiers, looked at Harriet and shook his head. &ldquo;The most of a man, naturally,&rdquo; he said, &ldquo;that I ever met.&rdquo;',
      '        For ten days John Brown stayed in St. Catharines with Harriet Tubman. Poring over his map, Harriet described the countryside where he proposed to begin operations. She located Underground Railroad stations for him, tracing the routes northward through Maryland and Pennsylvania. So impressed was he with her courage and leadership that he frequently spoke of her in masculine terms. &ldquo;Harriet Tubman hooked on his whole team at once,&rdquo; John Brown reported in a letter to his son. &ldquo;He is the most of a man, naturally, that I ever met with.&rdquo;')
R(FL, 'This short passage comes from the moment when Wendell Phillips names Harriet&rsquo;s courage. Read the narrator calmly, then give Phillips&rsquo;s words a thoughtful pause.',
      'This passage comes from the moment when John Brown names Harriet&rsquo;s courage. Read the narrator calmly, then give Brown&rsquo;s words a thoughtful pause.')
R(FL, '<strong>&mdash; Dorothy Sterling, <em>Freedom Train</em>, Ch. 15</strong>', '<strong>&mdash; Dorothy Sterling, <em>Freedom Train</em>, Ch. 15, p. 143</strong>')

# ---------- check-in: Ch. 15-17, real passages ----------
R(CK, '<em>Freedom Train</em> &#8212; Chapters 13&#8211;16</div>', '<em>Freedom Train</em> &#8212; Chapters 15&#8211;17</div>')
R(CK, 'In Chapters 13&#8211;16, we see Harriet through', 'In Chapters 15&#8211;17, we see Harriet through')
R(CK, 'Read the passage. What does <strong>perspective</strong> mean in this sentence?',
      'This passage shows two very different <strong>perspectives</strong> on Harriet. What does <strong>perspective</strong> mean?')
R(CK, '&#8220;Dorothy Sterling&#8217;s perspective toward Harriet Tubman is one of deep admiration &#8212; the author clearly believes that Tubman&#8217;s choices were not just brave, but historically essential.&#8221;<div class="excerpt-source">&#8212; <em>Freedom Train</em>, Ch. 13&#8211;16</div>',
      '&#8220;Thus Harriet became a symbol of her people in this great debate. To the slaveowners, she was &#8216;weak-minded&#8217; and &#8216;deluded&#8217;; to the Abolitionists she was &#8216;the greatest heroine of the age.&#8217;&#8221;<div class="excerpt-source">&#8212; <em>Freedom Train</em>, Ch. 15, p. 137</div>')
R(CK, 'Use the word <strong>evident</strong> in a sentence', 'Use the word <strong>persist</strong> in a sentence')
R(CK, "data-label=\"Q6: Sentence using 'evident' showing its meaning\"", "data-label=\"Q6: Sentence using 'persist' showing its meaning\"")
R(CK, '      &#8220;Sterling does not simply record what Harriet did &#8212; she explains why it mattered. Every detail she chooses seems designed to show the reader that Harriet Tubman was not just a survivor, but a leader who changed the course of history.&#8221;\r\n      <div class="excerpt-source">&#8212; <em>Freedom Train</em>, Ch. 13&#8211;16</div>',
      '      &#8220;Harriet&#8217;s steady hands and practical good humor brought her into demand as nurse among both contrabands and soldiers. &#8230; From the roots of swamp plants she prepared a drink which cooled their parched throats. Sipping it, they felt refreshed, and they swore that it was Harriet and her herb tea which were curing them.&#8221;\r\n      <div class="excerpt-source">&#8212; <em>Freedom Train</em>, Ch. 17, pp. 160&#8211;161</div>')
R(CK, '(Ch. 13–16)" id="resp9"', '(Ch. 15–17)" id="resp9"')
R(CK, 'a fact from Chapters 13&#8211;16 and then', 'a fact from Chapters 15&#8211;17 and then')
R(CK, 'data-label="Q12: Fact from Ch. 13–16 + explanation', 'data-label="Q12: Fact from Ch. 15–17 + explanation')
FILES[CK] = load(CK).replace('Freedom Train (Ch. 13–16)', 'Freedom Train (Ch. 15–17)')

# ---------- Sam's research essay, weeks 21-22: the songs Sterling actually records ----------
S1, S3, S4 = 'lesson-21-4-ft-ch8.html', 'lesson-22-3-ft-ch11.html', 'lesson-22-4-ft-ch12.html'
R(S1, '<strong>CATEGORY 1: Code songs and their meanings</strong> (notes from Sterling p.76, NPS, Bradford)<br><strong>CATEGORY 2: Signal songs near plantations</strong> (Sterling p.66, NPS)<br><strong>CATEGORY 3: Why songs worked as code</strong> (NPS, Bradford)',
      '<strong>CATEGORY 1: Songs that carried a hidden message</strong> (notes from Sterling p.66, p.112, Bradford)<br><strong>CATEGORY 2: Signal songs: the coast is clear</strong> (Sterling p.93, pp.97&ndash;98, NPS)<br><strong>CATEGORY 3: Why songs worked when notes couldn&rsquo;t</strong> (Sterling p.27, NPS)')
R(S1, '<br>Code songs (e.g. <em>Drinking Gourd</em>) and their meanings</div>', '<br>Songs that carried a hidden message (e.g. the <em>chariot</em> song)</div>')
R(S1, '<br>Signal songs sung near plantations</div>', '<br>Signal songs: the coast is clear</div>')
R(S3, 'Sam takes his Category 1 ("Code songs and their meanings") and writes a paragraph.', 'Sam takes his Category 1 ("Songs that carried a hidden message") and writes a paragraph.')
R(S3, '<em>Tubman used songs. One was Follow the Drinking Gourd. It was about directions.</em>', '<em>Tubman used songs. One was about a chariot. It was a goodbye.</em>')
R(S3, '<em>One way Tubman used songs was as a CODE for directions. The song <em>Follow the Drinking Gourd</em>, sung by enslaved people across the South, told runaways to follow the Big Dipper &mdash; the constellation that points to the North Star. According to the National Park Service, the song wasn&rsquo;t just folk music. It was a map. Singing the song aloud gave directions to anyone listening &mdash; without ever writing them down where a slave catcher could find them.</em>',
      '<em>One way Tubman used songs was to carry a hidden MESSAGE. When she ran away, she could not say goodbye out loud, because anyone might be listening. So she walked past the slave quarters singing &lsquo;When that old chariot comes, I&rsquo;m going to leave you&rsquo; (Sterling, p. 66). Her family heard a hymn about heaven, but they understood she was leaving. A song could say what words could not.</em>')
R(S3, '<div>One way Tubman used songs was as a CODE for directions.</div>', '<div>One way Tubman used songs was to carry a hidden MESSAGE.</div>')
R(S3, '<div>Follow the Drinking Gourd told runaways to follow the Big Dipper / North Star (NPS).</div>',
      '<div>She sang &lsquo;When that old chariot comes, I&rsquo;m going to leave you&rsquo; to say goodbye (Sterling, p. 66).</div>')
R(S3, '<div>Singing aloud gave directions without writing them down where a slave catcher could find them.</div>', '<div>A song could say what words could not.</div>')
R(S4, 'Sam writes body paragraph 2 from his Category 2 ("Signal songs near plantations").', 'Sam writes body paragraph 2 from his Category 2 ("Signal songs: the coast is clear").')
R(S4, '<em>Beyond directions, Tubman used songs as SIGNALS. As she approached a plantation in the dead of night, she would sing <em>Go Down, Moses</em> &mdash; a spiritual that sounded like ordinary praise music. But to enslaved people who knew what to listen for, the song was a coded signal: <em>I&rsquo;m here. Be ready.</em> According to Sterling&rsquo;s biography, a verse sung twice or a changed word could carry a warning, so Tubman could communicate without ever speaking. Slave catchers heard a religious song. Her passengers heard the cue to move.</em>',
      '<em>Beyond hidden messages, Tubman used songs as SIGNALS. Once she left a group of runaways hiding in a swamp while she went to check the road, and she promised to sing if it was safe. Minutes later they heard <em>Go Down, Moses</em> floating toward them, and they knew it was time to move (Sterling, pp. 97&ndash;98). Anyone else on the road heard a hymn. Her passengers heard the cue to move.</em>')
R(S4, '<div>Tubman also used songs as SIGNALS near plantations.</div>', '<div>Tubman also used songs as SIGNALS that it was safe.</div>')
R(S4, '<div>Sang <em>Go Down, Moses</em>; sounded like praise music; signaled &lsquo;I&rsquo;m here. Be ready.&rsquo; (Sterling)</div>',
      '<div>Promised to sing if the road was clear; then sang <em>Go Down, Moses</em>, and the runaways came out of the swamp (Sterling, pp. 97&ndash;98).</div>')
R(S4, '<div>Slave catchers heard a religious song. Her passengers heard a cue.</div>', '<div>Anyone else heard a hymn. Her passengers heard a cue.</div>')

for f, s in FILES.items():
    if '--apply' in sys.argv:
        io.open(f, 'w', encoding='utf-8', newline='').write(s)
    print(('written ' if '--apply' in sys.argv else 'ok ') + f)
