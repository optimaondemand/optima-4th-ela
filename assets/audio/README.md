# assets/audio

Recorded voice for the three spoken places in every lesson. There is no
manifest and no index: **drop a correctly-named MP3 in the right folder
and the control appears on the page.** Remove it and the control
disappears. No lesson file changes, ever.

The player asks the browser for the file and only reveals itself once
the file's metadata comes back, so a lesson with no recording yet shows
nothing at all — never a button that does nothing. Files can therefore
arrive in any order, over months.

## Naming

| Folder | File | Keyed by | Count for the year |
|---|---|---|---|
| `welcome/` | `g4ela-<week>-<day>.mp3` | lesson | 128 |
| `watch/`   | `g4ela-wk<week>.mp3`     | week   | 32 |
| `poem/`    | `<poem-slug>.mp3`        | poem   | ~8 |

Examples: `welcome/g4ela-7-1.mp3`, `watch/g4ela-wk7.mp3`,
`poem/lady-of-shalott.mp3`

The poem slug is the title lowercased, punctuation stripped, spaces
turned to hyphens — "The Lady of Shalott" becomes `lady-of-shalott`. The
code derives it from the poem title as the lesson spells it, so the two
must match.

## Format

Mono MP3, 22.05 kHz, 48-64 kbps, around -16 LUFS, peaks under -1 dBFS.
Half a second of silence at head and tail. Speech gains nothing from
stereo or a high bitrate; a full year at these settings is roughly
35 MB.

## Before this works in production

In the `AUDIO` block at the top of the sparkle layer:

```js
base: 'https://optimaondemand.github.io/optima-4th-ela/assets/audio/',
clips: { welcome: '', poem: '', watch: '' }   // delete the demo clips
```

The demo build embeds three robotic placeholder clips so the control can
be seen working with no server. They are marked in the code and must go
before anyone sees the lesson.

Full spec, including voice direction and where the scripts come from:
`claude/g4-audio-spec.md` in the ELA OAO project.
