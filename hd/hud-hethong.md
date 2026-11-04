# Hệ thống giao diện Miệt Vườn 2.0 (bản nháp 4/11/2026, chờ anh duyệt)

Mục đích: chốt bộ thành phần TRƯỚC, rồi mới áp vào từng màn. Mỗi thứ chỉ có một kiểu (hoặc một kiểu với vài cỡ). Cái gì không nằm trong bảng này thì không được vẽ thêm.

## 1. Màu (đã có trong game, chỉ gọi tên lại)
| Tên | Mã | Dùng cho |
|---|---|---|
| Mực | `#4A2F1E` | chữ chính, viền mọi thành phần, bóng cứng |
| Mực nhạt | `#8A5D3B` | chữ phụ, nhãn nhỏ |
| Gỗ | `#9A6A3C` → `#B07A46` | khung bảng, bảng tên, thanh giờ |
| Giấy | `#FFF8EA` | ruột bảng, thẻ ghim |
| Giấy sẫm | `#F6EBD3` | thẻ trạng thái trong bảng |
| Viền giấy | `#E3C9A6` | viền thẻ giấy (không dùng mực cho thẻ nền) |
| Rãnh | `#6B4529` | rãnh thanh tiến độ |
| Vàng rơm | `#F2C64A` | ruột thanh, nút nhận thưởng, ô việc xong |
| Lá chuối | `#7DB84A` | nút chính |
| Ghim | `#D9483A` | ghim, nút đóng, badge |

## 2. Chữ
- **Paytone One**: tiêu đề bảng 24 · tiêu đề thẻ 20 · số to 24 · chữ trong nút 19 (chính) / 16 (phụ) · nhãn nhỏ 12–13.
- **Baloo 2 600**: thân 13–15, nhãn phụ 12.
- **Patrick Hand 16**: chỉ lời Ngoại.
- **Luật đổ bóng chữ:** bóng chữ chỉ để tách chữ **sáng** khỏi nền **đậm hoặc rối** (chữ kem trên gỗ, trên nút xanh, trên vườn). Chữ **tối trên nền sáng** không bao giờ có bóng: bóng làm mép chữ nhòe và giảm tương phản. Chữ nhỏ dưới 14px cũng không bóng dù nền gì.

## 3. Khung và thẻ (bo góc theo bậc: ngoài 16 → trong 10 → nhỏ 6)
| Thành phần | Nền | Viền | Bóng | Bo |
|---|---|---|---|---|
| Bảng (sheet, Sổ) | gỗ ngoài, giấy trong | gỗ 7px + mực 3px | 7px mực (đã có) | 24 |
| Dải tiêu đề bảng | **cùng màu với viền gỗ** (`#9A6A3C`, bỏ gradient sáng hơn) để viền và dải đọc thành một tấm gỗ, không còn bậc sáng/tối ở mép | | | |
| Thẻ trạng thái (đầu bảng) | giấy sẫm | viền giấy 2px | không | 16 |
| Thẻ giấy ghim (Ngoại nhờ, việc) | giấy | gỗ 3px + mực 2px | 4px mực (đã có) | 16 |
| Ô số / ô việc | trắng | mực 2px | 3px mực | 10 |
| Nhãn ghim (NGOẠI NHỜ) | vàng rơm | mực 2px | 2px mực | 8 |
Ghim đỏ 14px luôn có trên thẻ giấy ghim, giữa mép trên. Nhãn ghim cách nội dung bên dưới ít nhất 8px.

