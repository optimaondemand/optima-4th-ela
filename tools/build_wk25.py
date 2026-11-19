#!/usr/bin/env python3
"""Writes data/lesson-25-1..4.json (week 25, Freedom Train: comparing three accounts of the Combahee River Raid).
Sources checked Nov 19 2026: Source A, Wisconsin State Journal, June 20, 1863 (unsigned correspondent);
Source B, Tubman's dictated letter, printed by F. B. Sanborn in The Commonwealth (Boston), July 1863 and reprinted in
Bradford 1869; Source C, Sarah Bradford, Scenes in the Life of Harriet Tubman (1869). Sterling Ch. 18 pp. 165-172.
Q4 (no recordings this month): Marcus's scripts are written and the slots set; clips get recorded later.
The quilt runs on the two fill-in days (25.1, 25.3): this week it sews the quilt's border."""
import json, io

V = [["gallant", "Brave and heroic, especially in a noble cause."],
     ["commissary", "A place where food and supplies are stored, especially for an army."],
     ["rebeldom", "The Confederate states; the land of the rebellion."],
     ["contraband", "During the Civil War, enslaved people who escaped to Union lines."]]
WP = "Prefixes that tell where: trans- = across, inter- = between, sub- = under, super- = above or beyond: transportation, international, submarine, supernatural."
GR = "Commas in a series: put a comma after each item in a list of three or more, including before and. She packed bread, cheese, and a knife."
SP = ("Some words sound alike but mean different things. Affect is the action, effect is the result. It’s means it is; its shows belonging. "
      "Their means belonging to them, there is a place, they’re means they are. Accept means take; except means leave out.")
K = "Freedom Watch · after you read"; I = "⭐"
PLATE = {"src": "plates/ft-ch18.png", "alt": "Harriet Tubman stands in a rowboat on the Combahee River at night, singing to families hurrying aboard while Union gunboats wait in the moonlight.",
         "credit": "The Combahee River Raid, June 1863, the night all three sources describe."}
def quilt(h, meanings, why, win):
    return {"type": "quilt", "strand": "Morphology", "kicker": "Sew the Border", "h": h,
            "voice": "Tap a prefix, then the word it starts. Or drag the prefix onto the word. Ask where each word points.",
            "why": {"icon": "🧵", "q": "Why a border?", "t": why}, "meanings": meanings,
            "winDay": "Four border patches are sewn in.", "win": win}
def media(d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/marcus/g4ela-25-%d-welcome" % d, "label": "Marcus’s welcome"},
         "read": {"kind": "audio", "path": "guide/marcus/g4ela-25-%d-read" % d, "label": "Marcus · before you read the sources"},
         ws: {"kind": "video", "path": "guide/marcus/g4ela-25-%d-%s" % (d, ws), "label": "Marcus · " + wslabel}}
    for off in ("guide1", "guide2", "guide3", "rwm", "copia"): m[off] = {"kind": ""}
    return m
def hint(h1, why): return {"h1": h1, "why": why}
def dol(raw, fixed, why, raw2, fixed2, why2):
    return {"a": {"raw": raw, "fixed": fixed, "why": why}, "b": {"raw": raw2, "fixed": fixed2, "why": why2}}
B = lambda s: "<strong>" + s + "</strong>"
PRE = {"trans": "across", "inter": "between", "sub": "under", "super": "above"}
WHY = ("Harriet’s mother finished a patchwork quilt in Chapter 2, and all year the word-parts game sewed patches like hers. "
       "The quilt was finished last week. This week you sew its border with four prefixes that tell <i>where</i>: "
       "<b>trans-</b> (across), <b>inter-</b> (between), <b>sub-</b> (under) and <b>super-</b> (above).")

