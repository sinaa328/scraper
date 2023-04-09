import requests
from bs4 import BeautifulSoup
import json
import base64
import wget
import os
import random
import glob


timefake = []
for mounth in range(1,13):
    if mounth < 10:
        mounth = "0" + str(mounth)
    for day in range(1,31):
        if day < 10:
            day = "0" + str(day)
        for s in range(3):
            time = f"2022-{mounth}-"
            time = time + str(day)
            hour = random.randint(0,24)
            minute = random.randint(0,60)
            if hour < 10:
                hour = '0' + str(hour)
            if minute < 10:
                minute = '0' + str(minute)
            time = time + 'T' + str(hour) + ':' + str(minute) + ':00'
            timefake.append(time)  
h = 0



links = []
for a in range(0,1):
    link = f"https://www.borna.news/%D8%A8%D8%AE%D8%B4-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C-7?curp=1&categories=7&dateRange%5Bstart%5D=-7776000&order=order_time&page={a}"

    req = requests.get(link)
    soup = BeautifulSoup(req.content, "html.parser")

    news_link = soup.find_all(class_="title", limit=1)

for i in news_link:
    
    mini = i.find("a").attrs["href"]
    links.append("https://www.borna.news"+mini)

for x in reversed(links):
    print(x)        
    req2 = requests.get(x)
    soup = BeautifulSoup(req2.content, "html.parser")
    res = soup.title
    pic = soup.find(fetchpriority="high")
    cap = soup.find_all(style="text-align:justify")[:-1]
    cap2 = []

    for x in cap:
        cap2.append(x.text)

    res1 = res.prettify()    
    res1 = res1.replace('<title>','')
    res1 = res1.replace('</title>','')

    print(res1)
    print(pic.attrs['src'])
    cap3 = ''
    for g in range(0,len(cap2)):
        cap3 += cap2[g] + '\n'
    print(cap3)

    url = "https://avaye-ryra.ir/wp-json/wp/v2"

    creditionals = 'adminy:e7j7 V4NF SBXv uEs9 URmS 077A'
    token = base64.b64encode(creditionals.encode()).decode()

    header = {'Authorization': f'Basic {token}'}

    babo = wget.download(pic.attrs['src'])

    for file in glob.glob('./*.jpg'):
        pic = os.rename(file,'image.jpg')

    media = {
        'file' : open('image.jpg', 'rb')
    }

    image = requests.post(url + '/media', headers=header, files=media)
    imageURL = json.loads(image.content)
    print(imageURL['link'])

    post = {
        'date': timefake[h],
        'title': res1,
        # 'content': '<img width="1200" height="800" src="' + imageURL['link'] + '"> \n \n \n \n' + cap3,
        'content': cap3,
        'categories' : '4',
        'status' : 'publish',
        'featured_image' : imageURL['link']
    }

    r = requests.post(url + '/posts', headers=header, data=post)
    h += 1

    print(r)