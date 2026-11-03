p='live/vuon3d.html';s=open(p,encoding='utf8').read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:100]); s=s.replace(a,b)
# 1. dữ liệu
rep("const GD = k => CROPS[k] || EXTRA[k] || DISH[k] || PHOI[k];",
"""// khạp muối (cấp 8): muối dưa, muối hột vịt — để lâu không hư
const MUOI = {
  dacai: { name: 'Dưa cải muối', unit: 'hũ', lv: 8, in: { cai: 4, muoi: 1 }, t: 12 * 3600, out: 1, sell: 65, story: 'Dưa cải muối chua ăn với thịt kho hột vịt, Tết nào nhà mình cũng có một khạp.' },
  hotvit: { name: 'Hột vịt muối', unit: 'hột', lv: 8, in: { trungvit: 4, muoi: 1 }, t: 24 * 3600, out: 4, sell: 42, story: 'Hột vịt ngâm nước muối đủ ngày là lòng đỏ son. Luộc ăn với cháo trắng là hết sẩy.' } };
const GD = k => CROPS[k] || EXTRA[k] || DISH[k] || PHOI[k] || MUOI[k];""")
rep("const EXTRA = { trungga: { name: 'Trứng gà', sell: 25, unit: 'trứng' }, trungvit: { name: 'Trứng vịt', sell: 30, unit: 'trứng' } };",
"const EXTRA = { trungga: { name: 'Trứng gà', sell: 25, unit: 'trứng' }, trungvit: { name: 'Trứng vịt', sell: 30, unit: 'trứng' }, caro: { name: 'Cá rô', sell: 25, unit: 'con' }, caloc: { name: 'Cá lóc', sell: 45, unit: 'con' }, muoi: { name: 'Muối hột', sell: 2, unit: 'bịch', nosell: true } };")
rep("const STORE = k => (DISH[k] || PHOI[k] || k === 'cui') ? (ST.gb = ST.gb || {}) : ST.inv;","const STORE = k => (DISH[k] || PHOI[k] || MUOI[k] || k === 'cui' || k === 'muoi') ? (ST.gb = ST.gb || {}) : ST.inv;")
s=s.replace("Object.entries(ST.gb || {}).some(([k, n]) => n > 0 && (DISH[k] || PHOI[k]))","Object.entries(ST.gb || {}).some(([k, n]) => n > 0 && (DISH[k] || PHOI[k] || MUOI[k]))")
rep("const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && (DISH[k] || PHOI[k]));","const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && (DISH[k] || PHOI[k] || MUOI[k]));")
rep("  banhchuoi: { name: 'Bánh chuối nướng',","  canhchuaca: { name: 'Canh chua cá lóc', sell: 145, unit: 'tô', lv: 9, in: { caloc: 1, cachua: 2, ot: 1, cui: 1 }, t: 40 * 60, story: 'Cá lóc đồng con câu ở bến, nấu canh chua với cà, ớt. Má Ngoại nói ai ăn canh này một lần là nhớ miệt vườn hoài.' },\n  banhchuoi: { name: 'Bánh chuối nướng',")
# 2. sim
rep("try { nongSim(dt); } catch (e) {}","try { nongSim(dt); khapSim(dt); hoSim(dt); loSim(dt); } catch (e) {}")
rep("try { nongSim(s2, Date.now() - off * 1000); } catch (e) {}","try { nongSim(s2, Date.now() - off * 1000); khapSim(s2); hoSim(s2); loSim(s2); } catch (e) {}")
# 3–5. vùng ô: bãi hông nhà (cấp 7) + mé sông (cấp 9)
rep("const BAIC = {","""// mé sông (cấp 9): 8 ô đất bồi phù sa dọc bờ sông bên phải bến
const SONG = { lv: 9, cost: 60, x0: 6.2, z0: 6.8, cw: .8, cl: .62, gap: .1, cols: 4 };
for (let i = 0; i < 8; i++){ const c = i % SONG.cols, r = Math.floor(i / SONG.cols), u0 = SONG.x0 + c * (SONG.cw + SONG.gap), v0 = SONG.z0 + r * (SONG.cl + SONG.gap); PLOTS.push({ id: 'S' + (i + 1), b: [u0, v0, u0 + SONG.cw, v0 + SONG.cl], name: `Mé sông · ô ${i + 1}`, bai: true, zone: 'song', lv: SONG.lv, cost: SONG.cost }); }
const SONGC = { x: SONG.x0 + 1.75, z: SONG.z0 + .67 };
const BAIC = {""")
rep("const isBed = P => /^[ABCH]/.test(P.id),","const isBed = P => /^[ABCHS]/.test(P.id),")
rep("const baiOn = () => (ST.lv || 1) >= BAI.lv, hidP = P => P.bai && !baiOn(), nOpen = () => ST.open.filter(i => i[0] !== 'H').length;",
"const baiOn = () => (ST.lv || 1) >= BAI.lv, hidP = P => P.bai && (ST.lv || 1) < (P.lv || BAI.lv), nOpen = () => ST.open.filter(i => i[0] !== 'H' && i[0] !== 'S').length;")
rep("  if (P.bai){ const on = baiOn(), lk = locked(P), nh = ST.nong && ST.nong.own && ST.nong.at === id;","  if (P.bai){ const on = !hidP(P), lk = locked(P), nh = (() => { try { return !!objAt(id); } catch (e) { return false; } })();")
rep("if (P.bai && ST.nong && ST.nong.at === id) return say('Ô này đang đặt nong phơi. Dời nong đi rồi mới đắp liếp được con.', 'dan');","if (P.bai && objAt(id)) return say(`Ô này đang đặt ${OBJD[objAt(id)].name}. Dời đi rồi mới đắp liếp được con.`, 'dan');")
rep("const c0 = P.bai ? BAI.cost : bedCost();","const c0 = P.bai ? (P.cost || BAI.cost) : bedCost();")
rep("    if (P.bai && (SUA || locked(P) || (ST.nong.own && ST.nong.at === arg))){","    if (P.bai && (SUA || locked(P) || objAt(arg))){")
# 6. chạm
rep("  if (nongHit(e.clientX, e.clientY)){ nong.takeAll(); openSheet('nong'); return; }",
"""  if (nongHit(e.clientX, e.clientY)){ nong.takeAll(); openSheet('nong'); return; } if (khapHit(e.clientX, e.clientY)){ khap.takeAll(); openSheet('khap'); return; } if (hoHit(e.clientX, e.clientY)){ openSheet('ho'); return; }
  { const lh = loHit(e.clientX, e.clientY); if (lh){ if (ST.lo.on && ST.lo.t <= 0) lo.hatch(); else if (lh === 'bub' && !ST.lo.on) lo.put(); else openSheet('lo'); hud(); return; } }
  if (cauHit(e.clientX, e.clientY)){ cauTap(); return; }""")
