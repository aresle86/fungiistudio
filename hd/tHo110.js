// v110: hái rau thì gốc rễ vô hố ủ; phân chuồng theo số gà vịt; gà nở có chúc mừng (pháo giấy). PAGE=mv2_t110.html node tHo110.js
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud10',{recursive:true});const PAGE=process.env.PAGE||'mv2_t110.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:13,xp:9300,xu:2000,inv:{},seeds:{},plots:{},
 qd:Object.fromEntries(Array.from({length:11},(_, i)=>[i+3,1])),land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'}},open:[],
 ho:{own:1,at:'H3',mat:0,bags:0,t:0,done:0,pct:Date.now()-13*3600e3},ga:{hens:5,rooster:1,trough:8,eggs:0,acc:0,lv:1,brood:{stage:'egg',t:3600,n:4},fixed:1},vit:{n:4,trough:8,eggs:0,acc:0,lv:1,fixed:1},
 tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
let bad=0;const ok=(c,m)=>{console.log((c?'OK ':'SAI ')+m);if(!c)bad++;};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:664},deviceScaleFactor:2,hasTouch:true});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});
await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});});
const cf=await p.evaluate(async()=>{let n=0;const mo=new MutationObserver(ms=>{for(const m of ms)for(const x of m.addedNodes)if(x.classList&&x.classList.contains('cft'))n++;});mo.observe(document.body,{childList:true,subtree:true});window.__O.gaSim(window.__O.GA.brood);await new Promise(r=>setTimeout(r,2500));mo.disconnect();return [n,JSON.stringify(window.__O.ST.ga.brood)];});
ok(cf[0]>10&&/chick/.test(cf[1]),'gà nở có pháo giấy ('+cf[0]+' mảnh) '+cf[1]);
const ph=await p.evaluate(()=>{const g=window.__g;return g?null:null});
const h=await p.evaluate(()=>{const O=window.__O,ST=O.ST,P=window.__G.PLOTS.find(P=>!P.tree&&!P.trellis&&!P.bai&&ST.plots[P.id]);const q=ST.plots[P.id];q.crop='cai';q.g=O.CROPS.cai.grow+5;q.moist=1;const m0=ST.ho.mat;window.__x.act.harvest(P.id);return [m0,ST.ho.mat];});
ok(h[1]===h[0]+1,'hái rau thì +1 gốc rau vô hố ('+h+')');
await p.screenshot({path:'../hud10/ph_hai.png'});
await p.evaluate(()=>window.__x.openSheet('ho'));await p.waitForTimeout(700);
const t=await p.evaluate(()=>document.getElementById('shB').innerText.replace(/\s+/g,' ').slice(0,300));ok(/3 phần\/6 giờ/.test(t)&&/chờ hốt/.test(t),'phân chuồng theo số con (10 con → 3 phần/6 giờ?): '+t);
await p.screenshot({path:'../hud10/ph_ho.png'});
ok(!errs.length,'không lỗi trang '+errs.join(' | '));console.log(bad?'XONG · '+bad+' SAI':'XONG · tất cả đúng');await b.close();})();
