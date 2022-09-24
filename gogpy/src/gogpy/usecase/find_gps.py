import os
import random
import math
import time

# haversine 모듈은 비사용.
from haversine import haversine
import h3

from gogpy.data.raw import Raw

# 피타고라스 정리를 활용하여
# 주변 n km 좌표를 구함.
def pythagoras(origin: tuple, target: tuple, r: float) -> bool:
    if r**2 > (target[0] - origin[0])**2 + (target[1] - origin[1])**2:
        return True
    else:
        return False

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

# dev
def find_gps(k, n_km):
    start = time.time()

    # 0-1. 랜덤한 파일 하나 선정.
    table_dir_path = "./datalake/table/"
    source_fname = random.choice(os.listdir(table_dir_path))
    print("랜덤 선정 Source Table 명 : {}".format(source_fname))

    target_fname = random.choice(os.listdir(table_dir_path))
    print("랜덤 선정 Table test 명 : {}".format(target_fname))

    # 0-2. 파일 내 좌표 중 하나를 랜덤하게 선정.
    with open(table_dir_path + source_fname, "r") as f:
        line = random.choice(f.readlines())
        source_raw = Raw(line)
    print("\n랜덤한 Source 좌표 : {} {}".format(source_raw.lat, source_raw.lon))

    with open(table_dir_path + target_fname, "r") as f:
        line = random.choice(f.readlines())
        target_raw = Raw(line)
    print("랜덤한 Target 좌표 : {} {}".format(target_raw.lat, target_raw.lon))

    # Haversine Distance 계산
    # Haversine Distance 모듈과 비교
    distance = myHaversine(
        source_raw.lat,
        source_raw.lon,
        target_raw.lat,
        target_raw.lon
    )
    print("\nMy Distance : {}".format(distance))
    m_distance = haversine(
        (source_raw.lat, source_raw.lon),
        (target_raw.lat, target_raw.lon),
        unit="km"
    )
    print("Module Distance : {}".format(m_distance))
    print("My Func VS Modlue Func : {}".format(abs(distance - m_distance)))

    # source h3와 이웃한 주변 h3 구하기.
    neighbors = h3.k_ring(source_fname, k)
    print("\nneighbor의 개수 : {}".format(len(neighbors)))
    # print("{}과 이웃한 좌표 : {}".format(source_fname, neighbors))
    for neighbor in neighbors:
        print("{}, {} is neighbor : {}".format(
            source_fname,
            neighbor,
            h3.h3_indexes_are_neighbors(source_fname, neighbor)
        ))

    # source h3와 이웃한 주변 h3 구하기.
    print("\n")
    tXYs = []
    for neighbor in neighbors:
        try:
            with open(table_dir_path + neighbor, "r") as f:
                for line in f.readlines():
                    target_raw = Raw(line)
                    # 거리가 20km 이내인 좌표만 tXYs에 추가.
                    if myHaversine(
                        source_raw.lat, source_raw.lon,
                        target_raw.lat, target_raw.lon) < n_km:
                        tXYs.append((target_raw.lat, target_raw.lon))
        except FileNotFoundError:
            print("{} is not found.".format(neighbor))
    # tXYs의 개수 구하기.
    print("\ntXYs Counts : {}".format(len(tXYs)))

    print("\n================= execute 시간 계산 ==================\n{}\n" \
        .format(time.time() - start))

def execute():
    find_gps(1, 10)
    find_gps(2, 20)
    find_gps(3, 30)

if __name__=="__main__":
    execute()
