const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:800,height:600}});await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','2')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.evaluate(()=>{window.__stop=true;});await p.waitForTimeout(300);
const hy=await p.evaluate(()=>{const g=window.__g;g.ST.realTime=false;g.ST.ovr=10;document.querySelector('#ngoai').hidden=true;const c=g.cam;const d=c.position.clone().sub(window.__ctl.target);window.__ctl.target.set(4,0,9.2);c.position.set(4,0,9.2).add(d);c.zoom=5;c.updateProjectionMatrix();return 1;});
for(let i=0;i<6;i++){await p.evaluate(()=>{window.__tick();});await p.waitForTimeout(80);await p.screenshot({path:'fl_'+i+'.png'});}
await b.close();})();
