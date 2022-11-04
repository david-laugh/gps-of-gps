import json
import os
import time

import mariadb
import pandas as pd
import h3


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
        cur, db_name, table_name, id_str,
        user_id_str, user_lang, lat, lon,
        country_code, cdate, device, category_name, 
        Timezone_offset_in_minutes
    ):
    """Adds the given contact to the contacts table"""

    cur.execute(
        "INSERT INTO {}.{}(id_str, user_id_str, user_lang, lat, lon," \
        "country_code, cdate, device, category_name, Timezone_offset_in_minutes)" \
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)".format(db_name, table_name),
        (
            id_str, user_id_str, user_lang, lat, lon, country_code, 
            cdate, device, category_name, Timezone_offset_in_minutes
        )
    )


DATA_DIR = "./datalake/gps"
ERROR_DIR = './datalake/error'
DB_NAME = "testdb"
def execute():
    conn = mariadb.connect(
        host = "127.0.0.1",
        port = 3306,
        user = "root",
        password = "YOUR PASSWORD"
    )
    cur = conn.cursor()

    create_database(cur, DB_NAME)
    
    f_list = [fname for fname in os.listdir(DATA_DIR) if "art" in fname]
    for fname in f_list:
        df = pd.read_csv(f'{DATA_DIR}/{fname}', encoding='utf-8')

        df['id_str'] = df['id_str'].astype(str)
        df['user_id_str'] = df['user_id_str'].astype(str)
        df['category_name'] = None
        df['Timezone_offset_in_minutes'] = None
        df['h3_code'] = df.apply(lambda r: h3.geo_to_h3(r.lat, r.lon, 5), axis=1)

        h3_codes = list(set(df['h3_code'].tolist()))
        # print(df.head())
        print(f"H3 코드 길이 : {len(h3_codes)}")

        start = time.time()
        # print(df_q.head())
        df.apply(lambda r: create_table(cur, DB_NAME, r.h3_code), axis=1)
        print(f"process1 실행 시간 : {time.time() - start}")

        df.apply(lambda r: insert_into_table(
            cur, DB_NAME, r.h3_code, r.id_str,
            r.user_id_str, r.user_lang, r.lat, r.lon,
            r.country_code, r.cdate, r.device, r.category_name, 
            r.Timezone_offset_in_minutes
        ), axis=1)
        print(f"process2 실행 시간 : {time.time() - start}")

    conn.close()


if __name__ == "__main__":
    execute()
