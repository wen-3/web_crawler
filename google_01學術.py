import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

url = 'https://scholar.google.com.tw/scholar?hl=zh-TW&as_sdt=0%2C5&q=job+crafting&btnG='

res = requests.get(url)
soup = BeautifulSoup(res.text, 'html.parser')

items = soup.select('div.gs_r.gs_or.gs_scl')  # 分成三個 class , 須加上「.」做修正

titles = []
journals = []
years = []
title_urls = []
for item in items:
    title = item.select('h3.gs_rt')[0].text     # 必須給索引值才能取出內容
    
    journal_year = item.select('div.gs_a')[0].text
    journal_year_path = journal_year.split("-")[1]

    # journal = journal_year_path.split(",")[0]  # 有些無法用索引值取出, 因為有的只由年份沒有期刊
    journal_year_split = journal_year_path.split(",")   # 分割出期刊和年份

    # 取出期刊
    if bool(re.search(r'\d', journal_year_split[0])) == True:    # 判斷取出的值是否為數字(年份), 是數字就印出空值,不是數字就印出期刊內容
        journal = " "
    else:
        journal = journal_year_split[0]

    # 取出年份
    journal_year_join = "".join(journal_year_split)    # 合併期刊和年份
    year = re.findall(r'[0-9]+', journal_year_join)
    
    # title_url = item.select('h3.gs_rt')[0].a.get('href')
    title_url = item.select('h3.gs_rt > a')[0].get('href')

    titles.append(title)
    journals.append(journal)
    years.append(year)
    title_urls.append(title_url)

search = {"標題":titles, "期刊":journals, "年分":years, "連結":title_urls}
df = pd.DataFrame(search)
df.to_csv("serch_result.csv", encoding="utf-8")
print(df)
