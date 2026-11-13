# -*- coding: utf-8 -*-
# v143b: anh Ares 13/11 — tới cấp 4 là có đơn Cải xanh xào liền, chưa nhóm bếp cũng có, để người chơi biết mà đi nấu.
# Đơn chưa nhóm bếp thì thẻ đơn nhắc thêm "nhóm bếp Ngoại rồi nấu nghe".
import sys, io
SRC, DST = sys.argv[1], sys.argv[2]
s = io.open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep(u"BUILD = 'v143a'", u"BUILD = 'v143b'")
rep(u"var LEAD = [{ k: 'caixao', q: 1, lv: 4, by: 'nb', ok: () => (ST.bep && (ST.bep.lit || Object.keys(ST.bep.made || {}).length > 0)) || has('caixao') > 0 },   /* v143a: đơn mở hàng của bếp là cải xanh xào */",
    u"var LEAD = [{ k: 'caixao', q: 1, lv: 4, by: 'nb', ok: () => true },   /* v143b: tới cấp 4 là có đơn cải xanh xào, chưa nhóm bếp cũng có */")
rep(u"<span>mua về ${ordWhyOf(o)}</span>",
    u"<span>mua về ${ordWhyOf(o)}${o.lead && DISH[o.lead] && !(ST.bep && ST.bep.lit) ? L135(' · nhóm bếp Ngoại rồi nấu nghe', ' · light Ngoại\\'s stove, then cook') : ''}</span>")
io.open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
