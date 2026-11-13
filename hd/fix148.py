# v148: icon độ thuần thục / tay nghề đổi từ ngôi sao sang nón lá (anh Ares chọn 13/11).
# Cỡ nhỏ dưới thẻ hạt (13) bỏ nan nón cho rõ; cỡ 24 có nan. Chữ "sao" đổi thành "nón" cho khớp hình, cả bản tiếng Anh.
import sys
SRC, DST = sys.argv[1], sys.argv[2]
s = open(SRC, encoding='utf-8').read()
def rep(a, b, n=1):
    global s
    assert s.count(a) == n, (s.count(a), a[:80])
    s = s.replace(a, b)
rep("BUILD = 'v147'", "BUILD = 'v148'")
rep("""<path d="M12 2.6l2.9 5.9 6.5.9-4.7 4.6 1.1 6.5L12 17.4l-5.8 3.1 1.1-6.5L2.6 9.4l6.5-.9z" fill="${i < s ? '#EDB940' : '#E3D3BC'}" stroke="${i < s ? '#C9952A' : '#CDBBA0'}" stroke-width="1.4" stroke-linejoin="round"/></svg>`;""",
    """<path d="M5.6 18C7.3 22.6 16.7 22.6 18.4 18" fill="none" stroke="${i < s ? '#C8452E' : '#CDBBA0'}" stroke-width="1.7" stroke-linecap="round"/><path d="M12 3.2L22.2 16.8Q12 19.8 1.8 16.8Z" fill="${i < s ? '#F0D58E' : '#E3D3BC'}" stroke="${i < s ? '#B07F22' : '#CDBBA0'}" stroke-width="1.5" stroke-linejoin="round"/>${z >= 20 ? `<path d="M12 3.2L8.2 17.9M12 3.2l3.8 14.7M6.9 10.4q5.1 1.5 10.2 0" fill="none" stroke="${i < s ? '#C9A451' : '#CDBBA0'}" stroke-width=".9"/>` : ''}</svg>`;""")
rep("vụ nữa lên sao$", "vụ nữa thêm nón$")
rep("more to the next star", "more to the next hat")
rep("đủ ba sao rồi$", "đủ ba nón rồi$")
rep("Harvested $1 times · all three stars", "Harvested $1 times · all three hats")
rep("sao thuần thục · \\\\+", "nón thuần thục · \\\\+")
rep("$2-star mastery", "$2-hat mastery")
rep("đủ ba sao rồi` :", "đủ ba nón rồi` :")
rep("vụ nữa lên sao`}", "vụ nữa thêm nón`}")
rep("sao thuần thục · +${xu}", "nón thuần thục · +${xu}")
rep("hours worked · all three stars", "hours worked · all three hats")
rep("more for a star:", "more for a hat:")
open(DST, 'w', encoding='utf-8').write(s)
print('ok', len(s))
