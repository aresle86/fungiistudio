const {chromium}=require('playwright');(async()=>{const b=await chromium.launch();const p=await b.newPage({viewport:{width:2060,height:2330}});
for(const n of ['so','cho']){await p.goto('http://127.0.0.1:8777/'+n+'_prev.html');await p.waitForTimeout(2500);await p.screenshot({path:n+'_prev.png',fullPage:true});}
await b.close();})();
