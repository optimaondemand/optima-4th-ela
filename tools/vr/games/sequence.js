  /* ── Window Seat Day game: sequence ──
     Tap the events in story order. Each right tap fills the next rung of the ladder. */
  var GAME = (function () {
    var G = D.game, $ = KIT.$, $$ = KIT.$$, esc = KIT.esc;
    var st = KIT.get('game', { ord: [] });
    var deck = (function () { var a = G.events.map(function (_, i) { return i; }), s = 5; for (var i = a.length - 1; i > 0; i--) { s = (s * 9301 + 49297) % 233280; var j = Math.floor(s / 233280 * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } if (a.join() === G.events.map(function (_, i) { return i; }).join()) a.reverse(); return a; })();
    function complete() { return st.ord.length === G.events.length; }
    function save() { KIT.set('game', st); }
    function render() {
      $('#ladder').innerHTML = G.events.map(function (_, i) {
        var k = st.ord[i], on = k !== undefined;
        return '<li class="rung' + (on ? ' on' : '') + (i === st.ord.length ? ' next' : '') + '"><span class="rn">' + (i + 1) + '</span>' + (on ? '<span class="ric">' + G.events[k].ic + '</span><b>' + esc(G.events[k].t) + '</b>' : '<i>?</i>') + '</li>';
      }).join('');
      $('#deck').innerHTML = deck.map(function (k) {
        var used = st.ord.indexOf(k) > -1, o = G.events[k];
        return '<button type="button" class="ev' + (used ? ' used' : '') + '" data-k="' + k + '"' + (used ? ' disabled' : '') + '><span class="ric">' + o.ic + '</span><span><b>' + esc(o.t) + '</b><small>' + esc(o.s) + '</small></span></button>';
      }).join('');
      $$('.ev', $('#deck')).forEach(function (b) { b.addEventListener('click', function () {
        var k = +b.dataset.k;
        if (k === st.ord.length) { st.ord.push(k); save(); KIT.ding(); KIT.say(complete() ? '✓ The whole chapter, in order! Now plan your 2 sentences.' : '✓ That’s number ' + st.ord.length + '.', true); if (complete()) KIT.fanfare(); }
        else { KIT.bonk(); b.classList.add('shake'); setTimeout(function () { b.classList.remove('shake'); }, 400); KIT.say(G.miss); return; }
        render();
      }); });
      KIT.done(complete()); KIT.refresh();
    }
    return { render: render, complete: complete };
  })();
