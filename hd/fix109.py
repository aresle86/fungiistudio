# v109 — gà vịt + đơn hàng (anh Ares duyệt 4/11/2026; xem hd/ga-vit-raso.md, hd/don-hang-v109.md)
#  Gà: bỏ nút "Ấp 1 trứng"; để 2–6 trứng trong ổ cho mái nằm ấp (ổ lớn theo chuồng), 85% trứng nở (ít nhất một nửa),
#      gà mái nằm ổ thấy được, gà con chỉ hiện lúc gà mẹ dẫn (sửa lỗi gà con hiện mãi), thẻ kết quả ở lại trong bảng,
#      trống dư để bán giống (đơn hàng xóm) hay Ngoại bán; gà ấp và gà dẫn con không đẻ; chợ mỗi ngày 1 gà mái tơ.
#  Vịt: số vịt lớn ngoài sân khớp số nuôi, vịt con chỉ hiện 12 tiếng sau khi lò nở; lò ấp có ngả "lấy làm hột vịt lộn".
#  Đơn hàng xóm: luôn có rau, đa dạng theo cấp (trứng, đồ phơi/muối/sấy, cá, món nấu, gà trống giống, hột vịt lộn),
#      chỉ đặt món làm được, cá trong mọi đơn + việc ≤ 3, rau lâu chưa đặt được ưu tiên, mỗi hàng xóm có món ruột,
#      "Để bữa khác" 3 lần/ngày đổi đơn ngay. Đơn ghe giữ nguyên.
# Dùng: python3 fix109.py live/v108a.html live/v109a.html
import sys
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (a[:80], c, n); s = s.replace(a, b)
def span(a, z, b):
    """thay đoạn từ a tới hết z (a, z đều duy nhất, z nằm sau a)"""
    global s
    assert s.count(a) == 1, (a[:60], s.count(a)); i = s.index(a); j = s.index(z, i); assert j > i, z[:40]
    s = s[:i] + b + s[j + len(z):]

# ---------- món mới ----------
rep("const EXTRA = { matong: { name: 'Mật ong', sell: 70, unit: 'hũ' },",
    "const EXTRA = { hotvitlon: { name: 'Hột vịt lộn', sell: 55, unit: 'trứng' }, gatrong: { name: 'Gà trống giống', sell: 110, unit: 'con', nosell: true }, matong: { name: 'Mật ong', sell: 70, unit: 'hũ' },")
rep("const STORE = k => (DISH[k]", "const STORE = k => k === 'gatrong' ? (ST.ga || {}) : (DISH[k]")
rep("$('#icSeed').src = UIC.seedbag;",
    "$('#icSeed').src = UIC.seedbag; ICON.gatrong = ICON.trong; ICON.hotvitlon = ICON.trungvit; try { const im = new Image(); im.onload = () => { const c = document.createElement('canvas'), w = c.width = im.width, h = c.height = im.height, x = c.getContext('2d'); x.drawImage(im, 0, 0); x.save(); x.beginPath(); x.ellipse(w * .5, h * .34, w * .17, h * .07, 0, 0, 7); x.fillStyle = '#6B5530'; x.fill(); x.lineWidth = Math.max(2, w * .025); x.strokeStyle = '#FBF2DC'; x.beginPath(); for (let i = 0; i <= 12; i++){ const a = Math.PI + i / 12 * Math.PI * 2, r = i % 2 ? .19 : .16; x.lineTo(w * .5 + Math.cos(a) * w * r, h * .34 + Math.sin(a) * h * r * .45); } x.stroke(); x.restore(); ICON.hotvitlon = c.toDataURL(); }; im.src = ICON.trungvit; } catch (e) {}")

