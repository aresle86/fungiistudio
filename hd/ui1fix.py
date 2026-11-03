#!/usr/bin/env python3
"""Đợt 1 giao diện: khay nền cho hàng nút, nút Ghé vườn riêng, thẻ chuồng đang dựng hiện tiến độ thời gian, chip vật liệu thay số cộng gộp,
bỏ chỉ chỗ lượm tre, nhân vật rảnh thì ngồi bậc thềm. Dùng: python3 ui1fix.py <vào> <ra>. Mỗi chỗ vá khớp đúng 1 lần."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b):
    global s
    c = s.count(a); assert c == 1, (c, a[:110]); s = s.replace(a, b)

# ---------- 1. khay nền + nút Ghé vườn ----------
rep('<button class="bt" id="bSo"><img id="icSo" alt=""><span class="tg">Sổ</span></button>',
    '<button class="bt" id="bVuon" hidden><img id="icVuon" alt=""><span class="tg">Ghé vườn</span><span class="bvn" id="bVuonN"></span></button><button class="bt" id="bSo"><img id="icSo" alt=""><span class="tg">Sổ</span></button>')
rep("#bSo.gold::after{content:\"\";position:absolute;inset:-4px;border-radius:18px;box-shadow:0 0 0 3px #F5D27A;animation:tlR 1.1s ease-out infinite;pointer-events:none}",
    "#bSo.gold img{animation:bNud 1.6s ease-in-out infinite}@keyframes bNud{0%,70%,100%{transform:none}80%{transform:translateY(-6px) rotate(-4deg)}90%{transform:translateY(0) rotate(3deg)}}\n"
    ".ui.bot>.row,#tray{background:rgba(255,251,242,.94);border-radius:24px;padding:8px 10px 10px;box-shadow:0 0 0 2px rgba(138,93,46,.4),0 4px 0 rgba(138,93,46,.35),0 10px 18px rgba(43,52,70,.22)}#tray{padding:10px 8px}"
    ".bt{position:relative}.bvn{position:absolute;right:2px;top:-4px;min-width:22px;height:22px;padding:0 5px;border-radius:11px;background:#C24A2E;color:#fff;font:400 13px/22px var(--f-game);text-shadow:none;box-shadow:0 0 0 2px #FFFBF2}.bvn:empty{display:none}")
# sheet Ghé vườn: vườn mẫu + hàng xóm
rep("  if (kind === 'ben'){ shT.textContent = 'Bến nhà'; h += benHTML(); }",
    "  if (kind === 'ben'){ shT.textContent = 'Bến nhà'; h += benHTML(); }\n  if (kind === 'vuon'){ shT.textContent = 'Ghé vườn'; h += vuonHTML(); }")
rep("if (kind === 'ben') setTimeout(() => nbLoad(), 0); SHEET = { kind, arg };", "if (kind === 'ben' || kind === 'vuon') setTimeout(() => nbLoad(), 0); SHEET = { kind, arg };")
rep("finally { NB2.at = Date.now(); NB2.busy = false; if (SHEET && SHEET.kind === 'ben') renderSheet(); } }",
    "finally { NB2.at = Date.now(); NB2.busy = false; if (SHEET && (SHEET.kind === 'ben' || SHEET.kind === 'vuon')) renderSheet(); vuonBadge(); } }")
rep("function benHTML(){",
    """function vuonHTML(){ const left = mauLeft(); return UX.title('Vườn mẫu') + `<div class="vcard"><img src="${ICON.xoai || ICON.cai}" alt=""><div><b>Vườn mẫu của Ngoại</b><span>Ngoại cho hái ${MAU.picks} món mỗi ngày${left < MAU.picks ? `, hôm nay còn ${left}` : ''}</span>${UX.pips(ICON.cai, left, MAU.picks)}</div><button class="btn g" data-a="gomau">Chèo qua</button></div>` + nbHTML(); }
