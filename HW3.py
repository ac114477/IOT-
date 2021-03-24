#作業3 : 依據作業 2 所下載的各個環保局測站感測器的描述資料，
#進一步點選 Datastreams、Locations，以及 Datastreams 點選進入後，
#點選 Observations 的 URL，觀察所下載到的資料內容，
#其中 Observations 內部是否包含個別感測器紀錄的資料。

import requests
import json
import pprint

url = "https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Things(1)/Datastreams"
r = requests.get(url)
result = r.json()
pprint.pprint(result['value'][0])

url = "https://sta.ci.taiwan.gov.tw/STA_AirQuality_EPAIoT/v1.0/Datastreams(1)/Observations"
r = requests.get(url)
result = r.json()
pprint.pprint(result['value'][0])