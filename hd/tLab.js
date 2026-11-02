const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push('ERR '+e.message));p.on('console',m=>{if(m.type()==='error')errs.push(m.text())});
await p.goto('http://127.0.0.1:8777/fishlab.html');await p.waitForFunction(()=>window.__done||window.__err,null,{timeout:300000}).catch(()=>{});
const out=await p.evaluate(()=>window.__out||{}),rep=await p.evaluate(()=>window.__rep||{});console.log(JSON.stringify(rep));console.log(errs.join('\n'));
const ks=[...new Set(Object.keys(out).map(k=>k.split('_')[0]))],vs=['icon','side','top','front','back','under'];
await p.setContent('<body style="margin:0;background:#FFFBF2;font:13px sans-serif"><table>'+ks.map(k=>'<tr>'+vs.map(v=>`<td style="text-align:center"><img src="${out[k+'_'+v]}" width="220"><br>${k} · ${v}</td>`).join('')+'</tr>').join('')+'</table></body>');
await p.screenshot({path:'../lab.png',fullPage:true});await b.close();})();
