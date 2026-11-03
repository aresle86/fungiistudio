const fs=require('fs');const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:700,height:700}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
for (const k of ['vusua']){
const u=await p.evaluate((k)=>{window.__stop=true;const {T,fairyModel}=window.__FT;const r=window.__r;const S=new T.Scene();S.background=new T.Color('#3A4A3A');
 S.add(new T.HemisphereLight('#FFF6E0','#8A7A5A',1.6));const d=new T.DirectionalLight('#FFF1D6',2.2);d.position.set(4,8,5);S.add(d);
 const st=[4];
 st.forEach((s,i)=>{const pad=new T.Mesh(new T.BoxGeometry(1.6,.08,1.6),new T.MeshStandardMaterial({color:'#8DBA5A',flatShading:true}));pad.position.set(i*2.3,-.04,0);S.add(pad);const m=fairyModel(k,s);m.position.set(i*2.3,0,0);S.add(m);});
 const W=r.domElement.width,H=r.domElement.height,asp=W/H,vh=3.4;const c=new T.OrthographicCamera(-vh*asp/2,vh*asp/2,vh/2,-vh/2,-50,50);const cx=(st.length-1)*2.3/2;c.position.set(cx+5,5,7);c.lookAt(cx+.3,1.3,0);c.updateProjectionMatrix();
 r.render(S,c);return r.domElement.toDataURL('image/png');},k);
fs.writeFileSync('../ft_vs_close.png',Buffer.from(u.split(',')[1],'base64'));}
console.log('errs',errs.slice(0,3));await b.close();})();
