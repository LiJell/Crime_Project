#### 서울시 구별 버스정류장 개수 정보 (2019년)

- 자치구 구별분류번호파일과 서울시 버스정류장 전체 정보가 담긴 파일을 자치구번호를 기준으로 병합
- 구별 버스정류장 개수 출력

```python
import pandas as pd
import numpy as np


num = pd.read_excel('./자치구별 정류소 번호 앞2자리.xlsx')
num.head()

num['구별 번호'] = num['구별 번호'].astype('str').str.zfill(2)
num.head()

num.info()


num.rename(columns={'구별 번호':'자치구번호2자리'}, inplace=True) 
num.head()

stop2019 = pd.read_excel('./서울시버스정류장2019.xlsx')
stop2019.head()

stop2019['ARS-ID'] = stop2019['ARS-ID'].astype('str').str.zfill(5)

stop2019['자치구번호2자리'] = stop2019['ARS-ID']

stop2019['자치구번호2자리'] = stop2019['자치구번호2자리'].str[0:2]

stop_2019_sum = stop2019[['자치구번호2자리','자치구번호']]

bus_stop_2019 = stop_2019_sum.groupby(['자치구번호2자리']).count()
bus_stop_2019.rename(columns={'자치구번호':'버스정류장개수'}, inplace=True)

seoul_stop_cnt = pd.merge(left=num, 
                         right=bus_stop_2019,
                         how='left',
                         left_on='자치구번호2자리',
                         right_on='자치구번호2자리')
seoul_stop_cnt.head()


seoul_stop_cnt.to_excel('./2019_seoul_busstop_cnt.xlsx', index=False)
```

