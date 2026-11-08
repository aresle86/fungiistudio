# nc118b: gắn 12 giống mới vào game (sau nc118.py đã thêm mô hình).
# Cấp mở theo bảng kế hoạch đã duyệt: đu đủ 13, mãng cầu 14, sung + bầu 15, khóm + mướp 16, mía 17, đậu rồng 18, bưởi Năm Roi 19, vú sữa Lò Rèn 20, sầu riêng + dừa sáp 25.
# Giá tính theo mức lời mỗi giờ của cây cùng loại đang có (cây trái ~17-19 xu/giờ, cấp cao nhỉnh hơn tới ~27).
# Vú sữa Lò Rèn dùng mã 'vusualr' vì 'vusua' đã là trái của cây cổ tích (không bán được).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

# 1) giống mới trong CROPS
NEW = """
Object.assign(CROPS, {   // v118: 12 giống mới đậm chất miền Tây
  dudu: { name: 'Đu đủ', kind: 'tree', tree: 1, grow: 12 * 3600, seed: 650, sell: 20, yield: 10, cuts: 1e6, re: 10 * 3600, dry: 10 * 3600, unit: 'trái', sway: 0, h: 1.9 },
  mangcau: { name: 'Mãng cầu', kind: 'tree', tree: 1, grow: 16 * 3600, seed: 700, sell: 30, yield: 7, cuts: 1e6, re: 10 * 3600, dry: 10 * 3600, unit: 'trái', sway: 0, h: 1.7 },
  sung: { name: 'Sung', kind: 'tree', tree: 1, grow: 14 * 3600, seed: 750, sell: 8, yield: 24, cuts: 1e6, re: 9 * 3600, dry: 10 * 3600, unit: 'trái', sway: 0, h: 2.0 },
  bau: { name: 'Bầu', kind: 'trellis', grow: 3 * 3600, seed: 45, sell: 30, yield: 2, cuts: 3, re: 2 * 3600, dry: 2 * 3600, unit: 'trái', sway: .25, h: 1.3 },
  khom: { name: 'Khóm', kind: 'row', grow: 6 * 3600, seed: 60, sell: 50, yield: 4, cuts: 1, re: 0, dry: 5 * 3600, unit: 'trái', sway: .2, h: .55 },
  muop: { name: 'Mướp', kind: 'trellis', grow: 150 * 60, seed: 40, sell: 22, yield: 2.5, cuts: 3, re: 90 * 60, dry: 2 * 3600, unit: 'trái', sway: .25, h: 1.3 },
  mia: { name: 'Mía tím', kind: 'row', grow: 5 * 3600, seed: 50, sell: 28, yield: 4, cuts: 2, re: 3 * 3600, dry: 5 * 3600, unit: 'cây', sway: .5, h: 1.5 },
  daurong: { name: 'Đậu rồng', kind: 'stake', grow: 3 * 3600, seed: 45, sell: 18, yield: 3, cuts: 4, re: 90 * 60, dry: 3 * 3600, unit: 'nắm', sway: .4, h: 1.1 },
  buoi: { name: 'Bưởi Năm Roi', kind: 'tree', tree: 1, grow: 24 * 3600, seed: 1000, sell: 60, yield: 6, cuts: 1e6, re: 14 * 3600, dry: 14 * 3600, unit: 'trái', sway: 0, h: 2.2 },
  vusualr: { name: 'Vú sữa Lò Rèn', kind: 'tree', tree: 1, grow: 24 * 3600, seed: 1100, sell: 45, yield: 8, cuts: 1e6, re: 14 * 3600, dry: 14 * 3600, unit: 'trái', sway: 0, h: 2.3 },
  saurieng: { name: 'Sầu riêng', kind: 'tree', tree: 1, grow: 36 * 3600, seed: 2000, sell: 180, yield: 3, cuts: 1e6, re: 20 * 3600, dry: 16 * 3600, unit: 'trái', sway: 0, h: 2.7 },
  duasap: { name: 'Dừa sáp', kind: 'tree', tree: 1, grow: 30 * 3600, seed: 1800, sell: 120, yield: 4, cuts: 1e6, re: 18 * 3600, dry: 24 * 3600, unit: 'trái', sway: 0, h: 2.4 } });
Object.assign(UNLOCK, { dudu: 13, mangcau: 14, sung: 15, bau: 15, khom: 16, muop: 16, mia: 17, daurong: 18, buoi: 19, vusualr: 20, saurieng: 25, duasap: 25 });"""
rep("const UNLOCK = { cai: 1, hanh: 1, raumuong: 2, ot: 3, bap: 4, cachua: 5, khoqua: 6, mongtoi: 7, daubap: 7, chuoi: 8, oi: 9, khe: 10, xoai: 11, dua: 12 };",
    "const UNLOCK = { cai: 1, hanh: 1, raumuong: 2, ot: 3, bap: 4, cachua: 5, khoqua: 6, mongtoi: 7, daubap: 7, chuoi: 8, oi: 9, khe: 10, xoai: 11, dua: 12 };" + NEW)

