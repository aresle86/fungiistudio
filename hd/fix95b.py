#!/usr/bin/env python3
"""v95b (chạy sau bubfix + fix95): thanh tiến độ trên bong bóng theo đúng kiểu thẻ việc (viên thuốc nâu, lõi vàng, số thời gian trắng viền nâu nằm giữa),
bỏ chữ "Xóm", thông báo ngắn dời xuống dưới (không đè bong bóng giữa màn hình), bảng đất đang phơi ải có thanh tiến độ."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

# ---- thanh tiến độ trên bong bóng: vẽ bằng canvas đúng kiểu .nqb ----
rep("""  { const bar = G(0, -.42, .012, 0, g); bar.visible = false; M(new T.PlaneGeometry(.42, .085), MB(BN), 0, 0, 0, { p: bar, cast: false }).userData.ro = 0; M(new T.PlaneGeometry(.39, .055), MB('#6B4529'), 0, 0, .002, { p: bar, cast: false }).userData.ro = 2; const fg = new T.PlaneGeometry(.39, .055); fg.translate(.195, 0, 0); const fill = M(fg, MB('#F2C64A'), -.195, 0, .004, { p: bar, cast: false }); fill.userData.ro = 3; g.userData.bar = bar; g.userData.fill = fill; }   /* thanh tiến độ dưới bong bóng */""",
    """  { const cv = document.createElement('canvas'); cv.width = 320; cv.height = 72; const tx = new T.CanvasTexture(cv); tx.colorSpace = T.SRGBColorSpace; tx.anisotropy = 4; const bar = new T.Mesh(new T.PlaneGeometry(.62, .62 * 72 / 320), new T.MeshBasicMaterial({ map: tx, transparent: true, toneMapped: false })); bar.position.set(0, -.5, .012); bar.userData.ro = 3; bar.userData.cv = cv; bar.userData.tx = tx; bar.userData.key = ''; bar.visible = false; g.add(bar); g.userData.bar = bar; }   /* thanh tiến độ dưới bong bóng, cùng kiểu thanh trong thẻ việc */""")
rep("""function bubCol(g, c){""",
    """function bubBar(br, f, left){ f = Math.max(0, Math.min(1, f)); const mn = Math.max(1, Math.ceil(left / 60000)), txt = mn >= 60 ? `còn ${Math.ceil(mn / 60)} giờ` : `còn ${mn} phút`, key = Math.round(f * 60) + txt; if (br.userData.key === key) return; br.userData.key = document.fonts && document.fonts.status !== 'loaded' ? '' : key;
  const cv = br.userData.cv, x = cv.getContext('2d'), W = cv.width, H = cv.height, rr = (a, b, w, h, r) => { x.beginPath(); x.moveTo(a + r, b); x.arcTo(a + w, b, a + w, b + h, r); x.arcTo(a + w, b + h, a, b + h, r); x.arcTo(a, b + h, a, b, r); x.arcTo(a, b, a + w, b, r); x.closePath(); };
  x.clearRect(0, 0, W, H); rr(2, 2, W - 4, H - 4, (H - 4) / 2); x.fillStyle = '#4A2F1E'; x.fill(); rr(8, 8, W - 16, H - 16, (H - 16) / 2); x.fillStyle = '#6B4529'; x.fill();   /* viền nâu đậm, lòng nâu */
  x.save(); rr(8, 8, W - 16, H - 16, (H - 16) / 2); x.clip(); x.fillStyle = 'rgba(0,0,0,.25)'; x.fillRect(8, 8, W - 16, 5); const fw = (W - 16) * f; if (fw > 1){ const gr = x.createLinearGradient(0, 8, 0, H - 8); gr.addColorStop(0, '#FFE27A'); gr.addColorStop(1, '#F2C64A'); rr(8, 8, Math.max(fw, H - 16), H - 16, (H - 16) / 2); x.fillStyle = gr; x.fill(); x.clip(); x.fillStyle = 'rgba(184,134,46,.6)'; x.fillRect(8, H - 15, Math.max(fw, H - 16), 7); } x.restore();   /* lõi vàng, bóng đáy như thanh trong thẻ */
  x.font = `400 34px ${getComputedStyle(document.body).getPropertyValue('--f-game') || 'sans-serif'}`; x.textAlign = 'center'; x.textBaseline = 'middle'; x.lineJoin = 'round'; x.lineWidth = 7; x.strokeStyle = '#4A2F1E'; x.strokeText(txt, W / 2, H / 2 + 2); x.fillStyle = '#fff'; x.fillText(txt, W / 2, H / 2 + 2); br.userData.tx.needsUpdate = true; }
function bubCol(g, c){""")
rep("""function objBub(V, v, url, t, y = .62, f){""", """function objBub(V, v, url, t, y = .62, f, left){""")
rep("""const br = b.userData.bar; if (br){ br.visible = f != null; if (f != null) b.userData.fill.scale.x = Math.max(.02, Math.min(1, f)); }""",
    """const br = b.userData.bar; if (br){ br.visible = f != null; if (f != null) bubBar(br, f, left || 0); }""")
rep("""1 - bldLeft(k) / Math.max(1, (BLDH[k] - Math.min(BLDH[k] / 2, (ST.bld[k].help || 0))) * 3600e3 / (ST.spd || 1)));""",
    """1 - bldLeft(k) / Math.max(1, (BLDH[k] - Math.min(BLDH[k] / 2, (ST.bld[k].help || 0))) * 3600e3 / (ST.spd || 1)), bldLeft(k));""")
rep("""1 - maiLeft() / Math.max(1, (MAI.h - Math.min(MAI.help, ST.mai.help || 0)) * 3600e3 / (ST.spd || 1)));""",
    """1 - maiLeft() / Math.max(1, (MAI.h - Math.min(MAI.help, ST.mai.help || 0)) * 3600e3 / (ST.spd || 1)), maiLeft());""")
rep("""1 - nhaLeft() / Math.max(1, (NHA.h - Math.min(NHA.help, ST.nha.help || 0)) * 3600e3 / (ST.spd || 1)));""",
    """1 - nhaLeft() / Math.max(1, (NHA.h - Math.min(NHA.help, ST.nha.help || 0)) * 3600e3 / (ST.spd || 1)), nhaLeft());""")
rep("""1 - tbLeft() / Math.max(1, (TB.h - Math.min(TB.help, ST.tb.help || 0)) * 3600e3 / (ST.spd || 1)));""",
    """1 - tbLeft() / Math.max(1, (TB.h - Math.min(TB.help, ST.tb.help || 0)) * 3600e3 / (ST.spd || 1)), tbLeft());""")

# ---- bỏ chữ "Xóm" ----
rep("""BLDN = { vit: 'Xóm qua dựng chuồng vịt', ao: 'Xóm qua đào ao', say: 'Xóm qua xây lò sấy' }""",
    """BLDN = { vit: 'Bắt đầu dựng chuồng vịt', ao: 'Bắt đầu đào ao', say: 'Bắt đầu xây lò sấy' }""")
rep("""toast(`${BLDN[k]} · chừng ${BLDH[k]} tiếng`)""", """toast(`${BLDN[k]} · xong sau ${BLDH[k]} tiếng`)""")
rep("""toast(`${BLDN[k]} · còn""", """toast(`${BLDN[k].replace('Bắt đầu', 'Đang')} · còn""")
rep("""toast(`Xóm qua đóng ghe · chừng ${TB.h} tiếng`)""", """toast(`Bắt đầu đóng ghe · xong sau ${TB.h} tiếng`)""")
rep("""toast(`Xóm đang đóng ghe · còn""", """toast(`Đang đóng ghe · còn""")
rep("""toast(`Xóm đang sửa nhà · còn""", """toast(`Đang sửa nhà · còn""")
rep("""toast(`Xóm đang lợp mái · còn""", """toast(`Đang lợp mái · còn""")
rep("""<div class="note">Xóm đóng chừng ${TB.h} tiếng, bạn ghé vườn phụ thì mau hơn.</div>""", """<div class="note">Đóng chừng ${TB.h} tiếng, bạn ghé vườn phụ thì mau hơn.</div>""")
rep("""UX.hero(ICON.cuoc || UIC.task, 'Xóm đang đóng ghe',""", """UX.hero(ICON.cuoc || UIC.task, 'Đang đóng ghe',""")
rep("""'Xóm đang sửa chuồng gà' : 'Xóm đang dựng chuồng vịt'""", """'Đang sửa chuồng gà' : 'Đang dựng chuồng vịt'""", 2)
rep("""say('Xóm qua phụ lợp lại mái rồi đó con.""", """say('Hàng xóm qua phụ lợp lại mái rồi đó con.""")
rep("""say('Xóm qua phụ sửa nhà rồi đó con.""", """say('Hàng xóm qua phụ sửa nhà rồi đó con.""")

# ---- thông báo ngắn nằm dưới, trên hàng nút, không đè bong bóng giữa cảnh ----
rep("""#tstw{position:fixed;left:50%;transform:translateX(-50%);top:calc(env(safe-area-inset-top,0px) + 92px);""",
    """#tstw{position:fixed;left:50%;transform:translateX(-50%);bottom:calc(env(safe-area-inset-bottom,0px) + 118px);flex-direction:column-reverse!important;""")

# ---- đất đang phơi ải: tên bảng đúng, thanh tiến độ, câu tích cực ----
rep("""return ok ? OBJD[ok].title : locked(P) ? (landOwn(id) ? 'Đất trống' : 'Đất hoang')""",
    """return ok ? OBJD[ok].title : locked(P) ? (landOwn(id) ? 'Đất trống' : landSt(id) === 'ai' ? 'Đất đang phơi ải' : 'Đất hoang')""")
rep("""if (ls === 'ai') return h + UX.hero(ICON.cuoc || UIC.sickle, 'Đất đang phơi ải', `Còn ${fmtMin(Math.max(1, (L.end - Date.now()) / 60000))} · thoát game đất vẫn ải`);""",
    """if (ls === 'ai'){ const lf = Math.max(0, L.end - Date.now()), T0 = Math.max(1, (L.m || 20) * 60000); return h + UX.hero(ICON.cuoc || UIC.sickle, 'Nắng đang làm đất tơi', 'Con đi làm việc khác, đất tự tơi kể cả lúc tắt game') + `<div class="pgb"><i><u style="width:${Math.round(Math.max(0, Math.min(1, 1 - lf / T0)) * 100)}%"></u><em>còn ${fmtMin(Math.max(1, lf / 60000))}</em></i></div>`; }""")
css = """.sheet{padding-left:16px!important;padding-right:16px!important;background:linear-gradient(#B07A46 0 34px,var(--dz) 34px)!important}   /* đầu bảng ván kéo sát mép, không lòi viền kem hai bên */
.pgb{padding:4px 6px 2px}.pgb i{position:relative;display:block;height:22px;border-radius:12px;background:#6B4529;box-shadow:inset 0 2px 0 rgba(0,0,0,.25),0 0 0 2px #4A2F1E;overflow:hidden}
.pgb i u{position:absolute;left:0;top:0;bottom:0;border-radius:12px;background:linear-gradient(#FFE27A,#F2C64A);box-shadow:inset 0 -3px 0 rgba(184,134,46,.6)}
.pgb i em{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;font:400 14px/1 var(--f-game);font-style:normal;color:#fff;text-shadow:1px 1px 0 #4A2F1E,-1px 1px 0 #4A2F1E,1px -1px 0 #4A2F1E,-1px -1px 0 #4A2F1E,0 1.5px 0 #4A2F1E}
"""
i = s.rindex('</style>'); s = s[:i] + css + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
