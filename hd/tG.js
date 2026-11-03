const fs=require('fs');const LOG='../tG_'+process.argv[4]+'.log';const L=m=>fs.appendFileSync(LOG,m+'\n');fs.writeFileSync(LOG,'');
const {chromium}=require('playwright');(async()=>{const [,,W,H,tag]=process.argv;const mob=+W<700;const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:+W,height:+H},hasTouch:mob,isMobile:mob});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;const i=document.getElementById('intro');i.hidden=true;const g=window.__g;g.ST.player={av:1,name:'Na',garden:'Vườn Na'};g.ST.lv=3;g.ST.xp=40;g.ST.xu=300;g.ST.seeds={cai:2,hanh:1};g.closeSheet();window.__w.hud();});
const tick=async(n=2)=>{await p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await p.waitForTimeout(150);};await tick(4);const sh=n=>p.screenshot({path:`qc4/G_${tag}_${n}.png`});
const info=await p.evaluate(()=>{const G=window.__G,g=window.__g;for(const P of G.PLOTS){if(g.ST.plots[P.id])g.ST.plots[P.id].crop=g.ST.plots[P.id].crop;}const e=G.PLOTS.filter(P=>G.needOf(P.id)==='seed'&&!P.tree&&!P.trellis).map(P=>P.id),o=G.PLOTS.filter(P=>G.needOf(P.id)==='open'&&!P.bai).map(P=>P.id);for(const id of e)window.__g.refreshPlot(id);return {e,o};});L('empty '+info.e+' open '+info.o);
await tick(3);
const pos=id=>p.evaluate(id=>{const G=window.__G,g=window.__g,v=G.PV[id],q=new g.T.Vector3(v.cx,v.bubY,v.cz).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];},id);
const tap=async([x,y])=>{if(mob)await p.touchscreen.tap(x,y);else await p.mouse.click(x,y);await tick();};
const A=info.e[0],B=info.e[1],C=info.e[2];
await tap(await pos(A));await tick();L('ring open '+await p.evaluate(()=>!document.getElementById('ring').hidden+' '+window.__G.RINGID));await sh('ring');
await p.click('#ring .rgi[data-k=cai]');await tick();L('A crop '+await p.evaluate(id=>window.__g.ST.plots[id].crop+' last '+window.__g.ST.lastSeed+' ring hidden '+document.getElementById('ring').hidden,A));
await tick(3);await sh('afterA');
await tap(await pos(B));await tick();L('B quick '+await p.evaluate(id=>window.__g.ST.plots[id].crop+' seeds '+JSON.stringify(window.__g.ST.seeds),B));
// long press C
const [cx,cy]=await pos(C);if(mob){await p.evaluate(([x,y])=>{},[cx,cy]);}await p.mouse.move(cx,cy);await p.mouse.down();await p.waitForTimeout(700);await p.mouse.up();await tick();L('C long ring '+await p.evaluate(()=>!document.getElementById('ring').hidden));await sh('long');
await p.evaluate(()=>window.__G.closeRing());
if(info.o.length){await p.evaluate(id=>window.__G.openRing(id,'open'),info.o[0]);await tick();await sh('open');const xu0=await p.evaluate(()=>window.__g.ST.xu);await p.click('#ring [data-r=open]').catch(e=>L('openbtn '+e.message.split('\n')[0]));await tick();L('opened bed xu '+xu0+'->'+await p.evaluate(()=>window.__g.ST.xu));}
L(errs.join('\n'));await b.close();})();
