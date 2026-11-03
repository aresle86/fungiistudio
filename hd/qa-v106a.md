# Miệt Vườn 2.0 · QA/QC bản v106a (3/11/2026)

Khung đánh giá: **design-critique** và **design-system audit** (plugin Design của Anthropic), **ui-ux-pro-max** (checklist trước khi giao), **gamedev-mietvuon** (game-ui-ux, game-feel, input, performance, audio).
Đo bằng script trên trình duyệt thật: điện thoại 390×664 và máy tính 1280×800 (`tPop.js`, `tAudit.js`, `tHiss.js`, `tA106.js`).

Mức độ: 🔴 nặng (người chơi kẹt hay mất đồ) · 🟡 vừa (khó hiểu, xấu, lệch kinh tế) · 🟢 nhẹ (đánh bóng)

---

## 0. Đã sửa trong đợt này (đã có trong v106a, chưa lên live)

| Việc | Trước | Sau |
|---|---|---|
| Chạm ma trên điện thoại | Chạm ô đất trống là tự đắp liếp; chạm nong tự mở chọn món (click trình duyệt bắn theo trúng nút trong bảng vừa mở) | Nuốt click đó trong 450 ms. `tA106` điện thoại: đất trống mở đúng bảng "Đất trống" |
| Popup chồng nhau | Thanh "Đặt đồ" đè "Ngoại nhờ"; thẻ "Về vườn" đè "Ngoại nhờ"; lên cấp mà Ngoại + thẻ việc vẫn hiện; toast đè bảng, Sổ | Một lúc một thẻ: thẻ mới hiện thì thẻ thấp hơn nhường chỗ. Toast dời lên trên khi mở bảng, xuống đáy khi mở Sổ. Thanh đặt đồ trên máy tính lên giữa trên. `tPop`: **0 chỗ chồng / 22 cảnh** |
| Tiếng xì xì | Nước mương là nhiễu 2,5 kHz kêu đều mọi lúc. Dải 2–5 kHz: sàn −64,9 dB, đỉnh −60,5 (đều đều) | Nước 900 Hz, chỉ nghe gần mương, từng đợt; lá, gió lặng giữa cơn. Dải 2–5 kHz: sàn **−82,6 dB** (nhỏ hơn ~18 dB), đỉnh −67 |
| Sổ cổ tích nói số cấp tương lai | "??? · cấp 14" | "???" + tên tích + lời gợi ý của Ngoại |
| Font Patrick Hand trong hình test | Hình chụp test ra font viết tay khác (do test chặn Google Fonts) | Trang test nạp font trong máy. **Game không đổi font** |

---

## 1. Ba điểm anh nêu

### 1.1 🟡 Tab Sổ xấu (Việc · Kho · Bộ sưu tập)

**Đánh giá (design-critique):**
- Ba tab ba cỡ: tab đang mở 84×84, hai tab kia 62×48 và **chỉ còn icon** (chữ bị ẩn, `font-size:0`). Người chơi mới không biết tab xanh lá là gì.
- Chữ trắng trên vàng ("Kho") tương phản thấp. Icon bọc viền trắng dày như sticker, lệch phong cách với icon trong trang.
- Tab đang mở tách khỏi trang giấy, không liền mạch như tab sổ thật.
- Gốc rễ: khoảng 25 luật CSS `.bkt` vá chồng qua nhiều bản, rất nhiều `!important`. Sửa lẻ sẽ còn vỡ tiếp.

**Đề xuất:**
1. Ba tab bằng nhau, luôn có **icon nhỏ + chữ** (Việc · Kho · Sưu tập), chữ màu mực nâu `--ink` trên nền tab nhạt.
2. Tab đang mở dùng **cùng màu giấy với trang** và dính liền trang, cao hơn 6px. Tab không mở tối hơn, thấp hơn, như nằm phía sau.
3. Bỏ viền trắng dày quanh icon.
4. Gom về **một khối CSS duy nhất**, xoá các lớp vá cũ.

