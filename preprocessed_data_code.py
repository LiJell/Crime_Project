# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 15:47:51 2022

@author: tnals
"""

import pandas as pd
import numpy as np


# 서울 구별 신호등
seoul_cafe = pd.read_csv('../data/서울시 횡단보도 통계_(2014_2017).txt', header = 1, sep = '\t', engine = 'python')
seoul_cafe_copy = seoul_cafe.copy()
seoul_cafe_copy.info()

seoul_cafe_copy = seoul_cafe[seoul_cafe['기간'] == 2017]
seoul_cafe_copy = seoul_cafe_copy.drop(seoul_cafe_copy.columns[3:], axis = 1).reset_index(drop = True)
seoul_cafe_copy.to_excel('../data/traffic_light_count.xlsx', index = False)


# ---------------------------------------------------------------------------------------------------------------------------------------

# 서울 구별 인구수
seoul_population = pd.read_csv('../data/서울시 주민등록인구 (연령별, 구별) 통계_(2014_2021).txt', sep = '\t', engine = 'python')
seoul_population.info()

var_list = ['기간', '행정구역별', '구분', '계']
sl_pop_cp = seoul_population[var_list]
sl_pop_cp.info()
sl_pop_cp = sl_pop_cp[sl_pop_cp['기간'] == 2019]
sl_pop_cp = sl_pop_cp.drop_duplicates('행정구역별')
sl_pop_cp.to_excel('../data/seoul_population_count_2019.xlsx', index = False)


# ---------------------------------------------------------------------------------------------------------------------------------------


# 서울 세대원수
df = pd.read_csv('../data/서울시 세대원수별 세대수(구별) 통계_(2014_2021).txt', sep = '\t', engine = 'python')
df.info()

df_copy = df.copy()
df_copy = df[df['기간'] == 2020]
df_copy
df_copy.to_excel('../data/number_of_household_members_count_2020.xlsx', index = False)



# ---------------------------------------------------------------------------------------------------------------------------------------


# (2) 결측값을 앞 방향 혹은 뒷 방향으로 채우기 (fill gaps forward or backward)

# : fillna(method='ffill' or 'pad'), fillna(method='bfill' or 'backfill')
# 출처: https://rfriend.tistory.com/262 [R, Python 분석과 프로그래밍의 친구 (by R Friend)]

df = pd.read_csv('./서울시 공원 통계2019.txt', header = 2, sep = '\t')
df = df[['기간', '자치구', '공원수']]
df.info()
df['공원수'] = df.loc[:, '공원수'].str.replace(',', '').astype('int64')
df.drop(26)
