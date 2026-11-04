#!/usr/bin/env python3
"""v107 đợt 1: lục bình, khô, giỏ để dưới hiên (gác bếp đầy củi chặn cả chuỗi giỏ: bot 0 giỏ); cho vịt ăn 1 bó = 4 phần;
bỏ số cấp tương lai ở vòng Cỏ rậm; chữ ≥12px, vùng chạm ≥44px, chữ nhạt đậm hơn.
Chạy trên nguồn v106:  python3 fix107.py live/vuon3d.html live/v107a.html"""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---- lục bình, lục bình khô, giỏ: để dưới hiên, không giành chỗ gác bếp ----
rep("const GB_CAP = 20, CUI_PRICE = 3, gbUsed = () => Object.values(ST.gb || {}).reduce((a, n) => a + (n > 0 ? n : 0), 0);",
    "let GB_CAP = 20; const GBX_MAX = 3, gbxCost = () => 150 + 100 * ((ST && ST.gbx) || 0), CUI_CAP = 20, CUI_PRICE = 3, HIEN = { lucbinh: 1, lucbinhkho: 1, gio: 1, cui: 1 }, gbUsed = () => Object.entries(ST.gb || {}).reduce((a, [k, n]) => a + (n > 0 && !HIEN[k] ? n : 0), 0);   /* gác bếp 20 chỗ, mua thêm tối đa 3 kệ (+10 mỗi kệ); củi chất dưới chái (tối đa CUI_CAP), lục bình, giỏ để dưới hiên: không tính chỗ gác bếp */")
# củi: đống củi riêng, không lấp gác bếp
rep("if (ST.xu >= CUI_PRICE * n && gbUsed() + n <= GB_CAP){ ST.xu -= CUI_PRICE * n; ST.gb.cui = (ST.gb.cui || 0) + n;",
    "if (ST.xu >= CUI_PRICE * n && has('cui') + n <= CUI_CAP){ ST.xu -= CUI_PRICE * n; ST.gb.cui = (ST.gb.cui || 0) + n;")
rep("else if (gbUsed() + n > GB_CAP) toast('Gác bếp hết chỗ để củi rồi con.', 'dan');", "else if (has('cui') + n > CUI_CAP) toast('Đống củi đầy rồi con, nấu bớt rồi mua thêm.', 'dan');")
rep("else if (o.k === 'cui'){ ST.gb = ST.gb || {}; if (gbUsed() < GB_CAP){ ST.gb.cui = (ST.gb.cui || 0) + 1; txt = '+1 bó củi';",
    "else if (o.k === 'cui'){ ST.gb = ST.gb || {}; if (has('cui') < CUI_CAP){ ST.gb.cui = (ST.gb.cui || 0) + 1; txt = '+1 bó củi';")
rep("else txt = 'Gác bếp hết chỗ';", "else txt = 'Đống củi đầy rồi';")
rep("else if (d === 'cui'){ ST.gb = ST.gb || {}; ST.gb.cui = (ST.gb.cui || 0) + 1; }",
    "else if (d === 'cui'){ ST.gb = ST.gb || {}; if (has('cui') < CUI_CAP) ST.gb.cui = (ST.gb.cui || 0) + 1; }")
rep("else if (k === 'cui'){ ST.gb = ST.gb || {}; ST.gb.cui = (ST.gb.cui || 0) + n; ST.gb.duong = (ST.gb.duong || 0) + 1; }",
    "else if (k === 'cui'){ ST.gb = ST.gb || {}; ST.gb.cui = Math.min(CUI_CAP, (ST.gb.cui || 0) + n); if (gbUsed() < GB_CAP) ST.gb.duong = (ST.gb.duong || 0) + 1; }")
# thưởng việc: không đẩy gác bếp, đống củi quá sức chứa; phần dư đổi xu
rep("else { const kk = x.rw[0]; STORE(kk)[kk] = (STORE(kk)[kk] || 0) + v; oth.push(",
    "else { const kk = x.rw[0], S0 = STORE(kk), room = kk === 'cui' ? CUI_CAP - (S0.cui || 0) : S0 === ST.gb && !HIEN[kk] ? GB_CAP - gbUsed() : v, put = Math.max(0, Math.min(v, room)); S0[kk] = (S0[kk] || 0) + put; if (put < v) xu += (v - put) * 3; oth.push(")
