# v139: sửa theo hình anh Ares 11/11 (chơi thật trên iPhone, cấp 10).
# (1) Chấm "Mới" ở nút Hạt / Chợ: cờ Mới nằm chung ST.moi với mồi câu (mồi "sâu" bắt đầu bằng s nên nút Hạt sáng hoài).
#     Dời cờ Mới qua ST.mn, chuyển cờ cũ sang. Chấm tròn lạc ra mép nút đổi thành nhãn chữ "Mới" ngay góc hình nút.
# (2) Thẻ Ngoại nhờ: thanh tối không chữ (số 9px) và hai chấm không nghĩa -> thanh sáng + số đọc được + "Bước 2/2".
#     Việc hôm nay xong hết và đã nhận quà thì thẻ co lại, bỏ dòng "Việc hôm nay" (nút Sổ đã có dấu ✓).
# (3) Hàng tab Chợ không xuống dòng ("Đơn hàng", "Trang trí" bị gãy hai dòng trên iPhone).
# (4) Chậu mai chiếu thủy: mặt đất trong chậu trùng mặt miệng chậu (cùng 0,26) nên nhấp nháy -> nâng đất lên chút.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v138'", "BUILD = 'v139'")

# (1) cờ Mới tách khỏi mồi câu
a = s.index('function moiTag'); b = s.index('setTimeout(moiDots, 1200);')
seg = s[a:b]; assert seg.count('ST.moi') == 12
seg = seg.replace('ST.moi', 'ST.mn')
seg = seg.replace("function moiDots(){ try { const a = $('#tSeed'), b = $('#bCho'); if (a) a.classList.toggle('moi', moiN('s') > 0); if (b) b.classList.toggle('moi', moiN('d') > 0 && dcOn()); } catch (e) {} }",
                  "function moiDots(){ try { const a = $('#tSeed'), b = $('#bCho'), t = L135('Mới', 'New'); if (a){ a.classList.toggle('moi', moiN('s') > 0); a.dataset.mn = t; } if (b){ b.classList.toggle('moi', moiN('d') > 0 && dcOn()); b.dataset.mn = t; } } catch (e) {} }")
assert "a.dataset.mn = t" in seg
seg = seg.replace("function moiN(p){ try { return Object.keys(ST.mn || {}).filter(k => k[0] === p).length; }", "function moiN(p){ try { return Object.keys(ST.mn || {}).filter(k => k.startsWith(p + '_')).length; }")
assert "k.startsWith(p + '_')" in seg
s = s[:a] + seg + "try { if (ST.moi) for (const k of Object.keys(ST.moi)) if (/^[sd]_/.test(k)){ (ST.mn = ST.mn || {})[k] = 1; delete ST.moi[k]; } } catch (e) {}\n" + s[b:]
rep("#bCho.moi::after{right:2px;top:2px}",
    "#bCho.moi::after{right:2px;top:2px}\n#tSeed.moi::after,#bCho.moi::after{content:attr(data-mn);width:auto;height:auto;left:auto;right:0;top:-6px;padding:1px 7px;font:800 12px/1.3 var(--f-body,'Baloo 2'),sans-serif;color:#fff;border-radius:999px;white-space:nowrap}")

# (2) thẻ Ngoại nhờ
rep("const barH = (f2, em2) => `<span class=\"bar\"><i style=\"width:${Math.round(Math.max(0, Math.min(1, f2)) * 100)}%\"></i><em>${em2}</em></span>`;",
    "const barH = (f2, em2) => `<span class=\"pbar\"><span class=\"bar\"><i style=\"width:${Math.round(Math.max(0, Math.min(1, f2)) * 100)}%\"></i></span><em>${em2}</em></span>`;")
rep("const steps = q && q.t === 'goal' && lab === 'NGOẠI NHỜ' && q.goals.length > 1 ? `<span class=\"steps\">${q.goals.map(([, f2, nn]) => `<i class=\"${f2() >= nn ? 'on' : ''}\"></i>`).join('')}</span>` : '';",
    "const steps = q && q.t === 'goal' && lab === 'NGOẠI NHỜ' && q.goals.length > 1 ? `<span class=\"stp\">${L135('Bước', 'Step')} ${Math.min(q.goals.length, q.goals.filter(([, f2, nn]) => f2() >= nn).length + 1)}/${q.goals.length}</span>` : '';")
rep("foot = `<span class=\"nqd2${gift ? ' gift' : ''}\" data-d=\"1\">Việc hôm nay ${dn}/${L3.length}${gift ? ' · có quà nhận' : ''} ›</span>`;",
    "foot = dn >= L3.length && !gift ? '' : `<span class=\"nqd2${gift ? ' gift' : ''}\" data-d=\"1\">Việc hôm nay ${dn}/${L3.length}${gift ? ' · có quà nhận' : ''} ›</span>`;")
rep(".nxq .nqd2.gift{color:#9A6E12}",
    ".nxq .nqd2.gift{color:#9A6E12}\n.nxq .nqd2.alld{color:#4F7D44;font-weight:700}"
    ".nxq .pbar{display:flex;align-items:center;gap:6px;margin-top:3px;width:100%}"
    ".nxq .pbar .bar{flex:1;position:relative;height:8px!important;min-width:40px;background:#EADBB8!important;border:0!important;border-radius:5px!important;overflow:hidden}"
    ".nxq .pbar .bar i{background:linear-gradient(#FFE27A,#E8B830)!important;border-radius:5px!important}"
    ".nxq .pbar>em{font:700 12px/1 var(--f-body,'Baloo 2'),sans-serif;font-style:normal;color:#6B4529;white-space:nowrap;text-shadow:none}"
    ".nxq .q .stp{display:block;margin-top:3px;font:700 12px/1.1 var(--f-body,'Baloo 2'),sans-serif;color:#8A5D3B}")

# (3) tab Chợ một dòng
rep(".sg{min-height:44px}", ".sg{min-height:44px}\n.seg .sg{white-space:nowrap;min-width:0;padding:0 4px;gap:4px}@media (max-width:430px){.seg .sg{font-size:14px}.seg .sg i{min-width:18px;padding:1px 5px}}")

# (4) chậu mai chiếu thủy hết nhấp nháy
rep("M(cyl(.22, .22, .02, 12), '#4A2F1E', 0, .25, 0);", "M(cyl(.22, .22, .02, 12), '#4A2F1E', 0, .257, 0);")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
