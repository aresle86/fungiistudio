// tCpn: mở game với vườn vừa đủ điểm lên cấp ngay lúc dựng cảnh -> không được báo lỗi dựng cảnh. node tCpn.js [trang]
const {chromium}=require('playwright');const PAGE=process.argv[2]||'mv2_t117b.html';const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SV={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1,sap1:1},player:{av:1,name:'Q',garden:'Q'},lv:9,xp:4400,xu:3000,inv:{},gb:{},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:8},(_,i)=>[i+3,1])),realTime:true,spd:1,real:Date.now()-3*864e5,dd:{last:'2026-1-1',n:3,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:1280,height:800}});p.setDefaultTimeout(600000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SV));
await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready,null,{timeout:600000}).catch(()=>{});await p.waitForTimeout(5000);
const box=await p.evaluate(()=>[...document.querySelectorAll('div,section')].filter(e=>/Có lỗi khi dựng cảnh/.test(e.textContent)&&e.children.length<3).map(e=>e.textContent.slice(0,160))[0]||'');
console.log(PAGE,'lỗi trang:',JSON.stringify(errs.slice(0,3)),'hộp lỗi:',box);console.log(!box&&!errs.some(e=>/cpN/.test(e))?'DONE all pass':'DONE FAIL');await b.close();})();
