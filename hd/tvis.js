const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1},xu:500,inv:{rom:1},seeds:{},lu:0,gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'A',garden:'Địa Đàng'},lv:3,xp:40,qd:{2:1},ga:{hens:2,rooster:1,trough:4,eggs:0,acc:0,lv:0,brood:null},plots:{}});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){const p=await b.newPage({viewport:{width:w,height:h},isMobile:tag==='m',hasTouch:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(500);
// tap boat hull
const sc=await p.evaluate(()=>{const g=window.__g;const bt=[...Object.values(g)];const v=new g.T.Vector3(4.1,.2,9.35).project(g.cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];});
await p.mouse.click(sc[0],sc[1]);await p.waitForTimeout(400);console.log(tag,'sheet',await p.evaluate(()=>document.getElementById('shT').textContent+'|'+!document.getElementById('sheet').hidden));
await p.evaluate(()=>window.__g.openSheet('ben'));await p.waitForTimeout(300);await p.screenshot({path:`qc2/v_${tag}_ben.png`,timeout:120000});
await p.evaluate(()=>document.querySelector('[data-a=gomau]').click());await p.waitForTimeout(1500);await p.waitForFunction(()=>window.__ready,null,{timeout:300000}).catch(e=>console.log('ERRS',errs));await p.waitForTimeout(1500);
console.log(tag,'in visit',await p.evaluate(()=>[document.body.classList.contains('visit'),window.__g.ST.lv,!!document.querySelector('.vbar'),document.getElementById('ngoaiTxt').textContent.slice(0,40)]));
// tap a ripe plot A1 and dry C1
for (const id of ['A1','C1','B1b']){const c=await p.evaluate(id=>{const g=window.__g,v=g.PV[id];const q=new g.T.Vector3(v.cx,.1,v.cz).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];},id);await p.mouse.click(c[0],c[1]);await p.waitForTimeout(400);}
console.log(tag,'after taps',await p.evaluate(()=>[document.getElementById('vInfo').textContent,document.getElementById('ngoaiTxt').textContent.slice(0,80)]));
console.log(tag,'img',await p.evaluate(()=>{const i=document.getElementById('ngoaiImg'),r=i.getBoundingClientRect(),cs=getComputedStyle(i);return [r.x,r.y,r.width,r.height,cs.opacity,cs.transform,i.complete,i.naturalWidth,i.src.length,cs.animationName]}));await p.waitForTimeout(1500);await p.screenshot({path:`qc2/v_${tag}_visit.png`,timeout:120000});
await p.evaluate(()=>document.getElementById('vHome').click());await p.waitForTimeout(1500);await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(2500);
console.log(tag,'home',await p.evaluate(()=>[document.body.classList.contains('visit'),JSON.stringify(window.__g.ST.inv),window.__g.ST.xp,JSON.stringify(window.__g.ST.mau),document.getElementById('ngoaiTxt').textContent.slice(0,90),window.__g.ST.lv]));
console.log(tag,'errs',errs.join('|'));await p.close();}
await b.close();})();
