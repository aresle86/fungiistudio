# v136: cảnh chợ nổi mới (bình minh, ghe chài, rạch Bến bà con) + Bến bà con phía game (chưa nối máy chủ)
import sys, os
SRC, DST = sys.argv[1], sys.argv[2]
HERE = os.path.dirname(os.path.abspath(__file__))
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v135'", "BUILD = 'v136'")
scene = open(os.path.join(HERE, 'cn136/game-scene.js'), encoding='utf-8').read()
ben = open(os.path.join(HERE, 'cn136/ben.js'), encoding='utf-8').read()
a, b = s.find('function cnoBuild(){'), s.find('function cnoTap(')
assert 0 < a < b and s.count('function cnoBuild(){') == 1
s = s[:a] + ben.rstrip() + '\n' + scene.rstrip() + '\n' + s[b:]
# máy quay phối cảnh cho chợ nổi
rep("function chCamSync(){ if (!CHM.cam) CHM.cam = new T.OrthographicCamera(-1, 1, 1, -1, .01, 200); const C = CHM.cam;",
    "function chCamSync(){ const cn0 = CHM.kind === 'cn'; if (!CHM.cam || !!CHM.cam.isPerspectiveCamera !== cn0) CHM.cam = cn0 ? new T.PerspectiveCamera(42, innerWidth / innerHeight, .1, 200) : new T.OrthographicCamera(-1, 1, 1, -1, .01, 200); const C = CHM.cam; if (cn0) return cnoCam(C);")
# kéo ngang chèo đi, kéo dọc lại gần / lùi xa
rep("tx: CHM.tx, moved: false, id: e.pointerId };", "tx: CHM.tx, dl: CNX.dl || 0, moved: false, id: e.pointerId };")
rep("const dx = e.clientX - d.x; if (Math.abs(dx) > 8) d.moved = true;",
    "const dx = e.clientX - d.x; if (CHM.kind === 'cn'){ const dy = e.clientY - d.y; if (!d.ax && Math.hypot(dx, dy) > 8){ d.ax = Math.abs(dx) >= Math.abs(dy) ? 'x' : 'y'; d.moved = true; } if (d.ax && !CNX.ben){ if (d.ax === 'x') CHM.tx = Math.max(-6, Math.min(6, d.tx - dx * 14 / innerWidth * (1 - .6 * d.dl))); else CNX.dl = Math.max(0, Math.min(1, d.dl - dy / innerHeight * 2.2)); } return; } if (Math.abs(dx) > 8) d.moved = true;")
rep("if (!d.moved) chTap(e.clientX, e.clientY); });",
    "if (!d.moved) chTap(e.clientX, e.clientY); });\naddEventListener('wheel', e => { if (!CHM.on || CHM.kind !== 'cn' || CNX.ben || !e.target || e.target.id !== 'c') return; CNX.dl = Math.max(0, Math.min(1, (CNX.dl || 0) - e.deltaY * .0015)); }, { passive: true });")
rep("function chTap(cx, cy){ if (!CHM.B) return;", "function chTap(cx, cy){ if (!CHM.B) return; if (CHM.kind === 'cn') cnoHits();")
rep("const d = p.distanceTo(rc.ray.origin);", "const d = p.distanceTo(rc.ray.origin) + (t === 'cn:ben' ? 1e3 : 0);")
rep("function cnoTap(best){ if (!best) return; sfx('pick'); $('#chSay').hidden = true; CNX.t0 = performance.now(); setTimeout(() => { if (CHM.on && CHM.kind === 'cn') openSheet('chono', best.slice(3)); }, 90); }",
    "function cnoTap(best){ if (!best) return; let a = best.slice(3); sfx('pick'); $('#chSay').hidden = true; if ((a === 'ben' || a.startsWith('bc:')) && !CNX.ben){ cnoBenV(1); return; } if (CNX.ben && a === 'so') a = 'ben'; CNX.t0 = performance.now(); setTimeout(() => { if (CHM.on && CHM.kind === 'cn') openSheet('chono', a); }, 90); }")
