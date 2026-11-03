const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1300,height:700}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const u=await p.evaluate(()=>{window.__stop=true;const {dcModel}=window.__FT;const S=window.__S,g=window.__g;g.ST.tm='fixed';g.ST.ovr=16;
 ['rao_go','rao_bup','cong_tre','cong_gach'].forEach((k,i)=>{const m=dcModel(k);m.position.set(-8.9+i*1.75,0,3.6);S.add(m);});
 for(let i=0;i<4;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-6.3,.6,3.6);c.object.position.copy(c.target).add(d);c.object.zoom=2.7;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();
 window.__r.render(S,g.cam);return window.__r.domElement.toDataURL('image/png');});
fs.writeFileSync('../gate.png',Buffer.from(u.split(',')[1],'base64'));console.log('errs',errs.slice(0,3));await b.close();})();
