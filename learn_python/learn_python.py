x = True
dust = [1, 2, "M", 3, x]
# 주소참조를 통한 shallow copy
# ddust = dust
# dust[1] = "REVISE"
# print(ddust)

# spread를 통한 deep copy
# ddust = [*dust]
# dust[1] = "change"
# print(ddust)

# 활용
# ddust는 이미 새로운 주소를 할당 받았고 그 후 새로운 dust를 뒤에 붙임(주소 X)
# ddust = [10] + dust
# dust[1] = "REVISE"
# print(ddust)