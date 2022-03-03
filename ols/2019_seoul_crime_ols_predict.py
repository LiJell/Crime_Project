# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 13:50:34 2022

@author: tnals
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 다중선형회귀 분석

df_1 = pd.read_excel('../data/data_total_2019.xlsx')
df1 = df.drop(['기간', '자치구'], axis = 1)
df1 = df[['인구 수(명)', '면적', '경찰관서 수', '소방관서 수', '카페 수', '편의점 수', '공원 수',
       '버스정류장 수', '가로등 수', 'ATM 수', '반려동물 가구 비율(%, 인구 수)', '행복지수 종합', '범죄발생건수']]

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

# ols
import statsmodels.formula.api as sm

df1.columns = ['인구수', '면적', '경찰관서수', '소방관서수', '카페수', '편의점수', '공원수', '버스정류장수', '가로등수', 'ATM수', '반려동물가구비율', '행복지수종합', '범죄발생건수']
result = sm.ols(formula = '범죄발생건수 ~ 인구수 + 면적 + 경찰관서수 + 소방관서수 + 카페수 + 편의점수 + 공원수 + 버스정류장수 + 가로등수 + ATM수 + 반려동물가구비율 + 행복지수종합', data = df1).fit()

print('절편과 기울기 : ', result.params)
print('유의확률 : ', result.pvalues)
print('결정계수 : ', result.rsquared)
print('각 독립변수의 범죄발생건수 예측 : ', result.predict())
result.summary()

df1['각_독립변수의_범죄발생건수_예측결과'] = result.predict()
df1['자치구'] = df['자치구']
df1['실제_범죄발생건수'] = df['범죄발생건수']
df1.columns
df1 = df1[['자치구', '인구수', '면적', '경찰관서수', '소방관서수', '카페수', '편의점수', '공원수', '버스정류장수', '가로등수',
       'ATM수', '반려동물가구비율', '행복지수종합', '범죄발생건수', '각_독립변수의_범죄발생건수_예측결과', '실제_범죄발생건수']]

df1.to_excel('../data/2019_seoul_crime_ols_predict.xlsx', index = False)


# -----------------------------------------------------------------------------------------------------------------

df = pd.read_excel('../data/data_preprocess(20220227_202609)_edit.xlsx')
df1 = df.copy()

df1 = df1.drop('자치구', axis = 1)
df1.columns
result_pvalue = sm.ols(formula = '십만명당_범죄발생건수 ~ 면적당_경찰관서_수 + 면적당_소방관서_수 + 면적당_카페_수 + 면적당_편의점_수 + 면적당_공원_수 + 면적당_버스정류장_수 + 면적당_가로등_수 + 면적당_ATM_수 + 인구당_반려동물수 + 행복지수', data = df1).fit()
result_predict = sm.ols(formula = '십만명당_범죄발생건수 ~ 면적당_카페_수 + 면적당_편의점_수 + 면적당_공원_수 +  면적당_ATM_수', data = df1).fit()


print('절편과 기울기 : ', result_predict.params)
print('유의확률 : ', result_predict.pvalues)
print('결정계수 : ', result_predict.rsquared)
print('각 독립변수의 범죄발생건수 예측 : ', result_predict.predict())
result_predict.summary()

df1['각_독립변수의_십만명당_범죄발생건수_예측결과'] = result_predict.predict()
df1['자치구'] = df['자치구']
df1['실제_범죄발생건수'] = df_1['범죄발생건수']
df1['실제값_예측값_차이값'] = abs(df1['십만명당_범죄발생건수'] - df1['각_독립변수의_십만명당_범죄발생건수_예측결과'])
df1['실제값_예측값_차이값'].sum()
df1.columns
df1 = df1[['자치구', '십만명당_범죄발생건수', '면적당_경찰관서_수', '면적당_소방관서_수', '면적당_카페_수', '면적당_편의점_수',
       '면적당_공원_수', '면적당_버스정류장_수', '면적당_가로등_수', '면적당_ATM_수', '인구당_반려동물수',
       '행복지수', '각_독립변수의_십만명당_범죄발생건수_예측결과', '실제_범죄발생건수', '실제값_예측값_차이값']]

df1.to_excel('../data/2019_seoul_ols_predict_2.xlsx', index = False)

# -----------------------------------------------------------------------------------------------------------------------
# 중구, 종로구 제거

df = pd.read_excel('../data/data_preprocess(20220227_202609)_edit.xlsx')
df1 = df.copy()

# df1 = df1.drop('자치구', axis = 1)
df1 = df1.drop(index =[22, 23])
df1.columns

result_predict = sm.ols(formula = '십만명당_범죄발생건수 ~ 면적당_카페_수 + 면적당_편의점_수 + 면적당_공원_수 +  면적당_ATM_수', data = df1).fit()

print('절편과 기울기 : ', result_predict.params)
print('유의확률 : ', result_predict.pvalues)
print('결정계수 : ', result_predict.rsquared)
print('각 독립변수의 범죄발생건수 예측 : ', result_predict.predict())
result_predict.summary()

df1['각_독립변수의_십만명당_범죄발생건수_예측결과'] = result_predict.predict()
df1['자치구'] = df['자치구']
df1['실제_범죄발생건수'] = df_1['범죄발생건수']
df1['실제값_예측값_차이값'] = abs(df1['십만명당_범죄발생건수'] - df1['각_독립변수의_십만명당_범죄발생건수_예측결과'])
df1['실제값_예측값_차이값'].sum()
df1.columns

df1 = df1[['자치구', '십만명당_범죄발생건수', '면적당_경찰관서_수', '면적당_소방관서_수', '면적당_카페_수', '면적당_편의점_수',
       '면적당_공원_수', '면적당_버스정류장_수', '면적당_가로등_수', '면적당_ATM_수', '인구당_반려동물수',
       '행복지수', '각_독립변수의_십만명당_범죄발생건수_예측결과', '실제_범죄발생건수', '실제값_예측값_차이값']]

df1.to_excel('../data/2019_seoul_ols_predict_2.xlsx', index = False)