# 2) mô hình vú sữa Lò Rèn dùng mã mới
rep("FR.buildN(k, g, st); };", "FR.buildN(k, g, st); }; CB.vusualr = (b, st) => { const g = G((b[0] + b[2]) / 2, .06, (b[1] + b[3]) / 2, 0); g.scale.setScalar(1.35); FR.buildN('vusua', g, st); };")

# 3) biểu tượng
I = open('nc118_icon.js', encoding='utf-8').read()
rep("  ri.renderLists.dispose(); return OUT; };\n\nObject.assign(ICON, crop5());", I + "  ri.renderLists.dispose(); return OUT; };\n\nObject.assign(ICON, crop5());")

# 4) ưa gì, mẹo trồng, chuyện Ngoại kể
rep("xoai: ['sun', 'Ưa nắng'], dua: ['drop', 'Mé sông'] };",
    "xoai: ['sun', 'Ưa nắng'], dua: ['drop', 'Mé sông'], dudu: ['sun', 'Ưa nắng'], mangcau: ['sun', 'Chịu hạn'], sung: ['drop', 'Ưa ẩm'], bau: ['drop', 'Gần mương'], muop: ['drop', 'Gần mương'], daurong: ['sun', 'Ưa nắng'], khom: ['sun', 'Chịu phèn'], mia: ['drop', 'Ưa nước'], buoi: ['drop', 'Ưa ẩm'], vusualr: ['drop', 'Ưa ẩm'], saurieng: ['drop', 'Ưa ẩm'], duasap: ['drop', 'Ưa nước'] };")
rep("  dua: ['Dừa trồng mé sông, rễ tự hút nước.', 'Buồng dừa ra dưới tàu lá.', 'Trái dừa xanh chặt uống là ngọt.'] };",
    """  dua: ['Dừa trồng mé sông, rễ tự hút nước.', 'Buồng dừa ra dưới tàu lá.', 'Trái dừa xanh chặt uống là ngọt.'],
  dudu: ['Đu đủ lớn mau, một thân thẳng, trái đeo sát thân.', 'Lá già vàng dưới gốc thì bẻ bỏ.', 'Trái ửng vàng một đường là hái được.'],
  mangcau: ['Mãng cầu thấp cây, dễ hái.', 'Mắt trái giãn ra, kẽ ửng trắng là chín.', 'Chịu hạn, ít tưới cũng được.'],
  sung: ['Trái sung mọc thành chùm ngay trên thân với cành.', 'Sung không thấy bông, bông nằm trong trái.', 'Trồng gần nước là sai trái.'],
  bau: ['Bầu leo giàn trên mương, trái thòng xuống.', 'Bông trắng nở chiều tối.', 'Hái trái non, vỏ còn lông tơ là ngon.'],
  muop: ['Mướp leo giàn trên mương, bông vàng nở sáng.', 'Hái trái non, để già là xơ thành xơ mướp.', 'Tưới đều thì trái dài, thẳng.'],
  daurong: ['Đậu rồng cắm cọc chữ A cho dây quấn.', 'Bông tím nhạt, trái bốn cánh.', 'Hái trái non cỡ một gang tay, già là xơ.'],
  khom: ['Khóm chịu đất phèn, ít tưới.', 'Bông tím đỏ mọc giữa bụi rồi thành trái.', 'Trái ngả vàng từ đít lên là hái.'],
  mia: ['Mía trồng hàng, thân lớn theo đốt.', 'Lột bẹ khô dưới gốc cho cây thoáng.', 'Chặt sát gốc, gốc đâm chồi lên vụ sau.'],
  buoi: ['Bưởi Năm Roi trồng một lần, cây ra trái nhiều năm.', 'Bông trắng thơm cả vườn.', 'Trái vỏ xanh ngả vàng là ngọt.'],
  vusualr: ['Lá vú sữa mặt dưới vàng óng như đồng.', 'Trái chín vỏ bóng, bóp nhẹ thấy mềm.', 'Hái phải cắt cuống, đừng giựt.'],
  saurieng: ['Sầu riêng cây cao nhất vườn, cành ngang từng tầng.', 'Bông nở ban đêm, thòng chùm dưới cành.', 'Trái chín tự rụng, đừng đứng dưới gốc.'],
  duasap: ['Dừa sáp trồng mé nước như dừa thường.', 'Trái nhìn y dừa thường, lắc không nghe nước.', 'Cơm dừa sáp đặc, dẻo như kem.'] };""")
