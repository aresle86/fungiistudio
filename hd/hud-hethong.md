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
| Nhãn ghim (NGOẠI NHỜ) | vàng rơm | mực 2px | 2px mực | 10 |
Ghim đỏ 14px luôn có trên thẻ giấy ghim, giữa mép trên. Nhãn ghim cách nội dung bên dưới ít nhất 8px.

## 4. Nút — đúng 4 loại
| Loại | Nền | Chữ | Cao | Dùng |
|---|---|---|---|---|
| Chính | lá chuối | kem 19 có bóng | 50 | một nút/bảng: Cho ăn, Gieo, Bán |
| Phụ | giấy | mực 16 không bóng | 44 | Mua gà mái, Ấp trứng, Dời |
| Thưởng | vàng rơm | mực 16 | 44 (trong ô việc vẽ nhỏ hơn nhưng vùng bấm vẫn đủ 44) | Nhận, Mở quà |
| Đóng | ghim, tròn | ✕ trắng | vẽ 36, vùng bấm 44 | góc bảng |
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

## 9. Quy tắc bổ sung (anh Ares duyệt 4/11 khi làm Sổ)
- **Lưới căn lề:** trong một thẻ, mọi chữ dùng chung một mép trái. Cột hình bên trái (icon lớn, icon nhỏ của từng phần nằm dưới icon lớn), cột chữ ở giữa, cột hành động bên phải.
- **Khoảng cách:** xem mục 10 (thang 4 / 8 / 12 / 16 / 24). Nhịp cũ 6 / 10 / 14 đã bỏ.
- **Cột phải cố định:** chip thưởng và nút phụ cùng bề ngang (72px), cùng chiều cao (24px), cùng mép phải, cách mép trên/dưới thẻ bằng nhau, thẳng hàng qua mọi thẻ.
- **Không nhãn khó hiểu:** nhãn nào phải tự giải thích; tiêu đề đã nói thì không gắn thêm tag.
- **Icon trước chữ** cho từng mục, từng phần việc.
- **HUD phải sinh động, trực quan:** ưu tiên hình, icon, thanh, màu khu hơn chữ; trạng thái đổi thì có chuyển động nhẹ (nảy, lóe, số chạy); không để mảng chữ dày.
- Tab Sổ: thẻ đánh dấu sách thò mép (máy tính mép phải, điện thoại mép trên), icon + một chữ, màu khu (Việc #F6B49F, Kho #F5D27A, Sưu tập #B9D79F); tiêu đề trang là bảng tên cùng màu, chữ mực.
- **Trước khi gửi hình:** phóng to từng thẻ, dò lại theo skill thiết kế và bảng này.

## 10. Quy tắc gốc cho mọi màn hình (anh Ares yêu cầu 14/11: làm từ gốc, theo skill UI)

Nguồn: skill `ui-ux-pro-max` (spacing-scale 4pt/8dp, touch-target-size, touch-spacing, chữ tối thiểu 12).

**10.1 Khoảng cách: chỉ 5 nấc, gọi bằng tên, không viết số lẻ**

| Tên | Số | Dùng cho |
|---|---|---|
| `--s1` | 4px | hình với chữ dính liền nhau trong một nhãn, chỉnh rất nhỏ |
| `--s2` | 8px | tiêu đề mục tới nội dung của nó; các ô nhỏ cùng hàng; icon với chữ trong nút |
| `--s3` | 12px | các khối trong cùng một mục (thẻ, hàng ô, nút); lề trong của thẻ |
| `--s4` | 16px | giữa hai mục; lề trong của bảng lớn |
| `--s6` | 24px | ngắt lớn: đầu bảng với nội dung, giữa hai phần khác hẳn nhau |

- Không dùng 6, 10, 14, 18, 22 hay số nào khác cho khoảng cách.
- Hai khối không bao giờ dính nhau (0px), trừ khi chúng cố ý là một khối.
- Ngoại lệ được phép: viền và bóng (2 đến 6px theo mục 3, 4), chỉnh mắt 1 đến 2px, số âm để kéo hình, và số lớn hơn 24 khi đó là vị trí đặt khối trên màn hình (không phải khoảng hở giữa hai khối).
- Khi đổi số cũ sang thang: lấy nấc gần nhất, đứng giữa hai nấc thì lấy nấc lớn hơn.

**10.2 Chỗ bấm**

- Mọi thứ bấm được có vùng bấm ít nhất 44 x 44px. Hình bên trong có thể nhỏ hơn (nút đóng vẽ 36px) nhưng vùng bấm phải đủ 44.
- Hai chỗ bấm cạnh nhau cách ít nhất 8px.
- Bấm vô phải có phản hồi thấy được (lún xuống, đổi màu).

**10.3 Chữ**

- Nhỏ nhất 12px. Không dùng 8, 9, 10, 11.
- Chỉ dùng các cỡ chẵn trong mục 2; bỏ các cỡ lẻ nửa (12.5, 13.5, 14.5).

**10.4 Bo góc**

- Ba bậc chính theo mục 3: ngoài 16, trong 10, nhỏ 6. Bảng lớn 24. Viên thuốc 999, hình tròn 50%. Chi tiết rất nhỏ được dùng 1, 2, 4. Bỏ 8, 9, 12, 14, 18.

**10.5 Khoá quy tắc (anh Ares yêu cầu 14/11: khoá lại, không để sai nữa)**

Mọi bản dựng phải qua HAI máy kiểm, cả hai ra 0 lỗi, rồi mới được đưa anh Ares coi hoặc đẩy:

1. `python3 uiluat.py live/<bản>.html` phải in `LECH LUAT 0 {}`. Máy này đọc mã: khoảng cách ngoài thang, chữ dưới 12, bo góc ngoài bộ số. `fixNNN.py` đụng tới giao diện phải tự gọi kiểm này (`assert not soat(s)`), sai là không ra file.
2. `node uicheck.js mv2_t<bản>.html <thư mục hình>` phải in `khac nhau 0 loi trang 0`. Máy này mở game thật, đi qua 43 màn + câu cá, thăm vườn, chợ huyện và đo: chữ dưới 12, chỗ bấm dưới 44, hai chỗ bấm cách dưới 8, hai khối dính nhau, nội dung tràn lề. Chạy ở ba cỡ: 390×844, 360×740, 1280×800.
3. Coi hình trước/sau bằng mắt (`node uimontage.js`), vì máy không bắt được chữ chật hay bố cục xấu.

- Màn mới, bảng mới: thêm một bước vô danh sách của `uicheck.js` ngay trong đợt đó.
- Không sửa máy kiểm cho nó bớt bắt lỗi. Muốn thêm ngoại lệ phải ghi lý do ở đây.
- Ngoại lệ đang có trong máy kiểm: hàng kẻ vạch ngăn (nền trong, không bóng) không tính là khối dính nhau; chỉ đo tràn ngang ở khung có cuộn ngang.

**10.6 Hiện trạng**

- v149b (đang live): máy đọc mã bắt 735 chỗ lệch; máy mở game bắt 63 kiểu lỗi (chữ nhỏ 30, dính nhau 133, chỗ bấm 71, tràn lề 12).
- v149c (bản nháp 14/11/2026, `fix149c.py`): đổi cả game sang thang bằng máy (`chuyen`), rồi đo và coi hình từng màn; cả hai máy ra 0 lỗi ở ba cỡ màn hình. Trước đó em ghi "không đổi một lượt cả game bằng máy"; đã đổi cách vì anh yêu cầu khoá toàn bộ, và việc coi từng màn vẫn giữ.
- Chưa đo: bảng lên cấp, bản tiếng Anh, cảnh chợ nổi, bảng đồ trang trí, iPad, iPhone thật. Bảng `ao` không mở được trong bài thử (lỗi có từ bản cũ).
- Đã sửa thêm trong v149c: điện thoại hẹp (từ 380 trở xuống) lề trang Sổ còn 16 để ô chọn mục Sưu tập gọn 2 hàng, icon dòng số thẻ hạt 16px; máy tính: hàng nút trang chi tiết giống chừa chỗ cho hình Ngoại (`.acts:has(+ .bkng)`), nút "Đem đi gieo" xuống hàng chứ không bị đè.
- Bước `cau-ca` của máy kiểm chờ 3 giây cho thẻ "Ngoại nghe đồn" hiện xong rồi mới đo (đo lúc thẻ đang phóng to ra số sai).
