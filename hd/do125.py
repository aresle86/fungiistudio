# do125: tủ đồ (bước 1 của tiệm may cô Ba, anh Ares duyệt 9/11). Chạy sau may123.py.
# - Từ cấp 5, chạm hình nhân vật góc trên mở Tủ đồ (dưới cấp 5 vẫn mở bảng đổi dáng như cũ).
# - Bốn ngăn: Áo, Quần, Khăn, Nón. Có sẵn: áo, quần của dáng đang chọn; bà ba trắng, bà ba nâu Ngoại may hồi trước;
#   quần đen; khăn rằn, nón lá của ông ngoại. Đồ may ở tiệm cô Ba sau này vô ST.tu.it (cùng chỗ).
# - Chạm là mặc: ST.tu.w = { ao, quan, khan, non }. Nhân vật trong vườn (placeAvatar) và hình đại diện (myFace) dựng theo đồ.
import sys, json
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

TU = r"""/* tủ đồ: đồ có sẵn + đồ may ở tiệm cô Ba (ST.tu.it), đang mặc ST.tu.w */
const TULV = 5, TUK = { ao: 'Áo', quan: 'Quần', khan: 'Khăn', non: 'Nón' };
const TUC = { ao: [['base', ''], ['ao_trang', 'Bà ba trắng', { shirt: '#EFE6D2', fab: 'bong', cut: 'suong', open: false }], ['ao_nau', 'Bà ba nâu', { shirt: '#8A5D3B', fab: 'bong', open: false }]],
  quan: [['base', ''], ['quan_den', 'Quần đen', { pants: '#22201E', pfab: 'bong' }]],
  khan: [['none', 'Không quàng'], ['khan_ran', 'Khăn rằn', { khan: ['#2B2522', '#F2EEE4'] }]],
  non: [['none', 'Không đội'], ['non_la', 'Nón lá', { hat: 'nonla' }]] };
const TUAO = { '#B5553A': 'đỏ gạch', '#D9A53A': 'vàng', '#6E8F5A': 'xanh lá', '#4E78A8': 'xanh', '#EFE6D2': 'ngà' }, TUQ = { '#2B2522': 'Quần đen', '#26304A': 'Quần xanh đậm', '#4A3326': 'Quần nâu', '#5E7A4A': 'Quần xanh rêu' };
function tuBase(k){ const A = AVS[(ST.player || {}).av || 0]; return k === 'ao' ? (A.open ? 'Sơ mi ' : 'Bà ba ') + (TUAO[A.shirt] || 'màu') : (TUQ[A.pants] || 'Quần dài'); }
function tuIt(k, id){ if (id === 'base') return { id, name: tuBase(k), o: null }; const b = TUC[k].find(x => x[0] === id); if (b) return { id, name: b[1], o: b[2] || null }; const c = ST.tu && ST.tu.it && ST.tu.it[id]; return c && c.k === k ? { id, name: c.name, o: c.o || null } : null; }
function tuList(k){ const A = AVS[(ST.player || {}).av || 0], dup = id => (id === 'ao_trang' && A.shirt === '#EFE6D2' && !A.open) || (id === 'quan_den' && A.pants === '#2B2522'); return [...TUC[k].map(x => x[0]).filter(id => !dup(id)), ...Object.keys((ST.tu && ST.tu.it) || {}).filter(id => ST.tu.it[id].k === k)]; }
function tuCur(k){ const W = (ST.tu && ST.tu.w) || {}; return W[k] && tuIt(k, W[k]) ? W[k] : (k === 'ao' || k === 'quan' ? 'base' : 'none'); }
function avOf(av){ const a = { ...AVS[av] }; for (const k of ['ao', 'quan', 'khan', 'non']){ const it = tuIt(k, tuCur(k)); if (it && it.o) Object.assign(a, it.o); } if (a.hat && a.prop === 'non') a.prop = null; if (a.khan && a.prop === 'khan') a.prop = null; return a; }
const AVME = { key: '', face: '', full: '' };
function avShot(a, kind){ const ri = ICR(), ps = sd; ri.setPixelRatio(1); ri.setClearColor(0, 0); ri.toneMapping = T.ACESFilmicToneMapping; ri.toneMappingExposure = 1.02; const W = kind === 'full' ? 220 : 140, H = kind === 'full' ? 280 : 140; ri.setSize(W, H);
  const sc = new T.Scene(), root = new T.Group(); sc.add(root); const pr = ROOT; ROOT = root; sd = 7; avBuild(root, a, {}); ROOT = pr;
  sc.add(new T.HemisphereLight('#fff4e2', '#94a474', 1.6)); sc.add(new T.AmbientLight('#ffffff', .25)); const l = new T.DirectionalLight('#fff0d8', 1.6); l.position.set(-2, 5, 4); sc.add(l);
  const c = kind === 'full' ? new T.Vector3(0, a.hat ? .7 : .62, 0) : new T.Vector3(0, .92, 0), sz = kind === 'full' ? (a.hat ? .86 : .78) : .42, cm = new T.OrthographicCamera(-sz * W / H, sz * W / H, sz, -sz, .01, 100); cm.position.copy(c).add(new T.Vector3(.35, .12, 1).normalize().multiplyScalar(20)); cm.lookAt(c);
  toonRender(ri, sc, cm); const u = toonURL(); sc.traverse(o2 => o2.geometry && o2.geometry.dispose()); ri.renderLists.dispose(); sd = ps; return u; }
function myFace(){ const P = ST.player; if (!P) return UIC.sprout; if (!ST.tu || !ST.tu.w) return AVIMG.face[P.av]; const key = P.av + JSON.stringify(ST.tu.w); if (AVME.key !== key){ AVME.key = key; AVME.face = avShot(avOf(P.av), 'face'); AVME.full = avShot(avOf(P.av), 'full'); } return AVME.face; }
function tuWear(k, id){ if (!tuIt(k, id)) return; ST.tu = ST.tu || {}; ST.tu.w = { ...(ST.tu.w || {}), [k]: id }; save(); try { placeAvatar(); } catch (e) {} avHud(); sfx('pick'); }
function tuSw(k, id){ const it = tuIt(k, id), o = (it && it.o) || {}; if (id === 'none') return 'background:transparent;box-shadow:inset 0 0 0 2px rgba(107,69,41,.35);border:2px dashed rgba(107,69,41,.35)';
  if (k === 'khan'){ const [a, b] = o.khan; return `background:repeating-conic-gradient(${a} 0 25%, ${b} 0 50%) 0 0/14px 14px`; } if (k === 'non') return 'background:radial-gradient(circle,#C9952A 0 2px,#EAD9B2 3px 7px,#C9952A 8px 9px,#EAD9B2 10px)';
  const A = AVS[(ST.player || {}).av || 0], col = k === 'ao' ? (o.shirt || A.shirt) : (o.pants || A.pants); if (o.fab === 'lanh' || o.pfab === 'lanh') return 'background:linear-gradient(135deg,#1A181E 40%,#5A5868 50%,#1A181E 60%)'; if (o.pat === 'soc') return `background:repeating-linear-gradient(90deg,${col} 0 7px,#F2EEE4 7px 10px)`; if (o.pat === 'bongnhi') return `background:radial-gradient(circle,#F6EEDC 0 2px,transparent 3px) 0 0/10px 10px,${col}`; return `background:${col}`; }
function tudoHTML(){ const P = ST.player; myFace(); sayOnce('tudo1', 'Tủ đồ của con nè. Bà ba trắng, bà ba nâu Ngoại may hồi trước, còn cái nón lá với khăn rằn là của ông ngoại để lại. Mặc thử coi.', 'vui');
  let h = `<div class="tuhd"><img src="${AVME.full || AVIMG.full[P.av]}" alt=""><div><b>${esc(P.name)}</b><span>Chạm món nào là mặc món đó.</span></div></div>`;
  for (const k of ['ao', 'quan', 'khan', 'non']){ const cur = tuCur(k); h += `<div class="sub">${TUK[k]}</div><div class="tugrid">` + tuList(k).map(id => { const it = tuIt(k, id); return `<button class="tui${id === cur ? ' on' : ''}" data-a="tuwear" data-k="${k}" data-i="${id}" aria-pressed="${id === cur}"><span class="sw" style="${tuSw(k, id)}"></span><b>${esc(it.name)}</b></button>`; }).join('') + '</div>'; }
  h += `<div class="acts"><button class="btn" data-a="avatar">Đổi dáng, tên vườn</button></div>`; if ((ST.lv || 1) < 21) h += `<div class="meta">Lên cấp 21 thì đi đò lên chợ huyện, đặt cô Ba may thêm đồ.</div>`; return h; }
"""
rep("/* avatar đứng trong vườn, trước bậc thềm */\nawait LDY(0);\nlet AVW = null;", TU + "/* avatar đứng trong vườn, trước bậc thềm */\nawait LDY(0);\nlet AVW = null;")
rep("if (!ST.player) return; const a = { ...AVS[ST.player.av] }; AVW = DYN(G(2.27, 0, 2.0, .35));", "if (!ST.player) return; const a = avOf(ST.player.av); AVW = DYN(G(2.27, 0, 2.0, .35));")
rep("try { $('#avbImg').src = AVIMG.face[P.av]; } catch (e) { return; }", "try { $('#avbImg').src = myFace(); } catch (e) { return; }")
rep("UX.hero(AVIMG && ST.player ? AVIMG.face[ST.player.av] : UIC.sprout,", "UX.hero(AVIMG && ST.player ? myFace() : UIC.sprout,")
rep("$('#avb').addEventListener('click', openIntro);", "$('#avb').addEventListener('click', () => (ST.lv || 1) >= TULV ? openSheet('tudo') : openIntro());")
rep("function renderSheet(){ if (!SHEET) return; const { kind, arg } = SHEET; let h = '';",
    "function renderSheet(){ if (!SHEET) return; const { kind, arg } = SHEET; let h = '';\n  if (kind === 'tudo'){ shT.textContent = 'Tủ đồ'; shB.innerHTML = tudoHTML(); return; }")
