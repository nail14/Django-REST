import time

import requests

DOMAIN = 'http://127.0.0.1:8000'


def timeout():
    time.sleep(2)


def get_url(url):
    return f'{DOMAIN}{url}'


headers = {'Accept': 'application/json; version=v3'}
response = requests.get(get_url('/api/users/'), headers=headers)
print(response.json())