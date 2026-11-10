# -*- coding: utf-8 -*-
# v128 sau v127: đợt 1 "Cửa vào" (phút đầu của người chơi mới).
# 1. Lần đầu mở game hỏi ngôn ngữ (Tiếng Việt / English), không đoán theo máy. Người đã có vườn thì không hỏi. Đổi lại trong Cài đặt như cũ.
# 2. Bỏ đoạn chờ cố định ở màn tải: câu khẩu hiệu hiện sớm hơn, vườn dựng xong là vào (giữ tối thiểu 3 giây cho kịp đọc khẩu hiệu).
# 3. Liếp vừa gieo hiện bong bóng giọt nước cho tới khi được tưới lần đầu; chạm là tưới.
# 4. Một người dẫn trong phút đầu: thẻ "NGOẠI CHỈ" đi từng bước gieo -> tưới -> chờ -> hái -> bán (tới lần bán đầu tiên),
#    lời Ngoại nói ngay theo việc vừa làm thay vì xếp hàng chờ; thẻ việc hôm nay không chen vào lúc này.
# 5. Tiếng Anh: số ít ("1 bed"), "Tưới N liếp" là việc cần làm ("Water N beds").
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v127'", "BUILD = 'v128'")

# ---------- 1. chọn ngôn ngữ ----------
rep("""const LANG = (() => { try { const v = localStorage.getItem('mv2-lang'); if (v) return v; } catch (e) {} return 'vi'; })(), EN = LANG === 'en';""",
"""const LANG = await (async () => { try { const v = localStorage.getItem('mv2-lang'); if (v) return v; if (localStorage.getItem('mv2-state')) return 'vi'; } catch (e) { return 'vi'; }   /* v128: người mới tự chọn tiếng, không đoán theo máy; đã có vườn thì giữ tiếng Việt như trước */
  const L = document.getElementById('load'); if (!L || window.__noLangAsk) return 'vi';
  return await new Promise(res => { const d = document.createElement('div'); d.className = 'lang0'; d.setAttribute('role', 'group'); d.setAttribute('aria-label', 'Chọn ngôn ngữ · Choose language');
    d.innerHTML = '<p>Chọn ngôn ngữ · Choose language</p><button type="button" class="btn" data-k="vi">Tiếng Việt</button><button type="button" class="btn" data-k="en">English</button>'; L.classList.add('ask'); L.appendChild(d);
    d.addEventListener('click', e => { const b = e.target.closest('button'); if (!b) return; const k = b.dataset.k; try { localStorage.setItem('mv2-lang', k); } catch (er) {}
      if (k === 'en'){ try { const a = L.querySelector('.ltag .l1'), c = L.querySelector('.ltag .l2'), sp = L.querySelector('.lbar span'); if (a) a.textContent = 'Escape the city.'; if (c) c.textContent = 'Meet your new chores.'; if (sp) sp.textContent = 'Building the garden…'; L.setAttribute('aria-label', 'Building the garden'); } catch (er) {} }
      d.remove(); L.classList.remove('ask'); window.__t0 = performance.now(); res(k); }); }); })(), EN = LANG === 'en';""")
rep("""#load .ltag .l1{font-size:5cqw;opacity:0;animation:ltagin .55s cubic-bezier(.3,1.5,.5,1) 2.6s forwards}#load .ltag .l2{font-size:5.8cqw;color:#FFD27A;opacity:0;transform-origin:50% 60%;animation:ltagp .6s cubic-bezier(.3,1.7,.5,1) 3.4s forwards}""",
"""#load .ltag .l1{font-size:5cqw;opacity:0;animation:ltagin .55s cubic-bezier(.3,1.5,.5,1) .5s forwards}#load .ltag .l2{font-size:5.8cqw;color:#FFD27A;opacity:0;transform-origin:50% 60%;animation:ltagp .6s cubic-bezier(.3,1.7,.5,1) 1.2s forwards}#load.ask .ltag,#load.ask .lbar{display:none}#load .lang0{position:absolute;left:50%;bottom:calc(9% + env(safe-area-inset-bottom,0px));transform:translateX(-50%);z-index:3;display:flex;flex-direction:column;align-items:stretch;gap:12px;width:min(280px,76vw)}#load .lang0 p{margin:0 0 2px;text-align:center;font:400 16px/1.2 var(--f-game);color:#FBF7EE;text-shadow:0 2px 0 #4A2F1E,2px 0 0 #4A2F1E,-2px 0 0 #4A2F1E,0 -2px 0 #4A2F1E}#load .lang0 .btn{min-height:52px;font-size:19px}""")

