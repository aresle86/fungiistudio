const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:1100,height:600}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
const res=await p.evaluate(async()=>{window.__stop=true;const I=window.__ICONS,U=window.__UIC;const src=[['Hạt',U.seedbag],['Sổ',U.so],['Chợ',I.cho],['Rơm',I.rom],['Cải',I.cai],['Cá rô',I.caro]];
 const load=u=>new Promise(r=>{const im=new Image();im.onload=()=>r(im);im.src=u;});
 const toon=async u=>{const im=await load(u),W=im.width,H=im.height,c=document.createElement('canvas');c.width=W;c.height=H;const x=c.getContext('2d');x.drawImage(im,0,0);const d=x.getImageData(0,0,W,H),D=d.data;
  for(let i=0;i<D.length;i+=4){if(D[i+3]<8)continue;let r=D[i]/255,g=D[i+1]/255,b2=D[i+2]/255;const mx=Math.max(r,g,b2),mn=Math.min(r,g,b2);let h=0,s=0,l=(mx+mn)/2;if(mx!==mn){const dd=mx-mn;s=l>.5?dd/(2-mx-mn):dd/(mx+mn);h=mx===r?(g-b2)/dd+(g<b2?6:0):mx===g?(b2-r)/dd+2:(r-g)/dd+4;h/=6;}
   s=Math.min(1,s*1.45+.06);const L=l<.3?.26:l<.52?.44:l<.74?.62:.8;l=L*.75+l*.25;
   const q=l<.5?l*(1+s):l+s-l*s,pp=2*l-q,f=t=>{t=(t+1)%1;return t<1/6?pp+(q-pp)*6*t:t<.5?q:t<2/3?pp+(q-pp)*(2/3-t)*6:pp;};D[i]=f(h+1/3)*255;D[i+1]=f(h)*255;D[i+2]=f(h-1/3)*255;}
  x.putImageData(d,0,0);
  /* sáng viền theo dáng từng vật: điểm ảnh nào có phía trên-trái là khoảng trống (mép hướng về đèn) thì sáng lên, dải mảnh chạy dọc mép hình */
  { const d2=x.getImageData(0,0,W,H),E=d2.data,A=(px,py)=>px<0||py<0||px>=W||py>=H?0:D[(py*W+px)*4+3],R=Math.max(2,Math.round(W/45));
    for(let py=0;py<H;py++)for(let px=0;px<W;px++){const i=(py*W+px)*4;if(D[i+3]<128)continue;let e=0;for(let k=1;k<=R;k++){if(A(px-k,py-k)<60){e=1-(k-1)/R;break;}}
     if(!e)continue;const a=.55*e;E[i]=E[i]+(255-E[i])*a;E[i+1]=E[i+1]+(255-E[i+1])*a;E[i+2]=E[i+2]+(255-E[i+2])*a*.85;}
    x.putImageData(d2,0,0);}
  /* nghiêng nhẹ */
  const o=document.createElement('canvas');o.width=W;o.height=H;const y=o.getContext('2d');y.translate(W/2,H/2);y.rotate(-.12);y.drawImage(c,-W/2,-H/2);return await window.__FT3.sticker(o.toDataURL());};
 const out=[];for(const [n,u] of src)out.push([n,await window.__FT3.sticker(u),await toon(u)]);return out;});
await p.setContent('<body style="margin:0;background:#86B06A;font:600 15px sans-serif;color:#2F4A22;padding:16px"><table style="border-spacing:18px 6px"><tr><td></td>'+res.map(r=>`<td style="text-align:center">${r[0]}</td>`).join('')+'</tr><tr><td>Hiện tại</td>'+res.map(r=>`<td><img src="${r[1]}" width="120"></td>`).join('')+'</tr><tr><td>Tô hoạt hình</td>'+res.map(r=>`<td><img src="${r[2]}" width="120"></td>`).join('')+'</tr><tr><td>Cỡ nút</td>'+res.map(r=>`<td style="text-align:center"><img src="${r[1]}" width="56"> <img src="${r[2]}" width="56"></td>`).join('')+'</tr></table></body>');
await p.screenshot({path:'../toon.png'});console.log(errs.join('|')||'no errors',await p.evaluate(()=>0));await b.close();})();
