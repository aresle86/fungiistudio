// v110b ghé vườn: thẻ việc ẩn, chỉ còn bình tưới có số liếp tưới giùm được; bấm bình tưới = tưới giùm 1 liếp, được 1 công
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud11',{recursive:true});const PAGE=process.env.PAGE||'mv2_t110b.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const ME={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:12,xp:7500,xu:900,inv:{},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:10},(_, i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
let bad=0;const ok=(c,m)=>{console.log((c?'OK ':'SAI ')+m);if(!c)bad++;};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['ph',{width:390,height:664}],['pc',{width:1280,height:800}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>{const m=r.request().url().match(/rpc\/(mv2_\w+)/);if(!m)return r.abort();return r.fulfill({status:200,contentType:'application/json',body:JSON.stringify(m[1]==='mv2_act'?{ok:true,left:4}:null)});});
 await p.addInitScript(([me])=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',me);localStorage.setItem('mv2-cloud',JSON.stringify({code:'MV-MEME',secret:'ABCDEFGHIJKL'}));
  const st=JSON.parse(me);st.player={av:2,name:'Tư',garden:'vườn giàu nhất xóm'};st.lv=16;sessionStorage.setItem('mv2-visit',JSON.stringify({kind:'ban',code:'MV-TUTU',owner:'Tư',name:'vườn giàu nhất xóm',myLv:12,left:5,cong:0,state:st,loot:{inv:{},xp:0,water:0,friend:'Tư',giftOut:[]}}));},[JSON.stringify(ME)]);
 await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});
 await p.evaluate(()=>{const g=window.__g||{},ST=window.__O.ST;let n=0;for(const P of window.__G.PLOTS){const q=ST.plots[P.id];if(q&&!P.tree&&!P.trellis&&n<3){q.crop='cai';q.g=10;q.moist=.4;n++;}}window.__w.hud();});await p.waitForTimeout(2500);
 const r=await p.evaluate(()=>{const q=document.getElementById('nxq'),can=document.getElementById('tCan');return {nxq:getComputedStyle(q).display,can:can&&getComputedStyle(can).display!=='none'&&!can.hidden,n:document.getElementById('tCanN').textContent};});
 ok(r.nxq==='none','thẻ việc ẩn khi ghé vườn');ok(r.can&&+r.n>=1,'bình tưới hiện, số liếp tưới giùm được: '+r.n);
 await p.screenshot({path:`../hud11/${tag}_visit_b.png`});
 const c=await p.evaluate(async()=>{const V=window.__V.VISIT,c0=V.cong||0;document.getElementById('tCan').click();await new Promise(r=>setTimeout(r,1500));return [c0,V.cong||0];});
 ok(c[1]===c[0]+1,'bấm bình tưới = tưới giùm 1 liếp, +1 công ('+c+')');
 ok(!errs.length,'không lỗi trang '+errs.join(' | '));await p.close();}
console.log(bad?'XONG · '+bad+' SAI':'XONG · tất cả đúng');await b.close();})();
