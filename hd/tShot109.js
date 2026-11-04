// chụp v109: gà nằm ổ ngoài vườn, bảng chuồng gà lúc ấp / lúc báo kết quả, đơn nhà bên, lò ấp vịt. node tShot109.js
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud9',{recursive:true});
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{trungvit:8,cai:6,hanh:4},gb:{cui:6},seeds:{cai:3},plots:{},
 qd:Object.fromEntries(Array.from({length:14},(_, i)=>[i+3,1])),land:{H1:{st:'own'}},open:['H1'],nong:{own:1,at:'H1',trays:[null,null],done:2,made:{otkho:1}},khap:{own:1,at:'H1',jars:[null,null],done:1,made:{dacai:1,hotvit:1}},bep:{lit:0,pots:[null,null],made:{}},
 ga:{hens:4,rooster:1,trough:8,eggs:2,acc:0,lv:1,brood:{stage:'egg',t:3*3600,n:4},fixed:1},vit:{n:4,trough:8,eggs:0,acc:0,lv:1,fixed:1},lo:{t:6*3600,T:18*3600,on:1,n:4,done:1,hatch:0,lon:1},
 tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['ph',{width:390,height:664}],['pc',{width:1280,height:800}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/mv2_t109.html',{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(2500);
 await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});const N=window.__x.NEST;window.__e.camTo(N,3.2);});await p.waitForTimeout(2600);
 await p.screenshot({path:`../hud9/${tag}_o_ga.png`});
 const step=async(n,f)=>{await p.evaluate(f);await p.waitForTimeout(700);await p.screenshot({path:`../hud9/${tag}_${n}.png`});await p.evaluate(()=>{const x=document.getElementById('shX');if(x&&!document.getElementById('sheet').hidden)x.click();});await p.waitForTimeout(300);};
 await step('ga_ap',()=>window.__x.openSheet('ga'));
 await step('ga_kq',()=>{const g=window.__O.ST.ga;g.brood={stage:'chick',t:2*3600,n:4,c:3};g.res={n:4,c:3,mai:2,trong:0,giong:1,ban:0,xu:0};window.__x.openSheet('ga');});
 await step('o_con',()=>{window.__x.openSheet('ga');window.__e.closeSheet();});
 await step('don',()=>{const O=window.__O;O.ST.ord={list:[O.ordMake(),O.ordMake(),O.ordMake()],acc:0,first:1};window.__x.openSheet('cho');});
 await step('lo',()=>window.__x.openSheet('lo'));
 console.log(tag,'errors',errs.length,errs.slice(0,2));await p.close();}
console.log('shots 109 done');await b.close();})();
