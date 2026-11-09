# -*- coding: utf-8 -*-
# v124a sau v123c: tép dễ hơn, khô cá đồng, (tiếp: bong bóng khó bấm, rau cho gà vịt, chợ hôm nay cần, đơn lớn của xóm)
import re, sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)

rep("BUILD = 'v123c'", "BUILD = 'v124a'")

# ---- tép: câu một lần ra cả nắm, công thức nhẹ hơn ----
rep("if (f.tier < 4) ST.inv[k] = (ST.inv[k] || 0) + 1;", "const nGot = k === 'tep' ? 3 + Math.floor(Math.random() * 3) : 1; if (f.tier < 4) ST.inv[k] = (ST.inv[k] || 0) + nGot;")
rep('<b>${f.name}</b><span class="fw">', '<b>${f.name}${nGot > 1 ? ` · ${nGot} con` : \'\'}</b><span class="fw">')
rep('tepphoi: { name: \'Tép phơi\', unit: \'bịch\', lv: 10, in: {"tep": 6, "muoi": 1}', 'tepphoi: { name: \'Tép phơi\', unit: \'bịch\', lv: 10, in: {"tep": 4, "muoi": 1}')
rep('mamtep: { name: \'Mắm tép\', unit: \'hũ\', lv: 12, in: {"tep": 8, "muoi": 2}', 'mamtep: { name: \'Mắm tép\', unit: \'hũ\', lv: 12, in: {"tep": 6, "muoi": 2}')

# ---- đơn hàng: món làm từ cá/tép chỉ đặt khi con đã câu được loài đó (cá tươi thì vẫn đặt theo mùa) ----
rep("if (FISHK[k]){ const f = FISHK[k]; return cauOn() &&", "if (k === 'canho') return cauOn() && CANHO().some(x => ST.fishLog[x] && ST.fishLog[x].n); if (FISHK[k] && d > 0) return cauOn() && !!(ST.fishLog[k] && ST.fishLog[k].n); if (FISHK[k]){ const f = FISHK[k]; return cauOn() &&")

# ---- khô cá đồng: 3 con cá nhỏ bất kỳ + 1 muối ----
rep("  lucbinhkho: { name: 'Lục bình khô'", "  khocadong: { name: 'Khô cá đồng', unit: 'xâu', lv: 9, in: { canho: 3, muoi: 1 }, t: 6 * 3600, sell: 75, story: 'Cá rô, cá sặc, cá diếc câu được con nào bỏ chung con đó, ướp muối phơi một nắng. Nhà quê gọi là khô cá đồng, chiên giòn ăn cơm nóng.' },\n  lucbinhkho: { name: 'Lục bình khô'")
rep("const has = k => (STORE(k)[k] || 0);", """const CANHO = () => Object.keys(FISHK).filter(x => FISHK[x].tier === 0 && FISHK[x].sz === 's' && x !== 'tep');   /* cá nhỏ làm khô cá đồng */
const canhoN = () => CANHO().reduce((a, x) => a + (ST.inv[x] || 0), 0);
function canhoTake(n){ while (n > 0){ const x = CANHO().filter(y => (ST.inv[y] || 0) > 0).sort((a, b) => ST.inv[b] - ST.inv[a])[0]; if (!x) break; ST.inv[x]--; n--; } }   /* lấy loài đang dư nhiều nhất */
const has = k => k === 'canho' ? canhoN() : (STORE(k)[k] || 0);""")
rep("setTimeout(() => bump('nong'), 0); for (const [ik, n] of Object.entries(d.in)) STORE(ik)[ik] -= n;", "setTimeout(() => bump('nong'), 0); for (const [ik, n] of Object.entries(d.in)) if (ik === 'canho') canhoTake(n); else STORE(ik)[ik] -= n;")
rep("const phoiName = k => k === 'lucbinh' ? 'lục bình'", "const phoiName = k => k === 'canho' ? 'cá nhỏ' : k === 'lucbinh' ? 'lục bình'")
rep("['say2', 'say']]) Object.defineProperty(ICON, a, { get: () => ICON[b], configurable: true });", "['say2', 'say'], ['khocadong', 'khocasac'], ['canho', 'caro']]) Object.defineProperty(ICON, a, { get: () => ICON[b], configurable: true });")
rep('"khocasac": "Dried gourami", ', '"khocasac": "Dried gourami", "khocadong": "Dried mixed fish", ')

