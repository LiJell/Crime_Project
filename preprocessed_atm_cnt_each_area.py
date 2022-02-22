# -*- coding: utf-8 -*-
"""
Created on Tue Feb 22 16:59:56 2022

@author: hanju
"""

import pandas as pd 
import numpy as np

atm = pd.read_excel('C:/Users/hanju/Desktop/Adata/atm_list.xlsx')
atm
type(atm)



atm_list = atm_list[atm_list['road_address'].str.contains('서울')].reset_index(drop = True)


atm_data = atm[atm['road_address'].str.contains('강남구')]
강남 = atm_data.count('index')[0]
type(강남)


ads = ['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구']

atm_df = pd.DataFrame()

for ad in ads:
    place = atm[atm['road_address'].str.contains(ad)]
    cnt = place.count('index')[0]
    df = pd.DataFrame({ad:[cnt]})
    atm_df = pd.concat([atm_df, df], axis=1)
    

atm_df.rename(index = {0 : 'counts'}, inplace = True)
atm_df = atm_df.T
atm_df.to_excel('D:/multi_project_sample_data_/atm_each_area.xlsx', index = True)
