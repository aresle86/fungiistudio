#!/usr/bin/env python3
"""v104: đơn hàng — phân vai hàng xóm (đồ tươi, món nấu) và ghe (trái cây, đồ khô, mứt, giỏ, mật);
đơn dẫn đường cho món mới; ghe chờ 6 tiếng từ lúc thấy, giao từng món, hết giờ trả tiền phần đã giao."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---------- phân vai ----------
rep("function ordMake(){", "const GHEK = k => (CROPS[k] && CROPS[k].tree) || PHOI[k] || MUOI[k] || SAY[k] || k === 'gio' || k === 'matong';   /* hàng của ghe chợ nổi */\nfunction ordMake(kind){")
rep("} catch (e) {} const known = pool.filter(",
    "} catch (e) {} { const pk = kind === 'ghe' ? pool.filter(GHEK) : pool.filter(k => !(SAY[k] || k === 'gio' || k === 'matong')); if (pk.length >= (kind === 'ghe' ? 2 : 1)) pool.splice(0, pool.length, ...pk); }   /* hàng xóm: đồ tươi, món nấu; ghe: trái cây, đồ khô, mứt, giỏ */ const known = pool.filter(")
rep("const a = ordMake(), b = ordMake()", "const a = ordMake('ghe'), b = ordMake('ghe')")

# ---------- đơn dẫn đường ----------
rep("ST.ord.acc = 0; try { ST.ord.list.push(ordMake()); } catch (e) {} }",
    "ST.ord.acc = 0; try { ST.ord.list.push(leadMake('nb') || ordMake()); } catch (e) {} }\n"
    "var LEAD = [{ k: 'trungchien', q: 1, lv: 4, by: 'nb', ok: () => (ST.bep && Object.keys(ST.bep.made || {}).length > 0) || has('trungchien') > 0 }, { k: 'trungga', q: 3, lv: 5, by: 'nb', ok: () => gaOn() }, { k: 'otkho', q: 1, lv: 7, by: 'nb', ok: () => ST.nong && ST.nong.own },\n"
    "  { k: 'dacai', q: 1, lv: 8, by: 'nb', ok: () => ST.khap && ST.khap.own }, { k: 'caro', q: 1, lv: 9, by: 'nb', ok: () => Object.keys(ST.fishLog || {}).some(f => FISHK[f]) }, { k: 'oi', q: 5, lv: 10, by: 'ghe', ok: () => PLOTS.some(P => ST.plots[P.id] && ST.plots[P.id].crop === 'oi') },\n"
    "  { k: 'xoaisay', q: 1, lv: 11, by: 'ghe', ok: () => ST.say && ST.say.own && PLOTS.some(P => ST.plots[P.id] && ST.plots[P.id].crop === 'xoai') }, { k: 'comdua', q: 1, lv: 12, by: 'ghe', ok: () => ST.say && ST.say.own && PLOTS.some(P => ST.plots[P.id] && ST.plots[P.id].crop === 'dua') },\n"
    "  { k: 'gio', q: 2, lv: 15, by: 'ghe', ok: () => gioOn() }, { k: 'matong', q: 1, lv: 17, by: 'ghe', ok: () => ST.ong && ST.ong.own }];   /* mở thứ mới thì có người đặt đúng món đó một lần */\n"
    "function leadMake(by){ const lv = ST.lv || 1, done = ST.leadDone = ST.leadDone || {}; const L = LEAD.find(x => x.by === by && lv >= x.lv && !done[x.k] && GD(x.k) && (() => { try { return x.ok(); } catch (e) { return false; } })()); if (!L) return null;\n"
    "  if (by === 'nb' && ((ST.ord && ST.ord.list) || []).some(o => o.lead)) return null; const val = L.q * GD(L.k).sell, who = by === 'ghe' ? pick(['Ghe bẹo cô Sáu', 'Ghe bẹo chú Mười', 'Ghe bẹo dì Bảy']) : pick(NB);\n"
    "  return { id: (by === 'ghe' ? 'ghe' : '') + Date.now() + '' + Math.floor(Math.random() * 1e4), who, why: by === 'ghe' ? 'nghe nói vườn mình mới có, đem ra chợ nổi bán thử' : 'nếm thử món mới nhà mình', items: [[L.k, L.q]], xu: Math.round(val * (by === 'ghe' ? GHE.mul : ORD.mul) * 1.5 / 5) * 5, xp: 8, lead: L.k, ghe: by === 'ghe' ? 1 : 0 }; }")
rep("if (!o || !ordCan(o)) return; for (const [k, q] of o.items) STORE(k)[k] -= q; ST.xu += o.xu; ST.ord.list.splice(i, 1);",
    "if (!o || !ordCan(o)) return; for (const [k, q] of o.items) STORE(k)[k] -= q; ST.xu += o.xu; ST.ord.list.splice(i, 1); if (o.lead){ (ST.leadDone = ST.leadDone || {})[o.lead] = 1; setTimeout(() => say(`${o.who} khen món ${GD(o.lead).name.toLowerCase()} nhà mình ngon lắm, mai mốt còn đặt nữa đó con.`, 'vui', { idle: true }), 800); }")
rep("return `<div class=\"ordr${ok ? ' ok' : ''}\"><div class=\"ow\"><b>${o.who}</b><span>mua về ${o.why}</span></div>",
    "return `<div class=\"ordr${ok ? ' ok' : ''}\"><div class=\"ow\"><b>${o.who}${o.lead ? '<em class=\"leadt\">Món mới</em>' : ''}</b><span>mua về ${o.why}</span></div>")

# ---------- ghe: chờ 6 tiếng từ lúc thấy, giao từng món ----------
rep("function gheSim(){ const g = ST.ghe; if (!gheOn() || VISIT) return; const dk = dayKey(); if (g.d === dk) return; g.d = dk; try { const a = ordMake('ghe')",
    "const GHEH = 6;   /* giờ ghe chờ, tính từ lúc con thấy ghe */\n"
    "const gheGot = (o, k) => ((o && o.got) || {})[k] || 0;\n"
    "function gheLeft(){ const o = ST.ghe.o; if (!o || !o.seen) return GHEH * 3600e3; return Math.max(0, o.seen + GHEH * 3600e3 / (ST.spd || 1) - Date.now()); }\n"
    "function gheLeave(){ const g = ST.ghe, o = g.o; if (!o) return; const part = o.items.reduce((s2, [k]) => s2 + gheGot(o, k) * GD(k).sell, 0), pay = Math.round(part * ORD.mul / 5) * 5; g.o = null; if (pay > 0){ ST.xu += pay; coinPop(`+${pay} xu · phần đã giao ghe`, '#9fd36a'); } if (!VISIT) say('Ghe bẹo nhổ sào đi rồi con, mai sáng ghé nữa.', 'dan', { idle: true }); save(); hud(); }\n"
    "function gheSim(){ const g = ST.ghe; if (!gheOn() || VISIT) return; if (g.o && g.o.seen && gheLeft() <= 0) gheLeave(); const dk = dayKey(); if (g.d === dk) return; if (g.o) gheLeave(); g.d = dk; const ld = leadMake('ghe'); if (ld){ g.o = ld; return; } try { const a = ordMake('ghe')")
rep("function gheGive(el){ const g = ST.ghe, o = g.o; if (!o || !ordCan(o)) return; for (const [k, q] of o.items) STORE(k)[k] -= q; ST.xu += o.xu; g.o = null; bump('ghe'); g.done = (g.done || 0) + 1; if (el) coinFly(el, 7); sfx('coin'); coinPop(`+${o.xu} xu · ${o.who}`, '#9fd36a'); gainXP(o.xp);\n  toast('Ghe bẹo nhổ sào đi rồi, mai lại ghé.'); save(); hud(); }",
    "function gheGive(el){ const g = ST.ghe, o = g.o; if (!o) return; o.got = o.got || {}; let n = 0; for (const [k, q] of o.items){ const d = Math.min(Math.max(0, q - gheGot(o, k)), has(k)); if (d > 0){ STORE(k)[k] -= d; o.got[k] = gheGot(o, k) + d; n += d; } } if (!n) return;\n"
    "  if (o.items.every(([k, q]) => gheGot(o, k) >= q)){ ST.xu += o.xu; g.o = null; bump('ghe'); g.done = (g.done || 0) + 1; if (o.lead) (ST.leadDone = ST.leadDone || {})[o.lead] = 1; if (el) coinFly(el, 7); sfx('coin'); coinPop(`+${o.xu} xu · ${o.who}`, '#9fd36a'); gainXP(o.xp); toast('Ghe bẹo nhận đủ hàng, nhổ sào đi rồi. Mai lại ghé.'); }\n"
    "  else { sfx('pop'); toast('Ghe nhận rồi, gom thêm cho đủ đơn nghe con'); } save(); hud(); renderSheet(); }")
rep("const ok = ordCan(o); return h + `<div class=\"ordr ghe${ok ? ' ok' : ''}\"><div class=\"ow\"><b>${o.who}</b><span>${o.why}</span></div><div class=\"oi\">${o.items.map(([k, q]) => { const have = has(k); return `<span class=\"oit${have >= q ? ' got' : ''}\"><img src=\"${ICON[k]}\" alt=\"\"><i>${Math.min(have, q)}/${q}</i></span>`; }).join('')}</div><div class=\"oa\"><button class=\"btn g\" data-a=\"ghegive\" ${ok ? '' : 'disabled'}>Giao · ${o.xu} xu</button></div></div>`; }",
    "const full = o.items.every(([k, q]) => gheGot(o, k) + has(k) >= q), some = o.items.some(([k, q]) => gheGot(o, k) < q && has(k) > 0), lf = gheLeft(), hh = Math.max(1, Math.ceil(lf / 3600e3));\n"
    "  return h + `<div class=\"ordr ghe${full ? ' ok' : ''}\"><div class=\"ow\"><b>${o.who}${o.lead ? '<em class=\"leadt\">Món mới</em>' : ''}</b><span>${o.why} · ghe chờ ${o.seen ? 'thêm ' + hh + ' tiếng' : GHEH + ' tiếng'}</span></div><div class=\"oi\">${o.items.map(([k, q]) => { const have = Math.min(q, gheGot(o, k) + has(k)); return `<span class=\"oit${have >= q ? ' got' : ''}\"><img src=\"${ICON[k]}\" alt=\"\"><i>${have}/${q}</i></span>`; }).join('')}</div><div class=\"oa\"><button class=\"btn g\" data-a=\"ghegive\" ${some ? '' : 'disabled'}>${full ? `Giao đủ · ${o.xu} xu` : 'Giao bớt'}</button></div></div>`; }")
# ghe: đánh dấu lúc thấy, bong bóng có thanh giờ, còn dưới 1 tiếng thì đỏ
rep("function gheTick(t){ const on = gheOn() && !!ST.ghe.o && !VISIT; GHEV.root.visible = on; GHEV.b.visible = false; if (!on) return;",
    "function gheTick(t){ const on = gheOn() && !!ST.ghe.o && !VISIT; GHEV.root.visible = on; GHEV.b.visible = false; if (!on) return; if (!ST.ghe.o.seen){ ST.ghe.o.seen = Date.now(); save(); } { const lf = gheLeft(), br = GHEV.b.userData.bar; try { bubCol(GHEV.b, lf < 3600e3 ? BUBC.gap : BUBC.lay); } catch (e) {} if (br){ br.visible = true; try { bubBar(br, 1 - lf / (GHEH * 3600e3), lf); } catch (e) {} } }")
rep("`Đơn lớn ${ST.ghe.o.xu} xu, ghe đi lúc hết ngày`", "`Đơn lớn ${ST.ghe.o.xu} xu, ghe chờ thêm ${Math.max(1, Math.ceil(gheLeft() / 3600e3))} tiếng`")
i = s.rindex('</style>'); s = s[:i] + "\n.leadt{display:inline-block;margin-left:6px;padding:1px 7px;border-radius:999px;background:#F2A23A;color:#fff;font:400 11px/1.5 var(--f-game);font-style:normal;vertical-align:2px}\n" + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
