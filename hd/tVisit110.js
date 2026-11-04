// chụp màn ghé vườn bạn (máy tính, iPad, điện thoại) để soát bảng/thẻ trên cùng. node tVisit110.js
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud11',{recursive:true});const PAGE=process.env.PAGE||'mv2_live110.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const ME={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:12,xp:7500,xu:900,inv:{},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:10},(_, i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ipad',{width:1160,height:820}],['ph',{width:390,height:664}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag!=='pc'});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>{const m=r.request().url().match(/rpc\/(mv2_\w+)/);if(!m)return r.abort();return r.fulfill({status:200,contentType:'application/json',body:JSON.stringify(m[1]==='mv2_act'?{ok:true,left:4}:null)});});
 await p.addInitScript(([me])=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',me);localStorage.setItem('mv2-cloud',JSON.stringify({code:'MV-MEME',secret:'ABCDEFGHIJKL'}));
  const st=JSON.parse(me);st.player={av:2,name:'Tư',garden:'vườn giàu nhất xóm'};st.lv=16;sessionStorage.setItem('mv2-visit',JSON.stringify({kind:'ban',code:'MV-TUTU',owner:'Tư',name:'vườn giàu nhất xóm',myLv:12,left:5,cong:0,state:st,loot:{inv:{},xp:0,water:0,friend:'Tư',giftOut:[]}}));},[JSON.stringify(ME)]);
 await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(2500);
 await p.screenshot({path:`../hud11/${tag}_visit.png`});
 const info=await p.evaluate(()=>{const q=document.getElementById('nxq');const r=q&&q.getBoundingClientRect();return {nxqHidden:q&&q.hidden,nxqDisp:q&&getComputedStyle(q).display,nxqH:r&&Math.round(r.height),vbar:[...document.querySelectorAll('.vbar')].filter(e=>!e.hidden).map(e=>{const r=e.getBoundingClientRect();return [e.className,Math.round(r.left),Math.round(r.right),Math.round(r.top),innerWidth]})};});
 console.log(tag,JSON.stringify(info),errs.slice(0,2));await p.close();}
await b.close();})();
