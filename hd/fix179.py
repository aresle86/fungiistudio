# -*- coding: utf-8 -*-
# v179 — kho cụp nhóm được, chợ đẩy món cần gấp lên trên (chặng 2).
#
# Anh Ares: "list thì lại rất dài ko có ux ui friendly ko có tổ chức" → "Làm chặng 2".
# v178 đã chia nhóm rồi, nhưng mở kho ra vẫn thấy đủ 45 dòng một lượt,
# và bảng Bán ngoài Chợ thì chưa đụng tới: 41 dòng, không sắp,
# món có nhãn "Chợ cần · giá ×2" nằm tuốt dòng thứ 13.
#
# Vá ba chỗ:
#   1. Sổ → Kho: mỗi nhóm thành một thanh bấm được, cụp vô xổ ra.
#      Nhóm nào trên 6 món thì lần đầu cụp sẵn, từ 6 trở xuống thì mở sẵn;
#      sau đó nhớ theo ý người chơi (ST.khoMo), lưu vô bản lưu.
#      Kho cấp 20 mở ra còn 7 thanh thay vì 45 dòng.
#   2. Chợ → Bán: thêm mục "Cần gấp" trên cùng, gom món chợ đang mua giá ×2
#      với món đang có đơn hàng chờ. Phần còn lại chia nhóm Rau · Trái · Cá ·
#      Trứng và thứ khác; gác bếp chia Đồ khô, đồ muối · Món nấu.
#   3. Chạm vô lu ngoài vườn: lưới món cũng chia nhóm, xếp theo tên.
#
# Thanh nhóm cao 44 để bấm trúng, chữ 16 đậm — tiện thể hết chìm như v178.
# Khoá nhóm của gác bếp đổi thành gkho/gmon/gkhac để không đụng khoá 'khac'
# của kho lu (hai nhóm trùng khoá thì cụp cái này tắt luôn cái kia).
import sys, io
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khớp %d lần, cần %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

# 0. số bản
rep("const BUILD = 'v178';", "const BUILD = 'v179';")

# 1. kiểu cho thanh nhóm bấm được
rep(".krow{display:grid;grid-template-columns:58px 1fr 64px;align-items:center;padding:4px 2px;border-bottom:2px dashed #E3D3BC}",
    ".krow{display:grid;grid-template-columns:58px 1fr 64px;align-items:center;padding:4px 2px;border-bottom:2px dashed #E3D3BC}\n"
    ".khnh{display:flex;align-items:center;justify-content:space-between;gap:12px;width:100%;min-height:44px;margin-top:8px;padding:8px 12px;background:#F1E6D2;border:0;border-radius:10px;font-family:var(--f-body);font-size:16px;font-weight:700;color:#6B4529;text-align:left;cursor:pointer}\n"
    ".khnh>i{display:inline-flex;align-items:center;gap:8px;font-style:normal;font-size:15px;font-weight:700;color:#8A5D3B}\n"
    ".khnh>i::after{content:\"\\25BE\"}\n"
    ".khnh.cup>i::after{content:\"\\25B8\"}")

# 2. khoá nhóm gác bếp khác khoá kho lu
rep("const gNhom = k => DISH[k] ? 'mon' : (PHOI[k] || SAY[k] || MUOI[k]) ? 'kho' : 'khac';",
    "const gNhom = k => DISH[k] ? 'gmon' : (PHOI[k] || SAY[k] || MUOI[k]) ? 'gkho' : 'gkhac';   /* khoá riêng, kẻo cụp nhóm 'khac' của kho lu là tắt luôn nhóm này */")
rep("KGB = [['kho', 'Đồ khô, đồ muối'], ['mon', 'Món nấu'], ['khac', 'Thứ khác']];",
    "KGB = [['gkho', 'Đồ khô, đồ muối'], ['gmon', 'Món nấu'], ['gkhac', 'Thứ khác']];")

