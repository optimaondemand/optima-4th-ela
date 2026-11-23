"""Drawings for the G4 ELA VR pages (inline SVG, no lettering, aria-hidden by the template).
Banners: week<W>.json picks "banner": "avenue" (the week 7 drawing) or gives a scene dict
  {"sky": "dusk|night|dawn|day|storm|gold", "ground": "#hex", "motifs": [[name, x, scale, {opts}], ...]}
  Motif names: hills, pines, trees, water, boat, house, cabin, castle, stars, moon, sun, lantern, candles,
  path, fence, wagon, train, bridge, torch, books, flag, cove, tent, owl, quilt.
Keepsakes (one per book): blossom (Anne), shell (NTS), quilt (FT), apple (PC), feather (Opti weeks)."""
import random


def _blossoms(rng, cx, cy, rx, ry, n, r0=5, r1=10):
    out = []
    for _ in range(n):
        x = cx + rng.uniform(-rx, rx); y = cy + rng.uniform(-ry, ry); r = rng.uniform(r0, r1)
        out.append('<circle cx="%.1f" cy="%.1f" r="%.1f" fill="%s" opacity="%.2f"/>' % (x, y, r, rng.choice(['#FFFFFF', '#FDF1F3', '#F8DCE3', '#FFF7F0']), rng.uniform(.75, 1)))
    return ''.join(out)


