const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:400,height:300}});await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.evaluate(()=>{window.__stop=true});
for(const [w,a] of [['chuoi',.8],['chuoi',2.6],['coop',.8],['coop',-.8]]){const u=await p.evaluate(([w,a])=>window.__iso(w,a),[w,a]);fs.writeFileSync(`iso_${w}_${a}.png`,Buffer.from(u.split(',')[1],'base64'));}
await b.close();})();
