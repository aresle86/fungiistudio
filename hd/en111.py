# v111 tiếng Anh — đợt 1: khung ngôn ngữ + tên món/cá/bướm + chữ giao diện cố định.
#  - LANG: localStorage 'mv2-lang' nếu đã chọn, không thì theo ngôn ngữ máy (vi → tiếng Việt, còn lại → English).
#  - Tên món, đơn vị, cá, bướm: thay ngay trong bảng dữ liệu khi EN.
#  - Chữ giao diện cố định: bảng UIEN (khớp nguyên chuỗi) + MutationObserver dịch nút, nhãn, tiêu đề khi hiện ra.
#  - Cài đặt có hàng "Ngôn ngữ / Language": Tiếng Việt · English (đổi là tải lại trang).
#  Đợt sau: câu có biến số (tx()), việc, đơn, lời Ngoại, sự tích.
# Dùng: python3 en111.py live/v110d.html live/v111a.html
import sys, json
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)

U = {'bó': 'bunch', 'trái': 'pc', 'nắm': 'handful', 'nải': 'hand', 'chậu': 'pot', 'trứng': 'egg', 'con': 'pc', 'hũ': 'jar', 'bịch': 'bag', 'miếng': 'piece', 'dĩa': 'plate', 'tô': 'bowl', 'tộ': 'pot', 'cái': 'pc', 'xâu': 'string', 'hột': 'egg'}
N = {  # tên tiếng Anh; món đặc trưng giữ tên Việt kèm nghĩa
 'cai': 'Mustard greens', 'hanh': 'Green onion', 'ot': 'Chili', 'bap': 'Corn', 'cachua': 'Tomato', 'raumuong': 'Water spinach', 'khoqua': 'Bitter melon', 'mongtoi': 'Malabar spinach', 'daubap': 'Okra',
 'chuoi': 'Banana', 'oi': 'Guava', 'khe': 'Starfruit', 'xoai': 'Mango', 'dua': 'Coconut', 'duahau': 'Golden watermelon', 'cuc': 'Chrysanthemum',
 'hotvitlon': 'Balut (hột vịt lộn)', 'gatrong': 'Breeding rooster', 'matong': 'Honey', 'trungga': 'Chicken egg', 'trungvit': 'Duck egg', 'muoi': 'Sea salt', 'trau': 'Betel quid', 'vusua': 'Star apple', 'duong': 'Sugar', 'lucbinh': 'Water hyacinth',
 'trungchien': 'Scallion omelette', 'bapluoc': 'Boiled corn', 'canhchua': 'Canh chua (sour soup)', 'khoquatrung': 'Bitter melon & egg', 'canhmongtoi': 'Malabar spinach soup', 'canhchuaca': 'Sour soup with snakehead', 'cakho': 'Cá kho (clay-pot fish)', 'nuongtrui': 'Straw-roasted snakehead', 'teprangkhe': 'Shrimp with starfruit', 'chuoimat': 'Honey-grilled banana', 'khemat': 'Starfruit in honey', 'banhchuoi': 'Baked banana cake',
 'otkho': 'Dried chili', 'chuoiphoi': 'Sun-dried banana', 'khocasac': 'Dried gourami', 'lucbinhkho': 'Dried hyacinth', 'dacai': 'Pickled mustard greens', 'hotvit': 'Salted duck egg',
 'mutkhe': 'Candied starfruit', 'xoaisay': 'Dried mango', 'comdua': 'Toasted coconut', 'mutdua': 'Tết coconut candy', 'gio': 'Hyacinth basket'}
F = {'caro': 'Climbing perch', 'sacran': 'Snakeskin gourami', 'sacbuom': 'Three-spot gourami', 'rophi': 'Tilapia', 'diec': 'Crucian carp', 'mevinh': 'Silver barb', 'chot': 'Mystus catfish', 'bongcat': 'Sand goby', 'tep': 'River shrimp', 'he': 'Tinfoil barb',
 'caloc': 'Snakehead', 'catre': 'Walking catfish', 'thatlat': 'Featherback', 'keo': 'Mudskipper goby', 'chach': 'Spiny eel', 'luon': 'Swamp eel', 'linh': 'Mud carp (cá linh)', 'lang': 'Long-whisker catfish', 'ngat': 'Eel-tail catfish', 'chep': 'Common carp', 'tomcang': 'Giant river prawn', 'chanhduc': 'Dwarf snakehead',
 'bongtuong': 'Marble goby', 'bonglau': 'Bông lau catfish', 'tra': 'Giant pangasius', 'cadua': 'Yellowtail catfish', 'hu': 'Hu catfish', 'rodauvang': 'Golden-head perch', 'locbong': 'Giant snakehead', 'caho': 'Giant barb'}