# trang Kho: gác bếp riêng, chái bếp + dưới hiên riêng
rep("const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0); if (gbi.length) h += `<div class=\"bkhn\" style=\"margin-top:12px;color:#6B4529\">Gác bếp · ${gbUsed()}/${GB_CAP}</div>` + gbi.map(",
    "const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && !HIEN[k]); if (gbi.length) h += `<div class=\"bkhn\" style=\"margin-top:12px;color:#6B4529\">Gác bếp · ${gbUsed()}/${GB_CAP}</div>` + gbi.map(")
rep("h += '</div>'; return full ? h + pgKhoCap() : h; }",
    "if (gbi.length && (ST.gbx || 0) < GBX_MAX) h += `<div class=\"acts\"><button class=\"btn\" data-b=\"gbx\" ${ST.xu < gbxCost() ? 'disabled' : ''}>Thêm kệ gác bếp · ${gbxCost()} xu</button></div><div class=\"bkhn\" style=\"font-size:17px;color:#8A5D3B\">Mỗi kệ tre chứa thêm 10 món khô, món nấu.</div>`;\n  const hie = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && HIEN[k]); if (hie.length) h += `<div class=\"bkhn\" style=\"margin-top:12px;color:#6B4529\">Chái bếp, dưới hiên</div>` + hie.map(([k, n]) => `<div class=\"krow\"><img src=\"${ICON[k]}\" alt=\"\"><span class=\"n\">${k === 'cui' ? `Củi · ${n}/${CUI_CAP}` : (GD(k) || { name: k }).name}</span><span class=\"q\" style=\"color:#9A6E12\">${n}</span></div>`).join('');\n  h += '</div>'; return full ? h + pgKhoCap() : h; }")
rep("has('lucbinh') < 10 && gbUsed() < GB_CAP", "has('lucbinh') < 10", 2)
rep("const on = PHOI[t.k].out || 1; if (gbUsed() + on > GB_CAP){", "const on = PHOI[t.k].out || 1; if (!HIEN[t.k] && gbUsed() + on > GB_CAP){")
rep("take(){ const g = ST.gio; if (!g.on || g.t > 0) return; if (gbUsed() >= GB_CAP) return toast('Gác bếp hết chỗ rồi con.', 'lo', { now: true });",
    "take(){ const g = ST.gio; if (!g.on || g.t > 0) return;")
rep("sayOnce('lbgb', 'Lục bình vớt lên Ngoại cất gác bếp.", "sayOnce('lbgb', 'Lục bình vớt lên Ngoại để dưới hiên cho ráo.")
rep("`+1 lục bình lên gác bếp · ${nl}/${GIO.need}`", "`+1 lục bình · ${nl}/${GIO.need}`")
rep("Lục bình vớt dưới mương, sông Ngoại cất gác bếp (máng vịt trống thì vịt ăn trước).", "Lục bình vớt dưới mương, sông Ngoại để dưới hiên (máng vịt trống thì vịt ăn trước).")
rep("Vớt dưới mương rồi Ngoại cất gác bếp cho.", "Vớt dưới mương rồi Ngoại để dưới hiên cho.")

# ---- vịt: 1 bó rau muống = 4 phần (12 vịt ăn ít bó hơn) ----
rep("cam: 6, rm: 2, nestMax: 3", "cam: 6, rm: 4, nestMax: 3")

# ---- không nói số cấp tương lai ----
rep("Đủ ${bedCap()} liếp rồi · cấp ${bedNext()} đắp thêm được", "Vườn đủ ${bedCap()} liếp chăm rồi con")

