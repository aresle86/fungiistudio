# sc117: sân cỏ để đặt đồ trang trí. python3 sc117.py vào ra
#  Đồ trang trí không phải chen giữa liếp, nong phơi nữa: các bãi cỏ trống thành ô "sân cỏ" chỉ đặt đồ trang trí.
#  Sân cỏ: luôn là đất của con, không đắp liếp, không gieo, không đặt nong/khạp/lò, không đào ao, không dời cây cổ tích vô.
#  Chừa chỗ 6 cây cổ tích (FT[k].at) và đồ cố định (chuồng gà, chuồng vịt, lò ấp, lối đi, mương, sông).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:80], s.count(a))
    s = s.replace(a, b)

# lưới sân cỏ: mỗi khu một chữ cái, ô cùng cỡ liếp ngắn; skip = ô bỏ (đụng chỗ cây cổ tích, đồ cố định)
GRID = r"""
const COZ = {
  coA: { pre: 'K', x0: -6.55, z0: 2.85, cw: 1.225, cl: .8, gap: .1, rg: .3, cols: 4, n: 8, skip: [4, 5, 6, 7, 8], name: 'Sân cỏ hông nhà' },
  coB: { pre: 'M', x0: 1.0, z0: 6.4, cw: 1.225, cl: .8, gap: .1, rg: .3, cols: 4, n: 4, skip: [1, 3, 4], name: 'Sân cỏ trước mương' },
  coC: { pre: 'P', x0: 7.3, z0: 4.3, cw: 1.225, cl: .8, gap: .1, rg: .3, cols: 2, n: 2, skip: [2], name: 'Sân cỏ cạnh giàn' },
  coD: { pre: 'Q', x0: -1.45, z0: -.45, cw: 1.225, cl: .8, gap: .3, rg: .3, cols: 1, n: 2, skip: [2], name: 'Sân cỏ đầu bãi' },
  coE: { pre: 'U', x0: -4.6, z0: 7.35, cw: 1.225, cl: .8, gap: .1, rg: .3, cols: 2, n: 2, skip: [2], name: 'Sân cỏ mé sông' } };
for (const [zk, Z] of Object.entries(COZ)) for (let i = 0; i < Z.n; i++){ if (Z.skip.includes(i + 1)) continue; const c = i % Z.cols, r = Math.floor(i / Z.cols), u0 = Z.x0 + c * (Z.cw + Z.gap), v0 = Z.z0 + r * (Z.cl + Z.rg); PLOTS.push({ id: Z.pre + (i + 1), b: [u0, v0, u0 + Z.cw, v0 + Z.cl], name: `${Z.name} · chỗ ${i + 1}`, bai: true, co: 1, zone: zk, lv: 7 }); }
"""
rep("const PL = Object.fromEntries(PLOTS.map(p => [p.id, p]));", GRID + "const PL = Object.fromEntries(PLOTS.map(p => [p.id, p]));")
rep("const ZGRID = { bai: [BAI, 'H', 12], song: [SONG, 'S', 8], sau: [SAU, 'N', 10] };",
    "const ZGRID = { bai: [BAI, 'H', 12], song: [SONG, 'S', 8], sau: [SAU, 'N', 10], ...Object.fromEntries(Object.entries(COZ).map(([k, Z]) => [k, [Z, Z.pre, Z.n]])) };")
# sân cỏ: luôn của con, không bao giờ là liếp
rep("const isBed = P => /^[ABCHSN]/.test(P.id), locked = P => isBed(P) && !ST.open.includes(P.id);",
    "const isBed = P => /^[ABCHSN]/.test(P.id), locked = P => !!P.co || (isBed(P) && !ST.open.includes(P.id));")
