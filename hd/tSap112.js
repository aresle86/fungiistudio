// Test v112 Sắp vườn trên game thật: nhấn giữ kéo từng loại món, hủy, cất, chế độ Sắp vườn, khay Túi đồ, bảng ô trống gọn.
// node tSap112.js  (PAGE=mv2_t112a.html)  → in PASS/FAIL từng bước, chụp hình vào ../hud16/t112_*.png
const {chromium}=require('playwright');const PAGE=process.env.PAGE||'mv2_t112a.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const own=Object.fromEntries(Array.from({length:12},(_,i)=>['H'+(i+1),{st:'own'}]));
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1,sap1:1},player:{av:1,name:'Q',garden:'Q'},lv:13,xp:9400,xu:3000,inv:{},gb:{},seeds:{cai:3},plots:{},
 qd:Object.fromEntries(Array.from({length:11},(_,i)=>[i+3,1])),land:own,open:['H4','H8'],
 nong:{own:1,at:'H1',trays:[{T:14400,k:'otkho',t:100,fast:false},null,null,null],done:2,made:{}},khap:{own:1,at:'H2',jars:[null,null],done:0,made:{}},
 dc:{rao:'rao_tre',ga:'ga_tre',vit:'vit_mac',own:{},bag:{sanh:1},items:[{k:'ghe_da',at:'H3'}]},
 ft:{vusua:{st:4,told:4,t:Date.now()}},big:{},tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
