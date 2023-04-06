import requests
import base64
import json
import os
import wget

url = "https://avaye-ryra.ir/wp-json/wp/v2/posts"

creditionals = 'adminy:e7j7 V4NF SBXv uEs9 URmS 077A'
token = base64.b64encode(creditionals.encode()).decode()

header = {'Authorization': f'Basic {token}'}

babo = wget.download('https://cdn.borna.news/thumbnail/jGQcWuuSTlYf/zKlnR2CgDMsLPypExSqkWVexFSgSRltNvp3exfX06vug6WJOtspsxLwVvO9faXc9wvplisndFdUHpxCkrVbVYeF9dj5XguJb/74.jpg')

# pic = os.rename('74.jpg','image.jpg')

media = {
    'file' : open('74.jpg', 'rb'),
    'caption' : 'try try'
}

image = requests.post(url + '/media', headers=header, files=media)
imageURL = str(json.loads(image.content))
print(imageURL)


post = {
    'date': '2023-04-04T21:00:00',
    'title': 'first try',
    'content': 'kosshere mahz for try <img src="' + imageURL + '">'
}

r = requests.post(url, headers=header, data=post)

print(r)