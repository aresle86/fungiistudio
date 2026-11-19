# v163 -> v164:
# 1) Nhẹ khung vẽ chính: gộp khối đứng yên của thùng ong, món việc vặt (sâu, lục bình, lá dừa, củi...), cầu khỉ / cầu ván.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v163'", "BUILD = 'v164'")

# ---------- 1) gộp khối đứng yên ----------
# stCompact(g, keep): gộp mọi lưới đứng yên trong nhóm g theo màu; phần có chuyển động (keep) và lưới ẩn để bắt chạm thì giữ nguyên
rep("function ftCompact(m, k){",
    "function stCompact(g, keep){ try { (keep || []).forEach(q => q && q.traverse(c => { c.userData.keep = 1; }));\n"
    "  g.traverse(o => { if (o.visible === false) o.traverse(c => { c.userData.keep = 1; }); else if (o.isMesh && (o.isInstancedMesh || o.isSkinnedMesh || !o.material || Array.isArray(o.material) || o.material.visible === false || o.children.length)) o.traverse(c => { c.userData.keep = 1; }); });\n"
    "  const drop = []; g.traverse(o => { if (o.isMesh && !o.userData.keep) drop.push(o); }); if (drop.length < 8) return g;\n"
    "  g.updateMatrixWorld(true); const out = mergeMeshes(g), iv = g.matrixWorld.clone().invert(); for (const o of drop) o.parent && o.parent.remove(o); for (const x of out){ x.geometry.applyMatrix4(iv); g.add(x); } } catch (e) { console.warn('stCompact', e); } return g; }\n"
    "function ftCompact(m, k){")
rep("g.add(h); ONGV.bees.push(...h.userData.bees); } ONGV.m = g; ONGV.root.add(g); }",
    "g.add(h); ONGV.bees.push(...h.userData.bees); } ONGV.m = g; ONGV.root.add(g); stCompact(g, ONGV.bees); }")
rep("h.userData.odd = o; g.add(h); ODDV.hits.push(h); return g; }",
    "h.userData.odd = o; stCompact(g, [g.userData.ar]); g.add(h); ODDV.hits.push(h); return g; }")
rep("else g.add(cauKia(2, false)); KIAV.m = g; KIAV.root.add(g); }",
    "else g.add(cauKia(2, false)); KIAV.m = g; KIAV.root.add(g); stCompact(g); }")

# ---------- 3) chuyến hàng chợ nổi: chất hàng lên ghe dần, đủ hàng thì ghe đi (số xu, số món y như cũ) ----------
rep("function tbChuyen(){ const B = ST.tb, d = dayKey(); if (B.cd === d && B.co) return B.co;",
    "const tbGot = (o, k) => (o.got && o.got[k]) || 0, tbGotN = o => o.items.reduce((a, [k]) => a + tbGot(o, k), 0);\n"
    "function tbChuyen(){ const B = ST.tb, d = dayKey(); if (B.co && (B.cd === d || (!B.co.done && tbGotN(B.co) > 0))) return B.co;   /* đã chất dở thì giữ chuyến qua ngày, không mất hàng */")
rep("function tbChoGo(){ const o = tbChuyen(); if (o.done || !o.items.every(([k, q]) => has(k) >= q)) return; let n = 0; for (const [k, q] of o.items){ STORE(k)[k] -= q; n += q; } o.done = 1; ST.xu += o.xu; ST.soldN = (ST.soldN || 0) + n; gainXP(12);",
    "function tbChoGo(){ const o = tbChuyen(); if (o.done) return; let n = 0; o.got = o.got || {}; for (const [k, q] of o.items){ const c = Math.max(0, Math.min(has(k), q - tbGot(o, k))); if (c > 0){ STORE(k)[k] -= c; o.got[k] = tbGot(o, k) + c; n += c; } } ST.soldN = (ST.soldN || 0) + n;\n"
    "  if (!o.items.every(([k, q]) => tbGot(o, k) >= q)){ if (n > 0){ sfx('pick'); buzz(12); for (let i = 0; i < 6; i++) puff('drop', TB.at[0] + R(-.5, .5), .05, TB.at[1] + R(-.2, .2), 1, '#9cc6e0', .6); save(); hud(); renderSheet(); } return; }   /* chưa đủ: hàng nằm trên ghe chờ */\n"
    "  o.done = 1; ST.xu += o.xu; gainXP(12);")
