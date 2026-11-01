# Miệt Vườn 2.0 · Tài liệu bàn giao QC (bản v83, 1/11/2026)

Tài liệu này để mở một thread mới chỉ làm QC toàn bộ game. Đọc hết trước khi bắt đầu.

## 1. Game là gì

- Game nông trại low-poly three.js, bối cảnh miền Tây (Mekong). Tất cả chữ trong game là tiếng Việt, mọi thứ phải đúng chất miền Tây/Việt Nam.
- Một file HTML duy nhất (khoảng 4.800 dòng, nhiều dòng rất dài), three.js 0.169 từ CDN, không build step.
- Chơi theo giờ thật: một ngày trong game = 40 phút ngoài đời. Cây **không chết khi người chơi vắng mặt**.
- Nhân vật dẫn dắt là **Ngoại** (bà ngoại), nói qua bong bóng thoại. Người chơi xưng "con".
- Lưu trong `localStorage` key `mv2-state`, có đồng bộ đám mây qua Supabase (mã vườn + mã bí mật, ẩn danh).

## 2. Nơi để code, cách deploy

| Thứ | Ở đâu |
|---|---|
| Bản live | https://fungiistudio.com/mietvuon2 (GitHub Pages, repo `aresle86/fungiistudio`, thư mục `mietvuon2/index.html`) |
| Artifact game | https://claude.ai/artifact/DkesRLV6eCUtN56HxQnwiT |
| Bản trong Project | `claude/mietvuon/miet-vuon-2.0.html` |
| Kịch bản toàn cảnh (Claude Doc) | https://claude.ai/artifact/5zrepCFVxTCYk3zmhfgAuU (có changelog từng bản, luật bố cục, kế hoạch cấp 13–20) |
| Danh sách lời Ngoại | Project: `claude/mietvuon/loi-thoai-ngoai.md` |
| Bộ test QC | repo `aresle86/fungiistudio`, **nhánh `mietvuon2-qc`** (không phải main), thư mục `hd/` |

`mietvuon2/index.html` = file nguồn `hd/live/vuon3d.html` + phần `<head>` do `hd/buildsite.py` thêm (meta, manifest, og). Muốn sửa game: sửa `hd/live/vuon3d.html`, chạy `python3 buildsite.py` (sửa đường dẫn ghi file trong script cho đúng máy), commit `mietvuon2/`, push `main` và `main:mietvuon2-online`.

Mỗi lần deploy phải đổi hằng số `const BUILD = 'v83'` (tab mở lâu sẽ thấy nút "Có bản mới · chạm để tải lại").

## 3. Dựng môi trường test

```bash
git clone https://github.com/aresle86/fungiistudio && cd fungiistudio && git checkout mietvuon2-qc
cd hd/lp && npm i            # three@0.169 + font Paytone One (bản offline cho test)
cd .. && python3 gen_test.py x40.js          # tạo lp/mv2_test.html từ live/vuon3d.html
(cd lp && python3 -m http.server 8777)       # chạy nền; server phải sống suốt lúc test
```

- `gen_test.py x40.js` → `lp/mv2_test.html`: thay CDN bằng `node_modules`, chèn `x40.js` (các hook `window.__…` để test gọi hàm nội bộ), và tự ẩn màn load.
- `gen_test2.py x40.js <nguồn> <đích>` → bản dev riêng (vd `lp/mv2_dev.html`) để thử mà không làm hỏng bản đang chạy regression.
- Playwright + Chromium cài sẵn trong môi trường Claude: `require('playwright')`, launch với `--use-angle=swiftshader --enable-unsafe-swiftshader --ignore-gpu-blocklist`.
- Kiểm cú pháp module (bắt buộc sau mỗi lần sửa): tách `<script type="module">` ra file `.mjs`, comment dòng import `mergeGeometries`, chạy `node --check`. `new Function()` không parse được module.

