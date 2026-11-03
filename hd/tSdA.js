const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1300,height:700}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;const {fairyModel}=window.__FT;const S=window.__S,g=window.__g;g.ST.tm='fixed';g.ST.ovr=17.6;
 const m=fairyModel('sodua',3);m.position.set(-8.2,0,4.2);S.add(m);window.__m=m;
 for(let i=0;i<4;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-8.2,.5,4.2);c.object.position.copy(c.target).add(d);c.object.zoom=4.5;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();});
for(const [i,t] of [0,.15,.3,.5,.7,.9,1.1,1.25,1.4].entries()){const u=await p.evaluate(t=>{const g=window.__g;window.__FT.sdAnim(window.__m.userData.so,3,t);window.__r.render(window.__S,g.cam);return window.__r.domElement.toDataURL('image/png');},t);fs.writeFileSync('fr'+i+'.png',Buffer.from(u.split(',')[1],'base64'));}
console.log('errs',errs.slice(0,3));await b.close();})();
