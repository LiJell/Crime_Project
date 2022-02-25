# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 10:44:22 2022

@author: hanju
"""

import numpy as np
import pandas as pd


# 2020
total = pd.read_excel('D:/multi_project_sample_data_/2020_edit_data_total.xlsx')
total_a = total.copy()

total_1 = total_a[total_a.columns.difference(['기간', '자치구','범죄발생건수/인구'])]
total_1



    
total_1.iloc[:,0]
total_1.columns
len(total.columns)
data = pd.DataFrame(index = range(len(total_a)))
for i in range(len(total_1.T)):
    
    name = '(범죄발생건수/인구) / '+'(' + total_1.columns[i]+ ')'
    data[name] = total_a['범죄발생건수/인구'] / total_1.iloc[:,i]    
 


total_place = total_a['자치구']
total_final = pd.concat([total_place,data], axis=1)
total_final.to_excel('D:/multi_project_sample_data_/2020_per_variable_finall.xlsx', index = False)

# 2019

total = pd.read_excel('D:/multi_project_sample_data_/2019_edit_data_total.xlsx')
total_a = total.copy()

total_1 = total_a[total_a.columns.difference(['기간', '자치구','범죄발생건수/인구'])]
total_1



    
total_1.iloc[:,0]
total_1.columns
len(total.columns)
data = pd.DataFrame(index = range(len(total_a)))
for i in range(len(total_1.T)):
    
    name = '(범죄발생건수/인구) / '+'(' + total_1.columns[i]+ ')'
    data[name] = total_a['범죄발생건수/인구'] / total_1.iloc[:,i]    
 


total_place = total_a['자치구']
total_final = pd.concat([total_place,data], axis=1)
total_final.to_excel('D:/multi_project_sample_data_/2019_per_variable_finall.xlsx', index = False)