# ---------- 2. bỏ chờ cố định ----------
rep("""wait = Math.max(900, (window.__ltag && !VISIT ? 5600 : 3300) - performance.now());""",
    """wait = Math.max(350, (window.__ltag && !VISIT ? 3000 : 0) - (performance.now() - (window.__t0 || 0)));   /* v128: dựng xong là vào; chỉ giữ đủ 3 giây cho câu khẩu hiệu */""")

# ---------- 3. bong bóng nước trên liếp vừa gieo ----------
rep("""Object.assign(p, { crop: k, g: 0, moist: Math.max(p.moist, .25), dry: 0, dead: false, cut: 0, fast: 0 });""",
    """Object.assign(p, { crop: k, g: 0, moist: Math.max(p.moist, .25), dry: 0, dead: false, cut: 0, fast: 0, nw: c.tree || PL[id].trellis || p.moist >= .6 ? 0 : 1 });   /* nw: gieo rồi mà chưa tưới lần nào */""")
rep("""function wet(id, amt){ const p = ST.plots[id], v = PV[id];""", """function wet(id, amt){ const p = ST.plots[id], v = PV[id]; p.nw = 0;""")
rep("""ripe(p) ? 'h' : (!P.trellis && p.moist <= 0) ? 'w' : null;""", """ripe(p) ? 'h' : (!P.trellis && (p.moist <= 0 || (p.nw && !VISIT && p.moist < .6))) ? 'w' : null;""")
rep("""if (!P.trellis && (p.moist <= 0 || condOf(p) === 'wilt')) return 'water'; return null; };""", """if (!P.trellis && (p.moist <= 0 || condOf(p) === 'wilt' || (p.nw && p.moist < .6))) return 'water'; return null; };""")

# ---------- 4. một người dẫn ----------
rep("""Ngoại chừa cho con một liếp nè. Chỗ nào có hình nhảy trên liếp là chỗ cần làm, chạm vô thử coi.`""", """Ngoại chừa cho con mấy liếp nè. Chạm vô liếp trống để gieo hạt nghe.`""")
rep('''["^Về rồi hả (.+)! Vô đây, Ngoại chừa cho con một liếp nè\\\\..*$", "You're home, $1! Come in, Grandma saved you a bed. Where an icon bounces on a bed, there's work to do; tap it and see."]''',
    '''["^Về rồi hả (.+)! Vô đây, Ngoại chừa cho con mấy liếp nè\\\\..*$", "You're home, $1! Come in, Grandma saved you a few beds. Tap an empty bed to sow seeds."], ["^Tưới 1 liếp$", "Water 1 bed"], ["^còn 1 (phút|min)$", "1 min left"], ["^còn (\\\\d+) (phút|min)$", "$1 min left"], ["^\\\\+(\\\\d+) xu$", "+$1 coins"], ["^(\\\\d+) xu/", "$1 coins/"], ["^Phủ rơm · còn 1 bó$", "Mulch · 1 bundle left"], ["^Phủ rơm · còn (\\\\d+) bó$", "Mulch · $1 bundles left"]''')
rep('''["^Tưới (\\\\d+) liếp$", "Watered $1 beds"]''', '''["^Tưới (\\\\d+) liếp$", "Water $1 beds"]''')
rep("""if (!PL[id].trellis) sayOnce('firstwater', 'Gieo xong nhớ tưới cho ướt đất nghe con. Đất khô thì hạt không lên.', 'dan'); },""",
    """if (!PL[id].trellis && !ST.seen.firstwater && !VISIT){ ST.seen.firstwater = 1; say('Gieo xong nhớ tưới cho ướt đất nghe con. Chạm giọt nước trên liếp là tưới.', 'dan', { now: true }); } },""")