**Lưu ý môi trường đã gặp:**
- `waitForFunction(fn, null, {timeout})`: tham số thứ hai phải là `null`, nếu không timeout mặc định 30 s.
- `canvas.toDataURL()` và `page.screenshot()` đôi khi treo trong swiftshader sau nhiều lần render (bị cả ở bản cũ v79). Đây là lỗi môi trường, không phải game. Test `tTet`, `tBuom` hay chết ở bước chụp hình.
- Không chạy hai regression cùng lúc. Không sửa `mv2_test.html` khi regression đang chạy.
- Server `http.server` chạy nền bị tắt sau 2 tiếng; khởi động lại. Đừng `pkill -f "http.server"` trong cùng lệnh khởi động (tự giết chính nó).

## 4. Bộ test có sẵn

`bash runall.sh` (khoảng 50 phút) = `runreg5.sh` + nhóm test mở rộng. Kết quả ở `reg5.txt` và `extra.txt`; tìm `ERR`, `Error`, `Node.js` (lỗi node), `errs [ ... ]` khác rỗng.

| Test | Kiểm |
|---|---|
| terr2 | Trang tải xong, `__ready` |
| tnew | Người chơi mới: gieo, hái, bán, lên cấp 3. Lỗi `openIntro innerHTML null` là do test tự xóa `#intro`, bỏ qua |
| told | Save cũ di trú đúng (cấp 6, kinh tế mới) |
| tga | Gà: mua, ấp, gà con lớn |
| tbai | Bãi hông nhà: khai hoang, đặt nong |
| todd | Việc lặt vặt (sâu, lục bình, lá, củi) |
| tbep | Bếp Ngoại: nhóm bếp, nấu, lấy món |
| tqa | Việc Ngoại dặn, di trú quest, Sổ + Chợ |
| tvis | Thăm vườn mẫu của Ngoại |
| tT, tR, tG | Cầm/cất dụng cụ, rơm phủ liếp, vòng chọn hạt tại chỗ |
| tC, tV | Sửa chuồng gà (lượm tre), dựng chuồng vịt |
| tL | Đi qua cấp 2→13, kiểm thẻ "Việc tiếp theo" và việc hôm nay |
| tLand | Phơi ải đất mới |
| tTet | Mùa Tết, tiệm Tết, lì xì, đơn Tết |
| tCloud | Lưu/kéo đám mây (mạng Supabase bị chặn trong môi trường test) |
| tTree | Cây trái, ô 2×2 |
| tFish, tFish3, tFish5 | Câu cá, mồi, cá hiếm, hội câu, thưởng tuần |
| tFt | Cây cổ tích vú sữa, tre trăm đốt |
| tTc | Cây trầu cau |
| tFt6 | 3 cây cổ tích mới (dưa hấu, khế vàng, Sọ Dừa), vàng khế, Sọ Dừa tưới giùm, quest cấp 14 |
| tDd | Thẻ về vườn 7 ngày liền |
| tBig | Đặt/dời đồ 2×2 (ao, cây cổ tích) |
| tDc | Trang trí cấp 13 (rào, chuồng, đồ kiểng). Hay báo `sheetfail` ở bước chụp, bỏ qua nếu `errs []` |
| tNg | Lời Ngoại sau khi giảm tải, toast, tab Sổ ẩn theo cấp |
| tMai | Lợp mái cấp 15: cũ → đang lợp → mới, bạn ghé phụ |
| tVisit, tMob, tTre, tReset, tLoad | Thăm vườn trên điện thoại, tràn màn hình, mũi tên lượm tre, chơi lại từ đầu, màn load |

Hook test chính (trong `x40.js`): `__g` (ST, act, sim, openSheet, closeSheet, say…), `__x` (openBook, levelUp, PLOTS, ICON…), `__FT` (fairyModel, sdAnim, dhBird, kvSpin), `__FT2` (FT, ftTap, ftTell, ftCheck, pgCotich…), `__FT3` (sdHelp, dcPay, ftCompact, roofState, maiLeft, doQuest), `__OB` (openBook), `__VG` (visitGo), `__ICON`. Gọi `window.__stop = true` để dừng vòng lặp rồi tự `__tick()`.

## 5. Tiến trình cấp và hệ thống

