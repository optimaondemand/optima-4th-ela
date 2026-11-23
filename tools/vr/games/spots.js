  /* ── Window Seat Day game: spots ──
     A board of named places. Tap a thing, then tap the place where the chapter puts it. */
  var GAME = (function () {
    var G = D.game, $ = KIT.$, $$ = KIT.$$, esc = KIT.esc;
    var st = KIT.get('game', { put: {} });   /* put[itemIndex] = spotIndex once right */
    var pick = null;
    function complete() { return G.items.every(function (_, i) { return st.put[i] !== undefined; }); }
    function save() { KIT.set('game', st); }
    function render() {
      $('#board').innerHTML = G.spots.map(function (s, k) {
        var inside = G.items.map(function (it, i) { return st.put[i] === k ? i : -1; }).filter(function (i) { return i >= 0; });
        return '<button type="button" class="spot" data-s="' + k + '"><span class="spic">' + s.ic + '</span><b>' + esc(s.name) + '</b><span class="spin">' + inside.map(function (i) { return '<em>' + (G.items[i].ic || '✓') + ' ' + esc(G.items[i].t) + '</em>'; }).join('') + '</span></button>';
      }).join('');
      $('#things').innerHTML = G.items.map(function (it, i) {
        var got = st.put[i] !== undefined;
        return '<button type="button" class="thing' + (got ? ' got' : '') + (pick === i ? ' pick' : '') + '" data-i="' + i + '"' + (got ? ' disabled' : '') + '>' + (it.ic ? '<span class="spic">' + it.ic + '</span>' : '') + '<span>' + esc(it.t) + '</span></button>';
      }).join('');
      $('#spot-why').innerHTML = Object.keys(st.put).map(function (i) { return '<li>✓ <b>' + esc(G.items[i].t) + '</b>: ' + esc(G.items[i].why) + '</li>'; }).join('');
      $$('.thing').forEach(function (b) { b.addEventListener('click', function () { pick = +b.dataset.i; KIT.ding(); render(); }); });
      $$('.spot').forEach(function (b) { b.addEventListener('click', function () {
        if (pick === null) { KIT.say('First tap a thing from the list.'); return; }
        var k = +b.dataset.s;
        if (G.items[pick].spot === k) { st.put[pick] = k; save(); pick = null; KIT.ding(); KIT.say(complete() ? '✓ Everything is in its place! Now plan your 2 sentences.' : '✓ Right where the chapter puts it.', true); if (complete()) KIT.fanfare(); }
        else { KIT.bonk(); b.classList.add('shake'); setTimeout(function () { b.classList.remove('shake'); }, 400); KIT.say(G.miss); return; }
        render();
      }); });
      KIT.done(complete()); KIT.refresh();
    }
    return { render: render, complete: complete };
  })();
