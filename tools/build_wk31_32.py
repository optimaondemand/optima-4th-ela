#!/usr/bin/env python3
"""Writes data/lesson-31-1..4.json and data/lesson-32-1..4.json (year-end synthesis + final project). Guide: Opti (he/him).
Q4: scripts written, not recorded. Every book moment in the Watch is checked in the text (Prince Caspian PDF, Bethany's copy of
Number the Stars, Anne of Green Gables public-domain text). No word game (no fill-in word-part blanks these weeks).
Run with an argument: 31 or 32."""
import json, io, sys
W = int(sys.argv[1]) if len(sys.argv) > 1 else 31
K = "Seven Pillars Watch"; I = "🏛️"
PIL = ["Honesty", "Respect", "Courtesy", "Responsibility", "Courage", "Service", "Perseverance"]
BOOKS = "Mrs. Frisby and the Rats of NIMH, Anne of Green Gables, Number the Stars, Freedom Train and Prince Caspian"
def media(w, d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/opti/g4ela-%d-%d-welcome" % (w, d), "label": "Opti’s welcome"},
         "read": {"kind": "audio", "path": "guide/opti/g4ela-%d-%d-read" % (w, d), "label": "Opti · before you start"},
         ws: {"kind": "video", "path": "guide/opti/g4ela-%d-%d-%s" % (w, d, ws), "label": "Opti · " + wslabel}}
    for off in ("guide1", "guide2", "guide3", "rwm", "copia"): m[off] = {"kind": ""}
    return m
def dol(raw, fixed, why, raw2, fixed2, why2):
    return {"a": {"raw": raw, "fixed": fixed, "why": why}, "b": {"raw": raw2, "fixed": fixed2, "why": why2}}
B = lambda s: "<strong>" + s + "</strong>"
def pv(title, intro, items):
    return {"kind": "pillars", "title": title, "intro": intro, "pillars": PIL, "items": items}
def log(title, intro, line, ph):
    return {"kind": "log", "title": title, "intro": intro, "options": [{"t": p} for p in PIL], "line": line, "placeholder": ph}
V31 = [["theme", "The big idea about life that a story keeps showing."], ["compare", "To tell how two things are alike."],
       ["contrast", "To tell how two things are different."], ["evidence", "Details from the text that prove what you say."]]
V32 = [["revise", "To change your writing to make the ideas better."], ["proofread", "To check writing for mistakes in capitals, usage, punctuation and spelling."],
       ["portfolio", "A collection of your best work."], ["reflect", "To think back on something and what it taught you."]]
GR = "Spiral review: capitals, commas, quotation marks, complete sentences. Read your sentence out loud and check each mark has a job."
SP = "Spiral review: drop the silent e, change y to i, double the last consonant when the beat is on the last syllable, and spell each word part the same way every time."
WP = "Every base from the year: port, tract, struct, spect, ject, script, rupt, duct, form, press, tain, lev, plus prefixes like pre-, re-, trans-, inter-."
CT = lambda n="three": {"find": "Thinking", "steps": ["Pick Explorer or Scholar.", "Answer all %s questions in full sentences." % n, "Use a detail from a book in every answer. The hint under each question helps.", "Last, write one or two sentences about your reading lens."]}
WGRD = {"find": "What Good Readers", "steps": ["Read the tip and the lenses.", "Tap the lens you will use today.", "Keep it in mind as you work."]}
DOLT = {"find": "Daily Oral", "steps": ["Tap each yellow part of the first sentence to see why it is correct.", "Pick Sentence A or Sentence B.", "Type it the right way in the box, then tap Check My Work."]}
COPY = {"find": "Copywork", "steps": ["Read the sentence and the note under it.", "Copy it in cursive in your reading journal, slowly."]}
POEM = {"find": "Poetry Corner", "steps": ["Read the poem slowly.", "Think about the question under it.", "Write your thinking in the box."]}
SHELF = {"find": "Reading Shelf", "steps": ["Look at the five books from this year.", "Think of one moment from each that fits your theme."]}

