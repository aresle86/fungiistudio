# -*- coding: utf-8 -*-
# v123c sau v123b: hai kho cho rõ. Kho lu (rau, trái, trứng, cá) và Gác bếp (đồ khô, món nấu)
# hiện thành hai thẻ có thanh + nút nâng ở tab Bán của chợ và trang Sức chứa trong Sổ.
# Muối, đường thành đồ dùng, không tốn chỗ gác bếp. Gác bếp nâng được 5 kệ (20 -> 70).
import re, sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()

def rep(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:80])
    s = s.replace(a, b)

rep("BUILD = 'v123b'", "BUILD = 'v123c'")

# muối, đường: đồ dùng; 5 kệ
rep("const GBX_MAX = 3,", "const GBX_MAX = 5,")
rep("HIEN = { lucbinh: 1, lucbinhkho: 1, gio: 1, cui: 1 }", "HIEN = { lucbinh: 1, lucbinhkho: 1, gio: 1, cui: 1, muoi: 1, duong: 1 }")

# thẻ hai kho dùng chung
rep("function pgKho(full = true){", """function khoHTML(at){ const ku = kUsed(), kc = kCap(), gu = gbUsed(), gc = GB_CAP, gx = (ST.gbx || 0) < GBX_MAX;
  const card = (img, t, sub, u, c, btn) => `<div class="khoc${u >= c ? ' full' : ''}"><div class="khd"><img src="${img}" alt=""><div><b>${t}</b><span>${sub}</span></div></div><div class="kbot"><div class="kn">${u}<small>/${c}</small>${u >= c ? '<em>đầy rồi</em>' : ''}</div><div class="kbar"><i style="width:${Math.round(c01(u / c) * 100)}%"></i></div>${btn}</div></div>`;
  return `<div class="khos">${card(UIC.lu || ICON.kho, 'Kho lu', 'rau, trái, trứng, cá', ku, kc, `<button class="btn kup" data-${at}="${at === 'a' ? 'buylu' : 'lu'}" ${ST.xu < luCost() ? 'disabled' : ''}><span>Thêm lu</span><small>${luCost()} xu</small></button>`)}${card(ICON.otkho || ICON.kho, 'Gác bếp', 'đồ khô, món nấu', gu, gc, gx ? `<button class="btn kup" data-${at}="gbx" ${ST.xu < gbxCost() ? 'disabled' : ''}><span>Thêm kệ</span><small>${gbxCost()} xu</small></button>` : '<div class="kmax">Đủ kệ rồi</div>')}</div>`; }   /* hai kho: lu và gác bếp, mỗi kho một thanh, nút nâng ngay dưới */
function pgKho(full = true){""")

# chợ, tab Bán: luôn có hai thẻ kho ở đầu, bỏ thẻ đầu bảng "Kho x/y chỗ" (trùng với thẻ Kho lu)
rep("if (SHEET.tab === 'ban') h += UX.hero(UIC.lu || ICON.kho, `Kho ${u}/${cp} chỗ`, items.length ? `Bán hết được chừng ${tot} xu` : 'Kho chưa có gì để bán', u >= cp ? 'warn' : '', [u / cp, u >= cp ? '#F08A6E' : '#EDB940']);", '')
rep("if (kUsed() >= kCap() * .9) h += LUROW.replace('margin-top:12px', 'margin-top:8px;box-shadow:0 0 0 2px #F08A6E');", "h += khoHTML('a');")
rep("else if (a === 'buylu'){", "else if (a === 'gbx'){ const c = gbxCost(); if ((ST.gbx || 0) < GBX_MAX && ST.xu >= c){ ST.xu -= c; ST.gbx = (ST.gbx || 0) + 1; GB_CAP = 20 + 10 * ST.gbx; save(); hud(); buyFx(b, ICON.otkho || ICON.kho, `Gác bếp chứa được ${GB_CAP} món`, c); } }\n  else if (a === 'buylu'){")

# Sổ: bỏ nút kệ lẻ trong danh sách, đổi tên chái bếp, trang Sức chứa hiện cả hai kho
rep("""  if (gbi.length && (ST.gbx || 0) < GBX_MAX) h += `<div class="acts"><button class="btn" data-b="gbx" ${ST.xu < gbxCost() ? 'disabled' : ''}>Thêm kệ gác bếp · ${gbxCost()} xu</button></div><div class="bkhn" style="font-size:17px;color:#8A5D3B">Mỗi kệ tre chứa thêm 10 món khô, món nấu.</div>`;
""", "")
rep("Chái bếp, dưới hiên</div>", "Đồ dùng · không tốn chỗ</div>")
m = re.search(r"function pgKhoCap\(head\)\{.*?\n(?=const BSTK)", s, re.S)
assert m
s = s[:m.start()] + """function pgKhoCap(head){ let h = head ? '<div class="bkhn" style="color:#6B4529;margin-top:0">Sức chứa</div>' : '<div style="height:14px"></div>';
  return h + `<div class="acts"><button class="btn g" data-b="cho">Đem ra chợ</button></div><div class="bkhn" style="font-size:17px;color:#8A5D3B">Mỗi lu chứa thêm ${LU_CAP} món tươi. Mỗi kệ tre chứa thêm 10 món khô, món nấu. Kho nào đầy thì món đó không cất được nữa.</div>` + (head ? `<img class="bkng" src="${NGOAI.ex_vui}" alt="">` : ''); }
""" + s[m.end():]

