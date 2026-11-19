# v166 -> v167:
# Gác bếp nới thêm chỗ (Ares duyệt "Cách 2" 19/11/2026): mua được 10 kệ thay vì 5.
#   Kệ 1-5: +10 chỗ mỗi kệ (như cũ, tối đa 70). Kệ 6-10: +15 chỗ mỗi kệ -> tối đa 145 chỗ.
#   Giá giữ đà cũ 150 + 100 x số kệ đã có: kệ 6-10 là 650, 750, 850, 950, 1.050 xu (tổng 4.250).
#   Lý do: gác bếp có 37 thứ (23 món nấu, 5 phơi, 3 muối, 6 sấy), ghe chợ nổi đặt 3-30 cái mỗi món, 70 chỗ không trữ sẵn nổi.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v166'", "BUILD = 'v167'")
rep("let GB_CAP = 20; const GBX_MAX = 5,", "let GB_CAP = 20; const gbCapN = n => 20 + 10 * Math.min(5, n || 0) + 15 * Math.max(0, (n || 0) - 5), GBX_MAX = 10,")
rep("GB_CAP = 20 + 10 * (ST.gbx || 0);", "GB_CAP = gbCapN(ST.gbx);")
rep("GB_CAP = 20 + 10 * ST.gbx;", "GB_CAP = gbCapN(ST.gbx);", 2)
rep("Mỗi kệ tre chứa thêm 10 món khô, món nấu.", "Mỗi kệ tre chứa thêm 10 tới 15 món khô, món nấu.", 3)
rep("Each bamboo shelf holds 10 more", "Each bamboo shelf holds 10 to 15 more", 2)
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
