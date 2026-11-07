// tFtShot: chụp cảnh mở cây cổ tích ở từng mốc (giữ đứng thời gian). node tFtShot.js [trang] [cây,...]
const {chromium}=require('playwright');const PAGE=process.argv[2]||'mv2_t116b.html';const KS=(process.argv[3]||'vusua,tretramdot,traucau,duahau,khevang,sodua').split(',');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());const LV={vusua:6,tretramdot:9,traucau:12,duahau:14,khevang:16,sodua:18};
const SV=(lv,x)=>({v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv,xp:80000,xu:50000,inv:{},gb:{},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:Math.max(0,lv-2)},(_,i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:3,full:0},ftrD:today,...x});
const OUT='/tmp/ftshot';require('fs').mkdirSync(OUT,{recursive:true});
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const k of KS){const p=await b.newPage({viewport:{width:600,height:760}});p.setDefaultTimeout(240000);const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
  await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SV(LV[k],{ft:{[k]:{st:0,told:0,t:Date.now(),said:1}}})));
  await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready);await p.waitForTimeout(2500);
  await p.addStyleTag({content:'.ftv,.ngoai,#tstw,.ddt{visibility:hidden!important}'});
  await p.evaluate(k=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>e.hidden=true);window.__hold=T=>{clearInterval(window.__hi);window.__hi=setInterval(()=>{const C=window.__DCX0.get().CERE;if(C)C.t=T;},10)};window.__DCX0.get().ftTap(k);window.__hold(.3)},k);
  for(const T of [1.6,2.6,3.1,3.9]){await p.evaluate(T=>window.__hold(T),T);await p.waitForTimeout(T===1.6?9000:3500);await p.screenshot({path:`${OUT}/${k}_${T}.png`});}
  console.log(k,'ok',errs.length?errs[0]:'');await p.close();}
await b.close();})();