def banner_avenue():
    """The White Way of Delight: a red road under arching apple blossom, sunset 'rose window' ahead,
    the pond off to the right, a white star over a far farmhouse."""
    rng = random.Random(7)
    s = ['<svg viewBox="0 0 920 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A red country road under arching apple trees in bloom, with a sunset sky ahead">',
         '<defs><linearGradient id="sky7" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3B3F7A"/><stop offset=".45" stop-color="#C77BA0"/><stop offset=".8" stop-color="#F6C27A"/><stop offset="1" stop-color="#FBE3B0"/></linearGradient>',
         '<radialGradient id="glow7" cx=".5" cy=".62" r=".35"><stop offset="0" stop-color="#FFF4D6" stop-opacity=".95"/><stop offset="1" stop-color="#FFF4D6" stop-opacity="0"/></radialGradient>',
         '<linearGradient id="pond7" x1="0" y1="0" x2="1" y2="0"><stop offset="0" stop-color="#E7A9B8"/><stop offset=".5" stop-color="#B9D8C9"/><stop offset="1" stop-color="#9CC3D6"/></linearGradient></defs>',
         '<rect width="920" height="260" fill="url(#sky7)"/><rect width="920" height="260" fill="url(#glow7)"/>',
         '<g class="b7-star"><path d="M745 38 l4 11 11 4 -11 4 -4 11 -4 -11 -11 -4 11 -4z" fill="#FFFFFF"/><circle cx="745" cy="53" r="16" fill="#FFFFFF" opacity=".18"/></g>',
         '<path d="M0 182 Q160 150 330 168 T640 160 T920 172 V260 H0Z" fill="#6E8F5A"/>',
         '<path d="M690 160 l18 -12 18 12 v16 h-36z" fill="#F4EFE4"/><path d="M686 161 l22 -15 22 15" fill="none" stroke="#3E6B45" stroke-width="3"/><rect x="703" y="166" width="6" height="10" fill="#E9C46A"/>',
         '<path d="M560 196 Q640 178 760 186 Q880 194 920 188 V214 Q820 222 700 214 Q600 210 560 206Z" fill="url(#pond7)" opacity=".95"/>',
         '<g fill="#FFFFFF"><ellipse cx="640" cy="200" rx="10" ry="3"/><ellipse cx="702" cy="206" rx="12" ry="3.5"/><ellipse cx="820" cy="200" rx="9" ry="3"/></g>',
         '<g fill="#F8DCE3"><circle cx="640" cy="198" r="3"/><circle cx="702" cy="203" r="3.5"/><circle cx="820" cy="198" r="3"/></g>',
         '<path d="M330 260 L440 168 L470 168 L600 260Z" fill="#B5543A"/><path d="M445 175 L465 175 L520 260 L410 260Z" fill="#C8693F" opacity=".5"/>']
    for x, lean in [(250, 14), (180, 18), (95, 22), (20, 26)]:
        s.append('<path d="M%d 260 Q%d 190 %d 110" stroke="#5B3A26" stroke-width="%d" fill="none" stroke-linecap="round"/>' % (x, x + lean, x + lean * 2 + 40, 10 + (250 - x) // 40))
    for x, lean in [(560, -14), (640, -18), (720, -22), (800, -26)]:
        s.append('<path d="M%d 260 Q%d 190 %d 110" stroke="#5B3A26" stroke-width="%d" fill="none" stroke-linecap="round"/>' % (x, x + lean, x + lean * 2 - 40, 10 + (x - 560) // 40))
    s.append('<g class="b7-sway">')
    s.append(_blossoms(rng, 150, 60, 170, 55, 170))
    s.append(_blossoms(rng, 700, 60, 190, 55, 170))
    s.append(_blossoms(rng, 455, 22, 130, 22, 60))
    s.append('</g>')
    s.append('<g transform="translate(436 176) scale(.55)"><path d="M10 30 Q2 14 14 8 L22 6 L26 0 L30 2 L28 8 Q36 12 34 20 L32 30Z" fill="#8A4B2A"/>'
             '<rect x="34" y="12" width="34" height="14" rx="3" fill="#2B1D12"/><circle cx="40" cy="30" r="7" fill="none" stroke="#2B1D12" stroke-width="2.5"/><circle cx="62" cy="30" r="7" fill="none" stroke="#2B1D12" stroke-width="2.5"/>'
             '<circle cx="50" cy="6" r="4" fill="#C8553D"/><circle cx="58" cy="7" r="3.5" fill="#5B4A36"/></g>')
    s.append('<g class="b7-petals" fill="#FFFFFF">' + ''.join('<circle cx="%d" cy="%d" r="2.4" opacity=".9"/>' % (rng.randint(60, 860), rng.randint(90, 200)) for _ in range(26)) + '</g>')
    s.append('</svg>')
    css = ('.b7-sway{animation:b7sway 6s ease-in-out infinite;transform-origin:460px 260px}'
           '@keyframes b7sway{0%,100%{transform:rotate(0)}50%{transform:rotate(.35deg)}}'
           '.b7-petals{animation:b7fall 9s linear infinite}@keyframes b7fall{from{transform:translate(0,-10px)}to{transform:translate(-30px,40px);opacity:.2}}'
           '.b7-star{animation:b7tw 2.6s ease-in-out infinite;transform-origin:745px 53px}@keyframes b7tw{50%{opacity:.6}}')
    return ''.join(s), css


# ───────────────────────── parametric scene banner ─────────────────────────
SKIES = {
    'dusk': ['#2E3466', '#7A5A8C', '#D98C7A', '#F3C9A0'],
    'night': ['#070B23', '#121A45', '#2A3A6E', '#44507E'],
    'dawn': ['#54557F', '#B98AA0', '#F2C58C', '#FBE9C6'],
    'day': ['#5E97D6', '#8FBCE8', '#C9E2F6', '#EAF3FB'],
    'storm': ['#2B2F3F', '#4A4F66', '#6E7489', '#9A9FB0'],
    'gold': ['#8E5A2E', '#C98A3B', '#EBC06C', '#F8E4B4'],
    'grey': ['#5B6274', '#8A91A3', '#B9BFCC', '#DDE1E8'],
}


def _g(name, stops, horizontal=False):
    d = 'x1="0" y1="0" x2="1" y2="0"' if horizontal else 'x1="0" y1="0" x2="0" y2="1"'
    n = len(stops) - 1
    return '<linearGradient id="%s" %s>%s</linearGradient>' % (name, d, ''.join('<stop offset="%.2f" stop-color="%s"/>' % (i / n, c) for i, c in enumerate(stops)))


def m_hills(x, s, o):
    c = o.get('color', '#4D6B4A'); y = o.get('y', 170)
    return '<path d="M%d %d Q%d %d %d %d T%d %d T%d %d V260 H%d Z" fill="%s"/>' % (x, y + 20, x + 120 * s, y - 30 * s, x + 240 * s, y + 10, x + 480 * s, y + 4, x + 720 * s, y + 12, x, c)


def m_pines(x, s, o):
    n = o.get('n', 5); c = o.get('color', '#1F3B2D'); out = []
    rng = random.Random(x)
    for i in range(n):
        px = x + i * 42 * s + rng.randint(-8, 8); h = (90 + rng.randint(0, 40)) * s; base = o.get('y', 250)
        out.append('<path d="M%.0f %d l%.0f %.0f l%.0f %.0f z M%.0f %.0f l%.0f %.0f l%.0f %.0f z M%.0f %.0f l%.0f %.0f l%.0f %.0f z" fill="%s"/>'
                   % (px, base, 20 * s, -h, 20 * s, h, px + 3 * s, base - h * .42, 17 * s, -h * .55, 17 * s, h * .55, px + 6 * s, base - h * .7, 14 * s, -h * .45, 14 * s, h * .45, c))
        out.append('<rect x="%.0f" y="%d" width="%.0f" height="%.0f" fill="#3B2A1C"/>' % (px + 17 * s, base - 8, 6 * s, 10))
    return '<g class="sway">' + ''.join(out) + '</g>'


def m_trees(x, s, o):
    n = o.get('n', 3); c = o.get('color', '#3E7A4A'); out = []
    for i in range(n):
        tx = x + i * 70 * s; base = o.get('y', 250)
        out.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" fill="#5B3A26"/><circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s"/><circle cx="%.0f" cy="%.0f" r="%.0f" fill="%s" opacity=".8"/>'
                   % (tx + 22 * s, base - 46 * s, 8 * s, 46 * s, tx + 26 * s, base - 60 * s, 30 * s, c, tx + 12 * s, base - 48 * s, 20 * s, c))
    return '<g class="sway">' + ''.join(out) + '</g>'


def m_water(x, s, o):
    y = o.get('y', 196); c = o.get('color', '#9CC3D6'); c2 = o.get('shine', '#FFFFFF')
    w = o.get('w', 920)
    return ('<path d="M%d %d Q%d %d %d %d T%d %d V260 H%d Z" fill="%s" opacity=".95"/>' % (x, y, x + w * .25, y - 8, x + w * .5, y, x + w, y, x, c)
            + '<g class="shine" fill="%s" opacity=".55">' % c2 + ''.join('<ellipse cx="%d" cy="%d" rx="%d" ry="2.2"/>' % (x + 40 + i * 70, y + 14 + (i % 3) * 11, 10 + (i % 4) * 4) for i in range(int(w / 70))) + '</g>')


def m_boat(x, s, o):
    c = o.get('color', '#8A4B2A'); y = o.get('y', 206); sail = o.get('sail', True)
    out = '<g class="bob" transform="translate(%d %d) scale(%.2f)"><path d="M0 0 L80 0 L68 18 L12 18 Z" fill="%s"/><rect x="6" y="-6" width="70" height="7" fill="#5B3A26"/>' % (x, y, s, c)
    if sail:
        out += '<rect x="38" y="-62" width="3" height="58" fill="#3B2A1C"/><path d="M41 -58 L74 -10 L41 -10 Z" fill="#F4EFE4"/>'
    else:
        out += '<rect x="20" y="-14" width="40" height="9" rx="2" fill="#2B1D12"/><rect x="30" y="-22" width="6" height="10" fill="#2B1D12"/>'
    return out + '</g>'


def m_house(x, s, o):
    y = o.get('y', 230); wall = o.get('wall', '#F4EFE4'); roof = o.get('roof', '#B5543A'); lit = o.get('lit', True)
    win = '#F6C27A' if lit else '#44507E'
    g = '<g transform="translate(%d %d) scale(%.2f)">' % (x, y, s)
    g += '<rect x="0" y="-40" width="70" height="40" fill="%s"/><path d="M-6 -40 L35 -72 L76 -40 Z" fill="%s"/>' % (wall, roof)
    g += '<rect x="10" y="-30" width="12" height="12" fill="%s" class="%s"/><rect x="48" y="-30" width="12" height="12" fill="%s" class="%s"/><rect x="29" y="-22" width="12" height="22" fill="#5B3A26"/>' % (win, 'glow' if lit else '', win, 'glow' if lit else '')
    if o.get('chimney', True): g += '<rect x="52" y="-66" width="8" height="16" fill="#6B4A3A"/>'
    return g + '</g>'


def m_cabin(x, s, o):
    y = o.get('y', 236); g = '<g transform="translate(%d %d) scale(%.2f)">' % (x, y, s)
    for i in range(5):
        g += '<rect x="0" y="%d" width="80" height="7" rx="3" fill="%s"/>' % (-8 - i * 8, '#8A5A3A' if i % 2 else '#7A4E32')
    g += '<path d="M-6 -48 L40 -74 L86 -48 Z" fill="#4A3324"/><rect x="33" y="-24" width="14" height="24" fill="#2B1D12"/><rect x="62" y="-70" width="8" height="18" fill="#5B4A36"/>'
    g += '<g class="smoke" fill="#FFFFFF" opacity=".5"><circle cx="66" cy="-80" r="5"/><circle cx="72" cy="-92" r="6"/><circle cx="80" cy="-104" r="7"/></g>'
    return g + '</g>'


def m_castle(x, s, o):
    y = o.get('y', 232); c = o.get('color', '#7E8798'); ruin = o.get('ruin', False)
    g = '<g transform="translate(%d %d) scale(%.2f)">' % (x, y, s)
    g += '<rect x="0" y="-60" width="34" height="60" fill="%s"/><rect x="34" y="-40" width="60" height="40" fill="%s" opacity=".9"/><rect x="94" y="-70" width="34" height="70" fill="%s"/>' % (c, c, c)
    for i in range(4): g += '<rect x="%d" y="-68" width="7" height="8" fill="%s"/>' % (i * 9, c)
    for i in range(4): g += '<rect x="%d" y="-78" width="7" height="8" fill="%s"/>' % (94 + i * 9, c)
    if ruin:
        g += '<path d="M34 -40 L50 -52 L62 -38 L80 -50 L94 -40" fill="%s"/><path d="M0 -60 L10 -72 L20 -58" fill="#0E1C42" opacity=".35"/>' % c
        g += '<path d="M40 -10 q10 -30 20 -10 q10 -30 20 0" fill="none" stroke="#3E7A4A" stroke-width="4"/>'
    else:
        g += '<path d="M48 0 a14 14 0 0 1 28 0 z" fill="#2B1D12"/>'
    return g + '</g>'


def m_stars(x, s, o):
    rng = random.Random(o.get('seed', 3)); n = o.get('n', 30); out = []
    for i in range(n):
        sx = rng.randint(10, 910); sy = rng.randint(8, int(o.get('y', 120))); r = rng.uniform(1, 2.4)
        out.append('<circle cx="%d" cy="%d" r="%.1f" fill="#FFFFFF" style="animation-delay:%.1fs"/>' % (sx, sy, r, rng.uniform(0, 3)))
    big = o.get('big')
    if big:
        bx, by = big
        out.append('<path d="M%d %d l5 13 13 5 -13 5 -5 13 -5 -13 -13 -5 13 -5z" fill="#FFFFFF"/><circle cx="%d" cy="%d" r="18" fill="#FFFFFF" opacity=".16"/>' % (bx, by - 18, bx, by))
    return '<g class="tw">' + ''.join(out) + '</g>'


def m_moon(x, s, o):
    y = o.get('y', 50); r = 22 * s
    return '<circle cx="%d" cy="%d" r="%.0f" fill="#FFF4D6"/><circle cx="%d" cy="%d" r="%.0f" fill="#FFF4D6" opacity=".15"/>' % (x, y, r, x, y, r * 1.8)


def m_sun(x, s, o):
    y = o.get('y', 70); r = 26 * s
    return '<circle cx="%d" cy="%d" r="%.0f" fill="#FFE9A8"/><circle cx="%d" cy="%d" r="%.0f" fill="#FFE9A8" opacity=".25"/>' % (x, y, r, x, y, r * 2)


def m_lantern(x, s, o):
    y = o.get('y', 160)
    return ('<g class="glow" transform="translate(%d %d) scale(%.2f)"><rect x="-2" y="-40" width="4" height="40" fill="#3B2A1C"/><rect x="-10" y="0" width="20" height="26" rx="3" fill="#2B1D12"/>'
            '<rect x="-7" y="3" width="14" height="20" fill="#FFD36A"/><circle cx="0" cy="13" r="26" fill="#FFD36A" opacity=".18"/></g>') % (x, y, s)


def m_candles(x, s, o):
    n = o.get('n', 5); y = o.get('y', 200); out = ['<g class="glow">']
    for i in range(n):
        cx = x + i * 26 * s; h = (28 + (i * 7) % 15) * s
        out.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="2" fill="#FFF3DC"/><ellipse cx="%.0f" cy="%.0f" rx="%.0f" ry="%.0f" fill="#FFB347"/><circle cx="%.0f" cy="%.0f" r="%.0f" fill="#FFD36A" opacity=".2"/>'
                   % (cx, y - h, 8 * s, h, cx + 4 * s, y - h - 7 * s, 3.5 * s, 7 * s, cx + 4 * s, y - h - 6 * s, 18 * s))
    return ''.join(out) + '</g>'


def m_path(x, s, o):
    c = o.get('color', '#C9A97A'); y = o.get('y', 200)
    return '<path d="M%d 260 Q%d %d %d %d Q%d %d %d %d L%d %d Q%d %d %d 260 Z" fill="%s" opacity=".9"/>' % (x, x + 80 * s, y + 20, x + 160 * s, y, x + 220 * s, y - 12, x + 300 * s, y - 16, x + 318 * s, y - 16, x + 240 * s, y + 10, x + 150 * s, c)


def m_fence(x, s, o):
    y = o.get('y', 236); out = []
    for i in range(o.get('n', 8)):
        out.append('<rect x="%.0f" y="%.0f" width="5" height="%.0f" fill="#D9C8A8"/>' % (x + i * 26 * s, y - 24 * s, 24 * s))
    out.append('<rect x="%d" y="%.0f" width="%.0f" height="4" fill="#D9C8A8"/><rect x="%d" y="%.0f" width="%.0f" height="4" fill="#D9C8A8"/>' % (x, y - 20 * s, o.get('n', 8) * 26 * s, x, y - 9 * s, o.get('n', 8) * 26 * s))
    return ''.join(out)


def m_wagon(x, s, o):
    y = o.get('y', 236)
    return ('<g transform="translate(%d %d) scale(%.2f)"><path d="M0 -18 h70 v18 h-70z" fill="#6B4A3A"/><path d="M4 -18 q31 -34 62 0z" fill="#F4EFE4"/>'
            '<circle cx="16" cy="4" r="10" fill="none" stroke="#2B1D12" stroke-width="4"/><circle cx="54" cy="4" r="10" fill="none" stroke="#2B1D12" stroke-width="4"/></g>') % (x, y, s)


def m_train(x, s, o):
    y = o.get('y', 232)
    return ('<g transform="translate(%d %d) scale(%.2f)"><rect x="0" y="-30" width="54" height="30" rx="4" fill="#2B2F3F"/><rect x="54" y="-44" width="30" height="44" fill="#3B3F55"/>'
            '<rect x="60" y="-38" width="16" height="14" fill="#F6C27A"/><rect x="8" y="-46" width="12" height="16" fill="#2B2F3F"/>'
            '<g class="smoke" fill="#FFFFFF" opacity=".5"><circle cx="14" cy="-56" r="6"/><circle cx="4" cy="-70" r="8"/><circle cx="-10" cy="-86" r="10"/></g>'
            '<circle cx="14" cy="2" r="9" fill="#111"/><circle cx="40" cy="2" r="9" fill="#111"/><circle cx="68" cy="2" r="9" fill="#111"/><rect x="-200" y="8" width="400" height="4" fill="#5B5B5B"/></g>') % (x, y, s)


def m_bridge(x, s, o):
    y = o.get('y', 200); c = o.get('color', '#8A8A8A')
    return '<g transform="translate(%d %d) scale(%.2f)"><rect x="0" y="-8" width="160" height="10" fill="%s"/><path d="M20 2 a30 22 0 0 1 60 0 z M90 2 a30 22 0 0 1 60 0 z" fill="%s"/><path d="M0 -8 h160" stroke="#555" stroke-width="2"/></g>' % (x, y, s, c, c)


def m_torch(x, s, o):
    y = o.get('y', 150)
    return '<g class="glow" transform="translate(%d %d) scale(%.2f)"><rect x="-3" y="0" width="6" height="40" fill="#3B2A1C"/><path d="M-9 0 q9 -26 18 0 q-9 -10 -18 0z" fill="#FFB347"/><path d="M-4 -2 q4 -14 8 0z" fill="#FFE08A"/><circle cx="0" cy="-6" r="28" fill="#FFB347" opacity=".18"/></g>' % (x, y, s)


def m_books(x, s, o):
    y = o.get('y', 236); cols = ['#B5476B', '#1F6F78', '#C7922C', '#2F7A55', '#C8553D', '#0E1C42']; out = []
    for i in range(o.get('n', 6)):
        h = (46 + (i * 11) % 22) * s
        out.append('<rect x="%.0f" y="%.0f" width="%.0f" height="%.0f" rx="2" fill="%s"/>' % (x + i * 16 * s, y - h, 14 * s, h, cols[i % 6]))
    return ''.join(out)


def m_flag(x, s, o):
    y = o.get('y', 150)
    return ('<g transform="translate(%d %d) scale(%.2f)"><rect x="0" y="0" width="4" height="90" fill="#3B2A1C"/>'
            '<g class="wave"><rect x="4" y="2" width="70" height="40" fill="#C8553D"/>' + ''.join('<rect x="4" y="%d" width="70" height="4" fill="#F4EFE4"/>' % (6 + i * 9) for i in range(4)) +
            '<rect x="4" y="2" width="30" height="22" fill="#2E3466"/></g></g>') % (x, y, s)


def m_cove(x, s, o):
    return '<path d="M%d 150 Q%d 120 %d 140 L%d 260 L%d 260 Z" fill="%s"/>' % (x, x + 60 * s, x + 130 * s, x + 170 * s, x - 10, o.get('color', '#4A4F66'))


def m_tent(x, s, o):
    y = o.get('y', 236)
    return '<g transform="translate(%d %d) scale(%.2f)"><path d="M0 0 L40 -52 L80 0 Z" fill="#E8DCC3"/><path d="M30 0 L40 -22 L50 0 Z" fill="#5B4A36"/></g>' % (x, y, s)


def m_owl(x, s, o):
    y = o.get('y', 120)
    return ('<g transform="translate(%d %d) scale(%.2f)"><ellipse cx="0" cy="0" rx="18" ry="24" fill="#8A6A4A"/><circle cx="0" cy="-16" r="16" fill="#A07E58"/>'
            '<circle cx="-6" cy="-18" r="5" fill="#FFF3DC"/><circle cx="6" cy="-18" r="5" fill="#FFF3DC"/><circle cx="-6" cy="-18" r="2.4" fill="#2B1D12"/><circle cx="6" cy="-18" r="2.4" fill="#2B1D12"/>'
            '<path d="M-3 -11 l3 5 3 -5z" fill="#C7922C"/><rect x="-26" y="26" width="52" height="5" rx="2" fill="#5B3A26"/></g>') % (x, y, s)


def m_quilt(x, s, o):
    y = o.get('y', 236); cols = ['#2F7A55', '#8A5A3A', '#E9C46A', '#4D6B4A', '#C8553D', '#F4EFE4']; out = ['<g transform="translate(%d %d) scale(%.2f)">' % (x, y, s)]
    for r in range(3):
        for c in range(4):
            out.append('<rect x="%d" y="%d" width="22" height="22" fill="%s" stroke="#FFF3DC" stroke-width="1.5"/>' % (c * 22, -66 + r * 22, cols[(r * 4 + c) % 6]))
    return ''.join(out) + '</g>'


def m_dogs(x, s, o):
    return ''


MOTIFS = {'hills': m_hills, 'pines': m_pines, 'trees': m_trees, 'water': m_water, 'boat': m_boat, 'house': m_house, 'cabin': m_cabin, 'castle': m_castle,
          'stars': m_stars, 'moon': m_moon, 'sun': m_sun, 'lantern': m_lantern, 'candles': m_candles, 'path': m_path, 'fence': m_fence, 'wagon': m_wagon,
          'train': m_train, 'bridge': m_bridge, 'torch': m_torch, 'books': m_books, 'flag': m_flag, 'cove': m_cove, 'tent': m_tent, 'owl': m_owl, 'quilt': m_quilt}


def banner_scene(sc):
    sky = SKIES[sc.get('sky', 'dusk')]
    s = ['<svg viewBox="0 0 920 260" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="%s">' % sc.get('alt', 'A scene from the chapter'),
         '<defs>' + _g('skyg', sky) + '</defs>', '<rect width="920" height="260" fill="url(#skyg)"/>']
    if sc.get('ground'):
        s.append('<rect x="0" y="%d" width="920" height="%d" fill="%s"/>' % (sc.get('groundY', 200), 260 - sc.get('groundY', 200), sc['ground']))
    for m in sc.get('motifs', []):
        name, x, scale = m[0], m[1], m[2]; opts = m[3] if len(m) > 3 else {}
        s.append(MOTIFS[name](x, scale, opts))
    s.append('</svg>')
    css = ('.sway{animation:bsway 7s ease-in-out infinite;transform-origin:50% 100%}@keyframes bsway{50%{transform:rotate(.4deg)}}'
           '.tw circle{animation:btw 2.8s ease-in-out infinite}@keyframes btw{50%{opacity:.35}}'
           '.glow{animation:bglow 2.2s ease-in-out infinite}@keyframes bglow{50%{opacity:.75}}'
           '.bob{animation:bbob 4s ease-in-out infinite}@keyframes bbob{50%{transform:translateY(4px)}}'
           '.shine ellipse{animation:bshine 3.5s ease-in-out infinite}@keyframes bshine{50%{opacity:.15}}'
           '.smoke{animation:bsmoke 6s linear infinite}@keyframes bsmoke{to{transform:translate(-14px,-30px);opacity:0}}'
           '.wave{animation:bwave 3s ease-in-out infinite;transform-origin:4px 20px}@keyframes bwave{50%{transform:skewY(3deg)}}')
    return ''.join(s), css


# ───────────────────────── keepsakes (one per book) ─────────────────────────
def _label(cls, size, inner, tilt=-4):
    return ('<svg class="%s" viewBox="0 0 120 120" width="%d" height="%d" aria-hidden="true">'
            '<rect x="12" y="12" width="96" height="96" rx="6" fill="#FFFBF1" stroke="#E5D3AE" stroke-width="2" transform="rotate(%d 60 60)"/>%s'
            '<rect x="40" y="6" width="40" height="13" fill="#F2E3B8" opacity=".85" transform="rotate(-6 60 12)"/></svg>') % (cls, size, size, tilt, inner)


def keepsake_blossom(size=120, cls='keep'):
    pet = ''.join('<ellipse cx="60" cy="38" rx="13" ry="19" fill="#FDF1F3" stroke="#E7B3C2" stroke-width="1.5" transform="rotate(%d 60 60)"/>' % a for a in range(0, 360, 72))
    return _label(cls, size, '<path d="M60 64 Q70 90 92 100" stroke="#6E8F5A" stroke-width="3" fill="none"/><ellipse cx="82" cy="88" rx="9" ry="4" fill="#7FA66A" transform="rotate(30 82 88)"/>'
                  + pet + '<circle cx="60" cy="60" r="8" fill="#F6C27A"/><g fill="#C7922C"><circle cx="56" cy="57" r="1.4"/><circle cx="63" cy="56" r="1.4"/><circle cx="61" cy="63" r="1.4"/></g>')


def keepsake_shell(size=120, cls='keep'):
    """A scallop shell from the shore at Uncle Henrik's (Number the Stars)."""
    ribs = ''.join('<path d="M60 86 L%d %d" stroke="#E0B8A0" stroke-width="2.2" stroke-linecap="round"/>' % (60 + int(38 * __import__('math').cos(a * 3.14159 / 180)), 86 - int(44 * __import__('math').sin(a * 3.14159 / 180))) for a in range(20, 161, 20))
    return _label(cls, size, '<path d="M60 86 L24 48 Q60 8 96 48 Z" fill="#F7E3D6" stroke="#D9A98E" stroke-width="2"/><path d="M24 48 Q60 28 96 48" fill="none" stroke="#D9A98E" stroke-width="2"/>' + ribs + '<rect x="52" y="84" width="16" height="10" rx="3" fill="#E7C9B8"/>')


def keepsake_quilt(size=120, cls='keep'):
    """A patchwork square like Old Rit's quilt (Freedom Train): green, brown and yellow scraps."""
    cols = ['#2F7A55', '#8A5A3A', '#E9C46A', '#8A5A3A', '#E9C46A', '#2F7A55', '#E9C46A', '#2F7A55', '#8A5A3A']
    sq = ''.join('<rect x="%d" y="%d" width="20" height="20" fill="%s" stroke="#FFF3DC" stroke-width="2"/>' % (30 + (i % 3) * 20, 30 + (i // 3) * 20, cols[i]) for i in range(9))
    return _label(cls, size, '<g transform="rotate(6 60 60)">' + sq + '<path d="M30 30 h60 v60 h-60z" fill="none" stroke="#5B3A26" stroke-width="2" stroke-dasharray="3 3"/></g>')


def keepsake_apple(size=120, cls='keep'):
    """A golden apple from the old orchard at Cair Paravel (Prince Caspian)."""
    return _label(cls, size, '<path d="M60 40 q-26 -10 -30 18 q-2 30 22 40 q8 3 8 0 q0 3 8 0 q24 -10 22 -40 q-4 -28 -30 -18z" fill="#E9B949" stroke="#B88A1C" stroke-width="2"/>'
                  '<path d="M60 40 q2 -14 10 -18" stroke="#5B3A26" stroke-width="3" fill="none"/><path d="M62 30 q14 -10 20 2 q-12 8 -20 -2z" fill="#6E8F5A"/><ellipse cx="48" cy="56" rx="6" ry="9" fill="#FFF3DC" opacity=".55"/>')


def keepsake_feather(size=120, cls='keep'):
    """An owl feather left by Opti (the year-end weeks)."""
    barbs = ''.join('<path d="M%d %d q-14 %d -22 %d" stroke="#A07E58" stroke-width="1.6" fill="none"/>' % (62 - i, 40 + i * 6, 2, -6) for i in range(0, 9))
    return _label(cls, size, '<g transform="rotate(-25 60 60)"><path d="M62 24 q26 18 4 78 q-28 -52 -4 -78z" fill="#C9A77A" stroke="#8A6A4A" stroke-width="2"/><path d="M62 26 L60 104" stroke="#5B3A26" stroke-width="2.5"/>' + barbs + '</g>')


def bookmark(color='#B5476B'):
    return ('<svg viewBox="0 0 90 150" aria-hidden="true"><path d="M14 4 H76 V140 L45 118 L14 140Z" fill="%s"/>'
            '<path d="M20 10 H70 V128 L45 110 L20 128Z" fill="none" stroke="#FFF3DC" stroke-width="2" stroke-dasharray="4 4"/>'
            '<rect x="30" y="30" width="30" height="36" rx="2" fill="#FFF3DC"/><path d="M33 34 h24 v28 h-24z" fill="#BFD9E0"/><path d="M45 34 v28 M33 48 h24" stroke="#FFF3DC" stroke-width="2"/>'
            '<circle cx="45" cy="86" r="6" fill="#FFF3DC"/></svg>') % color


BANNERS = {'avenue': banner_avenue}
KEEPSAKES = {'blossom': keepsake_blossom, 'shell': keepsake_shell, 'quilt': keepsake_quilt, 'apple': keepsake_apple, 'feather': keepsake_feather}
STAMPS = {k: (lambda f: (lambda: f(60, 'pcs')))(f) for k, f in KEEPSAKES.items()}
