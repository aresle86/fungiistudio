# Miệt Vườn 2.0 (nhánh mietvuon2-dev)

Game làm vườn miền Tây, three.js, một file HTML. Nguồn: `hd/live/vuon3d.html`. Bản live: `mietvuon2/index.html` trên `main`.

**Đọc `hd/HANDOFF.md` trước khi làm bất cứ gì.** Trong đó có trạng thái, luật thiết kế, cách vá, test, deploy và việc tiếp theo.

Tóm tắt luật quan trọng nhất:
- Nói tiếng Việt với anh Ares. Chữ trong game: tiếng Việt, giọng miền Tây, tích cực.
- Đề xuất trước khi làm việc lớn; thiết kế và mô hình mới gửi hình cho anh duyệt trước khi gắn vào game.
- Vá bằng script Python có kiểm tra số lần khớp (`rep(a, b, n)`), không sửa tay dòng dài. Kiểm cú pháp module bằng `node --check` sau mỗi lần vá.
- Chỉ hiện cái làm được ở cấp hiện tại; không nói số cấp tương lai; không ẩn vì thiếu xu.
- QC → deploy (`main` + `main:mietvuon2-online`, đổi `const BUILD`) → changelog.
- Luôn `git fetch` và so với live trước khi sửa.
