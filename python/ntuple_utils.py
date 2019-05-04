import os
import re

def files_from_dir(ntdir, regstr):
    retest = re.compile(regstr)
    flist = os.listdir(ntdir)
    files = set()
    for f in flist:
        if retest.match(f):
            files.add(f[:-5].replace("_nominal.bdt_response", ""))
    return ",".join(files)
