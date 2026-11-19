#!/usr/bin/env python3
"""Writes data/lesson-22-1..4.json (week 22, Freedom Train Ch. 10-14). Moments and quotes checked in Sterling."""
import json, io

VOCAB = [["abolition", "The act of ending something, especially slavery."],
         ["conductor", "A guide on the Underground Railroad; or, the person who runs a train."],
         ["obtain", "To get or acquire something."],
         ["express", "To make a thought, feeling, or idea known to others."]]
PARTS = "press means “push” and tain means “hold”: express, impress, contain, obtain."
SPELL = "The suffixes -ive, -al, and -ic turn a word into a describing word: act → active, music → musical, hero → heroic. Look at the base word first. Sometimes a letter drops, like a silent e."
K = "Freedom Watch · after you read"; I = "⭐"
WHY_QUILT = ("In Chapter 2, Harriet’s mother, Old Rit, finishes a patchwork quilt, the family’s only treasure. Years later, in Chapter 12, "
             "Harriet tucks that same quilt over her parents’ legs as she drives them out of slavery. "
             "<b>press</b> means <i>push</i>, and <b>tain</b> means <i>hold</i>. Each right word sews one patch into the quilt. Four each lesson, until the quilt is finished.")
def quilt(h):
    return {"type": "quilt", "strand": "Morphology", "kicker": "Sew the Quilt", "h": h,
            "voice": "Tap a root, then the word it finishes. Or drag the root onto the word. Ask what each word is about: pushing, or holding?",
            "why": {"icon": "🧵", "q": "Why a quilt?", "t": WHY_QUILT}, "meanings": {"press": "push", "tain": "hold"},
            "winDay": "Four more patches are sewn in. The next lesson’s words add more.",
            "win": "Old Rit’s quilt is finished, and a North Star is stitched across its middle. <b>press</b> = push, <b>tain</b> = hold."}
def media(d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/marcus/g4ela-22-%d-welcome" % d, "label": "Marcus’s welcome"},
         "read": {"kind": "audio", "path": "guide/marcus/g4ela-22-%d-read" % d, "label": "Marcus · before you read"},
         ws: {"kind": "audio", "path": "guide/marcus/g4ela-22-%d-%s" % (d, ws), "label": "Marcus · " + wslabel}}
    for off in ("guide1", "guide2", "guide3", "rwm", "copia"): m[off] = {"kind": ""}
    return m
def hint(h1, why): return {"h1": h1, "why": why}
def dol(raw, fixed, why, raw2, fixed2, why2):
    return {"a": {"raw": raw, "fixed": fixed, "why": why}, "b": {"raw": raw2, "fixed": fixed2, "why": why2}}
B = lambda s: "<strong>" + s + "</strong>"

