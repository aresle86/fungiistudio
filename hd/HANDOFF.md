# Miệt Vườn 2.0 · Hồ sơ bàn giao cho Claude Code (4/11/2026, live v110e)

Hồ sơ này gom mọi thứ để làm tiếp game trong Claude Code. Đọc mục 1–4 trước khi sửa gì.
Nói chuyện với anh Ares bằng tiếng Việt. Mọi chữ trong game là tiếng Việt, giọng miền Tây.

---

## 1. Trạng thái hiện tại

| Thứ | Ở đâu / trạng thái |
|---|---|
| Bản live | **v113t**, https://fungiistudio.com/mietvuon2. Commit trên `main` và `mietvuon2-online` (repo `aresle86/fungiistudio`), xem `git log main -1` |
| Nguồn game | `hd/live/vuon3d.html` trên nhánh **`mietvuon2-dev`** (= v110, khớp live). Dựng: `v107b` → `ui108.py` → `v108a` → `fix109.py` → `v109a` → `net110.py`, `ho110.py`, `cel110.py`, `odd110.py` → `v110a` (BUILD `v110a`; khi ship đổi thành `v110`) |
| Việc kế tiếp | **Làm lại HUD theo bộ khung chung** (ref 2 bảng gỗ + ghim giấy, ref 3 icon nhiều chữ ít): hướng đi trong `hd/hud-huongdi.md`, hình hiện trạng `hud/tongquan_*.png`. Đã qua 4 vòng mock (`hd/tKhung.js` dựng ngay trên khung gỗ cũ của game, chụp `hd/mock/khung2_*.png`); anh chê mock 1 (khung gỗ mới) và mock 2–3 (menu đóng khung, bo góc lệch, inset gây lé, vòng tròn, chữ tối đổ bóng). **Hệ thống thành phần** `hd/hud-hethong.md` (4 loại nút, 1 loại thanh 2 cỡ, 1 badge, bo góc 16/10/6, luật bóng chữ, menu giữ kiểu cũ) đang chờ anh chốt rồi mới áp vào game. Tab Sổ bản `tabso.css` **không duyệt** (anh chê, quá giống web), bỏ |
| Artifact game | https://claude.ai/artifact/DkesRLV6eCUtN56HxQnwiT (v105) |
| File trong Project "Farming game" | `claude/mietvuon/miet-vuon-2.0.html` (v105) |
| Kịch bản toàn cảnh + changelog từng bản (Claude Doc) | https://claude.ai/artifact/5zrepCFVxTCYk3zmhfgAuU |
| Rà nhiệm vụ theo cấp v101: quyết định, kết quả bot (Claude Doc) | https://claude.ai/artifact/7dy5ceisV6jpudW7E4KFsm |
| Bàn giao QC cũ (v83, v84–v91) | Project: `claude/mietvuon/qc-ban-giao.md`, `qc-v84-v90-ban-giao.md`. Lỗi còn mở ở mục 4 của file v84–v90 vẫn đúng phần lớn |
| Lời Ngoại | Project: `claude/mietvuon/loi-thoai-ngoai.md` |

**Luôn bắt đầu bằng:** `git fetch`, so `hd/live/vuon3d.html` với live (`mietvuon2/index.html` trên `main`). Nếu live đi trước thì lấy nguồn từ live (cách cắt ở mục 3.4) rồi mới vá.

---

## 2. Game là gì

- Game làm vườn low-poly three.js (0.169 qua CDN), bối cảnh miền Tây. **Một file HTML duy nhất** (~1,2 MB, nhiều dòng rất dài), không có bước build.
- Chơi theo giờ thật: một ngày trong game = 40 phút ngoài đời. Lưu `localStorage` key `mv2-state`. Đồng bộ mây qua Supabase (mã vườn + mã bí mật, ẩn danh).
- Nhân vật dẫn dắt là **Ngoại**. Ngoại chỉ hiện chữ trong bong bóng, không có giọng. Người chơi xưng "con", có avatar (6 dáng) và tên vườn.
- 20 cấp. Mỗi cấp mở một thứ chính. Việc Ngoại dặn (QUEST) là chỗ **duy nhất** giới thiệu thứ mới, nên mỗi việc phải dạy đúng thứ vừa mở.

### 2.1 Bảng cấp (v102 trở đi)

Kinh nghiệm để lên cấp (XPN): 2: 10 · 3: 30 · 4: 80 · 5: 190 · 6: 310 · 7: 800 · 8: 1.800 · 9: 3.000 · 10: 4.300 · 11: 5.800 · 12: 7.500 · 13: 9.300 · 14: 11.200 · 15: 13.300 · 16: 15.500 · 17: 18.000 · 18: 20.500 · 19: 23.500 · 20: 26.500.

Mục tiêu nhịp (người chơi chăm, 3 lần/ngày): cấp 8 ngày 5, cấp 12 ngày 14, cấp 16 ngày 25, cấp 20 ngày 40.

| Cấp | Mở ra (LVFEAT) | Rau mới | Việc Ngoại dặn để lên cấp này |
|---|---|---|---|
| 1 | Gieo, tưới, hái, bán, phủ rơm | cải, hành | – |
| 2 | Việc lặt vặt | rau muống | – |
| 3 | Đơn nhà bên, bắt sâu, ghé vườn bạn | ớt | Phát 14 bụi cỏ mé mương |
| 4 | Bếp Ngoại, nhặt củi, góc vườn mới | bắp | Đắp đủ 8 liếp + giao 1 đơn |
| 5 | Mua gà, ấp trứng | cà chua | Góp 120 xu dọn góc vườn (mở không cần tải lại) |
| 6 | Chuồng vịt, cây cổ tích vú sữa | khổ qua | Ấp nở 1 con gà |
| 7 | Nong phơi, bãi hông nhà | mồng tơi, đậu bắp | Dựng chuồng vịt + lượm 2 trứng vịt |
| 8 | Khạp muối, cây trái đầu (chuối), bướm | chuối | Đắp 2 liếp bãi hông nhà + phơi 1 mẻ |
| 9 | Câu cá, mé sông, khạp nuôi cá | ổi | Muối 1 khạp + trồng 1 gốc chuối |
| 10 | Ghe chợ nổi (ghe bẹo) | khế | Khai hoang 2 ô mé sông + câu 1 con cá |
| 11 | Lò sấy, sau nhà 10 ô | xoài | Giao 1 đơn ghe + 8 đơn nhà bên |
| 12 | Hố ủ phân, món Tết | dừa | Góp 250 xu dọn tre gai sau nhà |
| 13 | Trang trí vườn, giàn nong hai tầng, thêm khạp | – | Bón 1 liếp + phơi/sấy 10 mẻ |
| 14 | Lò ấp vịt | – | Mua 1 món trang trí + nâng nong hay khạp |
| 15 | Giỏ lục bình, mái lá mới | – | Góp 400 xu lợp mái (~10 tiếng, bạn ghé phụ) |
| 16 | Đào ao cá (2×2 ô) | – | Đan 2 giỏ + nấu 8 nồi món cá |
| 17 | Nuôi ong, món mật ong | – | Đào ao cá + hái 5 vụ cây trái |
| 18 | Sửa sang nhà cửa | – | Góp 600 xu sửa nhà (~8 tiếng) |
| 19 | Ghe tam bản đặt lờ | – | Câu đủ 15 loài cá |
| 20 | Một năm ở vườn Ngoại (tổng kết) | – | Lấy lờ ghe tam bản 1 lần |

