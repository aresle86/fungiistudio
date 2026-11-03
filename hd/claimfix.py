#!/usr/bin/env python3
"""v100: việc hôm nay xong thì chạm Nhận (hoặc Nhận hết) mới cộng thưởng, xu bay lên ô xu; quà Ngoại là túi quà chạm mở;
nút Sổ chấm vàng đếm món chờ nhận; qua ngày mới còn món chưa nhận thì game tự cộng giùm."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# hoàn thành: chờ nhận, không tự cộng
rep("""if (x.have >= x.need){ x.done = true; setTimeout(() => gainXP(5), 0); if (x.rw[0] === 'coin'){ ST.xu += x.rw[1]; coinPop(`+${x.rw[1]} xu · thưởng việc`, '#9fd36a'); } else ST.inv.rom = (ST.inv.rom || 0) + x.rw[1]; hud(); toast(`Xong việc: ${x.txt}`); } }""",
    """if (x.have >= x.need){ x.done = true; x.cl = false; setTimeout(() => gainXP(5), 0); hud(); toast(`Xong việc: ${x.txt} · mở Sổ nhận thưởng`); soBadge(); } }""")
rep("""if (!ST.tasks.got && ST.tasks.list.every(x => x.done)){ ST.tasks.got = true; ST.seeds[ST.tasks.bonus] = (ST.seeds[ST.tasks.bonus] || 0) + 1; say(`Xong hết rồi hả? Nghỉ tay chút. Ngoại có bao hạt ${CROPS[ST.tasks.bonus].name.toLowerCase()} này cho con nè.`, 'nhay', { idle: true }); }""",
    """if (!ST.tasks.got && !ST.tasks.gr && ST.tasks.list.every(x => x.done)){ ST.tasks.gr = 1; say('Xong hết việc rồi hả? Nghỉ tay chút. Ngoại có gói quà trong Sổ cho con nè.', 'nhay', { idle: true }); }""")
# qua ngày mới: cộng giùm món chưa nhận
rep("""  const pool = TASKT.slice(), list = [];""",
    """  try { if (ST.tasks && ST.tasks.list){ let xu = 0, rom = 0; for (const x of ST.tasks.list) if (x.done && x.cl === false){ if (x.rw[0] === 'coin') xu += x.rw[1]; else rom += x.rw[1]; x.cl = true; } if (ST.tasks.gr && !ST.tasks.got){ ST.seeds[ST.tasks.bonus] = (ST.seeds[ST.tasks.bonus] || 0) + 1; ST.tasks.got = true; } if (xu || rom){ ST.xu += xu; ST.inv.rom = (ST.inv.rom || 0) + rom; setTimeout(() => toast(`Thưởng việc hôm qua chưa nhận, Ngoại cộng giùm: ${[xu ? '+' + xu + ' xu' : '', rom ? '+' + rom + ' rơm' : ''].filter(Boolean).join(', ')}`), 1500); } } } catch (e) {}   /* không để mất thưởng */
  const pool = TASKT.slice(), list = [];""")
# thẻ việc trong Sổ
rep("""  let h = UX.title(`Việc hôm nay · ${wd}`, `xong ${nd}/${T2.list.length} · mỗi việc +5 kinh nghiệm`);
  h += L.map(x => `<div class="tkc${x.done ? ' done' : ''}">""",
    """  let h = UX.title(`Việc hôm nay · ${wd}`, `xong ${nd}/${T2.list.length} · mỗi việc +5 kinh nghiệm`); const pend = T2.list.filter(x => x.done && x.cl === false);
  if (pend.length >= 2) h += `<button class="tkall" data-b="tkall"><img src="${UIC.coin}" alt=""><span>Nhận hết · ${pend.length} món</span></button>`;
  h += L.map(x => x.done && x.cl === false ? `<div class="tkc claim" data-ti="${T2.list.indexOf(x)}"><img src="${TASKIC(x)}" alt=""><div class="tt"><b>${x.txt}</b><span class="ok">Xong rồi, nhận thưởng nè</span></div><button class="tkcl" data-b="tkclaim" data-k="${T2.list.indexOf(x)}"><span><img src="${x.rw[0] === 'coin' ? UIC.coin : ICON.rom}" alt="">+${x.rw[1]}</span><em>Nhận</em></button></div>` : `<div class="tkc${x.done ? ' done' : ''}">""")
rep("""  const L = T2.list.slice().sort((a, b) => (a.done - b.done) || ((b.have / b.need) - (a.have / a.need)));""",
    """  const rk = x => x.done ? (x.cl === false ? 0 : 2) : 1, L = T2.list.slice().sort((a, b) => (rk(a) - rk(b)) || ((b.have / b.need) - (a.have / a.need)));   /* chờ nhận lên đầu, đã nhận xuống cuối */""")
rep("""  h += `<div class="tkc bonus${T2.got ? ' done' : ''}"><img src="${ICON[T2.bonus]}" alt=""><div class="tt"><b>${T2.got ? 'Đã nhận quà' : 'Xong hết việc hôm nay'}</b>""",
    """  h += T2.gr && !T2.got ? `<div class="tkc bonus gift"><img src="${ICON[T2.bonus]}" alt=""><div class="tt"><b>Quà của Ngoại</b><span>Xong hết việc hôm nay rồi, mở quà coi</span></div><button class="tkcl gift" data-b="tkgift"><span><img src="${UIC.seedbag}" alt="">+1</span><em>Mở quà</em></button></div>` : `<div class="tkc bonus${T2.got ? ' done' : ''}"><img src="${ICON[T2.bonus]}" alt=""><div class="tt"><b>${T2.got ? 'Đã nhận quà' : 'Xong hết việc hôm nay'}</b>""")
# xử lý chạm
rep("""  else if (a === 'taskgo'){ closeBook();""",
    """  else if (a === 'tkclaim'){ tkClaim([+k], b); return; } else if (a === 'tkall'){ tkClaim(ST.tasks.list.map((x, i) => i).filter(i => ST.tasks.list[i].done && ST.tasks.list[i].cl === false), b); return; }
  else if (a === 'tkgift'){ if (!ST.tasks.gr || ST.tasks.got) return; ST.tasks.got = true; ST.seeds[ST.tasks.bonus] = (ST.seeds[ST.tasks.bonus] || 0) + 1; save(); sfx('pop'); buzz(20); const r0 = b.getBoundingClientRect(); confettiAt(r0.left + r0.width / 2, r0.top, 26, .8); b.classList.add('open'); setTimeout(() => { toast(`Ngoại tặng 1 bao hạt ${CROPS[ST.tasks.bonus].name.toLowerCase()}`); soBadge(); renderBook(); }, 650); return; }
  else if (a === 'taskgo'){ closeBook();""")
rep("""function coinPop(txt, col = '#F5D27A'){""",
    """/* nhận thưởng việc: xu bay từ nút lên ô xu, đếm nhảy, leng keng */
function tkClaim(ids, btn){ const T2 = ST.tasks; let xu = 0, rom = 0; const r0 = btn.getBoundingClientRect(), xr = $('#xu').getBoundingClientRect();
  ids.forEach((i, j) => { const x = T2.list[i]; if (!x || !x.done || x.cl !== false) return; x.cl = true; const v = x.rw[1], isC = x.rw[0] === 'coin'; if (isC) xu += v; else rom += v;
    const card = document.querySelector(`.tkc[data-ti="${i}"]`), cr = (card && card.getBoundingClientRect()) || r0, n = isC ? Math.min(6, 2 + Math.round(v / 8)) : 3;
    for (let q = 0; q < n; q++) setTimeout(() => { const d = document.createElement('img'); d.src = isC ? UIC.coin : ICON.rom; d.className = 'tkfly'; d.style.left = (cr.right - 50 + (Math.random() - .5) * 30) + 'px'; d.style.top = (cr.top + cr.height / 2 + (Math.random() - .5) * 20) + 'px'; document.body.appendChild(d);
      requestAnimationFrame(() => requestAnimationFrame(() => { d.style.left = (isC ? xr.left + 22 : r0.left) + 'px'; d.style.top = (isC ? xr.top + xr.height / 2 : 40) + 'px'; d.style.transform = 'translate(-50%,-50%) scale(.6)'; d.style.opacity = '.2'; }));
      setTimeout(() => { d.remove(); if (isC){ sfx('coin'); const c = $('#xu'); c.classList.remove('bump'); void c.offsetWidth; c.classList.add('bump'); } }, 620); }, j * 220 + q * 70);
    if (card){ card.classList.add('got'); } });
  if (!xu && !rom) return; ST.xu += xu; ST.inv.rom = (ST.inv.rom || 0) + rom; save(); buzz(15); const tail = ids.length * 220 + 700;
  setTimeout(() => { hud(); coinPop([xu ? `+${xu} xu` : '', rom ? `+${rom} rơm` : ''].filter(Boolean).join(' · ') + ' · thưởng việc', '#9fd36a'); soBadge(); if (BOOK) renderBook(); }, tail); }
function coinPop(txt, col = '#F5D27A'){""")
# nút Sổ: chấm vàng đếm món chờ nhận
rep("""function soBadge(){ const b = $('#bSo'); if (!b) return; let d = b.querySelector('.kb'); if (!d){ d = document.createElement('span'); d.className = 'kb'; b.appendChild(d); } let left = 0, gold = false; try { ensureTasks(); left = ST.tasks.list.filter(x => !x.done).length;""",
    """function soBadge(){ const b = $('#bSo'); if (!b) return; let d = b.querySelector('.kb'); if (!d){ d = document.createElement('span'); d.className = 'kb'; b.appendChild(d); } let left = 0, gold = false, pend = 0; try { ensureTasks(); left = ST.tasks.list.filter(x => !x.done).length; pend = ST.tasks.list.filter(x => x.done && x.cl === false).length + (ST.tasks.gr && !ST.tasks.got ? 1 : 0);""")
rep("d.hidden = false; d.classList.remove('new'); d.classList.toggle('ok', left === 0); d.textContent = left ? String(left) : '✓';",
    "d.hidden = false; d.classList.remove('new'); d.classList.toggle('ok', left === 0 && !pend); d.classList.toggle('claim', pend > 0); d.textContent = pend ? String(pend) : left ? String(left) : '✓';")   # có thưởng chờ nhận: chấm vàng đếm món
CSS = r"""
/* ===== v100 nhận thưởng việc ===== */
.tkc.claim{background:linear-gradient(#FFF6D6,#FFEFC2);box-shadow:inset 0 0 0 2.5px #EDB940,0 3px 0 #D9A32E;animation:tkGlow 1.6s ease-in-out infinite}
@keyframes tkGlow{50%{box-shadow:inset 0 0 0 2.5px #F5CB52,0 3px 0 #D9A32E,0 0 14px rgba(245,203,82,.6)}}
.tkc.claim .ok{color:#B07A1E!important}
.tkc.got{transition:opacity .4s,transform .4s;opacity:.35;transform:scale(.97)}
.tkcl{flex:none;display:flex;flex-direction:column;align-items:center;gap:1px;border:0;cursor:pointer;padding:6px 10px 5px;border-radius:14px;background:linear-gradient(#9CD066,#7DB84A);box-shadow:inset 0 2px 0 rgba(255,255,255,.45),0 0 0 2px #4A2F1E,0 4px 0 2px #4A2F1E;color:#FFF8EA;font:400 13px var(--f-game);text-shadow:0 1.5px 0 rgba(74,47,30,.6)}
.tkcl span{display:flex;align-items:center;gap:2px;font-size:15px}.tkcl span img{width:20px;height:20px}
.tkcl em{font-style:normal;font-size:12px}
.tkcl:active{transform:translateY(3px);box-shadow:inset 0 2px 0 rgba(255,255,255,.45),0 0 0 2px #4A2F1E,0 1px 0 2px #4A2F1E}
.tkcl.gift{background:linear-gradient(#FF9A8A,#D9483A);animation:tkShake 1.8s ease-in-out infinite}
.tkcl.gift.open{animation:tkPop .5s ease-out forwards}
@keyframes tkShake{0%,70%,100%{transform:rotate(0)}75%{transform:rotate(-7deg)}80%{transform:rotate(7deg)}85%{transform:rotate(-5deg)}90%{transform:rotate(4deg)}}
@keyframes tkPop{40%{transform:scale(1.25)}100%{transform:scale(0);opacity:0}}
.tkc.gift{background:linear-gradient(#FFEDE6,#FFE0D6);box-shadow:inset 0 0 0 2.5px #F08A6E,0 3px 0 #D9483A}
.tkall{display:flex;align-items:center;justify-content:center;gap:8px;width:100%;margin:2px 0 10px;padding:9px 12px 8px;border:0;border-radius:14px;cursor:pointer;background:linear-gradient(#FFE27A,#F2C64A);box-shadow:inset 0 2px 0 rgba(255,255,255,.5),0 0 0 2px #4A2F1E,0 4px 0 2px #4A2F1E;font:400 17px var(--f-game);color:#4A2F1E}
.tkall img{width:28px;height:28px}.tkall:active{transform:translateY(3px)}
.tkfly{position:fixed;z-index:200;width:30px;height:30px;transform:translate(-50%,-50%);pointer-events:none;transition:left .58s cubic-bezier(.5,-.3,.7,1),top .58s cubic-bezier(.3,.6,.5,1),transform .58s,opacity .58s}
#xu.bump{animation:xuB .25s}@keyframes xuB{50%{transform:scale(1.12)}}
.bt .kb.claim{background:#F2C64A!important;color:#4A2F1E!important;box-shadow:0 0 0 2.5px #4A2F1E!important;animation:kbP 1.2s ease-in-out infinite}@keyframes kbP{50%{transform:scale(1.15)}}
"""
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
