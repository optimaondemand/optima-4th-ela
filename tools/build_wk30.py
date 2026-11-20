#!/usr/bin/env python3
"""Writes data/lesson-27-1..4.json (week 30, Prince Caspian Ch. 13-15). Every moment checked in the text
(Planning docs/PrinceCaspian_CSL.pdf): Ch. 13 pp. 95-101, Ch. 14 pp. 102-110, Ch. 15 pp. 110-119.
Guide: Nell (original narrator). Q4: scripts written, not recorded.
No word game this week: the word-base activities are tap-and-choose, not fill-ins. Watch: the Seven Pillars Watch."""
import json, io

V = [["challenge", "An invitation to fight or compete that must be answered."],
     ["combat", "Fighting; single combat is one against one."],
     ["dictate", "To say words aloud for someone else to write down."],
     ["marshal", "An official who oversees a contest and keeps order."]]
WP = "Review of the unit’s bases: port, tract, struct, spect, ject, script/scribe, rupt, duct/duce, form, plus press = push, tain = hold, lev = lift."
GR = "Dialogue punctuation: quotation marks fence off the exact words; the comma or end mark goes inside the closing quotation mark; a tag like said Peter joins with a comma."
SP = "Cumulative review: a hard word is often two or three rules stacked up. Take it apart: se + par + ate + ion; forget + t + able."
K = "Seven Pillars Watch · after you read"; I = "🏛️"
PIL = ["Honesty", "Respect", "Courtesy", "Responsibility", "Courage", "Service", "Perseverance"]
def media(d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/nell/g4ela-30-%d-welcome" % d, "label": "Nell’s welcome"},
         "read": {"kind": "audio", "path": "guide/nell/g4ela-30-%d-read" % d, "label": "Nell · before you read" if d < 4 else "Nell · looking back"},
         ws: {"kind": "video", "path": "guide/nell/g4ela-30-%d-%s" % (d, ws), "label": "Nell · " + wslabel}}
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
 "connector": "Peter, Edmund and Trumpkin found Caspian just in time. Now the High King is in command, and there is a war still to settle. Today, ask what this story still has to answer, and watch the way Peter chooses to answer it. The way someone settles a fight shows what they value.",
 "writingFocus": "Resolution",
 "dol": dol("peter told caspian that he was to wounded to fight miraz in single combat",
            B("Peter") + " told " + B("Caspian") + " that he was " + B("too") + " wounded to fight " + B("Miraz") + " in single combat" + B("."),
            "Capitals on Peter, Caspian and Miraz; too (meaning more than enough), not to; a period ends it.",
            "edmund carried the challenge and glenstorm and wimbleweather walked beside him",
            B("Edmund") + " carried the challenge" + B(",") + " and " + B("Glenstorm") + " and " + B("Wimbleweather") + " walked beside him" + B("."),
            "Capitals on the three names; a comma before the and that starts a new complete thought; a period ends it."),
 "scholar": {"journal-q1": "… and quote one line from the challenge letter.",
             "journal-q2": "… and quote one thing a lord says to Miraz.",
             "journal-q3": "… and quote Reepicheep."},
 "flags": {"journal-q1": {"quote": True, "count": 1}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": True, "count": 3}},
 "copia": {"seed": "Peter <b data-verb>sent</b> Miraz a challenge.",
           "eg": ["To save his army, Peter sent Miraz a challenge.", "Peter <i>dared</i> Miraz to single combat.",
                  "Peter sent Miraz a challenge, written by Doctor Cornelius in the old formal words."]},
 "notes": {"wgrd": "Explain how resolution reveals theme: name what the story still has to settle, notice the way the characters choose to settle it, and ask what that way values.",
           "vocab": V, "wordParts": WP, "grammar": GR, "spelling": SP},
 "wgrd": {"catcher": {"title": "What still has to be settled", "intro": "As you read Ch. 13, catch the question and the way.",
                      "fields": [{"label": "The question this story still has to answer", "hint": "", "rows": 2},
                                 {"label": "The way Peter chooses, and the way he turns down", "hint": "", "rows": 2}],
                      "end": {"label": "He would rather … than …", "hint": ""}}, "useAt": ["journal-q1"]},
 "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 40},
 "virtue": pv("Which pillar is it?",
   "The OAO Seven Pillars are honesty, respect, courtesy, responsibility, courage, service and perseverance. In Chapter 13, Peter takes command. Read each moment. Tap the pillar it shows best.",
   [{"t": "Caspian is wounded, so Peter will not let him fight. Peter sends Miraz a challenge to single combat with himself, so that two armies won’t have to fight.", "ok": ["Courage", "Responsibility", "Service"], "why": "He puts himself in danger to protect everyone else.", "hint": "Who is in danger now, and who is safer?"},
    {"t": "The Bear says the bears always had the right to supply one marshal. Peter says, “It is your right. And you shall be one of the marshals.”", "ok": ["Respect"], "why": "Peter honours an old right, even though Trumpkin warns him the Bear will suck his paws.", "hint": "What does Peter honour?"},
    {"t": "Reepicheep asks to be a marshal. Peter gravely tells him it would not be quite fair to Miraz, since some humans are afraid of mice.", "ok": ["Courtesy", "Respect"], "why": "He says no without laughing at the Mouse.", "hint": "How does Peter say no?"},
    {"t": "Edmund asks if Peter can beat Miraz. Peter says, “That’s what I’m fighting him to find out.”", "ok": ["Honesty", "Courage"], "why": "He doesn’t pretend to be sure, and he goes anyway.", "hint": "Does Peter promise to win?"}]),
}
L[2] = {
 "connector": "Today the fight is settled. But the part that carries the theme isn’t who wins. It’s how the winning happens. Watch for one moment in the duel that could easily have gone the other way, and ask what that small choice proves.",
 "writingFocus": "Resolution",
 "dol": dol("trumpkin danced with delight and shouted the high king up old narnia",
            B("Trumpkin") + " danced with delight and shouted" + B(",") + " &ldquo;" + B("The High King") + B("!") + " " + B("Up") + B(",") + " " + B("Old Narnia") + B("!") + "&rdquo;",
            "Capital T on Trumpkin; no comma after delight (danced and shouted share one subject); a comma after shouted before the quote; capitals and exclamation points inside the quotation marks.",
            "edmund bit his lips till the blood came as the sword flashed down on peter",
            B("Edmund") + " bit his lips till the blood came" + B(",") + " as the sword flashed down on " + B("Peter") + B("."),
            "Lewis’s own sentence. Capitals on Edmund and Peter; a comma before as, which adds what was happening at that moment; a period ends it."),
 "scholar": {"journal-q1": "… and quote what Edmund thinks.",
             "journal-q2": "… and give one detail from each story.",
             "journal-q3": "… and quote what Glozelle shouts."},
 "flags": {"journal-q1": {"quote": True, "count": 1}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": True, "count": 1}},
 "notes": {"wgrd": "Watch how the fight is settled, not just who wins. Find the moment it could have gone otherwise, and name the idea it proves.",
           "vocab": V + [["hauberk", "A coat of chain-mail armor."], ["treachery", "Betraying someone who trusted you."]], "wordParts": WP,
           "grammar": GR + " Lewis lets a speaker shout in fragments when the action is fast.", "spelling": SP},
 "wgrd": {"catcher": {"title": "How it was settled", "intro": "As you read Ch. 14, catch the how.",
                      "fields": [{"label": "The steps of the duel", "hint": "", "rows": 3}, {"label": "The moment it could have gone otherwise", "hint": "", "rows": 2}],
                      "end": {"label": "Because it was settled this way, this book believes that …", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 40, "journal-q2": 40, "journal-q3": 32},
 "virtue": pv("Which pillar is it?", "In Chapter 14 the duel is fought and Narnia wakes. Read each moment. Tap the pillar it shows best.",
   [{"t": "During a rest, Peter says quietly, “Give my love to — to everyone at home, Ed, if he gets me.” Then he goes back into the lists.", "ok": ["Courage"], "why": "He knows he might die and goes back anyway.", "hint": "What does Peter think might happen?"},
    {"t": "Miraz trips on a tussock and falls face down. Peter steps back and waits for him to rise.", "ok": ["Courtesy", "Respect"], "why": "He won’t strike an enemy who has fallen by accident.", "hint": "What could Peter have done?"},
    {"t": "Peter’s wrist is hurt. Edmund and Doctor Cornelius bind it up tight so he can keep fighting.", "ok": ["Service"], "why": "They help him keep going.", "hint": "What do they do for Peter?"},
    {"t": "Aslan finds a little old woman dying in her bed. She opens her eyes and says, “Oh, Aslan! I knew it was true. I’ve been waiting for this all my life.”", "ok": ["Perseverance"], "why": "She kept believing her whole life, when no one around her did.", "hint": "How long has she waited?"}]),
}
L[3] = {
 "connector": "The last chapter. A story does its final work here: it hands out endings, and the endings show you who each character has become. Read with a then-and-now question in your head. Who is different from the person you met on the first page?",
 "writingFocus": "Resolution",
 "dol": dol("caspian kissed the lions paw and said i dont think i do sir",
            B("Caspian") + " kissed the " + B("Lion’s") + " paw and said" + B(",") + " &ldquo;" + B("I don’t") + " think " + B("I") + " do" + B(",") + " " + B("Sir") + B(".") + "&rdquo;",
            "Capitals on Caspian, Lion’s, I and Sir; apostrophes in Lion’s and don’t; a comma before the quote and before Sir; the period goes inside the quotation marks.",
            "the mice said they would cut off their own tails if their chief must go without his",
            B("The") + " " + B("Mice") + " said they would cut off their own tails if their " + B("Chief") + " must go without his" + B("."),
            "Lewis capitalizes the Mice and their Chief like names of a people and a title; no comma before if at the end; a period ends it."),
 "scholar": {"journal-q1": "… and quote Aslan’s answer.",
             "journal-q2": "… and quote what Peepiceek says.",
             "journal-q3": "… and quote what Peter says to Lucy."},
 "flags": {"journal-q1": {"quote": True, "count": 1}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "hints": {"s4w30cf1": hint("separate ends in silent e. What happens before -ion?", "Drop the e: separate + ion = separation."),
           "s4w30cf2": hint("celebrate ends in silent e. What happens before -ion?", "Drop the e: celebrate + ion = celebration."),
           "s4w30cf3": hint("restore ends in silent e. What happens before -ation?", "Drop the e: restore + ation = restoration."),
           "s4w30cf4": hint("for·GET has its beat on the last syllable. Double or not?", "Double the t: forget + t + able = forgettable.")},
 "notes": {"wgrd": "Make a then-and-now list for two or three characters, write what each change cost, and mark the line that shows it.",
           "vocab": V + [["sufficient", "Enough for what is needed."], ["coronation", "The ceremony of crowning a king or queen."], ["lineage", "The line of people you come from."]], "wordParts": WP,
           "grammar": GR + " Moving the tag changes the rhythm of a line.", "spelling": SP},
 "wgrd": {"catcher": {"title": "Then and now", "intro": "As you read Ch. 15, compare.",
                      "fields": [{"label": "Who they were at the start of the book", "hint": "Caspian: … Peter: …", "rows": 3},
                                 {"label": "Who they are now, and what it cost", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "The line that shows the biggest change", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 40, "journal-q2": 40, "journal-q3": 40},
 "virtue": pv("Which pillar is it?", "In Chapter 15 the story hands out its endings. Read each moment. Tap the pillar it shows best.",
   [{"t": "Aslan asks Caspian if he feels himself sufficient to be King. Caspian says, “I — I don’t think I do, Sir. I’m only a kid.”", "ok": ["Honesty"], "why": "He tells the truth about himself, even about a crown.", "hint": "What could Caspian have said instead?"},
    {"t": "The Mice draw their swords, ready to cut off their own tails so their Chief won’t be the only one without one.", "ok": ["Service", "Respect"], "why": "They give up something of their own for their leader.", "hint": "Whose tail is missing?"},
    {"t": "Aslan offers the Telmarines a door to a new world. A burly soldier pushes forward first: “Well, I’ll take the offer.”", "ok": ["Courage"], "why": "He goes first into the unknown.", "hint": "Who goes first?"},
    {"t": "Peter learns he will never come back to Narnia. Lucy asks if he can bear it. He says, “Well, I think I can.”", "ok": ["Perseverance", "Courage"], "why": "He accepts a hard ending without complaining.", "hint": "How does Peter take the news?"}]),
}
L[4] = {
 "connector": "You’ve finished Prince Caspian. All week you watched the story settle its big question. Today, say what that settling means. Not what the book is about, but what it believes, and prove it from the last three chapters.",
 "writingFocus": "Resolution",
 "dol": dol("sire said reepicheep my life is ever at your command but my honour is my own",
            "&ldquo;" + B("Sire") + B(",") + "&rdquo; said " + B("Reepicheep") + B(".") + " &ldquo;" + B("My") + " life is ever at your command" + B(",") + " but my honour is my own" + B(".") + "&rdquo;",
            "Reepicheep’s real words (Chapter 13). Each part of his speech gets quotation marks; capitals on Sire, Reepicheep and My; a comma before but; periods inside the quotation marks.",
            "well said peter we have had a time",
            "&ldquo;" + B("Well") + B("!") + "&rdquo; said " + B("Peter") + B(".") + " &ldquo;" + B("We") + " have had a time" + B(".") + "&rdquo;",
            "The book’s own last lines. Capitals on Well, Peter and We; the exclamation point goes inside the quotation mark; periods end each sentence."),
 "scholar": {"journal-q1": "… and quote Edmund’s thought about Peter.",
             "journal-q2": "… and say what Caspian learns about his own people.",
             "journal-q3": "… and use one character from early in the book."},
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "notes": {"wgrd": "Say what the book believes, not what it is about, and anchor it in the ending.",
           "vocab": V + [["sufficient", "Enough for what is needed."], ["coronation", "The ceremony of crowning a king or queen."], ["treachery", "Betraying someone who trusted you."]], "wordParts": WP,
           "grammar": GR + " Editing day.", "spelling": SP},
 "wgrd": {"catcher": {"title": "What this book believes", "intro": "Look back at Ch. 13–15, and the whole book.",
                      "fields": [{"label": "What got settled", "hint": "", "rows": 2}, {"label": "What did not", "hint": "", "rows": 2},
                                 {"label": "Who had to let go of something", "hint": "", "rows": 2}],
                      "end": {"label": "Prince Caspian believes that …", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 48, "journal-q2": 40, "journal-q3": 48},
 "plate": {"src": "plates/pc-ch15.png", "alt": "A glade at sunset where two wooden stakes and a third across the top make an empty doorway, with a great golden lion beside it.",
           "credit": "From Chapter 15, the door in the air."},
 "virtue": {"kind": "log", "title": "This book’s strongest pillar", "intro": "Think about all of Prince Caspian. Which pillar did the characters show most? Tap one.",
            "options": [{"t": p} for p in PIL],
            "line": "Name one moment that proves it.", "placeholder": "The strongest pillar was … because in Chapter … "},
}

T = {
 1: {"welcome": "Hello, it’s Nell. Peter has found Caspian, and the High King is in command. Today’s question: when there is more than one way to settle a fight, what does the way you choose say about you?",
     "read": "Listen to the challenge letter. It’s full of old, formal words, and every one of them is chosen on purpose. Then watch Peter choose his marshals, and say no to one volunteer. Notice how he says no.",
     "morphology": "This is a review of every base in the unit. Port, carry. Tract, pull. Struct, build. Spect, look. Ject, throw. Script, write. Rupt, break. Duct, lead. Form, shape. You know a lot of Latin now. Take a long word apart, and it will tell you what it means."},
 2: {"welcome": "Hello again, it’s Nell. Today the duel is fought. Today’s question: what matters more, who wins, or how?",
     "read": "Read the duel slowly, through Edmund’s eyes. Find the moment when Peter could have done the easy thing, and didn’t. Then follow Aslan, Lucy and Susan through the countryside, where a whole country is waking up.",
     "grammar": "Dialogue. Quotation marks go around the exact words. The comma or the end mark goes inside the closing quotation mark. Then the tag: said Trumpkin, cried Edmund. A fast shout can be just a fragment. The marks around it still follow the rules."},
 3: {"welcome": "Hello, it’s Nell. This is the last chapter. Today’s question: who has changed the most since the first page, and what did the change cost them?",
     "read": "Make a then-and-now list as you read. Caspian, Peter, Susan, Reepicheep. Who were they at the start, and who are they now? Slow down for the goodbyes, especially what Peter tells Lucy about coming back.",
     "spelling": "A hard word is usually two or three easy rules stacked up. Hopeful: hope, plus ful, and the e stays because ful starts with a consonant. Take the word apart, use the rules one at a time, and put it back together."},
 4: {"welcome": "Hello, it’s Nell. You’ve finished the book. I always sit for a minute with a book I’ve just finished. Today’s question: what does Prince Caspian believe, and what in the ending proves it?",
     "read": "Say what got settled, what didn’t, and who had to let go of something. Then finish the sentence: this book believes that. Not what it’s about. What it believes. Turn to the page in the ending that proves it.",
     "grammar": "Editing day, the last one for this book. Check every line of dialogue. Are the exact words inside quotation marks? Is the comma or end mark inside too? Does the tag join with a comma? Fix each one and say why."},
}
WS = {1: ("morphology", "every base in the unit"), 2: ("grammar", "dialogue marks"), 3: ("spelling", "stack the rules"), 4: ("grammar", "check every line of talk")}

for d in L:
    ws, lab = WS[d]
    L[d]["media"] = media(d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    L[d]["virtue"].update(kicker=K, icon=I, name="pillars")
    io.open('data/lesson-30-%d.json' % d, 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
for d in T:
    print('30.%d' % d, {k: len(t) for k, t in T[d].items()}, 'plain chars', sum(len(t) for t in T[d].values()), '/ 950')
