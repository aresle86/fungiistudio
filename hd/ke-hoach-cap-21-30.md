# Kế hoạch phát triển tới cấp 30 (21/11/2026, chờ anh Ares chốt)

Dựa trên: bản soi của chuyên gia dev game + chuyên gia tâm lý người chơi (21/11), cộng cách làm của mấy game cùng thể loại đang chạy. Anh Ares quyết giữ trần cấp 30.

Mọi số trong hồ sơ này **chưa chốt**. Mục "Số cần anh chốt" ở cuối.

---

## 0. Lỗ hổng đang có

| Cấp | Mở gì |
|---|---|
| 21 | — (chợ huyện `CHM.lv = 21` đã nằm trong code nhưng chưa ai mở cửa) |
| 22 | Sầu riêng + chè sầu riêng |
| 23 | — |
| 24 | Dừa sáp + dừa sáp dầm |
| 25–30 | — |

`LVFEAT` (bảng "lên cấp mở gì") **dừng ở cấp 20**. `UNLOCK` chỉ còn `saurieng: 22`, `duasap: 24`.

Từ cấp 20 lên 30 cần **72.500 điểm kinh nghiệm** — nhiều hơn cả 20 cấp đầu cộng lại (26.500) — để nhận gần như không gì.

Theo nhịp đo được (một vườn thật tới cấp 17 sau 11 ngày, ~1.400 điểm/ngày), đoạn 20→30 là **chừng 7–8 tuần chơi đều**. Chia cho 10 cấp là **khoảng 5 ngày một lần mở cái mới**. Nhịp đó chấp nhận được — với điều kiện mỗi lần mở là một thứ thật.

---

## 1. Bốn nguyên tắc cho đoạn cuối

Rút từ hai bản soi và từ game khác.

**1.1 — Cấp cao không phải "trồng nhiều hơn", mà là "bày ra".**
Tới cấp 20 người chơi đã có đủ: rau, cây trái, gà vịt, cá, phơi, muối, sấy, nấu, chợ, đơn, ghe, bạn bè. Vòng lõi **đã no**. Mấy game cùng thể loại giữ người ở đoạn cuối không bằng thêm việc làm, mà bằng **lớp trang trí và lớp sưu tầm** — chỗ người chơi bày ra cái mình đã làm được. Stardew Valley phải tới bản cập nhật gần đây mới thêm lớp đó, và người chơi nói thẳng là trước bản đó đoạn cuối quá mỏng.

**1.2 — Không thêm việc hằng ngày.**
Chuyên gia tâm lý đếm được **28 thứ** một người chơi cấp 13 phải để ý; tài liệu HUD của mình cũng ghi "vườn cấp 16 hiện ~30 bong bóng cùng lúc". Thêm 10 hệ nữa ở cấp 21–30 là giết game.

→ Mỗi thứ mở ở đoạn cuối phải là **một nơi để tới** hoặc **một cái kệ để bày**, không phải một cái nồi mới có đồng hồ riêng và bong bóng riêng.

**1.3 — Tiêu xu, đừng kiếm xu.**
Bot dư **118.000 xu** vào ngày 30. Đoạn cuối phải có chỗ tiêu, và chỗ tiêu đó **không được sinh lời** — nếu không là lạm phát tiếp.

Cảnh báo ngược từ Hay Day: game đó mở máy móc mà người chơi chưa đủ tiền mua, thành ra bỏ đơn, bỏ ghe, và một game thư giãn biến thành một cuộc cày khổ sở. **Bài học: món đắt phải mở ĐÚNG lúc người chơi đã dư tiền, không được sớm hơn.** Áo lụa 5.000 xu, bộ lãnh Mỹ A 12.000 xu nên nằm ở cấp 23–25, không phải cấp 21.

**1.4 — Sau cấp 30 không được hết.**
Cấp 30 là cái mốc "vườn mình đã thành", không phải màn hình "hết game". Ba thứ phải chạy tiếp vô hạn sau đó: **Sổ** đầy dần, **mùa** quay vòng (Tết, nước nổi, Kỳ Yên), **vườn** còn bày tiếp được.

---

## 2. Ba trụ

Thay vì rải 10 thứ lặt vặt, gom thành ba trụ. Mỗi trụ là một mạch, có mở đầu và có kết.

### Trụ 1 — Chợ huyện: một nơi chốn khác
Người chơi 20 cấp chỉ biết có mảnh vườn và khúc sông trước nhà. Cho họ **đi đâu đó**. Đi đò máy, mất tiền đò, lên tới nơi là một cảnh khác hẳn: nhà lồng chợ, dãy phố sơn vàng, bảng hiệu sơn tay.

