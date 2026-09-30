# Week 8 supply list — what you still owe

Lessons 8.1–8.4 are built, committed and pass the sweep. **They work right now without anything below.** Each clip appears on its own the moment its file is in the right folder. Nothing needs rebuilding.

All paths are inside `C:\repos\optima-4th-ela`.

## At a glance

| Lesson | Guide | Plate | Clips | Scripts |
|---|---|---|---|---|
| 8.1 (Ch. 6) | Marilla | ✓ have it (`anne-ch6.png`) | 15 | `Planning docs\g4-scripts-marilla-8-1.md` |
| 8.2 (Ch. 7–8) | Marilla | ✓ have it (`anne-ch7-8.png`) | 15 | `Planning docs\g4-scripts-marilla-8-2.md` |
| 8.3 (Ch. 9) | Mrs. Lynde | ✓ have it (`anne-ch9.png`) | 15 | `Planning docs\g4-scripts-rachel-8-3.md` |
| 8.4 (Ch. 10) | Matthew | ✓ have it (`anne-ch10.png`) | 14 | `Planning docs\g4-scripts-matthew-8-4.md` |

**59 audio clips in all.** The four chapter plates are already in `assets\plates\`, so there is no art to make this week.

## Where the files go

- **Audio:** `assets\audio\guide\<folder>\<filename>.mp3`
- **Video (optional):** the same filename as `.mp4` in `assets\video\guide\<folder>\`. A `.jpg` with the same name is its thumbnail.
- Each file stays hidden until it exists. If both an mp3 and an mp4 exist, both show.
- A misspelled name shows no error. The clip just never appears, so copy the names exactly.

When you add videos: copy the full-size originals to `Planning docs\video-originals\<folder>\` first, then compress to 1280 wide (`ffmpeg -vf scale=1280:-2 -c:v libx264 -profile:v high -pix_fmt yuv420p -preset slow -crf 27 -c:a aac -b:a 96k -movflags +faststart`) and make each thumbnail with `tools/make-thumbnail.py`.

## 8.1 — Marilla, folder `marilla`

| mp3 (required to hear it) | mp4 (optional) |
|---|---|
| `assets\audio\guide\marilla\g4ela-8-1-welcome.mp3` | `assets\video\guide\marilla\g4ela-8-1-welcome.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-wgrd.mp3` | `assets\video\guide\marilla\g4ela-8-1-wgrd.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-dol.mp3` | `assets\video\guide\marilla\g4ela-8-1-dol.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-guide1.mp3` | `assets\video\guide\marilla\g4ela-8-1-guide1.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-morphology.mp3` | `assets\video\guide\marilla\g4ela-8-1-morphology.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-vocabulary.mp3` | `assets\video\guide\marilla\g4ela-8-1-vocabulary.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-grammar.mp3` | `assets\video\guide\marilla\g4ela-8-1-grammar.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-spelling.mp3` | `assets\video\guide\marilla\g4ela-8-1-spelling.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-guide2.mp3` | `assets\video\guide\marilla\g4ela-8-1-guide2.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-read.mp3` | `assets\video\guide\marilla\g4ela-8-1-read.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-guide3.mp3` | `assets\video\guide\marilla\g4ela-8-1-guide3.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-chapter.mp3` | `assets\video\guide\marilla\g4ela-8-1-chapter.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-wordconn.mp3` | `assets\video\guide\marilla\g4ela-8-1-wordconn.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-workshop.mp3` | `assets\video\guide\marilla\g4ela-8-1-workshop.mp4` |
| `assets\audio\guide\marilla\g4ela-8-1-copia.mp3` | `assets\video\guide\marilla\g4ela-8-1-copia.mp4` |

## 8.2 — Marilla, folder `marilla`

| mp3 (required to hear it) | mp4 (optional) |
|---|---|
| `assets\audio\guide\marilla\g4ela-8-2-welcome.mp3` | `assets\video\guide\marilla\g4ela-8-2-welcome.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-wgrd.mp3` | `assets\video\guide\marilla\g4ela-8-2-wgrd.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-dol.mp3` | `assets\video\guide\marilla\g4ela-8-2-dol.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-guide1.mp3` | `assets\video\guide\marilla\g4ela-8-2-guide1.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-morphology.mp3` | `assets\video\guide\marilla\g4ela-8-2-morphology.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-vocabulary.mp3` | `assets\video\guide\marilla\g4ela-8-2-vocabulary.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-grammar.mp3` | `assets\video\guide\marilla\g4ela-8-2-grammar.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-spelling.mp3` | `assets\video\guide\marilla\g4ela-8-2-spelling.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-guide2.mp3` | `assets\video\guide\marilla\g4ela-8-2-guide2.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-read.mp3` | `assets\video\guide\marilla\g4ela-8-2-read.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-guide3.mp3` | `assets\video\guide\marilla\g4ela-8-2-guide3.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-chapter.mp3` | `assets\video\guide\marilla\g4ela-8-2-chapter.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-wordconn.mp3` | `assets\video\guide\marilla\g4ela-8-2-wordconn.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-workshop.mp3` | `assets\video\guide\marilla\g4ela-8-2-workshop.mp4` |
| `assets\audio\guide\marilla\g4ela-8-2-rwm.mp3` | `assets\video\guide\marilla\g4ela-8-2-rwm.mp4` |

## 8.3 — Mrs. Lynde, folder `rachel`

| mp3 (required to hear it) | mp4 (optional) |
|---|---|
| `assets\audio\guide\rachel\g4ela-8-3-welcome.mp3` | `assets\video\guide\rachel\g4ela-8-3-welcome.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-wgrd.mp3` | `assets\video\guide\rachel\g4ela-8-3-wgrd.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-dol.mp3` | `assets\video\guide\rachel\g4ela-8-3-dol.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-guide1.mp3` | `assets\video\guide\rachel\g4ela-8-3-guide1.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-morphology.mp3` | `assets\video\guide\rachel\g4ela-8-3-morphology.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-vocabulary.mp3` | `assets\video\guide\rachel\g4ela-8-3-vocabulary.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-grammar.mp3` | `assets\video\guide\rachel\g4ela-8-3-grammar.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-spelling.mp3` | `assets\video\guide\rachel\g4ela-8-3-spelling.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-guide2.mp3` | `assets\video\guide\rachel\g4ela-8-3-guide2.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-read.mp3` | `assets\video\guide\rachel\g4ela-8-3-read.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-guide3.mp3` | `assets\video\guide\rachel\g4ela-8-3-guide3.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-chapter.mp3` | `assets\video\guide\rachel\g4ela-8-3-chapter.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-wordconn.mp3` | `assets\video\guide\rachel\g4ela-8-3-wordconn.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-workshop.mp3` | `assets\video\guide\rachel\g4ela-8-3-workshop.mp4` |
| `assets\audio\guide\rachel\g4ela-8-3-rwm.mp3` | `assets\video\guide\rachel\g4ela-8-3-rwm.mp4` |

## 8.4 — Matthew, folder `matthew`

| mp3 (required to hear it) | mp4 (optional) |
|---|---|
| `assets\audio\guide\matthew\g4ela-8-4-welcome.mp3` | `assets\video\guide\matthew\g4ela-8-4-welcome.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-wgrd.mp3` | `assets\video\guide\matthew\g4ela-8-4-wgrd.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-dol.mp3` | `assets\video\guide\matthew\g4ela-8-4-dol.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-guide1.mp3` | `assets\video\guide\matthew\g4ela-8-4-guide1.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-morphology.mp3` | `assets\video\guide\matthew\g4ela-8-4-morphology.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-vocabulary.mp3` | `assets\video\guide\matthew\g4ela-8-4-vocabulary.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-grammar.mp3` | `assets\video\guide\matthew\g4ela-8-4-grammar.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-spelling.mp3` | `assets\video\guide\matthew\g4ela-8-4-spelling.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-guide2.mp3` | `assets\video\guide\matthew\g4ela-8-4-guide2.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-read.mp3` | `assets\video\guide\matthew\g4ela-8-4-read.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-guide3.mp3` | `assets\video\guide\matthew\g4ela-8-4-guide3.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-chapter.mp3` | `assets\video\guide\matthew\g4ela-8-4-chapter.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-wordconn.mp3` | `assets\video\guide\matthew\g4ela-8-4-wordconn.mp4` |
| `assets\audio\guide\matthew\g4ela-8-4-workshop.mp3` | `assets\video\guide\matthew\g4ela-8-4-workshop.mp4` |

## What I wrote rather than took from the page

These are my wording, and worth a look before students reach them:

- **8.1 Growing-Up Watch.** The old text quoted the end of Ch. 10. The new text covers Ch. 5–6 only (Anne passed from family to family, Marilla taking her back to Mrs. Spencer).
- **8.2 grammar and spelling sentences.** Two new Ch. 8 sentences (Anne’s daydreams, Marilla’s card, the Cuthberts’ wall). The answers are the same shape as before: three possessives, one of them plural.
- **8.3 DOL fix-it sentence.** It changed to match the new real model: "mrs lyndes words about annes looks werent kind".
- **8.4 grammar draft.** "Mrs. Lyndes forgiveness came quickly." replaces the Diana sentence. The apostrophe is missing on purpose.
- **Second DOL sentence on each day, and the Copia examples on 8.1.** Written by me, in the same error pattern as the printed one.
- **Hint ladders (8.1 morphology, all 15 blanks on 8.3) and miss lines (8.1, 8.2).** Derived from the answers on the page.

## Notes

- The welcome clip only plays for a student who has a profile. The profile is made on day 1.
- Curriculum fixes are in their own commits, separate from the sparkle commits. The 8.1 and 8.2 fixes landed inside the commit labeled "8.3" (`2514e2f`) because of a git lock clash with another session. The content is right; only the label is off.
