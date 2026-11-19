#!/usr/bin/env python3
"""Writes data/lesson-24-1..4.json (week 24, Freedom Train Ch. 18-20 + the whole book). Moments and quotes checked in
Sterling (IA borrow, Nov 19 2026): Ch. 18 pp. 165-172, Ch. 19 pp. 173-181, Ch. 20 pp. 182-191.
The quilt only runs on the fill-in days (24.1, 24.3); 24.2 and 24.4 keep their match games."""
import json, io

V1 = [["fortifications", "Military defensive structures, like walls, forts, and trenches."],
      ["torpedoes", "Underwater explosive devices used to destroy ships."],
      ["expedition", "An organized journey for a special purpose."],
      ["proclamation", "An official public announcement by a government leader."],
      ["territory", "An area of land under the control of a group or government."]]
V2 = [["furlough", "An official leave of absence, especially for a soldier."],
      ["reproaches", "Expressions of blame or disapproval."],
      ["querulous", "Complaining; grumbling."],
      ["matron", "A woman in charge of a household or hospital."]]
V3 = [["centenarians", "People who are 100 years old or older."],
      ["pension", "Regular payments given to a veteran or retired person."],
      ["mortgage", "A loan used to buy property, paid back over time."],
      ["temperance", "The movement to reduce or ban alcohol."]]
SPELL = ("Four suffix rules, one year: double the last consonant after a short vowel (run → running), drop the silent e (hope → hoping), "
         "and change y to i (happy → happiest, carry → carried). Look at the end of the base word first.")
K = "Freedom Watch · after you read"; I = "⭐"
def quilt(h, meanings, why, win):
    return {"type": "quilt", "strand": "Morphology", "kicker": "Sew the Quilt", "h": h,
            "voice": "Tap a root, then the word it finishes. Or drag the root onto the word. Ask what each word is doing.",
            "why": {"icon": "🧵", "q": "Why a quilt?", "t": why}, "meanings": meanings,
            "winDay": "Four more patches are sewn in.", "win": win}
def media(d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/marcus/g4ela-24-%d-welcome" % d, "label": "Marcus’s welcome"},
         "read": {"kind": "audio", "path": "guide/marcus/g4ela-24-%d-read" % d, "label": "Marcus · before you read" if d < 4 else "Marcus · looking back"},
         ws: {"kind": "video", "path": "guide/marcus/g4ela-24-%d-%s" % (d, ws), "label": "Marcus · " + wslabel}}
    for off in ("guide1", "guide2", "guide3", "rwm", "copia"): m[off] = {"kind": ""}
    return m
def hint(h1, why): return {"h1": h1, "why": why}
def dol(raw, fixed, why, raw2, fixed2, why2):
    return {"a": {"raw": raw, "fixed": fixed, "why": why}, "b": {"raw": raw2, "fixed": fixed2, "why": why2}}
B = lambda s: "<strong>" + s + "</strong>"
G = "A prepositional phrase starts with a preposition (in, on, at, through, past, toward) and ends with a noun. It tells where, when, or how."