# ---- bong bóng: chạm trúng bóng của liếp thì liếp luôn được ưu tiên hơn đồ vật kế bên (ghế Ngoại đan giỏ, nong, khạp...) ----
rep("function plotHit0(cx, cy){ ndc.set(", "function plotHit0(cx, cy){ PBH = false; ndc.set(")
rep("const hb = ray.intersectObjects(bubs, false)[0]; if (hb) return hb.object.userData.plot;", "const hb = ray.intersectObjects(bubs, false)[0]; if (hb){ PBH = true; return hb.object.userData.plot; } { const th = treeHitAt(cx, cy); if (th) return th; } ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam);")
rep("function plotHit(cx, cy){", """let PBH = false; const TREEH = {};
function treeHitAt(cx, cy){ const ms = []; for (const [h, gst] of Object.entries(ST.pairs || {})){ const p = ST.plots[h], c = p && p.crop && CROPS[p.crop], P = PL[h]; if (!c || !c.tree || !P || hidP(P)) continue; const u = unionB(h), w = u[2] - u[0], l = u[3] - u[1], hh = Math.max(1, (c.h || 1.5) * 1.05); let m = TREEH[h]; if (!m){ m = TREEH[h] = new T.Mesh(new T.BoxGeometry(1, 1, 1), new T.MeshBasicMaterial({ visible: false })); m.userData.plot = h; } m.scale.set(w * .8, hh, l * .8); m.position.set((u[0] + u[2]) / 2, hh / 2, (u[1] + u[3]) / 2); m.updateMatrixWorld(true); ms.push(m); }
  if (!ms.length) return null; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); const h = ray.intersectObjects(ms, false)[0]; return h ? h.object.userData.plot : null; }   /* cây trái trên đất trống (2 ô, cao): chạm tán, thân cũng trúng cây */
const treeG = (cx, cy) => { const h = treeHitAt(cx, cy); if (!h) return null; const [u0, v0, u1, v1] = PL[h].b; return { x: (u0 + u1) / 2, z: (v0 + v1) / 2 }; };
const toolG = (cx, cy) => (TOOL && (TOOL.kind === 'water' || TOOL.kind === 'cut' || TOOL.kind === 'rom') && treeG(cx, cy)) || groundAt(cx, cy);
function plotHit(cx, cy){""")
rep("G0 = { x: e.clientX, y: e.clientY, pid: e.pointerId, id, need, gk, wg, moved: false, held: false };", "G0 = { x: e.clientX, y: e.clientY, pid: e.pointerId, id, need, gk, wg, bub: !!id && PBH, moved: false, held: false };")
a = s.find("{ const od = oddHit(e.clientX, e.clientY);"); b = s.find("  { const hid = g.id || plotHit(e.clientX, e.clientY), HP = hid && PL[hid];")
assert 0 < a < b
s = s[:a] + "const OX = g.bub ? -1e5 : e.clientX, OY = g.bub ? -1e5 : e.clientY;   /* chạm trúng bóng liếp: bỏ qua đồ vật */\n  " + s[a:b].replace("(e.clientX, e.clientY)", "(OX, OY)") + s[b:]
rep("function strokeAt(cx, cy, dt){ const g = groundAt(cx, cy);", "function strokeAt(cx, cy, dt){ const g = toolG(cx, cy);")
rep("const g = TOOL.temp || TOOL.temp2 ? null : groundAt(e.clientX, aimY(e, e.clientY));", "const g = TOOL.temp || TOOL.temp2 ? null : toolG(e.clientX, aimY(e, e.clientY));")

# ---- A. rau cho gà vịt ăn: hết bắp (gà) / rau muống (vịt) thì lấy cải, mồng tơi, rau muống; mỗi bó 2 phần; hết rau mới mua cám ----
RAU_GA = "{ for (const rk of ['cai', 'mongtoi', 'raumuong', 'muop', 'bau']){ if (got >= need) break; const q = Math.min(ST.inv[rk] || 0, Math.ceil((need - got) / 2)); if (q){ ST.inv[rk] -= q; got += Math.min(need - got, q * 2); parts.push(`-${q} bó ${CROPS[rk].name.toLowerCase()}`); RAUAN = 1; } } }"
rep("parts.push(`-${bap} trái bắp`); }", "parts.push(`-${bap} trái bắp`); } RAUAN = 0; " + RAU_GA)
rep("parts.push(`${rm} bó rau muống`); }", "parts.push(`${rm} bó rau muống`); } RAUAN = 0; " + RAU_GA.replace("'cai', 'mongtoi', 'raumuong', 'muop', 'bau'", "'cai', 'mongtoi', 'muop', 'bau'"))
rep("const GA = {", "let RAUAN = 0; setInterval(() => { if (RAUAN){ RAUAN = 0; try { sayOnce('rauan', 'Rau dư đừng bỏ, Ngoại băm ra cho gà vịt ăn. Tụi nó ăn rau là đỡ tốn tiền cám đó con.', 'vui'); } catch (e) {} } }, 1500);\nconst GA = {")

