const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:620}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ddt,.ngoai,.ui,#tray,.nxq,#bCtr{display:none!important}'});
await p.evaluate(()=>{window.__stop=true;const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=6;g.ST.tm='fixed';g.ST.ovr=10;window.__FT3.placeAvatar();for(let i=0;i<60;i++)window.__tick();});
const shot=async(n,off,zm)=>{await p.evaluate(([off,zm])=>{const c=window.__ctl;c.maxZoom=40;const T=c.target.constructor;c.target.set(2.27,.15,2.0);c.object.position.copy(c.target).add(new T(...off));c.object.lookAt(c.target);c.object.zoom=zm;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();},[off,zm]);await p.screenshot({path:'../'+n+'.png',timeout:120000});};
await shot('sitA',[10,8.16,10],9);await shot('sitSide',[30,1.5,0],12);await shot('sitFront',[2,3,30],10);
console.log(errs.join('|')||'no errors');await b.close();})();
