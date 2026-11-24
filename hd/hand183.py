# -*- coding: utf-8 -*-
# Ghi v183 vo HANDOFF.md + sua lai ghi chu sai ve cay co tich
import io, sys
p = '/Users/macintoshhd/Documents/fungiistudio/hd/HANDOFF.md'
s = io.open(p, encoding='utf-8').read()
GATE = sys.argv[1] if len(sys.argv) > 1 else 'CHUA DO'

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khop %d lan, can %d: %s' % (c, n, a[:100])
    s = s.replace(a, b)

rep("| Nguồn game | `hd/live/vuon3d.html` trên nhánh **`mietvuon2-dev`** (= v182, khớp live). Mỗi bản = một script vá: `live/v180.html` → `fix181.py` → `live/v181.html` → `fix182.py` → `live/v182.html` |",
    "| Nguồn game | `hd/live/vuon3d.html` trên nhánh **`mietvuon2-dev`** (= v182, khớp live). Bản mới nhất là **v183, đã dựng, CHƯA ĐẨY** (`live/v182.html` → `fix183.py` → `live/v183.html`). Mỗi bản = một script vá |")

rep("| Việc kế tiếp | **Chặng 3 của kho** (chưa bàn, chưa duyệt): hàng nút lọc (Tất cả · Rau · Trái · Cá · Khô · Món), và có thể thêm ô tìm — anh Ares nói dùng thử v179 coi còn thấy thiếu không rồi tính. **Chặng 3 của kho** (chưa bàn, chưa duyệt): hàng nút lọc (Tất cả · Rau · Trái · Cá · Khô · Món), và có thể thêm ô tìm. **Chặng 2 cây cổ tích: mỗi cây một tác dụng** — năm cây chưa có gì (chỉ Sọ Dừa có `sdHelp`), `FT` chưa có ô phần thưởng; đụng tới xu nên chờ anh chốt số. Rồi **cấp 21–30** theo `hd/ke-hoach-cap-21-30.md`, chặng A (Chợ huyện + tiệm may) trước |",
    "| Việc kế tiếp | **Đẩy v183** khi anh Ares nhắn. Rồi **tác dụng cho tre trăm đốt** — cây duy nhất lớn rồi mà không cho gì (xem mục v183); đụng tới xu nên chờ anh chốt số. Rồi **chặng 3 của kho** (chưa bàn, chưa duyệt): hàng nút lọc (Tất cả · Rau · Trái · Cá · Khô · Món), có thể thêm ô tìm — anh Ares nói dùng thử v179 coi còn thấy thiếu không rồi tính. Rồi **cấp 21–30** theo `hd/ke-hoach-cap-21-30.md`, chặng A (Chợ huyện + tiệm may) trước |")

a = "\n## v182 (23/11/2026) — bảng ao cá nói ra cái lợi, thay vì giấu"
assert s.count(a) == 1

sec = u"""
## v183 (24/11/2026) — Sổ cổ tích nói rõ mỗi cây cho gì

**BẢN NHÁP — đã dựng, CHƯA ĐẨY.** `fix183.py`, v182 → v183. Anh Ares: "chặng 2 cổ tích đi".

**Ghi chú cũ trong hồ sơ này SAI, đã sửa.** Hồ sơ ghi "năm cây chưa có tác dụng, chỉ Sọ Dừa có `sdHelp`". Đọc lại `ftTap()` thì **năm trên sáu cây đã có tác dụng thật từ lâu**:

| Cây | Cấp | Tác dụng đang có trong code | Quy ra xu |
|---|---|---|---|
| Vú sữa | 6 | 2 trái vú sữa/ngày (`F.fd === dayKey()`), kho giữ tối đa 6 | 80 xu/ngày (sell 40, `giu: true` nên không vô đơn hàng) |
| Tre trăm đốt | 9 | `ttMagic()` — Khắc xuất / Khắc nhập, **chỉ là màn phép cho vui** | **0** |
| Trầu cau | 12 | 3 miếng trầu/ngày, kho giữ tối đa 6 | 60 xu/ngày (sell 20, `giu: true`) |
| Dưa hấu | 15 | 1 trái dưa khắc tên, mỗi 2 ngày | 20 xu/ngày (sell 40) |
| Khế vàng | 18 | 1 cục vàng/tuần (`F.wk !== wkKey()`), `ST.vang` trừ 300 xu khi mua đồ kiểng / sửa nhà | ~43 xu/ngày |
| Sọ Dừa | 20 | `sdHelp()` — chừng 20 phút lăn ra tưới giùm một liếp khô | không ra xu, đỡ công |

**Lỗ hổng thiệt sự là CHỮ, y như ao cá ở v182.** `pgCotich()` chỉ in tên cây, tên truyện và các đoạn truyện — **không một chữ nào nói cây cho gì**. Người chơi phải tự mò mới biết chạm cây được trái.

**Đã vá** — thêm `FTLOI`, một câu cho mỗi cây, viết bằng `L135(vi, en)`:
- Hiện ngay khi cây **mới mọc** (`F.st >= 1`), không chờ lớn, nên người chơi biết trước mình đang nuôi cái gì. Câu mở bằng "Lớn rồi thì…" nên đọc lúc nào cũng đúng.
- **Không hiện** với đốm sáng chưa chạm và cây chưa có (`???`) — khỏi lộ trước.
- CSS mới: `.ftc .loi` (hộp be, bo góc 10, padding 8/12).

**Còn hở: tre trăm đốt lớn rồi vẫn không cho gì.** Hai hướng đề xuất, chờ anh Ares chốt:
1. **Đốt tre để dành** — 3 đốt/ngày, bán 20 xu → 60 xu/ngày, ngang trầu cau. Cần thêm một món mới trong kho và một hình mới (phải gửi anh duyệt hình trước).
2. **Giàn sai trái hơn** — khổ qua / bầu / mướp trên giàn mỗi lứa thêm 1 trái (`yield` 2 → 3, +50%). Không cần món mới, không cần hình mới, và đúng y điều kiện mở cây (ba vụ khổ qua trên giàn). Khi hái nổi chữ "+1 trái · tre trăm đốt khắc nhập" cho người chơi thấy.

**Cổng:** `node --check` sạch · `uiluat.py` ra `LECH LUAT 0` · uicheck @@GATE@@ · `tCay176.js` chạy lại trên v183. Thử trong trình duyệt: mở Sổ cổ tích với đủ sáu cây đã lớn, cả sáu đều hiện câu lợi; đổi qua tiếng Anh thì ra đúng sáu câu tiếng Anh; cây mới mọc (`st 1`) có câu, đốm sáng và cây `???` thì không.
"""
s = s.replace(a, '\n' + sec.replace('@@GATE@@', GATE).strip() + '\n' + a, 1)
io.open(p, 'w', encoding='utf-8').write(s)
print('xong muc v183')