# ---- C. chợ hôm nay cần: mỗi ngày 3 món rau, bán trong số lượng đó được giá gấp đôi; đủ cả 3 thì thêm kinh nghiệm ----
rep("const sellValue = (k, n) => { let s = 0; const i0 = mkDay().s[k] || 0; for (let j = 0; j < n; j++) s += priceAt(k, i0 + j); return s; };",
    """const MKC = { lv: 3, n: 3, xp: 12 };
function mkcDay(){ const d = dayKey(); if (ST.mkc && ST.mkc.d === d) return ST.mkc; const lv = ST.lv || 1, grown = new Set(PLOTS.map(P => ST.plots[P.id] && ST.plots[P.id].crop).filter(Boolean)); let ks = Object.keys(CROPS).filter(k => !CROPS[k].tree && !CROPS[k].rare && unlocked(k) && (CROPS[k].kind !== 'trellis' || PLOTS.some(P => P.trellis)));
  ks = ks.map(k => [k, Math.random() * (grown.has(k) || (ST.inv[k] || 0) > 0 ? 3 : 1)]).sort((a, b) => b[1] - a[1]).slice(0, MKC.n).map(x => x[0]); ST.mkc = { d, items: ks.map(k => [k, Math.min(12, Math.max(4, Math.round(80 / CROPS[k].sell)))]), got: {}, done: 0 }; return ST.mkc; }   /* chọn món con đang trồng nhiều hơn */
const mkcLeft = k => { if ((ST.lv || 1) < MKC.lv) return 0; try { const M = mkcDay(), it = M.items.find(([x]) => x === k); return it ? Math.max(0, it[1] - (M.got[k] || 0)) : 0; } catch (e) { return 0; } };
function mkcSold(k, n){ const l = mkcLeft(k); if (!l) return; const M = ST.mkc; M.got[k] = (M.got[k] || 0) + Math.min(l, n); if (!M.done && M.items.every(([x, q]) => (M.got[x] || 0) >= q)){ M.done = 1; gainXP(MKC.xp); setTimeout(() => { toast(`Chợ hôm nay đủ hàng rồi · +${MKC.xp} kinh nghiệm`, 'vui'); sfx('up'); }, 300); } }
function mkcHTML(){ if ((ST.lv || 1) < MKC.lv) return ''; const M = mkcDay(); return `<div class="mkc${M.done ? ' ok' : ''}"><div class="mkh0"><b>Hôm nay chợ cần</b><span>${M.done ? 'Đủ hàng rồi, mai chợ cần món khác' : 'Bán mấy món này được giá gấp đôi'}</span></div><div class="oi">${M.items.map(([k, q]) => { const g = Math.min(q, M.got[k] || 0); return `<span class="oit${g >= q ? ' got' : ''}"><img src="${ICON[k]}" alt=""><i>${g}/${q}</i></span>`; }).join('')}${M.done ? '' : `<span class="mkxp">đủ cả ${M.items.length} món: +${MKC.xp} kinh nghiệm</span>`}</div></div>`; }
const sellValue = (k, n) => { let s = 0; const i0 = mkDay().s[k] || 0; for (let j = 0; j < n; j++) s += priceAt(k, i0 + j); return s + Math.min(mkcLeft(k), n) * (GD(k).sell || 0); };""")
rep("const mk = mkDay(); mk.s[k] = (mk.s[k] || 0) + n;", "const mk = mkDay(); mkcSold(k, n); mk.s[k] = (mk.s[k] || 0) + n;")
rep("h += khoHTML('a');", "h += mkcHTML() + khoHTML('a');")
rep('<span class="mkh">${low ? \'Bán nhiều, giá hạ · \' : \'\'}', '<span class="mkh">${mkcLeft(k) ? `<em class="mkt">Chợ cần ${mkcLeft(k)} · giá ×2</em>` : \'\'}${low ? \'Bán nhiều, giá hạ · \' : \'\'}')

