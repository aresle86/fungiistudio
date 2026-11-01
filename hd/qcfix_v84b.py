# QC v84b: tối ưu hiển thị cho điện thoại (chạy sau qcfix_v84.py).
import sys
P = sys.argv[1] if len(sys.argv) > 1 else 'live/vuon3d.html'
s = open(P, encoding='utf-8').read(); log = []
def rep(old, new, n=1, tag=''):
    global s
    c = s.count(old)
    if c != n: sys.exit(f'FAIL [{tag}] khớp {c} lần, cần {n}: {old[:80]!r}')
    s = s.replace(old, new); log.append(tag)

# A. 8 đèn điểm (7 đèn dầu/đèn bão + ánh trăng) nằm trong shader mọi lúc, kể cả ban ngày cường độ 0.
#    Tắt hẳn khi trời sáng → shader ban ngày không lặp qua 8 đèn. Chỉ đổi lúc chạng vạng/rạng sáng.
rep("const MOONFILL = new T.PointLight('#c9d6ff', 0, 11, .9);",
    "let LON8 = null; const MOONFILL = new T.PointLight('#c9d6ff', 0, 11, .9);", tag='biến bật đèn')
rep("+ (Math.random() < .02 ? -.25 : 0));\n",
    "+ (Math.random() < .02 ? -.25 : 0));\n  { const lon = night > .01; if (lon !== LON8){ LON8 = lon; MOONFILL.visible = lon; for (const l of LIGHTS) l.L.visible = lon; } }\n", tag='tắt đèn ban ngày')

# B. Bóng đổ vẽ lại mỗi frame (≈830 mesh đổ bóng). Mức đồ hoạ 0–1 (điện thoại): vẽ bóng cách 1 frame.
rep("  r.render(S, cam);\n  // UI",
    "  if (r.shadowMap.enabled){ r.shadowMap.autoUpdate = QI >= 2; if (QI < 2 && (SHF = (SHF + 1) % 2) === 0) r.shadowMap.needsUpdate = true; }\n  r.render(S, cam);\n  // UI", tag='bóng cách frame')
rep("const TERR = new Set();", "const TERR = new Set(); let SHF = 0;", tag='biến SHF')

open(P, 'w', encoding='utf-8').write(s); print('OK', ', '.join(log))

# C. Bảng gà: dòng máng "đủ chừng 0 giây" khi mái duy nhất đang ấp
s = open(P, encoding='utf-8').read(); log = []
rep("${food ? 'đủ chừng ' + fmtT(lasts) : 'hết rồi'}",
    "${food ? (lay > 0 ? 'đủ chừng ' + fmtT(lasts) : 'mái đang ấp, máng để dành') : 'hết rồi'}", tag='máng gà khi ấp')
open(P, 'w', encoding='utf-8').write(s); print('OK', ', '.join(log))
