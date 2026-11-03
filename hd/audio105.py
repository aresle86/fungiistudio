#!/usr/bin/env python3
"""v105: âm thanh giàu hơn, tạo hết bằng code — bộ trộn 3 kênh (nhạc, môi trường, hiệu ứng), nền môi trường theo giờ và chỗ đang nhìn
(gió, nước, chim, ve, dế, ếch, gà gáy, cá quẫy, mái chèo), nhạc đàn tranh thưa, tiếng sự kiện và tiếng thao tác. Không âm trầm."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

rep("let SFXOUT = null; const out = () => { if (!SFXOUT){ const hp = AC.createBiquadFilter(); hp.type = 'highpass'; hp.frequency.value = 260; const g = AC.createGain(); g.gain.value = .55; hp.connect(g).connect(AC.destination); SFXOUT = hp; } return SFXOUT; };",
    "let SFXOUT = null, SFXG = null; const out = () => { if (!SFXOUT){ const hp = AC.createBiquadFilter(); hp.type = 'highpass'; hp.frequency.value = 260; const g = AC.createGain(); g.gain.value = .55 * VOL().sfx; SFXG = g; hp.connect(g).connect(AC.destination); SFXOUT = hp; } return SFXOUT; };\n"
    r"""/* ===== v105 âm thanh: 3 kênh, nền môi trường, nhạc thưa, sự kiện — tạo hết bằng code, lọc bỏ âm trầm ===== */
