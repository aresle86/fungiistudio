window.__ctl = ctl; window.__x = { openSheet, openBook, levelUp, act, PLOTS, ICON, PL, ga, GAV, NEST, FEEDP, COOPC, gaHit: (x, y) => gaHit(x, y) };
window.__e = { get FM(){ return FM; }, fmEnter, fmExit, fmTap, fmCatch, FISHK, khap, lo, hoBon, hoAdd, cauTap, buyObj, placeObj, objAt, CAUV, LOV, LO, PV, doQuest, hoSim, khapSim, loSim, camTo, closeSheet, lsay, gio, gheSim, gheGive, soVuon, SAUC, GHE };
window.__w = { weedAt, weedGo, weedOn, WEEDP, weedLeft, nxq, lvCelebrate, openIntro, levelUp, checkLevel, gainXP, hud, openBook, closeBook, renderBook, groundAt, get TOOL(){ return TOOL; }, clearTool };
window.__G = { needOf, openRing, closeRing, quickSeed, seedTap, PV, PL, PLOTS, get RINGID(){ return RINGID; } };
window.__T = { setTool, putAway, autoPutAway, toolLeft, finishSow, get TOOL(){ return TOOL; } };
window.__H = { hasVoc, devoc, bark, SAYH };
window.__C = { coopRing, coopFix, coopCan, COOPC, oddDo, get odd(){ return ST.odd; } };
window.__P = { penRing, penFix, penCan, PENS, VIT };
window.__S = S; window.__visitGo = visitGo;
window.__L = { landStart, landWork, landSt, landCost, landWait, landCheck, landBusy, get LAND(){ return ST.land; } };
window.__x2 = { plotHit: (x, y) => plotHit(x, y), oddHit: (x, y) => oddHit(x, y), ordHit: (x, y) => ordHitAt(x, y), vitHit: (x, y) => vitHit(x, y), nongHit: (x, y) => nongHit(x, y), cau: (x, y) => cauHit(x, y), gio: (x, y) => gioHit(x, y), lo: (x, y) => loHit(x, y), say: (x, y) => sayHit(x, y), ghe: (x, y) => gheHit(x, y) };
window.__T2 = { mua, tetDay, unlocked, tetBuy, tetOrd, tetDayAt: s => { const tm = ST.muaTest; ST.muaTest = null; const r = tetDay(new Date(s + 'T10:00:00')); ST.muaTest = tm; return r; } };
window.__TT = { TETV, seasonTick };
window.__CL = { CLOUD, cloudSave, statPing, STAT, stepMark };
window.__TR = { treeSpot, treePlant, pairHost, pairBelow, unionB, nTrees: () => nTrees() };
window.__FM = { FM, FSH, fmEnter, fmExit, fmTap, fmCast, fmTick, fmCatch, FISHK, CAUV };
window.__FM = Object.assign(window.__FM||{}, { spotOf, fishPick, fAvail, gioNow, muaSong, moiHas, cauLeft, cauCap, DISH, PHOI, KCAV });
window.__FM = Object.assign(window.__FM||{}, { CAUV, FAREA });
window.__FM = Object.assign(window.__FM||{}, { fshClear, fshSpawn });
window.__FM = Object.assign(window.__FM||{}, { moonAge, trang, nuoc, wkKey, grpCheck, grpList, FGRP, hoiLoad, HOI, hoiReward, fishShare, KBEN });
window.__FT = { fairyModel, T };
window.__FT2 = { FT, FTV, FDV, ftTap, ftTell, fdTake, khacNhap, ftCheck, pgCotich };
window.__FT2.ftTick = ftTick;
window.__FT2.ddCheck = ddCheck;
window.__FT2 = Object.assign(window.__FT2, { bigPlace, bigFit, bigAt, aoBuy, bigHome, ttMagic, TTA, AOV, BIGD });
window.__FT.dcModel = dcModel; window.__FT.sdAnim = sdAnim; window.__FT.dhBird = dhBird; window.__FT.kvSpin = kvSpin;
window.__DC = { DCK, dcBuy, dcPlace, dcTake, DCV, decoAt };
window.__BU = { BUK, BUV, buTick, buCatch, buKinds };
window.__UP = { upxBuy, NONGV, KHAPV };
window.__FT2.FT = FT;
window.__OB = openBook; window.__DDS = ddShow;
window.__VG = visitGo;
window.__ICON = ICON;
window.__FT3 = { sdHelp, dcPay, get HOUR(){ return HOUR; } };
window.__FT3.ftCompact = ftCompact;
window.__FT3.roofState = roofState; window.__FT3.thatchRoof = thatchRoof;
window.__FT3.maiLeft = maiLeft; window.__FT3.doQuest = doQuest;
window.__FT3.bldLeft = bldLeft; window.__FT3.penFix = penFix;
window.__FT3.beeHive = beeHive; window.__FT3.beeAnim = beeAnim;
window.__FT3.ongTake = ongTake; window.__FT3.ongSim = ongSim;
window.__FT3.houseUp = houseUp;
window.__FT3.nhaLeft = nhaLeft; window.__FT3.nhaSt = nhaSt;
window.__FT3.gheTB = gheTB;
window.__FT3.Raycaster = T.Raycaster;
window.__FT3.TBV = TBV; window.__FT3.tbBuild = tbBuild; window.__FT3.tbTake = tbTake; window.__FT3.tbLeft = tbLeft; window.__FT3.loLeft = loLeft; window.__FT3.tbHTML = tbHTML; window.__FT3.tbHit = tbHit; window.__FT3.TB = TB; window.__FT3.GHEV = GHEV;
for (const [n, f] of Object.entries({ fmEnter: () => fmEnter, fmExit: () => fmExit, fmCast: () => fmCast, fmTap: () => fmTap, fmCastBtn: () => fmCastBtn, fuiAim: () => fuiAim, fuiWait: () => fuiWait, fuiBite: () => fuiBite, fuiReel: () => fuiReel, FM: () => FM, CAUV: () => CAUV, FSH: () => FSH })) { try { window.__FT3[n] = f(); } catch (e) {} }
window.__ICONS = ICON;
try { window.__FT3.rodBend = rodBend; } catch (e) {}
try { window.__FT3.hud = hud; window.__FT3.nxq = nxq; window.__FT3.taskGo = taskGo; } catch (e) {}
try { window.__FT3.openBook = openBook; window.__FT3.pingAt = pingAt; } catch (e) {}
try { window.__FT3.penFix = penFix; window.__FT3.bldStart = bldStart; window.__FT3.placeAvatar = placeAvatar; window.__FT3.vuonBadge = vuonBadge; window.__FT3.NB2 = NB2; window.__FT3.oddSpawn = typeof oddSpawn !== 'undefined' ? oddSpawn : null; } catch (e) {}
try { window.__AVIMG = AVIMG; window.__FT3.sticker = sticker; window.__FT3.openSheet = openSheet; } catch (e) {}
try { window.__UIC = UIC; } catch (e) {}
window.__SY = { say, sayOnce, SAYQ, IDLEQ, checkTips, oddTick, get sayT(){ return sayT; }, get SAYOK(){ return SAYOK; }, renderFan };
/* bot: người chơi thường, chạy trong module của game */
window.__bot = (() => {
  const E = {}, err = (k, e) => { E[k] = (E[k] || 0) + 1; if (E[k] < 3) console.warn('BOT', k, e && e.message); };
  const T_ = (k, f) => { try { return f(); } catch (e) { err(k, e); } };
  const forced = [];
  let gap = 4 * 3600;
  function step(sec){ let o = sec; while (o > 0){ const s = Math.min(60, o); sim(s); o -= s; } T_('land', () => landCheck()); }
  const ripeP = p => p && p.crop && !p.dead && p.g >= CROPS[p.crop].grow;
  const reserve = () => { const r = {}; for (const o of [...((ST.ord && ST.ord.list) || []), ...(ST.ghe && ST.ghe.o ? [ST.ghe.o] : [])]) for (const [k, q] of o.items) r[k] = (r[k] || 0) + q; return r; };
  function sellAll(){ const r = reserve(); for (const k of Object.keys(ST.inv)){ const g = GD(k); if (!g || g.nosell || !(ST.inv[k] > 0)) continue; if (k === 'rom') continue; let keep = r[k] || 0; if (k === 'trungga' && (ST.lv || 1) >= GA.buyLv) keep += 1; if (k === 'trungvit') keep += 4; if (k === 'bap' && gaOn()) keep += 2; if (k === 'raumuong' && vitOn()) keep += 2; if (k === 'ot' && (ST.lv || 1) >= 7) keep += 4; if (k === 'cai' && (ST.lv || 1) >= 8) keep += 4; const n = ST.inv[k] - keep; if (n > 0) T_('sell', () => act.sell(k, n)); }
    for (const k of Object.keys(ST.gb || {})){ if (!(ST.gb[k] > 0) || k === 'cui' || k === 'muoi' || k === 'duong' || k === 'lucbinh' || k === 'lucbinhkho') continue; const g = GD(k); if (!g || g.nosell) continue; const n = ST.gb[k] - (r[k] || 0); if (n > 0) T_('sellgb', () => act.sell(k, n)); } }
  function pickCrop(){ const lv = ST.lv || 1, ks = Object.keys(CROPS).filter(k => unlocked(k) && !CROPS[k].tree && !CROPS[k].rare && CROPS[k].kind !== 'trellis');
    const sc = ks.map(k => { const c = CROPS[k], t = Math.max(c.grow, gap) , v = (c.yield || 2) * c.sell * (1 + (c.cuts > 1 ? (c.cuts - 1) * .6 : 0)) - c.seed; return [k, v / t]; }).sort((a, b) => b[1] - a[1]);
    return sc.slice(0, 3).map(x => x[0]); }
  function farm(){ const top = pickCrop(); let i = 0; const need = []; { const r = reserve(); if ((ST.lv || 1) >= 8) r.cai = (r.cai || 0) + 4; if ((ST.lv || 1) >= 7) r.ot = (r.ot || 0) + 4; for (const [dk, dq] of Object.entries({ ...r })){ const D = DISH[dk]; if (!D || has(dk) >= dq) continue; for (const [ik, iq] of Object.entries(D.in)) if (CROPS[ik]) r[ik] = (r[ik] || 0) + iq * (dq - has(dk)); } for (const [k, q] of Object.entries(r)){ if (!CROPS[k] || CROPS[k].tree || !unlocked(k) || CROPS[k].kind === 'trellis') continue; const growing = PLOTS.filter(Q => ST.plots[Q.id] && ST.plots[Q.id].crop === k).length; let lack = q - has(k) - growing * Math.max(1, Math.round((CROPS[k].yield || 2) * .7)); while (lack > 0){ need.push(k); lack -= Math.max(1, Math.round((CROPS[k].yield || 2) * .7)); } } }
    for (const P of PLOTS){ if (!P.tree || hidP(P)) continue; const p = ST.plots[P.id]; if (p && !p.crop && unlocked(P.tree) && ST.xu >= CROPS[P.tree].seed + 50) T_('treeP', () => act.plant(P.id, P.tree)); }
    for (const P of PLOTS){ const p = ST.plots[P.id]; if (!p || locked(P) || hidP(P)) continue; if (ripeP(p)){ if (T_('kc', () => kCap() - kUsed()) < 12) sellAll(); T_('hv', () => act.harvest(P.id)); } }
    for (const P of PLOTS){ const p = ST.plots[P.id]; if (!p || locked(P) || hidP(P) || P.tree) continue; if (p.dead) T_('pull', () => act.pull(P.id)); if (!p.crop){ const k = P.trellis ? (unlocked('khoqua') ? 'khoqua' : null) : (need.length ? need.shift() : top[i++ % top.length]); if (k && ST.xu >= CROPS[k].seed + 10) T_('plant', () => act.plant(P.id, k)); } }
    for (const P of PLOTS){ const p = ST.plots[P.id]; if (!p || locked(P) || hidP(P) || !p.crop) continue; if (!P.trellis && p.moist < .6) T_('water', () => act.water(P.id)); if (!P.tree && !P.trellis && !(p.mulch > ST.gt)){ if (!(ST.inv.rom > 0) && ST.xu > 300) T_('rom', () => act.buyRom(3)); const romKeep = ((ST.lv || 1) >= 6 && !ST.vit.fixed) || ((ST.lv || 1) >= 2 && !ST.ga.fixed) ? 5 : 0; if ((ST.inv.rom || 0) <= romKeep && ST.xu > 100) T_('rom2', () => act.buyRom(2)); if (ST.inv.rom > romKeep) T_('mulch', () => act.mulch(P.id)); } } }
  function grow(){ const lv = ST.lv || 1;
    for (const k of ['nong', 'khap', 'ho', 'say', 'ong']){ const D = OBJD[k]; if (!D || lv < D.lv || (ST[k] && ST[k].own)) continue; if (ST.xu > D.buy + 150) T_('obj', () => buyObj(k)); }
    for (const P of PLOTS){ if (P.bai || P.tree || !locked(P) || hidP(P)) continue; if (nOpen() >= bedCap()) break; if (ST.xu > bedCost() + 60) T_('bed', () => act.openBed(P.id)); }
    for (const P of PLOTS){ if (!P.bai || hidP(P)) continue; const st = T_('lst', () => landSt(P.id)); if (st === 'wild' && landBusy() < 2 && ST.xu > 400) T_('land', () => landStart(P.id)); const L = ST.land[P.id]; if (L && L.st === 'cong'){ for (let k = 0; k < 4 && ST.land[P.id].st === 'cong'; k++) T_('lw', () => landWork(P.id)); } }
    for (const P of PLOTS){ if (!P.bai || hidP(P) || !locked(P)) continue; if (T_('lst2', () => landSt(P.id)) === 'own' && !objAt(P.id) && !pairHost(P.id)){ const tk = ['dua', 'xoai', 'khe', 'oi', 'chuoi'].find(k => unlocked(k) && ST.xu > CROPS[k].seed + 300 && nTrees() < 8 && !PLOTS.some(Q => ST.plots[Q.id] && ST.plots[Q.id].crop === k)); if (tk && T_('ts', () => treeSpot(P.id))) { T_('tree', () => treePlant(P.id, tk)); continue; } const zk = P.zone || 'bai', own = PLOTS.filter(Q => Q.bai && (Q.zone || 'bai') === zk && !hidP(Q) && T_('ls3', () => landSt(Q.id)) === 'own').length, beds = ST.open.filter(i => PL[i] && PL[i].bai && (PL[i].zone || 'bai') === zk).length; const wantObj = ['nong', 'khap', 'ho', 'say', 'ong'].some(k => OBJD[k] && objOn(k) && !(ST[k] && ST[k].own)); if (!wantObj && beds < Math.max(2, Math.floor(own / 2))) T_('bed2', () => act.openBed(P.id)); } }
    for (const k of ['ga', 'vit']) T_('pen', () => { if (penCan(k)) penFix(k); }); }
  function animals(){ if (gaOn()){ T_('gac', () => ga.collect()); if (ST.ga.trough < ST.ga.hens) T_('gaf', () => ga.feed()); if ((ST.lv || 1) >= GA.buyLv && ST.ga.hens + ST.ga.rooster < gaCap() && ST.xu > GA.buy + 300) T_('gab', () => ga.buy()); if (!ST.ga.brood && (ST.lv || 1) >= GA.buyLv && !(ST.qd || {})[6]) T_('gah', () => ga.hatch()); }
    if (vitOn()){ T_('vic', () => vit.collect()); if (ST.vit.trough < ST.vit.n) T_('vif', () => vit.feed()); if (ST.vit.n < vitCap() && ST.xu > VIT.buy + 300) T_('vib', () => vit.buy()); } }
  function craft(){ const lv = ST.lv || 1;
    ST.gb = ST.gb || {}; for (const [k, pr] of [['muoi', MUOI_PRICE], ['duong', DUONG_PRICE], ['cui', CUI_PRICE]]){ const need = (k === 'muoi' && lv >= 8) || (k === 'duong' && lv >= 10) || (k === 'cui' && lv >= 4) ? 3 : 0; while ((ST.gb[k] || 0) < need && ST.xu > pr + 50 && gbUsed() < GB_CAP){ ST.xu -= pr; ST.gb[k] = (ST.gb[k] || 0) + 1; } }
    if (ST.nong && ST.nong.own){ T_('nt', () => nong.takeAll()); ST.nong.trays.forEach((t, i) => { if (!t){ const k = ['lucbinhkho', 'chuoiphoi', 'otkho'].find(k => PHOI[k] && lv >= PHOI[k].lv && canIn(PHOI[k].in)); if (k) T_('np', () => nong.put(i, k)); } }); }
    if (ST.khap && ST.khap.own){ T_('kt', () => khap.takeAll()); (ST.khap.jars || ST.khap.slots || []).forEach((t, i) => { if (!t){ if (!(has('muoi') > 0) && ST.xu > 50) { ST.gb = ST.gb || {}; } const k = ['dacai', 'hotvit'].find(k => canIn(MUOI[k].in)); if (k) T_('kp', () => khap.put(i, k)); } }); }
    if (ST.say && ST.say.own){ T_('st', () => lsay.takeAll()); ST.say.trays.forEach((t, i) => { if (!t){ const k = ['xoaisay', 'mutkhe', 'comdua', 'chuoiphoi', 'otkho'].find(k => SAYR[k] && lv >= SAYR[k].lv && canIn(SAYR[k].in)); if (k) T_('sp', () => lsay.put(i, k)); } }); }
    if (lv >= BEP.lv && ST.bep){ T_('bt', () => bepTakeAll()); for (let n = 0; n < 3; n++){ const rq = reserve(), ks = Object.keys(DISH).filter(k => lv >= DISH[k].lv && bepCan(k)).sort((a, b) => ((rq[b] || 0) - has(b) > 0 ? 1e4 : 0) + DISH[b].sell - ((rq[a] || 0) - has(a) > 0 ? 1e4 : 0) - DISH[a].sell); if (!ks.length || !ST.bep.pots.some(p => !p)) break; T_('cook', () => bepCook(ks[0])); } }
    if (ST.ho && ST.ho.own){ T_('hr', () => { for (let i = 0; i < 6; i++) hoRau(); }); T_('hs', () => hoSim(0)); T_('hb', () => { while (ST.ho.bags > 0 && hoWorst()) hoBon(); }); } }
  function orders(){ for (const o of [...((ST.ord && ST.ord.list) || [])]){ o._seen = (o._seen || 0) + 1; if (o._seen > 6 && !ordCan(o)) T_('drop', () => ordDrop(o.id)); } for (const o of [...((ST.ord && ST.ord.list) || [])]) if (ordCan(o)) T_('ord', () => ordGive(o.id)); if (ST.ghe && ST.ghe.o && ordCan(ST.ghe.o)) T_('ghe', () => gheGive()); }
  function odd(){ for (const o of [...((ST.odd && ST.odd.list) || [])]) T_('odd', () => oddDo(o)); }
  function tasks(){ T_('et', () => ensureTasks()); for (const x of ST.tasks.list) if (x.done && x.cl === false){ x.cl = true; if (x.rw[0] === 'coin') ST.xu += x.rw[1]; else ST.inv.rom = (ST.inv.rom || 0) + x.rw[1]; } if (ST.tasks.gr && !ST.tasks.got){ ST.tasks.got = true; ST.seeds[ST.tasks.bonus] = (ST.seeds[ST.tasks.bonus] || 0) + 1; } }
  const qWait = {};
  function quest(day){ const lv = ST.lv || 1, n = lv + 1, q = QUEST[n]; if (!q || (ST.qd || {})[n]) return; if ((ST.xp || 0) < (XPN[n] || 1e9)) return;
    if (q.t === 'pay'){ if (ST.xu >= q.xu){ if (q.exp){ ST.xu -= q.xu; ST.qd = ST.qd || {}; ST.qd[n] = 1; ST.exp = 1; T_('chk5', () => checkLevel()); } else T_('pay', () => doQuest(n)); } return; }
    if (q.t === 'weed'){ for (let r = 0; r < 3 && weedLeft().length; r++) for (const i of weedLeft()) T_('weed', () => weedAt(WEEDP[i][0], WEEDP[i][1], .5)); T_('chkw', () => checkLevel()); return; }
    if (q.t === 'goal'){ if (goalsMet(q)){ ST.qd = ST.qd || {}; ST.qd[n] = 1; return; }
      /* việc bot không tự làm được (câu cá, nấu cá): coi như mất thêm thời gian ước lượng rồi cho qua */
      const hard = { 16: 1.5, 19: 2.5 }; if (hard[n]){ if (qWait[n] == null) qWait[n] = day; if (day - qWait[n] >= hard[n]){ ST.qd = ST.qd || {}; ST.qd[n] = 1; forced.push([n, 'ước lượng ' + hard[n] + ' ngày']); } } } }
  function extra(day){ const lv = ST.lv || 1;
    if (lv >= 9){ const fk = Object.keys(FISHK).filter(k => FISHK[k].tier === 0); if (fk.length && Math.random() < .6){ const k = fk[Math.floor(Math.random() * fk.length)]; ST.inv[k] = (ST.inv[k] || 0) + 1; ST.fishLog = ST.fishLog || {}; ST.fishLog[k] = ST.fishLog[k] || { n: 0 }; ST.fishLog[k].n++; } }   /* giả lập câu ~2 con mỗi ngày */
    if (lv >= 9 && !Object.keys(ST.fishLog || {}).some(k => FISHK[k])){ ST.fishLog = ST.fishLog || {}; ST.fishLog.caro = { n: 1 }; forced.push([lv, 'câu cá đầu (giả lập)']); }
    if (lv >= 13 && !((ST.dc && ST.dc.items) || []).length){ T_('dc', () => { const k = Object.keys(DCK).find(k => DCK[k].cat === 'k' && !DCK[k].sp && ST.xu > DCK[k].price + 200); if (k){ dcBuy(k); const P = PLOTS.find(P => P.bai && !hidP(P) && landSt(P.id) === 'own' && locked(P) && !objAt(P.id) && bigCellFree(P.id)); if (P) dcPlace(k, P.id); } }); }
    if (lv >= 13) T_('upx', () => { if (ST.nong && ST.nong.own && ST.nong.trays.length <= NONG.n && ST.xu > 600) upxBuy('nong'); });
    if (T_('gon', () => gioOn())){ T_('gt', () => gio.take()); T_('gp', () => gio.put()); }
    if (lv >= 16 && !(ST.big.ao && ST.big.ao.own) && ST.xu > 800) T_('ao', () => { for (const P of PLOTS){ if (!P.bai || hidP(P)) continue; if (bigFit(P.id, 'ao')){ aoBuy(P.id); break; } } });
    if (lv >= 19){ T_('tbb', () => { if (!ST.tb && ST.xu > TB.xu + 100) tbBuild(); }); T_('tbt', () => tbTake()); } }
  function visit(day){ T_('pt', () => penTick(performance.now() / 1000)); { const tt = performance.now() / 1000; for (const f of [() => bldTick(tt), () => maiTick(tt), () => nhaTick(tt), () => tbTick(tt), () => ftTick(tt), () => ongTick(tt)]) T_('tick', f); } extra(day); T_('dd', () => { if (window.__FT2 && window.__FT2.ddCheck) window.__FT2.ddCheck(); }); odd(); animals(); farm(); craft(); orders(); sellAll(); grow(); farm(); tasks(); quest(day); T_('chk', () => checkLevel()); try { document.querySelectorAll('.lvup,#lvup').forEach(e => { e.hidden = true; }); window.LVON = false; } catch (e) {} }
  function stat(){ return { ordL: ((ST.ord && ST.ord.list) || []).map(o => o.items.map(([k, q]) => k + ':' + has(k) + '/' + q).join(',')).join(' | '), gheL: ST.ghe && ST.ghe.o ? ST.ghe.o.items.map(([k, q]) => k + ':' + has(k) + '/' + q).join(',') : '-', lv: ST.lv, xp: ST.xp, xu: ST.xu, open: ST.open.length, trees: nTrees(), ord: (ST.ord && ST.ord.done) || 0, ghe: (ST.ghe && ST.ghe.done) || 0, days: ST.daysN || 0, nong: (ST.nong && ST.nong.done) || 0, say: (ST.say && ST.say.done) || 0, hatched: (ST.ga && ST.ga.hatched) || 0, qd: Object.keys(ST.qd || {}).join(','), tasksDone: ST.tasks ? ST.tasks.list.filter(x => x.done).length : 0, need: (() => { const q = QUEST[(ST.lv || 1) + 1]; return q && !(ST.qd || {})[(ST.lv || 1) + 1] ? q.txt + (q.t === 'goal' ? ' ' + q.goals.map(([t, f, n]) => t + ':' + f() + '/' + n).join(' ') : q.t === 'pay' ? ' ' + q.xu + 'xu' : '') : ''; })() }; }
  return { step, visit, stat, E, forced, setGap: g => gap = g };
})();