# ---- chữ nhạt đậm hơn (#A07A55 3,6:1 → #8A5D3B), số trong kho đậm hơn ----
rep("#A07A55", "#8A5D3B", 7)
rep('<span class="q" style="color:#6E9F57">', '<span class="q" style="color:#4F7D44">')
rep('<span class="q" style="color:#C9952A">', '<span class="q" style="color:#9A6E12">')
rep(".tkc .rw{display:inline-flex;align-items:center;gap:2px;font-size:13px;font-weight:800;color:#C9952A;flex:none}",
    ".tkc .rw{display:inline-flex;align-items:center;gap:2px;font-size:13px;font-weight:800;color:#9A6E12;flex:none}")

# ---- đổi công: "hái giùm" khi chưa có công (vườn bạn chín hết thì trước đây kẹt cứng) ----
rep("if (fr && !repay && !(VISIT.cong > 0)) return say(`Tưới giùm ${VISIT.owner} một liếp trước, rồi mới hái ké một món nghe.`, 'dan', { now: true });",
    "if (fr && !repay && !(VISIT.cong > 0)){ if ((VISIT.loot.help || 0) >= DOICONG) return say(`Hôm nay con phụ ${VISIT.owner} nhiều rồi, mai qua nữa nghe.`, 'vui', { now: true });   /* hái giùm: rau vô kho chủ vườn, mình được 1 công */\n"
    "      VISIT.busy = 1; try { const r = await vact('help', { id, k: k0, n: Math.max(1, Math.round(c.yield)) }); VISIT.busy = 0; if (!r || !r.ok) return toast('Hôm nay con phụ vườn này đủ rồi.', 'vui', { now: true }); } catch (e) { VISIT.busy = 0; return toast('Mạng chập chờn quá, chưa hái giùm được con.', 'lo', { now: true }); }\n"
    "      VISIT.loot.help = (VISIT.loot.help || 0) + 1; VISIT.loot.xp += 2; VISIT.cong = (VISIT.cong || 0) + 1; p.g = c.tree ? c.grow - c.re : 0; if (!c.tree && c.kind !== 'trellis') p.crop = null; refreshPlot(id);\n"
    "      floatAt(v.cx, .6, v.cz, `Hái giùm ${VISIT.owner} · được hái ké 1 món`, '#9fd36a'); sfx('cut', 4); sayOnce('haigium', `Hái giùm thì rau vô kho của ${VISIT.owner}. Giờ con chạm liếp chín khác, hái ké một món đem về nghe.`, 'vui'); visitPersist(); visitInfo(); return; }")
rep("Ở xóm mình đổi công: tưới giùm một liếp thì được hái ké một món đem về.",
    "Ở xóm mình đổi công: tưới giùm hay hái giùm một liếp thì được hái ké một món đem về.")
rep("Công đổi được ${VISIT.cong || 0} · tưới giùm ${VISIT.loot.water}/${DOICONG} · hái ké còn ${VISIT.left}",
    "Công đổi được ${VISIT.cong || 0} · đã phụ ${VISIT.loot.water + (VISIT.loot.help || 0)} liếp · hái ké còn ${VISIT.left}")
rep("{ name: e.name || 'Hàng xóm', water: 0, steal: [], gift: [], ask: 0, visit: 0 }",
    "{ name: e.name || 'Hàng xóm', water: 0, steal: [], help: [], gift: [], ask: 0, visit: 0 }")
rep("else if (e.kind === 'gift'){",
    "else if (e.kind === 'help'){ const p = ST.plots[pl.id]; if (p && p.crop === pl.k && ripe(p) && kCap() - kUsed() >= Math.max(1, harvestN(p) - (p.stolen || 0))){ try { act.harvest(pl.id); b.help.push(pl.k); } catch (er) {} } }   /* hàng xóm hái giùm: hái thật cho mình, kho đầy thì cây đứng chờ */\n    else if (e.kind === 'gift'){")
rep("if (b.ask) bits.push('xin con ít hạt giống');",
    "if (b.help.length) bits.push(`hái giùm ${b.help.map(k => CROPS[k].name.toLowerCase()).join(', ')} bỏ vô kho cho mình`); if (b.ask) bits.push('xin con ít hạt giống');")
