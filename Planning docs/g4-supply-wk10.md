# Week 10 supply list — what you still owe

Lessons 10.1–10.4 are built and pass the sweep (uncommitted until you say). They work right now without anything below: each clip and plate appears on its own the moment its file is in the right folder. Nothing needs rebuilding.

All paths are inside `C:\repos\optima-4th-ela`.

## At a glance

| Lesson | Guide | Plate | Clips | Scripts |
|---|---|---|---|---|
| 10.1 (Ch. 16) | Diana | ✗ need `anne-ch16.png` | 15 (copia) | `Planning docs\g4-scripts-diana-10-1.md` |
| 10.2 (Ch. 17–18) | Matthew | ✗ need `anne-ch17-18.png` | 15 (rwm) | `Planning docs\g4-scripts-matthew-10-2.md` |
| 10.3 (Ch. 19) | Miss Josephine Barry — **new voice** | ✗ need `anne-ch19.png` | 15 (rwm) | `Planning docs\g4-scripts-josephine-10-3.md` |
| 10.4 (Ch. 20) | Marilla | ✗ need `anne-ch20.png` | 14 | `Planning docs\g4-scripts-marilla-10-4.md` |

**59 audio clips and four plates.** Copia is on 10.1 only. RWM is on 10.2 and 10.3. 10.4 has neither. No poetry clips anywhere (the shipped By Heart card covers days 2 and 4, and the printed Poetry Corner isn't what students see).

## Where the files go

- **Audio:** `assets\audio\guide\<folder>\<filename>.mp3` — folders `diana`, `matthew`, `josephine` (new), `marilla`
- **Video (optional):** the same filename as `.mp4` in `assets\video\guide\<folder>\`. A `.jpg` with the same name is its thumbnail.
- **Plates:** `assets\plates\<filename>.png`
- Each file stays hidden until it exists. If both an mp3 and an mp4 exist, both show. A misspelled name shows no error; the clip just never appears, so copy the names exactly. The manifests for the rename helper are `tools\guide-manifest-<folder>-10-<d>.csv`.

## One new voice to pick

**Miss Josephine Barry (folder `josephine`).** Diana's great-aunt from Charlottetown, "seventy anyhow," thin, prim and rigid, gold-rimmed glasses, a temper that "is no joke." Elderly, crisp, sharp-tongued, secretly amused, and won over by Anne against her will. She speaks in short, exact, dry sentences and pretends to be crosser than she is; the laugh is always just behind the door. Look for an older woman's voice with a clipped, precise delivery and a clear upper-class edge, no warble and no sweetness, that can drop into dryness on a single word. She should sound like someone who has never hurried in her life. Not Marilla: Marilla is brisk and rural and warm underneath; Miss Barry is slower, grander, and funnier, and knows it. She comes back in 12.3, so pick a voice you'll be happy to hear twice.

The other three are the voices you already have: Diana (9.2), Matthew (7.2, 8.4), Marilla (7.3, 8.1, 8.2, 9.1).

Settings for every voice: Eleven Multilingual v2 · Stability 55 · Similarity 75 · Style 0–10 · Speaker boost on.

## Clip filenames

### 10.1 — Diana, folder `diana`

welcome · wgrd · dol · guide1 · morphology · vocabulary · grammar · spelling · copia · guide2 · read · guide3 · chapter · wordconn · workshop

Each as `assets\audio\guide\diana\g4ela-10-1-<slot>.mp3`

### 10.2 — Matthew, folder `matthew`

welcome · wgrd · dol · guide1 · morphology · vocabulary · grammar · spelling · guide2 · read · rwm · guide3 · chapter · wordconn · workshop

Each as `assets\audio\guide\matthew\g4ela-10-2-<slot>.mp3`

### 10.3 — Miss Barry, folder `josephine`

welcome · dol · guide1 · morphology · vocabulary · grammar · spelling · guide2 · wgrd · read · rwm · guide3 · chapter · wordconn · workshop

Each as `assets\audio\guide\josephine\g4ela-10-3-<slot>.mp3`

### 10.4 — Marilla, folder `marilla`

welcome · dol · guide1 · morphology · vocabulary · grammar · spelling · guide2 · wgrd · read · guide3 · chapter · wordconn · workshop

Each as `assets\audio\guide\marilla\g4ela-10-4-<slot>.mp3`

## Plate prompts

Paste this house-style block in front of each prompt:

> Pen-and-ink line drawing with a light watercolor wash, in the manner of early-twentieth-century English children's book illustration — confident contour line, cross-hatching for shadow rather than solid black, colour laid on thin and slightly outside the line the way a real wash sits on paper. Warm sepia-black ink, never pure black. Muted, aged palette: sage green, dusty rose, soft ochre, faded slate blue, with one restrained note of antique gold. No modern saturation, no gradients, no gloss, no drop shadow, no vector-flat shapes, no digital outline glow. Transparent background — the artwork must sit directly on cream paper with no card, box, frame, panel or backing colour of any kind. Generous empty margin around the subject. No text, no lettering, no numerals, no signature. Nothing cropped at the edge.

### `anne-ch16.png`, lesson 10.1

The day's question is how an honest mistake becomes a real problem, and the quote strip (corrected) reads *"I love bright red drinks, don't you? They taste twice as good as any other colour."*

> A farmhouse sitting room on an October afternoon, plain and tidy, with a closed pantry door in the background and a small table in the middle of the room. On the table, a tray with a single tall glass tumbler of a bright red drink and a squat dark bottle beside it. A rosy, dark-haired girl of eleven in a neat second-best dress sits very upright on a stiff chair with her toes together, lifting the glass to admire its colour. A thin red-haired girl in a too-small dress is halfway out of the doorway toward the kitchen, looking back over her shoulder, all attention on being a good hostess. Autumn light, warm ochre through the window; sage in the walls; the one note of antique gold is the red drink catching the light. Seen from across the room at the girls' own height. The full glass is the point of the picture.

### `anne-ch17-18.png`, lesson 10.2

The day's question is how the thing that made Anne's past hard becomes the gift that saves a life, and the quote strip reads *"You forget that Mrs. Hammond had twins three times."*

> A winter night, clear and frosty, all shadow and silver snow. Two small girls in coats and hoods hurry hand in hand across a wide crusted field toward a farmhouse whose one kitchen window is lit warm gold. One girl, thin and red-haired, is half a step ahead and pulling; the other, dark-haired with a shawl wrapped hastily over her head, is looking back toward the way they came. Big stars over the silent field; dark pointed firs with snow powdering their branches along one edge; a wisp of chimney smoke. Faded slate blue in the sky and snow shadows, warm ochre in the lit window as the single note of gold. Seen from behind and a little above the girls, so the window is the destination. The lit window and the joined hands are the point of the picture.

### `anne-ch19.png`, lesson 10.3

The day's question is what Anne's reaction after the spare-room catastrophe shows about who she is becoming, and the quote strip reads *"It is my duty to go home to Miss Marilla Cuthbert."*

> A small, respectable sitting room in a farmhouse, a fire low in the grate. In an upright chair by the fire sits a thin, prim, rigid old lady with gold-rimmed glasses, knitting fiercely, her needles stopped mid-stitch as she wheels around toward the door. In the open doorway stands a thin red-haired girl of eleven, white-faced, hands clasped tight in front of her, eyes enormous, one foot still on the threshold: she has just knocked and come in. Behind her, through the door, the corner of a kitchen and a hint of a second girl's dark hair ducking out of sight. Dusty rose in the old lady's shawl, sage in the walls, one note of antique gold in the firelight on the knitting. Seen from the fireside, a little behind the old lady's chair, so the girl in the doorway is the face we read. The distance between the chair and the door is the picture.

### `anne-ch20.png`, lesson 10.4

The day's question is what happens when imagination becomes its own kind of trap, and the quote strip (corrected) reads *"I'll be contented with commonplace places after this."*

> A June twilight in a spruce grove, the trunks close and dark, the path between them dim. A narrow log bridge crosses a brook in the foreground. A thin red-haired girl of eleven, bareheaded, has just stepped off the bridge onto the path and stands with her shoulders up and her hands clenched at her sides, staring into the trees ahead. Around her, drawn only in thin pen line and the faintest wash so that they might be branches and might not, are the things she imagined: a pale strip of birch bark blowing across the path, two old boughs rubbing together overhead, the swoop of a bat, and far up the path a white shape that could be a lady wringing her hands or could be mist. Behind her, across the brook, the last warm ochre light of the open field she came from; ahead, sage and slate shadow. The one note of antique gold is on the bridge behind her. Seen from a little way up the path, looking back at her as the wood would see her. The girl's stillness at the edge of the dark is the picture.

## What I wrote rather than took from the page

Worth a look before students reach them:

- **Curriculum fixes (own commit, to the pre-sparkle markup).** The 20 slips in the drift list, in the chat, plus one mechanical one: the four files ended `</body></html>` on one line and the injector wants `</body>` alone, so the last line is now two lines. The ones that change what a student sees: real DOL models on all four days (10.4's fix-it sentence changes to match its model: "You know I always mean what I say," said Marilla); exact epigraphs on 10.1 and 10.4; the 10.1 vocabulary lead-in and sentences (cordial from the book, the other three plain and non-spoiling, the worked example no longer tells Ch. 18); a Ch. 16 Growing-Up Watch on 10.1 instead of the Ch. 18 one; the 10.1 spelling sort swaps garden/gentle/cabbage for golden/genius/gorgeous (all in Ch. 16); the 10.2 grammar spotter sentence and spelling spotter words; the full RWM sentence on 10.2; the 10.3 vocab cloze no longer previews Ch. 20; "energ_" for "g_m" on 10.3; 10.3 Pause labels in order; "Week 10" on 10.4.
- **Second DOL sentence on each day.** Mine, in the same error pattern as the printed one. Practice sentences, not quotes, except 10.4's, which is Marilla's own "I'll cure you of imagining ghosts into places."
- **Copia seed on 10.1** is Montgomery's second sentence of Ch. 16 ("Anne revelled in the world of colour about her"); the three worked examples are mine.
- **Hint ladders** (10.1 morphology; all 15 blanks on 10.3) and **miss lines** (10.1 vocabulary match and both sorts; 10.2 vocabulary match). Derived from the answers on the page.
- **Scholar clauses and evidence flags** for every chapter question.
- **Miss Barry** says "white as paper" for the book's "white-faced," and "I have never guided anything but a knitting needle," which is her joke, not a book fact. Everything else she says is Ch. 19.

## Notes

- The welcome clip only plays for a student who has a profile. The profile is made on day 1.
- `guide2` sits over the Watch transcript, so it carries the week's courage theme. On 10.1 that transcript is the corrected Ch. 16 one.
- The sweep's match/sort miss probes are pinned to week 7, so they print "(none)" here; the week 10 miss lines get tested with the separate script, as in week 9.
