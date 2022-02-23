# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 15:27:54 2022

@author: hanju
"""
import pandas as pd
import numpy as np
from sklearn import preprocessing

crime = pd.read_excel('D:/multi_project_sample_data_/2020_total_per_area.xlsx')
crime_a = crime.copy()
type(crime_b)

crime_b =crime_a['범죄발생건수_per_area'].copy()
crime_b.to_frame(name='범죄발생건수')
log_crime = crime_b['log'].to_frame(name= 'log')



min_max_scaler = preprocessing.MinMaxScaler()
scaled_crime_log = min_max_scaler.fit_transform(log_crime)
data_df = pd.DataFrame(scaled_crime_log, columns = ['log_crime'])


total_place = crime_a['자치구']
total_final = pd.concat([data_df,total_place], axis=1)

total_final.to_excel('D:/multi_project_sample_data_/2020_crime_logged.xlsx', index = False)

total_final = pd.concat([scaled_data_2020,total_place], axis=1)

crime_log.to_excel('D:/multi_project_sample_data_/2020_crime_log.xlsx')
