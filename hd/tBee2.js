const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage({viewport:{width:900,height:450}});await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const u=await p.evaluate(()=>{window.__stop=true;const {T}=window.__FT,X=window.__FT3,r=window.__r;const sc=new T.Scene();sc.background=new T.Color('#cfe3c0');sc.add(new T.HemisphereLight('#fff','#888',2));const l=new T.DirectionalLight('#fff',1.5);l.position.set(2,4,3);sc.add(l);
 const h=X.beeHive(false);h.userData.bees.forEach(b=>b.visible=false);sc.add(h);const out=[];
 for(const pos of [[0,.4,3],[3,.4,0]]){const c=new T.OrthographicCamera(-.45,.45,.45,-.45,.1,20);c.position.set(...pos);c.lookAt(0,.4,0);r.setSize(450,450);r.render(sc,c);out.push(r.domElement.toDataURL('image/png'));}return out;});
const fs=require('fs');u.forEach((x,i)=>fs.writeFileSync('../bv'+i+'.png',Buffer.from(x.split(',')[1],'base64')));await b.close();})();