rep("${b.steal.length ? ' Ra bến chèo qua đòi nợ đi con!' : b.ask",
    "${b.steal.length > b.water + b.help.length ? ' Ra bến chèo qua đòi nợ đi con!' : b.ask")
rep("TS.push([t, b.steal.length ? 'lo' : 'vui']); }", "TS.push([t, b.steal.length > b.water + b.help.length ? 'lo' : 'vui']); }")

# ---- hố ủ: cho thấy đất mệt làm hụt sản lượng; "bỏ rau dư" (game không có rau hư) thành "hốt phân chuồng" ----
rep("ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0;",
    "ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0;"
    " if (!c.tree){ const lost = Math.round(c.yield * .45 * (1 - p.soil)); if (lost >= 1){ const v0 = PV[id], hh = c.h; setTimeout(() => floatAt(v0.cx, hh * .6 + .35, v0.cz, `Đất mệt · hụt ${lost} ${c.unit}`, '#F0B27A'), 550);"
    " sayOnce('datmet', ownObj('ho') ? 'Đất trồng hoài một thứ là mệt, ra ít bó hơn. Bón phân ủ hay trồng xen thứ khác thì đất lại sức con.' : 'Đất trồng hoài một thứ là mệt, ra ít bó hơn. Trồng xen thứ khác cho đất nghỉ nghe con.', 'dan'); } }   /* đất mệt: nói ra để người chơi thấy giá trị của phân ủ */")
rep("function hoAdd(n, x, z){",
    "const PHANT = 6 * 3600e3;   /* chuồng gà vịt: 6 tiếng ra 1 phần phân, tích tối đa 4 */\n"
    "function phanCh(){ const H = ST.ho; let on = false; try { on = gaOn() || vitOn(); } catch (e) {} if (!H || !on) return 0; if (!H.pct) H.pct = Date.now(); return Math.min(4, Math.floor((Date.now() - H.pct) / PHANT)); }\n"
    "function hoPhan(){ const H = ST.ho, a = phanCh(), n = Math.min(a, HO.cap - H.mat); if (n < 1) return toast(a ? 'Hố ủ đầy rồi con.' : 'Chuồng chưa có phân, chừng sáu tiếng hốt một lần.', 'dan', { now: true });\n"
    "  if (!hoAdd(n)) return; H.pct = n >= a ? Date.now() : H.pct + n * PHANT; toast(`+${n} phần phân chuồng vô hố`, 'vui'); sfx('pick'); save(); hud(); }\n"
    "function hoAdd(n, x, z){")
rep("'Quét lá, vớt lục bình, bỏ rau dư vô hố'", "'Quét lá, vớt lục bình, hốt phân chuồng gà vịt bỏ vô hố'")
rep("UX.btn('horau', 'Bỏ 1 rau dư', { img: ICON.cai, dis: !hoRoom() })",
    "(phanOn() ? UX.btn('hophan', 'Hốt phân chuồng', { img: ICON.phan, dis: phanCh() < 1 || !hoRoom(), sub: phanCh() ? `${phanCh()} phần` : 'chưa có' }) : '')")
rep("function phanCh(){", "const phanOn = () => { try { return gaOn() || vitOn(); } catch (e) { return false; } };\nfunction phanCh(){")
rep("Quét lá rụng +2 phần, vớt lục bình +1 phần (vịt no rồi thì lục bình vô hố), rau dư trong kho +1 phần. Đủ ${HO.need} phần thì Ngoại ủ, một ngày ra một bao. Bón một bao: đất liếp +0,3.",
    "Quét lá rụng +2 phần, vớt lục bình +1 phần (vịt no rồi thì lục bình vô hố), chuồng gà vịt sáu tiếng hốt được 1 phần phân. Đủ ${HO.need} phần thì Ngoại ủ, một ngày ra một bao. Liếp trồng hoài là đất mệt, ra ít bó; bón một bao thì vụ sau ra thêm chừng một bó.")