Người chơi cũ giữ đồ đã có dù cấp mở bị dời (`ST.keep`, di trú `ST.k102`).

**Cây cổ tích** (đặc sản của game, mỗi cây là một sự kiện lạ): vú sữa (6), tre trăm đốt (9), trầu cau (12), dưa hấu Mai An Tiêm (14), khế vàng (16), Sọ Dừa (18). Đốm sáng → chạm → lớn theo giờ thật → Ngoại kể từng đoạn → Sổ cổ tích. Chiếm 2×2 ô khi dời vào đất.

### 2.2 Các hệ đã có
Việc hôm nay (5 việc, bấm nhận thưởng), đơn nhà bên, ghe bẹo, bếp củi, nong, khạp, lò sấy, hố ủ, lò ấp vịt, giỏ lục bình, ong, ao cá, ghe tam bản, câu cá (mồi, giờ, con nước, trăng, hội câu tuần), Sổ cá/bướm/cổ tích, ghé vườn bạn (tưới giùm, hái ké, tặng hạt, để quà, phụ xây), thẻ về vườn 7 ngày, mùa Tết theo lịch thật, mùa nước nổi, khai hoang đất (tiền + công + phơi ải), trang trí (rào, chuồng, đồ kiểng), lợp mái, sửa nhà, âm thanh tạo bằng code.

### 2.3 Quyết định gần đây (v102–v105, đã lên live)
- **v102:** bảng cấp 20 cấp như trên; góc vườn mở không tải lại trang (`expOn()`); sửa bộ đếm hái cây trái (lỗi chặn cấp 16–17 và khế vàng, Sọ Dừa); đơn cá tối đa 1 đơn, ≤2 con; trái cây trong đơn ≤60% sản lượng; ghe không đòi món chưa nấu được; đốm sáng cổ tích có lời dẫn + thanh chờ; thau nước cho vịt thay cầu ván.
- **v103:** việc hôm nay theo công sức. 1 việc mới nhất + 2 việc của đồ đã có + 2 việc cơ bản; từ cấp 12: 3 + 1. Số lượng theo cỡ vườn. Thưởng xu tăng theo cấp (trần ×2,5). Một số thưởng bằng đồ (củi, muối, rơm). **Anh bác bỏ giá đồ kiểng tăng 30% mỗi món mua thêm**: giá cố định.
- **v104:** đơn phân vai. Hàng xóm đặt đồ tươi, món nấu. Ghe đặt trái cây, đồ khô, đồ muối, mứt, giỏ, mật. Đơn "Món mới" khi vừa mở món (trả ×1,5). Ghe chờ **6 tiếng** từ lúc thấy, giao từng phần được, hết giờ trả tiền phần đã giao.
- **v105:** âm thanh. Mặc định Nhạc đàn 35%, Tiếng vườn 60%, Hiệu ứng 100% (3 thanh trong Cài đặt). Nền vườn theo giờ, gió **từng cơn** (anh chê gió đều quá). **Không hạ nhạc khi Ngoại nói** vì Ngoại chỉ hiện chữ.

---

## 3. Cách làm việc (bắt buộc)

### 3.1 Quy trình với anh Ares
1. **Đề xuất trước khi làm việc lớn.** Anh muốn được nghe đề xuất từ góc nhìn người làm game có kinh nghiệm, rồi mới chốt.
2. **Thiết kế mới, mô hình mới: gửi hình cho anh duyệt trước khi gắn vào game.** Tự xem hình trước khi gửi.
3. Test kỹ trước khi gửi. Mỗi đợt: **QC → deploy → changelog.** Anh nói "ok / ship luôn" và không có lỗi thì đẩy live luôn.
4. Việc tạo hình/video AI: **chỉ viết prompt**, không chạy Higgsfield.

### 3.2 Luật thiết kế
- **Chỉ hiện cái làm được ở cấp hiện tại.** Thứ chưa tới cấp thì ẩn hẳn, không tô xám kèm "Cấp N". **Không bao giờ nói số cấp tương lai** trong chữ khoá ("mai mốt", "chăm vườn thêm ít bữa nữa").
- **Chỉ ẩn vì chưa tới cấp (hoặc chưa tới mùa), không ẩn vì thiếu xu.** Thiếu xu thì nút tắt kèm "còn thiếu N xu".
- Lỗi, giới hạn, xác nhận hiện bằng **toast**. Ngoại không tự nói khi đang mở bảng, Sổ, thẻ hay vòng chọn.
- Chữ **tích cực**, đúng giọng miền Tây. Không chữ tắt. Cái gì icon đã nói thì không thêm chữ giải thích.
- **Cây không bao giờ chết vì người chơi vắng.** Không bán "xây nhanh" bằng xu. Xây lớn có thời gian chờ, bạn ghé phụ thì mau hơn.
- **Không âm bass nặng.** Mọi âm thanh tạo bằng code (WebAudio), không dùng file thu.
- Mọi thứ thêm vào phải liên quan miền Tây hay Việt Nam. Thứ không liên quan thì báo anh trước.
- Đất mới luôn có mương giữa các hàng liếp. Đồ đặt trên ô nằm trên cỏ xanh, không trên đất nâu trơ.
- Thứ mới phải dễ khám phá: việc hôm nay kéo người chơi vào thứ vừa mở; nâng cấp phải thấy khác bằng mắt.
- Trên điện thoại: nút menu xếp dọc mép phải; icon không quá to.

