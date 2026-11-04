# v110b — Tre trăm đốt: săn tìm đốt tre khó hơn (anh Ares 4/11)
#  Trước: 10 đống, mỗi đống 10 đốt, hiện hết một lượt, có quầng sáng, một đống vướng chuồng vịt không chạm được.
#  Nay: mỗi đống 5 đốt (20 lần lượm), chỉ 2 đống nằm ngoài vườn một lúc, lượm xong 20–40 phút sau mới rớt đống khác ở chỗ khác;
#  16 chỗ quanh khu cây tre, né chuồng gà vịt và mé sông; không quầng sáng, chỉ lâu lâu lóe một chút cho người chịu kiếm.
# Dùng: python3 tre110.py live/v110b.html live/v110b.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)

rep("FTDOT = { need: 100, spots: [[-1.6, 6.6], [-5.6, 6.4], [-8.6, 6.0], [-2.4, 7.9], [-6.6, 7.8], [-1.6, 3.4], [-9.0, 3.4], [-2.2, 4.4], [-9.4, 5.0], [-4.8, 8.4]] };",
    "FTDOT = { need: 100, per: 5, show: 2, wait: [20, 40], spots: [[-3.0, 5.6], [-4.2, 4.0], [-5.6, 6.4], [-8.6, 6.0], [-2.6, 7.9], [-6.6, 7.8], [-9.0, 3.4], [-9.4, 5.0], [-4.6, 7.2], [-7.6, 3.2], [-3.6, 3.0], [-5.2, 2.6], [-8.0, 7.0], [-6.2, 5.2], [-3.4, 6.8], [-7.0, 6.6]] };   /* 5 đốt một đống, 2 đống một lúc, lượm rồi 20–40 phút mới rớt đống khác */")
rep("function fdBuild(){ const F = ST.ft.tretramdot, key = F && F.st === 2 ? (F.dot || 0) + '' : ''; if (key === FDV.key) return; FDV.key = key; for (const d of FDV.list) FDV.root.remove(d.g); FDV.list = []; if (!key) return; const left = Math.ceil((FTDOT.need - (F.dot || 0)) / 10);\n  FTDOT.spots.slice(0, left).forEach(([x, z], i) => { const g = G(x, 0, z, i * 1.3, FDV.root), pr = ROOT; ROOT = g; for (let k = 0; k < 4; k++) M(cyl(.04, .044, .13, 6), TTM.culm, Math.cos(k * 1.6) * .08, .04 + (k > 2 ? .06 : 0), Math.sin(k * 1.6) * .08, { r: [Math.PI / 2, k, 0] }); M(cyl(.05, .05, .015, 6), TTM.node, 0, .085, 0, { cast: false }); ftHalo(g, .15, .7, .5); ROOT = pr;",
    "function fdSpawn(){ const F = ST.ft.tretramdot; if (!F || F.st !== 2) return; const left = Math.ceil((FTDOT.need - (F.dot || 0)) / FTDOT.per); F.dsp = (F.dsp || []).filter(i => FTDOT.spots[i]); const now = Date.now(), add = () => { const free = FTDOT.spots.map((_, i) => i).filter(i => !F.dsp.includes(i) && i !== F.dlast); F.dsp.push(free[Math.floor(Math.random() * free.length)]); };\n  if (F.dnx == null){ while (F.dsp.length < Math.min(FTDOT.show, left)) add(); F.dnx = 0; save(); return; } if (F.dsp.length < Math.min(FTDOT.show, left) && now >= F.dnx){ add(); F.dnx = now + (FTDOT.wait[0] + Math.random() * (FTDOT.wait[1] - FTDOT.wait[0])) * 60000 / (ST.spd || 1); save(); } }\nfunction fdBuild(){ fdSpawn(); const F = ST.ft.tretramdot, key = F && F.st === 2 ? (F.dot || 0) + '/' + (F.dsp || []).join() : ''; if (key === FDV.key) return; FDV.key = key; for (const d of FDV.list) FDV.root.remove(d.g); FDV.list = []; if (!key) return;\n  (F.dsp || []).forEach(i => { const [x, z] = FTDOT.spots[i], g = G(x, 0, z, i * 1.3, FDV.root), pr = ROOT; ROOT = g; for (let k = 0; k < 3; k++) M(cyl(.035, .038, .12, 6), TTM.culm, Math.cos(k * 2.1) * .06, .035, Math.sin(k * 2.1) * .06, { r: [Math.PI / 2, k * 1.1, 0] }); ROOT = pr;")
rep("FDV.list.push({ g, h, i }); }); }", "FDV.list.push({ g, h, i }); }); }   /* không quầng sáng: phải đi kiếm */")
rep("fdBuild(); for (const d of FDV.list) d.g.position.y = Math.abs(Math.sin(t * 2 + d.i)) * .03;",
    "fdBuild(); for (const d of FDV.list){ d.g.position.y = 0; if (Math.random() < .004) puff('spark', d.g.position.x, .12, d.g.position.z, 1, '#FFE36A', .35); }   /* lâu lâu lóe một chút */")
rep("F.dot = Math.min(FTDOT.need, (F.dot || 0) + 10); const p = d.g.position; for (let i = 0; i < 10; i++) puff('spark', p.x, .2, p.z, 1, '#FFE36A', .8); floatAt(p.x, .5, p.z, `+10 đốt tre · ${F.dot}/${FTDOT.need}`, '#F5D27A');",
    "F.dot = Math.min(FTDOT.need, (F.dot || 0) + FTDOT.per); F.dsp = (F.dsp || []).filter(x => x !== d.i); F.dlast = d.i; F.dnx = Math.max(F.dnx || 0, Date.now() + (FTDOT.wait[0] + Math.random() * (FTDOT.wait[1] - FTDOT.wait[0])) * 60000 / (ST.spd || 1)); const p = d.g.position; for (let i = 0; i < 8; i++) puff('spark', p.x, .2, p.z, 1, '#FFE36A', .8); floatAt(p.x, .5, p.z, `+${FTDOT.per} đốt tre · ${F.dot}/${FTDOT.need}`, '#F5D27A');")
rep("return say(`Còn ${FTDOT.need - (F.dot || 0)} đốt tre rớt quanh vườn đó con, đi gom đủ một trăm đốt rồi lại đây.`, 'dan', { now: true }); }",
    "return say(`Còn ${FTDOT.need - (F.dot || 0)} đốt nữa con. Đốt tre rớt lẻ tẻ quanh khu bụi tre, có khi nằm khuất trong cỏ, lâu lâu mới rớt thêm. Chịu khó đi kiếm nghe.`, 'dan', { now: true }); }")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
