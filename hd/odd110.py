# v110 việc lặt vặt (anh Ares 4/11): lá rụng hay hơn và rơi chỗ dễ thấy; lục bình trôi trên sông, vướng xuồng (ít dưới mương);
# lục bình không vô hố ủ nữa (đã dùng đan giỏ, cho vịt ăn); lần đầu có củi / lục bình thì có mũi tên vàng + vòng sáng chỉ chỗ.
# Dùng: python3 odd110.py live/v110a.html live/v110a.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)

rep("la: { lv: 2, max: 2, every: 40 * 60, name: 'Quét lá' }", "la: { lv: 2, max: 3, every: 18 * 60, name: 'Quét lá' }")
rep("  if (k === 'lucbinh'){ const DD = EXP ? [M1, M2, M4] : [M1, M2], d = DD[Math.floor(Math.random() * DD.length)]; return { x: rnd2(d[0] + .3, d[2] - .3), z: rnd2(d[1] + .14, d[3] - .14) }; }",
    "  if (k === 'lucbinh'){ if (Math.random() < .75){ const sn = [[3.15, R0 + .5], [5.7, R0 + .55], [-.8, R0 + .4]][Math.floor(Math.random() * 3)]; return Math.random() < .5 ? { x: sn[0] + rnd2(-.12, .12), z: sn[1] + rnd2(-.08, .08), r: 1 } : { x: rnd2(-1.5, 8.5), z: rnd2(R0 + .3, R0 + .75), r: 1 }; }   /* phần nhiều trôi trên sông, vướng mé xuồng, mé bến */\n    const DD = EXP ? [M1, M2, M4] : [M1, M2], d = DD[Math.floor(Math.random() * DD.length)]; return { x: rnd2(d[0] + .3, d[2] - .3), z: rnd2(d[1] + .14, d[3] - .14) }; }")
rep("  const t = [[6.95, -1.15], [12.6, 5.9], [12.9, 4.3]][Math.floor(Math.random() * 3)], a = Math.random() * 6.28, r = rnd2(.5, .85); return { x: t[0] + Math.cos(a) * r, z: t[1] + Math.abs(Math.sin(a)) * r }; }",
    "  if (k === 'la' && Math.random() < .7){ const t = [[6.5, 1.2], [7.1, .6], [4.6, 1.6], [-1.2, 4.2], [1.6, 6.4], [.6, 5.6]][Math.floor(Math.random() * 6)]; return { x: t[0] + rnd2(-.25, .25), z: t[1] + rnd2(-.2, .2) }; }   /* lá rụng dưới mấy gốc cây quanh sân, chỗ nhìn thấy */\n  const t = [[6.95, -1.15], [12.6, 5.9], [12.9, 4.3]][Math.floor(Math.random() * 3)], a = Math.random() * 6.28, r = rnd2(.5, .85); return { x: t[0] + Math.cos(a) * r, z: t[1] + Math.abs(Math.sin(a)) * r }; }")
rep("else if (o.k === 'lucbinh') g.position.y = .02 + Math.sin(t * 2 + o.x) * .008;",
    "else if (o.k === 'lucbinh'){ g.position.y = (o.r ? WLR + .045 : .02) + Math.sin(t * 2 + o.x) * .008; if (o.r) g.position.x = o.x + Math.sin(t * .4 + o.z * 3) * .05; }")
# mũi tên lần đầu
rep("  const h = new T.Mesh(new T.SphereGeometry(o.k === 'sau' ? .1 : .16, 8, 6), new T.MeshBasicMaterial({ visible: false })); h.userData.odd = o; g.add(h); ODDV.hits.push(h); return g; }",
    "  if ((o.k === 'cui' || o.k === 'lucbinh') && !(ST.seen || {})['pick_' + o.k]){ const ar = G(0, .3, 0, 0, g); M(cone(.035, .09, 4), '#F2C64A', 0, 0, 0, { p: ar, r: [Math.PI, 0, 0], cast: false }); g.userData.ar = ar; try { pingAt(o.x, o.z); } catch (e) {} }   /* lần đầu: mũi tên vàng + vòng sáng chỉ chỗ */\n  const h = new T.Mesh(new T.SphereGeometry(o.k === 'sau' ? .1 : .16, 8, 6), new T.MeshBasicMaterial({ visible: false })); h.userData.odd = o; g.add(h); ODDV.hits.push(h); return g; }")
rep("g.userData.ar.rotation.y = t * 1.5; } } }",
    "g.userData.ar.rotation.y = t * 1.5; }\n    if (g.userData.ar && o.k !== 'tre'){ const ar = g.userData.ar; if ((ST.seen || {})['pick_' + o.k]) ar.visible = false; else { ar.position.y = .26 + Math.abs(Math.sin(t * 3 + o.x)) * .06; ar.rotation.y = t * 1.5; } } } }")
rep("function oddDo(o){ const i = ST.odd.list.indexOf(o); if (i < 0) return; ST.odd.list.splice(i, 1); let txt = '';",
    "function oddDo(o){ const i = ST.odd.list.indexOf(o); if (i < 0) return; ST.odd.list.splice(i, 1); let txt = ''; if (o.k === 'cui' || o.k === 'lucbinh') ST.seen['pick_' + o.k] = 1;")
# lục bình không vô hố ủ
rep("  else if (o.k === 'lucbinh' && hoRoom()){ hoAdd(1); txt = '+1 phần vô hố ủ'; for (let k = 0; k < 6; k++) puff('drop', o.x, .05, o.z, 1, '#9cc6e0', .5); }\n", "")
rep("UX.card('Lá rụng, lục bình', '+1–2', '', '', ICON.la || ICON.lucbinh)", "UX.card('Lá rụng · quét sân', '+2', '', '', ICON.la)")
rep(" Quét lá rụng +2 phần, vớt lục bình +1 phần (vịt no rồi thì lục bình vô hố).", " Quét lá rụng dưới gốc cây quanh sân +2 phần.")
rep("lucbinh: 'Lục bình mọc nghẹt mương rồi. Vớt lên phơi khô, phủ liếp như rơm được đó con.'", "lucbinh: 'Lục bình trôi vướng mé sông kìa con. Vớt lên cho vịt ăn, phơi khô đan giỏ được đó.'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
