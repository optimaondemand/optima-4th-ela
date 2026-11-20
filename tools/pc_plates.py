#!/usr/bin/env python3
"""Prince Caspian chapter plates from public-domain paintings (Wikimedia Commons), Nov 20 2026.
Source images: the 1400px Commons thumbnails, downloaded as ~/Downloads/pcpd-<ch>.jpg.
Writes assets/plates/pc-ch<N>.jpg and sets DATA.plate {src, alt, credit} on all 20 PC lessons (26-30)."""
import io, json, os, glob, subprocess, sys
from PIL import Image
DL = os.path.expanduser(sys.argv[1]) if len(sys.argv) > 1 else os.path.expanduser('~/mnt/Downloads')
P = {
 1: ('Kuindzhi At Valaam island 1873.jpg', 'On Valaam Island', 'Arkhip Kuindzhi', '1873',
     'A wild, rocky island shore under a dark sky, with thin trees and a wood behind.'),
 2: ('Turner Tintern1.jpg', 'The Transept of Tintern Abbey', 'J. M. W. Turner', '1794',
     'The roofless ruin of a great stone hall, its tall arches open to the sky and hung with ivy.'),
 3: ('Winslow Homer - The Fog Warning - Google Art Project.jpg', 'The Fog Warning', 'Winslow Homer', '1885',
     'A man rows a small boat over rough grey water, looking back over his shoulder.'),
 4: ('Joseph Wright of Derby - Philosopher giving a lecture on the orrery - Google Art Project.jpg', 'A Philosopher Lecturing on the Orrery', 'Joseph Wright of Derby', 'about 1766',
     'A teacher shows a model of the planets by lamplight while children lean in to watch.'),
 5: ('Ivan Bilibin 024.jpg', 'The Black Horseman, for Vasilisa the Beautiful', 'Ivan Bilibin', '1899–1900',
     'A rider on a dark horse travels through a forest at night.'),
 6: ('Böcklin - Centaur at the Village Blacksmith, 1888, 26.B.jpg', 'Centaur at the Village Blacksmith', 'Arnold Böcklin', '1888',
     'A centaur stands at a village forge, lifting a hoof for the smith while villagers stare.'),
 7: ('John Constable - Stonehenge - Google Art Project.jpg', 'Stonehenge', 'John Constable', '1835',
     'Ancient standing stones on a wide plain under a stormy sky with a double rainbow.'),
 8: ('Winslow Homer - Breezing Up (A Fair Wind) - Google Art Project.jpg', 'Breezing Up (A Fair Wind)', 'Winslow Homer', '1873–1876',
     'Three boys and a man sail a small boat that leans into the wind over choppy water.'),
 9: ('Shishkin, Ivan - Morning in a Pine Forest.jpg', 'Morning in a Pine Forest', 'Ivan Shishkin and Konstantin Savitsky', '1889',
     'Bear cubs climb a fallen tree in a misty pine forest.'),
 10: ('Briton Rivière - Una and the Lion.jpg', 'Una and the Lion', 'Briton Rivière', '1880',
     'A girl in a white dress walks beside a great lion at the edge of a dark wood.'),
 11: ('Rosa Bonheur - Lion (The look out).jpg', 'Lion (The Lookout)', 'Rosa Bonheur', '19th century',
     'A lion stands alone on open ground, head up, looking into the distance.'),
 12: ('Joseph Wright of Derby The Alchemist.jpg', 'The Alchemist Discovering Phosphorus', 'Joseph Wright of Derby', '1771',
     'A man kneels in a dark, vaulted room lit only by a glowing flask.'),
 13: ('Tavernier Jean Mielot.jpg', 'Jean Miélot at His Desk', 'Jean Le Tavernier', 'about 1450–1460',
     'A scribe in a hooded robe writes carefully at a slanted desk surrounded by books.'),
 14: ('San Romano Battle (Paolo Uccello, London) 01.jpg', 'The Battle of San Romano', 'Paolo Uccello', 'about 1438–1440',
     'Knights in armour on white and dark horses charge with long lances.'),
 15: ('Claude Monet - Arrival of the Normandy Train, Gare Saint-Lazare - Google Art Project.jpg', 'Arrival of the Normandy Train, Gare Saint-Lazare', 'Claude Monet', '1877',
     'A steam train comes into a busy glass-roofed railway station full of smoke and light.'),
}
def credit(n):
    t, a, y = P[n][1], P[n][2], P[n][3]
    return f'{t}, {a}, {y}. Public domain, via Wikimedia Commons.'
os.makedirs('assets/plates', exist_ok=True)
for n in P:
    im = Image.open(os.path.join(DL, f'pcpd-{n}.jpg')).convert('RGB')
    im.thumbnail((1400, 1400)); im.save(f'assets/plates/pc-ch{n}.jpg', quality=84, optimize=True, progressive=True)
day4 = {26: 2, 27: 6, 28: 9, 29: 11, 30: 15}
for w in range(26, 31):
    for d in range(1, 5):
        ch = (w - 26) * 3 + d if d < 4 else day4[w]
        page = glob.glob(f'lesson-{w}-{d}-*.html')[0]; df = f'data/lesson-{w}-{d}.json'
        cap = credit(ch) if d < 4 else f'From Chapter {ch}. ' + credit(ch)
        io.open('/tmp/plate_patch.json', 'w', encoding='utf-8').write(json.dumps({'plate': {'src': f'plates/pc-ch{ch}.jpg', 'alt': P[ch][4], 'credit': cap}}, ensure_ascii=False))
        subprocess.run([sys.executable, 'tools/setdata.py', page, df, '/tmp/plate_patch.json', '--apply'], check=True)
with io.open('assets/plates/pc-CREDITS.md', 'w', encoding='utf-8') as f:
    f.write('# Prince Caspian chapter plates (weeks 26–30)\n\nPublic-domain paintings, not book illustrations. Downloaded Nov 20 2026 as the 1400px Wikimedia Commons thumbnail; every file is marked Public domain on Commons.\n\n| File | Chapter | Title | Artist | Date | Source |\n|---|---|---|---|---|---|\n')
    for n, (fn, t, a, y, _) in P.items():
        f.write(f'| pc-ch{n}.jpg | {n} | {t} | {a} | {y} | https://commons.wikimedia.org/wiki/File:{fn.replace(" ", "_")} |\n')
print('ok')
