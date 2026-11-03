const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1},xu:1391,inv:{rom:3,trungga:3},seeds:{cai:2,hanh:1},lu:0,gt:9000,real:Date.now(),spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Ares',garden:'Địa Đàng'},lv:3,xp:60,qd:{2:1},ga:{hens:2,rooster:1,trough:2,eggs:0,acc:0,lv:0,brood:null},plots:{}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){const p=await b.newPage({viewport:{width:w,height:h},hasTouch:tag==='m',isMobile:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;});const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(300);};
await tick();
console.log(tag,'G want',await p.evaluate(()=>window.__g.PV.G.want));
await p.evaluate(()=>{window.__g.closeSheet();document.getElementById('tSeed').click();window.__g.say('Trứng gà ta đem chợ bán được giá lắm. Để dành một trứng, mai mốt ấp ra gà con.','vui',{now:true});});await tick();await p.waitForTimeout(400);
await p.screenshot({path:`qc2/f_${tag}_bar.png`});
const ov=await p.evaluate(()=>{const a=document.querySelector('#ngoai p').getBoundingClientRect(),b=document.getElementById('fan').getBoundingClientRect();return [Math.round(a.bottom),Math.round(b.top),a.right>b.left&&a.left<b.right]});console.log(tag,'ngoai bottom/fan top/xoverlap',ov, await p.evaluate(()=>[document.getElementById('ngoai').style.transform,getComputedStyle(document.getElementById('ngoai')).transform,getComputedStyle(document.getElementById('ngoai')).position]));
await p.screenshot({path:`qc2/f_${tag}_hud.png`,clip:{x:0,y:0,width:w,height:140}});
console.log(tag,errs.join('|'));await p.close();}
await b.close();})();
