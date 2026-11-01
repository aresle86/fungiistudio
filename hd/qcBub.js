const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});const p=await b.newPage();
await p.addInitScript(()=>{try{localStorage.clear()}catch(e){}});await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const r=await p.evaluate(()=>{window.__stop=true;const g=window.__g,ST=g.ST,X=window.__x;ST.lv=6;const cnt=xu=>{ST.xu=xu;for(const P of X.PLOTS)g.refreshPlot(P.id);let n=0,lk=0;for(const P of X.PLOTS){const v=g.PV[P.id];if(v&&v.want==='d')n++;}return n;};
 return {open:ST.open.length,xu58:cnt(58),xu60:cnt(60),xu500:cnt(500)};});console.log(JSON.stringify(r));
const g2=await p.evaluate(()=>{window.__w.openBook('giong');window.__tick();return document.querySelectorAll('#book .stk.lock').length;});console.log('so giong locks',g2);await b.close();})();
