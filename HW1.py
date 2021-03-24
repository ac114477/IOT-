#作業一
#練習使用一個民生物聯網 API，例如空氣、地震等感測站所回傳的紀錄資料。
import requests
import json
import pprint
url = "https://sta.ci.taiwan.gov.tw/STA_AirQuality_v2/v1.0/"
r = requests.get(url)
result = r.json()
pprint.pprint(result)