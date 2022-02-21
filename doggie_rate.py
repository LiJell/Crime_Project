# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 17:41:32 2022

@author: hanju
"""
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# 2019
dogs = pd.read_csv('D:/multi_project_sample_data_/pet.csv', header = 1, sep = ',', encoding = 'utf-8')
dogs
condition = dogs['기간'] == 2019
dogs_19 = dogs[condition]
dogs_19
condition2 = dogs['대분류'].isin(['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구'])
dogs_19_location = dogs_19[condition2]
dogs_19_location
dogs_2019 = dogs_19_location[['기간','대분류','있다']]
dogs_2019.reset_index(inplace = True, drop = True)
dogs_2019
dogs_2019.to_excel('D:/multi_project_sample_data_/2019_pet.xlsx', index = False)

# 2020
condition_20 = dogs['기간'] == 2020
dogs_20 = dogs[condition_20]
dogs_20
condition2_20 = dogs['대분류'].isin(['강남구','강동구','강북구','강서구','관악구','광진구','구로구','금천구','노원구','도봉구','동대문구','동작구','마포구','서대문구','서초구','성동구','성북구','송파구','양천구','영등포구','용산구','은평구','종로구','중구','중랑구'])
dogs_20_location = dogs_20[condition2_20]
dogs_20_location 
dogs_2020 = dogs_20_location[['기간','대분류','있다']]
dogs_2020.reset_index(inplace = True, drop = True)

dogs_2020
dogs_2020.to_excel('D:/multi_project_sample_data_/2020_pet.xlsx', index = False)

plt.title('2019 dogs rate')
plt.xlabel('own')
plt.ylabel('percentages')
plt.rc('font', family = "Malgun Gothic")
plt.rcParams['axes.unicode_minus'] = False
dogs_2019.boxplot(column=['있다'], notch=True)


