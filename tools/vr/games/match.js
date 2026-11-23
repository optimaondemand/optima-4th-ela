  /* ── Window Seat Day game: match ──
     Tap a card on the left, then the card on the right that goes with it. A right match locks the pair and shows why. */
  var GAME = (function () {
    var G = D.game, $ = KIT.$, $$ = KIT.$$, esc = KIT.esc;
    var st = KIT.get('game', { got: [] });   /* got = indexes of pairs matched */
    var pick = null;
    var order = (function () { var a = G.pairs.map(function (_, i) { return i; }), s = 11; for (var i = a.length - 1; i > 0; i--) { s = (s * 9301 + 49297) % 233280; var j = Math.floor(s / 233280 * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } if (a.join() === G.pairs.map(function (_, i) { return i; }).join()) a.reverse(); return a; })();
    function complete() { return st.got.length === G.pairs.length; }
    function save() { KIT.set('game', st); }
    function render() {
      var host = $('#match');
      host.innerHTML = '<div class="mcol"><div class="mlbl">' + esc(G.leftLabel) + '</div>' + G.pairs.map(function (p, i) {
        var got = st.got.indexOf(i) > -1;
        return '<button type="button" class="mc' + (got ? ' got' : '') + (pick === i ? ' pick' : '') + '" data-l="' + i + '"' + (got ? ' disabled' : '') + '>' + (p.ic ? '<span class="mic">' + p.ic + '</span>' : '') + '<span>' + esc(p.a) + '</span></button>';
      }).join('') + '</div><div class="mcol"><div class="mlbl">' + esc(G.rightLabel) + '</div>' + order.map(function (i) {
        var got = st.got.indexOf(i) > -1;
        return '<button type="button" class="mc r' + (got ? ' got' : '') + '" data-r="' + i + '"' + (got ? ' disabled' : '') + '><span>' + esc(G.pairs[i].b) + '</span></button>';
      }).join('') + '</div>';
      $('#match-why').innerHTML = st.got.map(function (i) { return '<li>✓ <b>' + esc(G.pairs[i].a) + '</b>: ' + esc(G.pairs[i].why) + '</li>'; }).join('');
      $$('[data-l]', host).forEach(function (b) { b.addEventListener('click', function () { pick = +b.dataset.l; KIT.ding(); render(); }); });
      $$('[data-r]', host).forEach(function (b) { b.addEventListener('click', function () {
        if (pick === null) { KIT.say('First tap a card on the left.'); return; }
        var r = +b.dataset.r;
        if (r === pick) { st.got.push(r); save(); pick = null; KIT.ding(); KIT.say(complete() ? '✓ All matched! Now plan your 2 sentences.' : '✓ That’s a match.', true); if (complete()) KIT.fanfare(); }
        else { KIT.bonk(); b.classList.add('shake'); setTimeout(function () { b.classList.remove('shake'); }, 400); KIT.say(G.miss); return; }
        render();
      }); });
      KIT.done(complete()); KIT.refresh();
    }
    return { render: render, complete: complete };
  })();
