/* ══════════════════════════════════════════════════════════════
   OAO Video Questions: "stop and answer" films (Edpuzzle-style)

   A film with a <name>.questions.json beside it (made in the Video
   Studio) stops at each question. The student answers, then the film
   goes on. sparkle.js finds the file and calls OAOVideoQ.attach().

   File shape:
     { "v":1, "noSkip":true,
       "questions":[ { "t":42.5, "type":"mc"|"write"|"think",
                       "q":"…", "choices":["…","…"], "answer":1, "why":"…" } ] }

   - mc     two to four choices; a wrong pick says "try again"; after two
            misses the right answer is shown with the "why".
   - write  a short written answer (saved, and added to My Work).
   - think  a pause to think, with a "keep watching" button.
   noSkip: the student can't jump ahead past a question they haven't
   answered. Going back is always fine. Answers are kept in this
   browser, like the rest of the lesson's answers.
   ══════════════════════════════════════════════════════════════ */
(function () {
'use strict';
if (window.OAOVideoQ) return;

var CSS =
'.vq-box{display:inline-block;max-width:100%;vertical-align:top;text-align:left}' +
'.vq-wrap{position:relative;display:block;line-height:0}' +
'.vq-wrap>video{display:block}' +
'.vq-card{position:absolute;inset:0;z-index:3;display:flex;align-items:center;justify-content:center;padding:14px;' +
  'background:rgba(14,28,66,.94);color:#fff;line-height:1.4;text-align:left;border-radius:10px;overflow:auto;' +
  'font-family:Nunito,"Segoe UI",system-ui,sans-serif;animation:vqIn .25s ease}' +
'.vq-card[hidden]{display:none}' +
'@keyframes vqIn{from{opacity:0;transform:scale(.98)}to{opacity:1;transform:none}}' +
'.vq-in{width:100%;max-width:560px}' +
'.vq-tag{display:inline-block;background:#E8A531;color:#0E1C42;font-weight:800;font-size:12px;letter-spacing:.6px;text-transform:uppercase;border-radius:20px;padding:3px 10px;margin-bottom:8px}' +
'.vq-q{font-size:clamp(16px,2.6vw,21px);font-weight:800;margin:0 0 12px}' +
'.vq-ch{display:grid;gap:7px}' +
'.vq-ch button{all:unset;box-sizing:border-box;cursor:pointer;background:#fff;color:#0E1C42;border-radius:10px;padding:9px 12px;font-weight:700;font-size:15px;border:2px solid transparent;display:flex;gap:9px;align-items:center}' +
'.vq-ch button:hover{border-color:#E8A531}' +
'.vq-ch button:focus-visible{outline:3px solid #E8A531;outline-offset:2px}' +
'.vq-ch button b{background:#eef2fa;border-radius:6px;padding:1px 7px;font-size:13px}' +
'.vq-ch button.vq-ok{background:#d9f3e6;border-color:#2f9e6b}' +
'.vq-ch button.vq-no{background:#fbe1e1;border-color:#d64545;opacity:.8}' +
'.vq-ch button[disabled]{cursor:default}' +
'.vq-fb{margin-top:10px;font-size:15px;font-weight:700;min-height:1px}' +
'.vq-fb.ok{color:#9ee6c0}.vq-fb.no{color:#ffc2c2}' +
'.vq-why{font-weight:600;color:#dfe6f7;margin-top:4px}' +
'.vq-ta{box-sizing:border-box;width:100%;min-height:84px;border-radius:10px;border:0;padding:10px;font:inherit;font-size:15px;line-height:1.45;color:#0E1C42}' +
'.vq-row{display:flex;gap:8px;flex-wrap:wrap;margin-top:12px;align-items:center}' +
'.vq-go{all:unset;cursor:pointer;background:#E8A531;color:#0E1C42;font-weight:800;border-radius:10px;padding:9px 16px;font-size:15px}' +
'.vq-go[disabled]{opacity:.45;cursor:not-allowed}' +
'.vq-back{all:unset;cursor:pointer;color:#c9d5f6;font-weight:700;font-size:14px;padding:6px 4px}' +
'.vq-back:hover{color:#fff}' +
'.vq-note{font-size:13px;color:#c9d5f6}' +
'.vq-strip{display:flex;align-items:center;gap:10px;margin:6px 0 0;width:100%;box-sizing:border-box;padding:0 4px;font:700 13px Nunito,"Segoe UI",system-ui,sans-serif;color:#5d6782;line-height:1.3}' +
'.vq-bar{position:relative;flex:1;height:8px;border-radius:5px;background:#e3e8f2;min-width:80px}' +
'.vq-dot{position:absolute;top:50%;width:14px;height:14px;margin:-7px 0 0 -7px;border-radius:50%;background:#fff;border:3px solid #0E1C42;box-sizing:border-box}' +
'.vq-dot.done{background:#E8A531;border-color:#E8A531}' +
'.vq-prog{position:absolute;left:0;top:0;bottom:0;background:#c9d5f6;border-radius:5px}' +
'.vq-toast{position:absolute;left:50%;bottom:64px;transform:translateX(-50%);z-index:4;background:#0E1C42;color:#fff;font:700 14px Nunito,system-ui,sans-serif;border-radius:9px;padding:7px 13px;line-height:1.3;pointer-events:none;opacity:0;transition:opacity .2s}' +
'.vq-toast.on{opacity:1}';

function css() {
  if (document.getElementById('vq-css')) return;
  var s = document.createElement('style'); s.id = 'vq-css'; s.textContent = CSS;
  (document.head || document.documentElement).appendChild(s);
}
function lessonKey() {
  return window._lessonKey || (document.title || 'ela-lesson').replace(/[^a-zA-Z0-9]+/g, '-').toLowerCase();
}
function load(k) { try { return JSON.parse(localStorage.getItem(lessonKey() + '-' + k) || 'null'); } catch (e) { return null; } }
function save(k, v) { try { localStorage.setItem(lessonKey() + '-' + k, JSON.stringify(v)); } catch (e) {} }
function esc(t) { var d = document.createElement('div'); d.textContent = t == null ? '' : String(t); return d.innerHTML; }
var LETTERS = 'ABCD';
var films = [];   /* for My Work */

function attach(video, data, src, label) {
  if (!video || video.getAttribute('data-vq')) return;
  var qs = ((data && data.questions) || []).filter(function (q) { return q && isFinite(+q.t) && q.q; })
    .map(function (q) { return { t: +q.t, type: q.type || 'think', q: String(q.q), choices: (q.choices || []).filter(function (c) { return String(c || '').trim(); }), answer: +q.answer || 0, why: q.why || '' }; })
    .sort(function (a, b) { return a.t - b.t; });
  if (!qs.length) return;
  video.setAttribute('data-vq', '1');
  css();
  var noSkip = data.noSkip !== false;
  var name = String(src || '').split('/').pop().replace(/\.(mp4|webm)(\?.*)?$/i, '');
  var key = 'vq-' + name;
  var st = load(key) || {};                 /* i -> {done, pick, tries, text} */
  var film = { name: name, label: label || video.getAttribute('aria-label') || name, qs: qs, st: st };
  films.push(film);

  var box = document.createElement('div'); box.className = 'vq-box';
  var wrap = document.createElement('div'); wrap.className = 'vq-wrap';
  video.parentNode.insertBefore(box, video); box.appendChild(wrap); wrap.appendChild(video);
  var card = document.createElement('div'); card.className = 'vq-card'; card.hidden = true;
  card.setAttribute('role', 'dialog'); card.setAttribute('aria-live', 'polite');
  wrap.appendChild(card);
  var tst = document.createElement('div'); tst.className = 'vq-toast'; wrap.appendChild(tst);
  var strip = document.createElement('div'); strip.className = 'vq-strip';
  strip.innerHTML = '<span>❓ ' + qs.length + ' stop-and-answer question' + (qs.length > 1 ? 's' : '') + '</span><span class="vq-bar"><span class="vq-prog"></span></span>';
  box.appendChild(strip);
  var bar = strip.querySelector('.vq-bar'), prog = strip.querySelector('.vq-prog'), dots = [];

  function done(i) { return st[i] && st[i].done; }
  function firstOpen() { for (var i = 0; i < qs.length; i++) if (!done(i)) return i; return -1; }
  function persist() { save(key, st); if (window.gatherAnswers) try { window.gatherAnswers(); } catch (e) {} }
  function toast(t) { tst.textContent = t; tst.classList.add('on'); clearTimeout(tst._t); tst._t = setTimeout(function () { tst.classList.remove('on'); }, 2200); }
  function drawDots() {
    var d = video.duration; if (!isFinite(d) || !d) return;
    dots.forEach(function (x) { x.remove(); }); dots = [];
    qs.forEach(function (q, i) {
      var x = document.createElement('span'); x.className = 'vq-dot' + (done(i) ? ' done' : '');
      x.style.left = Math.min(100, q.t / d * 100) + '%'; x.title = 'Question ' + (i + 1);
      bar.appendChild(x); dots.push(x);
    });
  }
  video.addEventListener('loadedmetadata', drawDots);
  video.addEventListener('durationchange', drawDots);
  if (video.readyState >= 1) drawDots();

  var open = -1, guard = false;
  function check() {
    var t = video.currentTime, d = video.duration;
    if (isFinite(d) && d) prog.style.width = Math.min(100, t / d * 100) + '%';
    if (open > -1) return;
    for (var i = 0; i < qs.length; i++) {
      if (!done(i) && t >= qs[i].t - 0.05 && t < qs[i].t + 2) { show(i); return; }
    }
  }
  video.addEventListener('timeupdate', check);
  video.addEventListener('ended', function () { var f = firstOpen(); if (f > -1 && open < 0) show(f); });
  video.addEventListener('play', function () { if (open > -1) video.pause(); });
  video.addEventListener('seeking', function () {
    if (guard) return;
    var f = firstOpen();
    if (noSkip && f > -1 && video.currentTime > qs[f].t + 0.4) {
      guard = true; video.currentTime = qs[f].t; setTimeout(function () { guard = false; }, 300);
      toast('Answer the question first, then you can go on');
    }
  });

  function finish(i) {
    st[i] = st[i] || {}; st[i].done = true; persist();
    if (dots[i]) dots[i].classList.add('done');
    card.hidden = true; card.innerHTML = ''; open = -1;
    var p = video.play(); if (p && p.catch) p.catch(function () {});
  }
  function backTo(i) {
    var from = i > 0 ? qs[i - 1].t + 0.2 : 0;
    card.hidden = true; card.innerHTML = ''; open = -1;
    guard = true; video.currentTime = Math.max(from, qs[i].t - 20); setTimeout(function () { guard = false; }, 300);
    var p = video.play(); if (p && p.catch) p.catch(function () {});
  }
  function show(i) {
    var q = qs[i]; open = i;
    video.pause();
    try { if (document.fullscreenElement) document.exitFullscreen(); } catch (e) {}
    if (video.webkitDisplayingFullscreen && video.webkitExitFullscreen) try { video.webkitExitFullscreen(); } catch (e) {}
    st[i] = st[i] || {};
    var tag = q.type === 'mc' ? 'Stop and answer' : q.type === 'write' ? 'Stop and write' : 'Stop and think';
    var h = '<div class="vq-in"><span class="vq-tag">' + tag + ' · ' + (i + 1) + ' of ' + qs.length + '</span><p class="vq-q">' + esc(q.q) + '</p>';
    if (q.type === 'mc' && q.choices.length >= 2) {
      h += '<div class="vq-ch">' + q.choices.map(function (c, k) { return '<button type="button" data-k="' + k + '"><b>' + LETTERS[k] + '</b><span>' + esc(c) + '</span></button>'; }).join('') + '</div><div class="vq-fb"></div>';
      h += '<div class="vq-row"><button type="button" class="vq-go" hidden>Keep watching ▶</button><button type="button" class="vq-back">↺ Watch that part again</button></div>';
    } else if (q.type === 'write') {
      h += '<textarea class="vq-ta" placeholder="Write your answer here…"></textarea>';
      h += '<div class="vq-row"><button type="button" class="vq-go" disabled>Save and keep watching ▶</button><button type="button" class="vq-back">↺ Watch that part again</button><span class="vq-note"></span></div>';
    } else {
      h += '<div class="vq-row"><button type="button" class="vq-go">I thought about it. Keep watching ▶</button><button type="button" class="vq-back">↺ Watch that part again</button></div>';
    }
    card.innerHTML = h + '</div>';
    card.hidden = false;
    var go = card.querySelector('.vq-go');
    card.querySelector('.vq-back').onclick = function () { backTo(i); };
    go.onclick = function () { if (!go.disabled) finish(i); };
    if (q.type === 'mc' && q.choices.length >= 2) {
      var fb = card.querySelector('.vq-fb'), btns = card.querySelectorAll('.vq-ch button');
      var settle = function (right) {
        btns.forEach(function (b) { b.disabled = true; if (+b.getAttribute('data-k') === q.answer) b.classList.add('vq-ok'); });
        fb.className = 'vq-fb ' + (right ? 'ok' : 'no');
        fb.innerHTML = (right ? 'That’s it!' : 'The answer is ' + LETTERS[q.answer] + '.') + (q.why ? '<div class="vq-why">' + esc(q.why) + '</div>' : '');
        go.hidden = false; go.focus();
      };
      btns.forEach(function (b) {
        b.onclick = function () {
          var k = +b.getAttribute('data-k');
          st[i].tries = (st[i].tries || 0) + 1;
          if (st[i].first == null) st[i].first = k;
          st[i].pick = k; save(key, st);
          if (k === q.answer) settle(true);
          else if (st[i].tries >= 2) { b.classList.add('vq-no'); settle(false); }
          else { b.classList.add('vq-no'); b.disabled = true; fb.className = 'vq-fb no'; fb.textContent = 'Not quite. Look again and try once more.'; }
        };
      });
      if (btns[0]) btns[0].focus();
    } else if (q.type === 'write') {
      var ta = card.querySelector('.vq-ta'), note = card.querySelector('.vq-note');
      ta.value = st[i].text || '';
      var upd = function () {
        var n = (ta.value.trim().match(/\S+/g) || []).length;
        go.disabled = n < 3; note.textContent = n && n < 3 ? 'Write a little more.' : '';
      };
      ta.oninput = function () { st[i].text = ta.value; save(key, st); upd(); };
      upd(); ta.focus();
    } else go.focus();
  }
}

/* My Work: add the film answers to what the lesson gathers */
function hookGather() {
  if (hookGather.done || !window.gatherAnswers) return;
  hookGather.done = true;
  var orig = window.gatherAnswers;
  window.gatherAnswers = function () {
    var r = orig.apply(this, arguments);
    var out = document.getElementById('gatheredOutput'); if (!out) return r;
    var txt = '';
    films.forEach(function (f) {
      var lines = [];
      f.qs.forEach(function (q, i) {
        var s = f.st[i]; if (!s) return;
        if (q.type === 'mc' && s.first != null) lines.push((i + 1) + '. ' + q.q + '\n   ' + (s.first === q.answer ? '✓ ' : '✗ first try: ' + (q.choices[s.first] || '') + ' · then ') + (s.first === q.answer ? q.choices[q.answer] : (s.pick === q.answer ? 'got it on the second try' : 'shown the answer')));
        else if (q.type === 'write' && s.text && s.text.trim()) lines.push((i + 1) + '. ' + q.q + '\n   ' + s.text.trim());
        else if (q.type === 'think' && s.done) lines.push((i + 1) + '. ' + q.q + '\n   (thought about it)');
      });
      if (lines.length) txt += '\n' + f.label + '\n' + lines.join('\n') + '\n';
    });
    if (txt) out.value += '\n🎬 VIDEO QUESTIONS\n────────────────' + txt;
    return r;
  };
}

window.OAOVideoQ = {
  attach: function (video, data, src, label) { attach(video, data, src, label); hookGather(); },
  /* look for <film>.questions.json beside a film and attach it if there is one */
  find: function (video, src, label) {
    if (!video || !src || !window.fetch) return;
    var url = String(src).replace(/\.(mp4|webm)(\?.*)?$/i, '.questions.json');
    if (url === src) return;
    fetch(url, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; })
      .then(function (d) { if (d) window.OAOVideoQ.attach(video, d, src, label); }).catch(function () {});
  }
};
})();
