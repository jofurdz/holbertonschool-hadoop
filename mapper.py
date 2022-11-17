#!/usr/bin/python3
"""module prints the id, the company
   and the total yearly compensation items"""
import sys


for x, line in enumerate(sys.stdin):
    data = line.replace("\n", "").split(",")

    if x == 0:
        id = data.index("id")
        company = data.index("company")
        tyc = data.index("totalyearlycompensation")

    print("{}\t{},{}".format(data[id], data[company], data[tyc]))