B = {'trangcai': 'Cabbage white', 'vang': 'Grass yellow', 'phuong': 'Tailed swallowtail', 'tim': 'Purple spotted', 'duoien': 'Green swallowtail', 'lakho': 'Dead-leaf butterfly', 'matran': 'Bush brown', 'hoatiet': 'Brocade butterfly'}
UI = {  # chữ giao diện cố định, khớp nguyên chuỗi
 'Ghé vườn': 'Visit', 'Sổ': 'Book', 'Chợ': 'Market', 'Cài đặt': 'Settings', 'Về giữa': 'Center', 'Sửa vườn': 'Edit', 'Đặt đồ': 'Place', 'Hủy': 'Cancel', 'Lên cấp rồi!': 'Level up!', 'Hay quá!': 'Great!',
 'Hạt': 'Seeds', 'Tưới': 'Water', 'Rơm': 'Straw', 'Liềm': 'Sickle', 'Mua hạt': 'Buy seeds', 'Việc': 'Tasks', 'Kho': 'Storage', 'Sưu tập': 'Collection', 'Đi làm ›': 'Go ›', 'Nhận': 'Claim', 'Biết rồi': 'Got it',
 'Việc của Ngoại': "Grandma's tasks", 'Ngoại nhờ': 'Grandma asks', 'NGOẠI NHỜ': 'GRANDMA ASKS', 'VIỆC HÔM NAY': 'TODAY', 'LÀM LIỀN': 'DO IT NOW', 'Chưa làm': 'Not yet', 'Xong rồi': 'Done', 'Để bữa khác': 'Maybe later',
 'Khuya': 'Late night', 'Bình minh': 'Dawn', 'Buổi sáng': 'Morning', 'Giữa trưa': 'Noon', 'Buổi chiều': 'Afternoon', 'Chạng vạng': 'Dusk', 'Tối': 'Evening',
 'Bán': 'Sell', 'Mua': 'Buy', 'Tiệm': 'Shop', 'Đơn hàng': 'Orders', 'Bán hết': 'Sell all', 'Cho ăn': 'Feed', 'Chuồng gà': 'Chicken coop', 'Chuồng vịt': 'Duck pen', 'Ao cá': 'Fish pond', 'Bếp Ngoại': "Grandma's kitchen", 'Gác bếp': 'Kitchen loft',
 'Bao hạt trong túi': 'Seed bags', 'Giống': 'Seeds', 'Cá': 'Fish', 'Bướm': 'Butterflies', 'Cổ tích': 'Folk tales', 'Bộ sưu tập': 'Collection', 'Củi': 'Firewood', 'Cây trái': 'Fruit trees',
 'Câu cá': 'Fishing', 'Câu tiếp': 'Keep fishing', 'GIỰT!': 'PULL!', 'Chờ cá': 'Waiting…', 'Giữ để kéo': 'Hold to reel', 'Cá rỉa mồi': 'Nibbling…', 'Buông tay!': 'Let go!', 'Cất vô kho': 'Store it', 'Cất vô kho, câu tiếp': 'Store & keep fishing',
 'Giờ trong vườn': 'Garden time', 'Luôn ban ngày': 'Always daytime', 'Trời trong vườn': 'Sky', 'Chơi lại từ đầu': 'Start over', 'Chắc chắn, chơi lại': 'Yes, start over', 'Chép mã khôi phục': 'Copy restore code',
 'Về vườn': 'Go to the garden', 'Tên con': 'Your name', 'Tên vườn': 'Garden name', 'Chọn dáng của con': 'Pick your look', 'Con chọn một dáng nghe': 'Pick a look, dear', 'Đặt tên con với tên vườn': 'Name yourself and your garden',
 'Gieo gì đây?': 'Plant what?', 'Chín rồi, hái thôi!': 'Ripe, harvest!', 'Cây non': 'Seedling', 'Cỏ rậm': 'Overgrown', 'Dọn cỏ, đắp liếp mới': 'Clear and make a bed', 'Dời qua ô khác': 'Move elsewhere', 'Chỗ này': 'Here',
 'Có bản mới · chạm để tải lại': 'New version · tap to reload', 'Chưa có mạng': 'Offline', 'Lượm': 'Collect', 'Lấy hết': 'Take all', 'Đóng': 'Close',
 'Chủ nhật': 'Sunday', 'Thứ hai': 'Monday', 'Thứ ba': 'Tuesday', 'Thứ tư': 'Wednesday', 'Thứ năm': 'Thursday', 'Thứ sáu': 'Friday', 'Thứ bảy': 'Saturday'}

