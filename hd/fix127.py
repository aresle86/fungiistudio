# -*- coding: utf-8 -*-
# v127 sau v126: thẻ "Đơn lớn của xóm" (góp đồ cho đám) ghi số món theo kiểu đơn nhà bên: đã góp + đang có trong kho / cần.
# Trước đó chỉ ghi số đã góp nên chưa góp lần nào thì hiện 0/12 dù kho có đủ, người chơi tưởng game đếm sai.
# Thanh tiến độ bên dưới vẫn là số đã góp, ghi rõ "đã góp".
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v126'", "BUILD = 'v127'")
rep("""${X.items.map(([k, q]) => { const g = Math.min(q, X.got[k] || 0); return `<span class="oit${g >= q ? ' got' : ''}"><img src="${ICON[k]}" alt=""><i>${g}/${q}</i></span>`; }).join('')}</div><div class="xbar"><div class="kbar"><i style="width:${Math.round(gt / tot * 100)}%"></i></div><span>${gt}/${tot}</span></div>""",
    """${X.items.map(([k, q]) => { const g = Math.min(q, (X.got[k] || 0) + (ST.inv[k] || 0)); return `<span class="oit${g >= q ? ' got' : ''}"><img src="${ICON[k]}" alt=""><i>${g}/${q}</i></span>`; }).join('')}</div><div class="xbar"><div class="kbar"><i style="width:${Math.round(gt / tot * 100)}%"></i></div><span>đã góp ${gt}/${tot}</span></div>""")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', DST)
