# v144 (BẢN THỬ, chưa lên live): bếp + đơn hàng theo bài học Hay Day, anh Ares duyệt "làm cả 2 bước" 13/11.
# Gói 1 (số):
#  (1) Món bếp mở rải đều theo cấp (mỗi cấp 1-2 món, hết dồn 4 món ở cấp 4 và cấp 9). Ai đã mở món nào thì giữ món đó (ST.bepOpen + món đã nấu).
#  (2) Giá món = tiền nguyên liệu + công theo thời gian nấu và theo cấp. Món lời quá mỏng thì nấu nồi lớn hơn (thêm nguyên liệu) thay vì chỉ nâng giá.
#  (3) Kinh nghiệm: nấu món = giá/8 (cũ giá/25), phơi/muối/sấy = giá/10 (cũ /15), đơn hàng = xu/10 (cũ 1 + 2 mỗi món).
#  (4) Đơn nhà bên: bảng 3 đơn, lên 4 ở cấp 8, 5 ở cấp 14. 10 đơn đầu mỗi ngày đơn mới tới sau 3 phút, sau đó 25 phút.
#      5 đơn đầu đời có đơn mới liền. Giao đủ 3 / 6 / 10 đơn trong ngày được thưởng thêm xu.
#      Món nấu vô đơn từ lúc nhóm bếp (cũ: cấp 8), hay đặt món ít nấu. Số món mỗi đơn tăng dần, cấp 16+ có 2 món chế biến.
# Gói 2 (thành thạo): bếp / nong / khạp / lò sấy cộng giờ làm, 3 sao: +10% giá bán, +10% kinh nghiệm, nhanh hơn 15%.
#      Dùng lại hàng sao "Thuần thục" của cây (không hình mới). Tính bù giờ cho món đã làm trước đây.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v143b'", "BUILD = 'v144'")

# (1)(2) bậc thang món + giá
rep("\nconst PHOI = {", """
/* v144: món mở rải đều theo cấp, giá theo công nấu. [cấp, giá, nguyên liệu mới nếu nồi lớn hơn] */
{ const D144 = { rmluoc: [4, 35], caixao: [4, 50], trungchien: [5, 85], bapluoc: [5, 90], canhchua: [6, 115], khoquatrung: [7, 150], canhmongtoi: [8, 95, { mongtoi: 6, hanh: 2, cui: 1 }], banhchuoi: [9, 200, { chuoi: 2, trungga: 2, cui: 1 }],
  nuongtrui: [10, 80], teprangkhe: [11, 70], cakho: [12, 130], canhchuaca: [13, 165], goidudu: [14, 95], canhbau: [15, 130, { bau: 2, tep: 2, hanh: 1, cui: 1 }], canhmuop: [16, 120, { muop: 2, mongtoi: 4, cui: 1 }], canhchuakhom: [16, 150],
  calinhkho: [17, 155], khemat: [17, 195], chuoimat: [18, 240], daurongxao: [18, 110, { daurong: 4, cui: 1 }], goibuoi: [19, 145], chesaurieng: [22, 290], duasapdam: [24, 160] };
  for (const k in D144){ const d = DISH[k], [lv, sell, inn] = D144[k]; if (!d) continue; d.lv0 = d.lv; d.lv = lv; d.sell = sell; if (inn) d.in = inn; } }
function dLv(k){ const d = DISH[k]; try { if (!ST.v144){ ST.v144 = 1; const o = ST.bepOpen = ST.bepOpen || {}, lv = ST.lv || 1; for (const j in DISH) if ((DISH[j].lv0 || 99) <= lv && DISH[j].lv > lv) o[j] = 1; } if ((ST.bepOpen && ST.bepOpen[k]) || (ST.bep && ST.bep.made && ST.bep.made[k])) return Math.min(d.lv, d.lv0 || d.lv); } catch (e) {} return d.lv; }   /* ai mở món nào rồi thì giữ */
const PHOI = {""")
rep("Object.keys(DISH).some(k => DISH[k].lv <= lv && !(ST.bep", "Object.keys(DISH).some(k => dLv(k) <= lv && !(ST.bep")
rep("Object.keys(DISH).filter(k => lv >= DISH[k].lv && ST.bep", "Object.keys(DISH).filter(k => lv >= dLv(k) && ST.bep")
rep("lv < (R2.lv || 1)) return false;", "lv < (DISH[k] ? dLv(k) : R2.lv || 1)) return false;")
rep("[k, { ...d, t: d.t / ST.spd }]", "[k, { ...d, lv: dLv(k), t: d.t / ST.spd }]")
rep("if ((ST.lv || 1) < d.lv || i < 0 || !bepCan(k)) return;", "if ((ST.lv || 1) < dLv(k) || i < 0 || !bepCan(k)) return;")