function VOL(){ return Object.assign({ mus: .35, amb: .6, sfx: 1 }, (ST && ST.vol) || {}); }
let BUS = null, NZB = null, BED = null;
function bus(){ if (!AC) return null; if (BUS) return BUS; const mk = (hpF, v) => { const hp = AC.createBiquadFilter(); hp.type = 'highpass'; hp.frequency.value = hpF; const g = AC.createGain(); g.gain.value = v; const dk = AC.createGain(); dk.gain.value = 1; hp.connect(g).connect(dk).connect(AC.destination); return { in: hp, g, dk }; }; const v = VOL(); BUS = { amb: mk(230, .5 * v.amb), mus: mk(260, .42 * v.mus) }; return BUS; }
function busVol(){ const v = VOL(); if (BUS){ BUS.amb.g.gain.value = .5 * v.amb; BUS.mus.g.gain.value = .42 * v.mus; } if (SFXG) SFXG.gain.value = .55 * v.sfx; }
function audDuck(){ if (!AC || !BUS) return; const t = AC.currentTime; for (const b of [BUS.amb, BUS.mus]){ b.dk.gain.cancelScheduledValues(t); b.dk.gain.setTargetAtTime(.45, t, .15); b.dk.gain.setTargetAtTime(1, t + 3.2, .8); } }   /* Ngoại nói: nền nhỏ lại */
const noiseBuf = () => NZB || (NZB = (() => { const n = AC.sampleRate * 2, b = AC.createBuffer(1, n, AC.sampleRate), d = b.getChannelData(0); for (let i = 0; i < n; i++) d[i] = Math.random() * 2 - 1; return b; })());
function nzz(t0, dur, f, q, v, dest, f2, type = 'bandpass'){ const s = AC.createBufferSource(); s.buffer = noiseBuf(); s.loop = true; const bp = AC.createBiquadFilter(); bp.type = type; bp.frequency.setValueAtTime(f, t0); if (f2) bp.frequency.exponentialRampToValueAtTime(f2, t0 + dur); bp.Q.value = q; const g = AC.createGain(); g.gain.setValueAtTime(.0001, t0); g.gain.linearRampToValueAtTime(v, t0 + Math.min(.02, dur * .25)); g.gain.exponentialRampToValueAtTime(.0001, t0 + dur); s.connect(bp).connect(g).connect(dest); s.start(t0, Math.random() * 1.5); s.stop(t0 + dur + .05); }
function tone(t0, dur, f, f2, v, dest, type = 'sine', att = .008){ const o = AC.createOscillator(); o.type = type; o.frequency.setValueAtTime(f, t0); if (f2) o.frequency.exponentialRampToValueAtTime(f2, t0 + dur); const g = AC.createGain(); g.gain.setValueAtTime(.0001, t0); g.gain.linearRampToValueAtTime(v, t0 + att); g.gain.exponentialRampToValueAtTime(.0001, t0 + dur); o.connect(g).connect(dest); o.start(t0); o.stop(t0 + dur + .05); }
const AMBS = {   /* tiếng môi trường, gọi với (t, đích) */
  chich: (t, d) => { const n = 4 + (Math.random() * 4 | 0), f = 3200 + Math.random() * 900; for (let i = 0; i < n; i++) tone(t + i * .07, .05, f + (i % 2) * 260, f + 600, .05, d); },   /* chim chích: líu lo nhanh */
  chaomao: (t, d) => { const base = 1700 + Math.random() * 300, m = [1, 1.26, 1.12, 1.5]; for (let i = 0; i < 3 + (Math.random() * 2 | 0); i++) tone(t + i * .16, .14, base * m[i % 4], base * m[i % 4] * 1.06, .06, d, 'sine', .02); },   /* chào mào: 3-4 nốt có giai điệu */
  sao: (t, d) => { tone(t, .32, 1500, 2600, .05, d, 'sine', .04); tone(t + .38, .2, 2400, 1900, .04, d, 'sine', .02); },   /* sáo: huýt luyến */
  ve: (t, d) => nzz(t, 2.6, 6300, 9, .03, d),   /* ve trưa */
  de: (t, d) => { for (let i = 0; i < 3; i++) tone(t + i * .05, .025, 4600, null, .03, d); },   /* dế */
  ech: (t, d) => { for (let i = 0; i < 2; i++){ tone(t + i * .22, .12, 460, 320, .07, d, 'triangle', .01); nzz(t + i * .22, .06, 900, 3, .02, d); } },   /* ếch ộp, giữ trên 300 Hz */
  nhai: (t, d) => { for (let i = 0; i < 6; i++) nzz(t + i * .045, .02, 1600, 6, .04, d); },
  ga: (t, d) => { const o = AC.createOscillator(); o.type = 'sawtooth'; const bp = AC.createBiquadFilter(); bp.type = 'bandpass'; bp.frequency.value = 1100; bp.Q.value = 2.5; const g = AC.createGain(); g.gain.setValueAtTime(.0001, t); g.gain.linearRampToValueAtTime(.05, t + .08); g.gain.setValueAtTime(.05, t + 1.0); g.gain.exponentialRampToValueAtTime(.0001, t + 1.4);
    for (const [dt, f] of [[0, 560], [.18, 820], [.45, 900], [.8, 760], [1.2, 520]]) o.frequency.linearRampToValueAtTime(f, t + dt); o.connect(bp).connect(g).connect(d); o.start(t); o.stop(t + 1.5); },   /* gà gáy xa */
  tom: (t, d) => { tone(t, .1, 900, 240, .08, d); nzz(t, .09, 1300, 1.2, .05, d); tone(t + .12, .05, 1700, 1500, .02, d); },   /* cá quẫy tõm */
  cheo: (t, d) => { nzz(t, .35, 600, 1.5, .05, d, 320); tone(t + .38, .04, 1900, 1700, .015, d); tone(t + .5, .04, 2100, 1800, .012, d); } };   /* mái chèo xa */
