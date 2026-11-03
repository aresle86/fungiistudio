const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:600,height:220}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const srcs=await p.evaluate(()=>['icSo','icCho','icSet'].map(i=>document.getElementById(i).src));
await p.setContent('<body style="margin:0;background:#86B06A">'+srcs.map(s=>`<img src="${s}" style="width:180px;height:180px;margin:10px">`).join('')+'</body>');await p.waitForTimeout(300);await p.screenshot({path:'qc2/icons.png'});await b.close();})();
