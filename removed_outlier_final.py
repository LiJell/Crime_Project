# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 11:35:45 2022

@author: hanju
"""
import pandas as pd
import seaborn as sns
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib.patheffects as path_effects

plt.rc('font', family = "Malgun Gothic")
plt.rcParams['axes.unicode_minus'] = False


# 2020 remove outlier
data = pd.read_excel('D:/multi_project_sample_data_/2020_per_variable_finall.xlsx')
data
data_a = data[data.columns.difference(['자치구'])]

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
    name_column = i + 'no outlier'
    outlier[name_column] = [[lower_outlier,upper_outlier]]
   

outlier.to_excel('D:/multi_project_sample_data_/2020_IQR.xlsx', index = False)

   # 이상치 대치
   
   

jachigu = data['자치구']

outlier.columns
outlier.iloc[:,0][0][0]
copy_1 = data_place.iloc[1,0].copy()
copy_1.replace(copy_1, outlier.loc[outlier[i][0]])
data_a

####################


for i in range(len(data_columns)):
    for j in range(len(data_a)):
        if data_a.iloc[j,i] < outlier.iloc[:,i][0][0]:
           data_a.iloc[j,i] = outlier.iloc[:,i][0][0]
            
            
        elif data_a.iloc[j,i] > outlier.iloc[:,i][0][1]:
            data_a.iloc[j,i] = outlier.iloc[:,i][0][1]
            
            
        else:
            pass
        
total_final = pd.concat([jachigu ,data_a], axis=1)
total_final.to_excel('D:/multi_project_sample_data_/2020_no_outlier.xlsx', index = False)

## 2019

data = pd.read_excel('D:/multi_project_sample_data_/2019_per_variable_finall.xlsx')
data
data_a = data[data.columns.difference(['자치구'])]

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
    name_column = i + 'no outlier'
    outlier[name_column] = [[lower_outlier,upper_outlier]]
   

outlier.to_excel('D:/multi_project_sample_data_/2019_IQR.xlsx', index = False)

   # 이상치 대치
   
   

jachigu = data['자치구']

outlier.columns
outlier.iloc[:,0][0][0]
copy_1 = data_place.iloc[1,0].copy()
copy_1.replace(copy_1, outlier.loc[outlier[i][0]])
data_a

####################


for i in range(len(data_columns)):
    for j in range(len(data_a)):
        if data_a.iloc[j,i] < outlier.iloc[:,i][0][0]:
           data_a.iloc[j,i] = outlier.iloc[:,i][0][0]
            
            
        elif data_a.iloc[j,i] > outlier.iloc[:,i][0][1]:
            data_a.iloc[j,i] = outlier.iloc[:,i][0][1]
            
            
        else:
            pass
        
total_final = pd.concat([jachigu ,data_a], axis=1)
total_final.to_excel('D:/multi_project_sample_data_/2019_no_outlier.xlsx', index = False)  