rep("function landSt(id){ const P = PL[id]; if (!P || !P.bai) return 'own';", "function landSt(id){ const P = PL[id]; if (P && P.co) return (ST.coOwn || []).includes(id) ? 'own' : 'co'; if (!P || !P.bai) return 'own';")
# không hiện mảng cỏ phát với cọc tre như đất mới khai hoang
rep("if (v.mow) v.mow.visible = on && lk && !nh && !cov && ls === 'own';", "if (v.mow) v.mow.visible = on && lk && !nh && !cov && ls === 'own' && !P.co;")
# chỉ đồ trang trí: không nong, khạp, lò, ao, cây cổ tích
rep("function bigFit(id, me){ const P = PL[id]; if (!P || !P.bai) return null;", "function bigFit(id, me){ const P = PL[id]; if (!P || !P.bai || P.co) return null;")
rep("function placeObj(k, id){ const O = ST[k], P = PL[id]; if (!O || !O.own || !P ||", "function placeObj(k, id){ const O = ST[k], P = PL[id]; if (!O || !O.own || !P || P.co ||")
rep("if (!(at && PL[at] && PL[at].bai && locked(PL[at])", "if (!(at && PL[at] && PL[at].bai && !PL[at].co && locked(PL[at])")
rep("const freeCell = () => { const c = PLOTS.find(P => P.bai &&", "const freeCell = () => { const c = PLOTS.find(P => P.bai && !P.co &&")
rep("function sapFree(id, it){ const P = PL[id]; if (!P || !P.bai ||", "function sapFree(id, it){ const P = PL[id]; if (!P || !P.bai || (P.co && it && it.t !== 'dc') ||")
rep("function sapWhy(id, it){ const P = PL[id]; if (!P || !P.bai) return '';", "function sapWhy(id, it){ const P = PL[id]; if (!P || !P.bai) return ''; if (P.co && it && it.t !== 'dc') return 'Sân cỏ chỉ đặt đồ trang trí';")
# mua sân cỏ (đất thổ cư): mắc hơn đất ruộng, miếng sau mắc hơn miếng trước; mua trong Sắp vườn
BUY = r"""
const CO_BASE = 500, CO_G = 1.13; if (!ST.coOwn) ST.coOwn = [];
const coCost = () => Math.round(CO_BASE * Math.pow(CO_G, (ST.coOwn || []).length) / 5) * 5;
function coBuy(id){ const P = PL[id]; if (!P || !P.co || landOwn(id)) return false; const c = coCost(); if (ST.xu < c){ toast(`Miếng đất này ${c} xu, con còn thiếu ${c - ST.xu} xu.`, 'dan', { now: true }); return false; }
  ST.xu -= c; ST.coOwn.push(id); coinPop(`-${c} xu · đất thổ cư`, '#F08A6E'); refreshPlot(id); objPuff(id); sfx('up'); buzz(15); save(); hud(); sayOnce('co1', 'Miếng đất thổ cư này là của con rồi. Kéo ghế đá, chậu kiểng trong túi ra đặt cho vườn đẹp nghe.', 'vui'); return true; }
"""
rep("function sapChipsDraw(){", BUY + " function sapChipsDraw(){ if (SAPSEL && PL[SAPSEL] && PL[SAPSEL].co){ const ch = $('#sapChips'); ch.innerHTML = landOwn(SAPSEL) ? `<button data-c=\"hint\"><img src=\"${UIC.dc_ghe_da || ICON.la}\" alt=\"\">Kéo đồ trang trí trong túi ra đây</button>` : `<button data-c=\"comua\"><img src=\"${UIC.coin}\" alt=\"\">Mua đất · ${coCost()} xu</button>`; return; }")
rep("function sapPick(id){ SAPSEL = SAPSEL === id ? null : id;", "function sapPick(id){ SAPSEL = SAPSEL === id ? null : id;")
rep("$('#sapChips').addEventListener('click', e => { const b = e.target.closest('[data-c]'); if (!b || !SAPSEL) return; const id = SAPSEL; SAPSEL = null; if (b.dataset.c === 'san')",
    "$('#sapChips').addEventListener('click', e => { const b = e.target.closest('[data-c]'); if (!b || !SAPSEL) return; const id = SAPSEL; SAPSEL = null; if (b.dataset.c === 'hint') return; if (b.dataset.c === 'comua'){ coBuy(id); return; } if (b.dataset.c === 'san')")
