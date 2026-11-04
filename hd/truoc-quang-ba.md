# Danh sách cần làm trước khi quảng bá Miệt Vườn 2.0 (4/11/2026)

Sắp theo mức: **A = phải xong trước khi share rộng**, B = nên có, C = sau.

## A. Phải xong
| # | Việc | Hiện trạng | Cách làm |
|---|---|---|---|
| A1 | Ship v108 (giao diện theo hệ thống) + v109 (gà vịt, đơn hàng) | Đã làm, đang chạy regression | Qua test → anh push → kiểm live |
| A2 | "Mạng chập chờn, chưa hái được" khi ghé vườn bạn | Log server: 7 lần **lỗi 400** sáng 4/11 (server từ chối, không phải mạng yếu). Game gom mọi lỗi thành câu "mạng chập chờn" nên không biết lý do thật | Hiện đúng lý do (vườn không còn / mã lệch / đã hái đủ); timeout 9 s thì tự thử lại 1 lần; ghi lỗi về thống kê để soi. Nghi lỗi gốc: mã bí mật trên máy lệch với server sau khi tải bản trên máy khác |
| A3 | Chơi 2 máy | Mở game không tự lấy bản mới, phải bấm "Tải bản mới nhất", dễ ghi đè | Mở game tự so bản mây, bản nào mới hơn thì dùng; báo khi có xung đột |
| A4 | Server chịu tải | Supabase gói **Free**: tự tạm dừng nếu 7 ngày không ai vào, 60 kết nối DB, 500 MB (đang 12 MB, 51 vườn) | Game chạy trên máy từng người, server chỉ nhận lưu và ghé vườn nên gói Free chịu được vài trăm người chơi/ngày. Share rộng (nghìn người) thì lên **Pro 25 USD/tháng**, thêm chỉ mục bảng sự kiện, giãn nhịp tự lưu |
| A5 | Hố ủ khó hiểu | Phân chuồng 1 phần/6 tiếng, tối đa 4, **không tăng theo số gà vịt**; gốc rễ rau khi hái **chưa có** | Phân theo số con (mỗi 3 con ra 1 phần/6 tiếng); hái rau tự rơi gốc rễ vô hố (chữ bay "+1 vô hố ủ"); bảng hố ủ hiện 3 nguồn bằng icon + thanh đầy hố + bao phân ra; Ngoại dặn lần đầu; việc hằng ngày "Hốt phân chuồng" |
| A6 | Hiệu năng điện thoại | Máy tính: tải 1,8 giây, 451 KB, ~55 khung/giây. Điện thoại ~554 lần vẽ/khung | Gộp bong bóng liếp + nhân vật (còn ~200 lần vẽ), bớt bong bóng khi liếp đang lớn, đo trên Android tầm trung thật, tự hạ đồ họa khi máy yếu |
| A7 | Thẻ xem trước khi share link | Chưa kiểm | Ảnh + tiêu đề + mô tả khi dán link vào Zalo, Messenger, Facebook |

## B. Nên có trước khi share
| # | Việc | Ghi chú |
|---|---|---|
| B1 | Gà vịt nở là **sự kiện chúc mừng** | v109 mới có Ngoại nói + chữ bay. Thêm: camera bay tới chuồng, pháo giấy lông vũ, tiếng chiêm chiếp, thẻ "Nở rồi!", cả lò ấp vịt |
| B2 | Hiệu ứng sinh động hơn | Thu hoạch: rau bay vô giỏ, đếm số nhảy · Tiền: đồng xu lăn vô túi, số xu chạy · Giao đơn: xuồng hàng xóm chèo đi · Lên cấp: pháo hoa nhỏ trên nhà · Mưa, gió, cá quẫy theo giờ |
| B3 | Chỗ tiêu xu (phần C đã duyệt) | Bot dư 118.000 xu ngày 30: bếp khang trang, đồ kiểng cao cấp, bảng tên vườn, đất bên kia rạch |
| B4 | Sổ, thẻ ngày, thẻ lên cấp theo hệ thống giao diện | Bước 4 của kế hoạch HUD |
| B5 | Lỗi QC cũ còn mở | Hộp thư cộng quà hai lần khi lỗi, khôi phục mây ghi đè giờ, bán được món không bán, rò bộ nhớ hình khối |
| B6 | Bong bóng liếp quá dày ở cấp cao | Chỉ hiện khi cần làm |
| B7 | Icon túi hạt cùng nét với menu | Vẽ lại |

## C. Sau (đã duyệt, chưa làm)
- v110 dây leo: dựng giàn trên đất mới, mướp, bầu, bí đao, đậu rồng, chanh dây (mô hình gửi duyệt trước).
- Phần B: tủ đồ, tiệm may, thợ nhà.
- Bảng Đất trống 2×2, khóa khu đất theo tiến độ, chuỗi nhiệm vụ 3 bước (`dexuat-v107.md`).
- Đình làng, lễ Kỳ Yên; mùa nước nổi.

## Thứ tự em đề xuất
A1 → A2 + A3 (mạng, 2 máy) → A5 (hố ủ) → B1 (nở chúc mừng) → A6 (hiệu năng) → A7 + A4 → B2–B7.
