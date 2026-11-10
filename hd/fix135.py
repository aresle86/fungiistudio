# v135: len cap de hieu hon (toi da 3 mon, nut "Dan con toi", hoan khi dang do tay), cham "Moi",
# "Sap mo" trong So (khong ghi so cap), o hat "Sap co" trong quat hat, cua "Trang tri" trong Cho (Vuon + Ao, mon bay hom nay).
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)

rep("BUILD = 'v134'", "BUILD = 'v135'")

# ---------- CSS ----------
CSS = """
.lvk span.go{background:#FFF1C9;box-shadow:inset 0 0 0 2px #E9B949;color:#7A4E12}
.lvk em{flex-basis:100%;font:600 13px var(--f-body);font-style:normal;color:#8A5D3B;margin-top:2px}
.lvbt{position:relative;z-index:1;display:flex;gap:10px;justify-content:center;flex-wrap:wrap}.lvc .lvbt .btn{padding:11px 20px;min-height:48px}
#tSeed.moi::after,#bCho.moi::after{content:'';position:absolute;top:-4px;width:13px;height:13px;border-radius:50%;background:#E8704A;box-shadow:0 0 0 2.5px #FBF7EE;pointer-events:none;z-index:2}
#tSeed.moi::after{left:-3px}#bCho.moi::after{right:2px;top:2px}
i.moi{font-style:normal;font:800 12px/1.3 var(--f-body);color:#fff;background:#E8704A;border-radius:999px;padding:1px 7px;white-space:nowrap}
.sk i.moi{position:absolute;left:0;top:2px;box-shadow:0 0 0 2px #FBF7EE;pointer-events:none}
.sn b i.moi{margin-left:6px;vertical-align:2px}
.sg i.moi2{background:#E8704A}
.tchip{min-height:44px!important}
.sk.lock>img{filter:grayscale(1) opacity(.5)}
@media (max-width:700px){body:has(#fan:not([hidden])) #tstw{top:auto!important;bottom:calc(236px + env(safe-area-inset-bottom,0px))!important}}
.smo{display:grid;gap:8px}.smi{display:grid;grid-template-columns:50px minmax(0,1fr);align-items:center;gap:10px;padding:6px 10px 6px 6px;background:#FBF7EE;border-radius:16px;box-shadow:0 3px 0 #E3D3BC}
.smi img{width:50px;height:50px;object-fit:contain}.smi b{display:block;font:400 16px var(--f-game);color:#6B4529}.smi span{display:block;font:600 13px/1.35 var(--f-body);color:#8A5D3B}
.smi.bm img{filter:brightness(0) opacity(.2)}.smi.bm span{font-size:14px;color:#6B4529}
"""
rep(".lvc .btn{font-size:18px;padding:11px 28px}", ".lvc .btn{font-size:18px;padding:11px 28px}" + CSS)

# ---------- man len cap ----------
rep("""<button class="btn g" id="lvOk">Hay quá!</button></div></div>""",
    """<div class="lvbt"><button class="btn g" id="lvOk">Hay quá!</button><button class="btn g" id="lvGo" hidden>Dẫn con tới</button></div></div></div>""")
rep("""$('#lvK').innerHTML = feats.map(([k, t], i) => `<span style="animation-delay:${.35 + i * .09}s"><img src="${icOf(k)}" alt="">${t}</span>`).join('');""",
    """lvCard(feats);""")
rep("""$('#lvOk').addEventListener('click', () => { lvClose(); sfx('pop'); });""",
    """$('#lvOk').addEventListener('click', () => { lvClose(); sfx('pop'); }); $('#lvGo').addEventListener('click', () => { const g = window.LVGO; window.LVGO = null; lvClose(); sfx('pop'); if (g) setTimeout(() => { try { g(); } catch (e) { console.warn(e); } }, 320); });""")
