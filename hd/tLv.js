const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage({viewport:{width:390,height:800},deviceScaleFactor:2});await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{document.getElementById('intro').style.display='none';window.__g.ST.player={av:1,name:'N',garden:'V'};window.__x.levelUp(15);});await p.waitForTimeout(1500);
await p.screenshot({path:'../lv.png',timeout:120000});await b.close();})();
