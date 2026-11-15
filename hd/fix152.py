# NHÁP v152: 7 đề xuất công trình (soat-cong-trinh.md) + nới khay lò sấy.
#   python3 fix152.py live/v151.html live/v152.html
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v151'", "BUILD = 'v152'")

# ---- lò sấy: mỗi mẻ ra 2, mật ong thay đường ra gấp đôi nữa, mỗi lò nới thêm 1 khay ----
rep("L.trays.slice(0, 2)", "L.trays.slice(0, sayN1())", 2)
rep("ST.say.trays.slice(2)", "ST.say.trays.slice(sayN1())")
rep("const lsay = {\n  put(i, k){ const L = ST.say, d = SAYR[k];",
    """const SAYUP = 2500, sayN1 = () => 2 + ((ST.say && ST.say.u1) || 0);   /* v152: khay của lò thứ nhất đứng trước, khay lò thứ hai đứng sau */
const sayR = () => { if (!ST.say.mat) return SAYR; const R = {}; for (const k in SAYR){ const d = SAYR[k]; if (d.in.duong){ const inn = { ...d.in }; delete inn.duong; inn.matong = 1; R[k] = { ...d, in: inn }; } else R[k] = d; } return R; };
function sayUp(n){ const L = ST.say; if (!L.own) return; if (n === 1 ? L.u1 : (L.u2 || !(ST.say2 && ST.say2.own))) return; if (ST.xu < SAYUP) return toast(L135(`Thêm khay ${vnX(SAYUP)} xu, con còn thiếu ${vnX(SAYUP - ST.xu)} xu.`, `The extra tray costs ${SAYUP} coins. You are ${SAYUP - ST.xu} short.`), 'dan', { now: true });
  ST.xu -= SAYUP; if (n === 1){ L.trays.splice(sayN1(), 0, null); L.u1 = 1; } else { L.trays.push(null); L.u2 = 1; } coinPop(L135(`-${vnX(SAYUP)} xu · thêm khay lò sấy`, `-${SAYUP} coins · extra oven tray`), '#F08A6E'); sfx('up'); save(); hud(); renderSheet(); bark(L135('Thêm một khay rồi đó con, lò đỏ lửa một lần sấy được nhiều hơn.', 'One more tray, dear. The oven dries more in one go.')); }
const lsay = {
  put(i, k){ const L = ST.say, d = sayR()[k], mm = !!d && d !== SAYR[k];""")
rep("T: fast ? 40 : ttTime(k, d.t), fast }; sfx('pick'); buzz(10); gainXP(1); save(); hud(); },\n  take(i){ const L = ST.say",
    "T: fast ? 40 : ttTime(k, d.t), fast }; if (mm) L.trays[i].m = 1; sfx('pick'); buzz(10); gainXP(1); save(); hud(); },\n  take(i){ const L = ST.say")
rep("STORE(t.k)[t.k] = (STORE(t.k)[t.k] || 0) + 1; L.trays[i] = null; L.done",
    "const nn = (SAY[t.k] ? 2 : 1) * (t.m ? 2 : 1); STORE(t.k)[t.k] = (STORE(t.k)[t.k] || 0) + nn; L.trays[i] = null; L.done")
rep("floatAt(P.cx, .7, P.cz, `+1 ${d.unit} ${d.name.toLowerCase()}`); }\n    sfx('pop'); gainXP(ttXP(t.k, d.sell / 10)); ttAdd(t.k, SAY[t.k]",
    "floatAt(P.cx, .7, P.cz, `+${nn} ${d.unit} ${d.name.toLowerCase()}`); }\n    sfx('pop'); gainXP(ttXP(t.k, d.sell / 10)); ttAdd(t.k, SAY[t.k]")
rep("return UX.pick('sput', SHEET.pick, SAYR, 'Khay');", "return UX.pick('sput', SHEET.pick, sayR(), 'Khay');")
rep("  return h + ttRow('say') + upxHTML('say') + UX.more('Cách sấy',",
    """  h += `<div class="note">${L135('Mỗi mẻ mứt, trái cây sấy ra 2 phần.', 'Each batch of jam or dried fruit makes 2.')}</div>`;
  if ((ST.ong && ST.ong.own) || has('matong') || L.mat) h += `<div class="vcard"><img src="${ICON.matong}" alt=""><div><b>${L135('Sấy mứt bằng mật ong', 'Honey instead of sugar')}</b><span>${L135(`Thay đường bằng 1 hũ mật, mứt ra gấp đôi · kho còn ${has('matong')} hũ`, `1 jar replaces the sugar, jam doubles · ${has('matong')} in storage`)}</span></div><button class="btn${L.mat ? ' g' : ''}" data-a="saymat">${L.mat ? L135('Đang bật', 'On') : L135('Bật', 'Turn on')}</button></div>`;
  return h + ttRow('say') + upxHTML('say') + UX.more('Cách sấy',""")
