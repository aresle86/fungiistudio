# NHÁP v156: mặc cả ông Bảy đổi từ giữ ngón sang trả giá qua lại (Ares: giữ ngón không trực quan).
# Mỗi lần bấm "Thêm chút nữa" giá lên một nấc 8%, tối đa 5 nấc (+40%). Ông chịu tới nấc nào tính từ ngưỡng ẩn 15 tới 35%
# của ngày đó (mối quen +5%). Ông lau kiếng là báo sắp hết chịu: một nửa số ngày còn bấm thêm được đúng một nấc.
# Bấm quá thì vẫn được +5%.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
def cut(a, b, new):
    global s
    assert s.count(a) == 1 and s.count(b) == 1, (s.count(a), s.count(b), a[:60])
    i, j = s.index(a), s.index(b); assert i < j
    s = s[:i] + new + s[j:]
rep("BUILD = 'v155'", "BUILD = 'v156'")
rep("B.ml = [d, +(K.lo + Math.random() * (K.hi - K.lo)).toFixed(3)];", "B.ml = [d, +(K.lo + Math.random() * (K.hi - K.lo)).toFixed(3), Math.random() < .5 ? 1 : 0];")
cut("function bayMcHTML(k){", "function bayAct(a, b){",
    "function mcOk(){ return Math.max(1, Math.min(5, Math.floor(mcLim() * 100 / 8 + 1e-6))); }\n"
    "function mcLau(n){ return n >= mcOk() - ((bayS().ml || [])[2] || 0); }\n"
    "function bayMcHTML(k){ const S = SHEET.bay, n = S.mcn || 0, p0 = bayPrice(k, 0), p = Math.round(p0 * (1 + n * .08)); let pic = ''; try { pic = bayArt().pic(mcLau(n) ? 'lau' : 'xem'); } catch (e) {}\n"
    "  return `<div class=\"bayh\"><img src=\"${pic}\" alt=\"\"><div class=\"bayq\">${S.line}</div></div>` + UX.title('Mặc cả', mcQuen() ? 'Mối quen' : '')\n"
    "    + `<div class=\"qset\"><img src=\"${ICON[k]}\" alt=\"\"><div><b>${bayName(k)} · ${bayN(k)}</b><span>${L135('Giá đầu ' + p0 + ' xu một ' + bayU(k), 'Opening price ' + p0 + ' coins each')}</span></div></div>`\n"
    "    + `<div class=\"mcp\"><b>${p} xu</b><span>${n ? L135('thêm ' + n * 8 + '%', '+' + n * 8 + '%') : L135('ông Bảy ra giá', 'his offer')}</span></div>`\n"
    "    + '<div class=\"mcd\">' + [0, 1, 2, 3, 4].map(i => `<i${i < n ? ' class=\"on\"' : ''}></i>`).join('') + '</div>'\n"
    "    + UX.cta([UX.btn('baymcok', n ? 'Chịu giá' : 'Thôi, để sau'), UX.btn('baymcup', 'Thêm chút nữa', { g: 1 })]); }\n"
    "function mcDone(S, B, k, n){ delete S.mc; S.mcn = 0; B.th[k] = +(1 + n * .08).toFixed(2); S.pose = 'xem'; S.line = L135(`Ừa, hàng đẹp vậy thì qua trả thêm ${n * 8}% cho cháu.`, `All right, goods this fine, I will pay ${n * 8}% more.`); try { sfx('up'); buzz(18); } catch (e) {} }\n")
rep("S.mc = k; S.pose = 'xem';", "S.mc = k; S.mcn = 0; S.pose = 'xem';")
cut("else if (a === 'baymcx'){", "else if (a === 'bayban'){",
    "else if (a === 'baymcup'){ const m = S.mc; if (!m || B.th[m] != null) return; const n = (S.mcn || 0) + 1;\n"
    "    if (n > mcOk()){ delete S.mc; S.mcn = 0; B.th[m] = mcK().over; S.pose = 'kha'; S.line = L135('Khà khà, cháu hét giá quá tay rồi. Thôi qua thêm chút đỉnh lấy thảo.', 'Ha ha, you pushed too far. Fine, a little extra for goodwill.'); try { sfx('pick'); buzz(30); } catch (e) {} }\n"
    "    else if (n >= 5) mcDone(S, B, m, n);\n"
    "    else { S.mcn = n; S.line = mcTxt(mcLau(n) ? 1 : 0); try { sfx('pick'); buzz(12); } catch (e) {} } }\n"
    "  else if (a === 'baymcok'){ const m = S.mc, n = S.mcn || 0; if (m && n && B.th[m] == null) mcDone(S, B, m, n); else { delete S.mc; S.mcn = 0; S.pose = 'xem'; S.line = 'Ừa, chừng nào muốn thì nói qua.'; try { sfx('pick'); } catch (e) {} } }\n"
    "  ")
cut("/* v155: giữ nút mặc cả */", "/* hết xu, hết hạt, vườn trống: Ngoại cho hạt, mỗi ngày một lần */", "")
rep('"Mặc cả": "Haggle",', '"Mặc cả": "Haggle", "Thêm chút nữa": "A bit more", "Chịu giá": "Deal",')
cut(".mcm{height:16px;", ".mch{touch-action:none;", 
    ".mcp{text-align:center;margin:0 0 8px}.mcp b{display:block;font:400 32px/1.2 var(--f-game);color:#4A2F1E;animation:mcpop .28s ease-out}.mcp span{display:block;font:600 12px/1.4 var(--f-body);color:#8A6A4A}\n"
    ".mcd{display:flex;justify-content:center;gap:8px;margin:0 0 16px}.mcd i{width:24px;height:8px;border-radius:999px;background:#EADFC8;box-shadow:inset 0 0 0 2px #E3C9A6}.mcd i.on{background:#E0803A;box-shadow:none}\n"
    "@keyframes mcpop{0%{transform:scale(.8)}60%{transform:scale(1.12)}100%{transform:scale(1)}}@media (prefers-reduced-motion:reduce){.mcp b{animation:none}}\n")
rep(".mch{touch-action:none;-webkit-user-select:none;user-select:none;-webkit-touch-callout:none}.mch.ing{transform:translateY(3px);box-shadow:0 1px 0 var(--woodD)}", "")
open(DST, 'w', encoding='utf-8').write(s); print('ok', len(s))
