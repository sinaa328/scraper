import requests
from bs4 import BeautifulSoup

req = requests.get("https://www.borna.news/fa/tiny/news-1450000")

soup = BeautifulSoup(req.content, "html.parser")

res = soup.title
pic = soup.find(fetchpriority="high")
cap = soup.find_all(style="text-align: justify;")[:-1]
# print(res.prettify())
# print(pic.attrs['src'])
print(cap[0])