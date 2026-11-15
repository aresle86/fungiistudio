# NHÁP v153: giống quý (Ares duyệt 1-6 ngày 15/11/2026).
#   python3 fix153.py live/v152.html live/v153.html
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v152'", "BUILD = 'v153'")

# ---- 1. không bao giờ mất giống: hết hạt trong túi thì lứa nào cũng trả lại 1 hạt; còn hạt thì 25% như cũ ----
rep("if (Math.random() < .25){ ST.seeds[k0]", "if (!(ST.seeds[k0] > 0) || Math.random() < .25){ ST.seeds[k0]")

# ---- 3. mùa ghi rõ trong sổ, kèm tháng ----
rep("const quyHas = (k, x) => {", "const quyHas = (k, x) => { if (x === 'mua') return true;")
rep("const quyLab = (q, x) => QCL[q[x]];",
    "const quyLab = (q, x) => QCL[q[x]] + (x !== 'mua' ? '' : q.mua === 'kho' ? L135(' (tháng 12 tới tháng 4)', ' (Dec to Apr)') : L135(' (tháng 5 tới tháng 11)', ' (May to Nov)'));")

# ---- 2. quà dọc đường của ông Bảy: giao 2 giống 300 xu, giao 4 giống 600 xu ----
rep("function bayHTML(){",
    """const BAYMOC = [[2, 300], [4, 600]];   /* v153 */
function bayMoc(S){ const B = bayS(); B.moc = B.moc || {}; const n = QGI.filter(k => B.stamp[k]).length; let got = 0;
  for (const [m, v] of BAYMOC) if (n >= m && !B.moc[m]){ B.moc[m] = 1; ST.xu += v; got = m; try { sfx('coin'); coinPop(L135(`+${v} xu · quà ông Bảy`, `+${v} coins · Uncle Bảy's gift`), '#F5D27A'); } catch (e) {} }
  if (got){ if (S && !(B.set.giong && n >= 6)){ S.pose = 'kha'; S.line = L135(`Được ${got} giống quý rồi đó. Qua gửi cháu chút quà dọc đường, ráng tìm cho đủ bộ nghe.`, `That's ${got} rare crops now. Here's a little something along the way. Keep looking for the full set.`); } save(); hud(); } return got; }
function bayHTML(){""")
rep("const S = SHEET.bay, nst = [...QGI, ...QCA]", "bayMoc(SHEET.bay); const S = SHEET.bay, nst = [...QGI, ...QCA]")
rep("+ UX.title('Ông Bảy Kiếng tặng') + `<div class=\"qset${set.giong",
    "+ UX.title('Ông Bảy Kiếng tặng') + `<div class=\"qset${((ST.bay || {}).moc || {})[4] ? ' ok' : ''}\"><img src=\"${UIC.coin}\" alt=\"\"><div><b>${L135('Quà dọc đường', 'Gifts along the way')}</b><span>${L135('Giao 2 giống: 300 xu · giao 4 giống: 600 xu', 'Hand over 2 crops: 300 coins · 4 crops: 600 coins')}</span></div></div>` + `<div class=\"qset${set.giong")

