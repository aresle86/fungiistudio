const {chromium}=require('playwright');(async()=>{const [,,out,W,H]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:+W,height:+H},hasTouch:true,isMobile:true});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
const pl=(crop,g,moist)=>({crop,g,moist,dry:0,mulch:0,soil:.9,cut:0});
await p.addInitScript(s=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}}catch(e){}},JSON.stringify({v:1,eco:2,xu:300,inv:{rom:3},seeds:{cai:2,hanh:1},gt:9000,real:Date.now(),spd:1,realTime:false,ovr:12,seen:{hello:1,firstwater:1,sell:1,sold:1},player:{av:0,name:'A',garden:'B'},lv:4,xp:130,qd:{2:1,4:1},exp:1,
 plots:{A1:pl('cai',1800,.8),A2:pl('cai',1800,.8),B1:pl('hanh',2700,.8),B2:pl('ot',1000,0),C1:pl('bap',2000,0),C2:pl(null,0,.5),G:pl('khoqua',2000,1),D1:pl(null,0,.5)}}));
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;const s=document.getElementById('sheet');window.__g.closeSheet();});
const tick=async()=>{await p.evaluate(()=>{for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(120);};await tick();
const scr=async(x,z)=>p.evaluate(([x,z])=>{const v=new window.__g.T.Vector3(x,.1,z).project(window.__g.cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];},[x,z]);
const S=async()=>p.evaluate(()=>{const s=window.__g.ST;return {A1:s.plots.A1.crop,A2:s.plots.A2.crop,B1:s.plots.B1.cut,B2m:+s.plots.B2.moist.toFixed(2),C1m:+s.plots.C1.moist.toFixed(2),C2:s.plots.C2.crop,D1:s.plots.D1.crop,inv:s.inv,seeds:s.seeds,sheet:!document.getElementById('sheet').hidden,fan:!document.getElementById('fan').hidden,tgt:window.__ctl.target.toArray().map(v=>+v.toFixed(2))};});
const drag=async(pts)=>{await p.mouse.move(...pts[0]);await p.mouse.down();for(let k=1;k<pts.length;k++){const [a,b2]=[pts[k-1],pts[k]];for(let i=1;i<=12;i++)await p.mouse.move(a[0]+(b2[0]-a[0])*i/12,a[1]+(b2[1]-a[1])*i/12);}await p.mouse.up();};
// 1 tap ripe plot body (A1 corner, not bubble)
let a=await scr(1.3,2.95);await p.touchscreen.tap(...a);await tick();console.log('tap A1',JSON.stringify(await S()));
// 2 swipe A2 -> B1 (two ripe)
await drag([await scr(4.0,3.2),await scr(5.5,3.2),await scr(5.5,4.5),await scr(2.0,4.5)]);await tick();console.log('swipe A2,B1',JSON.stringify(await S()));
// 3 water: tap B2 (dry), swipe from C1
await p.mouse.click(...await scr(5.0,4.55));await tick();
await drag([await scr(1.5,5.8),await scr(3.0,5.8)]);await tick();console.log('water',JSON.stringify(await S()));
// 4 tap empty C2 -> bar with PEND, then tap hanh slot
await p.mouse.click(...await scr(4.9,5.85));await tick();await p.screenshot({path:out+'_pend.png'});
await p.click('.sk[data-k=hanh]');await tick();console.log('pend sow',JSON.stringify(await S()));
// 5 drag cai from bar to D1
const sk=await (await p.$('.sk[data-k=cai]')).boundingBox();const d1=await scr(9.3,3.4);await drag([[sk.x+sk.width/2,sk.y+sk.height/2],[sk.x+sk.width/2,sk.y-60],d1]);await tick();console.log('drag D1',JSON.stringify(await S()));
// 6 long-press growing plot G -> sheet; tap outside closes
const gp=await scr(6.6,4.5);await p.keyboard.press('Escape');await p.mouse.move(...gp);await p.mouse.down();await p.waitForTimeout(650);await p.mouse.up();await tick();await p.screenshot({path:out+'_info.png'});console.log('longpress',JSON.stringify(await S()));
await p.mouse.click(30,200);await tick();console.log('outside',JSON.stringify(await S()));
// 7 pan from grass
const t0=await S();await drag([await scr(9,6.5),await scr(7,7.5)]);await tick();console.log('pan',JSON.stringify((await S()).tgt),'was',JSON.stringify(t0.tgt));
await p.screenshot({path:out+'_end.png'});console.log(errs.join('\n'));await b.close();})();
