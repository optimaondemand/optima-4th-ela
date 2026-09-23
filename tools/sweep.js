/*
 * sweep.js — regression sweep for a sparkled G4 ELA lesson.
 *
 *     node tools/sweep.js lesson-7-2-anne-ch2.html
 *
 * Serves the REPO over http on a scratch port and loads the lesson from
 * there. That matters: art and the layer are referenced, not embedded,
 * so a file:// load would silently show a lesson with no map, no
 * ornaments and no stylesheet — and every assertion below would be
 * testing the wrong page.
 *
 * Run from the repo root. Exits non-zero if any INVARIANT fails.
 */
const { chromium } = require('playwright');

/* Chromium lives in different places on different machines. The cloud
   container has one at /opt/pw-browsers; a normal install has its own.
   Try the container path, then let Playwright find its own. */
function launch() {
  const pinned = process.env.SWEEP_CHROMIUM || '/opt/pw-browsers/chromium';
  if (fs.existsSync(pinned)) return chromium.launch({ executablePath: pinned });
  return chromium.launch();      /* whatever `npx playwright install` put down */
}
const http = require('http');
const fs   = require('fs');
const path = require('path');

const REL = process.argv[2];
if (!REL) { console.error('usage: node tools/sweep.js <lesson.html>'); process.exit(2); }
const ROOT = process.cwd();
const ABS  = path.join(ROOT, REL);
if (!fs.existsSync(ABS)) { console.error('no such file: ' + ABS); process.exit(2); }

const TYPES = { '.html':'text/html', '.css':'text/css', '.js':'text/javascript',
  '.json':'application/json', '.png':'image/png', '.jpg':'image/jpeg',
  '.jpeg':'image/jpeg', '.svg':'image/svg+xml', '.mp3':'audio/mpeg',
  '.mp4':'video/mp4', '.webm':'video/webm', '.woff2':'font/woff2' };

const missing = [];            /* every 404 the page asked for */
const server = http.createServer((req, res) => {
  const rel = decodeURIComponent(req.url.split('?')[0]).replace(/^\/+/, '');
  const file = path.join(ROOT, rel);
  if (!file.startsWith(ROOT) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) {
    missing.push(rel); res.writeHead(404); res.end('nope'); return;
  }
  res.writeHead(200, { 'Content-Type': TYPES[path.extname(file).toLowerCase()] || 'application/octet-stream' });
  fs.createReadStream(file).pipe(res);
});

const errs = [];

