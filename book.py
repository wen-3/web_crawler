import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://search.books.com.tw/search/query/key/python/cat/all'
r = requests.get(url)
# print(r.status_code)

sp = BeautifulSoup( r.text, 'html.parser')
# sp = sp.prettify()

names = sp.find_all("li",class_ = "item", limit = 5)  # 只取五筆

titles = []
prices = []
for name in names:
    title = name.a.get("title")  # 取得書名
    price = name.find_all("b")[1].text  # 取得價格
    # print(title)
    # print(price)
    # print()
    titles.append(title)
    prices.append(price)
book = {"書名":titles, "價格":prices}
df = pd.DataFrame(book)
df.to_csv(r'C:\Users\Desktop\web_crawler\book.csv', encoding="utf-8")
print(df)