rep("""    if (SUA && SUA.move === 'nong'){ if (HP && HP.bai && locked(HP) && ST.nong.at !== hid && nong.place(hid)){ SUA.move = null; suaTx(); for (const P of PLOTS) if (P.bai) refreshPlot(P.id); say('Đặt nong ở đây rồi nè. Chạm nong mà phơi đồ nghe con.', 'vui', { now: true }); } else say('Nong chỉ đặt được trên ô cỏ ở bãi hông nhà con.', 'dan', { now: true }); return; }
    if (HP && HP.bai && ST.nong.own && ST.nong.at === hid){ nong.takeAll(); openSheet(SUA ? 'plot' : 'nong', hid); return; }""",
"""    if (SUA && SUA.move){ const mk = SUA.move; if (HP && HP.bai && locked(HP) && !objAt(hid) && placeObj(mk, hid)){ SUA.move = null; suaTx(); for (const P of PLOTS) if (P.bai) refreshPlot(P.id); say(`Đặt ${OBJD[mk].name} ở đây rồi nè.`, 'vui', { now: true }); } else say('Chỉ đặt được trên ô cỏ trống ở bãi hông nhà hay mé sông con.', 'dan', { now: true }); return; }
    { const ok = HP && HP.bai && objAt(hid); if (ok){ if (ok === 'nong') nong.takeAll(); if (ok === 'khap') khap.takeAll(); openSheet(SUA ? 'plot' : OBJD[ok].sheet, hid); return; } }""")
# 7. sheet + nút
rep("  if (kind === 'nong'){ shT.textContent = 'Nong phơi'; h += nongHTML(); }","  if (kind === 'nong'){ shT.textContent = 'Nong phơi'; h += nongHTML(); }\n  if (kind === 'khap'){ shT.textContent = 'Khạp muối'; h += khapHTML(); }\n  if (kind === 'ho'){ shT.textContent = 'Hố ủ phân'; h += hoHTML(); }\n  if (kind === 'lo'){ shT.textContent = 'Lò ấp vịt'; h += loHTML(); }")
rep("""else if (a === 'nbuy'){ const at = SHEET && SHEET.kind === 'plot' ? SHEET.arg : null; closeSheet(); nong.buy(at); return; } else if (a === 'nhere'){ nong.place(id); }
  else if (a === 'nopen'){ openSheet('nong'); return; } else if (a === 'nmove'){ closeSheet(); suaOn(true, 'nong'); return; }""",
"""else if (a === 'obuy'){ const at = SHEET && SHEET.kind === 'plot' ? SHEET.arg : null; closeSheet(); buyObj(b.dataset.k, at); return; } else if (a === 'ohere'){ placeObj(b.dataset.k, id); }
  else if (a === 'oopen'){ openSheet(OBJD[b.dataset.k].sheet); return; } else if (a === 'omove'){ closeSheet(); suaOn(true, b.dataset.k); return; }
  else if (a === 'kput'){ khap.put(+b.dataset.n, b.dataset.k); } else if (a === 'ktake'){ khap.take(+b.dataset.n); } else if (a === 'hobon'){ hoBon(); } else if (a === 'horau'){ hoRau(); } else if (a === 'bon'){ hoBon(id); }
  else if (a === 'loput'){ lo.put(); } else if (a === 'lohatch'){ lo.hatch(); } else if (a === 'gocho3'){ openSheet('cho'); SHEET.tab = 'mua'; renderSheet(); return; }
  else if (a === 'buymuoi'){ const n = +b.dataset.n; if (ST.xu >= MUOI_PRICE * n && gbUsed() + n <= GB_CAP){ ST.xu -= MUOI_PRICE * n; ST.gb.muoi = (ST.gb.muoi || 0) + n; save(); hud(); buyFx(b, ICON.muoi, `+${n} bịch muối`, MUOI_PRICE * n); } else if (gbUsed() + n > GB_CAP) say('Gác bếp hết chỗ để muối rồi con.', 'dan'); }""")
