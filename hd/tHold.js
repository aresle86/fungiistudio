const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:430,height:860},deviceScaleFactor:2,hasTouch:false});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_fh.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=9;g.ST.xp=1400;g.ST.tm='fixed';g.ST.ovr=10;});
const cam=async(x,y,z,zm)=>p.evaluate(([x,y,z,zm])=>{const c=window.__ctl;c.maxZoom=40;const d=c.object.position.clone().sub(c.target);c.target.set(x,y,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();},[x,y,z,zm]);
const shot=async n=>{};
await p.evaluate(()=>{for(let i=0;i<3;i++)window.__tick();});
await cam(1.6,.1,9.5,9);await shot('fx_shadow');
await cam(2.1,.35,9.6,3.2);await shot('fx_bub');
await p.evaluate(()=>{window.__FT3.fmEnter();for(let i=0;i<20;i++)window.__tick();});await p.waitForTimeout(900);await p.evaluate(()=>{for(let i=0;i<3;i++)window.__tick();});await shot('fx_aim');
await p.click('.fact[data-f=cast]',{force:true});console.log('cast',await p.evaluate(()=>{const F=window.__FT3.FM;return JSON.stringify([F.bob,F.tgt&&F.tgt.m.position,F.tgt===F.tutF,F.tutF&&F.tutF.m.position])}));
const seen={};const t0=Date.now();
while(Date.now()-t0<40000){const ph=await p.evaluate(()=>{window.__tick();return window.__FT3.FM.ph;});
 if(!seen[ph]){seen[ph]=1;console.log('ph',ph,await p.evaluate(()=>{const F=window.__FT3.FM;return F.tgt?Math.hypot(F.tgt.m.position.x-F.bob.x,F.tgt.m.position.z-F.bob.z).toFixed(3):'-'}),((Date.now()-t0)/1000).toFixed(1));if(['come','wait','nibble','bite'].includes(ph)){await p.waitForTimeout(250);await p.evaluate(()=>window.__tick());await shot('fx_'+ph);}}
 if(ph==='bite'){await p.waitForTimeout(300);await p.click('.fact[data-f=giut]',{force:true});}
 if(ph==='reel'){const L=[];for(let i=0;i<40;i++){L.push(await p.evaluate(()=>{window.__tick();const F=window.__FT3.FM;return [F.ph,F.hold,+F.ten.toFixed(2)];}));}console.log('no-press',JSON.stringify([L[0],L[10],L[39]]));await p.mouse.move(215,300);await p.mouse.down();const L2=[];for(let i=0;i<20;i++)L2.push(await p.evaluate(()=>{window.__tick();const F=window.__FT3.FM;return [F.hold,+F.ten.toFixed(2)];}));await p.mouse.up();const L3=[];for(let i=0;i<20;i++)L3.push(await p.evaluate(()=>{window.__tick();const F=window.__FT3.FM;return [F.hold,+F.ten.toFixed(2)];}));console.log('press',JSON.stringify([L2[0],L2[19]]),'release',JSON.stringify([L3[0],L3[19]]));await p.mouse.move(215,300);await p.mouse.down();for(let i=0;i<400;i++){const r=await p.evaluate(()=>{window.__tick();const F=window.__FT3.FM;return [F.ph,F.ten,F.prog];});if(i===15)await shot('fx_reel');if(r[0]!=='reel'){console.log('end',r);break;} if(r[1]>.7){await p.mouse.up();for(let k=0;k<10;k++)await p.evaluate(()=>window.__tick());await p.mouse.down();}}
  await p.mouse.up();await p.waitForTimeout(400);await shot('fx_catch');break;}
 await p.waitForTimeout(30);}
console.log(await p.evaluate(()=>JSON.stringify([window.__g.ST.seen.cauTut,window.__FT3.FM.tut,Object.keys(window.__g.ST.fishLog)])));
console.log(errs.join('\n'));await b.close();})();