rep("if (a === 'avatar'){ openIntro(); return; }", "if (a === 'avatar'){ openIntro(); return; } if (a === 'tuwear'){ tuWear(b.dataset.k, b.dataset.i); renderSheet(); return; }")
rep("button,[data-a],.btn{touch-action:manipulation}",
    "button,[data-a],.btn{touch-action:manipulation} .tuhd{display:flex;gap:14px;align-items:center;margin:2px 0 6px}.tuhd img{width:104px;height:132px;object-fit:contain;flex:none;background:#FBF7EE;border-radius:16px}.tuhd b{display:block;font-family:var(--f-game);font-size:20px;color:var(--ink)}.tuhd span{font-size:14px;color:#6B4529} .tugrid{display:grid;grid-template-columns:repeat(auto-fill,minmax(62px,1fr));gap:6px;margin-top:4px} .tui{appearance:none;border:0;background:#FBF7EE;border-radius:12px;padding:6px 3px 5px;min-height:64px;font:inherit;color:var(--ink);box-shadow:0 3px 0 #E3D3BC;cursor:pointer;display:flex;flex-direction:column;align-items:center;gap:4px} .tui b{font-size:11.5px;line-height:1.12;font-weight:700} .tui .sw{width:28px;height:28px;border-radius:50%;box-shadow:inset 0 0 0 2px rgba(0,0,0,.12)} .tui.on{box-shadow:0 0 0 3px #86B06A,0 3px 0 #6E9A54;background:#F1F7E6}")
