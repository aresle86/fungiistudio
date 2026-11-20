# v167 -> v168:
# Bến bà con ở màn 360x740: hai xuồng xa nhất không hiện bảng tên (ngưỡng ẩn 2,6 lần cỡ gốc; hai xuồng đó cần 2,77 và 2,91).
# Nới ngưỡng lên 3,0 để điện thoại 360 thấy đủ 8 bảng tên. Màn nhỏ hơn nữa vẫn ẩn như cũ, kéo tới gần thì hiện.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), n, a[:60])
    s = s.replace(a, b)
rep("BUILD = 'v167'", "BUILD = 'v168'")
rep("o.visible = !(q.far && (need > 2.6 || bk < .35))", "o.visible = !(q.far && (need > 3 || bk < .35))")
# Hai hàng bảng tên (xuồng bên trái / bên phải cầu) lúc hiện đủ thì hai bảng xa nhất chạm nhau ở giữa:
# bảng bên nào giữ bên đó, cách đường giữa cầu (x = 5) 4px mỗi bên -> hai bảng luôn hở 8px.
rep("if (dz > 0 && lim > 0){ const sh = Math.max(-lim, Math.min(lim, cx)) - cx;",
    "if (dz > 0 && lim > 0){ let c1 = cx; if (q.far){ const md = o.parent.localToWorld(new T.Vector3(5, q.p0.y, q.p0.z)).sub(C.position).dot(rt), hf = o.scale.x * ws.x / 2 + hw * 8 / innerWidth; c1 = q.p0.x < 5 ? Math.min(cx, md - hf) : Math.max(cx, md + hf); } const sh = Math.max(-lim, Math.min(lim, c1)) - cx;")

# ===== Tặng quà gom về một bảng + vú sữa/trầu bán được + cúng ông Địa =====
def fnspan(name):
    i = s.index('function ' + name + '('); k = s.index('{', s.index(')', i)); d = 0
    while True:
        if s[k] == '{': d += 1
        elif s[k] == '}':
            d -= 1
            if d == 0: break
        k += 1
    return i, k + 1
def repfn(name, new):
    global s
    assert s.count('function ' + name + '(') == 1, name
    i, j = fnspan(name); s = s[:i] + new + s[j:]

# --- B. vú sữa, trầu: bán được ở chợ (giu = không vô "Bán cả kho", không bày Bến bà con) ---
rep("trau: { name: 'Miếng trầu', sell: 0, unit: 'miếng', nosell: true }, vusua: { name: 'Trái vú sữa', sell: 0, unit: 'trái', nosell: true }",
    "trau: { name: 'Miếng trầu', sell: 20, unit: 'miếng', giu: true }, vusua: { name: 'Trái vú sữa', sell: 40, unit: 'trái', giu: true }")
rep("tot = items.reduce((s, [k, n]) => s + sellValue(k, n), 0);", "tot = items.filter(([k]) => !GD(k).giu).reduce((s, [k, n]) => s + sellValue(k, n), 0);")
rep("if (GD(k) && !GD(k).nosell && ST.inv[k] > 0) act.sell(k, ST.inv[k]); coinFly(b, 6);", "if (GD(k) && !GD(k).nosell && !GD(k).giu && ST.inv[k] > 0) act.sell(k, ST.inv[k]); coinFly(b, 6);")
rep("return !!(g && g.sell && !g.nosell && ICON[k] && !['duong',", "return !!(g && g.sell && !g.nosell && !g.giu && ICON[k] && !['duong',")
rep("const ok = k => GD(k) && GD(k).sell && !GD(k).nosell && ICON[k], tr = k =>", "const ok = k => GD(k) && GD(k).sell && !GD(k).nosell && !GD(k).giu && ICON[k], tr = k =>")
rep("return toast('Còn trái vú sữa trong kho, đem biếu bạn bè trước nghe.', 'dan');", "return toast('Kho còn đủ vú sữa rồi con. Đem tặng, cúng ông Địa hay bán bớt nghe.', 'dan');")
rep("return toast('Còn miếng trầu trong kho, đem mời khách trước nghe.', 'dan');", "return toast('Kho còn đủ trầu rồi con. Đem tặng hay bán bớt nghe.', 'dan');")
rep("sayOnce('vusua1', 'Trái vú sữa không bán đâu con. Chèo qua vườn bạn thì để lại một trái làm quà.', 'vui');",
    "sayOnce('vusua2', 'Trái vú sữa để tặng bạn, bán ở chợ cũng được. Nhà có miếu thì cúng ông Địa một trái, ổng mách nước cho.', 'vui');")
