import requests

url = "https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1021"

response = requests.get(url).json()

print(response.get("drwtNo1"))
print(response.get("drwtNo1"))