// game có tải xong không: in lỗi trang trong 90 giây đầu (chạy trước bộ test để khỏi chờ timeout 5 phút)
const {chromium}=require('playwright');
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:900,height:640}});const errs=[];p.on('pageerror',e=>errs.push(e.message+' @ '+(e.stack||'').split('\n')[1]));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(()=>{localStorage.clear();localStorage.setItem('mv3d-q','1');});
await p.goto('http://127.0.0.1:8777/'+(process.env.PAGE||'mv2_t107.html'),{waitUntil:'domcontentloaded'});
let ready=false;try{await p.waitForFunction(()=>window.__ready,null,{timeout:300000});ready=true;}catch(e){}
console.log(ready?'BOOT OK':'BOOT FAIL',errs.length?'\n'+errs.join('\n'):'');await b.close();process.exit(ready?0:1);})();