rep("sayOnce('trau1', 'Miếng trầu không bán đâu con. Chèo qua vườn bạn thì để lại một miếng làm quà, người ta vui lắm.', 'vui');",
    "sayOnce('trau2', 'Miếng trầu để tặng bạn, bán ở chợ cũng được nghe con.', 'vui');")

# --- C. cúng ông Địa một trái vú sữa: ổng mách một lời đồn cá quý / giống quý chưa có (mỗi ngày một lần) ---
rep("if (it) h += UX.hero(UIC['dc_' + it.k], DCK[it.k].name, 'Đang đặt ở ô này') + UX.cta([",
    "if (it) h += UX.hero(UIC['dc_' + it.k], DCK[it.k].name, 'Đang đặt ở ô này') + (it.k === 'mieu' ? diaCungHTML() : '') + UX.cta([")
rep("else if (a === 'dctake'){ dcTake(+b.dataset.k); closeSheet(); return; }",
    "else if (a === 'dctake'){ dcTake(+b.dataset.k); closeSheet(); return; }\n  else if (a === 'diacung'){ diaCung(); return; }")
rep("function diaTick(t){", r"""function diaCon(){ try { if (cauOn() && Object.keys(FISHK).some(k => FISHK[k].tier >= 3 && !(ST.fishLog[k] || {}).n && DONX.some(x => !donHas(k, x)))) return true; } catch (e) {} try { return !!(quyOn() && Object.keys(QUY).some(k => unlocked(QUY[k].base) && !(ST.quy && ST.quy.got && ST.quy.got[k]) && QCX.some(x => !quyHas(k, x)))); } catch (e) { return false; } }
function diaCungHTML(){ const D = diaState(), n = ST.inv.vusua || 0, h = `<div class="sub">Cúng ông Địa${n ? ` · con có ${n} trái vú sữa` : ''}</div>`;
  if (D.cd === dayKey()) return h + `<div class="note">Hôm nay con cúng rồi. Mai cúng tiếp, ông Địa mách thêm.</div>`;
  if (!diaCon()) return h + `<div class="note">Giờ ông Địa chưa có chuyện gì mới để mách. Khi nào có cá quý, giống quý con chưa gặp thì cúng nghe.</div>`;
  if (!n) return h + `<div class="note">Cúng một trái vú sữa, ông Địa mách chỗ câu cá quý hay cách kiếm giống quý con chưa có. Giờ kho con chưa có trái nào.</div>`;
  return h + `<div class="note">Cúng một trái vú sữa, ông Địa mách chỗ câu cá quý hay cách kiếm giống quý con chưa có.</div><div class="acts" style="margin-bottom:8px">${UX.btn('diacung', 'Cúng 1 trái vú sữa', { g: 1 })}</div>`; }
function diaCung(){ if (VISIT || DIA.on) return; const g = diaItem(), D = diaState(); if (!g || D.cd === dayKey() || !(ST.inv.vusua > 0)) return; const r = donAny(); if (!r || !r.txt){ toast('Giờ ông Địa chưa có chuyện gì mới để mách.', 'dan'); renderSheet(); return; }
  ST.inv.vusua--; D.cd = dayKey(); closeSheet(); if (!DIA.root) diaBuild(); DIA.root.position.set(g.position.x, 1.86, g.position.z - .12); try { camTo(new T.Vector3(g.position.x, .9, g.position.z), cam.zoom); } catch (e) {} DIA.on = true; DIA.t = 0; DIA.t0 = performance.now(); DIA.out = false; DIA.said = false; DIA.line = r.txt; DIA.life = 99; DIA.root.visible = true; save(); hud(); diaPuff(22); sfx('dia'); buzz(15); }
function diaTick(t){""")

