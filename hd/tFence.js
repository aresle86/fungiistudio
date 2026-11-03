const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:800,height:500}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()!=='log')errs.push(m.text().slice(0,200))});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;const g=window.__g,ST=g.ST;ST.lv=13;for(let i=1;i<=12;i++)ST.land['H'+i]={st:'own'};for(let i=0;i<100;i++)window.__tick();return {le:window.__le,oe:window.__oe};});
console.log(JSON.stringify(r),errs.slice(0,5));await b.close();})();
