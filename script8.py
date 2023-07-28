import requests

base = 'http://ptl-e9a1129a-625cfa0f.libcurl.so/'
url = base + 'pentesterlab'
#sending a request with custom method
rsp = requests.request('HACK', url)

print(rsp.text)