(async () => {
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  const FILE = 'http://127.0.0.1:' + server.address().port + '/' +
               path.relative(ROOT, ABS).split(path.sep).join('/');
  console.log('serving ' + ROOT + '\n   ->  ' + FILE + '\n');

  const browser = await launch().catch(e => {
    console.error('could not start Chromium: ' + e.message +
      '\nIf this is a fresh machine, run:  npx playwright install chromium');
    process.exit(2);
  });
  const ctx = await browser.newContext({ viewport: { width: 1100, height: 900 } });
  const page = await ctx.newPage();
  page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') errs.push(m.type()+': '+m.text()); });
  page.on('pageerror', e => errs.push('pageerror: ' + e.message));
  page.on('dialog', d => d.accept());

  await page.goto(FILE);
  const R = {};

  /* ── safe probes ──────────────────────────────────────────────
     The sweep runs on any lesson, and lessons differ: 7.1 has a sort
     bank, 7.2 does not; days 2 and 4 carry Poetry Corner, days 1 and 3
     do not. An assertion pinned to one lesson's element ids does not
     "fail" on another lesson — it HANGS for 30 seconds and then throws,
     which tells you nothing about the page.

     So every probe below is total: absent is a reportable value, not an
     exception. Only a real invariant is allowed to fail the run. */
  const SHORT = 1200;
  const has  = async sel => (await page.locator(sel).count()) > 0;
  const txt  = async sel => (await has(sel))
      ? (await page.locator(sel).first().innerText().catch(() => '(unreadable)')).trim()
      : '(absent)';
  const vis  = async sel => (await has(sel))
      ? await page.locator(sel).first().isVisible().catch(() => false) : '(absent)';
  const cnt  = async sel => await page.locator(sel).count();
  const tap  = async sel => { if (await has(sel)) {
      await page.locator(sel).first().click({ timeout: SHORT }).catch(() => {}); return true; }
      return false; };
  const type = async (sel, v) => { if (await has(sel)) {
      await page.locator(sel).first().fill(v, { timeout: SHORT }).catch(() => {}); return true; }
      return false; };


  // ── 2.1 first-visit profile card
  R['no build step failed'] = await page.evaluate(() => window.OAO_SPARKLE_FAILED || 'UNDEFINED');
  R['profile card shows on 7.1'] = await vis('#spkProfileCard');
  await type('#spkNameInput', '<script>Nora');
  R['companion picker (1 art = no picker)'] = await cnt('.spk-owl-pick');
  R['companion introduced'] = await cnt('.spk-companion-solo');
  await tap('#spkBegin');
  await page.waitForTimeout(150);
  R['greeting'] = (await txt('#spkGreet')).replace(/\n/g, ' ').trim();
  R['name rendered as text only'] = await page.evaluate(() => {
    const el = document.getElementById('spkGreetName');
    if (!el) return '(no greeting on this lesson)';
    return el.querySelectorAll('*').length === 0 &&
           el.textContent.indexOf('<') === -1;
  });
  R['header logo is still Optima'] = await page.evaluate(() => {
    const i = document.querySelector('.header-logo img');
    return !!i && getComputedStyle(i).display !== 'none' && /optima-assets/.test(i.src) &&
           document.querySelectorAll('.header-logo .spk-owl-avatar').length === 0;
  });
  R['no script injected'] = await page.evaluate(() => document.querySelectorAll('#spkGreet script').length);

  // ── 2.2 the "This week" dot row was removed; nothing should remain
  R['week dot row gone'] = await cnt('#spkTrack');

  // ── 2.2/2.3 the Reading Road now lives on the Reading tab (checked below)

  // ── 2.5 DOL choice
  R['dol cards'] = await cnt('.spk-dol-card');
  await tap('.spk-dol-card[data-pick="b"]');
  await page.waitForTimeout(220);
  R['dol other folded'] = (await has('.spk-dol-card[data-pick="a"]') ? await page.locator('.spk-dol-card[data-pick="a"]').first().isHidden() : '(absent)');
  await tap('.dol-check-btn');
  await page.waitForTimeout(200);
  R['dol answer B'] = (await txt('#dolAns')).slice(0, 60);

  // ── word study tab
  await tap('.tab-btn[data-tab="words"]');
  await page.waitForTimeout(400);

  // ── 2.7 hint ladder, three tries
  const ladder = [];
  for (let i = 0; i < 3; i++) {
    await type('#fill1', 'zzz');
    await tap('#fillinGame .fillin-check-btn');
    await page.waitForTimeout(180);
    ladder.push((await has('#fill1'))
      ? (await page.locator('#fill1').locator('xpath=..').locator('.spk-hint')
           .first().innerText({ timeout: SHORT }).catch(() => '(no hint)')).slice(0, 48)
      : '(no fill-in on this lesson)');
  }
  R['hint ladder'] = ladder;
  R['fill1 revealed+disabled'] = await page.evaluate(() => {
    const e = document.getElementById('fill1');
    if (!e) return '(no fill-in on this lesson)';
    return [e.value, e.disabled, e.classList.contains('spk-revealed')];
  });

  // finish the rest correctly
  await type('#fill2', 'com'); await type('#fill3', 'com'); await type('#fill4', 'con');
  await tap('#fillinGame .fillin-check-btn');
  await page.waitForTimeout(200);
  R['fillin feedback shown'] = await vis('#fillinFeedback');

  // ── 2.7 distractor line on the match game
  await tap('#matchGrid .match-item.is-word:has-text("placid")');
  await tap('#matchGrid .match-item:has-text("A feeling of great pleasure")');
  await page.waitForTimeout(250);
  R['match miss line'] = await cnt('.spk-miss') ? (await txt('.spk-miss')) : '(none)';

  // ── 2.7 distractor on the sort game
  await tap('#g4w7SBank .sort-chip:has-text("child")');
  await tap('#g4w7S .sort-col-drop[data-col="regular"]');
  await page.waitForTimeout(250);
  R['sort miss line'] = await cnt('#g4w7S .spk-miss') ? await txt('#g4w7S .spk-miss') : '(none)';

  // ── 2.8 copia
  R['copia card on day 2 tab'] = await cnt('.spk-copia-seed');
  await type('#journal-copia1', 'Every afternoon, Mrs. Rachel Lynde sat at her window.');
  await tap('.spk-mini-btn[data-eg="0"]');
  await page.waitForTimeout(150);
  R['copia example reveal'] = (await txt('.spk-copia-eg')).slice(0, 40);

  // ── reading tab: 2.9 memory ladder
  await tap('.tab-btn[data-tab="reading"]');
  await page.waitForTimeout(400);
  // the Reading Road now folds, and starts closed
  R['road starts folded'] = await page.evaluate(() => document.getElementById('spkRoadBody').hidden);
  R['Growing-Up Watch block removed'] = await page.evaluate(() =>
    ![...document.querySelectorAll('.activity-title')].some(t => /growing-up watch/i.test(t.textContent)));
  R['its words kept as a transcript'] = await page.evaluate(() => {
    const n = document.querySelector('#tab-reading .spk-note-body');
    return n ? n.textContent.trim().split(/\s+/).length + ' words' : 'MISSING';
  });
  await tap('#spkRoadFold');
  await page.waitForTimeout(700);
  R['shelf covers'] = [await cnt('.spk-book'), await cnt('.spk-book.has-cover')];
  R['no broken images'] = await page.evaluate(() => [...document.images].filter(i => i.complete && i.naturalWidth === 0).length);
  R['map spaces (40 painted)'] = await cnt('#spkMap .spk-space');
  R['board: done / here / ahead'] = [await cnt('#spkMap .spk-done'), await cnt('#spkMap .spk-here'), await cnt('#spkMap .spk-ahead')];
  R['board art loaded (by path, not embedded)'] = await page.evaluate(() => {
    const i = document.querySelector('#spkMap image');
    if (!i) return 'NO IMAGE';
    const href = i.getAttribute('href') || '';
    if (/^data:/.test(href)) return 'FAIL: embedded as a data URI';
    return /year-board/.test(href) ? href : ('unexpected href: ' + href);
  });
  R['map text (name + week badge)'] = await page.evaluate(() => [...document.querySelectorAll('#spkMap text')].map(t => t.textContent));
  R['here line'] = await txt('#spkHere');
  R['spaces travelled'] = await page.evaluate(() =>
    [...document.querySelectorAll('#spkMap .spk-space')].filter(g => g.classList.contains('spk-done')).length);
  R['books behind us are on the shelf'] = [await cnt('.spk-book.read'), await cnt('.spk-book')];
  R['old atlas/strip gone'] = await cnt('#spkAtlas, #spkStrip');
  R['poem lines'] = await cnt('#spkPoem div');
  R['rung 1 label'] = await txt('#spkRungLbl');
  R['rung1 faded words'] = await cnt('#spkPoem w.faded');
  await tap('#spkSaidIt');
  await page.waitForTimeout(200);
  R['rung 2 label'] = await txt('#spkRungLbl');
  R['rung2 faded words'] = await cnt('#spkPoem w.faded');
  await tap('#spkSaidIt');
  R['second advance same day blocked'] = await txt('#spkMemNote');

  // ── assignment tab: tiers + coaching + publish
  await tap('.tab-btn[data-tab="assignment"]');
  await page.waitForTimeout(400);
  R['two roads present'] = await cnt('.spk-road');
  await tap('.spk-road[data-tier="scholar"]');
  await page.waitForTimeout(120);
  R['scholar clause visible'] = await vis('.spk-scholar-add[data-for="journal-q1"]');

  await type('#journal-q3', 'She decides to go over to Green Gables.');
  await page.waitForTimeout(700);
  R['coach: short (scholar 20w)'] = await txt('.spk-coach[data-for="journal-q3"]');
  await type('#journal-q3', 'Mrs. Rachel decides she will walk straight over to Green Gables that very evening and find out the whole story from Marilla herself.');
  await page.waitForTimeout(700);
  R['coach: needs quote'] = await txt('.spk-coach[data-for="journal-q3"]');
  await type('#journal-q3', 'Mrs. Rachel decides to go to Green Gables because she cannot bear not knowing, and the book calls her "a notable housewife" who still finds time for everyone else’s business.');
  await page.waitForTimeout(700);
  R['coach: evidence'] = await txt('.spk-coach[data-for="journal-q3"]');

  await type('#journal-q2', 'Avonlea is quiet and green.');
  await page.waitForTimeout(700);
  R['coach: two details'] = await txt('.spk-coach[data-for="journal-q2"]');

  await type('#journal-writing', 'My story is about a girl who moves to a new town and learns about imagination.');
  await page.waitForTimeout(300);
  await tap('.gathered-actions button:has-text("Publish")');
  await page.waitForTimeout(400);
  R['illuminated page'] = await vis('#spkIllum');
  R['drop cap letter'] = await page.evaluate(() => document.querySelector('#spkIllum .spk-dropcap text').textContent);
  R['author line'] = await txt('#spkIllum .spk-by');

  R['seal before'] = await txt('#spkSealStrip');
  for (const [id, txt] of [
    ['journal-q1','Mrs. Rachel notices that Matthew Cuthbert has driven off in his best suit in the middle of the afternoon, and it bothers her because she cannot think of one errand that would explain it.'],
    ['journal-q2','Avonlea is a quiet village set down in a hollow with a brook running through it, and the road is lined with orchards, so everybody can see everybody else.'],
    ['journal-q3','She decides to walk to Green Gables that evening because the book calls her "a notable housewife" who still found time for everyone else, and that shows she is nosy.']]) {
    await type('#' + id, txt); await page.waitForTimeout(650);
  }
  await page.waitForTimeout(400);
  R['seal earned'] = (await txt('#spkSealStrip')).slice(0, 90);
  R['section illuminated'] = await cnt('.activity.spk-illuminated');

  // ── export additions
  R['export tail'] = (await page.inputValue('#gatheredOutput')).split('—— SPARKLE ——')[1] || '(missing)';

  // ── progress + storage
  R['progress pct'] = await txt('#progressPct');
  R['storage'] = await page.evaluate(() => {
    const o = {};
    ['oao.g4ela.scholar','oao.profile','oao.g4ela.progress','oao.g4ela.books','oao.g4ela.hints','oao.g4ela.tier','oao.g4ela.memory','oao.g4ela.dol']
      .forEach(k => o[k] = localStorage.getItem(k));
    return o;
  });

  // ── emoji gone from reveal bodies
  R['emoji left in reveals'] = await page.evaluate(() => {
    const re = /[✅\u{1F50D}\u{1F389}✨\u{1F331}\u{1F4D6}\u{1F9E9}]/u;
    return [...document.querySelectorAll('.dol-answer, .flip-card-back, .decode-reveal, .sort-score, .fillin-feedback, .match-feedback')]
      .filter(e => re.test(e.textContent)).map(e => e.id || e.className).slice(0, 5);
  });

  // ── §5 graceful degradation: same page with storage throwing
  const p2 = await ctx.newPage();
  p2.on('pageerror', e => errs.push('nostorage pageerror: ' + e.message));
  await p2.addInitScript(() => {
    Object.defineProperty(window, 'localStorage', { get() { throw new Error('blocked'); } });
  });
  await p2.goto(FILE);
  await p2.waitForTimeout(400);
  R['no-storage: page still renders tabs'] = await p2.locator('.tab-btn').count();
  await p2.click('.tab-btn[data-tab="words"]');
  await p2.waitForTimeout(300);
  R['no-storage: tab switch works'] = await p2.locator('#tab-words').isVisible();

  // ── reduced motion pass
  const p3 = await ctx.newPage();
  p3.on('pageerror', e => errs.push('reduced pageerror: ' + e.message));
  await p3.emulateMedia({ reducedMotion: 'reduce' });
  await p3.goto(FILE);
  await p3.waitForTimeout(400);
  R['reduced-motion: greeting (returning student)'] =
    (await p3.locator('#spkGreet').count())
      ? (await p3.locator('#spkGreet').first().innerText()).replace(/\n/g,' ').trim()
      : '(no greeting — first visit on this lesson)';
  R['reduced-motion: no pulse class'] = await p3.locator('#spkDots .spk-dot.current.pulse').count();


  /* ── the invariants that protect the rollout ─────────────────
     Each of these has already gone wrong once, or would cost 129
     files to undo if it went wrong silently. */
  const raw = fs.readFileSync(ABS, 'utf8');
  const bytes = Buffer.byteLength(raw);
  R['INVARIANT no data:image in the file'] = (raw.match(/data:image/g) || []).length;
  R['INVARIANT file size (bytes)'] = bytes;
  R['INVARIANT layer is linked, not pasted'] =
    /<link[^>]+sparkle\.css/.test(raw) && /<script[^>]+sparkle\.js/.test(raw);
  R['INVARIANT injected exactly once'] = (raw.match(/OAO SPARKLE LAYER/g) || []).length;
  /* A plate or a clip that has not been recorded yet is EXPECTED to
     404 — the control hides itself and the lesson is fine. Only list
     the ones that mean something is actually broken. */
  R['404s (art/audio not supplied yet — expected)'] =
    [...new Set(missing.filter(m => /^assets\/(plates|audio|video)\//.test(m)))];
  R['INVARIANT unexpected 404s'] =
    [...new Set(missing.filter(m => !/^assets\/(plates|audio|video)\//.test(m) && m !== 'favicon.ico'))];
  R['media slots mounted'] = await page.evaluate(() =>
    [...document.querySelectorAll('[data-spk-slot]')].map(e => e.getAttribute('data-spk-slot')));
  R['slots switched on in the manifest'] = await page.evaluate(() =>
    (window.OAO_MEDIA ? window.OAO_MEDIA.slots : []).filter(s => s.kind).map(s => s.id + ':' + s.kind));
  R['plate'] = await page.evaluate(() => {
    const i = document.querySelector('.spk-plate img');
    return i ? i.getAttribute('src') : '(none yet — art not supplied)';
  });

  console.log(JSON.stringify(R, null, 1));
  console.log('\n=== console errors/warnings ===');
  console.log(errs.length ? errs.join('\n') : 'NONE');

  /* A missing plate or clip is expected and fine. A 404 for the
     stylesheet, the script or the year map is not. */
  const fatal404 = missing.filter(m =>
    !/^assets\/(plates|audio|video)\//.test(m) && !/^favicon\.ico$/.test(m));
  const fail = [];
  if (R['no build step failed'] && R['no build step failed'].length) fail.push('build steps failed: ' + R['no build step failed']);
  if (R['INVARIANT no data:image in the file'] > 0) fail.push('data: URIs found in the file');
  if (!R['INVARIANT layer is linked, not pasted']) fail.push('sparkle.css/js not linked');
  if (R['INVARIANT injected exactly once'] !== 1) fail.push('layer injected ' + R['INVARIANT injected exactly once'] + ' times');
  if (bytes > 260000) fail.push('file is ' + bytes + ' bytes — something got inlined');
  if (fatal404.length) fail.push('404: ' + fatal404.join(', '));
  if (String(R['board art loaded (by path, not embedded)']).startsWith('FAIL')) fail.push('board art embedded');

  console.log('\n=== verdict ===');
  if (fail.length) { console.log('FAILED\n  - ' + fail.join('\n  - ')); }
  else { console.log('PASS'); }

  await browser.close();
  server.close();
  process.exit(fail.length ? 1 : 0);
})();

