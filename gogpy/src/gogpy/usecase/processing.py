import os
from tqdm import tqdm

import h3


if __name__ == "__main__":
    dir_name = "./art3_USA_CA"
    os.makedirs("datalake", exist_ok=True)
    for filename in os.listdir(dir_name):
        with open(dir_name + "/" + filename, "r") as f:
            for i, line in tqdm(enumerate(f.readlines())):
                if i == 0:
                    pass
                else:
                    h3_cell = h3.geo_to_h3(
                        float(line.split(",")[2]), float(line.split(",")[3]), 6
                    )
                    with open("datalake"+"/"+h3_cell, "a") as f:
                        f.write("{},{}\n".format(
                            float(line.split(",")[2]), float(line.split(",")[3])
                        ))
