const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:620}});p.on('pageerror',e=>console.log('ERR',e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.waitForTimeout(500);
await p.click('#inGo');await p.evaluate(()=>{window.__stop=true;const g=window.__g;g.ST.realTime=false;g.ST.ovr=10;document.querySelector('#ngoai').hidden=true;const c=g.cam,ct=window.__ctl.target,d=c.position.clone().sub(ct);ct.set(2.5,0,4.6);c.position.copy(ct).add(d);c.zoom=1.8;c.updateProjectionMatrix();window.__ctl.update();g.ST.plots.C2.crop=null;g.refreshPlot('C2');g.act.water('B1');});
for(let i=0;i<50;i++)await p.evaluate(()=>window.__tick());
await p.evaluate(()=>{document.querySelector('#tSeed').click();document.querySelector('.fk[data-k="cai"]').dispatchEvent(new PointerEvent('pointerdown',{bubbles:true,pointerId:1}));window.dispatchEvent(new PointerEvent('pointerup',{pointerId:1}));window.__tick();});
await p.screenshot({path:'t27_goto.png',timeout:200000});await b.close();})();