rep("dua: 'Có cây dừa là có bóng mát cho ghe đậu. Trưa nắng chặt trái dừa uống là đã khát.' };",
    """dua: 'Có cây dừa là có bóng mát cho ghe đậu. Trưa nắng chặt trái dừa uống là đã khát.',
  dudu: 'Mâm ngũ quả miền Nam có trái đu đủ, đọc là đủ. Cầu sung vừa đủ xài, con nhớ nghe.', mangcau: 'Mãng cầu là chữ cầu trên mâm ngũ quả. Năm nào cũng cầu cho nhà mình đủ đầy.', sung: 'Sung là sung túc. Trái sung mọc từng chùm, nhìn là thấy đông đủ con cháu.',
  khom: 'Khóm Cầu Đúc ngọt lừ. Bánh xèo củ hủ dừa mà thêm miếng khóm là hết sẩy.', mia: 'Mùa nước nổi cá linh về, kho với mía lau ngọt thanh. Ngoại kho một nồi là ăn cả tuần.',
  daurong: 'Đậu rồng luộc chấm kho quẹt, hay xào tỏi. Trái nó có bốn cánh như con rồng nên người ta kêu vậy.',
  buoi: 'Người ta kể hồi xưa có ông trộm bưởi bị chủ vườn dọa đánh năm roi, từ đó kêu là bưởi Năm Roi. Chuyện thiệt hư Ngoại hổng biết, mà bưởi thì ngọt thiệt.',
  vusualr: 'Vú sữa Lò Rèn ở Vĩnh Kim, đặt tên theo lò rèn của ông thợ có công trồng giống này. Trái ngọt như sữa, xưa đem tiến vua.',
  saurieng: 'Sầu riêng Cái Mơn trồng lâu lắm mới có trái. Cây này là để dành cho con cháu.', duasap: 'Dừa sáp Cầu Kè hiếm lắm, trăm trái dừa mới có vài trái sáp. Dầm với đường, nước đá ăn mát rượi.' };""")

# 5) đơn hàng nhà bên: lý do mua
rep("const NBWHY = { cai: 'xào tỏi',", "const NBWHY = { dudu: 'làm gỏi đu đủ', mangcau: 'chưng mâm ngũ quả', sung: 'làm gỏi sung', bau: 'nấu canh bầu', muop: 'nấu canh mướp', daurong: 'xào tỏi', khom: 'nấu canh chua', mia: 'kho cá linh', buoi: 'làm gỏi bưởi', vusualr: 'đem biếu', saurieng: 'nấu chè', duasap: 'dầm đường', cai: 'xào tỏi',")

# 6) màu trái bay lên khi hái
rep("khoqua: '#9fd36a', daubap: '#A2D45E',", "khoqua: '#9fd36a', daubap: '#A2D45E', dudu: '#F2A93A', mangcau: '#9AC46C', sung: '#C2804A', bau: '#A9D27A', muop: '#3E6E32', daurong: '#9ED46A', khom: '#E8B43A', mia: '#6C4458', buoi: '#BFD25A', vusualr: '#79B44A', saurieng: '#9AA644', duasap: '#7FA848',")

