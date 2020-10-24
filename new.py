# 自由時報電子報

import requests
from bs4 import BeautifulSoup
result = requests.get('https://m.ltn.com.tw/breakingnews/polities/1')

soup =  BeautifulSoup(result.text, 'html.parser')

news_title = soup.select('ul > li > a > p')

print("自由時報電子報政治及熱門前五大新聞標題:")

count = 0

for item in news_title[0:5]:
    count+= 1
    print("{0:2d}. {1}".format(count, item.text))