Đây là trụ **sẵn sàng nhất**: `CHM` đã nằm trong code, hình chợ huyện bản 5 và hình đồ may đã được anh duyệt từ 9/11. Phần còn lại là ráp vào.

- Tiệm may cô Ba: đo ni, chọn vải, đặt cọc, chờ, lên lấy, thử đồ
- **May cho Ngoại** — Ngoại mặc liền, hình Ngoại trong khung nói chuyện đổi theo
- Tiệm chụp hình: mặc đồ mới chụp chung với Ngoại, **treo tấm hình trong nhà**

Trụ này tiêu xu rất mạnh (600 → 15.000 xu một món) và không sinh một đồng lời nào. Đúng chỗ cần.

### Trụ 2 — Đình làng và hội: cái năm có hình dáng
Hiện game có đúng một mùa là Tết. Một năm chỉ có một cái mốc thì 11 tháng còn lại phẳng lì.

- **Đình làng** mở ra như một nơi chốn thứ ba (sau vườn và chợ huyện)
- **Lễ Kỳ Yên** — hội làng hằng năm: góp mâm bằng đồ vườn mình, xem hát bội
- **Mùa nước nổi** — mùa thứ hai: nước lên, bông điên điển, cá linh, đặt lờ

Trụ này nối thẳng vào Bến bà con đã có. Và nó phục vụ cái mà nghiên cứu game thư giãn gọi là *nhu cầu thuộc về một nơi* — thứ mà vườn một mình không cho được.

### Trụ 3 — Sổ và vườn mình: bày ra
- **Bộ sưu tập trang trí** (đã thiết kế trong `plan-trangtri-dat.md`): bộ Tết 1.500, bộ sân hiên 2.000, bộ bến sông 2.500. Đặt đủ bộ thì có hiệu ứng nhỏ + dấu trong Sổ
- **Ao cá ba bậc** (đã duyệt trong `ao-cong-trinh.md`): 2×2 → 2×3 → 3×3, có cồn giữa ao, chòi lá
- **Bảng tên vườn**
- **Sổ** — "Một năm ở vườn Ngoại" mở ở cấp 20, từ đó đầy dần và **không bao giờ đầy hết**

---

## 3. Bảng cấp 21–30

| Cấp | Mở | Trụ | Đã có gì |
|---|---|---|---|
| **21** | Chợ huyện + đò máy · Tiệm may cô Ba (vải bông, xi-ta: áo bà ba, quần đen, khăn rằn) · Tủ đồ | 1 | `CHM` trong code; hình chợ + hình đồ may đã duyệt |
| **22** | Sầu riêng + chè sầu riêng · **May cho Ngoại** | 1 | Giống đã có trong code; luồng may đã thiết kế |
| **23** | Vải sang: lụa, lãnh Mỹ A · **Áo dài** · Bộ sân hiên | 1 + 3 | Đã thiết kế cả hai |
| **24** | Dừa sáp + dừa sáp dầm · **Ao vừa 2×3**: kè bờ, cầu ao | 3 | Giống đã có; ao đã duyệt |
| **25** | **Tiệm chụp hình** — chụp chung với Ngoại, treo trong nhà | 1 | Đã thiết kế |
| **26** | **Đình làng** mở | 2 | Ý đã duyệt, chưa thiết kế |
| **27** | **Lễ Kỳ Yên** · Bộ bến sông | 2 + 3 | Chưa thiết kế |
| **28** | **Ao lớn 3×3**: cồn giữa ao, chòi lá, câu cá ao | 3 | Đã duyệt |
| **29** | **Mùa nước nổi** | 2 | Ý đã duyệt, chưa thiết kế |
| **30** | **Bảng tên vườn** · Tấm hình cả vườn chụp với Ngoại · Sổ trọn một năm | 3 | B3 trong `truoc-quang-ba.md` |

**Đọc theo hàng dọc:** cấp 21–25 là mạch chợ huyện (mặc đẹp, chụp hình) — mạch về *mình*. Cấp 26–29 là mạch đình làng và mùa — mạch về *xóm*. Cấp 30 khép lại bằng tấm hình cả vườn.

**Bảy trong mười cấp dùng thứ đã thiết kế hoặc đã duyệt hình.** Chỉ có đình làng, Kỳ Yên và mùa nước nổi là phải làm mới.