### 3.3 Luật mô hình 3D
- Low-poly, cùng độ chi tiết với mô hình cũ. Một khối chính nghiêng 3/4, ít mặt lớn màu phẳng. Các phần chồng lên nhau, không xuyên nhau. Phần thu hoạch (trái, lá) phóng to và lộ ra. Tán cây là các chùm lá rời, thân có nhánh. Mái lá, bông phủ kín, mượt.
- **Mô hình mới phải qua 3 bước trước khi gửi anh:** (1) chụp nhiều góc, kể cả cận hai đầu và nhìn từ trên xuống; (2) chiếu tia tìm chỗ thấy xuyên ra nước hay nền; (3) dò đỉnh tìm chi tiết lòi ra ngoài vỏ hay xuyên đáy. Mẫu: `hd/tGhe3.js`.
- Thêm vật có gọi `R()` thì giữ chuỗi ngẫu nhiên: `{ const sd0 = sd; …; sd = sd0; }`. Nếu không, mọi cỏ, bụi dựng sau sẽ xê dịch.

### 3.4 Luật code
- **Vá bằng script Python có kiểm tra**: mỗi chuỗi cần thay phải khớp đúng số lần mong đợi (hàm `rep(a, b, n=1)` assert). Không sửa tay trên dòng dài. Xem các file `hd/*fix*.py`, `hd/ui106.py`.
- Không viết chú thích `//` giữa dòng dài; dùng `/* */`. (Đã mất code vì nối dòng.)
- `Date.now()` là mili-giây, bảng thời lượng trong code là giây. So sánh phải ×1000.
- Dữ liệu từ người khác (tên vườn, payload hàng xóm) luôn thoát ký tự.
- Vật sinh/xoá liên tục phải dispose geometry, material riêng. Material từ `mat()` dùng chung, không dispose.
- Bảng vẽ lại định kỳ giữ trạng thái `details` và cuộn (`sheetSoft()`).
- Chức năng thử nghiệm chỉ hiện khi URL có `?dev`.
- Code trong module chạy xen `await LDY()` (nhường máy cho màn load). Hàm gọi sớm trong lúc tải có thể chạm biến chưa khai báo (TDZ). Bọc try như `avHud` ở v106a.
- Mỗi lần deploy đổi `const BUILD = 'vNNN'` (tab mở lâu sẽ thấy nút tải bản mới).

### 3.5 Deploy
1. `cp hd/live/vuon3d.html` thành bản mới, chạy `cd hd && python3 buildsite.py`. Script đọc `live/vuon3d.html`, ghi `mietvuon2/index.html` (bản trên nhánh này ghi thẳng vào `../mietvuon2/` cạnh thư mục `hd/`).
2. `git fetch` và chắc `HEAD..origin/main` trống. Commit `mietvuon2/index.html` lên `main`, push `main` và `main:mietvuon2-online`.
3. Cập nhật Artifact game (cùng URL) và file `claude/mietvuon/miet-vuon-2.0.html` trong Project.
4. Thêm một dòng changelog vào cuối danh sách trong Doc kịch bản (5zrepCFVxTCYk3zmhfgAuU), cùng giọng các dòng trước.

**Lấy nguồn từ live:** `mietvuon2/index.html` = phần `head` trong `buildsite.py` + nguồn (tiêu đề thêm " · Fungii") + `\n</body></html>\n`. Cắt ngược là ra nguồn; dựng lại phải ra y hệt.

---

## 4. Bộ test (thư mục `hd/`)

```bash
cd hd/lp && npm i                     # three@0.169 + font Paytone One offline
(cd hd/lp && python3 -m http.server 8777)   # chạy nền suốt lúc test
cd hd && python3 gen_test.py x40f.js live/vuon3d.html          # → lp/mv2_test.html
python3 gen_test2.py x40f.js live/v106a.html lp/mv2_t106.html  # bản thử riêng, không đụng bản regression
```

- `x40f.js` gắn hook vào module: `__g` (ST, act, sim, openSheet…), `__x`, `__e`, `__w`, `__G`, `__T`, `__P`, `__L`… `window.__stop = true` để dừng vòng lặp.
- **Kiểm cú pháp sau mỗi lần vá:** tách `<script type="module">` dài nhất ra `.mjs`, bỏ dòng import `mergeGeometries`, chạy `node --check`.
- **Regression chuẩn:** `tNav qcRepro tFan tFishUX2 tBld tSay tMai tNha tTB tFeat` + `qcLv.js` (đi cấp 1→20, mở mọi bảng; mong đợi `DONE 0 levels with err; 0 bad text; 1 console errs`, lỗi console còn lại là mạng Supabase bị chặn).
- Test theo bản: `tExp.js`, `tMig.js`, `tFt102.js`, `tTask103.js`, `tGhe104.js`, `tAud105.js`, `tA106.js` (chụp hình phần A, desktop 1280×800 + điện thoại 390×664).
- **Bot chơi tự động** đo nhịp lên cấp: `cat x40f.js botx.js > xbot.js`, chạy `tBot.js`. Bot ghé 3 lần/ngày, gọi tay các tick chỉ chạy khi vẽ (penTick, bldTick, maiTick, nhaTick, tbTick, ftTick, ongTick). Kết quả v102: cấp 8 ngày 3,8 · 10 ngày 7,3 · 12 ngày 10,8 · 14 ngày 14,3 · 16 ngày 19,8. Bot kẹt ở ao vì không còn 2×2 ô trống. Xu dư khoảng 90k ở ngày 30 (cần chỗ tiêu xu, mục 6.3).
- Save test phải có `plots:{}`, `v:1` (thiếu `plots` là game tạo vườn mới).
- Lưu ý môi trường: Playwright launch với `--use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`; `waitForFunction(fn, null, {timeout})`; chụp hình hay treo khi chạy song song nhiều test (tăng timeout lên 180 s). Không chạy hai regression cùng lúc. Server `http.server` nền có thể bị tắt sau ~2 tiếng.

---

## 5. Bản đồ code (tìm theo tên)

