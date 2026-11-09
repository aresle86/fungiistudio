# -*- coding: utf-8 -*-
# v123b sau v123a: (1) tưới/hái/rải rơm cây trái 2 ô: rê qua ô dưới cũng tính cho cây;
# (2) lý do mua của hàng xóm hợp với cả đơn, không lấy theo món đầu;
# (3) ghe bẹo: bỏ giao bớt, đủ đơn mới giao; đơn ghe 2-3 món.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)

rep("BUILD = 'v123a'", "BUILD = 'v123b'")

# (1) ô dưới của cây trái 2 ô trả về ô chủ (ô trên, nơi lưu cây)
rep("const plotAt = (x, z) => PLOTS.find(", "const pairUp = P => { if (!P || !P.bai) return P; try { const h = pairHost(P.id); return h ? PL[h] : P; } catch (e) { return P; } };\nconst plotAt = (x, z) => pairUp(plotAt0(x, z));\nconst plotAt0 = (x, z) => PLOTS.find(")
rep("const plotNear = (x, z, tol) => plotAt(x, z) || PLOTS.filter(P => !hidP(P) && !P.co).map(P => { const [u0, v0, u1, v1] = P.b; return [P, Math.hypot(Math.max(u0 - x, 0, x - u1), Math.max(v0 - z, 0, z - v1))]; }).filter(([, d]) => d < tol).sort((a, b) => a[1] - b[1]).map(([P]) => P)[0];",
    "const plotNear = (x, z, tol) => plotAt(x, z) || pairUp(PLOTS.filter(P => !hidP(P) && !P.co).map(P => { const [u0, v0, u1, v1] = P.b; return [P, Math.hypot(Math.max(u0 - x, 0, x - u1), Math.max(v0 - z, 0, z - v1))]; }).filter(([, d]) => d < tol).sort((a, b) => a[1] - b[1]).map(([P]) => P)[0]);")

# (2) lý do mua theo cả đơn
rep("const ORDCOMBO = [", """const NBOCC = ['đãi đám giỗ', 'nấu cơm đãi thợ gặt', 'dọn mâm cơm đãi khách', 'biếu sui gia', 'nấu cơm cho thợ cất nhà', 'cúng rằm'];   /* đơn nhiều món không ghép thành món nào: mua cho dịp trong nhà */
function ordWhy(items, id){ const ks = items.map(([k]) => k); if (ks.some(k => DISH[k])) return 'đãi khách'; const combo = ORDCOMBO.find(([a]) => a.every(x => ks.includes(x))); if (combo) return combo[1];
  const ws = [...new Set(ks.map(k => NBWHY[k] || 'nấu cơm chiều'))]; if (ws.length === 1) return ws[0]; let h = 0; for (const c of String(id || ks.join())) h = (h * 31 + c.charCodeAt(0)) >>> 0; return NBOCC[h % NBOCC.length]; }
const ordWhyOf = o => o.ghe || o.lead ? o.why : ordWhy(o.items, o.id);
const ORDCOMBO = [""")
rep("why: DISH[items[0][0]] ? 'đãi khách' : (NBWHY[items[0][0]] || 'nấu cơm chiều')", "why: ordWhy(items)")
rep("why: DISH[ks[0]] ? 'đãi khách' : combo ? combo[1] : (NBWHY[main] || 'nấu cơm chiều')", "why: ordWhy(items)")
rep("<span>mua về ${o.why}</span>", "<span>mua về ${ordWhyOf(o)}</span>")

# (3) ghe bẹo: không giao bớt nữa, đủ đơn mới giao (như đơn nhà bên); đơn ghe ít nhất 2 món
rep("${some ? '' : 'disabled'}>${full ? `Giao đủ · ${o.xu} xu` : 'Giao bớt'}</button></div></div>`; }",
    "${full ? '' : 'disabled'}>${full ? `Giao · ${o.xu} xu` : `Còn thiếu ${o.items.reduce((n, [k, q]) => n + Math.max(0, q - gheGot(o, k) - has(k)), 0)} món · ${o.xu} xu`}</button></div></div>`; }")
rep("function gheGive(el){ const g = ST.ghe, o = g.o; if (!o) return;", "function gheGive(el){ const g = ST.ghe, o = g.o; if (!o || !o.items.every(([k, q]) => gheGot(o, k) + has(k) >= q)) return;")
rep("function gheSim(){", """const gheQ = (k, q) => PHOI[k] || SAY[k] || MUOI[k] || DISH[k] ? Math.max(1, Math.min(2, q)) : FISHK[k] ? Math.min(2, q) : CROPS[k] && CROPS[k].tree ? Math.min(Math.max(2, q), Math.max(2, Math.round((CROPS[k].yield || 4) * .8))) : Math.min(8, Math.max(2, q));
function gheMore(items, n){ for (let t = 0; t < 6 && items.length < n; t++){ let o; try { o = ordMakeOld('ghe'); } catch (e) { break; } for (const [k, q] of o.items) if (items.length < n && !items.some(([x]) => x === k) && (!DISH[k] || has(k) >= 1)) items.push([k, gheQ(k, q)]); } return items; }   /* ghe đặt 2-3 món */
function gheLead(ld){ try { const it = gheMore([...ld.items], 2 + (Math.random() < .5 ? 1 : 0)), ex = it.slice(ld.items.length); ld.items = it; ld.xu += Math.round(ex.reduce((s2, [k, q]) => s2 + q * GD(k).sell, 0) * GHE.mul / 5) * 5; ld.xp += ex.length * 3; } catch (e) {} return ld; }   /* món mới kèm hàng quen */
function gheSim(){""")
rep("if (ld){ g.o = ld; return; }", "if (ld){ g.o = gheLead(ld); return; }")
rep("val = items.reduce((s2, [k, q]) => s2 + q * GD(k).sell, 0); g.o = { id: 'ghe'", "_m = gheMore(items, 2 + (Math.random() < .5 ? 1 : 0)), val = items.reduce((s2, [k, q]) => s2 + q * GD(k).sell, 0); g.o = { id: 'ghe'")

# tiếng Anh
rep('"Giao bớt": "Deliver some", ', '"Giao bớt": "Deliver some", '
    '"mua về đãi đám giỗ": "for a memorial feast", "đãi đám giỗ": "a memorial feast", "mua về nấu cơm đãi thợ gặt": "to feed the harvest crew", "nấu cơm đãi thợ gặt": "feeding the harvest crew", '
    '"mua về dọn mâm cơm đãi khách": "for a meal with guests", "dọn mâm cơm đãi khách": "a meal with guests", "mua về biếu sui gia": "as a gift for the in-laws", "biếu sui gia": "a gift for the in-laws", '
    '"mua về nấu cơm cho thợ cất nhà": "to feed the house builders", "nấu cơm cho thợ cất nhà": "feeding the house builders", ')
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
