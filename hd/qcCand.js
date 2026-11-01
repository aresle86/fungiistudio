// Kiểm danh sách vị trí: trên nước? trong ô đất? sát vật? che cây cổ tích (trong 5,5 m sau)? bị che?
const {chromium}=require('playwright');const C=JSON.parse(process.argv[2]);
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1280,height:800}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','0')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const R=await p.evaluate((C)=>{window.__stop=true;for(let i=0;i<3;i++)window.__tick();
 const S=window.__S,cam=window.__g.cam,x=window.__x,T=window.__g.T,ray=new T.Raycaster();
 const boxes=Object.entries(x.PL).filter(([k,P])=>P.b);const FTS=Object.entries(window.__FT2.FT).map(([k,f])=>[k,f.at]);
 const meshes=[];S.traverse(o=>{if(o.isMesh&&o.visible&&o.geometry)meshes.push(o);});
 return C.map(([px,pz,h])=>{const r={x:px,z:pz};
  ray.set(new T.Vector3(px,8,pz),new T.Vector3(0,-1,0));const hits=ray.intersectObjects(meshes,false);
  r.groundTop=hits.length?(hits[0].object.name||hits[0].object.material.type)+'@'+hits[0].point.y.toFixed(2):'none';
  r.water=hits.some(h=>h.point.y<-0.02&&h.point.y>-1)||(hits[0]&&hits[0].point.y<-.02);
  r.land=boxes.filter(([k,P])=>{const [a,b2,c,d]=P.b;return px>a-.5&&px<c+.5&&pz>b2-.5&&pz<d+.5;}).map(([k])=>k).slice(0,3);
  r.near=[];for(const [dx,dz] of [[0,0],[.6,0],[-.6,0],[0,.6],[0,-.6]]){ray.set(new T.Vector3(px+dx,8,pz+dz),new T.Vector3(0,-1,0));const hh=ray.intersectObjects(meshes,false).find(q=>q.point.y>.35);if(hh)r.near.push(hh.point.y.toFixed(1));}
  const top=new T.Vector3(px,h,pz),dir=top.clone().sub(cam.position).normalize();
  r.hidesFT=FTS.filter(([k,[fx,fz]])=>{const vx=fx-px,vz=fz-pz,L=Math.hypot(dir.x,dir.z),t=(vx*dir.x+vz*dir.z)/L;return t>0&&t<h*1.9&&Math.abs(vx*dir.z-vz*dir.x)/L<1.3;}).map(([k])=>k);
  const v=top.clone().project(cam);r.screen=[+v.x.toFixed(2),+v.y.toFixed(2)];return r;});},C);
for(const r of R)console.log(JSON.stringify(r));await b.close();})();