# ---------- gà ----------
rep("roosterSell: 80, nestMax: 3 };", "roosterSell: 80, nestMax: 3, clutch: [3, 4, 5, 6], hatchP: .85, maxRooster: [1, 1, 2, 2] };")
rep("gaLaying = () => ST.ga.hens - (ST.ga.brood && ST.ga.brood.stage === 'egg' ? 1 : 0);", "gaLaying = () => ST.ga.hens - (ST.ga.brood ? 1 : 0);   /* gà ấp và gà mẹ dẫn con đều không đẻ */")
span("const b = g.brood; if (b){ b.t += dt; if (b.stage === 'egg' && b.t >= GA.brood){",
     "g.news = female ? 'maiban' : 'trongban'; } } } }",
     """const b = g.brood; if (b){ b.t += dt; const n0 = b.n || 1;
    if (b.stage === 'egg' && b.t >= GA.brood){ let c = 0; for (let i = 0; i < n0; i++) if (Math.random() < GA.hatchP) c++; c = Math.max(Math.ceil(n0 / 2), c); b.stage = 'chick'; b.t = 0; b.c = c; g.hatched = (g.hatched || 0) + c; g.news = 'no'; try { aud('chiep'); } catch (e) {} }
    else if (b.stage === 'chick' && b.t >= GA.grow){ const c = b.c || 1, mr = GA.maxRooster[g.lv] || 1, r = { n: n0, c, mai: 0, trong: 0, giong: 0, ban: 0, xu: 0 }; g.brood = null;
      for (let i = 0; i < c; i++){ if (Math.random() < .5){ if (g.hens + g.rooster < gaCap()){ g.hens++; r.mai++; } else { r.ban++; r.xu += GA.roosterSell; } } else if (g.rooster < mr && g.hens + g.rooster < gaCap()){ g.rooster++; r.trong++; } else if ((g.gatrong || 0) < 2){ g.gatrong = (g.gatrong || 0) + 1; r.giong++; } else { r.ban++; r.xu += GA.roosterSell; } }
      ST.xu += r.xu; g.res = r; g.news = 'lon'; } } }""")
# gà con theo số con nở, chỉ lúc gà mẹ dẫn; vịt lớn khớp số nuôi; vịt con 12 tiếng sau khi lò nở
rep("for (const [x, z] of [[.6, 3.8], [.7, 3.7], [.55, 3.95], [.4, 4.5]]){ addA(chick(x, z, R(0, 6)), 'chick', { rad: .3, spd: .22 }); ANIM[ANIM.length - 1].gaC = 1; }",
    "[[.6, 3.8], [.7, 3.7], [.55, 3.95], [.4, 4.5]].forEach(([x, z], i) => { addA(chick(x, z, R(0, 6)), 'chick', { rad: .3, spd: .22 }); ANIM[ANIM.length - 1].gaC = i + 1; });")
rep("addA(duck(2.0, mz2, 0, { swim: true }), 'swim', { line: [1.3, 4.6, mz2], spd: .09 }); addA(duckling(2.3, mz2 + .04, 0, true), 'swim', { line: [1.3, 4.6, mz2 + .04], spd: .09 }); addA(duckling(2.5, mz2 - .03, .1, true), 'swim', { line: [1.3, 4.6, mz2 - .03], spd: .09 });",
    "addA(duck(2.0, mz2, 0, { swim: true }), 'swim', { line: [1.3, 4.6, mz2], spd: .09 }); ANIM[ANIM.length - 1].vitA = 1; addA(duckling(2.3, mz2 + .04, 0, true), 'swim', { line: [1.3, 4.6, mz2 + .04], spd: .09 }); ANIM[ANIM.length - 1].vitC = 1; addA(duckling(2.5, mz2 - .03, .1, true), 'swim', { line: [1.3, 4.6, mz2 - .03], spd: .09 }); ANIM[ANIM.length - 1].vitC = 1;")
rep("addA(duck(.5, 5.2, 1.7, { brown: true }), 'duck', { rad: .35, spd: .1 }); addA(duck(.35, 5.65, 1.2), 'duck', { rad: .35, spd: .1 });",
    "addA(duck(.5, 5.2, 1.7, { brown: true }), 'duck', { rad: .35, spd: .1 }); ANIM[ANIM.length - 1].vitA = 2; addA(duck(.35, 5.65, 1.2), 'duck', { rad: .35, spd: .1 }); ANIM[ANIM.length - 1].vitA = 3;")
rep("addA(duck(4.9, mz1, 3.14, { swim: true, brown: true }), 'swim', { line: [1.4, 5.8, mz1], spd: .07 });",
    "addA(duck(4.9, mz1, 3.14, { swim: true, brown: true }), 'swim', { line: [1.4, 5.8, mz1], spd: .07 }); ANIM[ANIM.length - 1].vitA = 4;")
