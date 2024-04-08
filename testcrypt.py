import requests

url = "https://public-api.birdeye.so/public/tokenlist?sort_by=v24hUSD&sort_type=desc&limit=10"

headers = {"X-API-KEY": "12f5f5656e734628830b8a78f0598867"}

response = requests.get(url, headers=headers)

print(response.text)
