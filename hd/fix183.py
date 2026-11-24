# -*- coding: utf-8 -*-
# v183 — Sổ cổ tích nói rõ mỗi cây cho gì
import io, sys
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khop %d lan, can %d: %s' % (c, n, a[:100])
    s = s.replace(a, b)

rep("const BUILD = 'v182'", "const BUILD = 'v183'")

# 1. CSS cho dòng "cây cho gì"
rep(".ftc em{font-style:normal;font-size:12px;background:#F1E8D6;border-radius:999px;padding:2px 8px;color:#6B4529}",
    ".ftc em{font-style:normal;font-size:12px;background:#F1E8D6;border-radius:999px;padding:2px 8px;color:#6B4529}\n.ftc .loi{display:block;margin:8px 0 2px;padding:8px 12px;background:#F6EFDC;border-radius:10px;font-size:13px;line-height:1.4;color:#6B4529}")

# 2. bảng lợi của từng cây
FTLOI = u"""const FTLOI = {
  vusua: () => L135('Lớn rồi thì mỗi ngày hái được 2 trái vú sữa. Để cúng ông Địa, tặng bạn, hay bán ở chợ.', 'Once grown it gives 2 star apples a day — to offer at the shrine, give to friends, or sell at the market.'),
  tretramdot: () => L135('Lớn rồi thì chạm vô là hô Khắc xuất, Khắc nhập — trăm đốt tre rời ra rồi dính lại cho con coi chơi.', 'Once grown, tap it to call out "Khắc xuất! Khắc nhập!" and watch the hundred joints fly apart and snap back together.'),
  traucau: () => L135('Lớn rồi thì mỗi ngày têm được 3 miếng trầu. Bạn bè ghé thì mời, không thì bán ở chợ.', 'Once grown it folds 3 betel quids a day — offer them to visiting friends, or sell them at the market.'),
  duahau: () => L135('Lớn rồi thì hai bữa cho một trái dưa, trên vỏ khắc tên con.', 'Once grown it gives one melon every two days, with your name carved on the rind.'),
  khevang: () => L135('Lớn rồi thì mỗi tuần chim ghé để lại một cục vàng. Một cục trừ được ba trăm xu khi mua đồ kiểng hay sửa nhà.', 'Once grown, the bird leaves a gold nugget every week. Each nugget covers three hundred xu on ornaments or house repairs.'),
  sodua: () => L135('Lớn rồi thì chừng hai chục phút Sọ Dừa lăn ra tưới giùm con một liếp khô.', 'Once grown, about every twenty minutes Sọ Dừa rolls out to water a dry bed for you.') };
"""
rep("function pgCotich(part){", FTLOI + "function pgCotich(part){")

# 3. gắn dòng đó vào thẻ của cây đã có
rep("${D.parts.slice(0, F.told).map(x => `<p>${x}</p>`).join('')}${BIGD[k] && !VISIT && baiOn() ?",
    "${D.parts.slice(0, F.told).map(x => `<p>${x}</p>`).join('')}${FTLOI[k] ? `<span class=\"loi\">${FTLOI[k]()}</span>` : ''}${BIGD[k] && !VISIT && baiOn() ?")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong', dst, len(s), 'byte')