# ---- 5. biếu Ngoại trái giống quý: nghe thêm một chuyện cũ, Ngoại ươm lại cho 1 hạt ----
rep("function pgQuy(part){",
    """const QUYB2 = { otvang: L135('Ngoại để trái ớt vàng này lên bàn thờ bà cố nghe. Hồi đó bà dầm ớt vàng vô chén nước mắm, cả nhà ngồi quanh mâm cơm, ai cũng hít hà.', "I'll set this golden chili on great-grandma's altar. She used to crush one into the fish sauce, and the whole family sat around the tray, gasping at the heat."),
  baptim: L135('Để Ngoại luộc trái bắp tím này, chia cho mấy đứa nhỏ trong xóm. Hồi xưa nghe mùi bắp luộc là tụi nó chạy qua đứng đầy sân.', "I'll boil this purple corn and share it with the neighborhood kids. Back then the smell of boiled corn filled our yard with children."),
  cachuavang: L135('Cà chua vàng ngọt y như hồi Ngoại còn nhỏ. Má Ngoại hay giấu mấy trái trong túi áo bà ba, đi chợ về là móc ra cho.', "This yellow tomato is as sweet as when I was little. My mother hid a few in her blouse pocket and pulled them out when she came home from market."),
  khoquarung: L135('Trái này Ngoại nấu chén canh cúng ông ngoại con. Ổng ăn đắng giỏi lắm, còn chọc Ngoại là ăn đắng quen rồi mới biết thương cái ngọt.', "I'll cook this into a bowl of soup for your grandpa's altar. He loved bitter things, and teased me that you only cherish sweetness once you know bitterness."),
  mongtoitia: L135('Để Ngoại nấu nồi canh mồng tơi tía, mời mấy bà bạn già qua ăn cơm. Lâu lắm rồi tụi Ngoại chưa thấy lại tô canh nước tím hồng.', "I'll make a pot of purple spinach soup and invite my old friends over. We haven't seen that pink-purple broth in so long."),
  khommat: L135('Khóm mật con trồng ngọt thiệt. Ngoại xẻ ra chia mỗi nhà trong xóm một miếng, để bà con biết vườn mình còn giữ được giống xưa.', "Your honey pineapple is truly sweet. I'll slice it and give every house a piece, so the neighbors know our garden still keeps the old variety.") };
const quyBieuK = () => QGI.find(k => (ST.inv[k] || 0) > 0 && !((ST.quy || {}).bieu || {})[k]);
function quyBieu(k){ const Q = quyQ(); Q.bieu = Q.bieu || {}; if (!QUYB2[k] || Q.bieu[k] || !((ST.inv[k] || 0) > 0)) return; ST.inv[k]--; Q.bieu[k] = 1; ST.seeds[k] = (ST.seeds[k] || 0) + 1; save(); hud();
  try { closeBook(); } catch (e) {} try { sfx('pop'); buzz(20); confettiAt(innerWidth / 2, innerHeight * .42, 24, .9); } catch (e) {}
  say(QUYB2[k], 'vui', { now: true }); setTimeout(() => { try { toast(L135('Ngoại ươm lại cho con 1 hạt ', 'Ngoại saved 1 seed for you: ') + CROPS[k].name.toLowerCase(), 'vui'); } catch (e) {} }, 1600); }
function pgQuy(part){""")
rep("+ '</div>'; }\n  if (part !== 1){ h += UX.title('Cá quý'",
    """+ '</div>';
    { const nb = QGI.filter(k => ((ST.quy || {}).bieu || {})[k]).length, bk = quyBieuK();
      if (ng && nb < 6) h += UX.title(L135('Biếu Ngoại', 'A gift for Ngoại'), nb + '/6') + (bk ? `<div class="qset"><img src="${ICON[bk]}" alt=""><div><b>${CROPS[bk].name}</b><span>${L135('Biếu Ngoại 1 trái, Ngoại kể chuyện xưa và ươm lại cho 1 hạt', 'Give Ngoại one. She tells an old story and saves you 1 seed')}</span></div></div><div class="cta"><button class="btn g" data-b="quybieu" data-k="${bk}"><span>${L135('Biếu Ngoại 1 trái', 'Give 1 to Ngoại')}</span></button></div>` : `<div class="qset"><div><b>${L135('Chưa có trái để biếu', 'Nothing to give yet')}</b><span>${L135('Có trái giống quý trong kho thì đem biếu Ngoại, Ngoại kể chuyện xưa.', 'Bring Ngoại a rare crop from storage and she tells an old story.')}</span></div></div>`); } }
  if (part !== 1){ h += UX.title('Cá quý'""")
rep("else if (a === 'weedgo'){ closeBook(); weedGo(); return; }", "else if (a === 'quybieu'){ quyBieu(k); return; }\n  else if (a === 'weedgo'){ closeBook(); weedGo(); return; }")


open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
