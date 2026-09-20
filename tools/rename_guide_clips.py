#!/usr/bin/env python3
"""
rename_guide_clips.py — file a folder of ElevenLabs downloads under the
names the Guide manifest expects.

You generate clips in ElevenLabs in manifest order and download them.
They arrive with names like

    ElevenLabs_2026-09-20T14_03_11_Rachel_pvc_s50_sb75.mp3
    You_ve_just_been_thinking_about_the.mp3
    generated_audio(3).mp3

This puts each one where it belongs, under the right name, without
touching your downloads.

    python rename_guide_clips.py --manifest guide-manifest-wk07.csv \
                                --downloads "C:\\Users\\you\\Downloads\\wk07" \
                                --repo "C:\\repos\\optima-4th-ela"

That is a DRY RUN: it prints what it would do and changes nothing. Add
--apply once the table looks right.

Matching, in order of preference:
  1. by text   — many ElevenLabs downloads carry the opening words in
                 the filename. Unambiguous when it works.
  2. by order  — oldest file to first manifest row, and so on. Used only
                 for whatever text-matching could not place, and only if
                 the leftovers line up exactly.

Nothing is overwritten and nothing is deleted. Downloads are copied, not
moved, unless you pass --move.

Written Sept 2026 for the G4 ELA guiding-voice track. See
claude/g4-guide-voice-spec.md.
"""
import argparse
import csv
import os
import re
import shutil
import sys
import unicodedata

AUDIO_EXT = {'.mp3', '.m4a', '.wav', '.ogg', '.flac'}


def norm(s):
    """Lowercase alphanumeric run, for comparing a filename to a script."""
    s = unicodedata.normalize('NFKD', s)
    s = s.encode('ascii', 'ignore').decode('ascii').lower()
    return re.sub(r'[^a-z0-9]+', ' ', s).strip()


def read_manifest(path):
    with open(path, encoding='utf-8-sig', newline='') as fh:
        rows = list(csv.DictReader(fh))
    if not rows:
        sys.exit('manifest %s is empty' % path)
    for i, r in enumerate(rows, 1):
        if not r.get('filename') or not r.get('text'):
            sys.exit('manifest row %d is missing filename or text' % i)
        r['key'] = norm(r['text'])
    return rows


def list_downloads(folder):
    if not os.path.isdir(folder):
        sys.exit('downloads folder not found: %s' % folder)
    files = [os.path.join(folder, f) for f in os.listdir(folder)
             if os.path.splitext(f)[1].lower() in AUDIO_EXT]
    if not files:
        sys.exit('no audio files in %s' % folder)
    files.sort(key=lambda p: (os.path.getmtime(p), os.path.basename(p)))
    return files


def opening_words(path):
    """Strip an ElevenLabs filename down to the script words it carries.

    Real downloads look like
        ElevenLabs_2026-09-20T14_03_11_Now_open_the_book_Chapter_one.mp3
    so the leading tokens — the product name, the timestamp, anything
    with a digit in it — are dropped, and what survives is the opening of
    the script, usually truncated mid-sentence."""
    stem = norm(os.path.splitext(os.path.basename(path))[0])
    words = stem.split()
    while words and (words[0] in ('elevenlabs', 'eleven', 'labs', 'audio',
                                  'generated', 'tts')
                     or any(c.isdigit() for c in words[0])):
        words.pop(0)
    while words and any(c.isdigit() for c in words[-1]):
        words.pop()                     # trailing voice/settings suffixes
    return ' '.join(words)


def match_by_text(rows, files):
    """Pair a download with a script when the download's name carries the
    script's opening words. A pairing is kept only when exactly one
    script matches: a wrong guess is worse than no guess, because the
    order pass below will place whatever is left."""
    pairs, used = {}, set()
    for path in files:
        probe = opening_words(path)[:60]
        if len(probe) < 15:             # nothing usable in the name
            continue
        hits = [r for r in rows
                if r['filename'] not in used and r['key'].startswith(probe)]
        if len(hits) == 1:
            pairs[path] = hits[0]
            used.add(hits[0]['filename'])
    return pairs


