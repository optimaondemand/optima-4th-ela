
/* ── Fill the Treasure Chamber (Prince Caspian, weeks 26–30; Bethany, Nov 19 2026).
   The children find the ruined castle's treasure chamber in Ch. 2: a dark vault with
   empty niches in its walls. Each right word part sets one treasure back in its niche,
   four a lesson, so a week of lessons fills all sixteen and the chamber's torches blaze.
   Same tap-or-drag mechanics as the quilt; generic treasures (no book illustrations). ── */
WORDGAME.treasure = function (cfg, act, game, W) {
  var day = dayNum(LESSON.day);
  var KEY = 'oao.g4ela.wg.' + LID;
  var placed = (Sparkle.get(KEY, []) || []).filter(function (i) { return i >= 0 && i < W.length; });
  var M = cfg.meanings || {};
  var stones = []; W.forEach(function (w) { if (stones.indexOf(w.a) < 0) stones.push(w.a); });
  game.classList.add('spk-hide');
  var lead = game.previousElementSibling;
  if (lead && lead.classList.contains('callout')) lead.classList.add('spk-hide');
  var PER = 4, base = (day - 1) * PER;
  /* sixteen generic treasures, drawn in a 40x40 box */
  var G = '#E9C46A', D = '#B8862B', R = '#B23A3A', B = '#3D6FB8', E = '#5E9E6B', S = '#D9DEE8';
  var T = [
    '<path d="M6 30 L10 14 L16 24 L20 10 L24 24 L30 14 L34 30 Z" fill="' + G + '" stroke="' + D + '"/><circle cx="20" cy="22" r="2.4" fill="' + R + '"/>',                       /* crown */
    '<path d="M12 6 h16 l-2 12 q-6 6 -12 0 Z" fill="' + G + '" stroke="' + D + '"/><rect x="18.5" y="19" width="3" height="10" fill="' + D + '"/><rect x="12" y="29" width="16" height="4" rx="2" fill="' + G + '"/>',  /* goblet */
    '<rect x="18.5" y="4" width="3" height="24" fill="' + S + '" stroke="#8A93A6"/><rect x="11" y="27" width="18" height="3" rx="1.5" fill="' + G + '"/><rect x="18" y="30" width="4" height="7" fill="' + D + '"/>',  /* sword */
    '<path d="M20 4 L33 9 Q33 26 20 36 Q7 26 7 9 Z" fill="' + B + '" stroke="' + G + '" stroke-width="2"/><path d="M20 10 v20 M12 17 h16" stroke="' + G + '" stroke-width="2"/>',              /* shield */
    '<ellipse cx="20" cy="30" rx="13" ry="4" fill="' + D + '"/><ellipse cx="14" cy="26" rx="5" ry="2" fill="' + G + '"/><ellipse cx="24" cy="24" rx="5" ry="2" fill="' + G + '"/><ellipse cx="19" cy="20" rx="5" ry="2" fill="' + G + '"/>',  /* coins */
    '<path d="M20 6 L30 16 L20 34 L10 16 Z" fill="' + E + '" stroke="#2E6B3B"/><path d="M10 16 h20 M20 6 L16 16 L20 34 L24 16 Z" fill="none" stroke="#BFE3C6" stroke-width=".8"/>',      /* gem */
    '<rect x="7" y="16" width="26" height="16" rx="2" fill="#8A5A33" stroke="' + D + '"/><path d="M7 16 q13 -12 26 0" fill="#A06A3A" stroke="' + D + '"/><rect x="18" y="20" width="4" height="5" fill="' + G + '"/>',  /* chest */
    '<circle cx="20" cy="22" r="9" fill="none" stroke="' + G + '" stroke-width="3.5"/><circle cx="20" cy="12" r="3.2" fill="' + R + '"/>',                                                    /* ring */
    '<path d="M9 26 Q9 8 20 8 Q31 8 31 26 Z" fill="' + S + '" stroke="#8A93A6"/><rect x="9" y="25" width="22" height="4" fill="' + G + '"/><path d="M18 14 h4 v8 h-4 Z" fill="#2A2F3A"/>',     /* helm */
    '<rect x="11" y="9" width="18" height="22" fill="#F2E6C8" stroke="' + D + '"/><circle cx="11" cy="9" r="3" fill="' + D + '"/><circle cx="29" cy="31" r="3" fill="' + D + '"/><path d="M15 15 h10 M15 19 h10 M15 23 h7" stroke="#A88B57"/>',  /* scroll */
    '<path d="M12 34 L12 10 Q22 4 30 14 L30 34 Z" fill="none" stroke="' + G + '" stroke-width="2.5"/><path d="M15 12 v20 M19 10 v22 M23 10 v22 M27 13 v19" stroke="#F4E3B0" stroke-width=".8"/>',  /* harp */
    '<path d="M12 22 q8 -8 16 0 l-2 8 h-12 Z" fill="' + G + '" stroke="' + D + '"/><path d="M28 24 q6 0 5 -5" fill="none" stroke="' + D + '" stroke-width="2"/><path d="M20 14 q3 -4 0 -8 q-3 4 0 8" fill="#F2A54A"/>',  /* lamp */
    '<circle cx="13" cy="20" r="6" fill="none" stroke="' + G + '" stroke-width="3"/><path d="M19 20 h15 M29 20 v5 M33 20 v4" stroke="' + G + '" stroke-width="3"/>',                         /* key */
    '<path d="M20 4 q10 6 6 14 q-2 4 -6 4" fill="none" stroke="' + G + '" stroke-width="2.5"/><path d="M8 30 q12 -16 24 0" fill="none" stroke="' + D + '" stroke-width="3"/><path d="M14 28 L26 20" stroke="' + S + '" stroke-width="1.5"/>',  /* bow */
    '<rect x="18" y="8" width="4" height="24" fill="' + G + '"/><rect x="12" y="30" width="16" height="4" rx="2" fill="' + D + '"/><path d="M20 3 q3 3 0 6 q-3 -3 0 -6" fill="#F2A54A"/>',      /* candlestick */
    '<path d="M8 10 Q20 34 32 10" fill="none" stroke="' + G + '" stroke-width="2.5"/><circle cx="20" cy="25" r="4" fill="' + B + '" stroke="' + G + '"/><circle cx="13" cy="19" r="2" fill="' + R + '"/><circle cx="27" cy="19" r="2" fill="' + R + '"/>'  /* necklace */
  ];
  var ORDER = [5, 10, 0, 15, 2, 13, 7, 8, 1, 14, 4, 11, 3, 12, 6, 9];
  var NW = 52, NH = 44, X0 = 216, Y0 = 34, GX = 4, GY = 6, pts = '';
  ORDER.forEach(function (si, k) {
    var x = X0 + (si % 4) * (NW + GX), y = Y0 + Math.floor(si / 4) * (NH + GY);
    pts += '<g class="pt" data-k="' + k + '" transform="translate(' + x + ' ' + y + ')">' +
      '<path class="bk" d="M0 ' + NH + ' V14 Q' + (NW / 2) + ' -4 ' + NW + ' 14 V' + NH + ' Z"/>' +
      '<g class="fab" transform="translate(' + ((NW - 40) / 2) + ' 4)">' + T[si] + '</g></g>';
  });
  var bricks = '';
  for (var r = 0; r < 12; r++) for (var c = 0; c < 12; c++) bricks += '<rect class="bkk" x="' + (c * 56 - (r % 2) * 28) + '" y="' + (r * 22) + '" width="54" height="20" rx="2"/>';
  var torch = function (x) {
    return '<g class="torch" transform="translate(' + x + ' 70)"><rect x="-3" y="0" width="6" height="34" fill="#5A3A22"/><rect x="-7" y="-2" width="14" height="6" rx="2" fill="#3A2A1E"/>' +
      '<path class="fl" d="M0 -26 q10 12 0 24 q-10 -12 0 -24" /></g>';
  };
  var svg =
    '<svg class="spk-tr-svg" viewBox="0 0 640 260" role="img" aria-label="A dark stone treasure chamber. Sixteen empty niches wait in the wall for their treasures.">' +
    '<defs><radialGradient id="spkTrGlow" cx="50%" cy="40%" r="60%"><stop offset="0" stop-color="#F2B65A" stop-opacity=".45"/><stop offset="1" stop-color="#F2B65A" stop-opacity="0"/></radialGradient></defs>' +
    '<rect width="640" height="260" fill="#25211F"/><g class="bricks">' + bricks + '</g>' +
    '<rect class="glow" width="640" height="260" fill="url(#spkTrGlow)"/>' +
    '<path class="arch" d="M196 238 V40 Q' + (X0 + 2 * (NW + GX)) + ' -14 444 40 V238"/>' +
    '<g class="pts">' + pts + '</g>' + torch(150) + torch(490) +
    '<rect class="floor" x="0" y="238" width="640" height="22"/>' +
    '</svg>';
  var box = document.createElement('div');
  box.className = 'spk-wg spk-treasure';
  box.innerHTML =
    '<div class="spk-wg-head"><span class="spk-wg-kicker">' + esc(cfg.kicker || 'Fill the Treasure Chamber') + '</span>' +
      '<span class="spk-wg-h">' + esc(cfg.h || 'One treasure at a time') + '</span></div>' +
    wgWhy(cfg.why) +
    (cfg.voice ? '<p class="spk-wg-voice">' + esc(cfg.voice) + '</p>' : '') +
    '<div class="spk-tr-scene">' + svg + '</div>' +
    '<p class="spk-wg-ct" aria-live="polite"></p>' +
    '<div class="spk-br-stones" role="group" aria-label="Word parts">' +
      stones.map(function (a) {
        return '<button type="button" class="spk-br-stone" data-a="' + esc(a) + '"><b>' + esc(a) + '</b>' +
               (M[a] ? '<small>' + esc(M[a]) + '</small>' : '') + '</button>';
      }).join('') + '</div>' +
    '<div class="spk-br-pile">' +
      W.map(function (w, i) {
        var pre = '', post = '', seen = false;
        [].forEach.call(w.inp.parentNode.childNodes, function (n) {
          if (n === w.inp) { seen = true; return; }
          var t = n.textContent || ''; if (seen) post += t; else pre += t;
        });
        post = post.split(/\s+[—–-]\s+/)[0].trim(); pre = pre.trim();
        return '<button type="button" class="spk-br-card" data-i="' + i + '">' +
               '<span class="w">' + (pre ? '<b>' + esc(pre) + '</b>' : '') + '<span class="blank">?</span>' + (post ? '<b>' + esc(post) + '</b>' : '') + '</span>' +
               '<small>' + esc(w.m) + '</small><span class="spk-wg-miss"></span></button>';
      }).join('') + '</div>' +
    '<div class="spk-wg-win" hidden></div>';
  game.parentNode.insertBefore(box, game);
  function paint(fresh) {
    var put = base + (placed.length === W.length ? PER : Math.min(PER, placed.length));
    box.querySelectorAll('.pt').forEach(function (el) {
      var k = +el.getAttribute('data-k');
      el.classList.toggle('on', k < put); el.classList.toggle('old', k < base);
      if (fresh && k === put - 1 && !REDUCED) { el.classList.remove('pop'); void el.getBoundingClientRect(); el.classList.add('pop'); }
    });
  }
  function count() {
    var n = placed.length;
    box.querySelector('.spk-wg-ct').innerHTML = n < W.length
      ? '<b>' + n + ' of ' + W.length + '</b> treasures back in place' + (day > 1 ? ' · lesson ' + day + ' of 4' : '') + '.' : '';
  }
  function setCard(i) {
    var w = W[i], card = box.querySelector('.spk-br-card[data-i="' + i + '"]');
    card.classList.add('placed'); card.disabled = true;
    card.querySelector('.blank').textContent = w.a;
    card.querySelector('.spk-wg-miss').innerHTML = '';
  }
  function finish(quiet) {
    W.forEach(function (w) { w.inp.value = w.a; });
    var btn = game.querySelector('.fillin-check-btn');
    try { if (quiet) _origCheckFillIn(btn); else window.checkFillIn(btn); } catch (e) {}
    var last = day >= 4, win = box.querySelector('.spk-wg-win');
    win.hidden = false;
    win.innerHTML = last ? (cfg.win || 'The chamber is full again, and every torch is lit.')
                         : (cfg.winDay || 'Four more treasures are back in their niches.');
    box.classList.add('done'); if (last) box.classList.add('free');
    paint(false);
    if (!quiet) setTimeout(function () { wgSfx('win'); }, 350);
  }
  function miss(i, a) {
    var w = W[i], card = box.querySelector('.spk-br-card[data-i="' + i + '"]');
    var line = (cfg.miss || {})[w.id] ||
      ('Not quite. Try <b>' + esc(a) + '</b> in the blank and read the word out loud. Does it look like a word you know? Read the meaning again: <i>' + esc(w.m) + '</i>.');
    card.querySelector('.spk-wg-miss').innerHTML = line;
    card.classList.remove('nope'); void card.offsetWidth; card.classList.add('nope');
    wgSfx('bonk');
  }
  var selStone = null, selCard = null;
  function clearSel() { selStone = selCard = null; box.querySelectorAll('.sel').forEach(function (e) { e.classList.remove('sel'); }); }
  function tryPlace(i, a) {
    if (placed.indexOf(i) >= 0) return;
    if (W[i].a === a) {
      placed.push(i); Sparkle.set(KEY, placed);
      setCard(i); paint(true); wgSfx('chime'); count();
      if (placed.length === W.length) finish(false);
    } else miss(i, a);
    clearSel();
  }
  box.querySelectorAll('.spk-br-stone').forEach(function (b) {
    b.addEventListener('click', function () {
      if (b._dragged) { b._dragged = false; return; }
      var a = b.getAttribute('data-a');
      if (selCard !== null) { tryPlace(selCard, a); return; }
      var on = selStone !== a; clearSel(); if (on) { selStone = a; b.classList.add('sel'); }
    });
    b.addEventListener('pointerdown', function (e) {
      if (e.button) return;
      var a = b.getAttribute('data-a'), sx = e.clientX, sy = e.clientY, ghost = null;
      function move(ev) {
        if (!ghost && Math.abs(ev.clientX - sx) + Math.abs(ev.clientY - sy) < 8) return;
        if (!ghost) { ghost = b.cloneNode(true); ghost.className = 'spk-br-stone spk-br-ghost'; document.body.appendChild(ghost); }
        ghost.style.left = ev.clientX + 'px'; ghost.style.top = ev.clientY + 'px';
        box.querySelectorAll('.spk-br-card.over').forEach(function (c) { c.classList.remove('over'); });
        var t = document.elementFromPoint(ev.clientX, ev.clientY), c = t && t.closest && t.closest('.spk-br-card');
        if (c && !c.disabled) c.classList.add('over');
        ev.preventDefault();
      }
      function up(ev) {
        document.removeEventListener('pointermove', move); document.removeEventListener('pointerup', up);
        if (!ghost) return;
        ghost.remove(); b._dragged = true; setTimeout(function () { b._dragged = false; }, 50);
        box.querySelectorAll('.spk-br-card.over').forEach(function (c) { c.classList.remove('over'); });
        var t = document.elementFromPoint(ev.clientX, ev.clientY), c = t && t.closest && t.closest('.spk-br-card');
        if (c && !c.disabled) tryPlace(+c.getAttribute('data-i'), a);
      }
      document.addEventListener('pointermove', move, { passive: false });
      document.addEventListener('pointerup', up);
    });
  });
  box.querySelectorAll('.spk-br-card').forEach(function (c) {
    c.addEventListener('click', function () {
      var i = +c.getAttribute('data-i');
      if (selStone) { tryPlace(i, selStone); return; }
      var on = selCard !== i; clearSel(); if (on) { selCard = i; c.classList.add('sel'); }
    });
  });
  placed.forEach(setCard);
  paint(false); count();
  if (placed.length === W.length) finish(true);
};