# 8. chợ mua
rep("""    if (nongOn()) h += `<div class="srow"><div class="sic"><img src="${ICON.nong}" alt=""></div><div class="sn"><b>Bộ nong phơi</b>${stI('coin', NONG.buy + ' xu')}<span class="mkh">4 nong tre, đặt ở bãi hông nhà</span></div><span></span><button class="btn sall" data-a="nbuy" ${ST.nong.own || ST.xu < NONG.buy ? 'disabled' : ''}>${ST.nong.own ? 'Đã có' : 'Mua'}</button></div>`;""",
"""    for (const [k, sub] of [['nong', '4 nong tre, đặt ở bãi hông nhà'], ['khap', 'Muối dưa cải, hột vịt'], ['ho', 'Ủ lá, lục bình thành phân']]) if (objOn(k)){ const D = OBJD[k], O = ST[k]; h += `<div class="srow"><div class="sic"><img src="${ICON[k]}" alt=""></div><div class="sn"><b>${D.title}</b>${stI('coin', D.buy + ' xu')}<span class="mkh">${sub}</span></div><span></span><button class="btn sall" data-a="obuy" data-k="${k}" ${O.own || ST.xu < D.buy ? 'disabled' : ''}>${O.own ? 'Đã có' : 'Mua'}</button></div>`; }
    if (objOn('khap')) h += `<div class="srow"><div class="sic"><img src="${ICON.muoi}" alt=""><span class="sq">${(ST.gb || {}).muoi || 0}</span></div><div class="sn"><b>Muối hột</b>${stI('coin', MUOI_PRICE + ' xu/bịch')}<span class="mkh">Để trên gác bếp</span></div><button class="btn s1" data-a="buymuoi" data-n="1" ${ST.xu < MUOI_PRICE ? 'disabled' : ''} aria-label="Mua 1 bịch muối">+1</button><button class="btn sall" data-a="buymuoi" data-n="4" ${ST.xu < MUOI_PRICE * 4 ? 'disabled' : ''}>+4<small>${MUOI_PRICE * 4} xu</small></button></div>`;""")
# 9. việc vặt đổ vô hố ủ
rep("  else if (o.k === 'lucbinh'){ if (kCap() - kUsed() > 0){","  else if (o.k === 'lucbinh' && hoRoom()){ hoAdd(1); txt = '+1 phần vô hố ủ'; for (let k = 0; k < 6; k++) puff('drop', o.x, .05, o.z, 1, '#9cc6e0', .5); }\n  else if (o.k === 'lucbinh'){ if (kCap() - kUsed() > 0){")
rep("  else { const P = PLOTS.filter(P => !P.tree && !P.trellis && !locked(P) && ST.plots[P.id])","  else if (hoRoom()){ hoAdd(2); txt = '+2 phần lá vô hố ủ'; for (let k = 0; k < 8; k++) puff('leaf', o.x, .1, o.z, 1, pick(['#C9952A', '#E3B23C', '#B48560']), .6); }\n  else { const P = PLOTS.filter(P => !P.tree && !P.trellis && !hidP(P) && !locked(P) && ST.plots[P.id])")
# 10. bón phân trong bảng liếp
rep("""    h += '<div class="acts">';\n    if (c && ripe(p)) h += `<button class="btn g" data-a="harvest">Hái</button>`;""",
"""    h += '<div class="acts">';\n    if (!P.trellis && !P.tree && ST.ho && ST.ho.bags > 0 && p.soil < .95) h += `<button class="btn" data-a="bon">Bón phân · đất +0,3</button>`;\n    if (c && ripe(p)) h += `<button class="btn g" data-a="harvest">Hái</button>`;""")
# 11. tick
rep("try { nongTick(t); } catch (e)","try { nongTick(t); khapTick(t); hoTick(t); loTick(t); cauTick(t, dt); boTick(); } catch (e)")
open(p,'w',encoding='utf8').write(s); print('ok')
