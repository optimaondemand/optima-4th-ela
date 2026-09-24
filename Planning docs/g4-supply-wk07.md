# Week 7 supply list — what you still owe

Lessons 7.2, 7.3 and 7.4 are built and pass the sweep. **They work right now without anything below.** Each plate and clip appears on its own the moment the file is in the right folder. Nothing needs rebuilding.

All paths are inside `C:\repos\optima-4th-ela`.

## At a glance

| Lesson | Plate | Audio (scripts in `g4-scripts-wk07.md`) |
|---|---|---|
| 7.1 | ✓ have it | re-record `turn\g4ela-7-1-2.mp3` |
| 7.2 | `assets\plates\anne-ch2.png` | `welcome\g4ela-7-2.mp3`, `turn\g4ela-7-2-1.mp3`, `-2`, `-3` |
| 7.3 | `assets\plates\anne-ch3-4.png` | `welcome\g4ela-7-3.mp3`, `turn\g4ela-7-3-1.mp3`, `-2`, `-3` |
| 7.4 | `assets\plates\anne-ch5.png` | `welcome\g4ela-7-4.mp3`, `turn\g4ela-7-4-1.mp3`, `-2`, `-3` |

The audio folders are under `assets\audio\guide\`. Plates must be **.png**, and the filename must match exactly. A misspelled name doesn't show an error; the plate just never appears.

---

## Plate prompts

Paste this house-style block in front of each prompt:

> Pen-and-ink line drawing with a light watercolor wash, in the manner of early-twentieth-century English children's book illustration — confident contour line, cross-hatching for shadow rather than solid black, colour laid on thin and slightly outside the line the way a real wash sits on paper. Warm sepia-black ink, never pure black. Muted, aged palette: sage green, dusty rose, soft ochre, faded slate blue, with one restrained note of antique gold. No modern saturation, no gradients, no gloss, no drop shadow, no vector-flat shapes, no digital outline glow. Transparent background — the artwork must sit directly on cream paper with no card, box, frame, panel or backing colour of any kind. Generous empty margin around the subject. No text, no lettering, no numerals, no signature. Nothing cropped at the edge.

### `anne-ch2.png`, lesson 7.2

The day's question is what makes Anne's voice hers, and the quote strip reads *"They should call it—let me see—the White Way of Delight."*

> A thin red-haired girl of eleven in a short, tight yellowish-grey dress and a faded brown sailor hat, sitting beside a shy, stooped, grey-bearded farmer on the seat of an old-fashioned open buggy drawn by a sorrel mare. They are passing beneath a long arch of apple trees in full white blossom, in the last light of evening. The girl has her hands clasped and her face lifted toward the blossom, rapt, mid-word. The man glances sideways at her, quietly astonished. A few petals drift down. Seen from slightly behind and to one side, with the tunnel of blossom receding ahead of them. A worn carpet-bag at her feet.

### `anne-ch3-4.png`, lesson 7.3

The day's question is how an author shows feeling through what a character does, and the quote strip reads *"You don't want me because I'm not a boy!"*

> A plain farmhouse kitchen at night, lit by a single oil lamp on a scrubbed wooden table. A thin red-haired girl in a too-small dress has flung herself into a chair and thrown her arms across the table, her face buried in them. Her braids are spilling forward, and her faded sailor hat has fallen to the floor. A tall, thin, grey-haired woman in a dark dress, hair in a hard knot, stands stiffly beside the table, taken aback. In the doorway, half in shadow, a stooped grey-bearded man holds his hat, helpless. Warm lamplight on the girl, cool slate shadow around the edges. Everything about the girl's body says what she is feeling; nobody's face needs to.

### `anne-ch5.png`, lesson 7.4

The day's question is how Anne's past shapes who she is, and the quote strip reads *"It's been my experience that you can nearly always enjoy things if you make up your mind firmly that you will."*

> An open buggy on a narrow shore road running along low red sandstone cliffs above a calm blue sea, drawn by a sorrel mare. A stern, grey-haired woman in a dark dress holds the reins and looks straight ahead. Beside her, a thin red-haired girl in a too-small dress and a faded sailor hat sits very upright, hands folded in her lap, talking earnestly with her eyes on the sea. Her face is thoughtful, not sad. Wild roses along the roadside, a few gulls, and a small sandy cove below. Seen from slightly above, with the long curve of the road and the sea opening out ahead of them.

---

## Things I wrote that you should check

This is everything in the lesson data that isn't taken straight from the page or the novel.

**7.2**
- **DOL:** second sentence "oh im going to love it here anne whispered" is mine.
- **Copia examples:** "past snug farmsteads" is Montgomery's; "blossoming orchards" is mine.
- **Vocabulary miss lines:** mine. The *companion* line uses the "shares your bread" root that the morphology card already teaches.
- **Coaching on Q2:** the question asks for three details, but the layer's coaching line says "This question asks for two details." That wording lives in `sparkle.js`, and I haven't changed it.

**7.3**
- **DOL:** second sentence "please dont send me away im trying to be good anne sobbed" is mine.
- **Copia examples:** the buggy in the yard, the lamplight and the kitchen door are my details. The seed sentence is Montgomery's.
- **Hint for the *placid* blank:** rewritten to fit the reworded sentence. The other 14 hints come from the answers on the page.

**7.4**
- **DOL:** second sentence "i think i will imagine something nicer said anne" is mine.
- **Copia verb swap:** the example uses *ventured* ("Marilla ventured no more questions"). It may be a stretch for some fourth graders; *risked* would be simpler.

---

## Curriculum fixes made this week

Each fix is its own commit, separate from the sparkle build, so either can be undone alone.

- **7.3** (`8950343`)
  - The Grammar and Spelling boxes asked about Chapter 5 a day early.
  - The vocabulary bank said *placid* while the answer was *placidly*.
- **7.2 and 7.4** (`8d14b85`)
  - Three quoted lines weren't in the novel: the quote strip, the DOL model and the RWM sentence on 7.2, and the quote strip and DOL model on 7.4. All now use real Ch. 2 and Ch. 5 lines.
  - 7.2's Grammar and Spelling sentences were labelled "Chapter 3" and described things not in the book.
  - 7.4 said "last day of Week 1".

**Not audited:** 7.1. I left it alone as asked.

## Not on this list

- **Poem recordings:** "Who Has Seen the Wind?" (`assets\audio\poem\who-has-seen-the-wind.mp3` and the `.mp4`) belongs to the By Heart card, which has its own supply list. The sweep lists these files as missing on 7.2 and 7.4, which is expected.
- **Optional recordings:** no section slots are on this week, so there are no extra recordings.