rep("function vitSpawn(){ while (VITV.extra.length < Math.max(0, ST.vit.n - 2)){", "function vitSpawn(){ while (VITV.extra.length < Math.max(0, ST.vit.n - 4)){")
rep("const chicks = on && ((g.hatched || 0) > 0 || (g.brood && g.brood.stage === 'chick')), vo = (() => { try { return vitOn(); } catch (e) { return true; } })(); for (const a of ANIM){ if (a.kind === 'hen') a.g.visible = on; else if (a.gaC) a.g.visible = chicks; else if (a.kind === 'duck' || a.vitC) a.g.visible = vo; } }",
    "const chicks = on && g.brood && g.brood.stage === 'chick' ? Math.min(4, g.brood.c || 1) : 0, vo = (() => { try { return vitOn(); } catch (e) { return true; } })(), vn = (ST.vit && ST.vit.n) || 0, kid = vo && Date.now() - ((ST.lo && ST.lo.kid) || 0) < GA.grow * 1000 / (ST.spd || 1); for (const a of ANIM){ if (a.kind === 'hen') a.g.visible = on; else if (a.gaC) a.g.visible = a.gaC <= chicks; else if (a.vitA) a.g.visible = vo && a.vitA <= vn; else if (a.vitC) a.g.visible = kid; else if (a.kind === 'duck') a.g.visible = vo; } }\n  if (GAV.sit) GAV.sit.visible = on && !!(g.brood && g.brood.stage === 'egg');")
# gà mái nằm ổ lúc ấp
rep("  v.extra = []; return v; })();", "  v.extra = []; v.sit = hen(NEST.x + .02, NEST.z, -1.4); v.sit.position.y = NEST.y - .07; v.sit.scale.set(.95, .72, .95); v.sit.visible = false; return v; })();")
# trống thứ hai (chuồng 9 con trở lên)
rep("function gaSpawn(){ while (GAV.extra.length < Math.max(0, ST.ga.hens - 2)){",
    "function gaSpawn(){ if ((ST.ga.rooster || 0) >= 2 && !GAV.r2){ GAV.r2 = rooster(.2, 4.6, 1.2); addA(GAV.r2, 'hen', { rad: .45 }); } while (GAV.extra.length < Math.max(0, ST.ga.hens - 2)){")
# báo tin: nở, lớn
span("if (on && g.news){ const m = {", "say(m, 'vui'); hud(); save(); } }",
     """if (on && g.news){ const nw = g.news, b = g.brood, r = g.res || {}; g.news = null; gaSpawn();
    if (nw === 'no' && b){ say(`Gà con nở rồi con! ${b.c}/${b.n || 1} trứng nở, gà mẹ đang dẫn đi kiếm mồi.`, 'vui'); try { floatAt(NEST.x, .9, NEST.z, `+${b.c} gà con`, '#9fd36a'); } catch (e) {} }
    else if (nw === 'lon'){ const p = []; if (r.mai) p.push(r.mai + ' gà mái'); if (r.trong) p.push(r.trong + ' gà trống'); say(`Bầy gà con lớn rồi con. ${p.length ? 'Chuồng có thêm ' + p.join(', ') : 'Chuồng hết chỗ rồi'}${r.giong ? `, ${r.giong} con trống để dành bán giống` : ''}${r.ban ? `, Ngoại bán ${r.ban} con được ${r.xu} xu` : ''}.`, 'vui'); try { floatAt(COOPC.x, 1, COOPC.z, `+${(r.mai || 0) + (r.trong || 0)} gà`, '#9fd36a'); } catch (e) {} }
    hud(); save(); } }""")
