const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1280,height:800}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,{timeout:300000});await p.evaluate(()=>{window.__stop=true;});await p.waitForTimeout(500);
console.log(await p.evaluate(()=>{const t=performance.now();for(let i=0;i<60;i++)window.__tick();return ((performance.now()-t)/60).toFixed(1)}));await b.close();})();