→ Em làm hình mẫu (máy tính + điện thoại) gửi anh duyệt trước rồi mới gắn vào game.

### 1.2 🟡 Hố ủ phân chưa rõ công dụng, "bỏ rau dư" vô nghĩa

**Code đang chạy thế này:**
- Đất liếp tụt **0,12 mỗi lần hái**. Trồng **lặp lại cùng loại rau thì tụt gấp đôi** (có luân canh ngầm).
- Đất tự hồi rất chậm (0,04 mỗi giờ).
- **Sản lượng = 55% + 45% × đất.** Đất kiệt chỉ ra khoảng 60% so với đất tốt.

Nghĩa là hố ủ có giá trị thật, nhưng người chơi **không thấy mình đang mất gần nửa sản lượng**. Chỉ có màu đất xỉn đi, vết nứt và mấy chấm "Đất" nằm trong bảng liếp. Còn nút "Bỏ 1 rau dư" là **bỏ rau tươi trong kho**, đúng như anh nói, game không có rau hư.

**Đề xuất:**
1. **Cho thấy cái giá của đất mệt:** khi hái trên liếp đất mệt, chữ bay ghi "Đất mệt · hụt 2 bó". Lần đầu Ngoại nói: "Đất trồng hoài một thứ là mệt, bón phân ủ thì đất mới lại sức." Liếp đất mệt có bong bóng nhỏ hình bao phân, giống bong bóng tưới nước.
2. **Thay "Bỏ 1 rau dư" bằng phân chuồng:** chuồng gà, vịt mỗi ngày có phân, bấm "Hốt phân chuồng" bỏ vô hố. Đúng cách ủ ở miền Tây (phân gà vịt + lá + lục bình), và nối hố ủ với chuồng sẵn có.
3. **Xác rau sau thu hoạch tự vào hố +1 phần** (gốc, lá úa), không cần bấm.
4. Ghi rõ trong bảng hố: "Bón 1 bao: liếp ra thêm chừng 2 bó mỗi vụ."

### 1.3 🔴 Giỏ lục bình: không biết làm gì, lục bình về không đủ

**Chuỗi hiện tại** (4 bước, không bước nào chỉ sang bước sau):
vớt lục bình → *(vịt ăn trước, vịt no mới lên gác bếp)* → mở nong, chọn "Lục bình khô" (5 tươi → 5 khô, **6 tiếng**) → mở hiên nhà, Ngoại đan (5 khô → 1 giỏ, 1 tiếng, tối đa 4/ngày) → bán ghe.

**Cung và cầu:**
- Lục bình mọc mỗi 35 phút, **trên mương tối đa 2 bụi**. Chơi 3 lần/ngày vớt được khoảng 6 bụi.
- Thứ tự khi vớt: **máng vịt trước** (12 vịt = máng 24 phần), gác bếp sau, hố ủ cuối. Có vịt thì gần như mọi bụi vào máng.
- 1 giỏ cần 5 bó; mức trần 4 giỏ/ngày cần 20 bó. Thực tế **khoảng 0–1 giỏ/ngày**, trong khi ghe vẫn đặt giỏ. **Không khớp.**

**Đề xuất:**
1. **Dẫn đường:** lần đầu lục bình lên gác bếp, Ngoại nói "Đủ 5 bó thì đem phơi nong cho khô, Ngoại đan giỏ cho." Việc hôm nay có "Phơi 5 bó lục bình". Bảng hiên nhà hiện cả **lục bình tươi x/5**, kèm nút **"Đem phơi"** mở nong và chọn sẵn lục bình. Chạm bụi lục bình đầu tiên thì chữ bay chỉ đường "Lên gác bếp · đủ 5 bó đem phơi".
2. **Từ cấp 15 (khi mở giỏ):** trên mương tối đa 4 bụi, mọc mỗi 20 phút. Vịt chỉ ăn lục bình khi máng **dưới một nửa**. Như vậy chơi 3 lần/ngày được khoảng 10–12 bó, đủ 2 giỏ.
3. Phơi lục bình **6 tiếng → 3 tiếng** cho nhịp khớp với ghe chờ 6 tiếng.
4. Chạy lại bot để so số giỏ/ngày với số đơn giỏ của ghe trước khi chốt.

