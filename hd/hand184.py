# -*- coding: utf-8 -*-
# Ghi v184 (giàn sai trái hơn) + ý đình làng vô HANDOFF.md
import io
p = '/Users/macintoshhd/Documents/fungiistudio/hd/HANDOFF.md'
s = io.open(p, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khop %d lan, can %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

rep("Bản mới nhất là **v183, đã dựng, CHƯA ĐẨY** (`live/v182.html` → `fix183.py` → `live/v183.html`).",
    "Bản mới nhất là **v184, đã dựng, CHƯA ĐẨY** (`live/v182.html` → `fix183.py` → `live/v183.html` → `fix184.py` → `live/v184.html`).")

rep("| Việc kế tiếp | **Đẩy v183** khi anh Ares nhắn. Rồi **tác dụng cho tre trăm đốt** — cây duy nhất lớn rồi mà không cho gì (xem mục v183); đụng tới xu nên chờ anh chốt số. Rồi",
    "| Việc kế tiếp | **Đẩy v183 + v184** khi anh Ares nhắn (hai bản đi chung một lần cho gọn). Rồi **chốt hướng cây cổ tích ở đình làng** — ý của người chơi, anh Ares thấy hay, em đã đề xuất ba hướng (xem mục dưới), chờ anh chọn. Rồi")

a = "\n## v183 (24/11/2026) — Sổ cổ tích nói rõ mỗi cây cho gì"
assert s.count(a) == 1

them = u"""
## Ý đang chờ anh chốt (24/11/2026) — cây cổ tích ở đình làng

Người chơi đề nghị: **đem bộ cây cổ tích vô đình làng, dùng chung cho các nhà.** Anh Ares: "t thấy ý này cũng hay. M thấy có thể phát triển thế nào".

Ý này rơi đúng một ô đã duyệt: `ke-hoach-cap-21-30.md` ghi **cấp 26 — Đình làng mở, trụ 2, "Ý đã duyệt, chưa thiết kế"**, nằm trong đợt C (đợt duy nhất phải thiết kế từ đầu, nên để sau cùng). Đình làng từ đầu tới giờ thiếu đúng một thứ: lý do để tới. Kỳ Yên một năm một lần, 364 ngày kia nó là sân trống. Bộ cây cổ tích giải đúng cái đó, mà giải bằng thứ đã làm xong (sáu mô hình, sáu truyện, sáu tác dụng đều có trong code).

**Nhưng "đem sáu cây ra đình, dùng chung" theo nghĩa thẳng thì vỡ ba chỗ:**

| Vỡ ở đâu | Vì sao |
|---|---|
| Mất sợi dây 20 cấp | Cây mọc ở vườn mình từ cấp 6 tới cấp 20, mỗi cây ba lần chạm mới nghe hết truyện. Sân chung thì người cấp 6 thấy sáu cây đã lớn hết — hết quà, lộ truyện. Trái luật "chỉ hiện cái làm được ở cấp hiện tại" |
| Tác dụng không chia được | Vú sữa 2 trái/ngày, trầu cau 3 miếng/ngày, khế vàng 1 cục vàng/tuần. Ai cũng lãnh đủ thì thành xu trời cho; chia hay ai tới trước lãnh trước thì thành cuộc đua — đua là phạt người vô trễ |
| Sọ Dừa không làm được từ xa | `sdHelp()` lăn ra tưới **một liếp khô trong vườn mình**. Đứng ngoài đình thì không tưới được gì |

Thêm nữa: đã có người chơi thật nuôi cây rồi, dời đi là lấy lại thứ họ đã công nuôi.

**Ba hướng đã đề xuất (em nghiêng về hướng 1 + cây đa của hướng 2):**

1. **Cây vẫn ở vườn mình, đình làng là chỗ góp.** Cây của ai người đó nuôi, không đổi một chữ. Cây **lớn hẳn** rồi thì chiết được một nhánh đem ra đình. Sân đình có sáu chỗ trống, nhánh ai góp thì cây đó mọc lên, dưới gốc có bảng gỗ nhỏ: *"Vú sữa — vườn của Út Lan, góp ngày 3 tháng 11"*. Sân đầy dần bằng cây của cả xóm. **Sân đình không trả xu, nó quyết Lễ Kỳ Yên to cỡ nào** (Kỳ Yên đã nằm sẵn ở cấp 27): hai cây thì hội nhỏ, đủ sáu cây thì đèn treo kín sân, ghe về đông, hát bội dài hơn. Không cày được, không đua được, không ai vô trễ mà thiệt, **và không cần chốt một con số kinh tế nào**.
2. **Đình làng có cây riêng của nó.** Giữ sáu cây cổ tích y nguyên trong vườn; sân đình trồng **cây đa** — cây thiệt của một cái đình miền Tây. Ai cũng thấy chung một cây, tới buộc sợi chỉ đỏ gởi điều mong, đọc được điều người khác gởi. Chung ở chỗ *cùng nhìn*, không chung ở chỗ *cùng ăn*.
3. **Sáu cây rời vườn hẳn** — em không khuyên: mất sợi dây 20 cấp, lộ truyện, Sọ Dừa chết, và lấy lại cây của người đã nuôi.

Hướng 1 và 2 không chống nhau: cây đa giữa sân, sáu chỗ góp vòng quanh.

**Phần máy chủ không đáng lo:** Bến bà con đã bày đồ cho người khác mua được (`mv2_ben_put/buy/collect/list`), ghé vườn được (`mv2_peek`), hàng xóm hái giùm được (`mv2_act`). Góp một nhánh chỉ là thêm một bảng ghi *vườn nào, cây gì, ngày nào* — không có gì phải tranh nhau sửa.

**Làm lúc nào:** em đề nghị chưa. Kế hoạch để đình làng ở đợt C cuối cùng, lý do đã viết sẵn trong đó: *"lúc đó cũng đã có người chơi thật tới cấp 26 để hỏi ý."* Giờ ghi hướng là đúng lúc; dựng thì còn ba trụ trước nó. **Chưa ghi vô `ke-hoach-cap-21-30.md` vì anh chưa chọn hướng.**

## v184 (24/11/2026) — tre trăm đốt: giàn sai trái hơn

**BẢN NHÁP — đã dựng, CHƯA ĐẨY.** `fix184.py`, v183 → v184. Anh Ares chọn **"Giàn sai trái hơn"** trong hai hướng của mục v183.

Tre trăm đốt là cây duy nhất lớn rồi mà không cho gì (chỉ có màn phép `ttMagic()` Khắc xuất / Khắc nhập cho vui). Giờ **lớn hẳn rồi thì giàn trong vườn mỗi đợt hái thêm một trái** — khổ qua, bầu, mướp. Đúng y điều kiện mở cây ("thu đủ ba vụ khổ qua trên giàn"), **không cần món mới trong kho, không cần hình mới**.

Sáu chỗ sửa, tất cả trong `fix184.py`:

1. `function ttUp()` — tre trăm đốt lớn hẳn chưa: `F.st >= 3 && F.told >= 3 && !VISIT`. Phải **nghe hết ba đoạn truyện** mới có, không chỉ cây mọc xong. Khai bằng `function` (không `const`) để `yS` gọi được từ chỗ khai sớm hơn trong mã.
2. `function ttGi(c)` — `c.kind === 'trellis' && ttUp() ? 1 : 0`.
3. `harvestN(p)` cộng `ttGi(c)` vào **sau** khi làm tròn, nên là đúng một trái, không nhân theo đất. Cộng trong `harvestN` chứ không ở chỗ gọi, để **ô xem trước, chỗ đo kho còn chỗ và số hái thật đều khớp** (nếu chỉ sửa chỗ gọi thì phép đo kho lệch một món).
4. Hái giàn thì nổi chữ `Tre trăm đốt · thêm 1 trái` sau 700ms (bắt `PV[id]`, `c.h` trước, vì liếp bị xoá sau đợt cuối).
5. `yS(c)` — thẻ số trong Sổ giống: `2×3` → `3×3`.
6. Sổ giống thêm câu *"Tre trăm đốt khắc nhập cho thêm một trái mỗi đợt."*, chỉ hiện khi cây đã lớn.
7. Sổ cổ tích: lời tre trăm đốt nói thêm *"Giàn trong vườn nhờ vậy mà mỗi đợt hái thêm được một trái."* (cả tiếng Anh).

**Đo thật trong trình duyệt** (`lp/mv2_t184.html`, đặt `ST.ft.tretramdot` ba mức):

| | chưa mọc (st 0) | mọc rồi chưa nghe hết (st 3, told 1) | lớn hẳn (st 3, told 3) |
|---|---|---|---|
| `ttUp()` | false | false | **true** |
| Khổ qua | 2 | 2 | **3** |
| Bầu | 2 | 2 | **3** |
| Mướp | 3 | 3 | **4** |
| Cải (không phải giàn) | 3 | 3 | 3 |
| Thẻ Sổ giống | 2×3 | 2×3 | **3×3** |

Hái thiệt một liếp giàn khổ qua: `act.harvest()` ra `true`, vô kho **3 trái**, chữ `Tre trăm đốt · thêm 1 trái` nổi lên đúng. Sổ giống lúc chưa lớn **không** có câu thêm (không lộ trước); lúc lớn thì có. Tiếng Anh ra đúng câu.

**Cổng:** `node --check` sạch · `uiluat.py` → `LECH LUAT 0 {}` · uicheck `khac nhau 0 loi trang 0` ở 390×844, 360×740, 1280×800 · `tCay176.js` **ĐẠT HẾT 13/13**. Lỗi console chỉ có hai thứ vô hại của bàn thử: `ERR_UNSAFE_PORT` (trang thử trỏ Supabase vô cổng 9) và `navigator.vibrate` bị chặn vì chưa có ngón tay chạm. Thêm 13 dòng so với v183. **Chưa thử iPhone thật.**

**Xu:** khổ qua 26 xu × 3 đợt = 78 xu thêm cho một vụ đầy (vụ chừng 7 tiếng). Không đổi số nào khác.
"""
s = s.replace(a, them + a, 1)

io.open(p, 'w', encoding='utf-8').write(s)
print('xong ghi v184 + y dinh lang')
