#!/usr/bin/env python3
"""v95: (1) thanh hạt kéo ngang được bằng chuột, lăn chuột, có nút mũi tên khi tràn;
(2) lời Ngoại theo tình trạng (sâu, héo, khô nước, việc lặt vặt) kèm điều kiện: tới lượt nói mà chuyện đã xong thì bỏ, đang nói mà xong thì tắt."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---------- 1. thanh hạt ----------
rep("""fan.innerHTML = (P ? `<div class="fhd">${P.tree ? 'Trồng ở ' + P.name.toLowerCase() : P.trellis ? 'Trồng ở giàn' : 'Gieo vào ' + P.name.toLowerCase()}</div>` : '') + `<div class="fsc">${h}</div>`;""",
    """fan.innerHTML = (P ? `<div class="fhd">${P.tree ? 'Trồng ở ' + P.name.toLowerCase() : P.trellis ? 'Trồng ở giàn' : 'Gieo vào ' + P.name.toLowerCase()}</div>` : '') + `<div class="fsc">${h}</div><button class="fnav l" aria-label="Xem hạt bên trái"></button><button class="fnav r" aria-label="Xem hạt bên phải"></button>`;""")
rep("fan.addEventListener('scroll', fanOvf, true);",
    """fan.addEventListener('scroll', fanOvf, true);
