#作業二
#練習操作 OGC SensorThings API，將環保局測站位置的資料抓取下來，並且觀察下載資料的內容。
#參考網址：https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things
import requests
import json
import pprint
url = "https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things"
r = requests.get(url)
result = r.json()
pprint.pprint(result['value'][0])