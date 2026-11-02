const {chromium}=require('playwright');(async()=>{const b=await chromium.launch({args:['--use-angle=swiftshader','--enable-unsafe-swiftshader','--ignore-gpu-blocklist']});
const p=await b.newPage();const errs=[];p.on('pageerror',e=>errs.push(e.message));await p.goto('http://127.0.0.1:8777/fishlab.html');await p.waitForFunction(()=>window.__done,null,{timeout:600000});
const out=await p.evaluate(()=>window.__out),rep=await p.evaluate(()=>window.__rep);console.log(JSON.stringify({tep:rep.tep,tomcang:rep.tomcang}),errs.join('|'));
const vs=['icon','side','top','back','under'];await p.setContent('<body style="margin:0;background:#FFFBF2;font:13px sans-serif"><table>'+['tep','tomcang'].map(k=>'<tr>'+vs.map(v=>`<td style="text-align:center"><img src="${out[k+'_'+v]}" width="220"><br>${k} · ${v}</td>`).join('')+'</tr>').join('')+'</table></body>');
await p.screenshot({path:'../tail.png',fullPage:true});await b.close();})();
