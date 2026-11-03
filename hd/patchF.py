p='live/vuon3d.html';s=open(p,encoding='utf8').read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:100]); s=s.replace(a,b)
rep("const GD = k => CROPS[k] || EXTRA[k] || DISH[k] || PHOI[k] || MUOI[k];",
"""// lò sấy (cấp 10) và đồ thủ công: mứt khế, xoài sấy, dừa sấy, mứt dừa Tết, giỏ lục bình
const SAY = {
  mutkhe: { name: 'Mứt khế', unit: 'hũ', lv: 10, in: { khe: 6, duong: 1 }, t: 6 * 3600, sell: 115, story: 'Mứt khế xắt lát, rim đường rồi sấy. Tết nào khay mứt nhà mình cũng có màu vàng khế.' },
  xoaisay: { name: 'Xoài sấy dẻo', unit: 'bịch', lv: 11, in: { xoai: 3 }, t: 8 * 3600, sell: 150, story: 'Xoài cát chín cây sấy dẻo, gửi lên thành phố biếu bà con ai cũng khen.' },
  comdua: { name: 'Cơm dừa sấy', unit: 'bịch', lv: 12, in: { dua: 2 }, t: 6 * 3600, sell: 75, story: 'Cơm dừa nạo sợi sấy giòn, nhai nghe sựt sựt, thơm béo.' },
  mutdua: { name: 'Mứt dừa Tết', unit: 'hũ', lv: 12, in: { dua: 2, duong: 1 }, t: 8 * 3600, sell: 90, story: 'Mứt dừa ngũ sắc là món Tết. Ngoại nhuộm bằng lá dứa, gấc, mấy màu tự nhiên trong vườn.' },
  gio: { name: 'Giỏ lục bình', unit: 'cái', lv: 10, sell: 40, story: 'Giỏ lục bình đan tay, đem ra chợ nổi bán cho khách phương xa.' } };
const DUONG_PRICE = 5;
const GD = k => CROPS[k] || EXTRA[k] || DISH[k] || PHOI[k] || MUOI[k] || SAY[k];""")
rep("muoi: { name: 'Muối hột', sell: 2, unit: 'bịch', nosell: true } };","muoi: { name: 'Muối hột', sell: 2, unit: 'bịch', nosell: true }, duong: { name: 'Đường cát', sell: 2, unit: 'bịch', nosell: true }, lucbinh: { name: 'Lục bình', sell: 1, unit: 'bó', nosell: true } };")
rep("const STORE = k => (DISH[k] || PHOI[k] || MUOI[k] || k === 'cui' || k === 'muoi') ?","const STORE = k => (DISH[k] || PHOI[k] || MUOI[k] || SAY[k] || k === 'cui' || k === 'muoi' || k === 'duong' || k === 'lucbinh') ?")
s=s.replace("Object.entries(ST.gb || {}).some(([k, n]) => n > 0 && (DISH[k] || PHOI[k] || MUOI[k]))","Object.entries(ST.gb || {}).some(([k, n]) => n > 0 && (DISH[k] || PHOI[k] || MUOI[k] || SAY[k]))")
rep("const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && (DISH[k] || PHOI[k] || MUOI[k]));","const gbi = Object.entries(ST.gb || {}).filter(([k, n]) => n > 0 && (DISH[k] || PHOI[k] || MUOI[k] || SAY[k]));")
rep("const canIn = inp => Object.entries(inp).every(([ik, n]) => (ik === 'lucbinh' ? 0 : has(ik)) >= n);","const canIn = inp => Object.entries(inp).every(([ik, n]) => has(ik) >= n);")
rep("const phoiName = k => k === 'lucbinh' ? 'lục bình' : k === 'muoi' ? 'muối' :","const phoiName = k => k === 'lucbinh' ? 'lục bình' : k === 'muoi' ? 'muối' : k === 'duong' ? 'đường' :")
# lò sấy là đồ đặt trên ô
rep("  ho: { name: 'hố ủ phân', title: 'Hố ủ phân', lv: 8, buy: 100, sheet: 'ho',","  say: { name: 'lò sấy', title: 'Lò sấy', lv: 10, buy: 600, sheet: 'say', hi: 'Lò sấy gạch này Ngoại xây hồi trước để sấy mứt Tết. Bỏ củi vô, chạy cả đêm không cần nắng.' },\n  ho: { name: 'hố ủ phân', title: 'Hố ủ phân', lv: 8, buy: 100, sheet: 'ho',")
# sau nhà
rep("const SONGC = {","""// sau nhà (cấp 11): 10 ô sau lưng nhà, phải dọn tre gai (việc lên cấp 12) mới đắp liếp được
const SAU = { lv: 11, cost: 70, x0: -6.3, z0: -3.4, cw: .8, cl: .65, gap: .1, cols: 5 };
for (let i = 0; i < 10; i++){ const c = i % SAU.cols, r = Math.floor(i / SAU.cols), u0 = SAU.x0 + c * (SAU.cw + SAU.gap), v0 = SAU.z0 + r * (SAU.cl + SAU.gap); PLOTS.push({ id: 'N' + (i + 1), b: [u0, v0, u0 + SAU.cw, v0 + SAU.cl], name: `Sau nhà · ô ${i + 1}`, bai: true, zone: 'sau', lv: SAU.lv, cost: SAU.cost }); }
const SAUC = { x: SAU.x0 + 2.2, z: SAU.z0 + .7 };
const SONGC = {""")
rep("const isBed = P => /^[ABCHS]/.test(P.id),","const isBed = P => /^[ABCHSN]/.test(P.id),")
rep("hidP = P => P.bai && (ST.lv || 1) < (P.lv || BAI.lv), nOpen = () => ST.open.filter(i => i[0] !== 'H' && i[0] !== 'S').length;",
"hidP = P => P.bai && ((ST.lv || 1) < (P.lv || BAI.lv) || (P.zone === 'sau' && !(ST.qd || {})[12])), nOpen = () => ST.open.filter(i => !/^[HSN]/.test(i)).length;")
rep("const zoneName = P => P.zone === 'song' ? 'Đất bồi mé sông' : 'Bãi cỏ';","const zoneName = P => P.zone === 'song' ? 'Đất bồi mé sông' : P.zone === 'sau' ? 'Đất sau nhà' : 'Bãi cỏ';")
# sim + tick
rep("khapSim(dt); hoSim(dt); loSim(dt); } catch (e) {}","khapSim(dt); hoSim(dt); loSim(dt); saySim(dt); gioSim(dt); gheSim(); } catch (e) {}")
rep("khapSim(s2); hoSim(s2); loSim(s2); } catch (e) {}","khapSim(s2); hoSim(s2); loSim(s2); saySim(s2); gioSim(s2); } catch (e) {}")
rep("cauTick(t, dt); boTick(); } catch (e)","cauTick(t, dt); boTick(); sayTick(t, dt); gioTick(t); gheTick(t); treTick(); } catch (e)")
# chạm
rep("  if (cauHit(e.clientX, e.clientY)){ cauTap(); return; }",
"""  if (cauHit(e.clientX, e.clientY)){ cauTap(); return; } if (sayHit(e.clientX, e.clientY)){ lsay.takeAll(); openSheet('say'); return; } if (gheHit(e.clientX, e.clientY)){ openSheet('cho'); SHEET.tab = 'don'; renderSheet(); return; }
  { const gh = gioHit(e.clientX, e.clientY); if (gh){ const g = ST.gio; if (g.on && g.t <= 0) gio.take(); else if (gh === 'bub' && !g.on) gio.put(); else openSheet('gio'); hud(); return; } }""")
