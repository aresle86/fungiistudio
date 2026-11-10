// v129: chơi lâu trong vườn lớn, bộ nhớ hình (geometry, texture) không được phình dần
// SAVE = đường dẫn bản lưu vườn lớn (json), N = số vòng trồng-hái
const {chromium}=require('playwright');const fs=require('fs');const PAGE=process.env.PAGE||'mv2_t129.html';const N=+(process.env.N||40);
let bad=0;const ok=(c,m)=>{console.log((c?'PASS ':'FAIL ')+m);if(!c)bad++};
(async()=>{const b=await chromium.launch({args:['--use-angle=metal','--enable-gpu','--ignore-gpu-blocklist','--enable-precise-memory-info','--js-flags=--expose-gc']});
const c=await b.newContext({viewport:{width:390,height:844}});const p=await c.newPage();p.setDefaultTimeout(180000);const e=[];p.on('pageerror',x=>e.push(x.message));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
const sv=JSON.parse(fs.readFileSync(process.env.SAVE,'utf8'));sv.real=Date.now();sv.seen={...(sv.seen||{}),hello:1,sap1:1};
await p.addInitScript(s=>{if(sessionStorage.getItem('t'))return;sessionStorage.setItem('t','1');localStorage.clear();localStorage.setItem('mv3d-q','2');localStorage.setItem('mv2-lang','vi');localStorage.setItem('mv2-state',s)},JSON.stringify(sv));
await p.goto('http://127.0.0.1:8777/'+PAGE,{timeout:300000});await p.waitForFunction(()=>window.__ready&&window.__DCX0&&window.__Q,null,{timeout:400000});await p.waitForTimeout(8000);
const cyc=n=>p.evaluate(async n=>{const G=window.__g,Q=window.__Q,X=window.__DCX0.get(),ST=G.ST;let did=0;
 for(let i=0;i<n;i++){ST.seeds.cai=999;ST.seeds.hanh=999;ST.xu=Math.max(ST.xu,99999);
  for(const P of Q.PLOTS){const pl=ST.plots[P.id];if(!pl)continue;try{if(!pl.crop){G.act.plant(P.id,i%2?'cai':'hanh')}else{pl.g=Q.CROPS[pl.crop].grow;pl.moist=1;pl.dead=0;G.refreshPlot(P.id);G.act.harvest(P.id);did++}}catch(x){}}
  try{G.openSheet('set')}catch(x){} await new Promise(r=>setTimeout(r,120));try{G.closeSheet()}catch(x){}
  try{G.sim(300)}catch(x){} for(const P of Q.PLOTS)try{G.refreshPlot(P.id)}catch(x){}
  await new Promise(r=>setTimeout(r,180));}
 if(window.gc)window.gc();await new Promise(r=>setTimeout(r,600));const m=X.r.info.memory;
 return {geo:m.geometries,tex:m.textures,heap:Math.round(performance.memory.usedJSHeapSize/1048576),did,crops:Q.PLOTS.filter(P=>ST.plots[P.id]&&ST.plots[P.id].crop).length,plots:Q.PLOTS.length,calls:X.r.info.render.calls,tri:X.r.info.render.triangles}},n);
const a=await cyc(6);console.log('  sau 6 vòng khởi động',JSON.stringify(a));
const m=await cyc(N);console.log('  sau thêm',N,'vòng',JSON.stringify(m));
const z=await cyc(N);console.log('  sau thêm',N,'vòng nữa',JSON.stringify(z));
ok(m.did>N,'có trồng và hái thật ('+m.did+' lần hái mỗi đợt)');
ok(z.geo-m.geo<=10,'số geometry đứng yên sau khi vườn đã đầy: '+a.geo+' → '+m.geo+' → '+z.geo);
ok(z.tex-a.tex<=Math.max(8,a.tex*.05),'số texture không phình: '+a.tex+' → '+m.tex+' → '+z.tex);
ok(z.heap-m.heap<=Math.max(12,m.heap*.15),'bộ nhớ JS không tăng dần: '+a.heap+' → '+m.heap+' → '+z.heap+' MB');
ok(!e.length,'không lỗi '+e[0]);
console.log(bad?'CÓ SAI '+bad:'DONE all pass');await b.close();process.exit(bad?1:0)})().catch(x=>{console.error('CRASH',x.message.slice(0,300));process.exit(2)});