import glob as _g
for _f in sorted(_g.glob('i18n/en_*.json')): UI.update(json.load(open(_f, encoding='utf-8')))   # bảng dịch theo đợt
UI.update({'CẤP': 'LEVEL', 'Kinh nghiệm có từ đâu': 'Where XP comes from', 'Đem ra chợ': 'Take to market', 'Sức chứa kho': 'Storage space', 'Sức chứa': 'Capacity', 'Chái bếp, dưới hiên': 'Kitchen shed, porch', 'Ghe chợ nổi': 'Floating-market boat', 'Giao bớt': 'Deliver some', 'Đơn nhà bên': "Neighbours' orders", 'Món mới': 'New item', 'Đủ hàng là bấm Giao, trả cao hơn bán chợ': 'Have everything? Tap Deliver, pays more than the market', 'Âm lượng': 'Volume', 'Nhạc đàn': 'Music', 'Tiếng vườn': 'Garden sounds', 'Hiệu ứng': 'Effects', 'Âm thanh và hình': 'Sound & graphics', 'Âm thanh: bật': 'Sound: on', 'Âm thanh: tắt': 'Sound: off', 'Đồ hoạ': 'Graphics', 'Thấp': 'Low', 'Vừa': 'Medium', 'Cao': 'High', 'Vườn online': 'Online garden', 'Lưu ngay': 'Save now', 'Tải bản mới nhất': 'Load latest', 'Hàng xóm': 'Neighbours', 'Vườn mẫu': 'Sample garden', 'Bón phân 1 liếp': 'Fertilize 1 bed', 'Phơi 10 mẻ': 'Dry 10 batches', 'Câu 2 con cá': 'Catch 2 fish', 'Câu 1 con cá': 'Catch 1 fish', 'Gieo hạt 2 liếp': 'Sow 2 beds', 'Giao hàng cho ghe bẹo': 'Deliver to the market boat', 'Đặt hố ủ phân trong vườn': 'Place a compost pit', 'Mua khạp nuôi cá trước hiên': 'Buy a fish jar for the porch', 'Xong hết việc hôm nay': 'All of today done', 'Ông Sáu': 'Uncle Sáu', 'Cô Tư': 'Aunt Tư', 'Chú Bảy': 'Uncle Bảy', 'Dì Út': 'Aunt Út', 'Thím Ba': 'Aunt Ba', 'Bé Na': 'Little Na', 'Cô Hai': 'Aunt Hai', 'Chú Năm': 'Uncle Năm', 'Tiếng Việt': 'Tiếng Việt', 'Ngôn ngữ · Language': 'Language · Ngôn ngữ', 'Giao': 'Deliver', 'Hôm nay': 'Today'})
RX = [x for _f in sorted(_g.glob('i18n/rx_*.json')) for x in json.load(open(_f, encoding='utf-8'))] + [['^Việc hôm nay (\\d+)/(\\d+)( · có quà nhận)? ›$', 'Today $1/$2$3 ›'], [' · có quà nhận', ' · gift to claim'], ['^Việc hôm nay · (.+)$', 'Today · $1'], ['^xong (\\d+)/(\\d+) · mỗi việc \\+(\\d+) kinh nghiệm$', '$1/$2 done · +$3 XP each'], ['^Cấp (\\d+) → (\\d+)$', 'Level $1 → $2'], ['^Cấp (\\d+)$', 'Level $1'], ['^Còn (\\d+) kinh nghiệm nữa lên cấp (\\d+)$', '$1 XP to level $2'], ['^Hạt (.+)$', '$1 seeds'], ['^Gác bếp · (\\d+)/(\\d+)$', 'Kitchen loft · $1/$2'], ['^Củi · (\\d+)/(\\d+)$', 'Firewood · $1/$2'], ['^Thêm kệ gác bếp · (\\d+) xu$', 'Add a loft shelf · $1 coins'], ['^Thêm lu · (\\d+) xu$', 'Add a jar · $1 coins'], ['^(\\d+) đơn giao được rồi$', '$1 order(s) ready'], ['^đổi đơn còn (\\d+) lần hôm nay$', '$1 swaps left today'], ['^Ghe bẹo (.+)$', "$1's market boat"], ['^(\\d+) xu$', '$1 coins'], ['^(\\d+) xu$', '$1 coins'], ['^thứ Hai$', 'Monday'], ['^thứ Ba$', 'Tuesday'], ['^thứ Tư$', 'Wednesday'], ['^thứ Năm$', 'Thursday'], ['^thứ Sáu$', 'Friday'], ['^thứ Bảy$', 'Saturday']]
pre = """const LANG = (() => { try { const v = localStorage.getItem('mv2-lang'); if (v) return v; } catch (e) {} return /^vi/i.test(navigator.language || '') ? 'vi' : 'en'; })(), EN = LANG === 'en';
const UIEN = %s, UIRX = %s.map(([a, b]) => [new RegExp(a), b]);
const enT = t => { if (UIEN[t]) return UIEN[t]; let o = t; for (let k = 0; k < 2; k++) for (const [r, b] of UIRX) o = o.replace(r, b); return UIEN[o] || o; };
function enWalk(root){ if (!EN || !root) return; const w = document.createTreeWalker(root, NodeFilter.SHOW_TEXT); let n; while ((n = w.nextNode())){ const t = n.nodeValue.trim(); if (t){ const e = enT(t); if (e !== t) n.nodeValue = n.nodeValue.replace(t, e); } } }
if (EN){ document.documentElement.lang = 'en'; { const st = document.createElement('style'); st.textContent = 'html[lang=en] .bkt span{font-size:11px!important;letter-spacing:-.01em} html[lang=en] .coin small{font-size:10px!important} .cta .btn>span{text-align:left;line-height:1.15} .cta .btn small{display:block} .upc>img{width:30px!important;height:30px!important;object-fit:contain;flex:none}'; document.head.appendChild(st); } enWalk(document.body); new MutationObserver(ms => { for (const m of ms) for (const x of m.addedNodes){ if (x.nodeType === 3){ const t = x.nodeValue.trim(), e = enT(t); if (e !== t) x.nodeValue = x.nodeValue.replace(t, e); } else if (x.nodeType === 1) enWalk(x); } }).observe(document.body, { childList: true, subtree: true }); }   /* đợt 1: chữ giao diện cố định */
""" % (json.dumps(UI, ensure_ascii=False), json.dumps(RX, ensure_ascii=False))
post = """if (EN){ const NEN = %s, UEN = %s, FEN = %s, BEN = %s;
  for (const T0 of [CROPS, EXTRA, DISH, PHOI, MUOI, SAY]) for (const k in T0){ if (NEN[k]) T0[k].name = NEN[k]; if (T0[k].unit && UEN[T0[k].unit]) T0[k].unit = UEN[T0[k].unit]; }
  try { for (const k in FISHK) if (FEN[k]) FISHK[k].name = FEN[k]; } catch (e) {} try { for (const k in BUK) if (BEN[k]) BUK[k].name = BEN[k]; } catch (e) {} }   /* tên món, cá, bướm tiếng Anh */
""" % (json.dumps(N, ensure_ascii=False), json.dumps(U, ensure_ascii=False), json.dumps(F, ensure_ascii=False), json.dumps(B, ensure_ascii=False))