# --- A. Tặng quà: một bảng duy nhất (chọn món -> kèm thư nếu muốn -> gửi), dùng được ở nhà lẫn lúc ghé vườn ---
rep("""if (kind === 'vuon'){ shT.textContent = L135('Bạn bè', 'Friends'); h += vuonHTML(); }""",
    """if (kind === 'vuon'){ shT.textContent = SHEET.tq ? 'Tặng quà' : L135('Bạn bè', 'Friends'); h += SHEET.tq ? tqHTML() : vuonHTML(); }""")
rep("""if (kind === 'visit'){ shT.textContent = SHEET.nc ? 'Giấu mật thư' : 'Quà và mật thư'; h += SHEET.nc ? noteComposeHTML() : visitSheetHTML(); }""",
    """if (kind === 'visit'){ if (!SHEET.tq) tqNew(VISIT.code, VISIT.owner); shT.textContent = 'Tặng quà'; h += tqHTML(); }""")
rep('id="vMore">Quà · mật thư</button>', 'id="vMore">Tặng quà</button>')
repfn('visitSheetHTML', r"""const tqKey = g => g.k + (g.seed ? '~s' : ''), tqName = g => g.seed ? 'Hạt ' + CROPS[g.k].name.toLowerCase() : GD(g.k).name;
const tqHere = code => VISIT && VISIT.code === code ? VISIT : null, tqDone = code => { const V = tqHere(code); return !!(vdOf(code).tq || (V && (V.gifted || V.noted))); }, tqAsked = code => { const V = tqHere(code); return !!(vdOf(code).ak || (V && V.asked)); };
function tqNew(code, name){ SHEET.tq = { code, name: name || 'Hàng xóm', sel: null, only: 0, thu: 0 }; SHEET.nc = { spot: 'chuoi', t: -1, st: 0, tab: 'khia' }; }
function tqList(){ const gv = g => !g.seed && GD(g.k).giu ? 1 : 0; return (VISIT ? VISIT.myInv || [] : myInvList()).filter(g => g.n > 0 && ICON[g.k] && (g.seed ? CROPS[g.k] && (!QUY[g.k] || g.n >= 2) : GD(g.k))).sort((a, b) => gv(b) - gv(a)); }
function tqHTML(){ const q = SHEET.tq, c = SHEET.nc, nm = esc(q.name), L = tqList(), g = q.sel ? L.find(x => tqKey(x) === q.sel) : null, ak = tqAsked(q.code);
  const askB = `<button class="btn" data-a="tqask" ${ak || q.abusy ? 'disabled' : ''}>${ak ? 'Đã xin hạt' : 'Xin hạt'}</button>`, backB = VISIT ? '' : `<button class="btn" data-a="tqback">Thôi</button>`;
  if (tqDone(q.code)) return UX.hero(ICON.thu, 'Hôm nay con tặng rồi', `Mai tặng ${nm} tiếp nghe.`) + `<div class="acts">${askB}${backB}</div>`;
  if (!g && !q.only){ let h = `<div class="note">Mỗi ngày tặng ${nm} một món, kèm lá thư cũng được.</div>` + (!VISIT && NB2.ask && NB2.ask[q.code] ? `<div class="note">${nm} đang xin hạt giống đó con.</div>` : '');
    h += `<div class="acts"><button class="btn" data-a="tqthuonly">Chỉ gửi lá thư</button>${askB}${backB}</div><div class="sub">Chọn món quà</div>`;
    return h + (L.length ? `<div class="grid">${L.map(x => `<button class="it" data-a="tqsel" data-k="${tqKey(x)}"><img src="${ICON[x.k]}" alt=""><b>${tqName(x)}</b><span>Con có ${x.n}</span></button>`).join('')}</div>` : '<div class="note">Kho con chưa có gì để làm quà.</div>'); }
  const lt = !!(q.only || q.thu), can = !lt || c.t >= 0, tabs = g ? ['qua', 'khia', 'cadao', 'do'] : ['khia', 'cadao', 'do'];
  let h = g ? UX.hero(ICON[g.k], tqName(g), `Tặng ${nm} · con có ${g.n}`) : UX.hero(ICON.thu, 'Lá thư', `Giấu trong vườn ${nm}`);
  if (g) h += `<div class="nchips"><button class="nchip${q.thu ? ' on' : ''}" data-a="tqthu" aria-pressed="${!!q.thu}">Viết thêm lá thư</button></div>`;
  if (lt){ h += `<div class="sub">Giấu ở đâu</div><div class="nchips">${Object.entries(NOTE.spots).map(([k, D]) => `<button class="nchip${k === c.spot ? ' on' : ''}" data-a="nsp" data-k="${k}" aria-pressed="${k === c.spot}">${D.n}</button>`).join('')}</div>`;
    h += `<div class="sub">Viết gì</div><div class="nchips">${tabs.map(k => `<button class="nchip${k === c.tab ? ' on' : ''}" data-a="ntab" data-k="${k}" aria-pressed="${k === c.tab}">${NOTE.tabs[k]}</button>`).join('')}</div>`;
    h += `<div class="ntxt">${noteLines(c, g).map(([x, i]) => `<button class="nt${i === c.t ? ' on' : ''}" data-a="ntx" data-k="${i}" aria-pressed="${i === c.t}">${esc(x.s)}</button>`).join('')}</div>`;
    h += `<div class="sub">Dán hình</div><div class="nstk">${NOTE.stick.map((k, i) => ICON[k] ? `<button class="nsi${i === c.st ? ' on' : ''}" data-a="nst" data-k="${i}" aria-label="${esc(GD(k) ? GD(k).name : k)}" aria-pressed="${i === c.st}"><img src="${ICON[k]}" alt=""></button>` : '').join('')}</div>`;
    if (c.t >= 0) h += `<div class="sub">Lá thư của con</div><div class="thu"><img class="ths" src="${noteIcon(c.st)}" alt=""><p>${esc(NOTE.texts[c.t].s)}</p></div>`; }
  return h + `<div class="acts"><button class="btn g" data-a="tqsend" ${can && !q.busy ? '' : 'disabled'}>${!can ? 'Chọn một câu đã nghen' : lt ? (g ? 'Tặng kèm thư' : `Giấu thư vô ${noteSp(c.spot)}`) : 'Tặng'}</button><button class="btn" data-a="tqchg">${g ? 'Đổi món khác' : 'Quay lại'}</button></div>`; }
const tqRpc = async (code, kind, payload) => { const a = { p_code: CLOUD.cred.code, p_secret: CLOUD.cred.secret, p_other: code, p_kind: kind, p_payload: payload || {} }; try { return await rpc('mv2_act', a); } catch (e) { if (!netDown(e)) throw e; return await rpc('mv2_act', a); } };
function tqSend(){ const q = SHEET && SHEET.tq, c = SHEET && SHEET.nc; if (!q || q.busy || !CLOUD.cred || tqDone(q.code)) return; const V = tqHere(q.code), g = q.sel ? tqList().find(x => tqKey(x) === q.sel) : null, lt = !!(q.only || q.thu); if (!g && !q.only) return; if (lt && !(c && c.t >= 0)) return;
  const pl = lt ? { t: c.t, st: c.st, spot: c.spot } : { k: g.k, n: 1, seed: g.seed ? 1 : 0 }, sp = lt ? noteSp(c.spot) : '', re = () => { if (SHEET && SHEET.tq === q){ renderSheet(); shB.scrollTop = 0; } }; if (lt && g){ pl.gk = g.k; if (g.seed) pl.gs = 1; }
  q.busy = 1; renderSheet();
  tqRpc(q.code, lt ? 'note' : 'gift', pl).then(r => { q.busy = 0; vdPut(q.code, { tq: 1 }); if (!(r && r.ok)){ if (V){ V.gifted = 1; visitPersist(); } toast('Hôm nay con tặng người này rồi.', 'vui'); return re(); }
    const xp = (g ? (g.seed && QUY[g.k] ? 15 : 3) : 0) + (lt ? 2 : 0);
    if (V){ if (g){ V.loot.giftOut.push({ k: g.k, n: 1, seed: g.seed ? 1 : 0 }); if (--g.n <= 0 && V.myInv.indexOf(g) >= 0) V.myInv.splice(V.myInv.indexOf(g), 1); V.gifted = 1; } if (lt) V.noted = 1; V.loot.xp += xp; visitPersist(); }
    else { if (g){ const S2 = g.seed ? ST.seeds : ST.inv; S2[g.k] = Math.max(0, (S2[g.k] || 0) - 1); if (g.seed && NB2.ask) delete NB2.ask[q.code]; } gainXP(xp); save(); hud(); }
    sfx('pop'); re(); say(lt ? `Con giấu thư ở ${sp} rồi. ${q.name} về thấy lá rung là kiếm ra liền.` : `Con để quà cho ${q.name} rồi. Có qua có lại mới toại lòng nhau.`, 'vui', { now: true });
  }).catch(e => { q.busy = 0; toast(vErr(e, 'chưa tặng được'), 'lo'); re(); }); }
function tqAsk(){ const q = SHEET && SHEET.tq; if (!q || q.abusy || !CLOUD.cred || tqAsked(q.code)) return; const V = tqHere(q.code), re = () => { if (SHEET && SHEET.tq === q) renderSheet(); }; q.abusy = 1; renderSheet();
  tqRpc(q.code, 'ask', {}).then(r => { q.abusy = 0; vdPut(q.code, { ak: 1 }); if (V){ V.asked = 1; visitPersist(); } re(); say(r && r.ok ? `Nhắn xin hạt rồi. Đợi ${q.name} trả lời nghe.` : 'Hôm nay con xin rồi.', 'vui', { now: true }); }).catch(e => { q.abusy = 0; toast(vErr(e, 'chưa nhắn được'), 'lo'); re(); }); }""")
