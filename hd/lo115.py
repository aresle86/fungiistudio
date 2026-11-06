# lo115: chuồng vịt đầy vẫn ấp được, vịt con dư Ngoại bán giùm (trước đây 12/12 là kẹt hẳn). python3 lo115.py vào ra
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
# ấp: luôn đủ một lứa, không còn chặn vì chuồng
rep("if ((ST.inv.trungvit || 0) < Math.min(LO.eggs, Math.max(1, vitCap() - ST.vit.n))) return say(","if ((ST.inv.trungvit || 0) < LO.eggs) return say(")
rep("const room0 = Math.max(0, vitCap() - ST.vit.n); if (room0 < 1) return toast('Chuồng vịt hết chỗ rồi. Mình nới chuồng trước rồi hẵng ấp.', 'dan', { now: true }); const ne = Math.min(LO.eggs, room0); L.n = ne;","const ne = LO.eggs; L.n = ne;")
# bắt: con nào không có chỗ thì Ngoại bán, không còn nằm chờ trong lò
rep("add = Math.min(L.hatch, room), sold = 0, wait = L.hatch - add; if (!add) return toast('Chuồng vịt hết chỗ rồi. Nới chuồng xong mình bắt vịt con ra nghe.', 'dan', { now: true }); v.n += add; v.trough += add; L.hatch = wait; if (!wait){ L.on = 0; L.n = 0; } L.done++; L.kid = Date.now(); vitSpawn(); celebAt(",
    "add = Math.min(L.hatch, room), sold = L.hatch - add; v.n += add; v.trough += add; L.hatch = 0; L.on = 0; L.n = 0; L.done++; if (add){ L.kid = Date.now(); vitSpawn(); } celebAt(")
rep("say(wait ? `Bắt được ${add} con ra chuồng rồi. Còn ${wait} con trong lò, nới chuồng rồi bắt tiếp.` : `Nở ${add} con vịt rồi nè! Thả chung với đàn luôn.`, 'vui', { now: true });",
    "say(!sold ? `Nở ${add} con vịt rồi nè! Thả chung với đàn luôn.` : add ? `${add} con ra chuồng, còn ${sold} con Ngoại bán cho hàng xóm được ${sold * LO.sellDuck} xu.` : `Chuồng chật rồi, ${sold} con vịt con Ngoại bán cho hàng xóm được ${sold * LO.sellDuck} xu.`, 'vui', { now: true });")
# bảng lò
rep("room = vitCap() - ST.vit.n; let h = '';\n  if (L.on && L.t <= 0)","room = Math.max(0, vitCap() - ST.vit.n), canUp = ST.vit.lv + 1 < VIT.caps.length; let h = '';\n  if (L.on && L.t <= 0)")
rep("room >= L.hatch ? 'Bắt thả chung với đàn nghe' : room > 0 ? `Chuồng còn ${room} chỗ, số còn lại chờ trong lò` : 'Chuồng hết chỗ, nới chuồng rồi bắt', 'go');",
    "room >= L.hatch ? 'Bắt thả chung với đàn nghe' : `${room > 0 ? `Chuồng còn ${room} chỗ, dư ${L.hatch - room} con` : `Chuồng đầy, ${L.hatch} con`} Ngoại bán giùm ${LO.sellDuck} xu một con${canUp ? '. Muốn giữ thì nới chuồng trước' : ''}`, 'go');")
rep("`Đang ấp ${LO.eggs} trứng`","`Đang ấp ${L.n || LO.eggs} trứng`")
rep("egg >= LO.eggs && cui >= LO.cui ? `Đủ ${LO.eggs} trứng vịt với củi rồi, ấp liền được` :",
    "egg >= LO.eggs && cui >= LO.cui ? (room < LO.eggs ? `${room > 0 ? `Chuồng còn ${room} chỗ` : 'Chuồng đầy'}, nở dư thì Ngoại bán giùm ${LO.sellDuck} xu một con` : `Đủ ${LO.eggs} trứng vịt với củi rồi, ấp liền được`) :")
rep("UX.btn('lohatch', 'Bắt vịt con', { g: 1, img: ICON.vitcon })","UX.btn('lohatch', room > 0 ? 'Bắt vịt con' : `Nhờ Ngoại bán ${L.hatch} con`, { g: 1, img: ICON.vitcon })")
rep("UX.btn('loput', room < 1 ? 'Chuồng hết chỗ' : `Ấp ${Math.min(LO.eggs, room)} trứng vịt`, { g: 1, img: ICON.trungvit, dis: egg < Math.min(LO.eggs, Math.max(1, room)) || cui < LO.cui || room < 1 })","UX.btn('loput', `Ấp ${LO.eggs} trứng vịt`, { g: 1, img: ICON.trungvit, dis: egg < LO.eggs || cui < LO.cui })")
rep("chuồng hết chỗ thì Ngoại bán cho hàng xóm.","chuồng hết chỗ thì Ngoại bán cho hàng xóm ${LO.sellDuck} xu một con.")
rep("`${ST.vit.n}/${vitCap()} <small>con</small>`","`${ST.vit.n}/${vitCap()} <small>${EN ? 'ducks' : 'con'}</small>`")
open(dst,'w',encoding='utf-8').write(s)
