# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 22:02:47 2022

@author: hanju
"""

import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
data = pd.read_excel('C:/Users/hanju/Desktop/multicamp/project모음/2020_del.xlsx')
data_all = data.copy()

all_data = data_all[data_all.columns.difference(['자치구'])]
all_data
data_minmax = MinMaxScaler().fit_transform(all_data)
data_minmax.mean()
all_minmax = pd.DataFrame(data_minmax, columns = all_data.columns)

jachigu = data_all['자치구']

all_minmax['자치구'] = jachigu
all_minmax.describe()
all_minmax.to_excel('C:/Users/hanju/Desktop/multicamp/project모음/2020_del_minmax.xlsx', index = False)

