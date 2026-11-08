# dish120: món nấu, đồ muối, đồ sấy từ giống mới (anh Ares duyệt 8/11). Giá = tiền nguyên liệu + ~25% (quy tắc Bếp Ngoại;
# củi 3, đường 5 xu mua, tép 8, cá linh 12). Chạy sau perf119.py. Biểu tượng nằm trong ic119.js (đã chèn qua nc118b.py).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

# món Bếp Ngoại
rep("""cui: 1 }, t: 60 * 60, story: 'Chuối xiêm chín cây nướng với trứng, thơm cả xóm. Tết nào Ngoại cũng làm một mâm.' } };""",
    """cui: 1 }, t: 60 * 60, story: 'Chuối xiêm chín cây nướng với trứng, thơm cả xóm. Tết nào Ngoại cũng làm một mâm.' },
  goidudu: { name: 'Gỏi đu đủ', sell: 75, unit: 'dĩa', lv: 13, in: { dudu: 2, ot: 1, duong: 1 }, t: 15 * 60, story: 'Đu đủ xanh bào sợi, trộn chua ngọt với ớt. Ăn với khô cá sặc là hết sẩy.' },
  canhbau: { name: 'Canh bầu nấu tép', sell: 70, unit: 'tô', lv: 15, in: { bau: 1, tep: 2, hanh: 1, cui: 1 }, t: 25 * 60, story: 'Bầu non nấu tép bạc, nước ngọt lịm. Trưa nắng húp một tô là mát ruột.' },
  canhmuop: { name: 'Canh mướp mồng tơi', sell: 50, unit: 'tô', lv: 16, in: { muop: 1, mongtoi: 2, cui: 1 }, t: 20 * 60, story: 'Mướp với mồng tơi nấu chung, thêm chút cua đồng là canh nhà nghèo mà ai đi xa cũng nhớ.' },
  canhchuakhom: { name: 'Canh chua khóm', sell: 115, unit: 'tô', lv: 16, in: { khom: 1, cachua: 1, daubap: 1, cui: 1 }, t: 35 * 60, story: 'Canh chua miền Tây phải có khóm mới đúng vị, chua thanh, ngọt dịu.' },
  calinhkho: { name: 'Cá linh kho mía', sell: 105, unit: 'nồi', lv: 17, in: { linh: 4, mia: 1, duong: 1, cui: 1 }, t: 50 * 60, story: 'Mùa nước nổi cá linh về, kho với mía lau cho ngọt thanh, xương mềm ăn được luôn.' },
  daurongxao: { name: 'Đậu rồng xào tỏi', sell: 70, unit: 'dĩa', lv: 18, in: { daurong: 3, cui: 1 }, t: 15 * 60, story: 'Đậu rồng hái non, xắt xéo, xào lửa lớn với tỏi cho giòn.' },
  goibuoi: { name: 'Gỏi bưởi tôm', sell: 115, unit: 'dĩa', lv: 19, in: { buoi: 1, tep: 2, ot: 1 }, t: 25 * 60, story: 'Bưởi Năm Roi tách múi, trộn tôm tép rang, rau răm. Món này Ngoại để dành đãi khách.' } };""")
