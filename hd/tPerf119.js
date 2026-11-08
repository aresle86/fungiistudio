// tPerf119: đo độ nặng khi vẽ với vườn cuối game (cấp 20, liếp trồng đầy, cây trái, gà vịt), trên chip đồ họa thật của máy (Metal).
// In: số hình mỗi giây khi để yên, số lần tính bóng mỗi giây, số lần vẽ mỗi hình, số tam giác, và nhóm vật tốn nhiều lần vẽ nhất.
// node tPerf119.js [trang] [mức đồ họa 0|1|2]
const { chromium } = require('playwright');
const PAGE = process.argv[2] || 'mv2_t118a.html', Q = process.argv[3] || '1';
const today = (d => d.getFullYear() + '-' + (d.getMonth() + 1) + '-' + d.getDate())(new Date());
const own = Object.fromEntries([...Array.from({ length: 12 }, (_, i) => 'H' + (i + 1)), ...Array.from({ length: 8 }, (_, i) => 'S' + (i + 1)), ...Array.from({ length: 10 }, (_, i) => 'N' + (i + 1))].map(k => [k, { st: 'own' }]));
const SV = { v: 1, eco: 2, split: 1, qv2: 1, exp: 1, k102: 1, seen: { hello: 1, sap1: 1 }, player: { av: 1, name: 'Q', garden: 'Q' }, spd: 1, lv: 20, xp: 26600, xu: 90000, inv: {}, gb: {}, seeds: {}, plots: {}, qd: Object.fromEntries(Array.from({ length: 18 }, (_, i) => [i + 3, 1])), land: own, open: [], dc: {}, realTime: true, real: Date.now(), dd: { last: today, n: 3, full: 0 }, ftrD: today };
(async () => { const b = await chromium.launch({ args: ['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist'] }); const c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 3, hasTouch: true, isMobile: true }); const p = await c.newPage(); p.setDefaultTimeout(600000); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.route(u => !u.href.startsWith('http://127.0.0.1'), r => r.abort()); await p.addInitScript(([s, q]) => { try { localStorage.setItem('mv3d-q', q); localStorage.setItem('mv2-state', s); } catch (e) {} }, [JSON.stringify(SV), Q]);
  await p.goto('http://127.0.0.1:8777/' + PAGE); await p.waitForFunction('window.__ready', null, { timeout: 600000 }); await p.waitForTimeout(3000);
  // trồng đầy: rau ở liếp, khổ qua ở giàn, cây trái ở các gốc và ô đất trống; cho lớn tới có trái
  const planted = await p.evaluate(() => { const G = window.__g, ST = G.ST, N = window.__N, out = []; const veg = ['cai', 'hanh', 'ot', 'bap', 'cachua', 'raumuong', 'mongtoi', 'daubap', 'khom', 'mia', 'daurong'], tr = ['dudu', 'mangcau', 'sung', 'buoi', 'vusualr', 'xoai', 'oi'];
    let vi = 0, ti = 0; for (const P of N.PLOTS){ try { if (P.tree){ ST.plots[P.id] = { ...(ST.plots[P.id] || {}), crop: P.tree, g: 9e9, dry: 0 }; } else if (P.trellis){ ST.plots[P.id] = { ...(ST.plots[P.id] || {}), crop: 'khoqua', g: 9e9, dry: 0 }; } else if (!P.bai || ST.land && ST.land[P.id]){ const k = veg[vi++ % veg.length]; ST.plots[P.id] = { ...(ST.plots[P.id] || {}), crop: k, g: N.CROPS[k].grow * .99, dry: 0 }; } else continue; G.refreshPlot(P.id); out.push(P.id); } catch (e) {} }
    return out.length; });
  await p.waitForTimeout(4000); await p.evaluate(() => { document.querySelectorAll('.ddt,.lvup,#intro,.sheet').forEach(e => e.hidden = true); });
  await p.waitForTimeout(3000);
  const R = await p.evaluate(async () => { const r = window.__r; let frames = 0, calls = 0, tris = 0, shadow = 0; const o = r.render.bind(r); r.render = (a, bb) => { if (r.shadowMap.needsUpdate || r.shadowMap.autoUpdate) shadow++; frames++; const x = o(a, bb); calls += r.info.render.calls; tris += r.info.render.triangles; return x; };
    const t0 = performance.now(); await new Promise(z => setTimeout(z, 8000)); const s = (performance.now() - t0) / 1000; r.render = o;
    // nhóm vật: đếm mesh đang hiện theo tên nhóm con cấp 1 của cảnh
    const sc = window.__N.S;
    const grp = {}; if (sc) sc.traverse(m => { if (!m.isMesh || !m.visible) return; let q = m, top = m; while (q.parent && q.parent !== sc){ q = q.parent; } top = q; const nm = (top.name || top.userData.k || top.type) + ''; grp[nm] = grp[nm] || [0, 0]; grp[nm][0]++; grp[nm][1] += m.castShadow ? 1 : 0; });
    const topG = Object.entries(grp).sort((a, b2) => b2[1][0] - a[1][0]).slice(0, 12);
    return { pr: r.getPixelRatio(), shadowMap: r.shadowMap.enabled ? (window.__g && 0, 'bật') : 'tắt', hinhGiay: +(frames / s).toFixed(1), bongGiay: +(shadow / s).toFixed(1), veMoiHinh: Math.round(calls / Math.max(1, frames)), tamGiac: Math.round(tris / Math.max(1, frames)), meshHien: Object.values(grp).reduce((a, x) => a + x[0], 0), nhom: topG }; });
  console.log(PAGE, 'mức', Q, 'trồng', planted, 'ô'); console.log(JSON.stringify(R)); console.log('lỗi', errs.slice(0, 3)); await b.close(); })().catch(e => { console.log('CRASH', e.message.slice(0, 300)); process.exit(1); });
