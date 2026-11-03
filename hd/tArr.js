const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,hasTouch:true});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=6;g.ST.xp=900;g.ST.seen.hello=1;g.ST.dd={n:1,d:new Date().toDateString(),last:Date.now()};for(const k in g.ST.plots){const q=g.ST.plots[k];if(q.crop)q.g=99999;}for(let i=0;i<200;i++)window.__tick();window.__stop=true;});
await p.addStyleTag({content:'.ddt{display:none!important}'});
const run=n=>p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);
await p.waitForTimeout(4000);await run(60);
const out=[];
for(const [x,z,zm,n] of [[-4.5,-1,1.7,'a1'],[9,1,1.6,'a2'],[3,-3,1.8,'a3']]){
 await p.evaluate(([x,z,zm])=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(x,0,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();},[x,z,zm]);await run(3);await p.waitForTimeout(600);
 const A=await p.evaluate(()=>[...document.querySelectorAll('.nava')].filter(e=>!e.hidden).map(e=>{const r=e.getBoundingClientRect();return [Math.round(r.x),Math.round(r.y),e.querySelector('b').textContent,e.querySelector('.nap').style.transform];}));
 out.push([n,A]);await p.screenshot({path:'../'+n+'.png',timeout:300000});}
console.log(JSON.stringify(out));console.log(errs.join('\n')||'no errors');await b.close();})();
