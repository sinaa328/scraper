import requests
import base64
import json


url = "https://avaye-ryra.ir/wp-json/wp/v2/posts"

# auth = HTTPBasicAuth("admin", "3YaP MzHY jlYX XHEG GUXS LZTP")
# creds = {"bot":"Vq3N ENnb Mcf6 VVPE vLSb uE8l"}

# token = base64.b64encode(creds.encode())

header = {'Authorization': 'Basic ' , "bot-scraper" : "sWlP 9gUi CwAh S8Jf 7B5O OVmQ"}

post = {
    'date': '2023-04-04T21:00:00',
    'title': 'first try',
    'content': 'kosshere mahz for try',
    # 'img': 'https://cdn.borna.news/thumbnail/Rf42scs2vWyY/zKlnR2CgDMsLPypExSqkWVexFSgSRltNvp3exfX06vug6WJOtspsxLwVvO9faXc9wvplisndFdUHpxCkrVbVYQ5UUO16yvPQ/509.jpg'
    # 'status': 'publish'
}

r = requests.post(url, headers=header,json=post)

print(r)

# payload = json.dumps({ 
#         "status":"published",
#         "title": "عباس محمدرضایی: استقلال و سپاهان شانس زیادی برای قهرمانی دارند/ عملکرد فنی ساپینتو قابل قبول است",
#         "content": "عباس محمدرضایی، پیشکسوت باشگاه استقلال در گفت‌وگو با خبرنگار گروه ورزشی خبرگزاری برنا درباره نمایش آبی‌پوشان مقابل ذوب‌آهن اصفهان اظهار داشت: فکر می‌کنم بازی خوبی را شاهد بودیم که خوشبختانه با برد استقلال همراه بود. هرچند که نباید از یاد برد چندین ملی‌پوش این تیم در هفته‌های گذشته در تمرینات نبودند اما با روحیه‌ای خوب وارد زمین شدند.",
#         "featured_media": "https://cdn.borna.news/thumbnail/Rf42scs2vWyY/zKlnR2CgDMsLPypExSqkWVexFSgSRltNvp3exfX06vug6WJOtspsxLwVvO9faXc9wvplisndFdUHpxCkrVbVYQ5UUO16yvPQ/509.jpg"
#     })

# response = requests.request(
#     "POST",
#     WP_url,
#     data=payload,
#     headers=headers,
#     auth=auth
#     )