L = {}
L[1] = {
 "connector": "Chapter 17 ended on January 1, 1863, with Harriet saying, “This is the first day we have ever had a country.” Now the Union army can fight for freedom out loud. In Chapter 18, General Hunter sends Harriet behind enemy lines. Collect the details Sterling chooses for the biggest night of her war.",
 "writingFocus": "Revise + Edit",
 "dol": dol("on a hot night in june three gunboats steamed up the combahee river",
            B("On") + " a hot night in " + B("June") + " three gunboats steamed up the " + B("Combahee River") + B("."),
            "Capital O starts the sentence; capital J on June (a month); capital C and R on Combahee River (the name of a river); a period ends it. On a hot night, in June, and up the Combahee River are prepositional phrases.",
            "harriet crept through the underbrush past a rebel sentry",
            B("Harriet") + " crept through the underbrush past a " + B("Rebel") + " sentry" + B("."),
            "Capital H on Harriet; capital R on Rebel, the way Sterling writes it; a period ends it. Through the underbrush and past a Rebel sentry are prepositional phrases that tell where."),
 "scholar": {"journal-q1": "… and quote what Harriet says about the penalty for spying.",
             "journal-q2": "… and explain which detail you would keep if you could keep only one.",
             "journal-q3": "… and tell what the freed people shouted at the end of each verse."},
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 3}, "journal-q3": {"quote": False, "count": 1}},
 "hints": {"fill1": hint("Trucks and ships carry things across. Which root means carry?", "port means carry: trans + port + ation = carrying across."),
           "fill2": hint("A volcano breaks open. Which root means break?", "rupt means break: e + rupt = break out."),
           "fill3": hint("Directions build up what you know. Which root means build?", "struct means build: in + struct + ions = directions that build knowledge."),
           "fill4": hint("To tell what will happen before it happens. Which root means say?", "dict means say: pre + dict = say before.")},
 "copia": {"seed": "Harriet <b data-verb>led</b> the gunboats up the river.",
           "eg": ["On a hot night in June, Harriet led the gunboats up the river.", "Harriet <i>guided</i> the gunboats up the river.",
                  "Harriet led the gunboats up the river, past the hidden torpedoes."]},
 "notes": {"wgrd": "Say the chapter’s big idea in one sentence. Collect three details: a number, a picture, a sound. Keep the ones that make your sentence clearer.",
           "vocab": V1, "wordParts": "port = carry, rupt = break, struct = build, dict = say: transport, erupt, instruct, predict.",
           "grammar": G, "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Details for the big idea", "intro": "As you read Ch. 18, catch the details.",
                      "fields": [{"label": "The chapter’s big idea, in one sentence", "hint": "", "rows": 2},
                                 {"label": "Three details: a number, a picture, a sound", "hint": "1. …", "rows": 4}],
                      "end": {"label": "The detail that makes my sentence clearest", "hint": ""}}, "useAt": ["journal-q2"]},
 "counters": {"journal-q1": 24, "journal-q2": 32, "journal-q3": 24},
 "wordgame": quilt("Year-end roots", {"port": "carry", "rupt": "break", "struct": "build", "dict": "say"},
                   "Harriet’s mother finished a patchwork quilt in Chapter 2, and all year the word-parts game has sewn patches like hers. This week it sews the last ones: four roots you met this year, <b>port</b> (carry), <b>rupt</b> (break), <b>struct</b> (build) and <b>dict</b> (say).",
                   "Four year-end patches are sewn in. <b>port</b> = carry, <b>rupt</b> = break, <b>struct</b> = build, <b>dict</b> = say."),
 "ft": {"songsIntro": "On the Combahee River, the rowboats can’t push off. Everyone wants to get aboard at once, and frightened hands hold on to the sides. Colonel Montgomery shouts, “Moses, you’ll have to give ’em a song.”",
        "songs": [
          {"title": "Come Along",
           "lines": ["Of all the whole creation in the East or in the West,", "The glorious Yankee nation is the greatest and the best.", "Come along! Come along! Don’t be alarmed.", "Uncle Sam is rich enough to give you all a farm."],
           "source": "Harriet’s song on the Combahee, as Sterling gives it (Ch. 18, p. 172)",
           "heardBy": "What the crowd heard",
           "heard": "A bright, joking song about the Union and Uncle Sam, the nickname for the United States.",
           "meant": "Don’t be afraid. You are welcome, and there is room for you. At the end of each verse the people threw up their hands and shouted, “Glory!”",
           "q": "Why did Colonel Montgomery ask Harriet for a song?",
           "a": "When the people let go of the boats to throw up their hands and shout “Glory!”, the rowers could push off. Load after load, almost eight hundred people got aboard."}]},
}
L[2] = {
 "connector": "Chapter 18 ended with almost eight hundred people aboard the “Lincoln boats.” In Chapter 19 the war really ends. As you read, sort the details: some show the victory is real, and some show it is not finished yet.",
 "writingFocus": "Revise + Edit",
 "dol": dol("harriet traveled to washington in february of 1865",
            B("Harriet") + " traveled to " + B("Washington") + " in " + B("February") + " of 1865" + B("."),
            "Capital H on Harriet; capital W on Washington (a city); capital F on February (a month); a period ends it. To Washington, in February, and of 1865 are prepositional phrases.",
            "three passengers dragged harriet down the aisle into the baggage car",
            B("Three") + " passengers dragged " + B("Harriet") + " down the aisle into the baggage car" + B("."),
            "Capital T starts the sentence; capital H on Harriet; a period ends it. Down the aisle and into the baggage car are prepositional phrases that tell where."),
 "scholar": {"journal-q1": "… and quote what Old Rit or Ben says about pay.",
             "journal-q2": "… and tell what the Surgeon General appoints her to be.",
             "journal-q3": "… and explain why Sterling ends the chapter right here."},
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "notes": {"wgrd": "Write the chapter’s big idea at the top. List five details. Keep only the ones that point back at your sentence.",
           "vocab": V2, "wordParts": "vict = conquer, liber = free, port = carry, matr = mother: victory, liberty, transport, matron.",
           "grammar": G + " Find the first word, then the noun that closes the phrase.", "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Two piles", "intro": "Sort the details as you read Ch. 19.",
                      "fields": [{"label": "The victory is real", "hint": "", "rows": 3}, {"label": "The victory is not finished", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "Which pile the last scene belongs in, and why", "hint": ""}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 32, "journal-q2": 24, "journal-q3": 32},
}
L[3] = {
 "connector": "Chapter 19 ended with Harriet hurt in a baggage car, on her way home from the war she helped win. In Chapter 20 she goes home to Auburn and lives for almost fifty more years. Pick one detail and build the bridge: this detail shows ___ about Harriet, because ___.",
 "writingFocus": "Revise + Edit",
 "dol": dol("harriet sold vegetables from door to door in auburn",
            B("Harriet") + " sold vegetables from door to door in " + B("Auburn") + B("."),
            "Capital H on Harriet; capital A on Auburn (a city); a period ends it. From door, to door, and in Auburn are prepositional phrases.",
            "a package from england came to the house on south street",
            B("A") + " package from " + B("England") + " came to the house on " + B("South Street") + B("."),
            "Capital A starts the sentence; capital E on England (a country); capital S on South Street (the name of a street); a period ends it. From England, to the house, and on South Street are prepositional phrases."),
 "scholar": {"journal-q1": "… and name the people she took into her home.",
             "journal-q2": "… and explain where the twelve hundred dollars from Mrs. Bradford’s book went.",
             "journal-q3": "… and quote the message she sent to the women working for the vote."},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 2}, "journal-q3": {"quote": True, "count": 2}},
 "hints": {"fill1": hint("To pay someone back for what they lost. Which root means pay or weigh out?", "pens means pay: com + pens + ate = pay back."),
           "fill2": hint("Someone who trusts in herself. Which root means trust?", "fid means trust: con + fid + ent = trusting in yourself."),
           "fill3": hint("To pick the best ones out of a group. Which root means choose?", "lect means choose: se + lect = choose apart, pick carefully."),
           "fill4": hint("Voters pick their leaders. Which root means choose?", "lect means choose: e + lect = choose by voting."),
           "g4w24cf1": hint("When did they start out? Which word in the bank tells the time ahead of sunrise?", "before tells when: before sunrise."),
           "g4w24cf2": hint("The papers were under the floorboards. Which bank word means under?", "beneath tells where: beneath the floorboards."),
           "g4w24cf3": hint("She walked in the direction of the light. Which bank word means in the direction of?", "toward tells where she walked: toward the lantern."),
           "g4w24cf4": hint("The wagon went from one side of the field to the other.", "across tells where: across the frozen field."),
           "s4w24cf1": hint("run has a short u and ends in one consonant.", "Double the n: running."),
           "s4w24cf2": hint("hope ends in a silent e.", "Drop the e: hoping."),
           "s4w24cf3": hint("happy ends in a consonant and y.", "Change y to i: happiest."),
           "s4w24cf4": hint("carry ends in a consonant and y.", "Change y to i: carried.")},
 "notes": {"wgrd": "A detail turns into evidence when you say how it proves your idea. Build the bridge: this detail shows ___ about Harriet, because ___.",
           "vocab": V3, "wordParts": "pens = pay or weigh out, fid = trust, lect = choose: pension, confident, select, elect.",
           "grammar": "Prepositional phrases add detail, but too many in one sentence bury the verb. Keep the ones the reader needs.",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Build the bridge", "intro": "Pick one detail from Ch. 20.",
                      "fields": [{"label": "One detail", "hint": "", "rows": 2}, {"label": "The bigger idea it serves", "hint": "", "rows": 2}],
                      "layout": "row", "end": {"label": "The bridge", "hint": "This detail shows … about Harriet, because …"}}, "useAt": ["journal-q1", "journal-q3"]},
 "counters": {"journal-q1": 32, "journal-q2": 32, "journal-q3": 32},
 "wordgame": quilt("The last patches", {"pens": "pay", "fid": "trust", "lect": "choose"},
                   "The last patches of the year. In Chapter 20, Harriet fights for years for a <b>pension</b>, and by the end of the century she is a legend in Auburn. <b>pens</b> means <i>pay</i>, <b>fid</b> means <i>trust</i>, and <b>lect</b> means <i>choose</i>.",
                   "The quilt is finished, and the North Star is stitched across its middle, the same star Harriet followed north. <b>pens</b> = pay, <b>fid</b> = trust, <b>lect</b> = choose."),
}
L[4] = {
 "connector": "You have read the whole biography, from a little girl asking Daddy Ben about the star “that never moves” to the last page, where the North Star shines again. Today, say in one sentence what the whole book is about, then test it against the beginning, the middle, and the end.",
 "writingFocus": "Conclusion",
 "plate": {"src": "plates/ft-ch1.png", "alt": "Daddy Ben points out the North Star to young Harriet outside a cabin in Maryland.",
           "credit": "From Chapter 1. The same star shines on the book’s last page."},
 "dol": dol("from her wheelchair harriet sang songs about the war",
            B("From") + " her wheelchair " + B("Harriet") + " sang songs about the war" + B("."),
            "Capital F starts the sentence; capital H on Harriet; a period ends it. From her wheelchair and about the war are prepositional phrases.",
            "at dusk the north star shone in the darkening sky",
            B("At") + " dusk the " + B("North Star") + " shone in the darkening sky" + B("."),
            "Capital A starts the sentence; capital N and S on North Star (the name of one star); a period ends it. At dusk and in the darkening sky are prepositional phrases."),
 "scholar": {"journal-q1": "… and use one detail from each part of the book: early, middle, and end.",
             "journal-q2": "… and name three different kinds of freedom from different chapters.",
             "journal-q3": "… and connect your moment to one other moment in the book."},
 "flags": {"journal-q1": {"quote": False, "count": 3}, "journal-q2": {"quote": False, "count": 3}, "journal-q3": {"quote": False, "count": 2}},
 "notes": {"wgrd": "Say the whole book’s idea in one sentence. Check the first pages and the last against it. Gather one detail from early, one from the middle, one from the end.",
           "vocab": V3, "wordParts": "pens = pay or weigh out, fid = trust, leg/lect = choose or gather: pension, confident, legend, elect.",
           "grammar": "Editing day. Cut the prepositional phrases the reader doesn’t need, then read it aloud. You should hear the verb again.",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Early, middle, end", "intro": "Look back across the whole book.",
                      "fields": [{"label": "The whole book in one sentence", "hint": "", "rows": 2},
                                 {"label": "A detail from early in the book", "hint": "", "rows": 2},
                                 {"label": "A detail from the middle", "hint": "", "rows": 2},
                                 {"label": "A detail from the end", "hint": "", "rows": 2}],
                      "end": {"label": "Does my sentence still fit? What would I change?", "hint": ""}}, "useAt": ["journal-q1", "journal-q2"]},
 "counters": {"journal-q1": 40, "journal-q2": 32, "journal-q3": 32},
}

