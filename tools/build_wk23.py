#!/usr/bin/env python3
"""Writes data/lesson-23-1..4.json (week 23, Freedom Train Ch. 15-17). Moments and quotes checked in Sterling
(IA borrow, Nov 19 2026): Ch. 15 pp. 134-148, Ch. 16 pp. 149-157, Ch. 17 pp. 158-164."""
import json, io

VOCAB = [["elevate", "To lift up; to raise to a higher level."],
         ["resist", "To stand against; to refuse to give in."],
         ["persist", "To keep going; to refuse to stop."],
         ["abolitionist", "A person who worked to end (abolish) slavery."]]
PARTS = "lev means “lift” and sist means “stand”: elevate, lever, resist, persist."
SPELL = ("In a long word, one syllable gets the stress and is said loud and clear. A vowel in a quiet syllable often fades to a lazy "
         "“uh,” the schwa: ab·o·LI·tion. To spell it, find a related word where that syllable is stressed: a·BOL·ish.")
K = "Freedom Watch · after you read"; I = "⭐"
WHY_QUILT = ("At the end of Chapter 16, in the camp outside Beaufort, a woman pieces together an American flag from scraps of old clothing "
             "and says, “Our time is coming.” <b>lev</b> means <i>lift</i>, and <b>sist</b> means <i>stand</i>. Each right word sews one patch. "
             "Four each lesson, until the quilt is finished.")
def quilt(h):
    return {"type": "quilt", "strand": "Morphology", "kicker": "Sew the Quilt", "h": h,
            "voice": "Tap a root, then the word it finishes. Or drag the root onto the word. Ask what each word is about: lifting, or standing?",
            "why": {"icon": "🧵", "q": "Why a quilt?", "t": WHY_QUILT}, "meanings": {"lev": "lift", "sist": "stand"},
            "winDay": "Four more patches are sewn in. The next lesson’s words add more.",
            "win": "The quilt is finished, and a North Star is stitched across its middle. <b>lev</b> = lift, <b>sist</b> = stand."}
def media(d, ws, wslabel):
    m = {"welcome": {"kind": "audio", "path": "guide/marcus/g4ela-23-%d-welcome" % d, "label": "Marcus’s welcome"},
         "read": {"kind": "audio", "path": "guide/marcus/g4ela-23-%d-read" % d, "label": "Marcus · before you read"},
         ws: {"kind": "audio", "path": "guide/marcus/g4ela-23-%d-%s" % (d, ws), "label": "Marcus · " + wslabel}}
    for off in ("guide1", "guide2", "guide3", "rwm", "copia"): m[off] = {"kind": ""}
    return m
def hint(h1, why): return {"h1": h1, "why": why}
def dol(raw, fixed, why, raw2, fixed2, why2):
    return {"a": {"raw": raw, "fixed": fixed, "why": why}, "b": {"raw": raw2, "fixed": fixed2, "why": why2}}
B = lambda s: "<strong>" + s + "</strong>"
H12 = {"fill1": hint("An elevator lifts you up to a higher floor. Which root means lift?", "lev means lift: e + lev + ate = lift up."),
       "fill2": hint("A lever is a bar you push down to lift something heavy. Which root means lift?", "lev means lift: lev + er = a tool for lifting."),
       "fill3": hint("When you stand against something and won’t give in, which root means stand?", "sist means stand: re + sist = stand against."),
       "fill4": hint("To keep standing through hard times and never quit. Which root means stand?", "sist means stand: per + sist = stand through, keep going.")}
H34 = {"fill1": hint("Medicine can lift a pain away. Which root means lift?", "lev means lift: al + lev + iate = lift away, make lighter."),
       "fill2": hint("A magician seems to make someone rise into the air. Which root means lift?", "lev means lift: lev + itate = rise into the air."),
       "fill3": hint("If you stand firm and won’t back down, which root means stand?", "sist means stand: in + sist = stand firm on a point."),
       "fill4": hint("A helper stands with you. Which root means stand?", "sist means stand: as + sist = stand with, help.")}

