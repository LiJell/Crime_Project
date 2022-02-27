# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 13:05:32 2022

@author: hanju
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc
plt.rc('font', family = "Malgun Gothic")
plt.rcParams['axes.unicode_minus'] = False
#   전처리만 된 2019 자료 
seoul = pd.read_excel('D:/multi_project_sample_data_/2019_edit_data_total_rm_outlier.xlsx')
seoul.head()
seoul.columns
seoul.set_index('자치구', inplace = True)
seoul.head()
seoul_a = seoul.drop('범죄발생건수/인구', axis = 1)
seoul_a
seoul_a.columns[0]
len(seoul_a.T)

seoul['범죄발생건수/인구'][0]

print(np.corrcoef(seoul['ATM/면적'], seoul['범죄발생건수/인구']))

len(np.corrcoef(seoul['ATM/면적'], seoul['범죄발생건수/인구'])[1])
type(np.corrcoef(seoul['ATM/면적'], seoul['범죄발생건수/인구'])[1])
cor = pd.DataFrame(index = ['feature', 'crime'])
cor


for i in seoul_a.columns:
    col_name = i + ' cor_coef'
    cor[col_name] = np.corrcoef(seoul[i], seoul['범죄발생건수/인구'])[1]    

cor.to_excel('D:/multi_project_sample_data_/cor_2019.xlsx', index = True)


#   전처리만 된 2020 자료 
seoul = pd.read_excel('D:/multi_project_sample_data_/2020_edit_data_total_rm_outlier.xlsx')
seoul.head()
seoul.columns
seoul.set_index('자치구', inplace = True)
seoul.head()
seoul_a = seoul.drop('범죄발생건수/인구', axis = 1)
seoul_a
seoul_a.columns[0]
len(seoul_a.T)

seoul['범죄발생건수/인구'][0]

print(np.corrcoef(seoul['ATM/면적'], seoul['범죄발생건수/인구']))

len(np.corrcoef(seoul['ATM/면적'], seoul['범죄발생건수/인구'])[1])
type(np.corrcoef(seoul['ATM/면적'], seoul['범죄발생건수/인구'])[1])
cor = pd.DataFrame(index = ['feature', 'crime'])
cor


for i in seoul_a.columns:
    col_name = i + ' cor_coef'
    cor[col_name] = np.corrcoef(seoul[i], seoul['범죄발생건수/인구'])[1]    

cor.to_excel('D:/multi_project_sample_data_/cor_2020.xlsx', index = True)