| Chủ đề | Tên trong code |
|---|---|
| Trạng thái, lưu | `ST`, `NEWST()`, `save()`, `store`, key `mv2-state` |
| Cấp, kinh nghiệm | `XPN`, `UNLOCK`, `LVFEAT`, `LVINTRO`, `QUEST`, `doQuest`, `gainXP`, `levelUp`, `lvCelebrate` |
| Việc hôm nay | `ensureTasks`, `featTasks`, `bump(t)`, `tkClaim`, `TASKIC`, `taskGo` |
| Đơn hàng | `ORD`, `ordMake(kind)`, `LEAD`, `leadMake`, `ordHTML`; ghe: `GHE`, `GHEK`, `GHEH`, `gheSim`, `gheGive`, `gheLeave`, `gheTick`, `gheHTML` |
| Bảng (sheet) | `openSheet(kind, arg)`, `renderSheet()`, `SHEET.tab`, `SHEET.sub`; Chợ là kind `cho` |
| Sổ | `BTAB`, `tabOn`, `openBook(tab)`, `renderBook()`, `pgGiong/pgKho/pgCa/pgBuom/pgCotich/pgViec` |
| Đất, bãi | `PLOTS`, `PL`, `PV`, `BAI/SONG/SAU`, `landSt`, `landWork`, `suaHTML`, `baiSan`, `placeObj`, `objAt`, `OBJD` |
| Đồ 2×2 | `BIGD`, `bigPlace`, `bigHTML`, `block4` |
| Trang trí | `DC`, `DCK`, `dcHTML`, `dcPlace`, `decoAt` |
| Chế độ đặt đồ | `SUA` (`{ move }`), `suaOn(on, move)`, `#suaBar` |
| Cây cổ tích | `FT`, `FTK`, `ftTap`, `ftTell`, `FTV` |
| Âm thanh | `VOL()`, `bus`, `aud(k)`, `AUDF`, `AMBS`, `ambTick`, `pluck`, `sfx` |
| Góc vườn mới | `EXP`, `expOn()`, `EXPG/EXPN` |
| Thời gian | `DAYM = 40`, `hourAt`, `sim(dt)`, `ST.spd` |

---

## 6. Việc tiếp theo (đã chốt, theo thứ tự)

### 6.1 v106 phần A: sắp lại giao diện (anh đã duyệt hướng, chờ duyệt hình)
Đã làm trong `hd/ui106.py` → `hd/live/v106a.html`, cú pháp qua. `tA106.js` đã chạy tới bước Chợ trên desktop: Sổ 3 tab, chip, nhớ chip, dời cây từ Sổ, thanh đặt + Hủy, tab Tiệm đều đúng, không lỗi trang (hình mẫu: `hd/shots/a106_*.png`). **3/11: `tA106.js` chạy hết, desktop + điện thoại, không lỗi trang.** Lỗi test cũ là `ev` làm rơi tham số (không phải `PV`); thêm chặn mạng ngoài, tắt thẻ "Về vườn ngày" trong save, chờ camera dừng. Trang test phải dựng bằng `cat x40f.js x106.js` (hook `__U` nằm trong `x106.js`). **Còn phải:** gửi hình anh duyệt, rồi regression + ship (BUILD đang là `v106a`, đổi thành `v106`).
- **Sửa thêm (3/11): popup không chồng nhau.** Luật CSS cuối khối CSS của `ui106.py`: thanh Đặt đồ, thẻ Về vườn, màn lên cấp hiện thì thẻ Ngoại nhờ (và Ngoại khi lên cấp) nhường chỗ; toast lên trên khi mở bảng, xuống đáy khi mở Sổ; thanh Đặt đồ trên máy tính nằm giữa trên. Kiểm bằng `tPop.js` (22 cảnh, mong đợi `DONE 0 chỗ chồng`).
- **Sửa thêm (3/11): tiếng xì nền.** `hd/aud106.py` (chạy sau `ui106.py`): nước mương 900 Hz chỉ nghe gần mương, lá/gió lặng giữa cơn. Đo bằng `tHiss.js` (dải 2–5 kHz sàn −65 → −83 dB).
- **Sửa thêm (3/11): giỏ lục bình chơi được.** `hd/gio106.py` (chạy sau `aud106.py`): từ cấp mở giỏ lục bình có chỗ riêng dưới mương (không chung 4 chỗ với củi/lá/sâu), 4 bụi/20 phút, vịt chỉ ăn lục bình khi máng trống, phơi 3 tiếng; chữ bay đếm x/5, Ngoại dặn đem phơi, bong bóng ở ghế hiên, bảng hiên có tươi/khô và nút "Đem 5 bó ra nong phơi". Kiểm bằng `tGio106.js` (mong đợi `DONE 0 chỗ sai`). Bot đo trước/sau: xem `qa-v106a.md` mục 1.3.
- **Dựng v106a:** `python3 ui106.py live/vuon3d.html live/v106a.html && python3 aud106.py live/v106a.html live/v106a.html && python3 gio106.py live/v106a.html live/v106a.html`, rồi đổi `BUILD = 'v105'` thành `'v106a'`. Trang test: `cat x40f.js x106.js xpop.js > /tmp/x.js; python3 gen_test2.py /tmp/x.js live/v106a.html lp/mv2_t106.html`. `gen_test2.py` nay nạp Baloo 2, Patrick Hand trong máy (test chặn mạng ngoài nên trước đó font bị thay).
- **QA/QC đầy đủ:** `hd/qa-v106a.md` (đề xuất giỏ lục bình, hố ủ, tab Sổ, draw call, token). Chờ anh chọn thứ tự.
- **Sửa thêm (3/11): chạm ma trên điện thoại.** Chạm vườn mở bảng lúc `pointerup`, rồi `click` trình duyệt bắn theo trúng nút trong bảng vừa mở: chạm đất trống là tự đắp liếp, chạm nong là tự mở chọn món. Đã nuốt click đó trong 450 ms (`TAPT`, dòng vá trong `ui106.py`).
- **Sổ còn 3 tab:** Việc · Kho · Bộ sưu tập. Bộ sưu tập có chip Giống · Cá · Bướm · Cổ tích (chip chỉ hiện khi tới cấp). `openBook('ca')` cũ vẫn chạy: mở Bộ sưu tập, chip Cá. Bấm lại Bộ sưu tập thì nhớ chip cuối (`BOOK.sub`).
- **Chợ:** tab "Trang trí" đổi thành **Tiệm**, có hàng chip (`SHEET.sub`). Hiện chỉ có chip Đồ kiểng; Tiệm may, Thợ nhà, Bảng tên thêm ở phần B, C. Tab Đơn hàng giữ nguyên.
- **Bỏ chế độ Sửa vườn:** không còn nút Sửa vườn. Chạm thẳng ô cỏ để khai hoang, ô đất trống để đắp liếp hay đặt đồ, chạm đồ kiểng mở bảng có Dời/Cất. Chạm ao mở bảng có "Xem sổ cá" + "Dời". Cây cổ tích dời từ Sổ cổ tích (nút "Dời cây qua chỗ khác"). Thùng ong có nút dời. Liếp trống ở bãi có "San thành đất trống" trong vòng gieo và bảng liếp. Thanh còn lại chỉ dùng khi đặt: "Đặt đồ · Chạm một ô trống để đặt X · **Hủy**"; đặt xong tự tắt.
- Sửa kèm: việc hôm nay "Đặt 1 món trang trí" trước đây mở bảng trống, nay mở Chợ › Tiệm. `avHud` không lỗi khi gọi lúc đang tải.
- Câu việc cấp 8 đổi thành "Chạm ô cỏ ở bãi hông nhà, khai hoang rồi đắp 2 liếp".
- Chưa làm: "khung cọc tre mờ" quanh ô đất trống (anh có nhắc trong đề xuất); kiểm lại `tbai.js`, `tBig.js`, `tDc.js` vì chúng có thể gọi `suaOn(true)` kiểu cũ.

