# Rà soát HUD Miệt Vườn 2.0 — hướng đi chung cho toàn bộ giao diện

Ngày 4/11/2026. Chụp từ bản v107a: 14 màn điện thoại + 9 màn máy tính (`hud/tongquan_ph.png`, `hud/tongquan_pc.png`). Ref chuẩn anh chọn: **ref 2** (quán cà phê thú cưng: bảng gỗ, giấy ghim, nét viền dày) làm style; **ref 3** học cách dùng icon nhiều, chữ ít.

## 1. Hiện trạng: ba "bộ" giao diện đang sống chung

| Nhóm | Màn | Nhận xét |
|---|---|---|
| A. Bảng gỗ (đã gần ref 2) | Thanh trên: avatar + cấp, bảng giờ gỗ, túi xu; bảng "Mé sông" trong vườn; nút "Về giữa" | Đúng chất liệu, có viền, có bóng. Đây là cái **giữ lại và nhân ra**. |
| B. App sheet (xa ref nhất) | Chợ, Chuồng gà, Ao cá, Nong, Cài đặt, Liếp trống, Đất trống | Đầu nâu phẳng + thân kem + thẻ trắng + nút xanh bo tròn. Nhìn như app ngân hàng/đặt xe. Không viền, không bóng cứng, không có chất liệu. Nhiều câu giải thích dài. |
| C. Sổ + thẻ trắng | Sổ (3 tab), thẻ "Về vườn ngày 1/7", thẻ lên cấp, thẻ "Ngoại nhờ" | Sổ có chất giấy nhưng tab yếu; thẻ ngày và lên cấp là ô trắng phẳng giữa màn hình. |

Hệ quả: người chơi đi từ vườn (ấm, gỗ, 3D) vào sheet (lạnh, phẳng, app) rồi sang Sổ (giấy) — mỗi lần đổi "thế giới". Ref 2 chỉ có một thế giới: mọi thứ đều là bảng gỗ ghim giấy.

Lỗi nhỏ thấy khi chụp:
- Nút Sổ/Chợ/Cài đặt/Ghé vườn góc dưới phải: icon mỗi cái một cỡ, chữ nhỏ 11–12px, nền chữ là pill mờ nên trên nền cỏ sáng rất khó đọc (máy tính).
- Chip Hạt/Rơm/công cụ bên trái máy tính rời rạc, không cùng hàng cùng cỡ với nhóm nút phải.
- Vườn cấp 16 hiện ~30 bong bóng tròn (bình tưới / cuốc) cùng lúc, lấn át cả cảnh. Ref không bao giờ cho 30 nút giống nhau lên màn.
- Thẻ "Ngoại nhờ" và "Việc hôm nay" đều là chữ + thanh tiến độ mỏng; ref 2 là icon to + thanh vàng + nút Claim sáng lên.
- Trong Chuồng gà: "Trứng kế tiếp chừng 2 giờ 58 phút", "đủ chừng 3 giờ", "chuồng 5/6 chỗ" — ba con số thời gian/sức chứa đều viết thành câu.

## 2. Nguyên tắc rút từ ref 2 + ref 3

1. **Một chất liệu cho mọi bảng**: khung gỗ nâu đậm → tờ giấy kem ghim ở giữa mép trên → nội dung nằm trên giấy. Tên bảng nằm trên **bảng tên** đè lên mép khung (không phải header màu). Nút đóng đỏ tròn ở góc trên phải, đè lên khung.
2. **Nét sticker đồng nhất**: viền nâu đậm 2.5–3px quanh mọi nút, thẻ, icon, tab; vệt sáng mỏng mép trên; bóng cứng 3px phía dưới. Nút bấm thì "lún" khi nhấn (bóng mất, dịch xuống 2px). Không còn bo tròn phẳng không viền.
3. **Icon trước, chữ sau** (ref 3): mỗi trạng thái có icon; chữ chỉ là nhãn một–hai từ hoặc con số to. Câu giải thích chuyển sang lời Ngoại (hộp thoại dưới trái đã có) hoặc nút "?" nhỏ.
4. **Số to, câu ngắn**: thời gian còn lại = icon đồng hồ + "2g58"; sức chứa = icon + "5/6"; tiến độ = thanh vàng có viền, có bóng.
5. **Mỗi khu một màu, dùng lại khắp nơi**: Việc = cam san hô, Kho = vàng, Sưu tập = tím, Chợ = xanh ngọc, Chuồng = nâu đỏ, Nước/cá = xanh dương. Tab, bảng tên, badge, icon của khu đó đều lấy màu đó.
6. **Nút điều hướng là ô vuông icon** (ref 1 + 2): ô gỗ/đá 56–64px, icon to ở giữa, nhãn ngắn dưới, badge đỏ tròn số góc trên phải. Cùng cỡ, cùng hàng.
7. **Màn hình vườn chỉ hiện việc cần làm**: bong bóng chỉ nổi khi liếp cần tưới/hái/có sâu; liếp đang lớn thì im. Ref 2 có đúng một thanh việc + vài thẻ.
8. **Chữ nhỏ nhất 13px, mục tiêu chạm 44px** (đã làm ở v107, giữ).
9. **Trang trí chỉ ở góc** (hoa lá, ghim, dây): một–hai chi tiết mỗi bảng, không rải.

