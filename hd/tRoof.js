const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1500,height:700}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g,{T}=window.__FT,S=window.__S,X=window.__FT3;g.ST.tm='fixed';g.ST.ovr=9.5;
 const mk=(x,z,f)=>{const h=new T.Group();h.position.set(x,0,z);S.add(h);const wall=new T.Mesh(new T.BoxGeometry(2.8,.9,1.8),new T.MeshStandardMaterial({color:'#C9A27A',flatShading:true}));wall.position.y=.65;h.add(wall);const r=f(h);r.position.y=1.1;};
 mk(-12,4,h=>X.roofState(h,2.8,1.8,.82,.26,0));mk(-8,4,h=>X.roofState(h,2.8,1.8,.82,.26,1));mk(-4,4,h=>X.roofState(h,2.8,1.8,.82,.26,2));
 for(let i=0;i<4;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-8,.9,4);c.object.position.copy(c.target).add(d);c.object.zoom=1.55;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();window.__r.render(S,g.cam);});
await p.screenshot({path:'../roof.png',timeout:120000});console.log(errs);await b.close();})();
