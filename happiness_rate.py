import pandas as pd
import numpy as np
import csv
data = pd.read_csv('C:/Users/hanju/LiJell_Project/LiJell/2019_happiniess.csv', header = 1, sep = ',', encoding = 'cp949')
data
data = data[27:]
data.reset_index(drop = True, inplace = True)
happy = data[['분류','행복지수 종합']]
happy
happy.to_excel('C:/Users/hanju/LiJell_Project/LiJell/2019_happiniess_rate.xlsx', index = False)


data2 = pd.read_csv('C:/Users/hanju/LiJell_Project/LiJell/2020_happiness.csv', header = 1, sep = ',', encoding = 'cp949')
data2 = data2[27:]
data2.reset_index(drop = True, inplace = True)
happy2 = data2[['분류','행복지수 종합']]
happy2
happy2.to_excel('C:/Users/hanju/LiJell_Project/LiJell/2020_happiniess_rate.xlsx', index = False)
