const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for (const [w,h,tag] of [[1280,800,'d'],[390,844,'m']]){
const p=await b.newPage({viewport:{width:w,height:h}});p.on('pageerror',e=>console.log('ERR',e.message));await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:240000});await p.evaluate(()=>{window.__stop=true;});await p.waitForTimeout(800);
await p.click('.avc[data-i="4"]');await p.fill('#inGarden','Vườn Cái Bè');await p.screenshot({path:`av_${tag}_intro.png`,timeout:120000});
await p.click('#inGo');await p.waitForTimeout(600);await p.evaluate(()=>{const g=window.__g;g.ST.realTime=false;g.ST.ovr=10;window.__tick();window.__tick();});await p.screenshot({path:`av_${tag}_hud.png`,timeout:120000});
if(tag==='d'){await p.evaluate(()=>{const g=window.__g,c=g.cam,ct=window.__ctl.target,d=c.position.clone().sub(ct);ct.set(6.3,.3,2.6);c.position.copy(ct).add(d);c.zoom=2.6;c.updateProjectionMatrix();window.__ctl.update();window.__tick();});await p.screenshot({path:'av_world.png',timeout:120000});}
await p.close();}
await b.close();})();