# hành động
span("  hatch(){ const g = ST.ga; if ((ST.lv || 1) < GA.buyLv || g.brood) return;", "Con gà đang ấp thì không đẻ nghe.`, 'vui'); save(); hud(); } };",
     """  brood(){ const g = ST.ga, n = Math.min(g.eggs, GA.clutch[g.lv] || 3); if ((ST.lv || 1) < GA.buyLv || g.brood) return; if (!g.rooster) return say('Phải có gà trống thì trứng mới ấp ra con được.', 'dan'); if (g.hens < 2) return say('Cần ít nhất 2 gà mái: một con nằm ấp, một con đẻ.', 'dan'); if (n < 2) return toast('Ổ cần ít nhất 2 trứng mới cho gà nằm ấp được con.', 'dan');
    g.eggs -= n; g.brood = { stage: 'egg', t: 0, n }; say(`Con mái vàng đòi ấp rồi. Ngoại để lại ${n} trứng cho nó nằm, chừng ${Math.round(GA.brood / 3600)} tiếng là nở. Gà nằm ấp với lúc dẫn con thì không đẻ nghe.`, 'vui'); sfx('pop'); save(); hud(); } };""")
rep("else if (a === 'gahatch') ga.hatch();", "else if (a === 'gabrood') ga.brood(); else if (a === 'gares'){ ST.ga.res = null; save(); }")
rep("if (ST.xu < GA.buy) return toast(`Gà mái ${GA.buy} xu một con, còn thiếu ${GA.buy - ST.xu} xu.`, 'dan');\n    ST.xu -= GA.buy; g.hens++;",
    "if (g.buyD === dayKey()) return toast('Hôm nay chợ hết gà mái tơ rồi, mai có tiếp nghe con.', 'dan'); if (ST.xu < GA.buy) return toast(`Gà mái ${GA.buy} xu một con, còn thiếu ${GA.buy - ST.xu} xu.`, 'dan');\n    ST.xu -= GA.buy; g.hens++; g.buyD = dayKey();")
rep("sayOnce('egg1', 'Trứng gà ta đem chợ bán được giá lắm. Để dành một trứng, mai mốt ấp ra gà con.', 'vui');",
    "sayOnce('egg1', 'Trứng gà ta đem chợ bán được giá lắm. Muốn có gà con thì để trứng lại trong ổ cho gà mái nằm ấp.', 'vui');")
rep("how: 'Chạm chuồng gà, cho một mái nằm ổ ấp trứng. Gà nở xong mới lên cấp'", "how: 'Để từ 2 trứng trong ổ, chạm chuồng gà cho một mái nằm ấp. Gà con nở là lên cấp'")
# bảng chuồng gà
rep("const g = ST.ga, cap = gaCap(), lvOk = (ST.lv || 1) >= GA.buyLv, b = g.brood, lay = gaLaying(), tcap = g.hens * GA.trough, food = Math.floor(g.trough), nestCap = g.hens * GA.nestMax;",
    "const g = ST.ga, cap = gaCap(), lvOk = (ST.lv || 1) >= GA.buyLv, b = g.brood, lay = gaLaying(), tcap = g.hens * GA.trough, food = Math.floor(g.trough), nestCap = g.hens * GA.nestMax, nB = Math.min(g.eggs, GA.clutch[g.lv] || 3);")
rep("let h = '';\n  if (g.eggs > 0) h += UX.hero(ICON.trungga, `Có ${g.eggs} trứng chờ lượm`",
    "let h = '';\n  if (g.res){ const r = g.res, p = [r.mai ? r.mai + ' mái' : '', r.trong ? r.trong + ' trống' : '', r.giong ? r.giong + ' trống giống' : ''].filter(Boolean).join(' · '); h += UX.hero(ICON.mai, `Nở ${r.c}/${r.n} trứng, gà con lớn rồi`, `${p ? 'Thêm ' + p : 'Chuồng hết chỗ'}${r.ban ? ` · Ngoại bán ${r.ban} con +${r.xu} xu` : ''}`, 'go') + UX.cta([UX.btn('gares', 'Biết rồi', { g: 1 })]); }\n  if (b) h += UX.hero(b.stage === 'egg' ? ICON.trungga : ICON.mai, b.stage === 'egg' ? `Gà mái đang ấp ${b.n || 1} trứng` : `Gà mẹ dẫn ${b.c || 1} gà con`, b.stage === 'egg' ? 'Nở sau' : 'Lớn sau', 'go', [b.t / (b.stage === 'egg' ? GA.brood : GA.grow), '#86B06A', fmtS(((b.stage === 'egg' ? GA.brood : GA.grow) - b.t) / ST.spd)]);\n  if (g.eggs > 0) h += UX.hero(ICON.trungga, `Có ${g.eggs} trứng chờ lượm`")
