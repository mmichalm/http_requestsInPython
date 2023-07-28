import requests

response = requests.get('http://ptl-706cc646d641-3ceae041e8fd.libcurl.me/pentesterlab?key=please')
print(response.content)
