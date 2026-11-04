# Đề xuất v111+ (4/11/2026 chiều)

## 1. Bản tiếng Anh: người nước ngoài chơi trọn, không rào cản
- **Chọn ngôn ngữ:** lần đầu mở game tự theo ngôn ngữ máy (máy tiếng Việt → tiếng Việt, còn lại → English); đổi được trong Cài đặt và ngay màn mở đầu (cờ VI / EN). Lưu theo máy.
- **Dịch hết:** mọi chữ giao diện, tên món, tên cá, tên bướm, việc, đơn hàng, ~300 câu của Ngoại, 6 sự tích, thẻ kỷ niệm 30 ngày, thông báo lỗi.
- **Giữ hồn miền Tây mà vẫn hiểu:** tên đặc trưng giữ tiếng Việt kèm nghĩa ngắn lần đầu gặp, sau đó dùng tên Việt. Ví dụ: "Ngoại (Grandma)", "ghe (wooden boat)", "nong (drying tray)", "áo bà ba". Món ăn: "Canh chua (sour fish soup)". Cá: tên Anh trước (Climbing perch · cá rô).
- **Giọng Ngoại tiếng Anh:** ấm, giản dị, hơi quê ("Come here, dear, the okra's ready."), không dịch máy từng chữ.
- **Kỹ thuật:** gom toàn bộ chữ vào một bảng `TXT.vi / TXT.en` trong file game; mọi chỗ in chữ gọi `tx('key')`. Chữ dài hơn (tiếng Anh dài ~20%) → soát lại mọi bảng, nút trên điện thoại.
- **Bạn bè khác ngôn ngữ:** tên vườn, tên người giữ nguyên; lời nhắn/mật thư dùng mẫu có sẵn nên hiện đúng ngôn ngữ của người đọc.
- **Làm theo đợt:** (1) khung + giao diện + món, (2) việc, đơn, Sổ, (3) Ngoại + sự tích, (4) soát điện thoại. Mỗi đợt có bài test dò chữ Việt còn sót khi bật English.

## 2. Đất linh hoạt: người chơi tự sắp vườn
- Ô đất trống (đã khai hoang) có 4 lựa chọn ngang nhau: **Đắp liếp · Trồng cây trái · Dựng giàn · Đặt đồ** (lu, nong, khạp, đồ kiểng).
- **Đổi qua lại:** bỏ liếp → trồng cây; đốn cây → đắp liếp (cây đang có trái thì hỏi lại); dỡ giàn → đất trống. Tốn chút công/xu, không mất vĩnh viễn.
- **Mua thêm** lu, nong, khạp (giá tăng nhẹ theo số đã có, có trần) để ai thích phơi, muối nhiều thì xây.
- Giàn trên đất mới mở dây leo v110 (bầu, bí, mướp…), khớp đơn hàng xóm.

## 3. Mật thư bụi chuối (ý anh Ares)
- Ghé vườn bạn, mỗi ngày được **giấu một mật thư** vào một chỗ trong vườn bạn: bụi chuối, gốc dừa, khạp nước, đống rơm.
- Thư gồm **câu chọn sẵn** (lời thăm, lời chúc, câu đố vui, câu ca dao) + một sticker; có thể kẹp kèm một món quà nhỏ (1 bó rau, 1 trứng). Không cho gõ tự do để tránh lời xấu và để dịch đúng sang tiếng Anh.
- Chủ vườn: chỗ có thư thì lá chuối **khẽ rung**, chạm vào → mở thư (hình giấy gấp, chữ tay), thư cất vào **Sổ › Thư bạn bè**.
- Server: thêm loại `note` vào `mv2_act` (+ ràng buộc bảng), tối đa 1/ngày/vườn; hộp thư đọc như các loại khác.
