# vis115: ghé vườn bạn, phân biệt hái giùm với hái ké. python3 vis115.py live/v115_1c.html live/v115_1d.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
# thanh trên cùng nói rõ lúc này chạm liếp chín thì rau về kho ai
rep("function visitInfo(){ const el = $('#vInfo'); if (el) el.textContent = VISIT.kind === 'ban' ? `${VISIT.repay ? 'Lấy lại 1 món · ' : ''}Công đổi được ${VISIT.cong || 0} · đã phụ ${VISIT.loot.water + (VISIT.loot.help || 0)} liếp · hái ké còn ${VISIT.left}` : `Còn hái được ${VISIT.left} món · đã tưới giùm ${VISIT.loot.water} liếp`; }",
"""function visitMode(){ if (VISIT.repay) return 've'; if ((VISIT.cong || 0) > 0 && VISIT.left > 0) return 've'; return (VISIT.loot.help || 0) < DOICONG || VISIT.loot.water < DOICONG ? 'phu' : 'xong'; }
function visitInfo(){ const el = $('#vInfo'); if (!el) return; if (VISIT.kind !== 'ban'){ el.textContent = `Còn hái được ${VISIT.left} món · đã tưới giùm ${VISIT.loot.water} liếp`; return; }
  const m = visitMode(), bar = el.closest('.vbar'), mo = $('#vMode'); if (bar) bar.dataset.m = m; if (mo){ mo.querySelector('img').src = m === 've' ? (ICON.gio || UIC.sickle) : UIC.sickle; mo.querySelector('b').textContent = VISIT.repay ? 'Lấy lại 1 món của con' : m === 've' ? `Hái ké đem về · còn ${VISIT.left} món` : m === 'phu' ? `Hái giùm ${VISIT.owner}` : 'Hôm nay phụ đủ rồi'; }
  el.textContent = m === 've' ? 'Chạm liếp chín, rau về kho con' : m === 'phu' ? `Tưới hay hái 1 liếp giúp ${VISIT.owner}, xong được hái ké 1 món` : 'Mai qua phụ tiếp nghe con'; const col = m === 've' ? '#F2B01E' : '#7DB84A'; for (const g of window.__BUBALL || []) if (g.userData.hotP) for (const x of g.userData.hotP) x.material.color.set(col); }""")
rep("""<div><b>${String(VISIT.name || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]))}</b><span id="vInfo"></span></div>""",
"""<div><b>${String(VISIT.name || '').replace(/[&<>"]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]))}</b>${fr ? '<div id="vMode"><img alt=""><b></b></div>' : ''}<span id="vInfo"></span></div>""")
# ghim liếp chín: xanh là hái giùm, vàng là hái ké
rep("ring.userData.ro = 3; M(new T.CircleGeometry(.268, 40), MB(BN)","ring.userData.ro = 3; if (hot) g.userData.hotP = [ring]; M(new T.CircleGeometry(.268, 40), MB(BN)")
rep("const tail = tri(.07, .1, -.215, col, .015); tail.userData.ro = 3;","const tail = tri(.07, .1, -.215, col, .015); tail.userData.ro = 3; if (hot) g.userData.hotP.push(tail);")
# vườn bạn: chỉ còn ghim hái, ghim tưới; ghim gieo hạt, đắp liếp là việc của chủ vườn
rep("  try { if (v.want === 'h') bubIcon(v.bub.h, ICON[p.crop]);","  if (VISIT && v.want && v.want !== 'h' && v.want !== 'w') v.want = null;\n  try { if (v.want === 'h') bubIcon(v.bub.h, ICON[p.crop]);")
# chữ bay lên nói rõ rau đi đâu
rep("`Hái giùm ${VISIT.owner} · được hái ké 1 món`","`Rau về kho ${VISIT.owner} · được hái ké 1 món`")
rep("`${fr ? 'Hái ké' : 'Hái'} +${n} ${c.unit} ${c.name.toLowerCase()}`","`${fr ? 'Đem về' : 'Hái'} +${n} ${c.unit} ${c.name.toLowerCase()}`")
rep("sayOnce('haigium', `Hái giùm thì rau vô kho của ${VISIT.owner}. Giờ con chạm liếp chín khác, hái ké một món đem về nghe.`, 'vui');","sayOnce('haigium', `Xong công rồi. Giờ ghim đổi màu vàng, con chạm liếp chín là hái ké đem về nghe.`, 'vui');")
i=s.index('</style>')
s=s[:i]+"#vMode{display:flex;align-items:center;gap:6px;margin:2px 0 1px}#vMode img{width:22px;height:22px;flex:none}#vMode b{font-family:var(--f-game);font-size:15px;font-weight:400;color:#3F7A31}.vbar[data-m=ve] #vMode b{color:#B5720F}.vbar[data-m=ve]{box-shadow:0 0 0 3px #F2B01E}.vbar[data-m=phu]{box-shadow:0 0 0 3px #7DB84A}\n"+s[i:]
open(dst,'w',encoding='utf-8').write(s)