### 1.4 🔴 Đổi công: vườn bạn không còn liếp cần tưới thì kẹt

**Code:** tưới giùm 1 liếp = 1 công = 1 lần hái ké (tối đa 5/ngày). Chỉ tưới được liếp **có cây, chưa chín, ẩm dưới 90%, chưa ai tưới giùm**. Chạm liếp chín khi chưa có công thì Ngoại lặp "Tưới giùm X một liếp trước…", nhưng không còn liếp nào tưới được. **Không có lối thoát.**

**Hay gặp nhất:** bạn vắng vài ngày nên cả vườn chín (cây chín không héo), không còn liếp chưa chín để tưới, nên người ghé không hái ké được gì, đúng lúc vườn đáng ghé nhất. Ngoài ra: bạn vừa tưới xong, phủ rơm, vườn toàn giàn, vườn trống.

**Đề xuất:**
1. Thêm cách đổi công thứ hai **"Hái giùm"**: hái 1 liếp chín cho chủ vườn (rau vào kho chủ) được 1 công. Đúng tinh thần đổi công: qua phụ hái rồi được biếu.
2. Khi hết liếp để tưới, Ngoại nói rõ: "Vườn X tưới đủ rồi, con phụ hái giùm một liếp rồi hái ké nghe."
3. Hộp thư chủ vườn: "Y ghé hái giùm 1 liếp cải."
4. Phải sửa hàm `mv2_act` trên Supabase (thêm loại `help_cut`) để rau vào đúng kho chủ, chống gian lận. Xem hàm hiện tại trước khi làm.

---

## 2. Design critique: các màn chính

### Ấn tượng chung
Phong cách đúng hướng "đất sét/đồ chơi" ấm áp: ván gỗ, giấy dó, viền nâu, bo tròn. ui-ux-pro-max cũng xếp game vào kiểu Claymorphism, hợp game nhẹ nhàng nên **không cần đổi phong cách**. Cơ hội lớn nhất là **sự nhất quán** (mục 3) và **chữ quá nhỏ trên điện thoại**.

### Dễ dùng
| Phát hiện | Mức | Đề xuất |
|---|---|---|
| Nút đóng (×) bảng và Sổ 36×36px, dưới chuẩn 44px | 🟡 | Giữ hình 36px nhưng mở vùng chạm ra 44px (padding trong suốt) |
| Nút "Đi làm ›" trong Sổ › Việc 78×30px | 🟡 | Cao tối thiểu 44px |
| "San thành đất trống" trong vòng gieo 28px cao | 🟡 | 44px, hoặc đưa vào hàng nút chính của vòng |
| Nút "Bán 1" ở Chợ 42×44 | 🟢 | Nới 2px ngang |
| Tab Chợ (Đơn hàng/Bán/Mua/Tiệm) cao 40px | 🟢 | 44px |
| Bàn phím chỉ có Esc | 🟢 | Thêm phím tắt S (Sổ), C (Chợ), Space (cất đồ) cho máy tính |

### Thứ bậc thị giác
- **Mắt nhìn đầu tiên:** Ngoại và bóng nói, rồi tới thẻ "Ngoại nhờ". Đúng, vì việc chính nằm ở đó.
- **Cạnh tranh:** trên điện thoại có 6–10 bong bóng chờ việc (liềm, cuốc) cùng hiện, và cùng cỡ với nút HUD. Nên thu nhỏ bong bóng ở xa và chỉ phóng to bong bóng gần camera.
- Bảng Chợ: thẻ "Kho 16/60 chỗ" to hơn danh sách hàng nên chiếm sự chú ý. Danh sách mới là việc chính, nên gọn thẻ đầu lại.

