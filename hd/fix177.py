# -*- coding: utf-8 -*-
# v177 — Khô cá đồng có hình riêng.
#
# Anh Ares báo: "2 icon khô bị trùng lặp ko biết là khô gì là khô gì khi nhận đc order".
# Gốc: trong bảng mượn hình có dòng ['khocadong', 'khocasac'] — Khô cá đồng
# cố ý xài chung hình với Khô cá sặc, và O.khocadong chưa từng được nặn.
# Hai món lại cùng cấp 9, cùng bán theo "xâu", nên thẻ đơn hàng không phân biệt nổi.
#
# Vá hai chỗ:
#   1. nặn O.khocadong: cái mẹt (nia, dùng chung với Ớt khô / Chuối phơi) với năm
#      con cá đồng lớn nhỏ không đều, nằm xoay đủ hướng, mỗi con có sống lưng sẫm.
#      Dáng NẰM, khác hẳn dáng ĐỨNG (xâu treo que tre) của Khô cá sặc — ở cỡ 44px
#      một bên là que ngang, một bên là dĩa tròn sẫm.
#      Không gọi R() nên chuỗi ngẫu nhiên của mấy icon sau giữ nguyên.
#   2. bỏ dòng mượn hình của khocadong; ICON[k] tự dựng từ O nên có hình riêng liền.
#      Cặp canho -> caro giữ nguyên (anh Ares chưa yêu cầu đổi).
#
# Hình đã gửi anh Ares duyệt trước khi gắn (trang coi thử: lp/khodong.html).
import sys, io
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khớp %d lần, cần %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

# 0. số bản
rep("const BUILD = 'v176';", "const BUILD = 'v177';")

# 1. nặn mô hình, đặt ngay sau Khô cá sặc / Khô cá lóc
rep("  // ---- DƯA CẢI MUỐI: hũ thủy tinh thấy dưa cải vàng xanh trong nước muối ----",
    "  // ---- KHÔ CÁ ĐỒNG: cá đồng lớn nhỏ không đều, xẻ phơi nằm trên nia ----\n"
    "  O.khocadong = p => { const n = nia(p), F = [[-.14, -.13, .55, .42, '#C68E44', '#E2B46C'], [.15, -.14, -1.05, .36, '#B4803A', '#D4A65E'], [-.16, .15, -.25, .38, '#CF9A4E', '#EABC78'], [.16, .14, 1.35, .30, '#AD7832', '#CC9E56'], [.00, -.01, 2.60, .26, '#C28C42', '#DEB068']];\n"
    "    for (let k = 0; k < F.length; k++){ const [x, z, h, L, c1, c2] = F[k], g = grp(n, x, .030 + k * .004, z, -Math.PI / 2, 0, h);\n"
    "      add(g, new T.ExtrudeGeometry(fishShape(L, L * .34), { depth: .024, bevelEnabled: false }), c1);\n"
    "      add(g, new T.ShapeGeometry(fishShape(L * .76, L * .2)), c2, 0, 0, .026);\n"
    "      add(g, new T.BoxGeometry(L * .56, L * .03, .007), '#7A5226', L * .02, 0, .029);\n"
    "      add(g, new T.SphereGeometry(L * .04, 4, 3), '#2A1E14', L * .31, L * .055, .029); } };   /* khac han xau treo que cua kho ca sac: mon nay nam ngang tren met */\n"
    "  // ---- DƯA CẢI MUỐI: hũ thủy tinh thấy dưa cải vàng xanh trong nước muối ----")

# 2. bỏ dòng mượn hình
rep("[['nong2', 'nong'], ['khap2', 'khap'], ['say2', 'say'], ['khocadong', 'khocasac'], ['canho', 'caro']]",
    "[['nong2', 'nong'], ['khap2', 'khap'], ['say2', 'say'], ['canho', 'caro']]")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong ->', dst, len(s), 'ky tu')
