```python
import requests
import json
import pandas as pd

searching = '서울시 편의점'
url = 'http://dapi.kakao.com/v2/local/search/keyword.json?query={}'.format(searching)
url

headers = {
    "Authorization": "KakaoAK f6ad62d2084bd0b047bdec6cc95b0ad1"
}

places = requests.get(url, headers = headers).json()
places

result = {'place_name': [],'address_name': [], 'x':[], 'y':[]}


for place in places['documents']:
    result['place_name'].append(place['place_name'])
    result['address_name'].append(place['address_name'])
    result['x'].append(place['x'])
    result['y'].append(place['y'])
    
df = pd.DataFrame(result)
df
```