### Trợ năng (đã loại các dòng đo nhầm chữ HUD nằm trên tấm gỗ)
| Chỗ | Đo được | Chuẩn |
|---|---|---|
| Chữ nút HUD trên điện thoại (Ghé vườn, Sổ, Chợ, Cài đặt, Về giữa) | **11px** | ≥12px, nên 13px |
| Nhãn "NGOẠI NHỜ" | **10px** | ≥12px |
| "Việc hôm nay 1/5" | 11,5px | ≥12px |
| Giá trong Tiệm ("-300 xu") | 11px | ≥12px |
| Sổ cá: "Thường", "mé lục bình · cả ngày" | 11px | ≥12px |
| Số vàng trong Kho ("4" củi) | 2,5:1 | ≥3:1 (chữ lớn) |
| Số xanh "3" hạt | 2,9:1 | ≥3:1 |
| Thưởng "+65" vàng | 2,6:1 | 4,5:1 |
| Chữ nâu nhạt `#A07A55` (0/5, Chưa làm, mô tả việc) | 3,6:1 | 4,5:1, đổi sang `#8A5D3B` |
| Chữ trắng trên huy hiệu xanh (số đơn) | 3,1:1 | đậm hơn: nền `#4F7D44` |

### Điểm làm tốt
- Giọng chữ miền Tây nhất quán, ấm. Icon 3D cùng một bộ, cùng ánh sáng.
- Bảng nào cũng theo khung "hero → nút chính → thẻ số → Cách làm", dễ học.
- Có chế độ chất lượng đồ hoạ, lưu sau mỗi hành động, tự lưu mây khi ẩn tab, âm thanh tắt khi ẩn tab.

---

## 3. Design-system audit

**Tổng: 48/100.** Bộ nhận diện có, nhưng giá trị gõ cứng quá nhiều nên mỗi bản vá lại lệch thêm.

### Token
| Loại | Có biến | Gõ cứng |
|---|---|---|
| Màu | ~20 biến (`--cream`, `--wood`, `--ink`, `--leaf`, `--vg`, `--dz`…) | **999 lần gõ mã hex, 167 màu khác nhau.** `#6B4529` gõ 268 lần dù đã có `--woodD`/`--vgD` |
| Khoảng cách | 1 (`--g: 8px`) | 62 giá trị; 38 giá trị lệch lưới 4px (471 chỗ: 6, 10, 14, 3, 5, 9px…) |
| Chữ | 3 font, tốt | 27 cỡ chữ (10→90px), 18 chỗ dưới 12px |
| Bo góc | 3 (`--r1/2/3`) | 32 giá trị |
| Bóng | 2 (`--hi`, `--lift`) | **136 kiểu bóng** |
| Chuyển động | 0 | 57 thời lượng khác nhau |
| Lớp chồng (z-index) | 0 | 19 mức (−1 → 200), chính nó gây popup chồng |
| `!important` | — | 261 |

### Thành phần
| Thành phần | Trạng thái | Biến thể | Ghi chú | Điểm |
|---|---|---|---|---|
| Nút `.btn` | thường, `.g` xanh, `.r`, tắt, giữ-để-làm | g, r, s1, sall | ít `:hover` (2 luật) | 7/10 |
| Bảng (sheet) | mở, cuộn, nhớ cuộn | — | ổn | 8/10 |
| Tab Sổ | — | 3 cỡ khác nhau | vá chồng, mục 1.1 | 3/10 |
| Chip (Sổ, Tiệm) | on/off | 2 kiểu chip gần giống nhau (`.bkchip`, `.tchip`) | gộp làm một | 6/10 |
| Toast | thường, `.lo` | — | có chỗ riêng khi mở bảng, Sổ | 7/10 |
| Thẻ nổi (Ngoại nhờ, Về vườn, thanh đặt) | — | — | nay đã có luật nhường chỗ | 6/10 |

