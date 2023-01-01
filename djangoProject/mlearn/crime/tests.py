'''
미국 주가 콜롬비아, 푸에르토-리코(준주) 포함시
콜롬비아('id': '11'-> 인덱스 8),
푸에르토리코('id': '72' -> 인덱스 51)는 준주라서 제거해야함
'''
import os.path
from dataclasses import dataclass

import googlemaps
import numpy as np
import pandas as pd
from sklearn import preprocessing
import folium

from basic.mlearn.crime.services import CrimeService


@dataclass
class MyChoroplethVO:
    geo_data = "",
    data = object,
    name = "",
    columns = [],
    key_on = "",
    fill_color = "",
    fill_opacity = 0.0,
    line_opacity = 0.0,
    legend_name = "",
    bins = None,
    location = [],
    zoom_start = 0,
    save_path = ''

def MyChoroplethService(vo):
    map = folium.Map(location=vo.location, zoom_start=vo.zoom_start)
    folium.Choropleth(
        geo_data=vo.geo_data,
        data=vo.data,
        name=vo.name,
        columns=vo.columns,
        key_on=vo.key_on,
        fill_color=vo.fill_color,
        fill_opacity=vo.fill_opacity,
        line_opacity=vo.line_opacity,
        legend_name=vo.legend_name
    ).add_to(map)
    map.save(vo.save_path)

def set_json_from_df(fname):
    df = pd.read_json(fname)
    df.drop(df.index[[8,51]], inplace=True)
    data = os.path.join(os.getcwd(), "data")
    df.to_json(os.path.join(data, "us-states.json"), orient='index')
if __name__ == '__main__':
    crime_menu = ["Exit",  # 0
                  "Show Spec",  # 1
                  "Save Police Position",  # 2.
                  "Save CCTV Population",  # 3
                  "Save Police Normalization",  # 4
                  "Save US Unemployment Map",  # 5
                  "Save Seoul Crime Map",  # 6
                  ]
    crime_lambda = {
        "1": lambda x: x.show_spec(),
        "2": lambda x: x.save_police_pos(),
        "3": lambda x: x.save_cctv_pop(),
        "4": lambda x: x.save_police_norm(),
        "5": lambda x: x.save_us_unemployment_map(),
        "6": lambda x: x.save_seoul_crime_map(),
    }
    crime = CrimeService()
    while True:
        [print(f"{i}. {j}") for i, j in enumerate(crime_menu)]
        menu = input('메뉴선택: ')
        if menu == '0':
            print("종료")
            break
        else:
            try:
                crime_lambda[menu](crime)
            except KeyError as e:
                if 'some error message' in str(e):
                    print('Caught error message')
                else:
                    print("Didn't catch error message")