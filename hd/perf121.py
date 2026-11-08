# perf121: chống nóng máy, đợt 2. Chạy sau gieng120.py.
# Đo (tCropTri, tSceneTri): vườn cuối game ~383 nghìn tam giác; phần lớn là chi tiết li ti (hoa, trái nhỏ, lá nhỏ, cọng)
# vẽ bằng hình cầu, lá cong nhiều đốt như vật to. Ở tầm nhìn của game các vật này chỉ rộng vài điểm ảnh.
# Giảm độ chi tiết theo kích thước, ngay tại các hàm dựng hình chung (áp cho cả rau, cây, cảnh, đồ trang trí):
#  - hình cầu: bán kính < 1,8 cm -> 4x3 mặt; < 3 cm -> tối đa 5x4; < 6 cm -> tối đa 6x5; to hơn giữ nguyên.
#  - lá: dài < 10 cm -> 3 đốt; < 20 cm -> tối đa 4 đốt; lá to giữ nguyên.
#  - ống trụ mảnh (bán kính lớn nhất < 1,2 cm): tối đa 4 cạnh.
# Đo tPerf119 vườn cuối game: 338 nghìn -> 272 nghìn tam giác mỗi hình (-20%), hình chụp trước/sau không khác (tShot121).
# Điện thoại: bóng đổ kiểu thường (PCF) thay bóng mềm (PCFSoft): mỗi điểm ảnh có bóng đọc bản đồ bóng ít lần hơn; hình chụp gần như y hệt.
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

rep("cyl = (a, b, h, n = 6) => new T.CylinderGeometry(a, b, h, n),",
    "cyl = (a, b, h, n = 6) => new T.CylinderGeometry(a, b, h, Math.max(a, b) < .012 ? Math.min(n, 4) : n),")
rep("sph = (rr, a = 8, b = 6) => new T.SphereGeometry(rr, a, b);",
    "sph = (rr, a = 8, b = 6, ...x) => { const r = Math.abs(rr); if (r < .018){ a = Math.min(a, 4); b = Math.min(b, 3); } else if (r < .03){ a = Math.min(a, 5); b = Math.min(b, 4); } else if (r < .06){ a = Math.min(a, 6); b = Math.min(b, 5); } return new T.SphereGeometry(rr, a, b, ...x); };")
rep("function leafGeo(L, Wd, fold = .35, droop = .3, seg = 6){ const k",
    "function leafGeo(L, Wd, fold = .35, droop = .3, seg = 6){ seg = L < .1 ? Math.min(seg, 3) : L < .2 ? Math.min(seg, 4) : seg; const k")
rep("r.shadowMap.type = T.PCFSoftShadowMap;", "r.shadowMap.type = MOBILE ? T.PCFShadowMap : T.PCFSoftShadowMap;")
s = s.replace("BUILD = 'v120a'", "BUILD = 'v121a'")
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
