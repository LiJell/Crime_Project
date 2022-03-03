# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 14:07:31 2022

@author: hanju
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing
data_20 = pd.read_excel('D:/multi_project_sample_data_/2020_total_per_area.xlsx')
data_20_c = data_20.copy()
data_20_a = data_20_c.iloc[:,1:]
data_20_a

min_max_scaler = preprocessing.MinMaxScaler()
scaled_20 = min_max_scaler.fit_transform(data_20_a)
scaled_data_2020 = pd.DataFrame(scaled_20, columns = data_20_a.columns)
scaled_data_2020
total_place = data_20_c['자치구']
total_final = pd.concat([scaled_data_2020,total_place], axis=1)

total_final.to_excel('D:/multi_project_sample_data_/2020_scaled_data.xlsx', index= False)
