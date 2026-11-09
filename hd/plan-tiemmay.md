# Tiệm may cô Ba ở chợ huyện (anh Ares góp ý 9/11, chờ duyệt hình mẫu)

## Mở theo cấp
- **Cấp 21:** mở đường lên chợ huyện. Ngoại chỉ đường, không đi theo:
  "Ngoại nghe nói cô Ba trên chợ huyện mới về vải mới đó con. Đi đò máy lên, tới bến hỏi tiệm may cô Ba là ai cũng biết."
  Đi đò máy, tiền đò 20–30 xu mỗi chuyến (đặt may một chuyến, lấy đồ một chuyến). Vải bông, vải xi-ta; áo bà ba, quần đen, khăn rằn.
- **Cấp 23:** cô Ba nhận vải sang: lụa, lãnh Mỹ A (chỉ đen tuyền, nhuộm trái mặc nưa). Mở áo dài cho Tết.
- **Cấp 25:** tiệm chụp hình ở chợ huyện: mặc đồ mới chụp hình chung với Ngoại, treo trong nhà. Cô Ba có học trò, may được 2 món một lúc.
- Tủ đồ (chạm nhân vật thay đồ) mở sớm từ cấp 5 với 6 bộ có sẵn.

## Luồng đặt may
1. Chọn **may cho ai**: cho con, hoặc **may cho Ngoại**.
2. Chọn kiểu, chọn vải, màu, hoa văn (khăn rằn phối 2 màu ô).
3. Đo ni lần đầu: một mình người chơi, cô Ba cầm thước dây đo, ghi sổ. Lần đầu may cho Ngoại: cô Ba nói "Ngoại con thì cô may cho bà hoài, số đo cô còn giữ nè."
4. Đặt cọc nửa tiền, cô Ba hẹn ngày; vô tiệm thấy cô Ba đạp máy may, thanh tiến độ.
5. Đi đò lên lấy, trả nốt tiền, thử đồ. Đồ cô Ba giữ hoài nếu chưa lấy. Không có nút may gấp.

## Nam, nữ (đề xuất, chờ anh chốt)
- Nhân vật hiện có 6 dáng không gắn giới tính (khác nhau ở kiểu tóc), giữ vậy, không bắt chọn nam/nữ.
- Đồ chia theo **kiểu may**, ai mặc cũng được:
  - Áo bà ba: kiểu ôm eo, tay lửng (thường của nữ) · kiểu suông, cổ trụ, túi hai bên (thường của nam).
  - Áo dài: áo dài nữ · áo dài nam kèm khăn đóng.
  - Nón: nón lá · nón tai bèo · mũ phớt.
  - Khăn rằn, quần đen, quần lãnh: chung.
- Cô Ba gợi ý kiểu hợp với dáng nhân vật đang chọn (theo kiểu tóc), người chơi đổi được.

## May cho Ngoại
- Áo bà ba, khăn rằn, nón lá, áo dài (cấp 23) cho Ngoại.
- Đem về đưa Ngoại: Ngoại mặc liền, nhân vật Ngoại trong vườn và hình Ngoại trong khung nói chuyện đổi theo.
- Ngoại nói một câu theo món, ví dụ: "Trời đất, may chi cho Ngoại tốn tiền vậy con. Mà đẹp thiệt, mai Ngoại mặc đi chùa."
- Ngoại có tủ đồ riêng; mỗi ngày Ngoại tự chọn mặc một bộ trong tủ (dịp Tết, rằm thì mặc đồ đẹp nhất).

## Giá (chỗ tiêu xu cuối game)
Khăn rằn ~600 · áo bà ba vải bông ~1.500 · xi-ta ~2.500 · lụa ~5.000 · bộ lãnh Mỹ A ~12.000 · áo dài ~15.000 xu. Thời gian may: 4–12 tiếng tùy vải; mùa Tết lâu hơn, Ngoại nhắc đặt sớm.

## Bước làm
1. Hình mẫu: áo bà ba, khăn rằn trên nhân vật và trên Ngoại, vài loại vải; một góc chợ huyện có tiệm may. Gửi anh duyệt.
2. Giao diện tiệm may, tủ đồ.
3. Ráp vào game, test.

## Đã duyệt (9/11)
- Hình mẫu đồ may (`may123.py`, chụp bằng `tMay123.js` -> ../hud16/may_mau.png): bà ba ôm eo / suông cổ trụ, 4 loại vải, khăn rằn, nón lá, nón tai bèo, mũ phớt; đồ cho Ngoại (`NGOAIB(OF)`). Bỏ biến thể Ngoại khăn trùm đầu.
- Chợ huyện bản 5 (`ch124.js`, chụp bằng `tCh124.js` -> ../hud16/ch124_*.png). Câu mô tả: "Buổi sáng chợ huyện miền Tây bên bờ sông: nhà lồng chợ mái ngói hai tầng làm điểm nhận, dãy phố một trệt một lầu sơn vàng, xanh có bảng hiệu sơn tay, tiệm may cô Ba phơi áo bà ba trước hiên, đò máy cập bến."
  Bố cục: sông · bến đò (cầu tàu chữ L, chòi BẾN ĐÒ) · sân gạch tàu có nhà lồng chợ + sạp dù · đường có cây me, cột đèn thấp · dãy 8 nhà phố (cà phê, tạp hóa, tiệm vàng, thuốc bắc, TIỆM MAY CÔ BA, chụp hình, hớt tóc, xe đạp) · nền nâu tới sau dãy nhà · bãi cỏ, 3 cây dừa.
  Anh Ares dặn: không bày cây cho rối; ghe không đâm, không lún; đo va chạm bằng `window.__chHit`, độ ngập ghe bằng `window.__chSink`.

## Ráp vào game (chưa làm)
1. Chợ huyện thành một cảnh riêng: dựng khi đi đò lên, gỡ khi về (vườn không nặng thêm). Nút "Lên chợ huyện" mở từ cấp 21, tiền đò.
2. Tủ đồ (cấp 5) + lưu đồ trong ST (`ST.do`), nhân vật vườn và hình avatar dựng theo đồ đang mặc.
3. Tiệm may cô Ba: chọn may cho ai, kiểu, vải, màu, hoa văn; đo ni lần đầu; đặt cọc, chờ may, lấy đồ. Đồ của Ngoại dựng lại hình Ngoại (`NGOAIB`).
4. Lời Ngoại, cô Ba (Việt, Anh); test; đo nóng máy khi ở chợ huyện.
