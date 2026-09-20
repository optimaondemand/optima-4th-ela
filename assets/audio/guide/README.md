# assets/audio/guide

The **guiding voice** — the teacher's framing that the introduction
videos were going to carry. This is a different job from the clips in
`welcome/`, `watch/` and `poem/`, which read what is printed on the
page. **A guide clip never reads the page.** It says why the work is
there, what it has to do with today's chapter, and how the parts join.

## turn/ — the three hand-offs between tabs

```
turn/g4ela-<week>-<day>-1.mp3    warm-up    → word study
turn/g4ela-<week>-<day>-2.mp3    word study → reading
turn/g4ela-<week>-<day>-3.mp3    reading    → assignment
```

So lesson 7.1 is `g4ela-7-1-1.mp3`, `g4ela-7-1-2.mp3`, `g4ela-7-1-3.mp3`.
Three per lesson, 387 for the year, every one unique to that day's
chapter.

The clip appears at the foot of its tab, just above the button that
moves on — the moment it is talking about. Position 1 plays before the
student has read anything, so its script only looks forward; position 3
plays after the chapter and can look back.

Drop a file in and the control appears. Take it away and it disappears.
Nothing else to configure, and the Assignment tab has no hand-off
because it is the last one.

## Format

Same as the read-aloud track: MP3, mono, 22.05 kHz, 48–64 kbps, about
−16 LUFS. 15–25 seconds each, which is 40–75 words.

## Scripts

Written per week and kept in the project:

- `claude/g4-guide-voice-spec.md` — the design, the rules for writing
  one, and the ElevenLabs settings
- `claude/g4-guide-scripts-wk07.md` — week 7, all twelve

`tools/rename_guide_clips.py` files a folder of ElevenLabs downloads
under these names. Run it with `--manifest tools/guide-manifest-wk07.csv`
and no `--apply` first; it prints what it would do and changes nothing.

## The rule that keeps this honest

Every guide clip is enrichment. The lesson must read completely without
any of it — clips arrive over months, and some students work with sound
off. If a script contains something a student actually *needs*, that
sentence belongs on the page instead.
