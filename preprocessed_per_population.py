# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 21:04:47 2022

@author: hanju
"""

import pandas as pd 
import numpy as np

data = pd.read_excel('D:/multi_project_sample_data_/data_total_2020.xlsx')
data_1 = data.copy()

data_a = data_1[data_1.columns.difference(['반려동물 가구 비율(%, 인구 수)', '행복지수 종합','기간','자치구','면적(㎢)'])]
data_a
len(data_a.T)


for i in range(len(data_a.T)):
    name = data_a.columns[i] + ' per_population'
    data_a[name] = data_a.iloc[:,i]/data_1['인구 수(명)']    
 
data_a
data_a.columns

total_data= data_a.iloc[:,-10:]
total_data
total_data.columns
place = data_1['자치구']

# 반려동물 100% -> 인구당 동물 수로 변환
data_dog = data_1['반려동물 가구 비율(%, 인구 수)']/ 100


# 행복지수 점수는 10점 기준 환산이기 때문에 10으로 나눠서  인구당 점수로 변환
happy = data_1['행복지수 종합']/100


total_final = pd.concat([place,total_data,data_dog, happy], axis=1)
total_final.to_excel('D:/multi_project_sample_data_/2020_per_population.xlsx', index = False)




# 2019


data = pd.read_excel('D:/multi_project_sample_data_/data_total_2019.xlsx')
data_1 = data.copy()

data_a = data_1[data_1.columns.difference(['반려동물 가구 비율(%, 인구 수)', '행복지수 종합','기간','자치구','면적(㎢)'])]
data_a
len(data_a.T)


for i in range(len(data_a.T)):
    name = data_a.columns[i] + ' per_population'
    data_a[name] = data_a.iloc[:,i]/data_1['인구 수(명)']    
 
data_a
data_a.columns

total_data= data_a.iloc[:,-10:]
total_data
total_data.columns
place = data_1['자치구']

# 반려동물 100% -> 인구당 동물 수로 변환
data_dog = data_1['반려동물 가구 비율(%, 인구 수)']/ 100


# 행복지수 점수는 10점 기준 환산이기 때문에 10으로 나눠서  인구당 점수로 변환
happy = data_1['행복지수 종합']/100


total_final = pd.concat([place,total_data,data_dog, happy], axis=1)
total_final.to_excel('D:/multi_project_sample_data_/2019_per_population.xlsx', index = False)
