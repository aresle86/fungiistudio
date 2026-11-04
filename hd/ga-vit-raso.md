# Rà soát chuồng gà / chuồng vịt (4/11/2026, theo code v107b)

## 1. Số con trên sân có khớp số trong bảng không?
- **Gà:** sân có sẵn 2 gà mái "của Ngoại" + 1 gà trống (vẽ cố định). Khi mua thêm, game sinh thêm `hens − 2` con (`gaSpawn`). → Số mái **khớp**. Gà trống luôn hiện 1 con dù `rooster` là 0 hay 1 (thực tế `rooster` không bao giờ giảm nên không lệch).
- **Vịt:** sân có sẵn 1 vịt bơi + 2 vịt đi bộ + 4 vịt con (trang trí). Khi mua thêm, sinh thêm `n − 2` con bơi. → Người chơi có 2 vịt nhưng thấy **3 vịt lớn + 4 vịt con**; có 6 vịt thì thấy 7. Vịt con trang trí hiện quanh năm dù không ấp gì. **Lệch.**

## 2. Ấp trứng: thấy gì, biết gì?
- Chỉ gà có ấp (`ga.hatch`): điều kiện cấp 5, có trống, ≥2 mái, có 1 trứng trong kho. **Luôn ấp đúng 1 trứng.** 10 tiếng nở, 12 tiếng lớn; con mái đang ấp ngưng đẻ.
- **Trong 10 tiếng ấp: ngoài sân không thấy gì** (không có gà nằm ổ, trứng trong ổ không đổi). Chỉ có một thẻ "Đang ấp trứng · còn 9 giờ" trong bảng.
- 12 tiếng gà con: có gà con chạy ngoài sân. **Lỗi:** cờ `g.hatched` chỉ tăng không giảm, nên sau lần ấp đầu tiên gà con hiện **mãi mãi** dù không còn ấp.
- Kết quả: 50% mái (thêm vào đàn nếu còn chỗ, hết chỗ thì bán 80 xu), 50% trống (giữ nếu chưa có, có rồi thì bán 80 xu). **Chỉ báo bằng một câu Ngoại nói một lần**, không có thẻ kết quả, không số bay, bỏ lỡ là không biết.
- Vịt: không ấp bằng vịt mái; có "lò ấp vịt" (ấp 4 trứng, nở thêm vịt) là món riêng. Cần rà lại cấp mở (code ghi cấp 9, bảng cấp v102 ghi lò ấp 14).

## 3. Nhiều gà/vịt có lợi thật không? (số theo code)
| | Gà | Vịt |
|---|---|---|
| Nhịp đẻ | 1 trứng / 3 giờ / con, cần 1 phần ăn mỗi trứng | 1 trứng / 4 giờ / con |
| Thức ăn | cám 6 xu/phần, hoặc 1 trái bắp = 4 phần (bắp bán 32 → đắt hơn cám) | cám 6 xu/phần, hoặc 1 bó rau muống = 4 phần |
| Trứng bán | 25 xu → lãi 19/trứng | 30 xu → lãi 24/trứng |
| Một con chăm đều | ~8 trứng/ngày ≈ **150 xu/ngày** | ~6 trứng/ngày ≈ **145 xu/ngày** |
| Giá mua | 150 xu → hoàn vốn 1 ngày | 180 xu → hoàn vốn 1,3 ngày |
| Trần | ổ chứa 3 trứng/con: không lượm trong 9 giờ là ngưng đẻ | 3 trứng/con, 12 giờ |
| Chuồng | 4 → 6 (300) → 9 (700) → 12 (1200) | 4 → 8 (500) → 12 (1200) |

→ Mua thêm con **rất lời** (hoàn vốn 1 ngày), nên "nhiều con = nhiều tiền" là đúng, nhưng bị chặn bởi ổ 3 trứng: lợi ích chỉ đến với người vào chơi 2–3 lần/ngày. Đây là trần có chủ ý, nhưng bảng chưa nói rõ "ổ đầy thì gà ngưng đẻ" ở chỗ dễ thấy.

→ **Ấp hiện không có lý do kinh tế:** tốn 1 trứng (25) + một mái nghỉ 10 tiếng (~3 trứng ≈ 75) + chờ 22 tiếng, để nhận trung bình 50% mái (150) / 50% 80 xu = 115 xu. Gần hòa vốn và chậm hơn mua thẳng 150 xu. Người chơi khôn sẽ không ấp bao giờ.

