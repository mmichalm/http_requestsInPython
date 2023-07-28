import requests

base = 'http://ptl-cb6c39e68d6f-79c0eca57a88.libcurl.me/'
url = base + 'pentesterlab?key=please&key=please'

response = requests.get(url)

print(response.text)

