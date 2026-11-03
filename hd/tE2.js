const {chromium}=require('playwright');const fs=require('fs');const L=m=>fs.appendFileSync('tE2.log',m+'\n');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b','H1','H2'],fg:{cai:1,ot:1},xu:2000,inv:{rom:1,cai:9,cachua:4,ot:3,trungvit:9},gb:{cui:4,muoi:2},seeds:{},lu:0,gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:9,xp:850,qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1},plots:{},vit:{n:3,trough:6,eggs:0,acc:0,lv:0},khap:{own:1,at:'H3',jars:[{k:'dacai',t:0,T:30,fast:true},null],done:0,made:{}},ho:{own:1,at:'H4',mat:2,t:0,bags:1,done:1}});
for (const [w,h,tag] of [[900,600,'d'],[390,844,'m']]){const p=await b.newPage({viewport:{width:w,height:h},isMobile:tag==='m',hasTouch:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning')errs.push(m.text())});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(1000);await p.evaluate(()=>{window.__stop=true;});
const tick=async(n=3)=>{await p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await p.waitForTimeout(100);};
const tap=async(x,y)=>{if(tag==='m')await p.touchscreen.tap(x,y);else await p.mouse.click(x,y);await p.waitForTimeout(200);await tick(2);};
const prj=async(x,y,z)=>p.evaluate(([x,y,z])=>{const g=window.__g;const q=new g.T.Vector3(x,y,z).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];},[x,y,z]);
const go=async(x,z)=>{await p.evaluate(([x,z])=>{const e=window.__e;e.closeSheet();e.camTo(new window.__g.T.Vector3(x,.3,z),1.3);},[x,z]);await p.waitForTimeout(50);for(let i=0;i<8;i++){await p.evaluate(()=>{const t0=performance.now();window.__tick();});await p.waitForTimeout(90);}};
const shot=async n=>p.screenshot({path:`qc2/E_${tag}_${n}.png`,timeout:240000});
// khạp bubble
let kc=await p.evaluate(()=>{const v=window.__e.PV['H3'];return [v.cx,v.cz]});await go(kc[0],kc[1]);await shot('bai');let c=await prj(kc[0],.7,kc[1]);await tap(c[0],c[1]);
L(tag+' khap '+await p.evaluate(()=>JSON.stringify([window.__g.ST.khap.jars,window.__g.ST.gb,document.getElementById('sheet').hidden?'':document.getElementById('shT').textContent])));
// lò ấp
await go(-1.45,6.3);await shot('lo');c=await prj(-1.45,.35,6.3);await tap(c[0],c[1]);L(tag+' lo0 '+await p.evaluate(()=>document.getElementById('sheet').hidden?'-':document.getElementById('shT').textContent));
await p.evaluate(()=>{const q=document.querySelector('[data-a=loput]');q&&q.click();window.__g.sim(70);});await tick(2);await go(-1.45,6.3);c=await prj(-1.45,.35,6.3);await tap(c[0],c[1]);
L(tag+' lo '+await p.evaluate(()=>JSON.stringify([window.__g.ST.lo,window.__g.ST.vit.n,window.__g.ST.xu])));
// câu cá
await go(1.9,9.6);await shot('ben');c=await prj(2.6-.7,.75,8.35+1.6);await tap(c[0],c[1]);L(tag+' c1 '+await p.evaluate(()=>JSON.stringify(window.__e.CST)));
await p.evaluate(()=>{window.__e.CST={st:'bite',t:5};});await tick(2);await shot('cau');
c=await p.evaluate(()=>{const r=window.__e.CAUV.rest;const g=window.__g;const q=new g.T.Vector3(r.x,.45,r.z).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];});await tap(c[0],c[1]);
L(tag+' c2 '+await p.evaluate(()=>JSON.stringify([window.__e.CST,window.__g.ST.inv.caro||0,window.__g.ST.inv.caloc||0,window.__g.ST.cau])));
// mé sông
await go(7.9,7.4);await p.evaluate(()=>{window.__g.openSheet('plot','S2');document.querySelector('[data-a=openbed]').click();window.__e.doQuest(10);});await tick(3);await go(7.9,7.4);await shot('song');
L(tag+' song '+await p.evaluate(()=>JSON.stringify([window.__g.ST.open.filter(i=>i[0]=='S'),window.__g.ST.plots.S2.soil,window.__g.ST.qd[10],window.__g.ST.xu])));
L(tag+' errs '+JSON.stringify(errs));await p.close();}
await b.close();L('END');})().catch(e=>{L('FAIL '+e.message.slice(0,300));process.exit(1)});
