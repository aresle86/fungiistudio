const {chromium}=require('playwright');(async()=>{const [,,out]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:780}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',JSON.stringify({v:1,eco:2,xu:180,inv:{rom:3},seeds:{cai:2,hanh:1},gt:9000,real:Date.now(),spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1},player:{av:0,name:'A',garden:'B'},lv:4,xp:130,qd:{2:1,4:1},exp:1,plots:{C2:{crop:null,g:0,moist:.5,dry:0,mulch:0,soil:.9,cut:0},C1:{crop:null,g:0,moist:.5,dry:0,mulch:0,soil:.9,cut:0}}}));}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;});const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(150);};
const scr=async(x,z)=>p.evaluate(([x,z])=>{const v=new window.__g.T.Vector3(x,.12,z).project(window.__g.cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];},[x,z]);
await tick();await p.click('#tSeed');await p.click('.sk[data-k=cai]');
const a=await scr(3.7,5.85),c=await scr(6.1,5.85),a2=await scr(3.7,5.6),c2=await scr(6.1,6.1);
await p.mouse.move(...a);await p.mouse.down();for(let i=0;i<=20;i++){await p.mouse.move(a[0]+(c[0]-a[0])*i/20,a[1]+(c[1]-a[1])*i/20);}
await tick();await p.screenshot({path:out+'_mid.png'});
for(let i=0;i<=20;i++){await p.mouse.move(c2[0]+(a2[0]-c2[0])*i/20,c2[1]+(a2[1]-c2[1])*i/20);} for(let i=0;i<=20;i++){await p.mouse.move(a2[0]+(c2[0]-a2[0])*i/20,a2[1]+(c2[1]-a2[1])*i/20+20);}
await p.mouse.up();await tick();await p.screenshot({path:out+'_done.png'});
console.log(JSON.stringify(await p.evaluate(()=>[window.__g.ST.plots.C2.crop,window.__g.ST.seeds.cai,document.querySelector('.sk.on')?.dataset.k,!document.getElementById('fan').hidden])));
const g=await scr(10.5,2.5);console.log('pt',g, await p.evaluate(([x,y])=>{const e=document.elementFromPoint(x,y);return e.tagName+'#'+e.id+'.'+e.className;},g));await p.mouse.click(...g);await tick();
console.log('after ground tap',JSON.stringify(await p.evaluate(()=>[!document.getElementById('fan').hidden, !!document.querySelector('.tl.on')])));
console.log(errs.join('\n'));await b.close();})();
