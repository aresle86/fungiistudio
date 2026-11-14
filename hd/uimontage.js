// Ghép hình trước | sau của từng màn để soát bằng mắt. node uimontage.js <thư mục trước> <thư mục sau> <thư mục ra> [số cặp mỗi tấm]
const { chromium } = require('playwright'); const fs = require('fs');
(async () => { const [A, B, O, n0] = process.argv.slice(2), N = +n0 || 4; fs.mkdirSync(O, { recursive: true });
  const names = fs.readdirSync(B).filter(f => f.endsWith('.png')).map(f => f.slice(0, -4)).filter(f => fs.existsSync(A + '/' + f + '.png'));
  const order = JSON.parse(fs.readFileSync(B + '/baocao.json')).rep; const list = Object.keys(order).filter(k => names.includes(k));
  const b = await chromium.launch(); const im = f => 'data:image/png;base64,' + fs.readFileSync(f).toString('base64');
  for (let i = 0, k = 0; i < list.length; i += N, k++){ let h = '<body style="margin:0;background:#222;font:14px sans-serif;color:#fff"><div style="display:flex;gap:10px;padding:6px">';
    for (const nm of list.slice(i, i + N)) h += `<div><div>${nm} · trước | sau</div><div style="display:flex;gap:2px"><img src="${im(A + '/' + nm + '.png')}" style="width:195px"><img src="${im(B + '/' + nm + '.png')}" style="width:195px"></div></div>`;
    const p = await b.newPage({ viewport: { width: N * 402 + 12, height: 460 }, deviceScaleFactor: 1.4 }); await p.setContent(h + '</div></body>'); await p.screenshot({ path: `${O}/ghep-${String(k).padStart(2, '0')}.png` }); await p.close(); }
  console.log('ok', list.length); await b.close(); })();