const AUDF = {   /* tiếng sự kiện, thao tác: đi qua kênh hiệu ứng */
  ghe: (t, d) => { for (const dt of [0, .26]){ const o = AC.createOscillator(); o.type = 'square'; o.frequency.setValueAtTime(470, t + dt); o.frequency.linearRampToValueAtTime(440, t + dt + .18); const bp = AC.createBiquadFilter(); bp.type = 'bandpass'; bp.frequency.value = 1150; bp.Q.value = 3; const g = AC.createGain(); g.gain.setValueAtTime(.0001, t + dt); g.gain.linearRampToValueAtTime(.26, t + dt + .02); g.gain.exponentialRampToValueAtTime(.0001, t + dt + .2); o.connect(bp).connect(g).connect(d); o.start(t + dt); o.stop(t + dt + .25); } AMBS.cheo(t + .7, d); },   /* kèn bóp ghe hàng */
  gheDi: (t, d) => { AMBS.cheo(t, d); AMBS.cheo(t + .9, d); },
  chime: (t, d) => { [2637, 3136, 3520, 4186, 3520].forEach((f, i) => tone(t + i * .09, .9, f, null, .03, d, 'sine', .005)); [7, 6, 5, 4, 3].forEach((i, j) => pluck(NGU[i], t + .5 + j * .05, .22, .995)); },   /* cây cổ tích hiện ra */
  chiep: (t, d) => { for (let i = 0; i < 5; i++) tone(t + i * .12 + Math.random() * .03, .07, 3800, 4500, .06, d); },   /* gà vịt con */
  gift: (t, d) => { for (let i = 0; i < 6; i++) nzz(t + i * .05, .04, 3200 + Math.random() * 1500, 2, .08, d); songlang(t + .35, .4); },   /* mở túi quà */
  confetti: (t, d) => { for (let i = 0; i < 5; i++) nzz(t + i * .07 + Math.random() * .03, .05, 2400 + Math.random() * 900, 1.5, .1, d); },   /* pháo giấy lên cấp */
  bite: (t, d) => AMBS.tom(t, d),   /* phao bị giật */
  water: (t, d) => nzz(t, .5, 1900, 1, .1, d, 1200),   /* tưới: nước rót */
  rustle: (t, d) => nzz(t, .25, 3400, .8, .08, d),   /* rơm xào xạc */
  hoe: (t, d) => { nzz(t, .12, 420, 1.2, .16, d); tone(t, .08, 320, 230, .05, d); },   /* cuốc thụp nhẹ */
  scatter: (t, d) => { for (let i = 0; i < 9; i++) nzz(t + Math.random() * .35, .015, 5200, 4, .06, d); },   /* rải thóc */
  clunk: (t, d) => { tone(t, .28, 880, 820, .08, d, 'triangle', .004); nzz(t, .06, 1100, 4, .06, d); } };   /* sành cốp */
