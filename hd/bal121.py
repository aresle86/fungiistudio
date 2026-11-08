# bal121: cân lại nhịp cấp 15–25 (anh Ares duyệt 9/11). Chạy sau perf121.py.
# 1) Nhiệm vụ cấp 15 "Lợp lại mái nhà" kẹt ở nguyên liệu: lá dừa nước và tre chỉ nằm tối đa 3 cái trên bản đồ,
#    người ghé 3 lần/ngày mất 2–3 ngày mới đủ 20 lá (bot ở cấp 15: 3,7 ngày, các cấp khác ~1,5). Giữ số xu và số lá,
#    cho bản đồ chứa tối đa 6 lá dừa, 5 cây tre cùng lúc -> khoảng 1 ngày.
# 2) Cấp 21–24 không có gì mới, cấp 25 có 2 cây. Dời sầu riêng về cấp 22, dừa sáp về cấp 24, mỗi cây kèm một món Bếp Ngoại
#    cùng cấp. Giá món = tiền nguyên liệu + ~25% (sầu riêng 180, dừa 25, đường 5, củi 3).
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

rep("ladua: { lv: roofW('ladua', 20) ? 2 : 999, max: 3,", "ladua: { lv: roofW('ladua', 20) ? 2 : 999, max: 6,")
rep("tredon: { lv: roofW('tredon', 10) ? 2 : 999, max: 3,", "tredon: { lv: roofW('tredon', 10) ? 2 : 999, max: 5,")
rep("saurieng: 25, duasap: 25 });", "saurieng: 22, duasap: 24 });")
rep("Món này Ngoại để dành đãi khách.' } };",
    "Món này Ngoại để dành đãi khách.' },\n"
    "  chesaurieng: { name: 'Chè sầu riêng', sell: 265, unit: 'chén', lv: 22, in: { saurieng: 1, dua: 1, duong: 1, cui: 1 }, t: 40 * 60, story: 'Sầu riêng nấu với nước cốt dừa, thêm hột lựu, đậu xanh. Thơm từ đầu xóm tới cuối xóm.' },\n"
    "  duasapdam: { name: 'Dừa sáp dầm', sell: 155, unit: 'trái', lv: 24, in: { duasap: 1, duong: 1 }, t: 10 * 60, story: 'Khoét nắp trái dừa sáp, dầm cơm với đường, bỏ chút đá bào. Múc từng muỗng dẻo quánh như kem.' } };")
rep('"goibuoi": "Pomelo & shrimp salad", ', '"goibuoi": "Pomelo & shrimp salad", "chesaurieng": "Durian sweet soup", "duasapdam": "Mashed wax coconut", ')
rep('"Bưởi Năm Roi tách múi, trộn tôm tép rang, rau răm. Món này Ngoại để dành đãi khách.": ',
    '"Sầu riêng nấu với nước cốt dừa, thêm hột lựu, đậu xanh. Thơm từ đầu xóm tới cuối xóm.": "Durian simmered in coconut milk with red tapioca rubies and mung beans. You can smell it from one end of the hamlet to the other.", '
    '"Khoét nắp trái dừa sáp, dầm cơm với đường, bỏ chút đá bào. Múc từng muỗng dẻo quánh như kem.": "Cut the top off a wax coconut, mash the flesh with sugar and a little shaved ice. Every spoonful is thick and soft like ice cream.", '
    '"Bưởi Năm Roi tách múi, trộn tôm tép rang, rau răm. Món này Ngoại để dành đãi khách.": ')
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