i, j = fnspan('noteComposeHTML'); s = s[:i] + s[j:]
i, j = fnspan('noteSend'); s = s[:i] + s[j:]
i, j = fnspan('noteFix'); s = s[:i] + s[j:]
# thẻ hàng xóm: một nút Tặng quà thay cho "Tặng hạt" + "Tặng giống quý"
rep("const VD = vdGet(), GQL = gqList(); return h + NB2.list.map(", "const VD = vdGet(); return h + NB2.list.map(")
a0 = s.index("""const btns = (ask ? `<button class="btn" data-a="nbgive" """); a1 = s.index("(!n.followed ? `<button class=\"btn\" data-a=\"nbfol\"", a0)
s = s[:a0] + """const btns = `<button class="btn" data-a="tqopen" data-k="${n.code}">Tặng quà</button>` + """ + s[a1:]
a0 = s.index(""" + (SHEET && SHEET.gq === n.code && GQL.length ? `<div class="gqrow">"""); a1 = s.index("; }).join('') + nbSugHTML(); }", a0)
s = s[:a0] + s[a1:]
# các nút bấm
a0 = s.index("else if (a === 'nbq'){ SHEET.gq = "); a1 = s.index("else if (a === 'nsp' && SHEET.nc){", a0)
s = s[:a0] + """else if (a === 'tqopen'){ const n = (NB2.list || []).find(x => x.code === b.dataset.k); tqNew(b.dataset.k, n && n.name); renderSheet(); shB.scrollTop = 0; return; }
  else if (a === 'tqback'){ SHEET.tq = null; SHEET.nc = null; renderSheet(); shB.scrollTop = 0; return; }
  else if (a === 'tqsel' && SHEET.tq){ Object.assign(SHEET.tq, { sel: b.dataset.k, only: 0 }); SHEET.nc.t = -1; SHEET.nc.tab = 'qua'; renderSheet(); shB.scrollTop = 0; return; }
  else if (a === 'tqchg' && SHEET.tq){ Object.assign(SHEET.tq, { sel: null, only: 0, thu: 0 }); SHEET.nc.t = -1; renderSheet(); shB.scrollTop = 0; return; }
  else if (a === 'tqthu' && SHEET.tq){ const q = SHEET.tq; q.thu = q.thu ? 0 : 1; SHEET.nc.t = -1; SHEET.nc.tab = 'qua'; renderSheet(); return; }
  else if (a === 'tqthuonly' && SHEET.tq){ Object.assign(SHEET.tq, { sel: null, only: 1, thu: 0 }); SHEET.nc.t = -1; SHEET.nc.tab = 'khia'; renderSheet(); shB.scrollTop = 0; return; }
  else if (a === 'tqask'){ tqAsk(); return; }
  else if (a === 'tqsend'){ tqSend(); return; }
  """ + s[a1:]
