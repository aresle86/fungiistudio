# ga115: số trên bình tưới, luồng ấp trứng. python3 ga115.py live/v115_1b.html live/v115_1c.html
import sys
src,dst=sys.argv[1],sys.argv[2]; s=open(src,encoding='utf-8').read()
def rep(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:70],s.count(a))
    s=s.replace(a,b)
# bình tưới: số trên bình đi theo số liếp khô thật, tưới xong hay mưa xong là đổi liền
rep("try { const nw = VISIT ? visWaterIds().length : dryIds().length; TRAY.water.hidden = false; TRAY.water.classList.toggle('zero', !nw); $('#tCanN').textContent = nw || ''; } catch (e) {}","canBadge();")
rep("const hud = () => { $('#xu')","function canBadge(){ try { const nw = VISIT ? visWaterIds().length : dryIds().length; TRAY.water.hidden = false; TRAY.water.classList.toggle('zero', !nw); $('#tCanN').textContent = nw || ''; } catch (e) {} }\nsetInterval(canBadge, 2000);\nconst hud = () => { $('#xu')")
rep("wet(id, 1); avGo(id); refreshPlot(id); save(); if (condOf(p) === 'ok'","wet(id, 1); avGo(id); refreshPlot(id); save(); canBadge(); if (condOf(p) === 'ok'")
# ấp trứng: trước khi có lứa gà con đầu tiên thì lượm trứng phải hỏi; trứng đã lượm vô kho cũng đem ấp được
rep("const gaOn = () =>","const gaHatchWant = () => (ST.lv || 1) >= GA.buyLv && !!ST.ga.fixed && !ST.ga.hatched && !ST.ga.brood, gaBroodN = () => Math.min(ST.ga.eggs + (ST.inv.trungga || 0), GA.clutch[ST.ga.lv] || 3), gaHatchOk = () => gaHatchWant() && ST.ga.rooster > 0 && ST.ga.hens >= 2 && gaBroodN() >= 2;\nconst gaOn = () =>")
rep("  collect(){ const g = ST.ga, n = g.eggs; if (!n) return; const free","  collect(force){ const g = ST.ga, n = g.eggs; if (!n) return; if (!force && gaHatchOk()) return openSheet('ga'); const free")
rep("else if (a === 'gaegg') ga.collect();","else if (a === 'gaegg') ga.collect(true);")
rep("brood(){ const g = ST.ga, n = Math.min(g.eggs, GA.clutch[g.lv] || 3); if","brood(){ const g = ST.ga, n = gaBroodN(); if")
rep("if (n < 2) return toast('Ổ cần ít nhất 2 trứng mới cho gà nằm ấp được con.', 'dan');\n    g.eggs -= n; g.brood = { stage: 'egg', t: 0, n }; say(`Con mái vàng đòi ấp rồi. Ngoại để lại ${n} trứng cho nó nằm,","if (n < 2) return toast('Cần ít nhất 2 trứng mới cho gà nằm ấp được con.', 'dan');\n    const tuO = Math.min(g.eggs, n), tuKho = n - tuO; g.eggs -= tuO; if (tuKho) ST.inv.trungga -= tuKho; g.brood = { stage: 'egg', t: 0, n }; say(`Con mái vàng đòi ấp rồi. Ngoại để lại ${n} trứng cho nó nằm,")
rep("nestCap = g.hens * GA.nestMax, nB = Math.min(g.eggs, GA.clutch[g.lv] || 3);","nestCap = g.hens * GA.nestMax, nB = gaBroodN(), hoiAp = gaHatchOk();")
rep("  const lasts = lay > 0 ? Math.floor(g.trough / lay) * GA.cyc / ST.spd : 0; const CTA = [g.eggs ? UX.btn('gaegg', `Lượm ${g.eggs} trứng`, { g: 1, img: ICON.trungga }) : '',","  if (hoiAp) h += UX.hero(ICON.trungga, 'Ngoại đang mong có gà con', `Để ${nB} trứng cho gà mái ấp là có gà con, xong việc Ngoại nhờ`, 'go') + UX.cta([UX.btn('gabrood', `Để ${nB} trứng cho gà ấp`, { g: 1, img: ICON.trungga, sub: g.eggs >= nB ? '' : `lấy ${nB - g.eggs} trứng trong kho` }), g.eggs ? UX.btn('gaegg', `Lượm hết ${g.eggs} trứng`, {}) : '']);\n  const lasts = lay > 0 ? Math.floor(g.trough / lay) * GA.cyc / ST.spd : 0; const CTA = [g.eggs && !hoiAp ? UX.btn('gaegg', `Lượm ${g.eggs} trứng`, { g: 1, img: ICON.trungga }) : '',")
rep("g: !g.eggs && food < tcap, img: ICON.bap","g: (!g.eggs || hoiAp) && food < tcap, img: ICON.bap")
rep("+ UX.upc('gabrood', ICON.trungga,","+ (hoiAp ? '' : UX.upc('gabrood', ICON.trungga,")
rep("nở sau ${fmtT(GA.brood / ST.spd)}` }) + '</div>'; }","nở sau ${fmtT(GA.brood / ST.spd)}` })) + '</div>'; }")
rep("  if (g.eggs > 0) h += UX.hero(ICON.trungga, `Có ${g.eggs} trứng chờ lượm`,","  if (hoiAp && g.eggs > 0) {} else if (g.eggs > 0) h += UX.hero(ICON.trungga, `Có ${g.eggs} trứng chờ lượm`,")
# việc Ngoại nhờ: nói rõ đang thiếu gì, có nút tới chuồng
rep("how: 'Để từ 2 trứng trong ổ, chạm chuồng gà cho một mái nằm ấp. Gà con nở là lên cấp', goals:","how: 'Để từ 2 trứng trong ổ, chạm chuồng gà cho một mái nằm ấp. Gà con nở là lên cấp', howF: () => { const g = ST.ga; if (g.brood) return 'Gà mái đang ấp rồi. Gà con nở là lên cấp'; if (!g.rooster) return 'Chuồng chưa có gà trống. Trứng có trống mới nở ra gà con'; if (g.hens < 2) return 'Cần 2 gà mái: một con ấp, một con đẻ. Mua thêm gà mái ở chuồng'; if (gaBroodN() < 2) return 'Cần ít nhất 2 trứng. Cho gà ăn rồi chờ gà đẻ nghe con'; return 'Đủ trứng rồi con. Vô chuồng gà, chọn để trứng cho gà ấp. Gà con nở là lên cấp'; }, goals:")
rep("<div class=\"qt\"><b>${q.txt}</b><span>${q.how}</span>`;","<div class=\"qt\"><b>${q.txt}</b><span>${q.howF ? q.howF() : q.how}</span>`;")
rep("  body += '</div></div>'; h += body;\n  if (q.t === 'pay')","  if (q.howF && !ST.ga.brood) body += `<button class=\"btn g qgo\" data-b=\"gahatch\"><img src=\"${ICON.trungga}\" alt=\"\"><span>Tới chuồng gà</span></button>`;\n  body += '</div></div>'; h += body;\n  if (q.t === 'pay')")
rep("  else if (a === 'weedgo'){ closeBook(); weedGo(); return; }","  else if (a === 'weedgo'){ closeBook(); weedGo(); return; }\n  else if (a === 'gahatch'){ closeBook(); openSheet('ga'); return; }")
rep("t = g[0]; em = `${v}/${g[2]}`; f = v / g[2]; go = ready; lab = 'NGOẠI NHỜ'; }","t = g[0]; em = `${v}/${g[2]}`; f = v / g[2]; go = ready; lab = 'NGOẠI NHỜ'; if (q.howF) act = 'gahatch'; }")
rep("if (a === 'weed') weedGo(); else if (a.startsWith('pen:')) penGo(a.slice(4));","if (a === 'weed') weedGo(); else if (a === 'gahatch') openSheet('ga'); else if (a.startsWith('pen:')) penGo(a.slice(4));")
open(dst,'w',encoding='utf-8').write(s)
