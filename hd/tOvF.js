const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:700,height:500},deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ddt,.ngoai,.nxq{display:none!important}'});
await p.evaluate(()=>{const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=6;g.ST.seen.hello=1;
 const ks=['ot','cachua','khoqua','cai','hanh','mongtoi','raumuong','bap'];let i=0;for(const id in g.ST.plots){const q=g.ST.plots[id];const P=window.__G.PL[id];if(!P||P.tree||P.bai)continue;if(i>5){i++;continue;}try{if(!q.crop){g.act.plant(id,P.trellis?'khoqua':ks[i%ks.length]);}}catch(e){}i++;}
 for(const id in g.ST.plots){const q=g.ST.plots[id];if(q.crop)q.g=99999;}window.__stop=true;for(let i=0;i<20;i++)window.__tick();});
await p.waitForTimeout(3000);
const run=n=>p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await run(30);
const pr=await p.evaluate(()=>{const G=window.__G,g=window.__g;const ids=Object.keys(g.ST.plots).filter(id=>g.ST.plots[id].crop&&G.PV[id]&&G.PV[id].want);const a=ids[0],b=ids[1],c=ids[2];G.PV[b].cx=G.PV[a].cx+.22;G.PV[b].cz=G.PV[a].cz+.12;G.PV[c].cx=G.PV[a].cx-.2;G.PV[c].cz=G.PV[a].cz+.2;return [G.PV[a].cx,G.PV[a].cz,ids.length];});console.log(pr);
for(const [x,z,zm,n] of [[pr[0],pr[1],3,'ovf1']]){await p.evaluate(([x,z,zm])=>{const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(x,.3,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();},[x,z,zm]);await run(4);await p.screenshot({path:'../'+n+'.png',timeout:300000});}
console.log(errs.join('\n')||'no errors');await b.close();})();
