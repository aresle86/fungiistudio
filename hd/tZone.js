const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const [,,out,lv,opens,views]=process.argv;const p=await b.newPage({viewport:{width:900,height:560}});p.on('pageerror',e=>console.log('ERR',e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(([lv,opens])=>{const g=window.__g,ST=g.ST;ST.player={av:1,name:'Na',garden:'V'};ST.lv=+lv;ST.qd=ST.qd||{};for(let i=2;i<=+lv;i++)ST.qd[i]=1;for(const id of opens.split(',').filter(Boolean)){if(!ST.open.includes(id))ST.open.push(id);}
for(const P of window.__x.PLOTS)g.refreshPlot(P.id);document.querySelectorAll('.lvup,#intro,#say,.ngoai,#nxq').forEach(e=>e.hidden=true);},[lv,opens||'']);
let i=0;for(const v of JSON.parse(views)){await p.evaluate(([x,z,zm])=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(x,.3,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();},v);
await p.waitForTimeout(2500);await p.screenshot({path:`${out}_${i++}.png`,timeout:120000});}
await b.close();})();
