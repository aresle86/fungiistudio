# -*- coding: utf-8 -*-
# Ghi v185 (ba lỗi ở chợ nổi / Bến bà con) vô HANDOFF.md
import io, sys
p = '/Users/macintoshhd/Documents/fungiistudio/hd/HANDOFF.md'
s = io.open(p, encoding='utf-8').read()
tet = sys.argv[1] if len(sys.argv) > 1 else '23'   # số lệch 'sat' đo được ở cỡ 393×640

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khop %d lan, can %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

rep("Bản mới nhất là **v184, đã dựng, CHƯA ĐẨY** (`live/v182.html` → `fix183.py` → `live/v183.html` → `fix184.py` → `live/v184.html`).",
    "Bản mới nhất là **v185, đã dựng, CHƯA ĐẨY** (`live/v182.html` → `fix183.py` → `live/v183.html` → `fix184.py` → `live/v184.html` → `fix185.py` → `live/v185.html`).")

rep("| Việc kế tiếp | **Đẩy v183 + v184** khi anh Ares nhắn (hai bản đi chung một lần cho gọn). Rồi",
    "| Việc kế tiếp | **Đẩy v183 + v184 + v185** khi anh Ares nhắn (ba bản đi chung một lần cho gọn; v185 sửa lỗi anh báo từ iPhone nên nên đẩy sớm). Rồi **thêm cỡ màn ngắn vô bộ đo** — xem mục v185. Rồi")

a = "\n## Ý đang chờ anh chốt (24/11/2026) — cây cổ tích ở đình làng"
assert s.count(a) == 1

them = u"""
## v185 (24/11/2026) — ba lỗi ở chợ nổi, anh Ares báo từ iPhone thật

**BẢN NHÁP — đã dựng, CHƯA ĐẨY.** `fix185.py`, v184 → v185. Anh Ares: *"Có lỗi ở chợ, báo số sai và ux bị lệch"*, kèm hai tấm hình chụp iPhone trên bản live v182; sau đó anh khoanh đỏ **cục xu** và nói *"Ý t là cái này"*.

### 1. Cục xu rớt xuống một hàng riêng, treo lơ lửng (cái anh khoanh)

Thanh trên đầu là một hàng `flex` có `flex-wrap:wrap`, trong đó `.top .coin` có `margin-left:auto`. Ra chợ thì luật

```css
body.chon .ui.top > :not(#avb):not(.coin){visibility:hidden}
```

giấu đồng hồ đi — **nhưng `visibility:hidden` vẫn giữ nguyên chỗ ngồi**. Hàng trên đầu thành: đệm 16 + hình đại diện 116 + khe 8 + chỗ trống của đồng hồ 128 + khe 8 + cục xu 156 = 432, quá khổ màn 393. Cục xu rớt xuống hàng hai, `margin-left:auto` đẩy nó sát phải, chừa một lỗ trống to bên trái. Đúng y hình.

**Sửa:** đổi `visibility:hidden` thành `display:none`. Đo lại ở 393×640: cục xu lên cùng hàng với hình đại diện (cả hai `top` 12), thanh trên đầu **từ 137 xuống 88** — trả lại 49 điểm màn cho cảnh chợ. Đây là luật duy nhất trong game giấu từng món trong `.ui.top`; mấy luật kia (`bookon`, `sap`, `greet`) giấu nguyên cả thanh nên không vỡ hàng.

### 2. "Trên xuồng con · 10/10 món" trong khi trên xuồng còn 5

`cnbOn(b) = b.my.reduce(…q) + (b.sd || 0)`, với `b.sd` = số món bà con **đã mua trong ngày** (`cnbSync` đặt từ `mv2_ben_collect`). Con số đó đúng cho hạn mức "mỗi ngày chất được 10 món" (dùng ở `cnbPut` và `room`), nhưng nhãn ghi *"Trên xuồng con"* nên đọc vô là sai: chất 10, bán 5, còn 5 trên xuồng, nhãn vẫn kêu 10.

**Sửa:** tách hai con số.
- Nhãn đếm đúng cái đang nằm trên xuồng: `nOn = b.my.reduce(…q)`.
- Chưa bán món nào (`b.sd === 0`) thì nhãn vẫn là `nOn/10` như cũ — không mất thông tin còn mấy chỗ.
- Bán rồi thì nhãn là `· 5 món`, và thêm một dòng riêng: *"Hôm nay con chất 10/10 món, bà con mua rồi 5."* (tiếng Anh: *"You loaded 10/10 today — neighbours have bought 5."*)

`b.sd` có được dọn mỗi ngày không: có, `cnbS()` đặt `b.sd = 0` khi qua ngày mới. Không có lỗi tồn.

### 3. Màn ngắn thì bảng trùm lên thanh xu

Luật điện thoại `@media (max-width:560px)` cho `.sheet` cao `74dvh` và cách đáy 10 điểm. `.sheet` đo theo **content-box** (viền 7+7, đệm 8+16) nên cao thiệt = `max-height + 38`. Trên máy anh, trình duyệt ăn mất một khúc màn nên chỉ còn chừng **640 điểm** cao thay vì 844: bảng cao 512, đáy 630, **đỉnh 118** — mà thanh HUD nằm 0–141. Bảng cắt ngang cục xu.

**Sửa:** `max-height:min(74dvh,calc(100dvh - 200px - env(safe-area-inset-top) - env(safe-area-inset-bottom)))`. Chừa 150 điểm trên đầu cho HUD (đo thiệt cao 137–143): 10 + 150 + 38 = 198, lấy tròn 200. Đo lại ở 640: đỉnh bảng **152**, cách HUD 16 điểm. **Màn cao từ 808 điểm trở lên không đổi một li**; 360×740 nhích 3,6 điểm.

### Vì sao máy đo không bắt được

`uicheck.js` xưa giờ chỉ chạy ba cỡ **390×844, 360×740, 1280×800** — không cỡ nào đủ ngắn để lòi lỗi 1 với lỗi 3 ra. Một iPhone thiệt có thanh trình duyệt chỉ còn chừng 640 điểm cao.

Đã chạy thử **393×640**: `TONG {"sat": NSAT} khac nhau 4 loi trang 0` — tức NSAT chỗ hai nút cách nhau dưới 8 điểm, nằm ở màn Tết (`tet-chip`, `tet-het`) và vài màn khác, **không có lỗi chạy nào**. Đây là lỗi cũ có sẵn, không phải v185 đẻ ra. **Việc kế tiếp:** dọn hết NSAT chỗ đó rồi thêm 393×640 vô bộ cổng bắt buộc, để từ nay đo bốn cỡ. Chưa làm trong v185 vì đó là việc riêng, không nên trộn vô bản sửa lỗi.

### Cổng

`node --check` sạch · `uiluat.py` → `LECH LUAT 0 {}` · uicheck `khac nhau 0 loi trang 0` ở 390×844, 360×740, 1280×800 · `tCay176.js` **ĐẠT HẾT 13/13**. Đo thật trong trình duyệt ở 393×640 (đúng cỡ màn máy anh): cục xu nằm cùng hàng hình đại diện, bảng đỉnh 152 không đụng HUD, nhãn ra *"Trên xuồng con · 5 món"* + dòng hạn mức, tiếng Anh đúng. Lỗi console chỉ có `ERR_UNSAFE_PORT` của bàn thử. **Chưa thử lại trên iPhone thật của anh.**
"""
s = s.replace(a, them.replace('NSAT', tet) + a, 1)

io.open(p, 'w', encoding='utf-8').write(s)
print('xong ghi v185')
