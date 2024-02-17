import requests

response = requests.get("http://api.kanye.rest")
response.raise_for_status()
data = response.json()
print(data)