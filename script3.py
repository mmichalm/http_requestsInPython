#In this one Content-Type header i set
import requests

url = 'http://ptl-9b6ab8eb5073-548cdc8ad445.libcurl.me/pentesterlab'
header = {'Content-Type':'key/please'}

response = requests.get(url, headers=header)

print(response.content)