# Gói 2: thành thạo
rep("function mastRow(k){", """/* v144: thành thạo chỗ chế biến, tính theo giờ làm */
function ttOf(k){ return DISH[k] ? 'bep' : PHOI[k] ? 'nong' : MUOI[k] ? 'khap' : SAY[k] ? 'say' : ''; }
function ttT(s){ return ({ bep: [5, 20, 60], nong: [40, 150, 400], khap: [100, 300, 800], say: [60, 200, 500] })[s]; }
function ttInit(){ if (ST.tt) return ST.tt; const T = ST.tt = { bep: 0, nong: 0, khap: 0, say: 0 }; try { for (const [k, n] of Object.entries((ST.bep && ST.bep.made) || {})) if (DISH[k]) T.bep += n * DISH[k].t; T.nong = ((ST.nong && ST.nong.done) || 0) * 5 * 3600; T.khap = ((ST.khap && ST.khap.done) || 0) * 14 * 3600; T.say = ((ST.say && ST.say.done) || 0) * 6.5 * 3600; } catch (e) {} return T; }   /* tính bù cho món đã làm trước v144 */
function ttS(s){ if (!s) return 0; const h = (ttInit()[s] || 0) / 3600, M = ttT(s); return h >= M[2] ? 3 : h >= M[1] ? 2 : h >= M[0] ? 1 : 0; }
function ttSell(k){ return GD(k).sell * (ttS(ttOf(k)) >= 1 ? 1.1 : 1); }
function ttXP(k, n){ return Math.max(1, Math.round(n * (ttS(ttOf(k)) >= 2 ? 1.1 : 1))); }
function ttTime(k, t){ return ttS(ttOf(k)) >= 3 ? Math.round(t * .85) : t; }
function ttPerk(b){ return b === 1 ? L135('bán được giá hơn 10%', 'sells for 10% more') : b === 2 ? L135('thêm 10% kinh nghiệm', '10% more experience') : L135('làm nhanh hơn 15%', '15% faster'); }
function ttName(s){ return s === 'bep' ? L135('Bếp Ngoại', "Ngoại's kitchen") : s === 'nong' ? L135('Nong phơi', 'Drying tray') : s === 'khap' ? L135('Khạp muối', 'Pickling jar') : L135('Lò sấy', 'Drying oven'); }
function ttAdd(k, sec){ const s = ttOf(k); if (!s) return; const a = ttS(s); ttInit()[s] += sec; const b = ttS(s); if (b > a) setTimeout(() => { try { gainXP(10 * b); sfx('up'); toast(`${ttName(s)} ${L135('lên', 'reached')} ${b} ${L135('sao thành thạo', b > 1 ? 'skill stars' : 'skill star')} · ${ttPerk(b)}`); hud(); } catch (e) {} }, 1300); }
function ttHr(h){ return (h < 10 ? Math.round(h * 10) / 10 : Math.round(h)).toString().replace('.', L135(',', '.')); }
function ttRow(s){ const st = ttS(s), M = ttT(s), h = (ttInit()[s] || 0) / 3600; return `<div class="mast"><span class="msts">${mastSt(st, 24)}</span><div><b>${L135('Thành thạo', 'Skill')}</b><small>${st >= 3 ? L135(`Đã làm ${ttHr(h)} giờ · đủ ba sao rồi`, `${ttHr(h)} hours worked · all three stars`) : L135(`Đã làm ${ttHr(h)} giờ · còn ${ttHr(Math.max(.1, M[st] - h))} giờ nữa lên sao: ${ttPerk(st + 1)}`, `${ttHr(h)} hours worked · ${ttHr(Math.max(.1, M[st] - h))} more for a star: ${ttPerk(st + 1)}`)}</small></div></div>`; }
function mastRow(k){""")
rep("h += upxHTML('nong');", "h += ttRow('nong') + upxHTML('nong');")
rep("h += upxHTML('khap');", "h += ttRow('khap') + upxHTML('khap');")
rep("return h + upxHTML('say') +", "return h + ttRow('say') + upxHTML('say') +")
rep("return h + UX.more('Bếp Ngoại', 'Hai nồi nấu cùng lúc", "return h + ttRow('bep') + UX.more('Bếp Ngoại', 'Hai nồi nấu cùng lúc")
# giá bán có sao
rep("Math.round(GD(k).sell * Math.max(MK.floor,", "Math.round(ttSell(k) * Math.max(MK.floor,")
rep("s2 + q * GD(k).sell, 0)", "s2 + q * ttSell(k), 0)", 4)
rep("const val = L.q * GD(L.k).sell,", "const val = L.q * ttSell(L.k),")
# thời gian có sao
rep("B.pots[i] = { k, t: d.t };", "B.pots[i] = { k, t: ttTime(k, d.t), T: ttTime(k, d.t) };")
rep("[1 - t.t / DISH[t.k].t, '#E9A23A']", "[1 - t.t / (t.T || DISH[t.k].t), '#E9A23A']")
rep("{ ...p, T: DISH[p.k].t, t: p.t }", "{ ...p, T: p.T || DISH[p.k].t, t: p.t }")
rep("{ k, t: fast ? NONG.first : d.t, T: fast ? NONG.first : d.t, fast }", "{ k, t: fast ? NONG.first : ttTime(k, d.t), T: fast ? NONG.first : ttTime(k, d.t), fast }")
rep("{ k, t: fast ? 30 : d.t, T: fast ? 30 : d.t, fast }", "{ k, t: fast ? 30 : ttTime(k, d.t), T: fast ? 30 : ttTime(k, d.t), fast }")
rep("{ k, t: fast ? 40 : d.t, T: fast ? 40 : d.t, fast }", "{ k, t: fast ? 40 : ttTime(k, d.t), T: fast ? 40 : ttTime(k, d.t), fast }")
rep("<div class=\"rm\">${fmtT(d.t)}<em>", "<div class=\"rm\">${fmtT(ttTime(k, d.t))}<em>")
# (3) kinh nghiệm + cộng giờ thành thạo
rep("B.made[p.k] = (B.made[p.k] || 0) + 1; flyTo(ICON[p.k], BEPW.x, .6, BEPW.z);", "ttAdd(p.k, d.t); B.made[p.k] = (B.made[p.k] || 0) + 1; flyTo(ICON[p.k], BEPW.x, .6, BEPW.z);")
rep("gainXP(Math.round(d.sell / 25) + 1); bump('cook');", "gainXP(ttXP(p.k, d.sell / 8)); bump('cook');")
rep("sfx('pop'); gainXP(Math.round(PHOI[t.k].sell * on / 15));", "sfx('pop'); gainXP(ttXP(t.k, PHOI[t.k].sell * on / 10)); ttAdd(t.k, PHOI[t.k].t);")
rep("sfx('pop'); gainXP(Math.round(d.sell * d.out / 15));", "sfx('pop'); gainXP(ttXP(j.k, d.sell * d.out / 10)); ttAdd(j.k, d.t);")
rep("sfx('pop'); gainXP(Math.round(d.sell / 15));", "sfx('pop'); gainXP(ttXP(t.k, d.sell / 10)); ttAdd(t.k, SAY[t.k] ? SAY[t.k].t : 0);")

