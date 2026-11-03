const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage();await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
console.log(await p.evaluate(()=>{const c=window.__g.cam;return JSON.stringify([c.position,window.__ctl.target])}));await b.close();})();
