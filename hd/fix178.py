# -*- coding: utf-8 -*-
# v178 — bảng Kho chia nhóm, có tiêu đề, trong nhóm xếp theo tên (chặng 1).
#
# Anh Ares: "arrangement của mấy thứ trong kho nhất là trong chỗ đựng đồ khô
# ko có một thứ tự gì hết, món ăn rải rác, các thứ rải rác mà list thì lại
# rất dài ko có ux ui friendly ko có tổ chức" → "Làm chặng 1".
#
# Đo trên v177, kho cỡ người chơi cấp 20:
#   - pgKho in thẳng Object.entries(ST.inv) và Object.entries(ST.gb), tức là
#     theo ĐÚNG THỨ TỰ MÓN ĐƯỢC CẤT VÀO — không sắp xếp, không chia nhóm.
#     Đọc ra: Cá sặc rằn, Cá hu, Ổi, Sung, Bắp nếp tím, Rau muống tía, Cá rô phi...
#   - 45 dòng, cao 3.350 px = hơn 4 màn điện thoại (375x812).
#   - Gác bếp nhét chung ba thứ khác hẳn nhau: món nấu (35 món), đồ khô/muối
#     (23 món), đồ dùng (củi, đường, muối, lục bình) — chỉ một tiêu đề.
#
# Vá: chia nhóm + xếp theo tên trong mỗi nhóm, mỗi nhóm một tiêu đề kèm số đếm.
#   Kho lu  : Rau · Trái · Cá · Trứng và thứ khác
#   Gác bếp : Đồ khô, đồ muối · Món nấu · Thứ khác
#   Bao hạt giống và Đồ dùng cũng xếp theo tên.
# Nhóm trống thì bỏ qua, không hiện tiêu đề rỗng.
#
# Phân nhóm lấy từ dữ liệu sẵn có (FISHK, CROPS[k].tree, DISH/PHOI/MUOI/SAY),
# thêm một bảng nhỏ KTRAI/KKHAC cho mấy món dữ liệu không nói được:
#   KTRAI = trái nhưng không mọc trên cây (khóm, mía, dưa hấu, trái vú sữa cổ tích)
#   KKHAC = cúc mâm xôi (hoa Tết) và rơm
# Muốn dời món nào qua nhóm khác chỉ cần thêm một chữ vô hai bảng đó.
#
# Không đụng tới xu, tới cách chơi, tới sức chứa — chỉ đổi cách bày ra màn hình.
import sys, io
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khớp %d lần, cần %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

# 0. số bản
rep("const BUILD = 'v177';", "const BUILD = 'v178';")

# 1. mấy hàm chia nhóm, đặt ngay trên pgKho
rep("function pgKho(full = true){",
    "const KTRAI = { khom: 1, khommat: 1, mia: 1, mialau: 1, duahau: 1, vusua: 1 }, KKHAC = { cuc: 1, rom: 1 };   /* trái không mọc trên cây; hoa Tết với rơm xếp chung thứ khác. Dời món nào qua nhóm khác thì sửa hai bảng này */\n"
    "const kTen = k => k === 'rom' ? 'Rơm' : k === 'cui' ? 'Củi' : (GD(k) || { name: k }).name;\n"
    "const kNhom = k => FISHK[k] ? 'ca' : KKHAC[k] ? 'khac' : ((CROPS[k] && CROPS[k].tree) || KTRAI[k]) ? 'trai' : CROPS[k] ? 'rau' : 'khac';\n"
    "const gNhom = k => DISH[k] ? 'mon' : (PHOI[k] || SAY[k] || MUOI[k]) ? 'kho' : 'khac';\n"
    "const kXep = L => L.slice().sort((a, b) => kTen(a[0]).localeCompare(kTen(b[0]), 'vi'));\n"
    "const kDe = t => `<div class=\"bkhn\" style=\"margin-top:12px;color:#6B4529\">${t}</div>`;\n"
    "function kNhomHTML(L, nhom, thutu, row){ let h = ''; for (const [g, ten] of thutu){ const P = kXep(L.filter(([k]) => nhom(k) === g)); if (!P.length) continue; h += kDe(`${ten} · ${P.length}`) + P.map(row).join(''); } return h; }   /* nhóm trống thì bỏ qua, khỏi hiện tiêu đề rỗng */\n"
    "const KLU = [['rau', 'Rau'], ['trai', 'Trái'], ['ca', 'Cá'], ['khac', 'Trứng và thứ khác']], KGB = [['kho', 'Đồ khô, đồ muối'], ['mon', 'Món nấu'], ['khac', 'Thứ khác']];\n"
    "function pgKho(full = true){")

# 2. kho lu: chia nhóm thay cho một dọc dài
rep("""  h += items.length ? items.map(([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${k === 'rom' ? 'Rơm' : (GD(k) || { name: k }).name}</span><span class="q">${n}</span></div>`).join('') : '<div class="bkhn">Kho trống trơn. Hái rau xong là có hàng đem bán.</div>';""",
    """  h += items.length ? kNhomHTML(items, kNhom, KLU, ([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${kTen(k)}</span><span class="q">${n}</span></div>`) : '<div class="bkhn">Kho trống trơn. Hái rau xong là có hàng đem bán.</div>';""")

# 3. bao hạt: xếp theo tên
rep("""if (seeds.length) h += `<div class="bkhn" style="margin-top:12px;color:#6B4529">Bao hạt trong túi</div>` + seeds.map(([k, n]) =>""",
    """if (seeds.length) h += kDe(`Bao hạt trong túi · ${seeds.length}`) + kXep(seeds).map(([k, n]) =>""")

# 4. gác bếp: tách đồ khô với món nấu
rep("""if (gbi.length) h += `<div class="bkhn" style="margin-top:12px;color:#6B4529">Gác bếp · ${gbUsed()}/${GB_CAP}</div>` + gbi.map(([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${k === 'cui' ? 'Củi' : (GD(k) || { name: k }).name}</span><span class="q" style="color:#9A6E12">${n}</span></div>`).join('');""",
    """if (gbi.length) h += kDe(`Gác bếp · ${gbUsed()}/${GB_CAP}`) + kNhomHTML(gbi, gNhom, KGB, ([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${kTen(k)}</span><span class="q" style="color:#9A6E12">${n}</span></div>`);""")

# 5. đồ dùng: xếp theo tên
rep("""if (hie.length) h += `<div class="bkhn" style="margin-top:12px;color:#6B4529">Đồ dùng · không tốn chỗ</div>` + hie.map(([k, n]) =>""",
    """if (hie.length) h += kDe('Đồ dùng · không tốn chỗ') + kXep(hie).map(([k, n]) =>""")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong ->', dst, len(s), 'ky tu')
