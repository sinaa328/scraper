import requests
import base64
import json

url = "https://avaye-ryra.ir/wp-json/wp/v2/posts"

creditionals = 'adminy:e7j7 V4NF SBXv uEs9 URmS 077A'
token = base64.b64encode(creditionals.encode()).decode()

header = {'Authorization': f'Basic {token}'}

post = {
    'date': '2023-04-04T21:00:00',
    'title': 'first try',
    'content': 'kosshere mahz for try',
}

r = requests.post(url, headers=header, data=post)

print(r)