a0 = s.index("else if (a === 'ngf' && SHEET.nc){"); a1 = s.index("else if (a === 'thuok'){", a0)
s = s[:a0] + s[a1:]
for dead in ["data-a=\"nbgive\"", "data-a=\"nbq\"", "noteComposeHTML", "noteSend(", "noteFix(", "visitSheetHTML", "SHEET.gq", "vgift", "'vask'", "'vnote'", "GQL"]:
    assert dead not in s, dead

# --- tiếng Anh ---
rep("  UIRX.unshift(\n    [/^Nghe nói con (.+) hay nằm ", """  Object.assign(UIEN, { "Tặng quà": "Send a gift", "Xin hạt": "Ask for seeds", "Đã xin hạt": "Asked today", "Chỉ gửi lá thư": "Just a letter", "Chọn món quà": "Pick a gift", "Viết thêm lá thư": "Add a letter", "Tặng": "Send", "Tặng kèm thư": "Send with letter", "Đổi món khác": "Pick another", "Quay lại": "Back", "Lá thư": "A letter", "Hôm nay con tặng rồi": "Gift sent today", "Hôm nay con xin rồi.": "You already asked today.",
    "Cúng ông Địa": "Offering to the Earth God", "Cúng 1 trái vú sữa": "Offer 1 star apple", "Hôm nay con cúng rồi. Mai cúng tiếp, ông Địa mách thêm.": "You made an offering today. Come back tomorrow and the Earth God will share more.",
    "Giờ ông Địa chưa có chuyện gì mới để mách. Khi nào có cá quý, giống quý con chưa gặp thì cúng nghe.": "The Earth God has nothing new to share right now. Make an offering when there's a rare fish or seed you haven't found.",
    "Giờ ông Địa chưa có chuyện gì mới để mách.": "The Earth God has nothing new to share right now.",
    "Cúng một trái vú sữa, ông Địa mách chỗ câu cá quý hay cách kiếm giống quý con chưa có.": "Offer a star apple and the Earth God will hint at where to catch a rare fish or how to find a rare seed you don't have yet.",
    "Cúng một trái vú sữa, ông Địa mách chỗ câu cá quý hay cách kiếm giống quý con chưa có. Giờ kho con chưa có trái nào.": "Offer a star apple and the Earth God will hint at a rare fish or rare seed you don't have yet. You have no star apples right now.",
    "Kho còn đủ vú sữa rồi con. Đem tặng, cúng ông Địa hay bán bớt nghe.": "You have plenty of star apples, dear. Gift some, offer one to the Earth God, or sell a few.",
    "Kho còn đủ trầu rồi con. Đem tặng hay bán bớt nghe.": "You have plenty of betel, dear. Gift some or sell a few.",
    "Trái vú sữa để tặng bạn, bán ở chợ cũng được. Nhà có miếu thì cúng ông Địa một trái, ổng mách nước cho.": "Star apples make a nice gift, and they sell at the market too. With a shrine at home, offer one to the Earth God and he'll give you a tip.",
    "Miếng trầu để tặng bạn, bán ở chợ cũng được nghe con.": "Betel makes a nice gift, and it sells at the market too, dear." });
  UIRX.unshift(
    [/^Mỗi ngày tặng (.+) một món, kèm lá thư cũng được\.$/, (m, a) => `One gift a day for ${a}. You can add a letter too.`],
    [/^(.+) đang xin hạt giống đó con\.$/, (m, a) => `${a} is asking for seeds, dear.`],
    [/^Mai tặng (.+) tiếp nghe\.$/, (m, a) => `Send ${a} another one tomorrow.`],
    [/^Tặng (.+) · con có (\\d+)$/, (m, a, n) => `For ${a} · you have ${n}`],
    [/^Giấu trong vườn (.+)$/, (m, a) => `Hidden in ${a}'s garden`],
    [/^Con có (\\d+)$/, (m, n) => `You have ${n}`],
    [/^Cúng ông Địa · con có (\\d+) trái vú sữa$/, (m, n) => `Offering to the Earth God · you have ${n} star apple${n > 1 ? 's' : ''}`],
    [/^Nghe nói con (.+) hay nằm """)
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
