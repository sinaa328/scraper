import requests
from bs4 import BeautifulSoup

links = []
for a in range(0,1):
    link = f"https://www.borna.news/%D8%A8%D8%AE%D8%B4-%D9%88%D8%B1%D8%B2%D8%B4%DB%8C-7?curp=1&categories=7&dateRange%5Bstart%5D=-7776000&order=order_time&page={a}"

    req = requests.get(link)
    soup = BeautifulSoup(req.content, "html.parser")

    news_link = soup.find_all(class_="title", limit=3)

for i in news_link:
    
    mini = i.find("a").attrs["href"]
    links.append("https://www.borna.news"+mini)
    
for x in links:
    print(x)    
    req2 = requests.get(x)
    soup = BeautifulSoup(req2.content, "html.parser")
    res = soup.title
    pic = soup.find(fetchpriority="high")
    cap = soup.find_all(style="text-align:justify")[:-1]
    cap2 = []
    for x in cap:
        cap2.append(x.text)
    print(res.prettify())
    print(pic.attrs['src'])
    for g in range(0,len(cap2)):
        print(cap2[g],end='\n')



    # print(len(cap2))

# print(len(links))
# WP_url = "" + "/wp-json/wp/v2/posts"
