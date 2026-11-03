const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1000,height:640}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
for (const [nm,hr] of [['day',10],['dusk',19.2]]){
const u=await p.evaluate(([hr,first])=>{window.__stop=true;const {fairyModel}=window.__FT;const S=window.__S,g=window.__g;g.ST.tm='fixed';g.ST.ovr=hr;
 if(first){const x=5.4,z=2.6;const a=fairyModel('vusua',4);a.position.set(x,0,z);S.add(a);const t=fairyModel('tretramdot',3);t.position.set(x+2.3,0,z+.6);S.add(t);window.__ftx=[x,z];}
 const [x,z]=window.__ftx;for(let i=0;i<8;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(x+1.2,1.1,z+.3);c.object.position.copy(c.target).add(d);c.object.zoom=2.3;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();
 window.__r.render(S,g.cam);return window.__r.domElement.toDataURL('image/png');},[hr,nm==='day']);
fs.writeFileSync('../ft_'+nm+'.png',Buffer.from(u.split(',')[1],'base64'));}
console.log('errs',errs.slice(0,3));await b.close();})();