function aud(k){ if (ST.snd === false) return; try { AC = AC || new (window.AudioContext || window.webkitAudioContext)(); if (AC.state === 'suspended') AC.resume(); const f = AUDF[k]; if (f) f(AC.currentTime + .01, out()); } catch (e) {} }
function bedOn(){ if (BED || !AC) return; const B = bus(); const mk = (type, f, q) => { const s = AC.createBufferSource(); s.buffer = noiseBuf(); s.loop = true; const bp = AC.createBiquadFilter(); bp.type = type; bp.frequency.value = f; bp.Q.value = q; const g = AC.createGain(); g.gain.value = 0; s.connect(bp).connect(g).connect(B.amb.in); s.start(); return { bp, g }; }; BED = { wind: mk('bandpass', 650, .7), water: mk('bandpass', 2500, 1.3), leaf: mk('highpass', 5200, .7) }; }
const ANX = {}; let MUSN = 0, MUSI = 3;
function ambTick(){ try { if (!AC || ST.snd === false || document.hidden || AC.state !== 'running') return; } catch (e) { return; } bedOn(); const B = bus(), t = AC.currentTime, h = HOUR, now = performance.now() / 1000, c = ctl.target;
  const dW = Math.min(...DITCH.map(([u0, v0, u1, v1]) => Math.hypot(Math.max(u0 - c.x, 0, c.x - u1), Math.max(v0 - c.z, 0, c.z - v1))), Math.max(0, R0 - c.z)), wv = Math.max(0, 1 - dW / 4), gu = Math.min(1, Math.max(0, typeof GUST === 'number' ? GUST : 0));
  if (!(ANX.gust > now)){ const g0 = AC.currentTime, pk = .035 + Math.random() * .045, up = 1.2 + Math.random() * 1.5, hold = .6 + Math.random() * 1.5, dn = 2 + Math.random() * 2.5; BED.wind.g.gain.cancelScheduledValues(g0); BED.wind.g.gain.setTargetAtTime(pk, g0, up / 3); BED.wind.g.gain.setTargetAtTime(.004, g0 + up + hold, dn / 3); BED.wind.bp.frequency.setTargetAtTime(520 + Math.random() * 380, g0, 1); BED.leaf.g.gain.setTargetAtTime(pk * .35, g0 + .3, up / 3); BED.leaf.g.gain.setTargetAtTime(.002, g0 + up + hold, dn / 3); ANX.gust = now + up + hold + dn + 6 + Math.random() * 16; }   /* gió từng cơn, lặng giữa các cơn */ BED.water.g.gain.setTargetAtTime((.012 + .045 * wv) * (.75 + .25 * Math.sin(now * 1.7) * Math.sin(now * .63)), t, .3);
  const every = (k, a, b, cond, fn) => { if (!cond) return; if (ANX[k] == null) ANX[k] = now + a + Math.random() * (b - a); if (now >= ANX[k]){ ANX[k] = now + a + Math.random() * (b - a); fn(); } }, D = B.amb.in, morn = h >= 5 && h < 10, aft = h >= 15 && h < 18.3, noon = h >= 10.5 && h < 15, night = h >= 19 || h < 4.8;
  every('chim', 3, 9, morn || aft || (h >= 10 && h < 15 && Math.random() < .3), () => AMBS[['chich', 'chaomao', 'sao', 'chich'][Math.random() * 4 | 0]](t, D));
  every('ve', 6, 14, noon, () => AMBS.ve(t, D)); every('de', .7, 1.6, night, () => AMBS.de(t, D)); every('ech', 2, 6, night && wv > .15, () => AMBS[Math.random() < .6 ? 'ech' : 'nhai'](t, D));
  every('ga', 40, 90, h >= 4.8 && h < 7.5, () => AMBS.ga(t, D)); every('cheo', 30, 70, aft || morn, () => AMBS.cheo(t, D));
  every('tom', 8, 20, wv > .3, () => { AMBS.tom(t, D); try { const dd = DITCH[Math.random() * DITCH.length | 0], x = dd[0] + Math.random() * (dd[2] - dd[0]), z = (dd[1] + dd[3]) / 2; for (let i = 0; i < 6; i++) puff('drop', x, WLD + .02, z, 1, '#cfe6ee', .35); } catch (e) {} });
  try { if (ST.bep && ST.bep.lit && Math.hypot(c.x - BEPW.x, c.z - BEPW.z) < 4) every('lua', .15, .5, true, () => nzz(t, .02, 2600 + Math.random() * 2000, 3, .04, D)); } catch (e) {}   /* lửa bếp tí tách khi nhìn gần */
  if (VOL().mus > 0 && now >= MUSN){ MUSN = now + 7 + Math.random() * 7; const M = B.mus.in, n = 3 + (Math.random() * 3 | 0), slow = night || aft ? 1.5 : 1; for (let i = 0; i < n; i++){ MUSI = Math.max(0, Math.min(7, MUSI + [-2, -1, 1, 2][Math.random() * 4 | 0])); pluck(NGU[MUSI] / (night ? 2 : 1), t + .2 + i * .42 * slow, .2, .996, i === n - 1 && Math.random() < .5 ? .045 : 0, M); } } }   /* nhạc đàn tranh thưa, tối thì trầm chậm */
