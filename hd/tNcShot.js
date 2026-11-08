// tNcShot: chụp bảng duyệt mô hình cây mới. node tNcShot.js [trang] [danh sách cây]
const {chromium}=require('playwright');const fs=require('fs');const PAGE=process.argv[2]||'mv2_nc.html';
const L=[['dudu','Đu đủ'],['mangcau','Mãng cầu ta'],['sung','Sung'],['buoi','Bưởi Năm Roi'],['vusua','Vú sữa Lò Rèn'],['saurieng','Sầu riêng'],['duasap','Dừa sáp'],['bau','Bầu (giàn trên mương)'],['muop','Mướp (giàn trên mương)'],['daurong','Đậu rồng (cọc chữ A)'],['khom','Khóm'],['mia','Mía']];
const ONLY=(process.argv[3]||'').split(',').filter(Boolean);
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:600,height:400}});p.setDefaultTimeout(600000);const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(()=>{localStorage.clear();localStorage.setItem('mv3d-q','1')});
await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready,null,{timeout:600000});await p.evaluate(()=>{window.__stop=1});
for(const [k,n] of L){ if(ONLY.length&&!ONLY.includes(k)) continue; const t=Date.now(); const u=await p.evaluate(([k,n])=>window.__nc.sheet(k,n),[k,n]); fs.writeFileSync('/tmp/nc/'+k+'.png',Buffer.from(u.split(',')[1],'base64')); console.log(k,Date.now()-t,'ms'); }
if(!ONLY.length||ONLY.includes('lineup')){ const u=await p.evaluate(()=>window.__nc.lineup(['chuoi','oi','khe','xoai','dua','dudu','mangcau','sung','buoi','vusua','saurieng','duasap'])); fs.writeFileSync('/tmp/nc/lineup.png',Buffer.from(u.split(',')[1],'base64'));
 const v=await p.evaluate(()=>window.__nc.lineup(['khoqua','bau','muop'],4,1.1)); fs.writeFileSync('/tmp/nc/lineup2.png',Buffer.from(v.split(',')[1],'base64'));
 const w=await p.evaluate(()=>window.__nc.lineup(['cachua','daurong','bap','khom','mia'],4,1.6)); fs.writeFileSync('/tmp/nc/lineup3.png',Buffer.from(w.split(',')[1],'base64')); }
console.log('errs',errs.slice(0,6));await b.close();})();