rep("function sapTap(cx, cy){ if (DROP){ DROP = null; return; } const id = sapCellXY(cx, cy);", "function sapTap(cx, cy){ if (DROP){ DROP = null; return; } const id = sapCellXY(cx, cy); if (id && PL[id].co && !landOwn(id)) return sapPick(id);")
# Sắp vườn vẽ cả sân cỏ chưa mua: viền vàng đứt nét, nút đồng xu
rep("const cells = PLOTS.filter(P => P.bai && !hidP(P) && landOwn(P.id));", "const cells = PLOTS.filter(P => P.bai && !hidP(P) && (landOwn(P.id) || P.co)), coBuyCells = DRAG || DROP ? [] : cells.filter(P => P.co && !landOwn(P.id));")
rep("  if (sv.dataset.h !== h){ sv.innerHTML = h; sv.dataset.h = h; }", "  for (const P of coBuyCells) h += `<polygon class=\"${P.id === SAPSEL ? 'sel' : 'cobuy'}\" points=\"${sapPoly(P.b)}\"/>`;   if (sv.dataset.h !== h){ sv.innerHTML = h; sv.dataset.h = h; }")
rep("for (const P of cells){ const fr = sapFree(P.id, null), sn = !fr && sapSan(P.id); if (!fr && !sn) continue;", "for (const P of cells){ const cb = P.co && !landOwn(P.id), fr = !cb && sapFree(P.id, null), sn = !cb && !fr && sapSan(P.id); if (!fr && !sn && !cb) continue;")
rep("if (b.dataset.m !== (sn ? 's' : 'p')){ b.dataset.m = sn ? 's' : 'p'; b.innerHTML = sn ? SAPSV.san : SAPSV.plus; b.setAttribute('aria-label', sn ? 'San liếp trống này thành cỏ' : 'Đặt gì ở ô này'); b.classList.toggle('san', sn); }",
    "if (b.dataset.m !== (cb ? 'c' : sn ? 's' : 'p')){ b.dataset.m = cb ? 'c' : sn ? 's' : 'p'; b.innerHTML = cb ? `<img src=\"${UIC.coin}\" alt=\"\" style=\"width:26px;height:26px\">` : sn ? SAPSV.san : SAPSV.plus; b.setAttribute('aria-label', cb ? 'Mua đất thổ cư' : sn ? 'San liếp trống này thành cỏ' : 'Đặt gì ở ô này'); b.classList.toggle('san', sn); b.classList.toggle('cob', cb); }")
rep("if (SAPSEL && !sapFree(SAPSEL, null) && !sapSan(SAPSEL)) SAPSEL = null;", "if (SAPSEL && !sapFree(SAPSEL, null) && !sapSan(SAPSEL) && !(PL[SAPSEL].co && !landOwn(SAPSEL))) SAPSEL = null;")
rep(".sapplus.on{background:#F2C64A;color:#4A2F1E}", ".sapplus.on{background:#F2C64A;color:#4A2F1E} .sapplus.cob{background:#FFF6DC;border-color:#B07A1A} #sapSvg .cobuy{fill:rgba(242,198,74,.18);stroke:#C9952A;stroke-width:3;stroke-dasharray:10 7}")
# chạm sân cỏ ngoài chế độ Sắp vườn: không mở bảng đắp liếp, không tưới, không gieo
rep("const plotAt = (x, z) => PLOTS.find(P => { if (hidP(P)) return false;", "const plotAt = (x, z) => PLOTS.find(P => { if (hidP(P) || P.co) return false;")
rep("const plotNear = (x, z, tol) => plotAt(x, z) || PLOTS.filter(P => !hidP(P))", "const plotNear = (x, z, tol) => plotAt(x, z) || PLOTS.filter(P => !hidP(P) && !P.co)")
# giá khai hoang: mở đất là chuyện lớn, ô đầu đã vài trăm xu, ô sau đắt hơn ô trước; khu mở trễ thì đắt hơn
rep("const LANDZ = { bai: { base: 100,", "const LANDZ = { bai: { base: 200, g: 1.15,")
rep("song: { base: 160,", "song: { base: 450, g: 1.17,")
rep("sau: { base: 200,", "sau: { base: 900, g: 1.18,")
rep("return Math.round(LANDZ[zk].base * Math.pow(1.05, k) * (k < 2 ? .5 : 1)); };", "return Math.round(LANDZ[zk].base * Math.pow(LANDZ[zk].g, k) / 5) * 5; };")
rep("landStarted(zk) < 2 ? 'Hai ô đầu Ngoại phụ nửa tiền.' : 'Ô sau tốn hơn ô trước một chút.'", "'Mở đất là chuyện lớn, ô sau tốn hơn ô trước.'")
# Sắp vườn mở cùng cấp 7 với bãi hông nhà, đất thổ cư và món trang trí đặt đầu tiên
rep("const SAPLV = 8;", "const SAPLV = 7;")
rep("get: () => ({ ftrCheck,", "get: () => ({ sapMode, PV, PL, COZ, coBuy, coCost, ftrCheck,")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
