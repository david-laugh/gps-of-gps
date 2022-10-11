import time
import random

import mariadb
import h3


"""
시간 측정
"""
def execute():
    conn = mariadb.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "YOUR PASSWORD"
    )
    cur = conn.cursor()

    count = 0
    times = []
    while count < 1000:
        x, y = random.random(), random.random()
        x = x * 360 - 180
        y = y * 180 - 90
        h3_code = h3.geo_to_h3(x, y, 5)
        h3_codes = h3.k_ring(h3_code, 3)

        tables = []
        start = time.time()
        for h3_code in h3_codes:
            try:
                cur.execute(
                    "SELECT * FROM sample.{};".format(h3_code)
                )
                table = cur.fetchall()
                tables.append(table)
            except:
                pass
        end = time.time() - start
        if tables:
            times.append(end)
            count += 1

    conn.close()
    print("최대 소요 시간 : {}".format(max(times)))
    print("최소 소요 시간 : {}".format(min(times)))
    print("평균 소요 시간 : {}".format(sum(times) / len(times)))
    print("전체 소요 시간 : {}".format(sum(times)))


if __name__=="__main__":
    execute()
