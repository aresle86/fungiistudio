const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:760}});p.on('pageerror',e=>console.log('ERR',e.message));p.on('console',m=>{if(m.type()==='error'&&!m.text().includes('TUNNEL'))console.log('CE',m.text())});await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});
await p.evaluate(()=>{window.__stop=true;const g=window.__g;g.ST.realTime=false;g.ST.ovr=10;document.querySelector('#ngoai').hidden=true;const c=g.cam,ct=window.__ctl.target,d=c.position.clone().sub(ct);ct.set(3.6,0,4.6);c.position.copy(ct).add(d);c.zoom=1.5;c.updateProjectionMatrix();window.__ctl.update();window.__tick();});
const S=async(x,z)=>await p.evaluate(([x,z])=>window.__scr(x,.035,z),[x,z]);
let t0=Date.now();
await p.click('#tCan');console.log('click',Date.now()-t0);
const w=await S(1.5,4.5);await p.mouse.move(w[0],w[1]);await p.mouse.down();console.log('down',Date.now()-t0);
for(let i=0;i<12;i++){const s=await S(1.3+i*.15,4.5+Math.sin(i)*.2);await p.mouse.move(s[0],s[1],{steps:2});await p.evaluate(()=>window.__tick());}
console.log('moves',Date.now()-t0);
await p.screenshot({path:'tt_water.png',timeout:120000});console.log('shot',Date.now()-t0);await p.mouse.up();
console.log('B1',await p.evaluate(()=>JSON.stringify([window.__g.ST.plots.B1.moist,window.__g.ST.can])));
const r=await S(2,3.88);await p.mouse.move(r[0],r[1]);await p.mouse.down();for(let i=0;i<30;i++){await p.evaluate(()=>window.__tick());}await p.mouse.up();
console.log('can',await p.evaluate(()=>window.__g.ST.can));
await p.click('#tCut');
const c0=await S(4.8,3.2);await p.mouse.move(c0[0],c0[1]);await p.mouse.down();const c1=await S(4.9,4.5);await p.mouse.move(c1[0],c1[1],{steps:10});for(let i=0;i<3;i++)await p.evaluate(()=>window.__tick());await p.screenshot({path:'tt_cut.png',timeout:120000});await p.mouse.up();
console.log('inv',await p.evaluate(()=>JSON.stringify(window.__g.ST.inv)));
await b.close();})();
