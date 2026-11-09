"""Drawings for the G4 ELA VR pages (inline SVG, no lettering, aria-hidden by the template).
Add a new keepsake or banner here by name; week<W>.json picks it with keepsake.art / banner."""
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
    # trunks
    for x, lean in [(250, 14), (180, 18), (95, 22), (20, 26)]:
        s.append('<path d="M%d 260 Q%d 190 %d 110" stroke="#5B3A26" stroke-width="%d" fill="none" stroke-linecap="round"/>' % (x, x + lean, x + lean * 2 + 40, 10 + (250 - x) // 40))
    for x, lean in [(560, -14), (640, -18), (720, -22), (800, -26)]:
        s.append('<path d="M%d 260 Q%d 190 %d 110" stroke="#5B3A26" stroke-width="%d" fill="none" stroke-linecap="round"/>' % (x, x + lean, x + lean * 2 - 40, 10 + (x - 560) // 40))
    # canopy arch
    s.append('<g class="b7-sway">')
    s.append(_blossoms(rng, 150, 60, 170, 55, 170))
    s.append(_blossoms(rng, 700, 60, 190, 55, 170))
    s.append(_blossoms(rng, 455, 22, 130, 22, 60))
    s.append('</g>')
    # buggy
    s.append('<g transform="translate(436 176) scale(.55)"><path d="M10 30 Q2 14 14 8 L22 6 L26 0 L30 2 L28 8 Q36 12 34 20 L32 30Z" fill="#8A4B2A"/>'
             '<rect x="34" y="12" width="34" height="14" rx="3" fill="#2B1D12"/><circle cx="40" cy="30" r="7" fill="none" stroke="#2B1D12" stroke-width="2.5"/><circle cx="62" cy="30" r="7" fill="none" stroke="#2B1D12" stroke-width="2.5"/>'
             '<circle cx="50" cy="6" r="4" fill="#C8553D"/><circle cx="58" cy="7" r="3.5" fill="#5B4A36"/></g>')
    # falling petals
    s.append('<g class="b7-petals" fill="#FFFFFF">' + ''.join('<circle cx="%d" cy="%d" r="2.4" opacity=".9"/>' % (rng.randint(60, 860), rng.randint(90, 200)) for _ in range(26)) + '</g>')
    s.append('</svg>')
    css = ('.b7-sway{animation:b7sway 6s ease-in-out infinite;transform-origin:460px 260px}'
           '@keyframes b7sway{0%,100%{transform:rotate(0)}50%{transform:rotate(.35deg)}}'
           '.b7-petals{animation:b7fall 9s linear infinite}@keyframes b7fall{from{transform:translate(0,-10px)}to{transform:translate(-30px,40px);opacity:.2}}'
           '.b7-star{animation:b7tw 2.6s ease-in-out infinite;transform-origin:745px 53px}@keyframes b7tw{50%{opacity:.6}}')
    return ''.join(s), css


def keepsake_blossom(size=120, cls='keep'):
    """A pressed apple blossom on a little paper label, taped down."""
    pet = ''.join('<ellipse cx="60" cy="38" rx="13" ry="19" fill="#FDF1F3" stroke="#E7B3C2" stroke-width="1.5" transform="rotate(%d 60 60)"/>' % a for a in range(0, 360, 72))
    return ('<svg class="%s" viewBox="0 0 120 120" width="%d" height="%d" aria-hidden="true">'
            '<rect x="12" y="12" width="96" height="96" rx="6" fill="#FFFBF1" stroke="#E5D3AE" stroke-width="2" transform="rotate(-4 60 60)"/>'
            '<path d="M60 64 Q70 90 92 100" stroke="#6E8F5A" stroke-width="3" fill="none"/><ellipse cx="82" cy="88" rx="9" ry="4" fill="#7FA66A" transform="rotate(30 82 88)"/>'
            '%s<circle cx="60" cy="60" r="8" fill="#F6C27A"/><g fill="#C7922C"><circle cx="56" cy="57" r="1.4"/><circle cx="63" cy="56" r="1.4"/><circle cx="61" cy="63" r="1.4"/></g>'
            '<rect x="40" y="6" width="40" height="13" fill="#F2E3B8" opacity=".85" transform="rotate(-6 60 12)"/></svg>') % (cls, size, size, pet)


def bookmark(color='#B5476B'):
    return ('<svg viewBox="0 0 90 150" aria-hidden="true"><path d="M14 4 H76 V140 L45 118 L14 140Z" fill="%s"/>'
            '<path d="M20 10 H70 V128 L45 110 L20 128Z" fill="none" stroke="#FFF3DC" stroke-width="2" stroke-dasharray="4 4"/>'
            '<rect x="30" y="30" width="30" height="36" rx="2" fill="#FFF3DC"/><path d="M33 34 h24 v28 h-24z" fill="#BFD9E0"/><path d="M45 34 v28 M33 48 h24" stroke="#FFF3DC" stroke-width="2"/>'
            '<circle cx="45" cy="86" r="6" fill="#FFF3DC"/></svg>') % color


def postcard_stamp_blossom():
    return keepsake_blossom(60, 'pcs')


BANNERS = {'avenue': banner_avenue}
KEEPSAKES = {'blossom': keepsake_blossom}
STAMPS = {'blossom': postcard_stamp_blossom}