Kinh nghiệm cần: cấp 2: 10 · 3: 30 · 4: 80 · 5: 190 · 6: 310 · 7: 450 · 8: 610 · 9: 840 · 10: 1.060 · 11: 1.320 · 12: 1.620 · 13: 1.960 · 14: 2.340 · 15: 2.760 · 16: 3.220 · 17: 3.720 · 18: 4.260 · 19: 4.840 · 20: 5.460.

| Cấp | Mở ra | Việc Ngoại dặn để lên cấp này |
|---|---|---|
| 1 | Cải, hành, gieo, tưới, hái, bán, rơm phủ | – |
| 2 | Việc lặt vặt, sửa chuồng gà (lượm 2 tre, 3 rơm, 40 xu) | – |
| 3 | Đơn nhà bên, bắt sâu | Phát 14 bụi cỏ mé mương |
| 4 | Bếp Ngoại, nhặt củi, góc vườn mới (120 xu) | Đắp đủ 8 liếp + giao 1 đơn |
| 5 | Mua gà, ấp trứng, hàng xóm online | Trả 120 xu dọn góc vườn |
| 6 | Chuồng vịt (lượm 3 tre, 4 rơm, 150 xu), cây cổ tích vú sữa | Ấp nở 1 con gà |
| 7 | Bãi hông nhà, Sửa vườn, nong phơi | Trả 100 xu cắm giàn tre |
| 8 | Khạp muối, hố ủ phân, bướm | Đắp 2 liếp bãi hông nhà + phơi 1 mẻ |
| 9 | Mé sông (8 ô), câu cá, lò ấp vịt, ao cá, tre trăm đốt | Giao 5 đơn |
| 10 | Lò sấy, ghe chợ nổi, giỏ lục bình | Trả 200 xu đắp bờ mé sông |
| 11 | Sau nhà 10 ô (dọn tre gai ở cấp 12) | Trồng 3 cây trái |
| 12 | Dừa, món Tết, Sổ vườn, trầu cau | Trả 250 xu dọn tre gai |
| 13 | Trang trí (rào, chuồng, chậu kiểng, cổng) | Phơi 10 mẻ |
| 14 | Cây cổ tích dưa hấu | Giao 3 đơn ghe chợ nổi |
| 15 | Lợp mái nhà (chờ khoảng 10 tiếng) | Trả 400 xu lợp mái |
| 16 | Cây cổ tích khế vàng | Nấu 8 nồi món cá |
| 17 | (chưa có nội dung mới; dự kiến ong) | Hái 5 vụ cây trái |
| 18 | Cây cổ tích Sọ Dừa | Có 3 cây cổ tích đã lớn |
| 19 | (dự kiến đóng xuồng) | Câu đủ 15 loài cá |
| 20 | (chưa có nội dung mới; dự kiến Ngoại tổng kết một năm) | Về vườn đủ 30 ngày |

**Cây cổ tích** (6 cây; mỗi cây: đốm sáng → chạm → lớn dần theo giờ thật → Ngoại kể từng đoạn → ghi Sổ cổ tích; dời được bằng Sửa vườn lên 2×2 ô):

| Cây | Cấp | Điều kiện hiện ra | Quà khi lớn |
|---|---|---|---|
| Vú sữa | 6 | Về vườn đủ 7 ngày liền | Mỗi ngày tối đa 2 trái (không bán, làm quà ghé vườn) |
| Tre trăm đốt | 9 | Thu 3 vụ khổ qua trên giàn | Gom 100 đốt tre → "Khắc nhập", chỉ để xem |
| Trầu cau | 12 | Khách ghé + đi thăm tổng 5 lần | Mỗi ngày 3 miếng trầu (không bán) |
| Dưa hấu | 14 | Chừa 1 ô đất mé sông trống qua 1 đêm | 2 ngày 1 trái dưa khắc tên |
| Khế vàng | 16 | Hái cây khế 5 vụ | Mỗi tuần 1 cục vàng = trừ 300 xu khi mua đồ trang trí |
| Sọ Dừa | 18 | Hái cây dừa 3 vụ | Khoảng 20 phút tự tưới 1 liếp khô |

Các hệ khác: ghé vườn bạn (đổi công tưới giùm/hái ké, tặng/xin hạt, để quà), thẻ về vườn 7 ngày, việc hôm nay (5 việc), đơn nhà bên, ghe bẹo, mùa Tết theo lịch thật, sổ cá/bướm/cổ tích, Ngoại kể chuyện món ăn.

