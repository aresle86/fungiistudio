const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b'],fg:{cai:1},xu:900,inv:{rom:1,raumuong:3},seeds:{},lu:0,gt:9000,real:Date.now()-5*3600*1000,spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:5,xp:300,qd:{3:1,4:1,5:1},plots:{}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){const p=await b.newPage({viewport:{width:w,height:h},isMobile:tag==='m',hasTouch:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(1500);
await p.evaluate(()=>{const g=window.__g;g.ST.qd[6]=1;window.__x.levelUp(6);});await p.waitForTimeout(800);await p.screenshot({path:`qc2/lv6_${tag}_a.png`,timeout:120000});
await p.evaluate(()=>{const c=document.querySelector('#lvup .btn, [data-a=lvok], .lvok');c&&c.click();});await p.waitForTimeout(4000);await p.evaluate(()=>{window.__stop=true;});await p.waitForTimeout(300);
await p.screenshot({path:`qc2/lv6_${tag}_b.png`,timeout:120000});console.log(tag,errs,await p.evaluate(()=>document.getElementById('ngoaiTxt').textContent));await p.close();}
await b.close();})();
