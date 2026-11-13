# -*- coding: utf-8 -*-
# v143a: bếp giờ có món nấu được ngay ở cấp 4 nên đơn "mở hàng" của bếp đổi từ Trứng chiên hành (cấp 4 chưa có trứng)
# sang Cải xanh xào, và hiện ngay khi bếp đã nhóm (trước đó phải nấu xong một món mới có đơn). Anh Ares 13/11.
import sys, io
SRC, DST = sys.argv[1], sys.argv[2]
s = io.open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep(u"BUILD = 'v143'", u"BUILD = 'v143a'")
rep(u"var LEAD = [{ k: 'trungchien', q: 1, lv: 4, by: 'nb', ok: () => (ST.bep && Object.keys(ST.bep.made || {}).length > 0) || has('trungchien') > 0 },",
    u"var LEAD = [{ k: 'caixao', q: 1, lv: 4, by: 'nb', ok: () => (ST.bep && (ST.bep.lit || Object.keys(ST.bep.made || {}).length > 0)) || has('caixao') > 0 },   /* v143a: đơn mở hàng của bếp là cải xanh xào */")
io.open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
