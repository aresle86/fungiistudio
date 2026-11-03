const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b','H1','H2'],xu:2000,inv:{},seeds:{},gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1},player:{av:2,name:'Nhu',garden:'Nhà Như'},lv:20,xp:20000,qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1},plots:{},daysN:30,hvN:86,treeHv:9,guestN:14,buom:{trangcai:2,vang:1,phuong:1},fishLog:{caro:1,rophi:2,diec:1},bep:{made:{canhchua:5,cakho:3}},dd:{n:30,d:new Date().toDateString(),last:Date.now()}});
const out={};
for(const [w,h,tag] of [[390,844,'m'],[360,740,'m2']]){
const p=await b.newPage({viewport:{width:w,height:h},deviceScaleFactor:2,isMobile:tag==='m'});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup').forEach(e=>e.remove());const I=document.getElementById('intro');if(I){I.hidden=true;I.style.display='none';}});
let ok=false;for(let i=0;i<40&&!ok;i++){await p.waitForTimeout(1000);ok=await p.evaluate(()=>!!document.querySelector('.yrc-scrim'));}
out[tag]=[ok,await p.evaluate(()=>JSON.stringify(window.__g.ST.yr&&window.__g.ST.yr.s))];
await p.waitForTimeout(1200);await p.screenshot({path:`../yr_${tag}.png`,timeout:300000});
if(tag==='d'){await p.click('[data-y=hang]');await p.waitForTimeout(500);await p.evaluate(()=>{window.__stop=true;for(let i=0;i<120;i++)window.__tick();});
 out.frame=await p.evaluate(()=>{const f=window.__YR.YR.frame;return f?[f.visible,f.position.toArray()]:null;});
 for(const [x,z,zm,n] of [[3.8,.9,6,'yrf1'],[3.8,.9,3,'yrf2']]){await p.evaluate(([x,z,zm])=>{const c=window.__ctl;c.maxZoom=40;const d=c.object.position.clone().sub(c.target);c.target.set(x,.75,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();window.__tick();},[x,z,zm]);await p.screenshot({path:`../${n}.png`,timeout:300000});}
 // tải lại: ảnh vẫn treo, không hiện lại trang kỷ niệm
 const st=await p.evaluate(()=>localStorage.getItem('mv2-state'));out.saveKB=Math.round(st.length/1024);
}
out['err_'+tag]=errs.join('|')||'none';await p.close();}
console.log(JSON.stringify(out));await b.close();})();
