#!/usr/bin/env python3
"""Writes data/lesson-26-1..4.json (week 26, Prince Caspian Ch. 1-3). Every moment checked in the text
(Planning docs/PrinceCaspian_CSL.pdf): Ch. 1 pp. 1-7, Ch. 2 pp. 8-14, Ch. 3 pp. 15-20.
Guide: Nell, an original narrator (a bookbinder; not a Lewis character, for copyright). Q4: scripts written, not recorded.
Word game: Fill the Treasure Chamber on the fill-in days (26.1, 26.3). Watch: the Seven Pillars Watch."""
import json, io

V = [["junction", "A place where things meet or connect, especially where train lines split."],
     ["thicket", "A dense group of bushes or small trees growing closely together."],
     ["brambles", "Thorny bushes, especially wild blackberry or raspberry bushes with prickly stems."],
     ["inhabited", "Lived in; having people or creatures living there."]]
WP = "Prefixes: pre- = before, re- = again or back, trans- = across, inter- = between: preview, return, transport, international."
GR = "Conjunctions join ideas. And adds one idea to another; or offers a choice between them. Stay in the castle or ride into the woods means one, not both."
SP = "To split a long word, peel off the prefix and suffix first, then the base is easy: un + familiar, transport + ed, discover + ed."
K = "Seven Pillars Watch · after you read"; I = "🏛️"
PIL = ["Honesty", "Respect", "Courtesy", "Responsibility", "Courage", "Service", "Perseverance"]
PRE = {"pre": "before", "re": "again", "trans": "across", "inter": "between"}
WHY = ("In Chapter 2, the children find the treasure chamber of their old castle, dusty and forgotten, its treasures waiting in the dark. "
       "Each word you build sets one treasure back in its place. This week’s word parts tell when and where: "
       "<b>pre-</b> (before), <b>re-</b> (again), <b>trans-</b> (across) and <b>inter-</b> (between).")
def treasure(h, win):
    return {"type": "treasure", "strand": "Morphology", "kicker": "Fill the Treasure Chamber", "h": h,
            "voice": "Tap a prefix, then the word it starts. Or drag the prefix onto the word.",
            "why": {"icon": "🗝️", "q": "Why a treasure chamber?", "t": WHY}, "meanings": PRE,
            "winDay": "Four treasures are back in their niches.", "win": win}
