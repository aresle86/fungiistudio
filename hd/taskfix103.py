#!/usr/bin/env python3
"""v103: việc hằng ngày theo công sức — thêm việc cho mọi hệ đã mở, số lượng theo cỡ vườn, thưởng theo cấp và thưởng bằng đồ."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---------- đếm việc mới ----------
rep("ST.ord.done = (ST.ord.done || 0) + 1;", "ST.ord.done = (ST.ord.done || 0) + 1; bump('ord');")
rep("ST.bonN = (ST.bonN || 0) + 1; gainXP(2); save(); hud(); }\nfunction hoRau", "ST.bonN = (ST.bonN || 0) + 1; bump('bon'); gainXP(2); save(); hud(); }\nfunction hoRau")
rep("L.on = 1; L.t = L.done ? LO.t : LO.first;", "L.on = 1; bump('lo'); L.t = L.done ? LO.t : LO.first;")
rep("g.n++; sfx('pick'); save(); hud();", "g.n++; bump('gio'); sfx('pick'); save(); hud();")
rep("function ongTake(){ const O = ST.ong; if (!O || !O.honey) return false; const n = O.honey,", "function ongTake(){ const O = ST.ong; if (!O || !O.honey) return false; bump('mat'); const n = O.honey,")
rep("function tbTake(){ const B = ST.tb; if (!B || !B.done || loLeft() > 0) return; ST.tbN = (ST.tbN || 0) + 1;", "function tbTake(){ const B = ST.tb; if (!B || !B.done || loLeft() > 0) return; ST.tbN = (ST.tbN || 0) + 1; bump('tb');")
rep("ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0;", "ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0; if (c.tree) bump('tree');")
rep("ST.dc.bag[k]--; ST.dc.items.push({ k, at: id });", "ST.dc.bag[k]--; ST.dc.items.push({ k, at: id }); bump('dc');")

# ---------- việc cho mọi hệ đã mở; thưởng đồ đúng việc ----------
rep("  try { if (lv >= 2) F.push({ lv: 2, t: 'odd', txt: 'Làm 2 việc lặt vặt quanh vườn', need: 2, rw: ['coin', 15] }); } catch (e) {}",
    "  try { if (lv >= 2) F.push({ lv: 2, t: 'odd', txt: 'Làm 2 việc lặt vặt quanh vườn', need: 2, rw: ['rom', 2] }); } catch (e) {}\n"
    "  try { if (lv >= ORD.lv) F.push({ lv: ORD.lv, t: 'ord', txt: 'Giao 2 đơn nhà bên', need: 2, rw: ['coin', 20] }); } catch (e) {}\n"
    "  try { if (nTrees() > 0) F.push({ lv: 8, t: 'tree', txt: 'Hái 1 vụ cây trái', need: 1, rw: ['coin', 20] }); } catch (e) {}\n"
    "  try { if (ownObj('ho')) F.push({ lv: OBJD.ho.lv, t: 'bon', txt: 'Bón phân 1 liếp', need: 1, rw: ['rom', 3] }); } catch (e) {}\n"
    "  try { if (dcOn() && !((ST.dc && ST.dc.items) || []).length) F.push({ lv: DC.lv + .5, t: 'dc', txt: 'Đặt 1 món trang trí trong vườn', need: 1, rw: ['coin', 25] }); } catch (e) {}\n"
    "  try { if (loOn()) F.push({ lv: LO.lv, t: 'lo', txt: 'Ấp 1 lò trứng vịt', need: 1, rw: ['cui', 2] }); } catch (e) {}\n"
    "  try { if (gioOn()) F.push({ lv: GIO.lv, t: 'gio', txt: 'Nhờ Ngoại đan 1 giỏ', need: 1, rw: ['coin', 25] }); } catch (e) {}\n"
    "  try { if (ownObj('ong')) F.push({ lv: OBJD.ong.lv, t: 'mat', txt: 'Lấy mật ong', need: 1, rw: ['coin', 30] }); } catch (e) {}\n"
    "  try { if (ST.tb && ST.tb.done) F.push({ lv: TB.lv, t: 'tb', txt: 'Lấy lờ ghe tam bản', need: 1, rw: ['coin', 30] }); } catch (e) {}")
rep("F.push({ lv: BEP.lv, t: 'cook', txt: 'Nấu 1 món ở bếp Ngoại', need: 1, rw: ['coin', 20] });", "F.push({ lv: BEP.lv, t: 'cook', txt: 'Nấu 1 món ở bếp Ngoại', need: 1, rw: ['cui', 3] });")
rep("F.push({ lv: OBJD.say.lv, t: 'say', txt: 'Sấy 1 mẻ ở lò', need: 1, rw: ['coin', 25] });", "F.push({ lv: OBJD.say.lv, t: 'say', txt: 'Sấy 1 mẻ ở lò', need: 1, rw: ['cui', 3] });")
rep("F.push({ lv: OBJD.khap.lv, t: 'khap', txt: 'Muối 1 khạp', need: 1, rw: ['coin', 20] });", "F.push({ lv: OBJD.khap.lv, t: 'khap', txt: 'Muối 1 khạp', need: 1, rw: ['muoi', 2] });")
rep("F.push({ lv: OBJD.nong.lv, t: 'nong', txt: 'Phơi 1 nong', need: 1, rw: ['coin', 15] });", "F.push({ lv: OBJD.nong.lv, t: 'nong', txt: 'Phơi 1 nong', need: 1, rw: ['rom', 3] });")

# ---------- việc cơ bản theo cỡ vườn ----------
rep("  () => ({ t: 'water', txt: 'Tưới liếp 3 lần', need: 3, rw: ['coin', 15] }),",
    "  () => { const n = Math.max(3, Math.round(PLOTS.filter(P => !P.tree && !P.trellis && !hidP(P) && !locked(P)).length * .3)); return { t: 'water', txt: `Tưới liếp ${n} lần`, need: n, rw: ['coin', 15] }; },")
rep("r => { const ks = ['cai', 'hanh', 'raumuong', 'ot', 'bap', 'cachua'].filter(k => unlocked(k));",
    "r => { const ks = Object.keys(UNLOCK).filter(k => unlocked(k) && CROPS[k] && !CROPS[k].tree).sort((a, b) => UNLOCK[b] - UNLOCK[a]).slice(0, 3);   /* ưu tiên rau mới mở */")
rep("  () => ({ t: 'sell', txt: 'Bán 6 món ở chợ', need: 6, rw: ['coin', 20] }),",
    "  () => { const n = 6 + Math.floor((ST.lv || 1) / 3) * 2; return { t: 'sell', txt: `Bán ${n} món ở chợ`, need: n, rw: ['coin', 20] }; },")

# ---------- cơ cấu: từ cấp 12 bớt việc cơ bản, thêm việc của đồ đã có; thưởng xu tăng theo cấp ----------
rep("const nf = Math.min(F.length, 2);", "const nf = Math.min(F.length, (ST.lv || 1) >= 12 ? 3 : 2);")
rep("  ST.tasks = { day: dk, list: list.map(x => ({ ...x, have: 0, done: false })), bonus: bk, got: false }; }",
    "  { const lvK = 1 + Math.min(1.5, ((ST.lv || 1) - 1) * .1); for (const x of list) if (x.rw[0] === 'coin') x.rw = ['coin', Math.round(x.rw[1] * lvK / 5) * 5]; }   /* thưởng xu tăng theo cấp, có trần */\n"
    "  ST.tasks = { day: dk, list: list.map(x => ({ ...x, have: 0, done: false })), bonus: bk, got: false }; }")

# ---------- nhận thưởng: xu, rơm, hay đồ gác bếp ----------
RWN = "{ cui: 'bó củi', muoi: 'bịch muối', duong: 'bịch đường' }"
rep("if (x.rw[0] === 'coin') xu += x.rw[1]; else rom += x.rw[1]; x.cl = true; }",
    "if (x.rw[0] === 'coin') xu += x.rw[1]; else if (x.rw[0] === 'rom') rom += x.rw[1]; else { const kk = x.rw[0]; STORE(kk)[kk] = (STORE(kk)[kk] || 0) + x.rw[1]; } x.cl = true; }")
rep("function tkClaim(ids, btn){ const T2 = ST.tasks; let xu = 0, rom = 0;", "function tkClaim(ids, btn){ const T2 = ST.tasks; let xu = 0, rom = 0; const oth = [];")
rep("const v = x.rw[1], isC = x.rw[0] === 'coin'; if (isC) xu += v; else rom += v;",
    "const v = x.rw[1], isC = x.rw[0] === 'coin'; if (isC) xu += v; else if (x.rw[0] === 'rom') rom += v; else { const kk = x.rw[0]; STORE(kk)[kk] = (STORE(kk)[kk] || 0) + v; oth.push(`+${v} ${(" + RWN + ")[kk] || kk}`); }")
rep("d.src = isC ? UIC.coin : ICON.rom;", "d.src = isC ? UIC.coin : (ICON[x.rw[0]] || ICON.rom);")
rep("if (!xu && !rom) return; ST.xu += xu;", "if (!xu && !rom && !oth.length) return; ST.xu += xu;")
rep("coinPop([xu ? `+${xu} xu` : '', rom ? `+${rom} rơm` : ''].filter(Boolean).join(' · ') + ' · thưởng việc', '#9fd36a');",
    "coinPop([xu ? `+${xu} xu` : '', rom ? `+${rom} rơm` : '', ...oth].filter(Boolean).join(' · ') + ' · thưởng việc', '#9fd36a');")
rep("${x.rw[0] === 'coin' ? UIC.coin : ICON.rom}", "${x.rw[0] === 'coin' ? UIC.coin : (ICON[x.rw[0]] || ICON.rom)}", 2)

# ---------- icon + đi làm cho việc mới ----------
rep("const TASKIC = x => ", "const TASKIC = x => x.t === 'ord' ? (ICON.cho || UIC.task) : x.t === 'tree' ? (ICON.xoai || ICON.chuoi) : x.t === 'bon' ? (ICON.phan || ICON.ho) : x.t === 'dc' ? (UIC.dc || UIC.task) : x.t === 'lo' ? (ICON.vitcon || ICON.trungvit) : x.t === 'gio' ? ICON.gio : x.t === 'mat' ? ICON.matong : x.t === 'tb' ? (UIC.tamban || ICON.caro) : ")
rep("  else if (t === 'cook'){ openSheet('bep'); return; } else if (t === 'fish'){ openSheet('ben'); return; }",
    "  else if (t === 'cook'){ openSheet('bep'); return; } else if (t === 'fish'){ openSheet('ben'); return; }\n"
    "  else if ({ ord: 'ben', bon: 'ho', lo: 'lo', gio: 'gio', mat: 'ong', tb: 'tb', dc: 'deco' }[t]){ try { openSheet({ ord: 'ben', bon: 'ho', lo: 'lo', gio: 'gio', mat: 'ong', tb: 'tb', dc: 'deco' }[t]); } catch (e) {} return; }\n"
    "  else if (t === 'tree') v = near(L.filter(P => P.tree && ST.plots[P.id] && ST.plots[P.id].crop && ripe(ST.plots[P.id])).map(P => P.id)) || near(L.filter(P => P.tree).map(P => P.id));")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