### 6.0 VIỆC ĐANG DỞ / TỒN ĐỌNG (cập nhật 4/11 chiều — đọc mục này trước)
- **v110b ĐÃ LÊN LIVE 4/11 chiều** (main 3844b95) (`live/v110b.html`, BUILD `v110b`; dựng: `python3 fix110b.py live/v110a.html live/v110b.html && python3 tre110.py live/v110b.html live/v110b.html`). Gồm: thẻ việc về một việc + dòng "Việc hôm nay N/5", ẩn khi ghé vườn; bình tưới luôn hiện, số liếp khô dần (<60% ẩm), chạm tưới hết; ở vườn bạn bình tưới = tưới giùm từng liếp lấy công; câu báo lỗi không lặp chữ; hái trộm 3/ngày (`DOICONG = 3`); tre trăm đốt 5 đốt/đống, 2 đống một lúc, 20–40 phút rớt thêm, không quầng sáng. Test: `tVisit110b.js` qua; regression đầy đủ đang chạy lúc chuyển phiên — chạy lại rồi ship (đổi BUILD `v110`→ `v110b`, `buildsite.py`, commit main qua worktree, **fetch + merge origin/main trước** vì phiên khác cũng push main, đưa anh lệnh push).
- **Server đã sửa 4/11:** ràng buộc `mv2_events_kind_check` có thêm `help` (trước đó mọi lần hái giùm lỗi 400); `mv2_act` steal 5 → 3. Ghi chú trong `hd/sql/`.
- **Anh đã duyệt, làm tiếp theo thứ tự:** (1) v111 theo `dexuat-v111.md`: bản tiếng Anh dịch đủ (bảng `TXT.vi/en`, tự theo ngôn ngữ máy, giữ tên đặc trưng kèm nghĩa), đất linh hoạt (ô trống: đắp liếp / trồng cây / dựng giàn / đặt đồ, đổi qua lại, mua thêm lu nong khạp), mật thư bụi chuối (câu chọn sẵn + quà nhỏ, loại `note` trên server); (2) hiệu năng điện thoại; (3) ảnh xem trước khi share; (4) hiệu ứng; (5) Sổ theo `hud-hethong.md` (mock trước); (6) giàn bầu bí; (7) ao công trình lớn (`ao-cong-trinh.md`, mock trước). Sau đó: chỗ tiêu xu, lỗi QC cũ, bong bóng liếp, icon túi hạt. Anh còn phải quyết: lên Supabase Pro trước khi quảng bá.
- **v110e LIVE 4/11 đêm** (`fix110e.py` trên v110d: ô hạt giống thẳng hàng, tên rau luôn chiếm 2 dòng, giá/thời gian cùng độ cao; dò `tGiong110e.js`). Tiếng Anh `en111.py` nay dựng trên v110e → `live/v111a.html`.
- **v112a (chờ ship, 4/11 khuya)** `sap112.py` trên v110e: nhấn giữ món đang đặt (nong, khạp, lò, hố ủ, thùng ong, đồ kiểng, cây cổ tích) là kéo; ô hợp lệ viền xanh nét đứt, ô không được đỏ + lý do; thả xong 3 nút Đặt/Hủy/Cất (cây cổ tích: Về chỗ cũ). Chế độ Sắp vườn (nút dưới Về giữa, cấp 8+): ẩn HUD + bong bóng, nút + trên ô trống bung Liếp/Cây, khay Túi đồ (đồ cất, đồ kiểng trong túi, món chưa mua kèm giá, ao), kéo vô khay là cất. Bảng ô trống gọn (Đắp liếp + dòng dẫn Sắp vườn). Đồ cất: `ST[k].at = null`. Lớp vẽ ô = SVG `#sapSvg` (SVG không nhận `.hidden`, phải dùng set/removeAttribute). Kèm: Sổ mép trên/dưới mờ dần (sticky ::before/::after, top/bottom -padding), tiêu đề mục Sổ chữ nhỏ xuống dòng; ao/lò/chuồng phút cuối đếm giây, chạm khi hết giờ là xong; vòng vẽ mỗi tick chạy riêng `tk()`. Giàn trên ô CHƯA làm (chưa có cây dây leo trồng trên ô). Test: `tSap112.js` (25 bước × ĐT/PC), `probe_bk.js`.
- **deco113 (bản vẽ chờ duyệt):** `deco113.py` thêm 10 món (đèn bão 250 → miếu Ông Địa 45.000), mô hình trong `DCX`, tờ hình `tDeco113.js` → `hud16/deco_sheet.png`, `deco_vuon.png`. Xuồng ba lá cần sửa mũi cong. Anh dặn: giá đồ trang trí phải hợp người dư xu (cả 14 món cũ 80–500 xu cũng cần nâng giá).
- **Sắp vườn (mock đã duyệt):** mock `tSap.js` → `hud16/{ph,pc}_{1_keo,2_sap,3_trong}.png`: nhấn giữ kéo (ô xanh/đỏ theo 4 góc ô thật, nút đặt/hủy/cất), chế độ Sắp vườn (thanh trên + Xong, nút + trên ô trống bung Liếp/Cây/Giàn, khay Túi đồ có Mua thêm), bảng ô trống gọn (Đắp liếp + dòng dẫn sang Sắp vườn). Kế hoạch: `plan-dat-linhhoat.md`.
- **v110d** 4/11 khuya (`fix110d.py` trên v110c: thẻ việc hẹp 70% chữ ≥12px, fmtMin làm tròn, mái chuồng vịt, thẻ cá chỉ nhận bấm bắt đầu sau khi hiện). **Tiếng Anh (`en111.py` trên v110d → `live/v111a.html`, bảng dịch `hd/i18n/en_*.json`, mẫu `rx_*.json`; dò `tEn111.js` 15 màn PC+ĐT gần sạch, còn 1 câu đơn ghe + 1 dòng tab Mua) — chưa ship, chờ anh duyệt hình.**
- **v110c LIVE 4/11 tối** (Sổ mới, `so110c.py` + `so110c.css`). **Tiếng Anh đợt 1 đã dựng:** `en111.py` trên v110c → `live/v111a.html` (LANG đầu module, UIEN + MutationObserver, tên món/cá/bướm, hàng Ngôn ngữ trong Cài đặt), chưa chụp/test.
- **Tiếng Anh, kế hoạch:** game có ~1.080 chuỗi chữ Việt khác nhau (~14.000 từ), viết thẳng trong code. Kế hoạch 4 đợt: (1) khung `TXT`/`tx()` + nút đổi ngôn ngữ + giao diện + tên món; (2) việc, đơn, Sổ, cá, bướm; (3) lời Ngoại, câu chuyện món, 6 sự tích; (4) soát điện thoại. Mỗi đợt có test bật EN dò chữ Việt sót.

