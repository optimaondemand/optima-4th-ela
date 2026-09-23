/* ══════════════════════════════════════════════════════════════
   OAO SPARKLE — Phase 1, demo build (inlined)
   Everything below lifts out verbatim into
   assets/oao-sparkle.js when the shared-script architecture (§1)
   goes in. Nothing above this block was modified except the
   <script type="application/json" id="oao-lesson"> declaration.
   ══════════════════════════════════════════════════════════════ */
(function () {
"use strict";

/* ── §1 storage layer ──────────────────────────────────────── */
var Sparkle = {
  get: function (k, dflt) {
    try { var v = localStorage.getItem(k); return v ? JSON.parse(v) : (dflt === undefined ? null : dflt); }
    catch (e) { return dflt === undefined ? null : dflt; }
  },
  set: function (k, v) { try { localStorage.setItem(k, JSON.stringify(v)); } catch (e) {} }
};
window.Sparkle = Sparkle;

var REDUCED = false;
try { REDUCED = window.matchMedia('(prefers-reduced-motion: reduce)').matches; } catch (e) {}

/* ── §1 lesson declaration ─────────────────────────────────── */
var LESSON = { grade: 4, subject: 'ela', book: 'anne', week: 7, day: 1 };
try {
  var decl = document.getElementById('oao-lesson');
  if (decl) LESSON = JSON.parse(decl.textContent);
} catch (e) {}
var LID = LESSON.week + '.' + LESSON.day;

/* ── §1.2 course map ───────────────────────────────────────── */
var COURSE = [
  { id:'frisby',  title:'Mrs. Frisby and the Rats of NIMH', weeks:[1,5],   place:'the Fitzgibbon farm' },
  { id:'writing', title:"Writer's Workshop",                weeks:[6,6],   place:null, kind:'workshop' },
  { id:'anne',    title:'Anne of Green Gables',             weeks:[7,14],  place:'Prince Edward Island' },
  { id:'bridge',  title:'Bridge to Number the Stars',       weeks:[15,15], place:'Denmark, 1943', kind:'bridge' },
  { id:'nts',     title:'Number the Stars',                 weeks:[16,19], place:'Copenhagen' },
  { id:'ft',      title:'Freedom Train',                    weeks:[20,25], place:'Maryland to Canada' },
  { id:'pc',      title:'Prince Caspian',                   weeks:[26,30], place:'Narnia' },
  { id:'synth',   title:'Synthesis',                        weeks:[31,32], place:null, kind:'synthesis' }
];
/* The shelf holds the five novels only. The student's own writing is
   not a book on the shelf — it lives on the map, at Writer's Workshop
   and again at Journey's End. */
var SHELF = [
  { id:'frisby', short:'Mrs. Frisby' },
  { id:'anne',   short:'Anne of Green Gables', gold:true },
  { id:'nts',    short:'Number the Stars' },
  { id:'ft',     short:'Freedom Train' },
  { id:'pc',     short:'Prince Caspian' }
];

/* ══════════════════════════════════════════════════════════════
   ART — the ONLY place image files are named.
   Drop Bethany's files in and every use of them updates at once.
   Anything left as '' falls back to the drawn version, so the
   lesson is never broken by a missing or slow image.
   `base` is prepended to any path that isn't already absolute.
   ══════════════════════════════════════════════════════════════ */
var ART = {
  /* ── PRODUCTION ─────────────────────────────────────────────
     When the assets are pushed to the repo, delete the embedded
     data URIs below and use these instead:

       base: 'https://optimaondemand.github.io/optima-4th-ela/assets/',
       covers: { frisby:'covers/frisby.jpg', anne:'covers/anne.jpg',
                 nts:'covers/nts.jpg', ft:'covers/ft.jpg',
                 pc:'covers/pc.jpg', mywriting:'covers/mywriting.svg' },
       companions: { optima:'companions/owl.png' }

     The demo embeds them so the file works by double-click with
     no server and no deploy.
     ──────────────────────────────────────────────────────────── */
  /* Every image is a PATH, never an embedded data: URI.

     This is deliberate and it is about the child's connection, not
     tidiness. Baked into the page, this art is ~2 MB that cannot be
     cached between lessons, so a student re-downloads the identical
     map and ornaments on all 129 of them — roughly 250 MB over a year.
     Referenced, the browser fetches each file once in week 7 and every
     later lesson is instant.

     The cost of the choice: a lesson only works served from the repo
     or Pages, not opened as a loose file off a desktop. That is the
     accepted trade. Do not inline something to make one file portable. */
  base: 'assets/',

  /* §2.2 the year map. Bethany's painted board — the spaces are part
     of the picture, so their coordinates were measured off the file
     (BOARD_SPACES below) and the progress layer is drawn on top. */
  board: { src: 'maps/year-board.jpg' },

  covers: {
    frisby:    'covers/frisby.jpg',
    anne:      'covers/anne.jpg',
    nts:       'covers/nts.jpg',
    ft:        'covers/ft.jpg',
    pc:        'covers/pc.jpg',
    mywriting: 'covers/mywriting.svg'
  },

  /* per-world art. `terrain` paints that stretch of the map and is
     feathered into its neighbours so the map stays one picture;
     `landmark` is the object that stands beside the road. Either
     can be left '' and the drawn version is used instead. */
  worlds: {
    frisby:  { terrain:'', landmark:'' },
    writing: { terrain:'', landmark:'' },
    anne:    { terrain:'', landmark:'' },
    bridge:  { terrain:'', landmark:'' },
    nts:     { terrain:'', landmark:'' },
    ft:      { terrain:'', landmark:'' },
    pc:      { terrain:'', landmark:'' },
    synth:   { terrain:'', landmark:'' }
  },

  /* The chapter illustration — one per lesson, printed under the quote
     the way a chapter heading sits on the page of a good children's
     book. No caption: the chapter quote above it is the only words.

     Not listed here, because it is not one file: the path is built
     from the lesson's own book and chapters by plateSrc() below. */
  plate: { src: '' },

  /* Two sizes of one mark. `scholar` is the full wreathed seal for the
     published page; `mark` is the wax disc alone, because at 46px on
     the year map the laurel closes into a smudge and the disc inside
     it is all that survives. */
  seals: {
    scholar: 'seals/scholar.png',
    mark:    'seals/scholar-mark.png'
  },

  /* Writer's Workshop headpieces, one per genre arc. */
  banners: {
    narrative:'banners/narrative.png', fiction: 'banners/fiction.png',
    opinion:  'banners/opinion.png',   research:'banners/research.png',
    analysis: 'banners/analysis.png',  yearend: 'banners/yearend.png'
  },

  /* pen-and-ink spot ornaments. Used sparingly and always decoratively —
     none of them carries meaning, so all are aria-hidden / CSS-only.
     The set is closed; eight is enough that the rotation does not show. */
  ornaments: {
    divider: 'ornaments/divider.png',
    corner:  'ornaments/corner.png',
    quill:   'ornaments/quill.png',
    blossom: 'ornaments/blossom.png',
    books:   'ornaments/books.png',
    letter:  'ornaments/letter.png',
    sprig:   'ornaments/sprig.png',
    divider2:'ornaments/divider-books.png'
  },

  companions: { optima: 'companions/owl.png' }
};

/* The chapter plate's filename, built from the lesson declaration:
     book 'anne' + chapters 'Ch. 3 & 4'  ->  plates/anne-ch3-4.png
     book 'anne' + chapters 'Ch. 1'      ->  plates/anne-ch1.png
   .png always. If the file is not there the plate simply does not
   render, and it appears the moment the file lands — no rebuild. */
function plateSrc() {
  if (ART.plate && ART.plate.src) return artURL(ART.plate.src);   /* override */
  var nums = String(LESSON.chapters || '').match(/\d+/g);
  if (!nums || !nums.length || !LESSON.book) return '';
  return artURL('plates/' + LESSON.book + '-ch' + nums.join('-') + '.png');
}
window.OAO_ART = ART;   /* exposed so art can be swapped without touching code */
/* after changing OAO_ART, call this to repaint everything that uses it */
window.OAO_refreshArt = function () {
  try { drawShelf(); } catch (e) {}
  try { if (document.getElementById('spkMap')) drawMap(); } catch (e) {}
};
/* the companions we have art for, in picker order */
function companionKeys() {
  return Object.keys(ART.companions).filter(function (k) { return !!artURL(ART.companions[k]); });
}
function defaultCompanion() { return companionKeys()[0] || 'tawny'; }
/* a profile saved by an earlier build may name a companion we no longer
   have art for — resolve it to one we do */
function resolveCompanion(key) {
  if (key && artURL(ART.companions[key])) return key;
  return companionKeys().length ? defaultCompanion() : (key || 'tawny');
}
function artURL(pathish) {
  if (!pathish) return '';
  return /^(https?:|data:|\/)/.test(pathish) ? pathish : (ART.base + pathish);
}

/* ── owl copy (§2.4) ───────────────────────────────────────── */
var OWL = {
  correct: ['Well spotted.', "That's the one.", 'Just so.', 'Good eye.'],
  complete: 'Well read',
  stuck: "Let's look at it together."
};
var owlCorrectIdx = 0;
window.__spkOwlDrawn = function (k, n) { return owlDrawn(k, n); };
/* inside an <svg> an <img> is invalid — use <image> there */
function owlMarkSVG(key, size) {
  key = resolveCompanion(key);
  var img = artURL(ART.companions[key]);
  /* stand the owl on the road: anchor the art to the bottom of its box */
  if (img) return '<image href="' + img + '" x="0" y="0" width="' + size + '" height="' + size +
                  '" preserveAspectRatio="xMidYMax meet"/>';
  return owlDrawn(key, size);
}

/* ── owl plumages (§2.5) ───────────────────────────────────── */
var PLUMAGE = {
  barn:        { label:'Barn',        body:'#D9B98C', face:'#FBF4E7', tuft:'#C29A68' },
  snowy:       { label:'Snowy',       body:'#EDF2FA', face:'#FFFFFF', tuft:'#CBD8EA' },
  greathorned: { label:'Great Horned',body:'#8A6A4B', face:'#E4CBA8', tuft:'#5E452E' },
  tawny:       { label:'Tawny',       body:'#B87333', face:'#EBD3A8', tuft:'#8A5220' }
};
function owlSVG(key, size) {
  key = resolveCompanion(key);
  size = size || 44;
  var img = artURL(ART.companions[key]);
  if (img) {
    /* portrait artwork: give it a height and let the width follow, or
       a square box squashes the bird */
    return '<img class="spk-companion-img" src="' + img + '" height="' + size +
           '" alt="" onerror="this.outerHTML=window.__spkOwlDrawn(\'' + key + '\',' + size + ')" />';
  }
  return owlDrawn(key, size);
}
function owlDrawn(key, size) {
  var p = PLUMAGE[key] || PLUMAGE.tawny; size = size || 44;
  return '<svg viewBox="0 0 64 64" width="' + size + '" height="' + size + '" aria-hidden="true">' +
    '<circle cx="32" cy="32" r="31" fill="' + p.body + '"/>' +
    '<path d="M12 18 L20 6 L26 17 Z" fill="' + p.tuft + '"/>' +
    '<path d="M52 18 L44 6 L38 17 Z" fill="' + p.tuft + '"/>' +
    '<ellipse cx="23" cy="30" rx="10" ry="11" fill="' + p.face + '"/>' +
    '<ellipse cx="41" cy="30" rx="10" ry="11" fill="' + p.face + '"/>' +
    '<circle cx="23" cy="30" r="4.6" fill="#0E1C42"/>' +
    '<circle cx="41" cy="30" r="4.6" fill="#0E1C42"/>' +
    '<circle cx="24.6" cy="28.4" r="1.5" fill="#fff"/>' +
    '<circle cx="42.6" cy="28.4" r="1.5" fill="#fff"/>' +
    '<path d="M32 33 L28 39 L36 39 Z" fill="#C7922C"/>' +
    '<path d="M22 46 Q32 54 42 46" stroke="' + p.tuft + '" stroke-width="2.5" fill="none" stroke-linecap="round"/>' +
    '</svg>';
}

/* ══════════════════════════════════════════════════════════════
   LESSON CONTENT (§3) — the authored data this lesson's
   sparkle features read. In the full build this lives in the
   HTML as data-* attributes; kept here so the demo file is
   readable in one place.
   ══════════════════════════════════════════════════════════════ */
var DATA = {
  /* §2.5 second DOL fix-it sentence, from Ch. 1 */
  dol: {
    a: { raw: 'mrs rachel lynde walked through avonlea every morning',
         fixed: '<strong>Mrs. Rachel Lynde</strong> walked through <strong>Avonlea</strong> every <strong>morning.</strong>',
         why: 'Capital letters on the title and names (Mrs. Rachel Lynde), a capital on the place name (Avonlea), a period at the end. Common nouns like "morning" stay lowercase.' },
    b: { raw: 'the brook ran past mrs rachels door in lyndes hollow',
         fixed: '<strong>The</strong> brook ran past <strong>Mrs. Rachel’s</strong> door in <strong>Lynde’s Hollow.</strong>',
         why: 'Capital at the start of the sentence, capitals on the title and names, apostrophes to show the door belongs to Mrs. Rachel and the hollow to the Lyndes, and a period at the end.' }
  },

  /* §2.5 Scholar variants of Chapter Thinking */
  scholar: {
    'journal-q1': '… and name one thing the narrator tells you about Matthew that Mrs. Rachel does not know.',
    'journal-q2': '… and for each detail, say what it makes you feel about living in Avonlea.',
    'journal-q3': '… and quote the line that shows it most clearly.'
  },

  /* §2.6 coaching flags */
  flags: {
    'journal-q1': { quote: false, count: 0 },
    'journal-q2': { quote: false, count: 2 },
    'journal-q3': { quote: true,  count: 0 }
  },

  /* §2.7 hint ladders for the morphology fill-ins */
  hints: {
    fill1: { h1:'The word means to join things together. Which of the two prefixes is spelled with an n?',
             h2:'c _ _', why:'<b>con-</b> means "with" or "together," so <b>connect</b> is to join one thing together with another.' },
    fill2: { h1:'Say it out loud: com-bine. Listen to the letter just before the b.',
             h2:'c _ _', why:'<b>com-</b> means "together." To <b>combine</b> is to bring things together into one.' },
    fill3: { h1:'A company is a group of people together. It takes the same prefix as combine.',
             h2:'c _ _', why:'<b>com-</b> means "together," so <b>company</b> is the people who go along together.' },
    fill4: { h1:'To continue is to keep going with what you started. Same prefix as connect.',
             h2:'c _ _', why:'<b>con-</b> means "with," so <b>continue</b> is to keep going with the thing you began.' }
  },

  /* §2.7 distractor lines */
  miss: {
    match: {
      'placid':     'Placid is about calm, not about company.',
      'imagine':    'Imagining happens in your head — look for the meaning about pictures in the mind.',
      'companion':  'A companion is a person, so its meaning should describe a person.',
      'delight':    'Delight is a feeling. Look for the meaning that names a feeling.'
    },
    sort: {
      'child → children': 'Children does not end in -s at all — the whole middle of the word changed.',
      'woman → women':    'Listen to the vowel: woman, women. The change is inside the word, not on the end.',
      'foot → feet':      'No ending was added here — oo simply became ee.',
      'road → roads':     'Roads is the ordinary -s rule, nothing surprising.',
      'gable → gables':   'Gables just adds -s. Nothing inside the word moved.',
      'window → windows': 'Windows adds -s like most nouns do.',
      'cats':    'Cat takes a plain -s — nothing hisses at the end.',
      'roads':   'Road takes a plain -s.',
      'trees':   'Tree takes a plain -s.',
      'boxes':   'Try saying "boxs." The x makes you need the extra -es.',
      'brushes': 'Try saying "brushs." The sh makes you need the extra -es.',
      'stories': 'Story ends in consonant + y, so the y became an i before -es.'
    }
  },

  /* §2.8 copia */
  copia: {
    seed: 'Mrs. Rachel Lynde <b data-verb>sat</b> at her window and watched the road.',
    eg: [
      'Every afternoon, Mrs. Rachel Lynde sat at her window and watched the road.',
      'Mrs. Rachel Lynde <i>perched</i> at her window and watched the road.',
      'Mrs. Rachel Lynde sat at her window in Lynde’s Hollow and watched the road carefully.'
    ]
  },

  /* the teacher's opening words. Every lesson gets one: it ties what
     they just finished to what they are about to do, in the voice a
     teacher would use standing at the front of the room. */
  writingFocus: 'Voice',

  connector: 'Last week you closed Mrs. Frisby and stood it on your shelf. Today we open a new one. ' +
             'Anne of Green Gables begins quietly \u2014 a woman at her window, a man driving past in his ' +
             'good suit, and a question she cannot leave alone. Watch how much Montgomery tells you about ' +
             'Avonlea before anybody in it says a word.',

  /* §2.9 memory work — Tennyson, "The Lady of Shalott" (1842, public domain) */
  poem: {
    title: 'The Lady of Shalott',
    author: 'Alfred, Lord Tennyson',
    lines: [
      ['On either side the river lie', 0],
      ['Long fields of barley and of rye,', 0],
      ['That clothe the wold and meet the sky;', 0],
      ['And thro’ the field the road runs by', 0],
      ['To many-tower’d Camelot;', 1],
      ['And up and down the people go,', 0],
      ['Gazing where the lilies blow', 0],
      ['Round an island there below,', 0],
      ['The island of Shalott.', 1]
    ]
  }
};

/* ══════════════════════════════════════════════════════════════
   THE WRITING PROJECT
   Writing runs the whole year in six genre arcs (see the scope &
   sequence). A lesson used to name only the day's step — "Week 7 ·
   VOICE" — so a student never learned what they were building. Each
   Workshop card now says the genre, what it means, and when it is
   published.
   ══════════════════════════════════════════════════════════════ */
var WRITING_ARCS = [
  { weeks:[1,6],   name:'a personal narrative',    gloss:'a true story from your own life' },
  { weeks:[7,14],  name:'a realistic fiction story', gloss:'a made-up story that could really happen' },
  { weeks:[15,19], name:'an opinion essay',        gloss:'writing where you say what you think and give reasons' },
  { weeks:[20,25], name:'a research report',       gloss:'writing that answers a real question with facts you gather' },
  { weeks:[26,30], name:'a literary analysis',     gloss:'writing that explains what a book means and how you know' },
  { weeks:[31,32], name:'your year-end project',   gloss:'comparing the books you have read this year' }
];
function titleCase(str) {
  return str.replace(/\b[a-z]/g, function (c) { return c.toUpperCase(); });
}
function writingArc(week) {
  for (var i = 0; i < WRITING_ARCS.length; i++) {
    var a = WRITING_ARCS[i];
    if (week >= a.weeks[0] && week <= a.weeks[1]) return a;
  }
  return null;
}

/* Every Workshop entry is mirrored into one shared place so the next
   day's lesson can read it. The lesson's own autoSave is keyed to
   _lessonKey (which comes from document.title), so Monday's writing
   is saved but invisible on Tuesday — which defeats a project that
   is supposed to build day by day. */
function writingSaveEntry(text) {
  var all = Sparkle.get('oao.g4ela.writing', {});
  if (!text || !text.trim()) { delete all[LID]; }
  else { all[LID] = { text: text, at: new Date().toISOString(), focus: DATA.writingFocus || '' }; }
  Sparkle.set('oao.g4ela.writing', all);
}
function writingEarlierEntries() {
  var all = Sparkle.get('oao.g4ela.writing', {});
  var arc = writingArc(LESSON.week); if (!arc) return [];
  return Object.keys(all).map(function (k) {
    var p = k.split('.');
    return { id: k, week: +p[0], day: +p[1], entry: all[k] };
  }).filter(function (e) {
    return e.week >= arc.weeks[0] && e.week <= arc.weeks[1] &&
           (e.week < LESSON.week || (e.week === LESSON.week && e.day < LESSON.day));
  }).sort(function (a, b) { return a.week - b.week || a.day - b.day; });
}

function buildWritingProject() {
  var box = document.getElementById('journal-writing'); if (!box) return;
  var card = box.closest('.activity'); if (!card) return;
  var body = card.querySelector('.activity-body'); if (!body) return;
  var arc = writingArc(LESSON.week); if (!arc) return;
  var step = LESSON.week - arc.weeks[0] + 1;
  var of = arc.weeks[1] - arc.weeks[0] + 1;

  /* the headpiece for this genre, above everything else in the card.
     Six arcs, six pictures — the Workshop used to look identical in
     every week of the year. Decorative only; the goal card below
     still says the genre in words. */
  var ARC_ART = ['narrative', 'fiction', 'opinion', 'research', 'analysis', 'yearend'];
  var arcKey = ARC_ART[WRITING_ARCS.indexOf(arc)];
  var headSrc = artURL((ART.banners || {})[arcKey]);
  if (headSrc) {
    var head = document.createElement('div');
    head.className = 'spk-arc-head';
    head.setAttribute('aria-hidden', 'true');
    var hi = document.createElement('img');
    hi.src = headSrc; hi.alt = ''; hi.loading = 'lazy';
    hi.onerror = function () { head.remove(); };
    head.appendChild(hi);
    body.insertBefore(head, body.firstChild);
  }

  /* the goal banner — first thing in the card */
  var goal = document.createElement('div');
  goal.className = 'spk-goal';
  goal.innerHTML =
    '<div class="spk-goal-label">What you are writing</div>' +
    '<div class="spk-goal-title">' + arc.name.charAt(0).toUpperCase() + arc.name.slice(1) + '</div>' +
    '<div class="spk-goal-gloss">' + arc.gloss + '</div>' +
    '<div class="spk-goal-meta">Week ' + step + ' of ' + of + ' \u00b7 you finish it and publish it in Week ' +
      arc.weeks[1] + '</div>' +
    '<div class="spk-keep">' +
      '<div class="spk-keep-title">Keep your writing in one place</div>' +
      '<p>Make one document just for this project and call it <b>My ' +
      titleCase(arc.name.replace(/^an? /, '').replace(/^your /, '')) +
      '</b> \u2014 a Google Doc, a Word file, or a page in your notebook. ' +
      'Every day: write in the box below, then <b>copy it into your own document</b>. ' +
      'That way your whole story is in one place and nothing gets lost.</p>' +
    '</div>';
  var firstReal = document.querySelector('.spk-arc-head');
  if (firstReal && firstReal.parentNode === body) body.insertBefore(goal, firstReal.nextSibling);
  else body.insertBefore(goal, body.firstChild);

  /* what they wrote on the earlier days of this project */
  var earlier = writingEarlierEntries();
  if (earlier.length) {
    var box2 = document.createElement('details');
    box2.className = 'spk-earlier';
    var items = earlier.map(function (e) {
      var d = document.createElement('div');
      d.className = 'spk-earlier-item';
      var h = document.createElement('div');
      h.className = 'spk-earlier-when';
      h.textContent = 'Lesson ' + e.id + (e.entry.focus ? ' \u00b7 ' + e.entry.focus : '');
      var t = document.createElement('p');
      t.className = 'spk-earlier-text'; t.textContent = e.entry.text;   /* student text: never innerHTML */
      d.appendChild(h); d.appendChild(t);
      return d;
    });
    var sum = document.createElement('summary');
    sum.textContent = 'What you wrote on this project before (' + earlier.length + ')';
    var caveat = document.createElement('p');
    caveat.className = 'spk-earlier-caveat';
    caveat.textContent = 'This only remembers work done on this computer. Your own document is the ' +
      'copy that always has everything.';
    box2.appendChild(sum);
    box2.appendChild(caveat);
    items.forEach(function (d) { box2.appendChild(d); });

    var last = earlier[earlier.length - 1];
    var carry = document.createElement('button');
    carry.type = 'button'; carry.className = 'spk-mini-btn';
    carry.textContent = 'Put my last writing in the box below';
    carry.onclick = function () {
      if (box.value.trim()) { carry.textContent = 'Your box already has writing in it'; return; }
      box.value = last.entry.text;
      box.dispatchEvent(new Event('input', { bubbles: true }));
      carry.textContent = 'Copied \u2014 keep building on it';
      carry.disabled = true; carry.style.opacity = '.6';
    };
    box2.appendChild(carry);
    body.insertBefore(box2, goal.nextSibling);
  }

  /* a one-tap copy, so "put it in your own document" is easy to obey */
  var tools = document.createElement('div');
  tools.className = 'spk-write-tools';
  var copy = document.createElement('button');
  copy.type = 'button'; copy.className = 'spk-btn spk-copy-writing';
  copy.textContent = 'Copy today\u2019s writing';
  var note = document.createElement('span');
  note.className = 'spk-write-note';
  note.textContent = 'Then paste it into your own document.';
  copy.onclick = function () {
    var text = box.value;
    if (!text.trim()) { note.textContent = 'Write something first, then copy it.'; return; }
    function done() {
      copy.textContent = 'Copied \u2014 now paste it in your document';
      note.textContent = 'Your document is the one that always has your whole story.';
      setTimeout(function () { copy.textContent = 'Copy today\u2019s writing'; }, 4000);
    }
    try {
      navigator.clipboard.writeText(text).then(done, function () { box.select(); document.execCommand('copy'); done(); });
    } catch (e) { box.select(); document.execCommand('copy'); done(); }
  };
  tools.appendChild(copy); tools.appendChild(note);
  box.parentNode.insertBefore(tools, box.nextSibling);

  /* mirror every keystroke into the shared store */
  box.addEventListener('input', function () { writingSaveEntry(box.value); });
  if (box.value.trim()) writingSaveEntry(box.value);
}

/* ══════════════════════════════════════════════════════════════
   §2.1  PROFILE + GREETING
   ══════════════════════════════════════════════════════════════ */
function profile() { return Sparkle.get('oao.profile', null); }

/* ══════════════════════════════════════════════════════════════
   NAME CHECK
   Two lists, because one cannot do both jobs:
     STRONG — matched anywhere in the name. These strings do not
              occur inside real first names.
     WHOLE  — matched only as a whole word. "ass" and "hell" sit
              inside Cassandra and Hellen, so a substring match
              would turn away real children by name.
   Leetspeak is folded first (4>a, 3>e, 1>i, 0>o, $>s) and repeated
   letters collapsed, so "sh1t" and "fuuuuck" are caught too.
   A starter list, not a guarantee — worth swapping for a maintained
   one before the course ships.
   ══════════════════════════════════════════════════════════════ */
var NAME_STRONG = [
  'fuck','shit','bitch','cunt','whore','slut','wank','bollock','bastard',
  'penis','vagina','boob','anus','turd','scrotum','testicle',
  'nigg','fagg','retard','kike','chink','tranny',
  'porn','rape','nazi','hitler'
];
var NAME_WHOLE = [
  'ass','arse','hell','damn','crap','piss','poop','pee','fart','butt','bum',
  'dick','cock','prick','knob','willy','tit','sex','kill',
  'dumb','stupid','idiot','loser','ugly','fatso','poopy','poopyhead'
];
function nameFold(v) {
  return String(v).toLowerCase()
    .replace(/[4@]/g, 'a').replace(/3/g, 'e').replace(/[1!|]/g, 'i')
    .replace(/0/g, 'o').replace(/[$5]/g, 's').replace(/7/g, 't')
    .replace(/[^a-z ]+/g, ' ')
    .replace(/(.)\1+/g, '$1')
    .replace(/\s+/g, ' ').trim();
}
var _STRONG_F = null, _WHOLE_F = null;
function nameProblem(raw) {
  if (!_STRONG_F) {
    _STRONG_F = NAME_STRONG.map(nameFold);
    _WHOLE_F  = NAME_WHOLE.map(nameFold);
  }
  var name = String(raw || '').trim();
  if (!name) return 'Type your first name.';
  if (name.replace(/[^A-Za-z]/g, '').length < 2) return 'That is a bit short \u2014 what do people call you?';
  var folded = nameFold(name);
  if (!folded) return 'Use letters for your name.';
  var i;
  for (i = 0; i < NAME_STRONG.length; i++) {
    if (_STRONG_F[i] && folded.indexOf(_STRONG_F[i]) !== -1) return 'block';
  }
  /* "F U C K" — letters spaced out. Check the de-spaced form too, but
     only against entries of 4+ folded characters: shorter ones would
     start matching across the join in ordinary two-part names. */
  var squashed = folded.replace(/ /g, '');
  for (i = 0; i < _STRONG_F.length; i++) {
    if (_STRONG_F[i].length >= 4 && squashed.indexOf(_STRONG_F[i]) !== -1) return 'block';
  }
  var words = folded.split(' ');
  for (i = 0; i < words.length; i++) {
    if (_WHOLE_F.indexOf(words[i]) !== -1) return 'block';
  }
  return null;
}
/* the map title is built by string concatenation into innerHTML */
function esc(t) {
  return String(t).replace(/&/g, '&amp;').replace(/</g, '&lt;')
                  .replace(/>/g, '&gt;').replace(/"/g, '&quot;');
}

/* returns [before-the-name, after-the-name] so the name itself can
   be set apart. Never innerHTML — the name is always textContent. */
function greetingParts(p) {
  var prog = Sparkle.get('oao.g4ela.progress', {});
  var me = prog[LID];
  if (LESSON.day === 'fluency') return ['Time to read aloud, ', '.'];
  if (me && me.tabs && me.tabs.length > 1) return ['Picking up where you left off, ', '.'];
  if (LESSON.day === 1) return ['Welcome back, ', '. A new week \u2014 and a new chapter.'];
  var prev = LESSON.week + '.' + (LESSON.day - 1);
  if (prog[prev] && prog[prev].done) return ['Welcome back, ', '. Yesterday you finished Lesson ' + prev + '.'];
  return ['Welcome back, ', '.'];
}

function renderGreeting() {
  var p = profile(); if (!p) return;
  var panel = document.getElementById('tab-warmup'); if (!panel) return;
  var line = document.getElementById('spkGreet');
  if (!line) {
    line = document.createElement('section');
    line.className = 'spk-open'; line.id = 'spkGreet';
    line.innerHTML =
      '<div class="spk-open-head">' +
        '<span class="spk-open-owl" id="spkGreetOwl"></span>' +
        '<h2 class="spk-open-greet"><span id="spkGreetA"></span>' +
        '<b class="spk-greet-name" id="spkGreetName"></b>' +
        '<span id="spkGreetB"></span>' +
        '<button type="button" class="spk-greet-edit" title="Fix the spelling of my name">\u270E</button></h2>' +
      '</div>' +
      '<p class="spk-open-say" id="spkOpenSay"></p>';
    line.querySelector('.spk-greet-edit').onclick = function () { showProfileCard(true); };
    panel.insertBefore(line, panel.firstChild);
  }
  var parts = greetingParts(p);
  document.getElementById('spkGreetA').textContent = parts[0];
  document.getElementById('spkGreetName').textContent = p.name;   /* never innerHTML */
  document.getElementById('spkGreetB').textContent = parts[1];
  document.getElementById('spkGreetOwl').innerHTML = owlSVG(p.owl, 52);
  var say = document.getElementById('spkOpenSay');
  if (DATA.connector) say.textContent = DATA.connector;
  else say.remove();
  try { buildMedia(); } catch (e) {}
  dividerAfterOpening();
}

/* The header logo is the Optima mark and is never replaced. The
   student's chosen companion appears on the map and on the profile
   card only. */

function showProfileCard(isEdit) {
  if (document.getElementById('spkProfileCard')) return;
  var anchor = document.getElementById('introSection');
  if (!anchor) return;
  var p = profile() || { name: '', owl: defaultCompanion() };
  var card = document.createElement('div');
  card.className = 'spk-profile-card'; card.id = 'spkProfileCard';
  var keys = companionKeys();
  var pickable = keys.length > 1 ? keys : [];
  var owls = pickable.map(function (k) {
    return '<button type="button" class="spk-owl-pick' + (p.owl === k ? ' sel' : '') +
      '" data-owl="' + k + '">' + owlSVG(k, 44) +
      '<span>' + ((PLUMAGE[k] && PLUMAGE[k].label) || k) + '</span></button>';
  }).join('');
  card.innerHTML =
    '<h3>' + (isEdit ? 'Fix your name' : 'Before we begin: what should Anne call you?') + '</h3>' +
    '<p class="spk-sub">Just your first name. It stays on this computer — nobody else sees it.</p>' +
    '<div class="spk-name-row">' +
      '<input class="spk-name-input" id="spkNameInput" maxlength="24" autocomplete="off" placeholder="Your name" />' +
      '<button class="spk-btn" id="spkBegin" type="button">' + (isEdit ? 'Save' : 'Begin') + '</button>' +
    '</div>' +
    (pickable.length
      ? '<div class="spk-owl-label">Which owl will read with you?</div>' +
        '<div class="spk-owl-row" id="spkOwlRow">' + owls + '</div>'
      : '<div class="spk-companion-solo">' + owlSVG(defaultCompanion(), 62) +
        '<span>This is the owl who reads along with you. You\u2019ll see it on the Reading Road.</span></div>');
  anchor.parentNode.insertBefore(card, anchor);

  var input = card.querySelector('#spkNameInput');
  input.value = p.name || '';
  var chosen = p.owl || defaultCompanion();
  card.querySelectorAll('.spk-owl-pick').forEach(function (b) {
    b.onclick = function () {
      chosen = b.getAttribute('data-owl');
      card.querySelectorAll('.spk-owl-pick').forEach(function (x) { x.classList.remove('sel'); });
      b.classList.add('sel');
    };
  });
  var begin = card.querySelector('#spkBegin');
  function clean(v) { return (v || '').replace(/[^A-Za-z \-']/g, '').trim().slice(0, 24); }
  function sync() { begin.disabled = clean(input.value).length === 0; }
  input.addEventListener('input', sync); sync();
  input.addEventListener('keydown', function (e) { if (e.key === 'Enter' && !begin.disabled) begin.click(); });
  var warn = document.createElement('div');
  warn.className = 'spk-name-warn'; warn.style.display = 'none';
  card.querySelector('.spk-name-row').insertAdjacentElement('afterend', warn);
  input.addEventListener('input', function () { warn.style.display = 'none'; });

  begin.onclick = function () {
    var name = clean(input.value);
    /* test what they typed AND what we keep — clean() strips digits,
       which is the whole trick behind "sh1t" and "n1gger" */
    var problem = nameProblem(input.value) || nameProblem(name);
    if (problem) {
      warn.style.display = 'block';
      warn.textContent = problem === 'block'
        ? 'Let\u2019s use your real first name \u2014 this is the name that goes on your work.'
        : problem;
      input.focus();
      return;
    }
    warn.style.display = 'none';
    var old = profile();
    Sparkle.set('oao.profile', { name: name, owl: chosen, created: (old && old.created) || new Date().toISOString() });
    card.parentNode.removeChild(card);
    renderGreeting();
    renderIllumAuthor();
    owlSay('Well met, ' + name + '.');
  };
  input.focus();
}

/* ══════════════════════════════════════════════════════════════
   §2.4  OWL SPEECH SLIP
   ══════════════════════════════════════════════════════════════ */
var owlTimer = null;
function owlSay(text) {
  var brand = document.querySelector('.header'); if (!brand) return;
  var slip = document.getElementById('spkOwlSlip');
  if (!slip) {
    slip = document.createElement('div');
    slip.className = 'spk-owl-slip'; slip.id = 'spkOwlSlip';
    brand.appendChild(slip);
  }
  slip.textContent = text;
  slip.classList.add('show');
  clearTimeout(owlTimer);
  owlTimer = setTimeout(function () { slip.classList.remove('show'); }, 2500);
}
function owlCorrect() {
  owlSay(OWL.correct[owlCorrectIdx % OWL.correct.length]); owlCorrectIdx++;
}

/* ══════════════════════════════════════════════════════════════
   §2.2  PROGRESS: dot track + year map   §2.3 bookshelf
   ══════════════════════════════════════════════════════════════ */
function lessonHref(week, day) {
  if (day === 'fluency') return 'lesson-' + week + '-fluency.html';
  /* Demo build knows only Week 7's filenames; the real script
     derives these from the repo's naming convention. */
  var MAP = { '7.1':'lesson-7-1-anne-ch1.html', '7.2':'lesson-7-2-anne-ch2.html',
              '7.3':'lesson-7-3-anne-ch3-4.html', '7.4':'lesson-7-4-anne-ch5.html' };
  return MAP[week + '.' + day] || null;
}

function markTabs(tabIds) {
  var prog = Sparkle.get('oao.g4ela.progress', {});
  var me = prog[LID] || { tabs: [], done: false, doneAt: null };
  tabIds.forEach(function (t) { if (me.tabs.indexOf(t) === -1) me.tabs.push(t); });
  prog[LID] = me; Sparkle.set('oao.g4ela.progress', prog);
}
function markDone() {
  var prog = Sparkle.get('oao.g4ela.progress', {});
  var me = prog[LID] || { tabs: [], done: false, doneAt: null };
  if (me.done) return false;
  me.done = true; me.doneAt = new Date().toISOString();
  prog[LID] = me; Sparkle.set('oao.g4ela.progress', prog);

  var book = COURSE.filter(function (b) { return b.id === LESSON.book; })[0];
  if (book && LESSON.week === book.weeks[1] && LESSON.day === 4) {
    var all = true;
    for (var w = book.weeks[0]; w <= book.weeks[1]; w++) {
      var k = w + '.4'; if (!(prog[k] && prog[k].done)) all = false;
    }
    if (all) {
      var books = Sparkle.get('oao.g4ela.books', {});
      books[book.id] = { done: true, doneAt: new Date().toISOString() };
      Sparkle.set('oao.g4ela.books', books);
      document.dispatchEvent(new CustomEvent('oao:bookfinished', { detail: { book: book } }));
      return true;
    }
  }
  return false;
}

function buildTrack() {
  var wrap = document.querySelector('.progress-wrap'); if (!wrap) return;
  var box = document.createElement('div');
  box.className = 'spk-track'; box.id = 'spkTrack';
  box.innerHTML =
    '<div class="spk-track-row"><span class="spk-track-label">This week</span><span id="spkDots"></span>' +
    '<button type="button" class="spk-track-jump" id="spkJump">See the Reading Road \u2192</button></div>';
  wrap.parentNode.insertBefore(box, wrap.nextSibling);
  document.getElementById('spkJump').onclick = function () {
    if (window.switchTab) window.switchTab('reading');
    setTimeout(function () {
      var c = document.querySelector('.spk-journey');
      if (c) c.scrollIntoView({ behavior: REDUCED ? 'auto' : 'smooth', block: 'center' });
    }, 320);
  };
  drawDots();
}

function drawDots() {
  var host = document.getElementById('spkDots'); if (!host) return;
  var prog = Sparkle.get('oao.g4ela.progress', {});
  var items = [['1','7.1'],['2','7.2'],['3','7.3'],['4','7.4'],['fluency','Read Aloud']];
  host.innerHTML = '';
  items.forEach(function (it) {
    var day = it[0] === 'fluency' ? 'fluency' : parseInt(it[0], 10);
    var key = LESSON.week + '.' + (day === 'fluency' ? 'fluency' : day);
    var isMe = String(LESSON.day) === String(day);
    var done = prog[key] && prog[key].done;
    var d = document.createElement('span');
    d.className = 'spk-dot' + (isMe ? ' current' + (REDUCED ? '' : ' pulse') : (done ? ' done' : ''));
    d.textContent = it[1];
    var href = lessonHref(LESSON.week, day);
    if (!isMe && done && href) { d.onclick = function () { window.location.href = href; }; }
    if (isMe) d.title = 'You are here';
    host.appendChild(d);
  });
}

/* ── world palettes + vignettes (§2.10 atlas) ───────────────── */
/* ══════════════════════════════════════════════════════════════
   §2.2 / §2.3  THE READING JOURNEY
   One continuous illustrated map. A single winding road of 32
   week-spaces runs through eight regions that blend into each
   other; the student's owl stands on this week's space. The
   shelf lives in the same card, below the map.
   Lives on the Reading tab. The week's four dots stay up top.
   ══════════════════════════════════════════════════════════════ */

/* region identity: the wash of color the land takes on, and the
   ink the landmark and label are drawn in */
var REGION = {
  frisby:  { wash:'#BCDCA2', ink:'#4A7C2E', label:'Fitzgibbon Farm' },
  writing: { wash:'#F3E0B6', ink:'#A87C24', label:"Writer's Workshop" },
  anne:    { wash:'#F2C4A8', ink:'#B5543A', label:'Green Gables' },
  bridge:  { wash:'#BAD0DF', ink:'#3D5F7A', label:'The Danish Coast' },
  nts:     { wash:'#AEB8D8', ink:'#333F6B', label:'Copenhagen' },
  ft:      { wash:'#99A6C6', ink:'#2A3A63', label:'North to Canada' },
  pc:      { wash:'#A8CEAA', ink:'#2F6B4B', label:'Narnia' },
  synth:   { wash:'#F1D79C', ink:'#A8801F', label:"Journey's End" }
};

/* Landmarks sit on the land beside the road. Drawn around (0,0)
   with the ground at y = 0, roughly 70 wide. */
var LANDMARK = {
  frisby: function () {
    return '<path d="M-34 0 L-34 -22 L-22 -32 L-10 -22 L-10 0 Z" fill="#B5543A"/>' +
      '<path d="M-37 -21 L-22 -34 L-7 -21 Z" fill="#8E3F2C"/>' +
      '<rect x="-26" y="-14" width="8" height="10" fill="#F6E3C8"/>' +
      '<rect x="-4" y="-18" width="10" height="18" rx="2" fill="#C9B79A"/><ellipse cx="1" cy="-18" rx="5" ry="3" fill="#A8977C"/>' +
      '<rect x="20" y="-14" width="4" height="14" fill="#7A5A3A"/><circle cx="22" cy="-20" r="11" fill="#5E9440"/><circle cx="14" cy="-16" r="7" fill="#6EA84C"/>';
  },
  writing: function () {
    return '<rect x="-30" y="-4" width="60" height="5" rx="1" fill="#B98B52"/>' +
      '<rect x="-24" y="-24" width="30" height="21" rx="1.5" fill="#FFFDF4" stroke="#DCC79E" stroke-width="1.2" transform="rotate(-5 -9 -13)"/>' +
      '<path d="M-19 -18 h20 M-19 -13 h20 M-19 -8 h12" stroke="#D3C3A2" stroke-width="1.2" transform="rotate(-5 -9 -13)"/>' +
      '<rect x="10" y="-14" width="13" height="11" rx="2" fill="#2A3558"/><ellipse cx="16.5" cy="-14" rx="6.5" ry="2.4" fill="#1B2440"/>' +
      '<path d="M20 -13 C27 -25 34 -35 40 -40 C36 -29 30 -18 24 -8 Z" fill="#FFFDF4" stroke="#D9C69E" stroke-width="1"/>';
  },
  anne: function () {
    return '<path d="M-14 0 V-24 L2 -37 L18 -24 V0 Z" fill="#FFFDF4" stroke="#DCCFB8" stroke-width="1.1"/>' +
      '<path d="M-17 -23 L2 -39 L21 -23 Z" fill="#3E7A4E"/>' +
      '<path d="M-6 0 V-13 L2 -20 L10 -13 V0 Z" fill="#FFFDF4"/><path d="M-9 -12 L2 -21 L13 -12 Z" fill="#3E7A4E"/>' +
      '<rect x="-1" y="-9" width="7" height="9" fill="#6A8FA8"/>' +
      '<rect x="-34" y="-16" width="4" height="16" fill="#7A5A3A"/>' +
      '<circle cx="-32" cy="-22" r="11" fill="#F2C3D0"/><circle cx="-40" cy="-18" r="7" fill="#F7D3DC"/><circle cx="-24" cy="-19" r="6" fill="#EFB9C8"/>';
  },
  bridge: function () {
    return '<ellipse cx="0" cy="-1" rx="40" ry="6" fill="#7FA3BC" opacity=".75"/>' +
      '<path d="M-20 -4 L22 -4 L15 -13 L-13 -13 Z" fill="#3B4F63"/>' +
      '<rect x="-2" y="-42" width="2.4" height="29" fill="#2C3B4B"/>' +
      '<path d="M1 -40 L1 -14 L22 -14 Z" fill="#FFFDF4"/>' +
      '<path d="M-2.4 -38 L-2.4 -16 L-18 -16 Z" fill="#DCE7EE"/>';
  },
  nts: function () {
    return '<path d="M-38 0 V-22 h12 l6 -8 6 8 h10 V-30 h8 V0 Z" fill="#26325A"/>' +
      '<path d="M2 0 V-30 h10 l6 -9 6 9 h10 V0 Z" fill="#1D2748"/>' +
      '<rect x="-32" y="-16" width="5" height="6" fill="#F0C64B" opacity=".85"/>' +
      '<rect x="-12" y="-20" width="5" height="6" fill="#F0C64B" opacity=".7"/>' +
      '<rect x="12" y="-18" width="5" height="6" fill="#F0C64B" opacity=".8"/>' +
      '<path d="M30 -44 l2.4 5.8 6.2 .4 -4.8 4.1 1.5 6.1 -5.3 -3.3 -5.3 3.3 1.5 -6.1 -4.8 -4.1 6.2 -.4 Z" fill="#F0C64B"/>';
  },
  ft: function () {
    return '<path d="M-6 0 L8 -34 L22 0 Z" fill="#1B2A4A"/><path d="M14 0 L24 -24 L34 0 Z" fill="#22355A"/>' +
      '<path d="M-38 0 L-26 -26 L-14 0 Z" fill="#1B2A4A"/>' +
      '<path d="M-30 0 L-22 -20 L-14 0" stroke="#8A9DC6" stroke-width="1.8" fill="none"/>' +
      '<path d="M-29 -4 h14 M-27 -9 h11 M-25 -14 h7" stroke="#8A9DC6" stroke-width="1.6" stroke-linecap="round"/>' +
      '<circle cx="4" cy="-14" r="11" fill="#F3D27A" opacity=".18"/>' +
      '<path d="M1 -22 h6" stroke="#C8A85A" stroke-width="1.3"/>' +
      '<path d="M0 -20 h8 l-1 9 h-6 Z" fill="#F7DE95"/>' +
      '<path d="M0 -20 q4 -6 8 0" stroke="#C8A85A" stroke-width="1.2" fill="none"/>';
  },
  pc: function () {
    return '<path d="M-42 0 V-26 h8 v26 Z M-24 0 V-34 h8 v34 Z" fill="#D2C9B1"/>' +
      '<path d="M-34 -24 q9 -11 15 -3" stroke="#D2C9B1" stroke-width="5.5" fill="none"/>' +
      '<path d="M22 0 L30 -30 L38 0 Z" fill="#1F4A30"/><path d="M34 0 L40 -20 L46 0 Z" fill="#265838"/>' +
      '<circle cx="-1" cy="-16" r="15" fill="#C9862F"/>' +
      '<path d="M-1 -31 l3 4 4 -2.4 -.8 4.8 4.8 .8 -3.2 4 4 3.2 -4.8 1.6 1.6 4.8 -4.8 -.8 -.8 4.8 -4 -3.2 -3.2 4 -3.2 -4 -4 3.2 -.8 -4.8 -4.8 .8 1.6 -4.8 -4.8 -1.6 4 -3.2 -3.2 -4 4.8 -.8 -.8 -4.8 4 2.4 Z" fill="#B5731F" opacity=".85"/>' +
      '<circle cx="-1" cy="-16" r="10" fill="#EBC077"/>' +
      '<circle cx="-7.5" cy="-22" r="3.2" fill="#D9A659"/><circle cx="5.5" cy="-22" r="3.2" fill="#D9A659"/>' +
      '<circle cx="-4.2" cy="-18" r="1.4" fill="#3A2A14"/><circle cx="2.2" cy="-18" r="1.4" fill="#3A2A14"/>' +
      '<path d="M-1 -14.5 l-2.6 2 h5.2 Z" fill="#8A5A22"/>' +
      '<path d="M-3.8 -10.5 q2.8 2.4 5.6 0" stroke="#8A5A22" stroke-width="1.2" fill="none" stroke-linecap="round"/>';
  },
  synth: function () {
    return '<path d="M0 -8 Q-18 -16 -34 -12 L-34 -34 Q-18 -38 0 -30 Z" fill="#FFFDF4" stroke="#D8C49A" stroke-width="1.2"/>' +
      '<path d="M0 -8 Q18 -16 34 -12 L34 -34 Q18 -38 0 -30 Z" fill="#FFFDF4" stroke="#D8C49A" stroke-width="1.2"/>' +
      '<path d="M0 -30 V-8" stroke="#C7922C" stroke-width="1.4"/>' +
      '<path d="M-27 -29 h18 M-27 -24 h18 M-27 -19 h12 M9 -29 h18 M9 -24 h18 M9 -19 h12" stroke="#DED0B2" stroke-width="1.3"/>' +
      '<path d="M-38 -26 q-11 10 -6 24 M38 -26 q11 10 6 24" stroke="#6E9450" stroke-width="2.2" fill="none"/>' +
      '<ellipse cx="-44" cy="-22" rx="4.4" ry="2.3" fill="#7DA85C" transform="rotate(-35 -44 -22)"/>' +
      '<ellipse cx="-46" cy="-13" rx="4.4" ry="2.3" fill="#7DA85C" transform="rotate(-8 -46 -13)"/>' +
      '<ellipse cx="-44" cy="-4" rx="4.4" ry="2.3" fill="#7DA85C" transform="rotate(20 -44 -4)"/>' +
      '<ellipse cx="44" cy="-22" rx="4.4" ry="2.3" fill="#7DA85C" transform="rotate(35 44 -22)"/>' +
      '<ellipse cx="46" cy="-13" rx="4.4" ry="2.3" fill="#7DA85C" transform="rotate(8 46 -13)"/>' +
      '<ellipse cx="44" cy="-4" rx="4.4" ry="2.3" fill="#7DA85C" transform="rotate(-20 44 -4)"/>';
  }
};

/* ── the painted board ──────────────────────────────────────
   Bethany's artwork is 1448x1086 and carries its own title, its own
   six worlds and its own forty spaces. Nothing here draws a map; it
   only lights up what the painting already shows. The coordinates
   were measured off the file (connected-component centroids), not
   eyeballed, so a repaint means re-measuring, not nudging.
   Forty spaces, thirty-two weeks: a week claims its space by
   proportion, which keeps Start at week 1 and Finish at week 32
   without leaving gaps in the middle.                            */
var BOARD_W = 1448, BOARD_H = 1086, BOARD_R = 23;
/* the painted vignettes, measured off the artwork. A world the
   student has not reached yet is desaturated and veiled, exactly the
   way an unread book lies flat on the shelf: the board then shows the
   year filling with colour as they go. */
var BOARD_WORLDS = [
  { id:'frisby', x:112, y:140, w:412, h:258 },
  { id:'anne',   x:544, y:156, w:428, h:252 },
  { id:'nts',    x:996, y:156, w:446, h:290 },
  { id:'ft',     x: 84, y:652, w:438, h:288 },
  { id:'pc',     x:512, y:682, w:406, h:270 },
  { id:'synth',  x:950, y:686, w:494, h:266 }
];
/* a world is 'reached' once this lesson's week is inside it or past
   it, or once storage says any of its weeks has been worked */
function worldReached(prog, id) {
  var b = COURSE.filter(function (c) { return c.id === id; })[0];
  if (!b) return true;
  if (LESSON.week >= b.weeks[0]) return true;
  for (var w = b.weeks[0]; w <= b.weeks[1]; w++) {
    for (var d = 1; d <= 4; d++) { var k = prog[w + '.' + d]; if (k && (k.done || (k.tabs && k.tabs.length))) return true; }
  }
  return false;
}
var BOARD_SPACES = [
  [118,373,'#C7922C'],
  [220,407,'#C7922C'],
  [329,433,'#C7922C'],
  [432,435,'#C7922C'],
  [536,420,'#6E8F3A'],
  [642,418,'#6E8F3A'],
  [746,434,'#6E8F3A'],
  [850,447,'#6E8F3A'],
  [955,438,'#6E8F3A'],
  [1062,434,'#4A6E8F'],
  [1165,450,'#4A6E8F'],
  [1267,468,'#4A6E8F'],
  [1352,510,'#4A6E8F'],
  [1369,594,'#4A6E8F'],
  [1270,647,'#4A6E8F'],
  [1153,652,'#4A6E8F'],
  [1040,651,'#4A6E8F'],
  [923,661,'#7A5C86'],
  [807,662,'#7A5C86'],
  [692,660,'#7A5C86'],
  [572,656,'#7A5C86'],
  [463,645,'#C0623F'],
  [356,619,'#C0623F'],
  [254,596,'#C0623F'],
  [156,605,'#C0623F'],
  [75,660,'#C0623F'],
  [60,747,'#C0623F'],
  [79,847,'#C0623F'],
  [146,909,'#C0623F'],
  [242,948,'#C0623F'],
  [347,965,'#C0623F'],
  [447,966,'#7A5C86'],
  [561,963,'#7A5C86'],
  [679,960,'#7A5C86'],
  [792,965,'#7A5C86'],
  [901,980,'#C7922C'],
  [1006,989,'#C7922C'],
  [1111,988,'#C7922C'],
  [1204,980,'#C7922C'],
  [1293,958,'#C7922C']
];
var BOARD_N = BOARD_SPACES.length;
/* ── where the owl stands ───────────────────────────────────────
   One step per LESSON DAY, not per week: 32 weeks x 4 lessons = 128
   days across 40 painted spaces, so the owl moves roughly one space
   every three lessons and the board lasts the whole year.

   The spaces are not divided evenly, because the artist placed the
   six vignettes for composition rather than in curriculum order. Each
   book is anchored to the stretch of path that actually runs past its
   own picture, so a student reading Anne stands under the green
   gables for all eight of those weeks. Freedom Train gets the long
   middle sweep and the left-hand loop, which suits a book about a
   journey; Prince Caspian gets the four spaces beneath its own tree.
   Change the artwork and these anchors have to be re-measured with
   it — they describe the painting, not the curriculum. */
var BOARD_LEGS = [
  { id:'frisby', weeks:[1,  6], spaces:[ 1,  4] },   /* Frisby + the wk-6 workshop */
  { id:'anne',   weeks:[7, 14], spaces:[ 5,  9] },
  { id:'nts',    weeks:[15,19], spaces:[10, 17] },   /* incl. the wk-15 bridge */
  { id:'ft',     weeks:[20,25], spaces:[18, 31] },
  { id:'pc',     weeks:[26,30], spaces:[32, 35] },
  { id:'synth',  weeks:[31,32], spaces:[36, 40] }
];
function legOfWeek(w) {
  for (var i = 0; i < BOARD_LEGS.length; i++) {
    if (w >= BOARD_LEGS[i].weeks[0] && w <= BOARD_LEGS[i].weeks[1]) return BOARD_LEGS[i];
  }
  return BOARD_LEGS[w < 1 ? 0 : BOARD_LEGS.length - 1];
}
/* the fluency page is not a numbered lesson day; it sits with day 4 */
function dayNum(d) { var n = parseInt(d, 10); return (n >= 1 && n <= 4) ? n : 4; }

/* lesson (week, day) -> space 1..40 */
function spaceOfLesson(w, d) {
  var leg = legOfWeek(w);
  var days = (leg.weeks[1] - leg.weeks[0] + 1) * 4;
  var idx  = (w - leg.weeks[0]) * 4 + dayNum(d);            /* 1..days */
  var n    = leg.spaces[1] - leg.spaces[0] + 1;
  var sp   = leg.spaces[0] + Math.floor((idx - 1) * n / days);
  return Math.max(leg.spaces[0], Math.min(leg.spaces[1], sp));
}
/* how many lesson days are behind this one, out of 128 */
function lessonIndex(w, d) { return (w - 1) * 4 + dayNum(d); }

/* space -> the week it belongs to, for the tooltip and the seal lookup */
function weekOfSpace(i) {
  for (var k = 0; k < BOARD_LEGS.length; k++) {
    var leg = BOARD_LEGS[k];
    if (i < leg.spaces[0] || i > leg.spaces[1]) continue;
    var n = leg.spaces[1] - leg.spaces[0] + 1;
    var days = (leg.weeks[1] - leg.weeks[0] + 1) * 4;
    var idx = Math.floor((i - leg.spaces[0]) * days / n);    /* 0-based day */
    return Math.min(leg.weeks[1], leg.weeks[0] + Math.floor(idx / 4));
  }
  return i <= 1 ? 1 : 32;
}

/* the one road, bottom-left to top-left, four passes */
var ROAD_D = 'M 58 600 C 200 580, 320 620, 460 598 C 600 576, 720 615, 812 591 ' +
             'C 868 577, 872 517, 812 497 C 700 475, 560 513, 420 489 ' +
             'C 300 469, 175 503, 104 479 C 46 460, 44 399, 104 377 ' +
             'C 220 357, 360 393, 500 371 C 620 353, 742 383, 816 361 ' +
             'C 872 345, 876 285, 816 263 C 700 241, 560 275, 430 253 ' +
             'C 344 239, 250 259, 176 241';

/* which region a given week belongs to */
function regionOfWeek(w) {
  for (var i = 0; i < COURSE.length; i++) {
    if (w >= COURSE[i].weeks[0] && w <= COURSE[i].weeks[1]) return COURSE[i];
  }
  return COURSE[0];
}
/* A student opening Lesson 7.1 has already read Mrs. Frisby — they
   just did it before any of this existed. So a week earlier than the
   one this lesson belongs to counts as travelled, whether or not
   local storage happens to remember it. Storage can only ever add to
   that picture, never take it away. */
function weekDone(prog, w) {
  if (w < LESSON.week) return 'done';
  var any = false, all = true;
  for (var d = 1; d <= 4; d++) {
    var k = w + '.' + d;
    if (prog[k] && prog[k].done) any = true; else all = false;
  }
  return all ? 'done' : (any ? 'started' : 'ahead');
}
/* likewise: a book whose last week is behind us has been read */
function bookRead(books, b) {
  if (books[b.id] && books[b.id].done) return true;
  return b.weeks[1] < LESSON.week;
}

/* ── the card, on the Reading tab ──────────────────────────── */
/* §2.10 chapter plate — under the quote banner, and on the left page
   of the open book. Printed with multiply so the illustration's own
   paper melts into the page instead of sitting in a white box. */
/* §2.10b the illuminated chapter numeral. A manuscript initial, set
   above the epigraph the way a chapter opens in a well-made children's
   book: numeral, then the line, then the picture. Purely decorative —
   the chapter is already named in the lesson header — so it is hidden
   from assistive tech. */
var ROMAN = [[10,'X'],[9,'IX'],[5,'V'],[4,'IV'],[1,'I']];
function roman(n) {
  var out = '';
  for (var i = 0; i < ROMAN.length; i++) { while (n >= ROMAN[i][0]) { out += ROMAN[i][1]; n -= ROMAN[i][0]; } }
  return out;
}
var WORDNUM = ['', 'ONE', 'TWO', 'THREE', 'FOUR', 'FIVE', 'SIX', 'SEVEN', 'EIGHT',
               'NINE', 'TEN', 'ELEVEN', 'TWELVE'];
function chapterNumbers() {
  var m = String(LESSON.chapters || '').match(/\d+/g);
  return m ? m.map(Number) : [];
}
function buildNumeral() {
  var quote = document.querySelector('.quote-strip'); if (!quote) return;
  var ns = chapterNumbers(); if (!ns.length) return;
  var n = ns[0];
  var rn = roman(n) || String(n);
  var size = rn.length > 2 ? 30 : 40;

  var fig = document.createElement('div');
  fig.className = 'spk-numeral';
  fig.setAttribute('aria-hidden', 'true');
  fig.innerHTML =
    '<svg viewBox="0 0 96 96" width="76" height="76">' +
      '<rect x="8" y="8" width="80" height="80" rx="4" fill="#0E1C42"/>' +
      '<rect x="12.5" y="12.5" width="71" height="71" rx="2.5" fill="none" stroke="#FFFDF7" stroke-width="1.1" opacity=".85"/>' +
      /* corner vines */
      '<path d="M16 34 q0 -18 18 -18 M80 62 q0 18 -18 18" stroke="#C7922C" stroke-width="1.6" fill="none" stroke-linecap="round"/>' +
      '<path d="M18 30 q7 -4 9 -11 q4 7 11 8 q-8 2 -10 10 q-3 -6 -10 -7 Z" fill="#C7922C" opacity=".9"/>' +
      '<path d="M78 66 q-7 4 -9 11 q-4 -7 -11 -8 q8 -2 10 -10 q3 6 10 7 Z" fill="#C7922C" opacity=".9"/>' +
      '<circle cx="74" cy="22" r="2.6" fill="#8FAE6A"/><circle cx="22" cy="74" r="2.6" fill="#8FAE6A"/>' +
      '<text x="48" y="' + (48 + size * 0.36) + '" font-size="' + size + '" text-anchor="middle" ' +
        'font-family="Lora,Georgia,serif" font-weight="700" fill="#E9C46A" letter-spacing="1">' + rn + '</text>' +
    '</svg>' +
    '<div class="spk-numeral-word">CHAPTER ' + (WORDNUM[n] || n) + '</div>';
  quote.parentNode.insertBefore(fig, quote);
}

function buildPlate() {
  /* built from the lesson's own book + chapters; hidden if absent */
  var src = plateSrc(); if (!src) return;

  var quote = document.querySelector('.quote-strip');
  if (quote) {
    var plate = document.createElement('figure');
    plate.className = 'spk-plate';
    var img = document.createElement('img');
    img.src = src; img.alt = 'Chapter illustration'; img.loading = 'lazy';
    img.onerror = function () { plate.remove(); };
    plate.appendChild(img);
    quote.parentNode.insertBefore(plate, quote.nextSibling);
  }

  /* the open book gets the same picture on its left page */
  var left = document.querySelector('.open-book-left');
  if (left) {
    var deco = left.querySelector('.open-book-left-deco');
    if (deco) deco.style.display = 'none';
    var bi = document.createElement('img');
    bi.className = 'spk-book-plate'; bi.src = src; bi.alt = ''; bi.loading = 'lazy';
    bi.onerror = function () { bi.remove(); if (deco) deco.style.display = ''; };
    left.appendChild(bi);
  }
}

function buildJourney() {
  var panel = document.getElementById('tab-reading'); if (!panel) return;
  /* the old per-chapter tracker is retired — the Reading Road covers the
     same ground for the whole year, and two trackers on one tab is one
     too many */
  var after = panel.querySelector('.tracker-card');
  if (after) { after.remove(); after = null; }
  var card = document.createElement('div');
  card.className = 'spk-card spk-journey';
  /* The map and the shelf are a keepsake, not a task — lovely to visit,
     in the way every day. So the card folds, and remembers whether the
     student left it open. Closed is the default: the road is still one
     click away, and the chapter is the reason they came. */
  card.innerHTML =
    '<button type="button" class="spk-card-head spk-fold" id="spkRoadFold" aria-expanded="false" aria-controls="spkRoadBody">' +
      '<div class="spk-card-num">✦</div><div>' +
      '<div class="spk-card-title">The Reading Road</div>' +
      '<div class="spk-card-sub">Thirty-two weeks, one road, six worlds — and the shelf you fill as you go</div>' +
      '</div><span class="spk-fold-chev" aria-hidden="true"></span>' +
    '</button>' +
    '<div class="spk-card-body spk-journey-body" id="spkRoadBody" hidden>' +
      '<div class="spk-map-wrap"><svg class="spk-map" id="spkMap" viewBox="0 0 900 660"></svg></div>' +
      '<div class="spk-here" id="spkHere"></div>' +
      '<div class="spk-shelf-head">Your shelf</div>' +
      /* the case around the books. Purely decorative furniture — the
         books themselves are still the only thing in #spkShelf, so
         drawShelf() is untouched and nothing here is announced. */
      '<div class="spk-bookcase" aria-hidden="false">' +
        '<div class="spk-case-crown" aria-hidden="true">' +
          '<span class="spk-case-medallion"></span></div>' +
        '<span class="spk-case-dentil" aria-hidden="true"></span>' +
        '<div class="spk-case-body">' +
          '<span class="spk-case-stile left" aria-hidden="true"></span>' +
          '<div class="spk-shelf" id="spkShelf"></div>' +
          '<span class="spk-case-stile right" aria-hidden="true"></span>' +
          '<span class="spk-case-board" aria-hidden="true"></span>' +
        '</div>' +
        '<div class="spk-case-plinth" aria-hidden="true">' +
          '<span class="spk-case-foot left"></span>' +
          '<span class="spk-case-foot right"></span></div>' +
      '</div>' +
      '<div class="spk-shelf-note" id="spkShelfNote">A book stands up once you have read all of it.</div>' +
    '</div>';
  if (after && after.nextSibling) after.parentNode.insertBefore(card, after.nextSibling);
  else panel.insertBefore(card, panel.firstChild);
  var fold = document.getElementById('spkRoadFold');
  var body = document.getElementById('spkRoadBody');
  var openRoad = Sparkle.get('oao.g4ela.roadOpen', false) === true;
  function setFold(open) {
    body.hidden = !open;
    fold.setAttribute('aria-expanded', open ? 'true' : 'false');
    card.classList.toggle('spk-open-road', open);
    Sparkle.set('oao.g4ela.roadOpen', open);
    /* the map measures itself off the DOM, so it can only be drawn
       once the body is actually on the page */
    if (open) { try { drawMap(); drawShelf(); } catch (e) {} }
  }
  fold.onclick = function () { setFold(body.hidden); };
  setFold(openRoad);
}

/* ── §2.2 the painted board, lit up ─────────────────────────────
   The picture is the base layer. On top of it go exactly three
   things: a cream veil over the road still ahead, an ink fill on
   the spaces already travelled, and the owl standing on today's
   space. If the art ever fails to load the generated road below
   is still there to fall back on. */
function drawBoardMap(svg) {
  var prog  = Sparkle.get('oao.g4ela.progress', {});
  var seals = Sparkle.get('oao.g4ela.scholar', {});
  var p     = profile();
  var art   = artURL(ART.board.src);
  var cur   = spaceOfLesson(LESSON.week, LESSON.day);

  svg.setAttribute('viewBox', '0 0 ' + BOARD_W + ' ' + BOARD_H);
  svg.classList.add('spk-map-board');

  var s = '<defs><filter id="spkUnread" color-interpolation-filters="sRGB">' +
          '<feColorMatrix type="saturate" values="0.10"/></filter>';
  /* a blurred mask rather than a hard clip: a rectangle with visible
     corners would read as a UI panel dropped on the painting. Feathered,
     it reads as light that has not reached that part of the board yet. */
  s += '<filter id="spkSoftEdge" x="-20%" y="-20%" width="140%" height="140%">' +
       '<feGaussianBlur stdDeviation="17"/></filter>';
  BOARD_WORLDS.forEach(function (v) {
    s += '<mask id="spkWorldMask_' + v.id + '" maskUnits="userSpaceOnUse" ' +
         'x="0" y="0" width="' + BOARD_W + '" height="' + BOARD_H + '">' +
         '<rect x="' + (v.x + 6) + '" y="' + (v.y + 6) + '" width="' + (v.w - 12) +
         '" height="' + (v.h - 12) + '" rx="26" fill="#fff" filter="url(#spkSoftEdge)"/></mask>';
  });
  s += '</defs>';
  s += '<image id="spkBoardImg" href="' + art + '" x="0" y="0" width="' + BOARD_W + '" height="' + BOARD_H + '"/>';

  /* worlds not yet reached lie quiet — colour drained, paper veiled */
  BOARD_WORLDS.forEach(function (v) {
    if (worldReached(prog, v.id)) return;
    s += '<g class="spk-world-unread" data-world="' + v.id + '" mask="url(#spkWorldMask_' + v.id + ')">' +
         '<use href="#spkBoardImg" filter="url(#spkUnread)"/>' +
         '<rect x="' + v.x + '" y="' + v.y + '" width="' + v.w + '" height="' + v.h +
         '" fill="#FBF3DF" opacity=".40"/></g>';
  });

  /* the student's name, hand-written into the open field the artist
     left in the middle of the board. Second place the name appears. */
  if (p && p.name) {
    s += '<text x="724" y="543" font-size="30" text-anchor="middle" ' +
         'font-family="Lora,Georgia,serif" font-style="italic" fill="#8B6914" opacity=".85">' +
         esc(p.name) + '’s journey</text>';
  }

  for (var i = 1; i <= BOARD_N; i++) {
    var sp = BOARD_SPACES[i - 1], x = sp[0], y = sp[1], ink = sp[2];
    var w  = weekOfSpace(i);
    var st = i < cur ? 'done' : (i === cur ? 'here' : weekDone(prog, w));
    s += '<g class="spk-space spk-' + st + '" data-week="' + w + '" data-space="' + i + '">' +
         '<title>Week ' + w + ' · ' + REGION[regionOfWeek(w).id].label + '</title>';

    var sealed = !!seals['w' + w];
    var sealArt = artURL((ART.seals || {}).mark) || artURL((ART.seals || {}).scholar);
    if (st === 'done' && sealed && sealArt) {
      /* a week that earned the Scholar's mark wears the seal instead of
         the tick — the higher honour replaces the lower one, and it sits
         inside the space's own footprint so it can never collide with
         the owl standing on today's space */
      s += '<circle cx="' + x + '" cy="' + y + '" r="' + BOARD_R + '" fill="' + ink + '" opacity=".88"/>';
    } else if (st === 'done') {
      s += '<circle cx="' + x + '" cy="' + y + '" r="' + BOARD_R + '" fill="' + ink + '" opacity=".88"/>' +
           '<path d="M' + (x - 9) + ' ' + y + ' l6 7 12 -14" stroke="#FFF8E9" stroke-width="4" ' +
           'fill="none" stroke-linecap="round" stroke-linejoin="round"/>';
    } else if (st === 'here') {
      s += '<circle cx="' + x + '" cy="' + y + '" r="' + (BOARD_R + 6) + '" fill="none" ' +
           'stroke="#C7922C" stroke-width="5"/>';
    } else {
      /* still ahead: veil it back so the travelled road reads first */
      s += '<circle cx="' + x + '" cy="' + y + '" r="' + (BOARD_R + 1) + '" fill="#FBF3DF" opacity=".5"/>';
      if (st === 'started') {
        s += '<circle cx="' + x + '" cy="' + y + '" r="8" fill="' + ink + '" opacity=".55"/>';
      }
    }
    if (sealed) {                               /* the Scholar's mark for that week */
      if (sealArt) {
        s += '<image href="' + sealArt + '" x="' + (x - 27) + '" y="' + (y - 27) +
             '" width="54" height="54" preserveAspectRatio="xMidYMid meet"/>';
      } else {
        s += '<path d="M' + (x - 26) + ' ' + (y + 4) + ' q-7 -19 7 -30 M' +
             (x + 26) + ' ' + (y + 4) + ' q7 -19 -7 -30" stroke="#C7922C" stroke-width="4" ' +
             'fill="none" stroke-linecap="round"/>';
      }
    }
    s += '</g>';
  }

  /* the owl stands on today's space */
  var me = BOARD_SPACES[cur - 1], OW = 150;
  /* the owl stands clear of the ring rather than on top of it, so the
     gold marker still reads as the space the student is on */
  var oy = me[1] - OW - 26;
  s += '<g transform="translate(' + (me[0] - OW / 2) + ',' + oy + ')">' +
       owlMarkSVG(p && p.owl ? p.owl : defaultCompanion(), OW) + '</g>';
  var label = 'LESSON ' + LESSON.week + '.' + dayNum(LESSON.day);
  var bw = 20 + label.length * 10.5;
  var bx = me[0] < BOARD_W - 200 ? me[0] + 46 : me[0] - 46 - bw;
  s += '<rect x="' + bx + '" y="' + (me[1] - 17) + '" width="' + bw + '" height="34" rx="17" fill="#C7922C"/>' +
       '<text x="' + (bx + bw / 2) + '" y="' + (me[1] + 7) + '" font-size="18" text-anchor="middle" ' +
       'font-family="Nunito,sans-serif" font-weight="800" fill="#FFF8E9">' + label + '</text>';

  svg.innerHTML = s;

  var here = document.getElementById('spkHere');
  if (here) {
    var behind = lessonIndex(LESSON.week, LESSON.day) - 1;
    here.textContent = 'Lesson ' + LESSON.week + '.' + dayNum(LESSON.day) + ' \u2014 week ' +
      LESSON.week + ' of 32, in ' + REGION[LESSON.book].label + '. ' +
      behind + (behind === 1 ? ' lesson' : ' lessons') + ' behind you, of 128.';
  }
}

function drawMap() {
  var svg = document.getElementById('spkMap'); if (!svg) return;
  if (artURL((ART.board || {}).src)) { drawBoardMap(svg); return; }
  var prog = Sparkle.get('oao.g4ela.progress', {});
  var books = Sparkle.get('oao.g4ela.books', {});
  var seals = Sparkle.get('oao.g4ela.scholar', {});
  var p = profile();

  /* 1. the land: soft washes that bleed into one another */
  var defs = '<radialGradient id="spkVig" cx="50%" cy="50%" r="62%">' +
    '<stop offset="60%" stop-color="#FFF8E9" stop-opacity="0"/>' +
    '<stop offset="100%" stop-color="#E8D6AE" stop-opacity=".55"/></radialGradient>';
  var s = '<rect width="900" height="660" fill="#FCF3DF"/>';

  /* measure the road so everything can be placed along it */
  svg.innerHTML = '<path id="spkRoadMeasure" d="' + ROAD_D + '" fill="none"/>';
  var road = svg.querySelector('#spkRoadMeasure');
  var L = road.getTotalLength();
  function at(t) { var pt = road.getPointAtLength(Math.max(0, Math.min(L, t * L))); return { x: pt.x, y: pt.y }; }

  /* week w (1..32) sits at this fraction along the road */
  function weekT(w) { return (w - 0.5) / 32; }

  COURSE.forEach(function (b, i) {
    var r = REGION[b.id];
    var mid = at(weekT((b.weeks[0] + b.weeks[1]) / 2));
    var span = (b.weeks[1] - b.weeks[0] + 1);
    var rad = 92 + span * 9;
    var terrain = artURL((ART.worlds[b.id] || {}).terrain);
    /* one feather mask per region — this is what keeps eight pieces
       of art reading as a single continuous land */
    defs += '<radialGradient id="spkFeather' + i + '" cx="50%" cy="50%" r="50%">' +
            '<stop offset="0" stop-color="#fff" stop-opacity="1"/>' +
            '<stop offset="58%" stop-color="#fff" stop-opacity=".92"/>' +
            '<stop offset="100%" stop-color="#fff" stop-opacity="0"/></radialGradient>' +
            '<mask id="spkMask' + i + '"><circle cx="' + mid.x.toFixed(1) + '" cy="' + mid.y.toFixed(1) +
            '" r="' + rad + '" fill="url(#spkFeather' + i + ')"/></mask>';
    if (terrain) {
      s += '<g mask="url(#spkMask' + i + ')"><image href="' + terrain + '" x="' + (mid.x - rad).toFixed(1) +
           '" y="' + (mid.y - rad).toFixed(1) + '" width="' + (rad * 2) + '" height="' + (rad * 2) +
           '" preserveAspectRatio="xMidYMid slice"/></g>';
    } else {
      defs += '<radialGradient id="spkW' + b.id + '" cx="50%" cy="50%" r="50%">' +
              '<stop offset="0" stop-color="' + r.wash + '" stop-opacity=".92"/>' +
              '<stop offset="65%" stop-color="' + r.wash + '" stop-opacity=".45"/>' +
              '<stop offset="100%" stop-color="' + r.wash + '" stop-opacity="0"/></radialGradient>';
      s += '<circle cx="' + mid.x.toFixed(1) + '" cy="' + mid.y.toFixed(1) + '" r="' + rad +
           '" fill="url(#spkW' + b.id + ')"/>';
    }
  });

  /* 2. the road itself */
  s += '<path d="' + ROAD_D + '" fill="none" stroke="#C9A97F" stroke-width="17" stroke-linecap="round"/>';
  s += '<path d="' + ROAD_D + '" fill="none" stroke="#F6E9CE" stroke-width="12" stroke-linecap="round"/>';

  /* 3. landmarks stand on the land above the road; the name sits below it */
  COURSE.forEach(function (b) {
    var r = REGION[b.id];
    var mid = at(weekT((b.weeks[0] + b.weeks[1]) / 2));
    var fin = bookRead(books, b);
    var lm = artURL((ART.worlds[b.id] || {}).landmark);
    if (lm) {
      s += '<image href="' + lm + '" x="' + (mid.x - 55).toFixed(1) + '" y="' + (mid.y - 104).toFixed(1) +
           '" width="110" height="82" preserveAspectRatio="xMidYMax meet"/>';
    } else {
      s += '<g transform="translate(' + mid.x.toFixed(1) + ',' + (mid.y - 26).toFixed(1) + ')">' +
           LANDMARK[b.id]() + '</g>';
    }
    var name = r.label + ' \u00b7 Wk ' +
      (b.weeks[0] === b.weeks[1] ? b.weeks[0] : b.weeks[0] + '\u2013' + b.weeks[1]) +
      (fin ? ' \u00b7 read' : '');
    s += '<text x="' + mid.x.toFixed(1) + '" y="' + (mid.y + 27).toFixed(1) + '" font-size="13.5" text-anchor="middle" ' +
         'font-family="Lora,Georgia,serif" font-style="italic" paint-order="stroke" stroke="#FCF3DF" stroke-width="4.5" ' +
         'stroke-linejoin="round" fill="' + r.ink + '">' + name + '</text>';
  });

  /* 4. the thirty-two week spaces */
  for (var w = 1; w <= 32; w++) {
    var pt = at(weekT(w));
    var st = weekDone(prog, w);
    var cur = w === LESSON.week;
    var ink = REGION[regionOfWeek(w).id].ink;
    var fill = st === 'done' ? ink : st === 'started' ? '#FFFDF4' : '#FFFDF4';
    s += '<g class="spk-space" data-week="' + w + '"><title>Week ' + w + ' · ' + REGION[regionOfWeek(w).id].label + '</title>' +
      '<circle cx="' + pt.x.toFixed(1) + '" cy="' + pt.y.toFixed(1) + '" r="' + (cur ? 11 : 8) + '" fill="' + fill +
        '" stroke="' + (cur ? '#C7922C' : ink) + '" stroke-width="' + (cur ? 3 : 1.8) + '" opacity="' + (st === 'ahead' && !cur ? .5 : 1) + '"/>';
    if (st === 'started' && !cur) {
      s += '<circle cx="' + pt.x.toFixed(1) + '" cy="' + pt.y.toFixed(1) + '" r="4" fill="' + ink + '" opacity=".55"/>';
    }
    if (seals['w' + w]) {                              /* a Scholar's laurel on that week */
      s += '<path d="M' + (pt.x - 11).toFixed(1) + ' ' + (pt.y + 2).toFixed(1) + ' q-3 -8 3 -13 M' +
           (pt.x + 11).toFixed(1) + ' ' + (pt.y + 2).toFixed(1) + ' q3 -8 -3 -13" stroke="#C7922C" stroke-width="2" fill="none" stroke-linecap="round"/>';
    }
    s += '</g>';
  }

  /* 5. the owl guide — the student's traveller on the road */
  var me = at(weekT(LESSON.week));
  var OW = 66;
  s += '<ellipse cx="' + me.x.toFixed(1) + '" cy="' + (me.y + 6).toFixed(1) +
    '" rx="22" ry="6" fill="#6B4E2A" opacity=".2"/>';
  s += '<g transform="translate(' + (me.x - OW / 2).toFixed(1) + ',' + (me.y - OW - 2).toFixed(1) + ')">' +
    owlMarkSVG(p && p.owl ? p.owl : defaultCompanion(), OW) + '</g>';
  var bw = 72, right = me.x < 760;
  var bx = right ? me.x + 24 : me.x - 24 - bw;
  s += '<rect x="' + bx.toFixed(1) + '" y="' + (me.y - 44).toFixed(1) +
    '" width="' + bw + '" height="19" rx="9.5" fill="#C7922C"/>' +
    '<text x="' + (bx + bw / 2).toFixed(1) + '" y="' + (me.y - 30).toFixed(1) + '" font-size="10.5" text-anchor="middle" ' +
    'font-family="Nunito,sans-serif" font-weight="800" fill="#FFF8E9">WEEK ' + LESSON.week + '</text>';

  s += '<rect width="900" height="660" fill="url(#spkVig)" pointer-events="none"/>';
  /* the second place their name appears: the map is the keepsake */
  var who = (p && p.name) ? esc(p.name) + '’s Year of Reading' : 'A Year of Reading';
  s += '<text x="450" y="34" font-size="19" text-anchor="middle" font-family="Lora,Georgia,serif" font-style="italic" fill="#8B6914">' +
       who + ' · Grade Four</text>';

  svg.innerHTML = '<defs>' + defs + '</defs>' + s;

  var here = document.getElementById('spkHere');
  if (here) {
    var done = 0; for (var k = 1; k <= 32; k++) if (weekDone(prog, k) === 'done') done++;
    here.innerHTML = '';
    var line = document.createElement('span');
    line.textContent = 'You are on week ' + LESSON.week + ' of 32, in ' +
      REGION[LESSON.book].label + '. ' + done + (done === 1 ? ' week' : ' weeks') + ' behind you.';
    here.appendChild(line);
  }
}

function drawShelf(fillId) {
  var host = document.getElementById('spkShelf'); if (!host) return;
  var books = Sparkle.get('oao.g4ela.books', {});
  host.innerHTML = '';
  host.classList.toggle('spk-shelf-covers', SHELF.some(function (b) { return !!artURL(ART.covers[b.id]); }));

  SHELF.forEach(function (b) {
    var course = COURSE.filter(function (c) { return c.id === b.id; })[0];
    var done = !b.writing && course && bookRead(books, course);
    var cover = artURL(ART.covers[b.id]);
    var el = document.createElement('div');
    el.className = 'spk-book' + (done ? ' read' : '') + (cover ? ' has-cover' : ' no-cover') +
                   (b.gold ? ' gold' : '') + (b.writing ? ' writing' : '');

    if (cover) {
      var im = document.createElement('img');
      im.className = 'spk-book-cover';
      im.src = cover; im.alt = b.short; im.loading = 'lazy';
      /* a cover that fails to load must not leave a hole */
      im.onerror = function () { el.classList.remove('has-cover'); el.classList.add('no-cover'); im.remove(); addSpine(); };
      el.appendChild(im);
    } else { addSpine(); }

    function addSpine() {
      var sp = document.createElement('span');
      sp.className = 'spk-book-spine'; sp.textContent = b.short;
      el.appendChild(sp);
    }

    if (!b.writing) {
      el.title = done ? b.short + ' \u2014 read' : 'Find ' + REGION[b.id].label + ' on the map';
      el.onmouseenter = function () { flashRegion(b.id, true); };
      el.onmouseleave = function () { flashRegion(b.id, false); };
      el.onclick = function () { flashRegion(b.id, true); setTimeout(function () { flashRegion(b.id, false); }, 1400); };
    } else { el.title = 'Your own writing, published at the end of the year'; }

    if (b.id === fillId && !REDUCED) {
      el.classList.add('spk-book-arriving');
      setTimeout(function () { el.classList.remove('spk-book-arriving'); }, 40);
    }
    host.appendChild(el);
  });
}

/* ring the weeks of one book on the map — the shelf and the road
   are the same journey seen two ways */
function flashRegion(bookId, on) {
  var svg = document.getElementById('spkMap'); if (!svg) return;
  var b = COURSE.filter(function (x) { return x.id === bookId; })[0]; if (!b) return;
  svg.querySelectorAll('.spk-space').forEach(function (g) {
    var w = +g.getAttribute('data-week');
    var mine = w >= b.weeks[0] && w <= b.weeks[1];
    var c = g.querySelector('circle');
    if (!mine || !c) return;
    if (on) { c.setAttribute('stroke', '#C7922C'); c.setAttribute('stroke-width', '3.4'); c.setAttribute('opacity', '1'); }
    else { drawMap(); }
  });
}

document.addEventListener('oao:bookfinished', function (e) {
  drawMap(); drawShelf(e.detail.book.id);
  owlSay('The book is closed, and kept.');
  var note = document.getElementById('spkShelfNote');
  if (note) note.innerHTML = 'You have read all of <em>' + e.detail.book.title + '</em>. It is on your shelf now!';
});

function buildDolChoice() {
  var label = document.querySelector('.dol-fix-label'); if (!label) return;
  var old = label.nextElementSibling;                       /* .dol-sentence-wrap  */
  var hint = old && old.nextElementSibling;                  /* .dol-hint           */
  var btn = document.querySelector('.dol-check-btn');
  var ans = document.getElementById('dolAns');
  if (!old || !ans) return;

  label.innerHTML = '🔧 Choose one to fix';
  old.style.display = 'none';

  var box = document.createElement('div');
  box.className = 'spk-dol-choice'; box.id = 'spkDolChoice';
  box.innerHTML =
    '<div class="spk-dol-card" data-pick="a"><span class="spk-dol-tag">Sentence A</span><span class="spk-dol-text">' + DATA.dol.a.raw + '</span></div>' +
    '<div class="spk-dol-card" data-pick="b"><span class="spk-dol-tag">Sentence B</span><span class="spk-dol-text">' + DATA.dol.b.raw + '</span></div>';
  label.parentNode.insertBefore(box, old);

  var swap = document.createElement('button');
  swap.type = 'button'; swap.className = 'spk-dol-swap'; swap.textContent = 'Show me the other one instead';
  swap.style.display = 'none';
  box.parentNode.insertBefore(swap, box.nextSibling);

  function paint(pick) {
    box.querySelectorAll('.spk-dol-card').forEach(function (c) {
      var mine = c.getAttribute('data-pick') === pick;
      c.classList.toggle('chosen', mine);
      c.classList.toggle('folded', !!pick && !mine);
    });
    swap.style.display = pick ? 'inline-block' : 'none';
    if (hint) hint.style.display = pick ? '' : 'none';
    if (btn) btn.style.display = pick ? '' : 'none';
    if (pick) {
      ans.innerHTML =
        '<p style="margin-bottom:6px;"><strong>Corrected:</strong> ' + DATA.dol[pick].fixed + '</p>' +
        '<p style="font-size:13px;color:#7A88A8;font-style:italic;">' + DATA.dol[pick].why + '</p>';
    } else { ans.classList.remove('show'); }
  }
  box.querySelectorAll('.spk-dol-card').forEach(function (c) {
    c.onclick = function () {
      var pick = c.getAttribute('data-pick');
      var all = Sparkle.get('oao.g4ela.dol', {}); all[LID] = pick; Sparkle.set('oao.g4ela.dol', all);
      paint(pick);
    };
  });
  swap.onclick = function () {
    var all = Sparkle.get('oao.g4ela.dol', {});
    var next = all[LID] === 'a' ? 'b' : 'a';
    all[LID] = next; Sparkle.set('oao.g4ela.dol', all);
    ans.classList.remove('show'); paint(next);
  };
  paint(Sparkle.get('oao.g4ela.dol', {})[LID] || null);
}

/* ══════════════════════════════════════════════════════════════
   §2.5  EXPLORER / SCHOLAR   +   §2.6  COACHING
   ══════════════════════════════════════════════════════════════ */
/* ══════════════════════════════════════════════════════════════
   §2.5  EXPLORER / SCHOLAR — the two roads
   Choosing Scholar has to feel like choosing something, so it
   pays three ways, all of them visible and none of them points:
     · the section illuminates the moment you choose it
     · finishing it seals the work with a laurel
     · the seal shows on your published page, in the work you
       turn in, and on that week's space on the map
   ══════════════════════════════════════════════════════════════ */
function currentTier() {
  var t = Sparkle.get('oao.g4ela.tier', {});
  return t[LID] || t._last || 'explorer';
}
function setTier(v) {
  var t = Sparkle.get('oao.g4ela.tier', {});
  t[LID] = v; t._last = v; Sparkle.set('oao.g4ela.tier', t);
}
function hasSeal() { return !!Sparkle.get('oao.g4ela.scholar', {})[LID]; }
function grantSeal() {
  var s = Sparkle.get('oao.g4ela.scholar', {});
  if (s[LID]) return false;
  s[LID] = true; s['w' + LESSON.week] = true;
  Sparkle.set('oao.g4ela.scholar', s);
  return true;
}

function laurelSVG(size) {
  size = size || 76;
  /* the painted seal when there is one; the drawn fallback below
     otherwise, so the mark never simply disappears. Under ~56px the
     wreath closes into a smudge, so the wax disc alone is used. */
  var seal = ART.seals || {};
  var src = (size < 56 ? (artURL(seal.mark) || artURL(seal.scholar))
                       : (artURL(seal.scholar) || artURL(seal.mark)));
  if (src) {
    return '<img class="spk-seal-img" src="' + src + '" width="' + size +
           '" alt="" aria-hidden="true" loading="lazy">';
  }
  return '<svg viewBox="0 0 100 100" width="' + size + '" height="' + size + '" aria-hidden="true">' +
    '<circle cx="50" cy="50" r="30" fill="#FFF3DC" stroke="#C7922C" stroke-width="2"/>' +
    '<path d="M32 24 Q14 46 30 74 M68 24 Q86 46 70 74" stroke="#6E9450" stroke-width="3" fill="none" stroke-linecap="round"/>' +
    '<ellipse cx="24" cy="36" rx="6" ry="3" fill="#7DA85C" transform="rotate(-40 24 36)"/>' +
    '<ellipse cx="20" cy="50" rx="6" ry="3" fill="#7DA85C" transform="rotate(-8 20 50)"/>' +
    '<ellipse cx="24" cy="64" rx="6" ry="3" fill="#7DA85C" transform="rotate(26 24 64)"/>' +
    '<ellipse cx="76" cy="36" rx="6" ry="3" fill="#7DA85C" transform="rotate(40 76 36)"/>' +
    '<ellipse cx="80" cy="50" rx="6" ry="3" fill="#7DA85C" transform="rotate(8 80 50)"/>' +
    '<ellipse cx="76" cy="64" rx="6" ry="3" fill="#7DA85C" transform="rotate(-26 76 64)"/>' +
    (size >= 56
      ? '<text x="50" y="45" font-size="15" text-anchor="middle" font-family="Lora,Georgia,serif" font-style="italic" fill="#8B6914">Scholar</text>' +
        '<path d="M34 52 h32" stroke="#C7922C" stroke-width="1.2"/>' +
        '<text x="50" y="66" font-size="10.5" text-anchor="middle" font-family="Nunito,sans-serif" font-weight="800" fill="#A8801F">EVIDENCE</text>'
      : '<path d="M38 50 l7 8 16 -18" stroke="#C7922C" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>') +
    '</svg>';
}

function buildTiers() {
  var q1 = document.getElementById('journal-q1'); if (!q1) return;
  var body = q1.closest('.activity-body');
  var firstBlock = body.querySelector('.q-block'); if (!firstBlock) return;
  var activity = q1.closest('.activity');

  var sw = document.createElement('div');
  sw.className = 'spk-roads';
  sw.innerHTML =
    '<div class="spk-roads-label">Pick how you want to answer today\u2019s three questions.</div>' +
    '<div class="spk-roads-cards">' +
      '<button type="button" class="spk-road" data-tier="explorer">' +
        '<span class="spk-road-name">Explorer</span>' +
        '<span class="spk-road-line">Answer all three questions.</span>' +
      '</button>' +
      '<button type="button" class="spk-road" data-tier="scholar">' +
        '<span class="spk-road-laurel">' + laurelSVG(46) + '</span>' +
        '<span class="spk-road-name">Scholar \u2014 go further</span>' +
        '<span class="spk-road-line">Every question asks you for <b>one more thing</b>: another detail, ' +
        'or <b>why</b> you think so. Finish all three and you earn the Scholar\u2019s seal.</span>' +
      '</button>' +
    '</div>' +
    '<div class="spk-roads-note">Either one finishes the lesson. You can switch whenever you want.</div>' +
    '<div class="spk-seal-strip" id="spkSealStrip"></div>';
  firstBlock.parentNode.insertBefore(sw, firstBlock);

  Object.keys(DATA.scholar).forEach(function (id) {
    var ta = document.getElementById(id); if (!ta) return;
    var block = ta.previousElementSibling;
    while (block && !block.classList.contains('q-block')) block = block.previousElementSibling;
    if (!block) return;
    var add = document.createElement('span');
    add.className = 'spk-scholar-add'; add.setAttribute('data-for', id);
    add.textContent = DATA.scholar[id]; add.style.display = 'none';
    block.querySelector('.q-text').appendChild(add);
  });

  function paint(v) {
    sw.querySelectorAll('.spk-road').forEach(function (b) {
      b.classList.toggle('on', b.getAttribute('data-tier') === v);
    });
    document.querySelectorAll('.spk-scholar-add').forEach(function (a) {
      a.style.display = v === 'scholar' ? 'block' : 'none';
    });
    if (activity) activity.classList.toggle('spk-illuminated', v === 'scholar');
    Object.keys(DATA.flags).forEach(function (id) { coach(document.getElementById(id)); });
    sealCheck(true);
  }
  sw.querySelectorAll('.spk-road').forEach(function (b) {
    b.onclick = function () {
      var v = b.getAttribute('data-tier'), was = currentTier();
      setTier(v); paint(v);
      if (v === 'scholar' && was !== 'scholar') {
        owlSay('The longer road, then. Good.');
        if (!REDUCED && activity) {
          activity.classList.remove('spk-lightup'); void activity.offsetWidth; activity.classList.add('spk-lightup');
        }
      }
    };
  });
  paint(currentTier());
}

/* the seal lands when all three Scholar answers are actually done */
function sealCheck(quiet) {
  var strip = document.getElementById('spkSealStrip'); if (!strip) return;
  var ids = Object.keys(DATA.scholar);
  var earned = hasSeal();

  if (currentTier() !== 'scholar' && !earned) { strip.innerHTML = ''; return; }

  if (!earned) {
    var ready = 0;
    ids.forEach(function (id) {
      var ta = document.getElementById(id);
      if (ta && words(ta.value) >= 20) ready++;
    });
    if (ready >= ids.length) {
      earned = grantSeal();
      if (!quiet && earned) {
        owlSay('Sealed. That is scholar’s work.');
        /* deliberately no confetti here: the stamp is the reward, and the
           spec's rule is classical, not gamified. To add it back, this
           line is all it takes:   window.fireConfetti();                */
      }
    } else {
      strip.innerHTML = '<div class="spk-seal-progress">' +
        '<span class="spk-seal-ghost">' + laurelSVG(40) + '</span>' +
        '<span><b>' + ready + ' of ' + ids.length + ' answers are long enough so far.</b><br>' +
        'To earn the seal, write about 3 sentences for each question, and say <b>why</b> you think so ' +
        '\u2014 or use words from the book.</span></div>';
      return;
    }
  }

  if (earned && !strip.querySelector('.spk-seal-won')) {
    strip.innerHTML = '<div class="spk-seal-won">' +
      '<span class="spk-seal-stamp">' + laurelSVG(86) + '</span>' +
      '<span><b>You earned the Scholar\u2019s seal.</b><br>It goes on the work you hand in, on your ' +
      'published page, and on Week ' + LESSON.week + ' of your Reading Road.</span></div>';
    drawMapIfPresent();
    if (window.gatherAnswers) window.gatherAnswers();
  }
}
function drawMapIfPresent() {
  var b = document.getElementById('spkRoadBody');
  if (b && b.hidden) return;                 /* folded away — nothing to redraw */
  if (document.getElementById('spkMap')) drawMap();
}

function words(s) { return (s.trim().match(/[A-Za-z0-9'’-]+/g) || []).length; }
function hasQuote(s) {
  return /"[^"]{2,}"/.test(s) || /“[^”]{2,}”/.test(s) || /'[^']{4,}'/.test(s);
}
function countCues(s) {
  var t = ' ' + s.toLowerCase() + ' ';
  var cues = [' and ', ' also ', ' second ', ' another ', ' then ', ' too '];
  var n = 0; cues.forEach(function (c) { if (t.indexOf(c) !== -1) n++; });
  if ((s.match(/[.!?]\s+[A-Za-z]/g) || []).length >= 1) n++;
  return n;
}

function coach(ta) {
  if (!ta) return;
  var line = ta.parentNode.querySelector('.spk-coach[data-for="' + ta.id + '"]');
  if (!line) return;
  var flags = DATA.flags[ta.id] || {};
  var v = ta.value, w = words(v);
  var minW = currentTier() === 'scholar' ? 20 : 12;
  line.classList.remove('good');
  if (!v.trim()) { line.textContent = ''; return; }
  if (w < minW) { line.textContent = 'Keep going — a full answer is about three sentences.'; return; }
  if (flags.quote && !hasQuote(v)) { line.textContent = 'Add words from the book, with "quotation marks" around them.'; return; }
  if (flags.count >= 2 && countCues(v) < 2) { line.textContent = 'This question asks for two details. I can only find one so far.'; return; }
  if (/\bbecause\b|\bso\b/i.test(v) || hasQuote(v)) {
    line.textContent = 'Good — you told why, and you used the book.'; line.classList.add('good');
    clearTimeout(line._t); line._t = setTimeout(function () { line.style.opacity = '0'; setTimeout(function () { line.textContent=''; line.style.opacity=''; }, 260); }, 3000);
    return;
  }
  line.textContent = '';
}

function buildCoaches() {
  Object.keys(DATA.flags).forEach(function (id) {
    var ta = document.getElementById(id); if (!ta) return;
    var line = document.createElement('div');
    line.className = 'spk-coach'; line.setAttribute('data-for', id);
    ta.parentNode.insertBefore(line, ta.nextSibling);
    var t = null;
    ta.addEventListener('input', function () {
      line.style.opacity = ''; clearTimeout(t);
      t = setTimeout(function () { coach(ta); sealCheck(false); }, 400);
    });
    coach(ta);
  });
}

/* ══════════════════════════════════════════════════════════════
   §2.7  HINT LADDERS + DISTRACTOR FEEDBACK
   ══════════════════════════════════════════════════════════════ */
function bumpHint(key) {
  var h = Sparkle.get('oao.g4ela.hints', {});
  h[LID + ':' + key] = (h[LID + ':' + key] || 0) + 1;
  Sparkle.set('oao.g4ela.hints', h);
  return h[LID + ':' + key];
}
function hintSlot(inp) {
  var slot = inp.parentNode.querySelector('.spk-hint');
  if (!slot) {
    slot = document.createElement('div'); slot.className = 'spk-hint';
    inp.parentNode.appendChild(slot);
  }
  return slot;
}
function blanks(word) {
  return word.charAt(0) + ' ' + word.slice(1).split('').map(function () { return '_'; }).join(' ');
}
window._spkRevealed = window._spkRevealed || {};

/* wraps the lesson's own checkFillIn */
var _origCheckFillIn = window.checkFillIn;
window.checkFillIn = function (btn) {
  var g = (btn && btn.closest) ? btn.closest('.fillin-game') : null;
  var scope = g || document;
  var inputs = [].slice.call(scope.querySelectorAll('.fillin-input'));
  var anyWrong = false, stuck = false;

  inputs.forEach(function (inp) {
    if (inp.disabled) return;
    var answer = (inp.getAttribute('data-answer') || '').toLowerCase();
    var val = inp.value.trim().toLowerCase();
    var cfg = DATA.hints[inp.id];
    var slot = cfg ? hintSlot(inp) : null;
    if (val === answer) { if (slot) slot.remove(); return; }
    anyWrong = true;
    /* An empty box is not a wrong try — the ladder only advances on
       an attempt, so tapping Check early never spends a student's hints. */
    if (val === '') { if (slot) slot.remove(); return; }
    if (!cfg) return;
    var n = bumpHint(inp.id);
    if (n === 1) { slot.className = 'spk-hint'; slot.innerHTML = cfg.h1; }
    else if (n === 2) {
      slot.className = 'spk-hint';
      slot.innerHTML = cfg.h1 + '<br><span class="spk-blanks">' + blanks(answer) + '</span>';
    } else {
      slot.className = 'spk-hint reveal';
      slot.innerHTML = '<b>' + answer + '</b> — ' + cfg.why;
      inp.value = answer; inp.disabled = true;
      inp.classList.add('spk-revealed'); inp.classList.remove('wrong', 'correct');
      window._spkRevealed[inp.id] = true;
      stuck = true;
    }
  });

  var r = _origCheckFillIn.apply(this, arguments);
  /* re-apply the revealed look the original may have cleared */
  inputs.forEach(function (inp) {
    if (window._spkRevealed[inp.id]) { inp.classList.add('spk-revealed'); inp.classList.remove('correct'); }
  });
  if (stuck) owlSay(OWL.stuck);
  else if (!anyWrong) owlCorrect();
  return r;
};

/* match-game distractor lines */
function missLine(host, text) {
  if (!text) return;
  var slot = host.querySelector('.spk-miss');
  if (!slot) { slot = document.createElement('div'); slot.className = 'spk-miss'; host.appendChild(slot); }
  slot.textContent = text;
  slot.style.animation = 'none'; void slot.offsetWidth; slot.style.animation = '';
  clearTimeout(slot._t);
  slot._t = setTimeout(function () { if (slot.parentNode) slot.parentNode.removeChild(slot); }, 4200);
}

var _origMatchClick = window.matchClick;
window.matchClick = function (item) {
  var grid = item.closest('.match-grid');
  var before = grid ? grid.querySelectorAll('.match-item.matched').length : 0;
  var sel = grid ? grid.querySelector('.match-item.selected') : null;
  var r = _origMatchClick.apply(this, arguments);
  if (!grid) return r;
  var after = grid.querySelectorAll('.match-item.matched').length;
  if (after > before) { owlCorrect(); return r; }
  if (sel && sel !== item) {
    var wordEl = sel.classList.contains('is-word') ? sel : (item.classList.contains('is-word') ? item : null);
    if (wordEl) missLine(grid.parentNode, DATA.miss.match[wordEl.textContent.trim()]);
  }
  return r;
};

var _origDrop = window.dropSortChip;
window.dropSortChip = function (colDrop, colName) {
  var g = colDrop.closest('.sort-game');
  var sel = g ? g._oaoSel : null;
  var wrong = sel && sel.getAttribute('data-group') !== colName;
  var label = sel ? sel.textContent.trim() : '';
  var r = _origDrop.apply(this, arguments);
  if (wrong) { missLine(g, DATA.miss.sort[label]); bumpHint('sort'); }
  else if (sel) { owlCorrect(); }
  return r;
};

/* ══════════════════════════════════════════════════════════════
   §2.8  COPIA
   ══════════════════════════════════════════════════════════════ */
function buildCopia() {
  var panel = document.getElementById('tab-words'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap'); if (!anchor) return;
  var card = document.createElement('div');
  card.className = 'spk-card';
  var slots = [
    ['Change the opener', 'Start with a when or a where.'],
    ['Swap the verb', 'Find a stronger word than the one in bold.'],
    ['Add a where or a how', 'Tell us where it happened, or how it was done.']
  ];
  var html =
    '<div class="spk-card-head"><div class="spk-card-num">✎</div><div>' +
    '<div class="spk-card-title">Copia · Say It Three Ways</div>' +
    '<div class="spk-card-sub">Erasmus had his students rewrite one sentence a hundred ways. You only need three.</div>' +
    '</div></div><div class="spk-card-body">' +
    '<p style="font-size:15px;color:#3A4A6B;">Here is one sentence from this week’s chapter. There is no wrong answer here — only more ways to say it.</p>' +
    '<div class="spk-copia-seed">' + DATA.copia.seed + '</div>';
  slots.forEach(function (s, i) {
    var id = 'journal-copia' + (i + 1);
    html += '<div class="spk-copia-slot">' +
      '<div class="spk-copia-slot-label">' + (i + 1) + '. ' + s[0] + '</div>' +
      '<div class="spk-copia-slot-hint">' + s[1] + '</div>' +
      '<textarea class="journal-box" id="' + id + '" data-label="Copia ' + (i + 1) + ': ' + s[0] + '" ' +
      'placeholder="Write your way here…" style="min-height:64px;"></textarea>' +
      '<button type="button" class="spk-mini-btn" data-eg="' + i + '">Show one way</button>' +
      '</div>';
  });
  html += '</div>';
  card.innerHTML = html;
  anchor.parentNode.insertBefore(card, anchor);

  card.querySelectorAll('textarea.journal-box').forEach(function (ta) {
    try { var v = localStorage.getItem(window._lessonKey + '-' + ta.id); if (v) ta.value = v; } catch (e) {}
    ta.addEventListener('input', function () {
      try { localStorage.setItem(window._lessonKey + '-' + ta.id, ta.value); } catch (e) {}
      if (window.gatherAnswers) window.gatherAnswers();
    });
  });
  card.querySelectorAll('.spk-mini-btn').forEach(function (b) {
    b.onclick = function () {
      var i = +b.getAttribute('data-eg');
      if (b.nextElementSibling && b.nextElementSibling.classList.contains('spk-copia-eg')) return;
      var eg = document.createElement('div');
      eg.className = 'spk-copia-eg';
      /* the examples carry one <i> around the swapped word. textContent
         printed the tag itself; building the node keeps the markup as
         markup without ever handing a string to innerHTML. */
      eg.appendChild(document.createTextNode('“'));
      DATA.copia.eg[i].split(/<i>|<\/i>/).forEach(function (part, n) {
        if (!part) return;
        if (n % 2) { var em = document.createElement('i'); em.textContent = part; eg.appendChild(em); }
        else eg.appendChild(document.createTextNode(part));
      });
      eg.appendChild(document.createTextNode('”'));
      b.parentNode.insertBefore(eg, b.nextSibling);
      b.textContent = 'One way, shown';
      b.disabled = true; b.style.opacity = '.6';
    };
  });
}

/* ══════════════════════════════════════════════════════════════
   §2.9  MEMORY-WORK FADE LADDER
   ══════════════════════════════════════════════════════════════ */
function memState() {
  var m = Sparkle.get('oao.g4ela.memory', {});
  if (!m[LESSON.book]) m[LESSON.book] = { rung: 1, advancedOn: null };
  return m;
}
function rungFor(week) { return Math.max(1, Math.min(8, week - 6)); }

/* which word indices are hidden at a given rung */
function fadeMask(lineWords, lineIdx, rung) {
  var n = lineWords.length, hide = {};
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

/* ══════════════════════════════════════════════════════════════
   §2.11  RECORDED VOICE

   Three places get a recording: the welcome that opens the lesson,
   the poem on the Reading tab, and the Growing-Up Watch intro.

   They are keyed at three different rates, because they repeat at
   three different rates:

     welcome  per lesson   g4ela-7-1.mp3        128 clips a year
     watch    per week     g4ela-wk7.mp3         32 clips a year
     poem     per poem     lady-of-shalott.mp3    ~8 clips a year

   A poem runs for a whole book arc, so one reading serves all eight
   weeks of it — which is right, since it is the model a student
   memorises against. Keying these by lesson instead would mean 384
   recordings for the same result.

   Nothing is per-lesson in the code: drop the file in the right
   folder under the naming rule and the control appears. Take it away
   and the control disappears. There is never a dead button, because
   the control starts hidden and only shows once the browser has the
   file's metadata in hand.
   ══════════════════════════════════════════════════════════════ */
/* ══════════════════════════════════════════════════════════════
   §2.12  THE MEDIA SLOT TABLE

   Every recording on the page — the welcome, the three guiding-voice
   clips, the poem, and any strand section you want to add one to — is
   ONE ROW in the table below. A row says where it mounts, what it is
   called, and what kind of thing it is:

     kind: ''          the slot is off. Nothing renders, nothing is
                       fetched. This is the default.
     kind: 'audio'     an .mp3 from assets/audio/
     kind: 'video'     an .mp4 from assets/video/
     kind: 'youtube'   an embedded YouTube player; needs `yt`

   Switching a slot between voice and film is a one-word edit in this
   table. Adding a recording to a section that has never had one is a
   row. No lesson HTML changes for either.

   THE ONE ASYMMETRY, and it matters:

     audio and video are hidden until the browser confirms the file is
     really there, so a missing recording is invisible — exactly like a
     missing chapter plate.

     A YouTube embed cannot be checked from the page. The iframe is a
     sealed box: if the id is wrong, private, deleted or blocked, it
     shows YouTube's own error inside the frame and the page has no way
     to know. So for 'youtube' the manifest IS the check — a row with
     no `yt` renders nothing, and a row with a bad `yt` renders a
     broken player rather than silence. Validate ids at build time.
   ══════════════════════════════════════════════════════════════ */

var MEDIA = {
  audioBase: 'assets/audio/',
  videoBase: 'assets/video/',
  /* youtube-nocookie: no cookie is written until the viewer presses
     play. For a K-5 course this is the host to use, not youtube.com. */
  ytBase: 'https://www.youtube-nocookie.com/embed/',

  slots: [
    /* ---- the guiding voice: on today ---- */
    { id:'welcome', kind:'audio', at:{greeting:true},
      path:'guide/welcome/g4ela-{w}-{d}',
      label:'Listen to today’s welcome' },

    { id:'guide1',  kind:'audio', at:{tab:'words'},
      path:'guide/turn/g4ela-{w}-{d}-1',
      label:'Before you begin the word work' },

    { id:'guide2',  kind:'audio', at:{tab:'reading'},
      path:'guide/turn/g4ela-{w}-{d}-2',
      label:'Before you open the book' },

    { id:'guide3',  kind:'audio', at:{tab:'assignment'},
      path:'guide/turn/g4ela-{w}-{d}-3',
      label:'Before you write' },

    { id:'poem',    kind:'audio', at:{el:'spkPoem'},
      path:'poem/{poem}', inline:true,
      label:'Hear the poem read aloud' },

    /* ---- the sections: every one, all off until you give it a kind ----
       `section` matches the text of an .activity-title, so a clip lands
       at the head of that activity wherever it sits on the page. The
       count after each is how many of the 129 lessons have it; where a
       lesson does not, the slot simply does not render.

       Turning one on means a script for it in that lesson's script doc.
       All seventeen on, every day, would be 2,193 recordings for the
       year and far too many voices for a nine-year-old — these exist so
       you can choose the few that earn it, not so they all get used. */
    { id:'wgrd',       kind:'', at:{section:/what good readers do/i},   /* 127 */
      path:'guide/wgrd/g4ela-{w}-{d}',     label:'About today’s reading move' },
    { id:'dol',        kind:'', at:{section:/daily oral/i},             /* 127 */
      path:'guide/dol/g4ela-{w}-{d}',      label:'About today’s sentence' },
    { id:'vocabulary', kind:'', at:{section:/vocabular/i},              /* 126 */
      path:'guide/vocab/g4ela-{w}-{d}',    label:'About today’s words' },
    { id:'grammar',    kind:'', at:{section:/grammar/i},                /* 127 */
      path:'guide/grammar/g4ela-{w}-{d}',  label:'About today’s grammar' },
    { id:'morphology', kind:'', at:{section:/morpholog/i},              /* 127 */
      path:'guide/morph/g4ela-{w}-{d}',    label:'About today’s word parts' },
    { id:'spelling',   kind:'', at:{section:/spelling/i},               /* 125 */
      path:'guide/spelling/g4ela-{w}-{d}', label:'About today’s spelling' },
    { id:'workshop',   kind:'', at:{section:/writer.s workshop/i},      /* 100 */
      path:'guide/workshop/g4ela-{w}-{d}', label:'About today’s writing' },
    { id:'chapter',    kind:'', at:{section:/chapter thinking/i},       /* 100 */
      path:'guide/chapter/g4ela-{w}-{d}',  label:'About today’s chapter' },
    { id:'read',       kind:'', at:{section:/open your (book|sources)|^[\W_]*read\b/i}, /* 103 */
      path:'guide/read/g4ela-{w}-{d}',     label:'Before you read' },
    { id:'poetry',     kind:'', at:{section:/poetry corner/i},          /* 63 */
      path:'guide/poetry/g4ela-{w}-{d}',   label:'About the poem' },
    { id:'wordconn',   kind:'', at:{section:/word study connection/i},  /* 98 */
      path:'guide/wordconn/g4ela-{w}-{d}', label:'How this connects' },
    { id:'copywork',   kind:'', at:{section:/copywork/i},               /* 18 */
      path:'guide/copywork/g4ela-{w}-{d}', label:'About today’s copywork' },
    { id:'shelf',      kind:'', at:{section:/your reading shelf/i},     /* 5 */
      path:'guide/shelf/g4ela-{w}-{d}',    label:'About your shelf' }
  ]
};
window.OAO_MEDIA = MEDIA;
/* test hook: the media functions, for the headless sweep */
window.OAO_MEDIA_FNS = null;

/* A per-lesson override, set from the lesson's DATA block. Lets one
   lesson use film where the rest of the year uses voice, without
   touching the table above:
     DATA.media = { guide2:{kind:'youtube', yt:'dQw4w9WgXcQ'} }            */
function mediaSlots() {
  var over = (typeof DATA === 'object' && DATA && DATA.media) || {};
  return MEDIA.slots.map(function (s) {
    var o = over[s.id]; if (!o) return s;
    var m = {}; for (var k in s) m[k] = s[k];
    for (var k2 in o) m[k2] = o[k2];
    return m;
  });
}

/* "The Lady of Shalott" -> "lady-of-shalott". The leading article is
   dropped: it keeps a folder of poems sorting by the word that
   matters, and it is what the spec told the recordist to name the
   file. (This function and the spec disagreed on exactly that point
   for one build — the code kept the "the-", the spec did not, and the
   first real recording landed under the spec's name and was not
   found. The spec wins.) */
function slug(s) {
  return String(s).toLowerCase().replace(/[’']/g, '')
    .replace(/^(the|a|an)\s+/, '')
    .replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
}

function mediaPath(slot) {
  return String(slot.path || '')
    .replace('{w}', LESSON.week)
    .replace('{d}', dayNum(LESSON.day))
    .replace('{poem}', slug((DATA.poem || {}).title || ''));
}
function mediaSrc(slot) {
  var p = mediaPath(slot); if (!p) return '';
  if (slot.src) return slot.src;                  /* explicit wins */
  if (slot.kind === 'audio') return MEDIA.audioBase + p + '.mp3';
  if (slot.kind === 'video') return MEDIA.videoBase + p + '.mp4';
  return '';
}

var GUIDE_NOTE = null;   /* what the Watch block used to say */

/* one clip plays at a time, and starting one silences the page's
   text-to-speech reader — two voices at once is the worst outcome */
var _nowPlaying = null;
function audioStopAll(except) {
  if (_nowPlaying && _nowPlaying !== except) { try { _nowPlaying.pause(); } catch (e) {} }
  try { if (window.speechSynthesis) window.speechSynthesis.cancel(); } catch (e) {}
}
function mmss(t) {
  if (!isFinite(t)) return '';
  var m = Math.floor(t / 60), s = Math.floor(t % 60);
  return m + ':' + (s < 10 ? '0' : '') + s;
}

/* Built hidden, revealed only once the file is known to exist.
   A missing recording is silent in both senses. */
function audioControl(label, src) {
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
    wrap.hidden = false;                       /* the file is really there */
    time.textContent = mmss(a.duration);
  });
  a.addEventListener('error', function () { wrap.remove(); });
  a.addEventListener('timeupdate', function () {
    if (a.duration) fill.style.width = (a.currentTime / a.duration * 100) + '%';
  });
  a.addEventListener('ended', function () {
    wrap.classList.remove('playing'); btn.setAttribute('aria-pressed', 'false');
    fill.style.width = '0%'; time.textContent = mmss(a.duration); _nowPlaying = null;
  });
  a.addEventListener('pause', function () {
    wrap.classList.remove('playing'); btn.setAttribute('aria-pressed', 'false');
  });
  a.addEventListener('play', function () {
    wrap.classList.add('playing'); btn.setAttribute('aria-pressed', 'true');
  });

  btn.setAttribute('aria-pressed', 'false');
  btn.onclick = function () {
    if (a.paused) { audioStopAll(a); _nowPlaying = a; a.play().catch(function () {}); }
    else { a.pause(); }
  };
  return wrap;
}

/* A film served from the repo. Same contract as the audio control:
   built hidden, revealed only once the browser confirms it can decode
   the file, removed if it cannot. That check is what catches an
   unplayable profile — the page shows nothing rather than a black box.

   Encode browser-safe or it will not play at all:
     H.264 High profile, yuv420p, AAC audio, +faststart.
   High 4:4:4 Predictive / yuv444p — what several AI video tools emit
   by default — has no decoder in any mainstream browser. */
function videoControl(label, src) {
  if (!src) return null;
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
    var poster = src.replace(/\.(mp4|webm)(\?|$)/i, '.jpg$2');
    if (poster !== src) v.poster = poster;
    if (v.videoWidth && v.videoHeight) {
      fig.style.setProperty('--spk-ar', v.videoWidth + ' / ' + v.videoHeight);
      if (v.videoHeight > v.videoWidth) fig.classList.add('spk-media-tall');
    }
  });
  var fail = function () {
    if (settled) return;
    settled = true;
    fig.remove();                  /* no film, or one no browser can play */
  };
  v.addEventListener('error', fail);
  srcEl.addEventListener('error', fail);
  v.addEventListener('play', function () { audioStopAll(v); _nowPlaying = v; });

  var cap = document.createElement('figcaption');
  cap.className = 'spk-media-cap';
  cap.textContent = label;
  fig.appendChild(v); fig.appendChild(cap);
  return fig;
}

/* A YouTube embed.

   Unlike the two above, this CANNOT be verified from the page — the
   iframe is cross-origin and silent about its own failures. So the
   only check is the one made here: no id, no element. A wrong id will
   render a player showing YouTube's error, which is why ids are
   checked when the lesson is built, not when it loads.

   The iframe is created lazily, on click, behind a still frame. That
   keeps YouTube from being contacted at all unless the student chooses
   to watch — which is both faster and the right default for children.
     rel=0        related videos limited to the same channel
     modestbranding=1  smaller YouTube wordmark
     playsinline=1     iOS plays in place instead of going fullscreen  */
function youtubeControl(label, id) {
  if (!id || !/^[A-Za-z0-9_-]{6,20}$/.test(id)) return null;

  var fig = document.createElement('figure');
  fig.className = 'spk-media spk-media-yt';

  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'spk-yt-poster';
  btn.setAttribute('aria-label', 'Play video: ' + label);
  var img = document.createElement('img');
  img.src = 'https://i.ytimg.com/vi/' + id + '/hqdefault.jpg';
  img.alt = '';
  img.loading = 'lazy';
  var play = document.createElement('span');
  play.className = 'spk-yt-play';
  play.setAttribute('aria-hidden', 'true');
  btn.appendChild(img); btn.appendChild(play);

  btn.onclick = function () {
    audioStopAll(null);
    var f = document.createElement('iframe');
    f.className = 'spk-media-video';
    f.src = MEDIA.ytBase + id +
      '?autoplay=1&rel=0&modestbranding=1&playsinline=1';
    f.title = label;
    f.allow = 'accelerometer; autoplay; encrypted-media; picture-in-picture';
    f.setAttribute('allowfullscreen', '');
    f.setAttribute('frameborder', '0');
    btn.replaceWith(f);
  };

  var cap = document.createElement('figcaption');
  cap.className = 'spk-media-cap';
  cap.textContent = label;
  fig.appendChild(btn); fig.appendChild(cap);
  return fig;
}

/* Build whichever element this slot's `kind` calls for. */
function mediaElement(slot) {
  if (slot.kind === 'audio')   return audioControl(slot.label, mediaSrc(slot));
  if (slot.kind === 'video')   return videoControl(slot.label, mediaSrc(slot));
  if (slot.kind === 'youtube') return youtubeControl(slot.label, slot.yt);
  return null;                                     /* kind:'' — slot off */
}

/* Where a slot mounts. Three anchors, in the order they are tried. */
function mediaMount(slot) {
  var at = slot.at || {};
  if (at.greeting) {
    var say = document.getElementById('spkOpenSay');
    return say ? { host: say.parentNode, before: say.nextSibling } : null;
  }
  if (at.el) {
    var e = document.getElementById(at.el);
    return e ? { host: e.parentNode, before: e.nextSibling } : null;
  }
  if (at.tab) {
    var p = document.getElementById('tab-' + at.tab);
    return p ? { host: p, before: p.firstChild } : null;
  }
  if (at.section) {
    var titles = document.querySelectorAll('.activity-title');
    for (var i = 0; i < titles.length; i++) {
      if (at.section.test(titles[i].textContent || '')) {
        var head = titles[i].closest('.activity-head') ||
                   titles[i].closest('.activity');
        var act  = titles[i].closest('.activity');
        if (!act) return null;
        return { host: act, before: head && head.parentNode === act
                                    ? head.nextSibling : act.firstChild };
      }
    }
  }
  return null;
}

function buildMedia() {
  /* Safe to call more than once. On a first visit the greeting does
     not exist at boot — it appears only after the student enters a
     name — so renderGreeting() calls this again, and each slot checks
     whether it has already been filled. */
  mediaSlots().forEach(function (slot) {
    if (!slot.kind) return;                        /* slot off */
    var m = mediaMount(slot); if (!m) return;      /* nowhere to put it */

    var scope = m.host;
    if (scope.querySelector('[data-spk-slot="' + slot.id + '"]')) return;

    var el = mediaElement(slot); if (!el) return;
    el.setAttribute('data-spk-slot', slot.id);
    if (slot.inline) el.classList.add('spk-audio-inline');
    if (slot.at && (slot.at.tab || slot.at.section)) el.classList.add('spk-guide');

    var wrap = el;
    /* the Reading clip carries what the Watch block used to say, so
       its words go underneath it, folded */
    if (slot.id === 'guide2' && GUIDE_NOTE && GUIDE_NOTE.text) {
      wrap = document.createElement('div');
      wrap.className = 'spk-guide-wrap';
      wrap.setAttribute('data-spk-slot', slot.id);
      wrap.appendChild(el);
      var det = document.createElement('details');
      det.className = 'spk-note';
      var sum = document.createElement('summary');
      sum.textContent = 'Read it instead' +
        (GUIDE_NOTE.title ? ' · ' + titleCase(GUIDE_NOTE.title.toLowerCase()) : '');
      det.appendChild(sum);
      var body = document.createElement('div');
      body.className = 'spk-note-body';
      body.textContent = GUIDE_NOTE.text;        /* never innerHTML */
      det.appendChild(body);
      wrap.appendChild(det);
    }
    m.host.insertBefore(wrap, m.before || null);
  });
}

/* The thematic strand runs all year under a different name per book:
     Virtue Watch      wk 1-5    (Mrs. Frisby)
     Virtue Words      wk 6
     Growing-Up Watch  wk 7-14   (Anne)
     Courage Watch     wk 15-19  (Number the Stars)
     Freedom Watch     wk 20-24  (Freedom Train)
   and nothing after 24.1 — see claude/g4-virtue-strand-survey.md.
   Match the family, not one name, or four fifths of the year is
   missed.

   The block comes off the Reading tab — it was carrying too much, and
   this is the part a teacher would simply have said. Its words are not
   thrown away: they are lifted out first and folded under the Reading
   clip as a transcript, so a student with the sound off, or on a
   lesson whose recording has not been made yet, can still read them.
   Audio is never the only copy. */
function liftWatchBlock() {
  var titles = document.querySelectorAll('.activity-title');
  for (var i = 0; i < titles.length; i++) {
    if (/\b(virtue|growing-up|courage|freedom|belief|character)\s+(watch|words)\b/i.test(titles[i].textContent || '')) {
      var act = titles[i].closest('.activity'); if (!act) return;
      var raw = (titles[i].textContent || '').trim();
      var head = raw.indexOf(':') > -1 ? raw.split(':').slice(1).join(':').trim() : raw;
      var body = act.querySelector('.activity-body');
      GUIDE_NOTE = { title: head, text: body ? (body.innerText || body.textContent || '').trim() : '' };
      act.remove();
      return;
    }
  }
}

/* kept so older call sites keep working */
function buildAudio() { liftWatchBlock(); buildMedia(); }
window.OAO_MEDIA_FNS = { buildMedia: buildMedia, liftWatchBlock: liftWatchBlock, mediaSlots: mediaSlots, mediaSrc: mediaSrc, plateSrc: plateSrc };
function buildGuide() { buildMedia(); }


function buildMemory() {
  var panel = document.getElementById('tab-reading'); if (!panel) return;
  var anchor = panel.querySelector('.tab-next-wrap'); if (!anchor) return;
  var st = memState(), rung = st[LESSON.book].rung;

  var card = document.createElement('div');
  card.className = 'spk-card';
  card.innerHTML =
    '<div class="spk-card-head"><div class="spk-card-num">♪</div><div>' +
    '<div class="spk-card-title">By Heart · “' + DATA.poem.title + '”</div>' +
    '<div class="spk-card-sub">' + DATA.poem.author + ' · one stanza, eight weeks, a little less each week</div>' +
    '</div></div><div class="spk-card-body">' +
    '<div class="spk-rung" id="spkRungLbl"></div>' +
    '<div class="spk-poem" id="spkPoem"></div>' +
    '<div style="display:flex;gap:10px;flex-wrap:wrap;align-items:center;">' +
      '<button type="button" class="spk-btn" id="spkSaidIt">I said it aloud</button>' +
      '<button type="button" class="spk-mini-btn" id="spkMore" style="margin-top:0;">Show a little more</button>' +
      '<span id="spkMemNote" style="font-size:13px;color:#7A88A8;font-style:italic;"></span>' +
    '</div></div>';
  anchor.parentNode.insertBefore(card, anchor);

  function paint(r) {
    var host = document.getElementById('spkPoem'); var s = '';
    DATA.poem.lines.forEach(function (ln, li) {
      var ws = ln[0].split(' ');
      var hide = fadeMask(ws, li, r);
      s += '<div class="' + (ln[1] ? 'ind' : '') + '">' + ws.map(function (w, wi) {
        return '<w class="' + (hide[wi] ? 'faded' : '') + '">' + w + '</w>';
      }).join(' ') + '</div>';
    });
    host.innerHTML = s;
    document.getElementById('spkRungLbl').innerHTML =
      'Rung ' + r + ' of 8' +
      '<span style="text-transform:none;font-family:Lora,Georgia,serif;font-style:italic;font-weight:400;letter-spacing:0;margin-left:8px;">' +
      (r === 1 ? 'the whole stanza — read it aloud twice'
               : r >= 8 ? 'first letters only — you have it'
               : 'a little less to lean on') + '</span>';
  }
  paint(rung);

  document.getElementById('spkMore').onclick = function () {
    paint(Math.max(1, rung - 1));
    setTimeout(function () { paint(rung); }, 8000);
  };
  document.getElementById('spkSaidIt').onclick = function () {
    var m = memState(), today = new Date().toISOString().slice(0, 10);
    var note = document.getElementById('spkMemNote');
    if (m[LESSON.book].advancedOn === today) {
      note.textContent = 'You have climbed a rung today already. Come back tomorrow.'; return;
    }
    if (m[LESSON.book].rung >= 8) { note.textContent = 'You know it by heart. Say it to someone.'; return; }
    m[LESSON.book].rung += 1; m[LESSON.book].advancedOn = today;
    Sparkle.set('oao.g4ela.memory', m);
    rung = m[LESSON.book].rung; paint(rung);
    note.textContent = 'A little less to lean on now.';
    owlSay('Said aloud is how it sticks.');
  };
}

/* ══════════════════════════════════════════════════════════════
   §2.10  ILLUMINATED PUBLISHING + MARGINALIA
   ══════════════════════════════════════════════════════════════ */
function dropCapSVG(letter) {
  return '<svg viewBox="0 0 62 62" width="62" height="62" aria-hidden="true">' +
    '<rect width="62" height="62" rx="3" fill="#0E1C42"/>' +
    '<rect x="3.5" y="3.5" width="55" height="55" rx="2" fill="none" stroke="#FFFDF7" stroke-width="1"/>' +
    '<path d="M8 54 q6 -10 2 -18 q8 5 9 -3 M54 8 q-6 10 -2 18 q-8 -5 -9 3" stroke="#C7922C" stroke-width="1.4" fill="none" stroke-linecap="round" opacity=".85"/>' +
    '<circle cx="10" cy="11" r="2" fill="#C7922C"/><circle cx="52" cy="51" r="2" fill="#C7922C"/>' +
    '<text x="31" y="45" font-size="38" text-anchor="middle" font-family="Lora,Georgia,serif" font-weight="700" fill="#C7922C">' +
    letter + '</text></svg>';
}

function renderIllumAuthor() {
  var by = document.querySelector('.spk-illum .spk-by'); if (!by) return;
  var p = profile();
  by.textContent = 'by ' + (p ? p.name : 'a fourth-grade writer') +
    ' · Optima Academy Online · ' + LESSON.bookTitle + ' unit';
}

function buildPublish() {
  var actions = document.querySelector('.gathered-actions'); if (!actions) return;
  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'gathered-btn'; btn.style.cssText = 'background:#C7922C;color:#fff;';
  btn.innerHTML = '✒️ Publish My Writing';
  actions.appendChild(btn);

  var page = document.createElement('div');
  page.className = 'spk-illum'; page.id = 'spkIllum'; page.style.display = 'none';
  page.innerHTML =
    '<h2 id="spkIllumTitle"></h2><div class="spk-by"></div>' +
    '<div class="spk-illum-seal" id="spkIllumSeal"></div>' +
    '<div class="spk-illum-body" id="spkIllumBody"></div>' +
    '<div class="spk-colophon" id="spkColophon"></div>';
  actions.parentNode.appendChild(page);
  renderIllumAuthor();

  btn.onclick = function () {
    var src = document.getElementById('journal-writing');
    var text = (src && src.value.trim()) || '';
    if (!text) {
      text = 'Write your Writer’s Workshop piece above, then press Publish again — this page is where it goes.';
    }
    var first = text.charAt(0).toUpperCase(), rest = text.slice(1);
    document.getElementById('spkIllumTitle').textContent = 'Week ' + LESSON.week + ' · Voice';
    var body = document.getElementById('spkIllumBody');
    body.innerHTML = '<span class="spk-dropcap">' + dropCapSVG(first) + '</span>';
    var para = document.createElement('span');
    para.textContent = rest;                       /* never innerHTML with student text */
    body.appendChild(para);
    renderIllumAuthor();
    var sealSlot = document.getElementById('spkIllumSeal');
    sealSlot.innerHTML = hasSeal() ? laurelSVG(72) : '';
    document.getElementById('spkColophon').textContent =
      (hasSeal() ? 'Written on the Scholar’s road. ' : '') +
      'Set down at Optima Academy Online on ' +
      new Date().toLocaleDateString(undefined, { year: 'numeric', month: 'long', day: 'numeric' }) + '.';
    page.style.display = 'block';
    page.scrollIntoView({ behavior: REDUCED ? 'auto' : 'smooth', block: 'start' });
    owlSay('A page worth keeping.');
  };
}

function marginalia() {
  ['morphNotice', 'spellReveal', 'g4w7SRev', 'dolAns'].forEach(function (id) {
    var el = document.getElementById(id); if (el) el.classList.add('spk-marginalia');
  });
  document.querySelectorAll('.flip-card-back').forEach(function (b) { b.classList.add('spk-marginalia'); });
  /* emoji out of reveal bodies (§2.10); buttons keep theirs */
  var EMO = /(✅|🔍|📖|🧩|🎉|✨|🌱)️?\s*/g;
  document.querySelectorAll('.dol-answer, .flip-card-back, .decode-reveal, .sort-score, .fillin-feedback, .match-feedback').forEach(function (el) {
    var walk = document.createTreeWalker(el, NodeFilter.SHOW_TEXT, null, false), t;
    while ((t = walk.nextNode())) { t.nodeValue = t.nodeValue.replace(EMO, ''); }
  });
  document.querySelectorAll('.sort-game[data-win]').forEach(function (g) {
    g.setAttribute('data-win', g.getAttribute('data-win').replace(EMO, ''));
  });
}

/* ══════════════════════════════════════════════════════════════
   HOOKS into the lesson's own functions
   ══════════════════════════════════════════════════════════════ */
function hookProgress() {
  var _orig = window.updateProgress;
  window.updateProgress = function () {
    var r = _orig.apply(this, arguments);
    var visited = [].slice.call(document.querySelectorAll('.tab-btn.visited'))
      .map(function (b) { return b.getAttribute('data-tab'); });
    markTabs(visited);
    var total = document.querySelectorAll('.tab-btn').length;
    if (visited.length >= total) {
      var finishedBook = markDone();
      if (!window._spkComplete) {
        window._spkComplete = true;
        var p = profile();
        if (!finishedBook) owlSay(OWL.complete + (p ? ', ' + p.name : '') + '.');
      }
    }
    drawDots();
    drawMapIfPresent();
    return r;
  };
}

function hookTabs() {
  var _orig = window.switchTab;
  window.switchTab = function (tabId) {
    var out = document.querySelector('.tab-panel.active');
    var r = _orig.apply(this, arguments);
    var plate = document.querySelector('.spk-plate');
    if (plate) plate.classList.toggle('spk-folded', tabId !== 'warmup');
    var next = document.getElementById('tab-' + tabId);
    if (next && !REDUCED && out !== next) {
      next.classList.remove('spk-in'); void next.offsetWidth; next.classList.add('spk-in');
      var voice = next.querySelector('.tab-transition-voice');
      if (voice) { voice.style.opacity = '0'; setTimeout(function () { voice.style.transition = 'opacity .2s'; voice.style.opacity = ''; }, 200); }
    }
    return r;
  };
}

function hookGather() {
  var _orig = window.gatherAnswers;
  window.gatherAnswers = function () {
    var r = _orig.apply(this, arguments);
    var out = document.getElementById('gatheredOutput'); if (!out) return r;
    var extra = '\n—— SPARKLE ——\n';
    extra += 'Question path: ' + (currentTier() === 'scholar' ? 'Scholar' : 'Explorer') + '\n';
    if (hasSeal()) extra += 'THE SCHOLAR\u2019S SEAL \u2014 all three answers given with evidence.\n';
    var dol = Sparkle.get('oao.g4ela.dol', {})[LID];
    if (dol) extra += 'DOL sentence chosen: ' + dol.toUpperCase() + '\n';
    var helped = Object.keys(window._spkRevealed || {});
    if (helped.length) extra += 'Answered with help: ' + helped.join(', ') + '\n';
    var copia = ['journal-copia1', 'journal-copia2', 'journal-copia3']
      .map(function (id) { var e = document.getElementById(id); return e && e.value.trim() ? e.value.trim() : null; })
      .filter(Boolean);
    if (copia.length) {
      extra += '\n✎ COPIA — SAY IT THREE WAYS\n────────────────\n';
      copia.forEach(function (c, i) { extra += (i + 1) + '. ' + c + '\n'; });
    }
    out.value += extra;
    return r;
  };
}

/* ══════════════════════════════════════════════════════════════
   BOOT
   ══════════════════════════════════════════════════════════════ */
function ornaments() {
  var o = ART.ornaments || {}, root = document.documentElement;
  ['divider', 'corner', 'quill', 'blossom', 'books', 'letter', 'sprig', 'divider2'].forEach(function (k) {
    var u = artURL(o[k]);
    if (u) root.style.setProperty('--spk-orn-' + k, 'url("' + u + '")');
  });
  if (!artURL(o.divider)) return;
  /* a rule at the close of each tab, and under the opening card */
  /* two dividers now, alternating, so four section breaks in a row do
     not print the same sprig four times */
  var alt = !!artURL(o.divider2), n = 0;
  document.querySelectorAll('.tab-next-wrap').forEach(function (w) {
    var d = document.createElement('div');
    d.className = 'spk-divider' + (alt && (n++ % 2) ? ' spk-divider-b' : '');
    d.setAttribute('aria-hidden', 'true');
    w.parentNode.insertBefore(d, w);
  });
  dividerAfterOpening();
}
/* called again after the greeting card is created, because on a first
   visit that happens after ornaments() has already run */
function dividerAfterOpening() {
  if (!artURL((ART.ornaments || {}).divider)) return;
  var open = document.getElementById('spkGreet');
  if (!open || open.nextElementSibling && open.nextElementSibling.classList.contains('spk-divider')) return;
  var d = document.createElement('div');
  d.className = 'spk-divider'; d.setAttribute('aria-hidden', 'true');
  open.parentNode.insertBefore(d, open.nextSibling);
}

/* ══════════════════════════════════════════════════════════════
   §2.14  DECLUTTER

   Four small removals, all additive: the original file is untouched,
   and dropping the sparkle layer puts every one of them back.
   ══════════════════════════════════════════════════════════════ */
function declutter() {
  /* 1. Today's Path and the You'll-need strip. Both restate the tab bar
     and the materials the student already has in front of them, and
     they sit in the most valuable space on the page — above the fold,
     before the lesson starts. */
  ['.todays-path', '.need-strip'].forEach(function (sel) {
    document.querySelectorAll(sel).forEach(function (el) { el.remove(); });
  });

  /* 2. The "you don't have to write this down" reassurances. They sit
     under prompts that are already marked as thinking prompts, so they
     tell a student something the page has just told them — 295 times
     across 102 of the 129 files, six different wordings, which is why
     matching one string was not enough.

     The rule is whole-line: a thinking-stop goes only when reassurance
     is ALL it says. Anything that also carries a direction survives —
     "Hold this question in your mind as you read", "you'll answer
     these in the Assignment", every "Think: …" prompt. That leaves
     181 of the 476 standing, which are the ones doing work. */
  var FILLER = new RegExp(
    '^(?:\\u{1F4AD}\\s*)?(?:' +
      "pause and think(?: about this)?\\s*-\\s*no need to write(?: here)?" +
      "|think about this as you read today\\s*-\\s*you don't need to write anything here" +
      "|think:?\\s*no need to write\\s*-\\s*just carry this question into your reading" +
      "|let this question sit with you\\s*-\\s*you don't need to write anything here" +
    ')\\.?$', 'iu');
  document.querySelectorAll('.thinking-stop').forEach(function (el) {
    var t = (el.textContent || '')
      .replace(/[\u2018\u2019]/g, "'")        /* curly apostrophes */
      .replace(/[\u2013\u2014]/g, '-')        /* en and em dashes  */
      .replace(/\s+/g, ' ').trim();
    if (FILLER.test(t)) el.remove();
  });
}

/* 3. Changing tabs used to jump to the top of the page. That is
   disorienting: a student two thirds of the way down Word Study clicks
   Reading and is thrown back to the header. The tab bar is sticky, so
   there is nothing to go back up for. This holds the scroll position
   across the switch by suppressing the original's scrollIntoView for
   the length of the call, then putting the scroll back. */
function hookTabScroll() {
  if (typeof window.switchTab !== 'function') return;
  var inner = window.switchTab;
  window.switchTab = function (tabId) {
    var y = window.pageYOffset || document.documentElement.scrollTop || 0;
    var top = document.getElementById('pageTop');
    var real = top && top.scrollIntoView;
    if (real) top.scrollIntoView = function () {};     /* muzzle it */
    try { return inner.apply(this, arguments); }
    finally {
      if (real) top.scrollIntoView = real;
      /* the browser may still settle a frame later, so put it back
         twice rather than fight the timing */
      window.scrollTo(0, y);
      requestAnimationFrame(function () { window.scrollTo(0, y); });
    }
  };
}

function boot() {
  /* Each step is isolated. Previously all eighteen sat inside one
     try/catch, so a lesson whose DATA was missing a key — no DOL pair,
     no copia seed — threw in the middle and silently skipped every step
     after it: no guiding voice, no ornaments, no declutter, and only a
     console warning to say so. Rolling this across 129 lessons, that
     failure mode would have been invisible and common.

     Now a builder that throws costs exactly its own feature. The names
     are logged so a broken lesson says which piece is missing. */
  var steps = [
    ['warm',        function () { document.body.classList.add('spk-warm'); }],
    ['hooks',       function () { hookProgress(); hookTabs(); hookGather(); hookTabScroll(); }],
    ['declutter',   declutter],
    ['numeral',     buildNumeral],
    ['plate',       buildPlate],
    ['writing',     buildWritingProject],
    ['journey',     buildJourney],
    ['greeting',    function () {
        if (profile()) renderGreeting();
        else if (LESSON.day === 1) showProfileCard(false);
    }],
    ['dol',         buildDolChoice],
    ['tiers',       buildTiers],
    ['coaches',     buildCoaches],
    ['copia',       buildCopia],
    ['memory',      buildMemory],
    ['watch',       liftWatchBlock],
    ['media',       buildMedia],
    ['publish',     buildPublish],
    ['marginalia',  marginalia],
    ['ornaments',   ornaments],
    ['seal',        function () { sealCheck(true); }],
    ['progress',    function () { if (window.updateProgress) window.updateProgress(); }]
  ];
  var failed = [];
  for (var i = 0; i < steps.length; i++) {
    try { steps[i][1](); }
    catch (e) {
      failed.push(steps[i][0]);
      if (window.console && console.warn) console.warn('[sparkle] ' + steps[i][0] + ' failed:', e);
    }
  }
  if (failed.length && window.console && console.warn) {
    console.warn('[sparkle] ' + failed.length + ' of ' + steps.length +
                 ' steps did not run: ' + failed.join(', '));
  }
  window.OAO_SPARKLE_FAILED = failed;   /* the sweep asserts this is empty */
}


if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', boot);
else boot();

})();
