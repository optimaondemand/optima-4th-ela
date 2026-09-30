# Week 9 supply list — what you still owe

Lessons 9.1–9.4 are built, committed and pass the sweep. They work right now without anything below: each clip and plate appears on its own the moment its file is in the right folder. Nothing needs rebuilding.

All paths are inside `C:\repos\optima-4th-ela`.

## At a glance

| Lesson | Guide | Plate | Clips | Scripts |
|---|---|---|---|---|
| 9.1 (Ch. 11) | Marilla | ✗ need `anne-ch11.png` | 15 (copia) | `Planning docs\g4-scripts-marilla-9-1.md` |
| 9.2 (Ch. 12–13) | Diana — **new voice** | ✗ need `anne-ch12-13.png` | 15 (rwm) | `Planning docs\g4-scripts-diana-9-2.md` |
| 9.3 (Ch. 14) | Anne | ✗ need `anne-ch14.png` | 15 (rwm) | `Planning docs\g4-scripts-anne-9-3.md` |
| 9.4 (Ch. 15) | Gilbert — **new voice** | ✗ need `anne-ch15.png` | 14 | `Planning docs\g4-scripts-gilbert-9-4.md` |

**59 audio clips and four plates.** Copia is on 9.1 only. RWM is on 9.2 and 9.3. 9.4 has neither. No poetry clips anywhere (the shipped By Heart card covers days 2 and 4).

## Where the files go

