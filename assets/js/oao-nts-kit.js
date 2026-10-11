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
    { id: 'oster', ch: 1, real: true, x: 330, y: 92, lx: -9, ly: 4, anchor: 'end', name: 'Østerbrogade',
      t: 'A real shopping street in Østerbro, in the northeast of Copenhagen. It is where Annemarie races Ellen in Chapter 1. In 1943 there really were German soldiers standing on its corners.' },
    { id: 'home', ch: 1, real: false, x: 366, y: 46, lx: 9, ly: 4, name: 'Annemarie’s building',
      t: 'The Johansens and the Rosens live in the same apartment building, on different floors. The building is made up, but it sits in a real neighborhood.' },
    { id: 'amal', ch: 2, real: true, x: 442, y: 204, lx: -9, ly: 4, anchor: 'end', name: 'Amalienborg Palace',
      t: 'Four palaces around one square, where the Danish royal family lived and still lives. King Christian X set out from here on his rides through the city.' },
    { id: 'holmen', ch: 2, real: true, x: 498, y: 236, lx: 9, ly: 4, name: 'Holmen naval harbor',
      t: 'Denmark’s navy was based here. On 29 August 1943, Danish sailors sank their own ships in the harbor so Germany could not use them.' },
    { id: 'shop', ch: 3, real: false, x: 352, y: 124, lx: 9, ly: 4, name: 'Mrs. Hirsch’s shop',
      t: 'The little shop that sells buttons and thread. It is in the story, not on a real map. But real Jewish families in Copenhagen did run shops just like it.' },
    { id: 'syn', ch: 4, real: true, x: 334, y: 236, lx: -9, ly: 4, anchor: 'end', name: 'The Great Synagogue',
      t: 'The synagogue on Krystalgade, built in 1833. On 29 September 1943, the morning before the Jewish New Year, the rabbi here warned everyone to hide. That warning really happened.' },
    { id: 'tivoli', ch: 4, real: true, x: 290, y: 306, lx: 9, ly: 4, name: 'Tivoli Gardens',
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

  function cphSVG() {
    return '<svg viewBox="0 0 640 400" role="img" aria-label="An old-style map of Copenhagen with pins on places from the story">' +
      '<defs><radialGradient id="nkPar" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#FBF4E2"/><stop offset=".8" stop-color="#F1E4C4"/><stop offset="1" stop-color="#E2CFA2"/></radialGradient>' +
      '<pattern id="nkHatch" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(20)"><path d="M0 4 H8" stroke="#9FBCC5" stroke-width=".8"/></pattern></defs>' +
      '<rect width="640" height="400" fill="url(#nkPar)"/>' +
      /* the Øresund to the east, Christianshavn across the harbor */
      '<path d="M520 0 C500 50 492 110 500 150 C520 175 560 190 640 200 L640 0 Z" fill="#C9DCE0"/>' +
      '<path d="M520 0 C500 50 492 110 500 150 C520 175 560 190 640 200 L640 0 Z" fill="url(#nkHatch)" opacity=".7"/>' +
      '<path d="M514 210 C560 205 600 214 640 222 L640 400 L376 400 C392 360 420 320 452 280 C470 255 490 225 514 210 Z" fill="#EFE3C3" stroke="#C9B48A" stroke-width=".8"/>' +
      '<path d="M500 150 C470 210 452 250 420 296 C392 336 370 368 356 400" fill="none" stroke="#C9DCE0" stroke-width="20" stroke-linecap="round"/>' +
      '<path d="M500 150 C470 210 452 250 420 296 C392 336 370 368 356 400" fill="none" stroke="#8FAEB8" stroke-width="1" stroke-dasharray="1 5" opacity=".8"/>' +
      /* the three lakes, west of the old town */
      '<g fill="#C9DCE0" stroke="#8FAEB8" stroke-width=".8">' +
        '<ellipse cx="292" cy="104" rx="38" ry="8" transform="rotate(-62 292 104)"/>' +
        '<ellipse cx="266" cy="166" rx="34" ry="8" transform="rotate(-72 266 166)"/>' +
        '<ellipse cx="252" cy="226" rx="30" ry="7" transform="rotate(-82 252 226)"/></g>' +
      /* parks and the star fortress */
      '<path d="M308 176 q22 -8 40 4 q8 18 -6 30 q-22 8 -36 -6 q-8 -14 2 -28 Z" fill="#CFD9B0" stroke="#A9B887" stroke-width=".8"/>' +
      '<path d="M268 290 q26 -10 46 2 q10 20 -4 34 q-26 10 -44 -4 q-10 -16 2 -32 Z" fill="#CFD9B0" stroke="#A9B887" stroke-width=".8"/>' +
      '<path d="M466 124 l12 4 l2 13 l-11 7 l-10 -8 Z" fill="#E2D3AE" stroke="#8C7444" stroke-width="1"/>' +
      '<text x="470" y="164" font-family="Lora,Georgia,serif" font-style="italic" font-size="9" fill="#8C7444" text-anchor="middle">Kastellet</text>' +
      /* streets, inked */
      '<g fill="none" stroke="#B49A68" stroke-width="1.4" stroke-linecap="round" opacity=".85">' +
        '<path d="M318 150 C330 110 346 72 382 6"/>' +
        '<path d="M300 236 C340 236 380 226 420 214"/>' +
        '<path d="M300 236 C300 260 296 280 292 300"/>' +
        '<path d="M336 150 C350 190 360 220 372 260"/>' +
        '<path d="M240 300 C280 290 330 280 380 284"/></g>' +
      /* names of the quarters */
      '<g font-family="Lora,Georgia,serif" font-size="12" fill="#9A835A" letter-spacing="2" text-anchor="middle">' +
        '<text x="420" y="96">ØSTERBRO</text><text x="392" y="262">INDRE BY</text><text x="540" y="300">CHRISTIANSHAVN</text></g>' +
      '<text x="590" y="90" font-family="Lora,Georgia,serif" font-style="italic" font-size="13" fill="#5E8592" text-anchor="middle">Øresund</text>' +
      /* cartouche and compass */
      '<g transform="translate(22 22)"><rect width="170" height="46" rx="4" fill="#FFF9EA" stroke="#B49A68"/><rect x="3" y="3" width="164" height="40" rx="3" fill="none" stroke="#D8C69E"/>' +
        '<text x="85" y="22" text-anchor="middle" font-family="Lora,Georgia,serif" font-size="15" font-weight="600" fill="#3B2E17">København</text>' +
        '<text x="85" y="36" text-anchor="middle" font-family="Nunito,sans-serif" font-size="9" font-weight="800" letter-spacing="2" fill="#8C7444">COPENHAGEN · 1943</text></g>' +
      '<g transform="translate(58 340)" fill="#8C7444"><circle r="20" fill="none" stroke="#B49A68"/><path d="M0 -24 L5 0 L0 24 L-5 0 Z" opacity=".85"/><path d="M-24 0 L0 4 L24 0 L0 -4 Z" opacity=".45"/>' +
        '<text y="-28" text-anchor="middle" font-family="Nunito,sans-serif" font-size="9" font-weight="800">N</text></g>' +
      '<g class="pins"></g></svg>';
  }
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
      '<text class="pl' + (p.real ? '' : ' story') + '" x="' + (x + (p.lx || 9)) + '" y="' + (y + (p.ly || 4)) + '" text-anchor="' + a + '">' + esc(p.name) + '</text></g>';
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
      back: '<b>He turned a hospital into a hiding place.</b> In October 1943, Dr. Køster and the doctors and nurses of Bispebjerg Hospital in Copenhagen hid Jewish families among the patients and in the hospital chapel. One day a long funeral line of twenty to thirty taxis drove away from the chapel. The riders were not going to a funeral. They were Jewish families on their way to the boats.' }
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
