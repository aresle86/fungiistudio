const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.9,cut:0});
const save=JSON.stringify({v:1,eco:2,split:1,open:['A1','A1b','A2','B1','B1b','B2'],fg:{cai:1,hanh:1},xu:120,inv:{rom:1},seeds:{cai:1,hanh:1},lu:0,gt:9000,real:Date.now(),spd:1,ovr:20.5,realTime:false,seen:{hello:1,firstwater:1,sell:1,sold:1,gaintro:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:1,xp:4,qd:{},plots:{A1:pl('cai',100,.9),A2:pl('hanh',100,.9)}});
const p=await b.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(800);
await p.evaluate(()=>{window.__stop=true;});const tick=async(n=3)=>{await p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await p.waitForTimeout(150);};await tick();
await p.screenshot({path:'qc2/dr0.png',timeout:120000});
await p.evaluate(()=>document.getElementById('tSeed').click());for(let i=0;i<30;i++)await tick(1);  // camera glide
await p.screenshot({path:'qc2/dr1.png',timeout:120000});
const card=await p.evaluate(()=>{const r=document.querySelector('.sk[data-k=cai]').getBoundingClientRect();return [r.x+r.width/2,r.y+r.height/2]});
const bed=await p.evaluate(()=>{const g=window.__g,v=g.PV.B1;const q=new g.T.Vector3(v.cx,.05,v.cz).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];});
console.log('card',card,'bed B1',bed);
// touch drag via CDP
const c=await p.context().newCDPSession(p);const T=(type,x,y)=>c.send('Input.dispatchTouchEvent',{type,touchPoints:type==='touchEnd'?[]:[{x,y}]});
await T('touchStart',card[0],card[1]);const tgt=[bed[0],bed[1]+38];
for(let i=1;i<=14;i++){await T('touchMove',card[0]+(tgt[0]-card[0])*i/14,card[1]+(tgt[1]-card[1])*i/14);await tick(1);}
await p.waitForTimeout(250);await T('touchMove',tgt[0]+2,tgt[1]);await tick(1);
await p.screenshot({path:'qc2/dr2.png',timeout:120000});
await T('touchEnd');await tick(3);
console.log('after',await p.evaluate(()=>{const S=window.__g.ST;return JSON.stringify({B1:S.plots.B1.crop,B1b:S.plots.B1b.crop,B2:S.plots.B2.crop,A1b:S.plots.A1b.crop,seeds:S.seeds,ng:document.getElementById('ngoaiTxt').textContent})}),errs);
await p.screenshot({path:'qc2/dr3.png',timeout:120000});await b.close();})();
