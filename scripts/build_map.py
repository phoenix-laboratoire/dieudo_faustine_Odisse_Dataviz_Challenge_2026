"""Génère data/regions.json (chemins SVG simplifiés) depuis le GeoJSON des régions.
Source du fond de carte : github.com/gregoiredavid/france-geojson (données IGN/Etalab, licence ouverte).
Usage : pip install shapely && python scripts/build_map.py"""
import json, math
from shapely.geometry import shape
G = json.load(open("scripts/regions-avec-outre-mer.geojson", encoding="utf-8"))
METRO = {"11","24","27","28","32","44","52","53","75","76","84","93","94"}
DROM = ["01","02","03","04"]          # Mayotte (06) absente des données du Baromètre
K = math.cos(math.radians(46.5))
def rings(geom, tol):
    g = geom.simplify(tol, preserve_topology=True)
    polys = [g] if g.geom_type == "Polygon" else list(g.geoms)
    return [list(p.exterior.coords) for p in polys if p.area > tol * tol * 4]
def path(rs, f):
    return "".join("M" + "L".join(f(x, y) for x, y in r) + "Z" for r in rs)
out, feats = [], {f["properties"]["code"]: f for f in G["features"]}
# métropole : projection équirectangulaire corrigée, largeur 560
mx = [shape(feats[c]["geometry"]).bounds for c in METRO]
x0, x1 = min(b[0] for b in mx) * K, max(b[2] for b in mx) * K
y0, y1 = min(b[1] for b in mx), max(b[3] for b in mx)
s = 560 / (x1 - x0); H = (y1 - y0) * s
for c in METRO:
    f = feats[c]
    d = path(rings(shape(f["geometry"]), 0.03), lambda x, y: f"{(x*K-x0)*s:.1f},{(y1-y)*s:.1f}")
    out.append({"c": c, "n": f["properties"]["nom"], "d": d})
# DROM : cadres 74x74 sous la métropole
frames, y_off = [], H + 14
for i, c in enumerate(DROM):
    f = feats[c]; g = shape(f["geometry"]); b = g.bounds
    kk = math.cos(math.radians((b[1] + b[3]) / 2))
    w, h = (b[2]-b[0]) * kk, b[3]-b[1]; sc = 60 / max(w, h)
    ox = 8 + i * 84 + (74 - w*sc) / 2; oy = y_off + 4 + (74 - h*sc) / 2
    d = path(rings(g, 0.01), lambda x, y: f"{ox+(x-b[0])*kk*sc:.1f},{oy+(b[3]-y)*sc:.1f}")
    out.append({"c": c, "n": f["properties"]["nom"], "d": d})
    frames.append([8 + i * 84, y_off, 74, 78])
json.dump({"w": 560, "h": round(y_off + 82), "frames": frames, "regions": out}, open("data/regions.json", "w", encoding="utf-8"), ensure_ascii=False, separators=(",", ":"))
