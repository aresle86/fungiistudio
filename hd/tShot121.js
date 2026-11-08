// tShot121: chụp vườn cuối game trên khung điện thoại, tầm nhìn mặc định và phóng to một liếp, cho hai trang để so trước/sau.
// node tShot121.js trangA trangB tiền_tố [mức đồ họa]
const { chromium } = require('playwright'); const [PA, PB, PRE, Q] = [process.argv[2], process.argv[3], process.argv[4] || '../hud16/s121', process.argv[5] || '1'];
const today = (d => d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate())(new Date());
const own = Object.fromEntries([...Array.from({ length: 12 }, (_, i) => 'H' + (i + 1)), ...Array.from({ length: 8 }, (_, i) => 'S' + (i + 1)), ...Array.from({ length: 10 }, (_, i) => 'N' + (i + 1))].map(k => [k, { st: 'own' }]));
const SV = { v: 1, eco: 2, split: 1, qv2: 1, exp: 1, k102: 1, seen: { hello: 1, sap1: 1 }, player: { av: 1, name: 'Q', garden: 'Q' }, spd: 1, lv: 20, xp: 26600, xu: 90000, inv: {}, gb: {}, seeds: {}, plots: {}, qd: Object.fromEntries(Array.from({ length: 18 }, (_, i) => [i + 3, 1])), land: own, open: [], dc: {}, tm: 'fixed', ovr: 10, realTime: false, real: Date.now(), dd: { last: today, n: 3, full: 0 }, ftrD: today };
(async () => { const b = await chromium.launch({ args: ['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist'] });
  for (const [pg, tag] of [[PA, 'a'], [PB, 'b']]){ const c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, hasTouch: true, isMobile: true }); const p = await c.newPage(); p.setDefaultTimeout(600000);
    await p.route(u => !u.href.startsWith('http://127.0.0.1'), r => r.abort()); await p.addInitScript(([s, q]) => { localStorage.setItem('mv3d-q', q); localStorage.setItem('mv2-state', s); }, [JSON.stringify(SV), Q]);
    await p.goto('http://127.0.0.1:8777/' + pg); await p.waitForFunction('window.__ready', null, { timeout: 600000 }); await p.waitForTimeout(2500);
    await p.evaluate(() => { const G = window.__g, ST = G.ST, N = window.__N; const veg = ['cai', 'hanh', 'ot', 'bap', 'cachua', 'raumuong', 'mongtoi', 'daubap', 'khom', 'mia', 'daurong'], fr = [.4, .7, .99, 1.2, 1.2]; let vi = 0;
      for (const P of N.PLOTS){ try { if (P.tree) ST.plots[P.id] = { ...(ST.plots[P.id] || {}), crop: P.tree, g: 9e9, dry: 0 }; else if (P.trellis) ST.plots[P.id] = { ...(ST.plots[P.id] || {}), crop: 'khoqua', g: 9e9, dry: 0 }; else if (!P.bai || ST.land && ST.land[P.id]){ const k = veg[vi % veg.length]; ST.plots[P.id] = { ...(ST.plots[P.id] || {}), crop: k, g: N.CROPS[k].grow * fr[vi % 5], dry: 0 }; vi++; } else continue; G.refreshPlot(P.id); } catch (e) {} } });
    await p.waitForTimeout(3000); await p.evaluate(() => { document.querySelectorAll('.ddt,.lvup,#intro,.sheet,#ngoai').forEach(e => e.style.visibility = 'hidden'); for (const g of (window.__BUBALL || [])) g.scale.setScalar(0.0001); });
    await p.waitForTimeout(1500); await p.screenshot({ path: `${PRE}_${tag}_full.png` });
    await p.screenshot({ path: `${PRE}_${tag}_zoom.png`, clip: { x: 95, y: 330, width: 260, height: 300 } }); await c.close(); }
  await b.close(); })().catch(e => { console.log('CRASH', e.message.slice(0, 300)); process.exit(1); });
