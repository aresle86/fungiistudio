const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:700}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g,S=window.__S,X=window.__FT3;g.ST.tm='fixed';g.ST.ovr=9.5;
 const a=X.beeHive(false);a.position.set(-8.6,0,6.6);a.scale.setScalar(1.6);S.add(a);const c2=X.beeHive(true);c2.position.set(-7.4,0,7.0);c2.scale.setScalar(1.6);c2.rotation.y=-.3;S.add(c2);X.beeAnim(a.userData.bees,1.2);X.beeAnim(c2.userData.bees,2.7);
 for(let i=0;i<4;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-7.5,.6,7);c.object.position.copy(c.target).add(d);c.object.zoom=8;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();X.beeAnim(a.userData.bees,1.2);X.beeAnim(c2.userData.bees,2.7);window.__r.render(S,g.cam);});
await p.screenshot({path:'../bee.png',timeout:120000});console.log(errs);await b.close();})();
