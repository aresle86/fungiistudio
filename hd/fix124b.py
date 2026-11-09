# -*- coding: utf-8 -*-
# v124b sau v124a: chống nóng đợt 3. Điện thoại màn 120 Hz (iPhone Pro…): khi đang chạm chỉ vẽ tối đa 60 hình/giây (trước đó vẽ 120).
# (Đã thử "đóng băng" vật đứng yên: tiết kiệm ma trận ngang công kiểm tra, không lợi, bỏ.)
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v124a'", "BUILD = 'v124b'")
rep("gap = idle ? (fn - FRH > 60000 ? 80 : AQ.lv >= 1 || fn - FRH > 8000 ? 45 : 30) : 0;", "gap = idle ? (fn - FRH > 60000 ? 80 : AQ.lv >= 1 || fn - FRH > 8000 ? 45 : 30) : MOBILE ? 15 : 0;")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
