import csv
import numpy as np
import datetime
from commit_func import make_time_git_commit


def get_commit_pattern(file_name):
    with open(file_name, "r") as f:
        reader = csv.reader(f)
        commit_pattern = list(reader)
    commit_pattern = np.array(commit_pattern)
    return commit_pattern.T


def change_file(file_name):
    with open(file_name, "a") as f:
        f.write("a")


def main():
    pattern_file = "pattern.csv"
    commit_pattern = get_commit_pattern(pattern_file)

    # 描画するパターンの中で最も日にちが早い箇所の基準点を設定
    START_YEAR  = 2020
    START_MONTH = 1
    START_DAY   = 12

    d = datetime.date(START_YEAR, START_MONTH, START_DAY)
    for b in commit_pattern.reshape(-1):
        if b == "1":
            change_file("commit_file")
            make_time_git_commit(d)
        d += datetime.timedelta(days=1)


if __name__ == "__main__":
    main()
