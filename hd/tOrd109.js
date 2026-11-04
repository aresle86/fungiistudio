// v109: đo thành phần đơn hàng xóm theo cấp + chạy thử ấp gà, lò ấp vịt. PAGE=mv2_t109.html node tOrd109.js
const {chromium}=require('playwright');const PAGE=process.env.PAGE||'mv2_t109.html';
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const base=(lv,extra)=>Object.assign({v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv,xp:0,xu:3000,inv:{},gb:{},seeds:{},plots:{},qd:Object.fromEntries(Array.from({length:Math.max(0,lv-2)},(_, i)=>[i+3,1])),land:{H1:{st:'own'}},open:['H1'],ga:{hens:4,rooster:1,trough:8,eggs:6,acc:0,lv:1,brood:null,fixed:1},vit:{n:4,trough:8,eggs:0,acc:0,lv:1,fixed:lv>=6?1:0},tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}},extra);
const P12={nong:{own:1,at:'H1',trays:[],done:2,made:{otkho:1,chuoiphoi:1}},khap:{own:1,at:'H1',jars:[],done:1,made:{dacai:1,hotvit:1}},say:{own:1,at:'H1',trays:[],done:1,made:{xoaisay:1}},bep:{lit:0,pots:[null,null],made:{canhchua:1,cakho:1}}};
const CASES=[['lv3',base(3,{})],['lv5',base(5,{})],['lv8',base(8,{nong:P12.nong,khap:{own:1,at:'H1',jars:[],done:1,made:{dacai:1}},bep:P12.bep})],['lv12',base(12,P12)],['lv16',base(16,Object.assign({},P12,{lo:{t:0,on:0,done:1,hatch:0,lon:1},ga:{hens:6,rooster:1,trough:8,eggs:0,acc:0,lv:2,brood:null,fixed:1,gatrong:1}}))]];
let bad=0;const ok=(c,m)=>{console.log((c?'OK ':'SAI ')+m);if(!c)bad++;};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
for(const [tag,SAVE] of CASES){const p=await b.newPage({viewport:{width:600,height:400}});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded',timeout:120000});await p.waitForFunction(()=>window.__ready,null,{timeout:400000});
 const r=await p.evaluate(()=>{const O=window.__O;window.__stop=true;const cat=k=>O.DISH[k]?'món nấu':O.PHOI[k]||O.MUOI[k]||O.SAY[k]?'chế biến':(k==='trungga'||k==='trungvit')?'trứng':O.FISHK[k]?'cá':k==='gatrong'||k==='hotvitlon'?'đặc biệt':O.CROPS[k]&&O.CROPS[k].tree?'trái cây':O.CROPS[k]?'RAU':'?';
  const c={},kinds=new Set();let n=0,veg=0,maxFish=0,orders=0,bad=[];
  for(let run=0;run<200;run++){O.ST.ord={list:[],acc:0,first:1};for(let j=0;j<3;j++){const o=O.ordMake();O.ST.ord.list.push(o);orders++;let f=0;for(const [k,q] of o.items){c[cat(k)]=(c[cat(k)]||0)+1;n++;kinds.add(k);if(!O.ordCanMake(k))bad.push(k);} if(o.items.some(([k])=>O.CROPS[k]&&!O.CROPS[k].tree))veg++;}
   const fishAll=O.ST.ord.list.reduce((a,o)=>a+o.items.reduce((s,[k,q])=>s+(O.FISHK[k]?q:0),0),0);maxFish=Math.max(maxFish,fishAll);}
  return {share:Object.fromEntries(Object.entries(c).map(([k,v])=>[k,Math.round(v/n*100)+'%'])),withVeg:Math.round(veg/orders*100),distinct:kinds.size,maxFish,bad:[...new Set(bad)],sample:O.ST.ord.list.map(o=>o.who+': '+o.why+' · '+o.items.map(x=>x.join('×')).join(', '))};});
 console.log(tag,JSON.stringify(r.share),'đơn có rau',r.withVeg+'%','loại món',r.distinct,'cá tối đa',r.maxFish);r.sample.forEach(x=>console.log('   ',x));
 ok(r.withVeg>=90,tag+' ≥90% đơn có rau');ok(r.maxFish<=3,tag+' cá trong 3 đơn ≤ 3');ok(!r.bad.length,tag+' chỉ đặt món làm được '+r.bad.join(','));
 if(tag==='lv8'){ // ấp gà: để trứng, nở, lớn
  const g=await p.evaluate(()=>{const O=window.__O,g=O.ST.ga;g.eggs=6;O.ga.brood();const a={eggs:g.eggs,brood:JSON.stringify(g.brood)};O.gaSim(O.GA.brood+1);a.after1=JSON.stringify(g.brood);const h0=g.hens,r0=g.rooster;O.gaSim(O.GA.grow+1);a.res=JSON.stringify(g.res);a.hens=[h0,g.hens];a.roo=[r0,g.rooster];a.brood2=g.brood;return a;});
  console.log('   ấp gà',JSON.stringify(g));ok(g.eggs===2&&/"n":4/.test(g.brood),'ổ chuồng cấp 1 để 4 trứng');ok(/"stage":"chick"/.test(g.after1),'10 tiếng thì nở');ok(g.res&&g.brood2==null,'12 tiếng thì lớn, có thẻ kết quả');
  const d=await p.evaluate(()=>{const O=window.__O,g=O.ST.ga;g.buyD='';g.lv=2;const x0=O.ST.xu,h0=g.hens;O.ga.buy();const h1=g.hens;O.ga.buy();return [h0,h1,g.hens];});ok(d[1]===d[0]+1&&d[2]===d[1],'chợ mỗi ngày 1 gà mái tơ '+d);}
 if(tag==='lv16'){const l=await p.evaluate(()=>{const O=window.__O,L=O.ST.lo;O.ST.inv.trungvit=8;O.ST.gb.cui=3;O.lo.put();const T=L.T||L.t;L.t=T*.3;O.lo.lon();return [O.ST.inv.hotvitlon,L.on];});ok(l[0]>=4&&!l[1],'lò ấp lấy ra hột vịt lộn '+l);}
 ok(!errs.length,tag+' không lỗi trang '+errs.slice(0,2).join(' | '));await p.close();}
console.log(bad?`XONG · ${bad} SAI`:'XONG · tất cả đúng');await b.close();})();
