import requests
import json
import pandas as pd

# 取得頁面資料
url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results"
my_params = {
    'q':'python',
    'sort':'sale/dc',
    'page':'1',
}

res = requests.get(url, params = my_params)

content = json.loads(res.text) 
print(content)
