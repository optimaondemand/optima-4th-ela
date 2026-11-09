#!/usr/bin/env python3
"""G4 ELA weekly VR page: tools/vr/week<W>.json -> vr-<W>.html (repo root).

Scope for Imagination (Bethany, 9 Nov 2026): one VR page per week, always Day 2, its own Canvas
assignment. The lessons never mention VR. Two paths on one page:
  Imagination Trip (VR)  photo straight to Canvas from the headset; earns the unit's keepsake
  Window Seat Day        an on-page game + a 40+ word paragraph -> PDF; earns the bookmark
The book's own guide voices 3 clips (one take): assets/audio/guide/<folder>/g4ela-<W>-vr-{brief,alt,saved}.mp3
Teacher video slot: assets/video/teacher/g4ela-<W>-vr.mp4 (hidden until it exists).

usage: python3 tools/vr/build_vr.py tools/vr/week7.json
"""
import html, json, os, re, sys
sys.path.insert(0, os.path.dirname(__file__))
import art

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
D = json.load(open(sys.argv[1], encoding='utf-8'))
W, DAY = D['week'], D['day']
PRE = 'g4ela-%d-vr' % W
CANVAS = '%d.%d VR · %s' % (W, DAY, D['title'])
e = lambda t: html.escape(str(t), quote=True)
show = lambda name: name.replace(' - ', ' · ')   # app names use " - "; student text has no dashes


def strip(t):
    return re.sub(r'<[^>]+>', '', t)


# ── VR step 1: the model groups ──
groups = ''.join(
    '<div class="grp" style="--gc:%s"><span class="gk">%s %s</span><span class="gm">%s</span><small>type: <b>%s</b></small><span class="gw">%s</span></div>'
    % (g['color'], g['ic'], e(g['name']), e(', '.join(show(m) for m in g['models'])), e(g['type']), g['why'])
    for g in D['groups'])

# ── help drawer (same as G4 science, images in assets/vr/) ──
HS = [
 ('🖥️ First time only: connect Canvas (on your computer)', [
  ('01-login', 'The Optima On Demand login page, with the Sign In button circled.', 'Log in', 'Go to <a href="https://xr.optimaed.com" target="_blank" rel="noopener">xr.optimaed.com</a> on your computer. Log in with the same login you use in VR.'),
  ('02-authorize', 'The Canvas box that asks to connect, with the Authorize button circled.', 'Connect to Canvas', 'Click <b>Connect to Canvas</b>. Log in with your usual Canvas username and password, then click <b>Authorize</b>. You will see <b>Canvas connection completed</b>.'),
  ('03-connected', 'The Canvas page on the website, with the Canvas button and the list of assignments circled.', 'Find our class', 'Click <b>Canvas</b> on the left and pick our class. Our assignments show up. You only do this part one time.')]),
 ('📄 Only if the assignment has a file', [
  ('04-upload', 'The Upload file box, with the Upload File button circled.', 'Get the file ready', 'Open the assignment and click <b>Open in Canvas</b> to download the file. Then click <b>My Files</b> and <b>Upload File</b>.')]),
 ('🥽 In the headset', [
  ('05-explore', 'The Explore tab in the headset, with the tab and the filter box circled.', 'Explore tab', 'Put on your headset. Click the <b>Explore</b> tab and type the map’s name in <b>Filter environments</b>.'),
  ('06-begin-solo', 'A map is picked and the Begin Solo button is circled.', 'Begin Solo', 'Click the map, then click <b>Begin Solo</b>.'),
  ('07-canvas', 'The Canvas tab in the headset, with the tab and the assignment box circled.', 'Read the assignment', 'Press the <b>top button on your right controller</b> to open your menu. Click the <b>Canvas</b> tab and pick our assignment to read the directions. Tip: point at a mint side grip and squeeze to pull the tablet to your hand.'),
  ('08-models', 'The Models tab open in an ocean map, with a list of models.', 'Bring out the models', 'Click <b>Models</b>. Type the exact name in the search box, or scroll with your thumbstick. Click a model to bring it out.'),
  ('08b-move', 'A controller moving a fish model in an ocean map.', 'Move and resize', 'Grab a model with the <b>palm trigger</b>. Turn and move it with the thumbstick. Use <b>both</b> palm triggers to make it bigger or smaller.'),
  ('09-placed', 'A picture file placed in an ocean map.', 'Need a file?', 'Click <b>Library</b>, then <b>Files</b>. Pick your file to place it in the world, next to your model.'),
  ('10-camera', 'The Library camera, with the Height slider and the Take photo button circled.', 'Take a photo', 'Click <b>Library</b>, then <b>Camera</b>. Move the tablet until your whole scene fits. Slide <b>Height</b> or the zoom bar if you need to. Click <b>Take photo</b>.'),
  ('11-choose', 'The My Files list in the headset, with the newest file circled.', 'Pick your photo', 'Click the <b>Canvas</b> tab and pick our assignment. Click <b>Choose from My Files</b>, pick your newest photo, then click <b>Use this file</b>.'),
  ('12-submitted', 'The Canvas tab after submitting, with the green Submitted tag circled.', 'Submit to Canvas', 'Click <b>Submit to Canvas</b> and look for the green <b>Submitted</b> tag. To leave VR, press the <b>Meta button</b> on your right controller, then click <b>Quit</b>.')]),
 ('🔁 Didn’t work in VR? Two other ways', [
  ('13-portal-submit', 'The Canvas page on the website, with the Choose from My Files button circled.', 'Use the website', 'Go to <a href="https://xr.optimaed.com" target="_blank" rel="noopener">xr.optimaed.com</a> and click <b>Canvas</b>. Pick our assignment, click <b>Choose from My Files</b>, pick your photo and submit it.')])]
