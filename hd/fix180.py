# -*- coding: utf-8 -*-
# v180 — cây ăn trái không cần phủ rơm, trồng ở đâu cũng vậy.
#
# Anh Ares: "gốc cây có đc game tính, mà đó là gốc cây trồng ở đất mới, ko phải
# gốc cây có sẵn" → chọn hướng "Cây không cần rơm".
#
# Gốc lỗi: `mulchBeds()` lọc theo LOẠI Ô ĐẤT (`!P.tree`), không hỏi trên ô đó
# đang trồng gì. Mà liếp đất mới vẫn là liếp thường, nên trồng cây ăn trái lên
# là nó vẫn bị đếm vô việc "Phủ rơm kín các liếp".
# Đo trên v179: trồng xoài lên H1 (bãi hông nhà), S1 (mé sông), C1 (liếp ngoài)
# thì cả ba đều bị đếm; cùng cây xoài đó đứng ở T1 (gốc có sẵn) thì không.
# Thêm nữa, rơm phủ dưới gốc cây bị thân với tán che mất gần một phần ba:
# đo bằng điểm ảnh, ô đất đổi màu 7,6% (cây) so với 11,0% (liếp trống).
#
# Vá: hỏi theo CÂY ĐANG TRỒNG, không hỏi theo loại ô đất.
#   - `laCayTrai(id)` mới: ô này đang trồng cây ăn trái hay không.
#   - `mulchBeds()` và `canMulch()` bỏ qua ô đang trồng cây ăn trái
#     → không bị đếm vô việc, không mời phủ ngoài vườn, nút "Đi làm"
#       của thẻ việc cũng không chỉ vô đó nữa (nó đi theo mulchBeds).
#   - Bảng của ô trồng cây ăn trái (và gốc có sẵn) đổi ô "Rơm phủ" thành
#     một câu giải thích, đúng kiểu câu sẵn có của giàn:
#       giàn  : "Giàn trên mương · Rễ sát mương · không cần tưới"
#       cây   : "Gốc cây · Rễ ăn sâu · không cần phủ rơm"
#   - Bỏ luôn nút "Phủ rơm" ở ô trồng cây ăn trái.
#
# Không đụng tới xu, tới sản lượng, tới số rơm. Chỉ bớt việc phải làm.
# Vườn nào mọi liếp đều trồng cây ăn trái thì `mulchCheck` đã lo sẵn:
# `x.have = Math.min(x.need, E.length ? m : 1)` → không còn liếp nào thì
# việc tự tính là xong, không kẹt.
import sys, io
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khớp %d lần, cần %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

# 0. số bản
rep("const BUILD = 'v179';", "const BUILD = 'v180';")

# 1. hỏi theo cây đang trồng, không hỏi theo loại ô đất
rep("const mulchBeds = () => PLOTS.filter(P => !P.tree && !P.trellis && !hidP(P) && !locked(P) && ST.plots[P.id]);",
    "const laCayTrai = id => { const p = ST.plots[id]; return !!(p && p.crop && CROPS[p.crop] && CROPS[p.crop].tree); };   /* cây ăn trái không cần phủ rơm: ở gốc có sẵn hay ở liếp đất mới cũng vậy */\n"
    "const mulchBeds = () => PLOTS.filter(P => !P.tree && !P.trellis && !hidP(P) && !locked(P) && ST.plots[P.id] && !laCayTrai(P.id));")

# 2. ngoài vườn cũng đừng mời phủ gốc cây
rep("const canMulch = P => P && !P.tree && !P.trellis && !hidP(P) && !locked(P) && ST.plots[P.id] && !(ST.plots[P.id].mulch > ST.gt);",
    "const canMulch = P => P && !P.tree && !P.trellis && !hidP(P) && !locked(P) && ST.plots[P.id] && !laCayTrai(P.id) && !(ST.plots[P.id].mulch > ST.gt);")

# 3. bảng gốc cây: thay ô "Rơm phủ" bằng câu giải thích, kiểu câu của giàn
rep("""    if (!P.tree) h += '<div class="uxs one">' + UX.card('Rơm phủ', mulched ? `còn ${fmtT((p.mulch - ST.gt) / ST.spd)} <small>· giữ ẩm, lớn nhanh hơn</small>` : 'Chưa phủ <small>· phủ rơm giữ ẩm lâu, cây lớn nhanh</small>', '', mulched ? 'go' : '') + '</div>'; }""",
    """    h += '<div class="uxs one">' + (P.tree || laCayTrai(id) ? UX.card('Gốc cây', 'Rễ ăn sâu <small>· không cần phủ rơm</small>') : UX.card('Rơm phủ', mulched ? `còn ${fmtT((p.mulch - ST.gt) / ST.spd)} <small>· giữ ẩm, lớn nhanh hơn</small>` : 'Chưa phủ <small>· phủ rơm giữ ẩm lâu, cây lớn nhanh</small>', '', mulched ? 'go' : '')) + '</div>'; }""")

# 4. bỏ nút Phủ rơm ở ô trồng cây ăn trái
rep("  if (!P.trellis && !P.tree) acts.push(UX.btn('mulch', `Phủ rơm · còn ${rom}`, { dis: rom < 1 || mulched }));",
    "  if (!P.trellis && !P.tree && !laCayTrai(id)) acts.push(UX.btn('mulch', `Phủ rơm · còn ${rom}`, { dis: rom < 1 || mulched }));")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong ->', dst, len(s), 'ky tu')
