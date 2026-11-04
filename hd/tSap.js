// Mock 3 cảnh "Sắp vườn": (1) nhấn giữ kéo cây cổ tích: ô xanh/đỏ + 3 nút ✓ ✕ 📦; (2) chế độ Sắp vườn có thanh trên + khay Túi đồ;
// (3) chạm ô trống ngoài chế độ: bảng gọn. Dựng trên game thật bằng lớp phủ, chưa sửa code. node tSap.js
const {chromium}=require('playwright');const fs=require('fs');fs.mkdirSync('../hud16',{recursive:true});const PAGE=process.env.PAGE||'mv2_t110e.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:13,xp:9400,xu:3000,inv:{},gb:{},seeds:{cai:3},plots:{},qd:Object.fromEntries(Array.from({length:11},(_, i)=>[i+3,1])),
 land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'},H4:{st:'own'},H5:{st:'own'},H6:{st:'own'},H7:{st:'own'},H8:{st:'own'}},open:['H4','H8'],nong:{own:1,at:'H2',trays:[null,null,null,null],done:2,made:{}},ft:{vusua:{st:4,told:4,t:Date.now()}},big:{vusua:{at:'H2'}},tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
const COIN='data:image/svg+xml;utf8,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="#F4C12E" stroke="#4A2F1E" stroke-width="3"/><circle cx="16" cy="16" r="8" fill="none" stroke="#B8860B" stroke-width="2"/></svg>');
const PLUS='data:image/svg+xml;utf8,'+encodeURIComponent('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><circle cx="16" cy="16" r="14" fill="#7DB84A" stroke="#4A2F1E" stroke-width="3"/><path d="M16 9v14M9 16h14" stroke="#fff" stroke-width="4" stroke-linecap="round"/></svg>');
const SVG={ok:'<svg viewBox="0 0 24 24" width="22" height="22"><path d="M5 12.5l4.5 4.5L19 7.5" fill="none" stroke="#fff" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round"/></svg>',
 no:'<svg viewBox="0 0 24 24" width="20" height="20"><path d="M6 6l12 12M18 6L6 18" stroke="#fff" stroke-width="3.6" stroke-linecap="round"/></svg>',
 box:'<svg viewBox="0 0 24 24" width="24" height="24"><path d="M3 8l9-4 9 4v9l-9 4-9-4z" fill="#E0A95C" stroke="#4A2F1E" stroke-width="2" stroke-linejoin="round"/><path d="M3 8l9 4 9-4M12 12v9" fill="none" stroke="#4A2F1E" stroke-width="2"/></svg>'};
