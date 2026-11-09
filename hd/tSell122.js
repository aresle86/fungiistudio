const {chromium}=require('playwright');const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SV={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1,sap1:1,don1:1},player:{av:1,name:'Q',garden:'Q'},lv:8,xp:3000,xu:500,inv:{cai:30,hanh:20,ot:18},gb:{},seeds:{},plots:{},qd:{3:1,4:1,5:1,6:1,7:1},realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0},ftrD:today};
(async()=>{const b=await chromium.launch({args:['--use-angle=metal','--enable-gpu','--ignore-gpu-blocklist']});
const ctx=await b.newContext({viewport:{width:390,height:844},deviceScaleFactor:3,isMobile:true,hasTouch:true});const p=await ctx.newPage();p.setDefaultTimeout(200000);
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(s=>{localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SV));
await p.goto('http://127.0.0.1:8777/'+process.argv[2]);await p.waitForFunction('window.__ready');await p.waitForTimeout(3000);
if(process.argv[3])await p.addStyleTag({content:process.argv[3]});await p.evaluate(()=>{window.__g.openSheet('cho');});await p.waitForTimeout(300);await p.evaluate(()=>{const t=[...document.querySelectorAll('[data-a=ctab]')].find(x=>x.dataset.k==='ban');t&&t.click()});await p.waitForTimeout(500);
await p.evaluate(()=>{window.__T=[];const sh=document.querySelector('[data-a=sell1]').closest('.sheet,#sheet')||document.body;sh.addEventListener('click',e=>{if(e.target.closest('[data-a=sell1]')){const t0=performance.now();setTimeout(()=>window.__T.push(performance.now()-t0),0)}},true)});
const inv0=await p.evaluate(()=>window.__g.ST.inv.cai);
for(let i=0;i<10;i++){const bx=await p.evaluate(()=>{const e=document.querySelector('[data-a=sell1][data-k=cai]').getBoundingClientRect();return [e.x+e.width/2,e.y+e.height/2]});await p.touchscreen.tap(bx[0],bx[1]);await p.waitForTimeout(150);}
await p.waitForTimeout(500);const inv1=await p.evaluate(()=>window.__g.ST.inv.cai);
const pf=await p.evaluate(()=>{const t0=performance.now();document.querySelector('[data-a=sell1][data-k=cai]').click();return performance.now()-t0});
console.log('10 lần chạm cách 150ms: bán được',inv0-inv1,'| 1 lần bấm tốn',pf.toFixed(1),'ms');
const sz=await p.evaluate(()=>localStorage.getItem('mv2-state').length);console.log('save size',sz);
await b.close();})();
