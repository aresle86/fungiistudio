// chụp Sổ thật của v110c (không chèn CSS): tab Việc, Kho, Sưu tập trên máy tính + điện thoại
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud13',{recursive:true});const PAGE=process.env.PAGE||'mv2_t110c.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:12,xp:7600,xu:3000,inv:{oi:6,cai:6,trungga:4},gb:{cui:4,muoi:2},seeds:{cai:3},plots:{},qd:Object.fromEntries(Array.from({length:10},(_, i)=>[i+3,1])),fishLog:{caro:{n:1}},tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(1500);
 await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});});
 for(const tab of ['viec','kho','giong']){await p.evaluate(t=>window.__w.openBook(t),tab);await p.waitForTimeout(800);await p.screenshot({path:`../hud13/${tag}_${tab}.png`});}
 console.log(tag,'errors',errs.length,errs.slice(0,2));await p.close();}
await b.close();})();
