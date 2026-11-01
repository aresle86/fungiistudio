// Tìm chỗ trống để đặt cây: không vật, không ô đất, thấy được từ camera mặc định, không che gì phía sau.
const fs=require('fs');const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1280,height:800}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','0')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const R=await p.evaluate(()=>{window.__stop=true;for(let i=0;i<3;i++)window.__tick();
 const S=window.__S,cam=window.__g.cam,x=window.__x,T=window.__g.T;const ray=new T.Raycaster();
 // vùng cấm: mọi ô đất (kể cả chưa mở) nới 0.6
 const boxes=Object.values(x.PL).filter(P=>P.b).map(P=>P.b);
 const FTS=Object.values(window.__FT2.FT).map(f=>f.at);const inLand=(px,pz)=>boxes.some(([a,b2,c,d])=>px>a-.6&&px<c+.6&&pz>b2-.6&&pz<d+.6)||FTS.some(([fx,fz])=>Math.hypot(px-fx,pz-fz)<1.6)||(px>7.9&&px<11.9&&pz>1.8&&pz<7.2);
 const meshes=[];S.traverse(o=>{if(o.isMesh&&o.visible&&o.geometry)meshes.push(o);});
 const solid=h=>h.object.geometry.type!=='PlaneGeometry'&&h.point.y>.5;
 const out=[];const camPos=cam.position.clone();
 for(let gx=-11;gx<=14;gx+=.5)for(let gz=-5;gz<=12;gz+=.5){
  if(inLand(gx,gz))continue;
  // trên xuống: có vật trong bán kính ~0.8?
  let blocked=false;for(const [dx,dz] of [[0,0],[.7,0],[-.7,0],[0,.7],[0,-.7]]){ray.set(new T.Vector3(gx+dx,8,gz+dz),new T.Vector3(0,-1,0));const h=ray.intersectObjects(meshes,false).find(solid);if(h){blocked=true;break;}}
  if(blocked)continue;
  // trong khung hình camera mặc định?
  const top=new T.Vector3(gx,1.6,gz),v=top.clone().project(cam);if(Math.abs(v.x)>.92||v.y>.85||v.y<-.75)continue;
  // bị che: tia camera → ngọn cây chạm vật trước
  const dir=top.clone().sub(camPos);const dist=dir.length();dir.normalize();ray.set(camPos,dir);ray.far=dist-.3;
  const occ=ray.intersectObjects(meshes,false).find(solid);ray.far=Infinity;
  // che vật phía sau: tia đi tiếp qua thân cây 4m nữa chạm vật / ô đất
  ray.set(top,dir);ray.far=5;const behind=ray.intersectObjects(meshes,false).find(h=>solid(h)||inLand(h.point.x,h.point.z));ray.far=Infinity;
  const base=new T.Vector3(gx,0,gz);ray.set(camPos,base.clone().sub(camPos).normalize());const bh=ray.intersectObjects(meshes,false).find(solid);const baseHidden=bh&&bh.distance<camPos.distanceTo(base)-.3;
  const hidesFT=FTS.some(([fx,fz])=>{const vx=fx-gx,vz=fz-gz;const dx=dir.x,dz=dir.z,L=Math.hypot(dx,dz);const t=(vx*dx+vz*dz)/L;if(t<0||t>5.5)return false;return Math.abs(vx*dz-vz*dx)/L<1.3;});
  out.push({hidesFT,x:gx,z:gz,sx:+v.x.toFixed(2),sy:+v.y.toFixed(2),occ:!!occ,behind:behind?behind.object.name||behind.object.geometry.type:null,baseHidden:!!baseHidden});
 }
 return {cam:[camPos.x,camPos.y,camPos.z].map(n=>+n.toFixed(1)),target:[window.__ctl.target.x,window.__ctl.target.z].map(n=>+n.toFixed(1)),n:out.length,good:out.filter(o=>!o.occ&&!o.behind&&!o.baseHidden&&!o.hidesFT)};});
fs.writeFileSync('qcSpots.json',JSON.stringify(R,null,1));console.log('cam',R.cam,'target',R.target,'free',R.n,'good',R.good.length);
await b.close();})();