# (4) đơn nhà bên
rep("const ORD = { lv: 3, max: 3, every: 25 * 60, again: 10 * 60, mul: 1.3, skip: 3, fish: 3 };",
    "const ORD = { lv: 3, max: 3, every: 25 * 60, soon: 3 * 60, again: 10 * 60, mul: 1.3, skip: 3, fish: 3 };\n"
    "function ordMax(){ const lv = ST.lv || 1; return lv < 8 ? 3 : lv < 14 ? 4 : 5; }   /* v144: bảng đơn rộng dần theo cấp */\n"
    "function ordDay(){ const d = dayKey(); return ST.ord.day && ST.ord.day.d === d ? ST.ord.day : (ST.ord.day = { d, n: 0 }); }\n"
    "function ordEvery(){ return ordDay().n < 10 ? ORD.soon : ORD.every; }   /* 10 đơn đầu ngày: 3 phút có đơn mới */\n"
    "function ordAfter(){ const D = ordDay(); D.n++; const lv = ST.lv || 1; if ((ST.ord.done || 0) <= 5){ try { if (ST.ord.list.length < ordMax()) ST.ord.list.push(leadMake('nb') || ordMake()); } catch (e) {} }\n"
    "  const m = [3, 6, 10].indexOf(D.n); if (m >= 0){ const xu = Math.round((15 + lv * 3) * (m + 1) / 5) * 5; ST.xu += xu; setTimeout(() => { try { sfx('up'); toast(L135(`Hôm nay giao ${D.n} đơn rồi · bà con thưởng thêm ${xu} xu`, `${D.n} orders today · neighbors tip ${xu} coins`)); hud(); } catch (e) {} }, 1500); } }\n"
    "function ordDayH(){ const n = ordDay().n, nx = [3, 6, 10].find(x => x > n); return nx ? `<div class=\"note\" style=\"margin:2px 0 8px\">${L135(`Hôm nay giao ${n} đơn · đủ ${nx} đơn bà con thưởng thêm`, `${n} orders today · reach ${nx} for a tip`)}</div>` : ''; }")
