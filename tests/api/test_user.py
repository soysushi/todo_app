import requests

url = "http://127.0.0.1:8000/api/token/"

payload={'username': 'test',
'password': 'testpass123'}
files=[

]
headers = {}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
