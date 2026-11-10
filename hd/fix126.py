# -*- coding: utf-8 -*-
# v126 sau v125: việc "góp xu" có đồ góp (Lợp lại mái nhà, Sửa sang nhà cửa) chỉ hiện trong Sổ khi đã đủ kinh nghiệm lên cấp.
# Trước đó thẻ hiện sớm với nút "Góp xu" mờ, người chơi đủ đồ đủ xu vẫn không bấm được mà không biết vì sao (thiếu kinh nghiệm).
# Lá dừa nước và tre vẫn rơi ra ở cấp 14 như cũ, Ngoại vẫn dặn gom để lợp mái.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v125'", "BUILD = 'v126'")
rep("const ready = xp >= need, early = q.t !== 'pay' || !!q.items; if (!early && !ready) return '';",
    "const ready = xp >= need, early = q.t !== 'pay'; if (!early && !ready) return '';")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', DST)