---

## 4. Những gì KHÔNG nên làm ở đoạn cuối

Rút từ chỗ game khác hỏng.

- **Không thêm giống cây mới sau cấp 24.** Thêm giống là thêm một dòng trong mọi bảng, mọi đơn, mọi món — tốn mà không ai thấy.
- **Không thêm máy chế biến mới.** Nong, khạp, lò, hố ủ, bếp, quầy nước đã là sáu cái. Cái thứ bảy không làm ai vui.
- **Không làm "cấp vượt cấp" (prestige) kiểu chơi lại từ đầu để lấy thưởng.** Mấy game dùng cách đó để lấp đoạn cuối, và người chơi gọi đúng tên: lấp chỗ trống bằng cách bắt làm lại. Vườn của Ngoại là một chỗ, không phải một ván chơi.
- **Không bày mục tiêu đếm được lên màn hình** (kiểu "còn 3/10 món nữa"). Sổ thì mở ra mới thấy. Đúng luật đã khoá.
- **Không có bảng xếp hạng.** Kết bạn một chiều, không so đo — giữ nguyên.

---

## 5. Thứ tự làm

Ba bản sửa trước đã bàn (chống mất vườn → 20 phút đầu → chỉnh số) vẫn đi trước. Sau đó:

**Đợt A — Chợ huyện** (lâu nhất, nhưng hình đã có)
1. Chợ huyện thành cảnh riêng: dựng khi đi đò, gỡ khi về (vườn không nặng thêm)
2. Tủ đồ + lưu đồ đang mặc; nhân vật và hình đại diện dựng theo đồ
3. Tiệm may: đo ni, chọn vải, đặt cọc, chờ, lấy, thử
4. May cho Ngoại + hình Ngoại đổi theo
5. Tiệm chụp hình

→ Mở cấp 21, 22, 23, 25.

**Đợt B — Vườn mình**
6. Ao bậc 2 và bậc 3 + đồ trang trí ao
7. Bộ sưu tập trang trí (sân hiên, bến sông) + dấu trong Sổ
8. Bảng tên vườn

→ Mở cấp 23, 24, 28, 30.

**Đợt C — Xóm**
9. Đình làng
10. Lễ Kỳ Yên
11. Mùa nước nổi

→ Mở cấp 26, 27, 29.

Đợt C là đợt duy nhất phải thiết kế từ đầu, nên để sau cùng — lúc đó cũng đã có người chơi thật tới cấp 26 để hỏi ý.

---

## 6. Số cần anh chốt

| Chỗ | Đề nghị | Ghi chú |
|---|---|---|
| Bảng kinh nghiệm cấp 21–30 | **Giữ nguyên** | 72.500 điểm chia cho 10 lần mở là ~5 ngày một lần. Hợp lý khi có nội dung |
| Tiền đò lên chợ huyện | 20–30 xu/chuyến | Đã ghi trong `plan-tiemmay.md` |
| Giá đồ may | khăn rằn 600 · bà ba vải bông 1.500 · xi-ta 2.500 · lụa 5.000 · lãnh Mỹ A 12.000 · áo dài 15.000 | Đã ghi trong `plan-tiemmay.md`, anh góp ý 9/11 |
| Ao bậc 2, bậc 3 | Chưa có số | Cần chốt xu + giờ xóm đào |
| Bộ sưu tập trang trí | Tết 1.500 · sân hiên 2.000 · bến sông 2.500 | Đã ghi trong `plan-trangtri-dat.md` |
| Có làm mùa nước nổi không | Có, ở cấp 29 | Mùa thứ hai của năm; nếu anh thấy nặng thì bỏ, cấp 29 lấy bộ trang trí thay |

---

## 7. Hai chỗ em chưa chắc

1. **Chưa ai chơi tới cấp 21.** Vườn cao nhất hiện là cấp 17. Cả bảng này là suy từ thiết kế, không phải từ người chơi thật. Nên làm đợt A trước rồi xem người đầu tiên tới cấp 21 phản ứng sao, đừng làm hết ba đợt rồi mới nhìn.

2. **Tiệm chụp hình là canh bạc lớn nhất và cũng đáng nhất.** Tấm hình chụp chung với Ngoại treo trong nhà — đó có thể là thứ người chơi chụp màn hình gửi cho nhau, tức là thứ kéo người mới về. Nhưng nó cũng là món khó làm nhất trong đợt A. Nếu phải cắt bớt để kịp, cắt cái khác, đừng cắt cái này.
