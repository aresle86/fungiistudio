# Đề xuất v107 · đất, ao cá, chuỗi nhiệm vụ, giá đồ muối (3/11/2026, chờ anh chốt)

Trả lời bốn điểm anh nêu từ bảng "Đất trống". Phần số liệu lấy thẳng trong code v106.

## 1. Bảng "Đất trống": vì sao "Đắp liếp" nổi bật, ao cá đòi gì

**Hiện tại:** nút xanh "Đắp liếp" luôn là nút chính vì đó là việc hay làm nhất với ô đất. Ao cá (cấp 16, 300 xu) cần **4 ô đất của con nằm sát nhau thành hình vuông 2 ô ngang × 2 ô dọc**, ô đang chạm là góc trên bên trái, cả 4 ô phải trống (chưa đắp liếp, chưa đặt đồ). Bảng chỉ ghi "Cần 4 ô trống sát nhau", không chỉ ô nào, nên người chơi không biết phải dọn ô nào.

**Đề xuất:**
- Thẻ "Hay đào ao cá" vẽ **lưới 2×2 nhỏ** ngay trong thẻ: ô đang chạm tô đậm, 3 ô còn lại tô xanh nếu trống, đỏ kèm lý do nếu vướng ("ô 7 đang có liếp", "ô 10 chưa khai hoang"). Nút "Đào ao" sáng khi cả 4 ô xanh.
- Ở ô có thể đào ao, hiện **cả hai nút cùng cỡ**: "Đắp liếp" và "Đào ao cá · 300 xu", không ưu tiên nút nào. Ô không đủ 2×2 thì giữ như cũ.
- Lời Ngoại lần đầu tới cấp 16: "Ao cá chiếm bốn ô đất vuông vức, con chọn góc nào trống bốn ô rồi chạm ô trên cùng bên trái."

## 2. Khu đất mới mở khi khu cũ chưa khai hoang hết

**Hiện tại:** ba khu mở theo cấp, không nhìn khu trước:
| Khu | Số ô | Mở ở cấp | Việc lên cấp chỉ đòi |
|---|---|---|---|
| Bãi hông nhà | 12 | 7 | 2 liếp (cấp 8) |
| Mé sông | 8 | 9 | 2 ô khai hoang (cấp 10) |
| Sau nhà | 10 | 11 (góp 250 xu ở cấp 12) | không đòi ô nào |

Bot cấp 16 ngày 19 mới mở 27 liếp trên tổng 30 ô + vườn chính, nghĩa là khu nào cũng dở dang.

**Đề xuất:** khu sau chỉ mở khi khu trước làm được **hơn nửa**, và việc Ngoại dặn nói rõ:
- Mé sông mở khi bãi hông nhà có **≥ 8/12** ô là đất của con. Việc cấp 10 thành "Làm đủ 8 ô bãi hông nhà, khai hoang 2 ô mé sông, câu 1 con cá".
- Sau nhà mở khi mé sông có **≥ 6/8** ô. Việc cấp 12 thành "Làm đủ 6 ô mé sông, góp 250 xu dọn tre gai".
- Bảng khu (tấm bảng "Mé sông · Khai hoang 80 xu") ghi thêm "Mở khi bãi hông nhà đủ 8 ô · đang 5/8", không nói số cấp.
- Người chơi cũ đã mở khu rồi thì giữ (`ST.keep`).

## 3. Chuỗi nhiệm vụ: làm có người đặt, đặt có chỗ bán

**Hiện tại:** việc Ngoại dặn mỗi cấp mới chỉ "chạm thử thứ vừa mở một lần" (muối 1 khạp, phơi 1 mẻ, đan 1 giỏ). Mở thứ mới thì có **một** đơn "Món mới" (danh sách `LEAD`), sau đó đơn thường chọn ngẫu nhiên trong những món đã từng làm (85%). Không có nhịp "làm → có người đặt → bán được giá → mở cái tiếp theo".

