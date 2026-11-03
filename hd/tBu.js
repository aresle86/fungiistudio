const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:600},deviceScaleFactor:1});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_bu.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ddt,.ngoai,.nxq,.ui,.top,#tray,.nava,.bt{display:none!important}'});
await p.evaluate(()=>{const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=12;g.ST.seen.hello=1;window.__stop=true;
 const U=window.__BU;U.BUV.t=0;for(let i=0;i<40;i++){window.__tick();}
 for(let i=0;i<8;i++){U.BUV.t=0;U.buTick(performance.now()/1000,.016);} });
const n=await p.evaluate(()=>window.__BU.BUV.list.length);console.log('bu',n);
// quỹ đạo 12 giây của 1 con, mô phỏng dt cố định
const tr=await p.evaluate(()=>{const U=window.__BU,b=U.BUV.list[0],out=[];let t=100;for(let i=0;i<720;i++){t+=1/60;for(const x of U.BUV.list)x.life=99;U.buTick(t,1/60);if(i%6===0)out.push([+b.m.position.x.toFixed(3),+b.m.position.y.toFixed(3),+b.m.position.z.toFixed(3),b.rest>0?1:0]);}return {out,sc:b.m.scale.x};});
require('fs').writeFileSync('../bu_path.json',JSON.stringify(tr));
// khung hình cận một con để soi cỡ so với liếp
const T0=await p.evaluate(()=>{const b=window.__BU.BUV.list[0];return [b.m.position.x,b.m.position.z];});
await p.evaluate(([x,z])=>{const c=window.__ctl;c.maxZoom=40;const d=c.object.position.clone().sub(c.target);c.target.set(x,.2,z);c.object.position.copy(c.target).add(d);c.object.zoom=7;c.object.updateProjectionMatrix();},T0);
let t=200;for(let f=0;f<24;f++){await p.evaluate(tt=>{const U=window.__BU;for(const x of U.BUV.list)x.life=99;for(let i=0;i<3;i++){U.buTick(tt+i/60,1/60);}const b=U.BUV.list[0],c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(b.m.position.x,.2,b.m.position.z);c.object.position.copy(c.target).add(d);window.__r&&0;},t);t+=3/60;
 await p.evaluate(()=>{window.__g.cam.updateMatrixWorld();window.__tick();});await p.screenshot({path:`../buf${String(f).padStart(2,'0')}.png`,timeout:300000});}
console.log(errs.join('\n')||'no errors');await b.close();})();