rep("const o = tbChuyen(), okc = o.items.every(([k, q]) => has(k) >= q);\n  h += UX.title('Chuyến hàng chợ nổi', o.done ? 'hôm nay chở rồi, mai có chuyến mới' : 'mỗi ngày một chuyến') + (o.done ? '' : `<div class=\"tbch\">${UX.chips(Object.fromEntries(o.items))}</div>` + UX.cta([UX.btn('tbcho', 'Chở đi', { g: 1, img: UIC.coin, dis: !okc, sub: `${o.xu} xu` })]));",
    "const o = tbChuyen(), okc = o.items.every(([k, q]) => has(k) + tbGot(o, k) >= q), okm = o.items.some(([k, q]) => tbGot(o, k) < q && has(k) > 0), gn = tbGotN(o);\n"
    "  h += UX.title('Chuyến hàng chợ nổi', o.done ? 'hôm nay chở rồi, mai có chuyến mới' : gn > 0 ? 'hàng chất rồi nằm chờ trên ghe' : 'có món nào chất món đó, đủ thì ghe đi') + (o.done ? '' : `<div class=\"tbch\">${o.items.map(([k, q]) => { const g = tbGot(o, k); return `<span class=\"chip${g + has(k) < q ? ' no' : ''}\"><img src=\"${ICON[k]}\" alt=\"\">${g >= q ? '✓' : g + '/' + q}</span>`; }).join('')}</div>` + UX.cta([UX.btn('tbcho', okc || !okm ? 'Chở đi' : 'Chất lên ghe', { g: 1, img: UIC.coin, dis: !okc && !okm, sub: `${o.xu} xu` })]));")

