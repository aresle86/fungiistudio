# NHÁP v154: bong bóng ghe bẹo hiện lộn hình dưa hấu trên iPhone (Ares báo 15/11/2026).
#   python3 fix154.py live/v153.html live/v154.html
# Gốc: bộ vẽ hình nhỏ dùng chung một khung. Lần vẽ nào hỏng (máy rút bộ vẽ, vẽ lỗi) thì khung còn nguyên hình trước,
# nên hình ghe lấy lộn hình cây cổ tích vẽ trước đó. Giờ: vẽ ra y hình trước hoặc vẽ lỗi thì dựng bộ vẽ mới vẽ lại,
# vẫn hỏng thì để trống chứ không lấy hình cũ; bong bóng ghe gặp hình trống thì vẽ lại lúc cần.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v153'", "BUILD = 'v154'")

rep("""function toonRender(ri, sc, cm){ let r2 = ri; try { r2 = toonLive(ri); toonRender0(r2, sc, cm); if (toonLost(r2)) TOONLAST = TOONBLANK; } catch (e) { console.warn('toon', e); try { TOONLAST = toonLost(r2) ? TOONBLANK : r2.domElement.toDataURL('image/png'); } catch (e2) { TOONLAST = TOONBLANK; } } }""",
"""/* v154: không bao giờ lấy lại hình của lần vẽ trước */
function toonFresh(ri){ const old = ICR.r; ICR.r = null; if (old){ try { old.dispose(); old.forceContextLoss(); } catch (e) {} } if (ri !== old && !toonLost(ri)){ try { ri.forceContextLoss(); } catch (e) {} } return toonLive(ri); }
function toonRender(ri, sc, cm){ const prev = TOONLAST; let r2 = ri, ok = false, drew = false;
  try { r2 = toonLive(ri); toonRender0(r2, sc, cm); drew = !toonLost(r2); ok = drew && TOONLAST !== prev; } catch (e) { console.warn('toon', e); }
  if (!ok && (window.__icRedo || 0) >= 6) ok = drew;   /* hết lượt dựng lại: hình vẽ trọn thì nhận, vẽ lỗi thì để trống */
  else if (!ok){ window.__icRedo = (window.__icRedo || 0) + 1; try { const R = toonFresh(r2); toonRender0(R, sc, cm); ok = !toonLost(R); } catch (e) { console.warn('toon2', e); ok = false; } }
  if (!ok) TOONLAST = TOONBLANK; }""")

# hình ghe bẹo: gói thành hàm để vẽ lại được lúc cần
rep("""  { const ps = sd, nL = LIGHTS.length, sc = new T.Scene(), m = gheBeo(); sd = ps;""",
    """  window.__gheIc = ri => { const ps = sd, nL = LIGHTS.length, sc = new T.Scene(), m = gheBeo(); sd = ps;""")
rep("""toonRender(ri, sc, cm); ICON.ghe = toonURL(); }""",
    """toonRender(ri, sc, cm); return toonURL(); }; ICON.ghe = window.__gheIc(ri);""")
rep("try { bubIcon(b, ICON.ghe); } catch (e) {}",
    "try { if (gheIcBad() && (GHEV.icT || 0) < 3){ GHEV.icT = (GHEV.icT || 0) + 1; const ri = ICR(); ri.setPixelRatio(1); ri.setSize(200, 200); ri.setClearColor(0, 0); ri.toneMapping = T.ACESFilmicToneMapping; ri.toneMappingExposure = 1.05; ICON.ghe = window.__gheIc(ri); ICR.free(); } bubIcon(b, gheIcBad() ? ICON.gio : ICON.ghe); } catch (e) {}")
rep("function gheTick(", "const gheIcBad = () => !ICON.ghe || ICON.ghe === TOONBLANK || ICON.ghe === UIC.tamban || Object.keys(UIC).some(k => k.startsWith('ft_') && UIC[k] === ICON.ghe);\nfunction gheTick(")

# ---- kẹt màn tải 47% "Cannot access 'CNX' before initialization": ai đã sơn mũi ghe tam bản thì lúc tải game
# dựng ghe (TBP) đọc bảng màu CNX.P trước khi CNX được khai báo. Bảng màu sơn chuyển vô hàm TBPP, gọi lúc nào cũng được. ----
P0 = "P: { moc: ['Gỗ mộc', 'Bare wood', 0, '#B48560', '#8A5D3B'], ngoc: ['Xanh ngọc', 'Jade green', 1200, '#3F9C8F', '#F4F0E4'], son: ['Đỏ son', 'Vermilion', 2500, '#B8402E', '#F2C230'], nghe: ['Vàng nghệ', 'Turmeric gold', 4000, '#E0A526', '#7A3B1E'], cham: ['Xanh chàm', 'Indigo', 6000, '#2F4E7A', '#F4F0E4'] },"
rep(P0, "P: TBPP(),")
rep("function TBP(){ const k = ST.tb && ST.tb.paint, P = k && k !== 'moc' && CNX.P[k];",
    "function TBPP(){ return TBPP.t || (TBPP.t = " + P0[3:-1] + "); }   /* v154: bảng màu sơn gọi được từ lúc tải, hàm thì dùng trước chỗ khai báo được */\nfunction TBP(){ const k = ST.tb && ST.tb.paint, P = k && k !== 'moc' && TBPP()[k];")

open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