L = {}
L[1] = {
 "connector": "Chapter 14 ended with nineteen trips and more than three hundred people led north. In Chapter 15, Harriet’s name spreads far past Maryland. As you read, notice the words Sterling chooses for Harriet, and the words other people use about her.",
 "writingFocus": "Elaborate w/ Facts",
 "dol": dol("harriet spoke more boldly than anyone expected the crowd cheered louder after every story",
            B("Harriet") + " spoke more boldly than anyone expected" + B(".") + " " + B("The") + " crowd cheered louder after every story" + B("."),
            "Capital H on Harriet; a period ends the first sentence; capital T starts the second. More boldly and louder are comparative adverbs: they compare how things were done.",
            "the crowd pushed harder than the police harriet held on more tightly than ever",
            B("The") + " crowd pushed harder than the police" + B(".") + " " + B("Harriet") + " held on more tightly than ever" + B("."),
            "Capital T starts the sentence; a period ends the first sentence; capital H on Harriet. Harder takes -er; more tightly uses more with an -ly adverb."),
 "scholar": {"journal-q1": "… and quote one thing John Brown says or writes about her.",
             "journal-q2": "… and explain why Sterling says Brown spoke of her ‘in masculine terms.’",
             "journal-q3": "… and compare a word the slaveowners use for Harriet with a word the abolitionists use."},
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": False, "count": 2}},
 "hints": H12,
 "copia": {"seed": "Harriet <b data-verb>told</b> her story to the crowd.",
           "eg": ["At a Fourth of July picnic in Framingham, Harriet told her story to the crowd.", "Harriet <i>shared</i> her story with the crowd.",
                  "Harriet told her story to the crowd, and they answered with cheers."]},
 "notes": {"wgrd": "An author’s feelings show in her word choice. Collect the words Sterling uses for Harriet. Is each one plain or admiring? Say how Sterling wants you to feel, and point to the word that told you.",
           "vocab": VOCAB, "wordParts": PARTS,
           "grammar": "A comparative adverb compares two actions: faster, more carefully. Short adverbs usually take -er. Most -ly adverbs take more.",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Sterling’s words", "intro": "As you read Ch. 15, catch the words.",
                      "fields": [{"label": "Words Sterling uses for Harriet", "hint": "", "rows": 3}, {"label": "Words other people use for her", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "How Sterling wants me to feel, and the word that told me", "hint": ""}}, "useAt": ["journal-q3"]},
 "counters": {"journal-q1": 24, "journal-q2": 24, "journal-q3": 24},
 "wordgame": quilt("The first four patches"),
}
L[2] = {
 "connector": "Chapter 15 ended with the Civil War beginning. Harriet watched soldiers march off singing “John Brown’s Body” and decided she would join the Union Army somehow. In Chapter 16 she sails south. Notice which moments Sterling gives whole pages to, and which get one line.",
 "writingFocus": "Elaborate w/ Facts",
 "dol": dol("the ship sailed slowly up the river harriet watched more closely than the lieutenant",
            B("The") + " ship sailed slowly up the river" + B(".") + " " + B("Harriet") + " watched more closely than the lieutenant" + B("."),
            "Capital T starts the sentence; a period ends the first sentence; capital H on Harriet. Slowly is a plain adverb; more closely compares how two people watched.",
            "general hunter paced faster as he talked harriet listened more carefully than ever",
            B("General Hunter") + " paced faster as he talked" + B(".") + " " + B("Harriet") + " listened more carefully than ever" + B("."),
            "Capital G and H on General Hunter (a title with a name); a period ends the first sentence; capital H on Harriet. Faster and more carefully are comparative adverbs."),
 "scholar": {"journal-q1": "… and tell which job Harriet seems to care about most.",
             "journal-q2": "… and use one thing the General says.",
             "journal-q3": "… and name one thing Sterling keeps short or leaves out."},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": True, "count": 1}, "journal-q3": {"quote": False, "count": 1}},
 "hints": H12,
 "notes": {"wgrd": "An author also shows her perspective by what she puts in and what she leaves out. The moments she spends whole pages on are the moments she thinks matter most.",
           "vocab": VOCAB, "wordParts": PARTS,
           "grammar": "A comparative adjective describes a noun (a faster horse). A comparative adverb describes a verb (the horse ran faster). Ask what each comparing word describes.",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Where the pages go", "intro": "As you read Ch. 16, sort the moments.",
                      "fields": [{"label": "Long parts (a page or more)", "hint": "", "rows": 3}, {"label": "Short parts (a line or two)", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "What the long parts tell me Sterling cares about", "hint": ""}}, "useAt": ["journal-q3"]},
 "counters": {"journal-q1": 24, "journal-q2": 24, "journal-q3": 16},
 "wordgame": quilt("The quilt grows"),
}
L[3] = {
 "connector": "In Chapter 16 you met General Hunter and the thousands of people who had escaped to Beaufort. Today you go back to one conversation: Harriet and the General, pages 152 to 155. Sort what anyone could check from what Sterling believes about it.",
 "writingFocus": "Elaborate w/ Facts",
 "dol": dol("the general laughed harder than harriet expected she grinned more widely at his answer",
            B("The") + " " + B("General") + " laughed harder than " + B("Harriet") + " expected" + B(".") + " " + B("She") + " grinned more widely at his answer" + B("."),
            "Capital T starts the sentence; capital G on General when it stands for one man’s title; capital H on Harriet; a period ends the first sentence; capital S starts the second. Harder and more widely compare.",
            "the children read more eagerly than ever the soldiers drilled more smartly each day",
            B("The") + " children read more eagerly than ever" + B(".") + " " + B("The") + " soldiers drilled more smartly each day" + B("."),
            "Capital T starts each sentence; a period ends the first. More eagerly and more smartly are comparative adverbs made with more."),
 "scholar": {"journal-q1": "… and name the governor whose letter Harriet carries.",
             "journal-q2": "… and tell who the doctor in the story stands for.",
             "journal-q3": "… and point to one fact and one judgment from the same page."},
 "flags": {"journal-q1": {"quote": False, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": True, "count": 1}},
 "hints": dict(H34, **{
           "g4w23cf1": hint("How did she walk compared with her brother? Quietly ends in -ly, so use more.", "more quietly compares how two people walked."),
           "g4w23cf2": hint("Soon is a short adverb. Add -er; don’t add more.", "sooner already compares. More sooner doubles it."),
           "g4w23cf3": hint("Hard is a short adverb. Add -er.", "harder compares how hard he worked with everyone else."),
           "g4w23cf4": hint("Of all of them means more than two. Use most, not more.", "most carefully compares her with the whole group."),
           "s4w23cf1": hint("Say abolish. Which vowel do you hear clearly after the b?", "abolish has a loud o, so abolition keeps the o."),
           "s4w23cf2": hint("Say cooperate. Which vowel do you hear after coop?", "cooperate has an e, so cooperation keeps the e."),
           "s4w23cf3": hint("Say define. Which vowel do you hear after the f?", "define has an i, so definition keeps the i."),
           "s4w23cf4": hint("Say separate. Which vowel do you hear after sep?", "separate has an a, so separation keeps the a.")}),
 "notes": {"wgrd": "A biography mixes facts anyone could check with the author’s judgments about them. Mark the dates, places, names, and numbers. Then mark the words that rate a person or a choice.",
           "vocab": VOCAB, "wordParts": PARTS,
           "grammar": "Never use more and -er together (more louder). And don’t use an adjective where you need an adverb: quicker should be more quickly.",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Fact or judgment?", "intro": "Pick one part of pages 152 to 155.",
                      "fields": [{"label": "A fact anyone could check", "hint": "", "rows": 2}, {"label": "Sterling’s judgment about it", "hint": "", "rows": 2}],
                      "layout": "row", "end": {"label": "Say it both ways", "hint": "The fact is … Sterling wants me to think …"}}, "useAt": ["journal-q3"]},
 "counters": {"journal-q1": 16, "journal-q2": 24, "journal-q3": 24},
 "wordgame": quilt("Four more patches"),
}
L[4] = {
 "connector": "Chapter 16 ended at a campfire, with a woman sewing a flag from scraps and saying, “Our time is coming.” In Chapter 17 those words come back again and again. Imagine a Union officer telling this chapter, and notice what Sterling keeps that he might leave out.",
 "writingFocus": "Elaborate w/ Facts",
 "dol": dol("the women sewed faster than before harriet baked pies more often for the soldiers",
            B("The") + " women sewed faster than before" + B(".") + " " + B("Harriet") + " baked pies more often for the soldiers" + B("."),
            "Capital T starts the sentence; a period ends the first sentence; capital H on Harriet. Faster and more often are comparative adverbs.",
            "on january 1 1863 the people sang louder than ever harriet spoke last",
            B("On January 1, 1863,") + " the people sang louder than ever" + B(".") + " " + B("Harriet") + " spoke last" + B("."),
            "Capital O starts the sentence; capital J on January; a comma after the day and after the year; a period ends the first sentence; capital H on Harriet. Louder compares; last tells when."),
 "scholar": {"journal-q1": "… and quote one thing Harriet said about the hospital.",
             "journal-q2": "… and explain what finally comes true at the end of the chapter.",
             "journal-q3": "… and quote the last thing Harriet says in the chapter."},
 "flags": {"journal-q1": {"quote": True, "count": 2}, "journal-q2": {"quote": False, "count": 1}, "journal-q3": {"quote": True, "count": 2}},
 "hints": H34,
 "notes": {"wgrd": "Imagine the same events told by someone else: a soldier, a nurse, an officer. Whatever that teller would change or leave out shows you the choices your author made.",
           "vocab": VOCAB, "wordParts": PARTS,
           "grammar": "Editing day. Leave correct comparisons alone. Fix the two mistakes: doubling up (more louder) and an adjective doing an adverb’s job (moved quicker).",
           "spelling": SPELL},
 "wgrd": {"catcher": {"title": "Another teller", "intro": "Pick one scene from Ch. 17.",
                      "fields": [{"label": "Who else could tell it", "hint": "", "rows": 2}, {"label": "What they would leave out or change", "hint": "", "rows": 3}],
                      "layout": "row", "end": {"label": "So Sterling’s perspective is …", "hint": ""}}, "useAt": ["journal-q3"]},
 "counters": {"journal-q1": 24, "journal-q2": 16, "journal-q3": 24},
 "wordgame": quilt("The last four patches"),
 "ft": {"songsIntro": "On January 1, 1863, a crowd gathers in a grove of live oaks outside Beaufort to hear Mr. Lincoln’s proclamation read aloud. Nobody cheers. Then one voice starts to sing, a voice “which had been heard before, on lonely paths in the woods under the North Star.”",
        "songs": [
          {"title": "My Country, ’Tis of Thee",
           "lines": ["My country, ’tis of thee,", "Sweet land of liberty,", "Of thee I sing.", "Land where my fathers died!", "Land of the Pilgrims’ pride!", "From every mountainside", "Let freedom ring!"],
           "source": "Words by Samuel Francis Smith, 1831 · public domain",
           "heardBy": "What the song usually meant",
           "heard": "A song about America that people sang on the Fourth of July. For most of the people in the grove, the “land of liberty” in the song had never included them.",
           "meant": "This morning, for the first time, the song could be theirs too. When the singing stops, Harriet says, “This is the first day we have ever had a country.”",
           "q": "Harriet sang this song on the day of the proclamation. Why might the words feel different to her that morning?",
           "a": "The country had kept her people enslaved. Now its President promised them freedom, so for the first time the song was about them too."}]},
}

T = {
 1: {"welcome": "Hey, it’s Marcus. Harriet has led more than three hundred people north, and now her name is spreading far past Maryland. Chapter 15 is called The Most of a Man. That’s something a famous man wrote about her. Today’s question: how does Sterling want you to see Harriet, and how can you tell?",
     "read": "As you read, listen to the words. Sterling never says, I admire her. She shows it in the words she picks. Watch a fight on the streets of Troy, a long talk over a map in Canada, and a song soldiers sing as they march off to war. Write down Sterling’s words for Harriet.",
     "morphology": "Two new roots. Lev means lift. Think of an elevator lifting you up. Sist means stand. When you resist, you stand against something. Every word today is lifting or standing. Ask which one, then sew the patch."},
 2: {"welcome": "Hey, it’s Marcus. The Civil War has started, and Harriet won’t sit it out. Chapter 16 takes her south to Beaufort, South Carolina, where thousands of people have just escaped to the Union army. Today’s question: what can Harriet do there that nobody else can?",
     "read": "Notice where Sterling spends her pages. Some moments get a whole page, and some get one line. Watch Harriet’s talk with General Hunter, and listen for a story about a snake. Then walk the camp at night with her. On my tours, people always ask about the book those kids were reading.",
     "grammar": "Faster can describe a horse, or it can describe how the horse runs. When it describes a thing, it’s an adjective. When it tells how someone did something, it’s an adverb. So don’t just spot the comparing words. Ask what each one is describing."},
 3: {"welcome": "Hey, it’s Marcus. Back to Chapter 16 today, and back to one conversation. Harriet tells a Union general what Mr. Lincoln is getting wrong, and she does it with a story. Today’s question: which parts of this chapter are facts, and which parts tell you what Sterling believes?",
     "read": "Read pages one fifty-two to one fifty-five slowly. Put the facts in one pile: names, places, numbers, the letter from Governor Andrew. Put the judgments in the other: words that rate a person or a choice. Then listen to the General’s letter to Congress. It’s funnier than you’d expect.",
     "spelling": "Here’s the trick for lazy vowels. In abolition, you can barely hear the o. So find a relative of the word where that part gets the stress. Abolish. Now the o is loud and clear. Say the relative, and the spelling shows itself."},
 4: {"welcome": "Hey, it’s Marcus. Chapter 17 is called Our Time Is Coming. Somebody says those words at the end of Chapter 16, and now Sterling keeps bringing them back. Today’s question: what does it feel like to be this close to something you’ve waited your whole life for?",
     "read": "Imagine a Union officer telling this chapter instead. What would he skip? Sterling keeps the small things: ice water in a basin, gingerbread for sale, herb tea for a fever ward. Then comes the first day of 1863. Listen to the very last thing Harriet says. It’s my favorite line in the whole book.",
     "grammar": "Editing day. Some comparing words are already right, so leave them alone. Look for two mistakes. One is doubling up, like more louder. The other is an adjective doing an adverb’s job, like moved quicker. Fix those, then read the sentence out loud to check."},
}
WS = {1: ("morphology", "the word game"), 2: ("grammar", "adjective or adverb?"), 3: ("spelling", "lazy vowels"), 4: ("grammar", "editing day")}

V = {
 1: {"kind": "line", "title": "Seen at last", "intro": "In Chapter 15, Harriet speaks at meetings across the North and helps a crowd free Charles Nalle in Troy. John Brown calls her General Tubman. To the slaveowners she is “deluded”; to the abolitionists she is “the greatest heroine of the age.”",
     "line": "Write one sentence: Why does it matter who sees Harriet clearly?", "placeholder": "It matters because…"},
 2: {"kind": "sort", "title": "Moving freedom forward?", "yes": "Moving freedom forward", "no": "Holding it back",
     "intro": "In Chapter 16, thousands of people have escaped to the Union army in Beaufort. Read each moment. Tap Moving freedom forward or Holding it back.",
     "items": [{"t": "Mr. Lincoln won’t let escaped slaves join the army. He is afraid of losing Maryland and Kentucky.", "ok": False, "why": "While he waits, the people in Beaufort are called contrabands of war, not free men."},
               {"t": "General Hunter forms the First South Carolina regiment from freed men.", "ok": True, "why": "Men who were enslaved now drill as soldiers, ready to fight for freedom."},
               {"t": "By the firelight, a woman slowly spells aloud, “Cat, bat, pat.”", "ok": True, "why": "Learning to read is a freedom slavery tried to keep from her."},
               {"t": "The soldiers are promised pay like the white soldiers, but the money never comes.", "ok": False, "why": "Without pay, a soldier with hungry children is only ‘half free.’"},
               {"t": "Harriet tells the General the war can’t be won by half measures.", "ok": True, "why": "She is pushing the Union to set the slaves free."}]},
 3: {"kind": "log", "title": "Freedom log", "intro": "In Chapter 16, people in Beaufort say, “We’s all free.” A soldier answers that they are not more than half free. Tap the moment that shows best what full freedom would take.",
     "options": [{"t": "The soldier says they need land to farm and a soldier’s pay before they are truly free."},
                 {"t": "Children learn to read from a soldiers’ handbook by the firelight."},
                 {"t": "A woman pieces together an American flag from scraps of old clothing."},
                 {"t": "General Hunter tells Congress his regiment is made of loyal persons whose masters ran away."}],
     "line": "Finish the sentence: This moment shows what freedom needs because…", "placeholder": "This moment shows what freedom needs because…"},
 4: {"kind": "meter", "title": "The freedom meter", "intro": "Think about the last pages of Chapter 17.",
     "moment": "On January 1, 1863, a doctor reads the President’s proclamation in a grove outside Beaufort. The crowd sings “My country, ’tis of thee.” Harriet says, “This is the first day we have ever had a country.”",
     "ask": "How free do the people in the grove feel that morning? Slide to show.", "line": "Tell why in one sentence.",
     "placeholder": "They feel this free because…",
     "take": "One way to see it: Harriet calls it the first flag “which promised us anything.” A promise is a beginning, not the end of the fight."},
}

for d in L:
    ws, lab = WS[d]
    L[d]["media"] = media(d, ws, lab)
    L[d]["transcripts"] = T[d]
    L[d]["navFixes"] = True
    L[d]["lens"] = True
    v = V[d]; v.update(kicker=K, icon=I, name="freedom"); L[d]["virtue"] = v
    io.open('data/lesson-23-%d.json' % d, 'w', encoding='utf-8').write(json.dumps(L[d], ensure_ascii=False, indent=1) + '\n')
budget = 950
for d in T:
    used = sum(len(t) for t in T[d].values())
    print('23.%d' % d, {k: len(t) for k, t in T[d].items()}, 'plain chars', used, '/', budget)
