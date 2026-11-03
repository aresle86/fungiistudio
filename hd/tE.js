const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b','H1','H2'],fg:{cai:1,ot:1},xu:2000,inv:{rom:1,cai:9,cachua:4,ot:3,trungvit:9},gb:{cui:4,muoi:2},seeds:{},lu:0,gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:9,xp:850,qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1},plots:{},vit:{n:3,trough:6,eggs:0,acc:0,lv:0}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){const p=await b.newPage({viewport:{width:w,height:h},isMobile:tag==='m',hasTouch:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning')errs.push(m.text())});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(1200);
const tick=async(n=3)=>{await p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await p.waitForTimeout(120);};
const tap=async(x,y)=>{if(tag==='m')await p.touchscreen.tap(x,y);else await p.mouse.click(x,y);await p.waitForTimeout(250);await tick();};
const prj=async(x,y,z)=>p.evaluate(([x,y,z])=>{const g=window.__g;const q=new g.T.Vector3(x,y,z).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];},[x,y,z]);
const out={};
// khạp + hố
await p.evaluate(()=>{window.__e.buyObj('khap');window.__e.buyObj('ho');});await tick(5);
out.obj=await p.evaluate(()=>[window.__g.ST.khap.at,window.__g.ST.ho.at,window.__g.ST.xu]);
await p.evaluate(()=>{window.__g.openSheet('khap');document.querySelector('[data-a=kput][data-k=dacai][data-n="0"]').click();document.querySelector('[data-a=kput][data-k=hotvit][data-n="1"]').click();});await tick();
await p.evaluate(()=>{window.__g.sim(40);});await tick(3);
let kc=await p.evaluate(()=>{const v=window.__e.PV[window.__g.ST.khap.at];return [v.cx,v.cz]});let c=await prj(kc[0],.7,kc[1]);await tap(c[0],c[1]);
out.khap=await p.evaluate(()=>JSON.stringify([window.__g.ST.khap.jars,window.__g.ST.gb,document.getElementById('shT').textContent]));
// hố: rau dư x6 → ủ 60s → bón
await p.evaluate(()=>{window.__g.closeSheet();window.__g.openSheet('ho');for(let i=0;i<6;i++)document.querySelector('[data-a=horau]').click();});await tick();
await p.evaluate(()=>{window.__g.sim(70);});await tick(3);
out.ho1=await p.evaluate(()=>JSON.stringify(window.__g.ST.ho));
await p.evaluate(()=>{window.__g.ST.plots.A1.soil=.3;window.__g.openSheet('ho');document.querySelector('[data-a=hobon]').click();});await tick();
out.ho2=await p.evaluate(()=>JSON.stringify([window.__g.ST.ho.bags,window.__g.ST.plots.A1.soil]));
// lò ấp
await p.evaluate(()=>window.__g.closeSheet());let lc=await prj(-1.45,.35,6.3);await tap(lc[0],lc[1]);out.lo0=await p.evaluate(()=>document.getElementById('shT').textContent);
await p.evaluate(()=>{const q=document.querySelector('[data-a=loput]');q&&q.click();window.__g.sim(70);});await tick(3);
await p.evaluate(()=>window.__g.closeSheet());await tap(lc[0],lc[1]);out.lo=await p.evaluate(()=>JSON.stringify([window.__g.ST.lo,window.__g.ST.vit.n,window.__g.ST.xu]));
// câu cá
await p.evaluate(()=>window.__g.closeSheet());let rc=await prj(2.6-.7,.75,8.35+1.6);
await p.evaluate(()=>{window.__g.camTo&&0;});
await tap(rc[0],rc[1]);out.c1=await p.evaluate(()=>JSON.stringify(window.__e.CST));
await p.evaluate(()=>{window.__e.CST={st:'bite',t:1.5};});await tick(2);
await p.screenshot({path:`qc2/E_${tag}_cau.png`,timeout:120000});
const pc=await p.evaluate(()=>{const r=window.__e.CAUV.rest;const g=window.__g;const q=new g.T.Vector3(r.x,.45,r.z).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];});await tap(pc[0],pc[1]);
out.c2=await p.evaluate(()=>JSON.stringify([window.__e.CST,window.__g.ST.inv.caro||0,window.__g.ST.inv.caloc||0,window.__g.ST.cau]));
// mé sông
await p.evaluate(()=>{window.__g.openSheet('plot','S1');document.querySelector('[data-a=openbed]').click();});await tick();
out.song=await p.evaluate(()=>JSON.stringify([window.__g.ST.open.filter(i=>i[0]=='S'),window.__g.ST.plots.S1.soil]));
await p.evaluate(()=>{window.__e.doQuest(10);});await tick(3);await p.evaluate(()=>window.__g.closeSheet());
const sc=await prj(7.95,.1,7.5);await p.evaluate(([x,y])=>0,sc);
await p.screenshot({path:`qc2/E_${tag}_song.png`,timeout:120000});
console.log(tag,JSON.stringify(out),errs);await p.close();}
await b.close();})();
