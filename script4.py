#In this one Accept-Language header is set
import requests

base = 'http://ptl-efedca71de1a-13be3f04fc1b.libcurl.me/'

url = base + 'pentesterlab'
header = {'Accept-Language':'key-please'}

response = requests.get(url, headers=header)

print(response.text)