# khạp muối: dưa đu đủ
rep("const MUOI = {\n", "const MUOI = {\n  duadudu: { name: 'Dưa đu đủ', unit: 'hũ', lv: 13, in: { dudu: 3, muoi: 1 }, t: 12 * 3600, sell: 80, story: 'Đu đủ xanh xắt mỏng, ngâm nước mắm đường. Để dành ăn cơm cả tuần không chán.' },\n")
# lò sấy: mứt sung
rep("  mutkhe: { name: 'Mứt khế', unit: 'hũ', lv: 10,", "  mutsung: { name: 'Mứt sung', unit: 'hũ', lv: 15, in: { sung: 6, duong: 1 }, t: 6 * 3600, sell: 70, story: 'Mứt sung là món Tết của người miền Nam. Sung là sung túc, khay mứt nào cũng phải có.' },\n  mutkhe: { name: 'Mứt khế', unit: 'hũ', lv: 10,")
rep("const SAYR = { mutkhe: SAY.mutkhe,", "const SAYR = { mutsung: SAY.mutsung, mutkhe: SAY.mutkhe,")
# tiếng Anh
rep('"canhchua": "Canh chua (sour soup)", ', '"canhchua": "Canh chua (sour soup)", "goidudu": "Green papaya salad", "canhbau": "Bottle gourd & shrimp soup", "canhmuop": "Luffa & Malabar spinach soup", "canhchuakhom": "Pineapple sour soup", "calinhkho": "Linh fish braised with cane", "daurongxao": "Garlic winged beans", "goibuoi": "Pomelo & shrimp salad", "duadudu": "Pickled green papaya", "mutsung": "Candied figs", ')
# lời kể tiếng Anh
EN = {
 'Đu đủ xanh bào sợi, trộn chua ngọt với ớt. Ăn với khô cá sặc là hết sẩy.': 'Shredded green papaya tossed sweet and sour with chili. With dried gourami it is perfect.',
 'Bầu non nấu tép bạc, nước ngọt lịm. Trưa nắng húp một tô là mát ruột.': 'Young bottle gourd simmered with tiny shrimp, the broth is so sweet. A bowl on a hot noon cools you right down.',
 'Mướp với mồng tơi nấu chung, thêm chút cua đồng là canh nhà nghèo mà ai đi xa cũng nhớ.': 'Luffa and Malabar spinach in one pot, a little field crab added: a poor family soup everyone misses when they move away.',
 'Canh chua miền Tây phải có khóm mới đúng vị, chua thanh, ngọt dịu.': 'Mekong sour soup needs pineapple to taste right: gently sour, softly sweet.',
 'Mùa nước nổi cá linh về, kho với mía lau cho ngọt thanh, xương mềm ăn được luôn.': 'When the floods come the linh fish arrive. Braised with sugarcane they turn sweet, and the bones go soft enough to eat.',
 'Đậu rồng hái non, xắt xéo, xào lửa lớn với tỏi cho giòn.': 'Young winged beans, sliced on the bias and stir-fried hot with garlic so they stay crisp.',
 'Bưởi Năm Roi tách múi, trộn tôm tép rang, rau răm. Món này Ngoại để dành đãi khách.': 'Năm Roi pomelo pulled into segments, tossed with toasted shrimp and Vietnamese coriander. Grandma saves this one for guests.',
 'Đu đủ xanh xắt mỏng, ngâm nước mắm đường. Để dành ăn cơm cả tuần không chán.': 'Thin slices of green papaya pickled in fish sauce and sugar. It keeps a whole week of rice interesting.',
 'Mứt sung là món Tết của người miền Nam. Sung là sung túc, khay mứt nào cũng phải có.': 'Candied figs are a southern Tết treat. "Sung" sounds like plenty, so every candy tray has some.' }
import json as _j
rep('"Hôm nay câu đủ rồi, để cá nó sanh sôi. Mai ra câu tiếp nghe.": ', ''.join(_j.dumps(k, ensure_ascii=False) + ': ' + _j.dumps(v, ensure_ascii=False) + ', ' for k, v in EN.items()) + '"Hôm nay câu đủ rồi, để cá nó sanh sôi. Mai ra câu tiếp nghe.": ')

# lời Ngoại khi mua đồ trang trí: nói ngay lúc mua (trước đây xếp hàng "nói lúc rảnh", mỗi 15 giây một câu, có khi trễ cả phút
# sau các câu xếp trước — bài tDia113 bắt được). Vẫn chỉ nói một lần mỗi món.
rep("if (DCSAY[k]) sayOnce('dcb_' + k, DCSAY[k], 'vui');",
    "if (DCSAY[k] && !ST.seen['dcb_' + k]){ ST.seen['dcb_' + k] = 1; say(DCSAY[k], 'vui', { now: true }); }")

s = s.replace("BUILD = 'v119a'", "BUILD = 'v120a'")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
