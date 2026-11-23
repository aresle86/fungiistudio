# -*- coding: utf-8 -*-
# v182 — bảng ao cá nói ra cái lợi, thay vì giấu.
#
# Anh Ares: "t vẫn ko hiểu có sẵn cá thả xuống miễn phí thì người chơi đc lợi gì?"
#
# Cái lợi CÓ THẬT, đọc từ `aoLuoi()`:
#   - đủ số cá đã thả, cộng thêm 1 con cho mỗi 2 con (`de = floor(ok.length / 2)`)
#   - 2 bó lục bình mỗi ngày (nếu tới cấp, và hôm nay chưa vớt)
#   - 1 phần bùn ao bỏ hố ủ (nếu có hố ủ)
#   - 2 kinh nghiệm mỗi con
#   Một mẻ 24 giờ. Thả miễn phí nếu cá có sẵn trong kho.
#   Ao nhỏ 6 con, ao vừa 10, ao lớn 15.
#   Ao vừa đầy cá tra lớn: thả 10 được 15, lời 700 xu một ngày.
#
# Gốc lỗi là CHỮ, không phải luật. Bảng có hai câu:
#   - ao trống : "...Cứ hai con nuôi lớn thì cá đẻ thêm một con." → có nói cái lợi
#   - đang nuôi: "Mẻ đầu lớn sau X. Lớn rồi kéo lưới về kho, cùng món cùng giá
#                 với cá câu." → MẤT SẠCH phần cá đẻ, lại thêm vế "cùng món cùng
#                 giá với cá câu" nghe như thả vô chẳng được gì.
# Thả cá vô một con là từ đó không còn chỗ nào nói vì sao nên thả.
# Lục bình, bùn ao, kinh nghiệm thì cả bảng không nhắc, chỉ hiện trong lời
# báo sau khi đã kéo lưới xong.
#
# Vá: tính thẳng con số theo số cá đang có, khỏi bắt người chơi nhẩm.
#   - đang nuôi    : "Mẻ đầu lớn sau X. Nuôi đủ một ngày thì kéo lưới được 6 con
#                     — 4 con nuôi với 2 con cá đẻ. Vớt thêm 2 bó lục bình với
#                     một phần bùn ao bỏ hố ủ."
#   - cá lớn rồi   : thêm một dòng y vậy ngay dưới nút Kéo lưới.
#   - ao dưới 2 con: nói thẳng "cứ hai con nuôi lớn mới có thêm một con cá đẻ",
#                    khỏi ghi "0 con cá đẻ" nghe kỳ.
#   - lục bình với bùn ao chỉ ghi khi thiệt sự được: đúng cấp, hôm nay chưa vớt,
#     và có hố ủ. Không hứa cái người chơi chưa có.
#
# Không đụng tới xu, số cá, thời gian. Chỉ là chữ trên bảng.
import sys, io
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khớp %d lần, cần %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

# 0. số bản
rep("const BUILD = 'v181';", "const BUILD = 'v182';")

# 1. hai câu phụ: tính số cá kéo lên được, và kể thêm lục bình với bùn ao
rep("function aoHTML(){ const B = ST.big.ao, tier = aoTier(),",
    "const aoLoi = n => { const de = Math.floor(n / 2); return de ? L135(`${n + de} con — ${n} con nuôi với ${de} con cá đẻ`, `${n + de} fish — ${n} raised plus ${de} young`) : L135(`${n} con · cứ hai con nuôi lớn mới có thêm một con cá đẻ`, `${n} fish · every two raised give one extra young`); };\n"
    "const aoThem = () => { const B = ST.big.ao || {}, t = [], e = []; try { if ((ST.lv || 1) >= oddDefs().lucbinh.lv && B.lbd !== dayKey()){ t.push('2 bó lục bình'); e.push('2 bundles of water hyacinth'); } } catch (err) {} if (ST.ho){ t.push('một phần bùn ao bỏ hố ủ'); e.push('a scoop of pond mud for the compost pit'); } return t.length ? L135(` Vớt thêm ${t.join(' với ')}.`, ` Also scooping ${e.join(' and ')}.`) : ''; };   /* chỉ hứa cái thiệt sự được: đúng cấp, hôm nay chưa vớt, và có hố ủ */\n"
    "function aoHTML(){ const B = ST.big.ao, tier = aoTier(),")

rep("if (rd) h += UX.cta([UX.btn('aoluoi', `Kéo lưới · ${rd} con`, { g: 1, img: ICON.caro })]); else if (nu.length){ const l = Math.max(0, Math.min(...nu.map(f => AONUOI / (ST.spd || 1) - (Date.now() - f.t)))); h += `<div class=\"note\">Mẻ đầu lớn sau ${fmtT(Math.ceil(l / 1000))}. Lớn rồi kéo lưới về kho, cùng món cùng giá với cá câu.</div>`; }",
    "if (rd){ h += UX.cta([UX.btn('aoluoi', `Kéo lưới · ${rd} con`, { g: 1, img: ICON.caro })]); h += `<div class=\"note\">${L135(`Cá lớn rồi, kéo lưới được ${aoLoi(rd)}.`, `Fish are grown; the net brings ${aoLoi(rd)}.`)}${aoThem()}</div>`; } else if (nu.length){ const l = Math.max(0, Math.min(...nu.map(f => AONUOI / (ST.spd || 1) - (Date.now() - f.t)))); h += `<div class=\"note\">${L135(`Mẻ đầu lớn sau ${fmtT(Math.ceil(l / 1000))}. Nuôi đủ một ngày thì kéo lưới được ${aoLoi(nu.length)}.`, `First batch grown in ${fmtT(Math.ceil(l / 1000))}. Raise them a full day and the net brings ${aoLoi(nu.length)}.`)}${aoThem()}</div>`; }")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong ->', dst, len(s), 'ky tu')