L = {}
L[1] = {
 "connector": "At the end of Chapter 9, Harriet stood in Philadelphia, free and earning her own money. But her family was still in Maryland. She told William Still she would go down, like Moses into Egypt, to lead them out. In Chapter 10, look for what makes each trip happen, and what each trip leads to.",
 "writingFocus": "Organize + Draft",
 "dol": dol("harriet walked carefully south her steps were silent and her heart beat loudly",
            B("Harriet") + " walked carefully south" + B(".") + " " + B("Her") + " steps were silent" + B(",") + " and her heart beat loudly" + B("."),
            "Capital H on Harriet; a period ends the first sentence; capital H starts the second; a comma before and joins two complete thoughts. Carefully and loudly are adverbs that tell how.",
            "mary ann sailed quietly up the bay harriet waited anxiously in baltimore",
            B("Mary Ann") + " sailed quietly up the " + B("Bay") + B(".") + " " + B("Harriet") + " waited anxiously in " + B("Baltimore") + B("."),
            "Capital M and A on Mary Ann (a name); capital B on the Bay, the name of a place; a period ends the first sentence; capital H on Harriet; capital B on Baltimore (a city). Quietly and anxiously are adverbs that tell how."),
 "scholar": {"journal-q1": "… and name one person Harriet goes back for in Chapter 10.",
             "journal-q2": "… and add a second effect that came from the first one.",
             "journal-q3": "… and explain where Harriet first sang the question in the title, back in Chapter 3."},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": False, "count": 1}},
 "hints": {"fill1": hint("When you say your feelings out loud, you push them out of you. Which root means push?", "press means push: ex + press = push out."),
           "fill2": hint("Pressing a stamp into wax leaves a mark. Which root means push?", "press means push: im + press = push in, leave a mark."),
           "fill3": hint("A box keeps everything together inside it. Which root means hold?", "tain means hold: con + tain = hold together."),
           "fill4": hint("If you keep something and won’t let it go, which root means hold?", "tain means hold: re + tain = hold back, keep.")},
 "copia": {"seed": "Harriet <b data-verb>led</b> her people north.",
           "eg": ["Through the snow on Christmas Eve, Harriet led her people north.", "Harriet <i>guided</i> her people north.",
                  "Harriet led her people north, from the swamp to John Hunn’s kitchen."]},
 "notes": {"wgrd": "In history, things happen for reasons. Name the event, look back for what made it happen, and say it with because: Harriet did this because …",
           "vocab": VOCAB, "wordParts": PARTS,
           "grammar": "An adverb tells more about a verb: how, when, or where. Many end in -ly, like slowly. Some don’t, like again and outside.",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Because …", "intro": "Pick one trip in Ch. 10. Write what made it happen, and what happened because of it.",
                      "fields": [{"label": "The cause", "hint": "", "rows": 2}, {"label": "The effect", "hint": "", "rows": 2}],
                      "layout": "row", "end": {"label": "Say it with because", "hint": "Harriet … because …"}}, "useAt": ["journal-q1", "journal-q2"]},
 "counters": {"journal-q1": 24, "journal-q2": 24, "journal-q3": 16},
 "wordgame": quilt("The first four patches"),
}
L[2] = {
 "connector": "Chapter 10 ended with forty people free and Harriet saying, “My people must go free.” In Chapter 11 she goes back for her brothers, who are about to be sold south. In Chapter 12 the people in danger are her old parents. Follow the chain: each problem, what Harriet does about it, and what that makes possible.",
 "writingFocus": "Organize + Draft",
 "dol": dol("she moved swiftly through the night her parents traveled slowly behind her",
            B("She") + " moved swiftly through the night" + B(".") + " " + B("Her") + " parents traveled slowly behind her" + B("."),
            "Capital S starts the sentence; a period ends the first sentence; capital H starts the second. Swiftly and slowly are adverbs that tell how.",
            "old rit sang bravely at the jail ben listened closely to her song",
            B("Old Rit") + " sang bravely at the jail" + B(".") + " " + B("Ben") + " listened closely to her song" + B("."),
            "Capital O and R on Old Rit (a name); a period ends the first sentence; capital B on Ben (a name). Bravely and closely are adverbs that tell how."),
 "scholar": {"journal-q4": "… and add one more link to the chain.",
             "journal-q1": "… and name the people who helped her do it.",
             "journal-q2": "… and use one thing Harriet says in Chapter 12.",
             "journal-q3": "… and name one thing about her that has not changed at all."},
 "flags": {"journal-q4": {"quote": False, "count": 3}, "journal-q1": {"quote": False, "count": 2},
           "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "hints": {"fill1": hint("Squeeze a sponge with both hands. Which root means push?", "press means push: com + press = push together."),
           "fill2": hint("A cruel ruler pushes his people down hard. Which root means push?", "press means push: op + press = push down hard."),
           "fill3": hint("When you finally reach a goal, you get hold of it. Which root means hold?", "tain means hold: at + tain = reach, get hold of."),
           "fill4": hint("The police can keep a person from leaving. Which root means hold?", "tain means hold: de + tain = hold back.")},
 "notes": {"wgrd": "One cause leads to an effect, and that effect can cause something else. Follow the whole chain, link by link, and say ‘so then’ between each one.",
           "vocab": VOCAB, "wordParts": PARTS,
           "grammar": "An adverb works with a verb. Find the verb first, then ask how, when, or where it happened.",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "The chain", "intro": "As you read Ch. 11 and 12, write the links in order.",
                      "fields": [{"label": "The problem", "hint": "", "rows": 2}, {"label": "What Harriet does", "hint": "", "rows": 2},
                                 {"label": "What that leads to", "hint": "", "rows": 2}],
                      "layout": "row", "end": {"label": "The link that holds the chain together", "hint": ""}}, "useAt": ["journal-q4", "journal-q1"]},
 "counters": {"journal-q4": 24, "journal-q1": 16, "journal-q2": 16, "journal-q3": 24},
 "wordgame": quilt("The quilt grows"),
 "ft": {"songsIntro": "In Chapter 12, Old Ben is in jail, and the sheriff never leaves him alone. Harriet has come to get him out, and he has to be ready. So Harriet tells Old Rit how to carry the message, and Old Rit sings.",
        "songs": [
          {"title": "Good News, the Chariot’s Coming",
           "lines": ["Good news, the chariot’s coming,", "Good news, the chariot’s coming,", "Good news, the chariot’s coming,", "An’ I don’t want it to leave me behind."],
           "heard": "A church song about the chariot that carries people home to heaven. The sheriff hears an old woman singing a hymn.",
           "meant": "Harriet is here, and she has come to take Ben out. He understands and mouths one word: When?",
           "q": "The sheriff is standing right there. Why does Old Rit sing the message instead of saying it?",
           "a": "Saying it would give the plan away. A hymn was safe to sing, and Ben knew how to listen to it."},
          {"title": "Lovely Fan",
           "lines": ["Then lovely Fan, will you come out tonight?", "Will you come out tonight?", "Will you come out tonight?", "Then lovely Fan, will you come out tonight,", "An’ dance by the light of the moon?"],
           "heard": "A silly old dance song, sung as the sheriff shoves Old Rit out the door.",
           "meant": "Tonight. Be ready to come out tonight.",
           "q": "Ben asked “When?” and there was no time to answer. How does this song answer him?",
           "a": "Its words ask someone to come out tonight. That tells Ben the escape is tonight."}]},
}
L[3] = {
 "connector": "Harriet has brought her brothers and her parents out of Maryland. But in 1850 Congress passes a new law, and runaways living in the North can be caught and sent back. As you read Chapter 13, test each link: did the law cause what happens next, or did it only come first?",
 "writingFocus": "Organize + Draft",
 "dol": dol("harriet traveled secretly each night her route stretched far across many states",
            B("Harriet") + " traveled secretly each night" + B(".") + " " + B("Her") + " route stretched far across many states" + B("."),
            "Capital H on Harriet; a period ends the first sentence; capital H starts the second. Secretly tells how she traveled; far tells where the route stretched.",
            "the train rolled slowly over the bridge the people shouted joyfully in canada",
            B("The") + " train rolled slowly over the bridge" + B(".") + " " + B("The") + " people shouted joyfully in " + B("Canada") + B("."),
            "Capital T starts each sentence; a period ends the first; capital C on Canada (a country). Slowly and joyfully are adverbs that tell how."),
 "scholar": {"journal-q1": "… and explain why Philadelphia was no longer the end of the line.",
             "journal-q2": "… and quote the words the runaways shout when they cross.",
             "journal-q3": "… and name one thing in the chapter that only came next, not because of the law."},
 "flags": {"journal-q1": {"quote": False, "count": 1}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "hints": {"fill1": hint("Pushing a button down. Which root means push?", "press means push: de + press = push down."),
           "fill2": hint("Holding in a sneeze pushes it under. Which root means push?", "press means push: sup + press = push under, hide."),
           "fill3": hint("Keeping a garden in good shape means holding it steady. Which root means hold?", "tain means hold: main + tain = hold steady."),
           "fill4": hint("To get something, you take hold of it. Which root means hold?", "tain means hold: ob + tain = take hold of."),
           "g4w22cf1": hint("How did the family talk so the neighbors would not hear? Look at the word bank.", "quietly tells how they spoke."),
           "g4w22cf2": hint("Which word in the bank tells when, all at once, with no warning?", "Suddenly tells when the dogs began to bark."),
           "g4w22cf3": hint("How would you fold and hide a paper so nobody noticed?", "carefully tells how she folded and hid it."),
           "g4w22cf4": hint("How many times did they use the same route? Look for a word that means not once.", "never tells how often: not even once."),
           "s4w22cf1": hint("create ends in a silent e. What happens to the e before -ive?", "Drop the silent e: create + ive = creative."),
           "s4w22cf2": hint("practice ends in a silent e too. Keep the c, drop the e, add -al.", "practice drops its e: practical."),
           "s4w22cf3": hint("history ends in y. The y drops before -ic.", "history drops its y: historic."),
           "s4w22cf4": hint("nation already ends in a consonant. Does anything drop?", "Nothing drops: nation + al = national.")},
 "notes": {"wgrd": "Not everything that comes next was caused by what came before. Line up two events and try ‘because’ between them. If it doesn’t hold up, it only came next.",
           "vocab": VOCAB, "wordParts": PARTS,
           "grammar": "Two adverbs propping up a weak verb can often become one strong verb. A strong verb shows how without the extra words.",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Cause, or only next?", "intro": "Pick two events from Ch. 13, an earlier one and a later one. Test them.",
                      "fields": [{"label": "Earlier event", "hint": "", "rows": 2}, {"label": "Later event", "hint": "", "rows": 2}],
                      "layout": "row", "end": {"label": "Cause, or only next? Why?", "hint": ""}}, "useAt": ["journal-q3"]},
 "counters": {"journal-q1": 16, "journal-q2": 16, "journal-q3": 24},
 "wordgame": quilt("Four more patches"),
}
L[4] = {
 "connector": "By Chapter 13, Harriet was leading people all the way to Canada, and still going back for more. In Chapter 14 the enslaved people begin calling her by a new name. As you read, list every reason that name fits, and decide which one matters most.",
 "writingFocus": "Organize + Draft",
 "dol": dol("everyone said she led them faithfully the song called her moses gently",
            B("Everyone") + " said she led them faithfully" + B(".") + " " + B("The") + " song called her " + B("Moses") + " gently" + B("."),
            "Capital E starts the sentence; a period ends the first sentence; capital T starts the second; capital M on Moses (a name). Faithfully and gently are adverbs that tell how.",
            "harriet planned each trip carefully she never acted recklessly",
            B("Harriet") + " planned each trip carefully" + B(".") + " " + B("She") + " never acted recklessly" + B("."),
            "Capital H on Harriet; a period ends the first sentence; capital S starts the second. Carefully and recklessly tell how; never tells how often."),
 "scholar": {"journal-q1": "… and name the reason you think matters most.",
             "journal-q2": "… and quote Harriet’s own words.",
             "journal-q3": "… and compare how the slaveowners see her with how the enslaved people see her."},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "hints": {"fill1": hint("Pushing back a laugh in a quiet room. Which root means push?", "press means push: re + press = push back, hold in."),
           "fill2": hint("Saying what you think pushes it out into words. Which root means push?", "press means push: ex + press = push out."),
           "fill3": hint("Food holds you up through a long day. Which root means hold?", "tain means hold: sus + tain = hold up, keep going."),
           "fill4": hint("To get something, you take hold of it. Which root means hold?", "tain means hold: ob + tain = take hold of.")},
 "notes": {"wgrd": "When many causes lead to one result, list them all. Take each one away and ask if the result still happens. The one it can’t do without matters most.",
           "vocab": VOCAB, "wordParts": PARTS,
           "grammar": "Cut adverbs that do no work. If a sentence says the same thing without the extra word, leave it out, or choose a stronger verb.",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Why Moses?", "intro": "As you read Ch. 14, list every reason the name fits.",
                      "fields": [{"label": "Reasons", "hint": "1. …", "rows": 5}],
                      "end": {"label": "The reason that matters most, and why", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 24, "journal-q2": 16, "journal-q3": 24},
 "wordgame": quilt("The last four patches"),
}

# Marcus scripts: welcome, before you read, one Word Study film clip (oao-audio-budget: 950 a lesson)
T = {
 1: {"welcome": "Hey, it’s Marcus. Last time, Harriet stood in Philadelphia, free, and said she would go back for her people. Chapter 10 is called Why Not Every Man? It comes from a song she sang in the fields as a girl. Today’s question: once you’re free, what do you owe the people still waiting?",
     "read": "Chapter 10 moves fast, one trip after another. Keep a list: who Harriet brings out each time, and what goes wrong. Watch a cold river, a door that should open and doesn’t, and a man talking to himself near a swamp. Ask what made each trip happen.",
     "morphology": "New roots this week. One means push. One means hold. Think of a printing press pushing ink onto paper, or a jar that holds jam. Every word in the quilt is pushing something or holding something. Ask which one, then sew."},
 2: {"welcome": "Hey, it’s Marcus. Two chapters today, and both are about Harriet’s own family. First her brothers, who are about to be sold. Then her mother and father, who are too old to walk north. Today’s question: what does Harriet do when the usual road to freedom won’t work?",
     "read": "Track the chain as you read: a problem, what Harriet does, and what that leads to. Watch a letter that makes no sense to the postmaster, and a pair of chickens. In Chapter 12, listen to what Old Rit sings at the jail. On my tours, that part always got a laugh.",
     "spelling": "These endings turn a word into a describing word. Here’s the tricky part. Some starting words end in a silent e, and that e drops off before the ending. Some lose nothing at all. So don’t trust your ears. Look hard at the starting word, then build."},
 3: {"welcome": "Hey, it’s Marcus. In 1850, Congress passed a new law, and suddenly the North wasn’t safe for anyone who had run away. Chapter 13 is called The Lion’s Paw. Hold that title in your head. Today’s question: if freedom keeps moving farther away, how far will Harriet go?",
     "read": "This chapter starts big, with a law, then zooms in on Harriet’s people. Follow the route north in your head, all the way across New York. Watch for friends along the way, and a train ride over roaring water. And look for Josiah Bailey. He’s my favorite person in this book.",
     "grammar": "Here’s a writer’s trick. When a sentence needs two little helper words to show how someone moved, the verb underneath is usually too weak. Swap in one strong verb, and the helpers can go. Say both versions out loud. Which one sounds like someone sneaking past a guard?"},
 4: {"welcome": "Hey, it’s Marcus. Harriet has gone back into Maryland again and again, and people start calling her by a new name. Chapter 14 is called Moses. On my walking tours, this was the chapter kids asked about most. Today’s question: why that name, and what does it say about how people see her?",
     "read": "As you read, list every reason people might call Harriet Moses. There are more than you’d think. Watch her disguises and her signals, and the posters that describe her. Then rank your reasons. Which one would the name fall apart without?",
     "grammar": "Last day with adverbs, and today you’re the editor. Some little words sound like they add a lot, but say nothing at all. Read each sentence without the extra word. If nothing is lost, cut it. If the verb feels weak, find a stronger one."},
}
WS = {1: ("morphology", "the word game"), 2: ("spelling", "the spelling move"), 3: ("grammar", "one strong verb"), 4: ("grammar", "the editor’s cut")}

V = {
 1: {"kind": "line", "title": "Why isn’t it enough?", "intro": "In Chapter 10, Harriet is free, but she keeps going back into Maryland: for her sister Mary Ann, her brother James, and William Henry. In two years she leads forty people out. She tells William Still, “My people must go free.”",
     "line": "Write one sentence: Why isn’t Harriet’s own freedom enough for her?", "placeholder": "Harriet’s freedom isn’t enough because…"},
 2: {"kind": "sort", "title": "Helping someone get free?", "yes": "Helping someone get free", "no": "Not this time",
     "intro": "In Chapters 11 and 12, many people help, in big ways and small ones. Read each moment. Tap Helping someone get free or Not this time.",
     "items": [{"t": "Harriet lets her chickens loose and chases them, so John Stewart won’t see her face.", "ok": True, "why": "Her trick keeps her hidden, so the rescue can go on."},
               {"t": "Ben brings food to the fodder house with a handkerchief over his eyes, so he can say he never saw his children.", "ok": True, "why": "He feeds them and protects them, without telling a lie."},
               {"t": "Old Rit and Ben fatten a pig all summer for a Christmas dinner.", "ok": False, "why": "That is love for their sons, but it is not part of the escape."},
               {"t": "Jacob Jackson gives up his only horse so Ben and Old Rit can ride.", "ok": True, "why": "He gives the thing he worked years for, so they can get away."},
               {"t": "The sheriff tells his wife that Ben laughs as if he’d come into a fortune.", "ok": False, "why": "The sheriff doesn’t understand what is happening at all."}]},
 3: {"kind": "log", "title": "Freedom log", "intro": "In Chapter 13, freedom means getting all the way to Canada. Tap the moment you think shows freedom best.",
     "options": [{"t": "The train crosses the bridge at Niagara Falls, and the runaways shout, “We’re free! We’ve shook the lion’s paw!”"},
                 {"t": "In the first hard winter in St. Catharines, Harriet chops wood, cooks, and nurses her people."},
                 {"t": "Harriet’s brothers own land, vote, and send their children to school in St. Catharines."},
                 {"t": "Josiah Bailey stands up on the train and sings, “One more soul got safe.”"}],
     "line": "Finish the sentence: This moment shows freedom because…", "placeholder": "This moment shows freedom because…"},
 4: {"kind": "meter", "title": "The freedom meter", "intro": "Think about one part of Chapter 14.",
     "moment": "Slaveowners put up posters and offer bigger and bigger rewards, until Harriet is worth $40,000 to anyone who catches her. She keeps going back until she has led more than three hundred people out.",
     "ask": "How much did the rewards change what Harriet did? Slide to show.", "line": "Tell why in one sentence.",
     "placeholder": "The rewards changed Harriet this much because…",
     "take": "One way to see it: not at all. Sterling writes, “Fearless, she was never reckless.”"},
}

for d in L:
    ws, lab = WS[d]
    L[d]["media"] = media(d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    v = V[d]; v.update(kicker=K, icon=I, name="freedom"); L[d]["virtue"] = v
    io.open('data/lesson-22-%d.json' % d, 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
budget = 950
for d in T:
    used = sum(len(t) for t in T[d].values())
    print('22.%d' % d, {k: len(t) for k, t in T[d].items()}, 'plain chars', used, '/', budget)
