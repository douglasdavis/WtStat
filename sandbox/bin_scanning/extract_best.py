from __future__ import print_function
import os

dirs = [d for d in os.listdir(".") if "vary2j2b" in d]
for d in dirs:
    with open("{}/tW/Fits/tW.txt".format(d)) as f:
        for line in f:
            if 'SigXsecOverSM' in line:
                print(line.strip(), d)
