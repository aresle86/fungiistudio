# ch125: chợ huyện (bước 2 của tiệm may cô Ba). Chạy sau do125.py.
# - Từ cấp 21, Bến nhà có nút "Đi đò lên chợ huyện · 20 xu". Lần đầu Ngoại chỉ đường (không đi theo).
# - Chợ huyện là cảnh riêng (CHM.B.sc, máy quay riêng CHM.cam): dựng khi lên, gỡ khi về; vườn vẫn chạy (cây lớn, đồng hồ).
#   Cảnh lấy từ hình mẫu đã duyệt ch124.js (bản 5), đồ tĩnh gộp lại bằng mergeRig cho đỡ lần vẽ.
# - Ở chợ: kéo ngang để dạo, chạm tiệm may / tiệm chụp hình / bến đò; nhân vật mình đứng ở bến, mặc đồ trong tủ; nút "Về vườn".
import sys, json, re
src, dst = sys.argv[1], sys.argv[2]
s = open(src, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (a[:90], s.count(a))
    s = s.replace(a, b)

lab = open('ch124.js', encoding='utf-8').read()
a0 = "const sc = new T.Scene(), root = new T.Group(); sc.add(root); const pr = ROOT; ROOT = root; sd = 31; const g = root;"
a1 = "  { root.updateWorldMatrix(true, true);"
body = lab[lab.index(a0) + len(a0):lab.index(a1)]
assert 'window.' not in body and 'ri.' not in body, 'builder body touches lab-only things'

CH = r"""/* ---------- chợ huyện (cấp 21): cảnh riêng, đi đò lên ---------- */
const CHM = { lv: 21, fare: 20, on: false, B: null, cam: null, tx: .9, tx0: .9, drag: null, sayT: 0 };
try { (LVFEAT[21] = LVFEAT[21] || []).push(['ghe', 'Đò lên chợ huyện']); } catch (e) {}
function chBuild(){ const BLOCK = false; const sc = new T.Scene(), root = new T.Group(); sc.add(root); const pr = ROOT, ps = sd; ROOT = root; sd = 31; const g = root;
""" + body + r"""
  { const me = G(2.95, 0, 1.9, -.5, g); me.userData.tag = 'tôi'; me.scale.setScalar(.42); avBuild(me, avOf(ST.player ? ST.player.av : 0), {}); }   /* mình đứng ở bến, mặc đồ trong tủ */
  ROOT = pr; sd = ps; root.updateWorldMatrix(true, true);
  const hits = []; root.traverse(o => { const t = o.userData.tag; if (t === 'phố TIỆM MAY CÔ BA' || t === 'phố CHỤP HÌNH' || t === 'bến' || t === 'đò'){ const bb = new T.Box3().setFromObject(o); hits.push([t, bb]); } });
  sc.background = new T.Color('#CFE6E0'); sc.add(new T.HemisphereLight('#fff4e2', '#94a474', 1.35)); sc.add(new T.AmbientLight('#ffffff', .22)); const l = new T.DirectionalLight('#fff0d4', 1.8); l.position.set(-4, 7, 5); l.castShadow = true; l.shadow.mapSize.set(MOBILE ? 1024 : 2048, MOBILE ? 1024 : 2048); Object.assign(l.shadow.camera, { left: -8, right: 8, top: 8, bottom: -8 }); l.shadow.bias = -.0005; sc.add(l);
  root.traverse(o => { if (o.isMesh){ o.receiveShadow = true; o.castShadow = o.castShadow !== false; o.userData.sway = 0; } });
  try { mergeRig(root, []); } catch (e) { console.warn('chmerge', e); }
  return { sc, root, hits }; }
function chFree(){ if (!CHM.B) return; CHM.B.sc.traverse(o => { if (o.geometry) o.geometry.dispose(); }); CHM.B = null; }
function chFade(txt, mid){ const f = $('#chFade'); f.querySelector('b').textContent = fxT(txt); f.hidden = false; f.classList.remove('out'); void f.offsetWidth; f.classList.add('in'); setTimeout(() => { try { mid(); } catch (e) { console.warn('ch', e); } f.classList.remove('in'); f.classList.add('out'); setTimeout(() => { f.hidden = true; }, 520); }, 900); }
function chSay(txt, who = 'Cô Ba'){ const b = $('#chSay'); b.innerHTML = `<b>${esc(fxT(who))}</b>${esc(fxT(txt))}`; b.hidden = false; b.classList.remove('pop'); void b.offsetWidth; b.classList.add('pop'); CHM.sayT = performance.now() + Math.max(4500, txt.length * 70); }
function chEnter(){ if (CHM.on || (ST.lv || 1) < CHM.lv) return; if (ST.xu < CHM.fare){ toast(`Tiền đò ${CHM.fare} xu, con bán bớt rau rồi đi nghe.`, 'dan'); return; }
  ST.xu -= CHM.fare; ST.ch = ST.ch || { n: 0 }; ST.ch.n++; save(); hud(); closeSheet(); sfx('pick');
  chFade('Đò máy chạy lên chợ huyện…', () => { chFree(); CHM.B = chBuild(); CHM.on = true; CHM.tx = CHM.tx0; ctl.enabled = false; document.body.classList.add('chon'); $('#chUi').hidden = false;
    if (!ST.seen.ch1){ ST.seen.ch1 = 1; save(); setTimeout(() => chSay('Chợ huyện đông vui ghê. Tiệm may cô Ba là cái tiệm sơn vàng, mái hiên sọc đỏ đó. Chạm vô tiệm là gặp cô Ba.', (ST.player && ST.player.name) || 'Con'), 700); } }); }
function chLeave(){ if (!CHM.on) return; chFade('Đò máy chạy về vườn…', () => { CHM.on = false; ctl.enabled = true; document.body.classList.remove('chon'); $('#chUi').hidden = true; $('#chSay').hidden = true; chFree(); }); }
function chCamSync(){ if (!CHM.cam) CHM.cam = new T.OrthographicCamera(-1, 1, 1, -1, .01, 200); const C = CHM.cam; C.left = cam.left; C.right = cam.right; C.top = cam.top; C.bottom = cam.bottom; C.zoom = (MOBILE && innerHeight > innerWidth ? 1.25 : .95); const tg = new T.Vector3(CHM.tx, .5, .45); C.position.copy(tg).add(new T.Vector3(.22, .62, 1).normalize().multiplyScalar(40)); C.lookAt(tg); C.updateProjectionMatrix(); C.updateMatrixWorld(); }
function chFrame(){ chCamSync(); if (CHM.sayT && performance.now() > CHM.sayT){ CHM.sayT = 0; $('#chSay').hidden = true; } }
function chTap(cx, cy){ if (!CHM.B) return; const v = new T.Vector2(cx / innerWidth * 2 - 1, -(cy / innerHeight) * 2 + 1), rc = new T.Raycaster(); rc.setFromCamera(v, CHM.cam); let best = null, bd = 1e9; for (const [t, bb] of CHM.B.hits){ const p = rc.ray.intersectBox(bb, new T.Vector3()); if (p){ const d = p.distanceTo(rc.ray.origin); if (d < bd){ bd = d; best = t; } } }
  if (best === 'phố TIỆM MAY CÔ BA'){ sfx('pick'); chShop(); } else if (best === 'phố CHỤP HÌNH'){ sfx('pick'); chSay((ST.lv || 1) >= 25 ? 'Tiệm chụp hình sắp mở cửa rồi. Bữa nào rủ Ngoại lên chụp chung một tấm nghe.' : 'Tiệm chụp hình đang sửa sang. Lên cấp 25 rủ Ngoại lên chụp chung một tấm.', 'Chú thợ hình'); } else if (best === 'bến' || best === 'đò'){ sfx('pick'); chLeave(); } }
function chShop(){ const nm = (ST.player && ST.player.name) || 'Con'; chSay(`${nm} đó hả? Lớn dữ vậy! Vải mới về cô đang soạn, mai mốt con ghé cô đo ni may cho bộ đồ nghe.`); }
addEventListener('pointerdown', e => { if (!CHM.on || e.target.id !== 'c') return; CHM.drag = { x: e.clientX, y: e.clientY, tx: CHM.tx, moved: false, id: e.pointerId }; }, true);
addEventListener('pointermove', e => { const d = CHM.drag; if (!CHM.on || !d || e.pointerId !== d.id) return; const dx = e.clientX - d.x; if (Math.abs(dx) > 8) d.moved = true; if (d.moved){ const k = (CHM.cam ? (CHM.cam.right - CHM.cam.left) / CHM.cam.zoom : 6) / innerWidth; CHM.tx = Math.max(-4.6, Math.min(5.6, d.tx - dx * k * 1.15)); } });
addEventListener('pointerup', e => { const d = CHM.drag; if (!CHM.on || !d || e.pointerId !== d.id) return; CHM.drag = null; if (!d.moved) chTap(e.clientX, e.clientY); });
function chRow(){ const lv = ST.lv || 1; if (lv >= CHM.lv){ sayOnce('ch21', 'Ngoại nghe nói cô Ba trên chợ huyện mới về vải mới đó con. Đi đò máy lên, tới bến hỏi tiệm may cô Ba là ai cũng biết.', 'vui'); return `<div class="chrow"><div><b>Đò máy lên chợ huyện</b><span>Tiệm may cô Ba, nhà lồng chợ, bến đò</span></div><button class="btn g" data-a="chgo">Đi đò · ${CHM.fare} xu</button></div>`; } return lv >= 18 ? `<div class="meta">Lên cấp ${CHM.lv} có đò máy lên chợ huyện.</div>` : ''; }
"""
# chèn sau phần tủ đồ (cần avOf), trước nhân vật vườn
rep("/* avatar đứng trong vườn, trước bậc thềm */\nawait LDY(0);\nlet AVW = null;", CH + "/* avatar đứng trong vườn, trước bậc thềm */\nawait LDY(0);\nlet AVW = null;")
# vẽ cảnh chợ thay vườn khi đang ở chợ
rep("r.render(S, cam); for (const g of SAPH) g.visible = true;", "if (CHM.on && CHM.B){ chFrame(); r.render(CHM.B.sc, CHM.cam); } else r.render(S, cam); for (const g of SAPH) g.visible = true;")
# chạm vườn bị chặn khi ở chợ
rep("canvas.addEventListener('pointerdown', e => { try { closeRing(); } catch (er) {}", "canvas.addEventListener('pointerdown', e => { if (CHM.on){ G0 = null; return; } try { closeRing(); } catch (er) {}")
# bến nhà: hàng đi đò
rep("function benHTML(){ const nOrd", "function benHTML(){ return chRow() + benHTML0(); }\nfunction benHTML0(){ const nOrd")
rep("if (a === 'tuwear'){", "if (a === 'chgo'){ chEnter(); return; } if (a === 'tuwear'){")
# giao diện ở chợ
rep('<canvas id="c"', '<div id="chUi" hidden><div id="chSay" hidden></div><button class="btn g" id="chBack">Về vườn</button></div><div id="chFade" hidden><b></b></div><canvas id="c"')
rep("$('#avb').addEventListener('click',", "$('#chBack').addEventListener('click', () => chLeave()); $('#avb').addEventListener('click',")
rep("button,[data-a],.btn{touch-action:manipulation}",
    "button,[data-a],.btn{touch-action:manipulation} body.chon > :not(#c):not(.ui.top):not(#chUi):not(#chFade):not(#sheet):not(#scrim):not(script):not(style):not(#load){visibility:hidden!important} body.chon .ui.top > :not(#avb):not(.coin){visibility:hidden} #chUi{position:fixed;left:0;right:0;bottom:calc(18px + env(safe-area-inset-bottom,0px));display:flex;flex-direction:column;align-items:center;gap:10px;z-index:5;pointer-events:none} #chUi > *{pointer-events:auto} #chBack{min-width:150px;height:52px;font-size:18px} #chSay{max-width:min(440px,calc(100vw - 32px));background:#FFF8EA;border-radius:18px;padding:10px 14px 11px;box-shadow:0 4px 0 #E3D3BC,0 10px 24px rgba(43,52,70,.25);font-size:15px;line-height:1.35;color:var(--ink)} #chSay b{display:block;font-family:var(--f-game);font-size:15px;color:#B02A1A;margin-bottom:2px} #chSay.pop{animation:fkIn .3s both cubic-bezier(.3,1.6,.5,1)} #chFade{position:fixed;inset:0;z-index:9;background:#2E4A5A;display:flex;align-items:center;justify-content:center;opacity:0;transition:opacity .45s} #chFade.in{opacity:1} #chFade.out{opacity:0} #chFade b{font-family:var(--f-game);color:#FBF2DA;font-size:22px} .chrow{display:flex;align-items:center;gap:10px;background:#FBF7EE;border-radius:16px;padding:10px 12px;box-shadow:0 3px 0 #E3D3BC;margin:4px 0 10px} .chrow div{flex:1} .chrow b{display:block;font-family:var(--f-game);font-size:17px;color:var(--ink)} .chrow span{font-size:13px;color:#6B4529}")
EN = {'Đò lên chợ huyện': 'Ferry to the district market', 'Đò máy lên chợ huyện': 'Motor ferry to the district market', 'Tiệm may cô Ba, nhà lồng chợ, bến đò': "Ms Ba's tailor shop, the market hall, the ferry pier", 'Về vườn': 'Back to the garden',
  'Đò máy chạy lên chợ huyện…': 'The ferry chugs up to the district market…', 'Đò máy chạy về vườn…': 'The ferry chugs home…', 'Cô Ba': 'Ms Ba', 'Con': 'You', 'Chú thợ hình': 'The photographer',
  'Chợ huyện đông vui ghê. Tiệm may cô Ba là cái tiệm sơn vàng, mái hiên sọc đỏ đó. Chạm vô tiệm là gặp cô Ba.': "The district market is so lively. Ms Ba's tailor shop is the yellow one with the red striped awning. Tap it to meet her.",
  'Tiệm chụp hình sắp mở cửa rồi. Bữa nào rủ Ngoại lên chụp chung một tấm nghe.': 'The photo studio opens soon. Bring Grandma up one day for a picture together.',
  'Tiệm chụp hình đang sửa sang. Lên cấp 25 rủ Ngoại lên chụp chung một tấm.': 'The photo studio is being done up. At level 25 bring Grandma for a picture together.',
  'Ngoại nghe nói cô Ba trên chợ huyện mới về vải mới đó con. Đi đò máy lên, tới bến hỏi tiệm may cô Ba là ai cũng biết.': "I hear Ms Ba at the district market just got new fabric, dear. Take the motor ferry up and ask anyone at the pier for her tailor shop."}
rep('["^còn (\\\\d+) (.+) nữa thì hạ giá$", "price drops after $1 more"]', '["^còn (\\\\d+) (.+) nữa thì hạ giá$", "price drops after $1 more"], ["^(.+) đó hả\\\\? Lớn dữ vậy! Vải mới về cô đang soạn, mai mốt con ghé cô đo ni may cho bộ đồ nghe\\\\.$", "$1, is that you? Look how you\'ve grown! I\'m still sorting the new fabric, come back soon and I\'ll measure you for an outfit."]')
rep('"Bán hết": "Sell all", ', '"Bán hết": "Sell all", ' + ''.join(json.dumps(k, ensure_ascii=False) + ': ' + json.dumps(v, ensure_ascii=False) + ', ' for k, v in EN.items()))
open(dst, 'w', encoding='utf-8').write(s)
print('ok', len(s))
