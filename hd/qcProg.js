// QC tiến trình cấp: thẻ "Việc tiếp theo" + Sổ › Việc ở nhiều trạng thái, chụp khung điện thoại.
const fs=require('fs');const {chromium}=require('playwright');const OUT=process.argv[2]||'..';
const CASES=[
 ['c1_lv6_thieu_kn_xongviec', {lv:6,xp:444,xu:58,tasksDone:true}],
 ['c2_lv6_thieu_kn_conviec', {lv:6,xp:444,xu:58,tasksDone:false}],
 ['c3_lv6_du_kn_thieu_xu',  {lv:6,xp:452,xu:58,tasksDone:true}],
 ['c4_lv6_du_kn_du_xu',     {lv:6,xp:452,xu:150,tasksDone:true}],
 ['c5_lv7_viec_lam_dan',    {lv:7,xp:500,xu:58,tasksDone:true}],
 ['c6_lv2_phat_co',         {lv:2,xp:12,xu:58,tasksDone:false}],
];
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:390,height:844},isMobile:true,hasTouch:true,deviceScaleFactor:2});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','0')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_dev.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
for(const [nm,c] of CASES){
 const r=await p.evaluate((c)=>{window.__stop=true;const g=window.__g,w=window.__w,ST=g.ST;ST.player={av:1,name:'Như',garden:'V'};
  document.querySelectorAll('#intro,#lvup,.lvup,#ngoai').forEach(e=>e.hidden=true);window.LVON=false;document.body.classList.remove('lvon');
  ST.lv=c.lv;ST.xp=c.xp;ST.xu=c.xu;ST.qd={};for(let i=2;i<=c.lv;i++)ST.qd[i]=1;ST.ga.fixed=1;ST.vit=ST.vit||{};ST.vit.fixed=1;ST.weed=0;
  try{w.openBook('viec');w.closeBook();}catch(e){} const L=ST.tasks.list;L.forEach((x,i)=>{if(c.tasksDone){x.done=1;x.have=x.need;}else{x.done=i<2?1:0;x.have=i<2?x.need:0;}});
  w.hud();w.nxq();for(let i=0;i<2;i++)window.__tick();
  const card=document.getElementById('nxq').innerText.replace(/\s+/g,' ');
  w.openBook('viec');for(let i=0;i<2;i++)window.__tick();const book=document.getElementById('book').innerText.replace(/\s+/g,' ').slice(0,420);
  return {card,book};},c);
 await p.waitForTimeout(300);
 try{await p.screenshot({path:`${OUT}/${nm}_so.png`,timeout:45000});}catch(e){}
 await p.evaluate(()=>{window.__w.closeBook();for(let i=0;i<2;i++)window.__tick();});await p.waitForTimeout(200);
 try{await p.screenshot({path:`${OUT}/${nm}_the.png`,timeout:45000,clip:{x:0,y:0,width:390,height:330}});}catch(e){}
 console.log('##',nm,'\n  THẺ:',r.card,'\n  SỔ :',r.book);
}
console.log('errs',errs);await b.close();})();
