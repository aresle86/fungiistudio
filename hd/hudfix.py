#!/usr/bin/env python3
"""Góc trên gọn lại: nút Về giữa và Sửa vườn về lại cột phải dưới đồng xu (v93 lỡ để .bt position:relative làm hai nút này rớt về góc trái, đè tên);
điện thoại: hàng nút dưới chừa chỗ cho cột Hạt/Rơm, không chồng lên nhau. Dùng: python3 hudfix.py <vào> <ra>."""
import sys
s = open(sys.argv[1], encoding='utf8').read()
CSS = """
/* ===== HUD gọn: mỗi thứ một chỗ cố định ===== */
.bt.ctr{position:fixed!important;left:auto!important;right:max(12px,env(safe-area-inset-right,0px))!important;width:64px!important;z-index:3}
.bt.ctr img{width:46px!important;height:46px!important}.bt.ctr .tg{font-size:11px!important;padding:2px 7px 3px!important}
@media (max-width:560px){ .ui.bot>.row{margin-left:84px!important;gap:2px!important;justify-content:space-between!important;flex-wrap:nowrap!important} .ui.bot>.row .bt{width:auto!important;flex:1 1 0;min-width:0} .ui.bot>.row .bt img{width:46px!important;height:46px!important} .ui.bot>.row .tg{font-size:11px!important;padding:2px 6px 3px!important} .bt.ctr{width:56px!important} .bt.ctr img{width:40px!important;height:40px!important} }
"""
i = s.rindex('</style>'); s = s[:i] + CSS + s[i:]
open(sys.argv[2], 'w', encoding='utf8').write(s); print('ok')
