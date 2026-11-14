// Máy đo quy tắc giao diện (hud-hethong.md mục 10). Đi qua mọi màn hình và đo:
//   chu  : chữ nhỏ hơn 12px
//   bam  : chỗ bấm nhỏ hơn 44px (tính cả vùng bấm nới bằng ::before / ::after)
//   sat  : hai chỗ bấm cách nhau dưới 8px
//   dinh : hai khối có nền/viền dính nhau (dưới 4px)
//   tran : khối tràn khỏi màn hình hoặc chữ bị cắt
//   le   : style viết thẳng trong thẻ có khoảng cách lệch thang
// Chạy: node uicheck.js <trang trong lp/> <thư mục hình> [rộng] [cao]
// In bảng tổng; ghi <thư mục>/baocao.json. Thoát mã 1 nếu còn lỗi (dùng làm chốt khoá trước khi đẩy).
const { chromium } = require('playwright'); const fs = require('fs');
const page = process.argv[2], out = process.argv[3], W = +process.argv[4] || 390, H = +process.argv[5] || 844;
const ONLY = process.argv[6] ? process.argv[6].split(',') : null;
const STEPS = [
  ['hud', ''],
  ['so-viec', "openBook('viec')"], ['so-kho', "openBook('kho')"], ['so-giong', "openBook('giong')"], ['so-giong-1', "openBook('giong','cai')"],
  ['so-ca', "openBook('ca')"], ['so-cotich', "openBook('cotich')"], ['so-mon', "openBook('mon')"], ['so-thu', "openBook('thu')"], ['so-buom', "openBook('buom')"],
  ['cho-ban', "openSheet('cho')"], ['cho-mua', "openSheet('cho');SHEET.tab='mua';renderSheet()"], ['cho-don', "openSheet('cho');SHEET.tab='don';renderSheet()"], ['cho-tiem', "openSheet('cho');SHEET.tab='tiem';renderSheet()"],
  ['ben', "openSheet('ben')"], ['chono', "openSheet('chono')"], ['vuon', "openSheet('vuon')"],
  ['o-dat', "openSheet('plot',Object.keys(ST.plots)[0])"], ['o-dat-2', "openSheet('plot',Object.keys(ST.plots).find(k=>ST.plots[k].crop)||Object.keys(ST.plots)[3])"],
  ['caidat', "openSheet('set')"], ['ga', "openSheet('ga')"], ['vit', "openSheet('vit')"], ['ao', "openSheet('big','ao')"], ['vusua', "openSheet('big','vusua')"],
  ['bep', "openSheet('bep')"], ['tb', "openSheet('tb')"], ['tb-ghe', "ST.tb={t:0,help:0,done:1,lo:1};const c=cnoS();c.own.son=1;c.own.ngoc=1;openSheet('tb')"], ['quay', "openSheet('quay')"], ['tudo', "openSheet('tudo')"], ['tiemmay', "openSheet('tiemmay')"],
  ['thu', "openSheet('thu')"], ['say', "openSheet('say')"], ['radio', "openSheet('radio')"], ['ong', "openSheet('ong')"], ['nong', "openSheet('nong')"],
  ['lo', "openSheet('lo')"], ['khap', "openSheet('khap')"], ['ho', "openSheet('ho')"], ['gio', "openSheet('gio')"], ['baoloi', "openSheet('bug')"],
  ['vong-chon', "openRing(Object.keys(ST.plots)[0])"], ['vong-hat', "openRing(Object.keys(ST.plots)[0],'seed')"],
  ['sap-xep', "sapMode(true)"], ['chon-dang', "openIntro()"],
  // ba màn dưới đổi cảnh, chạy riêng từng màn: node uicheck.js <trang> <thư mục> 390 844 cau-ca
  ['cau-ca', "for(const k in ST.inv)ST.inv[k]=0;fmEnter()", 3000], ['cau-ghe', "ST.tb={t:0,help:0,done:1,lo:Date.now()};for(const k in ST.inv)ST.inv[k]=0;fmEnter();FM.ghe=true;tbGheMove();fuiAim()", 3000], ['tham-vuon', "visitGo()"], ['cho-huyen', "ST.lv=Math.max(ST.lv,CHM.lv);chEnter()", 9000],
];
const MEASURE = () => {
  const VW = innerWidth, VH = innerHeight, OK = new Set([0, 1, 2, 4, 8, 12, 16, 24]);
  const vis = e => { const r = e.getBoundingClientRect(); if (r.width < 1 || r.height < 1) return null; if (r.bottom < 0 || r.top > VH || r.right < 0 || r.left > VW) return null;
    if (e.checkVisibility && !e.checkVisibility({ checkOpacity: true, checkVisibilityCSS: true })) return null; return r; };
  const sig = e => { const c = x => x.tagName.toLowerCase() + (x.id ? '#' + x.id : '') + (typeof x.className === 'string' && x.className.trim() ? '.' + x.className.trim().split(/\s+/).filter(k => !/^(on|off|now|done|sel|act|no|ok|hot)$/.test(k)).slice(0, 3).join('.') : ''); return (e.parentElement && e.parentElement !== document.body ? c(e.parentElement) + ' > ' : '') + c(e); };
  // chỉ đo lớp trên cùng: phần tử nằm dưới tấm che (scrim) thì bỏ
  const top = e => { const r = e.getBoundingClientRect(), x = Math.min(VW - 1, Math.max(0, r.left + r.width / 2)), y = Math.min(VH - 1, Math.max(0, r.top + Math.min(r.height / 2, 12))); const t = document.elementFromPoint(x, y); return !t || t === e || e.contains(t) || t.contains(e) || !(t.closest('#scrim') || (t.closest('#sheet,#book,#intro,#lvup') && !e.closest('#sheet,#book,#intro,#lvup'))); };
  const all = [...document.body.querySelectorAll('*')].filter(e => !/^(SCRIPT|STYLE|CANVAS|BR|PATH|G|SVG|DEFS)$/i.test(e.tagName) && !e.closest('svg') && !e.closest('#err,#load'));
  const out = []; const add = (t, e, v) => out.push([t, sig(e), v]);
  const V = []; for (const e of all){ const r = vis(e); if (r && top(e)) V.push([e, r, getComputedStyle(e)]); }
  // chữ
  for (const [e, r, cs] of V){ let own = false; for (const n of e.childNodes) if (n.nodeType === 3 && n.nodeValue.trim()){ own = true; break; } if (!own) continue; const fs = parseFloat(cs.fontSize); if (fs < 11.99) add('chu', e, fs); }
  // chỗ bấm
  const isC = e => /^(BUTTON|A|INPUT|SELECT|TEXTAREA|SUMMARY)$/.test(e.tagName) || e.hasAttribute('onclick') || e.getAttribute('role') === 'button' || e.hasAttribute('data-a') || e.hasAttribute('data-b');
  const C = []; for (const [e, r, cs] of V){ if (!isC(e)) { if (cs.cursor !== 'pointer' || (e.parentElement && getComputedStyle(e.parentElement).cursor === 'pointer')) continue; }
    if (cs.pointerEvents === 'none' || e.disabled) continue; if (e.closest('button,a') !== e && e.closest('button,a')) continue;
    let x0 = r.left, y0 = r.top, x1 = r.right, y1 = r.bottom;
    for (const ps of ['::before', '::after']){ const p = getComputedStyle(e, ps); if (p.content === 'none' || p.position !== 'absolute') continue; const f = k => { const v = parseFloat(p[k]); return isNaN(v) ? 0 : v; };
      if (f('left') < 0) x0 = Math.min(x0, r.left + f('left')); if (f('top') < 0) y0 = Math.min(y0, r.top + f('top')); if (f('right') < 0) x1 = Math.max(x1, r.right - f('right')); if (f('bottom') < 0) y1 = Math.max(y1, r.bottom - f('bottom')); }
    C.push([e, { l: x0, t: y0, r: x1, b: y1, vl: r.left, vt: r.top, vr: r.right, vb: r.bottom }]); }
  for (const [e, q] of C){ const w = Math.round((q.r - q.l) * 10) / 10, h = Math.round((q.b - q.t) * 10) / 10; if (w < 43.9 || h < 43.9) add('bam', e, Math.round(w) + 'x' + Math.round(h)); }
  for (let i = 0; i < C.length; i++) for (let j = i + 1; j < C.length; j++){ const [a, A] = C[i], [b, B] = C[j]; if (a.contains(b) || b.contains(a)) continue;
    const ov = (p0, p1, q0, q1) => Math.min(p1, q1) - Math.max(p0, q0); const oy = ov(A.vt, A.vb, B.vt, B.vb), ox = ov(A.vl, A.vr, B.vl, B.vr);
    let g = null; if (oy > 4 && ox <= 0) g = -ox; else if (ox > 4 && oy <= 0) g = -oy; if (g !== null && g < 7.9) add('sat', a, Math.round(g * 10) / 10 + ' voi ' + sig(b).split(' > ').pop()); }
  // khối dính nhau
  const kevach = cs => (cs.backgroundColor === 'rgba(0, 0, 0, 0)' || cs.backgroundColor === 'transparent') && cs.boxShadow === 'none' && parseFloat(cs.borderLeftWidth) === 0 && parseFloat(cs.borderRightWidth) === 0; // hàng danh sách chỉ có vạch kẻ ngang: không phải khối
  const boxy0 = cs => (cs.backgroundColor !== 'rgba(0, 0, 0, 0)' && cs.backgroundColor !== 'transparent') || parseFloat(cs.borderTopWidth) > 0 || cs.boxShadow !== 'none';
  const M = new Map(V.map(x => [x[0], x]));
  const boxy = cs => boxy0(cs) && !kevach(cs);
  for (const [e, r, cs] of V){ if (!boxy(cs) || cs.position === 'absolute' || cs.position === 'fixed') continue; let n = e.nextElementSibling; while (n && !M.has(n)) n = n.nextElementSibling; if (!n) continue; const [, r2, c2] = M.get(n); if (!boxy(c2) || c2.position === 'absolute' || c2.position === 'fixed') continue;
    const pd = getComputedStyle(e.parentElement); if (pd.display.includes('flex') && pd.columnGap === '0px' && pd.flexDirection.startsWith('row') && pd.overflow !== 'visible' && parseFloat(pd.borderTopLeftRadius) > 0) continue; // thanh chia đoạn cố ý
    const sh = s => { const m = /(-?[\d.]+)px (-?[\d.]+)px/.exec(s.boxShadow); return m ? Math.max(0, parseFloat(m[2])) : 0; };
    let g; if (r2.top >= r.bottom - 1) g = r2.top - r.bottom - sh(cs); else if (r2.left >= r.right - 1) g = r2.left - r.right; else continue; if (g < 3.9 && g > -6) add('dinh', e, Math.round(g * 10) / 10 + ' voi ' + sig(n).split(' > ').pop()); }
  // tràn
  for (const [e, r, cs] of V){ if (cs.position === 'fixed' && (r.right > VW + 1 || r.left < -1) && r.width <= VW) add('tran', e, 'ra ngoai ' + Math.round(Math.max(r.right - VW, -r.left)));
    let own = false; for (const n of e.childNodes) if (n.nodeType === 3 && n.nodeValue.trim()){ own = true; break; }
    if (own && cs.overflowX !== 'visible' && cs.textOverflow !== 'ellipsis' && e.scrollWidth > e.clientWidth + 1) add('tran', e, 'chu bi cat ' + (e.scrollWidth - e.clientWidth)); }
  for (const pn of document.querySelectorAll('#sheet,#bk,.bkpg,#shB')){ if (!vis(pn)) continue; if (pn.scrollWidth > pn.clientWidth + 1 && /auto|scroll/.test(getComputedStyle(pn).overflowX)) add('tran', pn, 'cuon ngang ' + (pn.scrollWidth - pn.clientWidth)); }
  // style viết thẳng
  for (const [e] of V){ const st = e.getAttribute('style'); if (!st) continue; for (const m of st.matchAll(/(?:^|;)\s*(gap|row-gap|column-gap|padding[-\w]*|margin[-\w]*)\s*:\s*([^;]+)/g)) for (const v of m[2].matchAll(/(-?[\d.]+)px/g)){ const a = Math.abs(parseFloat(v[1])); if (!OK.has(a) && a <= 24) add('le', e, m[1] + ':' + v[1]); } }
  return out;
};
(async () => {
  fs.mkdirSync(out, { recursive: true });
  const b = await chromium.launch({ args: ['--use-angle=metal', '--enable-gpu', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: W < 600 ? 2 : 1 }); const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.route(u => !u.href.startsWith('http://127.0.0.1'), r => r.abort());
  await p.addInitScript(() => { try { localStorage.clear(); localStorage.setItem('mv3d-q', '1'); localStorage.setItem('mv2-lang', 'vi'); localStorage.setItem('mv2-state', JSON.stringify({ v: 1, eco: 2, split: 1, qv2: 1, seen: { hello: 1 }, player: { av: 1, name: 'Bot', garden: 'Bot' }, lv: 19, xp: 26000, xu: 90000, exp: 1, qd: {}, inv: {}, seeds: {}, plots: {}, realTime: true, spd: 1, real: Date.now() })); } catch (e) {} });
  await p.goto('http://127.0.0.1:8777/' + page, { waitUntil: 'domcontentloaded' }); await p.waitForFunction(() => window.__ready, null, { timeout: 100000 }); await p.waitForTimeout(2500);
  const ev = s => p.evaluate(s => window.__ev(s), s);
  await ev('document.querySelectorAll(".ddt,#intro").forEach(e=>e.hidden=true)');
  try { await ev("(()=>{for(const k of Object.keys(ICON)){try{const g=GD(k);if(g&&g.name)ST.inv[k]=6}catch(e){}}ST.notes=ST.notes&&ST.notes.length?ST.notes:ST.notes;})()"); } catch (e) { console.log('inv', e.message.slice(0, 120)); }
  const rep = {}, tot = {}, uniq = new Map();
  for (const [name, code, cho] of STEPS){ if (ONLY && !ONLY.includes(name)) continue;
    try { await ev("(()=>{try{closeSheet()}catch(e){}try{if(FM.on)fmExit()}catch(e){}try{closeBook()}catch(e){}try{if(typeof SAP!=='undefined'&&SAP)sapMode(false)}catch(e){}try{RING.hidden=true}catch(e){}try{document.querySelector('#intro').hidden=true}catch(e){}})()"); } catch (e) {}
    let bad = ''; if (code){ try { await ev(code); } catch (e) { bad = e.message.split('\n')[0].slice(0, 140); } }
    await p.waitForTimeout(cho || 900);
    const r = await p.evaluate(MEASURE); rep[name] = r; const c = {}; for (const [t, s, v] of r){ c[t] = (c[t] || 0) + 1; tot[t] = (tot[t] || 0) + 1; const k = t + ' | ' + s + ' | ' + String(v).replace(/ voi .*/, ''); if (!uniq.has(k)) uniq.set(k, [name, String(v)]); }
    await p.screenshot({ path: out + '/' + name + '.png' });
    console.log(name.padEnd(12), JSON.stringify(c), bad ? 'LOI MO: ' + bad : '');
  }
  fs.writeFileSync(out + '/baocao.json', JSON.stringify({ page, W, H, tot, uniq: [...uniq].map(([k, v]) => [k, ...v]), rep }, null, 1));
  console.log('TONG', JSON.stringify(tot), 'khac nhau', uniq.size, 'loi trang', errs.length, errs.slice(0, 3));
  await b.close(); process.exit(uniq.size ? 1 : 0);
})().catch(e => { console.log('FAIL', e.message); process.exit(2); });
