#!/usr/bin/env python3
"""Rebuild the visible Texas (TEKS) codes in every G4 ELA page (the Texas row of the standards panel
and the footer) from the page's own Florida
codes and standards/crosswalk-g4.json, so TX always matches the FL standards bar (Nov 20 2026).
Before this, weeks 25, 31 and 32 showed 4.14.A / 4.14.B (no such TEKS; grade 4 ends at 4.13) and
most weeks left out the poetry and fluency TEKS. Run from the optima-4th-ela repo root; re-runnable."""
import glob, io, json, re

CW = json.load(io.open('standards/crosswalk-g4.json', encoding='utf8'))['map']
def short(c):            # 110.6(b)(8)(B) -> 4.8.B ; 110.6(b)(4) -> 4.4
    parts = re.findall(r'\(([^)]+)\)', c)[1:]
    return '4.' + '.'.join(parts)

changed = 0
for f in sorted(glob.glob('lesson-*.html')):
    s = io.open(f, encoding='utf8', newline='').read()
    m = re.search(r'(<div class="footer-standards">FL: )(.*?)( · TX: )(.*?)(</div>)', s)
    if not m: continue
    fl = [c.strip() for c in m.group(2).split(',')]
    tx = []
    for c in fl:
        for t in CW[c]['TX']:
            if short(t) not in tx: tx.append(short(t))
    new = m.group(1) + m.group(2) + m.group(3) + ', '.join(tx) + m.group(5)
    s2 = s[:m.start()] + new + s[m.end():]
    # the Texas row of the standards panel: <div class="standards-codes"><span class="tx-code">..</span> · ..</div>
    s2 = re.sub(r'(<div class="standards-codes">)(<span class="tx-code">.*?)(</div>)',
                lambda k: k.group(1) + ' · '.join('<span class="tx-code">%s</span>' % t for t in tx) + k.group(3), s2, count=1)
    if s2 != s:
        io.open(f, 'w', encoding='utf8', newline='').write(s2)
        changed += 1
print('footers rebuilt:', changed)
