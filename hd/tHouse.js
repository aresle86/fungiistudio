const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:760}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const setup=async add=>{await p.evaluate(add=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g;g.ST.tm='fixed';g.ST.ovr=10;g.ST.player={av:1,name:'N',garden:'V'};g.ST.mai={t:0,done:1};
 if(add){const h=window.__FT3.houseUp(add);h.position.set(2.4,0,.35);window.__S.add(h);}
 for(let i=0;i<4;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(2.6,.6,1.6);c.object.position.copy(c.target).add(d);c.object.zoom=2.3;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();},add);};
await setup(false);await p.screenshot({path:'../house0.png',timeout:120000}).catch(()=>console.log('f0'));
await setup(1);await p.screenshot({path:'../house1.png',timeout:120000}).catch(()=>console.log('f1'));await p.reload();await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await setup(3);await p.screenshot({path:'../house3.png',timeout:120000}).catch(()=>console.log('f3'));
console.log(errs);await b.close();})();
