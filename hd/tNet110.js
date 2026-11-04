// v110 mạng: ghé vườn bị server từ chối thì nói đúng lý do; rớt mạng thử lại 1 lần; mở game mà mây mới hơn thì tự tải. Server giả lập.
const {chromium}=require('playwright');const PAGE=process.env.PAGE||'mv2_t110.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const ME={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:10,xp:4300,xu:900,inv:{},seeds:{},plots:{},qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1},realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});let bad=0;
const ok=(c,m)=>{console.log(`${c?'OK ':'SAI'} ${m}`);if(!c) bad++;};
const mk=async(init,arg,act)=>{const p=await b.newPage({viewport:{width:900,height:640}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.setDefaultTimeout(300000);const calls=[];
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),async r=>{const u=r.request().url();const m=u.match(/rpc\/(mv2_\w+)/);if(!m) return r.abort();calls.push(m[1]);
  if(m[1]==='mv2_act') return act(r,calls.filter(c=>c==='mv2_act').length);
  if(m[1]==='mv2_save2') return r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({ok:false,stale:true,rev:9})});
  if(m[1]==='mv2_restore') return r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({rev:9,data:Object.assign({},JSON.parse(arg[0]),{xu:7777})})});
  return r.fulfill({status:200,contentType:'application/json',body:'null'});});
 await p.addInitScript(init,arg);await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(800);return {p,errs,calls};};
const visitInit=([me])=>{if(sessionStorage.getItem('done'))return;localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',me);localStorage.setItem('mv2-cloud',JSON.stringify({code:'MEME',secret:'s'}));
  const st=JSON.parse(me);st.player={av:2,name:'Tư',garden:'Tư'};sessionStorage.setItem('mv2-visit',JSON.stringify({kind:'ban',code:'TUTU',owner:'Tư',name:'Vườn Tư',myLv:10,left:5,cong:1,state:st,loot:{inv:{},xp:0,water:0,friend:'Tư',giftOut:[]}}));};
const tapRipe=async p=>p.evaluate(async()=>{const g=window.__g,V=window.__V,P=window.__G.PLOTS.find(P=>!P.tree&&!P.trellis&&!P.bai&&g.ST.plots[P.id]);const q=g.ST.plots[P.id];q.crop='cai';q.g=V.CROPS.cai.grow+10;q.moist=1;g.refreshPlot(P.id);
  const T=[];const mo=new MutationObserver(ms=>{for(const m of ms)for(const n of m.addedNodes)if(n.nodeType===1&&n.textContent)T.push(n.textContent);});mo.observe(document.body,{childList:true,subtree:true});await V.visitTap(P.id);await new Promise(r=>setTimeout(r,400));mo.disconnect();return T.join(' / ');});
for(const [name,act,want] of process.env.ONLY?[]:[
 ['vườn không còn',r=>r.fulfill({status:400,contentType:'application/json',body:JSON.stringify({message:'no farm'})}),/không còn nữa/],
 ['mã lệch',r=>r.fulfill({status:400,contentType:'application/json',body:JSON.stringify({message:'not allowed'})}),/Mã vườn trên máy này lệch/],
 ['rớt mạng 1 lần rồi được',(r,n)=>n===1?r.abort():r.fulfill({status:200,contentType:'application/json',body:JSON.stringify({ok:true,left:3})}),null]]){
 const {p,errs,calls}=await mk(visitInit,[JSON.stringify(ME)],act);const t=await tapRipe(p);
 if(want) ok(want.test(t),name+': '+t.slice(0,140)); else ok(calls.filter(c=>c==='mv2_act').length===2&&!/chập chờn/.test(t),name+' (gọi '+calls.filter(c=>c==='mv2_act').length+' lần): '+t.slice(0,100));
 ok(!errs.length,name+' không lỗi trang '+errs.join(' | '));await p.close();}
{const init=([me])=>{if(sessionStorage.getItem('seen'))return;sessionStorage.setItem('seen','1');localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',me);localStorage.setItem('mv2-cloud',JSON.stringify({code:'MV-MEME',secret:'ABCDEFGHIJKL'}));localStorage.setItem('mv2-rev','3');};
 const {p,errs,calls}=await mk(init,[JSON.stringify(ME)],r=>r.fulfill({status:200,body:'null'}));
 await p.waitForTimeout(8000);console.log('dbg',await p.evaluate(()=>{const C=window.__CL.CLOUD;return JSON.stringify({cred:C.cred,stale:C.stale,err:C.err,busy:C.busy,back:C.back,at:C.at,dirty:C.dirty})}));await p.evaluate(()=>window.__CL.cloudSave(true));await p.waitForTimeout(6000);const xu=await p.evaluate(()=>{try{return JSON.parse(localStorage.getItem('mv2-state')).xu}catch(e){return -1}});
 ok(calls.includes('mv2_restore')&&xu===7777,'mở game mà mây mới hơn thì tự tải (xu '+xu+', gọi '+[...new Set(calls)].join(',')+')');ok(!errs.length,'không lỗi trang '+errs.join(' | '));await p.close();}
console.log('DONE',bad,'chỗ sai');await b.close();})();
