# -*- coding: utf-8 -*-
"""
Created on Sun Feb 27 23:11:40 2022

@author: hanju
"""
import numpy as np
import pandas as pd
import math
import folium
import json


data_2020 = pd.read_excel('./2020_minmax.xlsx')

for i in range(len(data_2020)-1):
    try:
        json_file = '../crawling/datasalon-master/02_data_class/6_Starbucks_Location/maps/seoul_sgg.geojson'
        seoul_geo = json.load(open(json_file, encoding = 'utf-8'))
        seoul_map = folium.Map(location = [37.573050, 126.979189],
                               tiles = 'CartoDB positron',
                               zoom_start = 11)
        
        folium.Choropleth(seoul_geo,
                         data = data_2020,
                         columns = ['자치구', data_2020.columns[i+1]],
                         key_on = 'properties.SIG_KOR_NM',
                         fill_color = 'YlOrRd',
                         fill_opacity = 0.5,
                         line_opacity = 0.7).add_to(seoul_map)
        file_name = '2020_' + data_2020.columns[i+1]
        path = './'+ file_name + '.html'
        seoul_map.save(path, index = False)
    
    except:
        break
