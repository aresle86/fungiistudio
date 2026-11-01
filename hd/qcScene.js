const {chromium}=require('playwright');const PAGE=process.argv[2]||'mv2_test.html';(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:390,height:844}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;const g=window.__g,w=window.__w,ST=g.ST;document.querySelectorAll('#intro,#lvup').forEach(e=>e.hidden=true);ST.player={av:1,name:'Na',garden:'V'};
const stat=()=>{const S=window.__S;let n=0,eg=0,pl=0,me=0,vis=0,ma=new Set(),cast=0;S.traverse(o=>{n++;if(o.isPointLight)pl++;if(o.isMesh){me++;if(o.visible)vis++;ma.add(o.material&&o.material.uuid);if(o.castShadow)cast++;}if((o.type==='Group'||o.type==='Object3D')&&!o.children.length)eg++;});const R=window.__r;let t=performance.now();for(let i=0;i<20;i++)window.__tick(t+=16);t=performance.now();for(let i=0;i<30;i++)window.__tick(performance.now());return {nodes:n,meshes:me,emptyGroups:eg,pointLights:pl,materials:ma.size,castShadow:cast,calls:R.info.render.calls,tris:R.info.render.triangles,geos:R.info.memory.geometries,msTick:+((performance.now()-t)/30).toFixed(1)}};
const a=stat();const XPN=[0,0,10,30,80,190,310,450,610,840,1060,1320,1620,1960,2340,2760,3220,3720,4260,4840,5460];
ST.xp=XPN[20];w.levelUp(20);document.querySelectorAll('#lvup').forEach(e=>e.hidden=true);
// giả lập vườn cấp cao: đủ 6 cây cổ tích lớn
ST.ft=ST.ft||{};for(const k of ['vusua','tretramdot','traucau','duahau','khevang','sodua'])ST.ft[k]={st:3,told:3,t:Date.now()};
let t=performance.now();for(let i=0;i<40;i++)window.__tick(t+=50);
const z=stat();
// rò bộ nhớ: chạy 3 phút game với bướm
const g0=window.__r.info.memory.geometries;t=performance.now();for(let i=0;i<3600;i++)window.__tick(t+=50);const g1=window.__r.info.memory.geometries;
return {lv1:a,lv20:z,geoLeak3min:{before:g0,after:g1}}});
console.log(JSON.stringify(r,null,1));await b.close();})();
