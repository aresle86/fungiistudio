const {chromium}=require('playwright');(async()=>{const [,,out]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.9,cut:0});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},JSON.stringify({v:1,eco:2,xu:100,inv:{rom:3,cai:25,bap:6},seeds:{cai:2},gt:9000,real:Date.now(),spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1},player:{av:0,name:'A',garden:'B'},lv:7,xp:470,qd:{2:1,4:1,5:1,6:1},exp:1,
 plots:{A1:pl('bap',14400,.8),A2:pl('cachua',14400,.8),B1:pl('ot',10800,.8),B2:pl('mongtoi',5400,.8),C1:pl('daubap',9000,.8),C2:pl('cai',1800,.8),G:pl('khoqua',10800,1),D1:pl('hanh',2700,.8)}}));
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;window.__g.closeSheet();});const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(150);};
await tick();await p.screenshot({path:out+'_beds.png'});
await p.evaluate(()=>window.__g.openSheet('cho'));await tick();
console.log(await p.evaluate(()=>document.querySelector('.srow').innerText.replace(/\n/g,' | ')));
await p.click('[data-a=sellall][data-k=cai]');await tick();console.log('xu after sell 25 cai',await p.evaluate(()=>window.__g.ST.xu));
await p.evaluate(()=>{window.__g.ST.inv.cai=5;window.__g.openSheet('cho');});await tick();await p.screenshot({path:out+'_cho.png'});
console.log(await p.evaluate(()=>document.querySelector('.srow').innerText.replace(/\n/g,' | ')));
console.log(errs.join('\n'));await b.close();})();
