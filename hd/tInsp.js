const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});
const p=await b.newPage({viewport:{width:400,height:300}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;const T=window.__g.T,S=window.__S,out=[];const bb=new T.Box3(),c=new T.Vector3(),sz=new T.Vector3();
S.traverse(o=>{if(!o.isMesh)return;bb.setFromObject(o);if(bb.isEmpty())return;bb.getCenter(c);bb.getSize(sz);if(bb.max.x>0.6&&bb.min.x<4.2&&bb.max.z>-1&&bb.min.z<1.9&&Math.max(sz.x,sz.z)>2)out.push([o.name||o.type,o.geometry.attributes.position.count,[c.x,c.y,c.z].map(v=>+v.toFixed(2)),[sz.x,sz.y,sz.z].map(v=>+v.toFixed(2))]);});return out;});
console.log(JSON.stringify(r));await b.close();})();
