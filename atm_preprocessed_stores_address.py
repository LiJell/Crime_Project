# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 09:23:58 2022

@author: hanju
"""

import pandas as pd
atm_table = pd.read_excel('D:/multi_project_sample_data_/seoul_atm.xlsx')
atm_table.copy = atm_table
atm_table.copy[['stores', 'road_address']]
atm_list = atm_table.copy[['stores', 'road_address']]
atm_list
atm_list.info()
# 결측치 처리 ( 결측치들의 주소의 지역구는 같기 때문에 앞에 있는 값을 사용)
atm_list = atm_list.fillna(method = 'ffill')


atm_list
atm_list = atm_list[atm_list['road_address'].str.contains('서울')].reset_index(drop = True)
atm_list
atm_list.to_excel('D:\multi_project_sample_data_/atm_list.xlsx', index = False)
