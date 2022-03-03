# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 10:59:59 2022

@author: hanju
"""

import pandas as pd
import seaborn as sns
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects




plt.rc('font', family = "Malgun Gothic")
plt.rcParams['axes.unicode_minus'] = False # 한글폰트 사용시 - 부호 표시하기

data = pd.read_excel('D:/multi_project_sample_data_/2019_crime_per_density.xlsx')
data
data_a = data[data.columns.difference(['자치구','기간'])]

bplot= sns.boxplot(data=data_a,)

data_a.describe()
data_columns = data_a.columns
data_columns[0]
data_index = data['자치구']
outlier = pd.DataFrame(index = ['values'])
"데이터의 상한선과 하한선 계산"
for i in data_columns:
    IQR = data_a[i].quantile(0.75) - data_a[i].quantile(0.25)
    lower_outlier = data_a[i].quantile(0.25)-(1.5*IQR)
    upper_outlier = data_a[i].quantile(0.75)+(1.5*IQR)
    name_column = i + 'outlier'
    outlier[name_column] = [[lower_outlier,upper_outlier]]
   

outlier.to_excel('D:/multi_project_sample_data_/IQR_for_outlier.xlsx', index = False)

   # 이상치 대치
   
   
data_b = data[data.columns.difference(['기간'])]
jachigu = data_b['자치구']
data_place = data_b.set_index('자치구')
data_place_columns = data_place.columns
data_place.iloc[:,0]
len(data_place)
data_place['ATM밀도 수 대비 범죄발생건수'][0]
outlier.columns
outlier.iloc[:,0][0][0]
copy_1 = data_place.iloc[1,0].copy()
copy_1.replace(copy_1, outlier.loc[outlier[i][0]])

####################

L_outlier = []
U_outlier = []
for i in range(len(data_place_columns)):
    for j in range(len(data_place)):
        if data_place.iloc[j,i] < outlier.iloc[:,i][0][0]:
           data_place.iloc[j,i] = outlier.iloc[:,i][0][0]
            
            
        elif data_place.iloc[j,i] > outlier.iloc[:,i][0][1]:
            data_place.iloc[j,i] = outlier.iloc[:,i][0][1]
            
            
        else:
            pass
        

data_place.to_excel('D:/multi_project_sample_data_/modified_data_edit.xlsx', index = True)
   

########### 2020

data = pd.read_excel('D:/multi_project_sample_data_/2020_crime_per_density.xlsx')
data
data_a = data[data.columns.difference(['자치구','기간'])]



data_a.describe()
data_columns = data_a.columns
data_columns[0]
data_index = data['자치구']
outlier = pd.DataFrame(index = ['values'])
"데이터의 상한선과 하한선 계산"
for i in data_columns:
    IQR = data_a[i].quantile(0.75) - data_a[i].quantile(0.25)
    lower_outlier = data_a[i].quantile(0.25)-(1.5*IQR)
    upper_outlier = data_a[i].quantile(0.75)+(1.5*IQR)
    name_column = i + 'outlier'
    outlier[name_column] = [[lower_outlier,upper_outlier]]
   

outlier.to_excel('D:/multi_project_sample_data_/IQR_for_outlier_2020.xlsx', index = False)



#####이상치

data_b = data[data.columns.difference(['기간'])]
jachigu = data_b['자치구']
data_place = data_b.set_index('자치구')
data_place_columns = data_place.columns
data_place.iloc[:,0]
len(data_place)
data_place['ATM밀도 수 대비 범죄발생건수'][0]
outlier.columns
outlier.iloc[:,0][0][0]
copy_1 = data_place.iloc[1,0].copy()
copy_1.replace(copy_1, outlier.loc[outlier[i][0]])

####################


for i in range(len(data_place_columns)):
    for j in range(len(data_place)):
        if data_place.iloc[j,i] < outlier.iloc[:,i][0][0]:
           data_place.iloc[j,i] = outlier.iloc[:,i][0][0]
            
            
        elif data_place.iloc[j,i] > outlier.iloc[:,i][0][1]:
            data_place.iloc[j,i] = outlier.iloc[:,i][0][1]
            
            
        else:
            pass
        

data_place.to_excel('D:/multi_project_sample_data_/removed_outlier_data_by_2020_crime_per_density.xlsx', index = True)
