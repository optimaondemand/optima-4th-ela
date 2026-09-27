#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Render the 32 Anne-unit Writer's Workshop cards from cards.py and inject
them into the lesson files (replacing the existing #writers-workshop block).
Also adds the persistent My Story box + its script, and puts my-story into
the gathered work. Idempotent: safe to re-run.

    python3 tools/ww_anne/build.py [repo_dir]      # default: cwd
    python3 tools/ww_anne/build.py --dry           # render only, write nothing
"""
import html as H
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cards as C  # noqa: E402

MYSTORY_KEY = 'g4-anne-my-story'
SCRIPT_ID = 'oao-mystory'


def esc(s):
    """Escape & < > but keep the little bit of inline markup we use (<b>, <br>)."""
    s = H.escape(s, quote=False)
    s = s.replace('&lt;b&gt;', '<b>').replace('&lt;/b&gt;', '</b>').replace('&lt;br&gt;', '<br>')
    return s


def strip(week):
    cur = C.WEEK_STEP[week]
    out = []
    for i, name in enumerate(C.STEPS):
        if i < cur:
            out.append('<span style="background:#E8F1E8;color:#4A7C2E;padding:4px 9px;border-radius:6px;font-size:12px;">✓ %s</span>' % name)
        elif i == cur:
            out.append('<span style="background:#C7922C;color:#fff;padding:4px 9px;border-radius:6px;font-size:12px;font-weight:700;">★ %s</span>' % name)
        else:
            out.append('<span style="background:#F0F0F0;color:#7A88A8;padding:4px 9px;border-radius:6px;font-size:12px;">○ %s</span>' % name)
    return ('<div style="display:flex;flex-wrap:wrap;gap:4px;justify-content:flex-start;align-items:center;margin-bottom:10px;">\n'
            + '\n'.join('          ' + o for o in out) + '\n        </div>')


def table(rows, head_bg='#FFF8F0'):
    h = ['<table style="width:100%;border-collapse:collapse;font-size:14px;margin-top:8px;background:#FFF;">']
    for r_i, row in enumerate(rows):
        h.append('<tr>')
        for c in row:
            tag = 'th' if r_i == 0 else 'td'
            st = 'text-align:left;padding:6px 8px;border:1px solid #F0E6D2;vertical-align:top;'
            if r_i == 0:
                st += 'background:%s;color:#3D5285;font-size:13px;' % head_bg
            h.append('<%s style="%s">%s</%s>' % (tag, st, esc(c), tag))
        h.append('</tr>')
    h.append('</table>')
    return ''.join(h)


def watch_how(w):
    parts = ['<div class="key-concept" style="background:#FFFEF7;border-color:#F5E6C8;margin-bottom:14px;">',
             '<div class="key-concept-label" style="color:#C7922C;">\U0001F440 Watch How &mdash; Sam, our example writer</div>',
             '<p style="font-size:15px;">%s</p>' % esc(w['intro'])]
    if 'before' in w:
        parts.append('<div style="display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px;">'
                     '<div style="background:#FFF;border:1px solid #F5E6C8;border-radius:6px;padding:10px;">'
                     '<div style="font-size:12px;color:#C7627E;font-weight:700;letter-spacing:0.5px;">BEFORE</div>'
                     '<div style="font-style:italic;font-size:14px;margin-top:4px;">%s</div></div>'
                     '<div style="background:#FFF;border:1px solid #F5E6C8;border-radius:6px;padding:10px;">'
                     '<div style="font-size:12px;color:#4A7C2E;font-weight:700;letter-spacing:0.5px;">AFTER</div>'
                     '<div style="font-style:italic;font-size:14px;margin-top:4px;">%s</div></div></div>'
                     % (esc(w['before']), esc(w['after'])))
    if 'page' in w:
        parts.append('<div style="background:#FFF;border:1px solid #F5E6C8;border-radius:6px;padding:12px 14px;margin-top:10px;font-size:15px;line-height:1.6;">'
                     + ''.join('<p style="margin:0 0 6px 0;">%s</p>' % esc(p) for p in w['page']) + '</div>')
    if 'table' in w:
        parts.append(table(w['table']))
    parts.append('<p style="margin-top:10px;font-size:14px;color:#3A4A6B;"><strong>Notice:</strong> %s</p>' % esc(w['notice']))
    parts.append('</div>')
    return '\n        '.join(parts)


def tool(t):
    parts = ['<div class="key-concept" style="background:#F0F7FF;border-color:#C8DCEE;margin-bottom:14px;">',
             '<div class="key-concept-label" style="color:#3D5285;">\U0001F4CB Today&rsquo;s Tool: %s</div>' % esc(t['title']),
             '<p style="font-size:15px;">%s</p>' % esc(t['intro'])]
    if 'table' in t:
        parts.append(table(t['table'], '#F0F7FF'))
    if 'filled' in t:
        parts.append('<ul style="margin:8px 0 0 18px;font-size:14px;line-height:1.6;">'
                     + ''.join('<li style="margin-bottom:4px;">%s</li>' % esc(x) for x in t['filled']) + '</ul>')
    if t.get('yourturn'):
        parts.append('<p style="margin-top:12px;margin-bottom:4px;font-size:14px;color:#3D5285;"><strong>Your turn:</strong></p>'
                     '<div style="background:#FAFBFF;border:2px dashed #BFC8E0;border-radius:8px;padding:12px 14px;font-size:14px;color:#3A4A6B;">%s</div>'
                     % esc(t['yourturn']))
    parts.append('</div>')
    return '\n        '.join(parts)


def render(k):
    c = C.CARDS[k]
    w = c['week']
    frames = ''.join('<li style="margin-bottom:4px;">%s</li>\n' % esc(f) for f in c['frames'])
    return '''<div class="activity bl-gold" id="writers-workshop">
    <div class="activity-head" style="background:linear-gradient(135deg,#FFF8F0,#FFF3DC);border-bottom-color:#F5E6C8;">
      <div class="activity-num" style="background:#C7922C;">✍️</div>
      <div>
        <div class="activity-title">Writer&rsquo;s Workshop: Week %(week)d &middot; %(label)s</div>
        <div class="activity-sub">%(sub)s</div>
      </div>
    </div>
    <div class="activity-body">
      %(strip)s
      <div class="callout callout-info" style="margin:0 0 12px 0;padding:10px 14px;"><span class="callout-icon">\U0001F3AF</span><p style="font-size:15px;"><strong>Today&rsquo;s focus:</strong> %(focus)s</p></div>
      <div class="callout callout-info" style="background:#FFF3F5;border-color:#F0C8D2;margin:0 0 14px 0;padding:10px 14px;"><span class="callout-icon">\U0001F4D6</span><p style="font-size:15px;"><strong>Anne did it too.</strong> %(anne)s</p></div>

      <!-- WATCH HOW -->
      %(watch)s

      <!-- TODAY'S TOOL -->
      %(tool)s

      <!-- SENTENCE FRAMES -->
      <div class="key-concept" style="background:#F0E8FF;border-color:#D8CCF0;margin-bottom:14px;">
        <div class="key-concept-label" style="color:#6B4FB0;">\U0001FAB6 Sentence Frames You Can Borrow</div>
        <p style="font-size:14px;margin-bottom:6px;">Stuck on how to start? Try one of these:</p>
        <ul style="margin:0 0 0 18px;font-size:15px;">
          %(frames)s        </ul>
      </div>

      <!-- MY STORY (persistent across all Anne lessons) -->
      <div class="key-concept" style="background:#FFFDF5;border:2px solid #C7922C;margin-bottom:14px;">
        <div class="key-concept-label" style="color:#C7922C;">\U0001F4D6 My Story</div>
        <p style="font-size:15px;margin-bottom:8px;"><strong>%(msday)s</strong> %(ms)s</p>
        <textarea class="journal-box my-story" id="my-story" data-label="My Story (draft so far)" rows="12" style="min-height:220px;font-size:15px;line-height:1.6;" placeholder="Your story lives here. It stays in this box from lesson to lesson." oninput="saveMyStory(this)"></textarea>
        <div style="display:flex;justify-content:space-between;font-size:13px;color:#7A88A8;margin-top:4px;"><span id="my-story-count">0 words</span><span>Goal: about one page, 200–300 words, five scenes</span></div>
      </div>

      <!-- NOW YOU TRY -->
      <div class="callout callout-info" style="background:#E8F1E8;border-color:#A8C8A8;margin:0 0 10px 0;padding:10px 14px;"><span class="callout-icon">\U0001F4DD</span><p style="font-size:15px;"><strong>Now you try.</strong> Use what Sam showed you. Borrow a sentence frame if you want.</p></div>
      <div class="textbox-prompt">%(prompt)s</div>
      <textarea class="journal-box" id="journal-writing" data-label="Writing Connection" placeholder="%(ph)s" oninput="autoSave(this,'dot-writing');gatherAnswers();"></textarea>
    </div>
  </div>''' % dict(
        week=w, label=C.WEEK_LABEL[w], sub=esc(c['sub']), strip=strip(w), focus=esc(c['focus']),
        anne=esc(c['anne']), watch=watch_how(c['watch']), tool=tool(c['tool']), frames=frames,
        msday='Week %d, Day %d.' % (w, c['day']), ms=esc(c['ms']), prompt=esc(c['prompt']),
        ph=H.escape(c['ph'], quote=True))


SCRIPT = '''<script id="%s">
/* OAO My Story: one draft box shared by every Anne-unit lesson (Weeks 7-14).
   Saved under a fixed key, not the per-lesson key, so it carries day to day. */
(function(){
  var KEY='%s';
  function wc(s){s=(s||'').trim();return s?s.split(/\\s+/).length:0;}
  window.updateMyStoryCount=function(el){var c=document.getElementById('my-story-count');if(c){c.textContent=wc(el.value)+' words';}};
  window.saveMyStory=function(el){
    try{localStorage.setItem(KEY,el.value);}catch(e){}
    updateMyStoryCount(el);
    if(typeof gatherAnswers==='function'){gatherAnswers();}
  };
  function load(){
    var t=document.getElementById('my-story'); if(!t) return;
    try{var v=localStorage.getItem(KEY); if(v!==null){t.value=v;}}catch(e){}
    updateMyStoryCount(t);
  }
  if(document.readyState==='loading'){document.addEventListener('DOMContentLoaded',load);}else{load();}
})();
</script>
''' % (SCRIPT_ID, MYSTORY_KEY)


def find_block(src):
    i = src.find('id="writers-workshop"')
    if i < 0:
        return None
    start = src.rfind('<div', 0, i)
    depth = 0
    for m in re.finditer(r'<div\b|</div>', src[start:]):
        depth += 1 if m.group().startswith('<div') else -1
        if depth == 0:
            return start, start + m.end()
    return None


def inject(path, card_html):
    src = open(path, encoding='utf-8').read()
    span = find_block(src)
    if not span:
        raise SystemExit('no workshop block in ' + path)
    src = src[:span[0]] + card_html + src[span[1]:]
    # gathered work: put my-story ahead of the daily box (both functions)
    src = src.replace("ids: ['journal-writing']", "ids: ['my-story','journal-writing']")
    # script once, before the last </body>
    if 'id="%s"' % SCRIPT_ID not in src:
        j = src.rfind('</body>')
        src = src[:j] + SCRIPT + src[j:]
    open(path, 'w', encoding='utf-8', newline='').write(src)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    dry = '--dry' in sys.argv
    repo = args[0] if args else '.'
    for k in sorted(C.CARDS):
        html_ = render(k)
        path = os.path.join(repo, C.FILES[k])
        if dry:
            print(k, C.FILES[k], len(html_), 'chars')
        else:
            inject(path, html_)
            print('wrote', C.FILES[k])


if __name__ == '__main__':
    main()
