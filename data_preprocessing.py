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