rep("else if (a === 'horau'){ hoRau(); }", "else if (a === 'horau'){ hoRau(); } else if (a === 'hophan'){ hoPhan(); }")

# ---- đồ muối đáng công hơn (khạp chiếm chỗ 12–24 tiếng), đơn không lặp món đang có trong đơn khác ----
# giá giữ nguyên, tăng số lượng mỗi mẻ: một khạp 4 cải ra 2 hũ dưa; khạp hột vịt ngâm 6 trứng ra 6 hột (nhiều món hơn để giao cho nhiều người)
rep("dacai: { name: 'Dưa cải muối', unit: 'hũ', lv: 8, in: { cai: 4, muoi: 1 }, t: 12 * 3600, out: 1, sell: 65,",
    "dacai: { name: 'Dưa cải muối', unit: 'hũ', lv: 8, in: { cai: 4, muoi: 1 }, t: 12 * 3600, out: 2, sell: 65,")
rep("hotvit: { name: 'Hột vịt muối', unit: 'hột', lv: 8, in: { trungvit: 4, muoi: 1 }, t: 24 * 3600, out: 4, sell: 42,",
    "hotvit: { name: 'Hột vịt muối', unit: 'hột', lv: 8, in: { trungvit: 6, muoi: 1 }, t: 24 * 3600, out: 6, sell: 42,")
rep("  const nk = Math.min(pool.length, lv < 5",
    "  { const open = new Set(((ST.ord && ST.ord.list) || []).flatMap(o => o.items.map(([k2]) => k2))); const fresh = pool.filter(k => !open.has(k)); if (fresh.length) pool.splice(0, pool.length, ...fresh); }   /* món đang nằm trong đơn khác thì không đặt nữa */\n  const nk = Math.min(pool.length, lv < 5")

# ---- nong phơi: chế độ giờ cố định ban đêm thì nong không bao giờ khô → giờ cố định coi như có nắng ----
rep("for (const t of N.trays) if (t && t.t > 0 && (sun || t.fast)) t.t = Math.max(0, t.t - dt); }",
    "for (const t of N.trays) if (t && t.t > 0 && (sun || t.fast || ST.tm === 'fixed' || ST.tm === 'day')) t.t = Math.max(0, t.t - dt); }")

# ---- luân canh: vòng gieo đánh dấu thứ vừa trồng ở liếp này khi đất mệt ----
rep("body = '<div class=\"rgs\">' + ks.map(k => { const c = CROPS[k], n = ST.seeds[k] || 0, poor = !n && ST.xu < c.seed; return `<button class=\"rgi${poor ? ' poor' : ''}${k === ST.lastSeed ? ' last' : ''}\" data-k=\"${k}\" aria-label=\"${c.name}: ${n ? n + ' bao' : c.seed + ' xu'}\"><img src=\"${ICON[k]}\" alt=\"\" draggable=\"false\">",
    "const p0 = ST.plots[id] || {}, tired = p0.soil < .6 && p0.last; body = '<div class=\"rgs\">' + ks.map(k => { const c = CROPS[k], n = ST.seeds[k] || 0, poor = !n && ST.xu < c.seed, tk = tired === k; return `<button class=\"rgi${poor ? ' poor' : ''}${k === ST.lastSeed ? ' last' : ''}${tk ? ' tired' : ''}\" data-k=\"${k}\" aria-label=\"${c.name}: ${n ? n + ' bao' : c.seed + ' xu'}${tk ? ', đất mệt với thứ này' : ''}\">${tk ? '<i class=\"rgtd\">đất mệt</i>' : ''}<img src=\"${ICON[k]}\" alt=\"\" draggable=\"false\">")
rep("hint = ks.length > 0 ? 'Chạm để gieo liếp này · kéo xuống qua nhiều liếp' : '';",
    "hint = ks.length > 0 ? (tired && ks.includes(tired) ? `Liếp này trồng ${CROPS[tired].name.toLowerCase()} hoài nên đất mệt · gieo thứ khác cho đất nghỉ` : 'Chạm để gieo liếp này · kéo xuống qua nhiều liếp') : '';")

