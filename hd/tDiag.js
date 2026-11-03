const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage({viewport:{width:600,height:400}});
await p.addInitScript(()=>{try{localStorage.clear();localStorage.setItem('mv3d-q','1')}catch(e){}});
await p.goto('http://127.0.0.1:8777/mv2_test.html',{waitUntil:'domcontentloaded'});await p.waitForFunction(()=>window.__ready,null,{timeout:300000});
await p.waitForTimeout(2000);
const r=await p.evaluate(()=>{const L=window.__BUBALL||[];const g=L.find(g=>g.visible&&g.userData.ring);if(!g)return 'none '+L.length;const out=[];g.traverse(o=>{if(o.isMesh)out.push([o.type,o.parent===g?'direct':o.parent.type,o.renderOrder,o.material.transparent,o.material.visible!==false&&o.visible,o.material.color?o.material.color.getHexString():'',o.material.depthTest]);});return JSON.stringify({gro:g.renderOrder,isGroup:g.isGroup,col:g.userData.col,out});});
console.log(r);await b.close();})();
