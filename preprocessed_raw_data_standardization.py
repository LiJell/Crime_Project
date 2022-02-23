# -*- coding: utf-8 -*-
"""
Created on Wed Feb 23 17:46:49 2022

@author: hanju
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
data = pd.read_excel('D:/multi_project_sample_data_/data_total_2020.xlsx')
data_all = data.copy()

all_data = data_all[data_all.columns.difference(['자치구', '기간'])]
all_data
data_standadized = StandardScaler().fit_transform(all_data)
data_standadized.mean()
all_standardized = pd.DataFrame(data_standadized, columns = all_data.columns)

jachigu = data_all['자치구']

all_standardized['자치구'] = jachigu
all_standardized.describe()
all_standardized.to_excel('D:/multi_project_sample_data_/2020_standardized.xlsx', index = False)
# 2019
data = pd.read_excel('D:/multi_project_sample_data_/data_total_2019.xlsx')
data_all = data.copy()

all_data = data_all[data_all.columns.difference(['자치구', '기간'])]
all_data
data_standadized = StandardScaler().fit_transform(all_data)
all_standardized = pd.DataFrame(data_standadized, columns = all_data.columns)

jachigu = data_all['자치구']

all_standardized['자치구'] = jachigu
all_standardized
all_standardized.to_excel('D:/multi_project_sample_data_/2019_standardized.xlsx', index = False)


