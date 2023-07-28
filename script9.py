import requests

base = 'http://ptl-4bbbf4d4-1fffee89.libcurl.so/'
url = base + 'pentesterlab'

header = {'X-HTTP-Method-Override':'HACK'}

rsp = requests.get(url, headers = header)

print(rsp.text)