# 7) chỉ chỗ trồng: cây trái mới không có gốc riêng, trồng ở ô đất trống; giàn không chỉ có khổ qua
rep("const WHERE = k => { const c = CROPS[k]; return c.tree ? (k === 'dua' ? 'Gốc dừa mé sông' : 'Góc cây trái bên hông nhà')",
    "const WHERE = k => { const c = CROPS[k]; return c.tree ? (k === 'dua' ? 'Gốc dừa mé sông' : TREEOWN(k) ? 'Góc cây trái bên hông nhà' : 'Ô đất trống, chọn Cây')")
rep("const fits = (k, P) =>", "const TREEOWN = k => PLOTS.some(P => P.tree === k);\nconst fits = (k, P) =>")
rep("c.tree ? `${c.name} trồng ở ${k === 'dua' ? 'gốc dừa mé sông cạnh bến' : 'góc cây trái bên hông nhà'} con.` : P.tree ? `Gốc này để trồng ${CROPS[P.tree].name.toLowerCase()} con.` : c.kind === 'trellis' ? 'Khổ qua phải trồng ở giàn trên mương con.' : 'Giàn là để khổ qua leo, cây này trồng ở liếp nghe con.'",
    "c.tree ? (TREEOWN(k) ? `${c.name} trồng ở ${k === 'dua' ? 'gốc dừa mé sông cạnh bến' : 'góc cây trái bên hông nhà'} con.` : `${c.name} trồng ở ô đất trống con, chạm ô đất rồi chọn Cây.`) : P.tree ? `Gốc này để trồng ${CROPS[P.tree].name.toLowerCase()} con.` : c.kind === 'trellis' ? `${c.name} phải trồng ở giàn trên mương con.` : 'Giàn là để bầu bí leo, cây này trồng ở liếp nghe con.'", 2)
rep("c.kind === 'trellis' ? 'Kéo thả vào chân giàn trên mương để trồng khổ qua' : c.tree ? `Thả vào gốc ${c.name.toLowerCase()} ${t.k === 'dua' ? 'mé sông' : 'ở góc cây trái'} để trồng`",
    "c.kind === 'trellis' ? `Kéo thả vào chân giàn trên mương để trồng ${c.name.toLowerCase()}` : c.tree ? (TREEOWN(t.k) ? `Thả vào gốc ${c.name.toLowerCase()} ${t.k === 'dua' ? 'mé sông' : 'ở góc cây trái'} để trồng` : `Chạm ô đất trống, chọn Cây để trồng ${c.name.toLowerCase()}`)")

# 8) việc cấp 18: mâm ngũ quả "cầu sung vừa đủ xài" đủ năm trái (không chưng chuối)
rep("18: { t: 'pay', xu: 5000, items: [['dua', 2], ['xoai', 2], ['__dish', 3]], txt: 'Sửa sang nhà cửa', how: 'Tiền mua gạch tàu, sơn cửa. Dừa với xoài nhà trồng chưng bàn thờ ông Thiên, cho vừa đủ xài.",
    "18: { t: 'pay', xu: 5000, items: [['mangcau', 1], ['sung', 2], ['dua', 1], ['dudu', 1], ['xoai', 1], ['__dish', 3]], txt: 'Sửa sang nhà cửa', how: 'Tiền mua gạch tàu, sơn cửa. Mâm ngũ quả mãng cầu, sung, dừa, đu đủ, xoài chưng bàn thờ ông Thiên, cầu sung vừa đủ xài.")

