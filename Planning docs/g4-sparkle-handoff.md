# G4 ELA sparkle — handoff

Written 23 Sept 2026. Everything below was verified against the repo on
Bethany's machine, not against a copy.

Read `claude/g4-sparkle-rollout-spec.md` for the design and the settled
decisions. This file is the current state and the work remaining.

---

## Where things stand

**Repo:** `C:\repos\optima-4th-ela`, branch **`sparkle-layer`**, not
`main`. `main` is untouched and is the escape hatch. Two commits:

```
c4d8c49  Ship the corrected sparkle.js
0c60a39  Add the sparkle layer, per-lesson data, and the build tools
```

**Check you are on the right branch before anything else.** On `main`
none of the files below exist and lesson 7.1 is unsparkled.

| File | Size | State |
|---|---|---|
| `sparkle.js` | 132,401 | correct — verified on the machine |
| `sparkle.css` | 54,731 | correct |
| `tools/inject.py` | 8,798 | correct |
| `tools/sweep.js` | 18,559 | correct |
| `data/lesson-7-1.json` | 4,367 | the only lesson data that exists |

**Sparkled:** lesson 7.1 only. 7.2, 7.3, 7.4 are untouched originals.
`lesson-7-fluency.html` is deliberately left plain.

**Assets present:** `assets/plates/anne-ch1.png` (and a stale `.jpg`
that nothing reads — safe to delete). Audio: `guide/welcome/g4ela-7-1.mp3`
and `guide/turn/g4ela-7-1-{1,2,3}.mp3`. Nothing for 7.2–7.4.

**Uncommitted and not mine:** two modified PDFs, and Excel lock files
(`~$…xlsx`) from two open workbooks. Leave all four alone.

---

## Verify before trusting any of this

Four commands. If any answer differs, stop and say so.

```
git rev-parse --abbrev-ref HEAD      -> sparkle-layer
wc -c < sparkle.js                   -> 132401
grep -c 'oao-data' sparkle.js        -> 2
grep -c 'buildMemory\|Shalott' sparkle.js  -> 0
```

That check exists because a previous session shipped a stale
`sparkle.js` and reported it as verified. See "How this went wrong".

---

## How it works

**The layer is additive.** `tools/inject.py` adds two JSON blocks to
`<head>` and links `sparkle.css` / `sparkle.js` before `</body>`. It
rewrites nothing else. Delete those blocks and the lesson is byte-for-
byte what it was.

**Each lesson's content lives in the lesson.** `data/lesson-<w>-<d>.json`
is written into the page as `<script type="application/json" id="oao-data">`
and read by `sparkle.js`. Every key is optional; a missing key costs
only its own feature. An empty DATA is a valid lesson.

**Art and the layer are referenced, never inlined.** A lesson grows by
~410 bytes for the links plus the size of its DATA — normally 4–5 KB
total. Much over 250 KB means something got embedded.

**The poem is not ours.** `assets/js/oao-sparkle.js` ships the By Heart
card — one poem per book, eight rungs — and 66 lessons load it. This
layer must never build one. Note that days 1 and 3 do *not* load that
script; Poetry Corner lives on days 2 and 4.

### Build a lesson

```
python tools/inject.py lesson-7-2-anne-ch2.html \
    --book anne --week 7 --day 2 \
    --title "Anne of Green Gables" --chapters "Ch. 2" \
    --quote "<a stronger line from this chapter>"
```

Dry run by default; add `--apply`. It picks up `data/lesson-7-2.json`
automatically and refuses to inject a file twice.

### Check it

```
node tools/sweep.js lesson-7-2-anne-ch2.html
```

From the repo root. It serves the repo over http, runs the page, and
exits non-zero with a reason. **Run it where the files actually live.**

Missing plates and unrecorded clips 404 on purpose and are listed
separately — they are expected, not failures.

---

## What needs doing

### 1. Build 7.2, 7.3, 7.4

Week 7 is the live week. For each lesson:

- write `data/lesson-7-<d>.json` (see the DATA table in the skill)
- run `inject.py`, then `sweep.js`
- one commit per week, sparkle only

Chapters: 7.2 = Ch. 2, 7.3 = Ch. 3–4, 7.4 = Ch. 5.

**Show Bethany the drafted DATA for 7.2 before doing 7.3 and 7.4.** If
the register is wrong, better to find out after one lesson than three.

### 2. Two process fixes to the skill

Both come from today's failure and are not yet written down:

- **Test where the files live.** A sweep run against a mirror of the
  repo proves nothing about the repo. It passed against a scratch copy
  while the real file was stale.
- **Verify what shipped, not what was built.** After committing a file,
  read it back from its real path and check it is the one that was
  tested. Size alone would have caught this.

### 3. Smaller, non-blocking

- `g4ela-7-1-2.mp3` is the old recording against a rewritten script —
  Bethany is re-recording it.
- `assets/plates/anne-ch1.jpg` is dead; nothing reads `.jpg`.
- Week 7's scripts exist in `claude/g4-guide-scripts-wk07.md`; the
  manifest is `tools/guide-manifest-wk07.csv`.

---

## The boundary — do not cross it

**The scope and sequence and the weekly arc are read-only.** Read them
to write good DATA and scripts; never edit them. Not the Big Questions,
objectives, standards, chapters, assessments, word-study focus, workshop
progression, or anything a student is graded on.

The complete list of permitted changes is in the skill. It is closed.
Anything outside it is a question for Bethany, not an edit.

Also never edited: `assets/js/oao-sparkle.js`, the year map, the board
coordinates, the covers, the owl, the ornaments, the seals, the
headpieces, `COURSE` / `BOARD_LEGS` / `WRITING_ARCS`.

---

## How this went wrong, so it doesn't again

Four real bugs reached the repo today. Each was caught by a session that
stopped and checked rather than building on top of the last claim.

1. **DATA was hardcoded in the layer.** Every lesson would have shown
   7.1's sentence, hints and connector. Fixed.
2. **A duplicate By Heart card.** The shipped poem system was never
   read — it was missed because the demo was built on 7.1, one of the
   few lessons that doesn't load it. Fixed.
3. **The sweep was pinned to 7.1's elements.** On another lesson it
   hung for 30 seconds and threw, rather than reporting. Fixed.
4. **A stale `sparkle.js` was committed** after the correct one was
   tested elsewhere, and reported as verified. Fixed in `c4d8c49`.

The pattern in all four: **something was verified in the wrong place,
or not verified at all, and then asserted confidently.** Check the
artifact that will actually be used, at the path it will actually live,
before saying it works.
