const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1000,height:640}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;const ST=window.__g.ST,X=window.__FT2;ST.lv=6;ST.ft.vusua={st:2,told:1,t:Date.now()};try{X.ftTick(1);}catch(e){return 'ERR '+e.stack.slice(0,400);}const V=X.FTV.vusua;let p=V.root,ch=[];while(p){ch.push((p.type||'')+':'+p.visible);p=p.parent;}return {oe:window.__oe,chain:ch.join(' > '),kids:V.root.children.length,pos:V.root.position.toArray()};});
console.log(JSON.stringify(r));await b.close();})();
