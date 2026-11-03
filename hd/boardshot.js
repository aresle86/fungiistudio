const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:400,height:300}});p.on('pageerror',e=>console.log('ERR',e.message));await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.evaluate(()=>{window.__stop=true});
const save=(n,u)=>fs.writeFileSync('board/'+n+'.png',Buffer.from(u.split(',')[1],'base64'));
save('stall_a',await p.evaluate(()=>window.__stallShot(1.1,.42,1100,1000,1.55)));
save('stall_b',await p.evaluate(()=>window.__stallShot(.8,.82,1000,900,1.6)));
const ic=await p.evaluate(()=>window.__icons());for(const k in ic)save('ic_'+k,ic[k]);
const ng=await p.evaluate(()=>window.__ngoai());for(const k in ng)save('ng_'+k,ng[k]);
await b.close();})();
