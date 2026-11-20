#!/usr/bin/env python3
"""Writes data/lesson-27-1..4.json (week 29, Prince Caspian Ch. 10-12). Every moment checked in the text
(Planning docs/PrinceCaspian_CSL.pdf): Ch. 10 pp. 69-77, Ch. 11 pp. 78-86, Ch. 12 pp. 87-94.
Guide: Nell (original narrator). Q4: scripts written, not recorded.
No word game this week: the word-base activities are tap-and-choose, not fill-ins. Watch: the Seven Pillars Watch."""
import json, io

V = [["precipice", "A very steep cliff or drop."],
     ["bivouac", "A rough camp without proper shelter."],
     ["luminous", "Giving off light; glowing."],
     ["sentient", "Able to feel and sense things; aware."]]
WP = "Latin bases: rupt = break, duct and duce = lead, form = shape: interrupt, conduct, introduce, transform."
GR = "Commas in dates and places: a comma between the day and the year (June 12, 1941), between a town and its county or country (Dover, Kent), and another after them if the sentence goes on."
SP = "Greek and Latin parts you know: port (carry), spect (look), script and scribe (write), rupt (break), tele (far). Spell the part the same way every time: inter + rupt + ion."
K = "Seven Pillars Watch · after you read"; I = "🏛️"
PIL = ["Honesty", "Respect", "Courtesy", "Responsibility", "Courage", "Service", "Perseverance"]
def media(d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/nell/g4ela-29-%d-welcome" % d, "label": "Nell’s welcome"},
         "read": {"kind": "audio", "path": "guide/nell/g4ela-29-%d-read" % d, "label": "Nell · before you read" if d < 4 else "Nell · looking back"},
         ws: {"kind": "video", "path": "guide/nell/g4ela-29-%d-%s" % (d, ws), "label": "Nell · " + wslabel}}
    for off in ("guide1", "guide2", "guide3", "rwm", "copia"): m[off] = {"kind": ""}
    return m
def hint(h1, why): return {"h1": h1, "why": why}
def dol(raw, fixed, why, raw2, fixed2, why2):
    return {"a": {"raw": raw, "fixed": fixed, "why": why}, "b": {"raw": raw2, "fixed": fixed2, "why": why2}}
B = lambda s: "<strong>" + s + "</strong>"
MADEUP_NOTE = " Narnia has no calendar, so practice dates are made up."
def pv(title, intro, items, line=None, ph=None):
    v = {"kind": "pillars", "title": title, "intro": intro, "pillars": PIL, "items": items}
    if line: v.update(line=line, placeholder=ph or "")
    return v

