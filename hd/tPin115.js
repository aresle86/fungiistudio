const { chromium } = require('playwright'); const fs=require('fs');
(async () => { const b = await chromium.launch({ args: ['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist'] });
 for (const f of ['mv2_t115f.html','mv2_t115g.html']){ const c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2, hasTouch: true, isMobile: true }); const p = await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.setDefaultTimeout(180000); await p.route(u => !u.href.startsWith('http://127.0.0.1'), r => r.abort()); await p.addInitScript(() => { localStorage.setItem('mv2-state', JSON.stringify({ v: 1, eco: 2, split: 1, qv2: 1, exp: 1, k102: 1, seen: { hello: 1, sap1: 1 }, player: { av: 1, name: 'Q', garden: 'Q' }, spd: 1, lv: 20, xp: 9000, xu: 500, inv: {}, gb: {}, seeds: {}, plots: {}, qd: {}, land: {}, dc: {} })); }); await p.goto('http://127.0.0.1:8777/' + f); await p.waitForFunction('window.__ready'); await p.waitForTimeout(3000);
  const tag=f.includes('115f')?'f':'g'; const shot=async n=>{ await p.waitForTimeout(800); await p.screenshot({path:`/tmp/pin_${tag}_${n}.png`}); };
  await shot('ngay');
  await p.evaluate(()=>{const c=window.__ctl; c.target.set(.6,0,4.2); c.object.position.set(.6+2.2,3,4.2+3.2); c.update();}); await shot('ga');
  await p.evaluate(()=>{const c=window.__ctl; c.target.set(2.3,.3,2); c.object.position.set(2.3+.6,1,2+1.6); c.update();}); await shot('av');
  await p.evaluate(()=>{const c=window.__ctl; c.target.set(3.5,.4,4.6); c.object.position.set(3.5,3.5,4.6+3.2); c.update();}); await shot('ghim');
  await p.evaluate(()=>{const c=window.__ctl; c.target.set(-.3,.2,6.5); c.object.position.set(-.3+1.3,1.4,6.5+1.8); c.update();}); await shot('vit');
  await p.evaluate(()=>{const X=window.__DCX0.get(); (X.ST||X.S).ovr=20; const c=window.__ctl; c.target.set(3.5,.4,4.6); c.object.position.set(3.5,3.5,4.6+3.2); c.update();}); await p.waitForTimeout(1500); await shot('dem');
  console.log(tag,'lỗi',errs.length,errs.slice(0,2), await p.evaluate(()=>window.__r.info.render.calls)); await c.close(); }
 await b.close(); })().catch(e=>{console.log('CRASH',e.message.slice(0,300));process.exit(1)});
