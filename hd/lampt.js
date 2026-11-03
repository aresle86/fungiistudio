const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:700}});p.on('pageerror',e=>console.log('ERR',e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});
await p.evaluate(()=>{window.__stop=true;const g=window.__g;g.ST.realTime=false;g.ST.ovr=20.5;document.querySelector('#ngoai').hidden=true;document.querySelector('#tray').hidden=true;const c=g.cam,ct=window.__ctl.target,d=c.position.clone().sub(ct);ct.set(4.3,.6,1.6);c.position.copy(ct).add(d);c.zoom=3;c.updateProjectionMatrix();window.__ctl.update();window.__tick();window.__tick();});
await p.screenshot({path:'lamp.png',timeout:120000});await b.close();})();