T = {
 1: {"welcome": "Hey, it’s Marcus. Harriet is back in Union blue, and this time General Hunter needs her behind enemy lines. Chapter 18 is called Mr. Lincoln’s Army. It has the biggest night of her war. Today’s question: which details does Sterling choose to show you what that night meant?",
     "read": "Track the details. A twig snaps near a Rebel sentry. Nine scouts learn where the torpedoes hide. Then three gunboats go up the Combahee River, and you’ll count the picket posts with Harriet. Watch the riverbanks at the end. On my tours, people always laughed about the two pigs.",
     "morphology": "Last root review of the year. Port means carry. Rupt means break. Struct means build. Dict means say. They’ve been hiding in words all year. Ask what each word is doing: carrying, breaking, building, or saying. Then sew the patch."},
 2: {"welcome": "Hey, it’s Marcus. Chapter 19 is called Victory, and the war really does end. But Sterling doesn’t stop at the celebration. Today’s question: what does victory really mean, and who gets to have it?",
     "read": "Sort your details into two piles as you read: the victory is real, and the victory isn’t finished. Watch Harriet talk with her parents about pay, a hospital that needs cleaning, and a night in Washington the whole country remembers. Then read the train ride slowly. Decide which pile it goes in.",
     "grammar": "A prepositional phrase is a little package. It starts with a word like in, on, under, or through, and it ends with a noun. In the baggage car. Through the woods. Find the first word, then find the noun that closes the package."},
 3: {"welcome": "Hey, it’s Marcus. The war is over, and Harriet goes home to Auburn. Chapter 20 is called The Years of Peace. But you’ll see she never really learns to sit still. Today’s question: what does Harriet keep doing when nobody is watching anymore?",
     "read": "Pick one small detail as you read, something Harriet does, keeps, or says, and ask what bigger idea it proves. Watch for a package from England, a wheelchair, and a garden. Read the very last sentence slowly. Notice what Sterling puts in the sky.",
     "spelling": "Here’s the whole year in four words. Running: double the last letter after a short vowel. Hoping: drop the silent e. Happiest and carried: change y to i. Look at the end of the base word first. It tells you which rule fires."},
 4: {"welcome": "Hey, it’s Marcus. You finished Freedom Train. That’s a whole life, from a little girl asking about a star to a woman the whole country knew. Today’s question: what does Harriet’s life mean, taken all together?",
     "read": "Today you flip back, not forward. Find one moment from the beginning, one from the middle, and one from the end. Check that all three point to the same big idea. If they don’t, maybe your idea needs to grow. Then hold Chapter 1 and the last page side by side.",
     "grammar": "Last grammar job: the editor’s cut. Some sentences pile up so many little phrases that the action gets buried. Keep the ones the reader needs. Cut the rest. Then read it out loud. You should hear the verb again."},
}
WS = {1: ("morphology", "year-end roots"), 2: ("grammar", "little packages"), 3: ("spelling", "four rules"), 4: ("grammar", "the editor’s cut")}