n = 0
hd = ''
for title, items in HS:
    hd += '<h4 class="hd-group">%s</h4><ol class="hd-steps">' % title
    for img, alt, b, p in items:
        n += 1
        hd += '<li class="hd-step"><img loading="lazy" src="assets/vr/vr-canvas-help-%s.jpg" alt="%s"><div><span class="hd-n">%d</span><b>%s</b><p>%s</p></div></li>' % (img, e(alt), n, b, p)
    hd += '</ol>'
HELP = ('<details class="helpdrawer" id="vr-help"><summary><span class="hd-ic">🛟</span><span><b>Having trouble in VR?</b><small>Steps with pictures, and a how-to video</small></span><span class="hd-chev" aria-hidden="true">▾</span></summary>'
        '<div class="hd-body"><div class="hd-video"><div class="hd-frame" data-src="https://www.youtube-nocookie.com/embed/slDH-WN4scY?rel=0"></div><p class="hd-cap">How-to video: Optima On-Demand and Canvas</p></div>'
        '<p class="hd-note">These pictures come from other maps. Your map will be <b>%s</b>, but the buttons are the same.</p>%s'
        '<p class="hd-alt">Your photos save to <b>My Files</b> at xr.optimaed.com on their own. You can also download your photo there and upload it to the Canvas assignment yourself.</p></div></details>') % (e(D['map']), hd)

# ── Window Seat Day game ──
A = D['alt']
G = A['game']
if G == 'rename-order':
    GAME_HTML = ('<h3 class="gh">1 · Anne’s names</h3><div id="ren"></div>'
                 '<h3 class="gh">2 · The drive, in order</h3><p class="lock" id="order-lock">Finish part 1 first.</p><p style="font-size:16px">%s</p>'
                 '<div class="road" id="road"><ol class="mile" id="mile"></ol></div><div class="stops" id="stops"></div>') % e(A['orderQ'])
    GAME_CFG = {'rename': A['rename'], 'order': A['order'], 'orderMiss': A['orderMiss']}
else:
    sys.exit('unknown game: ' + G)
GAME_JS = open(os.path.join(HERE, 'games', G + '.js'), encoding='utf-8').read()
GAME_CSS = open(os.path.join(HERE, 'games', G + '.css'), encoding='utf-8').read()

banner, banner_css = art.BANNERS[D.get('banner', 'avenue')]()
K = D['keepsake']
keep = art.KEEPSAKES[K['art']]
WR = D['write']
TRANSCRIPTS = {k: re.sub(r'\s*\[[^\]]+\]\s*', ' ', v).strip() for k, v in D['scripts'].items()}

g = D['guide']
head = ('%s · %s, %s. Guide: %s (folder %s, voice %s). Map: %s. Models: %s. Extra: %s. Window Seat Day game: %s.'
        % (CANVAS, D['book'], D['chapters'], g['name'], g['folder'], g['voice'], D['map'],
           '; '.join(', '.join(gr['models']) for gr in D['groups']), ', '.join(D['steps']['extraModels']), G)).replace('--', '-')

