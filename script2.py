#This script is mostly the same as the first one, except it sends a cookie

import requests

url = 'http://ptl-23b8ef958187-e73aed315a6d.libcurl.me/pentesterlab'

#We can send cookies using a dictionary, this is a firt way to define it in Python
#cookie = dict(key='please')

#this is the second way
cookie = {'key':'please'}


response = requests.get(url, cookies=cookie)

print(response.content)

