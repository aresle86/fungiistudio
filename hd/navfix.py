#!/usr/bin/env python3
"""Chỉ đường cho người mới: (1) chạm thẻ Việc tiếp theo là camera bay tới chỗ làm, vòng sáng chỉ đúng chỗ, cầm sẵn đồ nghề;
(2) mũi tên mép màn hình chỉ về các bong bóng đang chờ mà nằm ngoài khung nhìn, chạm là bay tới.
Dùng: python3 navfix.py <vào> <ra>. Mỗi chỗ vá khớp đúng 1 lần."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b):
    global s
    c = s.count(a); assert c == 1, (c, a[:100]); s = s.replace(a, b)

# mọi bong bóng đăng ký vào một danh sách chung để mũi tên mép màn hình tìm
rep("function bubbleK(kind){ const g = DYN(G(0, 0, 0));",
    "function bubbleK(kind){ const g = DYN(G(0, 0, 0)); (window.__BUBALL = window.__BUBALL || []).push(g);")

# thẻ việc: việc hôm nay có đích để bay tới
rep("if (td){ try { ic = TASKIC(td); } catch (e) { ic = UIC.task; } t = td.txt;",
    "if (td){ try { ic = TASKIC(td); } catch (e) { ic = UIC.task; } act = 'task:' + td.t + ':' + (td.k || ''); t = td.txt;")
rep("else if (($('#nxq').dataset.a || '').startsWith('pen:')) penGo($('#nxq').dataset.a.slice(4)); else openBook('viec'); });",
    "else if (($('#nxq').dataset.a || '').startsWith('pen:')) penGo($('#nxq').dataset.a.slice(4)); else if (($('#nxq').dataset.a || '').startsWith('task:')){ const [, t, k] = $('#nxq').dataset.a.split(':'); taskGo(t, k); } else openBook('viec'); });\n" + r"""/* --- chỉ đường: bay tới chỗ làm việc hôm nay, vòng sáng nhấp nháy chỉ đúng chỗ --- */
let PING = null; const PINGS = { t: 9 };
function pingAt(x, z){ PINGS.x = x; PINGS.z = z; if (!PINGS.el){ PINGS.el = document.createElement('div'); PINGS.el.className = 'pinga'; document.body.appendChild(PINGS.el); } if (!PING){ PING = new T.Mesh(new T.RingGeometry(.34, .58, 40), new T.MeshBasicMaterial({ color: '#FFD23A', transparent: true, opacity: 0, depthWrite: false })); PING.rotation.x = -Math.PI / 2; PING.renderOrder = 6; PING.userData.keep = true; S.add(PING); } PING.position.set(x, .06, z); PINGS.t = 0; }
function pingTick(dt){ if (!PING) return; PINGS.t += dt; const t = PINGS.t, on = t < 3.6; PING.visible = on; if (PINGS.el){ PINGS.el.hidden = !on || busy(); if (on){ pv.set(PINGS.x, .55, PINGS.z).project(cam); PINGS.el.style.left = ((pv.x + 1) / 2 * innerWidth) + 'px'; PINGS.el.style.top = ((1 - pv.y) / 2 * innerHeight) + 'px'; } } if (!on) return; const k = (t % .9) / .9; PING.scale.setScalar(.7 + k * .6); PING.material.opacity = Math.min(1, (1 - k) * 1.3); }
function taskGo(t, k){ if (BOOK) closeBook(); if (SHEET) closeSheet(); const near = ids => { let best = null, bd = 1e9; const c = ctl.target; for (const id of ids){ const v = PV[id]; if (!v) continue; const d = Math.hypot(v.cx - c.x, v.cz - c.z); if (d < bd){ bd = d; best = v; } } return best; };
  const ok = P => !hidP(P) && !locked(P), L = PLOTS.filter(ok), W = w => L.filter(P => PV[P.id] && PV[P.id].want === w).map(P => P.id), crop = c => L.filter(P => ST.plots[P.id] && ST.plots[P.id].crop === c).map(P => P.id);
  let v = null, tool = null;
  if (t === 'water'){ v = near([...W('w'), ...W('u')]) || near(L.filter(P => ST.plots[P.id] && ST.plots[P.id].crop).map(P => P.id)); tool = { kind: 'water' }; }
  else if (t === 'harvest') v = near(W('h').filter(id => ST.plots[id].crop === k)) || near(crop(k)) || near(W('s'));
  else if (t === 'plant') v = near(W('s'));
  else if (t === 'mulch'){ v = near(L.filter(P => ST.plots[P.id] && ST.plots[P.id].crop && !(ST.plots[P.id].mulch > ST.gt)).map(P => P.id)); if ((ST.inv.rom || 0) > 0) tool = { kind: 'rom' }; }
  else if (t === 'sell'){ openSheet('cho'); return; }
  else if (t === 'buyrom'){ openSheet('cho'); SHEET.tab = 'mua'; renderSheet(); return; }
  if (!v) return openBook('viec');
  camTo(new T.Vector3(v.cx, .3, v.cz), Math.max(cam.zoom, DEFZ() * 1.15)); setTimeout(() => pingAt(v.cx, v.cz), 450); setTool(tool); }
