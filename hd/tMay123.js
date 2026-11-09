// tMay123: chụp bảng hình mẫu đồ may (nhân vật + Ngoại) ra ../hud16/may_*.png. node tMay123.js
const {chromium}=require('playwright');const fs=require('fs');
const ROWS=[
 ['Bà ba ôm eo (kiểu nữ)',[
  {base:'nang',cut:'om',tay:'dai',fab:'bong',shirt:'#E8B4C0',pat:'bongnhi',prop:null,label:'Vải bông bông nhí'},
  {base:'lanh',cut:'om',tay:'dai',fab:'xita',shirt:'#3E7FC4',pat:'soc',prop:null,label:'Xi-ta sọc'},
  {base:'moc',cut:'om',tay:'dai',fab:'lua',shirt:'#F2E6C8',prop:null,label:'Lụa ngà'},
  {base:'nang',cut:'om',tay:'dai',fab:'lanh',shirt:'#000',pfab:'lanh',pants:'#1A181E',prop:null,hat:'nonla',label:'Lãnh Mỹ A + nón lá'}]],
 ['Bà ba suông, cổ trụ (kiểu nam)',[
  {base:'gio',open:false,cut:'suong',tay:'dai',fab:'bong',shirt:'#EFE6D2',prop:null,khan:['#2B2522','#F2EEE4'],label:'Vải bông + khăn rằn'},
  {base:'song',cut:'suong',tay:'dai',fab:'xita',shirt:'#5E8A4A',prop:null,hat:'taibeo',label:'Xi-ta + nón tai bèo'},
  {base:'dat',cut:'suong',tay:'dai',fab:'lua',shirt:'#B8C8D8',prop:null,hat:'phot',label:'Lụa + mũ phớt'},
  {base:'gio',open:false,cut:'suong',tay:'dai',fab:'lanh',shirt:'#000',pfab:'lanh',pants:'#1A181E',prop:null,khan:['#B5302A','#F2EEE4'],label:'Lãnh Mỹ A + khăn rằn đỏ'}]]];
const NG=[[{},'Hiện tại'],[{ao:'#7A4A6A',fab:'bong',pat:'bongnhi'},'Bông nhí tím'],[{ao:'#3E6E8A',fab:'lua',khan:['#7A2A2A','#FBF7EE']},'Lụa xanh, khăn rằn đỏ'],[{ao:'#000',fab:'lanh',quan:'lanh',hat:'khan',khan:['#2B3446','#FBF7EE']},'Lãnh Mỹ A, khăn trùm đầu']];
(async()=>{const b=await chromium.launch({args:['--use-angle=metal','--enable-gpu','--ignore-gpu-blocklist']});const p=await b.newPage({viewport:{width:1200,height:900}});p.setDefaultTimeout(300000);const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());await p.addInitScript(()=>{localStorage.setItem('mv3d-q','1')});await p.goto('http://127.0.0.1:8777/mv2_mlab.html');await p.waitForFunction('window.__ready');
const av=await p.evaluate(R=>R.map(([t,l])=>[t,l.map(x=>x.label),window.__avLab(l)]),ROWS);const ng=await p.evaluate(N=>N.map(([o,t])=>[t,window.__ngLab(o)]),NG);
const card=(src,t)=>`<div class=c><img src="${src}"><b>${t}</b></div>`;
const html=`<html><head><meta charset="utf-8"></head><body style="margin:0;background:#F6EEDC;font:15px system-ui;color:#4A2F1E;padding:18px"><style>.r{display:flex;gap:10px;margin:6px 0 18px}.c{background:#FFF8EA;border-radius:16px;padding:6px;width:236px;text-align:center}.c img{width:220px;height:280px;display:block;margin:auto}.n img{width:180px;height:210px}h3{margin:4px 0}</style>`+av.map(([t,ls,im])=>`<h3>${t}</h3><div class=r>`+im.map((s,i)=>card(s,ls[i])).join('')+'</div>').join('')+`<h3>Đồ may cho Ngoại</h3><div class="r n">`+ng.map(([t,im])=>card(im[0],t)).join('')+'</div></body></html>';
fs.writeFileSync('lp/may_sheet.html',html);await p.goto('http://127.0.0.1:8777/may_sheet.html');await p.waitForTimeout(500);await p.screenshot({path:'../hud16/may_mau.png',fullPage:true});console.log('errs',errs);await b.close();})();
