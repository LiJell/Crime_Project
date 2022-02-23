# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:07:39 2022

@author: tnals
"""


import numpy as np
import pandas as pd
import math

import matplotlib.pyplot as plt
import seaborn as sns
plt.rcParams['figure.figsize'] = [10, 6]
%matplotlib inline

# boxplot 시각화
df = pd.read_excel('../data/data_total_2019.xlsx')
df.groupby(['', 'cafe개수']).size()

plt.boxplot(df['인구 수(명)'])
plt.show()


# 면적당 column들의 값 비율 및 데이터 스케일링
df.columns
var_list = ['인구 수(명)', '범죄발생건수', '경찰관서 수', '소방관서 수', '카페 수',
            '편의점 수', '공원 수', '버스정류장 수', '가로등 수', 'ATM 수']
df1 = df[var_list].div(df.면적, axis = 0) # var_list의 열들을 '면적'열의 값으로 한번에 나누기
df1['기간'] = df['기간']
df1['자치구'] = df['자치구']
df1 = df1[['기간', '자치구', '인구 수(명)', '범죄발생건수', '경찰관서 수', '소방관서 수',
           '카페 수', '편의점 수', '공원 수', '버스정류장 수', '가로등 수', 'ATM 수']]
df1.to_excel('../data/data_total_2019_pre_area.xlsx', index = False)

# 면적당 
var_list = ['인구 수(명)', '범죄발생건수', '경찰관서 수', '소방관서 수', '카페 수',
            '편의점 수', '공원 수', '버스정류장 수', '가로등 수', 'ATM 수']
df1 = df[var_list].div(df['인구 수(명)'], axis = 0) # var_list의 열들을 '면적'열의 값으로 한번에 나누기
df1['기간'] = df['기간']
df1['자치구'] = df['자치구']
df1 = df1[['기간', '자치구', '인구 수(명)', '범죄발생건수', '경찰관서 수', '소방관서 수',
           '카페 수', '편의점 수', '공원 수', '버스정류장 수', '가로등 수', 'ATM 수']]
df1.to_excel('../data/data_total_2019_pre_area.xlsx', index = False)

# RobustScaler
# 이상치 영향 최소화
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler # 표준화(standardization)
from sklearn.preprocessing import MinMaxScaler # 정규화

# RobustScaler
df1_cp = df.copy()
df1_cp = df1_cp.drop(['기간', '자치구'], axis = 1)
scaler = RobustScaler()
scaler = scaler.fit_transform(df1_cp)

# StandardScaler
scaler = StandardScaler()
scaler = scaler.fit_transform(df1_cp)
df1_cp_std = (df1_cp - np.mean(df1_cp, axis = 0)) / np.std(df1_cp, axis = 0)


# MinMaxScaler
scaler = MinMaxScaler()
scaler = scaler.fit_transform(df1_cp)
scaler_df = pd.DataFrame(scaler, columns = df1_cp.columns)
scaler_df['기간'] = df['기간']
scaler_df['자치구'] = df['자치구']

scaler_df = scaler_df[['기간', '자치구', '인구 수(명)', '범죄발생건수', '경찰관서 수', '소방관서 수',
           '카페 수', '편의점 수', '공원 수', '버스정류장 수', '가로등 수', 'ATM 수']]

scaler_df.to_excel('../data/data_total_Scaler_2019.xlsx', index = False)