rep("  if (b) h += '<div class=\"uxs one\">' + UX.card(b.stage === 'egg' ? 'Đang ấp trứng' : 'Gà con đang lớn', `còn ${fmtT(((b.stage === 'egg' ? GA.brood : GA.grow) - b.t) / ST.spd)}`, UX.mbar(b.t / (b.stage === 'egg' ? GA.brood : GA.grow), '#86B06A'), 'go') + '</div>';\n", "")
rep("`${g.hens}${g.rooster ? ' <small>+1</small>' : ''}`", "`${g.hens}${g.rooster ? ` <small>+${g.rooster}</small>` : ''}`")
rep("${g.rooster ? `<img src=\"${ICON.trong}\" alt=\"\">` : ''}${Array.from({ length: Math.max(0, cap - g.hens - g.rooster) }",
    "${Array.from({ length: g.rooster }, () => `<img src=\"${ICON.trong}\" alt=\"\">`).join('')}${Array.from({ length: Math.max(0, cap - g.hens - g.rooster) }")
rep("UX.card(`Đàn · ${g.hens + g.rooster}/${cap} chỗ`", "UX.card(`Đàn · ${g.hens + g.rooster}/${cap} chỗ${g.gatrong ? ` · ${g.gatrong} trống giống` : ''}`")
rep("why = b ? 'đang ấp một lứa' : !g.rooster ? 'cần gà trống' : g.hens < 2 ? 'cần 2 gà mái' : !(ST.inv.trungga > 0) ? 'cần 1 trứng trong kho' : '';",
    "why = b ? 'đang có một ổ' : !g.rooster ? 'cần gà trống' : g.hens < 2 ? 'cần 2 gà mái' : nB < 2 ? 'ổ cần 2 trứng trở lên' : '', bt = g.buyD === dayKey();")
rep("UX.upc('gabuy', ICON.mai, 'Mua gà mái', GA.buy, { dis: full || ST.xu < GA.buy, why: full ? 'chuồng hết chỗ' : '' })",
    "UX.upc('gabuy', ICON.mai, 'Gà mái tơ ở chợ', GA.buy, { dis: full || bt || ST.xu < GA.buy, why: full ? 'chuồng hết chỗ' : bt ? 'mai chợ có gà tiếp' : '' })")
rep("UX.upc('gahatch', ICON.trungga, 'Ấp 1 trứng', null, { dis: !!why, why: why || 'nở sau ' + fmtT(GA.brood / ST.spd) })",
    "UX.upc('gabrood', ICON.trungga, `Để ${Math.max(2, nB)} trứng cho gà ấp`, null, { dis: !!why, why: why || `ổ tối đa ${GA.clutch[g.lv] || 3} trứng · nở sau ${fmtT(GA.brood / ST.spd)}` })")

# ---------- lò ấp vịt: hai ngả ----------
rep("const LO = { lv: 14, eggs: 4, cui: 1, t: 18 * 3600, first: 60, at: [-1.45, 6.3], sellDuck: 40 };",
    "const LO = { lv: 14, eggs: 4, cui: 1, t: 18 * 3600, first: 60, at: [-1.45, 6.3], sellDuck: 40, lon: .6 };   /* ấp được 60% thì lấy ra làm hột vịt lộn được */")
rep("const lo = {\n", "const lo = {\n  lon(){ const L = ST.lo; if (!L.on || L.t <= 0 || 1 - L.t / (L.T || LO.t) < LO.lon) return; const n = L.n || LO.eggs; ST.inv.hotvitlon = (ST.inv.hotvitlon || 0) + n; L.on = 0; L.n = 0; L.t = 0; L.lon = (L.lon || 0) + 1; try { floatAt(LO.at[0], .7, LO.at[1], `+${n} hột vịt lộn`); } catch (e) {} sfx('pop'); gainXP(4); say('Hột vịt lộn luộc chín chấm muối tiêu chanh, ăn với rau răm. Chiều chiều hàng xóm hay ghé hỏi mua đó con.', 'vui'); save(); hud(); },\n")
rep("L.hatch = wait; if (!wait){ L.on = 0; L.n = 0; } L.done++;", "L.hatch = wait; if (!wait){ L.on = 0; L.n = 0; } L.done++; L.kid = Date.now();")
rep("a === 'loput'){ lo.put(); }", "a === 'loput'){ lo.put(); } else if (a === 'lolon'){ lo.lon(); }")
rep("h += UX.cta([L.on && L.t <= 0 ? UX.btn('lohatch', 'Bắt vịt con', { g: 1, img: ICON.vitcon }) : !L.on ?",
    "h += UX.cta([L.on && L.t > 0 && 1 - L.t / (L.T || LO.t) >= LO.lon ? UX.btn('lolon', `Lấy ${L.n || LO.eggs} hột vịt lộn`, { img: ICON.hotvitlon }) : '', L.on && L.t <= 0 ? UX.btn('lohatch', 'Bắt vịt con', { g: 1, img: ICON.vitcon }) : !L.on ?")
