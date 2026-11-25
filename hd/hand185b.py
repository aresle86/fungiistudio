# -*- coding: utf-8 -*-
# Ghi việc đẩy v183 + v184 + v185 lên live vô HANDOFF.md
import io
p = '/Users/macintoshhd/Documents/fungiistudio/hd/HANDOFF.md'
s = io.open(p, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khop %d lan, can %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

rep("| Bản live | **v182** (23/11/2026),", "| Bản live | **v185** (25/11/2026),")

rep("| Nguồn game | `hd/live/vuon3d.html` trên nhánh **`mietvuon2-dev`** (= v182, khớp live). Bản mới nhất là **v185, đã dựng, CHƯA ĐẨY** (`live/v182.html` → `fix183.py` → `live/v183.html` → `fix184.py` → `live/v184.html` → `fix185.py` → `live/v185.html`). Mỗi bản = một script vá |",
    "| Nguồn game | `hd/live/vuon3d.html` trên nhánh **`mietvuon2-dev`** (= v185, khớp live). Mỗi bản = một script vá: `live/v182.html` → `fix183.py` → `live/v183.html` → `fix184.py` → `live/v184.html` → `fix185.py` → `live/v185.html` |")

rep("| Việc kế tiếp | **Đẩy v183 + v184 + v185** khi anh Ares nhắn (ba bản đi chung một lần cho gọn; v185 sửa lỗi anh báo từ iPhone nên nên đẩy sớm). Rồi **thêm cỡ màn ngắn vô bộ đo** — xem mục v185. Rồi",
    "| Việc kế tiếp | **Thêm cỡ màn ngắn vô bộ đo** — dọn 23 chỗ `sat` có sẵn ở 393×640 rồi thêm cỡ đó vô cổng bắt buộc, để máy đo thấy được màn điện thoại thiệt có thanh trình duyệt (xem mục v185). Rồi")

rep("| Artifact game | https://claude.ai/artifact/DkesRLV6eCUtN56HxQnwiT (**v182**, bản 163).",
    "| Artifact game | https://claude.ai/artifact/DkesRLV6eCUtN56HxQnwiT (**v185**, bản 164).")

a = "\n## v185 (24/11/2026) — ba lỗi ở chợ nổi, anh Ares báo từ iPhone thật"
assert s.count(a) == 1
them = (u"\n**Đẩy xong (25/11), v183 + v184 + v185 đẩy chung một lần** — anh Ares nhắn \"Đẩy cả ba\". "
        u"Cùng một đường như mấy bản trước: `cp live/v185.html live/vuon3d.html` → commit `afaf81f` trên `mietvuon2-dev` → "
        u"`buildsite.py` → kiểm ngược đúng công thức `head + nguồn (đổi tiêu đề) + \"\\n</body></html>\\n\"`, ra `True` → "
        u"commit `main` bằng plumbing trên nền `61a62d4` (**không checkout**; `read-tree` giữ nguyên bốn file nhạc chỉ có trên `main`, đã kiểm còn đủ) → "
        u"`c08a86c` → push `mietvuon2-dev main main:mietvuon2-online`. So với bản live cũ chỉ đổi một file, 21 dòng thêm 8 dòng bớt. "
        u"Bản live thật: HTTP 200, 2.523.111 byte, `BUILD = 'v185'`, có đủ vết của cả ba bản (`FTLOI`, `ttGi`, `display:none` ở thanh chợ, dòng \"Hôm nay con chất\"), "
        u"**giống hệt từng byte** với bản mình dựng. Artifact game **bản 164** (version id `1795580567-5c42`), changelog Doc thêm ba mục v183, v184, v185 (rev 186).\n"
        u"\n*Lưu ý nhỏ về Artifact:* dịch vụ Artifact cảnh báo trang có chỗ cho người xem tải file mà khung Artifact không cấp quyền tải — "
        u"đó là nút xuất bản lưu trong game, trên bản live thật thì chạy được, chỉ bản Artifact là không. Lỗi có sẵn từ lâu, không phải v185 đẻ ra.\n")
s = s.replace(a, them + a, 1)

io.open(p, 'w', encoding='utf-8').write(s)
print('xong ghi viec day')
