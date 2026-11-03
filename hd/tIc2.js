const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage();await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const ic=await p.evaluate(()=>['rom','cui','tre'].map(k=>window.__ICON[k]));ic.forEach((u,i)=>u&&fs.writeFileSync('../ic'+i+'.png',Buffer.from(u.split(',')[1],'base64')));await b.close();})();
