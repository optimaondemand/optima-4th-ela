import json
exec(open('build.py').read().split("res={'H'")[0].replace("print('chains'","pass #"))
d=json.load(open('paths.json'))
W_,H_=640,round(H)
def q(x,y):
    a,b=P(x,y); return '%.0f %.0f'%(a,b)
def pl(pts): return 'M'+' L'.join(q(*t) for t in pts)
ROADS_MAJOR=[
 [(7978,9627),(7841,9856),(7781,9961),(7746,10092),(7751,10381),(7755,10900)],             # Østerbrogade
 [(6310,8699),(6172,8749),(5583,8972),(5395,9092),(4921,9408),(4029,9997),(3731,10113)],     # Nørrebrogade
 [(6735,7579),(6449,7452),(6077,7333),(5564,7233),(5171,7267),(4974,7261),(3998,7018),(2900,6900)], # Vesterbrogade
 [(7829,7187),(6807,7694),(6626,7855),(6588,7909),(6962,8214),(7355,8458),(7676,8664),(7901,8772),(8197,8920),(8628,9028),(8831,9083)], # the old wall line (Voldgaderne)
 [(8655,7516),(8798,7428),(9449,7077),(9615,6871),(9700,6780)],  # Knippelsbro + Torvegade
 [(7710,7100),(8012,6949),(8200,6820)],  # Langebro
]
ROADS_MINOR=[
 [(9073,9698),(9030,9964),(8857,10210),(8808,10344),(8695,10478),(8600,10673)], # Strandboulevarden
 [(8007,9634),(9162,9909)],  # Classensgade
 [(6113,9087),(6662,9388),(7177,9657),(7553,9858),(7781,9961)], # Blegdamsvej
 [(6594,8657),(8529,8144)],  # Gothersgade
 [(8734,8087),(9284,8760)],  # Bredgade
 [(8529,8144),(9027,8734)],  # Store Kongensgade
 [(9027,8734),(9897,8834)],  # Esplanaden
 [(6922,7638),(7285,7802),(7391,7842),(7614,7861),(7970,7898),(8241,7953),(8496,8031)], # Strøget
 [(7121,8046),(7509,8136)],  # Krystalgade
 [(8257,7670),(8555,7758),(8632,7762)], # Holmens Kanal
 [(7978,9627),(8065,9548),(8462,9341)], # toward Østerport
 [(6525,8620),(6247,8726)], # Dronning Louises Bro
]
green=d['green']
def txt(x,y,s,cls,rot=0,anchor='middle'):
    a,b=P(x,y); t=' transform="rotate(%d %.0f %.0f)"'%(rot,a,b) if rot else ''
    return '<text class="%s" x="%.0f" y="%.0f" text-anchor="%s"%s>%s</text>'%(cls,a,b,anchor,t,s)
svg=[]
svg.append('<svg viewBox="0 0 %d %d" role="img" aria-label="A map of Copenhagen in 1943: the old town, the harbor, Christianshavn, the lakes and Østerbro, with pins on places from the story">'%(W_,H_))
svg.append('<defs><radialGradient id="nkPar" cx="50%" cy="45%" r="75%"><stop offset="0" stop-color="#FBF4E2"/><stop offset=".8" stop-color="#F1E4C4"/><stop offset="1" stop-color="#E2CFA2"/></radialGradient>'
 '<pattern id="nkHatch" width="6" height="6" patternUnits="userSpaceOnUse" patternTransform="rotate(-30)"><path d="M0 3 H6" stroke="#A9C4CC" stroke-width=".7"/></pattern>'
 '<style>.nkq{font:600 11px Lora,Georgia,serif;letter-spacing:2.5px;fill:#8C7444;opacity:.9}.nkw{font:italic 600 10.5px Lora,Georgia,serif;fill:#4F7A88}.nkg{font:italic 9px Lora,Georgia,serif;fill:#5E6E3E}.nks{font:italic 600 9.5px Lora,Georgia,serif;fill:#7A6237;paint-order:stroke;stroke:#F6EEDB;stroke-width:3px}.nkc{font:8px Nunito,sans-serif;fill:#8C7444}</style></defs>')
svg.append('<rect width="%d" height="%d" fill="url(#nkPar)"/>'%(W_,H_))
# parks under water so moats sit on top
for n,v in green.items():
    fill='#D6DDB4' if n!='Christianshavns Vold' else '#D9DDB8'
    svg.append('<path d="%s" fill="%s" stroke="#A9B887" stroke-width=".6"/>'%(v,fill))
svg.append('<path d="%s" fill="#C9DCE0" fill-rule="evenodd" stroke="#8FAEB8" stroke-width=".8" stroke-linejoin="round"/>'%d['water'])
svg.append('<path d="%s" fill="url(#nkHatch)" fill-rule="evenodd" opacity=".55"/>'%d['water'])
# roads
svg.append('<g fill="none" stroke-linecap="round" stroke-linejoin="round"><g stroke="#B49A68" stroke-width="2" opacity=".75">'+''.join('<path d="%s"/>'%pl(r) for r in ROADS_MAJOR)+'</g>'
           '<g stroke="#C2AB7E" stroke-width="1.1" opacity=".8">'+''.join('<path d="%s"/>'%pl(r) for r in ROADS_MINOR)+'</g></g>')