**Đề xuất khung 3 bước cho mỗi thứ mới, áp từ cấp 7 trở đi:**
1. **Làm lần đầu** (việc Ngoại dặn, như hiện nay).
2. **Có người đặt:** ngay khi làm xong lần đầu, hàng xóm hay ghe đặt đúng món đó, số lượng bằng 2 mẻ, trả ×1,5. Hiện mới có 1 đơn kiểu này, đề xuất thành 2 đơn liên tiếp.
3. **Nối sang thứ kế:** đơn thứ hai đòi kèm **một món của thứ sắp mở** mà hiện đã làm được bằng cách khác, để người chơi thấy lý do mở thứ đó. Ví dụ: đơn ghe cấp 10 đặt "3 ổi + 2 mẻ ớt khô"; cấp 11 ghe đặt "xoài sấy" khi vừa trồng xoài, kéo sang lò sấy.

Việc hôm nay (5 việc) ưu tiên thứ vừa mở trong 3 ngày đầu, sau đó mới quay về việc chung. Em làm bảng chi tiết 20 cấp sau khi anh duyệt hướng này.

## 4. Đồ muối lâu có đáng công không, đơn dưa cải có nhiều quá không

**Số trong code:**
| Món | Nguyên liệu (giá bán thô) | Ra | Chờ | Lời so với bán thô |
|---|---|---|---|---|
| Dưa cải muối | 4 cải (40 xu) + muối (2) | 1 hũ **65 xu** | 12 tiếng, 1 trong 2 khạp | **+23 xu** (+55%) |
| Hột vịt muối | 4 trứng vịt (120 xu) + muối (2) | 4 hột **168 xu** | 24 tiếng | +46 xu (+38%) |
| Ớt khô (so sánh) | 4 nắm ớt (64 xu) | 1 bịch **90 xu** | 4 tiếng nắng, 1 trong 4 nong | +26 xu (+40%) |

Khạp chiếm chỗ 12–24 tiếng mà chỉ lời thêm 23–46 xu: **đúng là payoff thấp**, nhất là khi cải chỉ cần 30 phút một vụ. Đơn đặt dưa cải trả ×1,3 (85 xu), ghe ×1,6 (104 xu) thì mới đáng.

**Đơn dưa cải hay gặp không phải lỗi**, do ba chỗ cộng lại: (1) có đơn "Món mới" dưa cải ở cấp 8; (2) đơn thường chọn 85% trong món đã làm, lúc cấp 8–9 món đã làm còn ít nên dưa cải lặp; (3) không có luật "món đang có trong đơn khác thì không đặt nữa".

**Đề xuất:**
- **Giữ giá, tăng số lượng mỗi mẻ** (theo ý anh, để có nhiều món giao cho nhiều người): một khạp 4 cải ra **2 hũ** dưa (130 xu, lời +88); khạp hột vịt ngâm **6 trứng ra 6 hột** (252 xu, lời +70, mẻ to hơn trong cùng 24 tiếng). Giá từng món giữ nguyên nên đơn hàng xóm, ghe không đổi.
- Đơn: món đang nằm trong một đơn mở thì không chọn lại; mỗi món tối đa 1 đơn mở.
- Sau khi đổi giá, chạy lại bot 30 ngày để xem xu dư có tăng quá không (hiện ngày 30 dư ~90.000 xu, phần C "chỗ tiêu xu" sẽ gánh).

## 5. Năm câu hỏi thêm (3/11, tối)

**Ớt phơi nong rồi bỏ lò sấy?** Không có đường này trong code. Nong phơi làm ớt khô, chuối phơi, khô cá sặc, lục bình khô. Lò sấy chỉ nhận trái cây tươi và đường: mứt khế, xoài sấy, cơm dừa, mứt dừa. Việc "Phơi 10 mẻ" ở cấp 13 cộng cả nong lẫn lò, chỉ là đếm số mẻ. Nếu anh thấy chỗ nào cho bỏ ớt khô vô lò thì gửi hình.

