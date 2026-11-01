// Chụp vùng có cây/bụi sả bị comment: bản hiện tại vs bản bật lại.
const fs=require('fs');const {chromium}=require('playwright');
const OUT=process.argv[2]||'..';
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [pg,tag] of [['mv2_dev.html','hientai'],['mv2_trees.html','batlai']]){
 const p=await b.newPage({viewport:{width:1100,height:700}});
 await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
 await p.goto('http://127.0.0.1:8777/'+pg,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
 await p.evaluate(()=>{window.__stop=true;const ST=window.__g.ST;ST.player={av:1,name:'Na',garden:'V'};ST.tm='fixed';ST.ovr=9.5;document.querySelectorAll('#intro,#lvup,.lvup,#ngoai').forEach(e=>e.hidden=true);});
 for(const [nm,tx,tz,zm] of [['tong',4.5,3.2,1.0],['caytruoc',6.0,.9,1.6],['gocphai',9.6,4.4,1.7]]){
  const u=await p.evaluate(([tx,tz,zm])=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(tx,0,tz);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();for(let i=0;i<4;i++)window.__tick();window.__r.render(window.__S,window.__g.cam);return window.__r.domElement.toDataURL('image/jpeg',.85);},[tx,tz,zm]);
  fs.writeFileSync(`${OUT}/cay_${nm}_${tag}.jpg`,Buffer.from(u.split(',')[1],'base64'));console.log('shot',nm,tag);
 }
 await p.close();}
await b.close();})();
