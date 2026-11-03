// popup không được chồng lên nhau: dựng từng cảnh rồi đo khung các lớp nổi đang hiện
// dựng trang: cat x40f.js x106.js xpop.js > /tmp/x.js; python3 gen_test2.py /tmp/x.js live/v106a.html lp/mv2_t106.html
const {chromium}=require('playwright');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const base={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{oi:6,chuoi:4,cai:6},gb:{cui:4},seeds:{cai:3},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},
 land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'},H4:{st:'own'},H5:{st:'own'},H6:{st:'own'},H7:{st:'own'},H8:{st:'own'}},open:['H5'],
 dc:{rao:'rao_tre',ga:'ga_tre',vit:'vit_mac',own:{},bag:{sanh:1},items:[{k:'cong_tre',at:'H4'}]},
 ft:{vusua:{st:2,told:2,t:Date.now()-1e8}},realTime:true,spd:1,real:Date.now()};
const POPS=['#ngoai.on','#nxq','.ddt.on','#tstw .tst','#lvup','#sheet','#bk','#ring','#suaBar','#fan','.sktip','#intro','.fui .fcard'];
const scan=POPS=>{const out=[];for(const sel of POPS) for(const e of document.querySelectorAll(sel)){const c=getComputedStyle(e),r=e.getBoundingClientRect();
  if(e.closest('[hidden]')||c.display==='none'||c.visibility==='hidden'||+c.opacity<.05||r.width<2||r.height<2) continue; out.push([sel,r.x,r.y,r.right,r.bottom]);}
 const bad=[];for(let i=0;i<out.length;i++) for(let j=i+1;j<out.length;j++){const a=out[i],b=out[j],w=Math.min(a[3],b[3])-Math.max(a[1],b[1]),h=Math.min(a[4],b[4])-Math.max(a[2],b[2]);
  if(w>4&&h>4) bad.push(a[0]+' × '+b[0]+' ('+Math.round(w)+'×'+Math.round(h)+')');}
 return {on:out.map(o=>o[0]),bad};};
const SC=[
 ['vào vườn (thẻ về vườn + Ngoại nhờ + Ngoại chào)', {}, async(p)=>{await p.waitForTimeout(3500);}],
 ['Ngoại nói + thẻ về vườn', {}, async(p)=>{await p.evaluate(()=>window.__POP.say('Con coi nè, hôm nay trời đẹp ghê.','vui',{now:true}));await p.waitForTimeout(2500);}],
 ['Ngoại nói + toast', {dd:1}, async(p)=>{await p.evaluate(()=>{window.__POP.say('Con coi nè, hôm nay trời đẹp ghê.','vui',{now:true});window.__POP.toast('Còn thiếu 20 xu.','dan');});await p.waitForTimeout(400);}],
 ['Ngoại nói + vòng chọn', {dd:1}, async(p)=>{await p.evaluate(()=>{window.__POP.say('Con coi nè, hôm nay trời đẹp ghê.','vui',{now:true});window.__POP.openRing('H5','seed');});await p.waitForTimeout(400);}],
 ['vòng chọn rồi Ngoại nói', {dd:1}, async(p)=>{await p.evaluate(()=>{window.__POP.openRing('H5','seed');window.__POP.say('Con coi nè, hôm nay trời đẹp ghê.','vui',{now:true});});await p.waitForTimeout(400);}],
 ['bảng + toast', {dd:1}, async(p)=>{await p.evaluate(()=>{window.__POP.openSheet('cho');window.__POP.toast('Còn thiếu 20 xu.','dan');});await p.waitForTimeout(400);}],
 ['thanh đặt đồ + Ngoại nói + toast', {dd:1}, async(p)=>{await p.evaluate(()=>{window.__U.suaOn(true,'dc:sanh');window.__POP.say('Con coi nè, hôm nay trời đẹp ghê.','vui',{now:true});window.__POP.toast('Đồ kiểng đặt trên một ô đất trống của con.','dan');});await p.waitForTimeout(400);}],
 ['thanh đặt đồ + Ngoại nhờ', {dd:1}, async(p)=>{await p.evaluate(()=>window.__U.suaOn(true,'dc:sanh'));await p.waitForTimeout(400);}],
 ['Sổ + toast', {dd:1}, async(p)=>{await p.evaluate(()=>{window.__w.openBook('kho');window.__POP.toast('Kho đầy rồi con.','dan');});await p.waitForTimeout(400);}],
 ['lên cấp + thẻ về vườn', {lv:15,xp:13300}, async(p)=>{await p.waitForTimeout(2500);await p.evaluate(()=>window.__POP.levelUp(16));await p.waitForTimeout(800);}],
 ['lên cấp + Ngoại nói', {dd:1}, async(p)=>{await p.evaluate(()=>{window.__POP.say('Con coi nè, hôm nay trời đẹp ghê.','vui',{now:true});window.__POP.levelUp(16);});await p.waitForTimeout(800);}],
];
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});let nbad=0;
for(const [tag,vw] of [['pc',{width:1280,height:800}],['ph',{width:390,height:664}]]) for(const [i,[name,mod,run]] of SC.entries()){
 const S=Object.assign({},base,mod);if(mod.dd) S.dd={last:today,n:1,full:0};delete S.dd1;
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.setDefaultTimeout(180000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(S));
 await p.goto('http://127.0.0.1:8777/mv2_t106.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(600);
 await run(p);const r=await p.evaluate(scan,POPS);nbad+=r.bad.length;
 console.log(`${tag} ${i+1}. ${name}: ${r.bad.length?'CHỒNG '+r.bad.join(' ; '):'ok'}  [${r.on.join(', ')}]${errs.length?' ERR '+errs.join(' | '):''}`);
 await p.screenshot({path:`../pop_${tag}_${i+1}.png`});
 await p.close();}
console.log('DONE',nbad,'chỗ chồng');await b.close();})();
