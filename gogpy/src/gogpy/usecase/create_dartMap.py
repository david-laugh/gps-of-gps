import math
from collections import Counter

import folium
import numpy as np
import pandas as pd

from gogpy.usecase.find_gps import find_gps


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

def azimuth(sX, sY, tX, tY):
    """
    https://www.movable-type.co.uk/scripts/latlong.html
    """
    y = math.sin((tY * math.pi / 180) - (sY * math.pi / 180)) * math.cos(tX * math.pi / 180)
    x = math.cos(sX * math.pi / 180) \
        * math.sin(tX * math.pi / 180) \
        - math.sin(sX * math.pi / 180) \
        * math.cos(tX * math.pi / 180) \
        * math.cos(tY * math.pi / 180 - sY * math.pi / 180)
    a = math.atan2(y, x)
    bearing = (a * 180 / math.pi + 360) % 360

    return bearing


def execute():
    slat, slon, tXYs = find_gps(6, 100)
    # for i in range(1, 4):
    #     print("{} {}에서 {} {} : 방위각 {}" \
    #         .format(
    #             slat, slon, tXYs[i][0], tXYs[i][1],
    #             azimuth(slat, slon, tXYs[i][0], tXYs[i][1])
    #         )
    #     )

    map = folium.Map(location=[slat, slon], zoom_start=9)

    tooltip = "Source Lat, Lon"
    folium.Marker(
        [slat, slon],
        popup="{} {}".format(slat, slon),
        tooltip=tooltip
    ).add_to(map)

    for tXY in tXYs:
        angle = azimuth(slat, slon, tXY[0], tXY[1])
        distance = myHaversine(slat, slon, tXY[0], tXY[1])
        if 0 < angle and angle <= 90:
            if 0 <= distance and angle < 20:
                folium.CircleMarker(
                    [tXY[0], tXY[1]], radius=0.1, 
                    color='#D2B4DE', fill_color='#D2B4DE'
                ).add_to(map)
            if 20 <= distance and angle < 40:
                folium.CircleMarker(
                    [tXY[0], tXY[1]], radius=0.1, 
                    color='#A569BD', fill_color='#A569BD'
                ).add_to(map)
            if 40 <= distance and angle < 60:
                folium.CircleMarker(
                    [tXY[0], tXY[1]], radius=0.1, 
                    color='#7D3C98', fill_color='#7D3C98'
                ).add_to(map)
            if 60 <= distance and angle < 80:
                folium.CircleMarker(
                    [tXY[0], tXY[1]], radius=0.1, 
                    color='#6C3483', fill_color='#6C3483'
                ).add_to(map)
            if 80 <= distance and angle < 100:
                folium.CircleMarker(
                    [tXY[0], tXY[1]], radius=0.1, 
                    color='#4A235A', fill_color='#4A235A'
                ).add_to(map)
        elif 90 < angle and angle <= 180:
            folium.CircleMarker(
                [tXY[0], tXY[1]], radius=0.1, 
                color='#6495ED', fill_color='#6495ED'
            ).add_to(map)
        elif 180 < angle and angle <= 270:
            folium.CircleMarker(
                [tXY[0], tXY[1]], radius=0.1, 
                color='#FF0000', fill_color='#FF0000'
            ).add_to(map)
        else:
            folium.CircleMarker(
                [tXY[0], tXY[1]], radius=0.1, 
                color='#6495ED', fill_color='#6495ED'
            ).add_to(map)

    map.save("./examples/dart.html")


if __name__=="__main__":
    execute()
