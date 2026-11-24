# -*- coding: utf-8 -*-
# v184: tre trăm đốt lớn rồi thì giàn (khổ qua / bầu / mướp) mỗi đợt thêm một trái
import io, sys
src, dst = sys.argv[1], sys.argv[2]
s = io.open(src, encoding='utf-8').read()

def rep(a, b, n=1):
    global s
    c = s.count(a)
    assert c == n, 'khop %d lan, can %d: %s' % (c, n, a[:90])
    s = s.replace(a, b)

rep("const BUILD = 'v183'", "const BUILD = 'v184'")

# 1. hai hàm phụ: tre trăm đốt đã lớn chưa, và giàn được thêm mấy trái
rep("const harvestN = p => { const c = CROPS[p.crop]; return Math.max(1, Math.round(c.yield * (.55 + .45 * p.soil) * (p.mulch > ST.gt ? 1.1 : 1) * Math.max(.7, 1 - (p.wiltT || 0) / 21600 * .3))); };",
    "function ttUp(){ const F = (ST.ft || {}).tretramdot; return !!(F && F.st >= 3 && F.told >= 3 && !VISIT); }   /* tre trăm đốt lớn hẳn chưa */\n"
    "function ttGi(c){ return c && c.kind === 'trellis' && ttUp() ? 1 : 0; }   /* lớn rồi thì giàn mỗi đợt thêm một trái */\n"
    "const harvestN = p => { const c = CROPS[p.crop]; return Math.max(1, Math.round(c.yield * (.55 + .45 * p.soil) * (p.mulch > ST.gt ? 1.1 : 1) * Math.max(.7, 1 - (p.wiltT || 0) / 21600 * .3))) + ttGi(c); };")

# 2. hái giàn thì nổi chữ cho thấy ai cho thêm
rep("floatAt(PV[id].cx, CROPS[p.crop].h * .6, PV[id].cz, '+' + n + ' ' + c.unit + ' ' + c.name.toLowerCase());",
    "floatAt(PV[id].cx, CROPS[p.crop].h * .6, PV[id].cz, '+' + n + ' ' + c.unit + ' ' + c.name.toLowerCase());\n"
    "    if (ttGi(c)){ const vT = PV[id], hT = c.h; setTimeout(() => floatAt(vT.cx, hT * .6 + .55, vT.cz, 'Tre trăm đốt · thêm 1 ' + c.unit, '#CFE8A0'), 700); }   /* khắc nhập: giàn ra thêm một trái */")

# 3. con số trong Sổ cây trái phải khớp cái hái được
rep("const yS = c => c.tree ? c.yield + '/vụ' : c.cuts > 1 ? c.yield + '×' + c.cuts : c.yield;",
    "const yS = c => c.tree ? c.yield + '/vụ' : c.cuts > 1 ? (c.yield + ttGi(c)) + '×' + c.cuts : c.yield + ttGi(c);")

rep("Hái ${c.cuts} đợt, mỗi đợt ${c.yield} ${c.unit}, đợt sau cách ${growS(c.re)}.${c.dry > DRY ? ' Rễ sâu, ' + growS(c.dry) + ' mới khô đất.' : ''}",
    "Hái ${c.cuts} đợt, mỗi đợt ${c.yield + ttGi(c)} ${c.unit}, đợt sau cách ${growS(c.re)}.${ttGi(c) ? ' Tre trăm đốt khắc nhập cho thêm một trái mỗi đợt.' : ''}${c.dry > DRY ? ' Rễ sâu, ' + growS(c.dry) + ' mới khô đất.' : ''}")

# 4. Sổ cổ tích nói ra cái tre trăm đốt cho
rep("tretramdot: () => L135('Lớn rồi thì chạm vô là hô Khắc xuất, Khắc nhập — trăm đốt tre rời ra rồi dính lại cho con coi chơi.', 'Once grown, tap it to call out \"Khắc xuất! Khắc nhập!\" and watch the hundred joints fly apart and snap back together.'),",
    "tretramdot: () => L135('Lớn rồi thì chạm vô là hô Khắc xuất, Khắc nhập — trăm đốt tre rời ra rồi dính lại. Giàn trong vườn nhờ vậy mà mỗi đợt hái thêm được một trái.', 'Once grown, tap it to call out \"Khắc xuất! Khắc nhập!\" and watch the hundred joints fly apart and snap back together. Every trellis in the garden also gives one extra fruit each pick.'),")

io.open(dst, 'w', encoding='utf-8').write(s)
print('xong', dst, len(s), 'ky tu')
