/* ═══════════════════════════════════════════════════════════════════
   OAO Freedom Train Kit · weeks 20–25 (Dorothy Sterling, Freedom Train)

   1. The opening (same on every Freedom Train lesson; Bethany, 27 Oct
      2026). Old Rit's patchwork quilt fills the screen, the camera
      sinks into one dark square, and the square becomes a night sky:
      the Big Dipper comes out, its two pointer stars draw a line to
      the North Star, and a trail of small lights runs north through
      the trees. No words. About 8 seconds, once per lesson per browser
      session, skippable (button, click, Enter, Space, Esc), a Replay
      button in the header, and a still picture (no autoplay) under
      prefers-reduced-motion. ?intro forces it; ?nointro and automated
      test browsers skip the autoplay. Modelled on the math layer's
      pq-intro.js, painted rather than pixelled to match the ELA page.

   2. Songs with a hidden meaning. The spirituals in the book, short
      traditional (public-domain) lines only, with what the overseer
      heard beside what the singers meant, taken from what Sterling's
      chapter itself shows. One card after the reading, only on the
      lessons whose DATA.ft.songs lists songs.

   OAOFtKit.intro({ base })            plays / arms the opening
   OAOFtKit.mount('songs', host, { cfg: DATA.ft })
   Every part removes itself when what it needs is missing.
   ═══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var KIT = window.OAOFtKit = window.OAOFtKit || {};

  function esc(s) { return String(s == null ? '' : s).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  function clamp(v) { return v < 0 ? 0 : v > 1 ? 1 : v; }
  function P(t, a, b) { return clamp((t - a) / (b - a)); }
  function ease(p) { p = clamp(p); return p < .5 ? 4 * p * p * p : 1 - Math.pow(-2 * p + 2, 3) / 2; }
  function q(n) { try { return new URLSearchParams(location.search).has(n); } catch (e) { return false; } }
  function reduced() { try { return matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) { return false; } }

  var CSS = ''
  /* opening */
  + '.ftk-intro{position:fixed;inset:0;z-index:2147483000;background:#0B1430;cursor:pointer;opacity:1;transition:opacity .7s ease;}'
  + '.ftk-intro.out{opacity:0;}'
  + '.ftk-intro canvas{display:block;width:100%;height:100%;}'
  + '.ftk-intro .sr{position:absolute;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);}'
  + '.ftk-skip{position:absolute;right:18px;bottom:18px;font:800 14px "Nunito",sans-serif;color:#FFF3D6;background:rgba(14,28,66,.55);border:2px solid rgba(255,243,214,.55);border-radius:999px;padding:8px 18px;cursor:pointer;}'
  + '.ftk-skip:hover,.ftk-skip:focus-visible{background:rgba(14,28,66,.85);border-color:#F3D27A;outline:none;}'
  + 'body.ftk-on{overflow:hidden;}'
  + '.ftk-replay{font:800 12px "Nunito",sans-serif;color:#0E1C42;background:#FFF8E9;border:2px solid #E7D3A4;border-radius:999px;padding:5px 12px;cursor:pointer;margin-left:10px;white-space:nowrap;}'
  + '.ftk-replay:hover,.ftk-replay:focus-visible{border-color:#C7922C;outline:none;}'
  /* songs */
  + '.ftk-card{background:#fff;border:1px solid #E6EBF5;border-radius:12px;overflow:hidden;margin:18px 0;box-shadow:0 1px 4px rgba(14,28,66,.05);border-left:5px solid #7A5A2A;font-family:"Lora",Georgia,serif;color:#0E1C42;}'
  + '.ftk-head{display:flex;gap:12px;align-items:center;padding:12px 18px;background:linear-gradient(135deg,#FBF4E6,#F3E6CC);border-bottom:1px solid #E7D3A4;}'
  + '.ftk-num{width:34px;height:34px;border-radius:8px;background:#7A5A2A;color:#FFF3D6;display:flex;align-items:center;justify-content:center;font-size:18px;flex:none;}'
  + '.ftk-title{font-family:"Nunito",sans-serif;font-size:17px;font-weight:800;}'
  + '.ftk-sub{font-size:15px;color:#6B5A3E;font-style:italic;}'
  + '.ftk-body{padding:14px 20px 16px;}'
  + '.ftk-intro-p{margin:0 0 12px;font-size:16px;line-height:1.65;color:#3A4A6B;max-width:70ch;}'
  + '.ftk-tabs{display:flex;gap:6px;flex-wrap:wrap;margin:0 0 12px;}'
  + '.ftk-tab{font:800 12.5px "Nunito",sans-serif;border:2px solid #E7D3A4;background:#fff;color:#6B5A3E;border-radius:999px;padding:5px 13px;cursor:pointer;}'
  + '.ftk-tab[aria-pressed="true"]{border-color:#7A5A2A;color:#0E1C42;background:#FBF4E6;}'
  + '.ftk-song{display:none;}'
  + '.ftk-song.on{display:block;}'
  + '.ftk-lyric{font-size:18px;line-height:1.8;background:#FFFDF7;border:1px solid #EBD9AF;border-radius:10px;padding:12px 20px;margin:0 0 12px;}'
  + '.ftk-lyric .t{display:block;font-family:"Nunito",sans-serif;font-size:12px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:#8A6416;margin-bottom:4px;}'
  + '.ftk-lyric small{display:block;font-family:"Nunito",sans-serif;font-size:11.5px;color:#93815E;margin-top:4px;}'
  + '.ftk-two{display:grid;grid-template-columns:1fr 1fr;gap:12px;}'
  + '.ftk-side{border-radius:10px;padding:12px 16px;font-size:15.5px;line-height:1.6;}'
  + '.ftk-side b{display:block;font-family:"Nunito",sans-serif;font-size:12.5px;font-weight:800;letter-spacing:.03em;margin-bottom:4px;}'
  + '.ftk-heard{background:#F3F5F9;color:#3A4A6B;}'
  + '.ftk-heard b{color:#56627F;}'
  + '.ftk-meant{background:#FFF6E2;color:#3B2E17;border:1px dashed #D9B66A;}'
  + '.ftk-meant b{color:#8A6416;}'
  + '.ftk-meant .cover{display:flex;align-items:center;justify-content:center;min-height:70px;}'
  + '.ftk-meant .cover[hidden],.ftk-meant .txt[hidden]{display:none;}'
  + '.ftk-btn{font:800 13px "Nunito",sans-serif;color:#7A5A2A;background:#fff;border:2px solid #E7D3A4;border-radius:999px;padding:6px 14px;cursor:pointer;}'
  + '.ftk-btn:hover,.ftk-btn:focus-visible{border-color:#7A5A2A;outline:none;}'
  + '.ftk-q{margin:12px 0 0;background:#F4F7FC;border-radius:10px;padding:12px 16px;font-size:15.5px;line-height:1.6;color:#3A4A6B;}'
  + '.ftk-q .a{margin-top:8px;color:#0E1C42;}'
  + '.ftk-cred{display:block;font-family:"Nunito",sans-serif;font-size:11px;color:#8A94A8;margin-top:10px;}'
  + '@media(max-width:700px){.ftk-two{grid-template-columns:1fr;}.ftk-lyric{font-size:16px;padding:10px 14px;}}';
  function css() {
    if (document.getElementById('ftk-css')) return;
    var s = document.createElement('style'); s.id = 'ftk-css'; s.textContent = CSS; document.head.appendChild(s);
  }

  /* ─────────────────────────── the opening ─────────────────────────── */
  /* Old Rit's quilt is "green and brown and yellow" (Ch. 2); a few
     darker scraps and one navy square, the one the camera falls into. */
  var FAB = ['#5E8C4A', '#8A5A33', '#E0B23E', '#3F6B3A', '#B07A45', '#C99A2E', '#6E9B57', '#7A4B2A', '#A9C27A', '#D9A35A'];
  var PATS = ['solid', 'stripe', 'check', 'tri', 'dot', 'stripe', 'tri', 'check', 'solid', 'dot', 'tri', 'stripe'];
  /* the Big Dipper and Polaris, in a box 0..1 (x right, y down); hand-placed
     so the two pointer stars (Merak → Dubhe) really aim at the North Star */
  var DIP = [[.44, .44], [.39, .52], [.47, .58], [.52, .50], [.60, .53], [.67, .50], [.75, .56]];
  /* index: 0 Dubhe, 1 Merak, 2 Phecda, 3 Megrez, 4 Alioth, 5 Mizar, 6 Alkaid */
  var DIPL = [[1, 0], [1, 2], [2, 3], [3, 0], [3, 4], [4, 5], [5, 6]];

  function rng(seed) { return function () { seed = (seed * 9301 + 49297) % 233280; return seed / 233280; }; }

  function patch(x, cx, cy, s, k, night, sa) {
    var r = rng(17 + k * 31), c1 = night ? '#16234A' : FAB[k % FAB.length], c2 = night ? '#22325F' : FAB[(k * 7 + 3) % FAB.length];
    if (c2 === c1) c2 = FAB[(k + 4) % FAB.length];
    var h = s / 2, pat = night ? 'solid' : PATS[k % PATS.length], i;
    x.save(); x.beginPath(); x.rect(cx - h, cy - h, s, s); x.clip();
    x.fillStyle = c1; x.fillRect(cx - h, cy - h, s, s);
    x.fillStyle = c2;
    if (pat === 'stripe') for (i = 0; i < 6; i++) x.fillRect(cx - h + (i * 2 + .5) * s / 12, cy - h, s / 12, s);
    else if (pat === 'check') { x.fillRect(cx - h, cy - h, h, h); x.fillRect(cx, cy, h, h); }
    else if (pat === 'tri') { x.beginPath(); x.moveTo(cx - h, cy + h); x.lineTo(cx + h, cy - h); x.lineTo(cx + h, cy + h); x.fill(); }
    else if (pat === 'dot') for (i = 0; i < 9; i++) { x.beginPath(); x.arc(cx - h + (i % 3 + .5) * s / 3, cy - h + (Math.floor(i / 3) + .5) * s / 3, s * .07, 0, 7); x.fill(); }
    /* weave: faint threads so it reads as cloth up close */
    x.globalAlpha = .07; x.fillStyle = '#000';
    for (i = 0; i < 26; i++) { x.fillRect(cx - h, cy - h + r() * s, s, Math.max(1, s / 220)); x.fillRect(cx - h + r() * s, cy - h, Math.max(1, s / 220), s); }
    x.globalAlpha = 1;
    if (night && sa > 0) {                         /* a small stitched star on the dark square; it fades as the camera sinks in */
      x.globalAlpha = sa; x.strokeStyle = '#E9C46A'; x.lineWidth = Math.max(1, s / 90); x.setLineDash([s / 40, s / 60]);
      star(x, cx + s * .2, cy - s * .18, s * .06, false); x.setLineDash([]); x.globalAlpha = 1;
    }
    x.restore();
    /* running stitch inside each seam */
    x.save(); x.strokeStyle = 'rgba(255,246,222,.75)'; x.lineWidth = Math.max(1, s / 120); x.setLineDash([s / 28, s / 44]);
    x.strokeRect(cx - h + s * .06, cy - h + s * .06, s * .88, s * .88); x.restore();
  }
  function star(x, cx, cy, r, fill) {
    x.beginPath();
    for (var i = 0; i < 10; i++) { var a = -Math.PI / 2 + i * Math.PI / 5, rr = i % 2 ? r * .45 : r; x.lineTo(cx + Math.cos(a) * rr, cy + Math.sin(a) * rr); }
    x.closePath(); if (fill) x.fill(); else x.stroke();
  }
  function glow(x, cx, cy, r, col, a) {
    var g = x.createRadialGradient(cx, cy, 0, cx, cy, r); g.addColorStop(0, col.replace('A', a)); g.addColorStop(1, col.replace('A', 0));
    x.fillStyle = g; x.beginPath(); x.arc(cx, cy, r, 0, 7); x.fill();
  }

  function scene(x, W, H, t) {
    var M = Math.min(W, H), s0 = M / 3.4;           /* patch size at rest: a 5 x 5 quilt with the middle one centered */
    var Z = Math.max(W, H) / s0 * 1.25;             /* zoom that lets the middle patch overfill the screen */
    var z = 1 + (Z - 1) * ease(P(t, 1.4, 4.0)), s = s0 * z;
    var sky = P(t, 3.3, 4.2);                       /* the navy patch becomes the sky */
    /* table under the quilt */
    x.fillStyle = '#2A1D14'; x.fillRect(0, 0, W, H);
    if (sky < 1) {
      for (var gy = -3; gy <= 3; gy++) for (var gx = -3; gx <= 3; gx++) {
        var cx = W / 2 + gx * s, cy = H / 2 + gy * s;
        if (cx + s < 0 || cx - s > W || cy + s < 0 || cy - s > H) continue;
        var k = (gx + 3) * 7 + (gy + 3), night = gx === 0 && gy === 0;
        /* the quilt is 5 x 5; outside it, the wooden table */
        if (Math.abs(gx) > 2 || Math.abs(gy) > 2) continue;
        patch(x, cx, cy, s, k, night, 1 - P(t, 1.8, 2.8));
      }
      /* a soft lamp-light vignette while it is still a quilt */
      var v = x.createRadialGradient(W / 2, H / 2, M * .2, W / 2, H / 2, Math.max(W, H) * .75);
      v.addColorStop(0, 'rgba(0,0,0,0)'); v.addColorStop(1, 'rgba(10,6,2,' + (.55 * (1 - sky)) + ')');
      x.fillStyle = v; x.fillRect(0, 0, W, H);
    }
    if (sky <= 0) return;
    x.save(); x.globalAlpha = sky;
    var g = x.createLinearGradient(0, 0, 0, H); g.addColorStop(0, '#0B1430'); g.addColorStop(.75, '#1B2B55'); g.addColorStop(1, '#2C3E6A');
    x.fillStyle = g; x.fillRect(0, 0, W, H);
    /* the cloth's weave, fading out as the sky comes in */
    x.globalAlpha = sky * (1 - P(t, 3.9, 4.6)) * .12; var r = rng(5);
    x.fillStyle = '#000'; for (var i = 0; i < 60; i++) { x.fillRect(0, r() * H, W, 1); x.fillRect(r() * W, 0, 1, H); }
    x.globalAlpha = sky;
    /* background stars */
    r = rng(9);
    for (i = 0; i < 160; i++) {
      var sx = r() * W, sy = r() * H * .82, sr = r() * 1.3 + .3, tw = .45 + .55 * Math.sin(t * 2 + i);
      x.globalAlpha = sky * P(t, 3.9 + r() * .9, 4.6 + r() * .9) * (.25 + .5 * tw);
      x.fillStyle = '#E3E9F8'; x.beginPath(); x.arc(sx, sy, sr, 0, 7); x.fill();
    }
    x.globalAlpha = 1;
    /* the Dipper: a box that fits the screen; Polaris above and to the left of Dubhe */
    var bw = Math.min(W * .9, H * 1.25), bx = (W - bw) / 2, by = H * .02, bh = bw * .78;
    function pt(p) { return [bx + p[0] * bw, by + p[1] * bh]; }
    var D = DIP.map(pt), ds = Math.max(2.2, M / 170);
    x.strokeStyle = 'rgba(227,233,248,.55)'; x.lineWidth = Math.max(1, M / 500);
    DIPL.forEach(function (l, j) {
      var p = ease(P(t, 4.6 + j * .16, 4.9 + j * .16)); if (!p) return;
      var a = D[l[0]], b = D[l[1]]; x.beginPath(); x.moveTo(a[0], a[1]); x.lineTo(a[0] + (b[0] - a[0]) * p, a[1] + (b[1] - a[1]) * p); x.stroke();
    });
    D.forEach(function (d, j) {
      var p = P(t, 4.3 + j * .14, 4.6 + j * .14); if (!p) return;
      glow(x, d[0], d[1], ds * 6, 'rgba(255,244,210,A)', .55 * p);
      x.fillStyle = 'rgba(255,250,235,' + p + ')'; x.beginPath(); x.arc(d[0], d[1], ds * (j === 0 || j === 1 ? 1.25 : 1), 0, 7); x.fill();
    });
    /* pointer line: Merak → Dubhe, carried on about five times that gap */
    var m = D[1], d0 = D[0], vx = d0[0] - m[0], vy = d0[1] - m[1];
    var pol = [d0[0] + vx * 5, d0[1] + vy * 5];
    if (pol[1] < H * .06) { var sc = (d0[1] - H * .06) / -vy; pol = [d0[0] + vx * sc, H * .06]; }
    var pp = ease(P(t, 5.7, 6.5));
    if (pp) {
      x.save(); x.strokeStyle = 'rgba(243,210,122,.9)'; x.lineWidth = Math.max(1.4, M / 380); x.setLineDash([M / 90, M / 120]);
      x.beginPath(); x.moveTo(m[0], m[1]); x.lineTo(m[0] + (pol[0] - m[0]) * pp, m[1] + (pol[1] - m[1]) * pp); x.stroke(); x.restore();
    }
    var pf = P(t, 6.3, 6.9);
    if (pf) {
      var pulse = 1 + .12 * Math.sin(t * 5);
      glow(x, pol[0], pol[1], M * .12 * pulse, 'rgba(243,210,122,A)', .5 * pf);
      x.fillStyle = 'rgba(255,240,190,' + pf + ')'; x.strokeStyle = 'rgba(255,240,190,' + pf + ')';
      star(x, pol[0], pol[1], ds * 3.4 * (0.6 + .4 * ease(pf)), true);
    }
    /* the trees: a dark line of pines along the bottom */
    x.fillStyle = '#060B1C'; r = rng(23);
    var base = H * .9; x.fillRect(0, base, W, H - base);
    for (var tx = -20; tx < W + 20; tx += M / 22) {
      var th = M * (.07 + r() * .08), tw2 = th * .38;
      x.beginPath(); x.moveTo(tx, base + 2); x.lineTo(tx + tw2, base - th); x.lineTo(tx + tw2 * 2, base + 2); x.fill();
    }
    /* the north star path: small warm lights, one after another, from the woods toward the star */
    var start = [W * .12, H * .93], n = 11;
    for (i = 0; i < n; i++) {
      var f = i / (n - 1), lp = P(t, 6.6 + i * .12, 6.9 + i * .12); if (!lp) continue;
      var ex = start[0] + (pol[0] - start[0]) * f * .62 + Math.sin(f * 6) * M * .03, ey = start[1] + (pol[1] - start[1]) * f * .62;
      var lr = Math.max(1.6, M / 260) * (1.3 - f * .6);
      glow(x, ex, ey, lr * 6, 'rgba(255,200,110,A)', .6 * lp);
      x.fillStyle = 'rgba(255,226,160,' + lp + ')'; x.beginPath(); x.arc(ex, ey, lr, 0, 7); x.fill();
    }
    x.restore();
  }

  var LEN = 8.2, cur = null, opts = {};
  function key() { return 'oao.ft.intro:' + location.pathname; }
  function seen() { try { return sessionStorage.getItem(key()) === '1'; } catch (e) { return false; } }
  function mark() { try { sessionStorage.setItem(key(), '1'); } catch (e) {} }
  function size() {
    var vw = window.innerWidth, vh = window.innerHeight, tall = vh > (screen.height || 900) * 1.2;
    if (tall) vh = Math.min(vh, screen.height || 900, 900);       /* a Canvas iframe stretched to the page */
    return { vw: vw, vh: vh, tall: tall };
  }
  function play(still) {
    if (cur) return; mark(); css();
    var z = size(), dpr = Math.min(2, window.devicePixelRatio || 1), last = document.activeElement;
    var c = document.createElement('div'); c.className = 'ftk-intro';
    c.setAttribute('role', 'dialog'); c.setAttribute('aria-modal', 'true'); c.setAttribute('aria-label', 'Lesson opening');
    if (z.tall) { c.style.position = 'absolute'; c.style.top = (window.scrollY || 0) + 'px'; c.style.height = z.vh + 'px'; c.style.bottom = 'auto'; }
    c.innerHTML = '<canvas aria-hidden="true"></canvas>' +
      '<p class="sr">A patchwork quilt fills the screen. The view sinks into one dark square, which becomes a night sky. The Big Dipper comes out, its two pointer stars lead to the North Star, and a trail of small lights runs north from the trees toward it.</p>' +
      '<button type="button" class="ftk-skip">' + (still ? 'Start the lesson ▸' : 'Skip ▸▸') + '</button>';
    document.body.appendChild(c); document.body.classList.add('ftk-on');
    var cv = c.querySelector('canvas'), W = z.vw, H = z.vh;
    cv.width = Math.round(W * dpr); cv.height = Math.round(H * dpr); cv.style.width = W + 'px'; cv.style.height = H + 'px';
    var x = cv.getContext('2d'); x.scale(dpr, dpr);
    var t0 = performance.now(), st = { raf: 0, closing: false }; cur = st;
    function frame(now) {
      var t = still ? LEN : (now - t0) / 1000;
      try { scene(x, W, H, Math.min(t, LEN)); } catch (e) { (window.OAO_SPARKLE_FAILED = window.OAO_SPARKLE_FAILED || []).push('ft intro: ' + e.message); close(true); return; }
      if (!still && t >= LEN + .5) close();
      if (!st.closing && !still) st.raf = requestAnimationFrame(frame);
      else if (still && !st.closing) { /* one still frame */ }
    }
    function close(fast) {
      if (st.closing) return; st.closing = true; cancelAnimationFrame(st.raf);
      c.classList.add('out'); setTimeout(finish, fast ? 0 : 700);
    }
    function finish() {
      c.remove(); document.body.classList.remove('ftk-on'); document.removeEventListener('keydown', onKey, true); cur = null;
      if (last && last.focus && document.contains(last)) try { last.focus({ preventScroll: true }); } catch (e) {}
    }
    function onKey(e) {
      if (e.key === 'Escape' || e.key === 'Enter' || e.key === ' ') { e.preventDefault(); e.stopPropagation(); close(); }
      else if (e.key === 'Tab') { e.preventDefault(); c.querySelector('.ftk-skip').focus(); }
    }
    c.addEventListener('click', function () { close(); });
    document.addEventListener('keydown', onKey, true);
    st.raf = requestAnimationFrame(frame);
    setTimeout(function () { var b = c.querySelector('.ftk-skip'); if (b) b.focus({ preventScroll: true }); }, 50);
  }
  function replayButton() {
    var hdr = document.querySelector('.header-title') || document.querySelector('.header');
    if (!hdr || document.querySelector('.ftk-replay')) return;
    var b = document.createElement('button'); b.type = 'button'; b.className = 'ftk-replay';
    b.textContent = '🎬 Replay opening'; b.title = 'Watch the lesson opening again';
    b.onclick = function (e) { e.stopPropagation(); play(reduced()); };
    hdr.appendChild(b);
  }
  KIT.intro = function (o) {
    opts = o || {}; css(); replayButton();
    var bot = !!navigator.webdriver;
    if (q('nointro')) return;
    if (q('intro')) { play(reduced()); return; }
    if (bot || seen() || reduced()) return;
    play(false);
  };
  KIT._scene = scene;                                   /* for tests: draw one frame at time t */

  /* ─────────────────────────── songs ─────────────────────────── */
  function songs(host, opt) {
    var list = ((opt.cfg || {}).songs || []).filter(function (s) { return s && s.title && s.lines && s.lines.length; });
    if (!list.length) return false;
    css();
    var tabs = list.length > 1 ? '<div class="ftk-tabs" role="group" aria-label="Songs">' + list.map(function (s, i) {
      return '<button type="button" class="ftk-tab" data-i="' + i + '" aria-pressed="' + (i ? 'false' : 'true') + '">' + esc(s.title) + '</button>';
    }).join('') + '</div>' : '';
    var body = list.map(function (s, i) {
      return '<div class="ftk-song' + (i ? '' : ' on') + '" data-i="' + i + '">' +
        '<div class="ftk-lyric"><span class="t">' + esc(s.title) + '</span>' + s.lines.map(function (l) { return esc(l); }).join('<br>') +
          '<small>' + esc(s.source || 'A traditional spiritual · public domain') + '</small></div>' +
        '<div class="ftk-two">' +
          '<div class="ftk-side ftk-heard"><b>👂 What the overseer heard</b>' + esc(s.heard) + '</div>' +
          '<div class="ftk-side ftk-meant"><b>🤫 What the singers meant</b>' +
            '<div class="cover"><button type="button" class="ftk-btn ftk-show">Think first, then show me</button></div>' +
            '<div class="txt" hidden>' + esc(s.meant) + '</div></div>' +
        '</div>' +
        (s.q ? '<div class="ftk-q"><b>Look closer:</b> ' + esc(s.q) +
          (s.a ? ' <button type="button" class="ftk-btn ftk-ans" style="margin-left:6px;">Show an answer</button><div class="a" hidden>' + esc(s.a) + '</div>' : '') + '</div>' : '') +
      '</div>';
    }).join('');
    host.innerHTML =
      '<div class="ftk-card"><div class="ftk-head"><div class="ftk-num">♪</div><div>' +
        '<div class="ftk-title">Songs With a Hidden Meaning</div>' +
        '<div class="ftk-sub">The same words could mean two different things.</div></div></div>' +
      '<div class="ftk-body"><p class="ftk-intro-p">' + esc((opt.cfg || {}).songsIntro ||
        'The people Harriet grew up with sang all day in the fields. The overseer wanted them to sing. But some songs said one thing to him and something else to the people singing them.') + '</p>' +
        tabs + body + '</div></div>';
    host.querySelectorAll('.ftk-tab').forEach(function (b) {
      b.addEventListener('click', function () {
        var i = b.getAttribute('data-i');
        host.querySelectorAll('.ftk-tab').forEach(function (o) { o.setAttribute('aria-pressed', o === b ? 'true' : 'false'); });
        host.querySelectorAll('.ftk-song').forEach(function (s) { s.classList.toggle('on', s.getAttribute('data-i') === i); });
      });
    });
    host.querySelectorAll('.ftk-show').forEach(function (b) {
      b.addEventListener('click', function () { var side = b.closest('.ftk-meant'); side.querySelector('.cover').hidden = true; side.querySelector('.txt').hidden = false; });
    });
    host.querySelectorAll('.ftk-ans').forEach(function (b) {
      b.addEventListener('click', function () { b.nextElementSibling.hidden = false; b.remove(); });
    });
    return true;
  }

  KIT.mount = function (kind, host, opt) {
    try {
      if (kind === 'songs') return songs(host, opt || {});
    } catch (e) { (window.OAO_SPARKLE_FAILED = window.OAO_SPARKLE_FAILED || []).push('ft kit ' + kind + ': ' + e.message); }
    return false;
  };
})();
