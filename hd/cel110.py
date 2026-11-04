# v110 (B1): gà nở, gà con lớn, vịt con nở là sự kiện chúc mừng: camera bay tới (khi rảnh tay), pháo giấy, tiếng, chữ bay.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)
rep("if (on && g.news){ const nw = g.news, b = g.brood, r = g.res || {}; g.news = null; gaSpawn();",
    "if (on && g.news){ const nw = g.news, b = g.brood, r = g.res || {}; g.news = null; gaSpawn(); if (nw === 'no' || nw === 'lon') celebAt(nw === 'no' ? NEST : COOPC);")
rep("function gaTick(t){",
    "function celebAt(p){ try { if (!busy() && !VISIT) camTo(new T.Vector3(p.x, .3, p.z), Math.max(cam.zoom, DEFZ() * 2.2)); } catch (e) {} setTimeout(() => { try { pv.set(p.x, (p.y || .4) + .3, p.z).project(cam); confettiAt((pv.x + 1) / 2 * innerWidth, (1 - pv.y) / 2 * innerHeight, 40, 1.1); for (let i = 0; i < 12; i++) puff('leaf', p.x + R(-.25, .25), (p.y || .3) + .2, p.z + R(-.25, .25), 1, pick(['#ffe266', '#F5D27A', '#FBF7EE']), .6); } catch (e) {} try { sfx('up'); aud('chiep'); } catch (e) {} buzz(30); }, 700); }   /* nở, lớn: chúc mừng */\nfunction gaTick(t){")
rep("L.done++; L.kid = Date.now(); vitSpawn();", "L.done++; L.kid = Date.now(); vitSpawn(); celebAt({ x: LO.at[0], y: .3, z: LO.at[1] });")
rep("const BUILD = 'v110a'", "const BUILD = 'v110a'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
