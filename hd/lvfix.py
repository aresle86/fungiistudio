#!/usr/bin/env python3
"""v102: nhịp cấp mới — XP cần, dời mở khoá (lò sấy 11, hố ủ 12, lò ấp 14, giỏ 15, ao 16), việc lên cấp dạy đúng thứ vừa mở,
thẻ lên cấp đủ mục, Ngoại dẫn tới thứ chính, giữ đồ cho người chơi cũ."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---------- XP cần ----------
rep("const XPN = [0, 0, 10, 30, 80, 190, 310, 450, 610, 840, 1060, 1320, 1620, 1960, 2340, 2760, 3220, 3720, 4260, 4840, 5460];",
    "const XPN = [0, 0, 10, 30, 80, 190, 310, 800, 1800, 3000, 4300, 5800, 7500, 9300, 11200, 13300, 15500, 18000, 20500, 23500, 26500];   /* v102: đo bằng bản chơi tự động, cấp 20 khoảng ngày 40 với người chơi chăm */")

# ---------- dời mở khoá ----------
rep("  say: { name: 'lò sấy', title: 'Lò sấy', lv: 10", "  say: { name: 'lò sấy', title: 'Lò sấy', lv: 11")
rep("  ho: { name: 'hố ủ phân', title: 'Hố ủ phân', lv: 8", "  ho: { name: 'hố ủ phân', title: 'Hố ủ phân', lv: 12")
rep("const LO = { lv: 9", "const LO = { lv: 14")
rep("const GIO = { lv: 10", "const GIO = { lv: 15")
rep("ao: { name: 'ao cá', title: 'Ao cá', lv: 9", "ao: { name: 'ao cá', title: 'Ao cá', lv: 16")
rep("lucbinhkho: { name: 'Lục bình khô', unit: 'bó', lv: 10,", "lucbinhkho: { name: 'Lục bình khô', unit: 'bó', lv: 15,")
rep("story: 'Cọng lục bình phơi khô để đan giỏ, đan đệm. Cấp 10 Ngoại dạy con đan.' }", "story: 'Cọng lục bình phơi khô để đan giỏ, đan đệm. Ngoại ngồi hiên đan cho con coi.' }")
rep("gio: { name: 'Giỏ lục bình', unit: 'cái', lv: 10,", "gio: { name: 'Giỏ lục bình', unit: 'cái', lv: 15,")
rep(" Lò ấp trấu cạnh chuồng vịt cũng dùng được rồi.", "")
# người chơi cũ đã tới cấp mở cũ thì giữ quyền dùng
rep("objOn = k => (ST.lv || 1) >= OBJD[k].lv;", "objOn = k => (ST.lv || 1) >= OBJD[k].lv || !!(ST[k] && ST[k].own) || !!(ST.keep || {})[k];")
rep("const loOn = () => (ST.lv || 1) >= LO.lv && !!ST.vit.fixed;", "const loOn = () => ((ST.lv || 1) >= LO.lv || !!(ST.keep || {}).lo) && !!ST.vit.fixed;")
rep("const gioOn = () => (ST.lv || 1) >= GIO.lv;", "const gioOn = () => (ST.lv || 1) >= GIO.lv || !!(ST.keep || {}).gio;")
rep("function aoBuy(id){ const D = BIGD.ao; if ((ST.lv || 1) < D.lv ||", "function aoBuy(id){ const D = BIGD.ao; if (((ST.lv || 1) < D.lv && !(ST.keep || {}).ao) ||")
rep("if ((ST.lv || 1) >= BIGD.ao.lv && !(ST.big.ao && ST.big.ao.own)){", "if (((ST.lv || 1) >= BIGD.ao.lv || (ST.keep || {}).ao) && !(ST.big.ao && ST.big.ao.own)){")
rep("put(i, k){ const N = ST.nong, d = PHOI[k]; if (!d || N.trays[i] || (ST.lv || 1) < d.lv ||",
    "put(i, k){ const N = ST.nong, d = PHOI[k]; if (!d || N.trays[i] || ((ST.lv || 1) < d.lv && !(k === 'lucbinhkho' && (ST.keep || {}).gio)) ||")

# ---------- đếm thêm cho việc lên cấp ----------
rep("gainXP(2); save(); hud(); }\nfunction hoRau", "ST.bonN = (ST.bonN || 0) + 1; gainXP(2); save(); hud(); }\nfunction hoRau")
rep("ST.inv.trungvit = (ST.inv.trungvit || 0) + n; v.eggs = 0;", "ST.inv.trungvit = (ST.inv.trungvit || 0) + n; v.eggs = 0; ST.vitEggN = (ST.vitEggN || 0) + n;")
rep("function tbTake(){ const B = ST.tb; if (!B || !B.done || loLeft() > 0) return;", "function tbTake(){ const B = ST.tb; if (!B || !B.done || loLeft() > 0) return; ST.tbN = (ST.tbN || 0) + 1;")

# ---------- việc lên cấp: dạy đúng thứ vừa mở ----------
rep("  7: { t: 'pay', xu: 100, ic: 'tre', txt: 'Cắm giàn tre', how: 'Cắm giàn tre trên liếp cho mồng tơi leo' },",
    "  7: { t: 'goal', txt: 'Dựng chuồng vịt, lượm trứng vịt', how: 'Lượm tre, rơm dựng lại chuồng vịt bên mé mương. Cho vịt ăn rồi lượm hai trứng', goals: [['Dựng chuồng vịt', () => ST.vit && ST.vit.fixed ? 1 : 0, 1], ['Lượm 2 trứng vịt', () => ST.vitEggN || 0, 2]] },")
rep("  9: { t: 'goal', txt: 'Giao 5 đơn hàng', how: 'Giao đủ 5 đơn cho hàng xóm', goals: [['Giao 5 đơn', () => (ST.ord && ST.ord.done) || 0, 5]] },",
    "  9: { t: 'goal', txt: 'Muối khạp dưa, trồng gốc chuối', how: 'Mua khạp ở chợ, muối một khạp dưa cải. Trồng gốc chuối ở góc cây trái bên hông nhà', goals: [['Muối xong 1 khạp', () => (ST.khap && ST.khap.done) || 0, 1], ['Trồng 1 gốc chuối', () => PLOTS.some(P => ST.plots[P.id] && ST.plots[P.id].crop === 'chuoi') ? 1 : 0, 1]] },")
rep("  10: { t: 'pay', xu: 200, txt: 'Đắp bờ mé sông chống lở', how: 'Đóng cừ tre, đắp đất dọc mé sông cho mùa nước khỏi lở bờ.' },",
    "  10: { t: 'goal', txt: 'Khai hoang mé sông, câu con cá đầu', how: 'Khai hoang hai ô đất mé sông, rồi ra bến thả câu một con. Xong Ngoại nhờ xóm đắp bờ cho', goals: [['Khai hoang 2 ô mé sông', () => PLOTS.filter(P => P.bai && P.zone === 'song' && landSt(P.id) === 'own').length, 2], ['Câu 1 con cá', () => Object.keys(ST.fishLog || {}).filter(k => FISHK[k]).length, 1]] },")
rep("  13: { t: 'goal', txt: 'Phơi đủ 10 mẻ đồ khô', how: 'Phơi nong hay sấy lò đủ 10 mẻ', goals: [",
    "  13: { t: 'goal', txt: 'Bón phân, phơi sấy đủ 10 mẻ', how: 'Ủ phân ở hố rồi bón một liếp. Phơi nong hay sấy lò đủ 10 mẻ', goals: [['Bón phân 1 liếp', () => ST.bonN || 0, 1], ")
rep("  14: { t: 'goal', txt: 'Giao 3 đơn ghe chợ nổi', how: 'Sáng nào ghe bẹo cũng ghé bến đặt hàng, giao đủ 3 lần', goals: [['Giao 3 đơn ghe bẹo', () => (ST.ghe && ST.ghe.done) || 0, 3]] },",
    "  14: { t: 'goal', txt: 'Làm đẹp vườn, nâng nong khạp', how: 'Mua một món trang trí ở chợ đặt trong vườn. Nâng giàn nong hai tầng hay thêm khạp', goals: [['Mua 1 món trang trí', () => (((ST.dc && ST.dc.items) || []).length || Object.keys((ST.dc && ST.dc.own) || {}).length || Object.values((ST.dc && ST.dc.bag) || {}).some(n => n > 0)) ? 1 : 0, 1], ['Nâng nong hay khạp', () => ((ST.nong && ST.nong.trays && ST.nong.trays.length > NONG.n) || (ST.khap && ST.khap.jars && ST.khap.jars.length > 2)) ? 1 : 0, 1]] },")
rep("  16: { t: 'goal', txt: 'Nấu 8 nồi món cá', how: 'Câu cá về, nấu canh chua, kho tộ, nướng trui trên bếp Ngoại', goals: [",
    "  16: { t: 'goal', txt: 'Đan giỏ, nấu 8 nồi món cá', how: 'Phơi lục bình khô cho Ngoại đan hai cái giỏ. Câu cá về nấu canh chua, kho tộ, nướng trui', goals: [['Đan 2 giỏ lục bình', () => (ST.gio && ST.gio.done) || 0, 2], ")
rep("  17: { t: 'goal', txt: 'Hái 5 vụ cây trái', how: 'Chuối, ổi, khế, xoài, dừa: hái đủ 5 vụ', goals: [",
    "  17: { t: 'goal', txt: 'Đào ao cá, hái 5 vụ trái', how: 'Đào ao cá trên bốn ô đất trống sát nhau. Chuối, ổi, khế, xoài, dừa: hái đủ 5 vụ', goals: [['Đào ao cá', () => ST.big && ST.big.ao && ST.big.ao.own ? 1 : 0, 1], ")
rep("  20: { t: 'goal', txt: 'Về vườn đủ 30 ngày', how: 'Ngày nào cũng về vườn với Ngoại, đủ 30 ngày Ngoại tổng kết một năm', goals: [['Ngày về vườn', () => ST.daysN || 0, 30]] },",
    "  20: { t: 'goal', txt: 'Chèo tam bản đặt lờ', how: 'Đóng xong ghe tam bản thì chèo ra sông đặt lờ, sáng ra lấy cá', goals: [['Lấy lờ 1 lần', () => ST.tbN || 0, 1]] },")
rep("  11: { t: 'goal', txt: 'Trồng đủ 3 loại cây trái', how: 'Trồng 3 gốc cây trái ở góc vườn bên hông nhà hay trên đất mé sông', goals: [['Trồng 3 cây trái', nTrees, 3]] } };",
    "  11: { t: 'goal', txt: 'Giao hàng cho ghe bẹo', how: 'Sáng nào ghe bẹo cũng ghé bến. Giao một đơn ghe, giao thêm đơn cho hàng xóm', goals: [['Giao 1 đơn ghe bẹo', () => (ST.ghe && ST.ghe.done) || 0, 1], ['Giao 8 đơn nhà bên', () => (ST.ord && ST.ord.done) || 0, 8]] } };")

# ---------- thẻ lên cấp ----------
i = s.index("const LVFEAT = {"); j = s.index("};", i) + 2
s = s[:i] + ("const LVFEAT = { 2: [['la', 'Việc lặt vặt']], 3: [['cho', 'Đơn nhà bên'], ['sau', 'Bắt sâu'], ['vuon', 'Ghé vườn bạn']], 4: [['trungchien', 'Bếp Ngoại'], ['cui', 'Nhặt củi'], ['cuoc', 'Góc vườn mới']], 5: [['mai', 'Mua gà, ấp trứng']], 6: [['vitmai', 'Chuồng vịt'], ['ft_vusua', 'Cây cổ tích lạ']],\n"
  "  7: [['nong', 'Nong phơi'], ['cuoc', 'Bãi hông nhà · Sửa vườn']], 8: [['khap', 'Khạp muối'], ['chuoi', 'Cây trái đầu tiên'], ['bu_phuong', 'Bướm về vườn']], 9: [['cancau', 'Câu cá'], ['caloc', 'Mé sông'], ['caro', 'Khạp nuôi cá']], 10: [['ghe', 'Ghe chợ nổi']], 11: [['say', 'Lò sấy'], ['xoaisay', 'Sau nhà 10 ô']], 12: [['ho', 'Hố ủ phân'], ['mutdua', 'Món Tết']],\n"
  "  13: [['dc_cong_gach', 'Trang trí vườn'], ['nong', 'Giàn nong hai tầng, thêm khạp']], 14: [['vitcon', 'Lò ấp vịt']], 15: [['gio', 'Giỏ lục bình'], ['cuoc', 'Mái lá mới']], 16: [['caro', 'Đào ao cá']], 17: [['matong', 'Nuôi ong lấy mật'], ['chuoimat', 'Món mật ong']], 18: [['cuoc', 'Sửa sang nhà cửa']], 19: [['tamban', 'Ghe tam bản đặt lờ']], 20: [['so', 'Một năm ở vườn Ngoại']] };") + s[j:]

# ---------- Ngoại dẫn tới thứ chính khi lên cấp ----------
rep("if (LVQ.length) say(LVQ[0][0], LVQ[0][1], { idle: true }); LVQ.length = 0; }",
    "if (!LVQ.length && LVINTRO[n]){ const [t, at] = LVINTRO[n]; lvSay(t, 'vui'); if (at) setTimeout(() => { if (!VISIT) camTo(new T.Vector3(at[0], .3, at[1]), Math.max(cam.zoom, DEFZ() * 1.1)); }, 1600); } if (LVQ.length) say(LVQ[0][0], LVQ[0][1], { idle: true }); LVQ.length = 0; }\n"
    "var LVINTRO = { 7: ['Ra chợ mua bộ nong tre, đặt trên đất bãi hông nhà. Phơi ớt một nắng là có ớt khô bán được giá lắm nghe con.'],\n"
    "  8: ['Chợ có bán khạp da lươn đó con. Muối khạp dưa cải đầu tiên mau lắm, chút xíu là ăn được. Cây chuối giống Ngoại để sẵn rồi.'],\n"
    "  10: ['Từ mai sáng nào ghe bẹo cũng ghé bến mình. Ghe đem hàng ra chợ nổi Cái Răng, trả giá cao lắm con.'],\n"
    "  11: ['Lò sấy gạch Ngoại để dành lâu rồi. Mua về đặt trên đất trống, sấy mứt khế, xoài sấy đem bán là hết sẩy.'],\n"
    "  12: ['Đào cái hố ủ phân nghe con. Lá rụng, lục bình bỏ vô, ủ ra phân bón liếp cho đất tốt lại.'],\n"
    "  13: ['Chợ giờ có bán đồ trang trí rồi. Con chọn rào, chậu kiểng làm vườn mình đẹp lên nghe.'],\n"
    "  14: ['Lò ấp trấu cạnh chuồng vịt dùng được rồi đó. Bỏ trứng vịt vô ấp, ít bữa có bầy vịt con.', [-1.45, 6.3]],\n"
    "  15: ['Lục bình phơi khô rồi Ngoại đan giỏ được. Giỏ lục bình ghe bẹo mua đem ra chợ nổi bán cho khách.', [1.2, 1.62]],\n"
    "  16: ['Khạp cá chật rồi, mình đào cái ao cho cá bơi thong thả nghe con. Chọn bốn ô đất trống sát nhau mà đào.'],\n"
    "  17: ['Vườn nhiều bông rồi, ong về làm tổ đó con. Mua thùng ong đặt gần vườn, có mật ong ngào khế, nướng chuối.'],\n"
    "  19: ['Ghe tam bản đóng xong là con chèo ra sông đặt lờ, sáng ra lấy cá. Hay gặp loài lạ lắm.'],\n"
    "  20: ['Một năm ở vườn rồi đó con. Ngoại mừng lắm, vườn mình giờ đẹp nhứt xóm.'] };")

# ---------- người chơi cũ: giữ đồ đã mở, XP không thụt lùi ----------
rep("const goalsMet = q =>",
    "if (!ST.k102){ ST.k102 = 1; const L = ST.lv || 1; ST.keep = { say: L >= 10, ho: L >= 8, lo: L >= 9, gio: L >= 10, ao: L >= 9 }; }   /* v102 dời cấp mở: ai đã tới cấp mở cũ vẫn dùng tiếp */\n"
    "if ((ST.xp || 0) < (XPN[ST.lv || 1] || 0)) ST.xp = XPN[ST.lv || 1];   /* XP mới cao hơn: kéo lên mốc của cấp đang có, thanh kinh nghiệm không âm */\n"
    "const goalsMet = q =>")
rep("const icOf = k => ICON[k] || UIC[k] || UIC.task;", "const icOf = k => ICON[k] || UIC[k] || (k === 'vuon' ? (() => { try { return AVIMG.banbe; } catch (e) { return null; } })() : null) || UIC.task;")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
