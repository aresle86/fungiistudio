// v110e: lưới Sổ giống — tên và thông số mỗi hàng thẳng nhau (VI, EN điện thoại, EN máy tính)
const {chromium}=require('playwright');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:12,xp:7600,xu:3000,inv:{},gb:{},seeds:{cai:3},plots:{},qd:Object.fromEntries(Array.from({length:10},(_, i)=>[i+3,1])),tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
let bad=0;
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [page,lang,vw] of [['mv2_t110e.html','vi',{width:390,height:664}],['mv2_t110e.html','vi_pc',{width:1280,height:800}],['mv2_t111.html','en',{width:390,height:664}],['mv2_t111.html','en_pc',{width:1280,height:800}]]){const p=await b.newPage({viewport:vw,deviceScaleFactor:vw.width<500?2:1.25});p.setDefaultTimeout(300000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(([s,l])=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-lang',l.slice(0,2));localStorage.setItem('mv2-state',s)},[JSON.stringify(SAVE),lang]);
 await p.goto('http://127.0.0.1:8777/'+page,{waitUntil:'domcontentloaded',timeout:300000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(1200);
 await p.evaluate(()=>window.__w.openBook('giong'));await p.waitForTimeout(800);
 const r=await p.evaluate(()=>{const rows={};for(const k of document.querySelectorAll('.stk')){if(!k.querySelector('.sts')||!k.querySelector('b'))continue;const y=Math.round(k.getBoundingClientRect().top);const b=Math.round(k.querySelector('b').getBoundingClientRect().top),st=Math.round(k.querySelector('.sts').getBoundingClientRect().top);(rows[y]=rows[y]||[]).push([b,st]);}return Object.values(rows).map(a=>new Set(a.map(x=>x.join())).size===1);});
 const ok=r.every(Boolean);if(!ok)bad++;console.log((ok?'OK ':'SAI ')+lang+' '+JSON.stringify(r));await p.screenshot({path:'../hud14/giong_'+lang+'.png'});await p.close();}
console.log(bad?'XONG · '+bad+' SAI':'XONG · tất cả đúng');await b.close()})();
