const { chromium } = require('playwright');
(async () => { const br = await chromium.launch({ args: ['--use-gl=swiftshader', '--enable-webgl', '--ignore-gpu-blocklist'] });
  const p = await br.newPage({ viewport: { width: 760, height: 430 } }); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('http://127.0.0.1:8777/mv2_d115d.html'); await p.waitForFunction('window.__ready', null, { timeout: 180000 });
  const u = await p.evaluate(() => [window.__DUMP.ICON.cuc, window.__DUMP.ICON.maichau]);
  const q = await br.newPage({ viewport: { width: 760, height: 430 } });
  await q.setContent(`<body style="margin:0;background:#FFF8EA;font:700 16px sans-serif;color:#4A2F1E"><div style="display:flex;gap:14px;padding:14px;align-items:flex-end"><img src="${u[0]}" width=320><img src="${u[1]}" width=320></div><div style="display:flex;gap:14px;padding:0 14px;align-items:center"><span style="background:#F3E6C8;border-radius:12px;padding:6px"><img src="${u[0]}" width=52></span><span style="background:#F3E6C8;border-radius:12px;padding:6px"><img src="${u[1]}" width=52></span> cỡ trong bảng</div></body>`);
  await q.waitForTimeout(300); await q.screenshot({ path: '../hud16/chau_ic.png' }); console.log('lỗi', errs.length, errs.slice(0, 3));
  await br.close(); })();
