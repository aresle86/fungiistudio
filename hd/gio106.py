#!/usr/bin/env python3
"""v106: giỏ lục bình chơi được. Trước: lục bình chung 4 chỗ với củi/lá/sâu, vịt ăn trước, 2 bụi/35 phút, phơi 6 tiếng,
không chỗ nào chỉ đường vớt → phơi → đan (khoảng 0–1 giỏ/ngày, việc cấp 16 cần 2 giỏ).
Nay từ cấp mở giỏ: lục bình có chỗ riêng dưới mương, 4 bụi/20 phút, vịt chỉ ăn khi máng trống, phơi 3 tiếng;
chữ bay đếm x/5, Ngoại dặn đem phơi, bong bóng ở ghế hiên, nút "Đem 5 bó ra nong phơi" trong bảng hiên nhà.
Chạy sau aud106.py:  python3 gio106.py live/v106a.html live/v106a.html"""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---- nguồn lục bình ----
rep("function oddDefs(){ return { sau:", "function oddDefs(){ let lbG = false; try { lbG = gioOn(); } catch (e) {} return { sau:")
rep("lucbinh: { lv: 2, max: 2, every: 35 * 60, name: 'Vớt lục bình' }",
    "lucbinh: { lv: 2, max: lbG ? 4 : 2, every: (lbG ? 20 : 35) * 60, name: 'Vớt lục bình' }")
rep("if (ST.odd.list.length >= 4){ ST.odd.acc[k] = 0; continue; }",
    "if (k !== 'lucbinh' && ST.odd.list.filter(o => o.k !== 'lucbinh').length >= 4){ ST.odd.acc[k] = 0; continue; }   /* lục bình dưới mương, không giành chỗ với việc trên bờ */")
rep("else if (o.k === 'lucbinh' && vitOn() && ST.vit.trough < ST.vit.n * VIT.trough){",
    "else if (o.k === 'lucbinh' && vitOn() && ST.vit.trough < (gioOn() && has('lucbinh') < 10 && gbUsed() < GB_CAP ? 1 : ST.vit.n * VIT.trough)){   /* mở giỏ rồi: vịt chỉ ăn lục bình khi máng trống */")
rep("ST.gb.lucbinh = (ST.gb.lucbinh || 0) + 1; txt = '+1 bó lục bình lên gác bếp';",
    "ST.gb.lucbinh = (ST.gb.lucbinh || 0) + 1; { const nl = has('lucbinh'); txt = nl >= GIO.need ? `+1 lục bình · đủ ${GIO.need} bó, đem phơi` : `+1 lục bình lên gác bếp · ${nl}/${GIO.need}`;"
    " sayOnce('lbgb', 'Lục bình vớt lên Ngoại cất gác bếp. Đủ năm bó thì đem ra nong phơi cho khô, Ngoại ngồi hiên đan giỏ cho con.', 'vui');"
    " if (nl >= GIO.need) sayOnce('lb5', 'Đủ năm bó lục bình rồi con. Ra hiên nhà chạm ghế đẩu của Ngoại, Ngoại trải ra nong phơi liền.', 'vui'); }")
rep("lucbinhkho: { name: 'Lục bình khô', unit: 'bó', lv: 15, in: { lucbinh: 5 }, t: 6 * 3600,",
    "lucbinhkho: { name: 'Lục bình khô', unit: 'bó', lv: 15, in: { lucbinh: 5 }, t: 3 * 3600,")

# ---- đem phơi từ hiên nhà ----
rep("const gio = {\n  put(){",
    "const gio = {\n  phoi(){ const N = ST.nong, own = ownObj('nong'), i = own ? N.trays.findIndex(t => !t) : -1;   /* trải 5 bó lục bình tươi ra nong trống */\n"
    "    if (has('lucbinh') < GIO.need) return say(`Cần ${GIO.need} bó lục bình tươi. Vớt dưới mương rồi Ngoại cất gác bếp cho.`, 'dan', { now: true });\n"
    "    if (i < 0) return toast(own ? 'Nong đang phơi đầy, chờ khô bớt rồi đem lục bình ra nghe con.' : 'Chưa có nong phơi con.', 'dan', { now: true });\n"
    "    nong.put(i, 'lucbinhkho'); if (!N.trays[i]) return; const P = PV[N.at]; if (P) flyTo(ICON.lucbinh, P.cx, .3, P.cz); toast(`Trải ${GIO.need} bó lục bình ra nong phơi rồi`, 'vui'); },\n"
    "  put(){")
rep("else if (a === 'gioput'){ gio.put(); }", "else if (a === 'gioput'){ gio.put(); } else if (a === 'giophoi'){ gio.phoi(); }")
rep("else if (gh === 'bub' && !g.on) gio.put();",
    "else if (gh === 'bub' && !g.on){ if (has('lucbinhkho') >= GIO.need) gio.put(); else gio.phoi(); }")
# bong bóng ghế hiên: đủ lục bình tươi và còn nong trống thì hiện bong bóng lục bình
rep("const show = (g.on && g.t <= 0) || (!g.on && has('lucbinhkho') >= GIO.need && (g.d !== dayKey() || g.n < GIO.day));",
    "const show = (g.on && g.t <= 0) || (!g.on && has('lucbinhkho') >= GIO.need && (g.d !== dayKey() || g.n < GIO.day)) || (!g.on && has('lucbinhkho') < GIO.need && has('lucbinh') >= GIO.need && ownObj('nong') && ST.nong.trays.some(t => !t));")
