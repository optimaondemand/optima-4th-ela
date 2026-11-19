# G4 ELA Word Study films (Marcus), from week 22 on

Ported from optima-3rd-ela/tools/g3sparkle/video (same timeline/trim/capture flow). Zero extra credits:
each film reuses that lesson's Word Study clip (assets/audio/guide/marcus/g4ela-W-D-<slot>.mp3).
There is no Marcus portrait, so render.html shows a lantern with his name (flame and glow move while he talks).

Output: assets/video/guide/marcus/g4ela-W-D-<slot>.mp4 + .jpg poster + .vtt captions.
DATA.media.<slot> becomes {"kind": "video", "path": "guide/marcus/g4ela-W-D-<slot>", ...}; the mp3 is removed.

Built in the cloud container (Chromium/Playwright, ffmpeg, Poppins/Lora/Noto Color Emoji, pip pocketsphinx):
1. specs_g4wkW.py: scenes on anchor phrases from the script (never show an answer the page asks for).
2. `SPECS=specs_g4wkW python timeline.py scripts_g4wkW.json` (mp3s in /tmp/vid/) -> timeline.json
3. `node capture.js <clip> 12` (expects /tmp/vid/build/{timeline.json,render.html})
4. `ffmpeg -framerate 12 -i frames/<k>/f%04d.jpg -i <k>.mp3 -c:v libx264 -preset slow -tune stillimage -crf 30 -pix_fmt yuv420p -r 24 -c:a aac -b:a 96k -af apad -shortest -movflags +faststart <k>.mp4`
   Poster = frame 0.4 s before scene 2. VTT from timeline caps. Check a contact sheet of every scene before shipping.
