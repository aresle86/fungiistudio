const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:600}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const [x,z,zm]=process.argv.slice(2).map(Number);
const u=await p.evaluate(([x,z,zm])=>{const g=window.__g,ST=g.ST;ST.lv=10;ST.fishLog={caloc:{n:1,max:2},chep:{n:1,max:1},bongtuong:{n:1,max:1},caro:{n:2,max:.2}};window.__stop=true;for(let i=0;i<20;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(x,.2,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();for(let i=0;i<5;i++)window.__tick();window.__r.render(window.__S,g.cam);return window.__r.domElement.toDataURL('image/png');},[x,z,zm]);
fs.writeFileSync('../jar.png',Buffer.from(u.split(',')[1],'base64'));console.log('errs',errs.slice(0,3));await b.close();})();
