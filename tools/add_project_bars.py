#!/usr/bin/env python3
"""Put a Standards Alignment bar (Florida + Texas rows, same toggle as the lesson pages) on the
G4 unit project pages, right under the header (Nov 20 2026). Texas comes from
standards/crosswalk-g4.json. Re-runnable: replaces the bar if it is already there.
Then run  python3 tools/std_tag.py projects  to tag the pages.
Run from the optima-4th-ela repo root."""
import io, json, re
CW = json.load(io.open('standards/crosswalk-g4.json', encoding='utf8'))['map']
F = lambda *c: ['ELA.K12.' + x if x.startswith('EE') else 'ELA.4.' + x for x in c]
PROJECTS = {   # why each code: what the project has students do
 # Anne scrapbook: how Anne changes at 3 turning points (characterization, events, setting map) R.1.1;
 # one sentence about growing up true for anyone R.1.2; 2+ sentence explanations C.1.4 with a detail
 # for each word/claim EE.1.1; pictures, map, keepsakes arranged on pages C.5.1; scrapbook format EE.5.1
 'lesson-14-scrapbook.html': F('R.1.1', 'R.1.2', 'C.1.4', 'C.3.1', 'C.5.1', 'EE.1.1', 'EE.5.1'),
 # NTS: notes in a character's voice C.1.2; closing on what the book says about courage R.1.2;
 # real history tied to an object R.3.3; quote/exact detail in every note EE.1.1; rubric conventions
 # C.3.1; the chosen format (box, window, secret) held all the way EE.5.1
 'lesson-19-nts-project.html': F('R.1.2', 'R.3.3', 'C.1.2', 'C.3.1', 'EE.1.1', 'EE.5.1'),
}
def short(c): return '4.' + '.'.join(re.findall(r'\(([^)]+)\)', c)[1:])
CSS = """/* ======= STANDARDS TOGGLE BAR (same as the G4 lessons) ======= */
.standards-toggle-bar{display:flex;align-items:center;justify-content:space-between;background:linear-gradient(135deg,#1a2a3a,#1e3448);padding:10px 28px;cursor:pointer;user-select:none;border-bottom:1px solid rgba(85,200,232,.12);margin-top:12px;}
.standards-toggle-bar:hover{background:linear-gradient(135deg,#1e3044,#23394d);}
.standards-toggle-label{font-size:12px;color:rgba(255,255,255,.55);text-transform:uppercase;letter-spacing:1px;font-weight:700;display:flex;align-items:center;gap:8px;}
.standards-toggle-arrow{font-size:10px;color:rgba(255,255,255,.35);transition:transform .25s ease;}
.standards-toggle-bar.open .standards-toggle-arrow{transform:rotate(180deg);}
.standards-panel{max-height:0;overflow:hidden;transition:max-height .3s ease;background:#14212e;border-bottom:1px solid rgba(85,200,232,.08);}
.standards-panel.open{max-height:360px;}
.standards-panel-inner{display:flex;gap:32px;padding:14px 28px 16px;flex-wrap:wrap;}
.standards-group{display:flex;flex-direction:column;gap:6px;}
.standards-group-label{font-size:10px;color:rgba(255,255,255,.4);text-transform:uppercase;letter-spacing:.8px;font-weight:700;}
.standards-codes{font-size:12px;color:rgba(255,255,255,.65);line-height:1.7;font-weight:500;}
.standards-codes .fl-code{color:#80CBC4;}
.standards-codes .tx-code{color:#FFD54F;}
.standards-panel + .oao-info{margin-top:0;}
@media print{.standards-toggle-bar,.standards-panel{display:none!important;}}
"""
for f, fl in PROJECTS.items():
    s = io.open(f, encoding='utf8', newline='').read()
    s = re.sub(r'\s*<!-- STANDARDS -->.*?<!-- /STANDARDS -->', '', s, flags=re.S)
    s = re.sub(r'/\* ======= STANDARDS TOGGLE BAR \(same as the G4 lessons\) ======= \*/.*?@media print\{\.standards-toggle-bar,\.standards-panel\{display:none!important;\}\}\n', '', s, flags=re.S)
    tx = []
    for c in fl:
        for t in CW[c]['TX']:
            if short(t) not in tx: tx.append(short(t))
    bar = ('\n  <!-- STANDARDS -->\n'
      '  <div class="standards-toggle-bar" onclick="this.classList.toggle(\'open\');this.nextElementSibling.classList.toggle(\'open\');">\n'
      '    <span class="standards-toggle-label">Standards Alignment</span>\n    <span class="standards-toggle-arrow">▼</span>\n  </div>\n'
      '  <div class="standards-panel">\n    <div class="standards-panel-inner">\n'
      '      <div class="standards-group">\n        <div class="standards-group-label">Florida B.E.S.T.</div>\n'
      '        <div class="standards-codes">' + ' · '.join(f'<span class="fl-code">{c}</span>' for c in fl) + '</div>\n      </div>\n'
      '      <div class="standards-group">\n        <div class="standards-group-label">Texas TEKS</div>\n'
      '        <div class="standards-codes">' + ' · '.join(f'<span class="tx-code">{t}</span>' for t in tx) + '</div>\n      </div>\n'
      '    </div>\n  </div>\n  <!-- /STANDARDS -->')
    i = s.index('</header>', s.index('class="oao-header"')) + len('</header>')
    s = s[:i] + bar + s[i:]
    j = s.index('</style>'); s = s[:j] + CSS + s[j:]
    io.open(f, 'w', encoding='utf8', newline='').write(s); print('bar on', f, len(fl), 'FL,', len(tx), 'TX')
