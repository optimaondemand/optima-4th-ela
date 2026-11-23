  /* ── Window Seat Day game: choose ──
     One question at a time, three answers. A right pick shows why and moves on; a wrong one crosses out and nudges. */
  var GAME = (function () {
    var G = D.game, $ = KIT.$, $$ = KIT.$$, esc = KIT.esc;
    var st = KIT.get('game', { got: [] });   /* got[i] = true once question i is right */
    function complete() { return G.qs.every(function (_, i) { return st.got[i]; }); }
    function save() { KIT.set('game', st); }
    function render() {
      $('#choose').innerHTML = G.qs.map(function (q, i) {
        var got = !!st.got[i], open = got || G.qs.slice(0, i).every(function (_, k) { return st.got[k]; });
        if (!open) return '<div class="cq lock"><small>Question ' + (i + 1) + '</small><span>Finish the one above first.</span></div>';
        return '<div class="cq' + (got ? ' got' : '') + '"><small>Question ' + (i + 1) + ' of ' + G.qs.length + '</small><div class="cq-q">' + esc(q.q) + '</div><div class="copts">' +
          q.opts.map(function (o, k) { return '<button type="button" class="copt' + (got && k === q.ok ? ' ok' : '') + '" data-i="' + i + '" data-k="' + k + '"' + (got ? ' disabled' : '') + '>' + esc(o) + '</button>'; }).join('') +
          '</div>' + (got ? '<div class="cwhy">✓ ' + esc(q.why) + '</div>' : '') + '</div>';
      }).join('');
      $$('.copt').forEach(function (b) { b.addEventListener('click', function () {
        var i = +b.dataset.i, k = +b.dataset.k;
        if (k === G.qs[i].ok) { st.got[i] = true; save(); KIT.ding(); KIT.say(complete() ? '✓ All answered! Now plan your 2 sentences.' : '✓ Yes.', true); if (complete()) KIT.fanfare(); }
        else { KIT.bonk(); b.classList.add('no'); KIT.say(G.miss); return; }
        render();
      }); });
      KIT.done(complete()); KIT.refresh();
    }
    return { render: render, complete: complete };
  })();
