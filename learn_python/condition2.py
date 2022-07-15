dust = 70

if dust > 70:
    print("미세먼지 농도는 70보다 크다")
elif dust > 50:
    print("미세먼지 농도는 70보다 크다")
else:
    print("미세먼지 농도는 50보다 작거나 같다")

# dust 가 150보다 크다 -> 매우 나쁨
# dust 가 80보다 크고 150이하이다 -> 나쁨
# dust 가 30보다 크고 80이하이다 -> 보통
# dust 가 30이하이다 -> 좋음

if dust > 150:
    print("매우 나쁨")
elif 80 < dust <= 150:
    print("나쁨")
elif 30 < dust <= 80:
    print("보통")
elif dust <= 30:
    print("좋음")