## 4. Nút — đúng 4 loại
| Loại | Nền | Chữ | Cao | Dùng |
|---|---|---|---|---|
| Chính | lá chuối | kem 19 có bóng | 50 | một nút/bảng: Cho ăn, Gieo, Bán |
| Phụ | giấy | mực 16 không bóng | 44 | Mua gà mái, Ấp trứng, Dời |
| Thưởng | vàng rơm | mực 16 | 44 (hoặc 22 trong ô việc) | Nhận, Mở quà |
| Đóng | ghim, tròn | ✕ trắng | 36 | góc bảng |
Tất cả: viền mực 2px, bóng 3px mực, bo 10, bấm thì lún 2px. Nút tắt: phai 55% + chữ "còn thiếu N xu". Giá tiền nằm trong nút (ô mờ bên phải). Icon trong nút 24px, bên trái chữ.

## 5. Thanh tiến độ — một loại, hai cỡ
- Rãnh `#6B4529`, viền mực 2px, ruột vàng rơm. Không gradient, không vệt sáng. **Bo góc theo chỗ đặt** (bo trong = bo ngoài − lề): trong ô số bo 10, lề 6 → thanh bo 4, ruột bo 2; trong thẻ trạng thái bo 16, lề 10 → thanh bo 6, ruột bo 4. Ruột luôn bo cả hai đầu, không cắt vuông.
- **M 14px**: có chữ trắng viền mực ở giữa ("0/1", "2g58"). Dùng cho việc, thời gian chờ ở thẻ trạng thái, xây dựng.
- **S 10px**: không chữ, số đứng trên thanh. Dùng trong ô số (máng ăn 4/8).
- Mọi thứ "còn bao lâu", "được mấy phần", "làm tới đâu" đều là thanh này. Không dùng vòng tròn, không dùng chấm.

## 6. Badge, chip, icon
- **Badge**: một loại: tròn đỏ 18–20px, số trắng, góc trên phải, lòi ra ngoài mép 4px (như menu cũ). Dùng cho số việc chờ, số hạt, số bạn ghé.
- **Chip**: nền giấy sẫm, icon 20 + số, bo 999 (đã có), cho tài nguyên nhỏ (rơm/tre/xu khi gom).
- **Icon**: bộ icon 4 tông của game. Cỡ: 48 thẻ trạng thái · 30 ô số và ô việc · 24 trong nút · 20 chip · 14 trong thanh/giá.

## 7. Menu và khay
Giữ kiểu cũ: icon tự do trên vườn + nhãn gỗ nhỏ dưới, badge đỏ góc. Không đóng khung. Chỉnh: cùng cỡ icon (46), nhãn cùng cỡ chữ (13), khoảng cách đều; **số hạt / rơm dùng badge đỏ góc trên phải icon** như số việc ở Sổ, bỏ đồng xu to đè dưới nhãn; icon túi hạt vẽ lại cùng nét viền với các icon menu khác.

## 7b. Thẻ Ngoại nhờ
Nội dung thật: 1 việc theo cấp (có thể 2 phần) + 5 việc hôm nay. Thẻ có **tối đa 3 ô**: ô 1 luôn là việc theo cấp (mỗi phần một thanh nhỏ); ô 2–3 là hai việc hôm nay chưa xong gần nhất, góc ô 3 ghi "+N" nếu còn nữa. Ít hơn thì thẻ co lại theo số ô (1 hoặc 2 ô, ô rộng ra), không để ô trống. Xong hết việc hôm nay thì ô 2 thành ô vàng "Nhận hết". Thẻ ẩn khi mở bảng (như hiện nay).

## 7c. Lời Ngoại trong bảng
Chỉ hiện khi có việc cần quyết (chưa có gà trống, máng sắp hết, đất mệt). Trạng thái bình thường thì không có dòng này.

## 8. Thứ tự áp (sau khi anh chốt bảng này)
1. Thanh tiến độ + nút + thẻ: thay trong 12 bảng dùng chung một khung (sửa một chỗ).
2. Thẻ Ngoại nhờ 3 ô, thẻ việc trong Sổ.
3. Thẻ ngày, thẻ lên cấp về cùng khung giấy ghim.
4. Sổ: tab đánh dấu sách thò mép (mock riêng, chờ duyệt).
