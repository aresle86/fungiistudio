# -*- coding: utf-8 -*-
# v185: sửa ba lỗi ở chợ nổi / Bến bà con
#   1. Cục xu bị đẩy xuống một hàng riêng, lệch qua phải, chừa một lỗ trống to
#      (anh Ares khoanh đỏ): ra chợ thì đồng hồ bị giấu bằng visibility:hidden —
#      giấu kiểu đó vẫn chiếm chỗ, đẩy cục xu rớt hàng.
#   2. "Trên xuồng con · 10/10 món" trong khi trên xuồng chỉ còn 5 — số đó là
#      số đã chất trong ngày (gồm cả món bà con mua rồi), không phải số đang nằm trên xuồng.
#   3. Màn thấp (điện thoại thiệt, có thanh trình duyệt) thì bảng cao quá, trùm lên
#      thanh xu với đồng hồ ở trên đầu.
import io, sys
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khop %d lan, can %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

rep("const BUILD = 'v184'", "const BUILD = 'v185'")

# 1. giấu hẳn, đừng giấu nửa vời: display:none mới nhả chỗ ra cho cục xu lên cùng hàng với hình đại diện
rep("body.chon .ui.top > :not(#avb):not(.coin){visibility:hidden}",
    "body.chon .ui.top > :not(#avb):not(.coin){display:none}")

# 2. tách hai con số: đang nằm trên xuồng, và đã chất trong ngày
rep("  h += UX.title(cnL(`Trên xuồng con · ${on}/${CNB.cap} món`, `On your boat · ${on}/${CNB.cap}`));",
    "  const nOn = b.my.reduce((a, x) => a + x.q, 0);   /* đang nằm trên xuồng, khác với on = đã chất trong ngày */\n"
    "  h += UX.title(b.sd > 0 ? cnL(`Trên xuồng con · ${nOn} món`, `On your boat · ${nOn} items`) : cnL(`Trên xuồng con · ${nOn}/${CNB.cap} món`, `On your boat · ${nOn}/${CNB.cap}`));\n"
    "  if (b.sd > 0) h += `<div class=\"cnbox\">${cnL(`Hôm nay con chất ${on}/${CNB.cap} món, bà con mua rồi ${b.sd}.`, `You loaded ${on}/${CNB.cap} today — neighbours have bought ${b.sd}.`)}</div>`;")

# 3. bảng không trùm lên thanh trên đầu nữa.
#    .sheet đo theo content-box: cao thiệt = max-height + 8 + 16 (đệm) + 7 + 7 (viền) = +38.
#    Chừa 150px trên đầu cho thanh HUD (đo thiệt: cao 137–143) → 10 + 150 + 38 = 198, lấy tròn 200.
#    Màn cao từ 808px trở lên không đổi một li.
rep(".sheet{bottom:calc(10px + env(safe-area-inset-bottom,0px));max-height:74vh;max-height:74dvh}",
    ".sheet{bottom:calc(10px + env(safe-area-inset-bottom,0px));max-height:74vh;max-height:min(74dvh,calc(100dvh - 200px - env(safe-area-inset-top,0px) - env(safe-area-inset-bottom,0px)))}")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong', dst, len(s), 'ky tu')
