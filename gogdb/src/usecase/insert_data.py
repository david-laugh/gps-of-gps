from multiprocessing import Pool
import multiprocessing as mp
import time
import os

import pandas as pd
import h3
import mariadb

from gogpy.validation.gog_data import gog_validation


PROCESS_TIME = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))

def write_log(fname, id_strs):
    with open(f"./Log_{PROCESS_TIME}.txt", "a") as file:
        for id_str in id_strs:
            file.write(f"{fname}\t{id_str}\n")

def write_table(fname, item):
    with open(f"./datalake/result/{fname}", "a") as file:
        txt = "\t".join(str(tmp) for tmp in item)
        file.write(f"{txt}\n")

def add_item(item):
    for tmp in ["user_lang", "device", "category name", "Timezone offset in minutes"]:
        if tmp not in item.keys():
            item[tmp] = None

    return item

def sort_item(item):
    return (
        item["id_str"],
        item["user_id_str"],
        item["user_lang"],
        item["lat"],
        item["lon"],
        item["country_code"],
        item["cdate"],
        item["device"],
        item["category name"],
        item["Timezone offset in minutes"]
    )

def create_database(cur, db_name):
    cur.execute(
        "CREATE DATABASE IF NOT EXISTS {};".format(db_name)
    )

def create_table(cur, db_name, table_name):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS {}.{} (" \
            "id_str VARCHAR(25) NOT NULL," \
            "user_id_str VARCHAR(25) NOT NULL," \
            "user_lang VARCHAR(7)," \
            "lat FLOAT NOT NULL," \
            "lon FLOAT NOT NULL," \
            "country_code VARCHAR(2) NOT NULL," \
            "cdate DATETIME NOT NULL," \
            "device VARCHAR(25)," \
            "category_name VARCHAR(50)," \
            "Timezone_offset_in_minutes INTEGER" \
        ") ENGINE=InnoDB;".format(db_name, table_name)
    )

def insert_into_table(
        cur, db_name, table_name, items
    ):
    """Adds the given contact to the contacts table"""

    cur.execute(
        "INSERT INTO {}.{}(id_str, user_id_str, user_lang, lat, lon," \
        "country_code, cdate, device, category_name, Timezone_offset_in_minutes)" \
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(db_name, table_name),
        items
    )


DATA_DIR = "./datalake/gps"
RESULT_DIR = "./datalake/result"
def execute(item):
    item = add_item(item)
    # print(item)
    if item["user_lang"] != None and len(item["user_lang"]) > 8:
        print(item["user_lang"])
    else:
        h3_code = h3.geo_to_h3(item["lat"], item["lon"], 5)
        # print(item)
        # write_table(h3_code, sort_item(item))
    # else:
    #     write_log(fname, item["id_str"])

conn = mariadb.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "YOUR PASSWORD"
    )
cur = conn.cursor()

def execute_insert_data(fname):

    tmp = []
    with open(f"{RESULT_DIR}/{fname}", "r") as file:
        for line in file.readlines():
            items = line[:-1].split('\t')
            items[3] = float(items[3])
            items[4] = float(items[4])
            if items[2] == 'None':
                items[2] = None
            if items[8] == 'None':
                items[8] = None
            if items[9] != 'None':
                items[9] = int(items[9])
            else:
                items[9] = None
            tmp.append(items)
    insert_into_table(cur, "gogDB", fname, tmp)


if __name__ == "__main__":
    # f_list = os.listdir(DATA_DIR)
    start = time.time()

    # process 1
    # df = pd.read_csv(f"{DATA_DIR}/{f_list[0]}")
    # items = df.to_dict('records')

    # p = Pool(4)

    # ret = p.map(execute, items)

    # p.close()
    # p.join()

    # # write_log(f_list[0], ERROR)
    # print(time.time() - start)

    # process 2
    create_database(cur, "gogDB")
    f_list = os.listdir(RESULT_DIR)
    for fname in f_list:
        create_table(cur, "gogDB", fname)

    p = Pool(4)
    p.map(execute_insert_data, f_list)

    p.close()
    p.join()

    print(time.time() - start)

    conn.close()