/* --- mũi tên mép màn hình: bong bóng đang chờ mà nằm ngoài khung nhìn; mỗi phía một mũi tên (gần nhất), có số khi nhiều --- */
const NAVA = { el: {}, tgt: {}, wp: new T.Vector3(), t: 0 };
function navaEl(side){ let e = NAVA.el[side]; if (e) return e; e = document.createElement('button'); e.className = 'nava'; e.innerHTML = '<i class="nap"></i><img alt=""><b></b>'; e.hidden = true; document.body.appendChild(e);
  const go = ev => { ev.preventDefault(); ev.stopPropagation(); const p = NAVA.tgt[side]; if (!p) return; sfx('pick'); camTo(new T.Vector3(p.x, .3, p.z), Math.max(cam.zoom, DEFZ() * 1.1)); setTimeout(() => pingAt(p.x, p.z), 450); };
  e.addEventListener('pointerdown', ev => ev.stopPropagation()); e.addEventListener('click', go); return (NAVA.el[side] = e); }
function navaTick(dt){ NAVA.t += dt; if (NAVA.t < .12) return; NAVA.t = 0; const hide = () => { for (const k in NAVA.el) NAVA.el[k].hidden = true; };
  if (VISIT || FM.on || busy() || SUA || !ST.player) return hide(); const W = innerWidth, H = innerHeight, mx = 18, top = 96, bot = ng.hidden ? 132 : 210, cxs = W / 2, cys = (top + H - bot) / 2, best = {};
  const seen = new Set(), off = [];
  for (const g of (window.__BUBALL || [])){ let o = g, vis = true; while (o){ if (!o.visible){ vis = false; break; } o = o.parent; } if (!vis || !g.parent) continue; const pl = g.userData.pl, url = pl && pl.userData.url; if (!url) continue;
    g.getWorldPosition(NAVA.wp); pv.copy(NAVA.wp).project(cam); const sx = (pv.x + 1) / 2 * W, sy = (1 - pv.y) / 2 * H; if (sx > mx && sx < W - mx && sy > top && sy < H - bot){ seen.add(url); continue; } off.push({ sx, sy, url, x: NAVA.wp.x, z: NAVA.wp.z }); }
  for (const { sx, sy, url, x, z } of off){ if (seen.has(url)) continue;   /* loại này đang có cái thấy trên màn hình thì khỏi chỉ */
    const dx = sx - cxs, dy = sy - cys, side = Math.abs(dx) / (W / 2 - mx) > Math.abs(dy) / ((H - top - bot) / 2) ? (dx < 0 ? 'l' : 'r') : (dy < 0 ? 't' : 'b'), d = Math.hypot(dx, dy), B = best[side];
    if (!B || d < B.d) best[side] = { d, sx, sy, url, x, z, n: (B ? B.n : 0) + 1 }; else B.n++; }
  for (const side of ['l', 'r', 't', 'b']){ const B = best[side]; if (!B){ if (NAVA.el[side]) NAVA.el[side].hidden = true; NAVA.tgt[side] = null; continue; } const e = navaEl(side); NAVA.tgt[side] = B;
    const dx = B.sx - cxs, dy = B.sy - cys, k = Math.min((W / 2 - mx - 34) / Math.max(1, Math.abs(dx)), (H / 2 - (dy < 0 ? top : bot) + (dy < 0 ? 0 : 0) - 34) / Math.max(1, Math.abs(dy)), 1), px = cxs + dx * k, py = cys + dy * k;
    e.style.left = Math.max(mx + 30, Math.min(W - mx - 30, px)) + 'px'; e.style.top = Math.max(top + 30, Math.min(H - bot - 30, py)) + 'px'; e.querySelector('.nap').style.transform = `rotate(${Math.atan2(dy, dx)}rad)`;
    const im = e.querySelector('img'); if (im.dataset.u !== B.url){ im.src = B.url; im.dataset.u = B.url; } e.querySelector('b').textContent = B.n > 1 ? B.n : ''; e.hidden = false; } }
{ let lt = performance.now(); const L = () => { const n = performance.now(), dt = Math.min(.1, (n - lt) / 1000); lt = n; try { pingTick(dt); navaTick(dt); } catch (e) { if (!window.__nve){ window.__nve = 1; console.warn('nav', e); } } requestAnimationFrame(L); }; requestAnimationFrame(L); }""")

rep(".fbtns{display:flex;gap:8px;justify-content:center;margin-top:6px}",
    ".pinga{position:fixed;z-index:8;width:0;height:0;pointer-events:none}.pinga[hidden]{display:none}.pinga::after{content:'';position:absolute;left:-16px;top:-44px;border:16px solid transparent;border-top:22px solid #FFD23A;border-bottom:0;filter:drop-shadow(0 3px 0 #A8742A);animation:pgB .6s ease-in-out infinite}@keyframes pgB{50%{transform:translateY(-10px)}}\n.nava{position:fixed;z-index:9;width:50px;height:50px;margin:-25px 0 0 -25px;padding:0;border:0;border-radius:50%;background:#FFFBF2;box-shadow:0 0 0 4px #E8A23A,0 4px 0 4px #8A5D2E,0 8px 16px rgba(43,52,70,.3);cursor:pointer;animation:navB 1.6s ease-in-out infinite}.nava[hidden]{display:none}.nava img{position:absolute;inset:6px;width:38px;height:38px;pointer-events:none}.nava .nap{position:absolute;inset:0;pointer-events:none}.nava .nap::after{content:'';position:absolute;right:-21px;top:50%;margin-top:-13px;border:13px solid transparent;border-left:18px solid #E8A23A;border-right:0;filter:drop-shadow(0 2px 0 #8A5D2E)}.nava b{position:absolute;right:-6px;top:-6px;min-width:22px;height:22px;padding:0 5px;border-radius:11px;background:#C24A2E;color:#fff;font:400 14px/22px var(--f-game);box-shadow:0 0 0 2px #FFFBF2}.nava b:empty{display:none}@keyframes navB{50%{transform:scale(1.08)}}\n.fbtns{display:flex;gap:8px;justify-content:center;margin-top:6px}")

# Sổ › Việc hôm nay: mỗi việc chưa xong có nút "Đi làm" bay tới chỗ làm
rep("""(x.need > 1 ? UX.mbar(x.have / x.need, '#E9B23A') + `<span>${x.have}/${x.need}</span>` : '<span>Chưa làm</span>')}</div>""",
    """(x.need > 1 ? UX.mbar(x.have / x.need, '#E9B23A') + `<span>${x.have}/${x.need}</span>` : '<span>Chưa làm</span>')}${x.done ? '' : `<button class="tkgo" data-b="taskgo" data-k="${x.t}:${x.k || ''}">Đi làm ›</button>`}</div>""")
rep("""  else if (a === 'weedgo'){ closeBook(); weedGo(); return; }""",
    """  else if (a === 'weedgo'){ closeBook(); weedGo(); return; }
  else if (a === 'taskgo'){ closeBook(); const [t2, k2] = (k || '').split(':'); taskGo(t2, k2); return; }""")
rep(".nava{position:fixed;", ".tooling #nxq{visibility:hidden}.tkc .tkgo{display:inline-block;margin-top:6px;padding:5px 12px;border:0;border-radius:99px;background:#6E9F57;color:#fff;font:400 14px var(--f-game);box-shadow:0 3px 0 #4E7A3E;cursor:pointer}.tkc .tkgo:active{transform:translateY(2px);box-shadow:0 1px 0 #4E7A3E}\n.nava{position:fixed;")
open(sys.argv[2], 'w', encoding='utf8').write(s)
print('ok')
