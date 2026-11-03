const {chromium}=require('playwright');(async()=>{const [,,out]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for (const [w,h,tag] of [[1200,780,'d'],[390,780,'m']]){const p=await b.newPage({viewport:{width:w,height:h},hasTouch:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',JSON.stringify({v:1,eco:2,xu:180,inv:{rom:3,cai:17,cachua:12,khoqua:8,hanh:9,bap:8},seeds:{cai:2,hanh:1,ot:0},gt:9000,real:Date.now(),spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1},player:{av:0,name:'A',garden:'B'},lv:4,xp:130,qd:{2:1,4:1},exp:1,plots:{C2:{crop:null,g:0,moist:.5,dry:0,mulch:0,soil:.9,cut:0}}}));}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;});const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(250);};
await p.evaluate(()=>window.__g.openSheet('cho'));await tick();await p.screenshot({path:`${out}_${tag}_cho.png`});
await p.click('[data-a=sell1][data-k=cai]');await p.waitForTimeout(150);await tick();await p.screenshot({path:`${out}_${tag}_cho2.png`});
console.log(tag,'after sell1',JSON.stringify(await p.evaluate(()=>[window.__g.ST.inv.cai,window.__g.ST.xu])));
await p.click('[data-a=sellall][data-k=cachua]');await p.waitForTimeout(100);console.log(tag,'after sellall',JSON.stringify(await p.evaluate(()=>[window.__g.ST.inv.cachua,window.__g.ST.xu,document.querySelectorAll('.srow').length])));
await p.evaluate(()=>window.__g.closeSheet());
await p.click('#tSeed');await tick();await p.screenshot({path:`${out}_${tag}_bar.png`});
// long-press tip
const sk=await p.$('.sk[data-k=ot]');const bb=await sk.boundingBox();await p.mouse.move(bb.x+bb.width/2,bb.y+bb.height/2);await p.mouse.down();await p.waitForTimeout(600);await p.screenshot({path:`${out}_${tag}_tip.png`});await p.mouse.up();
console.log(tag,'tip-no-select',JSON.stringify(await p.evaluate(()=>[document.querySelector('.sk.on')?.dataset.k||null, window.__g.ST.xu])));
// tap cai to select
await p.click('.sk[data-k=cai]');await tick();await p.screenshot({path:`${out}_${tag}_sel.png`});
console.log(tag,'sel',JSON.stringify(await p.evaluate(()=>[document.querySelector('.sk.on')?.dataset.k||null, !document.getElementById('fan').hidden, document.getElementById('sbTx').textContent])));
// tap ot (0 bao) -> buy
await p.click('.sk[data-k=ot]');await p.waitForTimeout(100);console.log(tag,'buy ot',JSON.stringify(await p.evaluate(()=>[window.__g.ST.seeds.ot, window.__g.ST.xu, document.querySelector('.sk.on')?.dataset.k])));
console.log(errs.join('\n'));await p.close();}
await b.close();})();
