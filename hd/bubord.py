#!/usr/bin/env python3
"""v98: bong bóng chồng nhau không lẫn lớp: mỗi bong bóng vẽ trọn một khối, cái gần camera nằm trên."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("try { pingTick(dt); navaTick(dt); }", """try { pingTick(dt); navaTick(dt); bubOrder(); }""")
rep("function navaTick(dt){", """const BUBO = []; function bubOrder(){ BUBO.length = 0; for (const g of (window.__BUBALL || [])){ if (!g.visible || !g.parent) continue; let o = g.parent, v = true; while (o){ if (!o.visible){ v = false; break; } o = o.parent; } if (!v) continue; if (!g.userData.tr){ g.userData.tr = 1; g.userData.sub = []; g.traverse(m => { if (m !== g && m.isGroup) g.userData.sub.push(m); if (m.isMesh && m.material && m.material.visible !== false){ m.material.transparent = true; m.material.needsUpdate = true; } }); } g.getWorldPosition(pv); g.userData.cd = pv.distanceToSquared(cam.position); BUBO.push(g); } BUBO.sort((a, b) => b.userData.cd - a.userData.cd); for (let i = 0; i < BUBO.length; i++){ const g = BUBO[i]; g.renderOrder = 20 + i; for (const q of g.userData.sub) q.renderOrder = 20 + i; } }   /* nhóm con (icon) cùng thứ tự với bong bóng, không thì icon bị vẽ trước rồi bị đĩa che */   /* mọi lớp của bong bóng cùng nằm nhóm trong suốt để sắp theo khối; bong bóng xa vẽ trước, gần vẽ sau; trong một bong bóng giữ lớp viền, đĩa, vòng, icon */
function navaTick(dt){""")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
