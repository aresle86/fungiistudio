const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:760}});p.on('pageerror',e=>console.log('ERR',e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});
await p.evaluate(()=>{window.__stop=true;const g=window.__g;g.ST.realTime=false;g.ST.ovr=10;document.querySelector('#ngoai').hidden=true;const c=g.cam,ct=window.__ctl.target,d=c.position.clone().sub(ct);ct.set(3.6,0,4.6);c.position.copy(ct).add(d);c.zoom=1.5;c.updateProjectionMatrix();window.__ctl.update();window.__tick();});
const tick=async(n=3)=>{for(let i=0;i<n;i++){await p.evaluate(()=>window.__tick());}};
const S=async(x,z)=>await p.evaluate(([x,z])=>window.__scr(x,.035,z),[x,z]);
await p.click('#tSeed');await p.waitForTimeout(500);await p.screenshot({path:'tt_fan.png'});
await p.click('.fk[data-k="cai"]');await tick();
// drag zigzag over C2 [3.6,5.45,6.2,6.25]
let pts=[];for(let i=0;i<=10;i++){const x=3.7+i*0.24; for(const z of [5.6,5.85,6.1]) pts.push([x,z]);}
const a=await S(3.7,5.6);await p.mouse.move(a[0],a[1]);await p.mouse.down();
for(let i=0;i<=12;i++){const x=3.7+i*0.2;const z=i%2?5.6:6.1;const s=await S(x,z);await p.mouse.move(s[0],s[1],{steps:4});if(i==5){await tick(2);await p.screenshot({path:'tt_sow.png'});}}
for(let i=0;i<=12;i++){const x=6.1-i*0.2;const s=await S(x,5.85);await p.mouse.move(s[0],s[1],{steps:3});}
await p.mouse.up();await tick(5);await p.waitForTimeout(300);await p.screenshot({path:'tt_sowed.png'});
console.log(await p.evaluate(()=>JSON.stringify(window.__g.ST.plots.C2)));
// water B1 [1.0,4.15,3.5,4.95]
await p.click('#tCan');await tick();
const w=await S(1.5,4.5);await p.mouse.move(w[0],w[1]);await p.mouse.down();
for(let i=0;i<20;i++){const s=await S(1.3+i*.1,4.5+Math.sin(i)*.2);await p.mouse.move(s[0],s[1],{steps:2});await p.evaluate(()=>window.__tick());}
await p.screenshot({path:'tt_water.png'});await p.mouse.up();
console.log('B1',await p.evaluate(()=>JSON.stringify([window.__g.ST.plots.B1.moist,window.__g.ST.can])));
// refill at ditch M1 z 3.6..4.15
const r=await S(2,3.88);await p.mouse.move(r[0],r[1]);await p.mouse.down();for(let i=0;i<30;i++){await p.evaluate(()=>window.__tick());}await p.mouse.up();
console.log('can',await p.evaluate(()=>window.__g.ST.can));
// cut A2 (cachua ripe) & B2 (cai ripe): A2 [3.6,2.8,6.2,3.6], B2 [3.6,4.15,6.2,4.95]
await p.click('#tCut');await tick();
const c0=await S(4.8,3.2);await p.mouse.move(c0[0],c0[1]);await p.mouse.down();const c1=await S(4.9,4.5);await p.mouse.move(c1[0],c1[1],{steps:10});await tick(3);await p.screenshot({path:'tt_cut.png'});await p.mouse.up();
console.log('inv',await p.evaluate(()=>JSON.stringify(window.__g.ST.inv)));
await b.close();})();
