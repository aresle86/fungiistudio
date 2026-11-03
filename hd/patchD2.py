p='live/vuon3d.html';s=open(p,encoding='utf8').read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:90]); s=s.replace(a,b)
# tick
rep("bepTick(t); vitTick(t); }","bepTick(t); vitTick(t); } catch (e) { if (!window.__oe) { window.__oe = 1; console.warn(\"odd\", e); } } try { nongTick(t); ")
# chạm
rep("  if (bepHitAt(e.clientX, e.clientY)){ if ((ST.lv || 1) >= BEP.lv",
"""  if (nongHit(e.clientX, e.clientY)){ nong.takeAll(); openSheet('nong'); return; }
  { const hid = g.id || plotHit(e.clientX, e.clientY), HP = hid && PL[hid];
    if (SUA && SUA.move === 'nong'){ if (HP && HP.bai && locked(HP) && ST.nong.at !== hid && nong.place(hid)){ SUA.move = null; suaTx(); for (const P of PLOTS) if (P.bai) refreshPlot(P.id); say('Đặt nong ở đây rồi nè. Chạm nong mà phơi đồ nghe con.', 'vui', { now: true }); } else say('Nong chỉ đặt được trên ô cỏ ở bãi hông nhà con.', 'dan', { now: true }); return; }
    if (HP && HP.bai && ST.nong.own && ST.nong.at === hid){ nong.takeAll(); openSheet(SUA ? 'plot' : 'nong', hid); return; }
    if (HP && HP.bai && (SUA || locked(HP))){ openSheet('plot', hid); return; } }
  if (bepHitAt(e.clientX, e.clientY)){ if ((ST.lv || 1) >= BEP.lv""")
# sheet
rep("    if (P.bai){ shT.textContent = suaTitle(arg); h += suaHTML(arg); shB.innerHTML = h; return; }",
"    if (P.bai && (SUA || locked(P) || (ST.nong.own && ST.nong.at === arg))){ shT.textContent = suaTitle(arg); h += suaHTML(arg); shB.innerHTML = h; return; }")
rep("function suaHTML(id){ const P = PL[id], p = ST.plots[id], N = ST.nong; let h = `<div class=\"meta\">${esc(P.name)}</div>`;","function suaHTML(id){ const P = PL[id], p = ST.plots[id], N = ST.nong; let h = '';")
rep("  if (kind === 'vit'){ shT.textContent = 'Chuồng vịt'; h += vitHTML(); }","  if (kind === 'vit'){ shT.textContent = 'Chuồng vịt'; h += vitHTML(); }\n  if (kind === 'nong'){ shT.textContent = 'Nong phơi'; h += nongHTML(); }")
rep("  else if (a === 'openbed'){ act.openBed(id); }",
"""  else if (a === 'openbed'){ act.openBed(id); }
  else if (a === 'nput'){ nong.put(+b.dataset.n, b.dataset.k); } else if (a === 'ntake'){ nong.take(+b.dataset.n); } else if (a === 'nbuy'){ const at = SHEET && SHEET.kind === 'plot' ? SHEET.arg : null; closeSheet(); nong.buy(at); return; } else if (a === 'nhere'){ nong.place(id); }
  else if (a === 'nopen'){ openSheet('nong'); return; } else if (a === 'nmove'){ closeSheet(); suaOn(true, 'nong'); return; } else if (a === 'bsan'){ baiSan(id); } else if (a === 'suaon'){ closeSheet(); suaOn(true); return; }""")
# chợ mua: bộ nong
rep("    if ((ST.lv || 1) >= NB2.lv) h += `<div class=\"srow\"><div class=\"sic\"><img src=\"${UIC.task}\" alt=\"\"></div><div class=\"sn\"><b>Bù nhìn rơm</b>",
"    if (nongOn()) h += `<div class=\"srow\"><div class=\"sic\"><img src=\"${ICON.nong}\" alt=\"\"></div><div class=\"sn\"><b>Bộ nong phơi</b>${stI('coin', NONG.buy + ' xu')}<span class=\"mkh\">4 nong tre, đặt ở bãi hông nhà</span></div><span></span><button class=\"btn sall\" data-a=\"nbuy\" ${ST.nong.own || ST.xu < NONG.buy ? 'disabled' : ''}>${ST.nong.own ? 'Đã có' : 'Mua'}</button></div>`;\n    if ((ST.lv || 1) >= NB2.lv) h += `<div class=\"srow\"><div class=\"sic\"><img src=\"${UIC.task}\" alt=\"\"></div><div class=\"sn\"><b>Bù nhìn rơm</b>")
# lên cấp 7
rep("  if (n === GA.buyLv) say('Con mua thêm gà, nâng chuồng, ấp trứng được rồi đó. Chạm vô chuồng gà mà coi.', 'vui', { idle: true }); }",
"""  if (n === GA.buyLv) say('Con mua thêm gà, nâng chuồng, ấp trứng được rồi đó. Chạm vô chuồng gà mà coi.', 'vui', { idle: true });
  if (n === BAI.lv){ say('Ngoại phát sạch bãi cỏ bên hông nhà rồi. Mười hai ô đó con muốn đắp liếp hay đặt nong phơi chỗ nào là tùy con. Bấm nút Sửa vườn mà làm.', 'vui', { idle: true }); setTimeout(() => { if (!VISIT) camTo(new T.Vector3(BAIC.x + .4, .3, BAIC.z + .3), Math.max(cam.zoom, DEFZ() * 1.1)); }, 1600); } }""")
