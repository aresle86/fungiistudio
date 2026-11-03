const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:760}});p.on('pageerror',e=>console.log('ERR',e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});
const r=await p.evaluate(()=>{window.__stop=true;const g=window.__g,X=window.__x,S=g.ST,out={};
 // QC-01
 S.inv.cai=58; const nB2=X.harvestN(S.plots.B2); out.q01_before={free:X.kCap()-X.kUsed(),n:nB2}; const ok=X.act.harvest('B2'); out.q01={ok, crop:S.plots.B2.crop, cai:S.inv.cai};
 S.inv.cai=0; out.q01b={ok:X.act.harvest('B2'), crop:S.plots.B2.crop, cai:S.inv.cai};
 // QC-05/04: ripe A2 dry 10h; growing B1 dry 10h
 S.plots.A2.moist=0; S.plots.B1.moist=0; g.sim(36000); out.q05={A2:X.condOf(S.plots.A2), A2dead:S.plots.A2.dead, B1:X.condOf(S.plots.B1), B1dead:S.plots.B1.dead, B1wilt:Math.round(S.plots.B1.wiltT), B1n:X.harvestN({...S.plots.B1,g:1e9})};
 // QC-02: water via tap and track tasks
 X.ensureTasks(); S.tasks.list=[{t:'water',txt:'Tưới liếp 3 lần',need:3,rw:['coin',5],have:0,done:false}]; S.plots.C1.moist=0.1; X.act.water('C1'); out.q02tap=S.tasks.list[0].have;
 // QC-06: wall clock jump
 const gt0=S.gt; const o=Date.now; Date.now=()=>o()+3600e3; window.__tick(); Date.now=o; out.q06=Math.round(S.gt-gt0);
 // queue
 X.say('A'); X.say('B'); X.say('C'); out.q21=X.SAYQ.map(q=>q[0]);
 return out;});
console.log(JSON.stringify(r,null,1));
// QC-02 drag watering
await p.evaluate(()=>{const g=window.__g;const c=g.cam,ct=window.__ctl.target,d=c.position.clone().sub(ct);ct.set(3.6,0,4.6);c.position.copy(ct).add(d);c.zoom=1.5;c.updateProjectionMatrix();window.__ctl.update();g.ST.plots.B1.moist=0;window.__x.setTool({kind:'water'});window.__tick();});
const S=async(x,z)=>await p.evaluate(([x,z])=>window.__scr(x,.035,z),[x,z]);
const w=await S(1.5,4.5);await p.mouse.move(w[0],w[1]);await p.mouse.down();
for(let i=0;i<40;i++){const s=await S(1.3+(i%10)*.2,4.5);await p.mouse.move(s[0],s[1],{steps:1});await p.evaluate(()=>window.__tick());}
await p.mouse.up();
console.log('drag', await p.evaluate(()=>JSON.stringify({moist:window.__g.ST.plots.B1.moist, have:window.__g.ST.tasks.list[0].have})));
// QC-11 tap sow on C2
await p.evaluate(()=>{window.__x.setTool({kind:'seed',k:'cai'});window.__tick();});
const c2=await S(4.9,5.85);await p.mouse.click(c2[0],c2[1]);await p.evaluate(()=>window.__tick());
console.log('tapsow', await p.evaluate(()=>window.__g.ST.plots.C2.crop));
await p.evaluate(()=>{window.__x.setTool(null);window.__g.ST.inv.cai=6;window.__g.openSheet('cho');});await p.waitForTimeout(300);await p.screenshot({path:'qc_cho.png',timeout:120000});
await b.close();})();
