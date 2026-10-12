import sys, json
from shapely.geometry import LineString, Polygon, box, Point, MultiPolygon
from shapely.ops import linemerge, unary_union, polygonize
X0,X1,Y0,Y1 = 3000,11200,6850,10600
K=1.7727; S=640/(X1-X0)
H=(Y1-Y0)*K*S
def P(x,y): return ((x-X0)*S, (Y1-y)*K*S)
frame=box(X0,Y0,X1,Y1)
C=[];W=[];G=[]
for ln in open('/tmp/claude-0/map/data.txt',encoding='utf8'):
    ln=ln.strip()
    if not ln: continue
    c,n,r,i,pts=ln.split('|')
    v=list(map(int,pts.split(',')))
    p=list(zip(v[0::2],v[1::2]))
    (C if c=='C' else W if c=='W' else G).append((n,r,p))
lines=[LineString(p) for n,r,p in C if len(p)>1 and not (p[0]==p[-1] and len(p)>3)]
rings=[Polygon(p) for n,r,p in C if len(p)>3 and p[0]==p[-1]]  # closed coastline rings = islands (land)
merged=linemerge(lines)
segs=list(merged.geoms) if hasattr(merged,'geoms') else [merged]
print('chains',len(segs), [ (s.coords[0],s.coords[-1], s.is_ring) for s in segs if not s.is_ring][:20], file=sys.stderr)
# polygonize chains + frame boundary
allines=unary_union([s for s in segs]+[frame.exterior])
faces=list(polygonize(allines))
coastsegs=[]
for s in segs:
    cs=list(s.coords)
    for a,b in zip(cs,cs[1:]): coastsegs.append((a,b))
def side(pt):
    best=None
    for a,b in coastsegs:
        ls=LineString([a,b]); d=ls.distance(pt)
        if best is None or d<best[0]: best=(d,a,b)
    d,a,b=best
    cr=(b[0]-a[0])*(pt.y-a[1])-(b[1]-a[1])*(pt.x-a[0])
    return 'land' if cr>0 else 'water'
land=[]
for f in faces:
    f=f.intersection(frame)
    if f.is_empty or f.area<1: continue
    rp=f.representative_point()
    if side(rp)=='land': land.append(f)
landU=unary_union(land+[r for r in rings if r.is_valid])
waterU=frame.difference(landU)
wp=[]
for n,r,p in W:
    if len(p)<4: continue
    try: wp.append((r,Polygon(p).buffer(0)))
    except Exception as e: pass
outer=unary_union([g for r,g in wp if r=='o']); inner=unary_union([g for r,g in wp if r=='i'] or [Polygon()])
waterAll=unary_union([waterU, outer.difference(inner)]).intersection(frame)
def path(geom, tol=0):
    if tol: geom=geom.simplify(tol)
    polys=geom.geoms if hasattr(geom,'geoms') else [geom]
    out=[]
    for pg in polys:
        if pg.geom_type!='Polygon' or pg.area<20: continue
        for ring in [pg.exterior]+list(pg.interiors):
            pts=[P(x,y) for x,y in ring.coords][:-1]
            out.append('M'+' L'.join('%.1f %.1f'%q for q in pts)+'Z')
    return ''.join(out).replace(' L','L').replace('.0 ',' ').replace('.0L','L').replace('.0Z','Z')
res={'H':H,'water':path(waterAll,4)}
gd={}
for n,r,p in G:
    gd.setdefault(n,[]).append(Polygon(p).buffer(0))
res['green']={n:path(unary_union(v).intersection(frame),4) for n,v in gd.items()}
json.dump(res,open('/tmp/claude-0/map/paths.json','w'),ensure_ascii=False)
print(H, len(res['water']), {k:len(v) for k,v in res['green'].items()})
