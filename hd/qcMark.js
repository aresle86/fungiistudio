const fs=require('fs');const {chromium}=require('playwright');const OUT=process.argv[2];
const C=[['A',12.3,5.6],['B',12.6,6.5],['C',1.2,8.0],['D',0.0,7.0],['E',2.2,9.6],['F',6.0,11.0]];
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [W,H,tag] of [[1280,800,'pc'],[390,844,'mob']]){const p=await b.newPage({viewport:{width:W,height:H}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const u=await p.evaluate((C)=>{window.__stop=true;const T=window.__g.T,S=window.__S,ST=window.__g.ST;ST.tm='fixed';ST.ovr=9.5;
 for(const [n,x,z] of C){const m=new T.Mesh(new T.CylinderGeometry(.08,.08,2.4,8),new T.MeshBasicMaterial({color:'#ff2a2a'}));m.position.set(x,1.2,z);S.add(m);
  const c=document.createElement('canvas');c.width=c.height=64;const g=c.getContext('2d');g.fillStyle='#ff2a2a';g.beginPath();g.arc(32,32,30,0,7);g.fill();g.fillStyle='#fff';g.font='bold 40px sans-serif';g.textAlign='center';g.fillText(n,32,46);
  const sp=new T.Sprite(new T.SpriteMaterial({map:new T.CanvasTexture(c),depthTest:false}));sp.position.set(x,2.7,z);sp.scale.set(.7,.7,.7);S.add(sp);}
 for(let i=0;i<3;i++)window.__tick();window.__r.render(S,window.__g.cam);return window.__r.domElement.toDataURL('image/jpeg',.8);},C);
fs.writeFileSync(`${OUT}/mark_${tag}.jpg`,Buffer.from(u.split(',')[1],'base64'));await p.close();}
await b.close();console.log('ok');})();