L = {}
L[1] = {
 "connector": "You finished the biography. Now meet the raid the way people first read about it in 1863. Two writers told the story of the same night on the Combahee River. One left out Harriet’s name. The other printed her own words. Read them one at a time, then ask what only each one tells you.",
 "writingFocus": "Revise",
 "plate": PLATE,
 "dol": dol("the raiders burned the barns the storehouses and the rice fields along the combahee river",
            B("The") + " raiders burned the barns" + B(",") + " the storehouses" + B(",") + " and the rice fields along the " + B("Combahee River") + B("."),
            "Capital T starts the sentence; commas after barns and storehouses separate the three things in the list; capital C and R on Combahee River; a period ends it.",
            "families carried baskets bundles and babies down to the riverbank",
            B("Families") + " carried baskets" + B(",") + " bundles" + B(",") + " and babies down to the riverbank" + B("."),
            "Capital F starts the sentence; commas after baskets and bundles separate the three items, including the one before and; a period ends it."),
 "scholar": {"journal-q1": "… and use one detail that only Source A gives and one that only Source B gives.",
             "journal-q2": "… and say what Source A calls her instead of her name.",
             "journal-q3": "… and say what the other writer might have wanted readers to notice.",
             "journal-q4": "… and quote the part of the sentence that comes after the claim."},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1},
           "journal-q3": {"quote": False, "count": 1}, "journal-q4": {"quote": True, "count": 2}},
 "hints": {"fill1": hint("Goods carried from one place to another. Which prefix means across?", "trans- means across: trans + portation = carrying across."),
           "fill2": hint("Something that happens among many countries. Which prefix means between?", "inter- means between: inter + national = between nations."),
           "fill3": hint("A boat that travels under the sea. Which prefix means under?", "sub- means under: sub + marine = under the sea."),
           "fill4": hint("Something beyond what nature can do. Which prefix means above or beyond?", "super- means above or beyond: super + natural.")},
 "copia": {"seed": "The newspaper <b data-verb>left out</b> her name.",
           "eg": ["In June 1863, the newspaper left out her name.", "The newspaper <i>skipped</i> her name.",
                  "The newspaper left out her name and called her “a black woman.”"]},
 "notes": {"wgrd": "Read one account at a time. Say the event in your own words. Then list what only each account tells you.",
           "vocab": V, "wordParts": WP, "grammar": GR, "spelling": SP},
 "wgrd": {"catcher": {"title": "Two accounts, one night", "intro": "Read Source A, then Source B.",
                      "fields": [{"label": "Only Source A tells me…", "hint": "", "rows": 3}, {"label": "Only Source B tells me…", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "The event both writers describe, in my own words", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 32, "journal-q2": 24, "journal-q3": 24, "journal-q4": 32},
 "wordgame": quilt("Prefixes that tell where", PRE, WHY,
                   "Four border patches are sewn in. <b>trans-</b> = across, <b>inter-</b> = between, <b>sub-</b> = under, <b>super-</b> = above."),
}
L[2] = {
 "connector": "Yesterday you met two newspaper accounts. Today a third writer joins them: Sarah Bradford, who wrote a book about Harriet six years later. Pick one fact, like how many people were freed, and find it in every source. Where do they agree, and where don’t they?",
 "writingFocus": "Edit",
 "plate": PLATE,
 "dol": dol("the freed families carried babies bundles and chickens onto the waiting steamboats",
            B("The") + " freed families carried babies" + B(",") + " bundles" + B(",") + " and chickens onto the waiting steamboats" + B("."),
            "Capital T starts the sentence; commas separate babies, bundles, and chickens; a period ends it.",
            "the scouts watched the river the woods and the roads for rebel guards",
            B("The") + " scouts watched the river" + B(",") + " the woods" + B(",") + " and the roads for " + B("Rebel") + " guards" + B("."),
            "Capital T starts the sentence; commas separate the river, the woods, and the roads; capital R on Rebel, the way Sterling writes it; a period ends it."),
 "scholar": {"journal-q1": "… and name the source each detail comes from.",
             "journal-q2": "… and connect the disadvantage to Source C.",
             "journal-q3": "… and say what the other two sources would add.",
             "journal-q4": "… and compare it with one more row."},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 2},
           "journal-q3": {"quote": True, "count": 1}, "journal-q4": {"quote": False, "count": 1}},
 "notes": {"wgrd": "Pick one fact that more than one source reports. Write each version side by side. Decide if the difference is small or changes what you think happened.",
           "vocab": V, "wordParts": WP, "grammar": GR, "spelling": SP},
 "wgrd": {"catcher": {"title": "One fact, three versions", "intro": "Pick a fact more than one source reports.",
                      "fields": [{"label": "The fact I picked", "hint": "how many were freed, what they call her…", "rows": 1},
                                 {"label": "Source A says", "hint": "", "rows": 2}, {"label": "Source B says", "hint": "", "rows": 2},
                                 {"label": "Source C says", "hint": "", "rows": 2}],
                      "end": {"label": "Small gap, or does it change the story?", "hint": ""}}, "useAt": ["journal-q1", "journal-q4"]},
 "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 32, "journal-q4": 24},
}
L[3] = {
 "connector": "You’ve spent two days with three accounts of one night. Today, put each writer in their place: who was close to the raid, and who wrote about it later? Then pull it together. What do you understand now that you could never get from one source alone?",
 "writingFocus": "Publish",
 "plate": PLATE,
 "dol": dol("harriets guides watched the roads counted the guards and warned the families before dawn",
            B("Harriet’s") + " guides watched the roads" + B(",") + " counted the guards" + B(",") + " and warned the families before dawn" + B("."),
            "Capital H and an apostrophe in Harriet’s (the guides belong to her); commas separate the three actions; a period ends it.",
            "the reporter wrote about the boats the soldiers and the burning barns",
            B("The") + " reporter wrote about the boats" + B(",") + " the soldiers" + B(",") + " and the burning barns" + B("."),
            "Capital T starts the sentence; commas separate the boats, the soldiers, and the burning barns; a period ends it."),
 "scholar": {"journal-q1": "… and say why Source A alone would leave it out.",
             "journal-q2": "… and give one example of each from this week’s sources.",
             "journal-q3": "… and quote the line you would use."},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": True, "count": 1}},
 "hints": {"fill1": hint("Carrying people across state lines. Which prefix means across?", "trans- means across: trans + port."),
           "fill2": hint("Courage beyond what a person usually has. Which prefix means beyond?", "super- means above or beyond: super + human."),
           "fill3": hint("The torpedoes were hidden under the water. Which prefix means under?", "sub- means under: sub + merged."),
           "fill4": hint("The scouts and the gunboats worked with each other. Which prefix means between?", "inter- means between: inter + connected."),
           "vc1": hint("The newspaper praised the soldiers as brave. Which word means brave and noble?", "gallant: “Montgomery’s gallant band.”"),
           "vc2": hint("Food and supplies for an army. Which word names where they are kept?", "commissary: an army’s store of food and supplies."),
           "vc3": hint("The army’s word for people who escaped to its lines.", "contraband: Tubman writes “known up in your region as ‘contrabands.’”"),
           "vc4": hint("The land of the rebellion. Which word ends in -dom, like kingdom?", "rebeldom: the Confederate states."),
           "s4w25cf1": hint("Here you need the action word: what will the testimony do?", "affect is the verb: the testimony will affect the conclusion."),
           "s4w25cf2": hint("Here you need a thing, the result. It comes after The.", "effect is the noun: the effect of the new source."),
           "s4w25cf3": hint("Say it with it is. Does it still make sense?", "It’s = it is: It is the only account written that year."),
           "s4w25cf4": hint("The page belongs to the document. Which one shows belonging?", "its shows belonging, with no apostrophe.")},
 "notes": {"wgrd": "Ask where each writer stood: close to the event, or writing years later. Close tells you what the day looked like. Later tells you what it came to mean.",
           "vocab": V, "wordParts": WP, "grammar": GR + " A series can also join three ideas into one sentence so they feel true all at once.",
           "spelling": SP},
 "wgrd": {"catcher": {"title": "Where each writer stood", "intro": "Put each source in its place.",
                      "fields": [{"label": "Close to the raid (and when)", "hint": "", "rows": 2},
                                 {"label": "Writing later (and when)", "hint": "", "rows": 2}],
                      "layout": "row", "end": {"label": "What I understand now that one source couldn’t give me", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
 "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 32},
 "wordgame": quilt("The border, finished", PRE, WHY,
                   "The border is finished all the way around. <b>trans-</b> = across, <b>inter-</b> = between, <b>sub-</b> = under, <b>super-</b> = above. The quilt is ready to hang."),
}
L[4] = {
 "connector": "This is the last day with Harriet. You read a whole biography and three real accounts of one night. When accounts disagree, a good reader picks one to lean on and can say why. Which account would you trust, and what can none of them tell you?",
 "writingFocus": "Present",
 "plate": {"src": "plates/ft-ch20.png", "alt": "An elderly Harriet Tubman rests on her porch in Auburn at dusk, looking up at the North Star.",
           "credit": "From Chapter 20. Harriet lived to see her story told by others, and she told it herself."},
 "dol": dol("tubman dictated her letter because she could not read or write",
            B("Tubman") + " dictated her letter because she could not read or write" + B("."),
            "Capital T on Tubman, a name; a period ends it. No comma is needed: there is no list here.",
            "sanborn printed her words her name and her story in his newspaper",
            B("Sanborn") + " printed her words" + B(",") + " her name" + B(",") + " and her story in his newspaper" + B("."),
            "Capital S on Sanborn, a name; commas separate her words, her name, and her story; a period ends it."),
 "scholar": {"journal-q1": "… and name what you would have missed with only that one source.",
             "journal-q2": "… and quote one phrase from Source B that sounds like Harriet.",
             "journal-q3": "… and name one other person whose story was told by someone else."},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": True, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "notes": {"wgrd": "When accounts disagree, choose one to lean on and say why: who wrote it, when, and how close they were. Then name what none of them can tell you.",
           "vocab": V, "wordParts": WP, "grammar": GR + " Editing day: check every list for its commas.", "spelling": SP},
 "wgrd": {"catcher": {"title": "The account I lean on", "intro": "Think about all three sources.",
                      "fields": [{"label": "The source I trust most about that night", "hint": "", "rows": 1},
                                 {"label": "Why: who, when, how close", "hint": "", "rows": 3}],
                      "end": {"label": "One thing none of the sources can tell me", "hint": ""}}, "useAt": ["journal-q1"]},
 "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 32},
}

T = {
 1: {"welcome": "Hey, it’s Marcus. You finished Freedom Train, but we’re not done with Harriet. This week you read the Combahee River Raid the way people first read it, in 1863. Today’s question: why does it matter who tells a story?",
     "read": "Read Source A all the way through, then Source B. Don’t jump back and forth yet. One writer never says her name. The other lets her talk. On my tours, this is where people get quiet. Notice what each one gives you that the other can’t.",
     "morphology": "Some word parts tell you where. Trans means across. Inter means between. Sub means under. Super means above or beyond. Put one in front of a word, and the word knows where it’s going. Find the part that tells where, then sew the border patch."},
 2: {"welcome": "Hey, it’s Marcus. Today a third writer joins the story: Sarah Bradford, who wrote a book about Harriet six years after the raid. Today’s question: when writers tell the same story differently, what can the differences teach us?",
     "read": "Pick one fact, like how many people were freed, or what each writer calls Harriet. Find it in every source and set the versions side by side. Some gaps are small. Some change the whole picture. Read the table straight across, one row at a time.",
     "grammar": "A list needs commas so the reader can tell where one thing stops and the next begins. Lanterns, quilts, and dried meat. Without commas, you might wonder what a quilt meat is. Put a comma after every item but the last, and keep the one before and."},
 3: {"welcome": "Hey, it’s Marcus. You’ve spent two days with three accounts of one night. Today you pull it all together. Today’s question: what do you understand now that you could never get from just one source?",
     "read": "Put each writer in their place. Who was close to the raid, and who wrote about it later from other people’s words? Close can tell you what the night looked like. Later can tell you what it meant. Then ask which one you’d quote first in a report.",
     "spelling": "Some mistakes slip past a spellchecker because they’re real words in the wrong place. Affect is the action. Effect is the result. It’s means it is. Its shows something belongs. When you’re not sure, say the long form out loud. If it sounds wrong, it is."},
 4: {"welcome": "Hey, it’s Marcus. This is our last day with Harriet. You’ve read her whole life and three real accounts of her biggest night. Today’s question: what have you learned about how different writers tell the same story, and why it matters?",
     "read": "Today you choose. If you had to tell a friend what happened on the Combahee, which account would you lean on? Say why: who wrote it, when, and how close they were. Then name one thing about that night none of them can tell you. Harriet could not write, but she still got her words printed.",
     "grammar": "Editing day. Read every list in your writing out loud. If you hear three things, you need two commas. A comma can change what a sentence means, so don’t guess. Ask how many things are in the list, then count your commas. One more slow read, and you’re ready to present."},
}
WS = {1: ("morphology", "prefixes that tell where"), 2: ("grammar", "commas in a list"), 3: ("spelling", "words that sound alike"), 4: ("grammar", "a last comma check")}

VW = {
 1: {"kind": "line", "title": "Her own words",
     "intro": "In Source B, Harriet Tubman calls the people she helped free “seven hundred and fifty-six head of their most valuable livestock, known up in your region as ‘contrabands.’” She is using the slaveholders’ way of talking about people, on purpose.",
     "line": "Write one sentence: What is Harriet really saying about freedom?", "placeholder": "Harriet is really saying…"},
 2: {"kind": "sort", "title": "Moving freedom forward, or holding it back?", "yes": "Moves freedom forward", "no": "Holds it back",
     "intro": "These moments come from this week’s sources and Chapter 18. Tap Moves freedom forward or Holds it back.",
     "items": [{"t": "Harriet guides the gunboats past the torpedoes hidden in the river.", "ok": True, "why": "Her scouting keeps the boats safe so they can reach the people waiting on the banks."},
               {"t": "The Rebels hide torpedoes in the river to sink Union boats.", "ok": False, "why": "The torpedoes were set to stop the boats before anyone could be freed."},
               {"t": "A newspaper prints the story but leaves out Harriet’s name.", "ok": False, "why": "Her work is real, but she gets no credit for it."},
               {"t": "Harriet tells her own account, and it is printed in The Commonwealth.", "ok": True, "why": "Her own words reach readers, so the story is told by the person who led it."},
               {"t": "Nearly all the able-bodied men who were freed join the Black regiments.", "ok": True, "why": "People who were just freed fight to free others. (Bradford reprints this from 1863.)"}]},
 3: {"kind": "log", "title": "Freedom log", "intro": "Which moment from this week’s sources shows freedom best? Tap one.",
     "options": [{"t": "Almost eight hundred people climb aboard the “Lincoln boats” in one night."},
                 {"t": "The raiders return “without losing a man or receiving a scratch.”"},
                 {"t": "Harriet, who could not write, dictates her own account so her words are printed."},
                 {"t": "Freed men join the Black regiments to fight for the Union."}],
     "line": "Finish the sentence: This moment shows freedom because…", "placeholder": "This moment shows freedom because…"},
 4: {"kind": "meter", "title": "The freedom meter", "intro": "Think about the whole unit.",
     "moment": "In 1863 one newspaper told the story of the raid without Harriet’s name. Weeks later, her own words were printed. Six years later, a whole book told her life. Almost a hundred years later, Dorothy Sterling wrote Freedom Train for young readers like you.",
     "ask": "How much does it matter who gets to tell the story? Slide to show.", "line": "Tell why in one sentence.",
     "placeholder": "It matters this much because…",
     "take": "One way to see it: Harriet could not read or write, so she dictated her letter. Without that, we would know the raid only as the work of “a black woman.”"},
}

for d in L:
    ws, lab = WS[d]
    L[d]["media"] = media(d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    v = VW[d]; v.update(kicker=K, icon=I, name="freedom"); L[d]["virtue"] = v
    io.open('data/lesson-25-%d.json' % d, 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
for d in T:
    print('25.%d' % d, {k: len(t) for k, t in T[d].items()}, 'plain chars', sum(len(t) for t in T[d].values()), '/ 950')
