const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','2')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.waitForTimeout(800);
await p.evaluate(()=>{window.__stop=true;});await p.waitForTimeout(200);
for(const [n,x,z,zm] of [['zB',3.7,9.3,4.5]]){await p.evaluate(([x,z,zm])=>{const g=window.__g;g.ST.realTime=false;g.ST.ovr=10;document.querySelector('#ngoai').hidden=true;const c=g.cam;const d=c.position.clone().sub(window.__ctl.target);window.__ctl.target.set(x,.1,z);c.position.set(x,.1,z).add(d);c.zoom=zm;c.updateProjectionMatrix();if(window.__side){}const A=window.__g.ANIM||[];for(let i=0;i<3;i++)window.__tick();},[x,z,zm]);await p.waitForTimeout(300);await p.screenshot({path:n+'.png',timeout:180000});}
console.log(errs.join('\n'));await b.close();})();
