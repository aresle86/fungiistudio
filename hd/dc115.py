# dc115: đồ trang trí ao cất lại, đặt lại miễn phí; lục bình chờ tới cấp 15 mới xuất hiện. python3 dc115.py vào ra
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
# cất: vẫn thuộc về mình (dc), chỉ không hiện trên ao (off)
rep("has = { ...aoDc() }; if (has.sen || has.sung)","has = { ...aoDc() }; for (const k0 in (B && B.off) || {}) delete has[k0]; if (has.sen || has.sung)")
rep("function aoDcBuy(k){","function aoDcTog(k){ const B = ST.big.ao; if (!B || !B.dc || !B.dc[k]) return; B.off = B.off || {}; const was = !!B.off[k]; if (was) delete B.off[k]; else B.off[k] = 1; save(); sfx('pop'); buzz(10); const c0 = aoCenter(); if (c0 && was) for (let i = 0; i < 8; i++) puff('spark', c0[0] + R(-.9, .9), .35, c0[1] + R(-.6, .6), 1, pick(['#F5D27A', '#FBF7EE']), .7); renderSheet(); } function aoDcBuy(k){")
rep("h += UX.title('Trang trí ao', 'Mua là có liền, nâng ao đồ đi theo')","h += UX.title('Trang trí ao', 'Chạm món đã mua để cất hay đặt lại, không tốn xu')")
rep("return UX.upc('aodc', aoIc(k), d[0], vnX(d[1]), { k, dis: own || ST.xu < d[1], why: own ? 'Đã có trên ao' : '' });","const off = own && !!(B.off && B.off[k]); return own ? UX.upc('aodcx', aoIc(k), d[0], null, { k, why: off ? 'Đang cất · chạm để đặt lại' : 'Đang trên ao · chạm để cất' }) : UX.upc('aodc', aoIc(k), d[0], vnX(d[1]), { k, dis: ST.xu < d[1] });")
rep("else if (a === 'aodc'){ aoDcBuy(b.dataset.k); return; }","else if (a === 'aodc'){ aoDcBuy(b.dataset.k); return; } else if (a === 'aodcx'){ aoDcTog(b.dataset.k); return; }")
# lục bình chỉ xuất hiện khi đan giỏ được (cấp 15): chưa cần thì chưa cho lụm, bỏ đường ra rơm
rep("lucbinh: { lv: 2, max: lbG ? 4 : 2, every: (lbG ? 20 : 35) * 60, name: 'Vớt lục bình' }","lucbinh: { lv: lbG ? 2 : 999, max: 4, every: 20 * 60, name: 'Vớt lục bình' }")
rep("const D = oddDefs(), lv = ST.lv || 1;\n  for (const k in D){ if (lv < D[k].lv) continue;","const D = oddDefs(), lv = ST.lv || 1; if (lv < D.lucbinh.lv) ST.odd.list = ST.odd.list.filter(o => o.k !== 'lucbinh');   /* vườn cũ còn lục bình nổi từ trước thì dọn đi */\n  for (const k in D){ if (lv < D[k].lv) continue; if (k === 'lucbinh' && has('lucbinh') >= 10){ ST.odd.acc[k] = 0; continue; }")
rep("if (kCap() - kUsed() > 0){ ST.inv.rom = (ST.inv.rom || 0) + 1; txt = '+1 rơm phủ liếp'; flyTo(ICON.rom, o.x, .2, o.z); } else txt = 'Kho đầy, phơi bỏ mé mương';","txt = 'Đủ lục bình rồi con';")
rep("if (junk === 'lucbinh'){ const sl = STORE('lucbinh');","if (junk === 'lucbinh' && gioOn()){ const sl = STORE('lucbinh');")
rep("Vịt ăn rau muống, vớt lục bình cho ăn cũng được.","Vịt ăn rau muống, hết thì mua cám cũng được.")
rep("'Cho rau muống hay vớt lục bình cho vịt ăn'","'Cho vịt ăn rau muống hay cám'")
rep("lục bình vớt dưới mương (+1 phần, khỏi tốn xu), thiếu thì mua cám","${gioOn() ? 'lục bình vớt dưới mương (+1 phần, khỏi tốn xu), ' : ''}thiếu thì mua cám")
rep("Không có rau muống mà cũng hết xu mua cám rồi con. Vớt lục bình cho vịt ăn cũng được.","Không có rau muống mà cũng hết xu mua cám rồi con. Hái rau đem bán rồi mua cám nghe.")
rep("bubIcon(VITV.bF, ICON.lucbinh || ICON.raumuong)","bubIcon(VITV.bF, ICON.raumuong || ICON.lucbinh)")
rep("Hố này con bỏ lá rụng, lục bình, rau dư vô.","Hố này con bỏ lá rụng, rau dư vô.")
rep("Kho không còn rau dư con. Lá rụng với lục bình bỏ vô cũng được.","Kho không còn rau dư con. Lá rụng bỏ vô cũng được.")
rep("Đào cái hố ủ phân nghe con. Lá rụng, lục bình bỏ vô, ủ ra phân bón liếp cho đất tốt lại.","Đào cái hố ủ phân nghe con. Lá rụng, rau dư bỏ vô, ủ ra phân bón liếp cho đất tốt lại.")
rep("'Ủ lá, lục bình thành phân'","'Ủ lá, rau dư thành phân'")
rep("GD, levelUp, sfx, fxS:","GD, levelUp, sfx, oddDo, aoDcTog, fxS:")
open(dst,'w',encoding='utf-8').write(s)
