const {chromium}=require('playwright');(async()=>{const [,,out]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.9,cut:0});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},JSON.stringify({v:1,eco:2,xu:300,inv:{rom:3,cai:40,hanh:19},seeds:{},gt:9000,real:Date.now(),spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1},player:{av:0,name:'A',garden:'B'},lv:4,xp:200,qd:{2:1,4:1},exp:1,split:1,
 plots:{A1:pl('cai',1800,.8),A1b:pl('cai',1800,.8)}}));
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;window.__g.closeSheet();window.__g.say&&0;});const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(150);};await tick();
const scr=async(x,z)=>p.evaluate(([x,z])=>{const v=new window.__g.T.Vector3(x,.1,z).project(window.__g.cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];},[x,z]);
await p.evaluate(()=>{window.__g.ST.inv.cai=41;});await tick();await p.screenshot({path:out+'_full.png'});
await p.mouse.click(...await scr(1.4,3.2));await p.waitForTimeout(700);await tick();
console.log('after tap', await p.evaluate(()=>({sheet:document.getElementById('shT').textContent,open:!document.getElementById('sheet').hidden,inv:window.__g.ST.inv,badge:document.querySelector('#bCho .kb')?.textContent})));
await p.screenshot({path:out+'_cho.png'});
await p.click('[data-a=buylu]');await tick();console.log('lu',await p.evaluate(()=>[window.__g.ST.lu,window.__g.ST.xu]));
await p.evaluate(()=>window.__g.closeSheet());await p.mouse.click(...await scr(1.4,3.2));await tick();console.log('harvest now',await p.evaluate(()=>[window.__g.ST.plots.A1.crop,window.__g.ST.inv.cai]));
console.log(errs.join('\n'));await b.close();})();
