const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const [,,W,H,out,zs]=process.argv;const p=await b.newPage({viewport:{width:+W,height:+H}});p.on('pageerror',e=>console.log('ERR',e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{const g=window.__g;g.ST.player={av:1,name:'Na',garden:'V'};g.ST.lv=5;document.querySelectorAll('.lvup,#intro,#say').forEach(e=>e.hidden=true);});
for(const z of (zs||'1').split(',')){await p.evaluate(z=>{const c=window.__ctl.object;c.zoom=+z;c.updateProjectionMatrix();},z);await p.waitForTimeout(2500);await p.evaluate(()=>window.__stop=true);await p.waitForTimeout(300);await p.screenshot({path:`${out}_${z}.png`});await p.evaluate(()=>{window.__stop=false;requestAnimationFrame(window.__tick||(()=>{}))});}
await b.close();})();
