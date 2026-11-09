// Play a built G4 ELA VR page end to end in Chromium.
// usage: node tools/vr/playtest_vr.js 7 [port]   (run from the repo root; serves the repo itself)
// Both paths at 1150 and 420 px: the 6 required VR steps -> keepsake; help drawer images load;
// Window Seat Day: a wrong pick and a wrong stop first, then the right ones -> bookmark; paragraph chips; PDF.
const { chromium } = require('playwright');
const http = require('http'), fs = require('fs'), path = require('path');
const W = process.argv[2] || '7', PORT = +(process.argv[3] || 8765), ROOT = process.cwd();
const TYPES = { '.html': 'text/html', '.jpg': 'image/jpeg', '.png': 'image/png', '.mp3': 'audio/mpeg', '.js': 'text/javascript', '.css': 'text/css' };
const srv = http.createServer((q, r) => {
  const f = path.join(ROOT, decodeURIComponent(q.url.split('?')[0]));
  if (!f.startsWith(ROOT) || !fs.existsSync(f) || fs.statSync(f).isDirectory()) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { 'content-type': TYPES[path.extname(f)] || 'application/octet-stream' }); fs.createReadStream(f).pipe(r);
}).listen(PORT);

(async () => {
  const browser = await chromium.launch(); let fails = 0;
  const ok = (c, m) => { console.log((c ? '  ✓ ' : '  ✗ ') + m); if (!c) fails++; };
  const data = JSON.parse(fs.readFileSync(path.join(ROOT, 'tools/vr/week' + W + '.json'), 'utf8'));
  for (const width of [1150, 420]) {
    console.log('— ' + width + ' px');
    const page = await browser.newPage({ viewport: { width, height: 900 } }), errs = [];
    page.on('pageerror', e => errs.push(e.message));
    page.on('console', m => { if (m.type() === 'error' && !/404|Failed to load|ERR_|net::/.test(m.text())) errs.push(m.text()); });
    await page.goto(`http://localhost:${PORT}/vr-${W}.html`); await page.evaluate(() => localStorage.clear()); await page.reload();
    ok(await page.$eval('#pb-vr', b => b.getAttribute('aria-pressed')) === 'true', 'Imagination Trip is the default path');
    const scrollW = () => page.evaluate(() => document.documentElement.scrollWidth - innerWidth);
    ok(await scrollW() <= 0, 'no horizontal scroll (VR)');
    const chks = await page.$$('#vr-steps .chk');
    for (const i of [0, 1, 2, 3, 5]) await chks[i].click();
    ok(!(await page.$eval('#vr-done', d => d.classList.contains('show'))), 'keepsake waits for step 7');
    await chks[6].click();
    ok(await page.$eval('#vr-done', d => d.classList.contains('show')), 'keepsake shows after the 6 required steps (Extra skipped)');
    await page.click('#vr-help summary');
    await page.$$eval('#vr-help img', a => a.forEach(i => { i.loading = 'eager'; }));
    await page.waitForTimeout(800);
    const imgs = await page.$$eval('#vr-help img', a => a.map(i => i.complete && i.naturalWidth > 0));
    ok(imgs.length === 14 && imgs.every(Boolean), 'help drawer: 14 images load');
    ok(await page.$('#vr-help iframe') !== null, 'help video loads on open');
    if (width === 1150) await page.screenshot({ path: `/tmp/vr${W}-vr-${width}.png`, fullPage: true });

    await page.click('#pb-alt');
    ok(await page.$eval('#vr', s => getComputedStyle(s).display) === 'none', 'Window Seat Day hides the VR card');
    ok(await page.$$eval('.stop', b => b.every(x => x.disabled)), 'order is locked until part 1 is done');
    const R = data.alt.rename;
    for (let i = 0; i < R.length; i++) {
      const wrong = R[i].ok === 0 ? 1 : 0;
      await page.click(`.ropt[data-i="${i}"][data-k="${wrong}"]`);
      if (i === 0) ok(!(await page.$eval('#g-msg', m => m.classList.contains('ok'))), 'a wrong name gets a nudge');
      await page.click(`.ropt[data-i="${i}"][data-k="${R[i].ok}"]`);
    }
    const order = data.alt.order;
    await page.click(`.stop[data-k="${order.length - 1}"]`);
    ok(await page.$$eval('.ms.on', a => a.length) === 0, 'a stop out of order is not placed');
    for (let k = 0; k < order.length; k++) await page.click(`.stop[data-k="${k}"]`);
    ok(await page.$eval('#bmark', b => b.classList.contains('show')), 'bookmark shows when the game is done');
    ok(await scrollW() <= 0, 'no horizontal scroll (Window Seat Day)');
    const para = 'Anne renamed the Avenue. She called it the White Way of Delight because the apple trees were all white with blossoms over the road. ' +
      'The plain name had no meaning for her. In Chapter 2 she says a name that suits exactly gives her a thrill, so she picked a better one.';
    await page.fill('#para', para);
    ok(await page.$$eval('.chip', c => c.every(x => x.classList.contains('on'))), 'a good paragraph lights every chip');
    ok(/40 words ✓/.test(await page.textContent('#para-count')), 'word counter reaches 40');
    await page.fill('#g-name', 'Maya');
    const g = await page.textContent('#g-out');
    ok(/Maya/.test(g) && /White Way of Delight/.test(g) && /5\. Green Gables/.test(g), 'Gathered Answers has the name, the names and the order');
    await page.evaluate(() => { window.open = () => null; });
    await page.click('#pdf-btn');
    const pdf = await page.evaluate(() => window.VR_LAST_PDF || '');
    ok(/Window Seat bookmark/.test(pdf) && /My paragraph/.test(pdf), 'PDF has the game, the bookmark and the paragraph');
    if (width === 1150) await page.screenshot({ path: `/tmp/vr${W}-alt-${width}.png`, fullPage: true });
    else await page.screenshot({ path: `/tmp/vr${W}-alt-${width}.png`, fullPage: false });
    await page.reload();
    ok(await page.$eval('#bmark', b => b.classList.contains('show')) && (await page.inputValue('#para')).length > 50, 'progress survives a reload');
    ok(errs.length === 0, 'no page errors' + (errs.length ? ': ' + errs.join(' | ') : ''));
    await page.close();
  }
  await browser.close(); srv.close();
  console.log(fails ? `✗ ${fails} check(s) failed` : '✓ playtest passed');
  process.exit(fails ? 1 : 0);
})();
