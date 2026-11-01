const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1300,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').style.display='none';const g=window.__g,ST=g.ST,X=window.__FT3,o={};ST.player={av:1,name:'N',garden:'V'};ST.lv=10;ST.xu=5000;ST.tm='fixed';ST.ovr=10;ST.inv.rom=10;ST.tre=5;ST.vit.fixed=0;
 X.penFix('vit');o.vit=[JSON.stringify(ST.bld),ST.vit.fixed,Math.round(X.bldLeft('vit')/60000)];
 for(const id of ['H1','H2','H5','H6','H3','H4','H7','H8'])if(!ST.land||1){ST.land=ST.land||{};}
 try{window.__FT2.aoBuy&&window.__FT2.aoBuy('H1');}catch(e){o.aoErr=e.message;}o.ao=JSON.stringify(ST.big.ao)+' '+Math.round(X.bldLeft('ao')/60000);
 try{window.__e.buyObj('say');}catch(e){o.sayErr=e.message;}o.say=JSON.stringify(ST.say&&{own:ST.say.own,at:ST.say.at})+' '+Math.round(X.bldLeft('say')/60000);
 for(let i=0;i<5;i++)window.__tick();const c=window.__ctl;const d=c.object.position.clone().sub(c.target);c.target.set(-.35,.3,6.45);c.object.position.copy(c.target).add(d);c.object.zoom=3;c.object.updateProjectionMatrix();for(let i=0;i<3;i++)window.__tick();return o;});
console.log(JSON.stringify(r));await p.screenshot({path:'../bld1.png',timeout:120000}).catch(()=>console.log('shotfail'));
console.log(await p.evaluate(()=>{const ST=window.__g.ST;for(const k in ST.bld)ST.bld[k].t-=5*3600e3;for(let i=0;i<5;i++)window.__tick();return JSON.stringify([ST.bld,ST.vit.fixed]);}));
await p.screenshot({path:'../bld2.png',timeout:120000}).catch(()=>console.log('shotfail'));
console.log(errs.join('\n'));await b.close();})();
