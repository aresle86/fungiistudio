# v149b: lời giải thích mâm ngũ quả ở việc "Sửa sang nhà cửa" (người chơi không hiểu sao sửa nhà lại đòi sung).
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v149'", "BUILD = 'v149b'")
OLD = "Tiền mua gạch tàu, sơn cửa. Mâm ngũ quả mãng cầu, sung, dừa, đu đủ, xoài chưng bàn thờ ông Thiên, cầu sung vừa đủ xài. Nấu 3 nồi đãi thợ. Sửa chừng tám tiếng, bạn ghé phụ thì mau hơn"
NEW = "Tiền mua gạch tàu, sơn cửa. Sửa nhà phải cúng ông Thiên trước: mâm ngũ quả xứ mình đọc trại ra là lời cầu, cầu sung vừa đủ xài. Nấu 3 nồi đãi thợ. Sửa chừng tám tiếng, bạn ghé phụ thì mau hơn"
rep(OLD, NEW, 2)
rep("Coins buy bricks and paint. A five-fruit tray of sugar apple, fig, coconut, papaya and mango for the sky-god altar: in the south the names sound like a wish for just enough. Cook 3 pots",
    "Coins buy bricks and paint. Before fixing a house, folks offer a five-fruit tray to the sky god: read aloud, the fruit names sound like a wish for just enough to live on. Cook 3 pots")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
