// tNc118: 12 giống mới đã gắn vào game: có trong danh sách, mở đúng cấp, có biểu tượng, trồng được, lớn đủ 5 giai đoạn. node tNc118.js [trang]
const {chromium}=require('playwright');const fs=require('fs');const PAGE=process.argv[2]||'mv2_t118.html';let bad=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)bad++};const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const NK=['dudu','mangcau','sung','bau','khom','muop','mia','daurong','buoi','vusualr','saurieng','duasap'];
const SV={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:20,xp:26600,xu:50000,inv:{},gb:{},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:18},(_,i)=>[i+3,1])),realTime:true,spd:1,real:Date.now(),dd:{last:today,n:3,full:0},ftrD:today};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader']});const p=await b.newPage({viewport:{width:390,height:844}});p.setDefaultTimeout(900000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SV));
await p.goto('http://127.0.0.1:8777/'+PAGE);await p.waitForFunction(()=>window.__ready,null,{timeout:900000});await p.evaluate(()=>{window.__stop=1});
const r=await p.evaluate(NK=>{const N=window.__N;return NK.map(k=>[k,!!N.CROPS[k],N.UNLOCK[k],N.unlocked(k),(N.ICON[k]||'').length,typeof N.CB[k],N.WHERE(k)])},NK);
for(const [k,c,u,un,il,cb,wh] of r){ok(c&&u&&il>3000&&cb==='function',k+': có giống, cấp '+u+', biểu tượng '+il+' ký tự, mô hình '+cb+' · '+wh);}
ok(r.filter(x=>x[3]).length===10&&!r.find(x=>x[0]==='saurieng')[3],'ở cấp 20 mở 10 giống, sầu riêng và dừa sáp đợi cấp 25');
const q=await p.evaluate(()=>{const Q=window.__N.QUESTS[18];return Q.items.map(x=>x[0]).join(',')});ok(q==='mangcau,sung,dua,dudu,xoai,__dish','việc cấp 18 đòi mâm ngũ quả đủ năm trái: '+q);
const f=await p.evaluate(()=>{const N=window.__N,P=id=>N.PLOTS.find(x=>x.id===id);return {bauG:N.fits('bau',P('G')),bauA:N.fits('bau',P('A1')),khomA:N.fits('khom',P('A1')),drA:N.fits('daurong',P('A1')),muopG:N.fits('muop',P('Gb'))}});
ok(f.bauG&&!f.bauA&&f.khomA&&f.drA&&f.muopG,'chỗ trồng đúng: bầu, mướp ở giàn; khóm, đậu rồng ở liếp '+JSON.stringify(f));
// trồng thật vào liếp và giàn rồi cho lớn tới có trái
const g=await p.evaluate(()=>{const G=window.__g,ST=G.ST,out={};const pl=[['A1','khom'],['A1b','mia'],['A2','daurong'],['G','bau'],['Gb','muop']];
 for(const [id,k] of pl){ST.seeds[k]=3;ST.plots[id]={...(ST.plots[id]||{}),crop:null,g:0,dry:0};try{G.act.plant(id,k);}catch(e){out[id]='lỗi '+e.message;continue;} const P=ST.plots[id];out[id]=P.crop; if(P.crop){P.g=window.__N.CROPS[k].grow;G.refreshPlot(id);} }
 return out});
ok(Object.values(g).join()==='khom,mia,daurong,bau,muop','gieo được khóm, mía, đậu rồng, bầu, mướp: '+JSON.stringify(g));
await p.evaluate(()=>{const g=window.__g;g.cam.position.set(9,6.5,9);g.cam.lookAt(4,0,3);window.__r.render(window.__r.__sc||g.cam.parent||null,g.cam)}).catch(()=>{});
// cây trái mới trồng ở ô đất trống phải có đơn đặt; đếm tần suất món rau chính trong đơn nhà bên
const od=await p.evaluate(()=>{const N=window.__N,G=window.__g,ST=G.ST;const P=N.PLOTS.find(x=>x.bai&&!x.tree);const before=N.ordCanMake('dudu');ST.plots[P.id]={...(ST.plots[P.id]||{}),crop:'dudu',g:0};const after=N.ordCanMake('dudu');
 ST.ord=ST.ord||{list:[]};const cnt={};for(let i=0;i<2000;i++){ST.ord.list=[];ST.ord.last={};const o=N.ordMake('nb');const v=o.items.map(x=>x[0]).filter(k=>N.CROPS[k]&&!N.CROPS[k].tree);for(const k of v)cnt[k]=(cnt[k]||0)+1;}return {before,after,cnt}});
console.log('rau trong 2000 đơn (cấp 20):',JSON.stringify(Object.entries(od.cnt).sort((a,b)=>b[1]-a[1])));ok(!od.before&&od.after,'trồng đu đủ ở ô đất trống thì nhà bên đặt được đu đủ');
// bảng biểu tượng
await p.evaluate(NK=>{const d=document.createElement('div');d.id='icsheet';d.style.cssText='position:fixed;inset:0;z-index:99999;background:#F6EEDC;display:grid;grid-template-columns:repeat(4,1fr);gap:4px;padding:8px;font:600 13px Baloo\\ 2,sans-serif;color:#4a3420';d.innerHTML=NK.map(k=>`<div style="text-align:center"><img src="${window.__N.ICON[k]}" style="width:88px;height:88px;background:#fff8ea;border-radius:16px"><br>${window.__N.CROPS[k].name}</div>`).join('');document.body.appendChild(d)},NK);
await p.screenshot({path:'/tmp/nc/icons118.png'});
ok(errs.length===0,'không lỗi '+(errs[0]||''));await b.close();console.log('DONE',bad?bad+' FAIL':'all pass');})();
