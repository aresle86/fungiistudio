const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:700}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_trees.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const u=await p.evaluate(async()=>{window.__stop=true;const g=window.__g,ST=g.ST,w=window.__w;ST.player={av:1,name:'Na',garden:'V'};ST.tm='fixed';ST.ovr=9.5;ST.xp=840;w.levelUp(9);document.querySelectorAll('#intro,#lvup,.lvup,#ngoai').forEach(e=>e.hidden=true);
 const F=window.__FM;const r=F.FAREA;window.__e.fmEnter();for(let i=0;i<90;i++)window.__tick();window.__r.render(window.__S,g.cam);
 return {img:window.__r.domElement.toDataURL('image/jpeg',.85),area:r};});
fs.writeFileSync(process.argv[2],Buffer.from(u.img.split(',')[1],'base64'));console.log(JSON.stringify(u.area));await b.close();})();
