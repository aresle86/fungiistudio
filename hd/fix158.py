# v157 -> v158: bao hạt lạ tăng giá 40 -> 120 xu (Ares chốt 16/11/2026: 3 hạt rau đáng ~93 xu, bán 40 xu là quá rẻ so với tiệm).
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)

rep("BUILD = 'v157'", "BUILD = 'v158'")
rep("const BLA = { gia: 40,", "const BLA = { gia: 120,")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
