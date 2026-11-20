#!/usr/bin/env python3
"""Writes data/lesson-27-1..4.json (week 28, Prince Caspian Ch. 7-9). Every moment checked in the text
(Planning docs/PrinceCaspian_CSL.pdf): Ch. 7 pp. 44-51, Ch. 8 pp. 52-59, Ch. 9 pp. 60-68.
Guide: Nell (original narrator). Q4: scripts written, not recorded.
No word game this week: the word-base activities are tap-and-choose, not fill-ins. Watch: the Seven Pillars Watch."""
import json, io

V = [["council", "A group gathered to talk and decide what to do."],
     ["seneschal", "The chief steward who runs a lord’s household."],
     ["entrenchments", "Ditches and banks dug for defense."],
     ["consorts", "Companions, especially of a king or queen."]]
WP = "Latin bases: spect = look, ject = throw, script and scribe = write: inspect, reject, manuscript, spectacles."
GR = "A complex sentence has a main clause and a dependent clause that starts with a word like because, although, when, if or since. If the dependent clause comes first, put a comma after it."
SP = "Schwa is the lazy uh sound in an unstressed syllable. Your ear can’t spell it, so find a related word where that vowel is stressed: definite from finite, composition from compose."
K = "Seven Pillars Watch · after you read"; I = "🏛️"
PIL = ["Honesty", "Respect", "Courtesy", "Responsibility", "Courage", "Service", "Perseverance"]
def media(d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/nell/g4ela-28-%d-welcome" % d, "label": "Nell’s welcome"},
         "read": {"kind": "audio", "path": "guide/nell/g4ela-28-%d-read" % d, "label": "Nell · before you read" if d < 4 else "Nell · looking back"},
         ws: {"kind": "video", "path": "guide/nell/g4ela-28-%d-%s" % (d, ws), "label": "Nell · " + wslabel}}
    for off in ("guide1", "guide2", "guide3", "rwm", "copia"): m[off] = {"kind": ""}
    return m
def hint(h1, why): return {"h1": h1, "why": why}
def dol(raw, fixed, why, raw2, fixed2, why2):
    return {"a": {"raw": raw, "fixed": fixed, "why": why}, "b": {"raw": raw2, "fixed": fixed2, "why": why2}}
B = lambda s: "<strong>" + s + "</strong>"
def pv(title, intro, items, line=None, ph=None):
    v = {"kind": "pillars", "title": title, "intro": intro, "pillars": PIL, "items": items}
    if line: v.update(line=line, placeholder=ph or "")
    return v

