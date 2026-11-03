p='live/vuon3d.html';s=open(p,encoding='utf8').read()
def rep(a,b,cnt=1):
    global s
    n=s.count(a); assert n==cnt,(n,a[:90]); s=s.replace(a,b)
rep("if (!ST || ST.v !== 1 || !ST.plots) ST = NEWST();","""if (!ST || ST.v !== 1 || !ST.plots) ST = NEWST();
/* ---------- giờ trong vườn: một ngày 40 phút ngoài đời (bình minh 4 · ngày 28 · chạng vạng 4 · đêm 4) ---------- */
const DAYM = 40, DSEG = [[0, 4, 5.0, 6.4], [4, 32, 6.4, 17.6], [32, 36, 17.6, 19.0], [36, 40, 19.0, 29.0]];
const mAt = h => { if (h < 5) h += 24; for (const [m0, m1, h0, h1] of DSEG) if (h >= h0 && h <= h1) return m0 + (h - h0) / (h1 - h0) * (m1 - m0); return 0; };
const hAt = m => { m = ((m % DAYM) + DAYM) % DAYM; for (const [m0, m1, h0, h1] of DSEG) if (m >= m0 && m < m1) return (h0 + (m - m0) / (m1 - m0) * (h1 - h0)) % 24; return 6; };
if (ST.clk0 == null) ST.clk0 = Date.now() - mAt(!ST.seen || (!ST.seen.sold && (ST.gt || 0) < 120) ? 5.6 : 9) * 60000;   // vườn mới mở màn lúc bình minh
if (ST.tm == null) ST.tm = ST.realTime === false ? 'fixed' : 'game';
const HOLD = 16.4;   // lúc làm quen (chưa bán lần đầu) trời không qua khỏi buổi chiều
function gameHour(ms = Date.now()){ let m = (ms - ST.clk0) / 60000; if (!VISIT && ST.seen && !ST.seen.sold && ms >= Date.now() - 1000){ const cap = mAt(HOLD); if (m > cap){ ST.clk0 = ms - cap * 60000; m = cap; } } return hAt(m); }
const hourAt = ms => ST.tm === 'real' ? (d => d.getHours() + d.getMinutes() / 60)(new Date(ms)) : ST.tm === 'day' ? 10 : ST.tm === 'fixed' ? ST.ovr : gameHour(ms);""")
rep("const sunAt = ms => { const h = new Date(ms).getHours(); return h >= NONG.sun[0] && h < NONG.sun[1]; };","const sunAt = ms => { const h = hourAt(ms); return h >= NONG.sun[0] && h < NONG.sun[1]; };")
s=s.replace("HOUR = ST.realTime ? realHour() : ST.ovr;","HOUR = hourAt(Date.now());")
assert s.count("HOUR = hourAt(Date.now());")==2
rep("if (new Date().getHours() < GHE.from) return; g.d = dk;","g.d = dk;")
rep("""    h += `<div class="sub">Trời</div><div class="acts"><button class="btn" data-a="real" aria-pressed="${ST.realTime}">Theo giờ thật</button>${[['Sáng', 6.4], ['Trưa', 12], ['Chiều', 16.8], ['Tối', 20.5]].map(([n, v]) => `<button class="btn" data-a="hour" data-v="${v}" aria-pressed="${!ST.realTime && ST.ovr === v}">${n}</button>`).join('')}</div>`;""",
"""    h += `<div class="sub">Trời trong vườn</div><div class="acts">${[['game', 'Giờ trong vườn'], ['real', 'Theo giờ thật'], ['day', 'Luôn ban ngày']].map(([k, n]) => `<button class="btn${ST.tm === k ? ' g' : ''}" data-a="tm" data-k="${k}" aria-pressed="${ST.tm === k}">${n}</button>`).join('')}</div><div class="meta">${ST.tm === 'game' ? 'Một ngày trong vườn chừng 40 phút: sáng, trưa, chiều, tối đổi liền liền. Quà, việc, ghe chợ nổi vẫn tính theo ngày thật.' : ST.tm === 'real' ? 'Trời trong vườn y như ngoài đời, chơi buổi tối là thấy vườn ban đêm.' : 'Trời luôn sáng, dễ nhìn. Nong phơi lúc nào cũng có nắng.'}</div>`;
    h += `<details class="uxm"><summary>Chỉnh tay giờ trong vườn</summary><div><div class="acts">${[['Sáng', 6.4], ['Trưa', 12], ['Chiều', 16.8], ['Tối', 20.5]].map(([n, v]) => `<button class="btn" data-a="hour" data-v="${v}" aria-pressed="${ST.tm === 'fixed' && ST.ovr === v}">${n}</button>`).join('')}</div></div></details>`;""")
rep("else if (a === 'real'){ ST.realTime = true; save(); } else if (a === 'hour'){ ST.realTime = false; ST.ovr = +b.dataset.v; save(); }",
"else if (a === 'real'){ ST.tm = 'real'; ST.realTime = true; save(); } else if (a === 'tm'){ ST.tm = b.dataset.k; ST.realTime = b.dataset.k === 'real'; save(); } else if (a === 'hour'){ ST.tm = 'fixed'; ST.realTime = false; ST.ovr = +b.dataset.v; save(); }")
# đêm đủ sáng để chơi
for old,new in [("[0, '#2a3a66', '#1a2234', .55, '#9fb4ff', .32, .14, 1, '#24324f', .95]","[0, '#4a5a8e', '#2a3346', .9, '#a8bcff', .42, .24, 1, '#2E3E62', 1.05]"),
 ("[4.6, '#2a3a66', '#1a2234', .55, '#9fb4ff', .32, .14, 1, '#24324f', .95]","[4.6, '#4a5a8e', '#2a3346', .9, '#a8bcff', .42, .24, 1, '#2E3E62', 1.05]"),
 ("[19, '#5a5a8a', '#2a2a3a', .7, '#9a8aff', .38, .13, .85, '#3a3f66', .95]","[19, '#6a6a9a', '#3a3a4a', .95, '#a89aff', .45, .22, .85, '#454a72', 1.02]"),
 ("[20, '#2a3a66', '#1a2234', .55, '#9fb4ff', .32, .14, 1, '#24324f', .95]","[20, '#4a5a8e', '#2a3346', .9, '#a8bcff', .42, .24, 1, '#2E3E62', 1.05]"),
 ("[24, '#2a3a66', '#1a2234', .55, '#9fb4ff', .32, .14, 1, '#24324f', .95]]","[24, '#4a5a8e', '#2a3346', .9, '#a8bcff', .42, .24, 1, '#2E3E62', 1.05]]")]:
    rep(old,new)
open(p,'w',encoding='utf8').write(s); print('ok')