# Kastellet: re-draw the star on top of moat lines
svg.append('<path d="%s" fill="#E6DCB8" stroke="#8C7444" stroke-width="1"/>'%green['Kastellet'])
# quarter names
L=[]
L.append(txt(8520,9870,'ØSTERBRO','nkq',-12))
L.append(txt(4700,9150,'NØRREBRO','nkq',-33))
L.append(txt(4300,7330,'VESTERBRO','nkq',6))
L.append(txt(8060,8040,'INDRE BY','nkq',-10))
L.append(txt(8075,7975,'the old town','nkg',-10))
L.append(txt(9700,7330,'CHRISTIANSHAVN','nkq',-24))
L.append(txt(10640,7905,'HOLMEN','nkq'))
L.append(txt(10640,7840,'the navy base','nkg'))
L.append(txt(3900,8050,'FREDERIKSBERG','nkq',-60))
# water names
L.append(txt(6650,8860,'Søerne · the Lakes','nkw',35))
L.append(txt(9120,7540,'Inderhavnen · the harbor','nkw',-31))
L.append(txt(10330,9780,'to the Øresund','nkw',-72))
# parks + landmarks
L.append(txt(6900,10170,'Fælledparken','nkg'))
L.append(txt(7990,8540,'Kongens Have','nkg',-14))
L.append(txt(9440,9500,'Kastellet','nks'))
L.append(txt(9440,9445,'the star fort','nkg'))
L.append(txt(9570,10420,'Frihavnen','nkg',-78))
L.append(txt(9940,9180,'Langelinie','nkg',-78))
L.append(txt(7930,7690,'Christiansborg','nkg',-16))
L.append(txt(10935,9350,'Refshaleøen','nkg',-78))
# Østerbrogade street name along the street
svg.append(''.join(L))
# arrow to the Øresund
a=P(10450,10200); b=P(10900,10560)
svg.append('<path d="M%.0f %.0f L%.0f %.0f" stroke="#4F7A88" stroke-width="1.4" fill="none" marker-end="url(#nkArr)"/>'%(a[0],a[1],b[0],b[1]) if False else '')
# cartouche, compass, scale bar, credit
svg.append('<g transform="translate(16 16)"><rect width="170" height="46" rx="4" fill="#FFF9EA" stroke="#B49A68"/><rect x="3" y="3" width="164" height="40" rx="3" fill="none" stroke="#D8C69E"/>'
 '<text x="85" y="22" text-anchor="middle" font-family="Lora,Georgia,serif" font-size="15" font-weight="600" fill="#3B2E17">København</text>'
 '<text x="85" y="36" text-anchor="middle" font-family="Nunito,sans-serif" font-size="9" font-weight="800" letter-spacing="2" fill="#8C7444">COPENHAGEN · 1943</text></g>')
km=1000/0.6273*S; mi=804.67/0.6273*S
y0=H_-22
svg.append('<g transform="translate(16 %d)" font-family="Nunito,sans-serif" font-size="8.5" font-weight="700" fill="#6B5126">'%y0 +
 '<rect x="-6" y="-24" width="%.0f" height="38" rx="4" fill="#FFF9EA" opacity=".85"/>'%(km+34) +
 '<path d="M0 0 H%.1f" stroke="#6B5126" stroke-width="2"/><path d="M0 -4 V4 M%.1f -4 V4 M%.1f -3 V3" stroke="#6B5126" stroke-width="1.2"/>'%(km,km,km/2) +
 '<path d="M0 -8 H%.1f" stroke="#A88F5E" stroke-width="1"/><path d="M%.1f -11 V-5" stroke="#A88F5E"/>'%(mi,mi) +
 '<text x="%.1f" y="10" >1 kilometer</text><text x="%.1f" y="-12">½ mile</text></g>'%(km+4,mi+4))
cx,cy=W_-36,H_-44
svg.append('<g transform="translate(%d %d)" fill="#8C7444"><circle r="18" fill="#FFF9EA" fill-opacity=".8" stroke="#B49A68"/><path d="M0 -22 L4.5 0 L0 22 L-4.5 0 Z" opacity=".85"/><path d="M-22 0 L0 3.5 L22 0 L0 -3.5 Z" opacity=".45"/>'%(cx,cy) +
 '<text y="-25" text-anchor="middle" font-family="Nunito,sans-serif" font-size="9" font-weight="800">N</text></g>')
svg.append('<text class="nkc" x="%d" y="%d" text-anchor="end">Shorelines: © OpenStreetMap contributors, shown as they were in 1943</text>'%(W_-6,H_-4))
svg.append('<g class="pins"></g></svg>')
out=''.join(svg)
open('cph.svg.txt','w').write(out)
pins={'oster':(7880,9790),'home':(8150,10200),'shop':(7752,10380),'amal':(9333,8403),'syn':(7346,8112),'tivoli':(6860,7340),'holmen':(10300,8350)}
print(json.dumps({k:[round(v,0) for v in P(*xy)] for k,xy in pins.items()}), len(out), H_)