# 9) thẻ lên cấp: giống mới hiện trong danh sách món mới
rep("13: [['nong', 'Giàn nong hai tầng, thêm khạp']], 14: [['vitcon', 'Lò ấp vịt']], 15: [['gio', 'Giỏ lục bình'], ['cuoc', 'Mái lá mới']], 16: [['caro', 'Đào ao cá']], 17: [['matong', 'Nuôi ong lấy mật'], ['chuoimat', 'Món mật ong']], 18: [['cuoc', 'Sửa sang nhà cửa']], 19: [['tamban', 'Ghe tam bản đặt lờ']], 20: [['so', 'Một năm ở vườn Ngoại']] };",
    "13: [['nong', 'Giàn nong hai tầng, thêm khạp'], ['dudu', 'Cây đu đủ']], 14: [['vitcon', 'Lò ấp vịt'], ['mangcau', 'Cây mãng cầu']], 15: [['gio', 'Giỏ lục bình'], ['cuoc', 'Mái lá mới'], ['sung', 'Cây sung'], ['bau', 'Bầu trên giàn']], 16: [['caro', 'Đào ao cá'], ['khom', 'Khóm'], ['muop', 'Mướp trên giàn']], 17: [['matong', 'Nuôi ong lấy mật'], ['chuoimat', 'Món mật ong'], ['mia', 'Mía tím']], 18: [['cuoc', 'Sửa sang nhà cửa'], ['daurong', 'Đậu rồng']], 19: [['tamban', 'Ghe tam bản đặt lờ'], ['buoi', 'Bưởi Năm Roi']], 20: [['so', 'Một năm ở vườn Ngoại'], ['vusualr', 'Vú sữa Lò Rèn']] };")

# 10) tiếng Anh
rep('"dua": "Coconut", ', '"dua": "Coconut", "dudu": "Papaya", "mangcau": "Sugar apple", "sung": "Cluster fig", "bau": "Bottle gourd", "muop": "Luffa", "daurong": "Winged bean", "khom": "Pineapple", "mia": "Purple sugarcane", "buoi": "Năm Roi pomelo", "vusualr": "Lò Rèn star apple", "saurieng": "Durian", "duasap": "Wax coconut", ')

# 11) bỏ nét viền nâu giữa các khối lớn trên mọi biểu tượng (anh Ares: sạch như mía, khóm)
rep("function toonRender0(ri, sc, cm){ toonify(sc);", "function toonRender0(ri, sc, cm){ toonify(sc); if (!TOON_EDGE){ ri.render(sc, cm); TOONLAST = ri.domElement.toDataURL('image/png'); return; }")
rep("function toonRender(ri, sc, cm){", "const TOON_EDGE = false;   // v118: tắt nét viền nâu giữa các khối\nfunction toonRender(ri, sc, cm){")

# 12) biểu tượng khế: trái nguyên năm khía thon hai đầu, kèm lát khế hình sao
KHE_OLD = "icon('khe', p => { add(p, star(.5, .2, .11), '#F2C63A', -.1, .04, 0, [Math.PI / 2 - .25, .5, .35]); const sh = new T.Shape(); for (let i = 0; i < 10; i++){ const a = i / 10 * 6.283 + .31, r = i % 2 ? .075 : .16; sh[i ? 'lineTo' : 'moveTo'](Math.cos(a) * r, Math.sin(a) * r); } add(p, new T.ExtrudeGeometry(sh, { depth: .07, bevelEnabled: false }), '#F7DA6A', .2, -.1, .14, [0, -.25, 0]); }, V(.25, .35, 1));"
KHE_NEW = "icon('khe', p => { const stS = (R1, R2) => { const sh = new T.Shape(); for (let i = 0; i < 10; i++){ const a = i / 10 * 6.283 + Math.PI / 2, r = i % 2 ? R2 : R1; sh[i ? 'lineTo' : 'moveTo'](Math.cos(a) * r, Math.sin(a) * r); } sh.closePath(); return sh; }; const D = .66, bg = new T.ExtrudeGeometry(stS(.25, .13), { depth: D, steps: 12, bevelEnabled: false }), pp = bg.attributes.position; for (let i = 0; i < pp.count; i++){ const z = pp.getZ(i), u = z / D, k = Math.pow(Math.sin(Math.PI * (.04 + .92 * u)), .55); pp.setXYZ(i, pp.getX(i) * k, pp.getY(i) * k, z - D / 2); } bg.computeVertexNormals(); add(p, bg, '#F2C63A', -.1, .06, -.06, [.35, -.95, .25]); add(p, new T.CylinderGeometry(.018, .024, .08, 4), '#8A7A3A', -.1 + Math.sin(-.95) * -.36, .06 + .13, -.06 + Math.cos(-.95) * -.36 * .9, [0, 0, 1.2]); const sl = new T.Group(); sl.position.set(.24, -.2, .2); sl.rotation.set(-.35, -.35, 0); p.add(sl); add(sl, new T.ExtrudeGeometry(stS(.19, .1), { depth: .05, bevelEnabled: false }), '#F2C63A'); add(sl, new T.ShapeGeometry(stS(.17, .085)), '#FBE69A', 0, 0, .052); for (let k = 0; k < 5; k++){ const a = k / 5 * 6.283 + Math.PI / 2; add(sl, new T.SphereGeometry(.014, 5, 4), '#B8862A', Math.cos(a) * .05, Math.sin(a) * .05, .056, null, [1, .6, .5]); } }, V(.25, .35, 1));"
rep(KHE_OLD, KHE_NEW)

