# v149f — ông Bảy Kiếng (chạy bên trong fix149f.py)
rep("/*QUY_END*/", "/*QUY_END*/\n" + open(os.path.join(HERE, 'fix149f_bay.js'), encoding='utf-8').read())
rep("if (kind === 'ben'){ shT.textContent = 'Bến nhà'; h += benHTML(); }", "if (kind === 'ben'){ shT.textContent = 'Bến nhà'; h += benHTML(); }\n  if (kind === 'bay'){ shT.textContent = 'Ông Bảy Kiếng'; h += bayHTML(); }")
rep("else if (a === 'tbbuild'){ tbBuild(); return; }", "else if (a.startsWith('bay')){ bayAct(a, b); return; } else if (a === 'tbbuild'){ tbBuild(); return; }")
rep("if (gheHit(OX, OY)){ openSheet('cho');", "if (bayHit(OX, OY)){ sfx('pick'); openSheet('bay'); return; } if (gheHit(OX, OY)){ openSheet('cho');")
rep("tk('quy', () => quyTick(t));", "tk('quy', () => quyTick(t)); tk('bay', () => bayTick(t));")
rep("  { const me = G(2.95, 0, 1.9, -.5, g); me.userData.tag = 'tôi';", "  try { if (quyOn()){ const t = G(6.75, 0, 1.2, -.35, g); t.userData.tag = 'bay'; bayStall(t); } } catch (e) {}\n  { const me = G(2.95, 0, 1.9, -.5, g); me.userData.tag = 'tôi';")
rep("t === 'bến' || t === 'đò'){ const bb", "t === 'bến' || t === 'đò' || t === 'bay'){ const bb")
rep("else if (best === 'bến' || best === 'đò'){ sfx('pick'); chLeave(); }", "else if (best === 'bay'){ sfx('pick'); $('#chSay').hidden = true; openSheet('bay'); } else if (best === 'bến' || best === 'đò'){ sfx('pick'); chLeave(); }")
rep(".fcd .qst{", """.qset.no img{filter:brightness(0) opacity(.22)}
.bayh{display:flex;gap:12px;align-items:flex-end;margin:0 0 12px}.bayh img{width:96px;height:112px;flex:none}.bayq{flex:1;background:#FFFBF2;border-radius:16px;box-shadow:0 0 0 2px #E3C9A6;padding:12px;font:600 14px/1.45 var(--f-body);color:#4A2F1E}
.bayn{margin:0 0 8px;text-align:center;font:600 12px/1.4 var(--f-body);color:#8A6A4A}
.bayg{display:grid;grid-template-columns:repeat(6,1fr);gap:8px;margin:0 0 12px}.bayg div{position:relative;aspect-ratio:1;background:#FFFBF2;border-radius:16px;box-shadow:0 0 0 2px #E8DFCC;display:flex;align-items:center;justify-content:center}.bayg img{width:84%;height:84%}.bayg .no img{filter:brightness(0) opacity(.22)}.bayg .st{box-shadow:0 0 0 2px #E2B04A;background:#FFF6DC}.bayg .st::after{content:'';position:absolute;right:-4px;bottom:-4px;width:16px;height:16px;border-radius:50%;background:#B8402E;box-shadow:0 0 0 2px #FFFBF2}
.fcd .qst{""")