rep("else if (a === 'lu'){ const c = luCost();",
    "else if (a === 'gbx'){ const c = gbxCost(); if ((ST.gbx || 0) < GBX_MAX && ST.xu >= c){ ST.xu -= c; ST.gbx = (ST.gbx || 0) + 1; GB_CAP = 20 + 10 * ST.gbx; save(); hud(); toast(`Đóng thêm kệ tre rồi, gác bếp chứa được ${GB_CAP} món.`, 'vui'); } }\n  else if (a === 'lu'){ const c = luCost();")

# ---- trời trong vườn: chỉ còn "Giờ trong vườn" và "Luôn ban ngày"; bỏ "Theo giờ thật"; chỉnh tay giờ chỉ khi ?dev ----
rep("${[['game', 'Giờ trong vườn'], ['real', 'Theo giờ thật'], ['day', 'Luôn ban ngày']].map(",
    "${[['game', 'Giờ trong vườn'], ['day', 'Luôn ban ngày']].map(")
rep("<div class=\"meta\">${ST.tm === 'game' ? 'Một ngày trong vườn chừng 40 phút: sáng, trưa, chiều, tối đổi liền liền. Quà, việc, ghe chợ nổi vẫn tính theo ngày thật.' : ST.tm === 'real' ? 'Trời trong vườn y như ngoài đời, chơi buổi tối là thấy vườn ban đêm.' : 'Trời luôn sáng, dễ nhìn. Nong phơi lúc nào cũng có nắng.'}</div>`;",
    "<div class=\"meta\">${ST.tm === 'day' ? 'Trời luôn sáng, dễ nhìn. Nong phơi lúc nào cũng có nắng.' : 'Một ngày trong vườn chừng 40 phút: sáng, trưa, chiều, tối đổi liền liền. Quà, việc, ghe chợ nổi vẫn tính theo ngày thật.'}</div>`;")
rep("h += `<details class=\"uxm\"><summary>Chỉnh tay giờ trong vườn</summary>",
    "if (/[?&]dev\\b/.test(location.search)) h += `<details class=\"uxm\"><summary>Chỉnh tay giờ trong vườn (dev)</summary>")
rep("if (ST.tm == null) ST.tm = ST.realTime === false ? 'fixed' : 'game';",
    "GB_CAP = 20 + 10 * (ST.gbx || 0); if (ST.tm == null) ST.tm = 'game'; if (ST.tm === 'real' || (ST.tm === 'fixed' && !/[?&]dev\\b/.test(location.search))){ ST.tm = 'game'; ST.realTime = true; }   /* v107: bỏ chế độ theo giờ thật và giờ cố định (giờ cố định chỉ còn khi ?dev) */")

# ---- chữ ≥12px, vùng chạm ≥44px ----
CSS = """
/* v107: chữ tối thiểu 12px, vùng chạm tối thiểu 44px (nút giữ hình cũ, vùng chạm nới ra) */
.nxq small{font-size:12px!important}.nxq .nqd{font-size:12px!important}.fcd .ftag{font-size:12px!important}.fcd small,.fcd span{font-size:12px}
.btn small{font-size:12px!important}
@media (max-width:560px){ .tg{font-size:12px!important} }
#shX{position:relative}#shX::before,.bkx::before{content:"";position:absolute;inset:-5px;border-radius:50%}
.tkc .tkgo{min-height:44px;padding-top:0;padding-bottom:0;display:inline-flex;align-items:center}
.rgsan{min-height:44px;display:flex;align-items:center;justify-content:center}
.sg{min-height:44px}
.btn.s1{min-width:44px}
.rgi{position:relative}.rgi.tired{opacity:.72}.rgi .rgtd{position:absolute;left:50%;top:-4px;transform:translateX(-50%) rotate(-6deg);font:400 11px var(--f-game);font-style:normal;color:#FBF7EE;background:#B0603A;border-radius:8px;padding:2px 7px;white-space:nowrap;z-index:1}
"""
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