# 3. kNhomHTML biết cụp, thêm kiểu tiêu đề cho bảng ngoài Chợ
rep("function kNhomHTML(L, nhom, thutu, row){ let h = ''; for (const [g, ten] of thutu){ const P = kXep(L.filter(([k]) => nhom(k) === g)); if (!P.length) continue; h += kDe(`${ten} · ${P.length}`) + P.map(row).join(''); } return h; }   /* nhóm trống thì bỏ qua, khỏi hiện tiêu đề rỗng */",
    "const kSub = t => `<div class=\"sub\">${t}</div>`;\n"
    "const kMo = (g, n) => { const M = ST.khoMo || {}; return g in M ? !!M[g] : n <= 6; };   /* lần đầu: nhóm trên 6 món thì cụp sẵn; sau đó nhớ theo ý người chơi */\n"
    "function kNhomHTML(L, nhom, thutu, row, cup, de){ de = de || kDe; let h = '';\n"
    "  for (const [g, ten] of thutu){ const P = kXep(L.filter(([k]) => nhom(k) === g)); if (!P.length) continue;\n"
    "    if (!cup){ h += de(`${ten} · ${P.length}`) + P.map(row).join(''); continue; }\n"
    "    const on = kMo(g, P.length);\n"
    "    h += `<button class=\"khnh${on ? '' : ' cup'}\" data-b=\"khonhom\" data-k=\"${g}\" data-o=\"${on ? 1 : 0}\" aria-expanded=\"${on}\"><span>${ten}</span><i>${P.length}</i></button>` + (on ? P.map(row).join('') : ''); }\n"
    "  return h; }   /* nhóm trống thì bỏ qua, khỏi hiện tiêu đề rỗng */")

# 4. bảng Kho trong Sổ: cụp được, kể cả bao hạt với đồ dùng
rep("""  h += items.length ? kNhomHTML(items, kNhom, KLU, ([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${kTen(k)}</span><span class="q">${n}</span></div>`) : '<div class="bkhn">Kho trống trơn. Hái rau xong là có hàng đem bán.</div>';""",
    """  h += items.length ? kNhomHTML(items, kNhom, KLU, ([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${kTen(k)}</span><span class="q">${n}</span></div>`, 1) : '<div class="bkhn">Kho trống trơn. Hái rau xong là có hàng đem bán.</div>';""")

rep("""if (seeds.length) h += kDe(`Bao hạt trong túi · ${seeds.length}`) + kXep(seeds).map(([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt="" style="filter:drop-shadow(2px 0 0 #fff) drop-shadow(-2px 0 0 #fff)"><span class="n">Hạt ${CROPS[k].name.toLowerCase()}</span><span class="q" style="color:#4F7D44">${n}</span></div>`).join('');""",
    """if (seeds.length) h += kNhomHTML(seeds, () => 'hat', [['hat', 'Bao hạt trong túi']], ([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt="" style="filter:drop-shadow(2px 0 0 #fff) drop-shadow(-2px 0 0 #fff)"><span class="n">Hạt ${CROPS[k].name.toLowerCase()}</span><span class="q" style="color:#4F7D44">${n}</span></div>`, 1);""")

rep("""if (gbi.length) h += kDe(`Gác bếp · ${gbUsed()}/${GB_CAP}`) + kNhomHTML(gbi, gNhom, KGB, ([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${kTen(k)}</span><span class="q" style="color:#9A6E12">${n}</span></div>`);""",
    """if (gbi.length) h += kDe(`Gác bếp · ${gbUsed()}/${GB_CAP}`) + kNhomHTML(gbi, gNhom, KGB, ([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${kTen(k)}</span><span class="q" style="color:#9A6E12">${n}</span></div>`, 1);""")

rep("""if (hie.length) h += kDe('Đồ dùng · không tốn chỗ') + kXep(hie).map(([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${k === 'cui' ? `Củi · ${n}/${CUI_CAP}` : (GD(k) || { name: k }).name}</span><span class="q" style="color:#9A6E12">${n}</span></div>`).join('');""",
    """if (hie.length) h += kNhomHTML(hie, () => 'dung', [['dung', 'Đồ dùng · không tốn chỗ']], ([k, n]) => `<div class="krow"><img src="${ICON[k]}" alt=""><span class="n">${k === 'cui' ? `Củi · ${n}/${CUI_CAP}` : (GD(k) || { name: k }).name}</span><span class="q" style="color:#9A6E12">${n}</span></div>`, 1);""")

