// tIdle119: chống nóng máy trên điện thoại (chip đồ họa thật). Để yên: ~30 hình/giây, quá 8 giây ~20, quá 1 phút ~12; bóng đổ ≤ 8 lần/giây ở mọi mức;
// chạm vào thì vẽ mượt lại; trồng cây thì bóng tính lại ngay. node tIdle119.js [trang]
const { chromium } = require('playwright'); const PAGE = process.argv[2] || 'mv2_t119a.html'; let bad = 0; const ok = (c, m) => { console.log((c ? 'PASS ' : 'FAIL ') + m); if (!c) bad++; };
const today = (d => d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate())(new Date());
const SV = { v: 1, eco: 2, split: 1, qv2: 1, exp: 1, k102: 1, seen: { hello: 1, sap1: 1 }, player: { av: 1, name: 'Q', garden: 'Q' }, spd: 1, lv: 12, xp: 7600, xu: 9000, inv: {}, gb: {}, seeds: {}, plots: {}, qd: Object.fromEntries(Array.from({ length: 10 }, (_, i) => [i + 3, 1])), realTime: true, real: Date.now(), dd: { last: today, n: 3, full: 0 }, ftrD: today };
(async () => { const b = await chromium.launch({ args: ['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist'] });
  for (const q of ['1', '2']){ const c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, hasTouch: true, isMobile: true }); const p = await c.newPage(); p.setDefaultTimeout(600000); const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.route(u => !u.href.startsWith('http://127.0.0.1'), r => r.abort()); await p.addInitScript(([s, qq]) => { localStorage.setItem('mv3d-q', qq); localStorage.setItem('mv2-state', s); }, [JSON.stringify(SV), q]);
    await p.goto('http://127.0.0.1:8777/' + PAGE); await p.waitForFunction('window.__ready', null, { timeout: 600000 });
    await p.evaluate(() => { const r = window.__r, o = r.render.bind(r); window.__M = { f: 0, sh: 0 }; r.render = (a, b2) => { if (r.shadowMap.needsUpdate || r.shadowMap.autoUpdate) window.__M.sh++; window.__M.f++; return o(a, b2); }; });
    const win = async ms => { const a = await p.evaluate(() => ({ ...window.__M, t: performance.now() })); await p.waitForTimeout(ms); const z = await p.evaluate(() => ({ ...window.__M, t: performance.now() })); const s = (z.t - a.t) / 1000; return { fps: +((z.f - a.f) / s).toFixed(1), sh: +((z.sh - a.sh) / s).toFixed(1) }; };
    const pr = await p.evaluate(() => window.__r.getPixelRatio()); ok(q === '2' ? pr === 1.75 : pr === 1.5, `mức ${q}: độ nét ${pr}`);
    await p.mouse.click(200, 400); await p.waitForTimeout(2500); const a = await win(4000); ok(a.fps >= 25 && a.fps <= 35 && a.sh <= 8, `mức ${q}: để yên vài giây ~30 hình/giây, bóng ≤ 8: ${JSON.stringify(a)}`);
    await p.waitForTimeout(3000); const bb = await win(5000); ok(bb.fps >= 16 && bb.fps <= 24 && bb.sh <= 8, `mức ${q}: để yên quá 8 giây ~20 hình/giây: ${JSON.stringify(bb)}`);
    await p.mouse.move(150, 300); await p.mouse.down(); const drag = (async () => { for (let i = 0; i < 30; i++){ await p.mouse.move(150 + i * 4, 300 + i * 2); await p.waitForTimeout(50); } })(); await p.waitForTimeout(300);   /* đo trong lúc đang kéo */
    const d = await win(1000); await drag; await p.mouse.up(); ok(d.fps >= 40, `mức ${q}: vừa chạm kéo thì vẽ mượt lại: ${JSON.stringify(d)}`);
    const plant = await p.evaluate(async () => { const G = window.__g, ST = G.ST; window.__r.shadowMap.needsUpdate = false; ST.plots.A1 = { ...(ST.plots.A1 || {}), crop: 'cai', g: 0, dry: 0 }; G.refreshPlot('A1'); const s0 = window.__M.sh; await new Promise(z => setTimeout(z, 120)); return window.__M.sh - s0; }); ok(plant >= 1, `mức ${q}: trồng thì bóng tính lại ngay (${plant} lần trong 120 ms)`);
    if (q === '1'){ await p.waitForTimeout(62000); const e = await win(5000); ok(e.fps >= 9 && e.fps <= 15, `để yên quá 1 phút ~12 hình/giây: ${JSON.stringify(e)}`); }
    ok(errs.length === 0, `mức ${q}: không lỗi ${errs[0] || ''}`); await c.close(); }
  await b.close(); console.log('DONE', bad ? bad + ' FAIL' : 'all pass'); })().catch(e => { console.log('CRASH', e.message.slice(0, 300)); process.exit(1); });
