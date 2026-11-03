const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:400,height:300}});await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.evaluate(()=>{window.__stop=true});
let i=0;for(const [a,e] of [[1.5,.35],[1.0,.7]]){const u=await p.evaluate(([a,e])=>window.__isoBoat(a,e),[a,e]);fs.writeFileSync(`boat_${i++}.png`,Buffer.from(u.split(',')[1],'base64'));}
await b.close();})();
