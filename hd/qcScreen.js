// QC ma trận màn hình: mỗi kích cỡ mở mọi bảng/Sổ/Chợ ở cấp 13, kiểm tràn, nút bị che/cắt, cuộn ngang.
const fs = require('fs'); const {chromium} = require('playwright');
const PAGE = process.argv[2] || 'mv2_dev.html'; const SHOT = process.env.SHOT === '1';
const VPS = [[390, 844, 1], [375, 667, 1], [430, 932, 1], [844, 390, 1], [768, 1024, 0], [1280, 800, 0], [1920, 1080, 0]];
(async () => {
  const b = await chromium.launch({args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist']});
  const all = [];
  for (const [W, H, mob] of VPS) {
    const p = await b.newPage({viewport: {width: W, height: H}, isMobile: !!mob, hasTouch: !!mob, deviceScaleFactor: mob ? 2 : 1});
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.addInitScript(() => { try { localStorage.clear(); localStorage.setItem('mv3d-q', '0'); } catch (e) {} });
    await p.goto('http://127.0.0.1:8777/' + PAGE, {waitUntil: 'domcontentloaded'});
    await p.waitForFunction(() => window.__ready, null, {timeout: 300000});
    const R = await p.evaluate(async () => {
      window.__stop = true; const g = window.__g, w = window.__w, ST = g.ST, out = [];
      const hide = () => { document.querySelectorAll('#intro,#lvup,.lvup').forEach(e => e.hidden = true); window.LVON = false; document.body.classList.remove('lvon'); };
      hide(); ST.player = {av: 1, name: 'Nguyễn Thị Na', garden: 'Vườn Bà Năm Cái Răng'};
      const XPN = [0, 0, 10, 30, 80, 190, 310, 450, 610, 840, 1060, 1320, 1620, 1960];
      ST.xp = XPN[13]; w.levelUp(13); hide(); ST.xu = 4321; w.hud(); try { w.nxq(); } catch (e) {}
      const tick = n => { for (let i = 0; i < n; i++) window.__tick(); };
      const iw = innerWidth, ih = innerHeight;
      const check = (where) => {
        const pb = [];
        if (document.documentElement.scrollWidth > iw + 1) pb.push('cuộn ngang trang ' + document.documentElement.scrollWidth);
        for (const id of ['sheet', 'book']) { const el = document.getElementById(id); if (!el || el.hidden) continue; const r = el.getBoundingClientRect(); if (r.width < 2) continue;
          if (r.right > iw + 1 || r.left < -1) pb.push(`#${id} tràn ngang (${Math.round(r.left)}–${Math.round(r.right)} / ${iw})`);
          if (r.bottom > ih + 1 || r.top < -1) pb.push(`#${id} tràn dọc (${Math.round(r.top)}–${Math.round(r.bottom)} / ${ih})`);
          for (const sc of el.querySelectorAll('*')) { if (sc.scrollWidth > sc.clientWidth + 2 && getComputedStyle(sc).overflowX !== 'visible' && getComputedStyle(sc).overflowX !== 'auto' && getComputedStyle(sc).overflowX !== 'scroll' && sc.clientWidth > 0 && /hidden|clip/.test(getComputedStyle(sc).overflowX)) { pb.push(`chữ bị cắt: "${(sc.innerText || '').trim().slice(0, 30)}"`); if (pb.length > 12) break; } }
        }
        // nút nằm ngoài màn hình (chỉ nút đang hiển thị, không nằm trong vùng cuộn)
        for (const bt of document.querySelectorAll('button, .btn')) { const st = getComputedStyle(bt); if (st.display === 'none' || st.visibility === 'hidden' || bt.closest('[hidden]')) continue; const r = bt.getBoundingClientRect(); if (r.width < 4 || r.height < 4) continue;
          let sc = bt.parentElement, inScroll = false; while (sc && sc !== document.body) { const o = getComputedStyle(sc); if (/(auto|scroll)/.test(o.overflowY + o.overflowX)) { inScroll = true; break; } sc = sc.parentElement; }
          if (!inScroll && (r.right > iw + 2 || r.left < -2 || r.bottom > ih + 2 || r.top < -2)) pb.push(`nút ngoài màn: "${(bt.innerText || bt.getAttribute('aria-label') || bt.id).trim().slice(0, 24)}" (${Math.round(r.left)},${Math.round(r.top)})`);
          if (r.height < 30 && r.width < 30 && !bt.closest('#book .bkL')) pb.push(`nút nhỏ hơn 30px: "${(bt.innerText || bt.getAttribute('aria-label') || bt.className).trim().slice(0, 20)}" ${Math.round(r.width)}×${Math.round(r.height)}`);
        }
        // bảng che HUD/nút đóng
        const x = document.getElementById('shX'); if (x && !x.closest('[hidden]')) { const r = x.getBoundingClientRect(); if (r.width && (r.top < 0 || r.right > iw)) pb.push('nút đóng bảng ngoài màn'); }
        if (pb.length) out.push({where, pb: [...new Set(pb)].slice(0, 10)});
      };
      tick(3); check('màn chính');
      for (const [k, a] of [['cho'], ['plot', 'A1'], ['ga'], ['vit'], ['bep'], ['nong'], ['lo'], ['khap'], ['ho'], ['gio'], ['deco'], ['ben'], ['set'], ['say']]) {
        try { g.openSheet(k, a); tick(2); check('bảng ' + k);
          if (k === 'cho') for (const t of ['don', 'ban', 'mua', 'tt']) { const bt = document.querySelector(`[data-a="ctab"][data-k="${t}"]`); if (bt) { bt.click(); tick(1); check('chợ/' + t); } }
          g.closeSheet(); } catch (e) { out.push({where: 'bảng ' + k, pb: ['LỖI ' + e.message]}); }
      }
      for (const t of ['giong', 'kho', 'viec', 'ca', 'cotich', 'buom']) { try { w.openBook(t); tick(1); check('Sổ ' + t); w.closeBook(); } catch (e) { out.push({where: 'Sổ ' + t, pb: ['LỖI ' + e.message]}); } }
      try { window.__e.fmEnter(); tick(3); check('câu cá'); window.__e.fmExit(); } catch (e) { out.push({where: 'câu cá', pb: ['LỖI ' + e.message]}); }
      return out;
    });
    all.push({vp: `${W}×${H}`, issues: R, errs: errs.slice(0, 5)});
    console.log(`${W}×${H}: ${R.length} chỗ có vấn đề, ${errs.length} lỗi trang`);
    if (SHOT) { try { await p.evaluate(() => window.__g.openSheet('cho')); await p.screenshot({path: `../qcshot_${W}x${H}_cho.png`, timeout: 60000}); } catch (e) {} }
    await p.close();
  }
  fs.writeFileSync('../qcScreen.json', JSON.stringify(all, null, 1)); await b.close();
})();