**Nong phơi có khác giữa giờ thật và giờ game?** Có, và có một lỗi. Nong chỉ khô khi "có nắng" 6h–18h theo đồng hồ đang chọn: giờ thật thì phơi được 12 tiếng mỗi ngày thật; giờ game (1 ngày = 40 phút) thì khô 27 phút rồi nghỉ 13 phút, tính ra nhanh hơn giờ thật về đêm; **giờ cố định mà chọn giờ tối thì nong không bao giờ khô**. Đã vá trong v107: giờ cố định coi như luôn có nắng. Thời lượng phơi (ớt 4 tiếng, chuối 8, cá 6, lục bình 3) tính bằng giờ thật trong lúc có nắng, nên về đêm giờ thật thì chuối 8 tiếng có thể mất tới một ngày rưỡi.

**Luân canh có được nói ở đâu không?** Gần như không. Chỉ có một câu Ngoại nói mỗi ngày một lần khi hái lại cùng thứ trên cùng liếp, và dòng mô tả hố ủ. Người chơi không thấy mình mất gì. v107 đã thêm: chữ bay "Đất mệt · hụt N bó" khi hái, Ngoại giải thích một lần, và **vòng gieo gắn nhãn "đất mệt" lên thứ vừa trồng ở liếp đó** kèm dòng "gieo thứ khác cho đất nghỉ".

**Nong phơi lâu ngang muối dưa?** Nong 3–8 tiếng nắng, khạp 12–24 tiếng; nhưng nong có 4 chỗ, khạp 2, và nong nghỉ ban đêm. Lời thêm: ớt khô +26 xu, chuối phơi +40, dưa cải +23 (trước), hột vịt +46. Sau khi tăng số lượng mỗi mẻ (2 hũ dưa, 6 hột vịt) thì khạp lời +88 và +70 mỗi mẻ, xứng với thời gian chờ hơn.

**Chơi trên hai máy có sync tốt không?** Cơ chế: lưu lên mạng mỗi 15 giây khi có thay đổi và khi ẩn tab; mỗi bản lưu có số thứ tự; máy nào lưu bản cũ hơn thì máy chủ từ chối, máy đó ngưng lưu và Ngoại nhắc "Vô Cài đặt, bấm Tải bản mới nhất". Máy thứ hai nhập mã vườn trong Cài đặt là lấy được vườn. **Điểm yếu:** mở máy A sau khi đã chơi trên máy B, A không tự kiểm tra mà chơi tiếp bản cũ, chỉ sau 4 giây khi cố lưu mới báo, và người chơi phải tự bấm "Tải bản mới nhất"; làm gì trên A trước lúc tải về là mất. Đề xuất v108: lúc mở game hỏi máy chủ số thứ tự trước, bản trên mạng mới hơn thì tự tải về rồi mới vào vườn (màn tải ghi "Đang lấy vườn từ máy kia…").

**Gác bếp 20 chỗ không mở rộng được?** Đúng, trước giờ là số cố định. v107: củi, lục bình, giỏ không chiếm chỗ gác bếp nữa, và thêm nút "Thêm kệ gác bếp" trong Sổ › Kho: 150, 250, 350 xu cho ba kệ, mỗi kệ thêm 10 chỗ (tối đa 50). Đây cũng là một chỗ tiêu xu.

## Thứ tự em đề xuất làm
1. Giá dưa cải, hột vịt và luật không lặp đơn (nhỏ, vào v107 luôn).
2. Bảng "Đất trống" với lưới 2×2 (vào v107).
3. Khoá khu đất theo khu trước (v107, có di trú người chơi cũ).
4. Chuỗi nhiệm vụ 3 bước: làm bảng 20 cấp gửi anh duyệt, rồi v108.