rep("chừng ${LO.t / 3600} tiếng là nở. Vịt con vô chuồng chung với đàn, chuồng hết chỗ thì Ngoại bán cho hàng xóm.`",
    "chừng ${LO.t / 3600} tiếng là nở. Vịt con vô chuồng chung với đàn, chuồng hết chỗ thì Ngoại bán cho hàng xóm. Ấp được hơn nửa đường thì lấy ra luộc làm hột vịt lộn được, bán giá hơn trứng vịt.`")

# ---------- đơn hàng xóm ----------
rep("const ORD = { lv: 3, max: 3, every: 25 * 60, again: 10 * 60, mul: 1.3 };", "const ORD = { lv: 3, max: 3, every: 25 * 60, again: 10 * 60, mul: 1.3, skip: 3, fish: 3 };")
rep("function ordMake(kind){ const lv = ST.lv || 1, pool = Object.keys(CROPS)", "function ordMakeOld(kind){ const lv = ST.lv || 1, pool = Object.keys(CROPS)")
rep("function ordSim(dt){", """const NBFAV = { 'Cô Tư': ['cachua', 'daubap', 'raumuong'], 'Chú Bảy': ['khoqua', 'ot'], 'Dì Út': ['bap', 'cai'], 'Thím Ba': ['mongtoi', 'hanh'], 'Ông Sáu': ['cai', 'khoqua'], 'Bé Na': ['bap', 'cachua'], 'Cô Hai': ['raumuong', 'hanh'], 'Chú Năm': ['ot', 'daubap'] };   /* món ruột mỗi nhà */
const ORDCOMBO = [[['caloc', 'cachua'], 'nấu canh chua cá'], [['cachua', 'daubap'], 'nấu canh chua'], [['cachua', 'raumuong'], 'nấu canh chua'], [['hanh', 'trungga'], 'chiên trứng hành'], [['khoqua', 'trungga'], 'xào khổ qua trứng'], [['mongtoi', 'hanh'], 'nấu canh cua'], [['cai', 'hanh'], 'xào tỏi ăn cơm'], [['caro', 'ot'], 'kho tộ'], [['raumuong', 'trungvit'], 'luộc rau chấm trứng'], [['dacai', 'cai'], 'ăn với thịt kho'], [['hotvit', 'hanh'], 'ăn cháo trắng'], [['otkho', 'xoai'], 'giã muối ớt chấm xoài'], [['hotvitlon', 'raumuong'], 'ăn chiều'], [['chep', 'cai'], 'cúng ông Táo'], [['gatrong', 'ot'], 'gây giống gà']];
function ordFishLeft(){ let n = 0; for (const o of (ST.ord.list || [])) for (const [k, q] of o.items) if (FISHK[k]) n += q; try { for (const x of ((ST.tasks || {}).list || [])) if (x.t === 'fish' && !x.done) n += x.need - x.have; } catch (e) {} return Math.max(0, ORD.fish - n); }   /* câu 5 con/ngày: đơn + việc không giành quá 3 */
function ordCanMake(k, d = 0){ const lv = ST.lv || 1; if (d > 3) return false;
  if (CROPS[k]) return unlocked(k) && !CROPS[k].rare && (CROPS[k].tree ? PLOTS.some(P => P.tree === k && ST.plots[P.id] && ST.plots[P.id].crop) : CROPS[k].kind !== 'trellis' || PLOTS.some(P => P.trellis));
  if (k === 'trungga') return gaOn(); if (k === 'trungvit') return vitOn(); if (k === 'hotvitlon') return loOn() && (ST.lo.lon || 0) > 0; if (k === 'gatrong') return (ST.ga.gatrong || 0) > 0;
  if (FISHK[k]){ const f = FISHK[k]; return cauOn() && f.tier <= (lv >= 15 ? 2 : 1) && (!f.mua || (f.mua === 'nn' ? NN_ON : f.mua === muaSong())); }   /* loài câu được ở mùa này, không cần câu được hôm nay */
  const R2 = PHOI[k] || MUOI[k] || SAY[k] || DISH[k]; if (!R2 || k === 'gio' || k === 'lucbinhkho' || lv < (R2.lv || 1)) return false;
  if (PHOI[k] && !(ST.nong && ST.nong.own)) return false; if (MUOI[k] && !(ST.khap && ST.khap.own)) return false; if (SAY[k] && !(ST.say && ST.say.own)) return false; if (DISH[k] && !ST.bep) return false;
  return Object.keys(R2.in || {}).every(i => i === 'cui' || i === 'muoi' || i === 'duong' || i === 'rom' || ordCanMake(i, d + 1)); }
function ordMake(kind){ if (kind === 'ghe') return ordMakeOld(kind); const lv = ST.lv || 1, L0 = ST.ord.list || [], open = new Set(L0.flatMap(o => o.items.map(([k]) => k))), last = ST.ord.last = ST.ord.last || {}, now = Date.now();
  const used = new Set(L0.map(o => o.who)), free = NB.filter(n => !used.has(n)), who = free[Math.floor(Math.random() * free.length)] || NB[0], fav = NBFAV[who] || [];
  const ok = k => !open.has(k) && ordCanMake(k), pickW = (ks, w) => { if (!ks.length) return null; const ws = ks.map(w); let r = Math.random() * ws.reduce((a, b) => a + b, 0); for (let i = 0; i < ks.length; i++){ r -= ws[i]; if (r <= 0) return ks[i]; } return ks[ks.length - 1]; }, pick1 = ks => ks.length ? ks[Math.floor(Math.random() * ks.length)] : null;
  const items = [], add = (k, q) => { if (k && q > 0 && !items.some(([x]) => x === k)) items.push([k, q]); };
  const vegs = Object.keys(CROPS).filter(k => !CROPS[k].tree && ok(k)), vegW = k => (1 + Math.min(3, (now - (last[k] || 0)) / 864e5)) * (fav.includes(k) ? 2 : 1);   /* lâu chưa đặt thì hay đặt, món ruột nhà đó gấp đôi */
  const qVeg = k => { const c = CROPS[k]; return Math.max(2, Math.min(Math.ceil(c.yield * 1.6), Math.round(c.yield * (.8 + Math.random() * .6)))) + (lv >= 10 ? 1 : 0); };
  const nItems = lv < 5 ? (Math.random() < .4 ? 2 : 1) : lv < 11 ? 2 : lv < 15 ? 2 + (Math.random() < .5 ? 1 : 0) : 3;
  const dishes = lv >= 8 ? Object.keys(DISH).filter(ok) : []; if (dishes.length && Math.random() < (lv >= 15 ? .35 : lv >= 11 ? .3 : .2)) add(pick1(dishes), 1);   /* đơn món nấu, vẫn kèm rau */
  const main = pickW(vegs, vegW); if (main) add(main, qVeg(main));
  const pre = Object.keys({ ...PHOI, ...MUOI, ...(lv >= 11 ? SAY : {}) }).filter(ok), fish = Object.keys(FISHK).filter(ok), eggs = ['trungga', 'trungvit'].filter(ok), spec = ['gatrong', 'hotvitlon'].filter(ok), fl = ordFishLeft();
  const sideOf = c => c === 'egg' ? (k => k && [k, k === 'trungga' ? 3 : 2])(pick1(eggs)) : c === 'pre' ? (k => k && [k, k === 'dacai' || k === 'hotvit' ? 2 : 1])(pick1(pre)) : c === 'fish' ? (k => k && fl > 0 && [k, Math.min(fl, FISHK[k].tier ? 1 : 2)])(pick1(fish)) : c === 'spec' ? (k => k && [k, k === 'gatrong' ? 1 : 2 + Math.floor(Math.random() * 3)])(pick1(spec)) : null;
  const W = lv < 5 ? [] : lv < 8 ? [['egg', 1]] : lv < 11 ? [['egg', .45], ['pre', .55]] : lv < 15 ? [['egg', .3], ['pre', .4], ['fish', .3]] : [['egg', .2], ['pre', .3], ['fish', .3], ['spec', .2]];
  if (W.length && items.length < nItems && (lv >= 8 || Math.random() < .35)){ for (let tries = 0; tries < 4 && items.length < nItems; tries++){ const s0 = sideOf(pickW(W.map(x => x[0]), c => W.find(x => x[0] === c)[1])); if (s0){ add(...s0); break; } } }
  while (items.length < nItems){ const k = pickW(vegs.filter(v => !items.some(([x]) => x === v)), vegW); if (!k) break; add(k, qVeg(k)); }
  if (!items.length) return ordMakeOld(kind); for (const [k] of items) last[k] = now;
  const ks = items.map(([k]) => k), combo = ORDCOMBO.find(([a]) => a.every(x => ks.includes(x)));
  const val = items.reduce((s2, [k, q]) => s2 + q * GD(k).sell, 0); return { id: Date.now() + '' + Math.floor(Math.random() * 1e4), who, why: DISH[ks[0]] ? 'đãi khách' : combo ? combo[1] : (NBWHY[main] || 'nấu cơm chiều'), items, xu: Math.round(val * ORD.mul / 5) * 5, xp: 1 + items.length * 2 }; }
function ordSim(dt){""")
rep("function ordDrop(id){ const i = ST.ord.list.findIndex(o => o.id === id); if (i < 0) return; ST.ord.list.splice(i, 1); ST.ord.acc = Math.max(ST.ord.acc, ORD.every - ORD.again); save(); }",
    "const ordSkip = () => ST.ord.skip && ST.ord.skip.d === dayKey() ? ST.ord.skip : (ST.ord.skip = { d: dayKey(), n: 0 });\nfunction ordDrop(id){ const i = ST.ord.list.findIndex(o => o.id === id); if (i < 0) return; const sk = ordSkip(); ST.ord.list.splice(i, 1); if (sk.n < ORD.skip){ sk.n++; try { ST.ord.list.splice(i, 0, ordMake()); } catch (e) {} } else ST.ord.acc = Math.max(ST.ord.acc, ORD.every - ORD.again); save(); }   /* để bữa khác: 3 lần/ngày có đơn mới liền */")
