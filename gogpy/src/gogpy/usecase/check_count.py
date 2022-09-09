import os


if __name__ == "__main__":
    dir_name = "./art3_USA_CA"

    count_a = 0
    for filename in os.listdir(dir_name):
        with open(dir_name + "/" + filename, "r") as f:
            count_a += len(f.readlines()) - 1

    count_b = 0
    for filename in os.listdir("datalake"):
        with open("datalake" + "/" + filename, "r") as f:
            count_b += len(f.readlines()) - 1

    print("a : {}, b : {}".format(count_a, count_b))
