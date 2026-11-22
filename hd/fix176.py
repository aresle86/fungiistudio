# -*- coding: utf-8 -*-
# v176 — chặng 1 cây cổ tích: giãn cấp, một lúc một cây, giãn chỗ mọc.
#
# Anh Ares báo: "1 level xuất hiện 2 cây", chỗ mọc chen chúc.
# Đo trên v175:
#   - cấp mở: 6, 9, 12, 14, 16, 18 — bốn cây cuối chỉ cách nhau 2 cấp.
#   - mỗi cây cần thêm một việc, mà mấy việc đó đếm âm thầm từ trước,
#     nên tới cấp là đủ liền. Hai cây đủ cùng lúc là ra chung một lượt.
#   - ftCheck không có chốt nào chặn: hai cây cùng gọi say() và camTo()
#     trên cùng một hẹn giờ 1500 ms, lời Ngoại đè nhau, máy quay giật hai lần.
#   - chỗ mọc: sáu cây nằm trong dải 5,9 x 2,9; cặp gần nhất 1,71.
#     Khu bụi tre (chỗ rớt đốt tre) rộng 6,8 x 5,3 — còn trống gần gấp đôi.
#
# Vá ba chuyện:
#   1. cấp mở giãn ra 6, 9, 12, 15, 18, 20.
#   2. ftGive(): một lúc một cây. Cây mới chỉ hiện khi không còn đốm sáng nào
#      chưa ai chạm (quá 3 ngày thì thôi chờ, kẻo kẹt luôn), và phải qua ngày
#      khác với cây trước. Cây đủ điều kiện mà chưa tới lượt thì giữ nguyên
#      điều kiện, lần sau xét lại — không mất.
#   3. chỗ mọc giãn xuống phần đất trống: cặp gần nhất 1,71 -> 2,91.
#      Tránh luôn mấy liếp nằm trong khu: K1 K2 K3 (bên kia rạch, z 2,85-3,65)
#      và U1 (x -4,60..-3,37, z 7,35..8,15) — không cây nào đứng trên liếp.
#      Sáu chỗ rớt đốt tre bị đè hoặc nằm sát gốc cây mới thì dời đi,
#      mọi chỗ rớt đều cách gốc cây gần nhất >= 0,9 (trước có chỗ chỉ 0,2).
import sys, io
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khớp %d lần, cần %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

# 0. số bản
rep("const BUILD = 'v175';", "const BUILD = 'v176';")

# 1. cấp mở + chỗ mọc của sáu cây
rep("'Cây vú sữa', story: 'Sự tích cây vú sữa', lv: 6, at: [-3.7, 5.9],",
    "'Cây vú sữa', story: 'Sự tích cây vú sữa', lv: 6, at: [-3.0, 4.3],")
rep("'Tre trăm đốt', story: 'Cây tre trăm đốt', lv: 9, at: [-7.0, 4.6],",
    "'Tre trăm đốt', story: 'Cây tre trăm đốt', lv: 9, at: [-6.2, 4.6],")
rep("'Trầu cau', story: 'Sự tích trầu cau', lv: 12, at: [-5.6, 7.1],",
    "'Trầu cau', story: 'Sự tích trầu cau', lv: 12, at: [-2.8, 7.2],")
rep("'Dưa hấu', story: 'Mai An Tiêm', lv: 14, at: [-8.8, 5.2],",
    "'Dưa hấu', story: 'Mai An Tiêm', lv: 15, at: [-9.2, 3.4],")
rep("'Khế vàng', story: 'Ăn khế trả vàng', lv: 16, at: [-9.6, 6.9],",
    "'Khế vàng', story: 'Ăn khế trả vàng', lv: 18, at: [-9.2, 6.8],")
rep("'Sọ Dừa', story: 'Sọ Dừa', lv: 18, at: [-8.0, 7.5],",
    "'Sọ Dừa', story: 'Sọ Dừa', lv: 20, at: [-6.4, 7.6],")