i0 = max(range(len(s)), key=lambda _: 0)  # placeholder
import re as _re
_ms = [m for m in _re.finditer(r'<script type="module">', s)]
_big = max(_ms, key=lambda m: s.find('</script>', m.end()) - m.end())
s = s[:_big.end()] + "\n" + pre + s[_big.end():]   # LANG khai báo đầu module để mọi chỗ dùng được
rep("const PHASE = h =>", "const PHASE0 = h =>")
rep("h < 22.5 ? 'Tối' : 'Khuya';", "h < 22.5 ? 'Tối' : 'Khuya';\nconst PHASE = h => { const p = PHASE0(h); return EN ? ({ 'Khuya': 'Late night', 'Bình minh': 'Dawn', 'Buổi sáng': 'Morning', 'Giữa trưa': 'Noon', 'Buổi chiều': 'Afternoon', 'Chạng vạng': 'Dusk', 'Tối': 'Evening' }[p] || p) : p; };")
# chèn bảng tên sau khi mọi bảng đã dựng: ngay trước hàm vẽ Sổ
rep("function renderBook(){", post + "function renderBook(){")
# Cài đặt: chọn ngôn ngữ
rep("h += `<div class=\"sub\">Trời trong vườn</div>",
    "h += `<div class=\"sub\">Ngôn ngữ · Language</div><div class=\"acts\">${[['vi', 'Tiếng Việt'], ['en', 'English']].map(([k, n]) => `<button class=\"btn${LANG === k ? ' g' : ''}\" data-a=\"lang\" data-k=\"${k}\" aria-pressed=\"${LANG === k}\">${n}</button>`).join('')}</div>`;\n    h += `<div class=\"sub\">Trời trong vườn</div>")
rep("else if (a === 'gafeed') ga.feed();", "else if (a === 'lang'){ try { localStorage.setItem('mv2-lang', b.dataset.k); } catch (e) {} if (b.dataset.k !== LANG) location.reload(); return; } else if (a === 'gafeed') ga.feed();")
for _f in ['function bark(txt, mood = \'vui\'){', 'function say(txt, mood = \'vui\', o = {}){', 'function toast(txt, kind){']:
    rep(_f, _f + " if (EN && typeof txt === 'string') txt = enT(txt);")   # lời Ngoại, thông báo: dịch ngay lúc gọi (chữ hiện từng chữ nên không dò được trên màn)
rep("const BUILD = 'v110d'", "const BUILD = 'v111a'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