rep("""water(id){ const p = ST.plots[id]; stepMark('water1'); aud('water'); rainOn(id); wet(id, 1);""", """water(id){ const p = ST.plots[id]; stepMark('water1'); aud('water'); rainOn(id); wet(id, 1); tutW();""")
rep("""avGo(P.id); wet(P.id, 1); refreshPlot(P.id); sfx('pick'); buzz(10);""", """avGo(P.id); wet(P.id, 1); if (!VISIT){ stepMark('water1'); tutW(); } refreshPlot(P.id); sfx('pick'); buzz(10);""")
rep("""else if (!ST.seen.sell) sayOnce('sell', 'Hái được rồi! Đem ra chợ bán lấy xu mua hạt mới nghe.', 'nhay');""",
    """else if (!ST.seen.sell && !VISIT){ ST.seen.sell = 1; say('Hái được rồi! Đem ra chợ bán lấy xu mua hạt mới nghe.', 'nhay', { now: true }); }""")
rep("""function nxq(){ const el = $('#nxq');""",
"""/* v128: phút đầu chỉ một người dẫn. Tới lần bán đầu tiên, thẻ việc đi từng bước gieo -> tưới -> chờ -> hái -> bán */
function tutStep(){ if (VISIT || !ST.player || (ST.lv || 1) > 2) return null; const s = ST.steps || {}; if (s.sell1 || (ST.soldN || 0) > 0) return null;
  if (s.harvest1) return Object.entries(ST.inv || {}).some(([k, n]) => n > 0 && GD(k) && !GD(k).nosell && (GD(k).sell || 0) > 0) ? { k: 'sell' } : null;
  const L = PLOTS.filter(P => !P.tree && !P.trellis && !P.bai && !locked(P) && !(P.exp && !EXP)), C = L.map(P => ST.plots[P.id]).filter(p => p && p.crop && !p.dead);
  const rp = C.find(ripe); if (rp) return { k: 'cut', crop: rp.crop };
  const canSow = L.some(P => { const p = ST.plots[P.id]; if (p && p.crop) return false; try { return !!seedFor(P); } catch (e) { return false; } });
  if (canSow && (!s.seed1 || !C.length)) return { k: 'seed' };
  if (!C.length) return null;
  if (C.some(p => p.nw || p.moist <= 0)) return { k: 'water' };
  let best = null, bl = 1e9; for (const p of C){ const c = CROPS[p.crop], left = (c.grow - p.g) / fastK(p); if (left < bl){ bl = left; best = p; } }
  return { k: 'wait', crop: best.crop, f: best.g / CROPS[best.crop].grow, left: bl }; }
function tutW(){ try { if (VISIT || ST.seen.firstwait || !tutStep()) return; ST.seen.firstwait = 1; say('Tưới rồi đó. Lứa đầu lớn lẹ lắm, chừng ba phút là hái được. Con gieo luôn mấy liếp còn lại đi.', 'vui', { now: true }); } catch (e) {} }
function tutGo(k){ const tu = tutStep(); if (k === 'sell') return openSheet('cho'); if (k === 'seed') return taskGo('plant'); if (k === 'water') return taskGo('water'); return taskGo('harvest', tu && tu.crop); }
function nxq(){ const el = $('#nxq');""")
rep("""  if (penFirst && (qIdle || (q && n === 6 && penFirst === 'ga') || !q)) penCard(penFirst);""",
"""  const tu = (() => { try { return tutStep(); } catch (e) { return null; } })();
  if (tu){ lab = 'NGOẠI CHỈ'; isTask = true; act = 'tut:' + tu.k; const tic = x => { try { return TASKIC(x); } catch (e) { return UIC.task; } };
    if (tu.k === 'seed'){ ic = UIC.seedbag || tic({ t: 'plant' }); t = 'Gieo lên liếp trống'; em = 'chạm liếp trống'; }
    else if (tu.k === 'water'){ ic = UIC.can || tic({ t: 'water' }); t = 'Tưới liếp vừa gieo'; em = 'chạm giọt nước'; }
    else if (tu.k === 'wait'){ ic = ICON[tu.crop] || UIC.sprout || UIC.task; t = 'Chờ rau lớn'; f = tu.f; em = `còn ${Math.max(1, Math.ceil(tu.left / 60))} phút`; }
    else if (tu.k === 'cut'){ ic = UIC.sickle || tic({ t: 'harvest', k: tu.crop }); t = 'Hái rau chín'; f = 1; em = 'chạm liếp chín'; }
    else { ic = UIC.coin || UIC.task; t = 'Đem rau ra Chợ bán'; em = 'mở Chợ'; } }
  else if (penFirst && (qIdle || (q && n === 6 && penFirst === 'ga') || !q)) penCard(penFirst);""")
