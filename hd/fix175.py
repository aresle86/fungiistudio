# -*- coding: utf-8 -*-
# v175: chạm vô giàn thì trúng đúng giàn đó.
#
# Trước: plotHit0 chỉ "thấy" bong bóng, tán cây trái, rồi mặt đất.
# Giàn cao 1,05 không có gì để tia chạm bắt, nên tia xuyên qua giàn,
# rơi xuống đất phía sau rồi trả về một liếp khác.
# Đo trên v174 (390x844, cây đang lớn, 27 điểm rải trong khối giàn):
#   giàn G  : đúng 9/27, ra liếp khác 12/27, trôi 6/27
#   giàn Gb : đúng 10/27, ra liếp khác 12/27, trôi 5/27
#   liếp thường: đúng 22-24/27
#
# Cách vá: bắt tia vô ĐÚNG hình đang vẽ của giàn — thân dây, trái, khung giàn —
# chứ không dựng một khối hộp bao quanh. Hộp bao thì giàn ăn luôn mọi cú chạm
# vô liếp nằm sau nó (đo thử: liếp A2b mất sạch 27/27), vì giàn trống trải,
# nhìn xuyên qua thấy liếp sau rõ ràng. Bắt theo hình thật thì chạm vô chỗ có
# vẽ dây, vẽ trái mới tính là chạm giàn; chạm vô khoảng trống giữa hai cọc
# vẫn xuống tới liếp phía sau như cũ.
# Giá: 200 lần bắt tia = 1,3 ms (4 mesh đã gộp mỗi giàn), chỉ chạy lúc đặt ngón.
import sys, io

src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khớp %d lần, cần %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

# 1. hàm bắt tia vô hình thật của giàn
rep(
 "function plotHit0(cx, cy){ PBH = false;",
 "function gianHitAt(cx, cy){ const ms = []; for (const P of PLOTS){ if (!P.trellis || hidP(P) || locked(P)) continue; const v = PV[P.id]; if (!v || !v.root || !v.root.visible) continue;\n"
 "    for (const g of [v.crop, v.gianG]) if (g && g.visible && g.children.length){ g.userData.gplot = P.id; ms.push(g); } }\n"
 "  if (!ms.length) return null; ndc.set(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1); ray.setFromCamera(ndc, cam); const h = ray.intersectObjects(ms, true)[0]; if (!h) return null;\n"
 "  for (let o = h.object; o; o = o.parent) if (o.userData && o.userData.gplot) return o.userData.gplot; return null; }   /* giàn cao hơn liếp: chạm trúng dây, trúng trái, trúng khung thì tính là chạm giàn đó, kẻo tia xuyên qua giàn rơi xuống liếp phía sau. Bắt theo hình đang vẽ, không bắt theo khối hộp, để chạm vô khoảng trống giữa hai cọc vẫn tới được liếp sau */\n"
 "function plotHit0(cx, cy){ PBH = false;")

# 2. hỏi tới nó: sau tán cây trái, trước mặt đất
rep(
 "{ const th = treeHitAt(cx, cy); if (th) return th; } ndc.set(",
 "{ const th = treeHitAt(cx, cy); if (th) return th; } { const gh = gianHitAt(cx, cy); if (gh) return gh; } ndc.set(")

# 3. số bản
rep("const BUILD = 'v174'", "const BUILD = 'v175'")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong:', dst, len(s), 'ký tự')