# 5. bấm vô thanh nhóm thì cụp hay xổ, nhớ luôn
rep("  else if (a === 'quest'){ doQuest(+k); }",
    "  else if (a === 'khonhom'){ ST.khoMo = ST.khoMo || {}; ST.khoMo[k] = b.dataset.o === '1' ? 0 : 1; save(); }   /* nhớ nhóm nào đang mở, lần sau vô kho y vậy */\n"
    "  else if (a === 'quest'){ doQuest(+k); }")

# 6. chạm vô lu ngoài vườn: lưới cũng chia nhóm
rep("""    h += items.length ? '<div class="grid">' + items.map(([k, n]) => `<div class="it"><img src="${ICON[k]}" alt=""><b>${k === 'rom' ? 'Rơm' : GD(k).name}</b><span>${n} ${k === 'rom' ? 'bó' : GD(k).unit}</span></div>`).join('') + '</div>' : '<div class="note">Kho trống. Hái rau xong là có hàng đem bán.</div>';""",
    """    const kTile = ([k, n]) => `<div class="it"><img src="${ICON[k]}" alt=""><b>${kTen(k)}</b><span>${n} ${k === 'rom' ? 'bó' : GD(k).unit}</span></div>`;
    h += items.length ? KLU.map(([g, ten]) => { const P = kXep(items.filter(([k]) => kNhom(k) === g)); return P.length ? `<div class="sub">${ten} · ${P.length}</div><div class="grid">` + P.map(kTile).join('') + '</div>' : ''; }).join('') : '<div class="note">Kho trống. Hái rau xong là có hàng đem bán.</div>';""")

# 7. bảng Bán ngoài Chợ: món cần gấp lên trên, còn lại chia nhóm
rep("""      h += items.map(([k, n]) => { const c = GD(k), pr = priceNow(k), sold = mkDay().s[k] || 0, left = MK.n - sold % MK.n, low = pr < c.sell; return `<div class="srow">""",
    """      const ordCan2 = k => { try { const L = (ST.ord && ST.ord.list || []).slice(); if (gheOn() && ST.ghe.o) L.push(ST.ghe.o); return L.some(o => (o.items || []).some(([x]) => x === k)); } catch (e) { return false; } };
      const canGap = k => mkcLeft(k) > 0 || ordCan2(k);
      const srow = ([k, n]) => { const c = GD(k), pr = priceNow(k), sold = mkDay().s[k] || 0, left = MK.n - sold % MK.n, low = pr < c.sell; return `<div class="srow">""")

rep("""<button class="btn g sall" data-a="sellall" data-k="${k}">Bán hết<small>+${sellValue(k, n)} xu</small></button></div>`; }).join(''); }
    const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && (DISH[k] || PHOI[k] || MUOI[k] || SAY[k])); if (gbi.length) h += '<div class="sub">Gác bếp</div>' + gbi.map(([k, n]) => {""",
    """<button class="btn g sall" data-a="sellall" data-k="${k}">Bán hết<small>+${sellValue(k, n)} xu</small></button></div>`; };
      const gap = kXep(items.filter(([k]) => canGap(k))), con = items.filter(([k]) => !canGap(k));
      if (gap.length) h += `<div class="sub">Cần gấp · ${gap.length}</div>` + gap.map(srow).join('');   /* chợ đang mua giá ×2, hay đang có đơn chờ món đó */
      h += kNhomHTML(con, kNhom, KLU, srow, 0, kSub); }
    const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && (DISH[k] || PHOI[k] || MUOI[k] || SAY[k])); if (gbi.length) h += '<div class="sub">Gác bếp</div>' + kNhomHTML(gbi, gNhom, KGB, ([k, n]) => {""")

rep("""<button class="btn g sall" data-a="sellall" data-k="${k}">Bán hết<small>+${sellValue(k, n)} xu</small></button></div>`; }).join('');
    }""",
    """<button class="btn g sall" data-a="sellall" data-k="${k}">Bán hết<small>+${sellValue(k, n)} xu</small></button></div>`; }, 0, kSub);
    }""")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong ->', dst, len(s), 'ky tu')