REPL = {
 '{{CANVAS}}': e(CANVAS), '{{HEADCOMMENT}}': e(head), '{{WEEK}}': str(W), '{{TITLE}}': e(D['title']), '{{BOOK}}': e(D['book']), '{{CHAPTERS}}': e(D['chapters']),
 '{{GUIDE}}': e(g['name']), '{{BANNER}}': banner, '{{PRE}}': PRE,
 '{{L_BRIEF}}': e(D['labels']['brief']), '{{L_ALT}}': e(D['labels']['alt']), '{{L_SAVED}}': e(D['labels']['saved']),
 '{{PC_KICKER}}': e(D['postcard']['kicker']), '{{PC_H}}': e(D['postcard']['h']), '{{PC_BODY}}': ''.join('<p>%s</p>' % e(p) for p in D['postcard']['body']),
 '{{PC_SIGN}}': e(D['postcard']['sign']), '{{PC_WORD}}': D['postcard']['word'], '{{STAMP_ART}}': art.STAMPS[K['art']](),
 '{{KEEP_NAME}}': e(K['name']), '{{KEEP_SHORT}}': e(K['name'][0].upper() + K['name'][1:]), '{{KEEP_TITLE}}': e(K['name'][0].upper() + K['name'][1:] + ' earned!'),
 '{{KEEP_LINE}}': e(K['line']), '{{KEEP_ART}}': keep(70, 'peekart'), '{{KEEP_ART_BIG}}': keep(120, 'keep'), '{{BMARK_ART}}': art.bookmark(),
 '{{MINUTES}}': str(D['minutes']), '{{MISSION_H}}': e(D['mission']['h']), '{{MISSION_P}}': e(D['mission']['p']), '{{JOB}}': e(D['job']),
 '{{GROUPS}}': groups, '{{MAP}}': e(D['map']), '{{MAP_FILTER}}': e(D['mapFilter']),
 '{{S_BUILD}}': D['steps']['build'], '{{S_SAY}}': D['steps']['say'], '{{S_FRAME}}': e(D['steps']['frame']), '{{S_EXTRA}}': D['steps']['extra'], '{{FITS}}': e(D['steps']['fits']),
 '{{HELP}}': HELP, '{{POINTS}}': e(D['points']),
 '{{ALT_H}}': e(A['h']), '{{ALT_JOB}}': e(A['job']), '{{ALT_P}}': e(A['p']), '{{GAME_HTML}}': GAME_HTML, '{{GAME_CSS}}': GAME_CSS + banner_css, '{{GAME_JS}}': GAME_JS,
 '{{WRITE_Q}}': WR['q'], '{{CHIPS}}': ''.join('<span class="chip" data-chip="%s">%s</span>' % (c['k'], e(c['t'])) for c in WR['chips']),
 '{{NCHIPS}}': str(len(WR['chips'])), '{{STARTERS}}': ''.join('<li>%s</li>' % e(s) for s in WR['starters']),
 '{{CREDITS}}': (e(D['credits']) + ' ' if D.get('credits') else '') + 'Drawings made for this page. ' + e(D['book']) + ' by L. M. Montgomery (1908) is in the public domain.' if D['bookId'] == 'anne' else e(D.get('credits', '')),
 '{{DATA}}': json.dumps({'week': W, 'pre': PRE, 'canvas': CANVAS, 'guide': {k: g[k] for k in ('name', 'initials', 'color', 'folder')},
                          'transcripts': TRANSCRIPTS, 'game': GAME_CFG, 'chips': [{'k': c['k'], 'rx': c['rx']} for c in WR['chips']],
                          'writeQ': strip(WR['q'])}, ensure_ascii=False).replace('</', '<\\/'),
}
page = open(os.path.join(HERE, 'template.html'), encoding='utf-8').read()
for k, v in REPL.items():
    page = page.replace(k, v)
left = re.findall(r'\{\{\w+\}\}', page)
assert not left, left
out = os.path.join(ROOT, 'vr-%d.html' % W)
open(out, 'w', encoding='utf-8', newline='\n').write(page)
json.dump({'pre': PRE, 'voice': g['voice'], 'folder': g['folder'],
           'clips': {k: {'file': 'assets/audio/guide/%s/%s-%s.mp3' % (g['folder'], PRE, k), 'prompt': v, 'transcript': TRANSCRIPTS[k]} for k, v in D['scripts'].items()},
           'video': {'file': 'assets/video/teacher/%s.mp4' % PRE, 'script': D.get('video', '')}},
          open(os.path.join(HERE, 'week%d-scripts.json' % W), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', out, '(%d KB)' % (len(page.encode()) // 1024))
