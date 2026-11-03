const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:600}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g,ST=g.ST;ST.player={av:1,name:'N',garden:'V'};ST.lv=4;ST.odd=ST.odd||{list:[]};ST.odd.list.push({k:'cui',x:3.0,z:9.6},{k:'cui',x:3.6,z:9.9});
 for(let i=0;i<4;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(3.3,.1,9.75);c.object.position.copy(c.target).add(d);c.object.zoom=6;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();window.__r.render(window.__S,g.cam);});
await p.screenshot({path:'../cui.png'});console.log(errs);await b.close();})();
