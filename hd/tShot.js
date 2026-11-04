// chụp vườn (máy tính + điện thoại) của một trang test để so bằng mắt: PAGE=mv2_t107d.html OUT=../shot_d node tShot.js
const {chromium}=require('playwright');
const PAGE=process.env.PAGE||'mv2_t107.html',OUT=process.env.OUT||'../shot';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{},gb:{},seeds:{},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'},H4:{st:'own'}},open:['H1'],
 nong:{own:1,at:'H2',trays:[null,null,null,null],done:3,made:{}},khap:{own:1,at:'H3',jars:[null,null],done:2,made:{}},ga:{hens:4,rooster:1,trough:4,eggs:0,acc:0,lv:1,brood:null,fixed:1},vit:{n:6,trough:8,eggs:0,acc:0,lv:1,fixed:1},
 tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:1,hasTouch:tag==='ph'});p.setDefaultTimeout(180000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+PAGE+'?dev',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(2500);
 await p.evaluate(()=>{window.__stop=true;document.querySelectorAll('.ddt,.lvup,#intro,#nxq,.ngoai').forEach(e=>{e.hidden=true});});await p.waitForTimeout(300);
 await p.screenshot({path:`${OUT}_${tag}.png`});await p.close();}
console.log('ok');await b.close();})();