EN = {'Tủ đồ': 'Wardrobe', 'Áo': 'Tops', 'Quần': 'Trousers', 'Khăn': 'Scarves', 'Nón': 'Hats', 'Bà ba trắng': 'White bà ba', 'Bà ba nâu': 'Brown bà ba', 'Bà ba đỏ gạch': 'Brick-red bà ba', 'Bà ba vàng': 'Yellow bà ba', 'Bà ba xanh lá': 'Green bà ba', 'Sơ mi xanh': 'Blue shirt', 'Bà ba ngà': 'Ivory bà ba', 'Quần xanh đậm': 'Navy trousers', 'Quần nâu': 'Brown trousers', 'Quần xanh rêu': 'Moss-green trousers', 'Quần đen': 'Black trousers', 'Không quàng': 'No scarf', 'Khăn rằn': 'Checked scarf', 'Không đội': 'No hat', 'Nón lá': 'Conical hat', 'Đổi dáng, tên vườn': 'Change look, garden name', 'Chạm món nào là mặc món đó.': 'Tap anything to put it on.', 'Lên cấp 21 thì đi đò lên chợ huyện, đặt cô Ba may thêm đồ.': 'At level 21 take the ferry to the district market and have Ms Ba sew more clothes.', 'Tủ đồ của con nè. Bà ba trắng, bà ba nâu Ngoại may hồi trước, còn cái nón lá với khăn rằn là của ông ngoại để lại. Mặc thử coi.': "Here's your wardrobe. Grandma sewed the white and brown bà ba long ago, and the conical hat and checked scarf were Grandpa's. Try them on."}
rep('"Bán hết": "Sell all", ', '"Bán hết": "Sell all", ' + ''.join(json.dumps(k, ensure_ascii=False) + ': ' + json.dumps(v, ensure_ascii=False) + ', ' for k, v in EN.items()))
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
