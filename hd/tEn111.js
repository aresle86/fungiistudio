// bản tiếng Anh đợt 1: mở game với mv2-lang=en, chụp vườn, Sổ, Chợ, Cài đặt; đếm chữ Việt còn sót trên màn
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud14',{recursive:true});const PAGE=process.env.PAGE||'mv2_t111.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:12,xp:7600,xu:3000,inv:{oi:6,cai:6,trungga:4},gb:{cui:4,muoi:2},seeds:{cai:3},plots:{},qd:Object.fromEntries(Array.from({length:10},(_, i)=>[i+3,1])),tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph',locale:'en-US'});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-lang','en');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(2500);
 await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});});
 const vi=async()=>p.evaluate(()=>{const re=/[ăâđêôơưĂÂĐÊÔƠƯàáảãạằắẳẵặầấẩẫậèéẻẽẹềếểễệìíỉĩịòóỏõọồốổỗộờớởỡợùúủũụừứửữựỳýỷỹỵ]/i;const out=new Set();const w=document.createTreeWalker(document.body,NodeFilter.SHOW_TEXT);let n;while((n=w.nextNode())){const e=n.parentElement;if(!e||e.closest('[hidden]')||getComputedStyle(e).display==='none'||getComputedStyle(e).visibility==='hidden')continue;const r=e.getBoundingClientRect();if(!r.width||r.bottom<0||r.top>innerHeight)continue;const t=n.nodeValue.trim();if(t&&re.test(t))out.add(t.slice(0,50));}return [...out];});
 await p.screenshot({path:`../hud14/${tag}_vuon.png`});console.log(tag,'vườn còn chữ Việt:',JSON.stringify(await vi()).slice(0,500));
 for(const [n,f] of [['so',()=>window.__w.openBook('viec')],['kho',()=>window.__w.openBook('kho')],['cho',()=>{window.__w.closeBook();window.__x.openSheet('cho')}],['set',()=>window.__x.openSheet('set')]]){await p.evaluate(f);await p.waitForTimeout(700);await p.screenshot({path:`../hud14/${tag}_${n}.png`});console.log(tag,n,'còn chữ Việt:',JSON.stringify(await vi()).slice(0,400));await p.evaluate(()=>{const x=document.getElementById('shX');if(x&&!document.getElementById('sheet').hidden)x.click();});}
 console.log(tag,'errors',errs.slice(0,2));await p.close();}
await b.close();})();
