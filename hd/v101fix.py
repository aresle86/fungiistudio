#!/usr/bin/env python3
"""v101: (1) việc Phủ rơm: thành 'Phủ rơm kín các liếp' — đếm liếp đã phủ / tổng liếp (không tính gốc cây, giàn); kín rồi thì tự xong, chờ nhận quà;
chạm thẻ việc chỉ bay tới liếp chưa phủ, không chỉ gốc cây hay giàn khổ qua. (2) thanh hạt trên điện thoại: vuốt ngang lướt thanh (có trớn),
chỉ khi kéo hẳn lên mới bốc hạt, hết gieo nhầm."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)
# ---- 1. phủ rơm kín ----
rep("() => ({ t: 'mulch', txt: 'Phủ rơm cho 1 liếp', need: 1, rw: ['rom', 1] }),",
    "() => ({ t: 'mulch', txt: 'Phủ rơm kín các liếp', need: 1, rw: ['coin', 15] }),")
rep("function bump(t, n = 1, k){ ensureTasks();",
    """const mulchBeds = () => PLOTS.filter(P => !P.tree && !P.trellis && !hidP(P) && !locked(P) && ST.plots[P.id]);
function mulchCheck(){ try { ensureTasks(); const x = ST.tasks.list.find(y => y.t === 'mulch'); if (!x || x.done) return; const E = mulchBeds(), m = E.filter(P => ST.plots[P.id].mulch > ST.gt).length; x.need = Math.max(1, E.length); x.have = Math.min(x.need, E.length ? m : 1); if (x.have >= x.need) bump('mulch', 0); } catch (e) {} }   /* kín hết liếp là xong, kể cả kín sẵn */
setInterval(mulchCheck, 3000);
function bump(t, n = 1, k){ ensureTasks();""")
rep("p.mulch = ST.gt + MULCH_DUR; avGo(id); bump('mulch');", "p.mulch = ST.gt + MULCH_DUR; avGo(id); mulchCheck();")
rep("v = near(L.filter(P => ST.plots[P.id] && ST.plots[P.id].crop && !(ST.plots[P.id].mulch > ST.gt)).map(P => P.id));",
    "v = near(mulchBeds().filter(P => !(ST.plots[P.id].mulch > ST.gt)).map(P => P.id));")
# migrate task cũ trong ngày
rep("function ensureTasks(){ const dk = dayKey(); if (ST.tasks && ST.tasks.day === dk){",
    "function ensureTasks(){ const dk = dayKey(); if (ST.tasks && ST.tasks.day === dk){ for (const x of ST.tasks.list) if (x.t === 'mulch' && x.txt !== 'Phủ rơm kín các liếp' && !x.done){ x.txt = 'Phủ rơm kín các liếp'; x.rw = ['coin', 15]; }")
# ---- 2. thanh hạt cảm ứng ----
rep("msc = e.pointerType === 'mouse' ? fan.querySelector('.fsc') : null, l0 = msc ? msc.scrollLeft : 0; let started = false, held = false, slid = false;",
    "msc = fan.querySelector('.fsc'), l0 = msc ? msc.scrollLeft : 0; let started = false, held = false, slid = false, vx = 0, lx = e.clientX, lt = performance.now(); e.preventDefault();")
rep("if (slid){ msc.scrollLeft = l0 - dx; return; } if (Math.hypot(dx, dy) > 10){ clearTimeout(ht); hideTip(); if (Math.abs(dy) > Math.abs(dx) * .8){ started = true; PEND = null; if (pickSeed(k, b)) beginStroke(ev); } else if (msc){ slid = true; msc.scrollLeft = l0 - dx; } } };",
    "{ const nt = performance.now(), d = nt - lt; if (d > 0){ vx = vx * .6 + (ev.clientX - lx) / d * .4; lx = ev.clientX; lt = nt; } } if (slid){ msc.scrollLeft = l0 - dx; return; } if (Math.abs(dx) > 8 && Math.abs(dx) >= Math.abs(dy) && msc){ clearTimeout(ht); hideTip(); slid = true; msc.scrollLeft = l0 - dx; return; } if (dy < -16 && Math.abs(dy) > Math.abs(dx) * 1.4){ clearTimeout(ht); hideTip(); started = true; PEND = null; if (pickSeed(k, b)) beginStroke(ev); } };   /* ngang = lướt thanh; chỉ kéo hẳn lên mới bốc hạt */")
rep("    if (held || slid) return; if (PEND && !TOOL && sowPend(k, b)) return;",
    "    if (slid && msc && Math.abs(vx) > .2){ let v = -vx * 16; const fl = () => { msc.scrollLeft += v; v *= .92; if (Math.abs(v) > .5) requestAnimationFrame(fl); }; requestAnimationFrame(fl); }   /* thả tay còn trớn */\n    if (held || slid) return; if (PEND && !TOOL && sowPend(k, b)) return;")
CSS = "\n.fsc,.fsc .sk{touch-action:none!important}\n"
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
