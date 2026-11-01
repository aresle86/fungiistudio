// QC: tái hiện các lỗi nghi ngờ từ review code. Mỗi mục in PASS/FAIL + bằng chứng.
const fs = require('fs'); const {chromium} = require('playwright');
const PAGE = process.argv[2] || 'mv2_test.html';
(async () => {
  const b = await chromium.launch({args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist']});
  const p = await b.newPage({viewport: {width: 1200, height: 800}});
  const errs = []; p.on('pageerror', e => errs.push(e.message + ' @' + ((e.stack || '').split('\n')[1] || '').trim()));
  await p.addInitScript(() => { try { localStorage.clear(); localStorage.setItem('mv3d-q', '1'); } catch (e) {} });
  await p.goto('http://127.0.0.1:8777/' + PAGE, {waitUntil: 'domcontentloaded'});
  await p.waitForFunction(() => window.__ready, null, {timeout: 300000});
  const R = await p.evaluate(async () => {
    window.__stop = true;
    const g = window.__g, w = window.__w, ST = g.ST, out = {};
    const hide = () => { document.querySelectorAll('#intro,#lvup,.lvup').forEach(e => e.hidden = true); window.LVON = false; document.body.classList.remove('lvon'); };
    const tick = (n, dt = 16) => { let t = performance.now(); for (let i = 0; i < n; i++) { t += dt; window.__tick(t); } };
    hide(); ST.player = {av: 1, name: 'Na', garden: 'V'};
    const XPN = [0, 0, 10, 30, 80, 190, 310, 450, 610, 840, 1060, 1320, 1620, 1960, 2340, 2760, 3220, 3720, 4260, 4840, 5460];
    ST.xp = XPN[14]; w.levelUp(14); hide();

    // 1. Cây cổ tích lớn theo giờ thật? Đặt vú sữa st=1, t = 60 s trước, chạy ftTick.
    try { const F2 = window.__FT2; ST.ft = ST.ft || {}; ST.ft.vusua = {st: 1, told: 0, t: Date.now() - 60 * 1000};
      F2.ftTick && F2.ftTick(0.016); tick(5);
      out.fairyGrowth = {stAfter60s: ST.ft.vusua.st, expect: 'st vẫn 1 (cần 6 tiếng)'}; } catch (e) { out.fairyGrowth = 'ERR ' + e.message; }

    // 2. Hạt giống quý (dưa hấu ruột vàng, cúc) trong Sổ › Giống
    try { ST.inv.duahau = 2; ST.inv.cuc = 2; w.openBook('giong'); let e1 = null;
      for (const k of ['duahau', 'cuc']) { try { window.__OB('giong', k); } catch (e) { e1 = (e1 || '') + k + ': ' + e.message + '; '; } }
      out.rareSeedBook = {err: e1, text: document.getElementById('book').innerText.replace(/\s+/g, ' ').slice(0, 160)}; w.closeBook(); } catch (e) { out.rareSeedBook = 'ERR ' + e.message; }

    // 3. Bảng liếp: mở mục "Khác" rồi để tick chạy 1 s — còn mở không?
    try { g.openSheet('plot', 'A1'); tick(2); const d = document.querySelector('#sheet details'); if (!d) out.plotDetails = 'không có <details>';
      else { d.open = true; tick(70); const d2 = document.querySelector('#sheet details'); out.plotDetails = {stillOpen: !!(d2 && d2.open), sameNode: d === d2}; }
      g.closeSheet(); } catch (e) { out.plotDetails = 'ERR ' + e.message; }

    // 4. Bướm: chạm bướm 2 lần có ghi sổ 2 lần không
    try { const BU = window.__BU; ST.lv = 14; for (let i = 0; i < 400 && !(BU.BUV.list || BU.BUV.L || []).length; i++) tick(1, 50);
      const list = BU.BUV.list || BU.BUV.L || BU.BUV.bs || Object.values(BU.BUV).find(Array.isArray) || [];
      if (!list.length) out.butterfly = 'không có bướm sinh ra (keys: ' + Object.keys(BU.BUV).join(',') + ')';
      else { const bf = list[0]; const before = JSON.stringify(ST.buom || {}); BU.buCatch(bf); const mid = JSON.stringify(ST.buom || {}); try { BU.buCatch(bf); } catch (e) {} const after = JSON.stringify(ST.buom || {}); tick(200, 50); out.butterfly = {before, mid, after, stillInList: list.includes(bf), y: bf.m && +bf.m.position.y.toFixed(2)}; }
    } catch (e) { out.butterfly = 'ERR ' + e.message; }

    // 5. Tên vườn chứa HTML khi ghé vườn (giả lập VISIT.name) — kiểm hàm esc có tồn tại và ô hiển thị có thoát ký tự không
    try { const src = document.documentElement.outerHTML; out.xssVisitName = /innerHTML = `<div><b>\$\{VISIT\.name\}/.test(src) ? 'tên vườn chèn thẳng vào innerHTML (chưa esc)' : 'ok/không tìm thấy mẫu'; } catch (e) { out.xssVisitName = 'ERR ' + e.message; }

    // 6. Bảng gà khi chỉ 1 mái đang ấp
    try { ST.ga.hens = 1; ST.ga.brood = {stage: 'egg', t: 100}; g.openSheet('ga'); tick(2); const t = document.getElementById('sheet').innerText.replace(/\s+/g, ' '); out.gaNext = (t.match(/.{0,30}(0 giây|chừng 0).{0,30}/) || ['ok'])[0]; g.closeSheet(); } catch (e) { out.gaNext = 'ERR ' + e.message; }

    // 7. Tua vắng 7 ngày: frame đầu mất bao lâu
    try { ST.real = Date.now() - 7 * 86400e3; const t0 = performance.now(); tick(1); out.awayCatchupMs = +(performance.now() - t0).toFixed(0); } catch (e) { out.awayCatchupMs = 'ERR ' + e.message; }

    // 8. Số node trong scene + PointLight
    try { let s = g.cam; while (s.parent) s = s.parent; let n = 0, emptyG = 0, pl = 0, mesh = 0; s.traverse(o => { n++; if (o.isPointLight) pl++; if (o.isMesh) mesh++; if (o.type === 'Group' && !o.children.length) emptyG++; }); out.scene = {nodes: n, meshes: mesh, emptyGroups: emptyG, pointLights: pl}; } catch (e) { out.scene = 'ERR ' + e.message; }

    // 9. Save size (keepalive 64KB)
    try { out.saveBytes = JSON.stringify(ST).length; } catch (e) { out.saveBytes = 'ERR ' + e.message; }
    return out;
  });
  console.log(JSON.stringify(R, null, 1)); console.log('pageerrors', errs.slice(0, 8));
  await b.close();
})();