rep("CHM.B = cnoBuild(); CHM.on = true; CHM.tx = -1.4;", "CNX.bcL = null; CHM.B = cnoBuild(); CHM.on = true; CHM.tx = 0; CNX.dl = 0; CNX.ben = 0; CNX.bk = 0;")
rep("so.textContent = cnL('Sổ chợ', 'Notebook');", "so.textContent = cnL('Sổ chợ', 'Notebook'); $('#cnBen').hidden = false; cnoBenV(0); if (CNX.goBen){ CNX.goBen = 0; setTimeout(() => { if (CHM.on && CHM.kind === 'cn') cnoBenV(1); }, 600); }")
rep("'Chợ nổi đông vui ghê. Ghe nào treo gì trên cây bẹo là mua món đó. Chạm vô ghe để ghé, kéo ngang để chèo đi coi.', 'So lively! Each boat buys what hangs on its pole. Tap a boat to visit, drag sideways to row along.'",
    "'Chợ nổi đông vui ghê. Bảng tên ghe có hình món ghe đang kiếm bữa nay. Chạm vô ghe để ghé, kéo ngang để chèo đi coi, kéo lên xuống để lại gần hay lùi ra.', 'So lively! Each name board shows what that boat is buying today. Tap a boat to visit, drag sideways to row along, drag up or down to come closer or step back.'")
rep("$('#cnSo').hidden = true;", "$('#cnSo').hidden = true; $('#cnBen').hidden = true; CNX.ben = 0;")
rep("$('#cnSo').addEventListener('click', () => { sfx('pick'); openSheet('chono', 'so'); });",
    "$('#cnSo').addEventListener('click', () => { sfx('pick'); openSheet('chono', CNX.ben ? 'ben' : 'so'); }); $('#cnBen').addEventListener('click', () => { sfx('pick'); try { closeSheet(); } catch (e) {} cnoBenV(!CNX.ben); });")
rep('<button class="btn" id="cnSo" hidden>Sổ chợ</button>', '<button class="btn" id="cnBen" hidden>Bến bà con</button><button class="btn" id="cnSo" hidden>Sổ chợ</button>')
rep("#cnSo{min-width:110px;height:52px;font-size:18px;margin-right:10px}",
    "#cnSo,#cnBen{min-width:110px;height:52px;font-size:18px;margin-right:10px}\n@media (orientation:landscape) and (max-height:540px){#chUi:has(#cnBen:not([hidden])){flex-direction:row;justify-content:center;align-items:flex-end;bottom:calc(10px + env(safe-area-inset-bottom,0px))}}\n.cnpl{display:flex;gap:8px;margin:8px 0 2px}.cnpl button{flex:1;min-height:52px;appearance:none;border:0;border-radius:16px;background:#FBF7EE;box-shadow:0 3px 0 #E3D3BC;font:inherit;color:var(--ink);cursor:pointer}.cnpl button.on{background:#86B06A;color:#fff;box-shadow:0 3px 0 #6E9A54}.cnpl b{display:block;font-family:var(--f-game);font-weight:400;font-size:17px}.cnpl span{font-size:13px;font-weight:700}")
# bảng
rep("function cnoTitle(arg){ if (arg === 'so')", "function cnoTitle(arg){ if (arg === 'ben' || String(arg).startsWith('bc:')) return cnbTitle(arg); if (arg === 'so')")
rep("function cnoHTML(arg){ const c = cnoS(), nm = esc((ST.player && ST.player.name) || cnL('Con', 'Kid')); let h = '';",
    "function cnoHTML(arg){ const c = cnoS(), nm = esc((ST.player && ST.player.name) || cnL('Con', 'Kid')); let h = ''; if (arg === 'ben' || String(arg).startsWith('bc:')) return cnbHTML(arg);")
rep("function cnoEnter(){ if (CHM.on || (ST.lv || 1) < CNX.lv) return; const c = cnoS();", "function cnoEnter(){ if (CHM.on || (ST.lv || 1) < CNX.lv) return; try { cnbSync(); cnbLoad(); } catch (e) {} const c = cnoS();")
rep("if (a === 'cnogo') cnoEnter();", "if (a.startsWith('cnobc') || a === 'cnofind') return cnbAct(a, d, b); if (a === 'cnogo') cnoEnter();")
# nút "Ra bến tìm" ở đơn nhà bên và ghe bẹo
FIND = "${%s && (ST.lv || 1) >= CNX.lv ? `<button class=\"btn\" style=\"min-height:44px;white-space:nowrap\" data-a=\"cnofind\">${cnL('Ra bến tìm', 'To the pier')}</button>` : ''}"
rep('<button class="btn oskip" data-a="orddrop" data-k="${o.id}">Để bữa khác</button>', '<button class="btn oskip" data-a="orddrop" data-k="${o.id}">Để bữa khác</button>' + FIND % '!ok')
rep("- gheGot(o, k) - has(k)), 0)} món · ${o.xu} xu`}</button>", "- gheGot(o, k) - has(k)), 0)} món · ${o.xu} xu`}</button>" + FIND % '!full')
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
