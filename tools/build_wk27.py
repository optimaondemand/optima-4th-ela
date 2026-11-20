#!/usr/bin/env python3
"""Writes data/lesson-27-1..4.json (week 27, Prince Caspian Ch. 4-6). Every moment checked in the text
(Planning docs/PrinceCaspian_CSL.pdf): Ch. 4 pp. 21-29, Ch. 5 pp. 30-38, Ch. 6 pp. 39-44.
Guide: Nell (original narrator). Q4: scripts written, not recorded.
Word game: Fill the Treasure Chamber on the word-base days (27.1, 27.3). Watch: the Seven Pillars Watch."""
import json, io

V = [["tutor", "A private teacher who teaches one student or a few."],
     ["usurper", "Someone who takes power, like a throne, without the right to it."],
     ["astronomy", "The study of the stars, planets and sky."],
     ["sternly", "In a strict, serious, firm way."]]
WP = "Latin bases: port = carry, tract = pull or draw, struct = build: transport, attract, construct, instructed."
GR = "But and so join two complete sentences. But says the second part goes against what you expected; so says the second part happens because of the first. Put a comma before each."
SP = "Suffix rules: drop the silent e (hope + ing = hoping); change y to i (empty + er = emptier); double the last consonant when the last syllable is stressed (begin + ing = beginning, but visit + ing = visiting)."
K = "Seven Pillars Watch · after you read"; I = "🏛️"
PIL = ["Honesty", "Respect", "Courtesy", "Responsibility", "Courage", "Service", "Perseverance"]
BASES = {"port": "carry", "tract": "pull", "struct": "build"}
WHY = ("The treasure chamber at Cair Paravel is still waiting for its treasures. This week Caspian learns that the old stories are true, "
       "and the Old Narnians come out of hiding one by one. Each word you build sets one more treasure in its place. "
       "This week’s Latin bases: <b>port</b> (carry), <b>tract</b> (pull) and <b>struct</b> (build).")
def treasure(h, win):
    return {"type": "treasure", "strand": "Morphology", "kicker": "Fill the Treasure Chamber", "h": h,
            "voice": "Tap a word base, then the word it belongs in. Or drag the base onto the word.",
            "why": {"icon": "🗝️", "q": "Why a treasure chamber?", "t": WHY}, "meanings": BASES,
            "winDay": "More treasures are back in their niches.", "win": win}
