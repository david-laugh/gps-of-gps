import os
from tqdm import tqdm

import h3

from gogpy.data.raw import Raw


def execute():
    dir_name = "./examples/data/"
    os.makedirs("datalake", exist_ok=True)

    for filename in os.listdir(dir_name):
        with open(dir_name + "/" + filename, "r") as f:
            for i, line in tqdm(enumerate(f.readlines())):
                if i == 0:
                    pass
                else:
                    raw = Raw(line)
                    h3_cell = h3.geo_to_h3(
                        raw.lat, raw.lon, 6
                    )
                    with open("datalake"+"/"+h3_cell, "a") as f:
                        f.write("{},{}\n".format(
                            raw.lat, raw.lon
                        ))


if __name__ == "__main__":
    execute()
