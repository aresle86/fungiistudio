const { chromium } = require('playwright');
(async () => { const b = await chromium.launch({ args: ['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist'] });
 for (const f of ['mv2_t115f.html','mv2_t115g.html']){ const c = await b.newContext({ viewport: { width: 390, height: 844 }, deviceScaleFactor: 2 }); const p = await c.newPage(); const errs=[]; p.on('pageerror',e=>errs.push(e.message)); p.setDefaultTimeout(180000); await p.route(u => !u.href.startsWith('http://127.0.0.1'), r => r.abort()); await p.addInitScript(() => { localStorage.setItem('mv2-state', JSON.stringify({ v: 1, eco: 2, split: 1, qv2: 1, exp: 1, k102: 1, seen: { hello: 1, sap1: 1 }, player: { av: 1, name: 'Q', garden: 'Q' }, spd: 1, lv: 20, xp: 9000, xu: 500, inv: {}, gb: {}, seeds: {}, plots: {}, qd: {}, land: {}, dc: {}, tm:'fixed', ovr:20.5, realTime:false, real:Date.now() })); }); await p.goto('http://127.0.0.1:8777/' + f); await p.waitForFunction('window.__ready'); await p.waitForTimeout(3000); const tag=f.includes('115f')?'f':'g';
  await p.evaluate(()=>{ for(const e of document.querySelectorAll('.sheet,.modal,#ddp,#dd')) if(e.id!=='load') e.hidden=true; }); await p.mouse.click(195,600); await p.waitForTimeout(600);
  await p.screenshot({path:`/tmp/pin_${tag}_dem.png`});
  await p.mouse.move(195,500); for(let i=0;i<14;i++){ await p.mouse.wheel(0,600); await p.waitForTimeout(90);} await p.waitForTimeout(1500);
  await p.screenshot({path:`/tmp/pin_${tag}_xa.png`});
  console.log(tag,errs, await p.evaluate(()=>({dot:(window.__BUBALL||[]).filter(g=>g.userData.dot).length,hr:document.querySelector('#clock,.clk')?.textContent}))); await c.close(); }
 await b.close(); })().catch(e=>{console.log('CRASH',e.message.slice(0,400));process.exit(1)});