def media(d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/nell/g4ela-27-%d-welcome" % d, "label": "Nell’s welcome"},
         "read": {"kind": "audio", "path": "guide/nell/g4ela-27-%d-read" % d, "label": "Nell · before you read" if d < 4 else "Nell · looking back"},
         ws: {"kind": "video", "path": "guide/nell/g4ela-27-%d-%s" % (d, ws), "label": "Nell · " + wslabel}}
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
 "connector": "The Dwarf has started his story, and it’s a story inside a story: the four children are sitting by the fire, listening, while we go back to a castle and a boy named Caspian. Keep two lists as you read today: who is with Caspian, and who is against him.",
 "writingFocus": "Compare",
 "dol": dol("the nurse told him about old narnia but miraz sent her away",
            B("The") + " nurse told him about " + B("Old Narnia") + B(",") + " but " + B("Miraz") + " sent her away" + B("."),
            "Capitals start the sentence and name Old Narnia and Miraz; a comma comes before but because it joins two complete sentences; a period ends it.",
            "caspian loved history so doctor cornelius taught him in secret",
            B("Caspian") + " loved history" + B(",") + " so " + B("Doctor Cornelius") + " taught him in secret" + B("."),
            "Capitals on Caspian and Doctor Cornelius; a comma before so, which joins a cause to what it led to; a period ends it."),
 "scholar": {"journal-q1": "… and give each character a different word.",
             "journal-q2": "… and quote what Miraz calls the old stories.",
             "journal-q3": "… and quote something Caspian says on the tower."},
 "flags": {"journal-q1": {"quote": False, "count": 4}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "hints": {"fill1": hint("Carrying something across. Which base means carry?", "port means carry: trans + port."),
           "fill2": hint("Pulling something out. Which base means pull?", "tract means pull or draw: ex + tract."),
           "fill3": hint("Putting parts together. Which base means build?", "struct means build: con + struct."),
           "fill4": hint("Carrying goods in. Which base means carry?", "port means carry: im + port.")},
 "copia": {"seed": "Caspian <b data-verb>listened</b> to the old stories.",
           "eg": ["Every night at bedtime, Caspian listened to the old stories.", "Caspian <i>drank in</i> the old stories.",
                  "Caspian listened to the old stories of Talking Beasts, Dwarfs and Fauns."]},
 "notes": {"wgrd": "Track groups of characters: when someone new appears, put the name on one of two lists (with Caspian, or against him). Leave a question mark if you’re not sure yet.",
           "vocab": V, "wordParts": WP, "grammar": GR, "spelling": SP},
 "wgrd": {"catcher": {"title": "Who is on which side?", "intro": "As you read Ch. 4, sort the characters.",
                      "fields": [{"label": "With Caspian", "hint": "", "rows": 3}, {"label": "Against Caspian (or not sure yet?)", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "The person Caspian trusts most, and why", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
 "counters": {"journal-q1": 40, "journal-q2": 32, "journal-q3": 32},
 "wordgame": treasure("Bases that carry, pull and build", "Four treasures are back in their niches. <b>port</b> = carry, <b>tract</b> = pull, <b>struct</b> = build."),
 "virtue": pv("Which pillar is it?",
   "The OAO Seven Pillars are honesty, respect, courtesy, responsibility, courage, service and perseverance. Chapter 4 happens in Miraz’s castle, where the old stories are a secret. Read each moment. Tap the pillar it shows best.",
   [{"t": "Miraz asks what more anyone could wish for than to be King. Caspian answers, “All the same, I do wish,” and tells his uncle the truth: he wishes he could have lived in the Old Days.", "ok": ["Honesty"], "why": "Caspian says what he really thinks, even to the King.", "hint": "Does Caspian hide what he wishes?"},
    {"t": "Doctor Cornelius whispers that if the King found him telling Caspian secrets, he would lose his head. He goes on teaching Caspian the truth anyway.", "ok": ["Courage", "Service"], "why": "He takes a terrible risk so Caspian can know the truth.", "hint": "What could happen to the Doctor?"},
    {"t": "On the tower, the Doctor says Caspian can help the hidden Old Narnians when he is King. Caspian says, “I do, I do. But how can I help?”", "ok": ["Service", "Responsibility"], "why": "Caspian wants to help people who need it.", "hint": "What does Caspian ask?"}]),
}
L[2] = {
 "connector": "Yesterday Caspian learned the old stories are true. Tonight the Doctor wakes him with news that changes everything, and puts a horn in his hands. Keep your lists going: by the end of today, Caspian has new friends, and not all of them trust him.",
 "writingFocus": "Compare",
 "dol": dol("queen prunaprismia had a son but caspian was the true king so miraz wanted him gone",
            B("Queen Prunaprismia") + " had a son" + B(",") + " but " + B("Caspian") + " was the true king" + B(",") + " so " + B("Miraz") + " wanted him gone" + B("."),
            "Capitals on the three names; a comma before but (it goes against what you expect) and before so (it tells what happened because of it); a period ends it.",
            "the horn was a great treasure but caspian must not use it except at his greatest need",
            B("The") + " horn was a great treasure" + B(",") + " but " + B("Caspian") + " must not use it except at his greatest need" + B("."),
            "Capital T and capital C; a comma before but joins the two complete thoughts; a period ends it."),
 "scholar": {"journal-q1": "… and name what happened two hours before.",
             "journal-q2": "… and quote what Trufflehunter says about beasts.",
             "journal-q3": "… and name one risk the Doctor took in Chapter 4, too."},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "notes": {"wgrd": "Inside one group, members can feel opposite ways about the same person. Trufflehunter and Trumpkin save Caspian; Nikabrik wants him dead. Mark each reaction and ask what each one knows.",
           "vocab": V, "wordParts": WP, "grammar": GR + " Lewis uses but when a hope runs into trouble.", "spelling": SP},
 "wgrd": {"catcher": {"title": "One group, three answers", "intro": "As you read Ch. 5, catch how each one treats Caspian.",
                      "fields": [{"label": "Trufflehunter", "hint": "", "rows": 2}, {"label": "Trumpkin", "hint": "", "rows": 2}, {"label": "Nikabrik", "hint": "", "rows": 2}],
                      "end": {"label": "Why they don’t agree", "hint": ""}}, "useAt": ["journal-q2"]},
 "counters": {"journal-q1": 32, "journal-q2": 40, "journal-q3": 32},
 "virtue": pv("Which pillar is it?", "In Chapter 5 Caspian runs for his life. Read each moment. Tap the pillar it shows best.",
   [{"t": "The Doctor wakes Caspian and says, “Trust me and do exactly as I tell you.” Caspian is very surprised, but he begins doing what he is told at once.", "ok": ["Respect"], "why": "Caspian trusts his teacher and listens right away.", "hint": "How does Caspian treat his Tutor’s words?"},
    {"t": "Caspian asks the Doctor to come with him. The Doctor says, “I dare not. It would make your danger greater.”", "ok": ["Service", "Responsibility"], "why": "He stays behind to keep Caspian safer.", "hint": "Who is the Doctor thinking about?"},
    {"t": "Nikabrik grabs his dagger to stab Caspian. Trufflehunter and Trumpkin get in the way and hold him down.", "ok": ["Courage", "Service"], "why": "They protect a stranger, even from their own friend.", "hint": "Who steps in?"},
    {"t": "Trufflehunter says, “I’m a beast, I am, and a Badger what’s more. We don’t change. We hold on.”", "ok": ["Perseverance"], "why": "He has held on to the old truth for hundreds of years.", "hint": "What does holding on mean here?"}]),
}
L[3] = {
 "connector": "Caspian has met three Old Narnians. Today he meets dozens: bears, a squirrel, Dwarfs at a forge, a Centaur who reads the stars, and a very small Mouse with a very large bow. So many names! Group them as you go, and ask what each group wants from Caspian.",
 "writingFocus": "Compare",
 "dol": dol("reepicheep was very small so some creatures doubted him but his courage was the greatest of all",
            B("Reepicheep") + " was very small" + B(",") + " so some creatures doubted him" + B(",") + " but his courage was the greatest of all" + B("."),
            "Capital R on the name; a comma before so (cause and result) and before but (a surprise); a period ends it.",
            "the badger did not want armor so he kept only his claws and teeth",
            B("The") + " badger did not want armor" + B(",") + " so he kept only his claws and teeth" + B("."),
            "Capital T starts it; a comma before so, because the second part happens because of the first; a period ends it."),
 "scholar": {"journal-q1": "… and give each group one word.",
             "journal-q2": "… and name the two planets.",
             "journal-q3": "… and say what Caspian does to win them over."},
 "flags": {"journal-q1": {"quote": False, "count": 3}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "hints": {"s4w27cf1": hint("be·GIN is stressed on the last syllable. Double or not?", "Double the n: begin + n + ing = beginning."),
           "s4w27cf2": hint("VIS·it is stressed on the first syllable. Double or not?", "No double: visit + ing = visiting."),
           "s4w27cf3": hint("for·GET is stressed on the last syllable. Double or not?", "Double the t: forget + t + ing = forgetting."),
           "s4w27cf4": hint("TRAV·el is stressed on the first syllable. Double or not?", "In American spelling, no double: travel + ed = traveled.")},
 "notes": {"wgrd": "With a crowd of new characters, sort them into kinds (bears, Dwarfs, Centaurs, Fauns), give each kind one word, and ask what each group wants from Caspian.",
           "vocab": V, "wordParts": WP, "grammar": GR + " Swapping but for so can flip the meaning.", "spelling": SP},
 "wgrd": {"catcher": {"title": "The Old Narnians, sorted", "intro": "As you read Ch. 6, group the creatures.",
                      "fields": [{"label": "Who Caspian meets", "hint": "the Bulgy Bears, Pattertwig…", "rows": 4},
                                 {"label": "One word for each group", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "What they all want from Caspian", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 40, "journal-q2": 32, "journal-q3": 32},
 "wordgame": treasure("More treasures come home", "More treasures are back in the chamber. <b>port</b> = carry, <b>tract</b> = pull, <b>struct</b> = build."),
 "virtue": pv("Which pillar is it?", "In Chapter 6 the Old Narnians come out of hiding. Read each moment. Tap the pillar it shows best.",
   [{"t": "Reepicheep bows and says, “There are twelve of us, Sire,” and “I place all the resources of my people unreservedly at your Majesty’s disposal.”", "ok": ["Service", "Courage", "Courtesy"], "why": "He offers everything his people have, with perfect manners.", "hint": "What does Reepicheep offer?"},
    {"t": "Caspian thinks Reepicheep’s whole people could fit in a washing basket. He tries hard, and successfully, not to laugh.", "ok": ["Courtesy", "Respect"], "why": "He will not make fun of someone who has just offered to fight for him.", "hint": "What does Caspian hold back?"},
    {"t": "The Seven Brothers of Shuddering Wood give Caspian, Trumpkin and Nikabrik mail shirts, helmets and swords.", "ok": ["Service"], "why": "They give their best work to the cause.", "hint": "What do the Dwarfs give?"},
    {"t": "Glenstorm says, “I watch the skies, Badger, for it is mine to watch, as it is yours to remember.”", "ok": ["Responsibility"], "why": "He knows his own job and does it.", "hint": "What does each creature have to do?"}]),
}
L[4] = {
 "connector": "Three chapters of the Dwarf’s story are done. Caspian started in a castle full of Telmarines. He ends the week in a moonlit glade full of Fauns. Today, line up every group you met, say what each one wants, and find the two groups that are heading straight for each other.",
 "writingFocus": "Compare",
 "dol": dol("the telmarines had swords but the old narnians had something stronger the memory of aslan so they refused to give up",
            B("The Telmarines") + " had swords" + B(",") + " but the " + B("Old Narnians") + " had something stronger " + B("—") + " the memory of " + B("Aslan") + B(",") + " so they refused to give up" + B("."),
            "Capitals on Telmarines, Old Narnians and Aslan; a comma before but and before so; a dash sets off the important detail; a period ends it.",
            "nikabrik hated the telmarines so he did not trust caspian at first",
            B("Nikabrik") + " hated the " + B("Telmarines") + B(",") + " so he did not trust " + B("Caspian") + " at first" + B("."),
            "Capitals on the names; a comma before so joins the cause to its result; a period ends it."),
 "scholar": {"journal-q1": "… and give one reason for every name on your web.",
             "journal-q2": "… and say what Caspian needs that only one of them can give.",
             "journal-q3": "… and use one detail from Chapter 4 and one from Chapter 6."},
 "flags": {"journal-q1": {"quote": False, "count": 5}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 2}},
 "notes": {"wgrd": "Line up every group from Ch. 4–6, say what each wants, and find the two groups heading for each other.",
           "vocab": V, "wordParts": WP, "grammar": GR + " Editing day: check that each but or so carries the right logic.", "spelling": SP},
 "wgrd": {"catcher": {"title": "Every group, one goal", "intro": "Look back at Ch. 4–6.",
                      "fields": [{"label": "Groups with Caspian, and what they want", "hint": "", "rows": 3},
                                 {"label": "Groups against him, and what they want", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "The two groups heading for each other", "hint": ""}}, "useAt": ["journal-q1"]},
 "counters": {"journal-q1": 48, "journal-q2": 32, "journal-q3": 40},
 "virtue": {"kind": "log", "title": "This week’s strongest pillar", "intro": "Think about Chapters 4–6. Which pillar did Caspian and his friends show most this week? Tap one.",
            "options": [{"t": p} for p in PIL],
            "line": "Name one moment that proves it.", "placeholder": "The strongest pillar was … because in Chapter … "},
}

T = {
 1: {"welcome": "Hello, it’s Nell. The Dwarf is telling the children a story, and now we hear it too. It’s about a boy who grew up in a castle where the old stories were forbidden. Today’s question: why would the truth ever need to be hidden?",
     "read": "Keep two lists as you read. Everyone who helps Caspian goes on one. Everyone who controls him goes on the other. If you can’t tell yet, write the name with a question mark. Watch the nurse, the King, and the Doctor with the great spectacles.",
     "morphology": "Some words are built on old Latin bases. Port means carry, so a porter carries bags. Tract means pull, so a tractor pulls a plow. Struct means build, so a structure is something built. Find the base, ask what it does, and set a treasure back in its place."},
 2: {"welcome": "Hello again, it’s Nell. Last time, Caspian learned the old stories are true. Tonight, the Doctor wakes him in the dark with a message that can’t wait. Today’s question: who welcomes Caspian when he runs, and who doesn’t, and why?",
     "read": "Read the Doctor’s warning slowly. Notice what happened only two hours before, and the gift he puts in Caspian’s hands. Then the storm. When Caspian wakes up, he’s with three strangers. Listen to each one. They don’t all agree about him.",
     "grammar": "But and so are tiny hinges. But says, here comes a surprise: Caspian’s heart was sinking, but he tried to take it all in. So says, here’s what happened because of it. Put a comma before each when it joins two whole sentences."},
 3: {"welcome": "Hello, it’s Nell. Caspian has three friends now. Today he meets a whole hidden country of them. Today’s question: how do you keep track of so many new characters, and what does each group want?",
     "read": "So many names today! Don’t try to hold them all. Sort them as you go: the bears, the squirrel, the Dwarfs at the forge, the Centaur, the Mouse, the Fauns. Give each kind one word. And watch how Lewis starts each new visit.",
     "spelling": "Here’s a trick for long words. Say the word and listen for the strong beat. Be-GIN. If the beat is on the last part, and it ends in one vowel and one consonant, double the consonant: beginning. VIS-it has its beat at the front, so no double: visiting."},
 4: {"welcome": "Hello, it’s Nell. Three chapters of the Dwarf’s story are done. A castle, a storm, a cave, a forge, a moonlit dance. Today’s question: what changed for Caspian this week, and what made the change possible?",
     "read": "Line up every group you met this week, from Miraz’s court to the Fauns. Say what each group wants. Then find the two groups that want opposite things. They’re going to meet, and when they do, it won’t be gentle.",
     "grammar": "Editing day. Read each sentence with but or so, and ask if the logic is right. Caspian was tired, but he rode on. That works. Caspian was tired, so he rode on. That doesn’t. One small word, and the meaning flips."},
}
WS = {1: ("morphology", "bases that carry, pull and build"), 2: ("grammar", "but and so"), 3: ("spelling", "listen for the beat"), 4: ("grammar", "the right hinge")}

L[4]["plate"] = {"src": "plates/pc-ch6.png", "alt": "Fauns dance in the moonlight around a boy at the edge of a wide circle of grass.",
                "credit": "From Chapter 6, the night the old stories came alive for Caspian."}
for d in L:
    ws, lab = WS[d]
    L[d]["media"] = media(d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    L[d]["virtue"].update(kicker=K, icon=I, name="pillars")
    io.open('data/lesson-27-%d.json' % d, 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
for d in T:
    print('27.%d' % d, {k: len(t) for k, t in T[d].items()}, 'plain chars', sum(len(t) for t in T[d].values()), '/ 950')