### Việc nên làm (thứ tự)
1. **Bảng màu 12 token** (gỗ 3 bậc, giấy 2, mực 2, lá 2, vàng rơm, đỏ ghim, xanh nước). Thay dần 999 mã hex: đổi theo từng bảng khi đụng tới, không làm một lần.
2. **Thang z-index đặt tên:** cảnh → HUD → thẻ nổi → bảng/Sổ → lên cấp → toast. Hết chuyện chồng.
3. **Thang cỡ chữ 6 bậc** (12, 13, 15, 18, 24, 32) và lưới khoảng cách 4px.
4. **3 thời lượng chuyển động** (nhanh 150 ms, vừa 250 ms, chậm 450 ms) + `prefers-reduced-motion` áp toàn bộ (hiện chỉ có ở 4 chỗ).

---

## 4. Gamedev QA

| Mảng | Phát hiện | Mức | Đề xuất |
|---|---|---|---|
| Hiệu năng | **645 draw call trên điện thoại, 1.188 trên máy tính**, ~1.150–1.380 geometry. Máy yếu sẽ giật, nóng máy | 🔴 | Gộp cỏ, rào, cọc, mương thành `InstancedMesh` hay `mergeGeometries` theo khu. Mục tiêu dưới 250 draw call trên điện thoại |
| Âm thanh | Tiếng xì: đã sửa. Dế đêm kêu mỗi 0,7–1,6 giây ở 4,6 kHz suốt đêm | 🟢 | Cho dế thành từng tràng rồi nghỉ, đừng đều |
| Game feel | Hái, bán, nhận thưởng đã có chữ bay, bụi, tiếng, rung. Bón phân, phơi xong, đan xong giỏ còn nhạt | 🟢 | Thêm "pop" (phóng to rồi nhún về) cho icon bay vào gác bếp, kho |
| Input | Đã sửa chạm ma. Giữ tay 520 ms trên liếp mới mở bảng liếp, khó tự khám phá (chưa rà hết lời Ngoại có nhắc chỗ nào không) | 🟢 | Lần đầu Ngoại chỉ "Giữ tay lên liếp để coi chi tiết" |
| Lưu | Lưu sau mỗi hành động, mây khi ẩn tab: tốt. Không lưu ở `pagehide` | 🟢 | Thêm lưu cục bộ ở `pagehide` (Safari iOS đóng tab) |
| Chế độ giảm chuyển động | Chỉ 4 chỗ tôn trọng | 🟢 | Áp chung cho lá bay, rung camera, pháo giấy |
| Kinh tế | Lục bình, giỏ lệch (mục 1.3). Bot v102 ghi xu dư ~90k ngày 30 | 🟡 | Phần C (chỗ tiêu xu) đã duyệt sẽ giải phần này |

---

## 5. Thứ tự đề xuất

1. **Giỏ lục bình**: dẫn đường + tăng lục bình (1.3). Người chơi đang kẹt thật.
2. **Đổi công "Hái giùm"** (1.4). Hiện kẹt cứng khi vườn bạn chín hết.
3. **Hiệu năng draw call** (mục 4). Ảnh hưởng mọi người chơi điện thoại.
4. **Hố ủ**: cho thấy đất mệt + phân chuồng (1.2).
5. **Tab Sổ** làm lại, gửi hình duyệt (1.1).
6. **Chữ ≥12px, vùng chạm 44px, tương phản** (mục 2). Sửa nhanh, làm chung một đợt.
7. **Token màu và z-index** (mục 3). Làm dần mỗi lần đụng tới một bảng.

Ghi chú test: `tA106.js` trên điện thoại thỉnh thoảng chạm trượt ô vì camera chưa dừng (lần 1 trượt, lần 2 qua hết). Nên tăng thời gian chờ camera hay chờ tới khi camera đứng yên.
