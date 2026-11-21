/* v175: chạm vô giàn. node tGian175.js <trang>   (cần máy chủ lp ở cổng 8777)
   Đo đúng cái người chơi làm: chạm vô chỗ MÀN HÌNH ĐANG VẼ dây/trái/khung giàn.
   Mốc v174 (390x844, khổ qua đang lớn): giàn đúng 9-10/27 điểm trong khối, 12/27 ra liếp khác. */
const { chromium } = require('playwright');
const PAGE = process.argv[2] || 'mv2_t175b.html';
(async () => {
  const b = await chromium.launch({ args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist'] });
  const p = await b.newPage({ viewport: { width: 390, height: 844 } });
  const errs = []; p.on('pageerror', e => errs.push(String(e.message).slice(0, 200)));
  await p.route(u => !u.href.startsWith('http://127.0.0.1'), r => r.abort());
  await p.addInitScript(() => { try {
    localStorage.clear(); localStorage.setItem('mv3d-q', '1'); localStorage.setItem('mv2-lang', 'vi');
    localStorage.setItem('mv2-state', JSON.stringify({ v: 1, eco: 2, split: 1, qv2: 1, seen: { hello: 1, sold: 1 }, player: { av: 1, name: 'Bot', garden: 'Bot' }, lv: 20, xp: 40000, xu: 90000, exp: 1, qd: {}, inv: {}, seeds: {}, plots: {}, realTime: true, spd: 1, real: Date.now() }));
  } catch (e) {} });
  await p.goto('http://127.0.0.1:8777/' + PAGE);
  await p.waitForFunction(() => window.__ready, null, { timeout: 170000 });
  await p.waitForTimeout(3500);
  const ev = s => p.evaluate(s => window.__ev(s), s);
  await ev("document.querySelectorAll('.ddt,#intro').forEach(e=>e.hidden=true); try{closeSheet()}catch(e){}");
  let fail = 0;
  const ok = (n, c, got) => { console.log((c ? 'ĐẠT  ' : 'HỎNG ') + n + (c ? '' : '  -> ' + JSON.stringify(got))); if (!c) fail++; };

  /* cảnh: khổ qua đang lớn trên hai đoạn giàn, cải đang lớn trên liếp thường */
  const setup = await ev(`(()=>{
    const G = PLOTS.filter(P=>P.trellis).map(P=>P.id);
    for (const id of G){ ST.plots[id] = ST.plots[id]||{}; Object.assign(ST.plots[id], {crop:'khoqua', g: CROPS.khoqua.grow*0.7, moist:1, soil:1, dead:0}); }
    const B = PLOTS.filter(P=>!P.trellis && !P.tree && !P.bai && ST.plots[P.id] && !hidP(P) && !locked(P)).map(P=>P.id);
    for (const id of B) Object.assign(ST.plots[id], {crop:'cai', g: CROPS.cai.grow*0.7, moist:1, soil:1, dead:0});
    for (const Q of PLOTS) refreshPlot(Q.id);
    return { G, B };
  })()`);
  console.log('cảnh: giàn', JSON.stringify(setup.G), '· liếp thường', setup.B.length, 'cái');
  await p.waitForTimeout(1200);

  /* 1. chạm vô chỗ đang vẽ dây/trái của giàn thì phải ăn:
        ra đúng giàn đó, hoặc bong bóng của liếp khác thắng (bong bóng luôn được ưu tiên),
        hoặc ra đoạn giàn kế bên (hai đoạn đan dây vô nhau ở chỗ nối). */
  const r1 = await ev(`(()=>{
    const out = [];
    for (const id of ${JSON.stringify(setup.G)}){
      const v = PV[id], gs = [v.crop, v.gianG].filter(g=>g && g.visible && g.children.length);
      for (const g of gs) g.updateMatrixWorld(true);
      const bb = new T.Box3(); for (const g of gs) bb.expandByObject(g);
      let x0=1e9,y0=1e9,x1=-1e9,y1=-1e9;
      for (const sx of [bb.min.x,bb.max.x]) for (const sy of [bb.min.y,bb.max.y]) for (const sz of [bb.min.z,bb.max.z]){
        const q = new T.Vector3(sx,sy,sz).project(cam); const px=(q.x+1)/2*innerWidth, py=(1-q.y)/2*innerHeight;
        x0=Math.min(x0,px); x1=Math.max(x1,px); y0=Math.min(y0,py); y1=Math.max(y1,py);
      }
      let veDay=0, dung=0, bongThang=0, gianBen=0, hong=0; const hongAi={};
      for (let i=0;i<=24;i++) for (let j=0;j<=24;j++){
        const px = x0+(x1-x0)*i/24, py = y0+(y1-y0)*j/24;
        ndc.set(px/innerWidth*2-1, -(py/innerHeight)*2+1); ray.setFromCamera(ndc, cam);
        if (!ray.intersectObjects(gs, true)[0]) continue;    /* chỗ này không vẽ giàn: bỏ */
        veDay++; const got = plotHit(px, py);
        if (got === id) dung++;
        else if (PBH) bongThang++;
        else if (got && PL[got] && PL[got].trellis) gianBen++;
        else { hong++; hongAi[got||'trôi']=(hongAi[got||'trôi']||0)+1; }
      }
      out.push({ id, veDay, dung, bongThang, gianBen, hong, hongAi });
    }
    return out;
  })()`);
  for (const x of r1) ok('1. chạm vô dây/trái giàn ' + x.id + ': đúng ' + x.dung + ', bong bóng thắng ' + x.bongThang + ', đoạn kế ' + x.gianBen + ', rớt ' + x.hong + ' / ' + x.veDay + ' điểm',
                         x.veDay >= 40 && x.hong === 0, x);

  /* 2. liếp thường: chỗ nào KHÔNG bị tán giàn che thì phải chạm ra đúng liếp đó.
        Chỗ bị tán che thì ra giàn là đúng, vì người chơi đang nhìn thấy tán giàn ở đó. */
  const r2 = await ev(`(()=>{
    const gs = []; for (const P of PLOTS){ if (!P.trellis) continue; const v = PV[P.id]; for (const g of [v.crop, v.gianG]) if (g && g.visible && g.children.length){ g.updateMatrixWorld(true); gs.push(g); } }
    const proj = (x,y,z)=>{ const q = new T.Vector3(x,y,z).project(cam); return [ (q.x+1)/2*innerWidth, (1-q.y)/2*innerHeight ]; };
    const out = [];
    for (const id of ${JSON.stringify(setup.B)}){
      const P = PL[id], [u0,v0,u1,v1] = P.b, hi = (CROPS[(ST.plots[id]||{}).crop]||{}).h || .3;
      let troi=0, dung=0, bitTan=0, hong=0, lech=0; const hongAi={};
      for (const fy of [0.15,0.5,0.9]) for (const fx of [0.2,0.5,0.8]) for (const fz of [0.2,0.5,0.8]){
        const s = proj(u0+(u1-u0)*fx, hi*fy, v0+(v1-v0)*fz);
        ndc.set(s[0]/innerWidth*2-1, -(s[1]/innerHeight)*2+1); ray.setFromCamera(ndc, cam);
        const che = gs.length ? ray.intersectObjects(gs, true)[0] : null;
        const got = plotHit(s[0], s[1]);
        if (che){ bitTan++; continue; }
        if (got === id) dung++; else if (got == null) troi++; else { if (PL[got] && PL[got].trellis && !PBH && gianHitAt(s[0], s[1]) === got) hong++; else lech++; hongAi[got]=(hongAi[got]||0)+1; }
      }
      out.push({ id, dung, troi, bitTan, hong, lech, hongAi });
    }
    return out;
  })()`);
  const xau = r2.filter(x => x.hong > 0);
  console.log('   liếp bị tán giàn che một phần:', JSON.stringify(r2.filter(x=>x.bitTan).map(x=>({id:x.id, bitTan:x.bitTan, dung:x.dung, hong:x.hong}))));
  console.log('   lệch sẵn có từ v174 (tán cây trái, bờ giữa hai liếp, mép liếp bắt hụt):', JSON.stringify(r2.filter(x=>x.lech).map(x=>({id:x.id, lech:x.lech, ai:x.hongAi}))));
  ok('2. chỗ không bị tán giàn che: giàn không cướp cú chạm của liếp (' + r2.length + ' liếp)', xau.length === 0, xau);

  /* 3. bong bóng luôn thắng: liếp nào có việc thì bấm bong bóng vẫn ăn, kể cả liếp nằm sau giàn */
  const r3 = await ev(`(()=>{
    for (const id of ${JSON.stringify(setup.B)}){ const p = ST.plots[id]; p.g = CROPS[p.crop].grow; }
    for (const id of ${JSON.stringify(setup.G)}) ST.plots[id].g = CROPS[ST.plots[id].crop].grow;
    for (const Q of PLOTS) refreshPlot(Q.id);
    const proj = (x,y,z)=>{ const q = new T.Vector3(x,y,z).project(cam); return [ (q.x+1)/2*innerWidth, (1-q.y)/2*innerHeight ]; };
    const out = [];
    for (const id of ${JSON.stringify(setup.G.concat(setup.B))}){
      const v = PV[id]; if (!v.want || v.clH) continue;      /* clH: bong bóng đã gom vô cụm, liếp này không có bóng riêng */
      const bg = v.bub[v.want]; bg.position.set(v.cx, v.bubY, v.cz); bg.updateMatrixWorld(true);
      const w = new T.Vector3().setFromMatrixPosition(bg.matrixWorld), s = proj(w.x, w.y, w.z);
      const got = plotHit(s[0], s[1]);
      out.push({ id, gian: !!PL[id].trellis, want: v.want, got, laBong: PBH, ok: PBH === true, trung: got !== id ? got : null });
    }
    return out;
  })()`);
  const bHong = r3.filter(x => !x.ok), bTrung = r3.filter(x => x.trung);
  if (bTrung.length) console.log('   hai bong bóng chồng nhau (có sẵn từ v174):', JSON.stringify(bTrung.map(x=>x.id+'->'+x.trung)));
  ok('3. bấm bong bóng vẫn ăn vô bong bóng (' + r3.length + ' bong bóng)', bHong.length === 0, bHong);

  /* 4. hái thiệt trên giàn */
  const r4 = await ev(`(()=>{
    const id = ${JSON.stringify(setup.G[0])}, p = ST.plots[id], truoc = (ST.inv[p.crop]||0), n = harvestN(p);
    act.harvest(id);
    return { crop: p.crop, truoc, sau: (ST.inv[p.crop]||0), can: n, conCay: !!(ST.plots[id]||{}).crop };
  })()`);
  ok('4. hái giàn ăn thiệt (giàn hái xong vẫn giữ dây)', r4.sau - r4.truoc === r4.can && r4.can > 0, r4);

  /* 5. giàn tự dựng trên ô đất trống cũng chạm được (khung giàn, chưa trồng gì) */
  const r5 = await ev(`(()=>{
    { const Q0 = PLOTS.filter(P=>P.bai && !P.co && !hidP(P)).find(P=>{ try { return !objAt(P.id) && !bigAt(P.id) && decoAt(P.id)<0; } catch(e){ return true; } });   /* mở một ô đất trống ra để dựng giàn */
      if (Q0){ ST.open = ST.open || []; if (!ST.open.includes(Q0.id)) ST.open.push(Q0.id); ST.plots[Q0.id] = ST.plots[Q0.id] || { moist:1, soil:1, g:0 }; ST.plots[Q0.id].crop = null; ST.plots[Q0.id].g = 0; for (const Q of PLOTS) refreshPlot(Q.id); } }
    const P0 = PLOTS.filter(P=>P.bai && !P.co && !locked(P) && !hidP(P) && !(ST.plots[P.id]||{}).crop).filter(P=>{ try { return !objAt(P.id) && !bigAt(P.id) && decoAt(P.id)<0; } catch(e){ return true; } })[0];
    if (!P0) return { boQua: 'không có ô đất trống nào để dựng giàn' };
    ST.gian = ST.gian || {}; ST.gian[P0.id] = 1; for (const Q of PLOTS) refreshPlot(Q.id);
    const v = PV[P0.id], g = v.gianG;
    if (!g || !g.visible || !g.children.length) return { boQua: 'giàn chưa dựng được', id: P0.id };
    g.updateMatrixWorld(true);
    const bb = new T.Box3().expandByObject(g);
    let dung=0, ve=0;
    for (let i=0;i<=12;i++) for (let j=0;j<=12;j++){
      const q = new T.Vector3(bb.min.x+(bb.max.x-bb.min.x)*i/12, bb.max.y-0.02, bb.min.z+(bb.max.z-bb.min.z)*j/12).project(cam);
      const px=(q.x+1)/2*innerWidth, py=(1-q.y)/2*innerHeight;
      ndc.set(px/innerWidth*2-1, -(py/innerHeight)*2+1); ray.setFromCamera(ndc, cam);
      if (!ray.intersectObjects([g], true)[0]) continue;
      ve++; if (plotHit(px, py) === P0.id || PBH) dung++;
    }
    return { id: P0.id, ve, dung };
  })()`);
  if (r5.boQua) console.log('BỎ QUA 5:', r5.boQua, JSON.stringify(r5));
  else ok('5. chạm khung giàn tự dựng ' + r5.id + ' (' + r5.dung + '/' + r5.ve + ')', r5.ve >= 5 && r5.dung === r5.ve, r5);

  ok('6. không có lỗi chạy', errs.length === 0, errs.slice(0, 3));
  console.log(fail ? '\n=== CÒN ' + fail + ' CHỖ HỎNG ===' : '\n=== ĐẠT HẾT ===');
  await b.close();
  process.exit(fail ? 1 : 0);
})();
