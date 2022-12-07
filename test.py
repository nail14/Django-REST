import requests
from requests.auth import HTTPBasicAuth

# auth = HTTPBasicAuth(username='andrey', password='1')
# response = requests.get('http://127.0.0.1:8000/api/books/',auth=auth)
# print(response.json())
# data = {'username':'andrey', 'password':'1'}
# response = requests.post('http://127.0.0.1:8000/api-token-auth/', data=data)
# token = response.json().get('Token')
# response_book = requests.get('http://127.0.0.1:8000/api/books/', headers={'Authorization':f'Token {token}'})
# print(response.json())