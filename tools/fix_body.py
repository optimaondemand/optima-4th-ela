#!/usr/bin/env python3
"""Add the missing </body> before </html> (some Q4 lessons were saved without it; inject.py needs exactly one)."""
import io, sys
for fn in sys.argv[1:]:
    s = io.open(fn, encoding='utf-8', newline='').read()
    if '</body>' in s: print('has body', fn); continue
    i = s.rindex('</html>'); nl = '\r\n' if '\r\n' in s else '\n'
    s = s[:i] + '</body>' + nl + s[i:]
    io.open(fn, 'w', encoding='utf-8', newline='').write(s); print('added </body>', fn)
