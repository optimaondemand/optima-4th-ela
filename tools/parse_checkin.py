#!/usr/bin/env python3
"""Parse a G4 ELA week-N-checkin.html into a check-in dict (sections, questions, excerpts, options)."""
import html, re, sys, json

def clean(frag):
    """HTML fragment -> safe simple HTML (keep b/strong/em/i/br/u), normalized spaces."""
    frag = re.sub(r'<span class="q-number">.*?</span>', '', frag, flags=re.S)
    frag = re.sub(r'<span class="pts">.*?</span>', '', frag, flags=re.S)
    frag = re.sub(r'<(/?)(strong|b|em|i|u)\b[^>]*>', r'[[\1\2]]', frag)
    frag = re.sub(r'<br\s*/?>', '[[br]]', frag)
    frag = re.sub(r'</div>\s*<div[^>]*>', '[[br]]', frag)
    frag = re.sub(r'<[^>]+>', ' ', frag)
    frag = html.unescape(frag)
    frag = html.escape(frag, quote=False)
    frag = re.sub(r'\[\[(/?)(strong|b|em|i|u)\]\]', r'<\1\2>', frag)
    frag = frag.replace('[[br]]', '<br>')
    frag = re.sub(r'[ \t\r\n\xa0]+', ' ', frag)
    frag = re.sub(r'\s*<br>\s*', '<br>', frag)
    frag = re.sub(r'^(<br>)+|(<br>)+$', '', frag.strip())
    return frag.strip()

def plain(frag):
    return re.sub(r'\s+', ' ', html.unescape(re.sub(r'<[^>]+>', ' ', frag))).strip()

def div_block(s, start):
    """Return end index of the <div ...> starting at start (balanced)."""
    depth = 0
    for m in re.finditer(r'<div\b|</div>', s[start:]):
        depth += 1 if m.group(0) == '<div' else -1
        if depth == 0:
            return start + m.end()
    raise ValueError('unbalanced')

def parse(fn):
    s = open(fn, encoding='utf-8').read()
    body = re.sub(r'<script.*?</script>', '', s, flags=re.S)
    week = int(re.search(r'week-(\d+)-checkin', fn).group(1))
    title = plain(re.search(r'<title>(.*?)</title>', s, re.S).group(1))
    intro_m = re.search(r'<div class="intro[^"]*"[^>]*>(.*?)</div>', body, re.S)
    out = {'week': week, 'title': title, 'intro': clean(intro_m.group(1)) if intro_m else '', 'questions': []}
    for sm in re.finditer(r'<div class="section">', body):
        sec = body[sm.start():div_block(body, sm.start())]
        stitle = plain(re.search(r'<div class="section-title">(.*?)</div>', sec, re.S).group(1))
        spts = int(re.search(r'(\d+) points?', re.search(r'<div class="section-pts">(.*?)</div>', sec, re.S).group(1)).group(1))
        pending = []
        pos = 0
        while True:
            m = re.search(r'<div class="(excerpt|question)">', sec[pos:])
            if not m: break
            st = pos + m.start(); en = div_block(sec, st)
            blk = sec[st:en]; pos = en
            if m.group(1) == 'excerpt':
                src = re.search(r'<div class="excerpt-source">(.*?)</div>', blk, re.S)
                txt = re.sub(r'<div class="excerpt-source">.*?</div>', '', blk, flags=re.S)
                pending.append({'text': clean(txt), 'cite': clean(src.group(1)) if src else ''})
                continue
            q = {'section': stitle, 'section_pts': spts}
            q['label'] = clean(re.search(r'<div class="q-label">(.*?)</div>', blk, re.S).group(1))
            qn = re.search(r'<span class="q-number">(\d+)</span>', blk)
            q['n'] = int(qn.group(1))
            pts = re.search(r'\((\d) points?\)|<span class="pts">(\d) pts?</span>', blk)
            q['points'] = int(pts.group(1) or pts.group(2)) if pts else 1
            parts = []
            for pm in re.finditer(r'<div class="(rwm-model|q-text|excerpt|hint)"[^>]*>|<div style="[^"]*">', blk):
                pst = pm.start(); pen = div_block(blk, pst); piece = blk[pst:pen]
                kind = pm.group(1) or 'box'
                if any(pst > a and pen <= b for a, b in [(x[1], x[2]) for x in parts]):
                    continue
                parts.append((kind, pst, pen, piece))
            q['pre'] = pending; pending = []
            q['parts'] = []
            for kind, _, _, piece in parts:
                if kind == 'rwm-model':
                    lab = re.search(r'<div class="rwm-model-label">(.*?)</div>', piece, re.S)
                    txt = re.search(r'<div class="rwm-model-text">(.*?)</div>', piece, re.S)
                    q['parts'].append(('model', (clean(lab.group(1)) if lab else 'Model'), clean(txt.group(1))))
                elif kind == 'excerpt':
                    src = re.search(r'<div class="excerpt-source">(.*?)</div>', piece, re.S)
                    txt = re.sub(r'<div class="excerpt-source">.*?</div>', '', piece, flags=re.S)
                    q['parts'].append(('excerpt', clean(txt), clean(src.group(1)) if src else ''))
                else:
                    q['parts'].append((kind, clean(piece)))
            opts = re.findall(r'<li[^>]*><span class="opt-letter">\w</span>(.*?)</li>', blk, re.S)
            q['options'] = [clean(o) for o in opts]
            q['type'] = 'multiple_choice_question' if opts else 'essay_question'
            out['questions'].append(q)
    return out

if __name__ == '__main__':
    print(json.dumps(parse(sys.argv[1]), ensure_ascii=False, indent=1))
