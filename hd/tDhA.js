const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1300,height:700}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const {fairyModel}=window.__FT;const S=window.__S,g=window.__g;g.ST.tm='fixed';g.ST.ovr=10;
 const m=fairyModel('duahau',3);m.position.set(-8.2,0,4.2);S.add(m);window.__m=m;
 for(let i=0;i<4;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-8.2,.6,4.2);c.object.position.copy(c.target).add(d);c.object.zoom=3.2;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();});
for(const [i,t] of [0,.05,.11,1.2,2.4,3.6].entries()){await p.evaluate(t=>{window.__FT.dhBird(window.__m.userData.bird,t);window.__r.render(window.__S,window.__g.cam);},t);await p.screenshot({path:'../dhf'+i+'.png',clip:{x:60,y:20,width:600,height:520}});}
console.log('errs',errs.slice(0,3));await b.close();})();