setInterval(ambTick, 250);
document.addEventListener('visibilitychange', () => { try { if (!AC) return; if (document.hidden) AC.suspend(); else if (ST.snd !== false) AC.resume(); } catch (e) {} });
{ let first = true; addEventListener('pointerdown', () => { if (!first) return; first = false; try { if (ST.snd === false) return; AC = AC || new (window.AudioContext || window.webkitAudioContext)(); AC.resume(); bus(); const t = AC.currentTime + .1; [[2, 0], [4, .14], [3, .28], [5, .44], [7, .62]].forEach(([i, dt]) => pluck(NGU[i], t + dt, .3, .995, 0, bus().mus.in)); if (HOUR >= 4.8 && HOUR < 9) AMBS.ga(t + .9, bus().amb.in); } catch (e) {} }, { capture: true }); }   /* vào vườn: đàn tranh chào, sáng sớm có gà gáy */
addEventListener('input', e => { const el = e.target.closest && e.target.closest('[data-vol]'); if (!el) return; try { ST.vol = Object.assign(VOL(), { [el.dataset.vol]: +el.value }); busVol(); save(); } catch (er) {} });""")
rep("s.connect(g).connect(out()); s.start(t0); s.stop(t0 + 1.1); }", "s.connect(g).connect(arguments[5] || out()); s.start(t0); s.stop(t0 + 1.1); }")
# ---------- móc tiếng vào sự kiện, thao tác ----------
rep("water(id){ const p = ST.plots[id]; stepMark('water1');", "water(id){ const p = ST.plots[id]; stepMark('water1'); aud('water');")
rep("p.mulch = ST.gt + MULCH_DUR; avGo(id);", "p.mulch = ST.gt + MULCH_DUR; aud('rustle'); avGo(id);")
rep("L.w++; gainXP(1);", "L.w++; aud('hoe'); gainXP(1);")
rep("function lvCelebrate(n){", "function lvCelebrate(n){ setTimeout(() => aud('confetti'), 250);")
rep("if (F.st === 0 && !F.said){ F.said = 1; save();", "if (F.st === 0 && !F.said){ F.said = 1; save(); setTimeout(() => aud('chime'), 1400);")
rep("ST.tasks.gr = 1;", "ST.tasks.gr = 1; aud('gift');")
rep("FM.ph = 'bite'", "FM.ph = 'bite'; aud('bite')")
rep("g.hatched = (g.hatched || 0) + 1;", "g.hatched = (g.hatched || 0) + 1; aud('chiep');")
rep("v.trough = Math.min(cap, v.", "aud('scatter'); v.trough = Math.min(cap, v.")
rep("K.jars[i] = { k, t: fast ? 30 : d.t", "aud('clunk'); K.jars[i] = { k, t: fast ? 30 : d.t")
rep(" if (!ST.ghe.o.seen){ ST.ghe.o.seen = Date.now(); save(); }", " if (!ST.ghe.o.seen){ ST.ghe.o.seen = Date.now(); save(); aud('ghe'); }")
rep("toast('Ghe bẹo nhận đủ hàng, nhổ sào đi rồi. Mai lại ghé.');", "toast('Ghe bẹo nhận đủ hàng, nhổ sào đi rồi. Mai lại ghé.'); setTimeout(() => aud('gheDi'), 600);")
# ---------- Cài đặt: 3 thanh âm lượng ----------
rep("if (kind === 'set'){ shT.textContent = 'Cài đặt';",
    "if (kind === 'set'){ shT.textContent = 'Cài đặt'; { const v = VOL(); h += `<div class=\"sub\">Âm lượng</div><div class=\"vols\">${[['mus', 'Nhạc đàn'], ['amb', 'Tiếng vườn'], ['sfx', 'Hiệu ứng']].map(([k, n]) => `<label class=\"volr\"><span>${n}</span><input type=\"range\" min=\"0\" max=\"1\" step=\".05\" value=\"${v[k]}\" data-vol=\"${k}\" aria-label=\"${n}\"></label>`).join('')}</div>`; }")
i = s.rindex('</style>'); s = s[:i] + "\n.vols{display:grid;gap:6px;margin:4px 0 10px}.volr{display:grid;grid-template-columns:96px 1fr;align-items:center;gap:10px;font:400 14px var(--f-game);color:#6B4529}.volr input{width:100%;accent-color:#86B06A}\n" + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
