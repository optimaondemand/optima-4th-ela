#!/usr/bin/env python3
"""Add the Start here drawer (Opti's how-to video) to a plain fluency page, copied byte-for-byte from
lesson-24-fluency.html: the drawer <style> before </head> and the <details>+<script> after the header's closing </div>.
    python3 tools/fluency_start.py lesson-25-fluency.html [...]      (idempotent)"""
import io, re, sys
src = io.open('lesson-24-fluency.html', encoding='utf-8').read()
css = re.search(r'<style>/\* Start here drawer.*?</style>', src, re.S).group(0)
drawer = re.search(r'<details class="nav-start">.*?</details>\s*<script>\(function\(\)\{var d=document.querySelector\("\.nav-start"\).*?</script>', src, re.S).group(0)
for fn in sys.argv[1:]:
    s = io.open(fn, encoding='utf-8', newline='').read()
    if 'class="nav-start"' in s: print(fn, 'already has it'); continue
    nl = '\r\n' if '\r\n' in s else '\n'
    assert s.count('</head>') >= 1
    s = s.replace('</head>', css.replace('\n', nl) + '</head>', 1)
    m = re.search(r'<div class="header-badge">.*?</div>\s*</div>' + re.escape(nl), s, re.S)
    if not m: sys.exit(fn + ': header not found')
    s = s[:m.end()] + drawer.replace('\n', nl) + nl + s[m.end():]
    io.open(fn, 'w', encoding='utf-8', newline='').write(s); print('ok', fn)