rep(" return c ? UX.title('Mở rộng') + '<div class=\"upg\">' + c + '</div>' : ''; };",
    " if (k === 'say'){ const L = ST.say; if (!L.u1) c += UX.upc('sayup', ICON.say, L135('Thêm một khay cho lò sấy', 'One more tray for the oven'), vnX(SAYUP), { k: 1, dis: ST.xu < SAYUP }); else if (ST.say2 && ST.say2.own && !L.u2) c += UX.upc('sayup', ICON.say, L135('Thêm một khay cho lò thứ hai', 'One more tray for the second oven'), vnX(SAYUP), { k: 2, dis: ST.xu < SAYUP }); }\n  return c ? UX.title('Mở rộng') + '<div class=\"upg\">' + c + '</div>' : ''; };")
rep("else if (a === 'upx'){ upxBuy(b.dataset.k); return; }",
    "else if (a === 'sayup'){ sayUp(+b.dataset.k); return; } else if (a === 'saymat'){ ST.say.mat = ST.say.mat ? 0 : 1; sfx('pop'); save(); renderSheet(); return; } else if (a === 'bepkem'){ ST.bep.kem = ST.bep.kem ? 0 : 1; sfx('pop'); save(); renderSheet(); return; } else if (a === 'upx'){ upxBuy(b.dataset.k); return; }")

# ---- thùng ong thứ hai: mật ra nhanh gấp rưỡi ----
rep("const ongH = () => Math.max(ONG.hMin, ONG.h0 - ongBloom() * .4);",
    "const ongH = () => Math.max(ONG.hMin, ONG.h0 - ongBloom() * .4) / (((ST.ong || {}).n || 1) > 1 ? 1.5 : 1);")
rep("UX.btn('ongup', 'Thêm thùng thứ hai', { img: UIC.coin, dis: ST.xu < ONG.up, sub: `${ONG.up} xu` })",
    "UX.btn('ongup', 'Thêm thùng thứ hai', { img: UIC.coin, dis: ST.xu < ONG.up, sub: L135(`${ONG.up} xu · mật ra nhanh gấp rưỡi`, `${ONG.up} coins · honey 1.5× faster`) })")
rep("nhanh nhất sáu tiếng một hũ", "nhanh nhất sáu tiếng một hũ, có thùng thứ hai thì còn bốn tiếng", 2)

# ---- ao: cứ 2 con nuôi lớn thì cá đẻ thêm 1 con, mỗi ngày vớt thêm 2 bó lục bình ----
rep("for (const f of ok) ST.inv[f.k] = (ST.inv[f.k] || 0) + 1; try { gainXP(ok.length * 2); } catch (e) {}",
    "for (const f of ok) ST.inv[f.k] = (ST.inv[f.k] || 0) + 1; const de = Math.floor(ok.length / 2); for (let i = 0; i < de; i++){ const k = ok[i * 2].k; ST.inv[k] = (ST.inv[k] || 0) + 1; } let lb = 0; try { if (B.lbd !== dayKey() && (ST.lv || 1) >= oddDefs().lucbinh.lv){ B.lbd = dayKey(); ST.gb = ST.gb || {}; ST.gb.lucbinh = (ST.gb.lucbinh || 0) + 2; lb = 2; } } catch (e) {} try { gainXP(ok.length * 2); } catch (e) {}")
rep("toast(`Kéo lưới được ${ok.length} con cá${bun ? ', thêm 1 phần bùn ao vô hố ủ' : ''}`, 'vui', { now: true });",
    "toast(L135(`Kéo lưới được ${ok.length} con cá${de ? `, cá đẻ thêm ${de} con` : ''}${lb ? ', vớt 2 bó lục bình' : ''}${bun ? ', thêm 1 phần bùn ao vô hố ủ' : ''}`, `Netted ${ok.length} fish${de ? `, plus ${de} young ones` : ''}${lb ? ', 2 bundles of water hyacinth' : ''}${bun ? ', 1 share of pond mud for the compost pit' : ''}`), 'vui', { now: true });")
