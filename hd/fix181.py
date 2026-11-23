# -*- coding: utf-8 -*-
# v181 — cây ăn trái mở khoá rồi là hàng xóm bắt đầu đặt, để người chơi có cớ đi trồng.
#
# Anh Ares: "cây đã mở thì hàng xóm bắt đầu order để cho người chơi còn đi lo trồng."
#
# Gốc lỗi: `ordCanMake` với cây ăn trái đòi **vườn đang có sẵn cây đó**
# (`CROPS[k].tree ? PLOTS.some(P => ST.plots[P.id].crop === k) : ...`).
# Nên: không có đơn → không có cớ trồng → không trồng → không bao giờ có đơn.
# Đo trên v180, vườn cấp 20 chỉ trồng cải với hành: 24 giống mở khoá,
# 14 được đặt, 10 không bao giờ được đặt — cả 10 đều là cây ăn trái.
#
# Vá: thêm một loại đơn riêng, "đơn đặt trước trái cây" (`o.hen = 1`),
# sinh ở đầu `ordMake`, cùng chỗ với đơn mâm cơm.
#   - Chỉ nhắm cây ăn trái **đã mở khoá mà vườn chưa trồng**.
#   - **Một món thôi**, số lượng bằng đúng số lượng trái thường ngày
#     (`yield * .4`, ít nhất 2) — không gộp chung với rau cá trứng.
#   - **Một lúc một đơn** (`!L0.some(o => o.hen)`).
#   - 50% mỗi lần sinh đơn, nên nó tới thong thả chứ không dồn.
# Hai cái chốt đó là để đơn đừng thành không giao nổi: đơn nhiều món mà
# lẫn một trái chưa có cây thì cả đơn kẹt theo, mà bảng đơn chỉ có 3-5 chỗ.
#
# Đường đặt trái cũ (trái làm món phụ trong đơn nhiều món) GIỮ NGUYÊN luật
# "phải có cây rồi mới đặt", nên đơn thường vẫn giao được như cũ.
#
# Không đụng tới giá, tới xu thưởng: đơn này tính tiền bằng đúng công thức
# chung (`val * ORD.mul`).
import sys, io
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khớp %d lần, cần %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

# 0. số bản
rep("const BUILD = 'v180';", "const BUILD = 'v181';")

# 1. đơn đặt trước trái cây
rep("  const items = [], add = (k, q) => { if (k && q > 0 && !items.some(([x]) => x === k)) items.push([k, q]); };",
    "  if (!L0.some(o => o.hen) && Math.random() < .5){   /* đơn đặt trước trái cây: cây mở khoá rồi mà vườn chưa trồng thì hàng xóm hỏi mua trước, cho người chơi có cớ đi trồng */\n"
    "    const chuaTrong = k => !PLOTS.some(P => ST.plots[P.id] && ST.plots[P.id].crop === k);\n"
    "    const ht = Object.keys(CROPS).filter(k => CROPS[k].tree && !CROPS[k].rare && unlocked(k) && chuaTrong(k) && !open.has(k));\n"
    "    const k0 = pick1(ht);\n"
    "    if (k0){ const q0 = Math.max(2, Math.round((CROPS[k0].yield || 4) * .4)); last[k0] = now; const v0 = q0 * ttSell(k0);\n"
    "      return { id: Date.now() + '' + Math.floor(Math.random() * 1e4), who, why: `nghe nói vườn con sắp có ${GD(k0).name.toLowerCase()}, dặn trước một mớ`, items: [[k0, q0]], xu: Math.round(v0 * ORD.mul / 5) * 5, xp: Math.max(3, Math.round(v0 * ORD.mul / 10)), hen: 1 }; } }   /* một lúc một đơn, và chỉ một món, kẻo đơn nhiều món lẫn trái chưa có cây là kẹt cả đơn */\n"
    "  const items = [], add = (k, q) => { if (k && q > 0 && !items.some(([x]) => x === k)) items.push([k, q]); };")

# 2. cho lời đơn của mình được hiện: bảng đơn đang tự viết lại lời cho đơn thường
rep("const ordWhyOf = o => o.ghe || o.lead || o.mam || o.quy ? o.why : ordWhy(o.items, o.id);",
    "const ordWhyOf = o => o.ghe || o.lead || o.mam || o.quy || o.hen ? o.why : ordWhy(o.items, o.id);   /* đơn đặt trước trái cây giữ nguyên lời của nó, đừng để ordWhy viết đè */")

# 3. đơn đặt trước không ghép chữ "mua về" phía trước, giống đơn mâm cơm
rep("${o.mam ? '' : 'mua về '}${ordWhyOf(o)}", "${o.mam || o.hen ? '' : 'mua về '}${ordWhyOf(o)}")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong ->', dst, len(s), 'ky tu')
