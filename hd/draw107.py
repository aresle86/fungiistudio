#!/usr/bin/env python3
"""v107: bớt draw call. Hai bước gộp mesh (tĩnh toàn cảnh và từng nhóm: liếp, cây, chuồng…) đang gộp theo từng vật liệu,
mỗi màu một lần vẽ (điện thoại ~650 lần/khung). Nay vật liệu phẳng cùng đặc tính (độ nhám, mặt, flat shading, không texture,
không trong suốt) dùng chung một vật liệu màu-theo-đỉnh: màu nằm trong thuộc tính 'color' của đỉnh, nhiều màu gộp một lần vẽ.
Hình không đổi (màu đỉnh × màu trắng = màu cũ). Chạy sau fix107.py:  python3 draw107.py live/v107a.html live/v107a.html"""
import sys
s = open(sys.argv[1], encoding='utf8').read()
def rep(a, b, n=1):
    global s
    c = s.count(a); assert c == n, (c, a[:100]); s = s.replace(a, b)

rep("const swayMats = {}; function swayMatOf(m){",
    "const VCM = {};   /* vật liệu chung theo đặc tính, màu nằm trong đỉnh: nhiều màu gộp một lần vẽ */\n"
    "const vcKey = m => m && m.isMeshStandardMaterial && !m.map && !m.transparent && m.opacity === 1 && !m.alphaTest && !m.vertexColors && (!m.emissive || m.emissive.getHex() === 0) && !m.emissiveMap && !m.normalMap ? 'vc' + m.roughness + '/' + m.metalness + '/' + m.side + '/' + (m.flatShading ? 1 : 0) : null;\n"
    "const vcMat = (k, m) => VCM[k] || (VCM[k] = new T.MeshStandardMaterial({ vertexColors: true, flatShading: !!m.flatShading, roughness: m.roughness, metalness: m.metalness, side: m.side }));\n"
    "const vcBake = (g, m) => { const c = m.color, n = g.attributes.position.count, a = new Float32Array(n * 3); for (let i = 0; i < n; i++){ a[i * 3] = c.r; a[i * 3 + 1] = c.g; a[i * 3 + 2] = c.b; } g.setAttribute('color', new T.Float32BufferAttribute(a, 3)); };\n"
    "const swayMats = {}; function swayMatOf(m){")
rep("const sw = o.userData.sway || 0, key = o.material.uuid + (sw > 0 ? 's' : 'n') + (o.castShadow ? 'c' : '');",
    "const sw = o.userData.sway || 0, vk = vcKey(o.material), key = (vk || o.material.uuid) + (sw > 0 ? 's' : 'n') + (o.castShadow ? 'c' : '');", 2)
rep("g.setAttribute('aSway', new T.Float32BufferAttribute(new Float32Array(g.attributes.position.count).fill(sw), 1));",
    "g.setAttribute('aSway', new T.Float32BufferAttribute(new Float32Array(g.attributes.position.count).fill(sw), 1)); if (vk) vcBake(g, o.material);", 2)
rep("if (!buckets.has(key)) buckets.set(key, { mat: o.material, sw: sw > 0, cast: o.castShadow, list: [] });",
    "if (!buckets.has(key)) buckets.set(key, { mat: vk ? vcMat(vk, o.material) : o.material, sw: sw > 0, cast: o.castShadow, list: [] });", 2)
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
