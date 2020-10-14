import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://search.books.com.tw/search/query/key/python/cat/all'
r = requests.get(url)
# print(r.status_code)

sp = BeautifulSoup( r.text, 'html.parser')
# sp = sp.prettify()

names = sp.find_all("li",class_ = "item", limit = 5)  # 只取五筆

for name in names:
    print(name.a.get("title"))  # 取得書名
    print(name.find_all("b")[1].text)  # 取得價格
    print()


# for name in names:
#     title = name.a.get("title"))
#     price = name.find_all("b")[1].text) 

