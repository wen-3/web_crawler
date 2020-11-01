import requests
import json
import pandas as pd

# 取得頁面資料
def Get_PageContent(url, keyword, i):
    # 查詢參數
    my_params = {
        'q':keyword,
        'page':i,
        'sort':'sale/dc'
    }

    res = requests.get(url, params = my_params)
    content = json.loads(res.text)      # 將json字串轉成Python字典(以方便萃取出商品資料)
    return content

# 取得商品資料
def Parse_Get_MetaData(url, keyword, page):
    product_no = 0    # 商品序號
    products_list = []

    # 依頁碼順序取資料，各頁的商品包在'prods'中
    for i in range(1, page+1):
        data = Get_PageContent(url, keyword, i)

        if 'prods' in data:
            products = data['prods']    # 每分頁的商品資料都存在鍵「'prods'」中
        
            for product in products:     # 取出各頁中的每個商品
                product_no += 1
                products_list.append({
                    '編號': product_no,
                    '品名': product['name'],
                    '商品連結':'https://24h.m.pchome.com.tw/prod/' + product['Id'],   # product['Id'] 代表產品 id
                    '價格': product['price'],
                    '頁數':i
                })
        else:
            break
    
    return products_list

# 主程式
def main():

    url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results"
    keyword = input("請輸入欲查詢之商品關鍵字：")
    page_crawl = int(input("輸入要爬取頁數："))

    save_result = Parse_Get_MetaData(url, keyword, page_crawl)

    # 存入 excel 中
    df = pd.DataFrame(save_result)
    df.to_excel('pchome24.xlsx', sheet_name='sheet1', columns=['編號','品名','商品連結','價格','頁數'], encoding="utf-8")

if __name__ == '__main__':
    main()
