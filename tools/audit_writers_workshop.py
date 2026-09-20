#!/usr/bin/env python3
"""
audit_writers_workshop.py — Grade 4 ELA Writer's Workshop strand audit.

Scans every lesson-day HTML in optima-4th-ela and reports, per file:
  * whether a Writer's Workshop block is present
  * which week the block declares
  * the genre/step focus it names
and flags three failure modes:
  1. NO CARD      — no Writer's Workshop block at all
  2. WRONG WEEK   — the block declares a week that isn't this file's week
  3. NO ANCHOR    — a block is present but lacks id="writers-workshop"
                    (breaks in-page links and any script that targets it)

Usage:
    python3 audit_writers_workshop.py [repo_dir]     # default: current dir
    python3 audit_writers_workshop.py --csv out.csv

Written Sept 2026 alongside the Writer's Workshop handoff spec. The
regexes match both the HTML-entity spelling (Writer&rsquo;s) and the
literal curly apostrophe, because both appear in the repo.
"""
import csv
import glob
import html
import os
import re
import sys

DECL = re.compile(r'Writer(?:&rsquo;|’)s Workshop:\s*Week\s*(\d+)\s*(?:&middot;|·)\s*([^<]*)')
ANCHOR = 'id="writers-workshop"'
FNAME = re.compile(r'lesson-(\d+)-(\d)-')

# what the scope & sequence says each week's writing arc is
ARCS = [
    (1, 6, 'Narrative (personal narrative)'),
    (7, 14, 'Realistic fiction'),
    (15, 19, 'Opinion'),
    (20, 25, 'Expository / research'),
    (26, 30, 'Literary analysis'),
    (31, 32, 'Final project / portfolio'),
]


def arc_for(week):
    for lo, hi, name in ARCS:
        if lo <= week <= hi:
            return name
    return '(outside 1-32)'


def scan(repo):
    rows = []
    for path in sorted(glob.glob(os.path.join(repo, 'lesson-*-*.html'))):
        base = os.path.basename(path)
        m = FNAME.match(base)
        if not m:
            continue                      # fluency pages, check-ins, etc.
        week, day = int(m.group(1)), int(m.group(2))
        with open(path, encoding='utf-8') as fh:
            src = fh.read()

        has_anchor = ANCHOR in src
        dm = DECL.search(src)
        declared = int(dm.group(1)) if dm else None
        focus = html.unescape(dm.group(2)).strip() if dm else ''
        has_block = has_anchor or dm is not None

        if not has_block:
            status = 'NO CARD'
        elif declared is not None and declared != week:
            status = 'WRONG WEEK'
        elif not has_anchor:
            status = 'NO ANCHOR'
        else:
            status = 'ok'

        rows.append({
            'week': week, 'day': day, 'file': base, 'arc': arc_for(week),
            'status': status, 'declared_week': declared or '', 'focus': focus,
        })
    rows.sort(key=lambda r: (r['week'], r['day'], r['file']))
    return rows


def main():
    args = [a for a in sys.argv[1:]]
    out_csv = None
    if '--csv' in args:
        i = args.index('--csv')
        out_csv = args[i + 1]
        del args[i:i + 2]
    repo = args[0] if args else '.'

    rows = scan(repo)
    if not rows:
        print('No lesson-<week>-<day>-*.html files found in %s' % os.path.abspath(repo))
        return 1

    print('%-4s %-3s %-36s %-11s %-5s %s' %
          ('WK', 'D', 'FILE', 'STATUS', 'DECL', 'FOCUS'))
    for r in rows:
        print('%-4d %-3d %-36s %-11s %-5s %s' %
              (r['week'], r['day'], r['file'][:36], r['status'],
               r['declared_week'], r['focus'][:40]))

    def pick(s):
        return [r for r in rows if r['status'] == s]

    print('\nscanned %d lesson-day files' % len(rows))
    for label in ('NO CARD', 'WRONG WEEK', 'NO ANCHOR'):
        hit = pick(label)
        weeks = sorted(set(r['week'] for r in hit))
        print('%-11s %3d files   weeks: %s' % (label, len(hit), weeks or '-'))

    print('\nby writing arc:')
    for lo, hi, name in ARCS:
        inarc = [r for r in rows if lo <= r['week'] <= hi]
        bad = [r for r in inarc if r['status'] != 'ok']
        print('  wk %-5s %-32s %2d/%2d clean' %
              ('%d-%d' % (lo, hi), name, len(inarc) - len(bad), len(inarc)))

    if out_csv:
        with open(out_csv, 'w', newline='', encoding='utf-8') as fh:
            w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()))
            w.writeheader()
            w.writerows(rows)
        print('\nwrote %s' % out_csv)

    return 1 if any(r['status'] != 'ok' for r in rows) else 0


if __name__ == '__main__':
    sys.exit(main())
