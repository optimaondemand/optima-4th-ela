  /* ── Window Seat Day game: rename-order ──
     Part 1: pick Anne's name for each plain place name (3 choices, one try at a time).
     Part 2: tap the stops in story order; each lands on the next milestone of the road. */
  var GAME = (function () {
    var G = D.game, $ = KIT.$, $$ = KIT.$$, esc = KIT.esc;
    var st = KIT.get('game', { ren: [], ord: [] });   /* ren[i] = chosen index once right; ord = placed stop indexes */
    var deck = (function () { var a = G.order.map(function (_, i) { return i; }), s = 7; for (var i = a.length - 1; i > 0; i--) { s = (s * 9301 + 49297) % 233280; var j = Math.floor(s / 233280 * (i + 1)), t = a[i]; a[i] = a[j]; a[j] = t; } if (a.join() === G.order.map(function (_, i) { return i; }).join()) a.reverse(); return a; })();
    function renDone() { return G.rename.every(function (r, i) { return st.ren[i] === r.ok; }); }
    function ordDone() { return st.ord.length === G.order.length; }
    function complete() { return renDone() && ordDone(); }
    function save() { KIT.set('game', st); }

    function renderRename() {
      $('#ren').innerHTML = G.rename.map(function (r, i) {
        var got = st.ren[i] === r.ok;
        return '<div class="ren' + (got ? ' got' : '') + '"><div class="ren-q"><span class="ren-plain">' + esc(r.plain) + '</span><small>' + esc(r.hint) + '</small></div><div class="ren-opts">' +
          r.opts.map(function (o, k) { return '<button type="button" class="ropt' + (got && k === r.ok ? ' ok' : '') + '" data-i="' + i + '" data-k="' + k + '"' + (got ? ' disabled' : '') + '>' + esc(o) + '</button>'; }).join('') +
          '</div>' + (got ? '<div class="ren-why">✓ ' + esc(r.why) + '</div>' : '') + '</div>';
      }).join('');
      $$('.ropt', $('#ren')).forEach(function (b) { b.addEventListener('click', function () {
        var i = +b.dataset.i, k = +b.dataset.k, r = G.rename[i];
        if (k === r.ok) { st.ren[i] = k; save(); KIT.ding(); KIT.say('✓ Yes! Anne calls ' + r.plain + ' “' + r.opts[k] + '.”', true); }
        else { KIT.bonk(); b.classList.add('no'); KIT.say('Not that one. Anne’s name for ' + r.plain + ' shows how it made her feel. Try again.'); return; }
        render();
      }); });
    }
    function renderOrder() {
      var road = $('#road'), n = G.order.length;
      $('#mile').innerHTML = G.order.map(function (_, i) {
        var k = st.ord[i], on = k !== undefined;
        return '<li class="ms' + (on ? ' on' : '') + (i === st.ord.length ? ' next' : '') + '"><span class="ms-n">' + (i + 1) + '</span>' + (on ? '<span class="ms-ic">' + G.order[k].ic + '</span><b>' + esc(G.order[k].t) + '</b>' : '<i>?</i>') + '</li>';
      }).join('');
      road.style.setProperty('--fill', (st.ord.length / n * 100) + '%');
      $('#stops').innerHTML = deck.map(function (k) {
        var used = st.ord.indexOf(k) > -1, o = G.order[k];
        return '<button type="button" class="stop' + (used ? ' used' : '') + '" data-k="' + k + '"' + (used || !renDone() ? ' disabled' : '') + '><span class="s-ic">' + o.ic + '</span><span><b>' + esc(o.t) + '</b><small>' + esc(o.s) + '</small></span></button>';
      }).join('');
      $('#order-lock').hidden = renDone();
      $$('.stop', $('#stops')).forEach(function (b) { b.addEventListener('click', function () {
        var k = +b.dataset.k;
        if (k === st.ord.length) { st.ord.push(k); save(); KIT.ding(); KIT.say(ordDone() ? '✓ The whole drive, in order! Now plan your 2 sentences.' : '✓ Stop ' + st.ord.length + ' is on the road.', true); if (ordDone()) KIT.fanfare(); }
        else { KIT.bonk(); b.classList.add('shake'); setTimeout(function () { b.classList.remove('shake'); }, 400); KIT.say(G.orderMiss); return; }
        render();
      }); });
    }
    function render() { renderRename(); renderOrder(); KIT.done(complete()); KIT.refresh(); }
    function text() {
      return 'Rename it like Anne:\n' + G.rename.map(function (r, i) { return '  ' + r.plain + ' → ' + (st.ren[i] === r.ok ? r.opts[r.ok] : '(not done yet)'); }).join('\n') +
        '\n\nThe drive, in order (' + st.ord.length + ' of ' + G.order.length + '):\n' + (st.ord.length ? st.ord.map(function (k, i) { return '  ' + (i + 1) + '. ' + G.order[k].t; }).join('\n') : '  (none yet)');
    }
    function html() {
      return '<h2>Rename it like Anne</h2><table><tr><th>Plain name</th><th>Anne’s name</th></tr>' + G.rename.map(function (r, i) { return '<tr><td>' + esc(r.plain) + '</td><td>' + (st.ren[i] === r.ok ? esc(r.opts[r.ok]) : '<i>not done yet</i>') + '</td></tr>'; }).join('') + '</table>' +
        '<h2>The drive, in order: ' + st.ord.length + ' of ' + G.order.length + '</h2><table><tr><th>#</th><th>Stop</th><th>What happens</th></tr>' + G.order.map(function (o, i) { var k = st.ord[i]; return '<tr><td>' + (i + 1) + '</td><td>' + (k !== undefined ? esc(G.order[k].t) : '<i>not placed yet</i>') + '</td><td>' + (k !== undefined ? esc(G.order[k].s) : '') + '</td></tr>'; }).join('') + '</table>';
    }
    return { render: render, text: text, html: html, complete: complete };
  })();
