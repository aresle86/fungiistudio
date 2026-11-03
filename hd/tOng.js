const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:760}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:'+(process.env.PORT||8777)+'/'+(process.env.PAGE||'mv2_dev.html'),{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g,ST=g.ST,X=window.__FT3,o={};ST.player={av:1,name:'N',garden:'V'};ST.lv=17;ST.xu=3000;ST.tm='fixed';ST.ovr=10;
 const cells=window.__x.PLOTS.filter(P=>P.bai).map(P=>P.id);ST.land=ST.land||{};for(const id of cells.slice(0,4)){ST.land[id]={st:'ok'};}
 ST.ong.own=1;ST.ong.at=cells[0];ST.ong.t=Date.now();o.own=JSON.stringify(ST.ong);ST.ong.t-=30*3600e3;X.ongSim();o.honey=ST.ong.honey;for(let i=0;i<4;i++)window.__tick();
 o.take=X.ongTake();o.inv=ST.inv.matong;g.openSheet('ong');o.sheet=document.getElementById('shB')?document.getElementById('shB').innerText.slice(0,300):'';
 const at=ST.ong.at,v=at&&window.__g.PV?0:0;return o;});
console.log(JSON.stringify(r,null,1));
await p.evaluate(()=>{const g=window.__g,ST=g.ST;g.closeSheet();ST.ong.honey=2;ST.ong.n=2;for(let i=0;i<3;i++)window.__tick();const at=ST.ong.at;const P=window.__x.PLOTS.find(P=>P.id===at);const c=window.__ctl;const d=c.object.position.clone().sub(c.target);if(P){const b=P.b;c.target.set((b[0]+b[2])/2,.4,(b[1]+b[3])/2);}c.object.position.copy(c.target).add(d);c.object.zoom=4;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();});
await p.screenshot({path:'../ong.png',timeout:120000}).catch(()=>console.log('shotfail'));console.log(errs.join('\n'));await b.close();})();
