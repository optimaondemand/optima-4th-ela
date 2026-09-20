/* ══════════════════════════════════════════════════════════════════════
   OAO G4 ELA — SPARKLE LAYER : BY HEART
   ──────────────────────────────────────────────────────────────────────
   Option A. By Heart REPLACES Poetry Corner.

   One poem per book arc, memorised over eight rungs. The rotating
   anthology is retired: where a lesson used to show a different poem
   with a "notice what the poet did" prompt, it now shows the arc's
   one poem with a little less of it visible each time.

   HOW IT ATTACHES
     A lesson gets one line, before </body>:
       <script src=".../assets/js/oao-sparkle.js"></script>
     Nothing else. No per-lesson data, no CSS edit, no markup change.

     The file finds its own footing:
       - week and day come from #oao-lesson, or window.LESSON, or the
         filename (lesson-7-2-anne-ch2.html -> week 7, day 2)
       - the arc comes from the week, via COURSE
       - it renders ONLY where a .poem-box already exists, so the
         week's rhythm is exactly what the scope and sequence says

   WHAT IT DOES TO THE PAGE
     The Poetry Corner activity is hidden, not deleted. Its markup
     stays in the DOM with data-oao-retired="poetry-corner". Remove
     this script and the old Poetry Corner comes back untouched.

   STORAGE
     oao.g4ela.memory = { <arcId>: { rung:1..8, advancedOn:'YYYY-MM-DD' } }
     One rung per calendar day, per arc. Two lessons in one sitting
     still only advance once.
   ══════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  /* ── storage helper (reuse the page's if the sparkle demo is present) ── */
  var Sparkle = window.Sparkle || {
    get: function (k, d) {
      try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : (d === undefined ? null : d); }
      catch (e) { return d === undefined ? null : d; }
    },
    set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
  };
  window.Sparkle = Sparkle;

  /* ── §1  course map ──────────────────────────────────────────────────
     Mirrors COURSE in the lesson files. Kept here so the script stands
     alone in lessons that have no sparkle layer of their own.          */
  var COURSE = [
    { id: 'frisby',  weeks: [1, 5]   },
    { id: 'writing', weeks: [6, 6]   },
    { id: 'anne',    weeks: [7, 14]  },
    { id: 'bridge',  weeks: [15, 15] },
    { id: 'nts',     weeks: [16, 19] },
    { id: 'ft',      weeks: [20, 25] },
    { id: 'pc',      weeks: [26, 30] },
    { id: 'synth',   weeks: [31, 32] }
  ];

  /* Writer's Workshop (wk 6) and the NTS Bridge (wk 15) are their own
     book ids but have only two poetry days each — far too few for an
     eight-rung ladder. They ride with the arc they sit against:
     week 6 carries Frisby's poem forward, week 15 introduces the one
     Number the Stars is about to spend four weeks on.                  */
  var LADDER_OF = { writing: 'frisby', bridge: 'nts' };

  /* ── §2  the poems ──────────────────────────────────────────────────
     One per arc. Each is the FIRST STANZA of a poem the arc already
     uses, so nothing new was written and nothing new needs clearing.
     Four lines everywhere: it is what a fourth grader can actually
     hold, and it makes the rungs mean the same thing in every arc.

     Line shape is [text, indented]. All five are public domain except
     The Forest Remembers, which is Optima's own.                       */
  var POEMS = {
    frisby: {
      title: 'Hope Is the Thing with Feathers',
      author: 'Emily Dickinson',
      note: 'public domain',
      lines: [
        ['Hope is the thing with feathers', 0],
        ['That perches in the soul,', 0],
        ['And sings the tune without the words,', 0],
        ['And never stops at all,', 0]
      ]
    },
    anne: {
      title: 'Who Has Seen the Wind?',
      author: 'Christina Rossetti',
      note: 'public domain',
      lines: [
        ['Who has seen the wind?', 0],
        ['Neither I nor you:', 0],
        ['But when the leaves hang trembling,', 0],
        ['The wind is passing through.', 0]
      ]
    },
    nts: {
      title: 'There Will Come Soft Rains',
      author: 'Sara Teasdale',
      note: 'Flame and Shadow, 1920 — public domain',
      lines: [
        ['There will come soft rains and the smell of the ground,', 0],
        ['And swallows circling with their shimmering sound;', 0],
        ['And frogs in the pools singing at night,', 0],
        ['And wild plum-trees in tremulous white;', 0]
      ]
    },
    ft: {
      title: 'Sympathy',
      author: 'Paul Laurence Dunbar',
      note: 'Lyrics of the Hearthside, 1899 — public domain',
      lines: [
        ['I know what the caged bird feels, alas!', 0],
        ['When the sun is bright on the upland slopes;', 1],
        ['When the wind stirs soft through the springing grass,', 0],
        ['And the river flows like a stream of glass;', 0]
      ]
    },
    pc: {
      title: 'The Forest Remembers',
      author: 'Optima Academy Online',
      note: 'written in-house',
      lines: [
        ['The stones still stand where towers fell,', 0],
        ['The river hums a half-lost spell,', 0],
        ['The trees lean close as if to say,', 0],
        ['“We knew you’d find your way back someday.”', 0]
      ]
    },
    /* Weeks 31–32 have four poetry days. Four days cannot climb eight
       rungs, and a ladder nobody can top out is a worse ending than no
       ladder. The synthesis weeks ask for one already learned instead. */
    synth: null
  };

  /* Names shown on the synthesis card, in the order they were met. */
  var ARC_LABEL = {
    frisby: 'Mrs. Frisby and the Rats of NIMH',
    anne:   'Anne of Green Gables',
    nts:    'Number the Stars',
    ft:     'Freedom Train',
    pc:     'Prince Caspian'
  };
  var ARC_ORDER = ['frisby', 'anne', 'nts', 'ft', 'pc'];

  /* ── §3  where am I ─────────────────────────────────────────────── */
  function lessonInfo() {
    var L = null;
    try {
      var decl = document.getElementById('oao-lesson');
      if (decl) L = JSON.parse(decl.textContent);
    } catch (e) {}
    if (!L && window.LESSON && window.LESSON.week) L = window.LESSON;
    if (!L) {
      var m = (location.pathname.split('/').pop() || '').match(/lesson-(\d+)-(\d+|fluency)/i);
      if (m) L = { week: parseInt(m[1], 10), day: (m[2] === 'fluency' ? 'fluency' : parseInt(m[2], 10)) };
    }
    return L;
  }

  function arcOf(week) {
    for (var i = 0; i < COURSE.length; i++) {
      if (week >= COURSE[i].weeks[0] && week <= COURSE[i].weeks[1]) return COURSE[i].id;
    }
    return null;
  }

  /* The arc whose LADDER this lesson climbs — not always the arc it
     sits in. See LADDER_OF.                                           */
  function ladderArc(week) {
    var a = arcOf(week);
    return a ? (LADDER_OF[a] || a) : null;
  }

  /* ── §4  the ladder ─────────────────────────────────────────────── */
  function memState() {
    return Sparkle.get('oao.g4ela.memory', {});
  }
  function rungOf(arc) {
    var m = memState();
    return (m[arc] && m[arc].rung) || 1;
  }

  /* Which word indices are hidden at a given rung.
       1 whole stanza        5 last three on the other lines
       2 last word           6 back half of every line
       3 last two, alt lines 7 first word of each line only
       4 last two, all lines 8 nothing                          */
  function fadeMask(words, lineIdx, rung) {
    var n = words.length, hide = {};
    function last(k) { for (var i = Math.max(0, n - k); i < n; i++) hide[i] = 1; }
    if (rung >= 2) last(1);
    if (rung >= 3 && lineIdx % 2 === 1) last(2);
    if (rung >= 4) last(2);
    if (rung >= 5 && lineIdx % 2 === 0) last(3);
    if (rung >= 6) last(Math.ceil(n / 2));
    if (rung >= 7) for (var i = 1; i < n; i++) hide[i] = 1;
    if (rung >= 8) for (var j = 0; j < n; j++) hide[j] = 1;
    return hide;
  }

  function rungBlurb(r) {
    if (r === 1) return 'the whole stanza — read it aloud twice';
    if (r === 8) return 'nothing on the page — say it cold';
    if (r === 7) return 'first word of each line only';
    return 'a little less to lean on';
  }

  /* ── §5  styles (injected once; no lesson CSS is touched) ───────── */
  var CSS = ''
    + '.oao-bh{background:#fff;border:1px solid #E6EBF5;border-radius:12px;overflow:hidden;'
    +   'margin:0;box-shadow:0 1px 4px rgba(14,28,66,.05);border-left:5px solid #C7922C;}'
    + '.oao-bh-head{display:flex;gap:12px;align-items:center;padding:14px 18px;'
    +   'background:linear-gradient(135deg,#FFF8F0,#FFF3DC);border-bottom:1px solid #F5E6C8;}'
    + '.oao-bh-num{width:34px;height:34px;border-radius:8px;background:#C7922C;color:#fff;'
    +   'display:flex;align-items:center;justify-content:center;font-size:17px;flex:none;}'
    + '.oao-bh-title{font-family:"Nunito",sans-serif;font-size:17px;font-weight:800;color:#0E1C42;}'
    + '.oao-bh-sub{font-size:13px;color:#7A88A8;font-style:italic;}'
    + '.oao-bh-body{padding:18px 20px;}'
    + '.oao-bh-rung{font-family:"Nunito",sans-serif;font-size:11px;font-weight:800;'
    +   'letter-spacing:.08em;text-transform:uppercase;color:#7A88A8;}'
    + '.oao-bh-rung i{text-transform:none;font-family:"Lora",Georgia,serif;font-style:italic;'
    +   'font-weight:400;letter-spacing:0;margin-left:8px;}'
    + '.oao-bh-poem{font-family:"Lora",Georgia,serif;font-size:20px;line-height:2;color:#0E1C42;'
    +   'background:#FFFDF7;border:1px solid #EBD9AF;border-radius:10px;padding:20px 26px;margin:12px 0;}'
    + '.oao-bh-poem .ind{padding-left:38px;}'
    + '.oao-bh-poem w{transition:color .3s;}'
    + '.oao-bh-poem w.faded{color:#E2E8F4;}'
    + '.oao-bh-row{display:flex;gap:10px;flex-wrap:wrap;align-items:center;}'
    + '.oao-bh-btn{background:#0E1C42;color:#fff;border:none;border-radius:8px;padding:11px 22px;'
    +   'font-family:"Nunito",sans-serif;font-weight:800;font-size:14px;letter-spacing:.03em;cursor:pointer;}'
    + '.oao-bh-btn:hover{background:#16295c;}'
    + '.oao-bh-mini{background:#fff;border:2px solid #E6EBF5;border-radius:999px;padding:5px 14px;'
    +   'font-family:"Nunito",sans-serif;font-size:12px;font-weight:800;color:#7A88A8;cursor:pointer;}'
    + '.oao-bh-mini:hover{border-color:#C7922C;color:#0E1C42;}'
    + '.oao-bh-note{font-size:13px;color:#7A88A8;font-style:italic;}'
    + '.oao-bh-pick{display:flex;flex-wrap:wrap;gap:8px;margin:12px 0 4px;}'
    + '.oao-bh-pick button{background:#FFFDF7;border:2px solid #EBD9AF;border-radius:10px;'
    +   'padding:10px 14px;font-family:"Lora",Georgia,serif;font-size:15px;color:#0E1C42;cursor:pointer;text-align:left;}'
    + '.oao-bh-pick button:hover{border-color:#C7922C;}'
    + '.oao-bh-pick button.on{background:#FFF3DC;border-color:#C7922C;}'
    + '@media (prefers-reduced-motion: reduce){.oao-bh-poem w{transition:none;}}'
    /* ── recorded voice ── lifted verbatim from the sparkle demo, so a
       By Heart clip looks and behaves exactly like the poem control on
       lesson 7.1. Class names kept as .spk-audio* for the same reason:
       a lesson that already carries the sparkle layer styles it once. */
    + '.spk-audio{display:flex;align-items:center;gap:11px;margin:14px 0 2px;max-width:460px;}'
    + '.spk-audio[hidden]{display:none;}'
    + '.spk-audio-btn{display:inline-flex;align-items:center;gap:9px;flex:none;'
    +   'background:#FFFDF7;border:1.5px solid #E0CCA2;border-radius:999px;'
    +   'padding:7px 16px 7px 11px;cursor:pointer;font-family:"Nunito",sans-serif;'
    +   'font-size:13px;font-weight:700;color:#6E5A34;'
    +   'transition:border-color .18s,background .18s,transform .18s;}'
    + '.spk-audio-btn:hover{border-color:#C7922C;background:#FFF8E9;transform:translateY(-1px);}'
    + '.spk-audio-btn:focus-visible{outline:2px solid #C7922C;outline-offset:2px;}'
    + '.spk-audio-ico{width:19px;height:19px;flex:none;border-radius:50%;'
    +   'background:#C7922C;position:relative;}'
    + '.spk-audio-ico::before{content:"";position:absolute;left:7px;top:5px;'
    +   'border-left:7px solid #FFF8E9;border-top:4.5px solid transparent;'
    +   'border-bottom:4.5px solid transparent;}'
    + '.spk-audio.playing .spk-audio-ico::before{left:6px;top:5.5px;border:none;'
    +   'width:3px;height:8px;background:#FFF8E9;box-shadow:4px 0 0 #FFF8E9;}'
    + '.spk-audio-bar{flex:1 1 auto;height:4px;border-radius:2px;background:#EADCBE;overflow:hidden;}'
    + '.spk-audio-bar i{display:block;height:100%;width:0;background:#C7922C;transition:width .2s linear;}'
    + '.spk-audio-time{flex:none;font-family:"Nunito",sans-serif;font-size:11px;'
    +   'font-weight:700;color:#A08A5C;min-width:30px;text-align:right;}'
    + '.spk-audio-inline{margin:12px auto 4px;}'
    + '@media(max-width:700px){.spk-audio{gap:8px;}'
    +   '.spk-audio-btn{font-size:12px;padding:6px 13px 6px 9px;}}'
    + '@media (prefers-reduced-motion: reduce){.spk-audio-btn{transition:none;}'
    +   '.spk-audio-bar i{transition:none;}}'
    /* ── a recording that is a film ── also verbatim from the demo ── */
    + '.spk-media{margin:16px auto 4px;text-align:center;}'
    + '.spk-media[hidden]{display:none;}'
    + '.spk-media-video{display:block;margin:0 auto;max-width:100%;height:auto;'
    +   'background:#0E1C42;border-radius:10px;border:1px solid #E0CCA2;'
    +   'box-shadow:0 6px 18px rgba(46,32,14,.18);}'
    /* a portrait film would otherwise run the length of the page */
    + '.spk-media-tall .spk-media-video{max-height:440px;width:auto;}'
    + '.spk-media-video:focus-visible{outline:2px solid #C7922C;outline-offset:3px;}'
    + '.spk-media-cap{margin:8px 2px 0;font-family:"Lora",Georgia,serif;'
    +   'font-style:italic;font-size:13px;color:#8A7B5C;}'
    + '@media(max-width:700px){.spk-media-tall .spk-media-video{max-height:360px;}}';

  function injectCSS() {
    if (document.getElementById('oao-bh-css')) return;
    var s = document.createElement('style');
    s.id = 'oao-bh-css';
    s.textContent = CSS;
    document.head.appendChild(s);
  }

  function esc(s) {
    return String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  /* ═══════════════════════════════════════════════════════════════
     §5.5  RECORDED VOICE
     ───────────────────────────────────────────────────────────────
     Same method and same script as lesson-7-1-anne-ch1-SPARKLE.html:
     the control is BUILT HIDDEN and reveals itself only once the
     browser reports the file's metadata. A poem with no recording yet
     shows nothing — never a button that does nothing. Clips can
     therefore arrive over months with no code change.

     What changed from the demo, and only this: the demo keyed the
     poem clip off DATA.poem, one hardcoded poem per lesson file.
     Under Option A the poem is per-arc, so the slug comes from
     POEMS[arc].title instead. The naming rule is untouched.

     Five clips for the year, one per arc that has a ladder:

       assets/audio/poem/hope-is-the-thing-with-feathers.mp3
       assets/audio/poem/who-has-seen-the-wind.mp3
       assets/audio/poem/there-will-come-soft-rains.mp3
       assets/audio/poem/sympathy.mp3
       assets/audio/poem/forest-remembers.mp3

     NOTE THE LAST ONE. slug() drops a leading "The/A/An", so
     "The Forest Remembers" is forest-remembers, not
     the-forest-remembers. See claude/g4-audio-spec.md §2 — a
     filename mismatch is exactly the failure the hidden-until-
     confirmed design produces, and it is silent. If a control never
     appears, suspect the filename first.

     lady-of-shalott.mp3 is now surplus: The Lady of Shalott is not
     one of the five.
     ═══════════════════════════════════════════════════════════════ */

  /* Relative, so the same page works opened straight from the repo
     folder and served from GitHub Pages. */
  var AUDIO_BASE = window.OAO_AUDIO_BASE || 'assets/audio/';

  /* The leading article goes. It keeps a folder of poems sorting by
     the word that matters, and it is what the spec told the recordist
     to name the file. The spec wins. */
  function slug(s) {
    return String(s).toLowerCase().replace(/[\u2019']/g, '')
      .replace(/^(the|a|an)\s+/, '')
      .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
  }

  function poemAudioURL(title) {
    if (!AUDIO_BASE || !title) return '';
    return AUDIO_BASE + 'poem/' + slug(title) + '.mp3';
  }

  /* One clip plays at a time, and starting one silences the page's
     text-to-speech reader — two voices at once is the worst outcome.
     Shared with the demo's player when both are on the page. */
  function audioStopAll(except) {
    var cur = window._nowPlaying;
    if (cur && cur !== except) { try { cur.pause(); } catch (e) {} }
    try { if (window.speechSynthesis) window.speechSynthesis.cancel(); } catch (e) {}
  }

  function mmss(t) {
    if (!isFinite(t)) return '';
    var m = Math.floor(t / 60), sec = Math.floor(t % 60);
    return m + ':' + (sec < 10 ? '0' : '') + sec;
  }

  /* Builds the control hidden, and reveals it only once the file is
     known to exist. A missing recording is silent in both senses. */
  function audioControl(src, label) {
    if (!src) return null;

    var wrap = document.createElement('div');
    wrap.className = 'spk-audio';
    wrap.hidden = true;
    wrap.innerHTML =
      '<button type="button" class="spk-audio-btn">' +
        '<span class="spk-audio-ico" aria-hidden="true"></span>' +
        '<span class="spk-audio-label"></span>' +
      '</button>' +
      '<span class="spk-audio-bar"><i></i></span>' +
      '<span class="spk-audio-time"></span>';

    var btn  = wrap.querySelector('.spk-audio-btn');
    var lab  = wrap.querySelector('.spk-audio-label');
    var fill = wrap.querySelector('.spk-audio-bar i');
    var time = wrap.querySelector('.spk-audio-time');
    lab.textContent = label;
    btn.setAttribute('aria-label', label);

    var a = new Audio();
    a.preload = 'metadata';
    a.src = src;

    a.addEventListener('loadedmetadata', function () {
      wrap.hidden = false;                     /* the file is really there */
      time.textContent = mmss(a.duration);
    });
    a.addEventListener('error', function () { wrap.remove(); });
    a.addEventListener('timeupdate', function () {
      if (a.duration) fill.style.width = (a.currentTime / a.duration * 100) + '%';
    });
    a.addEventListener('ended', function () {
      wrap.classList.remove('playing'); btn.setAttribute('aria-pressed', 'false');
      fill.style.width = '0%'; time.textContent = mmss(a.duration);
      window._nowPlaying = null;
    });
    a.addEventListener('pause', function () {
      wrap.classList.remove('playing'); btn.setAttribute('aria-pressed', 'false');
    });
    a.addEventListener('play', function () {
      wrap.classList.add('playing'); btn.setAttribute('aria-pressed', 'true');
    });

    btn.setAttribute('aria-pressed', 'false');
    btn.onclick = function () {
      if (a.paused) { audioStopAll(a); window._nowPlaying = a; a.play().catch(function () {}); }
      else { a.pause(); }
    };
    return wrap;
  }

  /* ── the same place, on film ─────────────────────────────────
     The poem is a FILM when one exists. Keys and folders mirror the
     audio exactly, so poem/who-has-seen-the-wind.mp4 sits beside
     poem/who-has-seen-the-wind.mp3, and when both exist the film wins.

       assets/video/poem/<poem-slug>.mp4   (+ .jpg poster, optional)

     Encode browser-safe or it will not play at all:
       H.264 **High** profile, **yuv420p**, AAC audio, +faststart.
     High 4:4:4 Predictive / yuv444p — what several AI video tools emit
     by default — has no decoder in any mainstream browser. The first
     poem film arrived that way; see claude/g4-audio-spec.md §9.     */
  var VIDEO_BASE = window.OAO_VIDEO_BASE || 'assets/video/';

  function poemVideoURL(title) {
    if (!VIDEO_BASE || !title) return '';
    return VIDEO_BASE + 'poem/' + slug(title) + '.mp4';
  }
  function posterURL(src) {
    return src ? src.replace(/\.mp4(\?|$)/i, '.jpg$1') : '';
  }

  /* Same contract as the audio control: built hidden, revealed only
     once the browser confirms it can actually decode the file, removed
     if it cannot. That check is what catches an unplayable profile —
     the page falls back to the voice recording instead of showing a
     black box. */
  function videoControl(src, label, onFail) {
    if (!src) { onFail(); return null; }

    var fig = document.createElement('figure');
    fig.className = 'spk-media';
    fig.hidden = true;

    var v = document.createElement('video');
    v.className = 'spk-media-video';
    v.controls = true;
    v.playsInline = true;
    v.setAttribute('playsinline', '');
    v.preload = 'metadata';
    v.setAttribute('aria-label', label);

    var srcEl = document.createElement('source');
    srcEl.src = src;
    srcEl.type = /\.webm(\?|$)/i.test(src) ? 'video/webm' : 'video/mp4';
    v.appendChild(srcEl);

    var settled = false;
    v.addEventListener('loadedmetadata', function () {
      settled = true;
      fig.hidden = false;
      /* the poster is only worth fetching once we know the film is
         real — set earlier it would 404 alongside every absent film */
      var poster = posterURL(src);
      if (poster) v.poster = poster;
      /* portrait or landscape, let the box follow the film */
      if (v.videoWidth && v.videoHeight) {
        fig.style.setProperty('--spk-ar', v.videoWidth + ' / ' + v.videoHeight);
        if (v.videoHeight > v.videoWidth) fig.classList.add('spk-media-tall');
      }
    });
    var fail = function () {
      if (settled) return;
      settled = true;
      fig.remove();
      onFail();                    /* no film, or one no browser can play */
    };
    v.addEventListener('error', fail);
    srcEl.addEventListener('error', fail);
    v.addEventListener('play', function () {
      audioStopAll(v); window._nowPlaying = v;
    });

    var cap = document.createElement('figcaption');
    cap.className = 'spk-media-cap';
    cap.textContent = label;
    fig.appendChild(v); fig.appendChild(cap);
    return fig;
  }

  /* Put a recording in place: the film if there is one, the voice clip
     if there is not, nothing at all if there is neither. The film is
     tried first so the control never appears twice or flickers. */
  function placeMedia(title, watchLabel, hearLabel, how) {
    var audioFallback = function () {
      /* a voice clip is heard, not watched — the label has to follow
         whichever one the student actually got */
      var a = audioControl(poemAudioURL(title), hearLabel);
      if (a) { a.classList.add('spk-audio-inline'); how(a); }
    };
    var vid = videoControl(poemVideoURL(title), watchLabel, audioFallback);
    if (vid) how(vid);
  }

  /* ── §6  build ──────────────────────────────────────────────────── */
  function build() {
    /* The gate. By Heart appears exactly where Poetry Corner appeared,
       and nowhere else. One line, no per-lesson configuration.        */
    var box = document.querySelector('.poem-box');
    if (!box) return;

    var L = lessonInfo();
    if (!L || !L.week) return;

    var arcHere = arcOf(L.week);
    var arc = ladderArc(L.week);
    if (!arc) return;

    /* The activity that holds the Poetry Corner. */
    var host = box.closest ? box.closest('.activity') : null;
    if (!host) {
      var p = box.parentNode;
      while (p && p.className && p.className.indexOf('activity') === -1) p = p.parentNode;
      host = p;
    }
    if (!host || host.getAttribute('data-oao-retired')) return;

    injectCSS();

    var card = document.createElement('div');
    card.className = 'activity bl-gold oao-bh-wrap';
    card.setAttribute('data-oao-byheart', arc);

    if (POEMS[arc]) buildLadder(card, arc);
    else buildRecital(card);

    /* Rescue anything in the old activity that is the student's, not
       the poem's. Weeks 24-32 keep a saved journal textarea inside the
       Poetry Corner; retiring the activity would delete a writing box
       that autosaves and feeds the printable journal. It moves. */
    rescueJournal(host, card);

    /* Retire, do not destroy. The original Poetry Corner stays in the
       DOM, hidden and labelled, so this is one attribute away from
       being undone.                                                   */
    host.setAttribute('data-oao-retired', 'poetry-corner');
    host.style.display = 'none';
    host.parentNode.insertBefore(card, host);
  }

  /* ── 6.1  journal rescue ─────────────────────────────────
     In weeks 24-32 the Poetry Corner holds a .journal-box: a saved
     textarea wired to autoSave() and gatherAnswers() by inline
     handlers, and collected by the print-to-journal popup under
     #journal-poetry. That belongs to the student, so it survives the
     swap. Moving the node keeps every inline handler and the id
     intact, so autosave and the journal export need no change.

     The prompt that sat above it was written to one specific poem and
     cannot follow, so By Heart asks its own question instead — one
     that works in any arc, because the poem is now per-arc.        */
  var JOURNAL_PROMPT =
    'Say your poem aloud from memory, as far as you can get. ' +
    'Which line is hardest to hold on to — and what do you think ' +
    'makes that one slippery?';

  function rescueJournal(host, card) {
    var box = host.querySelector('.journal-box');
    if (!box) return;
    var body = card.querySelector('.oao-bh-body');
    if (!body) return;

    var label = host.querySelector('.journal-label');

    var prompt = document.createElement('p');
    prompt.style.cssText = 'font-size:17px;color:#3A4A6B;line-height:1.75;margin:16px 0 0;';
    prompt.textContent = JOURNAL_PROMPT;
    body.appendChild(prompt);

    /* The placeholder was written for the retired prompt and names the
       old poem's book. Re-point it at the question actually being
       asked; the id, handlers and saved text are untouched.        */
    box.setAttribute('placeholder',
      'The line I keep losing is... I think it slips because...');

    if (label) body.appendChild(label);
    body.appendChild(box);
  }

  /* ── 6a  the eight-rung ladder ──────────────────────────────────── */
  function buildLadder(card, arc) {
    var poem = POEMS[arc];
    var rung = rungOf(arc);

    card.innerHTML =
      '<div class="oao-bh-head"><div class="oao-bh-num">♪</div><div>' +
        '<div class="oao-bh-title">By Heart · “' + esc(poem.title) + '”</div>' +
        '<div class="oao-bh-sub">' + esc(poem.author) + ' · one stanza, held all the way through this book</div>' +
      '</div></div>' +
      '<div class="oao-bh-body">' +
        '<div class="oao-bh-rung" data-role="rung"></div>' +
        '<div class="oao-bh-poem" data-role="poem"></div>' +
        '<div class="oao-bh-row">' +
          '<button type="button" class="oao-bh-btn" data-role="said">I said it aloud</button>' +
          '<button type="button" class="oao-bh-mini" data-role="more">Show a little more</button>' +
          '<span class="oao-bh-note" data-role="note"></span>' +
        '</div>' +
      '</div>';

    var poemHost = card.querySelector('[data-role="poem"]');
    var rungHost = card.querySelector('[data-role="rung"]');
    var note     = card.querySelector('[data-role="note"]');

    function paint(r) {
      var s = '';
      poem.lines.forEach(function (ln, li) {
        var ws = ln[0].split(' ');
        var hide = fadeMask(ws, li, r);
        s += '<div class="' + (ln[1] ? 'ind' : '') + '">' + ws.map(function (w, wi) {
          return '<w class="' + (hide[wi] ? 'faded' : '') + '">' + esc(w) + '</w>';
        }).join(' ') + '</div>';
      });
      poemHost.innerHTML = s;
      rungHost.innerHTML = 'Rung ' + r + ' of 8<i>' + rungBlurb(r) + '</i>';
    }
    paint(rung);

    /* The model reading, directly under the stanza and above the
       button that says they have recited it — the demo's placement.
       Film first; the voice clip only if there is no film. */
    placeMedia(poem.title, 'Watch the poem read aloud', 'Hear the poem read aloud',
      function (el) { poemHost.parentNode.insertBefore(el, poemHost.nextSibling); });

    card.querySelector('[data-role="more"]').onclick = function () {
      if (rung <= 1) return;
      paint(Math.max(1, rung - 1));
      setTimeout(function () { paint(rung); }, 8000);
    };

    card.querySelector('[data-role="said"]').onclick = function () {
      var m = memState();
      if (!m[arc]) m[arc] = { rung: 1, advancedOn: null };
      var today = new Date().toISOString().slice(0, 10);
      if (m[arc].rung >= 8) {
        m[arc].learned = true;
        Sparkle.set('oao.g4ela.memory', m);
        note.textContent = 'You know it by heart. Say it to someone.';
        return;
      }
      if (m[arc].advancedOn === today) {
        note.textContent = 'You have climbed a rung today already. Come back tomorrow.';
        return;
      }
      m[arc].rung += 1;
      m[arc].advancedOn = today;
      if (m[arc].rung >= 8) m[arc].learned = true;
      Sparkle.set('oao.g4ela.memory', m);
      rung = m[arc].rung;
      paint(rung);
      note.textContent = 'A little less to lean on now.';
      if (typeof window.owlSay === 'function') window.owlSay('Said aloud is how it sticks.');
    };
  }

  /* ── 6b  weeks 31–32 — recite one you already know ─────────────── */
  function buildRecital(card) {
    var m = memState();
    var climbed = ARC_ORDER.filter(function (a) { return m[a] && m[a].rung > 1; });
    var list = climbed.length ? climbed : ARC_ORDER;

    var buttons = list.map(function (a) {
      var done = m[a] && m[a].rung >= 8;
      return '<button type="button" data-arc="' + a + '">' +
        '“' + esc(POEMS[a].title) + '”<br>' +
        '<span style="font-family:Nunito,sans-serif;font-size:12px;color:#7A88A8;">' +
        esc(ARC_LABEL[a]) + (done ? ' · learned' : '') + '</span></button>';
    }).join('');

    card.innerHTML =
      '<div class="oao-bh-head"><div class="oao-bh-num">♪</div><div>' +
        '<div class="oao-bh-title">By Heart · One You Already Know</div>' +
        '<div class="oao-bh-sub">No new poem this week — you have five of them already</div>' +
      '</div></div>' +
      '<div class="oao-bh-body">' +
        '<p style="font-size:17px;color:#3A4A6B;line-height:1.75;margin:0 0 4px;">' +
          'Every book this year left you a poem. Pick one and say it out loud, ' +
          'from memory, to somebody who has not heard it.</p>' +
        '<div class="oao-bh-pick">' + buttons + '</div>' +
        '<div class="oao-bh-poem" data-role="poem" style="display:none;"></div>' +
        '<div class="oao-bh-row">' +
          '<button type="button" class="oao-bh-mini" data-role="peek" style="display:none;">Let me check the words</button>' +
          '<span class="oao-bh-note" data-role="note"></span>' +
        '</div>' +
      '</div>';

    var poemHost = card.querySelector('[data-role="poem"]');
    var peek     = card.querySelector('[data-role="peek"]');
    var note     = card.querySelector('[data-role="note"]');
    var chosen   = null;

    card.querySelectorAll('.oao-bh-pick button').forEach(function (b) {
      b.onclick = function () {
        card.querySelectorAll('.oao-bh-pick button').forEach(function (x) { x.classList.remove('on'); });
        b.classList.add('on');
        chosen = b.getAttribute('data-arc');
        poemHost.style.display = 'none';
        peek.style.display = '';
        note.textContent = 'Say it first. The words are here if you get stuck.';

        /* Swap the reading to whichever poem they picked. */
        var had = card.querySelectorAll('.spk-audio, .spk-media');
        for (var i = 0; i < had.length; i++) had[i].remove();
        placeMedia(POEMS[chosen].title, 'Watch it read aloud', 'Hear it read aloud',
          function (el) { poemHost.parentNode.insertBefore(el, poemHost); });
      };
    });

    peek.onclick = function () {
      if (!chosen) return;
      poemHost.innerHTML = POEMS[chosen].lines.map(function (ln) {
        return '<div class="' + (ln[1] ? 'ind' : '') + '">' + esc(ln[0]) + '</div>';
      }).join('');
      poemHost.style.display = '';
      note.textContent = '';
    };
  }

  /* ── §7  go ─────────────────────────────────────────────────────── */
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', build);
  } else {
    build();
  }
})();
