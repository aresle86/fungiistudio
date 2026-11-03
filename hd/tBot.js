const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const DAYS=+process.argv[2]||50, PAGE=process.argv[3]||'mv2_bot.html', OUT=process.argv[4]||'../bot.json';
const p=await b.newPage({viewport:{width:900,height:600}});const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));p.on('console',m=>{if(/RELOADSET/.test(m.text()))console.log(m.text().slice(0,400));if(m.type()==='warning'&&/BOT/.test(m.text()))errs.push(m.text())});
const T0=new Date('2026-11-04T07:30:00+07:00').getTime();
await p.addInitScript(([t0])=>{const RD=Date;let off=t0-RD.now();window.__off=v=>{off=v-RD.now()};class FD extends RD{constructor(...a){if(a.length===0)super(RD.now()+off);else super(...a)}static now(){return RD.now()+off}}window.Date=FD;const ST0=window.setTimeout;window.setTimeout=function(f,ms,...r){try{if(typeof f==='function'&&/reload/.test(f.toString()))console.warn('BOT RELOADSET '+new Error().stack.split('\n').slice(1,5).join(' | '))}catch(e){}return ST0.call(this,f,ms,...r)};
 try{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',JSON.stringify({v:1,eco:2,split:1,qv2:1,seen:{hello:1},player:{av:1,name:'Bot',garden:'Bot'},lv:1,xp:0,xu:100,exp:1,qd:{},inv:{},seeds:{},plots:{},realTime:true,spd:1,real:t0}))}catch(e){}},[T0]);
await p.goto('http://127.0.0.1:8777/'+PAGE,{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.evaluate(()=>{window.__stop=true;document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});});
const VIS=[7.5,12.5,19.5];const lvAt={};let last=T0;const log=[];
for(let d=0;d<DAYS;d++){for(let vi=0;vi<VIS.length;vi++){const t=T0+d*86400e3+(VIS[vi]-7.5)*3600e3;const dt=(t-last)/1000;last=t;
  let st=null;for(let tr=0;tr<4&&!st;tr++){try{st=await p.evaluate(([t,dt,day])=>{window.__off(t);window.__stop=true;const B=window.__bot;B.setGap(5*3600);B.step(dt);B.visit(day);B.step(600);B.visit(day);const S0=window.__g&&window.__g.ST;return {...B.stat(),gio:S0&&S0.gio?S0.gio.done||0:0,lb:S0&&S0.gb?S0.gb.lucbinh||0:0};},[t,dt,d+vi/3]);await p.waitForTimeout(1800);if(p.url().indexOf('mv2')<0)throw 0;}catch(e){console.log('reload at day',d,vi,String((e&&e.message)||e).slice(0,200));st=null;try{await p.waitForTimeout(4000);await p.waitForFunction(()=>window.__ready&&window.__bot,null,{timeout:300000});await p.evaluate(t=>{window.__off(t);window.__stop=true;document.querySelectorAll('.ddt,.lvup,#intro').forEach(e=>{e.hidden=true});},t);}catch(e2){} }}
  if(!lvAt[st.lv]){lvAt[st.lv]={day:+(d+VIS[vi]/24).toFixed(2),xu:st.xu};console.log('LV',st.lv,'day',(d+VIS[vi]/24).toFixed(2),JSON.stringify(st))}
  if(vi===2)log.push({d,...st});}
  if(d%5===4)console.log('d',d+1,JSON.stringify(log[log.length-1]));
  if(log[log.length-1].lv>=20)break;}
const fin=await p.evaluate(()=>({E:window.__bot.E,forced:window.__bot.forced}));
require('fs').writeFileSync(OUT,JSON.stringify({lvAt,log,fin},null,1));console.log('FIN',JSON.stringify(fin));console.log(errs.slice(0,15).join('\n')||'no errors');await b.close();})();