rep("save(); try { lvCelebrate(n); } catch (e) { console.warn(e); }", "save(); try { lvWait(n); } catch (e) { console.warn(e); }")
rep("for (const k of ks) ST.seeds[k] = (ST.seeds[k] || 0) + 1;", "for (const k of ks) ST.seeds[k] = (ST.seeds[k] || 0) + 1; try { moiSet(n, ks); } catch (e) {}")

# ---------- quat hat: cham Moi + o "Sap co" ----------
rep("""'hết, ' + c.seed + ' xu'}"><img src="${ICON[k]}" alt="" draggable="false">""",
    """'hết, ' + c.seed + ' xu'}"><img src="${ICON[k]}" alt="" draggable="false">${moiTag('s_' + k)}""")
rep("""  if (false && nxt) h += `<div class="sk lock" aria-label="${CROPS[nxt].name} mở ở cấp ${UNLOCK[nxt]}"><img src="${ICON[nxt]}" alt="" draggable="false"><span class="pr">Cấp ${UNLOCK[nxt]}</span><b>${CROPS[nxt].name}</b></div>`;""",
    """  { const sx = P ? null : ks.find(k => UNLOCK[k] === (ST.lv || 1) + 1 && !CROPS[k].rare); if (sx) h += `<div class="sk lock" data-lock="1" aria-label="${CROPS[sx].name}: ${L135('sắp có', 'coming soon')}"><img src="${ICON[sx]}" alt="" draggable="false"><span class="pr">${L135('Sắp có', 'Soon')}</span><b>${CROPS[sx].name}</b></div>`; }""")
rep("if (!b || b.classList.contains('lock')) return; const k = b.dataset.k,",
    "if (!b || b.classList.contains('lock')) return; try { moiOff('s_' + b.dataset.k, b); } catch (e) {} const k = b.dataset.k,")

# ---------- So: Sap mo ----------
rep("  return h + UX.more('Kinh nghiệm có từ đâu',", "  try { h += sapMoHTML(feats); } catch (e) { console.warn(e); }\n  return h + UX.more('Kinh nghiệm có từ đâu',")

# ---------- Cho: tab Trang tri (Vuon + Ao) ----------
rep("dcOn() ? ['tiem', 'Tiệm', 0] : null].filter(Boolean).map(([k, n, c]) => `<button class=\"sg${SHEET.tab === k ? ' on' : ''}\" data-a=\"ctab\" data-k=\"${k}\">${n}${c ? `<i>${c}</i>` : ''}</button>`)",
    "dcOn() ? ['tiem', L135('Trang trí', 'Decor'), moiN('d'), 1] : null].filter(Boolean).map(([k, n, c, m]) => `<button class=\"sg${SHEET.tab === k ? ' on' : ''}\" data-a=\"ctab\" data-k=\"${k}\">${n}${c ? `<i${m ? ' class=\"moi2\"' : ''}>${c}</i>` : ''}</button>`)")
rep("const TC = [['kieng', 'Đồ kiểng', UIC.dc_mai_chieu_thuy]].filter(Boolean);",
    "const TC = [['kieng', L135('Vườn', 'Garden'), UIC.dc_mai_chieu_thuy], (ST.big && ST.big.ao) ? ['ao', L135('Ao', 'Pond'), aoIc('sen')] : null].filter(Boolean);")
rep("      if (SHEET.sub === 'kieng') h += dcHTML(); }",
    "      if (SHEET.sub === 'kieng'){ h += dcHTML(); SHEET.sawDc = 1; } else if (SHEET.sub === 'ao') h += aoDcBlock(); }")
rep("const closeSheet = () => { SHEET = null;", "const closeSheet = () => { try { if (SHEET && SHEET.sawDc) moiSeenDc(); } catch (e) {} SHEET = null;")
rep("""  h += UX.title('Trang trí ao', 'Chỉ để ngắm, không thu hoạch') + '<div class="upg">' + Object.keys(AOD).map(k => { const own = !!aoDc()[k], d = AOD[k]; const off = own && !!(B.off && B.off[k]); return own ? UX.upc('aodcx', aoIc(k), d[0], null, { k, why: off ? 'Đang cất · chạm để đặt lại' : 'Đang trên ao · chạm để cất' }) : UX.upc('aodc', aoIc(k), d[0], vnX(d[1]), { k, dis: ST.xu < d[1] }); }).join('') + '</div>';""",
    """  h += aoDcBlock();""")