V = {
 1: {"kind": "line", "title": "Never in a better cause", "intro": "In Chapter 18, General Hunter warns Harriet about the penalty for spying. She answers, “I’ve faced death before, sir. But never in a better cause.” Then she guides three gunboats up the Combahee, and almost eight hundred people climb aboard the “Lincoln boats.”",
     "line": "Write one sentence: Why is freedom worth that risk to Harriet?", "placeholder": "Freedom is worth it to Harriet because…"},
 2: {"kind": "sort", "title": "Real victory, or not yet?", "yes": "A real victory", "no": "Not finished yet",
     "intro": "In Chapter 19 the war ends, but not every moment feels like winning. Read each one. Tap A real victory or Not finished yet.",
     "items": [{"t": "Secretary Seward tells her, “This is your victory, Harriet. You fought for it long before the rest of us did.”", "ok": True, "why": "Someone powerful says out loud what Harriet has done."},
               {"t": "Black soldiers are first offered seven dollars a month. White soldiers get thirteen.", "ok": False, "why": "Unequal pay means the fight for fair treatment isn’t over."},
               {"t": "Congress passes a law giving Black soldiers the same pay as white soldiers, even for the months they fought without wages.", "ok": True, "why": "The soldiers who refused unequal pay finally win."},
               {"t": "Charleston falls, and Lee surrenders at Appomattox.", "ok": True, "why": "The Union wins the war that ended slavery."},
               {"t": "Three passengers throw Harriet into the baggage car, even with her War Department pass.", "ok": False, "why": "The war is won, but Black Americans are still not treated as equals."}]},
 3: {"kind": "log", "title": "Freedom log", "intro": "In Chapter 20, Harriet keeps working for freedom for the rest of her life. Tap the moment you think shows it best.",
     "options": [{"t": "She sells vegetables and chickens to support two freedmen’s schools in the South."},
                 {"t": "She speaks from the same platform as Elizabeth Cady Stanton and Susan B. Anthony for women’s rights."},
                 {"t": "She buys twenty-five acres to make a home for old people who have nowhere else to go."},
                 {"t": "From her bed, she sends a message to the women working for the vote: “stand together.”"}],
     "line": "Finish the sentence: This moment shows freedom because…", "placeholder": "This moment shows freedom because…"},
 4: {"kind": "meter", "title": "The freedom meter", "intro": "Think about the whole book.",
     "moment": "A little girl asks Daddy Ben about the star “that never moves.” Years later she crosses into Maryland nineteen times, guides the gunboats up the Combahee, and tells the women working for the vote to “stand together.” On the last page, the North Star is shining again.",
     "ask": "How much did Harriet change the world around her? Slide to show.", "line": "Tell why in one sentence.",
     "placeholder": "Harriet changed the world this much because…",
     "take": "One way to see it: when William Still told her to stay safe, she said, “I must go down, like Moses into Egypt, to lead them out.” She kept going down for the rest of her life."},
}

for d in L:
    ws, lab = WS[d]
    L[d]["media"] = media(d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    v = V[d]; v.update(kicker=K, icon=I, name="freedom"); L[d]["virtue"] = v
    io.open('data/lesson-24-%d.json' % d, 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
for d in T:
    print('24.%d' % d, {k: len(t) for k, t in T[d].items()}, 'plain chars', sum(len(t) for t in T[d].values()), '/ 950')
