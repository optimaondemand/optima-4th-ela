#!/usr/bin/env python3
"""Add WORDGAME.treasure (Fill the Treasure Chamber) and the Seven Pillars Watch (virtue kind 'pillars') to the G4 layer.
Run from the repo root once:  python3 tools/patch_layer_pc.py"""
import io, sys
js = io.open('sparkle.js', encoding='utf-8').read(); css = io.open('sparkle.css', encoding='utf-8').read()
if 'WORDGAME.treasure' in js: sys.exit('already patched')
TJ = io.open(sys.argv[1], encoding='utf-8').read(); TC = io.open(sys.argv[2], encoding='utf-8').read()
a = '\nfunction buildWordGame() {'
assert js.count(a) == 1; js = js.replace(a, TJ + a)
PIL = r"""  } else if (V.kind === 'pillars') {   /* Seven Pillars Watch (Prince Caspian): which pillar does each moment show? */
    mine.pil = mine.pil || {};
    var P = V.pillars || ['Honesty', 'Respect', 'Courtesy', 'Responsibility', 'Courage', 'Service', 'Perseverance'];
    V.items.forEach(function (it, i) {
      var r = el('div', 'g4-virtue-row'); r.appendChild(el('p', 'g4-virtue-moment', it.t));
      var btns = el('div', 'g4-virtue-btns g4-virtue-pils'), fb = el('p', 'g4-virtue-fb'); fb.setAttribute('aria-live', 'polite');
      P.forEach(function (p) {
        var b = el('button', 'g4-virtue-btn g4-virtue-pil', '👆 ' + p); b.type = 'button'; b.setAttribute('data-p', p);
        b.onclick = function () { mine.pil[i] = p; show(); save(); };
        btns.appendChild(b);
      });
      function show() {
        var a = mine.pil[i]; if (!a) return;
        var ok = (it.ok || []).indexOf(a) >= 0;
        [].forEach.call(btns.children, function (b) { b.setAttribute('aria-pressed', b.getAttribute('data-p') === a ? 'true' : 'false'); });
        fb.className = 'g4-virtue-fb ' + (ok ? 'ok' : 'no'); fb.textContent = ok ? '✓ Yes. ' + it.why : 'Look again. ' + (it.hint || 'Which pillar does this moment show most?');
      }
      r.appendChild(btns); r.appendChild(fb); card.appendChild(r); show();
    });
    if (V.line) { card.appendChild(el('p', 'g4-virtue-q', V.line)); card.appendChild(lineBox(V.placeholder)); }
"""
b = "  } else if (V.kind === 'log') {"
assert js.count(b) == 1; js = js.replace(b, PIL + b)
c = "      if (V.kind === 'sort') V.items.forEach(function (it, i) { if (mine.sort && mine.sort[i] !== undefined) t += (mine.sort[i] === it.ok ? '✅ ' : '⬜ ') + it.t + '\\n'; });"
assert js.count(c) == 1, 'gather'
js = js.replace(c, c + "\n      else if (V.kind === 'pillars') { V.items.forEach(function (it, i) { if (mine.pil && mine.pil[i]) t += ((it.ok || []).indexOf(mine.pil[i]) >= 0 ? '✅ ' : '⬜ ') + mine.pil[i] + ': ' + it.t + '\\n'; }); if (mine.why && mine.why.trim()) t += mine.why.trim() + '\\n'; }")
css += '\n' + TC + "\n/* Seven Pillars Watch (Prince Caspian) */\n.g4-virtue-pils { flex-wrap:wrap; gap:6px; }\n.g4-virtue-pil { font-size:14px; padding:6px 10px; }\n"
io.open('sparkle.js', 'w', encoding='utf-8').write(js); io.open('sparkle.css', 'w', encoding='utf-8').write(css)
print('patched')
