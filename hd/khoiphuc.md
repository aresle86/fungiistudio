# Miệt Vườn: chìa khóa, sao lưu, khôi phục

Trang này chỉ ghi chỗ cất và cách làm, không ghi mã. Kho GitHub đang công khai, đừng dán khóa hay mật khẩu vào đây.

## Tài khoản và chìa khóa

| Thứ | Ở đâu | Ai giữ |
|---|---|---|
| GitHub `aresle86` (code + trang web fungiistudio.com qua GitHub Pages) | github.com | anh Ares |
| Supabase, project `zgfanxtjdvioxpgpbcke` (dữ liệu vườn người chơi) | supabase.com | anh Ares |
| Tên miền fungiistudio.com | nhà đăng ký tên miền (anh ghi tên vào đây) | anh Ares |
| Email Google ares.le@… (khôi phục mọi tài khoản trên) | Google | anh Ares |
| Khóa quản trị trang Báo lỗi / Người chơi | file `hd/.baoloi-key` trên máy anh, không lên git | anh Ares |
| Khóa publishable Supabase | nằm trong game, công khai theo thiết kế | — |
| Mã khôi phục 2FA | giấy hoặc trình quản lý mật khẩu, không để trong máy code | anh Ares |
| Người dự phòng | (anh ghi tên) | |

## Trang quản trị

https://fungiistudio.com/mietvuon2/baoloi.html. Mở ra dán khóa quản trị. Có thẻ Báo lỗi và Người chơi.
Chép khóa vào bộ nhớ tạm mà không hiện ra màn hình: `pbcopy < ~/Documents/fungiistudio/hd/.baoloi-key`

## Sao lưu

- Chạy `python3 ~/Documents/fungiistudio/hd/saoluu.py`. Lưu ở `~/MietVuon-saoluu/<ngày giờ>/`, mỗi bảng một file JSON, kèm định nghĩa hàm (`_functions.json`) và cấu trúc cột (`_schema.json`). Giữ 12 bản mới nhất.
- Cần hàm `mv2_admin_export` trên Supabase (`hd/sql/mv2_admin_export.sql`), chỉ đọc, có khóa quản trị mới gọi được.
- Thư mục sao lưu nằm ngoài kho git, không bao giờ bị đẩy lên mạng. Nên chép thêm một bản ra ổ ngoài hoặc iCloud mỗi tháng.

## Khi có chuyện

**Lộ khóa quản trị** (lỡ gửi ai, lỡ commit):
1. Tạo khóa mới ngẫu nhiên, ghi đè `hd/.baoloi-key`.
2. Trên Supabase, sửa hàm `mv2_admin_ok` cho khớp mã băm SHA-256 của khóa mới. Em làm được, anh duyệt trước.
3. Khóa cũ hết tác dụng ngay.

**Lộ mật khẩu hay mất tài khoản GitHub / Supabase:**
1. Đổi mật khẩu, đăng xuất mọi phiên, xem lại 2FA.
2. GitHub: Settings → Sessions, Applications, SSH keys, Personal access tokens: xóa cái lạ.
3. Supabase: Organization → Members: xóa người lạ. Account → Access tokens: thu hồi hết, cấp lại cho em nếu cần.
4. Kiểm tra trang web còn đúng: mở fungiistudio.com/mietvuon2, xem BUILD.

**Mất dữ liệu người chơi:**
1. Lấy bản sao lưu mới nhất trong `~/MietVuon-saoluu/`.
2. Nhờ em dựng lại: tạo bảng theo `_schema.json`, hàm theo `_functions.json`, nạp lại dữ liệu từng bảng. Bước này ghi lên Supabase nên em hỏi anh trước.

**Trang web bị sửa bậy:** mọi bản cũ nằm trong lịch sử git. Quay về commit đúng trên nhánh `main` rồi push.

## Thói quen

- 2FA bằng passkey hoặc app tạo mã (không xài SMS) cho GitHub, Supabase, nhà đăng ký tên miền, email Google.
- Không chạy code hay cài plugin người lạ gửi khi chưa đưa em đọc.
- Claude chỉ ghi Supabase khi anh duyệt. Anh tự push code.
- Tháng một lần: chạy sao lưu, xem thẻ Người chơi, chạy kiểm tra bảo mật Supabase (Advisors → Security).
