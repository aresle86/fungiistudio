const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:760}});p.on('pageerror',e=>console.log('ERR',e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:240000});
console.log(await p.evaluate(()=>{window.__stop=true;document.querySelector('#intro').hidden=true;const g=window.__g,X=window.__x,S=g.ST,o={xu:S.xu,lu:X.luCost()};
 // cachua A2 ripe: harvest 3 times
 const res=[];for(let i=0;i<3;i++){S.plots.A2.moist=1;S.plots.A2.g=g.ST.plots.A2.crop?Math.max(S.plots.A2.g,0):0; S.plots.A2.g=1e9>0?14400:0; const r=X.act.harvest('A2'); res.push([r,S.plots.A2.crop,S.plots.A2.cut,X.stageOf(S.plots.A2),S.inv.cachua,+S.plots.A2.soil.toFixed(2)]); }
 o.cachua=res; return JSON.stringify(o);}));
await p.evaluate(()=>{window.__g.openBook?0:0;document.querySelector('#bSo').click();document.querySelector('.stk[data-k="ot"]').click();});await p.waitForTimeout(400);await p.screenshot({path:'eco_book.png',timeout:200000});
await b.close();})();