rep("let h = hdr('kho') + '<div style=\"margin-top:10px\">';", "let h = hdr('kho') + '<div style=\"margin-top:10px\">' + khoHTML('b');")

# Mở rộng: bảng lò sấy, nong, khạp chỉ chỗ mua thêm (nâng tầng, rồi bộ thứ hai). Chỉ hiện khi đã tới cấp mua được.
rep("""const upxHTML = k => { const U = UPX[k], O = ST[k], arr = k === 'nong' ? O.trays : O.jars; if (arr.length >= U.full) return ''; return UX.title('Mở rộng') + '<div class="upg">' + ((ST.lv || 1) >= U.lv ? UX.upc('upx', ICON[k], U.name, U.xu, { k, dis: ST.xu < U.xu }) : '') + '</div>'; };""",
    """const upxHTML = k => { const U = UPX[k], O = ST[k], arr = k === 'khap' ? O.jars : O.trays; let c = ''; if (U && arr.length < U.full && (ST.lv || 1) >= U.lv) c += UX.upc('upx', ICON[k], U.name, U.xu, { k, dis: ST.xu < U.xu });
  const k2 = k + '2', D2 = OBJD[k2]; if (D2 && ST[k2] && !ST[k2].own && objOn(k2)) c += UX.upc('obuy', ICON[k2], D2.title, D2.buy, { k: k2, dis: ST.xu < D2.buy }); return c ? UX.title('Mở rộng') + '<div class="upg">' + c + '</div>' : ''; };   /* nâng tại chỗ, rồi mua bộ thứ hai đặt trên ô đất trống */""")
rep("""h += '<div class="slots">' + L.trays.map((t, i) => UX.slot(i, t, SAYR, 'spick', 'stake', 'Khay', 'Sấy xong · chạm lấy')).join('') + '</div>';""",
    """h += '<div class="slots">' + L.trays.map((t, i) => UX.slot(i, t, SAYR, 'spick', 'stake', 'Khay', 'Sấy xong · chạm lấy')).join('') + '</div>';""")
rep("return h + UX.more('Cách sấy'", "return h + upxHTML('say') + UX.more('Cách sấy'")

# CSS: thẻ trạng thái giấy sẫm, thanh S, nút phụ
rep(".ordr{display:grid;", ".khos{display:grid;grid-template-columns:1fr 1fr;gap:8px;margin:4px 0 10px}.khoc{background:#F6EBD3;border:2px solid #E3C9A6;border-radius:16px;padding:10px;display:flex;flex-direction:column;gap:6px;min-width:0}.khoc.full{border-color:#F08A6E;background:#FFF1EA}.khoc .khd{display:flex;align-items:center;gap:8px;min-width:0}.khoc .khd img{width:34px;height:34px;object-fit:contain;flex:none}.khoc .khd b{display:block;font-family:var(--f-game);font-size:17px;color:#4A2F1E;line-height:1.1}.khoc .khd span{display:block;font-family:var(--f-body)!important;font-size:12px;font-weight:600;color:#8A5D3B;line-height:1.25}.khoc .kn{display:flex;align-items:baseline;gap:2px;font-family:var(--f-game);font-size:22px;color:#4A2F1E;line-height:1}.khoc .kn small{font-size:14px;color:#8A5D3B}.khoc .kn em{margin-left:auto;font-style:normal;font-size:12px;color:#C4502F}.khoc .kbar{margin-bottom:4px;height:10px;border-radius:6px;background:#6B4529;border:2px solid #4A2F1E;box-sizing:border-box;overflow:hidden}.khoc .kbar i{display:block;height:100%;border-radius:4px;background:#F2C64A}.khoc.full .kbar i{background:#F08A6E}.khoc .btn.kup{width:100%;height:44px!important;min-height:0!important;margin:2px 0 0!important;padding:0 10px!important;box-sizing:border-box;display:flex;align-items:center;justify-content:space-between;gap:6px;padding:0 10px;font-size:15px!important;white-space:nowrap}.khoc .btn.kup span{white-space:nowrap}.khoc .btn.kup small{font-size:12px!important;opacity:.75;font-family:inherit;white-space:nowrap}.khoc .khd span{font-size:12px!important}.khoc .khd b{font-size:17px!important}.khoc .kmax{font-size:13px!important}#bk .khoc{padding:8px}#bk .khoc .khd img{width:28px;height:28px}#bk .khoc .btn.kup{font-size:14px!important;padding:0 8px!important;gap:4px}#bk .khoc .btn.kup small{font-size:11px!important}.khoc .kbot{margin-top:auto;display:flex;flex-direction:column;gap:6px}.khoc .kmax{height:44px;margin-top:2px;box-sizing:border-box;border:2px dashed #E3C9A6;border-radius:10px;display:flex;align-items:center;justify-content:center;font-size:13px;font-weight:700;color:#8A5D3B}.ordr{display:grid;")

# tiếng Anh
rep('"Chái bếp, dưới hiên": "Kitchen shed, porch", ', '"Chái bếp, dưới hiên": "Kitchen shed, porch", "Đồ dùng · không tốn chỗ": "Supplies · take no space", "Kho lu": "Storage jars", "rau, trái, trứng, cá": "veg, fruit, eggs, fish", "đồ khô, món nấu": "dried goods, dishes", "Thêm lu": "Add a jar", "Thêm kệ": "Add a shelf", "Đủ kệ rồi": "All shelves built", "đầy rồi": "full", ')
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