L = {}; T = {}; WS = {}
if W == 31:
    WS = {1: ("morphology", "a year of word parts"), 2: ("grammar", "every mark has a job"), 3: ("spelling", "check the pattern"), 4: ("grammar", "your best sentence")}
    common = {"writingFocus": "Compare", "notes": {"wgrd": "Compare themes across texts: name a theme, find it in two books, and say how the characters show it alike and differently.", "vocab": V31, "wordParts": WP, "grammar": GR, "spelling": SP}}
    L[1] = {"connector": "Hoo, hello! You’ve read five books this year: " + BOOKS + ". This week you put them side by side. A theme is a big idea a story keeps coming back to, and the best ones show up in more than one book. Pick one today.",
            "dol": dol("peter said to caspian i havent come to take your place you know but to put you into it",
                       B("Peter") + " said to " + B("Caspian") + B(",") + " &ldquo;" + B("I haven’t") + " come to take your place" + B(",") + " you know" + B(",") + " but to put you into it" + B(".") + "&rdquo;",
                       "Peter’s real words (Prince Caspian, Ch. 12): capitals on Peter, Caspian and I; an apostrophe in haven’t; commas around you know; the period inside the quotation marks.",
                       "this year we read five books and we kept a learning journal",
                       B("This") + " year we read five books" + B(",") + " and we kept a learning journal" + B("."),
                       "Capital T to start; a comma before and joins two complete thoughts; a period ends it."),
            "scholar": {"journal-q1": "… and say how a theme is different from a topic.", "journal-q2": "… and name two books where you see it.", "journal-q3": "… and quote the character."},
            "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": True, "count": 1}},
            "copia": {"seed": "Annemarie <b data-verb>kept</b> Ellen’s necklace safe.", "eg": ["When the soldiers came, Annemarie kept Ellen’s necklace safe.", "Annemarie <i>clutched</i> Ellen’s necklace.", "Annemarie kept Ellen’s necklace safe, hidden in her fist."]},
            "wgrd": {"catcher": {"title": "My theme", "intro": "Choose a theme and find it.", "fields": [{"label": "The theme I chose", "hint": "courage, loyalty, belonging…", "rows": 1}, {"label": "Books and moments where I see it", "hint": "", "rows": 4}], "end": {"label": "What this theme means in real life", "hint": ""}}, "useAt": ["journal-q2", "journal-q3"]},
            "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 40},
            "virtue": pv("Which pillar is it?", "The OAO Seven Pillars are honesty, respect, courtesy, responsibility, courage, service and perseverance. These moments come from three books this year. Tap the pillar each one shows best.",
              [{"t": "Number the Stars: Uncle Henrik tells Annemarie, “That’s all that brave means — not thinking about the dangers. Just thinking about what you must do.”", "ok": ["Courage"], "why": "Brave means doing what you must, even when you are afraid.", "hint": "What does Uncle Henrik say brave means?"},
               {"t": "Anne of Green Gables: Matthew says, “Well now, I’d rather have you than a dozen boys, Anne.”", "ok": ["Respect", "Courtesy"], "why": "He tells Anne she is valued just as she is.", "hint": "How does Matthew make Anne feel?"},
               {"t": "Prince Caspian: Peter tells Caspian, “I haven’t come to take your place, you know, but to put you into it.”", "ok": ["Service", "Respect"], "why": "He uses his power to help Caspian, not to replace him.", "hint": "Who could have been king?"}])}
    L[2] = {"connector": "Last time you chose a theme. Today you find it in two different books and line the two characters up side by side. How do they show the same idea, and how do they show it differently?",
            "dol": dol("we might be some good to her said matthew suddenly and unexpectedly",
                       "&ldquo;" + B("We") + " might be some good to her" + B(",") + "&rdquo; said " + B("Matthew") + " suddenly and unexpectedly" + B("."),
                       "Matthew’s real words (Anne of Green Gables, Ch. 3): the comma goes inside the closing quotation mark, then the tag, then a period.",
                       "anne and annemarie are both brave but they show it in different ways",
                       B("Anne") + " and " + B("Annemarie") + " are both brave" + B(",") + " but they show it in different ways" + B("."),
                       "Capitals on both names; a comma before but joins two complete thoughts; a period ends it."),
            "scholar": {"journal-q1": "… and quote each character once.", "journal-q2": "… and name what drives each one.", "journal-q3": "… and say what would change if that moment were missing."},
            "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
            "wgrd": {"catcher": {"title": "Two characters, one theme", "intro": "Line them up.", "fields": [{"label": "Character 1, book, and moment", "hint": "", "rows": 2}, {"label": "Character 2, book, and moment", "hint": "", "rows": 2}], "layout": "row", "end": {"label": "Alike: … Different: …", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
            "counters": {"journal-q1": 40, "journal-q2": 40, "journal-q3": 32},
            "virtue": pv("Which pillar is it?", "More moments from this year’s books. Tap the pillar each one shows best.",
              [{"t": "Number the Stars: When the soldiers come, Annemarie clutches Ellen’s Star of David so hard it leaves its print in her hand.", "ok": ["Courage", "Service"], "why": "She protects her friend in a dangerous moment.", "hint": "Whose secret is she keeping safe?"},
               {"t": "Prince Caspian: Susan says to Lucy, “I see him now. I’m sorry.”", "ok": ["Honesty"], "why": "She admits she was wrong.", "hint": "What does Susan admit?"},
               {"t": "Prince Caspian: Trufflehunter says, “I’m a beast and we don’t change. I’m a badger, what’s more, and we hold on.”", "ok": ["Perseverance"], "why": "He held on to the truth for a very long time.", "hint": "What does holding on mean?"}])}
    L[3] = {"connector": "You have the theme and two characters. Today you build the comparison paragraph: a theme sentence, evidence from both books, and what makes them alike and different. Build it like a bridge, one board at a time.",
            "dol": dol("go now and get into your nightgowns it will be a long night",
                       "&ldquo;" + B("Go") + B(",") + " now" + B(",") + " and get into your nightgowns" + B(".") + " " + B("It") + " will be a long night" + B(".") + "&rdquo;",
                       "Real words from Number the Stars, Ch. 4: two sentences inside one pair of quotation marks; commas set off now; each sentence starts with a capital and ends with a period.",
                       "harriet and caspian both had to leave home in the night",
                       B("Harriet") + " and " + B("Caspian") + " both had to leave home in the night" + B("."),
                       "Capitals on the two names; no comma needed with one subject and one verb; a period ends it."),
            "scholar": {"journal-q1": "… and use one quote from each book.", "journal-q2": "… and fix one sentence you find.", "journal-q3": "… and name the third book."},
            "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
            "wgrd": {"catcher": {"title": "Build the paragraph", "intro": "Plan before you write.", "fields": [{"label": "Theme sentence", "hint": "", "rows": 1}, {"label": "Evidence from book 1", "hint": "", "rows": 2}, {"label": "Evidence from book 2", "hint": "", "rows": 2}], "end": {"label": "Alike and different, in one sentence", "hint": ""}}, "useAt": ["journal-q1"]},
            "counters": {"journal-q1": 80, "journal-q2": 32, "journal-q3": 32},
            "virtue": pv("Which pillar is it?", "One more set of moments from this year. Tap the pillar each one shows best.",
              [{"t": "Prince Caspian: Peter steps back when Miraz trips, and waits for him to rise.", "ok": ["Courtesy", "Respect"], "why": "He won’t strike a fallen enemy.", "hint": "What could Peter have done?"},
               {"t": "Prince Caspian: Caspian says he doesn’t feel sufficient to be King. “I’m only a kid.”", "ok": ["Honesty"], "why": "He tells the truth about himself.", "hint": "What does Caspian admit?"},
               {"t": "Anne of Green Gables: Matthew tells Anne, “It was a girl — my girl — my girl that I’m proud of.”", "ok": ["Respect"], "why": "He honours what Anne worked for.", "hint": "What is Matthew proud of?"}])}
    L[4] = {"connector": "Five books, side by side. Today you step back and ask what you discovered. Your theme isn’t just about Narnia or Denmark or Avonlea. It’s about people. Say what it means, in one sentence you’d be proud to sign.",
            "dol": dol("peter said he says were getting too old",
                       B("Peter") + " said" + B(",") + " &ldquo;" + B("He") + " says " + B("we’re") + " getting too old" + B(".") + "&rdquo;",
                       "Peter’s real words to Lucy (Prince Caspian, Ch. 15): we’re is we are, so it needs an apostrophe.",
                       "my favorite book this year was number the stars because annemarie was so brave",
                       B("My") + " favorite book this year was " + B("Number the Stars") + B(",") + " because " + B("Annemarie") + " was so brave" + B("."),
                       "Capitals on My, on each main word of the title and on Annemarie; a period ends it. (A comma before because is optional here.)"),
            "scholar": {"journal-q1": "… and name what surprised you.", "journal-q2": "… and quote one line from it.", "journal-q3": "… and say what you think they would answer."},
            "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
            "wgrd": {"catcher": {"title": "What I discovered", "intro": "Look back at the whole week.", "fields": [{"label": "My theme across the books", "hint": "", "rows": 2}, {"label": "What it says about people", "hint": "", "rows": 2}], "end": {"label": "My one-sentence takeaway", "hint": ""}}, "useAt": ["journal-q1"]},
            "counters": {"journal-q1": 40, "journal-q2": 40, "journal-q3": 32},
            "virtue": log("This year’s strongest pillar", "Think about all five books. Which pillar did the characters show most this year? Tap one.", "Name one moment from any book that proves it.", "The strongest pillar this year was … because in …")}
    T = {1: {"welcome": "Hoo, hello! It’s Opti. You’ve read five books this year, and now you get to put them side by side. Today’s question: what big ideas show up in more than one story?",
             "read": "A theme isn’t one word on a page. It’s a big idea about life that a story keeps showing, like courage or belonging. Look at your reading shelf. Pick one theme, and find one character who shows it.",
             "morphology": "You learned a lot of word parts this year. Port means carry. Spect means look. Rupt means break. Pre means before. When you meet a long word, find a part you know, and the word starts to explain itself."},
         2: {"welcome": "Hoo! It’s Opti. You chose a theme. Today you find it in two different books. Today’s question: how can two characters show the same idea in different ways?",
             "read": "Pick two characters from two books who show your theme. Write one moment for each. Then ask: how are they alike, and how are they different? Think about what makes each one act.",
             "grammar": "Every punctuation mark has a job. A capital starts a sentence and a name. A comma joins or separates. Quotation marks hold someone’s exact words. Read your sentence out loud, and ask each mark: what’s your job?"},
         3: {"welcome": "Hello again, it’s Opti. Today you build your comparison paragraph. Today’s question: how do you prove two characters share a theme?",
             "read": "Start with your theme sentence. Then evidence from the first book, then the second. Then say how they’re alike and how they’re different. Use real words from the books as your proof.",
             "spelling": "Before you hand in writing, check the patterns you know. Did a silent e drop before a suffix? Did a y change to i? Did a consonant double? Check one pattern at a time, and you’ll catch more."},
         4: {"welcome": "Hoo! It’s Opti. Five books, side by side. Today’s question: what did you discover about people from all of them together?",
             "read": "Step back from the whole week. Your theme is about more than one story. It’s about real people too. Write what you discovered in one strong sentence you would be proud to sign.",
             "grammar": "Your best sentence deserves a careful check. Capital at the start. Names capitalized. Commas where they join or separate. Quotation marks around exact words. An end mark that fits. Then read it out loud one last time."}}
else:
    WS = {1: ("morphology", "roots you can still use"), 2: ("grammar", "proofread like an editor"), 3: ("spelling", "the last check"), 4: ("grammar", "the final sentence")}
    common = {"writingFocus": "Reflect", "notes": {"wgrd": "Reflect on how your reading habits have grown: who you were as a reader in August, who you are now, and the proof.", "vocab": V32, "wordParts": WP, "grammar": GR, "spelling": SP}}
    L[1] = {"connector": "Hoo! The last week of 4th grade ELA. This week you polish your comparison paragraph, look back at how you’ve grown, and celebrate. Today: make your best paragraph even better.",
            "dol": dol("matthew cuthbert i believe that child has bewitched you said marilla",
                       "&ldquo;" + B("Matthew Cuthbert") + B(",") + " " + B("I") + " believe that child has bewitched you" + B("!") + "&rdquo; said " + B("Marilla") + B("."),
                       "Marilla’s real words (Anne of Green Gables, Ch. 3): a comma after the name of the person spoken to; the exclamation point inside the quotation marks.",
                       "i revised my paragraph and i fixed three spelling mistakes",
                       B("I") + " revised my paragraph" + B(",") + " and " + B("I") + " fixed three spelling mistakes" + B("."),
                       "Capital I both times; a comma before and joins two complete thoughts; a period ends it."),
            "scholar": {"journal-q1": "… and say which revision helped most.", "journal-q2": "… and give the before and after for one.", "journal-q3": "… and say what would raise it one level."},
            "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
            "copia": {"seed": "I <b data-verb>grew</b> as a reader this year.", "eg": ["Book by book, I grew as a reader this year.", "I <i>stretched</i> as a reader this year.", "I grew as a reader this year, from August to May."]},
            "wgrd": {"catcher": {"title": "Before and after", "intro": "Revise like a writer.", "fields": [{"label": "One sentence before", "hint": "", "rows": 2}, {"label": "The same sentence after", "hint": "", "rows": 2}], "layout": "row", "end": {"label": "What the change did", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
            "counters": {"journal-q1": 80, "journal-q2": 24, "journal-q3": 32}}
    L[2] = {"connector": "Last time you polished your writing. Today you write about yourself as a reader. Who were you in August, and who are you now? Bring proof, the way you would for a character.",
            "dol": dol("put this packet underneath do you understand hurry",
                       "&ldquo;" + B("Put") + " this packet underneath" + B(";") + " do you understand" + B("?") + " " + B("Hurry") + B(".") + "&rdquo;",
                       "Mama’s real words in Number the Stars: three short pieces, each with its own mark, inside one pair of quotation marks.",
                       "in august i read slowly but now i read with a pencil in my hand",
                       B("In") + " " + B("August") + " " + B("I") + " read slowly" + B(",") + " but now " + B("I") + " read with a pencil in my hand" + B("."),
                       "Capitals on In, August and I; a comma before but joins two complete thoughts; a period ends it."),
            "scholar": {"journal-q1": "… and name a book from the start and one from the end.", "journal-q2": "… and quote the moment.", "journal-q3": "… and name who should NOT read it, too."},
            "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
            "wgrd": {"catcher": {"title": "Reader then and now", "intro": "Look back.", "fields": [{"label": "Me as a reader in August", "hint": "", "rows": 2}, {"label": "Me as a reader now", "hint": "", "rows": 2}], "layout": "row", "end": {"label": "My proof", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
            "counters": {"journal-q1": 64, "journal-q2": 32, "journal-q3": 32}}
    L[3] = {"connector": "Today you build your portfolio page: your best piece of writing from the whole year, and why it’s your best. Choose the one that shows how you think, not just the longest one.",
            "dol": dol("marilla she demanded presently do you think that i shall ever have a bosom friend in avonlea",
                       "&ldquo;" + B("Marilla") + B(",") + "&rdquo; she demanded presently" + B(",") + " &ldquo;do you think that " + B("I") + " shall ever have a bosom friend in " + B("Avonlea") + B("?") + "&rdquo;",
                       "Anne’s real words (Ch. 8): the tag splits one sentence, so do stays lowercase; the question mark goes inside the last quotation mark.",
                       "my best piece is my comparison paragraph because it uses evidence from two books",
                       B("My") + " best piece is my comparison paragraph because it uses evidence from two books" + B("."),
                       "Capital M to start; no comma needed before because at the end; a period ends it."),
            "scholar": {"journal-q1": "… and copy one sentence you’re proudest of.", "journal-q2": "… and name the skill in one word.", "journal-q3": "… and say when you learned it."},
            "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
            "wgrd": {"catcher": {"title": "My portfolio piece", "intro": "Choose and explain.", "fields": [{"label": "The piece I chose", "hint": "", "rows": 1}, {"label": "What it shows I can do", "hint": "", "rows": 2}], "end": {"label": "Advice to me in Week 1", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
            "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 32}}
    L[4] = {"connector": "The last day. Today you say it out loud: what this year of reading did for you. Look back, look forward, and write the last sentence of your 4th grade ELA year.",
            "dol": dol("matthew said it was a girl my girl my girl that im proud of",
                       B("Matthew") + " said" + B(",") + " &ldquo;" + B("It") + " was a girl" + B("—") + "my girl" + B("—") + "my girl that " + B("I’m") + " proud of" + B(".") + "&rdquo;",
                       "Matthew’s real words (Anne of Green Gables, Ch. 36): dashes make the reader pause the way Matthew does.",
                       "next year i want to read a mystery and keep a reading journal",
                       B("Next") + " year " + B("I") + " want to read a mystery and keep a reading journal" + B("."),
                       "Capitals on Next and I; no comma needed (one subject doing two things); a period ends it."),
            "scholar": {"journal-q1": "… and name all five books.", "journal-q2": "… and quote them.", "journal-q3": "… and say how you’ll know you met it."},
            "flags": {"journal-q1": {"quote": False, "count": 3}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
            "wgrd": {"catcher": {"title": "Looking back, looking forward", "intro": "The whole year.", "fields": [{"label": "What this year did for me", "hint": "", "rows": 3}, {"label": "My reading goal for next year", "hint": "", "rows": 2}], "end": {"label": "My last sentence", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
            "counters": {"journal-q1": 80, "journal-q2": 32, "journal-q3": 32},
            "virtue": log("The pillar I’ll carry forward", "Which of the seven pillars do you want to carry into 5th grade? Tap one.", "Name a character from this year who showed it.", "I want to carry … like … did when …")}
    T = {1: {"welcome": "Hoo! It’s Opti. This is the last week of 4th grade ELA. Today’s question: what makes a strong comparison paragraph, and how can you make yours even stronger?",
             "read": "Read your paragraph as if someone else wrote it. Is the theme clear in the first sentence? Is there proof from both books? Change one sentence to make it sharper, then check capitals, usage, punctuation and spelling.",
             "morphology": "You know more roots than you think. Some you haven’t used yet. Try putting them to work: press means push, tain means hold, lev means lift. Find a word with one of them and use it in your own writing."},
         2: {"welcome": "Hoo, hello! It’s Opti. Today you write about yourself as a reader. Today’s question: who were you as a reader in August, and who are you now?",
             "read": "Think about the first book this year and the last. What can you do now that you couldn’t do then? Name the skill. Then prove it, the way you’d prove something about a character, with a real example.",
             "grammar": "Proofread like an editor. Read slowly, one sentence at a time. Check capitals, then usage, then punctuation, then spelling. Four quick passes catch more than one long one."},
         3: {"welcome": "Hello again, it’s Opti. Today you build your portfolio page. Today’s question: what is the most important thing you learned this year?",
             "read": "Look through your writing from the whole year. Choose the piece that shows how you think, not just the longest one. Then explain what makes it your best, and what you’d tell yourself back in Week 1.",
             "spelling": "One last spelling check. Read your piece out loud and touch each long word. Find the part you know. Check the ending. If a word looks strange, it probably is. Fix it now, and your best piece stays your best."},
         4: {"welcome": "Hoo! It’s Opti. The last day of 4th grade ELA. Today’s question: if you had one minute to tell someone what this year of reading did for you, what would you say first?",
             "read": "Look back at all five books and everything you wrote. Then look forward. Set one goal for next year, a real one. And write the last sentence of your year. Make it one you’d want to remember.",
             "grammar": "Your final sentence deserves your best care. Capital at the start. A complete thought. The right mark at the end. Read it out loud. If it sounds like you, it’s ready."}}

for d in L:
    ws, lab = WS[d]
    L[d].update({k: v for k, v in common.items() if k not in L[d]})
    L[d]["media"] = media(W, d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    if "virtue" in L[d]: L[d]["virtue"].update(kicker=K, icon=I, name="pillars")
    io.open('data/lesson-%d-%d.json' % (W, d), 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
for d in T:
    print('%d.%d' % (W, d), 'plain chars', sum(len(t) for t in T[d].values()), '/ 950')
