const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const save=JSON.stringify({v:1,eco:2,split:1,qv2:1,exp:1,open:['A1','A1b','A2','B1','B1b','B2','D1','D1b','H1','H2'],xu:2000,inv:{},seeds:{},gt:9000,real:Date.now(),spd:1,ovr:12,realTime:false,seen:{hello:1},player:{av:2,name:'Nhu',garden:'Nhu'},lv:9,xp:850,qd:{3:1,4:1,5:1,6:1,7:1,8:1,9:1},plots:{}});
const p=await b.newPage({viewport:{width:1300,height:850}});const errs=[];p.on('pageerror',e=>errs.push(e.message));
await p.addInitScript(s=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1');localStorage.setItem('mv2-state',s);}catch(e){}},save);
await p.goto('http://127.0.0.1:8777/mv2_test.html');await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.addStyleTag({content:'.ui,.ngoai,#tray,.top,.nxq,.ddt{display:none!important}'});
const objs=await p.evaluate(()=>{window.__stop=true;const T=window.__g.T,S=window.__S,out=[];
 // lưới đánh dấu tọa độ mỗi 1 đơn vị
 for(let x=5;x<=12;x++)for(let z=1;z<=6;z++){const m=new T.Mesh(new T.SphereGeometry(.05,6,4),new T.MeshBasicMaterial({color:(x%2?'#ff00ff':'#00ffff'),depthTest:false}));m.renderOrder=99;m.position.set(x,.35,z);S.add(m);}
 for(const o of S.children){if(!o.isObject3D)continue;const bx=new T.Box3().setFromObject(o);if(bx.isEmpty())continue;const c=bx.getCenter(new T.Vector3()),sz=bx.getSize(new T.Vector3());if(c.x>6.8&&c.x<12.5&&c.z>1.5&&c.z<5.5&&sz.x<4&&sz.z<4)out.push([o.type,+c.x.toFixed(2),+c.z.toFixed(2),+sz.x.toFixed(2),+sz.y.toFixed(2),+sz.z.toFixed(2),o.children.length]);}
 for(let i=0;i<4;i++)window.__tick();return out;});
console.log(objs.length);for(const o of objs)console.log(JSON.stringify(o));
const shot=async(n,x,z,zm)=>{await p.evaluate(([x,z,zm])=>{const c=window.__ctl;c.maxZoom=40;const d=c.object.position.clone().sub(c.target);c.target.set(x,.3,z);c.object.position.copy(c.target).add(d);c.object.zoom=zm;c.object.updateProjectionMatrix();for(let i=0;i<4;i++)window.__tick();},[x,z,zm]);await p.screenshot({path:'../'+n+'.png',timeout:300000});};
await shot('lay0',8.3,3.6,2.2);
console.log(errs.join('\n')||'no errors');await b.close();})();