rep("if (ok === 'khap') khap.takeAll(); openSheet(","if (ok === 'khap') khap.takeAll(); if (ok === 'say') lsay.takeAll(); openSheet(")
rep("  if (kind === 'lo'){ shT.textContent = 'Lò ấp vịt'; h += loHTML(); }","  if (kind === 'lo'){ shT.textContent = 'Lò ấp vịt'; h += loHTML(); }\n  if (kind === 'say'){ shT.textContent = 'Lò sấy'; h += sayHTML(); }\n  if (kind === 'gio'){ shT.textContent = 'Hiên nhà · đan giỏ'; h += gioHTML(); }")
rep("  else if (a === 'loput'){ lo.put(); }","  else if (a === 'sput'){ lsay.put(+b.dataset.n, b.dataset.k); } else if (a === 'stake'){ lsay.take(+b.dataset.n); } else if (a === 'gioput'){ gio.put(); } else if (a === 'giotake'){ gio.take(); } else if (a === 'ghegive'){ gheGive(b); }\n  else if (a === 'buyduong'){ const n = +b.dataset.n; if (ST.xu >= DUONG_PRICE * n && gbUsed() + n <= GB_CAP){ ST.xu -= DUONG_PRICE * n; ST.gb.duong = (ST.gb.duong || 0) + n; save(); hud(); buyFx(b, ICON.duong, `+${n} bịch đường`, DUONG_PRICE * n); } else if (gbUsed() + n > GB_CAP) say('Gác bếp hết chỗ rồi con.', 'dan'); }\n  else if (a === 'loput'){ lo.put(); }")
# chợ
rep("['ho', 'Ủ lá, lục bình thành phân']]) if (objOn(k)){","['ho', 'Ủ lá, lục bình thành phân'], ['say', 'Sấy mứt khế, xoài, dừa · chạy cả đêm']]) if (objOn(k)){")
rep("    if (objOn('khap')) h += `<div class=\"srow\"><div class=\"sic\"><img src=\"${ICON.muoi}\"","    if (objOn('say')) h += `<div class=\"srow\"><div class=\"sic\"><img src=\"${ICON.duong}\" alt=\"\"><span class=\"sq\">${(ST.gb || {}).duong || 0}</span></div><div class=\"sn\"><b>Đường cát</b>${stI('coin', DUONG_PRICE + ' xu/bịch')}<span class=\"mkh\">Rim mứt · để trên gác bếp</span></div><button class=\"btn s1\" data-a=\"buyduong\" data-n=\"1\" ${ST.xu < DUONG_PRICE ? 'disabled' : ''} aria-label=\"Mua 1 bịch đường\">+1</button><button class=\"btn sall\" data-a=\"buyduong\" data-n=\"4\" ${ST.xu < DUONG_PRICE * 4 ? 'disabled' : ''}>+4<small>${DUONG_PRICE * 4} xu</small></button></div>`;\n    if (objOn('khap')) h += `<div class=\"srow\"><div class=\"sic\"><img src=\"${ICON.muoi}\"")
rep("    if (SHEET.tab === 'don') h += ordHTML().replace('<div class=\"sub\">Đơn nhà bên</div>', '');","    if (SHEET.tab === 'don') h += (gheOn() ? gheHTML() + ordHTML() : ordHTML().replace('<div class=\"sub\">Đơn nhà bên</div>', ''));")
# lục bình cất gác bếp từ cấp 10
rep("  else if (o.k === 'lucbinh' && hoRoom()){","  else if (o.k === 'lucbinh' && gioOn() && has('lucbinh') < 10 && gbUsed() < GB_CAP){ ST.gb.lucbinh = (ST.gb.lucbinh || 0) + 1; txt = '+1 bó lục bình lên gác bếp'; flyTo(ICON.lucbinh, o.x, .2, o.z); for (let k = 0; k < 6; k++) puff('drop', o.x, .05, o.z, 1, '#9cc6e0', .5); }\n  else if (o.k === 'lucbinh' && hoRoom()){")
# lên cấp, việc, camera
rep("  if (n === 8) say(","""  if (n === 10) say('Cấp mười rồi đó con! Ngoại có lò sấy gạch, ra chợ đặt về mà sấy mứt khế. Sáng nào ghe bẹo chợ nổi cũng ghé bến, đơn lớn trả cao. Vớt lục bình phơi khô thì Ngoại ngồi hiên đan giỏ.', 'vui', { idle: true });
  if (n === SAU.lv){ say('Sau nhà tre gai mọc kín hết rồi. Dọn sạch thì có thêm mười ô đất tốt. Mở Sổ coi việc Ngoại dặn nghe.', 'vui', { idle: true }); setTimeout(() => { if (!VISIT) camTo(new T.Vector3(SAUC.x, .3, SAUC.z), Math.max(cam.zoom, DEFZ() * 1.05)); }, 1600); }
  if (n === 12) say('Cấp mười hai, vườn của con rồi đó. Dừa mé sông trồng được rồi, có dừa là làm mứt dừa Tết. Chờ mùa xoài đầu tiên nghe con, Ngoại có cái này giao cho con.', 'vui', { idle: true });
  if (n === 8) say(""")