const CSS=`
.mk-cell{position:fixed;z-index:4;pointer-events:none;border-radius:6px;transform:translate(-50%,-50%) rotateX(55deg) rotateZ(45deg)}
.mk-ok{background:rgba(125,184,74,.45);border:3px solid #4F7D44}.mk-no{background:rgba(217,72,58,.35);border:3px solid #9C3620}
.mk-btns{position:fixed;z-index:6;display:flex;gap:10px;transform:translate(-50%,0)}
.mk-btns{flex-direction:column;align-items:center;gap:6px}.mk-btns .r{display:flex;gap:10px}.mk-btns em{font:600 12px var(--f-body);font-style:normal;color:#4A2F1E;background:#FFF8EA;border:2px solid #4A2F1E;border-radius:8px;padding:1px 8px}
.mk-btns b{width:44px;height:44px;border-radius:50%;border:2px solid #4A2F1E;box-shadow:0 3px 0 #4A2F1E;display:flex;align-items:center;justify-content:center;font:400 20px var(--f-game);color:#fff}
.mk-btns .y{background:#7DB84A}.mk-btns .n{background:#D9483A}.mk-btns .s{background:#FFF8EA;color:#4A2F1E}
.mk-tip{position:fixed;z-index:6;transform:translate(-50%,-100%);background:#fff;border:2px solid #4A2F1E;border-radius:8px;box-shadow:0 2px 0 #4A2F1E;padding:3px 8px;font:600 12px var(--f-body);color:#9C3620;white-space:nowrap}
.mk-lift{position:fixed;z-index:5;transform:translate(-50%,-50%);width:120px;height:26px;border-radius:50%;background:rgba(43,52,70,.25);filter:blur(2px)}
.mk-top{position:fixed;left:50%;top:calc(12px + env(safe-area-inset-top,0px));transform:translateX(-50%);z-index:7;display:flex;align-items:center;gap:10px;background:#FFF8EA;border:2px solid #4A2F1E;border-radius:14px;box-shadow:0 3px 0 #4A2F1E;padding:6px 6px 6px 14px;font:400 15px var(--f-game);color:#4A2F1E;white-space:nowrap}
.mk-top i{font-style:normal;background:#7DB84A;color:#FBF7EE;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 2px 0 #4A2F1E;padding:4px 14px;text-shadow:0 1px 0 #4A2F1E}
.mk-ghost{position:fixed;z-index:6;transform:translate(-50%,-50%);filter:drop-shadow(0 6px 0 rgba(43,52,70,.25))}.mk-ghost img{width:84px;height:84px}
.mk-from{border:3px dashed #4A2F1E;background:rgba(255,248,234,.35)}.mk-sel{border:3px solid #F2C64A;background:rgba(242,198,74,.3)}
.mk-top .ic{width:28px;height:28px;border-radius:8px;background:#F2C64A;border:2px solid #4A2F1E;display:flex;align-items:center;justify-content:center}
.mk-sheet{box-sizing:border-box;position:fixed;left:50%;transform:translateX(-50%);width:min(360px,calc(100vw - 32px));bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:7;background:#FFF8EA;border:2px solid #4A2F1E;border-radius:16px;box-shadow:0 3px 0 #4A2F1E;padding:20px 12px 12px;display:flex;flex-direction:column;gap:10px}
.mk-sheet>small{position:absolute;top:-12px;left:14px;background:#B9D79F;border:2px solid #4A2F1E;border-radius:8px;padding:2px 10px;font:400 13px var(--f-game);color:#4A2F1E}
.mk-sheet .x{position:absolute;top:-14px;right:-8px;width:32px;height:32px;border-radius:50%;background:#D9483A;border:2px solid #4A2F1E;box-shadow:0 2px 0 #4A2F1E;display:flex;align-items:center;justify-content:center;padding:0}
.mk-sheet .main{display:flex;align-items:center;gap:12px;background:#7DB84A;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 3px 0 #4A2F1E;padding:8px 12px}
.mk-sheet .main img{width:44px;height:44px;background:#FFF8EA;border:2px solid #4A2F1E;border-radius:10px;padding:3px}
.mk-sheet .main span{display:flex;flex-direction:column;gap:1px}.mk-sheet .main b{font:400 18px var(--f-game);color:#FBF7EE;text-shadow:0 1px 0 #4A2F1E}.mk-sheet .main em{font:600 12px var(--f-body);font-style:normal;color:#FBF7EE}
.mk-sheet .alt{display:flex;align-items:center;gap:8px;padding:2px 2px 0;font:600 13px var(--f-body);color:#4A2F1E}
.mk-sheet .alt .ics{display:flex}.mk-sheet .alt .ics img{width:26px;height:26px;margin-right:-6px;background:#fff;border:2px solid #4A2F1E;border-radius:50%;padding:2px}
.mk-sheet .alt>span:nth-child(2){flex:1;margin-left:8px}
.mk-sheet .alt i{font:400 13px var(--f-game);font-style:normal;background:#F2C64A;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 2px 0 #4A2F1E;padding:5px 10px;white-space:nowrap}
.mk-tray{box-sizing:border-box;position:fixed;left:8px;right:8px;margin:0 auto;max-width:max-content;bottom:calc(10px + env(safe-area-inset-bottom,0px));z-index:7;background:#FFF8EA;border:2px solid #4A2F1E;border-radius:16px;box-shadow:0 3px 0 #4A2F1E;padding:16px 8px 8px}
.mk-tray>small{position:absolute;top:-11px;left:12px;background:#F2C64A;border:2px solid #4A2F1E;border-radius:8px;padding:2px 9px;font:400 12px var(--f-game);color:#4A2F1E}
.mk-tray .row{display:flex;flex-wrap:wrap;gap:12px 8px;padding-top:4px}
.mk-tray .it{flex:none;width:68px;background:#fff;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 3px 0 #4A2F1E;padding:6px 2px 4px;display:flex;flex-direction:column;align-items:center;gap:2px;font:400 12px/1.1 var(--f-game);color:#4A2F1E;text-align:center;position:relative}
.mk-tray .it img{width:36px;height:36px}.mk-tray .it .n{position:absolute;top:-7px;right:-6px;min-width:20px;height:20px;border-radius:10px;background:#D9483A;color:#fff;border:2px solid #4A2F1E;box-sizing:border-box;font:400 12px/16px var(--f-game);text-align:center}
.mk-tray .it.buy{background:#F3FBE9}
.mk-plus{position:fixed;z-index:6;transform:translate(-50%,-50%)}.mk-plus b{display:flex;width:36px;height:36px;border-radius:50%;background:#7DB84A;border:2px solid #4A2F1E;box-shadow:0 3px 0 #4A2F1E;align-items:center;justify-content:center;padding:0;color:#fff;filter:drop-shadow(0 1px 0 #4A2F1E)}.mk-plus.on b{background:#F2C64A;color:#4A2F1E;filter:none}
.mk-chips{position:fixed;z-index:6;transform:translate(-50%,-50%);display:flex;gap:4px}
.mk-chips span{background:#fff;border:2px solid #4A2F1E;border-radius:10px;box-shadow:0 3px 0 #4A2F1E;padding:5px 8px;font:400 12px var(--f-game);color:#4A2F1E;display:flex;align-items:center;gap:3px}
.mk-chips span img{width:20px;height:20px}
body.mk-tr .ui.bot,body.mk-tr #tray{visibility:hidden!important}
body.mk-sap .ui.bot,body.mk-sap .ui.top,body.mk-sap #nxq,body.mk-sap #tray{visibility:hidden!important}
`;
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,vw] of [['ph',{width:390,height:664}],['pc',{width:1280,height:800}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:tag==='ph'?2:1.25,hasTouch:tag==='ph'});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:300000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(1500);
 await p.evaluate(()=>{const PL=window.__G.PLOTS.filter(q=>/^H[1-8]$/.test(q.id));let x=0,z=0;for(const q of PL){x+=(q.b[0]+q.b[2])/2;z+=(q.b[1]+q.b[3])/2;}x/=PL.length;z/=PL.length;const c=window.__ctl,dx=x-c.target.x,dz=z-c.target.z+(innerWidth<600?.8:.4),dx2=innerWidth<600?.7:0;c.target.x+=dx+dx2;c.target.z+=dz;c.object.position.x+=dx+dx2;c.object.position.z+=dz;c.update();});await p.waitForTimeout(1200);
 const setup=async(scene)=>p.evaluate(([c,scene,COIN,PLUS,SV])=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});document.querySelectorAll('.mk').forEach(e=>e.remove());document.body.classList.remove('mk-sap','sheeton','mk-tr');
  let st=document.getElementById('mkcss');if(!st){st=document.createElement('style');st.id='mkcss';document.body.appendChild(st);}st.textContent=c;
  const T=window.__FT.T,cam=window.__ctl.object,PL=window.__G.PLOTS,I=window.__x.ICON;const prj=(x,z,y=0)=>{const v=new T.Vector3(x,y,z).project(cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];};
  const P=id=>PL.find(q=>q.id===id),ctr=id=>{const q=P(id);return [(q.b[0]+q.b[2])/2,(q.b[1]+q.b[3])/2];},size=id=>{const q=P(id),a=prj(q.b[0],q.b[1]),c=prj(q.b[2],q.b[3]);return Math.max(30,Math.hypot(c[0]-a[0],c[1]-a[1])*.62);};
  const poly=(ids,fill,stroke,dash)=>{let sv=document.getElementById('mksvg');if(!sv){sv=document.createElementNS('http://www.w3.org/2000/svg','svg');sv.id='mksvg';sv.setAttribute('class','mk');sv.style.cssText='position:fixed;inset:0;width:100vw;height:100vh;z-index:4;pointer-events:none';document.body.appendChild(sv);}
   for(const id of ids){const b=P(id).b,i=.04,pts=[[b[0]+i,b[1]+i],[b[2]-i,b[1]+i],[b[2]-i,b[3]-i],[b[0]+i,b[3]-i]].map(([x,z])=>prj(x,z,.03).join(',')).join(' ');sv.insertAdjacentHTML('beforeend',`<polygon points="${pts}" fill="${fill}" stroke="${stroke}" stroke-width="3" stroke-linejoin="round" ${dash?'stroke-dasharray="7 5"':''}/>`);}};
  const blk=ids=>{const bs=ids.map(id=>P(id).b);return [Math.min(...bs.map(b=>b[0])),Math.min(...bs.map(b=>b[1])),Math.max(...bs.map(b=>b[2])),Math.max(...bs.map(b=>b[3]))];};
  const add=(cls,html,x,y,w)=>{const d=document.createElement('div');d.className='mk '+cls;d.innerHTML=html||'';d.style.left=x+'px';d.style.top=y+'px';if(w){d.style.width=w+'px';d.style.height=w+'px';}document.body.appendChild(d);return d;};
  const hideBub=on=>{for(const g of (window.__BUBALL||[]))g.traverse(m=>{if(m.material){if(m.userData.mv0==null)m.userData.mv0=m.material.visible;m.material.visible=on?false:m.userData.mv0;}});};hideBub(scene!=='trong');
  if(scene==='keo'){poly(['H1','H5'],'rgba(125,184,74,.35)','#4F7D44',1);poly(['H4','H8'],'rgba(217,72,58,.35)','#9C3620');
   {const B=blk(['H2','H3','H6','H7']);let sv=document.getElementById('mksvg');const pts=[[B[0],B[1]],[B[2],B[1]],[B[2],B[3]],[B[0],B[3]]].map(([x,z])=>prj(x,z,.03).join(',')).join(' ');sv.insertAdjacentHTML('beforeend',`<polygon points="${pts}" fill="rgba(125,184,74,.45)" stroke="#2F5A2A" stroke-width="4" stroke-linejoin="round"/>`);
    const [sx,sy]=prj((B[0]+B[2])/2,B[3],0);add('mk-btns',`<div class="r"><b class="y">${SV.ok}</b><b class="n">${SV.no}</b><b class="s">${SV.box}</b></div>`,sx,sy+18);}
   {const [x,z]=ctr('H4'),[sx,sy]=prj(x,z);{const t=add('mk-tip','Đang có liếp',Math.min(sx,innerWidth-70),sy-6);}}}
  if(scene==='sap'){document.body.classList.add('mk-sap');{const t=add('mk-top','<span class="ic"><svg viewBox="0 0 24 24" width="18" height="18"><path d="M4 9l8-4 8 4-8 4zM4 15l8-4 8 4-8 4z" fill="#FFF8EA" stroke="#4A2F1E" stroke-width="1.8" stroke-linejoin="round"/></svg></span>Đang sắp vườn <i>Xong</i>',0,0);t.style.left='';t.style.top='';}
   poly(['H1','H5'],'rgba(255,248,234,.25)','#FFF8EA',1);
   {const [x,z]=ctr('H5'),[sx,sy]=prj(x,z);add('mk-plus','<b><svg viewBox="0 0 24 24" width="18" height="18"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg></b>',sx,sy);}
   {const [x,z]=ctr('H1'),[sx,sy]=prj(x,z);add('mk-plus on','<b><svg viewBox="0 0 24 24" width="18" height="18"><path d="M12 5v14M5 12h14" stroke="currentColor" stroke-width="4" stroke-linecap="round"/></svg></b>',sx,sy);const ch=add('mk-chips',`<span><img src="${I.cai}">Liếp</span><span><img src="${I.xoai}">Cây</span><span><img src="${I.khoqua}">Giàn</span>`,Math.max(sx,128),sy-44);}
   const it=(ic,t,n,cls='')=>`<div class="it ${cls}"><img src="${ic}">${t}${n?`<span class="n">${n}</span>`:''}</div>`;
   const tr=add('mk-tray',`<small>TÚI ĐỒ · kéo ra vườn</small><div class="row">${it(I.khap,'Khạp',1)}${it(I.nong,'Nong',1)}${it(I.ho,'Hố ủ')}${it(I.chuoi,'Cây chuối',2)}${it(I.matong,'Thùng ong')}${it(PLUS,'Mua thêm','','buy')}</div>`,0,0);tr.style.left='';tr.style.top='';}
  if(scene==='trong'){document.body.classList.add('sheeton','mk-tr');poly(['H5'],'rgba(242,198,74,.4)','#C08A12');
   const sh=add('mk-sheet',`<small>Ô đất trống</small><button class="x">${SV.no}</button><div class="main"><img src="${I.cai}"><span><b>Đắp liếp</b><em>Trồng rau · miễn phí</em></span></div><div class="alt"><span class="ics"><img src="${I.xoai}"><img src="${I.khoqua}"><img src="${I.nong}"></span><span>Đặt cây, giàn, đồ ở đây</span><i>Sắp vườn</i></div>`,0,0);sh.style.left='';sh.style.top='';}

  },[CSS,scene,COIN,PLUS,SVG]);
 await setup('keo');await p.waitForTimeout(700);await p.screenshot({path:`../hud16/${tag}_1_keo.png`});
 await setup('sap');await p.waitForTimeout(700);await p.screenshot({path:`../hud16/${tag}_2_sap.png`});
 await setup('trong');await p.waitForTimeout(700);await p.screenshot({path:`../hud16/${tag}_3_trong.png`});
 console.log(tag,'errors',errs.slice(0,2));await p.close();}
await b.close();})();
