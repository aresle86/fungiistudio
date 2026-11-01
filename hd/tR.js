const fs=require('fs');const L=m=>fs.appendFileSync('../tR.log',m+'\n');fs.writeFileSync('../tR.log','');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').hidden=true;const g=window.__g;g.ST.player={av:1,name:'Na',garden:'V'};g.ST.lv=3;g.ST.xp=40;g.ST.xu=300;g.ST.seeds={cai:5};g.ST.inv.rom=3;g.closeSheet();window.__w.hud();});
const tick=async(n=2)=>{await p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await p.waitForTimeout(150);};await tick(3);await p.screenshot({path:'qc4/R_hud.png'});
L('badge '+await p.evaluate(()=>{const k=document.querySelector('#bSo .kb');return k.textContent+' gold '+document.getElementById('bSo').classList.contains('gold');}));
await p.click('#tRom');await tick();L('tool '+await p.evaluate(()=>JSON.stringify(window.__T.TOOL)));
// drag across beds A1..B2 using projected centers
const pts=await p.evaluate(()=>{const G=window.__G,g=window.__g;return G.PLOTS.filter(P=>['A1','A2','B1','B2'].includes(P.id)).map(P=>{const v=G.PV[P.id],q=new g.T.Vector3(v.cx,.05,v.cz).project(g.cam);return [(q.x+1)/2*innerWidth,(1-q.y)/2*innerHeight];});});
await p.mouse.move(pts[0][0],pts[0][1]);await p.mouse.down();for(const [x,y] of pts){await p.mouse.move(x,y,{steps:8});}await p.mouse.up();await tick();
L('after drag rom='+await p.evaluate(()=>window.__g.ST.inv.rom+' tool '+JSON.stringify(window.__T.TOOL)+' mulched '+['A1','A2','B1','B2'].filter(id=>window.__g.ST.plots[id].mulch>window.__g.ST.gt)));
await p.screenshot({path:'qc4/R_after.png'});
L(errs.join('\n'));await b.close();})();
