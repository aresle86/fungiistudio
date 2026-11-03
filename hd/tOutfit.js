const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:500}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ui,.ddt,.ngoai,#tray,.nxq,#bCtr,.ctr{display:none!important}'});
const out=[];
for(let av=0;av<6;av++){for(const off of [[0,2,30],[14,4,14],[30,2,0],[-10,4,-25]]){
 await p.evaluate(([av,off])=>{window.__stop=true;const I=document.getElementById('intro');I.hidden=true;I.style.display='none';const g=window.__g;g.ST.player={av,name:'N',garden:'V'};g.ST.tm='fixed';g.ST.ovr=10;window.__FT3.placeAvatar();const A=window.__g.ST;
  for(let i=0;i<40;i++)window.__tick();
  const c=window.__ctl;c.maxZoom=60;const T=c.target.constructor;c.target.set(2.28,.25,2.03);c.object.position.copy(c.target).add(new T(...off));c.object.lookAt(c.target);c.object.zoom=13;c.object.updateProjectionMatrix();for(let i=0;i<2;i++)window.__tick();},[av,off]);
 out.push(await p.screenshot({clip:{x:450,y:100,width:300,height:300},timeout:120000}).then(b=>b.toString('base64')));}}
const ban=await p.evaluate(async()=>[window.__AVIMG.banbe,await window.__FT3.sticker(window.__AVIMG.banbe)]);const full=await p.evaluate(()=>window.__AVIMG.full);
await p.setContent('<body style="margin:0;background:#86B06A"><div style="display:grid;grid-template-columns:repeat(8,150px)">'+out.map(s=>`<img src="data:image/png;base64,${s}" width="150">`).join('')+'</div><div style="padding:10px;display:flex;gap:30px;align-items:end"><img src="'+ban[0]+'" width="300" style="background:#7CA35F"><img src="'+ban[1]+'" width="150"><img src="'+ban[1]+'" width="64"></div><div style="display:flex;gap:6px;padding:10px;background:#FFF8EA">'+full.map(u=>`<img src="${u}" width="190">`).join('')+'</div></body>');
await p.screenshot({path:'../outfit.png',fullPage:true});console.log(errs.join('|')||'no errors');await b.close();})();