def plan(rows, files):
    """Return [(download, row, how)] plus anything left unplaced."""
    by_text = match_by_text(rows, files)
    placed = [(p, by_text[p], 'text') for p in files if p in by_text]

    rest_files = [p for p in files if p not in by_text]
    rest_rows = [r for r in rows if r['filename'] not in
                 {row['filename'] for _, row, _ in placed}]

    if rest_files and len(rest_files) == len(rest_rows):
        placed += [(p, r, 'order') for p, r in zip(rest_files, rest_rows)]
        rest_files, rest_rows = [], []

    order = {r['filename']: i for i, r in enumerate(rows)}
    placed.sort(key=lambda t: order[t[1]['filename']])
    return placed, rest_files, rest_rows


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--manifest', required=True, help='the manifest CSV')
    ap.add_argument('--downloads', required=True, help='folder of ElevenLabs downloads')
    ap.add_argument('--repo', required=True, help='root of optima-4th-ela')
    ap.add_argument('--apply', action='store_true', help='actually write files')
    ap.add_argument('--move', action='store_true', help='move instead of copy')
    ap.add_argument('--force', action='store_true', help='allow overwriting existing clips')
    args = ap.parse_args()

    rows = read_manifest(args.manifest)
    files = list_downloads(args.downloads)

    print('manifest : %d clips  (%s)' % (len(rows), os.path.basename(args.manifest)))
    print('downloads: %d audio files\n' % len(files))
    if len(files) != len(rows):
        print('!! counts differ. Text-matched clips are still safe; anything')
        print('   left over will NOT be placed by order.\n')

    placed, spare_files, spare_rows = plan(rows, files)

    print('%-3s %-30s %-20s %-6s %s' %
          ('#', 'FROM (download)', 'TO', 'BY', 'SHOULD OPEN WITH'))
    for i, (src, row, how) in enumerate(placed, 1):
        # Only the order-matched rows need checking, so only they get the
        # opening words printed — play the file, hear these words, move on.
        opening = '' if how == 'text' else '"%s…"' % ' '.join(row['text'].split()[:7])
        print('%-3d %-30s %-20s %-6s %s' %
              (i, os.path.basename(src)[:30], row['filename'],
               how if how == 'text' else 'order', opening))
    if spare_files:
        print('\nnot placed — %d download(s):' % len(spare_files))
        for p in spare_files:
            print('   ', os.path.basename(p))
    if spare_rows:
        print('\nstill missing — %d clip(s) from the manifest:' % len(spare_rows))
        for r in spare_rows:
            print('   %-22s %s...' % (r['filename'], r['text'][:52]))

    if not placed:
        sys.exit('\nnothing to do.')

    if not args.apply:
        print('\nDRY RUN — nothing written. Re-run with --apply when this looks right.')
        if any(how == 'order' for _, _, how in placed):
            print('Rows marked "order" were placed by download time, not by name.')
            print('Check two or three of those by ear before trusting the rest.')
        return

    wrote = skipped = 0
    for src, row, _ in placed:
        dest_dir = os.path.join(args.repo, 'assets', 'audio', row.get('folder') or '')
        os.makedirs(dest_dir, exist_ok=True)
        dest = os.path.join(dest_dir, row['filename'])
        if os.path.exists(dest) and not args.force:
            print('exists, left alone:', row['filename'])
            skipped += 1
            continue
        (shutil.move if args.move else shutil.copy2)(src, dest)
        wrote += 1
    print('\n%s %d file(s); %d skipped.' %
          ('moved' if args.move else 'copied', wrote, skipped))
    if skipped:
        print('Pass --force to replace the ones that already exist.')


if __name__ == '__main__':
    main()