/* thanh hạt dài: lăn chuột lướt ngang, nút mũi tên hai đầu, kéo ngang chỗ trống cũng lướt */
fan.addEventListener('wheel', e => { const sc = fan.querySelector('.fsc'); if (!sc || sc.scrollWidth <= sc.clientWidth + 2) return; e.preventDefault(); sc.scrollLeft += Math.abs(e.deltaX) > Math.abs(e.deltaY) ? e.deltaX : e.deltaY; }, { passive: false });
fan.addEventListener('click', e => { const b = e.target.closest('.fnav'); if (!b) return; const sc = fan.querySelector('.fsc'); if (sc) sc.scrollBy({ left: (b.classList.contains('l') ? -1 : 1) * sc.clientWidth * .75, behavior: 'smooth' }); });
fan.addEventListener('pointerdown', e => { if (e.pointerType !== 'mouse' || e.target.closest('.sk, .fnav')) return; const sc = fan.querySelector('.fsc'); if (!sc) return; const x0 = e.clientX, l0 = sc.scrollLeft; const mv = ev => { sc.scrollLeft = l0 - (ev.clientX - x0); }, up = () => { removeEventListener('pointermove', mv); removeEventListener('pointerup', up); }; addEventListener('pointermove', mv); addEventListener('pointerup', up); });""")
# kéo trên thẻ hạt: dọc thì bốc hạt như cũ, ngang (chuột) thì lướt thanh
rep("""const k = b.dataset.k, x0 = e.clientX, y0 = e.clientY, pid = e.pointerId; let started = false, held = false;""",
    """const k = b.dataset.k, x0 = e.clientX, y0 = e.clientY, pid = e.pointerId, msc = e.pointerType === 'mouse' ? fan.querySelector('.fsc') : null, l0 = msc ? msc.scrollLeft : 0; let started = false, held = false, slid = false;""")
rep("""const mv = ev => { if (ev.pointerId !== pid || started) return; const dx = ev.clientX - x0, dy = ev.clientY - y0; if (Math.hypot(dx, dy) > 10){ clearTimeout(ht); hideTip(); if (Math.abs(dy) > Math.abs(dx) * .8){ started = true; PEND = null; if (pickSeed(k, b)) beginStroke(ev); } } };""",
    """const mv = ev => { if (ev.pointerId !== pid || started) return; const dx = ev.clientX - x0, dy = ev.clientY - y0; if (slid){ msc.scrollLeft = l0 - dx; return; } if (Math.hypot(dx, dy) > 10){ clearTimeout(ht); hideTip(); if (Math.abs(dy) > Math.abs(dx) * .8){ started = true; PEND = null; if (pickSeed(k, b)) beginStroke(ev); } else if (msc){ slid = true; msc.scrollLeft = l0 - dx; } } };""")
rep("""    if (held) return; if (PEND && !TOOL && sowPend(k, b)) return;""",
    """    if (held || slid) return; if (PEND && !TOOL && sowPend(k, b)) return;""")
css = """.fnav{position:absolute;top:50%;width:34px;height:34px;margin-top:-13px;border:0;border-radius:50%;background:#FBF7EE;box-shadow:0 0 0 2.5px #8A5D3B,0 3px 0 #6B4529;cursor:pointer;z-index:2;padding:0}
.fnav::before{content:"";position:absolute;left:50%;top:50%;width:9px;height:9px;border-left:3px solid #6B4529;border-bottom:3px solid #6B4529;transform:translate(-30%,-50%) rotate(45deg)}
.fnav.r::before{transform:translate(-70%,-50%) rotate(-135deg)}
.fnav.l{left:-6px}.fnav.r{right:-6px}.fnav:active{transform:translateY(2px);box-shadow:0 0 0 2.5px #8A5D3B,0 1px 0 #6B4529}
.fsc:not(.ovf)~.fnav,.fsc.atL~.fnav.l,.fsc.atR~.fnav.r{display:none}
.fan{overflow:visible!important}.fsc{border-radius:var(--r3)}
@media (hover:none){.fnav{display:none!important}}
"""
i = s.rindex('</style>'); s = s[:i] + css + s[i:]

# ---------- 2. lời Ngoại đúng lúc ----------
rep("""ng.addEventListener('click', () => { if (SAYQ.length){ const [a, b] = SAYQ.shift(); say(a, b, { now: true }); } else { ng.hidden = true; sayT = 0; } });""",
    """ng.addEventListener('click', () => { if (!(SAYQ.length && sayPop(SAYQ))){ ng.hidden = true; sayT = 0; } });""")
rep("""const SAYQ = [];""",
    """const SAYQ = []; let SAYOK = null;
/* câu nói theo tình trạng vườn mang điều kiện ok(): tới lượt mà chuyện đã xong (sâu bắt rồi, liếp tưới rồi) thì bỏ, không nói trễ */
const sayOkNow = o => { try { return !o || !o.ok || !!o.ok(); } catch (e) { return false; } };
function sayPop(Q){ while (Q.length){ const [t, m, o] = Q.shift(); if (sayOkNow(o)){ say(t, m, { now: true, ok: o && o.ok }); return true; } if (o && o.key && ST.seen) delete ST.seen[o.key]; } return false; }""")
rep("""const [t, m] = IDLEQ.shift(); say(t, m, { now: true }); IDLE0 = performance.now();""",
    """if (sayPop(IDLEQ)) IDLE0 = performance.now();""")
rep("""if (SAYQ.length && !busy()){ const [a, b] = SAYQ.shift(); say(a, b, { now: true }); }""",
    """if (SAYQ.length && !busy() && sayPop(SAYQ)){}""")
rep("""  if (sayT > 0){ sayT -= dt; if (sayT <= 0){""",
    """  if (sayT > 0 && SAYOK && !ng.hidden && !sayOkNow({ ok: SAYOK })){ SAYOK = null; sayT = Math.min(sayT, .01); }   /* chuyện Ngoại đang nói đã xong (bắt sâu rồi, tưới rồi) thì thôi nói */
  if (sayT > 0){ sayT -= dt; if (sayT <= 0){""")
rep("""function say(txt, mood = 'vui', o = {}){ if (!txt) return; if (!o.now && !o.love && SAYH.slice(-5).some(h => h.t === txt) && o.idle) return; if (o.idle){ try { if (busy() || IDLEQ.length){ if (!IDLEQ.some(q => q[0] === txt)) IDLEQ.push([txt, mood]); return; } } catch (e) {} } if (sayT > 0 && !o.now && !ng.hidden){ if (!SAYQ.some(q => q[0] === txt) && $('#ngoaiTxt').textContent !== txt){ SAYQ.push([txt, mood]); if (SAYQ.length > 3) SAYQ.shift(); } return; } txt = sayFilter(txt, o);""",
    """function say(txt, mood = 'vui', o = {}){ if (!txt) return; if (!sayOkNow(o)) return; const qm = o.ok || o.key ? { ok: o.ok, key: o.key } : null; if (!o.now && !o.love && SAYH.slice(-5).some(h => h.t === txt) && o.idle) return; if (o.idle){ try { if (busy() || IDLEQ.length){ if (!IDLEQ.some(q => q[0] === txt)) IDLEQ.push([txt, mood, qm]); return; } } catch (e) {} } if (sayT > 0 && !o.now && !ng.hidden){ if (!SAYQ.some(q => q[0] === txt) && $('#ngoaiTxt').textContent !== txt){ SAYQ.push([txt, mood, qm]); if (SAYQ.length > 3) SAYQ.shift(); } return; } SAYOK = o.ok || null; txt = sayFilter(txt, o);""")
rep("""function sayOnce(key, txt, mood){ if (VISIT) return; if (ST.seen[key]) return; ST.seen[key] = 1; say(txt, mood, { idle: true }); }""",
    """function sayOnce(key, txt, mood, ok){ if (VISIT) return; if (ST.seen[key]) return; if (ok && !sayOkNow({ ok })) return; ST.seen[key] = 1; say(txt, mood, { idle: true, ok, key: ok ? key : undefined }); }""")
# việc lặt vặt: chỉ nói khi món đó còn nằm đó
rep("""la: 'Lá khô rụng đầy sân kìa con. Quét gom lại, để dành ủ phân bón rau.' }[o.k], 'dan'); }""",
    """la: 'Lá khô rụng đầy sân kìa con. Quét gom lại, để dành ủ phân bón rau.' }[o.k], 'dan', (k => () => ST.odd.list.some(x => x.k === k))(o.k)); }""")
# khô nước / héo / chết: chỉ nói khi liếp vẫn còn y vậy
rep("""if (s === 'thirst') sayOnce('thirst1', `Liếp ${n} khô rồi, tưới chút nước nghen. Thấy giọt nước nhảy trên liếp là liếp cần tưới.`, 'dan'); else if (s === 'wilt' || s === 'dead') TIPW.push([s, N]); }""",
    """if (s === 'thirst') sayOnce('thirst1', `Liếp ${n} khô rồi, tưới chút nước nghen. Thấy giọt nước nhảy trên liếp là liếp cần tưới.`, 'dan', (id => () => { const q = ST.plots[id]; return !!(q && q.crop && !q.dead && q.moist <= 0); })(P.id)); else if (s === 'wilt' || s === 'dead') TIPW.push([s, N, P.id, p.crop]); }""")
rep("""Héo thì tưới, khô thì dọn trồng lại.`, 'lo'); } }""",
    """Héo thì tưới, khô thì dọn trồng lại.`, 'lo', { ok: () => TIPW.every(([s0, , id, cr]) => { const q = ST.plots[id]; return !!(q && q.crop === cr && (s0 === 'dead' ? q.dead : !q.dead && condOf(q) === 'wilt')); }) }); } }""")
open(sys.argv[2], 'w', encoding='utf8').write(s)
print('ok')
