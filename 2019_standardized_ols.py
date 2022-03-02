# -*- coding: utf-8 -*-
"""
Created on Wed Mar  2 10:49:48 2022

@author: hanju
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 다중선형회귀 분석

df = pd.read_excel('C:/Users/hanju/Desktop/multicamp/project모음/data_2019_stand.xlsx')
df1 = df.drop(['자치구'], axis = 1)


# 속성(변수) 선택
X = df1.iloc[:, :-1].values
y = df1['범죄발생건수'].values

# train, test 데이터 split(7:3)
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 10)

from sklearn.linear_model import LinearRegression

lr = LinearRegression()
lr.fit(X_train, y_train)

r_square = lr.score(X_test, y_test)
print('R-square : ', r_square)

print('X 변수 기울기 : ', lr.coef_)

print('절편 : ', lr.intercept_)

y_hat = lr.predict(X_test)

plt.figure(figsize = (10, 5))
plt.plot(y_test, label = 'y_test')
plt.plot(y_hat, label = 'y_hat')
plt.legend()
plt.show()




# -----------------------------------------------------------------------------------------------------------------

df = pd.read_excel('C:/Users/hanju/Desktop/2019_minmax.xlsx')
df1 = df.copy()

df1 = df1.drop('자치구', axis = 1)
df1.columns
result_pvalue = sm.ols(formula = '범죄발생건수 ~ 경찰관서수 + 소방관서수 + 카페수 + 편의점수 + 공원수 + 버스정류장수 + 가로등수 + ATM수 + 반려동물가구비율 + 행복지수종합', data = df1).fit()
# result_predict = sm.ols(formula = '범죄발생건수 ~ 카페수 + 편의점수 + 공원수 +  ATM수', data = df1).fit()


print('절편과 기울기 : ', result_pvalue.params)
print('유의확률 : ', result_pvalue.pvalues)
print('결정계수 : ', result_pvalue.rsquared)
print('각 독립변수의 범죄발생건수 예측 : ', result_pvalue.predict())
print(result_pvalue.summary())

df1['각_독립변수의_십만명당_범죄발생건수_예측결과'] = result_pvalue.predict()
df1['자치구'] = df['자치구']
df1['실제_범죄발생건수'] = df['범죄발생건수']
df1['실제값_예측값_차이값'] = abs(df1['범죄발생건수'] - df1['각_독립변수의_십만명당_범죄발생건수_예측결과'])
df1['실제값_예측값_차이값'].sum()
df1.columns
df1 = df1[['자치구', '범죄발생건수', '경찰관서수', '소방관서수', '카페수', '편의점수',
       '공원수', '버스정류장수', '가로등수', 'ATM수', '반려동물가구비율',
       '행복지수종합', '각_독립변수의_십만명당_범죄발생건수_예측결과', '실제_범죄발생건수', '실제값_예측값_차이값']]

df1.to_excel('C:/Users/hanju/Desktop/multicamp/project모음/2019_ols_stand.xlsx', index = False)

#-----------------------------------------------------------------------------------------------------
from statsmodels.stats.outliers_influence import variance_inflation_factor
df = pd.read_excel('C:/Users/hanju/Desktop/2019_minmax.xlsx')
df1 = df.copy()
df2 = df1.drop(['자치구','범죄발생건수','ATM수','가로등수','경찰관서수','편의점수'], axis = 1)

vif = pd.DataFrame()
vif["VIF Factor"] = [variance_inflation_factor(df2.values, i) for i in range(df2.shape[1])]
vif["features"] = df2.columns
vif = vif.sort_values("VIF Factor").reset_index(drop=True)
vif
'''
   VIF Factor  features
0    3.159857  반려동물가구비율
1    3.605759    행복지수종합
2    5.046444    버스정류장수
3    6.303021       공원수
4    6.748478       카페수
5    8.391458     소방관서수
6   10.450230      편의점수
'''
df = pd.read_excel('C:/Users/hanju/Desktop/2019_minmax.xlsx')
df1 = df.copy()
df2 = df1.drop(['자치구','ATM수','가로등수','경찰관서수','편의점수'], axis = 1)

df2
result_pvalue = sm.ols(formula = '범죄발생건수 ~ 소방관서수 + 카페수 + 공원수 + 버스정류장수 + 반려동물가구비율 + 행복지수종합', data = df2).fit()
# result_predict = sm.ols(formula = '범죄발생건수 ~ 카페수 + 편의점수 + 공원수 +  ATM수', data = df1).fit()


print('절편과 기울기 : ', result_pvalue.params)
print('유의확률 : ', result_pvalue.pvalues)
print('결정계수 : ', result_pvalue.rsquared)
print('각 독립변수의 범죄발생건수 예측 : ', result_pvalue.predict())
print(result_pvalue.summary())


