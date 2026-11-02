const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:620}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=9;g.ST.tm='fixed';g.ST.ovr=10;for(let i=0;i<3;i++)window.__tick();});
const shot=async(n,ph,ten,off,zm)=>{await p.evaluate(([ph,ten,off,zm])=>{const X=window.__FT3,F=X.FM,C=X.CAUV;F.on=ph!=='idle';F.ph=ph;F.ten=ten;F.vung=1;F.t=0;for(let i=0;i<40;i++)X.rodBend(1,.05);F.on=false;C.b.visible=false;
 const pos=C.line.geometry.attributes.position;C.ph.visible=true;C.line.visible=true;C.ph.position.copy(C.rest);if(ph==='bite')C.ph.position.y-=.05;pos.setXYZ(0,C.tip.x,C.tip.y,C.tip.z);pos.setXYZ(1,C.ph.position.x,C.ph.position.y+.1,C.ph.position.z);pos.needsUpdate=true;
 const c=window.__ctl;c.maxZoom=40;const T=c.target.constructor;c.target.set(2.05,.3,9.62);c.object.position.copy(c.target).add(new T(...off));c.object.lookAt(c.target);c.object.zoom=zm;c.object.updateProjectionMatrix();window.__r.render(window.__S,c.object);},[ph,ten,off,zm]);
 await p.screenshot({path:'../'+n+'.png',timeout:120000}).catch(()=>console.log('f',n));};
for(const [n,ph,ten] of [['bIdle','idle',0],['bBite','bite',0],['bReel','reel',1]]){await shot(n,ph,ten,[10,8.16,10],7.5);await shot(n+'S',ph,ten,[0,1,30],7.5);}
console.log(errs.join('\n')||'no errors');await b.close();})();
