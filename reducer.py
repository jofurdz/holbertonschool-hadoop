#!/uar/bin/python3
""" gives the top ten salaries sorted by totalyearlycompensation"""
import sys


data = []
min_idx = lambda data : (min(data), data.index(min(data)))

for x, line in enumerate(sys.stdin):
    row = line.strip().replace("\t", ",").split(",")
    row[-2], row[-1] = row[-1], row[-2]

    try:
        salary = row[-2] = float(row[-2])
        if len(data) < 10:
            data.append(row)
            continue

        m, i = min_idx(list(zip(*data))[-2])
        if salary > m:
            data[i] = row
    except Exception:
        continue

data = sorted(data, key=lambda x: -x[-2])

print("id\tSalary\tcompany")

for d in data:
    print("{}\t{}\t{}".format(*d))
