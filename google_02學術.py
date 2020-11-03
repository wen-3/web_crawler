import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

# 取得頁面資料
def Get_PageContent(url):
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')

    return soup

# 取得論文資料
def Parse_Get_MetaData(soup):
    items = soup.select('div.gs_r.gs_or.gs_scl')

    titles = []
    journals = []
    years = []
    title_links = []
    for item in items:
        title = item.select('h3.gs_rt')[0].text 
        
        journal_year = item.select('div.gs_a')[0].text
        journal_year_path = journal_year.split("-")[1]

        journal_year_split = journal_year_path.split(",")

        # 取出期刊
        if bool(re.search(r'\d', journal_year_split[0])) == True:
            journal = " "
        else:
            journal = journal_year_split[0]

        # 取出年份
        journal_year_join = "".join(journal_year_split)
        year = re.findall(r'[0-9]+', journal_year_join)
        
        # title_url = item.select('h3.gs_rt')[0].a.get('href')
        title_url = item.select('h3.gs_rt > a')[0].get('href')

        titles.append(title)
        journals.append(journal)
        years.append(year)
        title_links.append(title_url)

        search_results = {"標題":titles, "期刊":journals, "年分":years, "連結":title_links}
    
    return search_results

# 主程式
def main():
    keyword = input("請輸入欲查詢之商品關鍵字：")
    url =  "https://scholar.google.com.tw/scholar?hl=zh-TW&as_sdt=0%2C5&q=" + keyword
    soup = Get_PageContent(url)

    search_results = Parse_Get_MetaData(soup)
    df = pd.DataFrame(search_results)
    df.to_csv("serch_02test.csv", encoding="utf-8")
    print(df)

if __name__ == '__main__':
    main()