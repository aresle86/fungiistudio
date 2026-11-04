// Dò nhấp nháy: chụp N khung liên tiếp (vòng lặp vẫn chạy), đếm pixel đổi giữa hai khung theo ô 32px, so hai trang (v106 / v107).
// node tFlick.js mv2_t106.html mv2_test.html
const {chromium}=require('playwright');const fs=require('fs');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:16,xp:13400,xu:3000,inv:{},gb:{cui:6},seeds:{},plots:{},
 qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1,11:1,12:1,13:1,14:1,15:1,16:1},land:{H1:{st:'own'},H2:{st:'own'},H3:{st:'own'},H4:{st:'cong',w:0,m:900},H5:{st:'cong',w:0,m:900}},open:['H1'],
 ho:{own:1,at:'H3',mat:2,bags:0,t:0,done:0,pct:Date.now()-13*3600e3},ga:{hens:4,rooster:1,trough:4,eggs:0,acc:0,lv:1,brood:null,fixed:1},
 tm:'fixed',ovr:12,realTime:false,spd:1,real:Date.now(),dd:{last:today,n:1,full:0}};
const N=6,CELL=32;
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const res={};
for(const page of process.argv.slice(2)){
 const p=await b.newPage({viewport:{width:1280,height:800},deviceScaleFactor:1});p.setDefaultTimeout(180000);
 await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
 await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
 await p.goto('http://127.0.0.1:8777/'+page+'?dev',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});await p.waitForTimeout(3000);
 await p.evaluate(()=>{document.querySelectorAll('.ddt,.lvup,#intro,.ngoai').forEach(e=>{e.hidden=true});[...document.body.children].forEach(e=>{if(e.tagName!=='CANVAS')e.style.visibility='hidden'});});await p.waitForTimeout(300);
 const frames=[];for(let i=0;i<N;i++){frames.push((await p.screenshot({type:'png'})).toString('base64'));await p.waitForTimeout(90);}
 fs.writeFileSync(`mock/flick_${page}_0.png`,Buffer.from(frames[0],'base64'));fs.writeFileSync(`mock/flick_${page}_1.png`,Buffer.from(frames[1],'base64'));
 const q=await b.newPage({viewport:{width:1280,height:800}});
 const cells=await q.evaluate(async({frames,CELL})=>{const imgs=await Promise.all(frames.map(f=>new Promise(r=>{const im=new Image();im.onload=()=>r(im);im.src='data:image/png;base64,'+f;})));
  const W=imgs[0].width,H=imgs[0].height,cv=document.createElement('canvas');cv.width=W;cv.height=H;const g=cv.getContext('2d',{willReadFrequently:true});
  const data=imgs.map(im=>{g.drawImage(im,0,0);return g.getImageData(0,0,W,H).data;});
  const cx=Math.ceil(W/CELL),cy=Math.ceil(H/CELL),acc=new Float32Array(cx*cy);
  for(let f=1;f<data.length;f++){const a=data[f-1],c=data[f];for(let y=0;y<H;y++)for(let x=0;x<W;x++){const i=(y*W+x)*4;const d=Math.abs(a[i]-c[i])+Math.abs(a[i+1]-c[i+1])+Math.abs(a[i+2]-c[i+2]);if(d>60)acc[((y/CELL)|0)*cx+((x/CELL)|0)]+=1;}}
  const out=[];for(let i=0;i<acc.length;i++)if(acc[i]>0)out.push([(i%cx)*CELL,((i/cx)|0)*CELL,Math.round(acc[i]/(data.length-1))]);return out;},{frames,CELL});
 res[page]=Object.fromEntries(cells.map(([x,y,n])=>[x+','+y,n]));
 console.log(page,'cells changing:',cells.length,'total px/frame:',cells.reduce((a,c)=>a+c[2],0));
 await q.close();await p.close();}
const [A,B]=Object.keys(res);if(B){const rows=[];for(const k of new Set([...Object.keys(res[A]),...Object.keys(res[B])])){const a=res[A][k]||0,c=res[B][k]||0;if(c-a>40)rows.push([k,a,c]);}
 rows.sort((p,q)=>(q[2]-q[1])-(p[2]-p[1]));console.log('cells worse in',B,'(x,y a→b):');rows.slice(0,40).forEach(r=>console.log(' ',r.join(' ')));}
await b.close();})();