# ---------- Do kieng: mon bay hom nay, khong ghi so cap, mua lan dau dan thang toi Sap vuon ----------
rep("  const can = pr => ST.xu + (ST.vang || 0) * 300 >= pr; const row = k => {", "  const FT = dcFeat(); const can = pr => ST.xu + (ST.vang || 0) * 300 >= pr; const row = k => {")
rep("""<div class="sn"><b>${d.name}</b>${d.b4 ?""", """<div class="sn"><b>${d.name}${moiTag('d_' + k)}</b>${d.b4 ?""")
rep("const L = Object.keys(DCK).filter(k => DCK[k].cat === cat && dcLvOk(k)).sort(", "const L = Object.keys(DCK).filter(k => DCK[k].cat === cat && dcLvOk(k) && !FT.includes(k)).sort(")
rep(" + sec('Hàng rào', 'rao') + sec('Chuồng gà', 'ga')", " + (FT.length ? `<div class=\"sub\">${L135('Hôm nay tiệm bày', 'On display today')}</div>` + FT.map(row).join('') : '') + sec('Hàng rào', 'rao') + sec('Chuồng gà', 'ga')")
rep("(nxt ? `<div class=\"note\">Lên cấp ${DCLV[nxt]} Tiệm có thêm ${DCK[nxt].name.toLowerCase()}.</div>` : '')",
    "(nxt ? `<div class=\"note\">${EN ? 'Keep tending the garden and the shop will stock: ' + nm135(DCK[nxt].name) + '.' : 'Chăm vườn thêm ít bữa, tiệm có thêm ' + DCK[nxt].name.toLowerCase() + '.'}</div>` : '')")
rep("if (DCSAY[k] && !ST.seen['dcb_' + k]){ ST.seen['dcb_' + k] = 1; say(DCSAY[k], 'vui', { now: true }); } save(); hud(); renderSheet(); return; }",
    "let sd135 = 0; if (DCSAY[k] && !ST.seen['dcb_' + k]){ ST.seen['dcb_' + k] = 1; say(DCSAY[k], 'vui', { now: true }); sd135 = 1; } try { moiOff('d_' + k); } catch (e) {} save(); hud(); if (dcGo1(sd135)) return; renderSheet(); return; }")