L = {}
L[1] = {
 "connector": "Caspian has his army now: bears, Mice, Centaurs, Dwarfs and one Giant. Tonight they hold a council, and every group wants something different. Watch the arguing, then watch for the moment someone has to choose. A good leader listens first and decides second.",
 "writingFocus": "Leadership",
 "dol": dol("because nikabrik distrusted doctor cornelius he reached for his sword although caspian called the doctor his greatest friend",
            B("Because") + " " + B("Nikabrik") + " distrusted " + B("Doctor Cornelius") + B(",") + " he reached for his sword although " + B("Caspian") + " called the " + B("Doctor") + " his greatest friend" + B("."),
            "Capitals start the sentence and name the characters; a comma after the opening because clause; no comma before although at the end; a period ends it.",
            "when the great night came caspians heart swelled because he saw how many had come",
            B("When") + " the great night came" + B(",") + " " + B("Caspian’s") + " heart swelled because he saw how many had come" + B("."),
            "Capital W starts it; a comma after the opening when clause; capital C and an apostrophe in Caspian’s; no comma before because at the end; a period ends it."),
 "scholar": {"journal-q1": "… and quote one group’s suggestion.",
             "journal-q2": "… and quote what Caspian says about waiting for an even worse need.",
             "journal-q3": "… and quote Trumpkin’s reason for going."},
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "copia": {"seed": "Trumpkin <b data-verb>agreed</b> to carry the message.",
           "eg": ["Even though he didn’t believe in the Horn, Trumpkin agreed to carry the message.", "Trumpkin <i>volunteered</i> to carry the message.",
                  "Trumpkin agreed to carry the message to Cair Paravel, through enemy country, alone."]},
 "notes": {"wgrd": "Find the conflict (who is set against whom, and what is at stake) and the moment of choice: who decides, and how.",
           "vocab": V, "wordParts": WP, "grammar": GR, "spelling": SP},
 "wgrd": {"catcher": {"title": "The council", "intro": "As you read Ch. 7, catch the arguments and the choice.",
                      "fields": [{"label": "What each group wants", "hint": "the Bears: a feast first…", "rows": 4},
                                 {"label": "What is at stake", "hint": "", "rows": 2}],
                      "end": {"label": "The moment of choice: who decides, and what", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
 "counters": {"journal-q1": 40, "journal-q2": 32, "journal-q3": 32},
 "virtue": pv("Which pillar is it?",
   "The OAO Seven Pillars are honesty, respect, courtesy, responsibility, courage, service and perseverance. In Chapter 7, Caspian’s army meets, fights and nearly loses. Read each moment. Tap the pillar it shows best.",
   [{"t": "Nikabrik calls Doctor Cornelius a half-and-halfer. Caspian says, “This is my greatest friend and the saviour of my life. And anyone who doesn’t like his company may leave my army: at once.”", "ok": ["Respect", "Courage"], "why": "Caspian stands up for his friend in front of everyone.", "hint": "Whose side does Caspian take, and in front of whom?"},
    {"t": "Trufflehunter says it is time to blow the Horn. Caspian answers, “We are certainly in great need. But it is hard to be sure we are at our greatest.”", "ok": ["Responsibility"], "why": "He thinks hard before using the one treasure he was told to save.", "hint": "What was Caspian told about the Horn?"},
    {"t": "Trumpkin doesn’t believe in the Horn, but he says, “Send me, Sire, I’ll go.” He will travel through enemy country to Cair Paravel.", "ok": ["Service", "Courage"], "why": "He takes on a dangerous job for his King.", "hint": "What is the job, and is it safe?"},
    {"t": "Trumpkin says, “I know the difference between giving advice and taking orders. You’ve had my advice, and now it’s the time for orders.”", "ok": ["Respect", "Responsibility"], "why": "He says what he thinks, then follows his King’s decision.", "hint": "What does Trumpkin do after he disagrees?"}]),
}
L[2] = {
 "connector": "The Dwarf’s story is over. Now the children know who called them, and why. Today there’s no battle, only hard choices: walk or row, who leads, who keeps going when they’re worn out. Leading isn’t always shouting orders. Sometimes it’s just picking up the oar.",
 "writingFocus": "Leadership",
 "dol": dol("because the oars were too big for her lucy could not take a turn at rowing although she offered",
            B("Because") + " the oars were too big for her" + B(",") + " " + B("Lucy") + " could not take a turn at rowing although she offered" + B("."),
            "Capital B starts it; a comma after the opening because clause; capital L on Lucy; no comma before although at the end; a period ends it.",
            "when lucy dripped the cordial on his shoulder trumpkins wound was healed",
            B("When") + " " + B("Lucy") + " dripped the cordial on his shoulder" + B(",") + " " + B("Trumpkin’s") + " wound was healed" + B("."),
            "Capital W starts it; capitals on Lucy and Trumpkin; a comma after the opening when clause; an apostrophe in Trumpkin’s; a period ends it."),
 "scholar": {"journal-q1": "… and quote each of them.",
             "journal-q2": "… and name the creek Peter remembers.",
             "journal-q3": "… and quote what Peter says when Lucy offers to row."},
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": True, "count": 1}},
 "notes": {"wgrd": "Not every conflict is a fight. Notice the pressure (tired, lost, disagreeing), who moves first, and whether anyone told them to.",
           "vocab": V, "wordParts": WP, "grammar": GR + " Lewis uses if and because to show what depends on what.", "spelling": SP},
 "wgrd": {"catcher": {"title": "Quiet choices", "intro": "As you read Ch. 8, catch the choices.",
                      "fields": [{"label": "A choice the children make", "hint": "", "rows": 2}, {"label": "Who makes it, and was anyone told to?", "hint": "", "rows": 2}],
                      "layout": "row", "end": {"label": "What leading looks like without a battle", "hint": ""}}, "useAt": ["journal-q2", "journal-q3"]},
 "counters": {"journal-q1": 40, "journal-q2": 32, "journal-q3": 32},
 "virtue": pv("Which pillar is it?", "In Chapter 8 the children prove who they are and set out to find Caspian. Read each moment. Tap the pillar it shows best.",
   [{"t": "Susan beats Trumpkin at archery. She says, “It wasn’t really any better than yours. I think there was a tiny breath of wind as you shot.”", "ok": ["Courtesy"], "why": "She is kind to the person she just beat.", "hint": "How does Susan treat the loser?"},
    {"t": "Trumpkin answers, “No, there wasn’t. Don’t tell me. I know when I am fairly beaten.”", "ok": ["Honesty"], "why": "He won’t take an excuse that isn’t true.", "hint": "Does Trumpkin accept the excuse?"},
    {"t": "Lucy sees Trumpkin’s wounded shoulder and carefully drips one drop of her cordial onto it.", "ok": ["Service"], "why": "She uses her gift to help someone who is hurt.", "hint": "What does Lucy use her gift for?"},
    {"t": "Rowing is gruelling work. When Lucy offers to take a turn, Peter answers shortly, because he has no strength to spare for talking, and keeps rowing.", "ok": ["Perseverance"], "why": "He keeps going when he is worn out.", "hint": "How tired is Peter, and what does he do?"}]),
}
L[3] = {
 "connector": "The children are walking now, through wild woods and up to the edge of a deep gorge. Lucy sees something the others don’t, and the group has to vote. Watch each person weigh the choice. A vote tells you what someone values.",
 "writingFocus": "Leadership",
 "dol": dol("although lucy saw aslan clearly the others kept walking because they could not see him at all",
            B("Although") + " " + B("Lucy") + " saw " + B("Aslan") + " clearly" + B(",") + " the others kept walking because they could not see him at all" + B("."),
            "Capitals on Although, Lucy and Aslan; a comma after the opening although clause; no comma before because at the end; a period ends it.",
            "because edmund remembered being wrong before he voted to believe lucy",
            B("Because") + " " + B("Edmund") + " remembered being wrong before" + B(",") + " he voted to believe " + B("Lucy") + B("."),
            "Capitals on Because, Edmund and Lucy; a comma after the opening because clause; a period ends it."),
 "scholar": {"journal-q1": "… and quote one person’s reason.",
             "journal-q2": "… and quote Peter’s answer.",
             "journal-q3": "… and say what the plain words leave out."},
 "flags": {"journal-q1": {"quote": True, "count": 4}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "hints": {"s4w28cf1": hint("Think of finite. Which vowel do you hear clearly there?", "fin-ITE: the vowel is i, so defin<b>i</b>te."),
           "s4w28cf2": hint("Think of composite. Which vowel is stressed there?", "com-POS-ite: the vowel is i, so compos<b>i</b>tion."),
           "s4w28cf3": hint("Think of apart: separate means pulled apart. Which vowel?", "a-PART: the vowel is a, so sep<b>a</b>rate."),
           "s4w28cf4": hint("Think of councillor. Which consonant follows coun-?", "coun<b>c</b>il, like councillor.")},
 "notes": {"wgrd": "At the gorge, find the exact decision, weigh it from each voter’s side, and count what the choice costs.",
           "vocab": V + [["gorge", "A deep, narrow valley with steep sides."], ["bivouac", "A rough camp without proper shelter."]], "wordParts": WP,
           "grammar": GR + " Although and because let one sentence hold the doubt and the reason.", "spelling": SP},
 "wgrd": {"catcher": {"title": "The vote at the gorge", "intro": "As you read Ch. 9, record each vote.",
                      "fields": [{"label": "Who votes up, and why", "hint": "", "rows": 2}, {"label": "Who votes down, and why", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "What the choice costs", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
 "counters": {"journal-q1": 48, "journal-q2": 40, "journal-q3": 32},
 "virtue": pv("Which pillar is it?", "In Chapter 9 the group votes on which way to go. Read each moment. Tap the pillar it shows best.",
   [{"t": "Edmund says, “It was Lucy who discovered it first and none of us would believe her. I was the worst of the lot, I know.”", "ok": ["Honesty", "Courage"], "why": "He admits his old mistake in front of everyone.", "hint": "What does Edmund admit?"},
    {"t": "Susan says, “Don’t be angry, Lu, but I do think we should go down. I’m dead tired.”", "ok": ["Honesty", "Courtesy"], "why": "She tells the truth about how she feels, and says it gently.", "hint": "Does Susan hide her reason?"},
    {"t": "Peter says he’d much rather not have to vote. Trumpkin answers sternly, “You’re the High King.”", "ok": ["Responsibility"], "why": "Trumpkin reminds Peter that deciding is his job.", "hint": "Whose job is the choice?"},
    {"t": "Peter says, “I know Lucy may be right after all, but I can’t help it. We must do one or the other.”", "ok": ["Responsibility", "Honesty"], "why": "He makes the hard call and admits he might be wrong.", "hint": "What does Peter admit, and what does he still do?"}]),
}
L[4] = {
 "connector": "Three chapters, three hard choices: a council in the dark, a long row in the sun, and a vote at the edge of a gorge. Not every choice was right. Today you pick one, judge it, and prove your answer from the book.",
 "writingFocus": "Leadership",
 "dol": dol("because susan was dead tired she voted to go down so the group turned downstream",
            B("Because") + " " + B("Susan") + " was dead tired" + B(",") + " she voted to go down" + B(",") + " so the group turned downstream" + B("."),
            "Capitals on Because and Susan; a comma after the opening because clause and before so; a period ends it.",
            "although trumpkin did not believe in the horn he went to cair paravel because caspian was his king",
            B("Although") + " " + B("Trumpkin") + " did not believe in the " + B("Horn") + B(",") + " he went to " + B("Cair Paravel") + " because " + B("Caspian") + " was his king" + B("."),
            "Capitals on the names and on the Horn; a comma after the opening although clause; no comma before because at the end; a period ends it."),
 "scholar": {"journal-q1": "… and quote each leader once.",
             "journal-q2": "… and say what would have changed if Edmund had kept quiet.",
             "journal-q3": "… and use two different chapters for your two pieces of evidence."},
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "notes": {"wgrd": "Pick one choice from Ch. 7–9, say what the person was up against, and bring the moment from the book that proves your judgment.",
           "vocab": V + [["gorge", "A deep, narrow valley with steep sides."], ["bivouac", "A rough camp without proper shelter."]], "wordParts": WP,
           "grammar": GR + " Editing day: fix fragments and run-ons, and check each joint.", "spelling": SP},
 "wgrd": {"catcher": {"title": "Three hard choices", "intro": "Look back at Ch. 7–9.",
                      "fields": [{"label": "Ch. 7: Caspian at the council", "hint": "", "rows": 2},
                                 {"label": "Ch. 8: the children on the water", "hint": "", "rows": 2},
                                 {"label": "Ch. 9: Peter at the gorge", "hint": "", "rows": 2}],
                      "end": {"label": "The choice I’ll judge, and my verdict", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 40, "journal-q2": 32, "journal-q3": 48},
 "plate": {"src": "plates/pc-ch9.png", "alt": "Five small figures pick their way along the edge of a steep gorge above a rushing river.",
           "credit": "From Chapter 9, the vote at the gorge."},
 "virtue": {"kind": "log", "title": "This week’s strongest pillar", "intro": "Think about Chapters 7–9. Which pillar did the characters show most this week? Tap one.",
            "options": [{"t": p} for p in PIL],
            "line": "Name one moment that proves it.", "placeholder": "The strongest pillar was … because in Chapter … "},
}

T = {
 1: {"welcome": "Hello, it’s Nell. Caspian has an army now, a strange and wonderful one. Tonight it meets in council, and everybody has an idea. Today’s question: when everyone around a leader is arguing, what should the leader do?",
     "read": "Listen to each group at the council. The Bears want supper first. The Mice want to charge. The Moles want to dig. Ask what each idea tells you about who they are. Then watch for the moment the arguing stops and someone decides.",
     "morphology": "Three more Latin bases. Spect means look, so to respect someone is to look up to them. Ject means throw, so eject means throw out. Script and scribe mean write, and a scribe is a person whose job is writing. Find the base, and the word starts to explain itself."},
 2: {"welcome": "Hello again, it’s Nell. The Dwarf has finished his story, and the children know now who called them. Today’s question: what does leading look like when there’s no battle to fight?",
     "read": "This chapter has a sword fight for fun, an archery match, and a long, hot row. Watch who moves first when something has to be done. Nobody gives orders, but somebody always picks up the oar.",
     "grammar": "A complex sentence leans on a little word like because, although, when or if. Because Peter was worn out, he answered shortly. The because part can’t stand alone. It leans on the rest. When it comes first, put a comma after it."},
 3: {"welcome": "Hello, it’s Nell. The children are on foot now, and they come to the edge of a deep gorge. Today’s question: what does a vote tell you about the person who casts it?",
     "read": "Read the vote slowly. Listen to each person’s reason: Trumpkin, Susan, Edmund, then Peter. Nobody is silly here. Each one is weighing something real. Then notice the very last sentence of the chapter, and how plain it is.",
     "spelling": "Schwa is the lazy uh sound in a word. You can’t hear which vowel it is. So find a cousin of the word where the vowel is loud. Opposite sounds like uh in the middle. But oppose says its o clearly. So opposite has an o."},
 4: {"welcome": "Hello, it’s Nell. Three chapters, three hard choices. Today’s question: what makes a good leader, and which choice this week proves it?",
     "read": "Pick one choice from this week. Say what the person was up against before you judge them. Then find the page that proves what you think. One choice, looked at closely, beats three you mention quickly.",
     "grammar": "Editing day. Read each line out loud. Does it stand on its own? Because it was raining. That’s a piece, not a sentence. Does it run two sentences together with no joint? Fix the piece, mend the joint, and say why."},
}
WS = {1: ("morphology", "look, throw and write"), 2: ("grammar", "sentences that lean"), 3: ("spelling", "find the loud cousin"), 4: ("grammar", "pieces and joints")}

for d in L:
    ws, lab = WS[d]
    L[d]["media"] = media(d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    L[d]["virtue"].update(kicker=K, icon=I, name="pillars")
    io.open('data/lesson-28-%d.json' % d, 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
for d in T:
    print('28.%d' % d, {k: len(t) for k, t in T[d].items()}, 'plain chars', sum(len(t) for t in T[d].values()), '/ 950')
