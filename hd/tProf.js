const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1300,height:700}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.goto('http://127.0.0.1:8777/mv2_prof.html',{waitUntil:'domcontentloaded'});p.on('console',m=>{if(m.type()=='error')errs.push(m.text())});await p.waitForFunction(()=>window.__TM&&window.__TM.some(x=>x[0]==4186),null,{timeout:300000});
const t=await p.evaluate(()=>window.__TM);let pr=0;for(const [l,ms] of t){console.log(l,ms,ms-pr);pr=ms;}console.log(errs.slice(0,3));await b.close();})();
