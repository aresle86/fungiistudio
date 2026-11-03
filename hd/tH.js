const fs=require('fs');const L=m=>fs.appendFileSync('../tH.log',m+'\n');fs.writeFileSync('../tH.log','');
const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1200,height:800}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message+' '+(e.stack||'').split('\n')[1]));
await p.addInitScript(()=>{try{if(!sessionStorage.getItem('x')){sessionStorage.setItem('x',1);localStorage.clear();localStorage.setItem('mv3d-q','1');}}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.getElementById('intro').hidden=true;const g=window.__g;g.ST.player={av:1,name:'Na',garden:'V'};g.closeSheet();});
const r=await p.evaluate(()=>{const H=window.__H,out=[];const lines=['Liếp cải khô rồi, tưới đi con.','Hái xong đợt này, cây ra lại được 2 đợt nữa đó con.','Nở 3 con gà con.','Con về rồi hả!','Đổi xong rồi nghe con.','Chuồng chật rồi, nâng chuồng trước đã con.','Gác bếp hết chỗ rồi con. Đem món ra chợ bán bớt nghe.','Được 2 con.'];for(const t of lines)out.push(t+' => voc='+H.hasVoc(t)+' | '+H.devoc(t));
 for(const t of lines){window.__g.say(t,'vui',{now:true});out.push('SAID '+document.getElementById('ngoaiTxt').textContent);}return out.join('\n');});L(r);
L(errs.join('\n'));await b.close();})();
