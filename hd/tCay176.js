/* v176: cây cổ tích chặng 1. node tCay176.js <trang>   (cần máy chủ lp ở cổng 8777)
   Đo ba chuyện:
     A. một lúc chỉ một cây — đủ điều kiện cả sáu cây cũng chỉ ra một cây một lượt,
        chạm xong + qua ngày khác mới ra cây kế; đốm sáng bỏ lơ quá 3 ngày thì thôi chờ.
     B. cấp mở đúng 6, 9, 12, 15, 18, 20 — chưa tới cấp thì không ra.
     C. chỗ mọc: cặp cây gần nhất >= 2,8; không cây nào đứng trên liếp;
        chỗ rớt đốt tre cách gốc cây gần nhất >= 0,9.
   Mốc v175: cấp 6/9/12/14/16/18, cặp gần nhất 1,71, có chỗ rớt cách gốc 0,20. */
const { chromium } = require('playwright');
const PAGE = process.argv[2] || 'mv2_t176.html';
(async () => {
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 390, height: 844 } });
  const errs = []; p.on('pageerror', e => errs.push(String(e.message).slice(0, 200)));
  await p.route(u => !u.href.startsWith('http://127.0.0.1'), r => r.abort());
  await p.addInitScript(() => { try {
    localStorage.clear(); localStorage.setItem('mv3d-q', '1'); localStorage.setItem('mv2-lang', 'vi');
    localStorage.setItem('mv2-state', JSON.stringify({ v: 1, eco: 2, split: 1, qv2: 1, seen: { hello: 1, sold: 1 }, player: { av: 1, name: 'Bot', garden: 'Bot' }, lv: 20, xp: 40000, xu: 90000, exp: 1, qd: {}, inv: {}, seeds: {}, plots: {}, realTime: true, spd: 1, real: Date.now() }));
  } catch (e) {} });
  await p.goto('http://127.0.0.1:8777/' + PAGE);
  await p.waitForFunction(() => window.__ready, null, { timeout: 170000 });
  await p.waitForTimeout(3000);
  const ev = s => p.evaluate(s => window.__ev(s), s);
  await ev("document.querySelectorAll('.ddt,#intro').forEach(e=>e.hidden=true); try{closeSheet()}catch(e){}");
  let fail = 0;
  const ok = (n, c, got) => { console.log((c ? 'ĐẠT  ' : 'HỎNG ') + n + (c ? '' : '  -> ' + JSON.stringify(got))); if (!c) fail++; };

  /* A. một lúc một cây */
  const A = JSON.parse(await ev(`(()=>{
    const out = [];
    ST.lv = 20; ST.ft = {}; ST.ftLast = 0; ST.vsReady = 1;
    ST.kqHv = 9; ST.guestN = 9; ST.visitOut = 0; ST.kheHv = 9; ST.duaHv = 9;
    ftCheck(); out.push(Object.keys(ST.ft));
    ftCheck(); ftCheck(); out.push(Object.keys(ST.ft));
    ST.ft.vusua.st = 1; ST.ft.vusua.told = 1; ST.ftLast = Date.now() - 2*864e5;
    ftCheck(); out.push(Object.keys(ST.ft));
    ftCheck(); out.push(Object.keys(ST.ft));
    return JSON.stringify(out); })()`));
  ok('1a. cả sáu cây đủ điều kiện, một lượt ra đúng 1 cây', A[0].length === 1, A[0]);
  ok('1b. gọi thêm hai lượt nữa vẫn 1 cây', A[1].length === 1, A[1]);
  ok('1c. chạm cây 1 rồi, qua ngày khác thì ra cây 2', A[2].length === 2, A[2]);
  ok('1d. cùng ngày thì không ra cây 3', A[3].length === 2, A[3]);

  const A2 = JSON.parse(await ev(`(()=>{
    ST.lv = 20; ST.ft = { khevang: { st: 0, told: 0, t: Date.now() - 5*864e5, said: 1 } };
    ST.ftLast = 0; ST.vsReady = 1;
    ftCheck(); return JSON.stringify(Object.keys(ST.ft)); })()`));
  ok('1e. đốm sáng bỏ lơ 5 ngày thì thôi chờ', A2.length === 2, A2);

  const A3 = JSON.parse(await ev(`(()=>{
    ST.lv = 20; ST.ftLast = Date.now();
    ST.ft = { vusua: { st: 0, told: 0, t: Date.now() }, tretramdot: { st: 0, told: 0, t: Date.now(), dot: 0 } };
    ftCheck();
    return JSON.stringify(FTK.filter(k => ST.ft[k] && ST.ft[k].said)); })()`));
  ok('1f. một lượt chỉ một cây lên tiếng (bản lưu cũ có 2 đốm sáng)', A3.length === 1, A3);

  /* B. cấp mở */
  const B2 = JSON.parse(await ev(`JSON.stringify(FTK.map(k => [k, FT[k].lv]))`));
  ok('2a. cấp mở là 6, 9, 12, 15, 18, 20', JSON.stringify(B2.map(r => r[1])) === '[6,9,12,15,18,20]', B2);
  const B3 = JSON.parse(await ev(`(()=>{
    const out = [];
    for (const lv of [17, 20]){ ST.lv = lv; ST.ft = {}; ST.ftLast = 0; ST.vsReady = 0;
      ST.kqHv = 9; ST.guestN = 9; ST.kheHv = 9; ST.duaHv = 9;
      for (let i = 0; i < 9; i++){ ftCheck(); ST.ftLast = Date.now() - 2*864e5;
        FTK.forEach(k => { if (ST.ft[k] && ST.ft[k].st === 0){ ST.ft[k].st = 1; ST.ft[k].told = 1; } }); }
      out.push(Object.keys(ST.ft)); }
    return JSON.stringify(out); })()`));
  ok('2b. cấp 17: chỉ tre trăm đốt + trầu cau', JSON.stringify(B3[0].sort()) === '["traucau","tretramdot"]', B3[0]);
  ok('2c. cấp 20: thêm khế vàng + Sọ Dừa', B3[1].length === 4, B3[1]);

  /* C. chỗ mọc */
  const C = JSON.parse(await ev(`(()=>{
    const P = FTK.map(k => FT[k].at), D = (a, b) => Math.hypot(a[0]-b[0], a[1]-b[1]);
    let near = 99, pair = '';
    for (let i = 0; i < P.length; i++) for (let j = i+1; j < P.length; j++){ const d = D(P[i], P[j]); if (d < near){ near = d; pair = FTK[i]+'-'+FTK[j]; } }
    let dot = 99;
    for (const s of FTDOT.spots) for (const q of P) dot = Math.min(dot, D(s, q));
    const dr = (x, z, b) => Math.hypot(Math.max(b[0]-x, 0, x-b[2]), Math.max(b[1]-z, 0, z-b[3]));
    let liep = 99, lk = '';
    for (let i = 0; i < P.length; i++) for (const Q of PLOTS){ if (!Q.b) continue; const d = dr(P[i][0], P[i][1], Q.b); if (d < liep){ liep = d; lk = FTK[i]+' / '+Q.id; } }
    return JSON.stringify([near, pair, dot, liep, lk]); })()`));
  ok('3a. cặp cây gần nhất >= 2,8', C[0] >= 2.8, [C[0].toFixed(2), C[1]]);
  ok('3b. chỗ rớt đốt tre cách gốc cây >= 0,9', C[2] >= 0.9, C[2].toFixed(2));
  ok('3c. không cây nào đứng trên liếp (>= 0,5)', C[3] >= 0.5, [C[3].toFixed(2), C[4]]);

  ok('4. không có lỗi chạy', errs.length === 0, errs);
  console.log(fail ? '\n=== CÒN ' + fail + ' CHỖ HỎNG ===' : '\n=== ĐẠT HẾT ===');
  await b.close(); process.exit(fail ? 1 : 0);
})();
