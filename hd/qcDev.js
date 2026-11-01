const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const q of ['','?dev']){const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','0');}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html'+q,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;const g=window.__g;g.ST.spd=60;g.openSheet('set');const t=!!document.querySelector('#sheet details.dev');g.closeSheet();return {devPanel:t};});
// tải lại để xem cờ ×60 có bị trả về không
await p.evaluate(()=>{window.__g.ST.spd=60;localStorage.setItem('mv2-state',JSON.stringify(window.__g.ST));});
await p.reload({waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const spd=await p.evaluate(()=>window.__g.ST.spd);
console.log(q||'(không dev)',JSON.stringify(r),'spd sau khi tải lại:',spd,'errs',errs.length);await p.close();}
await b.close();})();