def media(d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/nell/g4ela-26-%d-welcome" % d, "label": "Nell’s welcome"},
         "read": {"kind": "audio", "path": "guide/nell/g4ela-26-%d-read" % d, "label": "Nell · before you read" if d < 4 else "Nell · looking back"},
         ws: {"kind": "video", "path": "guide/nell/g4ela-26-%d-%s" % (d, ws), "label": "Nell · " + wslabel}}
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
 "connector": "Welcome to a new book. I mend old books for a living, and this one I’ve read every winter since I was nine. Four children are sitting at a train station when something pulls at them. Where do they land, and when? Read for clues the way you’d read the cracks in an old binding: each one tells you how much time has passed.",
 "writingFocus": "Setting",
 "dol": dol("all around them stood trees sand seagulls and the wide blue water",
            B("All") + " around them stood trees" + B(",") + " sand" + B(",") + " seagulls" + B(",") + " and the wide blue water" + B("."),
            "Capital A starts the sentence; commas separate the four things in the list, including the one before and; a period ends it.",
            "the children found apples ivy daisies and an old stone wall",
            B("The") + " children found apples" + B(",") + " ivy" + B(",") + " daisies" + B(",") + " and an old stone wall" + B("."),
            "Capital T starts the sentence; commas separate the four things the children found, including the one before and; a period ends it."),
 "scholar": {"journal-q1": "… and use one detail for sight, one for sound, and one for feeling.",
             "journal-q2": "… and quote the words that make the change feel sudden.",
             "journal-q3": "… and ask one question the ruins make you wonder about."},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "hints": {"fill1": hint("Seeing something before it happens. Which prefix means before?", "pre- means before: pre + view."),
           "fill2": hint("Coming back again. Which prefix means again or back?", "re- means again or back: re + turn."),
           "fill3": hint("Carrying something across a distance. Which prefix means across?", "trans- means across: trans + port."),
           "fill4": hint("Between nations. Which prefix means between?", "inter- means between: inter + national.")},
 "copia": {"seed": "The children <b data-verb>found</b> an old stone wall.",
           "eg": ["Deep in the orchard, the children found an old stone wall.", "The children <i>stumbled on</i> an old stone wall.",
                  "The children found an old stone wall, broken down and covered with moss."]},
 "notes": {"wgrd": "In a fantasy setting, collect place clues (what the children see and touch) and time clues (what has crumbled or grown wild). Then say where and when they are in one sentence.",
           "vocab": V, "wordParts": WP, "grammar": GR, "spelling": SP},
 "wgrd": {"catcher": {"title": "Setting clues", "intro": "As you read Ch. 1, catch the clues.",
                      "fields": [{"label": "Place clues: what they see and touch", "hint": "", "rows": 3},
                                 {"label": "Time clues: what has crumbled or grown wild", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "Where and when they are, in one sentence", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 32, "journal-q2": 24, "journal-q3": 32},
 "wordgame": treasure("Prefixes of time and place", "Four treasures are back in their niches. <b>pre-</b> = before, <b>re-</b> = again, <b>trans-</b> = across, <b>inter-</b> = between."),
 "virtue": pv("Which pillar is it?",
   "The OAO Seven Pillars are honesty, respect, courtesy, responsibility, courage, service and perseverance. In Chapter 1 the children are hungry, thirsty and lost. Read each moment. Tap the pillar it shows best.",
   [{"t": "There are only two lunches among four children. They divide the sandwiches into four portions, even though nobody has quite enough.", "ok": ["Service", "Respect", "Courtesy"], "why": "They share fairly with each other instead of each keeping their own.", "hint": "Think about who gets the food."},
    {"t": "Edmund and Lucy want to leave their shoes on the beach. Susan says they might never find them again, and they will want them when night comes and it gets cold.", "ok": ["Responsibility"], "why": "Susan thinks ahead about what the group will need later.", "hint": "Who is thinking about tonight?"},
    {"t": "Peter thinks they may soon have to eat eggs raw, but he doesn’t say it out loud. Then he says, “Come on, Ed is right. And we must try to do something.”", "ok": ["Responsibility", "Perseverance", "Courage"], "why": "He keeps the others from losing heart and keeps the group moving.", "hint": "What does Peter do instead of complaining?"}]),
}
L[2] = {
 "connector": "Last time, the children stood in a sad, quiet ruin with walls all around. Today it gets a name. Watch Peter lay out his clues one by one, the way a good mender checks each page before saying what a book is. Then follow the torch down sixteen steps into the dark.",
 "writingFocus": "Setting",
 "dol": dol("susan found her presents the bow the ivory quiver and the feathered arrows",
            B("Susan") + " found her presents " + B("—") + " the bow" + B(",") + " the ivory quiver" + B(",") + " and the feathered arrows" + B("."),
            "Capital S on Susan; a dash before the list for emphasis; commas between the three presents; a period ends it.",
            "lucy took down her gift the little diamond bottle of cordial",
            B("Lucy") + " took down her gift " + B("—") + " the little diamond bottle of cordial" + B("."),
            "Capital L on Lucy; a dash points to the gift and makes the reader look at it; a period ends it."),
 "scholar": {"journal-q1": "… and put Peter’s four points in order.",
             "journal-q2": "… and say what Edmund’s missing gift tells you.",
             "journal-q3": "… and quote what Edmund says is “all impossible.”"},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": True, "count": 1}},
 "notes": {"wgrd": "Watch the children’s understanding of the place change. Each new clue (the chess-knight, the well, the orchard, the hidden door) moves them closer to knowing where they are.",
           "vocab": V, "wordParts": WP, "grammar": GR + " Lewis uses or when only one thing can be true.", "spelling": SP},
 "wgrd": {"catcher": {"title": "Peter’s clues", "intro": "As you read Ch. 2, list the clues in order.",
                      "fields": [{"label": "Clues that this is Cair Paravel", "hint": "1. the chess-knight…", "rows": 4}],
                      "end": {"label": "What the gifts tell me about who the children were", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
 "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 32},
 "virtue": pv("Which pillar is it?", "In Chapter 2 the children find their old treasure chamber. Read each moment. Tap the pillar it shows best.",
   [{"t": "Lucy asks where Susan’s horn is. Susan thinks, then says she took it hunting on their last day in Narnia and must have lost it.", "ok": ["Honesty"], "why": "Susan tells the truth about losing something very important.", "hint": "What does Susan admit?"},
    {"t": "In the middle of the treasures, Edmund says, “We mustn’t waste the battery.” They take what they need and go.", "ok": ["Responsibility"], "why": "Edmund remembers they will need the torch again.", "hint": "Who is thinking about later?"},
    {"t": "Peter’s pocket-knife breaks while they clear the ivy from the hidden door. They keep going with Edmund’s.", "ok": ["Perseverance"], "why": "They don’t quit when the tool breaks.", "hint": "What happens after the knife breaks?"},
    {"t": "Edmund goes first down the dark steps with the light, counting them out loud.", "ok": ["Courage"], "why": "He leads the way into a place none of them can see.", "hint": "Who goes first into the dark?"}]),
}
L[3] = {
 "connector": "The children have worked out the hardest clue: hundreds of years have passed in Narnia since they left. Today a boat comes round the point with two soldiers and a struggling bundle. Watch how quickly the children act, and listen to what the stranger they rescue tells them about the Narnia of now.",
 "writingFocus": "Setting",
 "dol": dol("lucys knife stayed in its sheath and the children hided among the trees and watched the boat",
            B("Lucy’s") + " knife stayed in its sheath" + B(",") + " and the children " + B("hid") + " among the trees and watched the boat" + B("."),
            "Capital L and an apostrophe in Lucy’s; a comma before and joins two complete thoughts; hid, not hided; a period ends it.",
            "peter and susan plunged into the water and they hauled the boat to the bank",
            B("Peter") + " and " + B("Susan") + " plunged into the water" + B(",") + " and they hauled the boat to the bank" + B("."),
            "Capitals on Peter and Susan; a comma before and joins two complete thoughts; a period ends it."),
 "scholar": {"journal-q1": "… and compare it to something from our world, the way Peter does.",
             "journal-q2": "… and quote what Susan says about shooting.",
             "journal-q3": "… and name the two kinds of Narnians the Dwarf talks about."},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": True, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "hints": {"s4w26cf1": hint("Peel off un-. What word is left?", "un + familiar: the base is familiar."),
           "s4w26cf2": hint("Peel off -ed. What word is left?", "transport + ed: the base is transport."),
           "s4w26cf3": hint("Peel off -ed. What word is left?", "discover + ed: the base is discover."),
           "s4w26cf4": hint("Peel off -ed. What word is left?", "desert + ed: the base is desert.")},
 "notes": {"wgrd": "Use setting details to learn how this world works: soldiers in steel caps, a Dwarf, stories of ghosts in the woods. Each one is a rule of the new Narnia.",
           "vocab": V, "wordParts": WP, "grammar": GR + " Too many ands in a row give every idea the same weight.", "spelling": SP},
 "wgrd": {"catcher": {"title": "Rules of the new Narnia", "intro": "As you read Ch. 3, catch what has changed.",
                      "fields": [{"label": "What the children remember", "hint": "", "rows": 3}, {"label": "What Narnia is like now", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "My prediction about what has happened", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 32},
 "wordgame": treasure("The chamber fills", "The treasure chamber is full again, and every torch is lit. <b>pre-</b> = before, <b>re-</b> = again, <b>trans-</b> = across, <b>inter-</b> = between."),
 "virtue": pv("Which pillar is it?", "In Chapter 3 the children save a stranger’s life. Read each moment. Tap the pillar it shows best.",
   [{"t": "Two soldiers are about to drown a bound Dwarf. Susan shoots; she is very pale, but she is already fitting a second arrow.", "ok": ["Courage"], "why": "She is scared and acts anyway to save a life.", "hint": "How does Susan feel, and what does she do?"},
    {"t": "Peter and Susan plunge into the water fully dressed and haul the boat to the bank.", "ok": ["Service", "Courage"], "why": "They help someone who cannot help himself.", "hint": "Who are they helping?"},
    {"t": "The Dwarf says, “Ghosts or not, you’ve saved my life and I’m extremely obliged to you.”", "ok": ["Courtesy", "Respect"], "why": "He thanks them properly, even though he doesn’t know who they are.", "hint": "What kind of words does he use?"},
    {"t": "The Dwarf says they must hide the boat. Peter says, “I ought to have thought of that myself.”", "ok": ["Honesty"], "why": "Peter admits he missed something.", "hint": "What does Peter admit?"}]),
}
L[4] = {
 "connector": "You’ve read three chapters. A station, an island, a ruin, a treasure chamber, a rescue. Today, step back the way I step back from a book I’ve just rebound. How did the setting grow from Chapter 1 to Chapter 3, and what kind of story do you think this is going to be?",
 "writingFocus": "Reflect",
 "dol": dol("trumpkin finished his story and looked at the children and peter began to plan",
            B("Trumpkin") + " finished his story and looked at the children" + B(",") + " and " + B("Peter") + " began to plan" + B("."),
            "Capitals on Trumpkin and Peter; a comma before the last and, which joins a new complete thought; a period ends it.",
            "edmund beat the ivy with a stick and the wall made a hollow sound",
            B("Edmund") + " beat the ivy with a stick" + B(",") + " and the wall made a hollow sound" + B("."),
            "Capital E on Edmund; a comma before and joins two complete thoughts; a period ends it."),
 "scholar": {"journal-q1": "… and use one detail from each chapter.",
             "journal-q2": "… and say what the object stands for, not just what it does.",
             "journal-q3": "… and name one thing that could only happen in Narnia.",
             "journal-q4": "… and say whether their idea changed yours."},
 "flags": {"journal-q1": {"quote": False, "count": 3}, "journal-q2": {"quote": False, "count": 1},
           "journal-q3": {"quote": False, "count": 1}, "journal-q4": {"quote": False, "count": 1}},
 "notes": {"wgrd": "Track how the setting grows across chapters: what the children knew at the start, what they figure out, and what it means for the story.",
           "vocab": V, "wordParts": WP, "grammar": GR + " Editing day: check that each and or or is doing the right job.", "spelling": SP},
 "wgrd": {"catcher": {"title": "How the setting grew", "intro": "Look back at Ch. 1–3.",
                      "fields": [{"label": "Ch. 1: where they think they are", "hint": "", "rows": 2},
                                 {"label": "Ch. 2: what they figure out", "hint": "", "rows": 2},
                                 {"label": "Ch. 3: what they learn about Narnia now", "hint": "", "rows": 2}],
                      "end": {"label": "What kind of story I think this will be", "hint": ""}}, "useAt": ["journal-q1"]},
 "counters": {"journal-q1": 40, "journal-q2": 32, "journal-q3": 32, "journal-q4": 24},
 "virtue": {"kind": "log", "title": "This week’s strongest pillar", "intro": "Think about Chapters 1–3. Which pillar did the children show most this week? Tap one.",
            "options": [{"t": p} for p in PIL],
            "line": "Name one moment that proves it.", "placeholder": "The strongest pillar was … because in Chapter … "},
}

T = {
 1: {"welcome": "Hello, I’m Nell. I mend old books, and this one I’ve read every winter since I was nine. It’s called Prince Caspian. Four children are waiting at a train station, and then they aren’t. Today’s question: what kind of place have they arrived at, and what clues tell you?",
     "read": "Read like a detective with a magnifying glass. Every time Lewis names something the children can see or touch, picture it. The water, the trees, the stone. Then watch for things that have crumbled or gone wild. Those tell you how long a place has been left alone.",
     "morphology": "Some word parts tell you when and where. Pre means before. Re means again, or back. Trans means across. Inter means between. Find the part at the front, ask what it adds to the word, and set one more treasure back in its place."},
 2: {"welcome": "Hello again, it’s Nell. Yesterday the children found a quiet, sad ruin. Today they find out whose it was. Today’s question: what new details do you learn about this place, and how does the children’s understanding of it change?",
     "read": "Watch Peter work it out one point at a time: the hall, the well, a little golden chess piece, an orchard. Then a hollow sound behind the ivy. When they go down the steps, count with them. And notice which gift isn’t where it should be.",
     "grammar": "And and or are small words with big jobs. And says both things are true. Or says choose one. The bread and the cheese means you get both. The bread or the cheese means you get one. When you see or, ask: what is the choice?"},
 3: {"welcome": "Hello, it’s Nell. The children have worked out something strange about time in Narnia. Today a boat comes round the point, and they have to decide fast. Today’s question: what does one rescue tell us about the children, and about the Narnia they’ve come back to?",
     "read": "Read Edmund’s idea about time slowly. It explains everything you’ve seen so far. Then watch the boat. Notice how fast the children act, and listen to the stranger they save. Everything he says is a clue about what Narnia is like now.",
     "spelling": "Long words look scary until you take them apart. Peel off the beginning and the ending first. What’s left is usually a word you already know. Unhappy: take off un, and there’s happy. Then the syllables almost split themselves."},
 4: {"welcome": "Hello, it’s Nell. You’ve read three chapters of Prince Caspian. Today you step back and look at the whole room before you open the next door. Today’s question: what kind of story do you think this is going to be, and what clues have you seen so far?",
     "read": "Flip back through Chapters 1 to 3. Find one place the children stood in each chapter. Notice how much more they understand by the end. Then pick one treasure they found and ask what it means to the person it belongs to.",
     "grammar": "Editing day. Read each sentence that uses and or or out loud. Ask if it’s doing the right job. And adds. Or offers a choice. And if a sentence has and, and, and, and, it’s time to cut a few and let one idea lead."},
}
WS = {1: ("morphology", "prefixes of time and place"), 2: ("grammar", "and or or"), 3: ("spelling", "take long words apart"), 4: ("grammar", "the right joining word")}

for d in L:
    ws, lab = WS[d]
    L[d]["media"] = media(d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    L[d]["virtue"].update(kicker=K, icon=I, name="pillars")
    io.open('data/lesson-26-%d.json' % d, 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
for d in T:
    print('26.%d' % d, {k: len(t) for k, t in T[d].items()}, 'plain chars', sum(len(t) for t in T[d].values()), '/ 950')
