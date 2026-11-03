const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.9,cut:0});
for (const [away,tag] of [[3*3600,'3h'],[2*86400,'2d'],[60,'1m']]){
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1},xu:1391,inv:{rom:3},seeds:{cai:2},lu:0,gt:9000,real:Date.now()-away*1000,spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Ares',garden:'Địa Đàng'},lv:3,xp:60,qd:{2:1},ga:{hens:2,rooster:1,trough:6,eggs:0,acc:0,lv:0,brood:null},plots:{A1:pl('cai',100,.9),A2:pl('hanh',100,.9),B1:pl(null,0,.5)}});
const p=await b.newPage({viewport:{width:1280,height:800}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});await p.waitForTimeout(2500);
console.log(tag,await p.evaluate(()=>({sheet:!document.getElementById('sheet').hidden,ng:document.getElementById('ngoai').hidden?'':document.getElementById('ngoaiTxt').textContent})),errs.join('|'));
await p.close();}
await b.close();})();