const VUON = { lv: 3 };
function vuonBadge(){ const b = document.getElementById('bVuon'); if (!b) return; const on = !VISIT && !!ST.player && (ST.lv || 1) >= VUON.lv; b.hidden = !on; if (!on) return; { const im = document.getElementById('icVuon'), u = (typeof UIC !== 'undefined' && UIC.tamban) || ICON.ghe; if (im && u && im.dataset.u !== u){ im.src = u; im.dataset.u = u; } } const n = Object.keys(NB2.ask || {}).length + Object.keys(NB2.steal || {}).length; const e = document.getElementById('bVuonN'); if (e) e.textContent = n ? n : ''; }
function benHTML(){""")
rep("$('#nxq').addEventListener('click', e => {",
    """{ const b = document.getElementById('bVuon'); if (b) b.addEventListener('click', () => { sfx('pick'); openSheet('vuon'); }); setInterval(vuonBadge, 2000); setTimeout(vuonBadge, 300); }
$('#nxq').addEventListener('click', e => {""")

# ---------- 2. thẻ Việc tiếp theo: chuồng đang dựng hiện thời gian; đang gom đồ hiện chip từng món ----------
rep("""  if (penFirst && (qIdle || (q && n === 6 && penFirst === 'ga') || !q)){ const F = PENS[penFirst].F; ic = ICON.cuoc || UIC.task; t = penFirst === 'ga' ? 'Sửa chuồng gà' : 'Dựng chuồng vịt'; const have = Math.min(ST.inv.rom || 0, F.rom) + Math.min(ST.tre || 0, F.tre) + (ST.xu >= F.xu ? 1 : 0), tot = F.rom + F.tre + 1; em = penCan(penFirst) ? 'đủ đồ rồi' : `${have}/${tot}`; f = have / tot; go = penCan(penFirst); act = 'pen:' + penFirst; }""",
    """  let chips = ''; const penCard = k => { const F = PENS[k].F; ic = ICON.cuoc || UIC.task; act = 'pen:' + k;
    if (bldOn(k)){ const L = bldLeft(k), T0 = (BLDH[k] - Math.min(BLDH[k] / 2, (ST.bld[k].help || 0))) * 3600e3 / (ST.spd || 1); t = k === 'ga' ? 'Xóm đang sửa chuồng gà' : 'Xóm đang dựng chuồng vịt'; f = 1 - L / T0; em = 'còn ' + fmtMin(Math.ceil(L / 60000)); go = false; lab = 'ĐANG DỰNG'; return; }
    t = k === 'ga' ? 'Sửa chuồng gà' : 'Dựng chuồng vịt'; go = penCan(k); const c = (img, h0, n0) => `<span class="nqc${h0 >= n0 ? ' ok' : ''}"><img src="${img}" alt="">${h0 >= n0 ? '✓' : Math.min(h0, n0) + '/' + n0}</span>`;
    chips = c(ICON.rom, ST.inv.rom || 0, F.rom) + c(ICON.tre || ICON.cui, ST.tre || 0, F.tre) + c(UIC.coin, ST.xu, F.xu); };   /* mỗi món một chip, không cộng gộp rơm + tre + xu thành một số */
  if (penFirst && (qIdle || (q && n === 6 && penFirst === 'ga') || !q)) penCard(penFirst);""")
rep("""  else if (q && n === 6 && !ST.ga.fixed && penOpen('ga')){ const F = COOPFIX; ic = ICON.cuoc || UIC.task; t = 'Sửa chuồng gà trước'; const have = Math.min(ST.inv.rom || 0, F.rom) + Math.min(ST.tre || 0, F.tre) + (ST.xu >= F.xu ? 1 : 0), tot = F.rom + F.tre + 1; em = `${have}/${tot}`; f = have / tot; go = penCan('ga'); act = 'pen:ga'; }""",
    """  else if (q && n === 6 && !ST.ga.fixed && penOpen('ga')){ penCard('ga'); if (!bldOn('ga')) t = 'Sửa chuồng gà trước'; }""")
rep("""  else if (Object.keys(PENS).some(penOpen)){ const pk = Object.keys(PENS).find(penOpen), F = PENS[pk].F; ic = ICON.cuoc || UIC.task; t = pk === 'ga' ? 'Sửa chuồng gà' : 'Dựng chuồng vịt'; const have = Math.min(ST.inv.rom || 0, F.rom) + Math.min(ST.tre || 0, F.tre) + (ST.xu >= F.xu ? 1 : 0), tot = F.rom + F.tre + 1; em = penCan(pk) ? 'đủ đồ rồi' : `${have}/${tot}`; f = have / tot; go = penCan(pk); act = 'pen:' + pk; }""",
    """  else if (Object.keys(PENS).some(penOpen)) penCard(Object.keys(PENS).find(penOpen));""")
rep("""<span class="nqb"><i><u style="width:${Math.round(Math.max(0, Math.min(1, f)) * 100)}%"></u></i><em>${em}</em></span>${dl}</span>`;""",
    """${chips ? `<span class="nqb nqcs">${chips}</span>` : `<span class="nqb"><i><u style="width:${Math.round(Math.max(0, Math.min(1, f)) * 100)}%"></u></i><em>${em}</em></span>`}${dl}</span>`;""")
rep(".nxq .nqt{min-width:0;flex:1}",
    ".nxq .nqcs{gap:5px}.nxq .nqc{display:inline-flex;align-items:center;gap:2px;padding:1px 6px 1px 2px;border-radius:99px;background:#F1E8D6;font:400 12px var(--f-game);color:#8A5D3B}.nxq .nqc img{width:20px;height:20px}.nxq .nqc.ok{background:#DCEBC8;color:#4E7A3E}\n.nxq .nqt{min-width:0;flex:1}")
# Sổ › Việc: chuồng đang dựng thì hiện tiến độ, không hiện bảng gom đồ
rep("""function pgCoop(){ const pk = Object.keys(PENS).find(penOpen); if (!pk) return '';""",
    """function pgCoop(){ const pk = Object.keys(PENS).find(penOpen); if (!pk) return ''; if (bldOn(pk)){ const L = bldLeft(pk), T0 = (BLDH[pk] - Math.min(BLDH[pk] / 2, (ST.bld[pk].help || 0))) * 3600e3 / (ST.spd || 1); return UX.title('Việc Ngoại nhờ thêm') + UX.hero(ICON.cuoc || UIC.task, pk === 'ga' ? 'Xóm đang sửa chuồng gà' : 'Xóm đang dựng chuồng vịt', `Còn ${fmtMin(Math.ceil(L / 60000))} · bạn ghé phụ bớt 1 tiếng`, '', [1 - L / T0, '#EDB940']); }""")

# ---------- 3. lượm tre không chỉ chỗ: bỏ mũi tên vàng + vòng sáng, bỏ nút chỉ chỗ, bỏ câu chỉ đường ----------
rep("""g.scale.setScalar(1.3); const ar = G(0, .5, 0, 0, g); M(new T.ConeGeometry(.07, .15, 4), FTM('#FFD45A'), 0, 0, 0, { p: ar, r: [Math.PI, 0, 0], cast: false }); M(cyl(.025, .025, .1, 4), FTM('#FFD45A'), 0, .12, 0, { p: ar, cast: false }); g.userData.ar = ar; M(new T.RingGeometry(.32, .38, 24), new T.MeshBasicMaterial({ color: '#FFE38A', transparent: true, opacity: .7, depthWrite: false }), 0, .01, 0, { p: g, r: [-Math.PI / 2, 0, 0], cast: false }).userData.rg = 1; }   /* tre chờ lượm: mũi tên vàng nhún trên đầu, vòng sáng dưới đất cho dễ thấy */""",
    """g.scale.setScalar(1.3); }   /* tre chờ lượm: nằm tự nhiên dưới đất, không chỉ chỗ, để người chơi tự tìm */""")
rep("""<span>Lượm ${F.tre} cây tre Ngoại chặt sẵn, nằm dưới đất cạnh chuồng chỗ có mũi tên vàng. Thêm""",
    """<span>Lượm ${F.tre} cây tre Ngoại chặt sẵn đâu đó quanh vườn. Thêm""")
rep("""<span>${(ST.tre || 0) < F.tre ? 'Chỉ chỗ lượm tre' : 'Ra ' + P.name}</span>""", """<span>Ra ${P.name}</span>""")
rep("""function penGo(k){ const F = PENS[k].F, tr = ST.odd && ST.odd.list.find(o => o.k === 'tre'); if ((ST.tre || 0) < F.tre && tr){ camTo(new T.Vector3(tr.x, .2, tr.z), Math.max(cam.zoom, DEFZ() * 1.3)); setTimeout(() => bark('Tre nằm dưới đất chỗ mũi tên vàng đó con. Chạm vô là lượm.'), 600); return; } const c""",
    """function penGo(k){ const c""")

# ---------- 4. nhân vật rảnh thì về ngồi bậc thềm trước hiên ----------
rep("""for (const sx of [-1, 1]){ const lg = G(sx * .1, .28, 0, 0, g); M(cyl(.095, .125, .26, 8), a.pants, 0, -.12, 0, { p: lg });""",
    """for (const sx of [-1, 1]){ const lg = G(sx * .1, .28, 0, 0, g); if (sx < 0) a.legL = lg; else a.legR = lg; M(cyl(.095, .125, .26, 8), a.pants, 0, -.12, 0, { p: lg });""")
rep("AVW = DYN(G(6.42, 0, 2.18, .75));", "AVW = DYN(G(2.27, 0, 2.0, .35));")
rep("const AVHOME = new T.Vector3(6.42, 0, 2.18);", "const AVHOME = new T.Vector3(2.27, 0, 2.0);   /* chỗ nghỉ: bậc thềm trên, giữa hiên nhà */")
rep("""  if (L > .03){ d.normalize(); AVW.position.addScaledVector(d, Math.min(L, dt * 1.5));""",
    """  const sitP = (on, t2) => { for (const lg of [a && a.legL, a && a.legR]) if (lg) lg.rotation.x = on ? -1.25 + Math.sin(t2 * 2.2 + (lg === a.legL ? 0 : 1.6)) * .12 : 0; };
  if (L > .03){ sitP(false); d.normalize(); AVW.position.addScaledVector(d, Math.min(L, dt * 1.5));""")
rep("""} else { AVIDLE += dt; AVW.rotation.y += (.75 - AVW.rotation.y) * Math.min(1, dt * 3); } }""",
    """} else { AVIDLE += dt; AVW.rotation.y += (.35 - AVW.rotation.y) * Math.min(1, dt * 3); AVW.position.y = .065; sitP(true, AVIDLE); } }   /* ngồi bậc thềm, đong đưa chân */""")
open(sys.argv[2], 'w', encoding='utf8').write(s)
print('ok')
