import os
import sys
import time

import mariadb
import h3

from gogpy.data.raw import Raw


"""
Refer to
https://mariadb.com/docs/connect/programming-languages/python/
"""
# Adds single contact
def add_contact(
        cur, db_name, table_name,
        id_str, user_id_str, user_lang,
        lat, lon, country_code, cdate, device
    ):
    """Adds the given contact to the contacts table"""

    cur.execute(
        "INSERT INTO {}.{}(id_str, user_id_str, user_lang," \
        "lat, lon, country_code, cdate, device)" \
        "VALUES (?, ?, ?, ?, ?, ?, ?, ?)".format(db_name, table_name),
        (id_str, user_id_str, user_lang,
        lat, lon, country_code, cdate, device)
    )

def create_database(cur, db_name):
    cur.execute(
        "CREATE DATABASE IF NOT EXISTS {};".format(db_name)
    )

def create_table(cur, db_name, table_name):
    cur.execute(
        "CREATE TABLE IF NOT EXISTS {}.{} (" \
            "id_str VARCHAR(25)," \
            "user_id_str VARCHAR(25)," \
            "user_lang VARCHAR(7)," \
            "lat FLOAT," \
            "lon FLOAT," \
            "country_code VARCHAR(2)," \
            "cdate DATETIME," \
            "device VARCHAR(25)" \
        ") ENGINE=InnoDB;".format(db_name, table_name)
    )

def execute():
    start = time.time()

    try:
        conn = mariadb.connect(
            host = "127.0.0.1",
            port = 3306,
            user = "root",
            password = "YOUR PASSWORD"
        )

        # Instantiate Cursor
        cur = conn.cursor()

        create_database(cur, "sample")

        for fname in os.listdir('YOUR DIR')[1:10]:
            with open("YOUR DIR" + fname, "r", encoding="UTF-8") as f:
                for line in f.readlines()[1:]:
                    source_raw = Raw(line)
                    h3_code = h3.geo_to_h3(source_raw.lat, source_raw.lon, 5)

                    create_table(cur, "sample", h3_code)
                    try:
                        add_contact(
                            cur, "sample", h3_code,
                            source_raw.id,
                            source_raw.user_id_str,
                            source_raw.user_lang,
                            source_raw.lat,
                            source_raw.lon,
                            source_raw.country_code,
                            source_raw.cdate,
                            source_raw.device
                        )
                    except:
                        pass
            # Close Connection

            print("소요 시간 : {}".format(time.time() - start))

        conn.close()
    except mariadb.Error as e:
        print(f"Error connecting to the database: {e}")
        sys.exit(1)


if __name__=="__main__":
    execute()
