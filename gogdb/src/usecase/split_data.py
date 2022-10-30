import os
import time
from multiprocessing import Pool
import multiprocessing as mp

import pandas as pd
import h3


DATA_DIR = "./datalake/gps"
RESULT_DIR = './datalake/result'
DB_NAME = "gogDB"
def execute(fname):
    print(fname)
    df = pd.read_csv(f'{DATA_DIR}/{fname}', encoding='utf-8')

    df['id_str'] = df['id_str'].astype(str)
    df['user_id_str'] = df['user_id_str'].astype(str)
    df['category_name'] = None
    df['Timezone_offset_in_minutes'] = None
    df['h3_code'] = df.apply(lambda r: h3.geo_to_h3(r.lat, r.lon, 5), axis=1)

    h3_codes = list(set(df['h3_code'].tolist()))
    # print(df.head())
    # print(f"H3 코드 길이 : {len(h3_codes)}")

    for h3_code in h3_codes:
        df_q = df[df.h3_code == h3_code]
        df_q = df_q[[
            'id_str',
            'user_id_str',
            'user_lang',
            'lat',
            'lon',
            'country_code',
            'cdate',
            'device',
            'category_name',
            'Timezone_offset_in_minutes'
        ]]
        with open(f"{RESULT_DIR}/{h3_code}", "a") as f:
            for values in df_q.values.tolist():
                f.write("{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\n".format(
                    values[0],values[1],values[2],values[3],values[4],
                    values[5],values[6],values[7],values[8],values[9]
                ))


if __name__ == "__main__":
    start = time.time()
    f_list = [fname for fname in os.listdir(DATA_DIR)[:10] if "art" in fname]

    p = Pool(4)
    p.map(execute, f_list)
    p.close()
    p.join()

    print(time.time() - start)