L = {}
L[1] = {
 "connector": "Last week ended with Lucy coming last, crying. Tonight she wakes alone and hears the voice she likes best in the world. This week, watch the choices that keep coming back. When one choice echoes another, the story is pointing at its big idea.",
 "writingFocus": "Theme",
 "dol": dol("at night lucy crept out of the camp because she herd aslan calling her name in the forrest",
            B("At") + " night" + B(",") + " " + B("Lucy") + " crept out of the camp because she " + B("heard") + " " + B("Aslan") + " calling her name in the " + B("forest") + B("."),
            "Capitals on At, Lucy and Aslan; a comma after the opening phrase At night; heard, not herd; forest has one r; a period ends it.",
            "edmund woke first but he could not see aslan in the moonlight",
            B("Edmund") + " woke first" + B(",") + " but he could not see " + B("Aslan") + " in the moonlight" + B("."),
            "Capitals on Edmund and Aslan; a comma before but joins two complete thoughts; a period ends it."),
 "scholar": {"journal-q1": "… and quote the words Lewis uses for the voice.",
             "journal-q2": "… and say what else could grow besides size.",
             "journal-q3": "… and name the earlier time Lucy saw what others couldn’t."},
 "flags": {"journal-q1": {"quote": True, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "copia": {"seed": "Lucy <b data-verb>woke</b> the others.",
           "eg": ["Though she knew they wouldn’t believe her, Lucy woke the others.", "Lucy <i>shook</i> the others awake.",
                  "Lucy woke the others, one by one, starting with Edmund."]},
 "notes": {"wgrd": "Notice theme through repeated choices: mark each choice in a few words, hunt for an earlier choice it echoes, and say the two together.",
           "vocab": V, "wordParts": WP, "grammar": GR, "spelling": SP},
 "wgrd": {"catcher": {"title": "Echoes", "intro": "As you read Ch. 10, catch the choices.",
                      "fields": [{"label": "A choice someone makes now", "hint": "", "rows": 2}, {"label": "An earlier choice it echoes", "hint": "Ch. 9…", "rows": 2}],
                      "layout": "row", "end": {"label": "Earlier, someone had to … and now someone has to …", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 32},
 "virtue": pv("Which pillar is it?",
   "The OAO Seven Pillars are honesty, respect, courtesy, responsibility, courage, service and perseverance. In Chapter 10, Lucy finds Aslan and has to go back for the others. Read each moment. Tap the pillar it shows best.",
   [{"t": "Lucy starts to complain that the others wouldn’t believe her. Then she says, “I’m sorry. I didn’t mean to start slanging the others.”", "ok": ["Honesty", "Respect"], "why": "She stops blaming others and owns what she said.", "hint": "What does Lucy stop doing?"},
    {"t": "Aslan tells Lucy she must wake the others and follow him, even if they don’t believe her. She hides her face in his mane, then sits up: “I’m sorry, Aslan. I’m ready now.”", "ok": ["Courage"], "why": "She is afraid of being laughed at and goes anyway.", "hint": "What is Lucy afraid of?"},
    {"t": "Lucy has to tell her story to each of them. Each time she says it, it sounds less convincing. She keeps saying it.", "ok": ["Perseverance"], "why": "She keeps going when it gets harder each time.", "hint": "What happens each time she says it?"}]),
}
L[2] = {
 "connector": "Last time, Lucy woke the others, and they couldn’t see what she saw. Today they follow her through the dark, one by one, and some of them begin to see. Line up the choices from both chapters. What one word fits all of them?",
 "writingFocus": "Theme",
 "dol": dol("oh aslan said king peter im so glad",
            "&ldquo;" + B("Oh") + B(",") + " " + B("Aslan") + B(",") + "&rdquo; said " + B("King Peter") + B(",") + " &ldquo;" + B("I’m") + " so glad" + B(".") + "&rdquo;",
            "Peter’s real words in Chapter 11. Capitals on Oh, Aslan, King Peter and I’m; quotation marks around each part he says; commas separate his words from said King Peter; the period goes inside the quotation mark.",
            "lucy said susan in a very small voice",
            "&ldquo;" + B("Lucy") + B(",") + "&rdquo; said " + B("Susan") + " in a very small voice" + B("."),
            "Lewis’s own sentence. Capitals on Lucy and Susan; the comma goes inside the quotation mark after Lucy; a period ends it."),
 "scholar": {"journal-q1": "… and quote what else Susan says to Lucy.",
             "journal-q2": "… and describe one tree-person Lewis shows you.",
             "journal-q3": "… and quote what Aslan says back to Peter."},
 "flags": {"journal-q1": {"quote": True, "count": 1}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "notes": {"wgrd": "Put the echoes side by side: list each choice from Ch. 10 and 11, find one word that fits them all, and test it on every line.",
           "vocab": V + [["revelry", "Wild, noisy celebration."], ["romp", "Lively, rough play."]], "wordParts": WP,
           "grammar": GR + MADEUP_NOTE, "spelling": SP},
 "wgrd": {"catcher": {"title": "One word for all of them", "intro": "As you read Ch. 11, list the choices.",
                      "fields": [{"label": "Choices in Ch. 10 and 11", "hint": "Lucy follows… Susan admits…", "rows": 4}],
                      "end": {"label": "The one word that fits them all", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 32},
 "virtue": pv("Which pillar is it?", "In Chapter 11 the others begin to see Aslan. Read each moment. Tap the pillar it shows best.",
   [{"t": "Susan says to Lucy in a very small voice, “I see him now. I’m sorry.” Then: “But I’ve been far worse than you know.”", "ok": ["Honesty"], "why": "She admits more than anyone asked her to.", "hint": "What does Susan admit?"},
    {"t": "Peter drops on one knee before Aslan: “I’m so glad. And I’m so sorry. I’ve been leading them wrong ever since we started.”", "ok": ["Honesty", "Courage"], "why": "The High King owns his mistake out loud.", "hint": "What is hard about a king saying this?"},
    {"t": "Aslan welcomes Edmund with two words: “Well done.” Edmund was the one who voted to believe Lucy at the gorge.", "ok": ["Courage", "Respect"], "why": "He stood by his sister when the vote went against her.", "hint": "What did Edmund do in Chapter 9?"},
    {"t": "Lucy follows Aslan through the dark, keeping her eyes on him, while the others stumble after her and can’t see him yet.", "ok": ["Perseverance", "Courage"], "why": "She keeps following when she is the only one who can see.", "hint": "Who can see him?"}]),
}
L[3] = {
 "connector": "While the children were finding Aslan, Caspian was losing hope in the dark of Aslan’s How. Tonight Nikabrik brings two strange guests to the council. You have a pattern now, and a word for it. Today, turn it into a sentence about what the book believes.",
 "writingFocus": "Theme",
 "dol": dol("nikabrik wanted caspian dead but trufflehunter the badger said we dont change we hold on",
            B("Nikabrik") + " wanted " + B("Caspian") + " dead" + B(",") + " but " + B("Trufflehunter") + " the badger said" + B(",") + " &ldquo;We " + B("don’t") + " change" + B(".") + " We hold on" + B(".") + "&rdquo;",
            "Capitals on the three names; a comma before but; a comma before the quotation; don’t needs an apostrophe; Trufflehunter’s words from Chapter 5 are two short sentences inside the quotation marks.",
            "caspian said i am sorry for nikabrik",
            B("Caspian") + " said" + B(",") + " &ldquo;" + B("I") + " am sorry for " + B("Nikabrik") + B(".") + "&rdquo;",
            "Capitals on Caspian, I and Nikabrik; a comma before the quotation; the period goes inside the closing quotation mark."),
 "scholar": {"journal-q1": "… and quote Nikabrik’s reason in his own words.",
             "journal-q2": "… and say what Peter could have done instead.",
             "journal-q3": "… and name one character who suffered and did not turn bitter."},
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "hints": {"s4w29cf1": hint("A porter carries bags. What does port mean?", "port = carry."),
           "s4w29cf2": hint("Spectacles help you do what?", "spect = look."),
           "s4w29cf3": hint("A scribe’s job is to …?", "script = write."),
           "s4w29cf4": hint("When a volcano erupts, the ground …?", "rupt = break.")},
 "notes": {"wgrd": "Turn the pattern into a theme sentence: what repeats, what happens to people who choose each way, then cut the names so it is true about people.",
           "vocab": V + [["sorcery", "Dark magic."], ["treason", "Betraying your own king or country."]], "wordParts": WP,
           "grammar": GR + MADEUP_NOTE, "spelling": SP},
 "wgrd": {"catcher": {"title": "Two roads", "intro": "As you read Ch. 12, watch both roads.",
                      "fields": [{"label": "Nikabrik’s choice, and where it leads", "hint": "", "rows": 3}, {"label": "Peter’s and Caspian’s choices, and where they lead", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "My theme sentence: when people have to choose whom to trust, …", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 40, "journal-q2": 32, "journal-q3": 40},
 "virtue": pv("Which pillar is it?", "In Chapter 12, Caspian’s council faces a terrible offer. Read each moment. Tap the pillar it shows best.",
   [{"t": "Nikabrik says the Dwarfs are always sent on the dangerous raids and go short when the rations fail. The Badger answers, “Lies! All lies!”", "ok": ["Honesty", "Courage"], "why": "He says out loud that something is false, to an angry Dwarf with a weapon.", "hint": "Is it safe to say this?"},
    {"t": "Peter meets Caspian for the first time and says, “I haven’t come to take your place, you know, but to put you into it.”", "ok": ["Respect", "Service"], "why": "The High King uses his power to help Caspian, not to replace him.", "hint": "Who could Peter have made king?"},
    {"t": "Peter thanks Trufflehunter for never doubting them. The Badger says, “No credit to me, your Majesty. I’m a beast and we don’t change.”", "ok": ["Perseverance"], "why": "He held on to the truth for a very long time.", "hint": "What does holding on mean here?"},
    {"t": "Caspian says, “I am sorry for Nikabrik, though he hated me from the first moment he saw me.”", "ok": ["Respect", "Courtesy"], "why": "He is fair even to someone who wanted him dead.", "hint": "How does Caspian speak of his enemy?"}]),
}
L[4] = {
 "connector": "Three chapters, and one question asked three times: whom do you trust, and what does trusting cost? Today you test your theme sentence on a character you haven’t used yet. If it holds, bring the page that proves it. If it doesn’t, make it wider.",
 "writingFocus": "Theme",
 "dol": dol("caspian spoke sadly of nikabrik and said he had gone sour inside from long suffering and hateing",
            B("Caspian") + " spoke sadly of " + B("Nikabrik") + " and said" + B(",") + " &ldquo;" + B("He") + " had gone sour inside from long suffering and " + B("hating") + B(".") + "&rdquo;",
            "Capitals on Caspian, Nikabrik and He; a comma before the quotation; hating drops the silent e before -ing; the period goes inside the closing quotation mark.",
            "wraiths and wreckage gasped trumpkin in the ghost of a voice",
            "&ldquo;" + B("Wraiths") + " and wreckage" + B("!") + "&rdquo; gasped " + B("Trumpkin") + " in the ghost of a voice" + B("."),
            "Lewis’s own sentence. Capitals on Wraiths and Trumpkin; the exclamation point goes inside the quotation marks; a period ends the sentence."),
 "scholar": {"journal-q1": "… and quote each character once.",
             "journal-q2": "… and say which response Lewis seems to admire most.",
             "journal-q3": "… and use two different chapters."},
 "flags": {"journal-q1": {"quote": True, "count": 3}, "journal-q2": {"quote": False, "count": 3}, "journal-q3": {"quote": False, "count": 2}},
 "notes": {"wgrd": "Test your theme sentence on someone new from Ch. 10–12. Keep it if it fits; widen it if it doesn’t.",
           "vocab": V + [["revelry", "Wild, noisy celebration."], ["sorcery", "Dark magic."], ["treason", "Betraying your own king or country."]], "wordParts": WP,
           "grammar": GR + MADEUP_NOTE + " Editing day.", "spelling": SP},
 "wgrd": {"catcher": {"title": "Test the theme", "intro": "Look back at Ch. 10–12.",
                      "fields": [{"label": "My theme sentence", "hint": "", "rows": 2},
                                 {"label": "A new character to test it on, and their choice", "hint": "", "rows": 2}],
                      "end": {"label": "Does it hold? Keep it or widen it", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 48, "journal-q2": 40, "journal-q3": 40},
 "plate": {"src": "plates/pc-ch11.png", "alt": "A great golden lion on a hill at dawn, head raised in a roar, while trees bend and move like dancers.",
           "credit": "From Chapter 11, the night the trees woke."},
 "virtue": {"kind": "log", "title": "This week’s strongest pillar", "intro": "Think about Chapters 10–12. Which pillar did the characters show most this week? Tap one.",
            "options": [{"t": p} for p in PIL],
            "line": "Name one moment that proves it.", "placeholder": "The strongest pillar was … because in Chapter … "},
}

T = {
 1: {"welcome": "Hello, it’s Nell. Last time, Lucy lost the vote and came last, crying. Tonight she wakes up alone, and someone is calling her name. Today’s question: what does it cost to trust what only you can see?",
     "read": "Watch for echoes. Has anyone in this book already had to decide whether to believe Lucy? Mark each choice in a few words as you read. And listen closely to what Aslan tells her about what would have happened.",
     "morphology": "Three more Latin bases. Rupt means break, so to interrupt is to break in. Duct and duce mean lead, so an aqueduct leads water across a valley. Form means shape, so a formation is a shape made by many people. Find the base. It carries the meaning."},
 2: {"welcome": "Hello again, it’s Nell. The others are following Lucy through the dark, and they still can’t see what she sees. Today’s question: what do all of this week’s choices have in common?",
     "read": "Line up the choices: Lucy following, Susan admitting, Peter kneeling. Find one word that fits all of them. Then, when Aslan roars, slow down. Watch what the trees do, and who they turn into.",
     "grammar": "Commas in dates and places. A date: June 12, 1941. The comma sits between the day and the year. A place: Dover, Kent. The comma sits between the town and the bigger place it belongs to. If the sentence keeps going, add one more comma after."},
 3: {"welcome": "Hello, it’s Nell. While the children found Aslan, Caspian’s side was losing hope in the dark. Today’s question: when people have to choose whom to trust, what does this book seem to believe?",
     "read": "This is a dark chapter. Watch Nikabrik’s road and Peter’s road side by side. Where does each one lead? Then, at the end, listen to what Caspian says about Nikabrik. It tells you a lot about Caspian.",
     "spelling": "Long words are built from parts you already know. Find the part, and spell it the same way every time. Portable: port, able. Spectator: spect, a, tor. The part never changes its spelling, even when the word around it does."},
 4: {"welcome": "Hello, it’s Nell. Three chapters, one question asked three times: whom do you trust, and what does it cost? Today’s question: does your theme sentence hold for everyone?",
     "read": "Say your theme sentence out loud. Then try it on someone you haven’t used yet: Susan, Trumpkin, Nikabrik, Caspian. If it fits, find the page. If it doesn’t, change the sentence. Never leave the character out to protect it.",
     "grammar": "Editing day. Read each date and place. Is there a comma between the day and the year? Between the town and the bigger place? And if the sentence keeps going, is there a comma after? Fix each one and say what it separates."},
}
WS = {1: ("morphology", "break, lead and shape"), 2: ("grammar", "commas in dates and places"), 3: ("spelling", "spell the part you know"), 4: ("grammar", "check every date and place")}

for d in L:
    ws, lab = WS[d]
    L[d]["media"] = media(d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    L[d]["virtue"].update(kicker=K, icon=I, name="pillars")
    io.open('data/lesson-29-%d.json' % d, 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
for d in T:
    print('29.%d' % d, {k: len(t) for k, t in T[d].items()}, 'plain chars', sum(len(t) for t in T[d].values()), '/ 950')
