#In this one the post request is sent
import requests

base = 'http://ptl-8694cb6ac868-7471c7eb0582.libcurl.me/'

url = base + 'pentesterlab'
data = {'key': 'please'}


response = requests.post(url, data=data)

print(response.text)
