#!/usr/bin/env python3
"""v106: bớt tiếng xì nền. Nước mương là nhiễu lọc 2,5 kHz kêu đều mọi lúc (sàn .012 dù ở xa) nên nghe như xì xì.
Nay: nước 900 Hz trầm như róc rách, chỉ nghe gần mương, nhấp nhô; lá và gió lặng hẳn giữa các cơn.
Chạy sau ui106.py:  python3 aud106.py live/v106a.html live/v106a.html"""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

rep("water: mk('bandpass', 2500, 1.3)", "water: mk('bandpass', 900, .9)")
rep("BED.wind.g.gain.setTargetAtTime(.004, g0 + up + hold, dn / 3);", "BED.wind.g.gain.setTargetAtTime(.0005, g0 + up + hold, dn / 3);")
rep("BED.leaf.g.gain.setTargetAtTime(pk * .35, g0 + .3, up / 3); BED.leaf.g.gain.setTargetAtTime(.002, g0 + up + hold, dn / 3);",
    "BED.leaf.g.gain.setTargetAtTime(pk * .2, g0 + .3, up / 3); BED.leaf.g.gain.setTargetAtTime(.0002, g0 + up + hold, dn / 3);")
rep("BED.water.g.gain.setTargetAtTime((.012 + .045 * wv) * (.75 + .25 * Math.sin(now * 1.7) * Math.sin(now * .63)), t, .3);",
    "BED.water.g.gain.setTargetAtTime(.032 * wv * wv * (.55 + .45 * Math.sin(now * 2.3) * Math.sin(now * .71)), t, .3);   /* nước chỉ nghe gần mương, róc rách từng đợt */")
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
