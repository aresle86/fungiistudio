const {chromium}=require('playwright');(async()=>{const [,,out,w,h]=process.argv;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:+w,height:+h},hasTouch:false});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,{timeout:240000});await p.waitForTimeout(1500);
const frame=async()=>{await p.evaluate(()=>{window.__stop=true;});await p.waitForTimeout(150);await p.evaluate(()=>{window.__g.ST.realTime=false;window.__g.ST.ovr=12;for(let i=0;i<3;i++)window.__tick();});};
await frame();
// tap water bubble on B1 through the real canvas
const pos=await p.evaluate(()=>{const g=window.__g,v=g.PV.B1,b=v.bub[v.want];const q=b.position.clone().project(g.cam);return {want:v.want,x:(q.x+1)/2*innerWidth,y:(1-q.y)/2*innerHeight};});
console.log('bubble',JSON.stringify(pos));
await p.mouse.move(pos.x,pos.y);await p.mouse.down();await p.mouse.up();await p.waitForTimeout(200);
console.log('B1 moist after tap',await p.evaluate(()=>window.__g.ST.plots.B1.moist));
// tap empty plot C2? (harvest B2 first via its hand bubble)
const pos2=await p.evaluate(()=>{const g=window.__g,v=g.PV.B2,b=v.bub[v.want];const q=b.position.clone().project(g.cam);return {want:v.want,x:(q.x+1)/2*innerWidth,y:(1-q.y)/2*innerHeight};});
await p.mouse.move(pos2.x,pos2.y);await p.mouse.down();await p.mouse.up();await p.waitForTimeout(200);console.log('inv',JSON.stringify(await p.evaluate(()=>window.__g.ST.inv)), 'B2 bubble was', pos2.want);
// wilt + dead look
await p.evaluate(()=>{const g=window.__g;g.ST.plots.A2.moist=0;g.ST.plots.A2.dry=0;g.ST.plots.C1.moist=0;g.ST.plots.A1.moist=0;g.sim(60*60);g.ST.plots.C1.moist=0;g.sim(3.2*3600);g.ST.plots.B1.moist=0;g.ST.plots.B1.dry=45*60;for(const k of Object.keys(g.PV))g.refreshPlot(k);});
await frame();await p.waitForTimeout(500);await p.screenshot({path:out+'_wilt.png',timeout:180000});
console.log(JSON.stringify(await p.evaluate(()=>{const s=window.__g.ST.plots;return Object.fromEntries(Object.entries(s).map(([k,v])=>[k,[v.crop,Math.round(v.g),v.moist.toFixed(2),Math.round(v.dry),v.dead]]));})));
console.log(errs.join('\n'));await b.close();})();
