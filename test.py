import requests
import json


resp = requests.get('http://127.0.0.1:8000/api/v2.1/ocm/ocm-provider/')
print('resp = {}'.format(resp.content))
response_native = json.loads(resp.text)
print('response_native = {}'.format(response_native))