### 6.1d v108–v110 — lên live 4/11 chiều
- **v108 giao diện** theo `hud-hethong.md` (anh duyệt sau 4 vòng mock): dải tiêu đề cùng màu viền gỗ, thẻ trạng thái, ô số, thanh 1 loại 2 cỡ, 4 loại nút; Chuồng gà ba ô; thẻ Ngoại nhờ 3 ô (ô CẤP có chấm bước, "+N"); khay trái badge đỏ, hết rơm "+ 5 xu", hết hạt "Mua hạt"; menu giữ kiểu cũ.
- **v109 gà vịt + đơn hàng** (`ga-vit-raso.md`, `don-hang-v109.md`): để 2–6 trứng cho mái ấp (ổ theo chuồng), 85% nở, gà nằm ổ, gà con chỉ lúc dẫn, thẻ kết quả, trống dư bán giống; chợ 1 gà mái/ngày; vịt khớp số; lò ấp có ngả hột vịt lộn. Đơn hàng xóm luôn có rau, đa dạng theo cấp, chỉ món làm được, cá trong mọi đơn + việc ≤ 3, món ruột mỗi nhà, "Để bữa khác" 3 lần/ngày. Đo `tOrd109.js`: 100% đơn có rau, rau ~50–55% ở cấp 8+.
- **v110** (`truoc-quang-ba.md` A2, A3, A5, B1 + ý anh): ghé vườn báo đúng lỗi server (`vErr`), rớt mạng thử lại 1 lần, 10 lỗi gần nhất ở `localStorage['mv2-neterr']`; mở game/quay lại mà mây mới hơn và chưa chạm gì thì tự tải; hố ủ 3 nguồn (gốc rau khi hái, phân chuồng theo số con, lá rụng) có thanh + bong bóng; lục bình không vô hố, 3/4 trôi trên sông vướng xuồng; lá rụng 18 phút, chỗ thấy; mũi tên lần đầu cho củi, lục bình; gà vịt nở có chúc mừng.
- Test: regression chuẩn + `tPop tOrd109 tNet110 tHo110 tOdd110` + qcLv đều qua trên v110a. Việc tiếp: hiệu năng → ảnh xem trước → hiệu ứng → Sổ → ao công trình lớn (`ao-cong-trinh.md`).
- Ghi chú máy: macOS không có lệnh `timeout`; máy nặng tải thì boot trên trang test mất ~30 giây (`tBoot.js` chờ 300 s).

### 6.1c v107b — lên live 4/11 trưa: **sửa nhấp nháy đất trống / hố ủ / đất phơi ải** (`hd/fix107b.py`, một dòng). Lỗi do `draw107`: tấm đất ô trống (`v.bareMat`) vừa được giữ bản gốc (để đổi màu theo ải/công) vừa bị gộp thêm một bản vào vật liệu chung → hai tấm chồng khít → z-fighting. Vá: `bm.userData.keep = true` để `mergeMeshes` bỏ qua. Kiểm: ô đất v107 có 4 mesh (dư 'vc:132'), v107b còn 3. Regression 7 bài + qcLv qua. **Bài học:** chỗ nào so sánh `material ===` sau `mergeMeshes` (bare, FSH) đều phải xem lại khi đổi cách gộp. `hd/tFlick.js` đếm pixel đổi giữa khung hình (chưa đủ nhạy vì cây đung đưa).

