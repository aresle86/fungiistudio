const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b','H1','H2'],xu:2000,inv:{},seeds:{},gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1},player:{av:2,name:'Nhu',garden:'Nhà Như'},lv:19,xp:9000,qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1},plots:{}});
const S={garden:'Nhà Như',days:30,harv:86,tree:9,fish:17,cook:23,bu:6,guest:14};
for(const [w,h,tag] of [[1100,760,'d'],[390,844,'m']]){
const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:2,isMobile:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ui,.ngoai,#tray,.top,.nxq,.ddt,.bt,.nava,.lvup{display:none!important}'});
await p.evaluate(()=>{const g=window.__g;for(const id in g.ST.plots){}window.__stop=true;const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(4.5,.3,3.5);c.object.position.copy(c.target).add(d);c.object.zoom=1.5;c.object.updateProjectionMatrix();for(let i=0;i<6;i++)window.__tick();});
await p.waitForTimeout(1500);await p.evaluate(()=>{for(const g of (window.__BUBALL||[]))g.visible=false;document.querySelectorAll('.nava,.pinga').forEach(e=>e.remove());window.__r.render(window.__S,window.__g.cam);});
let photo;
if(tag==='d'){const buf=await p.screenshot({timeout:300000,clip:{x:150,y:120,width:800,height:600}});require('fs').writeFileSync('../recap_photo.png',buf);}
photo='data:image/png;base64,'+require('fs').readFileSync('../recap_photo.png').toString('base64');
await p.addScriptTag({url:'/recap_mock.js'});await p.evaluate(([ph,S])=>window.__recapMock(ph,S),[photo,S]);await p.waitForTimeout(1500);
await p.screenshot({path:`../recap_${tag}.png`,timeout:300000,fullPage:false});
console.log(tag,errs.join('|')||'no errors');await p.close();}
await b.close();})();