# 2. dời sáu chỗ rớt đốt tre ra khỏi gốc cây mới
rep("spots: [[-3.0, 5.6], [-4.2, 4.0], [-5.6, 6.4], [-8.6, 6.0], [-2.6, 7.9], [-6.6, 7.8], [-9.0, 3.4], [-9.4, 5.0], [-4.6, 7.2], [-7.6, 3.2], [-3.6, 3.0], [-5.2, 2.6], [-8.0, 7.0], [-6.2, 5.2], [-3.4, 6.8], [-7.0, 6.6]] }",
    "spots: [[-3.0, 5.6], [-4.2, 4.0], [-5.6, 6.4], [-8.6, 6.0], [-4.0, 6.3], [-5.4, 7.9], [-8.4, 2.8], [-9.4, 5.0], [-4.6, 7.2], [-7.6, 3.2], [-8.8, 4.4], [-5.2, 2.6], [-8.0, 7.0], [-7.2, 5.4], [-7.8, 6.2], [-7.0, 6.6]] }")

# 3. một lúc một cây
rep("\nfunction ftCheck(){ if (VISIT) return; ddCheck();",
    "\nfunction ftHold(){ if (ST.ftLast && dayK(ST.ftLast) === dayKey()) return 1; const now = Date.now();\n"
    "  return FTK.some(k => { const F = ST.ft[k]; return F && F.st === 0 && now - (F.t || 0) < 3 * 864e5; }) ? 1 : 0; }   /* còn đốm sáng nào chưa ai chạm thì cây sau chờ; chờ quá ba ngày thì thôi, kẻo kẹt luôn */\n"
    "function ftGive(k, ex){ if (ST.ft[k] || (ST.lv || 1) < FT[k].lv || ftHold()) return 0; ST.ft[k] = Object.assign({ st: 0, told: 0, t: Date.now() }, ex || {}); ST.ftLast = Date.now(); save(); return 1; }   /* một lúc một cây: chưa tới lượt thì giữ nguyên điều kiện, lần sau xét lại, không mất */\n"
    "function ftCheck(){ if (VISIT) return; ddCheck();")

rep(" if (ST.vsReady && (ST.lv || 1) >= FT.vusua.lv && !ST.ft.vusua){ ST.vsReady = 0; ST.ft.vusua = { st: 0, told: 0, t: Date.now() }; save(); } if ((ST.lv || 1) >= FT.tretramdot.lv && (ST.kqHv || 0) >= 3 && !ST.ft.tretramdot){ ST.ft.tretramdot = { st: 0, told: 0, t: Date.now(), dot: 0 }; save(); }",
    " if (ST.vsReady && ftGive('vusua')) ST.vsReady = 0; if ((ST.kqHv || 0) >= 3) ftGive('tretramdot', { dot: 0 });")

rep("  if ((ST.lv || 1) >= FT.traucau.lv && (ST.guestN || 0) + (ST.visitOut || 0) >= 5 && !ST.ft.traucau){ ST.ft.traucau = { st: 0, told: 0, t: Date.now() }; save(); }",
    "  if ((ST.guestN || 0) + (ST.visitOut || 0) >= 5) ftGive('traucau');")

rep("if (ST.dhN && ST.dhN !== dk && h >= 5 && free){ ST.ft.duahau = { st: 0, told: 0, t: Date.now() }; save(); } }",
    "if (ST.dhN && ST.dhN !== dk && h >= 5 && free) ftGive('duahau'); }")

rep("  if ((ST.lv || 1) >= FT.khevang.lv && (ST.kheHv || 0) >= 5 && !ST.ft.khevang){ ST.ft.khevang = { st: 0, told: 0, t: Date.now() }; save(); }\n"
    "  if ((ST.lv || 1) >= FT.sodua.lv && (ST.duaHv || 0) >= 3 && !ST.ft.sodua){ ST.ft.sodua = { st: 0, told: 0, t: Date.now() }; save(); }",
    "  if ((ST.kheHv || 0) >= 5) ftGive('khevang');\n"
    "  if ((ST.duaHv || 0) >= 3) ftGive('sodua');")

# 4. bản lưu cũ lỡ có hai đốm sáng: một lượt chỉ một cây lên tiếng, khỏi đè lời nhau
rep("  for (const k of FTK){ const F = ST.ft[k]; if (!F) continue; if (F.st === 0 && !F.said){ F.said = 1;",
    "  let ann = 0; for (const k of FTK){ const F = ST.ft[k]; if (!F) continue; if (F.st === 0 && !F.said && !ann){ ann = 1; F.said = 1;")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong ->', dst, len(s), 'ky tu')
