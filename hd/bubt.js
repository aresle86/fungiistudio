const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:760}});p.on('pageerror',e=>console.log('ERR',e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});
await p.evaluate(()=>{window.__stop=true;const g=window.__g;g.ST.realTime=false;g.ST.ovr=10;document.querySelector('#ngoai').hidden=true;g.ST.plots.B1.dry=2500;g.ST.plots.B1.moist=0;g.ST.plots.C1.dead=true;g.refreshPlot('B1');g.refreshPlot('C1');const c=g.cam,ct=window.__ctl.target,d=c.position.clone().sub(ct);ct.set(2.6,0,4.9);c.position.copy(ct).add(d);c.zoom=2.4;c.updateProjectionMatrix();window.__tick();});
await p.waitForTimeout(500);await p.screenshot({path:'bub.png'});
await p.click('#bSo');await p.waitForTimeout(600);await p.screenshot({path:'bk_leg.png'});await b.close();})();