JS = r"""
/* ===== v135: lên cấp dễ hiểu, chấm Mới, Sắp mở, cửa Trang trí ===== */
function L135(vi, en){ try { return EN ? en : vi; } catch (e) { return vi; } }
function nm135(t){ try { return EN && UIEN[t] ? UIEN[t] : t; } catch (e) { return t; } }
const LVNHO = { 'Việc lặt vặt': 1, 'Bắt sâu': 1, 'Nhặt củi': 1 };
function lvCrop(k){ return CROPS[k] && UNLOCK[k] != null && !CROPS[k].rare ? CROPS[k] : null; }
function lvOrder(feats){ const dup = {}; for (const [k, t] of feats) if (lvCrop(k) && CROPS[k].name !== t) dup[k] = 1; feats = feats.filter(([k, t]) => !(dup[k] && CROPS[k].name === t)); { const sn = {}; feats = feats.filter(([k, t]) => sn[k + '|' + t] ? false : (sn[k + '|' + t] = 1)); } const rk = ([k, t]) => /^dc_/.test(k) ? 3 : t === 'Câu thêm cá' ? 4 : LVNHO[t] ? 2 : lvCrop(k) ? 1 : 0; return feats.map((f, i) => [f, i]).sort((a, b) => rk(a[0]) - rk(b[0]) || a[1] - b[1]).map(x => x[0]); }
function lvDest(k, t){ if (VISIT) return null; const at = (x, z) => () => { camTo(new T.Vector3(x, .3, z), Math.max(cam.zoom, DEFZ() * 1.1)); setTimeout(() => { try { pingAt(x, z); } catch (e) {} }, 500); };
  if (/^dc_/.test(k)) return () => taskGo('dc');
  if (lvCrop(k) && (CROPS[k].name === t || CROPS[k].kind !== 'trellis')) return () => { if (TOOL) clearTool(); PEND = null; renderFan(); fan.hidden = false; };
  const M = { 'Đơn nhà bên': () => openSheet('ben'), 'Câu cá': () => openSheet('ben'), 'Chợ nổi': () => openSheet('ben'), 'Đò lên chợ huyện': () => openSheet('ben'),
    'Ghe chợ nổi': () => at(GHEV.root.position.x, GHEV.root.position.z)(), 'Góc vườn mới': () => at(BAIC.x + .4, BAIC.z + .3)(), 'Bãi hông nhà': () => at(BAIC.x + .4, BAIC.z + .3)(),
    'Bếp Ngoại': () => at(5.15, .05)(), 'Mua gà, ấp trứng': () => penGo('ga'), 'Chuồng vịt': () => penGo('vit'), 'Lò ấp vịt': () => penGo('vit'),
    'Mé sông': () => at(SONGC.x, SONGC.z)(), 'Sau nhà 10 ô': () => at(SAUC.x, SAUC.z)(), 'Nong phơi': () => taskGo('nong'), 'Khạp muối': () => taskGo('khap'), 'Lò sấy': () => taskGo('say'), 'Hố ủ phân': () => taskGo('bon') };
  return M[t] || null; }
function lvCard(feats){ const L = lvOrder(feats), top = L.slice(0, 3), more = L.length - top.length; let gi = -1, go = null;
  for (let i = 0; i < top.length && !go; i++){ const d = lvDest(top[i][0], top[i][1]); if (d){ go = d; gi = i; } }
  $('#lvK').innerHTML = top.map(([k, t], i) => `<span${i === gi ? ' class="go"' : ''} style="animation-delay:${.35 + i * .09}s"><img src="${icOf(k)}" alt="">${t}</span>`).join('') + (more > 0 ? `<em>${L135(`Còn ${more} món nữa, con cứ chơi là gặp`, `${more} more to find as you play`)}</em>` : '');
  try { if (EN){ $('#lvT').textContent = `You reached level ${$('#lvN').textContent}!`; $('#lvS').textContent = feats.length ? 'Grandma has new things for you' : 'Well done, Grandma is so proud'; } } catch (e) {}
  window.LVGO = go; const g = $('#lvGo'), ok = $('#lvOk'); g.hidden = !go; g.textContent = L135('Dẫn con tới', 'Take me there'); ok.classList.toggle('g', !go); }
let LVW = 0;
function lvHot(){ const t = f => { try { return !!f(); } catch (e) { return false; } }; return t(() => STROKE) || t(() => CHM.on) || t(() => FM.on) || t(() => SAP) || t(() => TRAYP) || t(() => document.body.classList.contains('drag')); }
function lvWait(n){ if (LVW) return; if (!lvHot()) return lvCelebrate(n); let calm = 0, tries = 0; LVW = setInterval(() => { tries++; let far = false; try { far = !!(CHM.on || FM.on); } catch (e) {} if (lvHot() && (far || tries < 50)){ calm = 0; return; } if (++calm < 2 && tries < 50) return; clearInterval(LVW); LVW = 0; try { lvCelebrate(ST.lv || n); } catch (e) { console.warn(e); } }, 400); }
/* chấm Mới: s_<hạt>, d_<đồ trang trí> */
function moiTag(key){ try { return (ST.moi || {})[key] ? `<i class="moi">${L135('Mới', 'New')}</i>` : ''; } catch (e) { return ''; } }
function moiN(p){ try { return Object.keys(ST.moi || {}).filter(k => k[0] === p).length; } catch (e) { return 0; } }
function moiDots(){ try { const a = $('#tSeed'), b = $('#bCho'); if (a) a.classList.toggle('moi', moiN('s') > 0); if (b) b.classList.toggle('moi', moiN('d') > 0 && dcOn()); } catch (e) {} }
function moiSet(n, ks){ ST.moi = ST.moi || {}; for (const k of ks) if (!CROPS[k].rare) ST.moi['s_' + k] = 1; for (const k of Object.keys(DCLV)) if (DCLV[k] === n && DCK[k] && !DCK[k].sp && n > DC.lv) ST.moi['d_' + k] = 1; save(); moiDots(); }
function moiOff(key, el){ if (!ST.moi || !ST.moi[key]) return; delete ST.moi[key]; save(); moiDots(); try { const i = el && el.querySelector('i.moi'); if (i) i.remove(); } catch (e) {} }
function moiSeenDc(){ if (!ST.moi) return; let ch = 0; for (const k of Object.keys(ST.moi)) if (k[0] === 'd'){ delete ST.moi[k]; ch = 1; } if (ch){ save(); moiDots(); } }
setTimeout(moiDots, 1200);
fan.addEventListener('click', e => { if (e.target.closest('.sk.lock')) toast(L135('Chăm vườn thêm chút nữa là Ngoại đưa hạt này cho con.', 'Tend the garden a little more and Grandma will hand you these seeds.'), 'vui'); });
/* Sắp mở: chỉ hé bước kế, không ghi số cấp. Quà và chuyện bất ngờ thì giấu hẳn */
const SMHE = { 'Bếp Ngoại': ['Chái bếp nguội lâu rồi, sắp có khói lại.', 'The old kitchen has been cold a long while. Smoke will rise again soon.'],
  'Nong phơi': ['Nắng tốt vầy mà để không thì uổng.', 'All this good sun, a shame to let it go to waste.'],
  'Khạp muối': ['Ngoại đang lựa mấy cái khạp sành ngoài chợ.', 'Grandma is picking out clay jars at the market.'],
  'Lò sấy': ['Mùa mưa tới, phơi nắng hổng kịp nữa.', 'Rainy season is near, the sun alone will not keep up.'],
  'Hố ủ phân': ['Lá rụng, vỏ trái đừng bỏ, sắp có chỗ dùng.', 'Keep the fallen leaves and peels, they will be useful soon.'],
  'Câu cá': ['Dưới bến dạo này cá quẫy dữ lắm.', 'The fish have been splashing a lot down by the dock.'],
  'Lò ấp vịt': ['Vịt đẻ sai quá, Ngoại đang tính chuyện ấp.', 'The ducks lay so well, Grandma is thinking about hatching.'],
  'Đào ao cá': ['Góc bãi trũng, mưa xuống là đọng nước hoài.', 'That low corner keeps pooling water whenever it rains.'],
  'Nuôi ong lấy mật': ['Bông nở nhiều, ong lạ bay về dòm ngó.', 'So many flowers, wild bees keep dropping by.'],
  'Ghe tam bản đặt lờ': ['Ngoài bến có chiếc ghe đang đóng dở.', 'A half-built boat sits out by the dock.'],
  'Giỏ lục bình': ['Lục bình trôi đầy sông, mà Ngoại biết đan đó nghe.', 'Water hyacinth fills the river, and Grandma knows how to weave.'],
  'Mái lá mới': ['Mái lá nhà mình cũ rồi, Ngoại tính lợp lại.', 'Our thatched roof is getting old. Grandma plans to redo it.'],
  'Sửa sang nhà cửa': ['Nhà mình ở lâu rồi, Ngoại tính sửa sang lại.', 'The house has seen many years. Grandma plans to fix it up.'],
  'Đò lên chợ huyện': ['Bến đò dạo này có người hỏi thăm rau nhà mình.', 'Folks at the ferry landing have been asking about our greens.'] };
function sapMoHTML(feats){ const hid = ([k, t]) => /^(ft_|bu_|dc_)/.test(k) || t === 'Món Tết' || t === 'Một năm ở vườn Ngoại' || t === 'Món mật ong' || LVNHO[t];
  const L = lvOrder(feats).filter(f => !hid(f)), he = L.filter(f => SMHE[f[1]]), ro = L.filter(f => !SMHE[f[1]]), pick = [...he.slice(0, 1), ...ro].slice(0, 2); if (!pick.length) return '';
  const row = ([k, t]) => { const m = SMHE[t]; if (m) return `<div class="smi bm"><img src="${icOf(k)}" alt=""><div><span>${L135(m[0], m[1])}</span></div></div>`;
    const c = lvCrop(k), dat = { 'Góc vườn mới': 1, 'Bãi hông nhà': 1, 'Mé sông': 1, 'Sau nhà 10 ô': 1 }[t]; return `<div class="smi"><img src="${icOf(k)}" alt=""><div><b>${t}</b><span>${c ? (c.tree ? L135('Cây trái mới', 'New fruit tree') : L135('Hạt giống mới', 'New seed')) : dat ? L135('Thêm đất trồng', 'More land to plant') : L135('Việc mới', 'New thing to do')}</span></div></div>`; };
  return UX.title(L135('Sắp mở', 'Coming up'), L135('Chăm vườn thêm là tới', 'Keep tending to get there')) + `<div class="smo">${pick.map(row).join('')}</div>`; }
/* Trang trí ao: dùng chung cho bảng ao và tab Trang trí trong Chợ */
function aoDcBlock(){ const B = ST.big.ao; if (!B) return ''; return UX.title('Trang trí ao', 'Chỉ để ngắm, không thu hoạch') + '<div class="upg">' + Object.keys(AOD).map(k => { const own = !!aoDc()[k], d = AOD[k]; const off = own && !!(B.off && B.off[k]); return own ? UX.upc('aodcx', aoIc(k), d[0], null, { k, why: off ? 'Đang cất · chạm để đặt lại' : 'Đang trên ao · chạm để cất' }) : UX.upc('aodc', aoIc(k), d[0], vnX(d[1]), { k, dis: ST.xu < d[1] }); }).join('') + '</div>'; }
/* mỗi ngày tiệm bày 2 món kiểng lên đầu (không giảm giá, chỉ để người chơi thấy món mới) */
function dcFeat(){ try { const L = Object.keys(DCK).filter(k => DCK[k].cat === 'k' && !DCK[k].sp && dcLvOk(k)); if (L.length < 4) return []; let h = 7; for (const c of dayKey()) h = (h * 31 + c.charCodeAt(0)) % 100003; const a = L[h % L.length], L2 = L.filter(k => k !== a), b = L2[(h >> 3) % L2.length]; return [a, b]; } catch (e) { return []; } }
/* mua món kiểng đầu tiên: đóng bảng, vô thẳng Sắp vườn để đặt */
function dcGo1(said){ try { if (ST.seen.dcgo1 || !sapOk()) return false; const bag = Object.values(ST.dc.bag || {}).reduce((a, b) => a + (b || 0), 0); ST.seen.dcgo1 = 1; save(); if ((ST.dc.items || []).length || bag !== 1) return false; closeSheet(); if (!SAP) sapMode(true); else sapTrayDraw(); if (!said) toast(L135('Món mới nằm trong túi đồ. Kéo ra ô đất trống nghe con.', 'Your new piece is in the bag. Drag it onto an empty plot.'), 'vui'); return true; } catch (e) { return false; } }
"""
rep("function taskGo(t, k){", JS + "function taskGo(t, k){")

open(DST, 'w', encoding='utf-8').write(s)