# ---- B. đơn lớn của xóm mỗi ngày: rau nhiều, góp dần, trả ×1.3 như đơn nhà bên, quà kiểng ở đơn thứ 3, 10, 20 ----
rep("const ordOn = (ST.lv || 1) >= ORD.lv", "const ordOn = (ST.lv || 1) >= ORD.lv")
rep("function ordHTML(){", """const XOM = { lv: 5, who: [['Nhà chú Tư', 'đám giỗ ông nội'], ['Nhà cô Hai', 'đám cưới con gái'], ['Nhà anh Sáu', 'ăn tân gia'], ['Cả xóm', 'cúng đình cuối mùa'], ['Nhà dì Bảy', 'mừng thọ bà cụ']], gift: ['chuong_ga_hoa', 'chuong_vit_hoa', 'chuong_ga_thienly'], giftAt: [3, 10, 20], mul: 1.3 };   /* mỗi ngày một đám; trả như đơn nhà bên (×1.3), quà kiểng ở đơn thứ 3, 10, 20 */
function xomWeek(){ if ((ST.lv || 1) < XOM.lv) return null; const wk = dayKey(); if (ST.xom && ST.xom.wk === wk) return ST.xom; const lv = ST.lv || 1, grown = new Set(PLOTS.map(P => ST.plots[P.id] && ST.plots[P.id].crop).filter(Boolean));
  let ks = Object.keys(CROPS).filter(k => !CROPS[k].tree && !CROPS[k].rare && unlocked(k) && (CROPS[k].kind !== 'trellis' || PLOTS.some(P => P.trellis))); ks = ks.map(k => [k, Math.random() * (grown.has(k) ? 3 : 1)]).sort((a, b) => b[1] - a[1]).slice(0, lv >= 15 ? 4 : 3).map(x => x[0]); const tv = lv >= 15 ? 180 : lv >= 10 ? 150 : 100;
  const items = ks.map(k => [k, Math.min(30, Math.max(4, Math.round(tv / CROPS[k].sell)))]), val = items.reduce((a, [k, q]) => a + q * CROPS[k].sell, 0), [who, why] = XOM.who[Math.floor(Math.random() * XOM.who.length)], nth = (ST.xomN || 0) + 1, gift = XOM.giftAt.includes(nth) ? XOM.gift.find(g => DCK[g] && !(ST.dc && ST.dc.own && ST.dc.own[g])) || null : null;
  ST.xom = { wk, who, why, items, got: {}, xu: Math.round(val * XOM.mul / 5) * 5, xp: 8 + items.length * 3, gift, done: 0 }; return ST.xom; }
const xomLeftD = () => 0;
function xomGop(el){ const X = xomWeek(); if (!X || X.done) return; let n = 0; for (const [k, q] of X.items){ const d = Math.min(Math.max(0, q - (X.got[k] || 0)), ST.inv[k] || 0); if (d > 0){ ST.inv[k] -= d; X.got[k] = (X.got[k] || 0) + d; n += d; } } if (!n) return; sfx('pop');
  if (X.items.every(([k, q]) => (X.got[k] || 0) >= q)){ X.done = 1; ST.xomN = (ST.xomN || 0) + 1; ST.xu += X.xu; gainXP(X.xp); if (X.gift && ST.dc && ST.dc.own) ST.dc.own[X.gift] = 1; if (el) coinFly(el, 8); sfx('coin'); coinPop(`+${X.xu} xu · ${X.who}`, '#9fd36a'); say(`${X.who} gửi lời cảm ơn con.${X.gift ? ` Có quà ${DCK[X.gift].name.toLowerCase()}, vô Sắp vườn mà đổi kiểu chuồng nghe.` : ''} Mai xóm có đám khác.`, 'vui', { now: true }); }
  else toast(`Góp ${n} món rồi, gom thêm cho đủ nghe con`, 'vui'); save(); hud(); renderSheet(); }
function xomHTML(){ const X = xomWeek(); if (!X) return ''; const tot = X.items.reduce((a, [, q]) => a + q, 0), gt = X.items.reduce((a, [k, q]) => a + Math.min(q, X.got[k] || 0), 0), can = X.items.reduce((a, [k, q]) => a + Math.min(Math.max(0, q - (X.got[k] || 0)), ST.inv[k] || 0), 0);
  let h = '<div class="sub">Đơn lớn của xóm</div>'; if (X.done) return h + `<div class="note">${X.who} ${X.why} xong rồi. Mai xóm có đám khác con.</div>`;
  return h + `<div class="ordr xom"><div class="ow"><b>${X.who}</b><span>${X.why} · trong hôm nay</span></div><div class="oi">${X.items.map(([k, q]) => { const g = Math.min(q, X.got[k] || 0); return `<span class="oit${g >= q ? ' got' : ''}"><img src="${ICON[k]}" alt=""><i>${g}/${q}</i></span>`; }).join('')}</div><div class="xbar"><div class="kbar"><i style="width:${Math.round(gt / tot * 100)}%"></i></div><span>${gt}/${tot}</span></div><div class="xrw"><img src="${UIC.coin}" alt="">+${X.xu} xu${X.gift ? ` · quà: ${DCK[X.gift].name}` : ''}</div><div class="oa"><button class="btn g" data-a="xomgop" ${can ? '' : 'disabled'}>${can ? `Góp ${can} món` : 'Kho chưa có món xóm cần'}</button></div></div>`; }
function ordHTML(){""")
rep("if (SHEET.tab === 'don') h += (gheOn() ?", "if (SHEET.tab === 'don') h += xomHTML() + (gheOn() ?")
rep("else if (a === 'ghegive'){ gheGive(b); }", "else if (a === 'ghegive'){ gheGive(b); } else if (a === 'xomgop'){ xomGop(b); }")
rep(".khos{display:grid;", ".mkc{background:#F6EBD3;border:2px solid #E3C9A6;border-radius:16px;padding:10px 12px;margin:4px 0 10px}.mkc.ok{border-color:#9BD35A;background:#F3F8E8}.mkc .mkh0 b{display:block;font-family:var(--f-game);font-size:17px;color:#4A2F1E;line-height:1.1}.mkc .mkh0 span{display:block;font-size:13px;font-weight:600;color:#8A5D3B;margin:2px 0 6px}.mkc .oi{display:flex;gap:6px;flex-wrap:wrap;align-items:center}.mkc .mkxp{font-size:12px;font-weight:700;color:#8A5D3B}.mkt{display:inline-block;font-style:normal;font-weight:700;color:#4F7D44;margin-right:4px}.ordr.xom .xbar{display:flex;align-items:center;gap:8px}.ordr.xom .xbar .kbar{flex:1;height:10px;border-radius:6px;background:#6B4529;border:2px solid #4A2F1E;box-sizing:border-box;overflow:hidden}.ordr.xom .xbar .kbar i{display:block;height:100%;border-radius:4px;background:#F2C64A}.ordr.xom .xbar span{font-family:var(--f-game);font-size:14px;color:#4A2F1E}.ordr.xom .xrw{display:flex;align-items:center;gap:4px;font-size:13px;font-weight:700;color:#6B4529}.ordr.xom .xrw img{width:18px;height:18px}.khos{display:grid;")
rep('"Kho lu": "Storage jars", ', '"Kho lu": "Storage jars", "Hôm nay chợ cần": "Market wants today", "Bán mấy món này được giá gấp đôi": "These sell for double today", "Đủ hàng rồi, mai chợ cần món khác": "All filled; new picks tomorrow", "Đơn lớn của xóm": "Village big order", "Kho chưa có món xóm cần": "Nothing the village needs yet", ')

# ---- ghe chỉ đặt hàng ghe (trái cây trên cây, đồ khô, mứt, giỏ, mật ong); vườn chưa có thì đơn ít món, không kèm rau; không có gì thì hôm đó ghe không ghé ----
rep("if (pk.length >= (kind === 'ghe' ? 2 : 1)) pool.splice(0, pool.length, ...pk);", "if (kind === 'ghe' || pk.length >= 1) pool.splice(0, pool.length, ...pk);")
rep("xp: 6 + items.length * 3, ghe: 1 }; } catch (e) {} }", "xp: 6 + items.length * 3, ghe: 1 }; if (!items.length) g.o = null; } catch (e) {} }")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