## 4. Mạch mở khoá hiện tại
Cấp 1 có gà (sửa chuồng cấp 2: 3 rơm, 2 tre, 40 xu) → cấp 5 mua gà, ấp → cấp 6 dựng chuồng vịt (4 rơm, 3 tre, 150 xu) → lò ấp vịt (cấp 9 hay 14, cần chốt) → khạp muối hột vịt cấp 8 → trứng chiên, hột vịt muối vào đơn hàng.

## 5. Đề xuất (chờ anh chốt rồi mới làm)
1. **Thấy ấp:** suốt 10 tiếng có một gà mái nằm trên ổ (model gà xẹp xuống, xoay), trứng đang ấp vẽ màu khác; bong bóng đếm giờ trên ổ như cây cổ tích. Gà con chỉ hiện trong 12 tiếng lớn, đi theo mẹ. Sửa lỗi gà con hiện mãi.
2. **Biết kết quả:** hết giờ thì thẻ trong bảng "Nở rồi: gà mái, đàn 5 → 6" (hay "gà trống, Ngoại bán 80 xu") + số bay trên chuồng + Ngoại nói. Thẻ ở lại tới khi người chơi mở bảng xem.
3. **Ấp có nghĩa:** cho chọn ấp 1–3 trứng một lứa (ổ 3 trứng), mỗi trứng 50% mái; giữ mua gà 150 là đường tắt, còn ấp là cách nhân đàn rẻ (3 trứng = 75 xu cho kỳ vọng 1,5 mái). Hoặc rõ hơn: gà nở từ ấp là "gà nhà" đẻ nhanh hơn 20%.
4. **Vịt khớp số:** bớt 1 vịt lớn trang trí, vịt con chỉ hiện khi lò ấp vịt đang có lứa.
5. **Bảng:** ô "Trong ổ" khi đầy đổi sang cảnh báo "Ổ đầy · gà ngưng đẻ" (màu cam) để người chơi hiểu trần.

## 6. Đơn hàng phải khớp (đo trên v108a, 600 đơn hàng xóm mỗi mốc, kho không còn rau)
| Cấp | Rau củ trong món đặt | Đơn có ít nhất 1 rau | Còn lại |
|---|---|---|---|
| 5 | 19% | 15% | trứng 81% |
| 8 | 11% | 15% | đồ chế biến 47%, trứng 42% |
| 12 | 8% | 13% | chế biến 35%, trứng 24%, cá 18%, món nấu 15% |
| 16 | 8% | 13% | chế biến 33%, cá 24%, trứng 23%, món nấu 13% |

**Nguyên nhân:** `ordMake` có luật "hay đặt món con từng làm": 85% số đơn chỉ chọn trong nhóm *đã biết*. Trứng, đồ phơi, đồ muối, cá, trái cây được tính là đã biết mãi mãi, còn rau chỉ được tính khi **đang có trong kho**. Người chơi hái rau xong bán liền nên rau gần như luôn bị loại. Mở càng nhiều thứ, rau càng bị pha loãng.

**Đề xuất v109: đơn theo bữa cơm**
- Rau củ là cơm hằng ngày: **mỗi đơn hàng xóm luôn có ít nhất 1 rau củ** làm món chính; "đã biết" với rau = đã từng trồng, không phải đang có trong kho.
- Đơn gom thành món ăn thật: canh chua (cà chua, đậu bắp, rau muống, kèm cá ở cấp cao), trứng chiên hành (hành + trứng gà), canh khổ qua, canh mồng tơi, rau muống xào tỏi, bắp luộc… Lý do trên đơn chính là món đó.
- Đơn hỏi 2–3 loại rau khác nhau nên tự kéo người chơi trồng đa dạng, khớp với luật đất mệt / luân canh.
- Theo cấp: 3–4 chỉ rau; 5–7 rau + đôi khi trứng; 8–11 rau + 1 món kèm (trứng, đồ muối, đồ phơi), 1/4 là đơn món nấu (vẫn kèm rau); 12+ đơn công thức 2–3 món, có cá.
- Ghe chợ nổi giữ vai đồ đi xa: trái cây, đồ khô, mứt, giỏ, mật.
- Gà vịt: trứng là món kèm, không chiếm món chính; **gà trống giống** chỉ đặt khi có trống dư (tối đa 1 đơn/ngày, giá hơn bán thẳng); **hột vịt lộn** đặt chiều tối khi đã có lò ấp; vịt con có thể là đơn hiếm.
- Mục tiêu đo lại bằng bài này: rau củ ≥ 60% số món, ≥ 90% đơn hàng xóm có rau.
