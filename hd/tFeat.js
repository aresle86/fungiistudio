const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:640},deviceScaleFactor:1.5});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b','H1','H2'],xu:3000,inv:{},seeds:{},gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:10,xp:2600,qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1},plots:{},nong:{own:1,at:'H1',trays:[]},vit:{n:6,trough:6,eggs:2,acc:0,lv:0,fixed:1},ga:{fixed:1,hens:2,rooster:1,trough:4,eggs:0,lv:0}});
await p.addInitScript(s=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup').forEach(e=>e.remove());window.__stop=true;for(let i=0;i<10;i++)window.__tick();});
const L=await p.evaluate(()=>JSON.stringify(window.__g.ST.tasks.list.map(x=>[x.t,x.k||'',x.txt])));console.log('tasks lv10',L);
await p.evaluate(()=>window.__OB('viec'));await p.waitForTimeout(800);await p.screenshot({path:'../feat1.png',timeout:300000});await p.evaluate(()=>{const c=document.querySelector('[data-b=close]');if(c)c.click();});
// chuồng vịt 3 bậc
const shots=[];for(const lv of [0,1,2]){await p.evaluate(lv=>{const g=window.__g;g.ST.vit.lv=lv;const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-.35,.25,6.45);c.object.position.copy(c.target).add(d);c.maxZoom=40;c.object.zoom=5;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();},lv);await p.screenshot({path:'../vit'+lv+'.png',timeout:300000});}
console.log(errs.join('\n')||'no errors');await b.close();})();