rep("${n === 6 ? ', chuồng vịt ven mương, lục bình cho vịt ăn' : ''}","${n === 6 ? ', chuồng vịt ven mương, lục bình cho vịt ăn' : ''}${n === 7 ? ', bãi hông nhà 12 ô, Sửa vườn, nong phơi ớt' : ''}")
rep("  9: { t: 'goal', txt: 'Giao 5 đơn hàng',",
"""  8: { t: 'goal', txt: 'Đắp liếp bãi hông nhà, phơi mẻ ớt đầu', how: 'Bấm Sửa vườn, đắp 2 liếp ở bãi hông nhà. Mua bộ nong ở chợ, phơi xong một mẻ', goals: [['Đắp 2 liếp bãi hông nhà', () => ST.open.filter(i => i[0] === 'H').length, 2], ['Phơi xong 1 mẻ', () => (ST.nong && ST.nong.done) || 0, 1]] },
  9: { t: 'goal', txt: 'Giao 5 đơn hàng',""")
# camera tới được bãi
rep("tg.x = Math.max(-1, Math.min(11.5, tg.x));","tg.x = Math.max(baiOn() ? -3 : -1, Math.min(11.5, tg.x));")
# đơn hàng: đồ phơi
rep("if (gaOn()) pool.push('trungga'); if (vitOn()) pool.push('trungvit');","if (gaOn()) pool.push('trungga'); if (vitOn()) pool.push('trungvit'); try { for (const k of Object.keys(ST.nong.made || {})) if (PHOI[k]) pool.push(k); } catch (e) {}")
rep("const known = pool.filter(k => k === 'trungga' || k === 'trungvit' ||","const known = pool.filter(k => k === 'trungga' || k === 'trungvit' || PHOI[k] ||")
rep("const items = pick2.map(k => { const g = GD(k), base = (k === 'trungga' || k === 'trungvit') ?","const items = pick2.map(k => { const g = GD(k), base = PHOI[k] ? 1 : (k === 'trungga' || k === 'trungvit') ?")
rep("trungvit: 'luộc chấm muối tiêu',","trungvit: 'luộc chấm muối tiêu', otkho: 'giã muối ớt', chuoiphoi: 'cho tụi nhỏ ăn vặt',")
# vườn mẫu có bãi + nong
rep("  for (const [id, k, g] of [['D1', 'bap', .5], ['D1b', 'cai', 1.3]]){ m.plots[id] = pl0(k, g, .85); m.plots[id].soil = .95; }   // góc vườn mới có sẵn ở vườn mẫu",
"""  for (const [id, k, g] of [['D1', 'bap', .5], ['D1b', 'cai', 1.3]]){ m.plots[id] = pl0(k, g, .85); m.plots[id].soil = .95; }   // góc vườn mới có sẵn ở vườn mẫu
  for (const [id, k, g] of [['H1', 'ot', 1.3], ['H2', 'ot', .6], ['H5', 'cai', 1.3], ['H6', 'hanh', .8], ['H9', 'cachua', 1.3], ['H10', 'mongtoi', .5]]){ m.open.push(id); m.plots[id] = pl0(k, g, .85); m.plots[id].soil = .95; }
  m.nong = { own: 1, at: 'H3', trays: [{ k: 'otkho', t: 0, T: 1 }, { k: 'otkho', t: 7000, T: 14400 }, { k: 'chuoiphoi', t: 20000, T: 28800 }, null], done: 3, made: { otkho: 1 } };""")
open(p,'w',encoding='utf8').write(s); print('ok')
