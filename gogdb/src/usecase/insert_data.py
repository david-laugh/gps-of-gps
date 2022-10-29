from multiprocessing import Pool
import multiprocessing as mp
import time
import os

import pandas as pd
import h3

from gogpy.validation.gog_data import gog_validation


PROCESS_TIME = time.strftime('%Y-%m-%d-%H-%M', time.localtime(time.time()))

def write_log(fname, id_str):
    with open(f"./Log_{PROCESS_TIME}.txt", "a") as file:
        file.write(f"{fname}\t{id_str}\n")

def write_table(fname, item):
    with open(f"./result/{fname}", "a") as file:
        txt = '\t'.join(item)
        file.write(f"{txt}\n")

def add_item(item):
    for tmp in ["user_lang", "device", "category name", "Timezone offset in minutes"]:
        if tmp not in item.keys():
            item[tmp] = None

    h3_code = h3.geo_to_h3(item["lat"], item["lon"], 5)
    item["h3_code"] = h3_code

    return item

def sort_item(item):
    return (
        str(item["id_str"]),
        str(item["user_id_str"]),
        str(item["user_lang"]),
        str(item["lat"]),
        str(item["lon"]),
        item["country_code"],
        item["cdate"],
        str(item["device"]),
        str(item["category name"]),
        str(item["Timezone offset in minutes"])
    )


DATA_DIR = "./datalake"
def execute(fname):
    print(fname)
    df = pd.read_csv(f"{DATA_DIR}/{fname}")
    items = df.to_dict('records')
    for item in items:
        if gog_validation(item):
            item = add_item(item)
            # print(item)
            write_table(item["h3_code"], sort_item(item))

        else:
            write_log(fname, item["id_str"])


if __name__ == "__main__":
    f_list = os.listdir(DATA_DIR)

    p = Pool(8)

    p.map(execute, f_list)

    p.close()
    p.join()
