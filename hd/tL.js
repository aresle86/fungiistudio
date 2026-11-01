const fs=require('fs');const L=m=>fs.appendFileSync('../tL.log',m+'\n');fs.writeFileSync('../tL.log','');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').hidden=true;const g=window.__g,w=window.__w,out=[];g.ST.player={av:1,name:'Na',garden:'V'};
 const XPN=[0,0,10,30,80,190,310,450,610,840,1060,1320,1620];
 for(let n=2;n<=12;n++){try{g.ST.xp=XPN[n];w.levelUp(n);document.getElementById('lvup').hidden=true;window.LVON=false;document.body.classList.remove('lvon');w.hud();w.nxq();
  w.openBook('viec');const bk=document.getElementById('book').innerText.replace(/\s+/g,' ').slice(0,160);w.closeBook();
  const tasks=g.ST.tasks.list.map(x=>x.txt).join('|');
  out.push(`lv${n} nxq=[${document.getElementById('nxq').innerText.replace(/\s+/g,' ')}] gaFix=${g.ST.ga.fixed} vitFix=${g.ST.vit.fixed} tasks=${tasks}`);
  if(n===2){const P=window.__P;g.ST.tre=2;g.ST.inv.rom=9;g.ST.xu=999;P.penFix('ga');out.push(' fixed ga '+g.ST.ga.fixed);}
  if(n===6){const P=window.__P;g.ST.tre=3;g.ST.inv.rom=9;g.ST.xu=999;P.penFix('vit');out.push(' fixed vit '+g.ST.vit.fixed);}
 }catch(e){out.push('lv'+n+' ERR '+e.message);}}
 const H=window.__H;out.push('SAYH voc pattern: '+H.SAYH.map(h=>h.v?'C':'.').join(''));
 out.push('SAYH last: '+H.SAYH.slice(-6).map(h=>h.t.slice(0,70)).join(' || '));return out.join('\n');});
L(r);L(errs.join('\n'));await b.close();})();
