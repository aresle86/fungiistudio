const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:600}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;const g=window.__g,V=window.__FT3.TBV;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=19;const o=[];for(const xu of [500,700,1200]){g.ST.xu=xu;for(let i=0;i<3;i++)window.__tick();o.push(xu+':'+V.b.visible);}return o.join(' ');});
console.log(r,errs.join('|'));await b.close();})();