## 6. Luật thiết kế phải giữ khi QC

- Đất mới luôn có mương giữa các hàng liếp. Đồ đặt trên ô nằm trên cỏ xanh.
- Mô hình mới phải cùng độ chi tiết với mô hình cũ; mái lá/hoa phủ kín, mượt, không lởm chởm; cây theo dáng thật, tán phân tầng.
- Chữ trong game nói theo hướng tích cực. Không âm bass nặng.
- Cây không chết vì vắng mặt. Không bán "xây nhanh" bằng xu.
- Ngoại không tự nói khi đang có bảng, Sổ, vòng chọn, thẻ lên cấp, thẻ 7 ngày, thẻ cá, thông báo nổi; câu tự nói cách nhau ≥15–20 s. Lỗi/giới hạn/xác nhận hiện bằng thông báo nhỏ (toast), không phải lời Ngoại.
- Tab Sổ chỉ hiện khi tới cấp (Cổ tích 6, Bướm 8, Cá 9).

## 7. Lỗi đã biết, chỗ cần QC kỹ

1. **Nút "Về vườn mình" ở vườn mẫu biến mất**: người chơi báo, chưa tái hiện được. v80 đã thêm tự gắn lại nút sau 1,5 s. Cần thử nhiều trên iPhone thật (Chrome iOS, Safari).
2. **Tràn màn hình điện thoại** (iPhone có thanh trình duyệt dưới): đã chuyển sang `dvh` ở v80; cần kiểm lại mọi bảng (Chợ, Sổ, bếp, chuồng, trang trí, câu cá).
3. **Màn load**: đã thêm thanh tiến trình và nhường máy giữa các phần dựng (`await LDY()` khắp file). Kiểm trên máy yếu xem còn khựng không.
4. **Chơi lại từ đầu**: v80 sửa lỗi `ST.ga.fixed` và nhảy cấp 6. Save bị bản cũ reset vẫn mang cấp 6 cho tới khi reset lại một lần ở bản mới.
5. Cấp 17, 19, 20 chưa có nội dung mở mới (chỉ có việc Ngoại dặn). Nhà lợp mái cấp 15 mới đổi hình mái, các phần sửa nhà khác chưa làm.
6. Hiệu năng: cây cổ tích đã gộp mảnh (ftCompact), mái nhà gộp mảnh. Cần đo FPS trên điện thoại ở cấp cao (nhiều cây, nhiều đồ kiểng, bướm, cá trong ao).
7. Đồng bộ đám mây: chưa test được trong môi trường Claude (Supabase bị chặn). Cần test tay: hai máy cùng mã vườn, cảnh báo "đã chơi tiếp ở máy khác".

## 8. Gợi ý kế hoạch QC

1. Chạy `runall.sh`, ghi lại mọi lỗi.
2. Viết thêm test đi trọn đường cấp 1 → 20 bằng hook (`__x.levelUp`, `__g.sim`), mỗi cấp mở Sổ/Chợ/bảng liên quan, bắt lỗi console.
3. Ma trận màn hình: 390×844, 375×667, 430×932 (dọc), 844×390 (ngang), 768×1024, 1280×800, 1920×1080. Mỗi màn: load, intro, Sổ (mọi tab), Chợ (3 tab), bếp, chuồng, trang trí, câu cá, ghé vườn. Kiểm không có nút bị che, không cuộn ngang.
4. Ma trận save: mới tinh, save cũ trước v79, save giữa chừng mỗi cấp, save đang ở vườn bạn (sessionStorage `mv2-visit`).
5. Thời gian thật: tua `ST.t`/`Date.now()` qua đêm, qua tuần, vắng 3 ngày, vắng 30 ngày; Tết.
6. Lời Ngoại: đếm số câu tự nói trong 15 phút đầu (mục tiêu ≤12), không câu nào lặp liền, không nói đè lên bảng.
7. Báo cáo: mỗi lỗi ghi bước tái hiện, màn hình, hình chụp, mức độ; xếp theo mức nghiêm trọng.
