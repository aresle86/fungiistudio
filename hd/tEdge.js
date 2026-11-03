const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:966,height:585}});p.on('pageerror',e=>console.log('ERR',e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const i=0;for(const [x,z,zm] of [[11.5,10,.8],[-4.6,10,.8]]){await p.evaluate(([x,z,zm])=>{const g=window.__g;g.ST.player={av:1,name:'Na',garden:'V'};g.ST.lv=12;document.querySelectorAll('.lvup,#intro').forEach(e=>e.hidden=true);const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(x,.3,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();},[x,z,zm]);
await p.waitForTimeout(2500);await p.screenshot({path:`../edge_${x}.png`,timeout:120000});}
// bark
await p.evaluate(()=>{const c=window.__ctl;c.object.zoom=1.3;c.target.set(4.2,.4,4.6);c.object.updateProjectionMatrix();});
await p.evaluate(()=>{try{window.__e.lsay?0:0}catch(e){}});
await b.close();})();
