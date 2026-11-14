# v149f — trang "Đồ quý miệt vườn" trong Sổ (chạy bên trong fix149f.py)
rep("const BTAB = { mon: ['Sổ món',", "const BTAB = { quy: ['Đồ quý miệt vườn', '#E2B04A', '#9A6A14', 'otvang'], mon: ['Sổ món',")
rep("const BSTK = ['giong', 'mon', 'ca', 'buom', 'cotich', 'thu'], BSTN = { mon: 'Món ăn',", "const BSTK = ['giong', 'mon', 'ca', 'quy', 'buom', 'cotich', 'thu'], BSTN = { quy: 'Đồ quý', mon: 'Món ăn',")
rep("const tabOn = k => { const lv = ST.lv || 1;", "const tabOn = k => { const lv = ST.lv || 1; if (k === 'quy') return quyOn();")
rep("else if (tab === 'ca'){ L = pgCa(nr ? 0 : 1); Rr = nr ? '' : pgCa(2); }", "else if (tab === 'ca'){ L = pgCa(nr ? 0 : 1); Rr = nr ? '' : pgCa(2); } else if (tab === 'quy'){ L = pgQuy(nr ? 0 : 1); Rr = nr ? '' : pgQuy(2); }")
rep(".tbch{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 8px}", """.tbch{display:flex;flex-wrap:wrap;gap:8px;margin:0 0 8px}
.fcd .qst{background:#F6E3B0;color:#6B4529;border-radius:999px;padding:0 8px;font:400 12px var(--f-game)}
.qset{display:flex;align-items:center;gap:12px;background:#FFFBF2;border-radius:16px;box-shadow:0 0 0 2px #E8DFCC;padding:8px 12px;margin:0 0 8px}.qset img{width:44px;height:44px;flex:none}.qset b{display:block;font:400 15px var(--f-game);color:#4A2F1E}.qset span{display:block;font:600 12px var(--f-body);color:#6B4529}.qset.ok{box-shadow:0 0 0 2px #E2B04A;background:#FFF6DC}""")
