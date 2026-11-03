const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1400,height:900}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g,ST=g.ST,{fairyModel}=window.__FT;ST.player={av:1,name:'N',garden:'V'};ST.lv=18;ST.tm='fixed';ST.ovr=10;
 ST.ft.vusua={st:4,told:4,t:0};ST.ft.tretramdot={st:3,told:3,t:0};ST.ft.traucau={st:3,told:3,t:0};const S=window.__S;
 for(const k of ['duahau','khevang','sodua'])ST.ft[k]={st:3,told:3,t:0};
 for(let i=0;i<6;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-5.5,.5,6);c.object.position.copy(c.target).add(d);c.object.zoom=1.25;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();window.__r.render(S,g.cam);});
await p.screenshot({path:'../pos.png',timeout:120000});await b.close();})();