rep("Một ngày là lớn, kéo lưới về kho.", "Một ngày là lớn, kéo lưới về kho. Cứ hai con nuôi lớn thì cá đẻ thêm một con.", 2)

# ---- khạp nuôi cá: khách ghé coi cá kỷ lục, mỗi ngày để lại 5 tới 20 xu ----
rep("KCAV.root.visible = on; KCAV.hit.visible = on; if (!on) return;",
    "KCAV.root.visible = on; KCAV.hit.visible = on; if (KCAV.b) KCAV.b.visible = false; if (!on) return; kcaSim(); if (ST.kcaXu > 0 && KCAV.b) objBub(KCAV, { cx: KCA.at[0], cz: KCA.at[1] }, UIC.coin, t, .78);")
rep("function cauTick(t, dt){ const on = cauOn() && !VISIT;",
    """try { Object.assign(KCAV, mkBub()); } catch (e) {}
function kcaAmt(){ let m = -1; for (const [k, L] of Object.entries(ST.fishLog || {})) if (L.n && FISHK[k] && FISHK[k].tier < 4) m = Math.max(m, FISHK[k].tier); return m < 0 ? 0 : 5 + 5 * m; }   /* v152: cá thường 5 xu, hiếm 10, quý 15, rất hiếm 20 mỗi ngày; dồn tối đa 3 ngày */
function kcaSim(){ if (!ST.kca) return; const D = 86400e3 / (ST.spd || 1), now = Date.now(); if (!ST.kcaT){ ST.kcaT = now; return; } const n = Math.floor((now - ST.kcaT) / D); if (n < 1) return; ST.kcaT += n * D; const a = kcaAmt(); if (a) ST.kcaXu = Math.min(3 * a, (ST.kcaXu || 0) + n * a); }
function kcaTake(){ const x = ST.kcaXu || 0; if (!x) return false; ST.kcaXu = 0; ST.xu += x; try { coinPop(L135(`+${x} xu · khách coi cá`, `+${x} coins · fish visitors`)); sfx('coin'); buzz(10); } catch (e) {} save(); hud(); sayOnce('kca1', L135('Bà con ghé coi cá kỷ lục của con, để lại ít xu uống nước đó. Cá càng quý thì khách càng đông.', 'Neighbors stopped by to see your record fish and left a few coins. The rarer the fish, the more visitors.'), 'vui'); return true; }
function cauTick(t, dt){ const on = cauOn() && !VISIT;""")
rep("if (kcaHit(OX, OY) || kbenHit(OX, OY)){ sfx('pick'); openBook('ca'); return; }",
    "if ((kcaHit(OX, OY) || bubHit(KCAV, OX, OY)) && kcaTake()) return;\n  if (kcaHit(OX, OY) || kbenHit(OX, OY)){ sfx('pick'); openBook('ca'); return; }")

# ---- bếp: nấu kèm đồ khô, đồ muối thì món ra gấp đôi phần ----
rep("function bepSim(dt){ if (!ST.bep)",
    """const KEM = { goidudu: 'khocasac', goibuoi: 'khocasac', cakho: 'dacai', khoquatrung: 'hotvit', calinhkho: 'otkho', nuongtrui: 'otkho', banhchuoi: 'chuoiphoi', chebap: 'comdua', chesaurieng: 'comdua', rmluoc: 'khocadong', caixao: 'khocadong' };   /* v152: món bếp → đồ khô, đồ muối nấu kèm */
const kemOk = k => !!(ST.bep && ST.bep.kem && KEM[k] && has(KEM[k]) >= 1);
const kemUse = k => { if (!kemOk(k)) return 0; const j = KEM[k]; if (j === 'khocadong' && !(STORE(j)[j] > 0)) return 0; STORE(j)[j] -= 1; return 1; };
function bepSim(dt){ if (!ST.bep)""")
rep("if (p) bepBank(p.k); const k = B.q.shift(), T2 = ttTime(k, DISH[k].t); B.pots[i] = { k, t: T2, T: T2 }; }",
    "if (p) bepBank(p.k, p.x2); const k = B.q.shift(), m = (B.qm || []).shift(), T2 = ttTime(k, DISH[k].t); B.pots[i] = { k, t: T2, T: T2 }; if (m) B.pots[i].x2 = 1; }")