### 6.1b v107 — lên live 4/11 sáng. Bộ test v107 (7 bài) + regression chuẩn (11 bài) qua trên `live/v107a.html`; migration `sql/mv2_act_help.sql` đã apply (4/11, kiểm `pg_get_functiondef` có `'help'`). Tab Sổ `tabso.css` không vào bản này.
Nguồn `hd/live/v107a.html` = v106 + `hd/fix107.py` (vá có kiểm tra, chạy trên `live/vuon3d.html`). Đã làm và test qua:
- **Củi có đống riêng** (`CUI_CAP` 20, không tính chỗ gác bếp); lục bình, lục bình khô, giỏ để dưới hiên (`HIEN`). Trước đó củi lấp đầy gác bếp nên chuỗi giỏ kẹt (bot 0 giỏ/30 ngày → nay 28 giỏ). Thưởng việc quá sức chứa thì đổi xu.
- **Đổi công "hái giùm"** (`tDoiCong.js`): chạm liếp chín khi chưa có công = hái giùm, rau vô kho chủ vườn qua hộp thư (loại `help`). Server: `mv2_act` trên Supabase (project `zgfanxtjdvioxpgpbcke`) đã có `when 'help' then 5` (migration `mv2_act_help_kind`, 4/11).
- **Hố ủ** (`tHo107.js`): "Bỏ 1 rau dư" thành "Hốt phân chuồng" (chuồng gà/vịt 6 tiếng 1 phần, tối đa 4, `ST.ho.pct`); hái liếp đất mệt hiện chữ bay "Đất mệt · hụt N" và Ngoại giải thích một lần (`seen.datmet`).
- Vịt 1 bó rau muống = 4 phần; vòng Cỏ rậm không nói số cấp; chữ ≥12px, vùng chạm ≥44px, chữ nhạt `#A07A55` → `#8A5D3B`.
- Dưa cải: 4 cải ra 2 hũ (giá giữ 65); hột vịt: 6 trứng ra 6 hột; đơn không chọn món đang nằm trong đơn khác.
- Nong phơi: chế độ giờ cố định coi như luôn có nắng (trước đó chọn giờ tối thì nong không bao giờ khô). Vòng gieo gắn nhãn "đất mệt" lên thứ vừa trồng ở liếp đó khi đất < 0,6.
- Trời trong vườn: Cài đặt chỉ còn "Giờ trong vườn" và "Luôn ban ngày" (anh chốt 3/11). Bỏ "Theo giờ thật"; "Chỉnh tay giờ" chỉ hiện khi URL có `?dev`. Lúc mở game, `tm` là `real` (hay `fixed` không có ?dev) tự về `game`.
- Gác bếp mua thêm kệ: `ST.gbx` 0–3, `GB_CAP = 20 + 10·gbx` (nay là `let`), nút trong Sổ › Kho, 150/250/350 xu.
- Tab Sổ làm lại: bản mẫu CSS `hd/tabso.css` anh **không duyệt** (vẫn kiểu nút web). Làm lại trong đợt HUD chung (`hd/hud-huongdi.md`).
- Đề xuất chờ chốt: `hd/dexuat-v107.md` (bảng Đất trống 2×2, khoá khu đất, chuỗi nhiệm vụ 3 bước).
- **Draw call:** `hd/draw107.py` (chạy sau `fix107.py`): hai bước gộp mesh gộp theo đặc tính vật liệu thay vì từng màu, màu nằm trong đỉnh (`vcKey/vcMat/vcBake`). Điện thoại 697 → 554 lần vẽ/khung, hình y hệt (so `tShot.js`). Còn lại chủ yếu là bong bóng việc trên liếp (~160, `MeshBasicMaterial`, mỗi bong bóng 3 mesh) và nhân vật (40 mesh, nhóm `DYN`): gộp tiếp ở v108 (bong bóng thành một `InstancedMesh` hay sprite atlas; nhân vật gộp theo từng chi). Đo bằng `tDraw.js`.
- Server: `hd/sql/mv2_act_help.sql` là migration cho đổi công (thêm `'help'`), đã apply 4/11.
- **Dựng v107:** `python3 fix107.py live/vuon3d.html live/v107a.html && python3 draw107.py live/v107a.html live/v107a.html`, rồi đổi `BUILD` thành `v107a` (khi ship: `v107`).
- Bot v107 (30 ngày, 3/11 đêm): cấp 16 ngày 17,8; 29 giỏ; xu dư ngày 30 **118.000** (v106: 93.000, tăng do dưa cải 2 hũ, hột vịt 6) → phần C "chỗ tiêu xu" càng cần.
- Test v107: `tSet107 tGio106 tDoiCong tHo107 tPop tA106 tAudit` (+ `tBoot.js` chạy trước để bắt lỗi khởi động trong 90 giây thay vì chờ 5 phút) trên trang `lp/mv2_t107.html` (dựng từ `live/v107a.html` với `x40f.js x106.js xpop.js`). Draw call: đang đo bằng `tDraw.js`.

### 6.2 v106 phần B: đồ nhân vật và nhà (anh đã duyệt)
- **Tủ đồ:** chạm avatar mở tủ đồ. Đồ theo từng món; 6 dáng sẵn có (`AVS`) thành bộ đồ ban đầu.
- **Tiệm may** (cấp 5) trong Chợ › Tiệm: bán áo bà ba, nón lá, khăn rằn…
- **Thợ nhà** (cấp 18): chạm nhà mở thợ nhà. Sơn nhà, mái ngói, hiên gạch tàu, cửa sổ chạm, bàn thờ ông Thiên.
- Món đặc biệt chỉ có qua sự kiện (Tết, hội câu…).
- Mô hình, hình đồ phải gửi anh duyệt trước.

### 6.3 v106 phần C: chỗ tiêu xu (anh đã duyệt)
- Mở rộng bếp (bếp khang trang hơn).
- Đồ kiểng cao cấp: hòn non bộ, mai vàng, lu Bát Tràng, chuồng bồ câu, giàn bông giấy. **Giá cố định**, không tăng theo số món.
- **Bảng tên vườn:** bảng đầu miễn phí; đổi tên phải làm bảng mới, tốn xu. Bậc: bảng gỗ tạp → gỗ sơn → cổng tre → cổng gạch. (Hiện đổi tên vườn tự do, cần chuyển qua bảng.)
- Đất xa hơn bên kia rạch.
- Mô hình duyệt trước.

### 6.4 Sau đó
- **Dây leo, giàn trên đất mới:** khổ qua 6, mướp 8, bầu 10, bí đao 12, đậu rồng 14, chanh dây 17. Từ cấp 9 dựng giàn được trên đất mới, tối đa 2 giàn mỗi khu. Giữ 20 cấp. Mỗi dây phải khớp ngược với bảng cấp, việc, món ăn, đơn hàng xóm, đơn ghe.
- Công trình xóm, đình làng (lễ Kỳ Yên): để sau khi mở rộng bản đồ.
- Chạy lại bot đo nhịp sau mỗi thay đổi lớn.
- Vòng "Cỏ rậm" (vườn chính, đủ liếp) còn ghi `cấp ${bedNext()} đắp thêm được`: trái luật không nói số cấp tương lai, chưa sửa (cần anh chọn câu thay).
- **Chờ anh trả lời:** cho vịt ăn hiện tốn nhiều bó rau muống (12 vịt × 2 phần, 1 bó = 2 phần). Đã đề xuất 1 bó = 4 phần, anh chưa chốt.
- **Đã chốt (3/11):** Sổ cổ tích giữ ô "???" cho cây chưa mọc (để người chơi thấy còn cây để tìm) nhưng bỏ số cấp. Đã vá trong `hd/ui106.py` (dòng `rep` "sổ cổ tích") và `hd/live/v106a.html`.
- Lỗi còn mở từ QC cũ: xem mục 4 của `qc-v84-v90-ban-giao.md` (hộp thư cộng quà hai lần khi ack lỗi, khôi phục mây ghi đè `real`, bán được món `nosell`, rò geometry, draw call cao…).

---

## 7. Về anh Ares
Creative director, chạy Fungii Studio (TP.HCM). Mạnh về concept, hình ảnh, trải nghiệm; không viết code. Anh chơi thử trên máy tính lẫn điện thoại và hay gửi ảnh chụp lỗi. Anh muốn game sống động (ánh sáng ngày đêm, đom đóm, lá bay, cá nhảy), kinh tế chặt và hợp lý, thứ gì phi lý là anh hỏi lại. Khi anh hỏi "m thấy sao", trả lời như người làm game có kinh nghiệm: nêu ý kiến rõ và lý do.

