/* ═══════════════════════════════════════════════════════════════════
   OAO NTS Kit · weeks 16–19 (Number the Stars)
   No character voices in a copyrighted book, so the real history does
   the work: Annemarie's Path (a map that grows chapter by chapter),
   the Museum Case (one real object a lesson), Then & Now (a drag
   slider), Real Rescuers (portrait cards collected across the unit),
   and the Psalm card (the title's source, on the day the book reaches
   it). Grete, the narrator, speaks as a witness: a storyteller who
   grew up in Copenhagen. She is invented and says so.

   OAONtsKit.mount(kind, host, { week, day, base: 'assets/', cfg: DATA.nts })
   Every card hides itself when what it needs is missing.
   ═══════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';
  var KIT = window.OAONtsKit = window.OAONtsKit || {};
  /* Øresund shapes: the same Natural Earth outline the bridge week used (public domain) */
  var ORESUND = {"denmark":"M357,265L370,298L370,300L362,309L354,312L348,318L343,320L338,312L335,302L335,293L337,288L346,279L352,264L355,260ZM36,405L35,399L28,398L25,401L23,405L16,405L16,405L13,393L20,394L25,392L33,385L40,383L42,378L42,373L39,371L40,367L38,359L31,339L25,334L20,333L13,337L12,335L14,326L25,323L27,317L26,310L24,302L13,290L3,283L-5,281L-5,275L-5,275L13,277L10,270L-3,264L-5,263L-5,248L-5,248L1,249L8,248L23,243L30,241L30,244L25,243L21,246L25,253L30,259L38,261L43,257L34,249L37,246L38,249L50,249L55,248L62,242L70,240L76,234L78,220L77,214L72,205L78,209L84,210L88,208L93,203L101,204L107,193L109,178L101,164L95,161L80,160L63,153L57,149L55,142L84,156L90,155L124,160L129,164L138,163L154,159L162,153L166,153L169,156L168,160L160,172L162,176L161,179L157,180L154,178L155,172L145,174L143,178L154,197L158,209L155,216L152,217L144,215L141,216L135,224L131,224L131,228L134,229L145,228L156,222L160,222L164,232L165,241L147,245L142,249L147,252L158,251L161,249L165,252L171,260L173,267L169,277L176,269L185,249L185,245L183,240L185,228L189,219L193,216L204,211L208,199L198,174L200,167L204,168L211,176L218,180L217,191L218,197L221,203L225,214L229,230L230,246L224,255L216,251L212,252L209,263L201,271L198,277L202,277L209,275L215,269L215,263L219,261L223,263L226,266L228,271L220,269L221,273L224,275L232,279L234,271L239,258L240,249L231,205L231,191L230,186L224,164L221,159L217,157L212,157L194,163L188,165L185,161L188,151L200,142L221,128L256,99L274,89L292,90L312,101L328,101L332,103L340,111L346,113L358,123L355,130L346,142L342,149L337,165L333,172L340,182L345,193L346,200L348,209L354,222L352,231L352,240L350,251L354,257L349,263L340,281L332,287L328,296L323,298L313,293L309,293L293,302L274,322L263,345L269,366L280,376L284,377L298,378L311,388L316,394L318,400L319,405L36,405Z","sweden":"M645,367L641,367L632,371L618,369L588,371L584,373L580,379L573,384L564,383L556,385L535,399L529,401L513,403L506,401L469,387L457,387L448,385L445,381L438,379L431,381L426,385L420,383L405,387L405,380L412,366L414,366L422,373L427,373L432,370L435,366L434,359L440,361L438,350L427,333L425,321L427,309L434,301L449,290L456,276L457,271L455,263L449,256L446,249L442,251L437,250L435,243L426,241L423,235L428,233L430,224L426,207L418,199L409,195L403,186L400,177L400,171L398,167L392,161L389,147L388,142L380,136L378,132L377,124L375,120L355,94L346,72L343,68L340,51L334,39L332,30L323,23L320,18L363,37L368,45L377,51L382,49L393,49L397,49L401,45L405,40L405,34L405,28L394,23L390,14L383,-4L382,-5L645,-5Z","_pts":{"copenhagen":[347,269],"helsingor":[356,129],"helsingborg":[374,121],"gilleleje":[289,93],"malmo":[443,301],"dragor":[369,305]}};

  /* which chapter each lesson reaches (the afterword counts as 18) */
  var CH = { '16.1': 1, '16.2': 2, '16.3': 3, '16.4': 4, '17.1': 5, '17.2': 6, '17.3': 7, '17.4': 8,
             '18.1': 9, '18.2': 10, '18.3': 11, '18.4': 12, '19.1': 14, '19.2': 15, '19.3': 17, '19.4': 18 };
  function chOf(opt) { return CH[opt.week + '.' + opt.day] || 1; }
  function lidNum(l) { var p = String(l).split('.'); return (+p[0]) * 10 + (+p[1]); }

  var CSS = ''
  + '.nk-card{background:#fff;border:1px solid #E6EBF5;border-radius:12px;overflow:hidden;margin:18px 0;box-shadow:0 1px 4px rgba(14,28,66,.05);border-left:5px solid #3D5F7A;font-family:"Lora",Georgia,serif;color:#0E1C42;}'
  + '.nk-head{display:flex;gap:12px;align-items:center;padding:12px 18px;background:linear-gradient(135deg,#F3F6FA,#E9EFF6);border-bottom:1px solid #DCE4EE;}'
  + '.nk-num{width:34px;height:34px;border-radius:8px;background:#3D5F7A;color:#fff;display:flex;align-items:center;justify-content:center;font-size:17px;flex:none;}'
  + '.nk-ht{flex:1;min-width:0;}'
  + '.nk-title{font-family:"Nunito",sans-serif;font-size:17px;font-weight:800;}'
  + '.nk-sub{font-size:15px;color:#56627F;font-style:italic;}'
  + '.nk-what-btn{flex:none;font-family:"Nunito",sans-serif;font-size:12px;font-weight:800;color:#3D5F7A;background:#fff;border:2px solid #C9D6E4;border-radius:999px;padding:4px 12px;cursor:pointer;}'
  + '.nk-what-btn:hover,.nk-what-btn[aria-expanded="true"]{border-color:#3D5F7A;}'
  + '.nk-what{padding:12px 20px 2px;background:#FAFCFE;border-bottom:1px solid #DCE4EE;font-size:15.5px;line-height:1.65;color:#3A4A6B;}'
  + '.nk-what p{margin:0 0 10px;max-width:70ch;}'
  + '.nk-body{padding:14px 20px 16px;}'
  + '.nk-card button:focus-visible,.nk-card input:focus-visible,.nk-card [tabindex]:focus-visible{outline:3px solid #C7922C;outline-offset:2px;}'
  + '.nk-cred{display:block;font-family:"Nunito",sans-serif;font-size:11px;color:#8A94A8;margin-top:6px;line-height:1.4;}'
  + '.nk-voice{display:inline-flex;align-items:center;gap:8px;font-family:"Nunito",sans-serif;font-size:13px;font-weight:800;color:#3D5F7A;background:#F3F6FA;border:2px solid #C9D6E4;border-radius:999px;padding:6px 14px;cursor:pointer;margin:2px 0 10px;}'
  + '.nk-voice[hidden]{display:none;}'
  + '.nk-voice[aria-pressed="true"]{border-color:#C7922C;background:#FFF8E9;color:#0E1C42;}'
  + '.nk-voice i{font-style:normal;}'
  /* Annemarie's Path */
  + '.nk-tabs{display:flex;gap:6px;margin:0 0 10px;flex-wrap:wrap;}'
  + '.nk-tab{font-family:"Nunito",sans-serif;font-size:12.5px;font-weight:800;border:2px solid #DCE4EE;background:#fff;color:#56627F;border-radius:999px;padding:5px 13px;cursor:pointer;}'
  + '.nk-tab[aria-pressed="true"]{border-color:#3D5F7A;color:#0E1C42;background:#EEF3F8;}'
  + '.nk-map{position:relative;border-radius:10px;overflow:hidden;border:1px solid #D9CBA8;box-shadow:inset 0 0 0 3px #FFFDF6;}'
  + '.nk-map svg{display:block;width:100%;height:auto;}'
  + '.nk-map .pin{cursor:pointer;outline:none;}'
  + '.nk-map .pin .hit{fill:transparent;}'
  + '.nk-map .pin .drop{fill:#A8432F;stroke:#6E2716;stroke-width:1;}'
  + '.nk-map .pin.story .drop{fill:#FFF8E7;stroke:#7A5A2A;stroke-width:1.4;stroke-dasharray:2.5 2;}'
  + '.nk-map .pin .dot{fill:#FFF3D6;}'
  + '.nk-map .pin.story .dot{fill:#7A5A2A;}'
  + '.nk-map .pin.today .drop,.nk-map .pin.today .dot{animation:nk-bob 1.6s ease-in-out infinite;}'
  + '@keyframes nk-bob{50%{transform:translateY(-3px);}}'
  + '.nk-map .pin .ring{fill:none;stroke:#C7922C;stroke-width:2;opacity:0;}'
  + '.nk-map .pin.sel .ring,.nk-map .pin:focus-visible .ring{opacity:1;}'
  + '.nk-map .pl{font:700 10.5px "Nunito",sans-serif;fill:#3B2E17;paint-order:stroke;stroke:#F6EEDB;stroke-width:3px;stroke-linejoin:round;}'
  + '.nk-map .pl.story{font-style:italic;fill:#6B5126;}'
  + '.nk-info{margin-top:10px;padding:10px 14px;border-radius:10px;background:#FBF7EC;border:1px solid #EBDDBB;font-size:15.5px;line-height:1.6;color:#3A4A6B;min-height:3.2em;}'
  + '.nk-info b{color:#0E1C42;}'
  + '.nk-tag{display:inline-block;font-family:"Nunito",sans-serif;font-size:10.5px;font-weight:800;letter-spacing:.08em;text-transform:uppercase;border-radius:999px;padding:2px 8px;margin-right:6px;vertical-align:2px;}'
  + '.nk-tag.real{background:#F5E1DA;color:#8A3220;}'
  + '.nk-tag.story{background:#F3ECD9;color:#6B5126;border:1px dashed #B79E6A;}'
  + '.nk-tag.ch{background:#E9EFF6;color:#3D5F7A;}'
  + '.nk-legend{display:flex;gap:14px;flex-wrap:wrap;margin-top:8px;font-family:"Nunito",sans-serif;font-size:12px;color:#56627F;}'
  + '.nk-legend span{display:inline-flex;align-items:center;gap:6px;}'
  + '.nk-legend i{width:11px;height:11px;border-radius:50% 50% 50% 0;transform:rotate(-45deg);display:inline-block;background:#A8432F;}'
  + '.nk-legend i.s{background:#FFF8E7;border:1.4px dashed #7A5A2A;}'
  /* the museum case */
  + '.nk-case{display:grid;grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);gap:18px;align-items:start;}'
  + '@media (max-width:620px){.nk-case{grid-template-columns:1fr;}}'
  + '.nk-vitrine{position:relative;padding:14px;border-radius:10px;background:linear-gradient(160deg,#4A3424,#2C1E14);box-shadow:inset 0 0 0 2px #6B4E33,0 6px 16px -8px rgba(30,18,8,.6);}'
  + '.nk-glass{position:relative;border-radius:4px;overflow:hidden;background:radial-gradient(ellipse at 50% 20%,#3B4652 0%,#1A2129 75%);padding:16px;min-height:120px;display:flex;align-items:center;justify-content:center;}'
  + '.nk-glass::before{content:"";position:absolute;inset:0;background:radial-gradient(ellipse 60% 45% at 50% 0%,rgba(255,240,205,.35),transparent 70%);pointer-events:none;}'
  + '.nk-glass::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,transparent 30%,rgba(255,255,255,.10) 42%,transparent 48%);pointer-events:none;}'
  + '.nk-glass img{position:relative;max-width:100%;max-height:300px;display:block;border-radius:2px;box-shadow:0 10px 22px -8px rgba(0,0,0,.75);cursor:zoom-in;}'
  + '.nk-plaque{margin:12px auto 0;max-width:92%;padding:8px 12px;border-radius:3px;text-align:center;background:linear-gradient(180deg,#F1DCA0,#D2B062);color:#3D2B0C;box-shadow:inset 0 1px 0 rgba(255,255,255,.6),0 2px 4px rgba(0,0,0,.4);font-family:"Lora",Georgia,serif;}'
  + '.nk-plaque b{display:block;font-size:15px;}'
  + '.nk-plaque span{font-family:"Nunito",sans-serif;font-size:11px;font-weight:800;letter-spacing:.1em;text-transform:uppercase;}'
  + '.nk-label{font-size:15.5px;line-height:1.65;color:#3A4A6B;}'
  + '.nk-label p{margin:0 0 10px;}'
  + '.nk-look{margin-top:6px;border-top:1px dashed #DCE4EE;padding-top:10px;}'
  + '.nk-look-h{font-family:"Nunito",sans-serif;font-size:12px;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:#3D5F7A;margin-bottom:6px;}'
  + '.nk-q{margin:0 0 8px;}'
  + '.nk-q button{all:unset;box-sizing:border-box;width:100%;cursor:pointer;display:block;font-size:15.5px;line-height:1.5;color:#0E1C42;padding:6px 10px;border-radius:8px;background:#F3F6FA;}'
  + '.nk-q button::before{content:"\\1F50D  ";}'
  + '.nk-q button:hover{background:#E9EFF6;}'
  + '.nk-q .a{font-size:15px;line-height:1.55;color:#3A4A6B;padding:6px 10px 2px 30px;}'
  + '.nk-zoom{position:fixed;inset:0;z-index:99999;background:rgba(10,14,24,.88);display:flex;align-items:center;justify-content:center;padding:20px;cursor:zoom-out;}'
  + '.nk-zoom img{max-width:96vw;max-height:92vh;border-radius:4px;box-shadow:0 10px 40px rgba(0,0,0,.6);}'
  /* then & now */
  + '.nk-tn{position:relative;border-radius:10px;overflow:hidden;user-select:none;-webkit-user-select:none;background:#222;aspect-ratio:3/2;}'
  + '.nk-tn img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;display:block;pointer-events:none;}'
  + '.nk-tn .then{clip-path:inset(0 calc(100% - var(--x,50%)) 0 0);}'
  + '.nk-tn .bar{position:absolute;top:0;bottom:0;left:var(--x,50%);width:3px;margin-left:-1.5px;background:#FFF8E7;box-shadow:0 0 6px rgba(0,0,0,.5);pointer-events:none;}'
  + '.nk-tn .knob{position:absolute;top:50%;left:var(--x,50%);width:40px;height:40px;margin:-20px 0 0 -20px;border-radius:50%;background:#FFF8E7;border:2px solid #C7922C;display:flex;align-items:center;justify-content:center;font:800 15px "Nunito",sans-serif;color:#5A4416;box-shadow:0 2px 8px rgba(0,0,0,.4);pointer-events:none;}'
  + '.nk-tn .yr{position:absolute;bottom:10px;font:800 12px "Nunito",sans-serif;letter-spacing:.08em;color:#fff;background:rgba(14,28,66,.72);padding:3px 9px;border-radius:999px;pointer-events:none;}'
  + '.nk-tn .yr.l{left:10px;} .nk-tn .yr.r{right:10px;}'
  + '.nk-tn input{position:absolute;inset:0;width:100%;height:100%;opacity:0;cursor:ew-resize;margin:0;}'
  + '.nk-tn-cap{font-size:15.5px;line-height:1.6;color:#3A4A6B;margin:10px 0 0;}'
  /* real rescuers */
  + '.nk-shelf{display:grid;grid-template-columns:repeat(auto-fill,minmax(160px,1fr));gap:14px;}'
  + '.nk-rc{perspective:900px;}'
  + '.nk-rc .flipper{all:unset;display:block;width:100%;height:250px;cursor:pointer;position:relative;transform-style:preserve-3d;transition:transform .6s;}'
  + '.nk-rc.flip .flipper{transform:rotateY(180deg);}'
  + '.nk-rf,.nk-rb{position:absolute;inset:0;backface-visibility:hidden;-webkit-backface-visibility:hidden;border-radius:10px;overflow:hidden;border:1px solid #D9CBA8;box-shadow:0 3px 10px -5px rgba(14,28,66,.4);}'
  + '.nk-rf{background:#FFFDF6;display:flex;flex-direction:column;}'
  + '.nk-rf .ph{flex:1;background:#E8E1D0 center 22%/cover no-repeat;display:flex;align-items:center;justify-content:center;font:600 40px "Lora",Georgia,serif;color:#9C8A64;filter:grayscale(.15) sepia(.2);}'
  + '.nk-rf .nm{padding:8px 10px 9px;text-align:center;border-top:3px double #C7922C;}'
  + '.nk-rf .nm b{display:block;font-size:15px;line-height:1.25;}'
  + '.nk-rf .nm span{font-family:"Nunito",sans-serif;font-size:11px;color:#56627F;}'
  + '.nk-rf .turn{position:absolute;top:8px;right:8px;font:800 10px "Nunito",sans-serif;color:#7A6A44;background:rgba(255,253,246,.85);border-radius:999px;padding:2px 7px;}'
  + '.nk-rb{transform:rotateY(180deg);background:#FBF7EC;padding:12px 12px 10px;font-size:13.5px;line-height:1.5;color:#3A4A6B;overflow:auto;}'
  + '.nk-rb b{color:#0E1C42;}'
  + '.nk-rc.new .nk-rf::after{content:"New today";position:absolute;top:8px;left:8px;font:800 10px "Nunito",sans-serif;letter-spacing:.08em;text-transform:uppercase;background:#C7922C;color:#fff;padding:3px 8px;border-radius:999px;}'
  + '.nk-count{font-family:"Nunito",sans-serif;font-size:13px;color:#56627F;margin:0 0 10px;}'
  /* the psalm */
  + '.nk-psalm{position:relative;border-radius:10px;overflow:hidden;background:radial-gradient(ellipse at 50% 0%,#24386A,#0B1430 70%);padding:30px 20px 26px;text-align:center;color:#F6EBCB;}'
  + '.nk-psalm .sk{position:absolute;inset:0;pointer-events:none;}'
  + '.nk-psalm blockquote{position:relative;margin:0 auto;max-width:30ch;font:italic 500 24px/1.45 "Lora",Georgia,serif;}'
  + '.nk-psalm cite{position:relative;display:block;margin-top:12px;font:800 12px "Nunito",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#C9B47A;font-style:normal;}'
  + '@media (prefers-reduced-motion:reduce){.nk-map .pin.today .drop,.nk-map .pin.today .dot{animation:none;}.nk-rc .flipper{transition:none;}}';

  function injectCSS() {
    if (document.getElementById('nk-css')) return;
    var s = document.createElement('style'); s.id = 'nk-css'; s.textContent = CSS; document.head.appendChild(s);
  }
  function esc(t) { return String(t == null ? '' : t).replace(/[&<>"]/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]; }); }
  var uid = 0;
  function card(icon, title, sub, what) {
    var id = 'nk' + (++uid);
    var el = document.createElement('div');
    el.className = 'nk-card';
    var has = what && what.length;
    el.innerHTML =
      '<div class="nk-head"><div class="nk-num" aria-hidden="true">' + icon + '</div>' +
      '<div class="nk-ht"><div class="nk-title">' + esc(title) + '</div><div class="nk-sub">' + esc(sub) + '</div></div>' +
      (has ? '<button type="button" class="nk-what-btn" aria-expanded="false" aria-controls="' + id + '-w">What is this?</button>' : '') + '</div>' +
      (has ? '<div class="nk-what" id="' + id + '-w" hidden>' + what.map(function (p) { return '<p>' + p + '</p>'; }).join('') + '</div>' : '') +
      '<div class="nk-body"></div>';
    var btn = el.querySelector('.nk-what-btn'), w = el.querySelector('.nk-what');
    if (btn) btn.onclick = function () { w.hidden = !w.hidden; btn.setAttribute('aria-expanded', String(!w.hidden)); };
    return el;
  }
  function src(opt, p) { return /^(https?:|\/)/.test(p) ? p : (opt.base || 'assets/') + p; }

  /* One voice at a time: a Grete clip stops any other kit clip, and the
     sparkle layer's own players when it has said how (opt.stopAll). */
  var cur = null;
  function voiceBtn(opt, file, label) {
    var b = document.createElement('button');
    b.type = 'button'; b.className = 'nk-voice'; b.hidden = true; b.setAttribute('aria-pressed', 'false');
    b.innerHTML = '<i>▶</i> ' + esc(label);
    var a = new Audio(); a.preload = 'metadata';
    function icon(on) { b.setAttribute('aria-pressed', on ? 'true' : 'false'); b.querySelector('i').textContent = on ? '❚❚' : '▶'; }
    a.addEventListener('loadedmetadata', function () { b.hidden = false; });
    a.addEventListener('ended', function () { icon(false); });
    a.addEventListener('pause', function () { icon(false); });
    a.addEventListener('play', function () { icon(true); });
    a.src = src(opt, 'audio/guide/narrator/' + file + '.mp3');
    b.onclick = function () {
      if (!a.paused) { a.pause(); return; }
      if (cur && cur !== a) cur.pause();
      try { if (typeof opt.stopAll === 'function') opt.stopAll(a); } catch (e) {}
      cur = a; var p = a.play(); if (p && p.catch) p.catch(function () {});
    };
    return b;
  }
  function zoomable(img) {
    img.setAttribute('tabindex', '0'); img.setAttribute('role', 'button'); img.title = 'Click to see it bigger';
    function open() {
      var z = document.createElement('div'); z.className = 'nk-zoom'; z.setAttribute('role', 'dialog'); z.setAttribute('aria-label', img.alt || 'Bigger picture');
      z.innerHTML = '<img src="' + esc(img.src) + '" alt="' + esc(img.alt) + '">';
      function close() { z.remove(); document.removeEventListener('keydown', key); }
      function key(e) { if (e.key === 'Escape') close(); }
      z.onclick = close; document.addEventListener('keydown', key);
      document.body.appendChild(z);
    }
    img.onclick = open;
    img.onkeydown = function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); open(); } };
  }
  /* build only once every image has loaded: a missing file costs the card, never the page */
  function whenLoaded(urls, ok) {
    var left = urls.length, bad = false;
    if (!left) { ok(); return; }
    urls.forEach(function (u) {
      var im = new Image();
      im.onload = function () { if (!bad && --left === 0) ok(); };
      im.onerror = function () { bad = true; };
      im.src = u;
    });
  }

  /* ── 1. Annemarie's Path ──────────────────────────────────────────
     Two views of one map. Real places are solid pins; places that are
     only in the story are dashed. A pin appears on the lesson whose
     chapter first takes the reader there, never before. */
  var CPH_PINS = [
    { id: 'oster', ch: 1, real: true, x: 381, y: 112, lx: -9, ly: 4, anchor: 'end', name: 'Østerbrogade',
      t: 'A real shopping street in Østerbro, in the northeast of Copenhagen. It is where Annemarie races Ellen in Chapter 1. In 1943 there really were German soldiers standing on its corners.' },
    { id: 'home', ch: 1, real: false, x: 402, y: 55, lx: 9, ly: 4, name: 'Annemarie’s building',
      t: 'The Johansens and the Rosens live in the same apartment building, on different floors. The building is made up, but it sits in a real neighborhood.' },
    { id: 'amal', ch: 2, real: true, x: 494, y: 304, lx: -9, ly: 4, anchor: 'end', name: 'Amalienborg Palace',
      t: 'Four palaces around one square, where the Danish royal family lived and still lives. King Christian X set out from here on his rides through the city.' },
    { id: 'holmen', ch: 2, real: true, x: 570, y: 311, lx: 0, ly: 16, anchor: 'middle', name: 'Holmen naval harbor',
      t: 'Denmark’s navy was based here. On 29 August 1943, Danish sailors sank their own ships in the harbor so Germany could not use them.' },
    { id: 'shop', ch: 3, real: false, x: 371, y: 30, lx: -9, ly: 4, anchor: 'end', name: 'Mrs. Hirsch’s shop',
      t: 'The little shop that sells buttons and thread. It is in the story, not on a real map. But real Jewish families in Copenhagen did run shops just like it.' },
    { id: 'syn', ch: 4, real: true, x: 339, y: 344, lx: -9, ly: 4, anchor: 'end', name: 'The Great Synagogue',
      t: 'The synagogue on Krystalgade, built in 1833. On 29 September 1943, the morning before the Jewish New Year, the rabbi here warned everyone to hide. That warning really happened.' },
    { id: 'tivoli', ch: 4, real: true, x: 301, y: 451, lx: 9, ly: 4, name: 'Tivoli Gardens',
      t: 'An amusement park that opened in 1843, with music, lights, a carousel and fireworks. Danish Nazi helpers set fire to part of it in June 1944, a little later than in the story.' }
  ];
  var REGION_PINS = [
    { id: 'cph', ch: 1, real: true, k: 'copenhagen', lx: 9, ly: 4, name: 'Copenhagen',
      t: 'Denmark’s capital, and Annemarie’s home. In 1943 about 7,000 Jewish people lived in Denmark, most of them here.' },
    { id: 'swe', ch: 2, real: true, x: 540, y: 190, label: true, name: 'Sweden',
      t: 'Sweden stayed out of the war, so German soldiers did not rule there. Annemarie has seen it from Denmark’s coast, across a narrow strip of sea.' },
    { id: 'klamp', ch: 6, real: true, x: 350, y: 240, lx: 9, ly: 4, name: 'Klampenborg and the Deer Park',
      t: 'A real station on the coast line north of Copenhagen, beside a huge old park full of deer. The train passes it in Chapter 6, and Annemarie wishes they could stop.' },
    { id: 'gill', ch: 6, real: true, k: 'gilleleje', lx: -9, ly: -4, anchor: 'end', name: 'Gilleleje',
      t: 'A fishing town on the north coast of Zealand. From the shore here you can see Sweden on a clear day.' }
  ];
  var REGION_LINES = [ { ch: 6, from: 'copenhagen', to: 'gilleleje' } ];

  /* Copenhagen in 1943. Shorelines, lakes, canals, moats and parks are traced from
     OpenStreetMap (ODbL, credited on the map) and projected to scale, so every pin sits
     where the real place is. Built by tools/maps/cph-1943/gen.py; edit there, not here. */
  var CPH_SVG = '<svg viewBox="0 0 640 519" role="img" aria-label="A map of Copenhagen in 1943: the old town, the harbor, Christianshavn, the lakes and Østerbro, with pins on places from the story"><defs><radialGradient id="nkPar" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#FBF4E2"/><stop offset=".8" stop-color="#F1E4C4"/><stop offset="1" stop-color="#E2CFA2"/></radialGradient><pattern id="nkHatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(-30)"><path d="M0 3 H6" stroke="#A9C4CC" stroke-width=".7"/></pattern><style>.nkq{font:600 11px Lora,Georgia,serif;letter-spacing:2.5px;fill:#8C7444;opacity:.9}.nkw{font:italic 600 10.5px Lora,Georgia,serif;fill:#4F7A88}.nkg{font:italic 9px Lora,Georgia,serif;fill:#5E6E3E}.nks{font:italic 600 9.5px Lora,Georgia,serif;fill:#7A6237;paint-order:stroke;stroke:#F6EEDB;stroke-width:3px}.nkc{font:8px Nunito,sans-serif;fill:#8C7444}</style></defs><rect width="640" height="519" fill="url(#nkPar)"/><path d="M266.5 361.3L265.8 359.3L282.8 319.9L284.8 319.3L304.5 333L304.9 335L303.8 336.6L280.2 369L278.4 369.3Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M319.5 265.8L347.1 233.1L362.8 244.6L370.3 253.5L371.7 256.9L339.7 294.1L315.1 283.5L316.9 279.6L315.9 277.7L321.2 271.3L320.5 270.6L321.2 269.7L320.2 269L321.4 267.4Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M402.1 426.7L408.8 436.9L399.8 442.9L401.3 445.2L400.6 445.6L398.8 442.9L398.9 441.4L393.1 432.6Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M519.7 244.8L511.5 245.7L512.1 248.2L492.2 252.4L491.2 251.4L506.4 238.3L514.7 241.4L517.2 239.4L520.4 231.3L525.9 231.3Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M352.5 230.6L365.9 221.9L368.6 226.1L374.5 222.3L371.7 218.2L428.3 181.4L438.9 191.1L405.7 226.9L391.6 239.1L393.4 241.2L380.2 252.9L376.8 252.8Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M380.9 258.7L416.6 275.9L417 277.3L396.9 319.1L394.5 319.9L362.5 304.9L371.7 291.5L363.1 284.5L364.8 282.1L361.3 280.3L363 279.2L362.7 274.8L361.9 274.1L377.5 259.3Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M511.5 296.8L516.3 299.1L502.9 327.5L498.2 325.3Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M528.6 225.9L515.7 224.7L513.8 222.1L508.8 223L505.4 224.3L504.7 227.7L493.3 235.2L492.2 234.2L489.8 221.6L491.9 218.7L487.3 211.1L483.6 211.4L472.9 202L483.5 192.7L487.1 192.9L491.6 185.5L489.4 182.4L492.1 169.1L493.4 168.9L504.3 176.4L504.9 180L512.9 182.2L515.1 179.6L528.8 178.3L529.7 179.7L525.7 194.4L522.1 196.2L522.2 207.7L525.9 209.9L530.1 224Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M319.2 123.1L320.2 124.1L318.4 125.8L318.2 131L315.6 133.2L313 129.8L312 130.5L269.8 85.6L251 102.5L251.9 86.7L252.3 84.7L253.3 83.7L252 81.6L256.4 16.3L259.4 0L264.8 0L267.6 2.6L268.9 1.4L267.4 0L336.1 0L347.9 11.3L347.2 12.5L339.5 12.7L336.3 10.5L335.1 11.6L334.2 15.5L335.8 19.1L310.8 47.3L318.4 54.7L315.1 58.4L345.9 88L348.8 88L351 90.2L350.8 98.6L348.8 98.8L337.1 109.6L334.8 107.2Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M295.6 473.3L283.2 453L289.3 449L288.2 447L285.5 448.3L282.1 447.4L277.8 436.7L276.1 435.4L280 433.1L280.9 434.4L284.1 432.4L287.6 435.4L293.2 435L299.9 430.4L301.4 427.9L326.2 449.7L320.2 457.3Z" fill="#D6DDB4" stroke="#A9B887" stroke-width=".6"/><path d="M407.1 500.7L412.9 493.1L410.7 489.9L428.6 493.4L430.4 504.6L432.9 507.1L435.3 506.9L437.2 505L441.4 496.4L458.4 500L461.2 504.2L461.7 509.7L464.9 511.5L467 509.8L467.9 499.9L484.9 494.2L488.4 494.9L498.1 485.2L501.9 489.6L501.9 491.2L500.2 492.1L501.9 497.1L498.7 509L486.9 506.1L484.5 501.7L481.3 500.3L475.1 502.2L473.8 504.4L472.5 511.8L464.8 518.4L456.4 512.5L453.9 504.4L452.1 503.3L445.2 502.8L440.3 511.1L432.1 514.8L430.6 514.4L424.1 506.4L422.6 498.6L415 495.5L412.6 496.4L407.6 502.7L401.6 504.4L399.4 503.1ZM502.7 481.3L501.3 480.1L502.8 477.7L507.2 476.6L510.6 477.7L515.3 475.1L520.4 476.9L526.2 474.6L529.5 469.4L530.3 465L532.1 463.4L550 459.8L551.5 460L555.8 466.1L563.3 467.8L565.3 462.1L564.6 454.2L579.5 443.6L586.1 446.8L594.4 445.6L595.3 438.2L591.8 431.7L592.3 429.6L603.3 415.1L612.5 416.6L617.5 414L616 407.2L610.7 401L618.7 382.1L625.6 382.1L630.2 379.4L630.7 376.9L629.3 372.2L621.3 367.1L625.2 346.9L632.6 344.9L635.3 343.1L637.5 339L634.6 333.9L625.6 331L625 315.5L627.9 313.5L627.8 315L626.9 315.2L627.7 325.3L628.4 325.3L629 328.3L633.4 329.7L635.5 328.6L640 335.5L640 345.1L638.3 348.1L630.2 351.7L626.9 364.8L632.8 368.7L636 379.2L635.6 380.6L627.4 386.6L620.7 387.4L618.5 392L618.6 393.6L615.6 398.7L616.7 402.2L620.6 407.6L621.3 416.6L610.8 421L607.3 419.8L603.5 420.9L601.7 422.7L596.1 431.8L598.6 439.4L597.5 447L587.2 450.4L580.6 447.7L574.2 451.9L568.4 456.7L568.2 462.9L564.4 472.2L554 469L548.5 462.9L536 467.1L534.2 468.8L533.4 473.6L525.4 482.6L508.7 484.2L505.6 487.4L501.5 482.7Z" fill="#D9DDB8" stroke="#A9B887" stroke-width=".6"/><path d="M444.1 504L446.5 502.5L453.2 503.9L456.4 512.5L464.8 518.4L472.5 511.8L473.8 504.4L475.1 502.2L481.3 500.3L484.5 501.7L486.9 506.1L498.7 509L501.9 497.1L500.2 492.1L500.8 491.2L503.1 492.1L509.5 506.7L503.8 514.7L499.7 517.9L496 518.8L420.9 518.8L410.7 514L409.3 509.6L404.3 508L401.2 506L401.2 505L407.6 502.7L412.6 496.4L415 495.5L422.6 498.6L424.1 506.4L431.2 514.8L440.3 511.1ZM376.7 514.3L373.7 511.9L368.3 518.8L345.3 518.8L362.9 501.7L363.3 501.1L361.5 499.3L371 489.8L372.8 490.2L376.1 486.5L375.4 484.9L391.1 468.9L384.5 461.4L356.2 419.9L357 416.3L371.9 399.7L378.5 395L388.1 391.6L395.4 393.8L411.5 406.5L413 406.1L422.9 413.4L446.6 416.9L446.9 418.3L448.9 419.1L452 417.1L451 415.2L467.9 405.2L479.5 395.6L490.8 384.1L496.8 375.5L451.9 354.3L451.7 353.4L453.5 352.3L452.7 351.3L499.2 372.9L503.7 363.9L507.3 365L511.1 356.5L508.3 354.3L523 322.5L517.6 319.9L506.1 344.5L498.8 341.1L535 263.3L541.7 246.7L541.1 238.3L537.8 233.8L540.4 229.3L544.4 229.8L544.9 234.8L545.9 234.8L549.2 206.4L543.6 206L540.6 203.9L538.8 201L537.6 194.8L538.8 185.3L541 180.6L548.9 173.1L551 165.9L548.6 165.5L543.1 172.9L532.4 169.6L532.6 162.6L544.5 153.9L546.3 154.4L549.1 163L551 163.3L551.4 161.5L550.6 153.6L547.4 147.6L537.4 143.2L537.1 144.3L527.7 143.1L531.6 115.7L530.5 115.5L533.7 101.6L527.6 100.4L528 97.3L527.1 96.3L526 97L525.7 100.2L524.5 100L518.6 141.7L507 140L520.8 68.2L516.5 65L528.6 48.8L528.9 47.1L526.8 46.6L508.8 63.5L505.2 59.8L506.9 54.5L506.2 47.6L504.9 44.1L528.9 34.7L549.1 10L548.3 9L545 9.5L527.3 28.6L523 29.3L524.2 27.4L526.3 27L542 9.1L519.6 12.7L520.8 27.9L522.2 27.7L520.9 29.7L519.2 30L517.9 13.1L507.9 14.9L509.3 31.1L507.4 31.4L506.1 15.2L495 17.7L494.8 16.5L488.4 17.6L484.2 0.1L640 0L640 29.9L637.7 30.6L636.9 32L640 37.3L640 115.7L634.8 116.2L633.8 117.5L618.4 121.6L619.7 121.9L624.1 127L636.3 130.3L636.6 132.1L640 133.2L640 146.2L627.8 142.2L628.2 140.7L611.4 120.6L610.1 120.5L606.7 145.6L624.7 151.4L620.7 164L605.3 159L601.6 185.5L633.7 196.2L634.2 197.6L632.6 198.5L601.4 188.3L598.9 206.8L627.3 216.3L624.9 223.3L598.6 214.7L596.3 221.1L626.3 230.8L627.4 227.3L630.9 230.1L630.9 231.2L629.1 231.5L630.9 232.6L628.1 232.6L626.4 235.2L626 249.7L623.1 249.5L622.2 254.9L619.2 254.3L618.5 256.5L612.2 257.6L611.5 260.1L620.6 294.8L622.1 303.8L618.8 303.8L607.4 254.6L609.4 254.2L610.7 250.4L607.4 231.9L603.4 229.3L590.3 233.7L590.4 235.8L591.7 235.8L591.8 237.1L576.9 238.4L576.6 241L591.7 241.3L591.5 254.7L587.2 257.2L586.6 271.6L591.5 271.6L591.3 283.6L589.8 284L586.7 290.5L587.8 291.1L581.9 304L598.1 308.1L597.7 309.9L598.9 310.7L599.7 310.7L601.7 306.2L615.2 305.5L622.4 307.2L623.3 318.1L622.1 343.5L622.9 344.6L621.3 357.7L617.4 374.7L609.3 393.9L605.5 401.7L602.4 406.6L580.1 432.4L574.4 435.4L571.6 435.8L567.4 435.8L564 434.4L560.6 431.4L556.3 408.4L558.1 408L562.7 430.6L576.1 431.4L596.2 407.6L602.6 391.8L551.4 368.6L542.4 387L540.3 385L539.2 383.1L547.3 366.7L529.3 358.9L528.7 360L527.5 359.5L519 375.5L526.7 379.9L529.2 379.9L528.3 381.6L537.8 386.3L553.8 396.7L555.2 399.2L554.5 406.1L553.6 406.4L552.9 402.5L538.6 394L516.6 420.3L449.1 493.2L434.6 479.3L432.5 479L428.2 475.5L418 465.7L385.8 501.3ZM609 393.8L609 393.8L609.3 393.9ZM499.3 434.6L481.4 410.9L464.1 422.4L472.2 430.8L469.1 434.3L466.8 432.2L467.5 431.4L461 425.4L448.2 437.5L447.8 439.7L437.6 448.4L439.3 450.1L436.9 449L435.3 450.5L433.7 450.1L429 454.1L430.9 456L430.2 456.6L428.2 454.6L420.8 462.5L449.6 488.5L497.7 437.5ZM520.1 382L512.9 387.8L519.7 395.6L519.2 396.1L515.5 398.6L509.2 391.3L509.5 389.9L483.7 409.8L501 431.7L534.2 391.2L534 389.8ZM390.7 394.5L388.4 394L383 396L373.4 402.1L358.9 418.4L386.7 459.2L393.5 466.7L395.9 466.1L406.6 456.9L407.7 457.1L418.4 450.1L417.8 449L429.7 440.1L433.6 438.7L445.6 428.5L448.1 425.6L447.7 424.8L419.1 415.2ZM446.7 435.4L447.4 436.5L450.8 432.9L449.8 432.6ZM442.9 431.5L443.9 432.2L447.1 428.9L446 428.6ZM558.6 344.6L541.7 336.5L534.4 352.1L550.9 360.3ZM591.8 382.4L597.5 384.9L592.1 381.7L592.9 379.9L598.8 382.7L600.3 379.7L597.3 378.3L597.8 377.4L600.7 378.7L602.3 375.2L600.4 374.1L603.9 368.2L610 338.7L608.4 319.5L598 314.5L598.5 312.2L597.1 311.5L595.9 312.8L591.8 320.6L586.9 318.2L590.1 311.6L589.9 310.5L579.1 308.1L552 366L591.1 383.8ZM565.1 331.4L545.4 322.1L540.1 333.6L559.5 342.7ZM574.5 312.1L557 303.6L553.8 309.9L565.1 315.9L565.4 317.7L563.9 318.2L552.2 313L548.3 321.1L566.1 329.6ZM550.4 144.4L556.2 30.7L557 28.6L555.9 28.2L552.7 30.7L543.8 44.4L540.8 101.8L537.3 141.7L547.4 146.4ZM222.4 432L219.4 430.7L217.5 431.1L216 433.1L216 435.3L214.2 436L212.8 438.7L200.2 442.7L199.2 439.8L206.8 389.9L228.2 393.5ZM231 345.6L234.7 349.4L229.5 386.2L207.6 382.8L214.2 338.7L217.1 338.1L223.2 340.6ZM269.2 272.6L268 276.3L269.4 280L238.7 338L232.4 333.9L232.5 332.1L230.1 330.3L227.7 328.7L226 329.4L219.2 324.9L251.5 265.8L256.3 263.7ZM318.7 212L315.5 218.1L302 233.5L276.6 267.3L273 268L271.1 269.9L258 260.7L258.9 258.2L258.3 255.4L284.7 220.1L300.5 201.7L306.4 197.7L314.7 205.7ZM525.9 231.3L520.4 231.3L517.2 239.4L514.7 241.4L506.4 238.3L491.4 250.4L490.1 248.4L493.6 244.9L494.1 242.3L507 233.1L514.1 237.6L516.8 229.5L510.6 228.6L495.4 239.4L491.3 239.8L489.4 237.8L484.8 217.1L471.3 206.2L469.5 203.2L469.5 201.3L471.3 198.1L484.8 187.3L488.3 167L492.8 164.5L509.4 175.3L520.5 175.3L528.5 173.5L533.8 174.9L535.5 177.1L535.9 180.7L534 195.9L530.8 197.6L528.9 202.4L530.1 205.7L532.9 208L534 210.4L534.1 217.8L531.6 226.2L532.2 229.7L530.2 230.1L529.5 228.4L527.6 228ZM528.8 178.3L515.1 179.6L512.9 182.2L504.9 180L504.3 176.4L493.4 168.9L492.1 169.1L489.4 182.4L491.6 185.5L487.1 192.9L483.5 192.7L472.9 202L483.6 211.4L487.3 211.1L491.9 218.7L489.8 221.6L492.2 234.2L493.3 235.2L504.7 227.7L505.4 224.3L508.8 223L513.8 222.1L515.7 224.7L528.6 225.9L530.1 224L525.9 209.9L522.2 207.7L522.1 196.2L525.7 194.4L529.7 179.7ZM475.9 223L484.2 224.7L487.5 238.9L485.9 241.3L482.8 237.1L481.7 227.7L475.7 226.4L472.9 222.2L472.7 220L474 216.4L462.9 208.4L458 201.3L458.5 199.4L461.7 196.5L473.4 188.4L472 185.1L485.3 170.3L484.2 181L475.6 182.5L478.4 187.5L478 189.3L467.7 197.7L465.6 197.6L459.6 202.4L466.3 207.1L468.6 207L478.2 214.7L478.3 216.5ZM358.2 160.9L349.3 180.3L330.5 201L326.9 203.7L319.1 200.1L310.8 193L314 186.4L330.6 168L338.7 150.9L342.5 145.8L378.4 115.9L386.5 136.8ZM548.1 501.4L550.6 495.9L571.5 479.8L579.6 480L581.5 473L602.9 457.4L614.9 442.5L618.4 442.7L622 440.5L621.5 434.2L630.4 421.9L635.2 410L640 408.6L640 411.9L636.6 412.6L631.4 424.9L623.8 434.7L624.6 439.8L621.6 445.1L615.3 446.1L603.4 459.5L582 474.6L581.4 479.5L579.2 481.6L573.2 481.3L554.5 494.5L551.9 497.4L550.6 502L548.5 504.2L540.8 502.7L521.2 509.7L519.5 507.8L540 500.3ZM533.4 473.6L534.2 468.8L536 467.1L548.5 462.9L554 469L564.4 472.2L568.2 462.9L568.4 456.7L574.2 451.9L580.6 447.7L587.2 450.4L597.5 447L598.6 439.4L596.1 431.8L603.5 420.9L607.3 419.8L610.8 421L621.3 416.7L620.6 407.6L616.7 402.2L615.6 398.7L618.6 393.6L618.5 392L620.7 387.4L627.4 386.6L635.6 380.6L636 379.2L632.8 368.7L626.9 364.8L630.2 351.7L638.3 348.1L640 345.1L640 386.9L624.2 423L600.3 453.8L566 478.9L557.1 481.9L552.5 487.2L552.3 489L536 498.4L515.4 504.2L514.7 501.8L517.8 500.2L516.8 494.6L514.5 489.8L509.6 491.7L506 486.3L508.7 484.2L525.4 482.6ZM539.3 476.8L539.1 478.3L540.2 480.5L546 485.4L549.7 478.6L549.9 475.7L544.8 474.3ZM638.2 333.7L636.5 329.8L632 326.4L630.6 313.1L636.6 309L640 302.9L640 336.1ZM624.5 289.7L621.2 279.9L618.2 280.4L617.7 278.5L620.5 277.5L622.1 273.9L626.1 269.8L628.1 263.2L632.7 262.2L635.9 264.8L640 274.4L640 297.2L638.9 297.9L631.8 291.9Z" fill="#C9DCE0" fill-rule="evenodd" stroke="#8FAEB8" stroke-width=".8" stroke-linejoin="round"/><path d="M444.1 504L446.5 502.5L453.2 503.9L456.4 512.5L464.8 518.4L472.5 511.8L473.8 504.4L475.1 502.2L481.3 500.3L484.5 501.7L486.9 506.1L498.7 509L501.9 497.1L500.2 492.1L500.8 491.2L503.1 492.1L509.5 506.7L503.8 514.7L499.7 517.9L496 518.8L420.9 518.8L410.7 514L409.3 509.6L404.3 508L401.2 506L401.2 505L407.6 502.7L412.6 496.4L415 495.5L422.6 498.6L424.1 506.4L431.2 514.8L440.3 511.1ZM376.7 514.3L373.7 511.9L368.3 518.8L345.3 518.8L362.9 501.7L363.3 501.1L361.5 499.3L371 489.8L372.8 490.2L376.1 486.5L375.4 484.9L391.1 468.9L384.5 461.4L356.2 419.9L357 416.3L371.9 399.7L378.5 395L388.1 391.6L395.4 393.8L411.5 406.5L413 406.1L422.9 413.4L446.6 416.9L446.9 418.3L448.9 419.1L452 417.1L451 415.2L467.9 405.2L479.5 395.6L490.8 384.1L496.8 375.5L451.9 354.3L451.7 353.4L453.5 352.3L452.7 351.3L499.2 372.9L503.7 363.9L507.3 365L511.1 356.5L508.3 354.3L523 322.5L517.6 319.9L506.1 344.5L498.8 341.1L535 263.3L541.7 246.7L541.1 238.3L537.8 233.8L540.4 229.3L544.4 229.8L544.9 234.8L545.9 234.8L549.2 206.4L543.6 206L540.6 203.9L538.8 201L537.6 194.8L538.8 185.3L541 180.6L548.9 173.1L551 165.9L548.6 165.5L543.1 172.9L532.4 169.6L532.6 162.6L544.5 153.9L546.3 154.4L549.1 163L551 163.3L551.4 161.5L550.6 153.6L547.4 147.6L537.4 143.2L537.1 144.3L527.7 143.1L531.6 115.7L530.5 115.5L533.7 101.6L527.6 100.4L528 97.3L527.1 96.3L526 97L525.7 100.2L524.5 100L518.6 141.7L507 140L520.8 68.2L516.5 65L528.6 48.8L528.9 47.1L526.8 46.6L508.8 63.5L505.2 59.8L506.9 54.5L506.2 47.6L504.9 44.1L528.9 34.7L549.1 10L548.3 9L545 9.5L527.3 28.6L523 29.3L524.2 27.4L526.3 27L542 9.1L519.6 12.7L520.8 27.9L522.2 27.7L520.9 29.7L519.2 30L517.9 13.1L507.9 14.9L509.3 31.1L507.4 31.4L506.1 15.2L495 17.7L494.8 16.5L488.4 17.6L484.2 0.1L640 0L640 29.9L637.7 30.6L636.9 32L640 37.3L640 115.7L634.8 116.2L633.8 117.5L618.4 121.6L619.7 121.9L624.1 127L636.3 130.3L636.6 132.1L640 133.2L640 146.2L627.8 142.2L628.2 140.7L611.4 120.6L610.1 120.5L606.7 145.6L624.7 151.4L620.7 164L605.3 159L601.6 185.5L633.7 196.2L634.2 197.6L632.6 198.5L601.4 188.3L598.9 206.8L627.3 216.3L624.9 223.3L598.6 214.7L596.3 221.1L626.3 230.8L627.4 227.3L630.9 230.1L630.9 231.2L629.1 231.5L630.9 232.6L628.1 232.6L626.4 235.2L626 249.7L623.1 249.5L622.2 254.9L619.2 254.3L618.5 256.5L612.2 257.6L611.5 260.1L620.6 294.8L622.1 303.8L618.8 303.8L607.4 254.6L609.4 254.2L610.7 250.4L607.4 231.9L603.4 229.3L590.3 233.7L590.4 235.8L591.7 235.8L591.8 237.1L576.9 238.4L576.6 241L591.7 241.3L591.5 254.7L587.2 257.2L586.6 271.6L591.5 271.6L591.3 283.6L589.8 284L586.7 290.5L587.8 291.1L581.9 304L598.1 308.1L597.7 309.9L598.9 310.7L599.7 310.7L601.7 306.2L615.2 305.5L622.4 307.2L623.3 318.1L622.1 343.5L622.9 344.6L621.3 357.7L617.4 374.7L609.3 393.9L605.5 401.7L602.4 406.6L580.1 432.4L574.4 435.4L571.6 435.8L567.4 435.8L564 434.4L560.6 431.4L556.3 408.4L558.1 408L562.7 430.6L576.1 431.4L596.2 407.6L602.6 391.8L551.4 368.6L542.4 387L540.3 385L539.2 383.1L547.3 366.7L529.3 358.9L528.7 360L527.5 359.5L519 375.5L526.7 379.9L529.2 379.9L528.3 381.6L537.8 386.3L553.8 396.7L555.2 399.2L554.5 406.1L553.6 406.4L552.9 402.5L538.6 394L516.6 420.3L449.1 493.2L434.6 479.3L432.5 479L428.2 475.5L418 465.7L385.8 501.3ZM609 393.8L609 393.8L609.3 393.9ZM499.3 434.6L481.4 410.9L464.1 422.4L472.2 430.8L469.1 434.3L466.8 432.2L467.5 431.4L461 425.4L448.2 437.5L447.8 439.7L437.6 448.4L439.3 450.1L436.9 449L435.3 450.5L433.7 450.1L429 454.1L430.9 456L430.2 456.6L428.2 454.6L420.8 462.5L449.6 488.5L497.7 437.5ZM520.1 382L512.9 387.8L519.7 395.6L519.2 396.1L515.5 398.6L509.2 391.3L509.5 389.9L483.7 409.8L501 431.7L534.2 391.2L534 389.8ZM390.7 394.5L388.4 394L383 396L373.4 402.1L358.9 418.4L386.7 459.2L393.5 466.7L395.9 466.1L406.6 456.9L407.7 457.1L418.4 450.1L417.8 449L429.7 440.1L433.6 438.7L445.6 428.5L448.1 425.6L447.7 424.8L419.1 415.2ZM446.7 435.4L447.4 436.5L450.8 432.9L449.8 432.6ZM442.9 431.5L443.9 432.2L447.1 428.9L446 428.6ZM558.6 344.6L541.7 336.5L534.4 352.1L550.9 360.3ZM591.8 382.4L597.5 384.9L592.1 381.7L592.9 379.9L598.8 382.7L600.3 379.7L597.3 378.3L597.8 377.4L600.7 378.7L602.3 375.2L600.4 374.1L603.9 368.2L610 338.7L608.4 319.5L598 314.5L598.5 312.2L597.1 311.5L595.9 312.8L591.8 320.6L586.9 318.2L590.1 311.6L589.9 310.5L579.1 308.1L552 366L591.1 383.8ZM565.1 331.4L545.4 322.1L540.1 333.6L559.5 342.7ZM574.5 312.1L557 303.6L553.8 309.9L565.1 315.9L565.4 317.7L563.9 318.2L552.2 313L548.3 321.1L566.1 329.6ZM550.4 144.4L556.2 30.7L557 28.6L555.9 28.2L552.7 30.7L543.8 44.4L540.8 101.8L537.3 141.7L547.4 146.4ZM222.4 432L219.4 430.7L217.5 431.1L216 433.1L216 435.3L214.2 436L212.8 438.7L200.2 442.7L199.2 439.8L206.8 389.9L228.2 393.5ZM231 345.6L234.7 349.4L229.5 386.2L207.6 382.8L214.2 338.7L217.1 338.1L223.2 340.6ZM269.2 272.6L268 276.3L269.4 280L238.7 338L232.4 333.9L232.5 332.1L230.1 330.3L227.7 328.7L226 329.4L219.2 324.9L251.5 265.8L256.3 263.7ZM318.7 212L315.5 218.1L302 233.5L276.6 267.3L273 268L271.1 269.9L258 260.7L258.9 258.2L258.3 255.4L284.7 220.1L300.5 201.7L306.4 197.7L314.7 205.7ZM525.9 231.3L520.4 231.3L517.2 239.4L514.7 241.4L506.4 238.3L491.4 250.4L490.1 248.4L493.6 244.9L494.1 242.3L507 233.1L514.1 237.6L516.8 229.5L510.6 228.6L495.4 239.4L491.3 239.8L489.4 237.8L484.8 217.1L471.3 206.2L469.5 203.2L469.5 201.3L471.3 198.1L484.8 187.3L488.3 167L492.8 164.5L509.4 175.3L520.5 175.3L528.5 173.5L533.8 174.9L535.5 177.1L535.9 180.7L534 195.9L530.8 197.6L528.9 202.4L530.1 205.7L532.9 208L534 210.4L534.1 217.8L531.6 226.2L532.2 229.7L530.2 230.1L529.5 228.4L527.6 228ZM528.8 178.3L515.1 179.6L512.9 182.2L504.9 180L504.3 176.4L493.4 168.9L492.1 169.1L489.4 182.4L491.6 185.5L487.1 192.9L483.5 192.7L472.9 202L483.6 211.4L487.3 211.1L491.9 218.7L489.8 221.6L492.2 234.2L493.3 235.2L504.7 227.7L505.4 224.3L508.8 223L513.8 222.1L515.7 224.7L528.6 225.9L530.1 224L525.9 209.9L522.2 207.7L522.1 196.2L525.7 194.4L529.7 179.7ZM475.9 223L484.2 224.7L487.5 238.9L485.9 241.3L482.8 237.1L481.7 227.7L475.7 226.4L472.9 222.2L472.7 220L474 216.4L462.9 208.4L458 201.3L458.5 199.4L461.7 196.5L473.4 188.4L472 185.1L485.3 170.3L484.2 181L475.6 182.5L478.4 187.5L478 189.3L467.7 197.7L465.6 197.6L459.6 202.4L466.3 207.1L468.6 207L478.2 214.7L478.3 216.5ZM358.2 160.9L349.3 180.3L330.5 201L326.9 203.7L319.1 200.1L310.8 193L314 186.4L330.6 168L338.7 150.9L342.5 145.8L378.4 115.9L386.5 136.8ZM548.1 501.4L550.6 495.9L571.5 479.8L579.6 480L581.5 473L602.9 457.4L614.9 442.5L618.4 442.7L622 440.5L621.5 434.2L630.4 421.9L635.2 410L640 408.6L640 411.9L636.6 412.6L631.4 424.9L623.8 434.7L624.6 439.8L621.6 445.1L615.3 446.1L603.4 459.5L582 474.6L581.4 479.5L579.2 481.6L573.2 481.3L554.5 494.5L551.9 497.4L550.6 502L548.5 504.2L540.8 502.7L521.2 509.7L519.5 507.8L540 500.3ZM533.4 473.6L534.2 468.8L536 467.1L548.5 462.9L554 469L564.4 472.2L568.2 462.9L568.4 456.7L574.2 451.9L580.6 447.7L587.2 450.4L597.5 447L598.6 439.4L596.1 431.8L603.5 420.9L607.3 419.8L610.8 421L621.3 416.7L620.6 407.6L616.7 402.2L615.6 398.7L618.6 393.6L618.5 392L620.7 387.4L627.4 386.6L635.6 380.6L636 379.2L632.8 368.7L626.9 364.8L630.2 351.7L638.3 348.1L640 345.1L640 386.9L624.2 423L600.3 453.8L566 478.9L557.1 481.9L552.5 487.2L552.3 489L536 498.4L515.4 504.2L514.7 501.8L517.8 500.2L516.8 494.6L514.5 489.8L509.6 491.7L506 486.3L508.7 484.2L525.4 482.6ZM539.3 476.8L539.1 478.3L540.2 480.5L546 485.4L549.7 478.6L549.9 475.7L544.8 474.3ZM638.2 333.7L636.5 329.8L632 326.4L630.6 313.1L636.6 309L640 302.9L640 336.1ZM624.5 289.7L621.2 279.9L618.2 280.4L617.7 278.5L620.5 277.5L622.1 273.9L626.1 269.8L628.1 263.2L632.7 262.2L635.9 264.8L640 274.4L640 297.2L638.9 297.9L631.8 291.9Z" fill="url(#nkHatch)" fill-rule="evenodd" opacity=".55"/><g fill="none" stroke-linecap="round" stroke-linejoin="round"><g stroke="#B49A68" stroke-width="2" opacity=".75"><path d="M389 135 L378 103 L373 88 L370 70 L371 30 L371 -42"/><path d="M258 263 L248 256 L202 225 L187 209 L150 165 L80 83 L57 67"/><path d="M292 418 L269 436 L240 452 L200 466 L169 461 L154 462 L78 496 L-8 512"/><path d="M377 472 L297 402 L283 380 L280 372 L309 330 L340 296 L365 268 L383 253 L406 232 L439 217 L455 210"/><path d="M441 427 L453 439 L503 487 L516 516 L523 529"/><path d="M368 484 L391 505 L406 523"/></g><g stroke="#C2AB7E" stroke-width="1.1" opacity=".8"><path d="M474 125 L471 88 L457 54 L453 35 L444 17 L437 -10"/><path d="M391 134 L481 96"/><path d="M243 209 L286 168 L326 130 L355 103 L373 88"/><path d="M281 269 L432 340"/><path d="M448 348 L490 255"/><path d="M432 340 L470 258"/><path d="M470 258 L538 244"/><path d="M306 410 L334 387 L343 382 L360 379 L388 374 L409 366 L429 355"/><path d="M322 353 L352 341"/><path d="M410 405 L434 393 L440 393"/><path d="M389 135 L395 146 L426 174"/><path d="M275 274 L253 259"/></g></g><path d="M528.6 225.9L515.7 224.7L513.8 222.1L508.8 223L505.4 224.3L504.7 227.7L493.3 235.2L492.2 234.2L489.8 221.6L491.9 218.7L487.3 211.1L483.6 211.4L472.9 202L483.5 192.7L487.1 192.9L491.6 185.5L489.4 182.4L492.1 169.1L493.4 168.9L504.3 176.4L504.9 180L512.9 182.2L515.1 179.6L528.8 178.3L529.7 179.7L525.7 194.4L522.1 196.2L522.2 207.7L525.9 209.9L530.1 224Z" fill="#E6DCB8" stroke="#8C7444" stroke-width="1"/><text class="nkq" x="431" y="101" text-anchor="middle" transform="rotate(-12 431 101)">ØSTERBRO</text><text class="nkq" x="133" y="201" text-anchor="middle" transform="rotate(-33 133 201)">NØRREBRO</text><text class="nkq" x="101" y="452" text-anchor="middle" transform="rotate(6 101 452)">VESTERBRO</text><text class="nkq" x="395" y="354" text-anchor="middle" transform="rotate(-10 395 354)">INDRE BY</text><text class="nkg" x="396" y="363" text-anchor="middle" transform="rotate(-10 396 363)">the old town</text><text class="nkq" x="523" y="452" text-anchor="middle" transform="rotate(-24 523 452)">CHRISTIANSHAVN</text><text class="nkq" x="596" y="373" text-anchor="middle">HOLMEN</text><text class="nkg" x="596" y="382" text-anchor="middle">the navy base</text><text class="nkq" x="70" y="353" text-anchor="middle" transform="rotate(-60 70 353)">FREDERIKSBERG</text><text class="nkw" x="285" y="241" text-anchor="middle" transform="rotate(35 285 241)">Søerne · the Lakes</text><text class="nkw" x="478" y="423" text-anchor="middle" transform="rotate(-31 478 423)">Inderhavnen · the harbor</text><text class="nkw" x="572" y="113" text-anchor="middle" transform="rotate(-72 572 113)">to the Øresund</text><text class="nkg" x="304" y="59" text-anchor="middle">Fælledparken</text><text class="nkg" x="389" y="285" text-anchor="middle" transform="rotate(-14 389 285)">Kongens Have</text><text class="nks" x="503" y="152" text-anchor="middle">Kastellet</text><text class="nkg" x="503" y="160" text-anchor="middle">the star fort</text><text class="nkg" x="513" y="25" text-anchor="middle" transform="rotate(-78 513 25)">Frihavnen</text><text class="nkg" x="542" y="196" text-anchor="middle" transform="rotate(-78 542 196)">Langelinie</text><text class="nkg" x="385" y="403" text-anchor="middle" transform="rotate(-16 385 403)">Christiansborg</text><text class="nkg" x="619" y="173" text-anchor="middle" transform="rotate(-78 619 173)">Refshaleøen</text><g transform="translate(16 16)"><rect width="170" height="46" rx="4" fill="#FFF9EA" stroke="#B49A68"/><rect x="3" y="3" width="164" height="40" rx="3" fill="none" stroke="#D8C69E"/><text x="85" y="22" text-anchor="middle" font-family="Lora,Georgia,serif" font-size="15" font-weight="600" fill="#3B2E17">København</text><text x="85" y="36" text-anchor="middle" font-family="Nunito,sans-serif" font-size="9" font-weight="800" letter-spacing="2" fill="#8C7444">COPENHAGEN · 1943</text></g><g transform="translate(16 497)" font-family="Nunito,sans-serif" font-size="8.5" font-weight="700" fill="#6B5126"><rect x="-6" y="-24" width="158" height="38" rx="4" fill="#FFF9EA" opacity=".85"/><path d="M0 0 H124.4" stroke="#6B5126" stroke-width="2"/><path d="M0 -4 V4 M124.4 -4 V4 M62.2 -3 V3" stroke="#6B5126" stroke-width="1.2"/><path d="M0 -8 H100.1" stroke="#A88F5E" stroke-width="1"/><path d="M100.1 -11 V-5" stroke="#A88F5E"/><text x="128.4" y="10" >1 kilometer</text><text x="104.1" y="-12">½ mile</text></g><g transform="translate(604 475)" fill="#8C7444"><circle r="18" fill="#FFF9EA" fill-opacity=".8" stroke="#B49A68"/><path d="M0 -22 L4.5 0 L0 22 L-4.5 0 Z" opacity=".85"/><path d="M-22 0 L0 3.5 L22 0 L0 -3.5 Z" opacity=".45"/><text y="-25" text-anchor="middle" font-family="Nunito,sans-serif" font-size="9" font-weight="800">N</text></g><text class="nkc" x="634" y="515" text-anchor="end">Shorelines: © OpenStreetMap contributors, shown as they were in 1943</text><g class="pins"></g></svg>';
  function cphSVG() { return CPH_SVG; }
  function regionSVG() {
    var R = ORESUND;
    return '<svg viewBox="0 0 645 405" role="img" aria-label="A map of northern Denmark and southern Sweden, with the sea between them">' +
      '<rect width="645" height="405" fill="#C9DCE0"/>' +
      '<path d="' + R.denmark + '" fill="#EFE3C3" stroke="#B49A68" stroke-width="1"/>' +
      '<path d="' + R.sweden + '" fill="#DCE6C8" stroke="#9CAE84" stroke-width="1"/>' +
      '<text x="120" y="300" font-family="Lora,Georgia,serif" font-size="14" letter-spacing="3" fill="#9A835A">DENMARK</text>' +
      '<text x="120" y="318" font-family="Lora,Georgia,serif" font-style="italic" font-size="11" fill="#9A835A">the island of Zealand</text>' +
      '<text x="402" y="232" font-family="Lora,Georgia,serif" font-style="italic" font-size="13" fill="#5E8592" transform="rotate(-72 402 232)">Øresund</text>' +
      '<g class="lines"></g><g class="pins"></g></svg>';
  }
  function pinG(p, x, y, today) {
    var a = p.anchor || 'start';
    return '<g class="pin' + (p.real ? '' : ' story') + (today ? ' today' : '') + '" data-id="' + p.id + '" tabindex="0" role="button" aria-label="' + esc(p.name) + '">' +
      '<circle class="hit" cx="' + x + '" cy="' + (y - 9) + '" r="16"/>' +
      '<circle class="ring" cx="' + x + '" cy="' + (y - 12) + '" r="12"/>' +
      '<path class="drop" d="M' + x + ' ' + y + ' C' + (x - 3) + ' ' + (y - 6) + ' ' + (x - 7) + ' ' + (y - 9) + ' ' + (x - 7) + ' ' + (y - 13) + ' A7 7 0 1 1 ' + (x + 7) + ' ' + (y - 13) + ' C' + (x + 7) + ' ' + (y - 9) + ' ' + (x + 3) + ' ' + (y - 6) + ' ' + x + ' ' + y + ' Z"/>' +
      '<circle class="dot" cx="' + x + '" cy="' + (y - 13) + '" r="2.6"/>' +
      '<text class="pl' + (p.real ? '' : ' story') + '" x="' + (x + (p.lx != null ? p.lx : 9)) + '" y="' + (y + (p.ly != null ? p.ly : 4)) + '" text-anchor="' + a + '">' + esc(p.name) + '</text></g>';
  }
  function pathCard(host, opt) {
    var ch = chOf(opt);
    var el = card('🧭', 'Annemarie’s Path', 'Real places and story places, one chapter at a time.', [
      '<i>Number the Stars</i> is a made-up story set in a real city at a real time: Copenhagen, Denmark, in 1943.',
      'Solid pins are <b>real places</b> you could visit today. Dashed pins are <b>story places</b>. Lois Lowry made them up, but she put them in real streets.',
      'A new pin appears when the chapter you are reading first goes there. Nothing ahead of you is shown.'
    ]);
    var b = el.querySelector('.nk-body');
    b.innerHTML = '<div class="nk-tabs" role="group" aria-label="Which map">' +
        '<button type="button" class="nk-tab" data-v="cph">Copenhagen</button>' +
        '<button type="button" class="nk-tab" data-v="reg">Denmark &amp; Sweden</button></div>' +
      '<div class="nk-map"></div><div class="nk-info" aria-live="polite"></div>' +
      '<div class="nk-legend"><span><i></i>Real place</span><span><i class="s"></i>Only in the story</span></div>';
    var mapEl = b.querySelector('.nk-map'), info = b.querySelector('.nk-info');
    function show(p) {
      info.innerHTML = '<span class="nk-tag ' + (p.real ? 'real">Real place' : 'story">In the story') + '</span>' +
        '<span class="nk-tag ch">Ch. ' + p.ch + '</span> <b>' + esc(p.name) + '.</b> ' + esc(p.t);
      mapEl.querySelectorAll('.pin').forEach(function (g) { g.classList.toggle('sel', g.getAttribute('data-id') === p.id); });
    }
    function wire(list) {
      mapEl.querySelectorAll('.pin').forEach(function (g) {
        var p = list.filter(function (q) { return q.id === g.getAttribute('data-id'); })[0];
        if (!p) return;
        g.addEventListener('click', function () { show(p); });
        g.addEventListener('keydown', function (e) { if (e.key === 'Enter' || e.key === ' ') { e.preventDefault(); show(p); } });
      });
    }
    function view(v) {
      b.querySelectorAll('.nk-tab').forEach(function (t) { t.setAttribute('aria-pressed', t.getAttribute('data-v') === v ? 'true' : 'false'); });
      var list, newest = null;
      if (v === 'cph') {
        mapEl.innerHTML = cphSVG();
        list = CPH_PINS.filter(function (p) { return p.ch <= ch; });
        mapEl.querySelector('.pins').innerHTML = list.map(function (p) { return pinG(p, p.x, p.y, p.ch === ch); }).join('');
      } else {
        mapEl.innerHTML = regionSVG();
        var P = ORESUND._pts;
        list = REGION_PINS.filter(function (p) { return p.ch <= ch; });
        mapEl.querySelector('.lines').innerHTML = REGION_LINES.filter(function (l) { return l.ch <= ch; }).map(function (l) {
          var a = P[l.from], c = P[l.to];
          return '<path d="M' + a[0] + ' ' + a[1] + ' Q' + ((a[0] + c[0]) / 2 - 40) + ' ' + ((a[1] + c[1]) / 2) + ' ' + c[0] + ' ' + c[1] + '" fill="none" stroke="#A8432F" stroke-width="2" stroke-dasharray="5 4"/>';
        }).join('');
        mapEl.querySelector('.pins').innerHTML = list.map(function (p) {
          if (p.label) return '<g class="pin" data-id="' + p.id + '" tabindex="0" role="button" aria-label="' + esc(p.name) + '"><rect class="hit" x="' + (p.x - 54) + '" y="' + (p.y - 22) + '" width="108" height="34"/>' +
            '<circle class="ring" cx="' + p.x + '" cy="' + (p.y - 5) + '" r="30"/><text x="' + p.x + '" y="' + p.y + '" text-anchor="middle" font-family="Lora,Georgia,serif" font-size="17" letter-spacing="3" fill="#5E7A4A">SWEDEN</text></g>';
          var xy = p.k ? P[p.k] : [p.x, p.y]; return pinG(p, xy[0], xy[1], p.ch === ch);
        }).join('');
      }
      list.forEach(function (p) { if (!newest || p.ch >= newest.ch) newest = p; });
      wire(list);
      if (newest) show(newest); else info.textContent = '';
    }
    b.querySelectorAll('.nk-tab').forEach(function (t) { t.onclick = function () { view(t.getAttribute('data-v')); }; });
    view(ch >= 6 ? 'reg' : 'cph');   /* the story leaves the city in Chapter 6 */
    host.appendChild(el);
  }

  /* ── 2. the Museum Case: one real object, its label, things to look for ── */
  function caseCard(host, opt) {
    var c = opt.cfg && opt.cfg['case']; if (!c || !c.src) return false;
    var url = src(opt, c.src);
    whenLoaded([url], function () {
      var el = card('🏛️', c.kicker || 'The Museum Case', c.sub || 'A real object from Denmark in the war years.', c.what || null);
      var b = el.querySelector('.nk-body'), n = ++uid;
      b.innerHTML =
        '<div class="nk-case"><div class="nk-vitrine"><div class="nk-glass"><img alt="' + esc(c.alt) + '" src="' + esc(url) + '"></div>' +
          '<div class="nk-plaque"><b>' + esc(c.title) + '</b><span>' + esc(c.date || '') + '</span></div></div>' +
        '<div class="nk-label">' + (c.label || []).map(function (p) { return '<p>' + p + '</p>'; }).join('') +
          ((c.look || []).length ? '<div class="nk-look"><div class="nk-look-h">Look closely</div>' + c.look.map(function (q, i) {
            return '<div class="nk-q"><button type="button" aria-expanded="false" aria-controls="nkq' + n + '-' + i + '">' + esc(q.q) + '</button><div class="a" id="nkq' + n + '-' + i + '" hidden>' + q.a + '</div></div>';
          }).join('') + '</div>' : '') +
          '<span class="nk-cred">' + esc(c.credit || '') + '</span></div></div>';
      zoomable(b.querySelector('.nk-glass img'));
      b.querySelectorAll('.nk-q button').forEach(function (q) {
        q.onclick = function () { var a = q.nextElementSibling; a.hidden = !a.hidden; q.setAttribute('aria-expanded', String(!a.hidden)); };
      });
      var lab = b.querySelector('.nk-label');
      lab.insertBefore(voiceBtn(opt, 'g4ela-' + opt.week + '-' + opt.day + '-case', c.voiceLabel || 'Grete remembers'), lab.querySelector('.nk-look') || lab.querySelector('.nk-cred'));
      host.appendChild(el);
    });
  }

  /* ── 3. Then & Now: drag the line between the war years and today ── */
  function thenNowCard(host, opt) {
    var c = opt.cfg && opt.cfg.thennow; if (!c || !c.then || !c.now) return false;
    var u1 = src(opt, c.then.src), u2 = src(opt, c.now.src);
    whenLoaded([u1, u2], function () {
      var el = card('⇆', c.kicker || 'Then & Now', c.sub || 'Drag the line to travel between the years.', null);
      var b = el.querySelector('.nk-body');
      b.innerHTML =
        '<div class="nk-tn" style="--x:50%"><img class="now" src="' + esc(u2) + '" alt="' + esc(c.now.alt) + '">' +
          '<img class="then" src="' + esc(u1) + '" alt="' + esc(c.then.alt) + '">' +
          '<span class="yr l">' + esc(c.then.label || 'Then') + '</span><span class="yr r">' + esc(c.now.label || 'Today') + '</span>' +
          '<span class="bar"></span><span class="knob" aria-hidden="true">⇆</span>' +
          '<input type="range" min="0" max="100" value="50" aria-label="Slide between ' + esc(c.then.label || 'then') + ' and ' + esc(c.now.label || 'today') + '"></div>' +
        (c.caption ? '<p class="nk-tn-cap">' + c.caption + '</p>' : '') +
        '<span class="nk-cred">' + esc(c.then.credit || '') + '<br>' + esc(c.now.credit || '') + '</span>';
      var tn = b.querySelector('.nk-tn'), r = b.querySelector('input');
      r.addEventListener('input', function () { tn.style.setProperty('--x', r.value + '%'); });
      host.appendChild(el);
    });
  }

  /* ── 4. Real Rescuers: cards collected across the unit ──
     The roster is history, not lesson content, so it lives here. Each
     card opens on the lesson whose chapter its part of the history
     belongs to, and stays on every lesson after. */
  var ROSTER = [
    { lid: '16.4', id: 'melchior', name: 'Marcus Melchior', years: '1897–1969', role: 'Rabbi in Copenhagen', img: 'rescuers/melchior.jpg', pos: '50% 0%', initials: 'MM', credit: 'Photo about 1940, public domain, via Wikimedia Commons.',
      back: '<b>He warned everyone.</b> On 29 September 1943, at the morning service before the Jewish New Year, Rabbi Melchior told the people in the Great Synagogue that the Nazis were coming for them in two days. He told them not to stay home, and to pass the warning to every Jewish family they knew. His own family hid with a Danish pastor, then crossed to Sweden.' },
    { lid: '16.4', id: 'duckwitz', name: 'Georg Duckwitz', years: '1904–1973', role: 'A German who told the secret', img: 'rescuers/duckwitz.jpg', pos: '50% 0%', initials: 'GD', credit: 'Photo 1960 (cropped): Renate Patzek, Bundesarchiv B 145 Bild-F008672-0032, CC BY-SA 3.0 DE, via Wikimedia Commons.',
      back: '<b>He worked for the other side, and he still warned them.</b> Georg Duckwitz worked for the German government in Copenhagen. When he learned the date of the raid, he secretly told Danish leaders, and they passed the warning on to the Jewish community. In 1971 Israel honored him as one of the Righteous Among the Nations.' },
    { lid: '17.4', id: 'koster', name: 'Karl Henry Køster', years: '1943', role: 'Surgeon at Bispebjerg Hospital', img: 'rescuers/koster.jpg', pos: '50% 30%', initials: 'KK', credit: 'No free photo of Dr. Køster exists. This plaque at Bispebjerg Hospital thanks its doctors and nurses. Photo: Karen Mardahl, CC BY-SA 2.0, via Wikimedia Commons.',
      back: '<b>He turned a hospital into a hiding place.</b> In October 1943, Dr. Køster and the doctors and nurses of Bispebjerg Hospital in Copenhagen hid Jewish families among the patients and in the hospital chapel. One day a long funeral line of twenty to thirty taxis drove away from the chapel. The riders were not going to a funeral. They were Jewish families on their way to the boats.' },
    { lid: '18.4', id: 'marie', name: 'Børge Laursen & Jacob Andersen', years: '1943', role: 'Fishermen on the boat Marie', img: 'rescuers/marie.jpg', pos: '45% 50%', initials: 'BL', credit: 'The two fishermen aboard Marie. Nationalmuseet (National Museum of Denmark), CC BY-SA 2.0, via Wikimedia Commons.',
      back: '<b>They made the trip again and again.</b> In October 1943, the fishermen Børge Laursen and Jacob Andersen carried Jewish refugees across the water to Sweden in their little boat, <i>Marie</i>. They made about ten trips. Each one meant a dark harbor, a hidden load of people, and German patrol boats somewhere out on the sea.' }
  ];
  function rescuersCard(host, opt) {
    var here = lidNum(opt.week + '.' + opt.day);
    var open = ROSTER.filter(function (r) { return lidNum(r.lid) <= here; });
    if (!open.length) return false;
    var el = card('✦', 'Real Rescuers', 'Real people who helped. Tap a card to turn it over.', [
      'The people in <i>Number the Stars</i> are made up. These people are not. Each card is someone who really helped Denmark’s Jewish families in 1943.',
      'A new card appears on the lesson where the story reaches their part of the history. Your cards stay here for the rest of the book.'
    ]);
    var b = el.querySelector('.nk-body');
    b.innerHTML = '<p class="nk-count">' + open.length + ' card' + (open.length === 1 ? '' : 's') + ' so far.</p><div class="nk-shelf"></div>';
    var shelf = b.querySelector('.nk-shelf');
    open.forEach(function (r) {
      var isNew = r.lid === opt.week + '.' + opt.day;
      var d = document.createElement('div');
      d.className = 'nk-rc' + (isNew ? ' new' : '');
      d.innerHTML = '<button type="button" class="flipper" aria-label="' + esc(r.name) + ', ' + esc(r.role) + '. Turn the card over."><div class="nk-rf"><div class="ph">' + esc(r.initials) + '</div>' +
        '<span class="turn">tap to turn ↻</span><div class="nm"><b>' + esc(r.name) + '</b><span>' + esc(r.years) + ' · ' + esc(r.role) + '</span></div></div>' +
        '<div class="nk-rb">' + r.back + '<span class="nk-cred">' + esc(r.credit || '') + '</span></div></button>';
      var ph = d.querySelector('.ph');
      if (r.img) { var im = new Image(); im.onload = function () { ph.textContent = ''; ph.style.backgroundImage = 'url("' + im.src + '")'; if (r.pos) ph.style.backgroundPosition = r.pos; }; im.src = src(opt, r.img); }
      d.querySelector('.flipper').onclick = function () { d.classList.toggle('flip'); };
      if (isNew) d.appendChild(voiceBtn(opt, 'g4ela-' + opt.week + '-' + opt.day + '-rescuer-' + r.id, 'Grete on ' + r.name.split(' ').slice(-1)[0]));
      shelf.appendChild(d);
    });
    host.appendChild(el);
  }

  /* ── 5. The Psalm (Ch. 10): where the book’s title comes from ── */
  function psalmCard(host, opt) {
    var el = card('✧', 'Where the Title Comes From', 'A verse about three thousand years old.', [
      'This verse is Psalm 147, verse 4, in the old King James translation of the Bible. Jewish and Christian readers both know it.',
      'Today’s chapter is the first time the book uses the words of its own title.'
    ]);
    var b = el.querySelector('.nk-body'), sky = '', seed = 3;
    for (var i = 0; i < 60; i++) {
      seed = (seed * 9301 + 49297) % 233280; var x = seed / 233280 * 100;
      seed = (seed * 9301 + 49297) % 233280; var y = seed / 233280 * 100;
      sky += '<circle cx="' + x.toFixed(1) + '%" cy="' + y.toFixed(1) + '%" r="' + (i % 4 ? .8 : 1.5) + '" fill="#fff" opacity="' + (i % 3 ? .4 : .8) + '"/>';
    }
    b.innerHTML = '<div class="nk-psalm"><svg class="sk" width="100%" height="100%" aria-hidden="true">' + sky + '</svg>' +
      '<blockquote>He telleth the number of the stars; he calleth them all by their names.</blockquote><cite>Psalm 147 : 4</cite></div>';
    b.appendChild(voiceBtn(opt, 'g4ela-' + opt.week + '-' + opt.day + '-psalm', 'Hear Grete read it'));
    host.appendChild(el);
  }

  /* where each card appears; the rest is decided by DATA.nts and the roster */
  KIT.SCHEDULE = { psalm: ['18.2'] };
  KIT.ROSTER = ROSTER;
  KIT.mount = function (kind, host, opt) {
    opt = opt || {};
    var sch = KIT.SCHEDULE[kind];
    if (sch && !opt.force && sch.indexOf(opt.week + '.' + opt.day) < 0) return false;
    injectCSS();
    try {
      return ({ path: pathCard, 'case': caseCard, thennow: thenNowCard, rescuers: rescuersCard, psalm: psalmCard })[kind](host, opt);
    } catch (e) { if (window.console) console.warn('nts kit', kind, e); return false; }
  };
})();
