#!/usr/bin/env python3
"""'What to do' steps for every activity in G4 ELA week 7 (Nov 10 2026, ahead of
the pilot review). Writes DATA.todo into data/lesson-7-N.json and each page's
oao-data block. Steps say exactly what to tap, read and write, in order."""
import io, json, re, glob

DOL = {"find": "Daily Oral", "steps": ["Tap each yellow part of the first sentence to see why it is correct.", "Pick Sentence A or Sentence B.", "Type it the right way in the box, then tap Check My Work."]}
CT = {"find": "Chapter Thinking", "steps": ["Pick Explorer or Scholar.", "Answer all three questions in full sentences.", "Use a detail from the book in every answer. The hint under each question helps."]}
WSC = {"find": "Word Study Connection", "steps": ["Nothing to do here. Your Word Study answer shows up in your work below."]}
def read(ch, notes):
    return {"find": "^\\s*\\S*\\s*Read:", "steps": ["Read the Pause & Think questions first.", "Open your book and read " + ch + ".", "Stop at each question and think of your answer.", "As you read, fill in the " + notes + " boxes."]}
def wgrd(where):
    return {"find": "What Good Readers", "steps": ["Read the tip and the three How to Do It steps.", "Keep the question at the bottom in your head while you read.", "Nothing to write here." + where]}
def ww(look, do):
    return {"find": "Writer.s Workshop", "steps": ["Read Today's focus. Then read how Sam " + look + ".", do, "Type it in the box.", "Tap Copy today's writing and paste it into your own document."]}

T = {
1: [wgrd(" Your note boxes are on the Reading tab."), DOL,
    {"find": "Morphology", "steps": ["Read the four words. Look at how each one starts.", "Answer the Try these first questions in your head.", "Tap See if you cracked it.", "Type the missing prefix in each word, then tap Check My Work.", "Use a con- or com- word in a sentence in the Show What You Know box."]},
    {"find": "Vocabulary", "steps": ["Read how we figured out companion.", "Read each sentence, guess what the word means, then tap the card to check.", "Play Quick Match: tap a word, then tap its meaning."]},
    {"find": "Grammar", "steps": ["Look at the six plurals. Some follow the -s rule and some don't.", "Tap a word, then tap Group A or Group B to sort it.", "Tap Now check your thinking.", "Name both groups in the Show What You Know box."]},
    {"find": "Spelling", "steps": ["Look at the six plurals and how each one ends.", "Tap a word, then tap the group it belongs in.", "Tap Now check your thinking.", "Write the rule in the Show What You Know box."]},
    {"find": "Copia", "steps": ["Read the sentence about Mrs. Rachel.", "Write it three new ways, one box at a time.", "Stuck? Tap Show one way."]},
    read("Chapter 1", "Whose view is it?"), CT,
    ww("picked his idea", "Make your own list of three ideas, then pick one. Write the one sentence that starts your story.")],
2: [wgrd(" Your note boxes are on the Reading tab."), DOL,
    {"find": "Poetry", "steps": ["Read the poem out loud.", "Read the Think About It question.", "Think of your answer. Nothing to write here."]},
    {"find": "Morphology", "steps": ["Read what con- and com- mean.", "Tap a word part, then tap its meaning.", "Match them all."]},
    {"find": "Vocabulary", "steps": ["Tap a word, then tap its meaning.", "Match all four words."]},
    {"find": "Grammar", "steps": ["Read the sentence about Chapter 2.", "Tap every irregular plural. There is more than one.", "In the box, write one you tapped and its singular form."]},
    {"find": "Spelling", "steps": ["Read the sentence about Chapter 2.", "Tap every plural that needed more than a plain -s.", "In the box, explain the rule for one you tapped."]},
    read("Chapter 2", "Riding along with Matthew"), CT,
    ww("made a character card", "Make your own character card: a name, one thing your kid wants, and one thing your kid is afraid of.")],
3: [DOL,
    {"find": "Morphology", "steps": ["Read what con- and com- mean.", "Type the missing prefix at the start of each word.", "Tap Check My Work."]},
    {"find": "Vocabulary", "steps": ["Read each sentence.", "Type the missing word from the word bank.", "Tap Check My Work."]},
    {"find": "Grammar", "steps": ["Type the plural of each word in brackets.", "Tap Check My Work.", "In the box, write your own sentence with an irregular plural."]},
    {"find": "Spelling", "steps": ["Type the plural of each word in brackets.", "Tap Check My Work.", "In the box, make one more plural and name the rule."]},
    {"find": "What Good Readers", "steps": ["Read the tip and the three How to Do It steps.", "Keep the question in your head while you read Chapters 3 and 4.", "Nothing to write here."]},
    read("Chapters 3 and 4", "Whose word is it?"), CT,
    ww("swapped plain words for specific ones", "Use the word-choice planner to pick specific words for your kid.")],
4: [DOL,
    {"find": "Poetry", "steps": ["Read the poem out loud.", "Read the Think About It question.", "Think of your answer. Nothing to write here."]},
    {"find": "Morphology", "steps": ["Read what con- and com- mean.", "Tap a word part, then tap its meaning.", "Match them all."]},
    {"find": "Vocabulary", "steps": ["Pick ONE activity from the menu.", "Write your answer in the Show What You Know box."]},
    {"find": "Grammar", "steps": ["Read the short draft.", "Tap only the sentences with a plural mistake.", "In the box, fix one and say why the -s rule does not work."]},
    {"find": "Spelling", "steps": ["Tap only the words that are spelled wrong.", "In the box, fix one and name the rule it broke."]},
    {"find": "What Good Readers", "steps": ["Read the tip and the three How to Do It steps.", "Keep the question in your head while you read Chapter 5.", "Nothing to write here."]},
    read("Chapter 5", "Move the chair"), CT,
    ww("showed Mateo's reaction", "Climb the reaction ladder: what your kid says, what your kid does, and what your kid's body does.")],
}
for d, todo in T.items():
    p = 'data/lesson-7-%d.json' % d
    j = json.load(io.open(p, encoding='utf-8')); j['todo'] = todo
    import subprocess
    orig = subprocess.run(['git', 'show', 'origin/main:' + p], capture_output=True, text=True).stdout or io.open(p, encoding='utf-8').read()
    ind = len(orig.split('\n')[1]) - len(orig.split('\n')[1].lstrip(' '))
    io.open(p, 'w', encoding='utf-8').write(json.dumps(j, ensure_ascii=False, indent=ind) + ('\n' if orig.endswith('\n') else ''))
    f = glob.glob('lesson-7-%d-*.html' % d)[0]; h = io.open(f, encoding='utf-8').read()
    m = re.search(r'(id="oao-data">\s*)(\{.*?\})(\s*</script>)', h, re.S)
    k = json.loads(m.group(2)); k['todo'] = todo
    h = h[:m.start(2)] + json.dumps(k, ensure_ascii=False, indent=1) + h[m.end(2):]
    io.open(f, 'w', encoding='utf-8').write(h); print(f, len(todo), 'activities')