rep("bubIcon(b, g.on ? ICON.gio : ICON.lucbinhkho);", "bubIcon(b, g.on ? ICON.gio : has('lucbinhkho') >= GIO.need ? ICON.lucbinhkho : ICON.lucbinh);")

# ---- bảng hiên nhà: tươi + khô, nút đem phơi, đang phơi còn bao lâu ----
rep("""  else h += UX.hero(ICON.lucbinhkho, kho >= GIO.need ? 'Đủ lục bình khô rồi' : `Cần ${GIO.need} bó lục bình khô`, kho >= GIO.need ? 'Nhờ Ngoại đan một giỏ nghe' : 'Vớt lục bình rồi đem phơi nong', kho >= GIO.need ? '' : 'warn');
  h += UX.cta([g.on && g.t <= 0 ? UX.btn('giotake', 'Lấy giỏ', { g: 1, img: ICON.gio }) : !g.on ? UX.btn('gioput', 'Nhờ Ngoại đan một giỏ', { g: 1, img: ICON.gio, dis: left <= 0 || kho < GIO.need }) : '']);
  h += '<div class="uxs">' + UX.card('Lục bình khô', `${kho}/${GIO.need} <small>bó</small>`, UX.pips(ICON.lucbinhkho, Math.min(kho, GIO.need), GIO.need), kho >= GIO.need ? 'go' : '') + UX.card('Hôm nay', `${GIO.day - left}/${GIO.day} <small>giỏ</small>`, UX.pips(ICON.gio, GIO.day - left, GIO.day)) + '</div>';
  return h + UX.more('Cách đan giỏ', `Lục bình vớt dưới mương, sông cất lên gác bếp (khi vịt no). Phơi nong 5 lục bình ra 5 bó khô. Ngoại đan ${GIO.need} bó một giỏ, mỗi ngày tối đa ${GIO.day} giỏ.`); }""",
    """  else if (kho >= GIO.need) h += UX.hero(ICON.lucbinhkho, 'Đủ lục bình khô rồi', 'Nhờ Ngoại đan một giỏ nghe', '');
  else if (dry) h += UX.hero(ICON.lucbinh, 'Lục bình đang phơi nong', dry.t > 0 ? `Khô sau ${fmtT(dry.t)} nắng` : 'Khô rồi, ra nong lấy cất nghe con', dry.t > 0 ? '' : 'go', dry.t > 0 ? [1 - dry.t / (dry.T || PHOI.lucbinhkho.t), '#B8A070'] : undefined);
  else if (tuoi >= GIO.need) h += UX.hero(ICON.lucbinh, 'Đủ lục bình tươi rồi', 'Đem ra nong phơi cho khô, rồi Ngoại đan', 'go');
  else h += UX.hero(ICON.lucbinh, `Cần ${GIO.need} bó lục bình`, `Vớt lục bình dưới mương · còn thiếu ${GIO.need - tuoi} bó`, 'warn');
  const tray = ownObj('nong') ? ST.nong.trays.findIndex(t => !t) : -1, canPhoi = !g.on && kho < GIO.need && tuoi >= GIO.need;
  h += UX.cta([g.on && g.t <= 0 ? UX.btn('giotake', 'Lấy giỏ', { g: 1, img: ICON.gio }) : canPhoi ? UX.btn('giophoi', `Đem ${GIO.need} bó ra nong phơi`, { g: 1, img: ICON.lucbinh, dis: tray < 0, sub: tray < 0 ? 'nong đang đầy' : '' }) : !g.on ? UX.btn('gioput', 'Nhờ Ngoại đan một giỏ', { g: 1, img: ICON.gio, dis: left <= 0 || kho < GIO.need }) : '']);
  h += '<div class="uxs">' + UX.card('Lục bình tươi', `${tuoi}/${GIO.need} <small>bó</small>`, UX.pips(ICON.lucbinh, Math.min(tuoi, GIO.need), GIO.need), tuoi >= GIO.need && kho < GIO.need ? 'go' : '') + UX.card('Lục bình khô', `${kho}/${GIO.need} <small>bó</small>`, UX.pips(ICON.lucbinhkho, Math.min(kho, GIO.need), GIO.need), kho >= GIO.need ? 'go' : '') + '</div>';
  return h + UX.more('Cách đan giỏ', `Lục bình vớt dưới mương, sông Ngoại cất gác bếp (máng vịt trống thì vịt ăn trước). Đủ ${GIO.need} bó tươi đem phơi nong chừng ${PHOI.lucbinhkho.t / 3600} tiếng nắng ra ${GIO.need} bó khô. Ngoại đan ${GIO.need} bó khô một giỏ, mỗi ngày đan được ${GIO.day} giỏ, hôm nay đan ${GIO.day - left}.`); }""")
rep("function gioHTML(){ const g = ST.gio, left = g.d === dayKey() ? GIO.day - g.n : GIO.day, kho = has('lucbinhkho'); let h = '';",
    "function gioHTML(){ const g = ST.gio, left = g.d === dayKey() ? GIO.day - g.n : GIO.day, kho = has('lucbinhkho'), tuoi = has('lucbinh'), dry = ST.nong && ST.nong.trays && ST.nong.trays.find(t => t && t.k === 'lucbinhkho'); let h = '';")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
