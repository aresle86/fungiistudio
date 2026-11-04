# v107b: sửa nhấp nháy đất trống. Từ v107 (draw107) tấm đất của ô trống (v.bareMat) vừa được giữ bản gốc vừa bị gộp
# thêm một bản vào vật liệu chung (màu nằm trong đỉnh), hai tấm chồng khít → z-fighting (hố ủ, đất phơi ải, đất trống đều nhấp nháy).
# Vá: đánh dấu keep cho tấm đất để mergeMeshes bỏ qua, chỉ còn bản gốc (màu đổi theo trạng thái ải/công).
# Dùng: python3 fix107b.py live/vuon3d.html live/v107b.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:60], c, n); s = s.replace(a, b)
rep("const bm = new T.Mesh(new T.BoxGeometry(w - .08, .03, l - .08, 3, 1, 2), v.bareMat); bm.position.set(cx, .0, cz); bm.receiveShadow = true; bare.add(bm); }",
    "const bm = new T.Mesh(new T.BoxGeometry(w - .08, .03, l - .08, 3, 1, 2), v.bareMat); bm.position.set(cx, .0, cz); bm.receiveShadow = true; bm.userData.keep = true; bare.add(bm); }")
rep("const BUILD = 'v107'", "const BUILD = 'v107b'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
