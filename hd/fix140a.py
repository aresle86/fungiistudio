# v140a: hình món bị lộn (anh Ares 12/11, iPhone: nong phơi hiện toàn hình mía cho ớt khô, chuối phơi, muối...).
# Hình món vẽ một lần lúc mở game bằng một bộ vẽ phụ. iPhone rút bộ vẽ phụ giữa chừng (máy nóng, nhiều tab) thì
# các hình vẽ sau đó lấy lại tấm cuối cùng còn trong bộ đệm (mía). Mở lại game thì hết, nhưng lúc đó hình sai.
# Sửa: trước mỗi lần vẽ, bộ vẽ phụ đã mất thì dựng bộ mới (chép cỡ, màu nền, ánh sáng) rồi vẽ; vẫn không vẽ được
# thì để hình trống, không lấy lộn hình món khác.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v140'", "BUILD = 'v140a'")
rep("function toonRender(ri, sc, cm){ try { toonRender0(ri, sc, cm); } catch (e) { console.warn('toon', e); try { TOONLAST = ri.domElement.toDataURL('image/png'); } catch (e2) { TOONLAST = 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw=='; } } }",
    "const TOONBLANK = 'data:image/gif;base64,R0lGODlhAQABAAAAACH5BAEKAAEALAAAAAABAAEAAAICTAEAOw==';\n"
    "const toonLost = r => { try { return r.getContext().isContextLost(); } catch (e) { return true; } };\n"
    "/* v140a: bộ vẽ phụ bị máy rút thì dựng bộ mới, chép cỡ và cách vẽ của bộ cũ */\n"
    "function toonLive(ri){ if (!toonLost(ri)) return ri; let R = ICR.r; if (!R || R === ri || toonLost(R)) R = ICR.r = new T.WebGLRenderer({ antialias: true, alpha: true, preserveDrawingBuffer: true }); const z = ri.getSize(new T.Vector2()), c = new T.Color(); ri.getClearColor(c); R.setRenderTarget(null); R.setPixelRatio(ri.getPixelRatio()); R.setSize(z.x, z.y); R.setClearColor(c, ri.getClearAlpha()); R.toneMapping = ri.toneMapping; R.toneMappingExposure = ri.toneMappingExposure; R.shadowMap.enabled = ri.shadowMap.enabled; R.shadowMap.type = ri.shadowMap.type; window.__icLost = (window.__icLost || 0) + 1; return R; }\n"
    "function toonRender(ri, sc, cm){ let r2 = ri; try { r2 = toonLive(ri); toonRender0(r2, sc, cm); if (toonLost(r2)) TOONLAST = TOONBLANK; } catch (e) { console.warn('toon', e); try { TOONLAST = toonLost(r2) ? TOONBLANK : r2.domElement.toDataURL('image/png'); } catch (e2) { TOONLAST = TOONBLANK; } } }")
# (2) Hàng tab Chợ lệch (hình anh Ares 12/11): bốn tab chia đều bề ngang nên "Đơn hàng 1" dài hơn ô của nó, tràn ra ngoài mép trái.
#     Sửa: tab rộng theo chữ của nó, phần dư chia đều; máy hẹp thì chữ 13px và bỏ bớt lề.
rep(".seg .sg{white-space:nowrap;min-width:0;padding:0 4px;gap:4px}@media (max-width:430px){.seg .sg{font-size:14px}.seg .sg i{min-width:18px;padding:1px 5px}}",
    ".seg .sg{white-space:nowrap;flex:1 1 auto;min-width:44px;padding:0 8px;gap:4px}@media (max-width:430px){.seg .sg{font-size:14px}.seg .sg i{min-width:18px;padding:1px 5px}}@media (max-width:374px){.seg{gap:2px}.seg .sg{font-size:13px;padding:0 4px}}@media (max-width:340px){.seg .sg{font-size:12px;padding:0 2px;gap:2px}.seg .sg i{min-width:16px;padding:1px 4px}}")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
