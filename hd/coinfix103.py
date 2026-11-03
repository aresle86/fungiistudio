#!/usr/bin/env python3
"""v103: bỏ chữ báo số cấp tương lai ở bảng trang trí."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
rep("return UX.hero(UIC.dc_rao_go, 'Trang trí vườn', `Tới cấp ${DC.lv} mới trang trí vườn được con`);", "return UX.hero(UIC.dc_rao_go, 'Trang trí vườn', 'Chăm vườn thêm ít bữa nữa rồi mình trang trí nghe con');")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