rep("function bepBank(k){ const B = ST.bep, d = DISH[k]; ST.gb[k] = (ST.gb[k] || 0) + 1;",
    "function bepBank(k, x2){ const B = ST.bep, d = DISH[k]; ST.gb[k] = (ST.gb[k] || 0) + (x2 ? 2 : 1);")
rep("B.q.push(k); sfx('pop'); buzz(10); save(); hud(); }",
    "B.q.push(k); B.qm = B.qm || []; while (B.qm.length < B.q.length - 1) B.qm.push(0); B.qm.push(kemUse(k)); sfx('pop'); buzz(10); save(); hud(); }")
rep("B.q.splice(i, 1); for (const [j, q] of Object.entries(DISH[k].in))",
    "B.q.splice(i, 1); { const m = (B.qm || []).splice(i, 1)[0], j = KEM[k]; if (m && j) STORE(j)[j] = (STORE(j)[j] || 0) + 1; } for (const [j, q] of Object.entries(DISH[k].in))")
rep("B.pots[i] = { k, t: ttTime(k, d.t), T: ttTime(k, d.t) }; sfx('pop'); buzz(10); for (let n = 0; n < 6; n++) puff('spark', BEPW.x",
    "B.pots[i] = { k, t: ttTime(k, d.t), T: ttTime(k, d.t) }; if (kemUse(k)) B.pots[i].x2 = 1; sfx('pop'); buzz(10); for (let n = 0; n < 6; n++) puff('spark', BEPW.x")
rep("const d = DISH[p.k]; B.pots[i] = null; bepBank(p.k); flyTo(ICON[p.k], BEPW.x, .6, BEPW.z); floatAt(BEPW.x, .9, BEPW.z, `+1 ${d.name.toLowerCase()}`",
    "const d = DISH[p.k]; B.pots[i] = null; bepBank(p.k, p.x2); flyTo(ICON[p.k], BEPW.x, .6, BEPW.z); floatAt(BEPW.x, .9, BEPW.z, `+${p.x2 ? 2 : 1} ${d.name.toLowerCase()}`")
rep("""filter(([, d]) => !d.nuoc).map(([k, d]) => [k, { ...d, name: d.name + (k === tu ? `<em class="leadt mam">${L135('Món tủ', 'Signature')}</em>` : ''),""",
    """filter(([, d]) => !d.nuoc).map(([k, d]) => [k, { ...d, name: d.name + (k === tu ? `<em class="leadt mam">${L135('Món tủ', 'Signature')}</em>` : '') + (kemOk(k) ? `<em class="leadt kem">${L135('Kèm ' + GD(KEM[k]).name.toLowerCase() + ' · ra 2', 'With ' + GD(KEM[k]).name.toLowerCase() + ' · makes 2')}</em>` : ''),""")
rep("  if (lv >= QN.lv) h += qnOn()",
    """  if (B.kem || Object.values(KEM).some(j => has(j) >= 1)) h += `<div class="vcard"><img src="${ICON.khocasac}" alt=""><div><b>${L135('Nấu kèm đồ khô, đồ muối', 'Cook with dried or pickled sides')}</b><span>${L135('Món hợp vị ra 2 phần, tốn 1 món kèm trên gác bếp', 'Matching dishes make 2 and use 1 side from the loft')}</span></div><button class="btn${B.kem ? ' g' : ''}" data-a="bepkem">${B.kem ? L135('Đang bật', 'On') : L135('Bật', 'Turn on')}</button></div>`;
  if (lv >= QN.lv) h += qnOn()""")
rep(".leadt.moi{background:#C24A2E}", ".leadt.moi{background:#C24A2E}.leadt.kem{background:#557A2A}")

# ---- nút Quay lại ở màn chọn món: nới cho đủ 44px (lỗi cũ, màn chọn món trước giờ chưa có trong uicheck) ----
rep("cursor:pointer;padding:2px 0 8px;font-size:13px}", "cursor:pointer;padding:0 12px 0 0;min-height:44px;min-width:44px;font-size:13px}")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