# (2) chữ tiếng Anh còn sót: bảng chữ, mẫu câu có số, nhãn đọc màn hình
import json as _j, re as _re
_i = s.index('const UIEN = ') + 13; _U = _j.loads(s[_i:s.index('}, UIRX = [', _i) + 1])
_m = _re.search(r"FEN = (\{[^}]+\})", s); _F = _j.loads(_m.group(1))
_t = s.index('for (const [k, name, tier'); _fish = dict(_re.findall(r"\['(\w+)', '([^']+)', \d", s[_t:_t + 12000]))
EX = {
 'Bạn bè': 'Friends', 'Vú sữa Lò Rèn': 'Lò Rèn star apple', 'Kho đầy': 'Storage full',
 'Vườn trồng nhiều thứ, có bông có trái thì bướm bay tới. Chạm vô con bướm để ghi sổ.': 'Grow many things, with flowers and fruit, and butterflies come. Tap a butterfly to note it in the book.',
 'Rim mứt · để trên gác bếp': 'For candying · kept in the kitchen loft', 'Để trên gác bếp': 'Kept in the kitchen loft',
 'Nhà chú Tư': "Uncle Tư's family", 'Nhà cô Hai': "Aunt Hai's family", 'Nhà anh Sáu': "Brother Sáu's family", 'Cả xóm': 'The whole hamlet', 'Nhà dì Bảy': "Aunt Bảy's family",
 'đám giỗ ông nội': "Grandpa's memorial feast", 'đám cưới con gái': "their daughter's wedding", 'ăn tân gia': 'a housewarming', 'cúng đình cuối mùa': 'the season-end temple offering', 'mừng thọ bà cụ': "Granny's longevity party",
 'Hàng rào': 'Fence', 'Đang dùng': 'In use', 'Mẫu đặc biệt': 'Special designs', 'Sắp có ở tiệm': 'Coming to the shop',
 'Đồ kiểng · đặt trên một ô đất trống': 'Ornaments · placed on an empty plot', 'Chiếm 4 ô đất': 'Takes 4 plots',
 'Chuyện ma': 'Ghost stories', 'Chọn chuyện': 'Pick a story', 'Khạp nước cạn': 'The dry water jar', 'Chuyến đò cuối': 'The last ferry', 'Con chó sủa vào vườn trống': 'The dog barking at the empty garden',
 'Cây vú sữa': 'Star apple tree',
 'Bấm dời rồi chạm vô một ô đất trống của con. Cây vú sữa chiếm ô đó với ba ô sát bên, hai ngang hai dọc.': 'Tap Move, then tap one of your empty plots. The star apple tree takes that plot and the three next to it, two across and two down.',
 'Ghe tam bản': 'Sampan', 'Thả lờ bắt cá, câu giữa sông, chở hàng ra chợ nổi': 'Set fish traps, fish mid-river, carry goods to the floating market',
 'Thả lờ ở đâu': 'Where to set traps', 'lờ gom cá của chỗ đó': 'traps catch the fish of that spot',
 'Gần bến': 'Near the pier', 'Giữa sông': 'Mid-river', 'Mé lục bình': 'By the hyacinth',
 'Câu giữa sông': 'Mid-river fishing', 'hôm nay câu đủ rồi, mai ra tiếp': 'enough fishing today, more tomorrow', 'Chèo ra câu': 'Paddle out to fish',
 'Chuyến hàng chợ nổi': 'Floating market trip', 'mỗi ngày một chuyến': 'one trip a day',
 'có món nào chất món đó, đủ thì ghe đi': 'load what you have; the boat leaves when full', 'hàng chất rồi nằm chờ trên ghe': 'loaded goods wait on the boat', 'hôm nay chở rồi, mai có chuyến mới': 'delivered today, a new trip tomorrow',
 'Chở đi': 'Send off', 'Chất lên ghe': 'Load the boat', 'Sơn mũi ghe': 'Paint the bow', 'dùng màu đã mua cho xuồng': 'uses the colours bought for the canoe',
 'Đỏ viền xanh': 'Red with green trim', 'Gỗ mộc': 'Bare wood', 'Xanh ngọc': 'Jade green', 'Đỏ son': 'Vermilion', 'Vàng nghệ': 'Turmeric gold', 'Xanh chàm': 'Indigo',
 'Hiên nhà · đan giỏ': 'Porch · basket weaving', 'Nhờ Ngoại đan một giỏ': 'Ask Grandma to weave a basket', 'Lục bình khô': 'Dried hyacinth', 'Lục bình tươi': 'Fresh hyacinth', 'bó': 'bunches',
 '‹ Quay lại': '‹ Back', 'Ớt khô từ ớt tươi': 'Dried chili from fresh chili', 'Chuối khô từ chuối tươi': 'Sun-dried banana from fresh banana',
 'Hai nồi nấu cùng lúc, mỗi món một bó củi. Xếp món vô hàng chờ thì nồi trống là tự nấu tiếp. Món chín cất lên gác bếp, đem ra chợ bán hoặc giao đơn nhà bên. Lần đầu nấu món nào Ngoại kể chuyện món đó.': "Two pots cook at once, one bundle of firewood per dish. Queue dishes and an empty pot starts the next one. Cooked dishes go to the kitchen loft, to sell at the market or fill neighbours' orders. The first time you cook a dish, Grandma tells its story.",
 'Đang sắp vườn': 'Arranging the garden', 'Lưu': 'Save', 'Đặt thùng ong': 'Place the beehive', 'chưa làm': 'not done', 'Cô Út': 'Miss Út',
 'Gửi link cho bạn, bạn bấm vô là thành hàng xóm.': 'Send the link to a friend; when they tap it you become neighbours.', 'Thêm hàng xóm': 'Add a neighbour',
 'Hôm nay hái ké đủ rồi': "That's enough picking for today", 'Hôm nay hái đủ rồi': "That's enough picking for today",
 'Vườn khác': 'Other gardens', 'Về nhà': 'Go home', 'Qua vườn khác': 'Visit another garden', 'Về vườn mình': 'Back to my garden',
 'Chạm vào bóng cá có vòng sáng để quăng câu': 'Tap a fish shadow with a glowing ring to cast', 'Quăng câu': 'Cast',
 'Đang dựng vườn': 'Building the garden', 'Giờ trong vườn, mở cài đặt': 'Garden time, open settings', 'Về giữa vườn': 'Back to the middle of the garden',
 'Xem liếp': 'View bed', 'Bao hạt': 'Seed bag', 'Thùng tưới': 'Watering can', 'Cầm rơm phủ liếp': 'Hold straw to cover beds', 'Cầm liềm': 'Hold the sickle',
 'Lên cấp': 'Level up', 'Chọn việc trên liếp': 'Choose a job for the bed', 'Buồng thay đồ, chọn nhân vật': 'Dressing room, choose a character',
 'Sổ vườn của Ngoại': "Grandma's garden book", 'Bộ sưu tập': 'Collection', 'Đóng sổ': 'Close the book', 'Thôi câu': 'Stop fishing',
 'Mua 1 bịch đường': 'Buy 1 bag of sugar', 'Mua 1 bịch muối': 'Buy 1 bag of salt', 'Mua 1 bó rơm': 'Buy 1 bunch of straw', 'Mua 1 bó củi': 'Buy 1 bundle of firewood',
 'Hiệu ứng': 'Sound effects', 'Nhạc đàn': 'Music', 'Tiếng vườn': 'Garden sounds', 'Mua đất thổ cư': 'Buy house land',
 'Vườn nhà Ngoại dựng 3D: nhà mái lá, liếp rau, mương nước, giàn khổ qua, chuồng gà, sông có bến đò và ghe': "Grandma's garden in 3D: thatched house, vegetable beds, canals, a bitter melon trellis, a chicken coop, a river with a pier and boats",
}
for _k, _n in _fish.items():
    if _k in _F: EX.setdefault(_n, _F[_k])
