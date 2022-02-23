# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 11:11:32 2022

@author: hanju
"""
import pandas as pd 
import numpy as np
# 2020
total = pd.read_excel('D:/multi_project_sample_data_/data_total_2020.xlsx')
total

total_1 = total[total.columns.difference(['반려동물 가구 비율(%, 인구 수)', '행복지수 종합'])]
total_1



    
total_2 = total_1[total_1.columns.difference(['자치구', '면적(㎢)'])]
total_2.iloc[:,0]
total_2.columns
len(total.columns)
for i in range(len(total_2.T)):
    name = total_2.columns[i] + '_per_area'
    total[name] = total_2.iloc[:,i]/total['면적(㎢)']    
 

total = total.iloc[:,-13:-1]

total.to_excel('D:/multi_project_sample_data_/2020_total_per_area.xlsx', index = False)

total.info()


