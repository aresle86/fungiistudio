const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:600}});await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','2')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.evaluate(()=>{window.__stop=true;document.querySelector('#ngoai').hidden=true;const g=window.__g;g.ST.realTime=false;g.ST.ovr=10;});
for(let i=0;i<4;i++){await p.evaluate(i=>{const c=window.__g.cam,ct=window.__ctl.target;const d=c.position.clone().sub(ct);ct.set(6+i*.013,0,8.3);c.position.copy(ct).add(d);c.zoom=2.2;c.updateProjectionMatrix();window.__tick();},i);await p.waitForTimeout(150);await p.screenshot({path:'pan_'+i+'.png'});}
await b.close();})();
