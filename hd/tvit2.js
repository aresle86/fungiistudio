const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b'],fg:{cai:1},xu:900,inv:{rom:1,raumuong:3},seeds:{},lu:0,gt:9000,real:Date.now()-5*3600*1000,spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:6,xp:320,qd:{3:1,4:1,5:1,6:1},plots:{},vit:{n:2,trough:4,eggs:0,acc:0,lv:0}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m2']]){const p=await b.newPage({viewport:{width:w,height:h},isMobile:tag==='m2',hasTouch:tag==='m2',deviceScaleFactor:tag==='d'?2:1});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning'&&/^odd/.test(m.text()))errs.push(m.text())});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(800);await p.evaluate(()=>{window.__stop=true;});
const tick=async(n=3)=>{await p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await p.waitForTimeout(150);};await tick();
const st=await p.evaluate(()=>JSON.stringify(window.__g.ST.vit));
const sc=await p.evaluate(()=>{const g=window.__g;const v=new g.T.Vector3(-.35,.3,6.45).project(g.cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];});
if(tag==='d') await p.screenshot({path:'qc2/vit_d2.png',clip:{x:Math.max(0,sc[0]-200),y:Math.max(0,sc[1]-160),width:400,height:300},timeout:120000});
if(tag==='m2')await p.touchscreen.tap(sc[0],sc[1]);else await p.mouse.click(sc[0],sc[1]);await tick();await p.waitForTimeout(400);const sh=await p.evaluate(()=>document.getElementById('shT').textContent);
await p.evaluate(()=>{const q=s=>document.querySelector(s);if(!q('[data-a=vitfeed]'))return;q('[data-a=viteggs]')&&document.querySelector('[data-a=viteggs]').click();document.querySelector('[data-a=vitfeed]').click();document.querySelector('[data-a=vitbuy]').click();});await tick();
console.log(tag,st,sc.map(Math.round),sh,await p.evaluate(()=>JSON.stringify([window.__g.ST.vit,window.__g.ST.inv,window.__g.ST.xu])),errs);
if(tag==='m2') await p.screenshot({path:'qc2/vit_m.png',timeout:120000});await p.close();}
await b.close();})();
