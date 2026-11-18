/* —— chợ nổi: bạn mới chở hàng ra bến thì thấy liền, khỏi tải lại game —— */
const cnbSg = () => JSON.stringify(cnoBcBoats().filter(x => x.real).map(x => [x.nm, x.pk, x.eye, x.it.slice(0, 3).map(t => t.k)]));
function cnbFresh(){ if (!(CHM.on && CHM.kind === 'cn') || !CHM.B) return; const old = CNX.bcL; CNX.bcL = null; const sg = cnbSg(); CNX.bcP = 0;
  if (sg === CNX.scSg){ try { if (SHEET && SHEET.kind === 'chono' && /^bc/.test(String(SHEET.arg))){ const i = +String(SHEET.arg).slice(2); if (JSON.stringify(old && old[i] && old[i].it) !== JSON.stringify(CNX.bcL[i] && CNX.bcL[i].it)) renderSheet(); } } catch (e) {} return; }
  /* xuồng ở bến đổi: dựng lại cảnh chợ lúc con không mở bảng nào, không đang sơn xuồng */
  let busy = !!SHEET || CNX.son || CNX.pa; try { busy = busy || !$('#chFade').hidden; } catch (e) {}
  if (busy){ CNX.bcL = old; CNX.bcP = 1; return; }
  try { const B0 = CHM.B, pos = B0.me.position.clone(), ry = B0.me.userData.ry, had = new Set((old || []).filter(x => x.real).map(x => x.nm)); for (const x of B0.TX || []) try { x.dispose(); } catch (e) {} chFree(); CHM.B = cnoBuild(); CNX.scSg = sg;
    const B = CHM.B, t = performance.now() / 1000; B.me.position.copy(pos); B.me.userData.ry = ry; B.me.rotation.y = ry; let nw = 0; cnoBcBoats().forEach((x, i) => { if (x.real && !had.has(x.nm) && B.pals[i]){ B.pals[i].userData.hit = t; nw++; } }); if (nw && CNX.ben) sfx('pick'); }
  catch (e) { console.warn('cnb fresh', e); } }
setInterval(() => { try { if (!(CHM.on && CHM.kind === 'cn') || document.visibilityState !== 'visible') return; if (CNX.bcP) cnbFresh(); if (Date.now() - (CNX.pollAt || 0) > (CNX.ben ? 15000 : 40000)){ CNX.pollAt = Date.now(); cnbLoad(); } } catch (e) {} }, 3000);
addEventListener('visibilitychange', () => { if (document.visibilityState === 'visible') CNX.pollAt = 0; });
