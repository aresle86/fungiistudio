const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:700},deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ddt,.ngoai{display:none!important}'});
await p.evaluate(()=>{window.__stop=true;const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=6;g.ST.xp=0;g.ST.tm='fixed';g.ST.ovr=10;g.ST.seen.hello=1;g.ST.xu=500;g.ST.inv.rom=5;g.ST.tre=3;g.ST.ga.fixed=1;
 for(const id in g.ST.plots){const q=g.ST.plots[id];if(q.crop&&!g.ST.plots[id].dead){q.g=99999;break;}}
 window.__FT3.penFix('vit');if(g.ST.bld&&g.ST.bld.vit)g.ST.bld.vit.t-=30*60e3;for(let i=0;i<40;i++)window.__tick();});
const L=await p.evaluate(()=>{const g=window.__g,out=[];const sc=window.__r?null:null;const T=g.T;let root=g.cam.parent;while(root&&root.parent)root=root.parent;
 const seen=[];window.__S.traverse(o=>{if(o.userData&&o.userData.ring&&o.visible){let v=true,q=o;while(q){if(!q.visible)v=false;q=q.parent;}if(!v)return;const w=new T.Vector3();o.getWorldPosition(w);out.push({x:+w.x.toFixed(2),z:+w.z.toFixed(2),bar:!!(o.userData.bar&&o.userData.bar.visible),col:o.userData.col});}});return out;});
console.log(JSON.stringify(L));
const shot=async(n,x,z,zm)=>{await p.evaluate(([x,z,zm])=>{const c=window.__ctl;c.maxZoom=40;const d=c.object.position.clone().sub(c.target);c.target.set(x,.3,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();for(let i=0;i<4;i++)window.__tick();},[x,z,zm]);await p.screenshot({path:'../'+n+'.png',timeout:300000});};
const bar=L.find(o=>o.bar),gr=L.find(o=>o.col==='#7DB84A'||o.col==='lay');
if(bar)await shot('bubBar',bar.x,bar.z,4);if(gr)await shot('bubGreen',gr.x,gr.z,4);
console.log(errs.join('\n')||'no errors');await b.close();})();
