// chụp toàn bộ màn HUD/sheet để rà soát thiết kế: node tHud.js → ../hud/<pc|ph>_<tên>.png
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud',{recursive:true});
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{oi:6,chuoi:4,cai:6},gb:{cui:4},seeds:{cai:3},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},fishLog:{caro:{n:1}},land:{H1:{st:'own'},H2:{st:'own'}},nong:{own:1,at:'H2',trays:[null,null,null,null],done:3,made:{}},ga:{hens:4,rooster:1,trough:4,eggs:0,acc:0,lv:1,brood:null,fixed:1},
 tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
const STEPS=[
 ['hud',()=>{}],
 ['ring',()=>{const id=Object.keys(window.__G.PLOTS||{})[0]||window.__x.PLOTS[0].id;window.__G.openRing(id,'seed')}],
 ['sheet_plot',()=>{window.__G.closeRing&&window.__G.closeRing();const id=window.__x.PLOTS[0].id;window.__x.openSheet('plot',id)}],
 ['sheet_cho',()=>window.__x.openSheet('cho')],
 ['sheet_ga',()=>window.__x.openSheet('ga')],
 ['sheet_set',()=>window.__x.openSheet('set')],
 ['sheet_ao',()=>window.__x.openSheet('big','ao')],
 ['sheet_nong',()=>window.__x.openSheet('nong')],
 ['book_viec',()=>window.__w.openBook('viec')],
 ['book_kho',()=>window.__w.openBook('kho')],
 ['book_giong',()=>window.__w.openBook('giong')],
 ['book_cotich',()=>window.__w.openBook('cotich')],
 ['daily',()=>{window.__w.closeBook();window.__DDS('')}],
 ['lvup',()=>{document.querySelectorAll('.ddt').forEach(e=>e.remove());window.__w.lvCelebrate(16)}],
];
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(180000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/mv2_t107.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(2500);
 await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});});
 for(const [n,f] of STEPS){try{await p.evaluate(f);}catch(e){console.log(tag,n,'ERR',e.message.slice(0,80));}await p.waitForTimeout(700);await p.screenshot({path:`../hud/${tag}_${n}.png`});
  try{await p.evaluate(()=>{const x=document.getElementById('shX');if(x&&!document.getElementById('sheet').hidden)x.click();});}catch(e){}}
 await p.close();}
console.log('hud shots done');await b.close();})();