EX = {k: v for k, v in EX.items() if k not in _U}
EN2 = r"""
try {
  Object.assign(UIEN, __EX__);
  const _u = { 'cây': 'stalk', 'chén': 'bowl', 'nồi': 'pot', 'ly': 'glass', 'bịch': 'bag', 'bó': 'bunch', 'khay': 'tray', 'nong': 'tray', 'khạp': 'jar' };
  const _g = { 'sáng': 'morning', 'trưa': 'noon', 'chiều': 'afternoon', 'đêm': 'night', 'tối': 'evening', 'trăng rằm': 'full moon', 'không trăng': 'moonless', 'nước lớn': 'high tide', 'nước ròng': 'low tide' };
  const _nm = a => { const e = UIEN[a] || UIEN[a[0].toUpperCase() + a.slice(1)]; return e ? e[0].toLowerCase() + e.slice(1) : a; };
  UIRX.unshift(
    [/^Sổ bướm · (\d+)\/(\d+) loài$/, 'Butterfly book · $1/$2 kinds'],
    [/^đủ cả (\d+) món: \+(\d+) kinh nghiệm$/, 'all $1 items: +$2 XP'],
    [/^Chợ cần (\d+) · giá ×2$/, 'Market wants $1 · price ×2'],
    [/^đã góp (\d+)\/(\d+)$/, 'given $1/$2'],
    [/^Góp (\d+) món$/, 'Give $1 items'],
    [/^Góp (\d+) xu$/, 'Give $1 coins'],
    [/^(.+) · trong hôm nay$/, (m, a) => enT(a) + ' · today'],
    [/^(Đóng|Làm) chừng (\d+) tiếng, bạn ghé vườn phụ thì mau hơn\.$/, 'Takes about $2 hours; friends who visit make it faster.'],
    [/^Còn (.+) · bạn ghé phụ bớt 1 tiếng$/, (m, a) => enT(a) + ' left · each visiting friend saves 1 hour'],
    [/^(\d+) xu một (bó|bịch)$/, (m, n, u) => n + ' coins a ' + _u[u]],
    [/^Cần (\d+) trứng vịt và (\d+) bó củi$/, 'Needs $1 duck eggs and $2 bundles of firewood'],
    [/^Ấp (\d+) trứng vịt$/, 'Hatch $1 duck eggs'],
    [/^Cần (\d+) bó lục bình$/, 'Needs $1 bunches of hyacinth'],
    [/^Vớt lục bình dưới mương · còn thiếu (\d+) bó$/, 'Pull hyacinth from the canal · $1 bunches short'],
    [/^Chọn món cho (khay|nồi|nong|khạp) (\d+)$/, (m, u, n) => 'Choose for ' + _u[u] + ' ' + n],
    [/^Nồi (\d+)$/, 'Pot $1'],
    [/^Dọn cỏ, đắp liếp · (\d+) xu$/, 'Clear weeds, build a bed · $1 coins'],
    [/^Vườn đủ (\d+) liếp chăm rồi con$/, 'You have $1 beds to tend now, dear'],
    [/^Mã vườn con: (.+)$/, 'Your garden code: $1'],
    [/^Vườn (.+) · cấp (\d+)$/, "$1's garden · level $2"],
    [/^Còn hái ké (\d+) món$/, 'You may still pick $1 items'],
    [/^Hôm nay còn hái (\d+) món$/, '$1 items left to pick today'],
    [/^Còn hái được (\d+) món · đã tưới giùm (\d+) liếp$/, '$1 items left to pick · $2 beds watered for them'],
    [/^Câu cá · (.+)$/, (m, a) => 'Fishing · ' + a.split(', ').map(x => _g[x] || _g[x.replace(/^đêm /, '')] || x).join(', ')],
    [/^Chạm vào bóng cá dưới nước để quăng · còn (\d+) con hôm nay$/, 'Tap a fish shadow in the water to cast · $1 fish left today'],
    [/^Hôm nay câu đủ (\d+) con rồi, mai câu tiếp$/, 'Caught all $1 fish for today; more tomorrow'],
    [/^Chèo ghe ra giữa sông · còn (\d+) lượt$/, 'Paddle the boat mid-river · $1 trips left'],
    [/^còn (\d+) lượt hôm nay$/, '$1 trips left today'],
    [/^mua về nếm thử món mới nhà mình · (.+)$/, (m, a) => 'wants to taste your new dish · ' + enT(a)],
    [/^‹ (.+)$/, (m, a) => '‹ ' + enT(a)],
    [/^Lục bình vớt dưới mương, sông Ngoại để dưới hiên \(máng vịt trống thì vịt ăn trước\)\. Đủ (\d+) bó tươi đem phơi nong chừng (\d+) tiếng nắng ra \d+ bó khô\. Ngoại đan \d+ bó khô một giỏ, mỗi ngày đan được (\d+) giỏ, hôm nay đan (\d+)\.$/, 'Hyacinth pulled from the canal and river is kept under the porch (if the duck trough is empty, the ducks eat it first). $1 fresh bunches dry on the tray in about $2 hours of sun into $1 dry bunches. Grandma weaves $1 dry bunches into one basket, up to $3 baskets a day; $4 woven today.'],
    [/^Dáng (\d+)$/, 'Look $1'],
    [/^Bán 1 (\S+) (.+)$/, (m, u, n) => { const e = _nm(n), w = _u[u] || u; return 'Sell 1 ' + (w === 'pc' || w === 'egg' ? '' : w + ' of ') + e; }],
    [/^Việc tiếp theo: (.+), ([^,]+)$/, (m, a, b) => 'Next task: ' + enT(a) + ', ' + enT(b)],
    [/^Sổ · còn (\d+) việc hôm nay$/, 'Book · $1 tasks left today'],
    [/^(\d+) đơn giao được$/, '$1 orders ready to deliver'],
    [/^(.+) · Cấp (\d+), (\d+)% tới cấp (\d+) · đổi nhân vật$/, '$1 · Level $2, $3% to level $4 · change character'],
    [/^(.+) · Cấp (\d+), cấp cao nhất · đổi nhân vật$/, '$1 · Level $2, top level · change character'],
    [/Đặt lò sấy trong vườn/, 'Place the drying oven in the garden'],
    [/Đặt thùng ong trong vườn/, 'Place the beehive in the garden']
  );
  UIRX.push(
    [/(\d+) coins\/(bịch|bó|cây|chén|nồi|ly)$/, (m, n, u) => n + ' coins/' + _u[u]],
    [/ · mùa nước nổi/, ' · flood season'],
    [/ Lò ấp trấu cạnh chuồng ấp trứng vịt ra vịt con\.$/, ' A rice-husk incubator by the pen hatches duck eggs into ducklings.'],
    [/^Vườn ([A-ZÀ-Ỵ][^·,.!?]{0,20})$/, "$1's garden"]
  );
} catch (e) {}
"""
EN2 = EN2.replace('__EX__', _j.dumps(EX, ensure_ascii=False))
rep("function enWalk(root){ if (!EN || !root) return; if (root.querySelectorAll) for (const i of root.querySelectorAll('[placeholder]')){ const a = i.getAttribute('placeholder'), e = enT(a); if (e !== a) i.setAttribute('placeholder', e); }",
    EN2.strip() + " function enWalk(root){ if (!EN || !root) return; if (root.querySelectorAll) for (const at of ['placeholder', 'aria-label', 'title']) for (const i of [...(root.matches && root.matches('[' + at + ']') ? [root] : []), ...root.querySelectorAll('[' + at + ']')]){ const a = i.getAttribute(at), e = enT(a); if (e !== a) i.setAttribute(at, e); }")
rep("} }).observe(document.body, { childList: true, subtree: true }); }",
    "} }).observe(document.body, { childList: true, subtree: true }); new MutationObserver(ms => { for (const m of ms){ const a = m.target.getAttribute('aria-label'); if (a){ const e = enT(a); if (e !== a) m.target.setAttribute('aria-label', e); } } }).observe(document.body, { attributes: true, attributeFilter: ['aria-label'], subtree: true }); }")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
