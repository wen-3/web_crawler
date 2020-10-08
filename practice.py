import requests
from bs4 import BeautifulSoup

url = 'https://search.books.com.tw/search/query/key/python/cat/all'
r = requests.get(url)

print(r.status_code)
# print(r.text)

# sp = BeautifulSoup( r.text, 'html.parser')
# results = sp.find_all("li").select(".item")
# for result in results.head:
#     print(results)

