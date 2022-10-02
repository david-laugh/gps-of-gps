import os


"""
총 데이터 수 확인하기.
"""
def execute():
    # raw : 원시 데이터
    # gps of gps의 원시 데이터 경로
    dir_name = "./datalake/raw"

    count = 0
    for filename in os.listdir(dir_name):
        print(filename)
        with open(dir_name + "/" + filename, "r") as f:
            """
            첫 헤더라인 수 제거.
            """
            count += len(f.readlines()) - 1

    print("데이터 수 : {}".format(count))
    # 377,347,200


if __name__ == "__main__":
    execute()
