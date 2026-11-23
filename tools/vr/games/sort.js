  /* ── Window Seat Day game: sort ──
     One card at a time. Tap the bin it belongs in. A right pick files it and shows why; a wrong one nudges. */
  var GAME = (function () {
    var G = D.game, $ = KIT.$, $$ = KIT.$$, esc = KIT.esc;
    var st = KIT.get('game', { done: [] });   /* done = card indexes filed, in order */
    function complete() { return st.done.length === G.cards.length; }
    function save() { KIT.set('game', st); }
    function next() { for (var i = 0; i < G.cards.length; i++) if (st.done.indexOf(i) < 0) return i; return -1; }
    function render() {
      var host = $('#sort'), i = next();
      host.innerHTML = '<div class="sdeck">' + (i < 0 ? '<div class="scard done">✓ Every card is sorted.</div>' : '<div class="scard"><small>Card ' + (st.done.length + 1) + ' of ' + G.cards.length + '</small>' + esc(G.cards[i].t) + '</div>') + '</div>' +
        '<div class="sbins">' + G.bins.map(function (b, k) {
          var inb = st.done.filter(function (c) { return G.cards[c].bin === k; });
          return '<div class="sbin"><button type="button" class="sbin-b" data-b="' + k + '"' + (i < 0 ? ' disabled' : '') + '><span class="sic">' + b.ic + '</span>' + esc(b.name) + '</button><ul class="sin">' + inb.map(function (c) { return '<li><b>' + esc(G.cards[c].t) + '</b><br><span>' + esc(G.cards[c].why) + '</span></li>'; }).join('') + '</ul></div>';
        }).join('') + '</div>';
      $$('.sbin-b', host).forEach(function (b) { b.addEventListener('click', function () {
        var k = +b.dataset.b, c = next(); if (c < 0) return;
        if (G.cards[c].bin === k) { st.done.push(c); save(); KIT.ding(); KIT.say(complete() ? '✓ All sorted! Now plan your 2 sentences.' : '✓ Filed under ' + G.bins[k].name + '.', true); if (complete()) KIT.fanfare(); }
        else { KIT.bonk(); b.classList.add('shake'); setTimeout(function () { b.classList.remove('shake'); }, 400); KIT.say(G.miss); return; }
        render();
      }); });
      KIT.done(complete()); KIT.refresh();
    }
    return { render: render, complete: complete };
  })();
