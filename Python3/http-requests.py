import requests
url = 'http://www.google.com'
response = request.get(url)
print(f'Request to {url}. Status code is {response.status_code}.')