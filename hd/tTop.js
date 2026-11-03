const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1400,height:1089}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g,ST=g.ST,{T}=window.__FT;ST.player={av:1,name:'N',garden:'V'};ST.lv=18;
 ST.ft.vusua={st:4,told:4,t:0};ST.ft.tretramdot={st:3,told:3,t:0};ST.ft.traucau={st:3,told:3,t:0};
 const S=window.__S;const C=[[-9.2,7.4,'#f00'],[-3.4,8.4,'#00f'],[-1.4,6.2,'#ff0'],[-8.8,2.6,'#0ff'],[-6.2,9.2,'#f0f'],[-10.2,5.6,'#0f0'],[0,0,'#000'],[-5,5,'#fff']];
 for(const [x,z,c] of C){const m=new T.Mesh(new T.CylinderGeometry(.35,.35,3,12),new T.MeshBasicMaterial({color:c}));m.position.set(x,1.5,z);S.add(m);}
 for(let i=0;i<6;i++)window.__tick();const cm=new T.OrthographicCamera(-9,9,7,-7,.1,100);cm.position.set(-4,40,5);cm.up.set(0,0,-1);cm.lookAt(-4,0,5);const r=window.__r;r.setSize(1400,1089);r.render(S,cm);});
await p.screenshot({path:'top.png'});await b.close();})();
