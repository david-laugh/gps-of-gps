import math
from collections import Counter

import folium
import numpy as np
import pandas as pd


def myHaversine(sX, sY, tX, tY):
    radius = 6371
    radian = math.pi / 180

    deltaLat = abs(sX - tX) * radian
    deltaLon = abs(sY - tY) * radian

    sinDeltaLat = math.sin(deltaLat / 2)
    sinDeltaLon = math.sin(deltaLon / 2)

    distance = math.asin(math.sqrt(
        math.pow(sinDeltaLat, 2)
        + math.cos(sX * radian) * math.cos(tX * radian)
        * math.pow(sinDeltaLon, 2)
    )) * radius * 2

    return distance

def execute():
    df = pd.read_csv('./results.csv')
    print("df 행 수 : {}".format(len(df)))
    df = df.sample(frac=0.01)
    print(df.head())

    avg_lat = df['latitude'].mean()
    avg_lon = df['longitude'].mean()

    distance = []
    for n in df.index:
        d = myHaversine(avg_lat, avg_lon, df['latitude'][n], df['longitude'][n])
        distance.append(d*1000)

    final_degree = []
    for n in df.index:
        r = math.atan(
            (df['latitude'][n]-avg_lat) / (df['longitude'][n]-avg_lon)
        ) 
        degree = (r * 180) / math.pi

        if df['longitude'][n]>avg_lon:
            fd = 90 - degree
        else:
            fd = 270 - degree
        final_degree.append(fd)
 
    # 다트형 공간 분할.

    # sample
    # map = folium.Map(location=[avg_lat, avg_lon], zoom_start=16)
    # for n in df2.index:
    #     folium.CircleMarker(
    #         [df2['latitude'][n], df2['longitude'][n]],
    #         radius=(df2['count'][n])/20, 
    #         color='#990000',
    #         fill_color='#3186cc'
    #     ).add_to(map)
    # map.save("index3.html")



if __name__=="__main__":
    execute()
