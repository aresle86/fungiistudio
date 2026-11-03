const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.5,cut:0});
const save=JSON.stringify({v:1,eco:2,split:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b'],fg:{cai:1,hanh:1},xu:500,inv:{rom:1,hanh:4,trungga:4,bap:2},seeds:{},gb:{cui:2},lu:0,gt:9000,real:Date.now(),spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Ares',garden:'Địa Đàng'},lv:4,xp:90,qd:{2:1,4:1},ga:{hens:2,rooster:1,trough:4,eggs:0,acc:0,lv:0,brood:null},plots:{}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){
const p=await b.newPage({viewport:{width:w,height:h},hasTouch:tag==='m',isMobile:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning'&&m.text().startsWith('odd'))errs.push(m.text())});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});await p.waitForTimeout(800);
await p.evaluate(()=>{window.__stop=true;});const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(250);};await tick();
const Q=()=>p.evaluate(()=>{const S=window.__g.ST;return JSON.stringify({bep:S.bep,gb:S.gb,inv:S.inv,xu:S.xu,sheet:document.getElementById('shT').textContent})});
// tap the hut
const sc=await p.evaluate(()=>{const g=window.__g;const v=new g.T.Vector3(5.15,.5,.05).project(g.cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];});
await p.mouse.click(sc[0],sc[1]);await tick();console.log(tag,'tap hut',await Q());
await p.screenshot({path:`qc2/b_${tag}_lock.png`,timeout:120000});
await p.evaluate(()=>{window.__g.ST.gb.cui=3;window.__g.openSheet('bep');});await tick();
await p.evaluate(()=>document.querySelector('[data-a=bplite]').click());await tick();
await p.evaluate(()=>{document.querySelector('[data-a=bpick]').click();document.querySelector('[data-a=bpcook][data-k=trungchien]').click();});await tick();
await p.evaluate(()=>{window.__g.ST.gb.cui=(window.__g.ST.gb.cui||0)+2;window.__g.openSheet('bep');document.querySelector('[data-a=bpick]').click();document.querySelector('[data-a=bpcook][data-k=bapluoc]').click();});await tick();
console.log(tag,'cooking',await Q());await p.screenshot({path:`qc2/b_${tag}_cook.png`,timeout:120000});
await p.evaluate(()=>{window.__g.sim(16*60);window.__g.closeSheet();});await tick();await p.waitForTimeout(300);
await tick();await p.waitForTimeout(500);await tick();await p.screenshot({path:`qc2/b_${tag}_ready.png`,timeout:120000});
await p.mouse.click(sc[0],sc[1]);await tick();console.log(tag,'collect',await Q());
await p.evaluate(()=>window.__g.openSheet('cho'));await tick();await p.screenshot({path:`qc2/b_${tag}_cho.png`,timeout:120000});
console.log(tag,'errs',errs.join('|'));await p.close();}
await b.close();})();
