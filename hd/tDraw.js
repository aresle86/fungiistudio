// đếm draw call theo nguồn: mesh nào còn vẽ riêng sau bước gộp (dyn? sway? keep? vật liệu nào, nhóm nào)
// dựng trang: python3 gen_test2.py /tmp/x.js live/v107a.html lp/mv2_t107.html
const {chromium}=require('playwright');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{},gb:{},seeds:{},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'},H4:{st:'own'}},open:['H1'],
 nong:{own:1,at:'H2',trays:[null,null,null,null],done:3,made:{}},khap:{own:1,at:'H3',jars:[null,null],done:2,made:{}},ga:{hens:4,rooster:1,trough:4,eggs:0,acc:0,lv:1,brood:null,fixed:1},vit:{n:6,trough:8,eggs:0,acc:0,lv:1,fixed:1},
 realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:664},deviceScaleFactor:2,hasTouch:true});p.setDefaultTimeout(180000);
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
await p.goto('http://127.0.0.1:8777/mv2_t107.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(3000);
const r=await p.evaluate(()=>{const S=window.__S,cam=window.__g.cam,r=window.__r;const fr=new (window.__g.T.Frustum)();const pv=new (window.__g.T.Matrix4)().multiplyMatrices(cam.projectionMatrix,cam.matrixWorldInverse);fr.setFromProjectionMatrix(pv);
 const by={},mats={},groups={};let n=0,vis=0,shadow=0,inst=0;
 S.traverse(o=>{if(!o.isMesh&&!o.isInstancedMesh&&!o.isPoints&&!o.isLine) return;n++;let v=true;for(let a=o;a;a=a.parent) if(a.visible===false){v=false;break;}if(!v) return;
  const geo=o.geometry;let inF=true;try{if(o.frustumCulled!==false&&geo){if(!geo.boundingSphere) geo.computeBoundingSphere();const sp=geo.boundingSphere.clone().applyMatrix4(o.matrixWorld);inF=fr.intersectsSphere(sp);}}catch(e){}
  if(!inF) return;vis++;if(o.isInstancedMesh) inst++;if(o.castShadow) shadow++;
  let dyn='static',g=null;for(let a=o.parent;a;a=a.parent){if(a.userData.dyn){dyn='dyn';break;}}
  const key=(o.isInstancedMesh?'inst ':'')+dyn+(o.userData.keep?' keep':'')+(o.userData.sway>0?' sway':'')+(o.material&&o.material.transparent?' transp':'')+(o.isPoints?' points':'')+(o.isLine?' line':'');
  by[key]=(by[key]||0)+1;const mk=o.material?(o.material.type+' '+(o.material.color?'#'+o.material.color.getHexString():'')):'?';mats[mk]=(mats[mk]||0)+1;
  // nhóm cha gần nhất có tên hay có nhiều con
  let gp=o.parent,d=0;while(gp&&gp!==S&&gp.children.length<8&&d<6){gp=gp.parent;d++;}const gn=gp===S?'ROOT':(gp.name||('grp@'+gp.position.x.toFixed(1)+','+gp.position.z.toFixed(1)+' n'+gp.children.length));groups[gn]=(groups[gn]||0)+1;});
 const top=o=>Object.entries(o).sort((a,b)=>b[1]-a[1]).slice(0,25);
 return {calls:r.info.render.calls,meshes:n,visibleInFrustum:vis,inst,shadow,by:top(by),mats:top(mats),groups:top(groups)};});
console.log(JSON.stringify(r,null,1));await b.close();})();
