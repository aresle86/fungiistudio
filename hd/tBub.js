const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:760},deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ddt,.ngoai{display:none!important}'});
await p.evaluate(()=>{window.__stop=true;const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av:1,name:'N',garden:'V'};g.ST.lv=6;g.ST.xp=0;g.ST.tm='fixed';g.ST.ovr=10;g.ST.seen.hello=1;g.ST.xu=500;g.ST.inv.rom=5;g.ST.tre=3;g.ST.ga.fixed=1;
 const ids=Object.keys(g.ST.plots);let k=0;for(const id of ids){const q=g.ST.plots[id];if(!q.crop)continue;k++;if(k%3===0)q.moist=0;if(k%4===0){q.cond='wilt';q.moist=0;}}
 window.__FT3.penFix('vit');g.ST.bld.vit.t-=50*60e3;for(let i=0;i<40;i++)window.__tick();});
const shot=async(n,x,z,zm)=>{await p.evaluate(([x,z,zm])=>{const c=window.__ctl;c.maxZoom=40;const d=c.object.position.clone().sub(c.target);c.target.set(x,.3,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();for(let i=0;i<4;i++)window.__tick();},[x,z,zm]);await p.screenshot({path:'../'+n+'.png',timeout:300000});};
await shot('bubA',3.2,4.4,1.9);await shot('bubB',3.4,4.4,4.2);
const vit=await p.evaluate(()=>{const k='vit';return JSON.stringify(window.__g.ST.bld);});console.log(vit);
await shot('bubC',-1.2,0.5,3.2);
console.log(errs.join('\n')||'no errors');await b.close();})();
