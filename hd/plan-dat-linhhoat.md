# Đất linh hoạt — giải pháp UX (4/11/2026, chờ anh duyệt)

## 1. Ý tưởng chính: mọi thứ trên đất đều là "món đặt", dời được
Mỗi ô đất của con (đã khai hoang) chứa đúng một thứ, theo khuôn ô:
| Thứ | Khuôn | Ghi chú |
|---|---|---|
| Liếp rau | 1 ô | đắp / san phẳng |
| Giàn dây leo | 1 ô | khổ qua, sau này bầu bí mướp |
| Cây trái | 1×2 (ô + ô ngay dưới, tán lấn) | như gốc cố định hiện nay |
| Nong, khạp, lò, hố ủ, thùng ong | 1 ô mỗi bộ | mua thêm được |
| Đồ kiểng | 1 ô | 26 món có sẵn + món mới |
| Cây cổ tích | 2×2 | đã có sẵn cách dời từ Sổ (v106), gom vào cùng một cách |
| Ao | 2×2 → 2×3 → 3×3 | theo `ao-cong-trinh.md` |

## 2. Ba thao tác, một cách làm
**A. Ô trống → bảng "Ô đất trống"**: 4 ô lựa chọn ngang nhau, icon to, một chữ: **Liếp · Cây · Giàn · Đồ**. Chưa tới cấp thì ô đó ẩn (luật cũ), không xám.
- Chọn "Đồ" mở **Túi đồ** (kệ hình các món con đang có mà chưa đặt: nong, khạp, chậu kiểng…) + nút "Mua thêm" dẫn ra Chợ › Tiệm.

**B. Chạm thứ đang đặt → bảng của nó có nút "Dời chỗ" và "Cất vô túi"** (cây trái: "Đốn", hỏi lại nếu đang có trái, được 2 củi; liếp: "San phẳng").

**C. Dời chỗ = thanh đặt đồ đang có (v106)**: món bay theo ngón tay, mọi ô hợp lệ cho khuôn đó tô xanh nhạt, ô không hợp lệ tô đỏ kèm lý do ngắn khi rê qua ("đang có liếp", "chưa khai hoang", "cần 2×2"). Thả vào ô xanh → hiện **Đặt / Hủy**. Không tốn xu; cây đang lớn giữ nguyên tiến độ; nong/khạp đang phơi, muối thì đồ trong đó đi theo.

Chỉ một cách đặt cho mọi thứ nên người chơi học một lần là dùng được hết. Không bật lại "Chế độ sửa vườn" (đã bỏ ở v106 vì rối); mọi thứ đi qua chạm thẳng như hiện nay.

## 3. Mua thêm nong, khạp, lò
- Mỗi thứ tối đa 3 bộ, mỗi bộ chiếm 1 ô: nong 80 / 250 / 500, khạp 150 / 350 / 700, lò 600 / 1.200. Mua xong vào Túi đồ, con tự chọn chỗ đặt.
- Bảng nong (khạp, lò) gom mọi bộ: "Nong · 3 bộ · 12 khay", chạm khay nào phơi khay đó; ngoài vườn mỗi bộ có bong bóng riêng.
- Nâng cấp tầng hai (đang có) giữ nguyên, áp cho từng bộ.

## 4. Mở theo cấp (khớp mạch hiện tại, không nói số cấp tương lai trong game)
| Cấp | Mở | Lý do |
|---|---|---|
| 7 | Bảng Ô đất trống: Liếp · Đồ (đã có nong) | bãi hông nhà mở ở cấp 7 |
| 8 | **Dời chỗ, Cất vô túi** mọi món (kể cả cây vú sữa có từ cấp 6) | lúc này vườn có đủ thứ để sắp |
| 9 | **Cây** trên ô đất (cây giống ở Chợ: chuối, ổi; khế 10, xoài 11, dừa 12 theo bảng mở hạt) | ổi mở cấp 9 |
| 10 | **Giàn** trên ô đất (120 xu + 2 tre) | đã có khổ qua từ cấp 6, mương có 2 giàn |
| 11 | Mua bộ nong, khạp thứ hai | sau khi quen phơi, muối |
| 13 | Bộ thứ ba; đồ kiểng (giữ như hiện nay) | |
| 14 | Lò sấy thứ hai | lò mở cấp 11 |
| 16 | Ao (đã có) đi qua cùng cách đặt | |
Mỗi mốc có việc Ngoại nhờ dạy đúng thao tác đó (ví dụ cấp 8: "Dời cây vú sữa ra chỗ con thích").

## 5. Giới hạn để vườn không vỡ kinh tế
- Cây trái thêm tối đa 6 cây (cây cho trái theo vụ, không vượt rau).
- Giàn thêm tối đa 2 giàn mỗi khu (đúng kế hoạch dây leo đã duyệt).
- Mọi thứ đặt trên ô đất của con nên số ô (30 + vườn chính) tự giới hạn: muốn nhiều đồ thì bớt liếp, đó chính là lựa chọn custom.

## 6. Thực thi (3 bản)
1. **v112 Đất linh hoạt cơ bản:** bảng Ô đất trống 4 lựa chọn, Túi đồ, Dời chỗ / Cất cho mọi món + cây cổ tích (gom code `bigPlace`, `dcPlace`, `placeObj` vào một hàm đặt chung theo khuôn), trồng cây trái và dựng giàn trên ô. Lưu: `ST.slots[id] = { k, at }`, chuyển dữ liệu cũ sang tự động.
2. **v113 Mua thêm bộ:** nong, khạp, lò nhiều bộ; bảng gom bộ.
3. **v114 Đồ trang trí mới + ao công trình** theo `plan-trangtri-dat.md`, `ao-cong-trinh.md`.
Mỗi bản: mock duyệt trước, test dời từng loại món, bot 30 ngày đo xu.
