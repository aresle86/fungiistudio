const fs=require('fs');const L=m=>fs.appendFileSync('../tT.log',m+'\n');fs.writeFileSync('../tT.log','');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').hidden=true;const g=window.__g;g.ST.player={av:1,name:'Na',garden:'V'};g.ST.lv=3;g.ST.xu=300;g.ST.seeds={cai:5};g.closeSheet();});
const tick=async(n=2)=>{await p.evaluate(n=>{for(let i=0;i<n;i++)window.__tick();},n);await p.waitForTimeout(150);};await tick(3);
await p.evaluate(()=>window.__T.setTool({kind:'seed',k:'cai'}));await tick();L('btn '+await p.textContent('#sbX'));await p.screenshot({path:'qc4/T_bar.png'});
// tap river (bottom-left)
await p.mouse.click(150,700);await tick();L('after tap empty: '+await p.evaluate(()=>JSON.stringify(window.__T.TOOL)));
await p.evaluate(()=>window.__T.setTool({kind:'seed',k:'cai'}));await p.keyboard.press('Escape');L('after esc: '+await p.evaluate(()=>JSON.stringify(window.__T.TOOL)));
await p.evaluate(()=>window.__T.setTool({kind:'seed',k:'cai'}));await p.mouse.click(600,400,{button:'right'});L('after right: '+await p.evaluate(()=>JSON.stringify(window.__T.TOOL)));
// sow all empty beds via finishSow
const r=await p.evaluate(()=>{const G=window.__G,T=window.__T;T.setTool({kind:'seed',k:'cai'});const e=G.PLOTS.filter(P=>G.needOf(P.id)==='seed'&&!P.tree&&!P.trellis).map(P=>P.id);const out=[];for(const id of e){T.finishSow(id);out.push(id+':'+JSON.stringify(T.TOOL));}return out.join(' ');});L('sow all '+r);
await tick();await p.screenshot({path:'qc4/T_auto.png'});L(errs.join('\n'));await b.close();})();
