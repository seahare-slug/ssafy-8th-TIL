import requests

url = "https://api.agify.io/?name=jun"

print(requests.get(url).json())

response = requests.get(url).json()

print(response.get("name"))