rep("let h = `<div class=\"sub\">Đơn nhà bên</div>`;", "const skl = ORD.skip - ordSkip().n; let h = `<div class=\"sub\">Đơn nhà bên${L.length ? `<small style=\"float:right;font-weight:600\">đổi đơn còn ${skl} lần hôm nay</small>` : ''}</div>`;")
rep("<button class=\"x ox\" data-a=\"orddrop\" data-k=\"${o.id}\" aria-label=\"Bỏ đơn này\">×</button>", "<button class=\"btn oskip\" data-a=\"orddrop\" data-k=\"${o.id}\">Để bữa khác</button>")
rep("</style><style id=\"s108\">", "</style><style id=\"s108\">\n.oa .oskip{min-height:36px!important;font-size:12px!important;padding:4px 8px!important}")
# lò sấy: ghi rõ sấy từ đồ tươi
rep("otkho: { ...PHOI.otkho, t: PHOI.otkho.t / 2 }, chuoiphoi: { ...PHOI.chuoiphoi, t: PHOI.chuoiphoi.t / 2 } };",
    "otkho: { ...PHOI.otkho, t: PHOI.otkho.t / 2, name: 'Ớt khô từ ớt tươi' }, chuoiphoi: { ...PHOI.chuoiphoi, t: PHOI.chuoiphoi.t / 2, name: 'Chuối khô từ chuối tươi' } };   /* phơi nong hay sấy lò đều làm từ đồ tươi, không phải hai bước */")

rep("const BUILD = 'v108a'", "const BUILD = 'v109a'")
open(dst, 'w', encoding='utf-8').write(s); print('ok', len(s))