rep("""else if (a.startsWith('task:')){ const [, t, k] = a.split(':'); taskGo(t, k); } else openBook('viec'); });""",
    """else if (a.startsWith('tut:')) tutGo(a.slice(4)); else if (a.startsWith('task:')){ const [, t, k] = a.split(':'); taskGo(t, k); } else openBook('viec'); });""")

# ---------- 5. tiếng Anh ----------
rep("""const UIEN = {"Ghé vườn": "Visit",""",
    """const UIEN = {"Buồng thay đồ · sửa soạn về vườn Ngoại": "Dressing room · getting ready for Grandma's garden", "Chọn dáng trước nghe con": "Pick a look first, dear", "Con · Vườn nhà Ngoại": "Dear · Grandma's Garden", "Ngoại gọi con là…": "Grandma calls you…", "Vườn nhà Ngoại": "Grandma's Garden", "Mã vườn bạn: MV-XXXX": "Friend's garden code: MV-XXXX", "Phủ rơm luôn?": "Mulch it too?", "Đất giữ ẩm lâu, cây lớn nhanh hơn": "Soil stays moist longer, crops grow faster", "NGOẠI CHỈ": "GRANDMA SAYS", "Gieo lên liếp trống": "Sow an empty bed", "Chạm để gieo liếp này · kéo xuống qua nhiều liếp": "Tap to sow this bed · drag down across several beds", "chạm liếp trống": "tap an empty bed", "Tưới liếp vừa gieo": "Water the sown bed", "chạm giọt nước": "tap the water drop", "Chờ rau lớn": "Wait for it to grow", "Hái rau chín": "Harvest the ripe crop", "chạm liếp chín": "tap the ripe bed", "Đem rau ra Chợ bán": "Sell it at the Market", "mở Chợ": "open the Market", "Gieo xong nhớ tưới cho ướt đất nghe con. Chạm giọt nước trên liếp là tưới.": "After sowing, water the soil, dear. Tap the water drop on a bed to water it.", "Tưới rồi đó. Lứa đầu lớn lẹ lắm, chừng ba phút là hái được. Con gieo luôn mấy liếp còn lại đi.": "Nicely watered. The first crop grows fast, about three minutes to harvest. Go sow the other beds too.", "Ghé vườn": "Visit",""")
rep("""const enT = t => { if (UIEN[t]) return UIEN[t]; let o = t; for (let k = 0; k < 2; k++) for (const [r, b] of UIRX) o = o.replace(r, b); return UIEN[o] || o; };""",
    """const EN1 = /(^|[^\\d.,:\\/])1 (beds|bags|coins|items|eggs|minutes|hours|days|orders|tasks|plots|hens|ducks|chicks|ducklings|times|friends|bundles|poles|fronds|baskets|jars|trees|dishes|pieces)\\b/g;   /* v128: số ít */
const enT = t => { if (UIEN[t]) return UIEN[t]; let o = t; for (let k = 0; k < 2; k++) for (const [r, b] of UIRX) o = o.replace(r, b); o = UIEN[o] || o; return o === t ? o : o.replace(EN1, (m, a, w) => a + '1 ' + (w === 'dishes' ? 'dish' : w.slice(0, -1))); };""")
rep("$('#inName').value.trim() || 'Con'", "$('#inName').value.trim() || (EN ? 'Dear' : 'Con')", 2)
rep("$('#inGarden').value.trim() || 'Vườn nhà Ngoại'", "$('#inGarden').value.trim() || (EN ? \"Grandma's Garden\" : 'Vườn nhà Ngoại')", 2)
rep("function enWalk(root){ if (!EN || !root) return;", "function enWalk(root){ if (!EN || !root) return; if (root.querySelectorAll) for (const i of root.querySelectorAll('[placeholder]')){ const a = i.getAttribute('placeholder'), e = enT(a); if (e !== a) i.setAttribute('placeholder', e); }   /* v128: chữ mờ trong ô nhập */")
rep("function mulchOffer(id){ if (", "function mulchOffer(id){ try { if (tutStep()) return; } catch (e) {}   /* v128: phút đầu không chen thêm lời mời phủ rơm */ if (")
rep('"Thêm lu": "Add a jar", "Thêm kệ": "Add a shelf"', '"Thêm lu": "Add jar", "Thêm kệ": "Add shelf"')   # v128: chữ tràn nút ở bản tiếng Anh
open(DST, 'w', encoding='utf-8').write(s)
print('ok', DST)
