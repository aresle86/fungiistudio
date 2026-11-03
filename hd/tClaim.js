const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:844},deviceScaleFactor:2,isMobile:true,hasTouch:true});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_claim.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const out={};
await p.evaluate(()=>{const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=6;g.ST.seen.hello=1;g.ST.dd={n:1,d:new Date().toDateString(),last:Date.now()};document.querySelectorAll('.ddt').forEach(e=>e.remove());window.__stop=true;for(let i=0;i<10;i++)window.__tick();
 const T=g.ST.tasks;T.list.forEach((x,i)=>{if(i<3){x.have=x.need;x.done=true;x.cl=false;}});});
out.xu0=await p.evaluate(()=>window.__g.ST.xu);out.badge=await p.evaluate(()=>{const d=document.querySelector('#bSo .kb');return d?[d.textContent,d.className]:null;});
await p.evaluate(()=>window.__OB('viec'));await p.waitForTimeout(800);await p.screenshot({path:'../cl1.png',timeout:300000});
out.btns=await p.evaluate(()=>[document.querySelectorAll('.tkcl').length,!!document.querySelector('.tkall')]);
await p.evaluate(()=>document.querySelector('.tkcl').click());await p.waitForTimeout(300);await p.screenshot({path:'../cl2.png',timeout:300000});await p.waitForTimeout(1500);
out.xu1=await p.evaluate(()=>window.__g.ST.xu);
await p.evaluate(()=>{const a=document.querySelector('.tkall');if(a)a.click();});await p.waitForTimeout(2500);out.xu2=await p.evaluate(()=>window.__g.ST.xu);
// xong hết -> túi quà
await p.evaluate(()=>{const g=window.__g;g.ST.tasks.list.forEach(x=>{if(!x.done){x.have=x.need-1;}});for(const x of g.ST.tasks.list)if(!x.done){window.__BUMP&&0;}});
await p.evaluate(()=>{const T=window.__g.ST.tasks;T.list.forEach(x=>{x.done=true;if(x.cl===undefined)x.cl=true;});T.gr=1;window.__OB('viec');});await p.waitForTimeout(800);await p.screenshot({path:'../cl3.png',timeout:300000});
const s0=await p.evaluate(()=>{const g=window.__g;return g.ST.seeds[g.ST.tasks.bonus]||0;});await p.evaluate(()=>document.querySelector('.tkcl.gift').click());await p.waitForTimeout(1500);out.gift=[s0,await p.evaluate(()=>{const g=window.__g;return [g.ST.seeds[g.ST.tasks.bonus]||0,g.ST.tasks.got];})];
await p.evaluate(()=>window.__OB('giong'));await p.waitForTimeout(1200);await p.screenshot({path:'../cl4.png',timeout:300000});
console.log(JSON.stringify(out));console.log(errs.join('\n')||'no errors');await b.close();})();