rep("${n === 9 ? ', mé sông 8 ô, câu cá ở bến, lò ấp vịt, canh chua cá lóc' : ''}","${n === 9 ? ', mé sông 8 ô, câu cá ở bến, lò ấp vịt, canh chua cá lóc' : ''}${n === 10 ? ', lò sấy, ghe chợ nổi, giỏ lục bình' : ''}${n === 11 ? ', sau nhà 10 ô (dọn tre gai), xoài sấy' : ''}${n === 12 ? ', mứt dừa Tết, cơm dừa sấy, Sổ vườn' : ''}")
rep("  11: { t: 'goal', txt: 'Trồng đủ 3 loại cây trái',","  12: { t: 'pay', xu: 250, txt: 'Dọn tre gai sau nhà', how: 'Chặt bụi tre gai sau lưng nhà, mở mười ô đất mới' },\n  11: { t: 'goal', txt: 'Trồng đủ 3 loại cây trái',")
rep("tg.x = Math.max(baiOn() ? -3.6 : -1, Math.min(11.5, tg.x)); tg.z = Math.max(-.5,","tg.x = Math.max((ST.lv || 1) >= SAU.lv ? -4.6 : baiOn() ? -3.6 : -1, Math.min(11.5, tg.x)); tg.z = Math.max((ST.lv || 1) >= SAU.lv ? -2.4 : -.5,")
rep("if (x > 6.1 && x < 9.8 && z > 6.7 && z < 8.3) continue;","if (x > 6.1 && x < 9.8 && z > 6.7 && z < 8.3) continue; if (x < -1.6 && z < -1.8) continue;")
# xoài đầu mùa
rep("ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0;","ST.inv[p.crop] = (ST.inv[p.crop] || 0) + n; p.stolen = 0; if (p.crop === 'xoai') try { soVuon(); } catch (e) {}")
# đơn hàng
rep("for (const k of Object.keys(ST.khap.made || {})) if (MUOI[k]) pool.push(k);","for (const k of Object.keys(ST.khap.made || {})) if (MUOI[k]) pool.push(k); for (const k of Object.keys(ST.say.made || {})) if (SAY[k]) pool.push(k); if (ST.gio.done) pool.push('gio');")
rep("const known = pool.filter(k => k === 'trungga' || k === 'trungvit' || PHOI[k] || MUOI[k] ||","const known = pool.filter(k => k === 'trungga' || k === 'trungvit' || PHOI[k] || MUOI[k] || SAY[k] ||")
rep("base = PHOI[k] || k === 'dacai' ? 1 :","base = PHOI[k] || SAY[k] || k === 'dacai' ? 1 :")
rep("dacai: 'ăn với thịt kho',","dacai: 'ăn với thịt kho', mutkhe: 'bày mâm Tết', xoaisay: 'gửi lên thành phố', comdua: 'cho tụi nhỏ ăn vặt', mutdua: 'bày mâm Tết', gio: 'đi chợ',")
# vườn mẫu
rep("  m.qd[10] = 1;","  m.qd[10] = 1; m.qd[11] = 1; m.qd[12] = 1; m.say = { own: 1, at: 'S4', trays: [{ k: 'mutkhe', t: 9000, T: 21600 }, { k: 'otkho', t: 0, T: 1 }], done: 3, made: { mutkhe: 1 } }; m.gio = { d: '', n: 0, t: 0, on: 0, done: 2 };\n  for (const [id, k, g] of [['N1', 'mongtoi', 1.3], ['N2', 'daubap', .8], ['N3', 'bap', 1.3], ['N6', 'khoqua', .6], ['N7', 'cai', 1.3], ['N8', 'hanh', 1.3]]){ if (!CROPS[k]) continue; m.open.push(id); m.plots[id] = pl0(k, g, .85); m.plots[id].soil = .95; }")
# đắp xong việc trả xu thì cập nhật ô (dọn tre gai)
rep("  ST.qd = ST.qd || {}; ST.qd[n] = 1; if (q.exp){ ST.exp = 1; } save(); hud(); checkLevel();","  ST.qd = ST.qd || {}; ST.qd[n] = 1; if (q.exp){ ST.exp = 1; } if (n === 12){ for (const P of PLOTS) if (P.zone === 'sau') refreshPlot(P.id); for (let i = 0; i < 40; i++) puff('leaf', R(SAU.x0, SAU.x0 + 4.4), .3, R(SAU.z0, SAU.z0 + 1.4), 1, pick(['#5a8e3a', '#7aa84a', C.bamboo]), .9); say('Dọn sạch tre gai rồi! Mười ô sau nhà đất còn tơi, con đắp liếp trồng gì cũng được.', 'vui', { now: true }); } save(); hud(); checkLevel();")
a="/* --- câu cá ở bến"
assert s.count(a)==1
s=s.replace(a,open('f_block.js',encoding='utf8').read()+a)
open(p,'w',encoding='utf8').write(s); print('ok')
