# v149f — chữ tiếng Anh cho phần đồ quý (exec từ fix149f.py)
import json as _j
_EN = {
 "Ớt sừng vàng đó con. Hồi xưa bà cố trồng một bụi trước sân, trái chín vàng như nghệ, cay mà thơm lắm.": "That's golden horn chili, dear. Great-grandma grew a bush out front; the fruit ripened yellow as turmeric, hot and so fragrant.",
 "Bắp nếp tím nè con. Hồi nhỏ Ngoại hay luộc một nồi, nước ra tím như lá cẩm, cả xóm qua xin.": "Purple sticky corn, dear. When Ngoại was little we boiled a potful, the water came out purple, and the whole hamlet came asking.",
 "Cà chua bi vàng, ngọt như trái cây. Hồi đó má Ngoại để dành cho mấy đứa nhỏ ăn chơi.": "Yellow cherry tomatoes, sweet as fruit. Ngoại's mother used to save them for the little ones to snack on.",
 "Khổ qua rừng trái nhỏ xíu mà đắng thấu trời. Ông ngoại con nói đắng vậy mới mát gan.": "Wild bitter melon, tiny but bitter to the heavens. Your grandpa said that much bitter is what cools the liver.",
 "Mồng tơi tía, nấu canh nước ra tím hồng. Hồi con gái Ngoại còn lấy trái nó nhuộm móng tay.": "Red Malabar spinach turns the soup pink-purple. As a girl Ngoại dyed her nails with its berries.",
 "Khóm mật, ruột vàng như mật ong. Giống này Ngoại tưởng mất luôn rồi, ai dè vườn mình còn giữ được.": "Honey pineapple, flesh gold as honey. Ngoại thought this one was lost for good, and here our garden kept it.",
 "Giống quý": "Rare crops", "Cá quý": "Rare fish", "Đã ghi sổ": "In his book", "Ông Bảy Kiếng tặng": "Gifts from Uncle Bảy",
 "Chưa có giống gốc": "Base crop not unlocked yet", "Chưa ra bến câu": "Not fishing yet",
 "Giàn trái giống trước hiên": "Seed-fruit rack by the porch", "Đã dựng trước hiên nhà": "Standing by the porch",
 "Bảng Tay câu ở bến": "Angler's board at the dock", "Đã treo ở bến nhà": "Hung at the home dock",
 "Đồ quý miệt vườn": "Rare finds", "Đồ quý": "Rare finds", "Ông Bảy Kiếng": "Uncle Bảy Kiếng",
 "Qua là Bảy Kiếng, đi ghe gom đồ quý miệt vườn. Cháu có trái lạ, cá lạ thì để dành cho qua nghe.": "I'm Bảy Kiếng. I go by boat collecting the rare things of the orchards. If you get an odd fruit or an odd fish, save it for me.",
 "Ủa, cháu có món lạ đó hả? Đưa qua coi.": "Oh, you have something unusual there? Let me see.",
 "Cá hô mà cháu cũng gặp rồi hả? Thả nó về là phải. Để qua ghi vô sổ.": "You even met a giant barb? Letting it go was right. Let me write it in my book.",
 "Chèn ơi, ba chục năm qua mới thấy lại trái này. Để qua ghi vô sổ.": "My goodness, thirty years since I last saw this fruit. Let me write it in my book.",
 "Chèn ơi, ba chục năm qua mới thấy lại con này. Để qua ghi vô sổ.": "My goodness, thirty years since I last saw this fish. Let me write it in my book.",
 "Ừa, hàng đẹp vậy thì qua trả thêm cho cháu.": "Fair enough, for goods this fine I'll pay you more.",
 "Khà khà, cháu nói thách còn non lắm.": "Heh heh, you're still green at haggling.",
 "Món này qua chở lên chợ huyện, người ta quý lắm.": "I'll carry this up to the district market. Folks treasure it there.",
 "Chuyện đồ quý qua kể cháu nghe hết rồi đó.": "I've told you every rare-find story I know.",
 "Đủ sáu giống quý rồi! Qua tặng cháu cái giàn treo trái giống, dựng trước hiên cho bà con ghé coi.": "All six rare crops! Here's a rack for hanging seed fruit. Set it by the porch for the neighbors to see.",
 "Đủ năm con cá quý! Qua tặng cháu tấm bảng Tay câu, treo ở bến cho cả xóm biết.": "All five rare fish! Here's an Angler's board. Hang it at the dock so the whole hamlet knows.",
 "Hôm nay qua tìm mua": "Looking for today", "Trả thêm phân nửa giá": "Pays half again",
 "Món quý cháu đang có": "Rare things you have", "Chưa có món nào": "Nothing yet",
 "Chăm liếp cho đúng, câu cho đúng lúc, có ngày gặp.": "Tend the beds right, fish at the right hour, and one day you'll find one.",
 "Cháu gặp rồi thả về sông. Kể qua nghe là đủ.": "You met it and let it go. Telling me is enough.",
 "Kể chuyện cá hô · +900 xu": "Tell the giant barb story · +900 coins",
 "Nói thách": "Haggle", "Sổ tìm mua": "His wanted book", "Hỏi chuyện đồ quý": "Ask about rare finds",
 "Ngày nào qua cũng ngồi ngoài chợ huyện. Thứ Tư với Chủ nhật qua ghé bến nhà cháu.": "I sit at the district market every day. Wednesdays and Sundays I stop at your dock.",
 "Thứ Tư với Chủ nhật qua ghé bến nhà cháu.": "Wednesdays and Sundays I stop at your dock.",
 "Ngoại nghe nói liếp nào chăm đúng ý thì có khi ra trái lạ, kèm hạt giống quý. Con mở Sổ, trang Đồ quý coi thử nghe.": "Ngoại hears a bed tended just right may give an odd fruit with a rare seed. Open the Book, Rare finds page, and have a look.",
 "Sông mình có mấy con cá quý, hiếm ai gặp lắm. Bóng tụi nó Ngoại vẽ sẵn trong Sổ, trang Đồ quý đó con.": "Our river has a few rare fish hardly anyone meets. Ngoại drew their shadows in the Book, Rare finds page.",
 "Vô mùa khô rồi con. Có mấy giống quý chỉ ra mùa này thôi đó.": "Dry season is here, dear. A few rare crops only come now.",
 "Vô mùa mưa rồi con. Có mấy giống quý chỉ ra mùa này thôi đó.": "Rainy season is here, dear. A few rare crops only come now.",
 "Bà con xóm trên": "Folks from the upper hamlet", "mua về ăn thử giống quý vườn mình": "to try your garden's rare crops",
 "Cô Út bán rau": "Miss Út the greengrocer",
}
_new = {k: v for k, v in _EN.items() if (_j.dumps(k, ensure_ascii=False) + ': ') not in s}
print('en skip', sorted(set(_EN) - set(_new)))
rep('const UIEN = {', 'const UIEN = {' + ', '.join(_j.dumps(k, ensure_ascii=False) + ': ' + _j.dumps(v, ensure_ascii=False) for k, v in _new.items()) + ', ')
rep("const ordWhyOf = o => o.ghe || o.lead || o.mam ? o.why", "const ordWhyOf = o => o.ghe || o.lead || o.mam || o.quy ? o.why")
