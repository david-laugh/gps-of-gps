import time
import sys
import os

import pandas as pd
import mariadb
import h3

from gogpy.validation.gog_data import gog_validation


PROCESS_TIME = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))

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
            "device VARCHAR(25)" \
            "category_name VARCHAR(50)" \
            "Timezone_offset_in_minutes INT" \
        ") ENGINE=InnoDB;".format(db_name, table_name)
    )

def write_log(fname, id_str):
    with open(f"./Log_{PROCESS_TIME}.txt", "a") as file:
        file.write(f"{fname}\t{id_str}\n")

def write_table(fname, item):
    with open(f"./result/{fname}", "a") as file:
        file.write(f"{'\t'.join(item)}\n")

def add_item(item):
    for tmp in ["user_lang", "device", "category name", "Timezone offset in minutes"]:
        if tmp not in item.keys():
            item[tmp] = None

    h3_code = h3.geo_to_h3(item["lat"], item["lon"], 5)
    item["h3_code"] = h3_code

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


DATA_DIR = "./datalake"
DB_NAME = "gogDB"
def execute():
    start = time.time()

    try:
        # conn = mariadb.connect(
        #     host = "127.0.0.1",
        #     port = 3306,
        #     user = "root",
        #     password = "YOUR PASSWORD"
        # )

        # # Instantiate Cursor
        # cur = conn.cursor()

        # create_database(cur, DB_NAME)

        ### Process
        for fname in os.listdir(DATA_DIR):
            print(fname)
            # tmp = {}

            df = pd.read_csv(f"{DATA_DIR}/{fname}")
            items = df.to_dict('records')
            for item in items:
                if gog_validation(item):
                    item = add_item(item)
                    # print(item["h3_code"])
                    write_table(item["h3_code"], item)
                    # if item["h3_code"] not in tmp.keys():
                    #     tmp[item["h3_code"]] = [sort_item(item)]
                    # else:
                    #     tmp[item["h3_code"]].append(sort_item(item))

                else:
                    write_log(fname, item["id_str"])

            print(time.time() - start)

            # for key, value in tmp.items():
            #     # create_table(cur, DB_NAME, key)
            #     # insert_into_table(cur, DB_NAME, key, value)
            #     print(key)
            #     print(value)


        # conn.close()
    except mariadb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)

if __name__=="__main__":
    execute()
