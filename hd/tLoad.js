const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:780}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1');window.__keepLoad=1}catch(e){}});
const t0=Date.now();await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'commit'});let i=0,last=0;
while(Date.now()-t0<60000){const r=await p.evaluate(()=>{const b=document.querySelector('#load .lbar i b');return [b?getComputedStyle(b).width:'',!!window.__ready,document.getElementById('load')?.className]}).catch(()=>null);const t=Date.now()-t0;if(r){console.log(t,t-last,JSON.stringify(r));last=t;if(i%3==0)await p.screenshot({path:'ld'+(i/3)+'.png'});i++;if(document=>0, r[1]&&r[2]&&r[2].includes('out'))break;}await new Promise(r=>setTimeout(r,150));}
console.log(errs.slice(0,3));await b.close();})();
