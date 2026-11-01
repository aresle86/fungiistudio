// Xuất icon của game ra file PNG để xem. Dùng: node qcIcons.js <thư mục ra> <khoá1,khoá2,...>
const fs = require('fs'); const {chromium} = require('playwright');
const OUT = process.argv[2]; const KEYS = process.argv[3].split(',');
(async () => {
  const b = await chromium.launch({args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist']});
  const p = await b.newPage();
  await p.addInitScript(() => { try { localStorage.clear(); } catch (e) {} });
  await p.goto('http://127.0.0.1:8777/'+(process.env.PG||'mv2_dev.html')+'', {waitUntil: 'domcontentloaded'});
  await p.waitForFunction(() => window.__ready, null, {timeout: 300000});
  const r = await p.evaluate((K) => {
    window.__stop = true; const I = window.__ICON || window.__x.ICON; const out = {};
    for (const k of K) out[k] = I[k] || null;
    out.__keys = Object.keys(I).filter(k => /tre|gian|cuoc|coc|cot|trellis|hoe|lieng|liem/i.test(k));
    return out;
  }, KEYS);
  console.log('keys', r.__keys.join(','));
  for (const k of KEYS) { if (r[k] && r[k].startsWith('data:')) { fs.writeFileSync(`${OUT}/icon_${k}.png`, Buffer.from(r[k].split(',')[1], 'base64')); console.log('saved', k); } else console.log('missing', k); }
  await b.close();
})();
