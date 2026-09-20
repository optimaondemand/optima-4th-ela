# assets/audio/guide

The **guiding voice** — the teacher's framing that the introduction
videos were going to carry. **A guide clip never reads the page.** It
says why the work is there, what it has to do with today's chapter, and
how the parts join.

One guiding voice at the head of every tab, which is what the videos
were for:

| Tab | Folder | File | Keyed by | Clips |
|---|---|---|---|---|
| Warm-Up | `welcome/` | `g4ela-<week>-<day>.mp3` | lesson | 128 |
| Word Study | `turn/` | `g4ela-<week>-<day>-1.mp3` | lesson | 128 |
| Reading | `turn/` | `g4ela-<week>-<day>-2.mp3` | lesson | 128 |
| Assignment | `turn/` | `g4ela-<week>-<day>-3.mp3` | lesson | 128 |
| *(Growing-Up Watch block)* | `watch/` | `g4ela-wk<week>.mp3` | week | 32 |

So lesson 7.1 is `welcome/g4ela-7-1.mp3` and `turn/g4ela-7-1-1.mp3`,
`-2`, `-3`.

**The number in `turn/` is the tab the clip OPENS**, not the one it
leaves: 1 opens Word Study, 2 opens Reading, 3 opens Assignment. Each
clip plays at the top of the tab it is talking about. (They used to sit
at the foot of the *previous* tab, pointing forward, which meant hearing
"before you open the book" while looking at the word study — being told
about a page you are not on.)

Because a clip introduces what is in front of the student, the first
one can only look forward; `-3`, at the top of Assignment, is the only
one that can look back at the chapter.

Drop a file in and the control appears. Take it away and it disappears.

## Not here

`../poem/` is the one remaining read-aloud: a recording of the poem
itself, because there, reading the actual words is the point. Keyed by
poem, not by lesson.

The empty `../welcome/` and `../watch/` folders are the old read-aloud
locations and are no longer used — safe to delete.

## Format

MP3, mono, 22.05 kHz, 48–64 kbps, about −16 LUFS. 15–25 seconds, which
is 40–75 words.

**Level them before filing.** ElevenLabs does not hold a consistent
output level between generations — the first three clips came out at
−16.3, −23.0 and −24.6 LUFS, an 8 dB spread that a student hears as
one tab being much quieter than the last.

## Scripts and tools

- `claude/g4-guide-voice-spec.md` — the design, the rules for writing
  one, and the ElevenLabs settings
- `claude/g4-guide-scripts-wk07.md` — week 7
- `tools/rename_guide_clips.py` — files a folder of downloads under
  these names. Run it without `--apply` first; it prints what it would
  do and changes nothing.

## The rule that keeps this honest

Every guide clip is enrichment. The lesson must read completely without
any of it — clips arrive over months, and some students work with sound
off. If a script contains something a student actually *needs*, that
sentence belongs on the page instead.
