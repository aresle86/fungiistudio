const {chromium}=require('playwright');const fs=require('fs');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:900}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const ic=await p.evaluate(async()=>{window.__stop=true;const I={};const src={banbe:window.__AVIMG.banbe,so:document.getElementById('icSo').dataset.stk,cho:document.getElementById('icCho').dataset.stk,set:document.getElementById('icSet').dataset.stk};
 const g=(id)=>document.getElementById(id);src.seed=g('icSeed').dataset.stk||g('icSeed').src;src.rom=g('icRom').dataset.stk||g('icRom').src;
 const imgs=[...document.querySelectorAll('#shB img, img')].map(x=>x.src);
 src.coin=window.__UIC.coin;src.sprout=window.__UIC.sprout||window.__UIC.task;for(const [k,u] of Object.entries(src)){I[k]=await window.__FT3.sticker(u);I[k+'_raw']=u;}
 return I;});
const css=fs.readFileSync('../ui2fix.py','utf8').split('CSS = r"""')[1].split('"""')[0];
const page=fs.readFileSync('../board.html','utf8').replace('/*CSS*/',css).replace(/\{\{(\w+)\}\}/g,(m,k)=>ic[k]||'');
fs.writeFileSync('board_r.html',page);await p.goto('http://127.0.0.1:8777/board_r.html');await p.evaluate(()=>document.fonts.ready);await p.waitForTimeout(800);await p.screenshot({path:'../board.png',fullPage:true});
console.log(errs.join('|')||'no errors');await b.close();})();
