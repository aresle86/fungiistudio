// đo tiếng xì: gắn analyser vào kênh "Tiếng vườn", nghe 20 s giữa vườn và 20 s sát mương, đo năng lượng theo dải tần
// dựng trang: cat x40f.js x106.js xpop.js > /tmp/x.js; python3 gen_test2.py /tmp/x.js live/v106a.html lp/mv2_t106.html
const {chromium}=require('playwright');
const today=(d=>d.getFullYear()+'-'+(d.getMonth()+1)+'-'+d.getDate())(new Date());
const SAVE={v:1,eco:2,split:1,qv2:1,exp:1,k102:1,seen:{hello:1},player:{av:1,name:'Q',garden:'Q'},lv:10,xp:4300,xu:900,inv:{},seeds:{},plots:{},qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1,10:1},realTime:true,spd:1,real:Date.now(),dd:{last:today,n:1,full:0},vol:{mus:0,amb:.6,sfx:0}};
(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist','--autoplay-policy=no-user-gesture-required']});
const p=await b.newPage({viewport:{width:900,height:640}});const errs=[];p.on('pageerror',e=>errs.push(e.message));p.setDefaultTimeout(180000);
await p.route(u=>!u.href.startsWith('http://127.0.0.1'),r=>r.abort());
await p.addInitScript(s=>{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s)},JSON.stringify(SAVE));
await p.goto('http://127.0.0.1:8777/'+(process.env.PAGE||'mv2_t106.html'),{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.mouse.click(450,600);await p.waitForTimeout(1500);
const listen=async(where)=>p.evaluate(async where=>{const A=window.__AUD,ac=A.AC;if(!ac) return 'no AudioContext';if(ac.state!=='running') await ac.resume();
 if(where==='mương'){const d=A.DITCH[0];A.camTo(new window.__g.T.Vector3((d[0]+d[2])/2,.3,(d[1]+d[3])/2),window.__g.cam.zoom);}
 const an=ac.createAnalyser();an.fftSize=4096;an.smoothingTimeConstant=0;A.BUS.amb.dk.connect(an);const bins=new Float32Array(an.frequencyBinCount),hz=ac.sampleRate/an.fftSize;
 const band=(lo,hi)=>{let e=0;for(let i=Math.floor(lo/hz);i<Math.ceil(hi/hz);i++) e+=Math.pow(10,bins[i]/10);return 10*Math.log10(e+1e-20);};
 const B={'300-1k':[300,1000],'1-2k':[1000,2000],'2-5k':[2000,5000],'5-10k':[5000,10000]},R={};for(const k in B) R[k]=[];
 await new Promise(r=>setTimeout(r,3000));
 for(let n=0;n<80;n++){await new Promise(r=>setTimeout(r,250));an.getFloatFrequencyData(bins);for(const k in B) R[k].push(band(...B[k]));}
 an.disconnect();const q=(a,f)=>{const s=[...a].sort((x,y)=>x-y);return s[Math.floor(f*(s.length-1))].toFixed(1);};
 return where+': '+Object.keys(B).map(k=>`${k} sàn ${q(R[k],.1)} / giữa ${q(R[k],.5)} / đỉnh ${q(R[k],.95)} dB`).join(' · ');},where);
for(const w of ['giữa vườn','mương']) console.log(await listen(w));
console.log(errs.length?'ERR '+errs.join(' | '):'no errors');await b.close();})();
