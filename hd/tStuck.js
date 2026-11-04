// Nạp bản lưu thật, xem ô đất phơi ải hết giờ có thành đất của con không, và vòng vẽ có lỗi gì. node tStuck.js <save.json>
const {chromium}=require('playwright');const fs=require('fs');const SAVE=fs.readFileSync(process.argv[2],'utf8');const PAGE=process.env.PAGE||'mv2_t110e.html';
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:390,height:664}});
const logs=[];p.on('console',m=>{if(m.type()==='warning'||m.type()==='error')logs.push(m.type()+': '+m.text().slice(0,300))});p.on('pageerror',e=>logs.push('PAGEERR '+e.message));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},SAVE);
await p.goto('http://127.0.0.1:8777/'+PAGE,{timeout:300000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(8000);
const r=await p.evaluate(()=>{const S=JSON.parse(localStorage.getItem('mv2-state'));return {S4:S.land&&S.land.S4,oe:window.__oe,le:window.__le,se:window.__se}});
console.log(JSON.stringify(r));console.log(logs.slice(0,15).join('\n'));await b.close();})();
