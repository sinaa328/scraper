import requests
import base64
import json
# import os
# import wget

url = "https://avaye-ryra.ir/wp-json/wp/v2"

creditionals = 'adminy:e7j7 V4NF SBXv uEs9 URmS 077A'
token = base64.b64encode(creditionals.encode()).decode()

header = {'Authorization': f'Basic {token}'}

# babo = wget.download('https://cdn.borna.news/thumbnail/jGQcWuuSTlYf/zKlnR2CgDMsLPypExSqkWVexFSgSRltNvp3exfX06vug6WJOtspsxLwVvO9faXc9wvplisndFdUHpxCkrVbVYeF9dj5XguJb/74.jpg')

# pic = os.rename('74.jpg','image.jpg')

media = {
    'file' : open('97.jpg', 'rb'),
    'caption' : 'try try'
}

image = requests.post(url + '/media', headers=header, files=media)
imageURL = json.loads(image.content)
print(imageURL['source_url'])


post = {
    'date': '2023-04-04T21:00:00',
    'title': 'first trey',
    'content': 'kosshere mahz for try',
    'featured_media' : imageURL['id']

}

r = requests.post(url + '/posts', headers=header, data=post)

print(r)