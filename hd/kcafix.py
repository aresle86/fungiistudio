#!/usr/bin/env python3
"""v101: khạp cá kỷ lục dời ra khỏi thềm nhà (đứng trên sân, cách lan can), và thành món mua: tới cấp câu cá thì bến có 'Khạp nuôi cá' 120 xu,
việc hôm nay nhắc mua; người đã có cá trong Sổ thì được sẵn khạp. Mua xong camera bay tới, Ngoại dặn một câu."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("const KCA = { at: [1.6, 2.05], r: .2 };", "const KCA = { at: [1.22, 2.24], r: .2, xu: 120 };   /* đứng trên sân trước hiên, cách lan can, không chạm đá lối đi */")
rep("const lb = G(KCA.at[0] + .42, 0, KCA.at[1] + .12, 0, root);", "const lb = G(KCA.at[0] - .4, 0, KCA.at[1] + .06, 0, root);")
rep("on = cauOn() && ks.length > 0 && !VISIT;", "on = cauOn() && !!ST.kca && !VISIT;")
rep("function kcaTick(t){", "if (ST.kca == null && Object.keys(ST.fishLog || {}).some(k => FISHK[k] && ST.fishLog[k].n)) ST.kca = 1;   /* người chơi cũ đã thấy khạp: giữ nguyên */\nfunction kcaTick(t){")
rep("  return h + nbHTML(); }", "  if (cauOn() && !ST.kca) h += UX.title('Nuôi cá kỷ lục') + '<div class=\"upg\">' + UX.upc('kcabuy', ICON.khap || ICON.caro, 'Khạp nuôi cá trước hiên', KCA.xu, { dis: ST.xu < KCA.xu, why: ST.xu < KCA.xu ? `còn thiếu ${KCA.xu - ST.xu} xu` : '' }) + '</div>';\n  return h + nbHTML(); }")
rep("else if (a === 'vitup') vit.up();", "else if (a === 'vitup') vit.up(); else if (a === 'kcabuy'){ if (ST.kca || ST.xu < KCA.xu) return; ST.xu -= KCA.xu; ST.kca = 1; coinPop(`-${KCA.xu} xu · khạp nuôi cá`, '#F08A6E'); sfx('up'); save(); hud(); try { bump('own', 1, 'kca'); } catch (e) {} closeSheet(); camTo(new T.Vector3(KCA.at[0], .3, KCA.at[1]), Math.max(cam.zoom, DEFZ() * 2)); setTimeout(() => { for (let i = 0; i < 14; i++) puff('spark', KCA.at[0] + R(-.25, .25), .35, KCA.at[1] + R(-.2, .2), 1, pick(['#9cc6e0', '#F5D27A', '#FBF7EE']), .6); say('Khạp này để nuôi mấy con cá to nhất con câu được. Câu được con nào bự hơn là Ngoại thả vô đây cho khách coi.', 'vui', { now: true }); }, 700); }")
rep("  try { if (cauOn()) F.push({ lv: CAU.lv, t: 'fish', txt: 'Câu 2 con cá', need: 2, rw: ['coin', 20] }); } catch (e) {}",
    "  try { if (cauOn()) F.push({ lv: CAU.lv, t: 'fish', txt: 'Câu 2 con cá', need: 2, rw: ['coin', 20] }); if (cauOn() && !ST.kca) F.push({ lv: CAU.lv + .4, t: 'own', k: 'kca', txt: 'Mua khạp nuôi cá trước hiên', need: 1, rw: ['coin', 20] }); } catch (e) {}")
rep("function ownCheck(){ try { ensureTasks(); for (const x of ST.tasks.list) if (x.t === 'own' && !x.done && ownObj(x.k)) bump('own', 1, x.k); } catch (e) {} }",
    "function ownCheck(){ try { ensureTasks(); for (const x of ST.tasks.list) if (x.t === 'own' && !x.done && (x.k === 'kca' ? !!ST.kca : ownObj(x.k))) bump('own', 1, x.k); } catch (e) {} }")
rep("  else if (t === 'own'){ try { suaOn(true); }", "  else if (t === 'own' && k === 'kca'){ openSheet('ben'); return; }\n  else if (t === 'own'){ try { suaOn(true); }")
rep("const TASKIC = x => x.t === 'own' ?", "const TASKIC = x => x.t === 'own' && x.k === 'kca' ? (ICON.khap || ICON.caro) : x.t === 'own' ?")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
