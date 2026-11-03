// QC: đi cấp 1→20, mỗi cấp mở mọi bảng, Sổ, Chợ; bắt lỗi console + chữ hỏng; đo hiệu năng.
const fs = require('fs'); const {chromium} = require('playwright');
const OUT = process.argv[2] || '../qcLv.json'; const PAGE = process.argv[3] || 'mv2_test.html';
(async () => {
  const b = await chromium.launch({args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist']});
  const p = await b.newPage({viewport: {width: 1200, height: 800}});
  const errs = []; p.on('pageerror', e => errs.push('PAGEERR ' + e.message + ' @' + ((e.stack || '').split('\n')[1] || '').trim()));
  p.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') errs.push('CONSOLE.' + m.type() + ' ' + m.text().slice(0, 200)); });
  await p.addInitScript(() => { try { localStorage.clear(); localStorage.setItem('mv3d-q', '1'); } catch (e) {} });
  await p.goto('http://127.0.0.1:8777/' + PAGE, {waitUntil: 'domcontentloaded'});
  await p.waitForFunction(() => window.__ready, null, {timeout: 300000});
  const res = await p.evaluate(async () => {
    window.__stop = true;
    const g = window.__g, w = window.__w, ST = g.ST, out = {levels: [], bad: []};
    const hide = () => { document.querySelectorAll('#intro,#lvup,.lvup').forEach(e => e.hidden = true); window.LVON = false; document.body.classList.remove('lvon'); };
    hide(); ST.player = {av: 1, name: 'Na', garden: 'Vườn Na'};
    const XPN = [0, 0, 10, 30, 80, 190, 310, 450, 610, 840, 1060, 1320, 1620, 1960, 2340, 2760, 3220, 3720, 4260, 4840, 5460];
    const SHEETS = [['cho'], ['plot', 'A1'], ['ga'], ['vit'], ['bep'], ['nong'], ['lo'], ['khap'], ['ho'], ['gio'], ['deco'], ['ben'], ['set'], ['say']];
    const BOOK = ['giong', 'kho', 'viec', 'ca', 'cotich', 'buom'];
    const scan = (where, el) => { const t = (el && el.innerText) || ''; const m = t.match(/.{0,40}(undefined|NaN|\[object Object\]|null xu|Infinity).{0,40}/); if (m) out.bad.push(where + ' :: ' + m[0].replace(/\s+/g, ' ')); };
    const tick = n => { for (let i = 0; i < n; i++) { try { window.__tick(performance.now() + i * 16); } catch (e) { out.bad.push('TICK ' + e.message); break; } } };
    for (let n = 1; n <= 20; n++) {
      const L = {lv: n, err: []};
      try {
        if (n > 1) { ST.xp = XPN[n]; w.levelUp(n); }
        ST.xu = 5000; hide(); w.hud(); try { w.nxq(); } catch (e) { L.err.push('nxq ' + e.message); }
        scan('lv' + n + ' nxq', document.getElementById('nxq'));
        tick(3);
        for (const [k, a] of SHEETS) {
          try { g.openSheet(k, a); tick(2); scan('lv' + n + ' sheet ' + k, document.getElementById('sheet'));
            if (k === 'cho') for (const t of ['don', 'ban', 'mua', 'tt']) { const bt = document.querySelector(`[data-a="ctab"][data-k="${t}"]`); if (bt) { bt.click(); tick(1); scan('lv' + n + ' cho/' + t, document.getElementById('sheet')); } }
            g.closeSheet();
          } catch (e) { L.err.push('sheet ' + k + ': ' + e.message); try { g.closeSheet(); } catch (_) {} }
        }
        for (const t of BOOK) {
          try { w.openBook(t); tick(1); const bk = document.getElementById('book'); scan('lv' + n + ' book ' + t, bk);
            // bấm thử từng mục trong tab (giống, cá, cổ tích…)
            const items = [...bk.querySelectorAll('[data-sel],[data-k]')].slice(0, 30);
            for (const it of items) { try { it.click(); tick(1); scan('lv' + n + ' book ' + t + ' item ' + (it.dataset.sel || it.dataset.k), bk); } catch (e) { L.err.push('book ' + t + ' item ' + (it.dataset.sel || it.dataset.k) + ': ' + e.message); } }
            w.closeBook();
          } catch (e) { L.err.push('book ' + t + ': ' + e.message); try { w.closeBook(); } catch (_) {} }
        }
      } catch (e) { L.err.push('LEVEL ' + e.message); }
      L.tabs = [...document.querySelectorAll('#book [data-a="btab"],#book .btab')].map(x => x.innerText.trim()).join('|');
      out.levels.push(L);
    }
    // hiệu năng ở cấp 20 (trạng thái mặc định sau khi đi cấp)
    const r = window.__r; tick(30);
    let nodes = 0, meshes = 0, lights = 0; window.__g.T && 0;
    const scene = (() => { let o = window.__g.cam; while (o && o.parent) o = o.parent; return o; })();
    const root = r.info ? null : null;
    const t0 = performance.now(); tick(60); const ft = (performance.now() - t0) / 60;
    out.perf = {calls: r.info.render.calls, tris: r.info.render.triangles, geos: r.info.memory.geometries, tex: r.info.memory.textures, progs: (r.info.programs || []).length, msPerTickSwiftshader: +ft.toFixed(1), pr: r.getPixelRatio(), shadow: r.shadowMap.enabled, shadowType: r.shadowMap.type};
    return out;
  });
  // đếm node scene riêng
  res.errs = errs; fs.writeFileSync(OUT, JSON.stringify(res, null, 1)); console.log('DONE', res.levels.filter(l => l.err.length).length, 'levels with err;', res.bad.length, 'bad text;', errs.length, 'console errs'); console.log(JSON.stringify(res.perf));
  await b.close();
})();
