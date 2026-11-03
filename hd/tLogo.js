const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1600,height:900}});p.on('pageerror',e=>console.log('ERR',e.message));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{const g=window.__g;g.ST.player={av:1,name:'Na',garden:'V'};g.ST.lv=12;window.__visitGo();});
await p.waitForTimeout(1500);await p.waitForFunction(()=>window.__ready,{timeout:300000});await p.waitForTimeout(1500);
const views=JSON.parse(process.argv[2]);
for(const [i,v] of views.entries()){
 const url=await p.evaluate(v=>{window.__stop=true;const g=window.__g,T=g.T,r=window.__r,S=window.__S;const W=v.W||1600,H=v.H||900;
  const cm=new T.PerspectiveCamera(v.fov||30,W/H,v.near||.05,v.far||200);cm.position.set(...v.pos);cm.lookAt(new T.Vector3(...v.at));cm.updateProjectionMatrix();
  S.traverse(o=>{if(o.userData&&o.userData.bub&&o.parent)o.parent.visible=false;});if(v.box){const B=v.box,ms=[];S.traverse(o=>{if(o.isMesh&&!o.isInstancedMesh&&o.geometry&&o.geometry.attributes.position)ms.push(o);else if((o.isPoints||o.isInstancedMesh||o.isSprite)&&v.mode==='only')o.visible=false;});
 const pa=new T.Vector3(),pb=new T.Vector3(),pc=new T.Vector3();
 for(const o of ms){o.updateMatrixWorld();let g=o.geometry;if(g.index)g=g.toNonIndexed();const P=g.attributes.position,n=P.count/3,keepIn=[],keepOut=[];
  for(let t=0;t<n;t++){pa.fromBufferAttribute(P,t*3).applyMatrix4(o.matrixWorld);pb.fromBufferAttribute(P,t*3+1).applyMatrix4(o.matrixWorld);pc.fromBufferAttribute(P,t*3+2).applyMatrix4(o.matrixWorld);
   const cx=(pa.x+pb.x+pc.x)/3,cy=(pa.y+pb.y+pc.y)/3,cz=(pa.z+pb.z+pc.z)/3;(cx>B[0]&&cx<B[2]&&cz>B[1]&&cz<B[3]&&cy>.045?keepIn:keepOut).push(t);}
  const sub=list=>{const ng=new T.BufferGeometry();for(const k in g.attributes){const A=g.attributes[k],is=A.itemSize,arr=new A.array.constructor(list.length*3*is);list.forEach((t,q)=>{for(let e=0;e<3*is;e++)arr[q*3*is+e]=A.array[t*3*is+e];});ng.setAttribute(k,new T.BufferAttribute(arr,is,A.normalized));}return ng;};
  if(v.mode==='only'){o.geometry=sub(keepIn);}
  else if(keepIn.length){o.geometry=sub(keepOut);const gh=m=>{m=m.clone();m.colorWrite=false;m.depthWrite=false;return m;};const sh=new T.Mesh(sub(keepIn),Array.isArray(o.material)?o.material.map(gh):gh(o.material));sh.castShadow=true;sh.matrixAutoUpdate=false;sh.matrix.copy(o.matrix);o.parent.add(sh);}}
}
const bg=S.background,fg=S.fog;if(v.alpha){S.background=null;S.fog=null;r.setClearColor(0,0);}r.setPixelRatio(1);r.setSize(W,H,false);r.render(S,cm);
  const sh=new T.Vector3(...v.ridge).project(cm);window.__ridge=[(sh.x+1)/2*W,(1-sh.y)/2*H];
  return r.domElement.toDataURL('image/png');},v);
 fs.writeFileSync(`../../logo/view${i}.png`,Buffer.from(url.split(',')[1],'base64'));console.log(i,JSON.stringify(await p.evaluate(()=>window.__ridge)));}
await b.close();})();
