const {chromium}=require('playwright');(async()=>{const [,,out]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},JSON.stringify({v:1,eco:2,xu:1000,inv:{rom:3,bap:2},seeds:{},gt:9000,real:Date.now()-7*3600e3,spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1},player:{av:0,name:'A',garden:'B'},lv:5,xp:330,qd:{2:1,4:1,5:1},exp:1,split:1,plots:{}}));
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;window.__g.closeSheet();});const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(150);};
const G=()=>p.evaluate(()=>JSON.stringify({ga:window.__g.ST.ga,inv:window.__g.ST.inv,xu:window.__g.ST.xu}));
console.log('after 7h away',await G());
await p.evaluate(()=>{const c=window.__g.cam,x=window.__x;window.__ctl.target.set(-.4,.4,4);c.position.set(9.6,8.56,14);c.zoom=2.4;c.updateProjectionMatrix();c.lookAt(-.4,.4,4);});await tick();await p.screenshot({path:out+'_coop.png'});
const scr=async(v)=>p.evaluate(v=>{const q=new window.__g.T.Vector3(v.x,v.y,v.z).project(window.__g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];},v);
const nb=await p.evaluate(()=>{const b=window.__x.GAV.bubE;return {x:b.position.x,y:b.position.y,z:b.position.z,vis:b.visible};});console.log('egg bubble',JSON.stringify(nb));
if(nb.vis){await p.mouse.click(...await scr(nb));await tick();console.log('tap egg bubble',await G());}
await p.evaluate(()=>{window.__g.ST.ga.trough=0;});await tick();
const fb=await p.evaluate(()=>{const b=window.__x.GAV.bubF;return {x:b.position.x,y:b.position.y,z:b.position.z,vis:b.visible};});console.log('feed bubble',JSON.stringify(fb));
await p.screenshot({path:out+'_hungry.png'});
if(fb.vis){await p.mouse.click(...await scr(fb));await tick();console.log('tap feed',await G());}
await p.mouse.click(...await scr({x:-.75,y:.6,z:3.6}));await tick();await p.screenshot({path:out+'_sheet.png'});
console.log('sheet',await p.evaluate(()=>document.getElementById('shT').textContent));
await p.click('[data-a=gabuy]');await p.click('[data-a=gahatch]').catch(()=>{});await tick();console.log('buy+hatch',await G());
await p.evaluate(()=>{window.__g.sim(23*3600);});await tick();console.log('after 23h',await G());
await p.evaluate(()=>window.__g.openSheet('cho'));await tick();await p.screenshot({path:out+'_cho.png'});
console.log(errs.join('\n'));await b.close();})();
