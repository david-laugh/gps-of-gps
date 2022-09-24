import os
from tqdm import tqdm

import h3

from gogpy.data.raw import Raw


def execute():
    raw_dir_path = "./datalake/raw/"
    table_dir_name = "./datalake/table/"
    # os.makedirs("datalake", exist_ok=True)

    for filename in os.listdir(raw_dir_path):
        with open(raw_dir_path + filename, "r") as f:
            for i, line in tqdm(enumerate(f.readlines())):
                if i == 0:
                    pass
                else:
                    raw = Raw(line)
                    h3_cell = h3.geo_to_h3(
                        raw.lat, raw.lon, 5
                    )
                    with open(table_dir_name + h3_cell, "a") as f:
                        f.write("{},{},{},{},{},{},{},{}\n".format(
                            raw.id,
                            raw.user_id_str,
                            raw.user_lang,
                            raw.lat,
                            raw.lon,
                            raw.country_code,
                            raw.cdate,
                            raw.device
                        ))


if __name__ == "__main__":
    execute()
