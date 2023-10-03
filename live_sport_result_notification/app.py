import requests
import json
from scorejson import send_info

url = "https://api.sofascore.com/api/v1/sport/football/events/live"

payload = {}
headers = {
  'authority': 'api.sofascore.com',
  'accept': '*/*',
  'accept-language': 'en-US,en;q=0.9,bg;q=0.8',
  'cache-control': 'max-age=0',
  'dnt': '1',
  'if-none-match': 'W/"1e55549cfa"',
  'origin': 'https://www.sofascore.com',
  'referer': 'https://www.sofascore.com/',
  'sec-ch-ua': '"Microsoft Edge";v="117", "Not;A=Brand";v="8", "Chromium";v="117"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-site',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 '
                '(HTML, like Gecko) Chrome/117.0.0.0 Safari/537.36 Edg/117.0.2045.47'
}

response = requests.request("GET", url, headers=headers, data=payload)

data = json.loads(response.text)

result = send_info()

print(result)
