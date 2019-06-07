from __future__ import print_function
import sys
import os

max2j2b = str(sys.argv[1])

dirs = [d for d in os.listdir(".") if "nbinscan".format(max2j2b) in d]

pairs = []

for d in dirs:
    if not os.path.exists("{}/tW/Fits/tW.txt".format(d)):
        continue
    with open("{}/tW/Fits/tW.txt".format(d)) as f:
        for line in f:
            if "SigXsecOverSM" in line:
                pairs.append((float(line.strip().split()[2]), d))
                break

for p in reversed(sorted(pairs, key=lambda tup: tup[0])):
    print(p)