let fails=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)fails++;};
for(const [tag,vw] of [['ph',{width:390,height:740}],['pc',{width:1280,height:800}]]){
 const p=await b.newPage({viewport:vw,deviceScaleFactor:2});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));p.on('console',m=>{if(m.type()==='warning'&&/sap|tick/.test(m.text()))errs.push(m.text().slice(0,200))});
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+PAGE,{timeout:300000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});await p.waitForTimeout(1500);
 await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>e.hidden=true);try{window.__x.closeSheet&&window.__x.closeSheet()}catch(e){}});
 const pan=async(dx=0,dz=0)=>{await p.evaluate(([dx,dz])=>{const PL=window.__G.PLOTS.filter(q=>/^H([1-9]|1[0-2])$/.test(q.id));let x=0,z=0;for(const q of PL){x+=(q.b[0]+q.b[2])/2;z+=(q.b[1]+q.b[3])/2;}x/=PL.length;z/=PL.length;const c=window.__ctl;const ex=x-c.target.x+dx,ez=z-c.target.z+dz;c.target.x+=ex;c.target.z+=ez;c.object.position.x+=ex;c.object.position.z+=ez;c.update();},[dx,dz]);await p.waitForTimeout(900);};
 const at=id=>p.evaluate(id=>{const T=window.__FT.T,cam=window.__ctl.object,q=window.__G.PLOTS.find(q=>q.id===id);const v=new T.Vector3((q.b[0]+q.b[2])/2,0,(q.b[1]+q.b[3])/2).project(cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];},id);
 const ST=()=>p.evaluate(()=>{const S=window.__O.ST;return {nong:S.nong.at,khap:S.khap.at,dc:S.dc.items.map(i=>i.k+'@'+i.at).join(','),bag:JSON.stringify(S.dc.bag),big:JSON.stringify(S.big),xu:S.xu,open:S.open.join(','),say:S.say&&S.say.at,ntray:S.nong.trays[0]&&S.nong.trays[0].k};});
 const hold=async(a,bb,ms=650)=>{await p.mouse.move(a[0],a[1]);await p.mouse.down();await p.waitForTimeout(ms);for(let i=1;i<=8;i++){await p.mouse.move(a[0]+(bb[0]-a[0])*i/8,a[1]+(bb[1]-a[1])*i/8);await p.waitForTimeout(30);}};
 const vis=sel=>p.evaluate(sel=>{const e=document.querySelector(sel);return !!e&&!e.hidden&&getComputedStyle(e).visibility!=='hidden'&&e.getBoundingClientRect().width>0},sel);
 await pan();
 // 1. kéo nong H1 → H6, hiện 3 nút, Hủy là về chỗ cũ
 await hold(await at('H1'),await at('H6'));await p.waitForTimeout(150);await p.screenshot({path:`../hud16/t112_${tag}_1keo.png`});console.log('DBG drag',tag,await p.evaluate(()=>{const g=document.querySelector('#sapGhost'),r=g.getBoundingClientRect(),sv=document.querySelector('#sapSvg');return JSON.stringify({gh:g.hidden,src:(g.src||'').slice(0,30),r:[r.left|0,r.top|0,r.width|0],poly:sv.querySelectorAll('polygon').length,svh:sv.hasAttribute('hidden')})}));await p.mouse.up();await p.waitForTimeout(300);
 let s=await ST();ok(s.nong==='H6',`${tag} kéo nong H1→H6 (${s.nong})`);ok(await p.waitForFunction(()=>{const e=document.querySelector('#sapBtns');return e&&!e.hidden},null,{timeout:6000}).then(()=>true,()=>false),`${tag} hiện 3 nút sau khi thả`);ok(s.ntray==='otkho',`${tag} đồ đang phơi đi theo nong`);
 await p.screenshot({path:`../hud16/t112_${tag}_2tha.png`});
 await p.click('#sapBtns [data-d="no"]');await p.waitForTimeout(300);s=await ST();ok(s.nong==='H1',`${tag} Hủy: nong về H1 (${s.nong})`);ok(!(await vis('#sapBtns')),`${tag} nút ẩn sau Hủy`);
 // 2. kéo nong vô ô có liếp: không được, giữ nguyên
 await hold(await at('H1'),await at('H4'));await p.waitForTimeout(150);ok(await vis('#sapTip'),`${tag} rê qua liếp: hiện lý do`);await p.screenshot({path:`../hud16/t112_${tag}_3sai.png`});await p.mouse.up();await p.waitForTimeout(300);
 s=await ST();ok(s.nong==='H1',`${tag} thả vô liếp: không dời (${s.nong})`);
 // 3. kéo ghế đá H3 → H7, bấm Cất: vô túi
 await hold(await at('H3'),await at('H7'));await p.mouse.up();await p.waitForTimeout(300);s=await ST();ok(s.dc==='ghe_da@H7',`${tag} kéo ghế đá H3→H7 (${s.dc})`);
 await p.click('#sapBtns [data-d="box"]');await p.waitForTimeout(300);s=await ST();ok(s.dc===''&&/ghe_da/.test(s.bag),`${tag} Cất: ghế đá vô túi (${s.bag})`);
 // 4. kéo khạp H2 → H5, chạm chỗ khác là giữ (✓ ngầm)
 await hold(await at('H2'),await at('H5'));await p.mouse.up();await p.waitForTimeout(300);await p.click('#sapBtns [data-d="ok"]');await p.waitForTimeout(200);s=await ST();ok(s.khap==='H5',`${tag} khạp H2→H5, Đặt (${s.khap})`);
 // 5. bảng ô trống gọn ngoài chế độ
 const c2=await at('H2');await p.mouse.click(c2[0],c2[1]);await p.waitForTimeout(500);ok(await p.evaluate(()=>!!document.querySelector('#shB [data-a="sapgo"]')&&!!document.querySelector('#shB [data-a="openbed"]')),`${tag} bảng ô trống: Đắp liếp + Sắp vườn`);
 ok(await p.evaluate(()=>!document.querySelector('#shB [data-a="obuy"],#shB [data-a="ohere"]')),`${tag} bảng ô trống gọn, không còn danh sách dài`);
 await p.screenshot({path:`../hud16/t112_${tag}_4bang.png`});
 // 6. vô chế độ Sắp vườn từ bảng
 await p.click('#shB [data-a="sapgo"]');await p.waitForTimeout(1500);ok(await vis('#sapBar')&&await vis('#sapTray'),`${tag} chế độ Sắp vườn mở: thanh + khay`);ok(!(await vis('#nxq')),`${tag} HUD ẩn trong chế độ`);
 await pan();const nplus=await p.evaluate(()=>document.querySelectorAll('#sapLay .sapplus').length);ok(nplus>=4,`${tag} có nút + trên ô trống (${nplus})`);
 await p.screenshot({path:`../hud16/t112_${tag}_5sap.png`});
 // 7. chạm + ở H2 → chip, bấm Liếp → đắp liếp
 const c22=await at('H2');await p.mouse.click(c22[0],c22[1]);await p.waitForTimeout(300);ok(await p.waitForFunction(()=>{const e=document.querySelector('#sapChips');return e&&!e.hidden},null,{timeout:6000}).then(()=>true,()=>false),`${tag} chạm ô trống: bung chip`);await p.screenshot({path:`../hud16/t112_${tag}_6chip.png`});
 await p.click('#sapChips [data-c="liep"]');await p.waitForTimeout(400);s=await ST();ok(s.open.split(',').includes('H2'),`${tag} chip Liếp: đắp liếp H2 (${s.open})`);
 // 8. kéo chậu sanh từ túi ra H6
 const it=await p.evaluate(()=>{const e=[...document.querySelectorAll('#sapTray .it')].find(x=>/Sanh|sanh/i.test(x.textContent));if(!e)return null;const r=e.getBoundingClientRect();return [r.left+r.width/2,r.top+r.height/2];});
 ok(!!it,`${tag} khay có chậu sanh`);if(it){await hold(it,await at('H3'),80);await p.mouse.up();await p.waitForTimeout(400);s=await ST();ok(/sanh@H3/.test(s.dc),`${tag} kéo sanh từ túi ra H3 (${s.dc})`);}
 // 9. kéo khạp vô khay = cất
 const tr=await p.evaluate(()=>{const r=document.querySelector('#sapTray').getBoundingClientRect();return [r.left+r.width/2,r.top+20];});
 await hold(await at('H5'),tr,400);await p.mouse.up();await p.waitForTimeout(400);s=await ST();ok(s.khap===null,`${tag} kéo khạp vô khay: cất (${s.khap})`);
 ok(await p.evaluate(()=>[...document.querySelectorAll('#sapTray .it')].some(x=>/Khạp/.test(x.textContent))),`${tag} khạp hiện trong khay`);
 await p.screenshot({path:`../hud16/t112_${tag}_7khay.png`});
 // 10. kéo cây vú sữa (đang ở bãi cỏ) vô khối 2×2 H9-H10-… rồi Về chỗ cũ
 await p.evaluate(()=>{const q=window.__G.PLOTS.find(q=>q.id==='H6'),c=window.__ctl;const x=(-3.7+(q.b[0]+q.b[2])/2)/2,z=(5.9+(q.b[1]+q.b[3])/2)/2;const ex=x-c.target.x,ez=z-c.target.z;c.target.x+=ex;c.target.z+=ez;c.object.position.x+=ex;c.object.position.z+=ez;c.object.zoom*=.8;c.object.updateProjectionMatrix();c.update();});await p.waitForTimeout(1000);
 const vs=await p.evaluate(()=>{const T=window.__FT.T,cam=window.__ctl.object;const v=new T.Vector3(-3.7,.6,5.9).project(cam);return [(v.x+1)/2*innerWidth,(1-v.y)/2*innerHeight];});
 const free=await p.evaluate(()=>{const S=window.__O.ST;return ['H9','H10','H11','H12','H7','H8'].filter(i=>!S.open.includes(i));});
 if(vs[0]>0&&vs[0]<innerWidthSafe(vw)&&vs[1]>0&&vs[1]<vw.height){await hold(vs,await at('H10'),400);await p.waitForTimeout(150);await p.screenshot({path:`../hud16/t112_${tag}_8cay.png`});await p.mouse.up();await p.waitForTimeout(400);s=await ST();ok(/vusua/.test(s.big),`${tag} kéo cây vú sữa vô 2×2 (${s.big})`);
   if(await vis('#sapBtns')){await p.click('#sapBtns [data-d="box"]');await p.waitForTimeout(300);s=await ST();ok(!/"at":"H/.test(s.big),`${tag} Về chỗ cũ (${s.big})`);} }
 else console.log(`SKIP ${tag} cây vú sữa ngoài màn hình`,vs);
 // 11. Xong
 await p.click('#sapOk');await p.waitForTimeout(400);ok(!(await vis('#sapBar'))&&!(await vis('#sapTray')),`${tag} Xong: thoát chế độ`);ok(await p.evaluate(()=>!document.querySelector('#sapLay .sapplus')),`${tag} hết nút + khi thoát`);
 ok(errs.length===0,`${tag} không lỗi trang: ${errs.slice(0,3).join(' | ')}`);
 await p.close();}
console.log(fails?`DONE ${fails} FAIL`:'DONE all pass');await b.close();})();
function innerWidthSafe(vw){return vw.width}
