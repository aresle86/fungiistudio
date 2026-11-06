# egg115: chạm ổ trứng: khi cho gà ấp được thì chọn ngay tại ổ, Ấp hay Lượm; nút ấp không còn lẫn trong Nuôi thêm. python3 egg115.py vào ra
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
# chạm ổ
rep("collect(force){ const g = ST.ga, n = g.eggs; if (!n) return; if (!force && gaHatchOk()) return openSheet('ga');",
    "collect(force){ const g = ST.ga, n = g.eggs; if (!n) return; if (!force && (gaEggAsk() || gaHatchWant())) return gaEggRing();")
rep("gaHatchOk = () => gaHatchWant() && ST.ga.rooster > 0 && ST.ga.hens >= 2 && gaBroodN() >= 2;",
    "gaHatchOk = () => gaHatchWant() && ST.ga.rooster > 0 && ST.ga.hens >= 2 && gaBroodN() >= 2, gaEggAsk = () => { const g = ST.ga; return (ST.lv || 1) >= GA.buyLv && !!g.fixed && !g.brood && g.rooster > 0 && g.hens >= 2 && gaBroodN() >= 2 && (!g.hatched || g.hens + g.rooster < gaCap()); };")
# câu nhắc sau lần lượm đầu: trứng trong kho vẫn ấp được
rep("sayOnce('egg1', 'Trứng gà ta đem chợ bán được giá lắm. Muốn có gà con thì để trứng lại trong ổ cho gà mái nằm ấp.', 'vui');",
    "sayOnce('egg1', (ST.lv || 1) >= GA.buyLv ? 'Trứng gà ta đem chợ bán được giá lắm. Trứng trong kho vẫn cho gà ấp được, đừng bán hết nghe con.' : 'Trứng gà ta đem chợ bán được giá lắm. Tới cấp 5 Ngoại chỉ con cho gà nằm ấp.', 'vui');")
# bán hết trứng khi còn cần ấp
rep("SRC[k] -= n; ST.xu += v; stepMark('sell1');",
    "SRC[k] -= n; ST.xu += v; stepMark('sell1'); if (k === 'trungga' && gaHatchWant() && !gaHatchOk()) sayOnce('eggsell', 'Ngoại còn cần 2 trứng cho gà ấp đó con. Lứa sau chừa lại nghe.', 'dan');")
# vòng chọn tại ổ
rep("const coopRing = () => penRing('ga');",
"""const coopRing = () => penRing('ga');
function gaEggRing(){ const g = ST.ga, n = g.eggs, ok = gaEggAsk(), nB = gaBroodN(), kho = nB - Math.min(g.eggs, nB), why = !g.rooster ? 'Chuồng cần gà trống mới ấp được' : g.hens < 2 ? 'Cần 2 gà mái: một con ấp, một con đẻ' : nB < 2 ? 'Cần 2 trứng mới cho gà ấp được' : ''; RINGID = '__nest'; PEND = null; if (TOOL) clearTool(); fan.hidden = true;
  RING.innerHTML = `<div class="rgh"><span>Ổ có ${n} trứng</span><button class="rgb" data-r="x" aria-label="Đóng">×</button></div>${ok ? `<div class="rgo egg"><div><button class="btn g" data-r="gabrood"><img src="${ICON.mai}" alt="">Để ${nB} trứng cho gà ấp</button><small>${kho ? `Lấy ${kho} trứng trong kho · ` : ''}nở sau ${fmtT(GA.brood / ST.spd)}</small></div></div>` : `<div class="rgo egg"><small>${why}</small></div>`}<div class="rgo egg"><button class="btn${ok ? '' : ' g'}" data-r="gaegg"><img src="${ICON.trungga}" alt="">Lượm ${n} trứng</button></div>`;
  RING.hidden = false; ringPos(); sfx('pick'); }""")
rep("if (String(RINGID).startsWith('__pen:')){ const P = PENS[RINGID.slice(6)], c = P.at(); pv.set(c.x, P.by + .25, c.z).project(cam); }",
    "if (RINGID === '__nest') pv.set(NEST.x, NEST.y + .3, NEST.z).project(cam); else if (String(RINGID).startsWith('__pen:')){ const P = PENS[RINGID.slice(6)], c = P.at(); pv.set(c.x, P.by + .25, c.z).project(cam); }")
rep("if (a === 'penfix'){ closeRing(); penFix(b.dataset.k); return; }",
    "if (a === 'penfix'){ closeRing(); penFix(b.dataset.k); return; } if (a === 'gabrood'){ closeRing(); ga.brood(); hud(); return; } if (a === 'gaegg'){ closeRing(); ga.collect(true); hud(); try { kfOpen(); } catch (e) {} return; }")
# bảng chuồng: ấp được thì là nút lớn, không nằm chung với đồ mua
rep("nB < 2 ? 'ổ cần 2 trứng trở lên' : '', bt = g.buyD === dayKey();\n    h += UX.title('Nuôi thêm'",
    "nB < 2 ? 'cần 2 trứng trở lên' : '', bt = g.buyD === dayKey();\n    if (!hoiAp && !why) h += UX.cta([UX.btn('gabrood', `Để ${nB} trứng cho gà ấp`, { img: ICON.trungga, sub: `${nB > g.eggs ? `lấy ${nB - g.eggs} trứng trong kho · ` : ''}nở sau ${fmtT(GA.brood / ST.spd)}` })]);\n    h += UX.title('Nuôi thêm'")
rep("(hoiAp ? '' : UX.upc('gabrood', ICON.trungga,","(hoiAp || !why ? '' : UX.upc('gabrood', ICON.trungga,")
# nhiệm vụ
rep("how: 'Để từ 2 trứng trong ổ, chạm chuồng gà cho một mái nằm ấp. Gà con nở là lên cấp'","how: 'Cần 2 trứng, trong ổ hay trong kho đều được. Chạm ổ rồi chọn để gà ấp. Gà con nở là lên cấp'")
s=s.replace("</style>",".rgo.egg{padding:3px 2px}.rgo.egg .btn{min-height:44px}.rgo.egg small{margin-top:3px}\n</style>",1)
open(dst,'w',encoding='utf-8').write(s)
