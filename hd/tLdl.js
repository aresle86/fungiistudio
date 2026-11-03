const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:780}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html');await p.waitForFunction(()=>window.__ready,null,{timeout:200000});
const l=await p.evaluate(()=>[window.__LDL,performance.now()|0]);let pr=0;let pl="";for(const [a,t,s] of l[0]){if(t-pr>150)console.log(a,t,t-pr,"from",pl,"to",(s||"").slice(-12));pr=t;pl=(s||"").slice(-12);}console.log('end',l[1]);await b.close();})();