## 3. Bộ nền chung (design kit) — làm một lần, dùng cho tất cả

Toàn bộ làm bằng CSS + SVG trong file game, không thêm file ảnh ngoài.

- **Khung bảng** `.wd` : nền gỗ `#8A5D3B` → viền `#4A2C17` 3px → bóng `0 4px 0 #3A2010` → góc bo 16px → mép trong vệt sáng `inset 0 2px 0 rgba(255,255,255,.25)`.
- **Tờ giấy** `.pp` : `#FFF6E3`, viền `#C9A77A` 2px, bóng nhẹ, góc bo 10px, cách khung 10px.
- **Bảng tên** `.plate` : gỗ sáng `#C98A4E`, viền đậm, chữ Baloo 2 700 kem, đặt `top:-14px` giữa khung, có 2 đinh/ghim.
- **Nút** `.btn` : nền màu khu, viền `#4A2C17` 2.5px, bóng `0 3px 0` tối hơn, chữ kem có text-shadow 1px; `:active` lún 2px. Ba cỡ: 44 / 52 / 64px.
- **Ô icon** `.tile` : 56×56 gỗ sáng, viền, bóng, icon SVG 32px, nhãn 12–13px dưới, badge đỏ `.bd`.
- **Thanh tiến độ** `.bar` : rãnh nâu tối có viền, lớp vàng `#F4C12E`, vệt sáng trên.
- **Icon**: một bộ SVG ~40 cái cùng nét (viền 2px nâu, hai tông màu, đốm sáng): tưới, hái, gieo, phân, cỏ, sâu, trứng, cám, cá, giỏ, củi, xu, đồng hồ, sao, ✓, !, khóa, thùng, nhà, chợ, sổ, cài đặt, ghé vườn… Thay toàn bộ emoji và ảnh icon lẻ hiện nay.

## 4. Áp vào từng màn (ưu tiên từ trên xuống)

1. **Nút điều hướng góc dưới phải + chip bên trái** → 4 ô `.tile` cùng hàng (Ghé vườn · Sổ · Chợ · Cài đặt), bên trái 2 ô (Hạt · Rơm) cùng cỡ. Việc nhỏ nhưng thấy ngay ở mọi màn.
2. **Khung sheet chung** (Chợ, Chuồng, Ao, Nong, Khạp, Lò, Liếp, Đất trống, Cài đặt) → một khung `.wd` + bảng tên + giấy. Sửa một chỗ, 12 sheet đổi theo. Nội dung trong sheet: thẻ trạng thái = icon to + số to + thanh; nút chính to ở dưới cùng.
3. **Thẻ Ngoại nhờ / Việc hôm nay** → thanh việc kiểu ref 2: 3 ô icon + tiến độ, ô xong sáng vàng "Nhận". Trong Sổ, mỗi việc là một thẻ có icon to bên trái.
4. **Sổ**: khung gỗ + hai trang giấy (giữ), tab thành **thẻ đánh dấu thò mép** cùng màu khu, icon to + một chữ ("Việc", "Kho", "Sưu tập"); tab đang mở nối liền trang.
5. **Thẻ "Về vườn ngày 1/7", lên cấp** → cùng khung gỗ; 7 ô ngày thành 7 ô quà có viền, ô đã nhận có dấu ✓ vàng.
6. **Vườn**: bong bóng chỉ hiện khi có việc; liếp đang lớn hiện vòng tiến độ nhỏ mờ. Giảm nhiễu, giảm draw call luôn.
7. **Cài đặt**: thanh trượt thành thanh gỗ có núm; nút lựa chọn thành ô có viền + ✓.

## 5. Cách làm, để anh duyệt từng bước bằng hình

- Bước 1: em dựng **mock tĩnh** (HTML riêng, không đụng game) màn Chuồng gà + thanh điều hướng + thanh việc theo kit trên, chụp điện thoại + máy tính gửi anh. Chốt được kit ở bước này là chốt cho tất cả.
- Bước 2: vẽ bộ icon SVG, gửi một tờ icon để duyệt.
- Bước 3: đưa kit vào game theo thứ tự mục 4 (1→2→3 trong v108, 4→7 trong v109), mỗi bước có hình trước/sau + test như thường lệ.

Việc này không chạm luật chơi, nên có thể chạy song song với phần kinh tế (chỗ tiêu xu) và ship riêng.
