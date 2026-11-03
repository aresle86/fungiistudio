const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b'],fg:{cai:1,ot:1},xu:900,inv:{rom:1,ot:9},seeds:{},lu:0,gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:7,xp:460,qd:{3:1,4:1,5:1,6:1,7:1},plots:{}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){const p=await b.newPage({viewport:{width:w,height:h},isMobile:tag==='m',hasTouch:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning')errs.push(m.text())});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(1200);await p.evaluate(()=>{const ST=window.__g.ST;for(let i=1;i<=12;i++)ST.land['H'+i]={st:'own'};for(const P of window.__x.PLOTS)window.__g.refreshPlot(P.id);});
const tick=async(n=3)=>{await p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await p.waitForTimeout(150);};
const tap=async(x,y)=>{if(tag==='m')await p.touchscreen.tap(x,y);else await p.mouse.click(x,y);await p.waitForTimeout(250);await tick();};
const scr=async(id)=>p.evaluate(id=>{const g=window.__g,v=g.PV[id];const q=new g.T.Vector3(v.cx,.05,v.cz).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];},id);
const sua=await p.evaluate(()=>{const b=document.getElementById('bSua');return [b.hidden,b.getBoundingClientRect().top|0]});
await p.evaluate(()=>{document.getElementById('bSua').click();});await p.waitForTimeout(1500);await p.evaluate(()=>{window.__stop=true;});await tick(30);
await p.screenshot({path:`qc2/bai_${tag}_1.png`,timeout:120000});
let c=await scr('H1');await tap(c[0],c[1]);const t1=await p.evaluate(()=>[document.getElementById('shT').textContent,document.getElementById('sheet').hidden]);
await p.evaluate(()=>document.querySelector('[data-a=openbed]').click());await tick();
c=await scr('H2');await tap(c[0],c[1]);await p.evaluate(()=>document.querySelector('[data-a=openbed]').click());await tick();
await p.waitForTimeout(1200);await tick(30);console.log(tag,'tool',await p.evaluate(()=>JSON.stringify(window.__T.TOOL)));await p.evaluate(()=>{try{window.__T.putAway()}catch(e){}});await p.evaluate(()=>{window.__ev=[];for(const t of ['pointerdown','pointerup','pointercancel','click'])addEventListener(t,e=>window.__ev.push(t+':'+(e.target.id||e.target.className||e.target.tagName)+':'+e.pointerType+':'+e.isPrimary),true);});await p.evaluate(()=>{const g=window.__g,v=g.PV.H3,c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(v.cx,.3,v.cz);c.object.position.copy(c.target).add(d);c.update();});await tick(5);c=await scr('H4');console.log(tag,'pre',JSON.stringify(await p.evaluate(c=>{const el=document.elementFromPoint(c[0],c[1]);const cv=document.querySelector('canvas');return [el&&(el.tagName+'#'+el.id+'.'+el.className),getComputedStyle(cv).pointerEvents,document.body.className,innerWidth,innerHeight,c]},c)));await tap(c[0],c[1]);console.log(tag,'ev',await p.evaluate(()=>window.__ev.join(' ')));console.log(tag,'ph',JSON.stringify(await p.evaluate(c=>{const X=window.__x2,o={};for(const k in X){try{o[k]=X[k](c[0],c[1])}catch(e){o[k]='E'}}return o},c)));console.log(tag,'afterH4',await p.evaluate(()=>[document.getElementById('sheet').hidden,document.getElementById('shT').textContent,document.querySelector('.ngoai')&&document.querySelector('.ngoai').getBoundingClientRect().top|0]));if(await p.evaluate(()=>document.getElementById('sheet').hidden)){await tap(c[0],c[1]);}await p.evaluate(()=>document.querySelector('[data-a=obuy][data-k=nong]').click());await p.waitForTimeout(900);await tick(20);
const st1=await p.evaluate(()=>JSON.stringify([window.__g.ST.open.filter(i=>i[0]=='H'),window.__g.ST.nong.at,window.__g.ST.xu]));
console.log(tag,'st1',st1,await scr('H4'));console.log(tag,'hit',await p.evaluate(()=>{const g=window.__g,v=g.PV.H4,q=new g.T.Vector3(v.cx,.05,v.cz).project(g.cam);const x=(q.x+1)/2*innerWidth,y=(1-q.y)/2*innerHeight;const el=document.elementFromPoint(x,y);return [el&&(el.id||el.className),window.__x.PL.H4.b]}));c=await scr('H4');await tap(c[0],c[1]);const t2=await p.evaluate(()=>document.getElementById('shT').textContent);
console.log(tag,'t2',t2);await p.evaluate(()=>{const q=document.querySelector('[data-a=oopen]');q&&q.click();});await tick();
await p.evaluate(()=>{document.querySelector('[data-a=npick][data-n="0"]').click();document.querySelector('[data-a=nput][data-k=otkho][data-n="0"]').click();});await tick();
await p.evaluate(()=>{document.querySelector('[data-a=npick][data-n="1"]').click();document.querySelector('[data-a=nput][data-k=otkho][data-n="1"]').click();});await tick();
await p.evaluate(()=>{window.__g.sim(25);});await tick(5);
const st2=await p.evaluate(()=>JSON.stringify([window.__g.ST.nong.trays,window.__g.ST.inv.ot,document.getElementById('shT').textContent]));
await p.evaluate(()=>window.__g.closeSheet());await tick(5);
await p.screenshot({path:`qc2/bai_${tag}_2.png`,timeout:120000});
// dời nong
await p.evaluate(()=>{window.__g.openSheet('nong');document.querySelector('[data-a=omove]').click();});await tick(20);c=await scr('H8');await tap(c[0],c[1]);
const st3=await p.evaluate(()=>JSON.stringify([window.__g.ST.nong.at,document.getElementById('ngoaiTxt').textContent]));
// lấy ớt khô qua bubble
await p.evaluate(()=>{document.getElementById('suaOk').click();});await tick(10);
const nb=await p.evaluate(()=>{const g=window.__g,v=g.PV['H8'];const q=new g.T.Vector3(v.cx,.62,v.cz).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];});await tap(nb[0],nb[1]);
const st4=await p.evaluate(()=>JSON.stringify([window.__g.ST.gb,window.__g.ST.nong.done,document.getElementById('shT').textContent]));
console.log(tag,sua,t1,st1,t2,st2,st3,st4,errs);await p.close();}
await b.close();})();