## Đồ trang trí (bản nháp v113j, chưa ship, chờ anh Ares duyệt)
- Dựng: `python3 deco113.py live/v112a.html live/v113j.html` (mô hình ở `deco113_models.js`), so sánh: `node tDecoCmp.js` ra `hud16/deco_*.png`.
- Còn phải làm khi duyệt: đặt món 2x2 (xuồng, chòi, miếu) qua Sắp vườn và tiệm, áp bảng giá mới trong `tDecoCmp.js` (P2) vào DCK, đo máy điện thoại yếu.
- Đã duyệt hướng: rào đất mới chỉ giữ hai cạnh sau, hai cạnh trước là bờ thấp; mương đất mới chỉ hiện cạnh ô có liếp. Dò đâm xuyên: `node tDecoQC.js`.
- Skill Makone nằm ở `~/Makone/skills` (world, object, craft), không nằm trong danh sách skill của phiên.

- Test: trang do `gen_test*.py` dựng không chạm Supabase thật. Cần thử mạng thật thì đặt `MV_ONLINE=1`; vườn tạo từ trang test luôn mang tên bắt đầu bằng `TEST `.

### v113v (5/11) — Ông Địa ngồi thẳng, bụp ra, xoay một vòng rồi nói; tối ưu mô hình
- Dựng: `python3 deco113.py live/v112a.html live/v113v.html`. Que mảnh trong `lim` ít mặt theo bán kính, mái chòi 14 cột lá, viên ngói miếu 3 mặt (`ngoiRoof` thêm tham số `seg`, nhà chính không đổi), gạch sân miếu là tấm phẳng có nền lót.
- Đo: `node tOpt.js` (số tam giác, bóng, lượt vẽ), `node tOpt2.js` (cả cảnh), `node tOptCmp.js truoc|sau` (so hình). Miếu 19.8k còn 14.2k, chòi 17.8k còn 11.5k. Cả cảnh còn khoảng 800 lượt vẽ, phần lớn là mảnh nhỏ chưa gộp của người và con vật: đây là chỗ lợi nhất để tối ưu tiếp.
- Bảng ao đã duyệt, chưa vào game (`ao114_models.js`, `ao114.py`, `tAoSheet.js`). Nước ao dùng `waterMat` như sông, không gợn vì ba lớp nước sát nhau. Ao lớn 17.8k. Khi đưa vào game: lưới nước giữ `keep` nhưng `dcBuild` đang đặt bóng cho mesh `keep` và không nhận bóng, phải sửa; đèn lồng ao cần giới hạn số đèn thật, phần dư chỉ tự sáng; `LIGHTS.push` trong mô hình phải tránh tích lũy khi dựng lại.

### v113w (5/11) — câu cá theo cấp
- `CAU = { lv: 9, day: 6, them: [[12, 7], [15, 8], [18, 10]] }`, cộng 1 lượt thưởng như cũ. Lên đúng mốc có dòng "Câu thêm cá" và Ngoại báo. Test: `tCau113.js`, `tCauLv.js`.

### v114g (5/11) — sao lưu, ao ba bậc, giảm lượt vẽ, ghe, đèn đỏ, radio, mua thêm đồ, tiếng Anh
- Dựng: `./build114.sh` (deco113 → sv114 → aog114 → opt114 → fix114 → rad114 → multi114 → en111), ra `live/v114g.html`. Test: `tBak114 tAog114 tFix114 tRad114 tMulti114 tEn114`, trang test mặc định tiếng Việt.
- Sao lưu chỉ nằm trên máy người chơi (`mv2-bak`, 6 bản, tối đa 1,2 MB), không ghi Supabase.
- Ao: `ST.big.ao = { own, at, tier, to, at0, dc, nuoi }`. Ao lớn 3×3 chỉ vừa khu H. Đèn lồng ao tối đa 2 đèn thật.
- Radio ẩn khi chưa có nhạc. Bỏ file vào `hd/nhac/` tên `giut_*`, `cailuong_*`, `chieu_*`, `tin_*`, chạy lại build và chép thư mục `nhac` vào `mietvuon2/nhac`. Cần làm bước chép này khi có nhạc thật.
- Mua thêm: khoá giả `nong2, khap2, say2` trong `OBJD`, chung khay với món đầu, không đổi cấu trúc lưu.
- Tiếng Anh: `i18n/en_*.json`, `rx_*.json`. Máy không để tiếng Việt tự vào tiếng Anh. Lời Ngoại chưa soát hết.

## v115d (06/11/2026): sửa gấp sau báo lỗi live

- **Vườn "mất" là do http.** `http://fungiistudio.com` không tự chuyển sang https, mà trình duyệt lưu riêng cho mỗi địa chỉ. `load115_head.html` chuyển http sang https, mang vườn theo qua `#mv2mig=`; vườn cấp cao hơn được giữ, vườn kia vô `mv2-bak`. Link `#mv2mig` giả có thể đè vườn bằng vườn cấp cao hơn, bản cũ vẫn còn trong sao lưu. Đừng bật Enforce HTTPS của GitHub Pages sớm: nó chuyển trước khi script chạy, vườn đang nằm ở http sẽ kẹt lại.
- **Kẹt 62% là do tạo quá nhiều WebGLRenderer.** Tái hiện được trên WebKit của Playwright: v115b kẹt đúng 62%, v115d vào trong khoảng 4 giây. Mọi chỗ vẽ biểu tượng lúc tải dùng chung `ICR()`, giải phóng sau `__ready`. Thêm nữa: `toonRender` có đường lùi khi lỗi, màn tải tự tải lại một lần, rồi hiện nút Tải lại (`load115_watch.js`).
- **Lưu ý gen_test:** `gen_test.py` và `gen_test2.py` khớp đúng chuỗi ngay trước `{ const L0 = $('#load')`. Chèn gì vào giữa là mất `__tick`, `__g`, cả loạt test báo undefined.
- **Chậu Tết vẽ lại** (`chau115.py`): icon cúc, mai không còn dùng Math.random; `maiTree` trong vườn đổi thân chữ S. Chưa đổi `cucBush` trên liếp và chậu trên ghe chợ hoa.
- **Quét toàn game:** `node tScan.js webkit nhanh` với `PAGE=`. Macbook không có lệnh `timeout`, dùng `perl -e 'alarm N; exec @ARGV'`. Không chạy song song hai trình duyệt: test sẽ timeout giả (tDia113, tSap112 báo lỗi khi máy bận, chạy riêng thì qua).
- **Còn lại từ bài quét:** tiếng Anh còn sót chữ Việt (tên vườn lúc thử, bảng 3D "Mé sông"); `.stk` Xoài, Dừa tràn nhẹ.
