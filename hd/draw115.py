import sys
a,b=sys.argv[1:3]; s=open(a,encoding='utf8').read()
def rep(x,y,n=1):
    global s
    c=s.count(x); assert c==n,(c,x[:70]); s=s.replace(x,y)
js=open('draw115_pin.js',encoding='utf8').read()
rep("function hen(x, z, ry, kind = 'brown', noTail = false){", js+"function hen(x, z, ry, kind = 'brown', noTail = false){")
# gà
rep("M(sph(.003, 4, 3), '#fff', .026, .014, sz * .038, { p: hd }); } return g; }","M(sph(.003, 4, 3), '#fff', .026, .014, sz * .038, { p: hd }); } if (!noTail) mergeRig(g, [b, nk]); return g; }")
rep("{ p: b, r: [0, 0, -.15] }); } return g; }","{ p: b, r: [0, 0, -.15] }); } mergeRig(g, [b, g.userData.neck]); return g; }")
# vịt
rep("'#cdeff4', -.05, .045, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false }); } return g; }","'#cdeff4', -.05, .045, 0, { p: g, r: [Math.PI / 2, 0, 0], cast: false }); } mergeRig(g); return g; }")
rep("M(sph(.005, 5, 4), C.ink, .058, .097, sz * .018, { p: g }); return g; }","M(sph(.005, 5, 4), C.ink, .058, .097, sz * .018, { p: g }); mergeRig(g); return g; }")
# chuồng vịt
rep("  ROOT = pr; const hit = new T.Mesh(new T.BoxGeometry(1.2, .7, .9),","  const sg = new T.Group(); root.add(sg); for (const o of struct) sg.add(o); mergeLive(sg); mergeLive(up1); mergeLive(up2);\n  ROOT = pr; const hit = new T.Mesh(new T.BoxGeometry(1.2, .7, .9),")
rep("return { root, eggs, feed, hit, struct, bE, bF, up1, up2,","return { root, eggs, feed, hit, struct: [sg], bE, bF, up1, up2,")
# nhân vật
rep("AVW.traverse(o => { if (o.isMesh){ o.castShadow = true; o.userData.sway = 0; } }); AVT = null;","AVW.traverse(o => { if (o.isMesh){ o.castShadow = true; o.userData.sway = 0; } }); mergeRig(AVW, [a.legL, a.legR, a.handL, a.handR]); AVT = null;")
# ghim
rep("M(new T.CircleGeometry(.268, 40), MB(BN), 0, 0, 0, { p: g, cast: false }).userData.ro = 0;","const bord = M(new T.CircleGeometry(.268, 40), MB(BN), 0, 0, 0, { p: g, cast: false }); bord.userData.ro = 0;")
rep("  g.traverse(o => { if (o.isMesh && o.userData.icon){ o.renderOrder = 21; return; }","  if (kind !== 'h' && kind !== 's'){ ic.traverse(o => { if (o.isMesh) o.userData.sway = 0; }); mergeLive(ic); }\n  g.traverse(o => { if (o.isMesh && o.userData.icon){ o.renderOrder = 21; return; }")
rep("o.material.emissiveIntensity = 0; o.renderOrder = 20 + (o.userData.ro","o.material.emissiveIntensity = 0; if (o.material.vertexColors){ vcEmis(o.material); o.material.transparent = true; } o.renderOrder = 20 + (o.userData.ro")
rep("  const hit = new T.Mesh(new T.SphereGeometry(.24, 8, 6), new T.MeshBasicMaterial({ visible: false })); g.add(hit); hit.userData.bub = kind;","  for (const m of [bord, disk, ring, tailB, tail]) m.visible = false; { const pm = new T.Mesh(pinGeo(col, '#FFFBF2', false), PINM); pm.renderOrder = 20.3; g.add(pm); g.userData.pm = pm; }\n  const hit = new T.Mesh(new T.SphereGeometry(.24, 8, 6), new T.MeshBasicMaterial({ visible: false })); g.add(hit); hit.userData.bub = kind;")
rep("for (const m of [u.pl, u.tail, u.tailB]) if (m) m.visible = !on; if (u.disk) u.disk.material.color.set(on ? (u.col || BUBC.lam) : '#FFFBF2'); }","if (u.pl) u.pl.visible = !on; if (u.disk) u.disk.material.color.set(on ? (u.col || BUBC.lam) : '#FFFBF2'); pinSync(g); }")
rep("if (m.material.emissive) m.material.emissive.set(c).multiplyScalar(.5); } }","if (m.material.emissive) m.material.emissive.set(c).multiplyScalar(.5); } pinSync(g); }")
rep("if (g.userData.hotP) for (const x of g.userData.hotP) x.material.color.set(col); }","if (g.userData.hotP){ for (const x of g.userData.hotP) x.material.color.set(col); pinSync(g); } }")
open(b,'w',encoding='utf8').write(s)