# 13) tiếng Anh cho lời việc cấp 18 mới
rep('"Tiền mua gạch tàu, sơn cửa. Dừa với xoài nhà trồng chưng bàn thờ ông Thiên, cho vừa đủ xài. Nấu 3 nồi đãi thợ. Sửa chừng tám tiếng, bạn ghé phụ thì mau hơn": "Coins buy bricks and paint. Home-grown coconuts and mangoes for the sky-god altar, a southern wish for just enough.',
    '"Tiền mua gạch tàu, sơn cửa. Mâm ngũ quả mãng cầu, sung, dừa, đu đủ, xoài chưng bàn thờ ông Thiên, cầu sung vừa đủ xài. Nấu 3 nồi đãi thợ. Sửa chừng tám tiếng, bạn ghé phụ thì mau hơn": "Coins buy bricks and paint. A five-fruit tray of sugar apple, fig, coconut, papaya and mango for the sky-god altar: in the south the names sound like a wish for just enough.')

# 14) 19 biểu tượng làm lại (ic119.js): món là chính, hũ thủy tinh, túi trong, nia sẫm; vẽ cùng ánh sáng với biểu tượng sản vật
IC = open('ic119.js', encoding='utf-8').read().replace('window.IC119 = (T, add) =>', 'const IC119 = (T, add) =>', 1)
assert 'const IC119 = (T, add) =>' in IC
rep("Object.assign(ICON, crop5()); Object.assign(ICON, FR.icons);",
    "Object.assign(ICON, crop5()); Object.assign(ICON, FR.icons);\n" + IC + """
{ const ri = ICR(); ri.setPixelRatio(1); ri.setSize(160, 160); ri.setClearColor(0, 0); const MC = {}, mt = c => MC[c] || (MC[c] = new T.MeshStandardMaterial({ color: c, flatShading: true, roughness: .85, side: T.DoubleSide }));
  const add = (p, geo, c, x = 0, y = 0, z = 0, r, s) => { const m = new T.Mesh(geo, mt(c)); m.position.set(x, y, z); if (r) m.rotation.set(...r); if (s) m.scale.set(...s); p.add(m); return m; };
  const O = IC119(T, add); for (const k in O){ if (k.includes('_')) continue; try { const sc = new T.Scene(), root = new T.Group(); sc.add(root); O[k](root); sc.add(new T.HemisphereLight('#fff4e2', '#94a474', 1.5)); sc.add(new T.AmbientLight('#fff', .2)); const l = new T.DirectionalLight('#fff0d8', 1.7); l.position.set(-3, 8, 4); sc.add(l);
    const bb = new T.Box3().setFromObject(root), c = bb.getCenter(new T.Vector3()), s = bb.getSize(new T.Vector3()).length() * .42, cm = new T.OrthographicCamera(-s, s, s, -s, .01, 100); cm.position.copy(c).add(new T.Vector3(.3, .4, 1).normalize().multiplyScalar(20)); cm.lookAt(c); toonRender(ri, sc, cm); ICON[k] = toonURL(); } catch (e) { console.warn('ic119', k, e); } } }
await LDY(0);""")

# 15) đơn hàng cây trái: tính cả cây trồng ở ô đất trống (trước chỉ tính gốc cố định, nên giống cây trái mới không bao giờ có đơn)
rep("PLOTS.some(P => P.tree === k && ST.plots[P.id] && ST.plots[P.id].crop)", "PLOTS.some(P => ST.plots[P.id] && ST.plots[P.id].crop === k)", 3)   # đơn nhà bên, đơn Tết, đơn ghe

s = s.replace("BUILD = 'v117b'", "BUILD = 'v118a'")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