rep("if (ST.ord.list.length >= ORD.max){ ST.ord.acc = 0; return; } ST.ord.acc += dt; if (ST.ord.acc < ORD.every) return;", "if (ST.ord.list.length >= ordMax()){ ST.ord.acc = 0; return; } ST.ord.acc += dt; if (ST.ord.acc < ordEvery()) return;")
rep("Math.ceil((ORD.every - ST.ord.acc) / ST.spd / 60)", "Math.ceil((ordEvery() - ST.ord.acc) / ST.spd / 60)")
rep("ST.ord.acc = Math.max(ST.ord.acc, ORD.every - ORD.again);", "ST.ord.acc = Math.max(ST.ord.acc, ordEvery() - ORD.again);")
rep("ST.ord.done = (ST.ord.done || 0) + 1; bump('ord');", "ST.ord.done = (ST.ord.done || 0) + 1; bump('ord'); ordAfter();")
rep("return h + L.map(o => { const ok = ordCan(o);", "return h + ordDayH() + L.map(o => { const ok = ordCan(o);")
rep("xu: Math.round(val * ORD.mul / 5) * 5, xp: 1 + items.length * 2 }; }", "xu: Math.round(val * ORD.mul / 5) * 5, xp: Math.max(3, Math.round(val * ORD.mul / 10)) }; }", 2)
rep("* 1.5 / 5) * 5, xp: 8, lead: L.k,", "* 1.5 / 5) * 5, xp: Math.max(8, Math.round(val * ORD.mul * 1.5 / 10)), lead: L.k,")
rep("const nItems = lv < 5 ? (Math.random() < .4 ? 2 : 1) : lv < 11 ? 2 : lv < 15 ? 2 + (Math.random() < .5 ? 1 : 0) : 3;",
    "const nItems = lv < 5 ? (Math.random() < .4 ? 2 : 1) : lv < 8 ? 2 : lv < 12 ? 2 + (Math.random() < .5 ? 1 : 0) : lv < 16 ? 3 : 3 + (Math.random() < .5 ? 1 : 0);")
rep("const dishes = lv >= 8 ? Object.keys(DISH).filter(ok) : []; if (dishes.length && Math.random() < (lv >= 15 ? .35 : lv >= 11 ? .3 : .2)) add(pick1(dishes), 1);",
    "const dishes = ST.bep && ST.bep.lit ? Object.keys(DISH).filter(ok) : []; if (dishes.length && Math.random() < (lv >= 8 ? .34 : .25)) add(pickW(dishes, k => 1 / (1 + ((ST.bep.made || {})[k] || 0)) + .15), lv >= 12 && Math.random() < .3 ? 2 : 1);   /* v144: nhóm bếp rồi là có đơn món nấu, hay đặt món ít nấu */")
rep("for (let tries = 0; tries < 4 && items.length < nItems; tries++){ const s0 = sideOf(pickW(W.map(x => x[0]), c => W.find(x => x[0] === c)[1])); if (s0){ add(...s0); break; } } }",
    "let ns = 0; for (let tries = 0; tries < 6 && items.length < nItems && ns < (lv >= 16 ? 2 : 1); tries++){ const s0 = sideOf(pickW(W.map(x => x[0]), c => W.find(x => x[0] === c)[1])); if (s0 && !items.some(([x]) => x === s0[0])){ add(...s0); ns++; } } }")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