- **Audio:** `assets\audio\guide\<folder>\<filename>.mp3` — folders `marilla`, `diana`, `anne`, `gilbert`
- **Video (optional):** the same filename as `.mp4` in `assets\video\guide\<folder>\`. A `.jpg` with the same name is its thumbnail.
- **Plates:** `assets\plates\<filename>.png`
- Each file stays hidden until it exists. If both an mp3 and an mp4 exist, both show. A misspelled name shows no error; the clip just never appears, so copy the names exactly. The manifests for the rename helper are in `tools\guide-manifest-<folder>-9-<d>.csv`.

## Two new voices to pick

- **Diana (folder `diana`).** A girl of about eleven, bright, loyal, a little giggly. She laughs before she speaks, says *awfully* and *jolly*, and is easily delighted. Look for a young, light, warm girl's voice with a smile in it, quicker than Anne's will be, never breathy or babyish.
- **Gilbert (folder `gilbert`).** A boy of about thirteen, easy and teasing. Confident, quick, a grin in the voice, never mean. He says *awful* for *very* ("awful sorry") and *honest* for *honestly*. Look for a real boy's voice, not a man doing a boy, with a light, unhurried, good-humored delivery. In weeks 13–14 he needs to sound steadier, so pick a voice that can do both.

Settings for every voice: Eleven Multilingual v2 · Stability 55 · Similarity 75 · Style 0–10 · Speaker boost on.

## Clip filenames

### 9.1 — Marilla, folder `marilla`

welcome · wgrd · dol · guide1 · morphology · vocabulary · grammar · spelling · copia · guide2 · read · guide3 · chapter · wordconn · workshop

Each as `assets\audio\guide\marilla\g4ela-9-1-<slot>.mp3`

### 9.2 — Diana, folder `diana`

welcome · wgrd · dol · guide1 · morphology · vocabulary · grammar · spelling · guide2 · read · rwm · guide3 · chapter · wordconn · workshop

Each as `assets\audio\guide\diana\g4ela-9-2-<slot>.mp3`

### 9.3 — Anne, folder `anne` (the same Anne voice as 7.4)

welcome · dol · guide1 · morphology · vocabulary · grammar · spelling · guide2 · wgrd · read · rwm · guide3 · chapter · wordconn · workshop

Each as `assets\audio\guide\anne\g4ela-9-3-<slot>.mp3`

### 9.4 — Gilbert, folder `gilbert`

welcome · dol · guide1 · morphology · vocabulary · grammar · spelling · guide2 · wgrd · read · guide3 · chapter · wordconn · workshop

Each as `assets\audio\guide\gilbert\g4ela-9-4-<slot>.mp3`

## Plate prompts

Paste this house-style block in front of each prompt:

> Pen-and-ink line drawing with a light watercolor wash, in the manner of early-twentieth-century English children's book illustration — confident contour line, cross-hatching for shadow rather than solid black, color laid on thin and slightly outside the line the way a real wash sits on paper. Warm sepia-black ink, never pure black. Muted, aged palette: sage green, dusty rose, soft ochre, faded slate blue, with one restrained note of antique gold. No modern saturation, no gradients, no gloss, no drop shadow, no vector-flat shapes, no digital outline glow. Transparent background — the artwork must sit directly on cream paper with no card, box, frame, panel or backing color of any kind. Generous empty margin around the subject. No text, no lettering, no numerals, no signature. Nothing cropped at the edge.

### `anne-ch11.png`, lesson 9.1

The day's question is how the author shows desire and disappointment at once, and the quote strip now reads *"But I'd rather look ridiculous when everybody else does than plain and sensible all by myself."*

> A small, plain upstairs bedroom under a sloping gable roof, with one window letting in soft daylight. Three new dresses are spread out side by side on a narrow white bed: one snuff-brown gingham, one black-and-white check, one stiff dull blue, every one of them with tight, plain, narrow sleeves. A thin red-haired girl of eleven in a too-small dress stands at the foot of the bed with her hands clasped, looking down at them, her face caught between politeness and disappointment. A tall, thin, gray-haired woman in a dark dress stands in the doorway with her arms folded, waiting for thanks. Cool slate shadow in the corners, warm ochre light on the dresses. The sleeves are the point of the picture.

### `anne-ch12-13.png`, lesson 9.2

The day's question is how small actions show a friendship beginning, and the quote strip now reads *"I solemnly swear to be faithful to my bosom friend, Diana Barry, as long as the sun and moon shall endure."*

> A summer flower garden beside a farmhouse, full of old-fashioned blooms: roses, bleeding-heart, tiger lilies, sweet-peas along a fence. Two girls of eleven stand facing each other on a narrow dirt path between the flowerbeds and clasp hands across it, as solemnly as if the path were a stream. One is thin and red-haired in a too-small faded dress; the other is rosy and dark-haired with black eyes and a merry face, in a neat pink dress, half laughing. A ring of white birch trees shows in the distance beyond the fence. Sage green and dusty rose throughout, a note of antique gold in the sunlight on the path. Seen from slightly to one side, at the girls' own height.

### `anne-ch14.png`, lesson 9.3

The day's question is how one bad choice creates a bigger problem, and the quote strip now reads *"Marilla, I'm ready to confess."*

> The same small gable bedroom, but the door is shut and the window is open on a bright summer afternoon. A thin red-haired girl of eleven sits very upright on the edge of the narrow bed with her hands folded in her lap, looking at the closed door with an expression of tragic resolve. On the floor by the door, an untouched plate. Through the open window, far off, a tiny picnic is visible in a field by a lake: little figures, a white tablecloth, a wisp of smoke, none of it more than a few pen strokes. Warm ochre light spills across the floorboards toward her and stops short. The distance between the girl and the window is the picture.

### `anne-ch15.png`, lesson 9.4

The day's question is what inside Anne caused the slate to break on Gilbert's head, and the quote strip reads *"The iron has entered into my soul, Diana."*

> The inside of a one-room country schoolhouse, low in the eaves and wide in the windows, with rows of worn wooden double desks. In the middle of the room a thin red-haired girl of eleven has sprung to her feet, her face white with fury, holding a school slate that has just cracked clean in two. Across the aisle a tall boy with curly brown hair and a teasing grin, caught mid-laugh, one hand still half raised as if it had just let go of the end of her long red braid. Every other child in the room has turned to look. On the wall, a blank blackboard. Slate blue in the windows, warm ochre on the desks, one note of antique gold in the sun on the floorboards. Seen from the back of the room, over the heads of the other children.

## What I wrote rather than took from the page

Worth a look before students reach them:

- **Curriculum fixes (own commit, `7050883`).** The 14 slips from the drift list are fixed in the pre-sparkle markup: real DOL models on all four days (9.1's fix-it sentence changed to match: "anne sat on the bed looking sadly at the plain sleeves"), exact epigraphs, exact vocabulary sentences on 9.1, a Ch. 1–11 Growing-Up Watch on 9.1, "hat" for "brooch" in the 9.1 noun sort, Mrs. Barry not Mrs. Lynde on 9.2, a new 9.2 grammar spotter sentence (abstract nouns: friendship, happiness, hope), 9.3's grammar fill without the ridgepole or Josie Pye, a 9.3 vocab cloze that doesn't preview Ch. 15, 9.3 Pause labels in order, and "Week 9" on 9.4.
- **Second DOL sentence on each day.** Mine, in the same error pattern as the printed one. 9.3's ("Marilla packed bread, cookies, and a pie into the basket") and 9.4's ("Ouch!" Gilbert yelled) are practice sentences, not quotes.
- **Copia seed on 9.1** is Montgomery's exact sentence ("Anne clasped her hands and looked at the dresses"); the three worked examples are mine.
- **Hint ladders** (9.1 morphology; all 15 blanks on 9.3) and **miss lines** (9.1 vocabulary match and both sorts; 9.2 vocabulary match). Derived from the answers on the page.
- **Scholar clauses and evidence flags** for every chapter question.

## Notes

- The welcome clip only plays for a student who has a profile. The profile is made on day 1.
- The sweep's match/sort miss probes are pinned to week 7, so they print "(none)" here; I tested the week 9 miss lines with a separate script and they fire.
